<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kevinnadar22/mdisky">
    <img src="https://play-lh.googleusercontent.com/7ByFpdTmtc3JCmTUCUKQTmQChqbvlk79JSnyt27ORfTKK-51m_kyFs3B6YE7xRzLM2k=rw" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Mdisky</h3>

  <p align="center">
   An Unofficial Python version of Mdisk API wrapper
    <br />
    ·
    <a href="https://www.telegram.dog/ask_admin001">Report Bug</a>
  </p>
</div>


---

# Mdisky
An Unofficial Python version of Mdisk API wrapper. Used to convert and rename Mdisk Files.

## Installation

Install mdisky with pip

```bash
pip install mdisky
```
    
To Upgrade

```bash
pip install --upgrade mdisky
```
    
    
## Usage

```python
from mdisky import Mdisk
import asyncio

async def main():
    mdisk = Mdisk('us5CqX8oandALtQ86FLq')
    link = await mdisk.convert('https://mdisk.me/convertor/16x9/H331KO')
    print(link)

asyncio.run(main())
```

```python
Output: https://mdisk.me/convertor/16x9/gvh9fI
```
---
## See the [documentation](https://github.com/kevinnadar22/mdisky) for more information about the Mdisk API wrapper.