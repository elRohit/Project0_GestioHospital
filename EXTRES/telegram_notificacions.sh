#!/bin/bash

# Configura las variables de entorno
TOKEN="tu_token_de_telegram"
CHAT_ID="tu_chat_id"

# Función para enviar un mensaje a través del bot de Telegram
function enviar_mensaje() {
    mensaje="$1"
    curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
        -d chat_id="$CHAT_ID" \
        -d text="$mensaje" \
        -d parse_mode="HTML"
}

# Función para notificar al médico sobre la visita del paciente
function notificar_medico() {
    paciente="$1"
    medico="$2"
    fecha="$3"
    hora="$4"
    mensaje="¡Hola $medico! Tienes una visita médica programada:\n\nPaciente: $paciente\nFecha: $fecha\nHora: $hora"
    enviar_mensaje "$mensaje"
}

# Ejemplo de uso: enviar una notificación de prueba
notificar_medico "Juan Pérez" "Dr. García" "2022-10-01" "10:00 AM"

# Aquí puedes agregar más funciones y lógica para administrar tu programa del hospital
