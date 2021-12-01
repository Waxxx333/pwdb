[![GitHub version](https://img.shields.io/badge/Version-0.2-pink.svg)](https://github.com/waxxx333/pwdb)
[![Python Version](https://img.shields.io/badge/Python-3.9-purple.svg)](https://shields.io/) 
[![Self](https://img.shields.io/badge/WaXxX333-PWDB-orange.svg)](https://shields.io)
[![LIB](https://img.shields.io/badge/Python-PyCrypto-turquoise)](https://shields.io)
[![lib](https://img.shields.io/badge/Python-Tabulate-magenta)](https://github.com/waxxx333)
<h1 align="center">PWDB | Password Database</h1>
<p align="center">
  <img src="https://imgur.com/aMxmxFR.png">
</p>
<p align="center">
  <img src="https://imgur.com/ffwAXr3.png">
</p>

<!--<p align="center">A password database written in Python 3. This script creates 4 files containing encrypted passwords, account names, usernames, and notes on the accounts. The script is featured with tab completion. It uses the `pycrypto` library as well as `tabulate`</p>-->
### A password database written in Python 3. This script creates 4 files containing encrypted passwords, account names, usernames, and notes on the accounts. It uses the ***`pycrypto`*** library as well as ***`tabulate`***. It uses the ***`tabulate`*** library to make the output a little nicer and ***`pycrypto`*** to encrypt and decrypt entries. 
<hr>

# Features:
* ***Self-destruction***: **Deletes all files after 5 wrong password attempts**
* ***Tab Completion:*** **Press the tab button while at input prompts for tab/auto completion**
* ***Tables***: **Prints your account's info in table format**
<hr>

<p align="center">
  <img src="https://imgur.com/Hpi4Wjm.png">
</p>

<p align="center">
  <img src="https://imgur.com/n0RIbpc.png">
</p>

<p align="center">
  <img src="https://imgur.com/kaO1qjd.png">
</p>

<p align="center">
  <img src="https://imgur.com/1iN8WyI.png">
</p>
<hr>

### Example of data output
```fix
╒═══════════╤═════════════════════╤════════════════╤════════════════════════════════╕
│ Account   │ Username            │ Password       │ Notes                          │
╞═══════════╪═════════════════════╪════════════════╪════════════════════════════════╡
│ github    │ waxxx333@github.com │ MyRealPassword │ Demo screenshot for the README │
╘═══════════╧═════════════════════╧════════════════╧════════════════════════════════╛
```
<hr>

## Not currently working with Windows
<hr>

## Required Python Libraries
* **tabulate**
* **pycrypto**
<hr>

#
<hr> 

> Todos

- [ ] Create `setup.py`
- [ ] Make compatible with Windows
  - [x] Convert to Py3 from Py2
