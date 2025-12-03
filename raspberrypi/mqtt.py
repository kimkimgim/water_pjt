import paho.mqtt.publish as publish

def send_message(message, topic="water", host="52.78.138.103"):
    publish.single(topic, message, hostname=host)
    print(f"[MQTT] Sent: {message}")
