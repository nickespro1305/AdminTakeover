import json
import subprocess

def execute_curl_from_json(file_path):
    """
    Lee URLs de un archivo JSON y ejecuta `curl` para cada una de ellas.
    
    Args:
        file_path (str): Ruta al archivo JSON que contiene las URLs.
        
    Returns:
        list: Resultados de las ejecuciones de `curl` (stdout o errores).
    """
    try:
        # Cargar el archivo JSON
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Validar que es una lista de URLs
        if not isinstance(data, list):
            raise ValueError("El archivo JSON debe contener una lista de URLs.")

        results = []
        for url in data:
            if isinstance(url, str):  # Validar que sea una cadena
                try:
                    print(f"Ejecutando curl para: {url}")
                    # Ejecutar curl
                    result = subprocess.run(
                        ["curl", url],
                        text=True,
                        capture_output=True,
                        check=True
                    )
                    results.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    print(f"Error ejecutando curl para {url}: {e}")
                    results.append(str(e))
            else:
                print(f"Entrada no válida (no es una cadena): {url}")
                results.append(None)

        return results

    except Exception as e:
        print(f"Error al procesar el archivo JSON: {e}")
        return None

def update():
    # Ejemplo de uso
    file_path = "parent-keys.json"
    resultados = execute_curl_from_json(file_path)

    # Imprimir los resultados
    if resultados:
        for idx, res in enumerate(resultados, start=1):
            print(f"Resultado {idx}:\n{res}")
    return


