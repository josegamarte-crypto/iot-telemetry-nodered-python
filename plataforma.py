"""Módulo para publicar métricas de sistema vía MQTT."""

import json
import time
import paho.mqtt.client as mqtt
import psutil

# Configuración del Broker MQTT
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC_METRICAS = "portafolio/iot/metricas"

# Inicialización del Cliente MQTT (compatibilidad con Paho-MQTT v2)
client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="Python_IoT_Publisher"
)


def conectar():
    """Establece la conexión con el broker MQTT."""
    try:
        client.connect(BROKER, PORT, 60)
        print(f"Conectado exitosamente al broker MQTT: {BROKER}")
    except (ConnectionError, OSError) as e:
        print(f"Error al conectar con el broker MQTT: {e}")


# Conectar al broker
conectar()

print("Enviando telemetría... Presiona Ctrl+C para detener.")

try:
    while True:
        # Muestra de métricas del sistema
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        # Paquete de datos en formato JSON
        payload = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "cpu": cpu_usage,
            "ram": ram_usage,
            "estado": "NORMAL" if cpu_usage < 85 else "ALERTA"
        }

        # Publicación en el tópico MQTT
        client.publish(TOPIC_METRICAS, json.dumps(payload))
        print(f"Publicado en {TOPIC_METRICAS}: {payload}")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nPublicación detenida por el usuario.")
    client.disconnect()
