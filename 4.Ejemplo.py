from netmiko import ConnectHandler

def respaldo_configuracion(hostname, username, password):
    try:
        # Definir los parámetros de conexión
        dispositivo = {
            'device_type': 'cisco_ios',  # Cambia esto según el tipo de dispositivo
            'host': hostname,
            'username': username,
            'password': password,
        }

        # Conectar al dispositivo
        conexion = ConnectHandler(**dispositivo)

        # Obtener la configuración del dispositivo
        configuracion = conexion.send_command('show running-config')

        # Guardar la configuración en un archivo
        nombre_archivo = f'{hostname}_configuracion.txt'
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(configuracion)

        print(f"La configuración de {hostname} ha sido respaldada en {nombre_archivo}")

    except Exception as e:
        print(f"Error al respaldar la configuración de {hostname}: {str(e)}")

    finally:
        # Cerrar la conexión
        conexion.disconnect()

# Configuración del dispositivo de red
hostname = '192.168.18.68'  # Cambia esto por la dirección IP o el nombre de dominio de tu dispositivo
username = 'REYNA 2.4G'
password = 'Uch4s4r4'

# Llamar a la función para respaldar la configuración del dispositivo
respaldo_configuracion(hostname, username, password)
