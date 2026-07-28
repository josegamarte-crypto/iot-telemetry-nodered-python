# iot-telemetry-nodered-python
Sistema de monitoreo de telemetría en tiempo real (CPU y RAM) usando Python, MQTT y Node-RED Dashboard 2.0.
# 📡 Real-Time IoT Telemetry System (Python + MQTT + Node-RED)

Este proyecto implementa un sistema distribuido de monitoreo e instrumentación en tiempo real para métricas de rendimiento de hardware (CPU y RAM). Captura datos mediante un script en Python, los transmite mediante un broker MQTT público y los procesa y visualiza dinámicamente en una interfaz HMI/Dashboard desarrollada en Node-RED.

---

## 🛠️ Arquitectura del Sistema

El flujo de información sigue una arquitectura **Publicador / Broker / Suscriptor**:

1. **Productor (Capa de Captura):** Script en Python (`telemetry_publisher.py`) que utiliza la librería `psutil` para leer los recursos del sistema, empaquetando la lectura en un formato JSON (`{"cpu": float, "ram": float}`) y publicándola cada segundo.
2. **Broker (Capa de Transporte):** Servidor Mosquitto público (`test.mosquitto.org:1883`) encargándose de la mensajería asíncrona bajo el tópico `portafolio/iot/metricas`.
3. **Consumidor / HMI (Capa de Visualización):** Servidor Node-RED integrado con **Dashboard 2.0**, el cual procesa los datos mediante nodos de cambio (*change nodes*) e indicadores analógicos (*Gauges*).

---

## 🚀 Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Librerías Python:** `paho-mqtt`, `psutil`, `json`, `time`
* **Orquestación y Dashboard:** Node-RED v3.x+ / `@flowfuse/node-red-dashboard`
* **Protocolo:** MQTT V3.1.1 (Puerto 1883 TCP)

---

## 📦 Estructura del Repositorio

```text
├── telemetry_publisher.py   # Script de Python para captura y envío MQTT
├── flows.json               # Flujo exportado de Node-RED
└── README.md                # Documentación del proyecto
