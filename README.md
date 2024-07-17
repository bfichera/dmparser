# Description

Simple way to load data and metadata from dm3 or dm4 files. Direct copy of `ncempy.io`.

# Installation
`pip install git+ssh://git@github.com/bfichera/dmparser.git`

# Dependencies
- `numpy`

# Usage

```
from pathlib import Path

from dmparser import parse

path = Path('/Users/bfichera/mnt/Lorentz/CD/TEM_Data/ALTEM/2024/2024_05_31_FGT512/bef_heat/001_FGT512_20240529_tx0.3_Ty0.9_SA1_CL94cm_SADP_RT.dm4')

reader = parse(path)
```
