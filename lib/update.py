import json
import subprocess
import tempfile
from lib.interactiveFuncs import *
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.console import Console

def update():
    console = Console()
    
    # Variables para almacenar los valores
    filenames = []  # Lista para almacenar los filenames
    urls = []  # Lista para almacenar las urls

    try:
        # Leer el archivo JSON
        file_path = "keys/parent-keys.json"  # Cambia esto si la ruta es diferente
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Validar que el contenido sea una lista
        if not isinstance(data, list):
            raise ValueError("El archivo JSON no contiene una lista válida.")
        
        # Extraer los valores de 'filename' y 'url' y almacenarlos en las variables
        for item in data:
            if isinstance(item, dict) and 'filename' in item and 'url' in item:
                filenames.append(item['filename'])
                urls.append(item['url'])
            else:
                console.print(f"[red]Error: El objeto {item} no contiene 'filename' o 'url'[/red]")

        # Ahora las variables 'filenames' y 'urls' contienen los valores extraídos
        console.print(f"[green]Filnames: {filenames}[/green]")
        console.print(f"[green]URLs: {urls}[/green]")

    except Exception as e:
        console.print(f"[red]Error al leer el archivo JSON: {e}[/red]")



    # Crear un archivo temporal para almacenar el JSON
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file1, \
         tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file2, \
        tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file3:
        temp_file_path1 = temp_file1.name
        temp_file_path2 = temp_file2.name
        temp_file_path3 = temp_file3.name
        
    with Progress(
        TextColumn("[bold blue]{task.description}", justify="right"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.1f}%",
        TimeRemainingColumn(),
    ) as progress:
        # Descargar el primer archivo
            task_id_1 = progress.add_task("Downloading main Keyring", total=100)
            try:
                process1 = subprocess.Popen(
                    f"curl -s -k {urls[0]} -o {temp_file_path1}",
                    shell=True
                )
                while process1.poll() is None:
                    progress.update(task_id_1, advance=5)
                    progress.refresh()
                progress.update(task_id_1, completed=100)
            except Exception as e:
                console.log(f"[red]Error downloading Keyring 1: {e}")
                return

            # Descargar el segundo archivo
            task_id_2 = progress.add_task("Downloading plugins keyring", total=100)
            try:
                process2 = subprocess.Popen(
                    f"curl -s -k {urls[1]} -o {temp_file_path2}",
                    shell=True
                )
                while process2.poll() is None:
                    progress.update(task_id_2, advance=5)
                    progress.refresh()
                progress.update(task_id_2, completed=100)
            except Exception as e:
                console.log(f"[red]Error downloading Keyring 2: {e}")
                return
            
            # descargando el tercer archivo
            task_id_3 = progress.add_task("Downloading plugins keyring", total=100)
            try:
                process3 = subprocess.Popen(
                    f"curl -s -k {urls[2]} -o {temp_file_path3}",
                    shell=True
                )
                while process3.poll() is None:
                    progress.update(task_id_3, advance=5)
                    progress.refresh()
                progress.update(task_id_3, completed=100)
            except Exception as e:
                console.log(f"[red]Error downloading Keyring 3: {e}")
                return
        
    # Leer el JSON descargado
    try:
        with open(temp_file_path1, "r") as file1, open(temp_file_path2, "r") as file2, open(temp_file_path3, "r") as file3:
            data1 = json.load(file1)
            data2 = json.load(file2)
            data3 = json.load(file3)

        # Imprimir los JSON en color
        console.print("")
        console.print("[blue]Keyring 1")
        console.print("")
        console.print_json(json.dumps(data1, indent=2))
        console.print("")
        console.print("[blue]Keyring 2")
        console.print("")
        console.print_json(json.dumps(data2, indent=2))
        console.print("")
        console.print("[blue]Keyring 3")
        console.print("")
        console.print_json(json.dumps(data3, indent=2))

        # Pedir una ultima confirmacion
        confirmation1 = confirmation("[blue]Update Keys?[/blue] [green]Y[/green]/[red]n[/red]", "[purple]$", 1)
        if confirmation1 == "Y":
            # Descargar los archivos actualizados a las rutas finales
            final_path1 = "/keys/main.json"
            final_path2 = "/keys/exploits.json"
            final_path3 = "/keys/plugins.json"

            with Progress(
                TextColumn("[bold blue]{task.description}", justify="right"),
                BarColumn(),
                "[progress.percentage]{task.percentage:>3.1f}%",
                TimeRemainingColumn(),
            ) as progress:
                # Descargar el primer archivo actualizado
                task_id_1 = progress.add_task("Updating Main Keyring", total=100)
                try:
                    process1 = subprocess.Popen(
                        f"curl -s -k {urls[0]} -o {final_path1}",
                        shell=True
                    )
                    while process1.poll() is None:
                        progress.update(task_id_1, advance=5)
                        progress.refresh()
                    progress.update(task_id_1, completed=100)
                except Exception as e:
                    console.log(f"[red]Error updating Keyring 1: {e}")

                # Descargar el segundo archivo actualizado
                task_id_2 = progress.add_task("Updating Plugins Keyring", total=100)
                try:
                    process2 = subprocess.Popen(
                        f"curl -s -k {urls[1]} -o {final_path2}",
                        shell=True
                    )
                    while process2.poll() is None:
                        progress.update(task_id_2, advance=5)
                        progress.refresh()
                    progress.update(task_id_2, completed=100)
                except Exception as e:
                    console.log(f"[red]Error updating Keyring 2: {e}")

                # Descargar el tercer archivo actualizado
                task_id_3 = progress.add_task("Updating Plugins Keyring", total=100)
                try:
                    process2 = subprocess.Popen(
                        f"curl -s -k {urls[2]} -o {final_path3}",
                        shell=True
                    )
                    while process3.poll() is None:
                        progress.update(task_id_3, advance=5)
                        progress.refresh()
                    progress.update(task_id_3, completed=100)
                except Exception as e:
                    console.log(f"[red]Error updating Keyring 3: {e}")

        else:
            print("[yellow]Operation canceled.")

    except Exception as e:
        console.log(f"[red]Error reading JSON files: {e}")

    return