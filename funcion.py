# Importar Librerias
import RPi.GPIO as GPIO
import time


def run():
	GPIO.setmode(GPIO.BOARD)

    # Configurar el pin GPIO como una salida para el LED
	GPIO.setup(37, GPIO.OUT)

    # Configurar el pin GPIO como una entrada para el pulsador
	GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Encender el LED al inicio del programa
	GPIO.output(37, GPIO.HIGH)
    # Esperar a que el pulsador sea presionado
	while True:
        # Cambiar el estado del LED APAGADO/PRENDIDO
		if GPIO.input(38) == GPIO.HIGH:
			GPIO.output(37, GPIO.LOW)
			print('apagado')
		else:
			GPIO.output(37, GPIO.HIGH)
			print('encendido')

    # Limpiar los pines GPIO
	GPIO.cleanup()
