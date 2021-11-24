import json
import logging
from uncertainties import ufloat

from yadg.parsers.basiccsv import process_row
import yadg.dgutils

version = "1.0.dev1"


def process(
    fn: str,
    encoding: str = "utf-8",
    timezone: str = "localtime",
    convert: dict = None,
    calfile: str = None,
) -> tuple[list, dict, dict]:
    """
    Legacy MCPT measurement log parser.

    This parser is included to maintain parity with older schemas and datagrams. For
    new applications, please use the base `basiccsv` parser.

    """
    logging.warning("meascsv: This parser is deprecated. Please switch to 'basiccsv'.")

    if calfile is not None:
        with open(calfile, "r") as infile:
            calib = json.load(infile)
    else:
        calib = {}
    if convert is not None:
        calib.update(convert)

    metadata = {}

    with open(fn, "r", encoding=encoding) as infile:
        lines = [i.strip() for i in infile.readlines()]

    headers = [i.strip() for i in lines.pop(0).split(";")]
    _units = [i.strip() for i in lines.pop(0).split(";")]
    units = {}
    for h in headers:
        units[h] = _units.pop(0)

    datecolumns, datefunc = yadg.dgutils.infer_timestamp_from(
        spec={"timestamp": {"index": 0, "format": "%Y-%m-%d-%H-%M-%S"}},
        timezone=timezone,
    )
    timesteps = []
    for line in lines:
        ts = process_row(
            headers, line.split(";"), units, datefunc, datecolumns, calib=calib
        )
        ts["fn"] = str(fn)

        if "derived" in ts:
            xin = {}
            total = ufloat(0, 0)
            for mfc in ts["derived"].keys():
                if mfc.startswith("flow") or mfc.startswith("T"):
                    continue
                xin[mfc] = ufloat(ts["derived"][mfc]["n"], ts["derived"][mfc]["s"])
                total += xin[mfc]
            if xin != {}:
                ts["derived"]["xin"] = {}
                for species in xin:
                    x = xin[species] / total
                    ts["derived"]["xin"][species] = {"n": x.n, "s": x.s, "u": "-"}
        timesteps.append(ts)
    return timesteps, None, None