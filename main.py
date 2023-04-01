import argparse
from paho.mqtt.client import Client

# define an argument options
option_help = '''Options to request to MQTT:
  [1] - Turn ON/OFF the TV
  [2] - Volume UP
  [3] - Volume DOWN
  [4] - Mute
  [5] - Switch to HDMI 1
  [6] - Switch to HDMI 2
  [7] - Switch to HDMI 3
  [8] - Switch to HDMI 4
'''
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-n', '--TvNumber', help="input to choose the number of TV", required=True)
parser.add_argument('-op', '--options', help=option_help, required=True)
args = parser.parse_args()

# MQTT
mqtt_host = "broker.emqx.io"


def execute_command():
    tv_number = args.TvNumber
    option = args.options
    if option == '1':
        mqttc.publish("tv/{}".format(tv_number if tv_number != "ALL" else "ALL"), "toggle")
    elif option == '2':
        mqttc.publish("tv/{}".format(tv_number if tv_number != "ALL" else "ALL"), "vol_up")
    elif option == '3':
        mqttc.publish("tv/{}".format(tv_number if tv_number != "ALL" else "ALL"), "vol_down")
    elif option == '4':
        mqttc.publish("tv/{}".format(tv_number if tv_number != "ALL" else "ALL"), "mute")
    elif option == '5':
        mqttc.publish("tv/{}".format(tv_number if tv_number != "ALL" else "ALL"), "hdmi1")
    elif option == '6':
        mqttc.publish("tv/{}".format(tv_number if tv_number != "ALL" else "ALL"), "hdmi2")
    elif option == '7':
        mqttc.publish("tv/{}".format(tv_number if tv_number != "ALL" else "ALL"), "hdmi3")
    elif option == '8':
        mqttc.publish("tv/{}".format(tv_number if tv_number != "ALL" else "ALL"), "av")


if __name__ == '__main__':
    mqttc = Client()
    mqttc.connect(mqtt_host, 1883, 60)
    execute_command()
