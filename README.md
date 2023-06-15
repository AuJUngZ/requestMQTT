# requestMQTT

This is a simple example of how to use the MQTT protocol to send to a server. This will use with other devices such as
Stream Deck.
To allow the Stream Deck to send commands to the server, you will need to install the MQTT plugin.

## Installation

- Install python3 in your system
- Install the paho-mqtt library

## Usage

- set Stream Deck button to run the script by passing the arguments following the example below:
  - ``` main.py -n [number of TV] -op [options] ```
- if you not sure about the options, you can run the script with the argument ```-h``` to see the help. example:
  ``` main.py -h```

## To use without terminal

- Use pythonw instead of python :
    - ```pythonw main.py -n [number of TV] -op [options]```

## Arguments

| Option     | Description               |
|------------|---------------------------|
| -n         | Number of TV    [REQUIRE] |
| -op        | Options         [REQUIRE] |
| -h, --help | Help                      |


