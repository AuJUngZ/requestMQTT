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
mqtt_host = "<broker-mqtt>"


prefix_topic = "TLIC/MeetingLauncher/activeroom1/tv{}"


def execute_command():
    tv_number = args.TvNumber
    option = args.options
    if option == '1':
        mqttc.publish(prefix_topic.format(tv_number if tv_number != "all" else "all"), "toggle")
    elif option == '2':
        mqttc.publish(prefix_topic.format(tv_number if tv_number != "all" else "all"), "vol_up")
    elif option == '3':
        mqttc.publish(prefix_topic.format(tv_number if tv_number != "all" else "all"), "vol_down")
    elif option == '4':
        mqttc.publish(prefix_topic.format(tv_number if tv_number != "all" else "all"), "mute")
    elif option == '5':
        mqttc.publish(prefix_topic.format(tv_number if tv_number != "all" else "all"), "hdmi1")
    elif option == '6':
        mqttc.publish(prefix_topic.format(tv_number if tv_number != "all" else "all"), "hdmi2")
    elif option == '7':
        mqttc.publish(prefix_topic.format(tv_number if tv_number != "all" else "all"), "hdmi3")
    elif option == '8':
        mqttc.publish(prefix_topic.format(tv_number if tv_number != "all" else "all"), "av")


if __name__ == '__main__':
    mqttc = Client()
    # set username and password
    mqttc.username_pw_set("<username>", "<password>")
    mqttc.connect(mqtt_host, 1883, 60)
    execute_command()
