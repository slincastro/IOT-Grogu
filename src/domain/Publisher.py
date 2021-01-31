from umqtt.simple import MQTTClient
from domain.Servo import Servo
import time


def write_log(message):
    f = open("log.txt", "a")
    f.write(message + " \n")
    f.close()

class Publisher:
    def __init__(self, configuration, rgb_led, wifi_connection):
        self.configuration = configuration

        write_log("clinetID : " + self.configuration.mqtt.client_id +
                       " server :" + self.configuration.mqtt.mqtt_server + "\n")
        write_log("topic : " + self.configuration.mqtt.topic_pub + "\n")
        self.wifi_connection = wifi_connection
        self.rgb_led = rgb_led
        self.servo = Servo(14)
        self.pulse = 40

    def connect(self):
        pass

    def sub_cb(self, topic, msg):
        message = str(msg)
        self.rgb_led.blink(self.rgb_led.green_led)
        write_log("receiving message =>" + message)
        write_log("Topic =>" + message)

    def publish(self):
        write_log("start connection to server")
        client = MQTTClient(self.configuration.mqtt.client_id, self.configuration.mqtt.mqtt_server)

        client.set_callback(self.sub_cb)

        retry = 0
        write_log("wifi status :" + str(self.wifi_connection.isconnected()))
        write_log("wifi config :" + str(self.wifi_connection.ifconfig()))
        while retry < 20:
            try:
                while not client.connect():
                    time.sleep(4.5)
                    self.rgb_led.blink(self.rgb_led.blue_led)
                    msg = " hi from python :" + str(retry)
                    write_log("connecting to server ....")
                    client.publish(self.configuration.mqtt.topic_pub, msg)

            except Exception as e:
                write_log("Can't connect to mqtt..... try:" + str(retry + 1))
                write_log(str(e))
                self.rgb_led.blink(self.rgb_led.red_led)
            finally:
                write_log("finish connection proccess ....")
                retry += 1
                pass
            time.sleep(5)

