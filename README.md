[![DOI](https://joss.theoj.org/papers/10.21105/joss.04166/status.svg)](https://doi.org/10.21105/joss.04166)
[![Documentation](https://badgen.net/badge/docs/dgbowl.github.io/grey?icon=firefox)](https://dgbowl.github.io/yadg)
[![PyPi version](https://badgen.net/pypi/v/yadg/?icon=pypi)](https://pypi.org/project/yadg)
[![Github link](https://badgen.net/github/tag/dgbowl/yadg/?icon=github)](https://github.com/dgbowl/yadg/)
[![Github status](https://badgen.net/github/checks/dgbowl/yadg/?icon=github)](https://github.com/dgbowl/yadg/actions/workflows/push-master.yml)


# ![yet another datagram](./docs/source/images/yadg_banner.png)

Set of tools to process raw instrument data according to a *dataschema* into a standardised form called *datagram*, annotated with metadata, provenance information, timestamps, units, and uncertainties. Developed by the [Materials for Energy Conversion](https://www.empa.ch/web/s501) lab at Empa (Dübendorf, CH) and by the [Centre for Advanced Ceramic Materials](https://www.tu.berlin/ceramics) at Technische Universität Berlin (Berlin, DE).

![schema to datagram with yadg](./docs/source/images/schema_yadg_datagram.png)

### Capabilities:
- Parsing **tabulated data** using CSV parsing functionality, including Bronkhorst and DryCal output formats. 
- Parsing **chromatography data** from gas and liquid chromatography, including several Agilent, Masshunter, and Fusion formats.
- Parsing **reflection coefficient** traces from network analysers. 
- Parsing **potentiostat files** for electrochemistry applications. Supports BioLogic file formats.

### Features:
- timezone-aware timestamping using Unix timestamps
- automatic uncertainty determination using data contained in the raw files, instrument specification, or last significant digit
- uncertainty propagation to derived quantities
- tagging of data with units
- extensive *dataschema* and *datagram* validation using provided specifications
- mandatory metadata (such as provenance) is enforced

The full list of capabilities and features is listed in the [project documentation](http://dgbowl.github.io/yadg).

### Installation:
The released versions of `yadg` are available on the Python Package Index (PyPI) under [yadg](https://pypi.org/project/yadg). Those can be installed using:

```bash
    pip install yadg
```

If you wish to install the current development version as an editable installation, check out the `master` branch using git, and install `yadg` as an editable package using pip:

```bash
   git clone git@github.com:dgbowl/yadg.git
   cd yadg
   pip install -e .
```

Additional targets `yadg[testing]` and `yadg[docs]` are available and can be specified in the above commands, if testing and/or documentation capabilities are required.

### Contributors:
- [Peter Kraus](http://github.com/PeterKraus)
- [Nicolas Vetsch](http://github.com/vetschn)

### Acknowledgements

This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 957189. The project is part of BATTERY 2030+, the large-scale European research initiative for inventing the sustainable batteries of the future.
