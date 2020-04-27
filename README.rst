####################################################################################################
Next Bus Arrival Time Python API Wrapper for Citybus Limited and New World First Bus Service Limited
####################################################################################################

Info
====

This is a simple python API wrapper for the Next Bus arrival time API in Hong Kong by Citybus Limited and New World First Bus Services Limited

Api Specs: https://www.nwstbus.com.hk/datagovhk/bus_eta_api_specifications.pdf

Installation
============

This is just a py file as of now, so you can simply copy the nextBusApi.py file to your project and install the 'requests' module.

Alternatively you can clone this project and use [poetry](https://python-poetry.org) to install deps.

1. clone the project
2. poetry shell
3. poetry install

Running
=======

Look at the example.py file for usage example. You can simply run ```python example.py```

FAQ: 
====

1) Could not install packages due to an EnvironmentError: Could not find a suitable TLS CA certificate bundle:

Please find the path of you certificate file by using the code below 
```
import certifi 
print(certifi.where())
```
finally export this path

```export REQUESTS_CA_BUNDLE='path'```

