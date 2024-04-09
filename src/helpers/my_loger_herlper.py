import logging
import os

# Obtén la ruta absoluta al directorio actual desde donde se ejecuta el script
ruta_directorio_actual = os.path.abspath(os.getcwd())

# Define la ruta relativa a la carpeta "logs" en el directorio actual
ruta_carpeta_logs = os.path.join(ruta_directorio_actual, 'logs')

# Asegúrate de que la carpeta "logs" exista; si no, créala
if not os.path.exists(ruta_carpeta_logs):
    os.makedirs(ruta_carpeta_logs)

# Configura el sistema de registros para guardar en la carpeta "logs"
archivo_log = os.path.join(ruta_carpeta_logs, 'log_file.log')
logging.basicConfig(filename=archivo_log, filemode='a', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ConsoleColors:
    RESET = "\033[0m"
    RED = "\033[91m"  # Red
    ORANGE = "\033[38;5;208m"  # Orange
    BLUE = "\033[94m"  # Blue
    PINK = "\033[95m"  # Magenta
    YELLOW = "\033[93m"  # Yellow
    GREEN = "\033[92m"  # Green
    CYAN = "\033[96m"  # Cyan

class MyLogger:
    @staticmethod
    def red(message):
        colored_message = f"{ConsoleColors.RED}MyLogger:{ConsoleColors.RESET} {message}"
        print(colored_message)
        logging.error(message)

    @staticmethod
    def orange(message):
        colored_message = f"{ConsoleColors.ORANGE}MyLogger:{ConsoleColors.RESET} {message}"
        print(colored_message)
        logging.warning(message)

    @staticmethod
    def blue(message):
        colored_message = f"{ConsoleColors.BLUE}MyLogger:{ConsoleColors.RESET} {message}"
        print(colored_message)
        logging.info(message)
        
    @staticmethod
    def pink(message):
        colored_message = f"{ConsoleColors.PINK}MyLogger:{ConsoleColors.RESET} {message}"
        print(colored_message)
        logging.info(message)
    
    @staticmethod
    def yellow(message):
        colored_message = f"{ConsoleColors.YELLOW}MyLogger:{ConsoleColors.RESET} {message}"
        print(colored_message)
        logging.info(message)

    @staticmethod
    def green(message):
        colored_message = f"{ConsoleColors.GREEN}MyLogger:{ConsoleColors.RESET} {message}"
        print(colored_message)
        logging.info(message)

    @staticmethod
    def cyan(message):
        colored_message = f"{ConsoleColors.CYAN}MyLogger:{ConsoleColors.RESET} {message}"
        print(colored_message)
        logging.info(message)

MyLogger.yellow("MyLogger inicializado correctamente")
