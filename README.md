

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
    ·
    <a href="#usage">Usage</a>
    ·
    <a href="#reference">Reference</a>
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

mdisk = Mdisk('us5CqX8oandALtQ86FLq')

async def main():
    link = await mdisk.convert('https://mdisk.me/convertor/16x9/H331KO')
    print(link)

asyncio.run(main())
```

```python
Output: https://mdisk.me/convertor/16x9/gvh9fI
```


## Features

- Single URL Convert
- Batch Convert from list
- Convert from Text
- Rename Filename

## Contributing

Contributions are always welcome!



## Reference

### Init
```python
from mdisky import Mdisk
import asyncio

mdisk = Mdisk("Your MDisk API Key")

```

### Convert a single URL

```python
convert(link, silently_fail) -> str
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `link` | `string` | **Required**. Others Mdisk Link |
| `silently_fail` | `bool` | Raise an exception or not if error ocuurs |

Example:

```python
async def main():
    link = await mdisk.convert('https://mdisk.me/convertor/16x9/H331KO')
    print(link)

asyncio.run(main())

## Output: https://mdisk.me/convertor/16x9/gvh9fI
```

### Bulk Convert

```python
bulk_convert(urls:list, silently_fail) -> list
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `urls`      | `list` | **Required**. List of URLs to convert |

Example:

```python
async def main():
    links = ['https://mdisk.me/convertor/16x9/zlG3T0', 'https://mdisk.me/convertor/16x9/H331KO']
    link = await mdisk.bulk_convert(links)
    print(link)

asyncio.run(main())

## Output: ['https://mdisk.me/convertor/16x9/RpLLan', 'https://mdisk.me/convertor/16x9/gvh9fI']
```

### Convert from Text

```python
convert_from_text(text:str, silently_fail:bool=True)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text`      | `str` | **Required**. Text containing Mdisk links to convert|

Example:

```python
async def main():
    text = """
Ep 1:-https://mdisk.me/convertor/16x9/H331KO
Ep 2:-https://mdisk.me/convertor/16x9/mRnSFW
"""
    link = await mdisk.convert_from_text(text)
    print(link)

asyncio.run(main())

## Output:
Ep 1:-https://mdisk.me/convertor/16x9/gvh9fI
Ep 2:-https://mdisk.me/convertor/16x9/5JIit7
```

### Get filename

```python
get_filename(link:str)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `link`      | `str` | **Required**. Link to get the filename of|

Example:

```python
async def main():
    link = "https://mdisk.me/convertor/16x9/5JIit7"
    filename = await mdisk.get_filename(link)
    print(filename)

asyncio.run(main())

## Output: Mdisky Demo Link
```


### Change filename

```python
change_filename(link, filename)
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `link`      | `str` | **Required**. Link to Change the filename of|
| `filename`      | `str` | **Required**. New Filename|

Example:

```python
async def main():
    link = "https://mdisk.me/convertor/16x9/5JIit7"
    link = await mdisk.change_filename(link, 'Mdisky Demo Link')
    print(link)

asyncio.run(main())

## Output: Mdisky Demo Link
```

## Support

For support, email jesikamaraj@gmail.com or PM [Dev](https://t.me/ask_admin001)


## Roadmap

- Async API Request for time saving
- Add more integrations

## Disclaimer

[![GNU Affero General Public License v3.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL v3.0.](https://github.com/CrazyBotsz/Adv-Auto-Filter-Bot-V2/blob/main/LICENSE)
Selling The Codes To Other People For Money Is *Strictly Prohibited*.


## Credits
 - [Thanks To Me](https://github.com/Kevinnadar22)