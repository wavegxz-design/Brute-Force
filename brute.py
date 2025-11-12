#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time # ¡Corregido a minúsculas!
import random
import string
import os
import sys
from datetime import datetime

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'

def clear_screen():
    # Usa 'clear' para Linux/macOS y 'cls' para Windows
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .    ·▄▄▄▄        ▄▄▄   ▄▄· ▄▄▄ .
▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·    ██▪ ██ ▪     ▀▄ █·▐█ ▌▪▀▄.▀·
▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄    ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄ ██ ▄▄▐▀▀▪▄
██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌    ██. ██ ▐█▌.▐▌▐█•█▌▐███▌▐█▄▄▌
·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀     ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀·▀▀▀  ▀▀▀ 
{Colors.RESET}
{Colors.GREEN}                    ┌─────────────────────┐
                    │   By: BLACKNIXU    │
                    └─────────────────────┘{Colors.RESET}
{Colors.YELLOW}                       Version: v2.1 (FIXED){Colors.RESET}
"""
    print(banner)

def format_time(seconds):
    if seconds < 60:
        return f"{int(seconds)}s"
    elif seconds < 3600:
        return f"{int(seconds // 60)}m {int(seconds % 60)}s"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours}h {minutes}m {secs}s"

def format_number(num):
    # Formatea un número con punto como separador de miles
    return f"{num:,}".replace(',', '.')

def create_progress_bar(progress, width=40):
    filled = int(width * progress / 100)
    bar = '█' * filled + '░' * (width - filled)
    return f"{Colors.GREEN}[{bar}]{Colors.RESET} {Colors.YELLOW}{progress:.4f}%{Colors.RESET}"

# --- GENERADORES DE CONTRASEÑAS (Sin Cambios) ---
class PasswordGenerators:
    @staticmethod
    def random_basic(length=8):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(random.randint(4, length)))
    
    @staticmethod
    def eset_style():
        length = random.randint(12, 16)
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice("!@#$%^&*"))
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password.extend(random.choice(chars) for _ in range(length - 4))
        random.shuffle(password)
        return ''.join(password)
    
    @staticmethod
    def strong_style():
        length = random.randint(14, 20)
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = []
        for _ in range(length // 4):
            password.append(random.choice(string.ascii_uppercase))
        for _ in range(length // 4):
            password.append(random.choice(string.ascii_lowercase))
        for _ in range(length // 4):
            password.append(random.choice(string.digits))
        remaining = length - len(password)
        password.extend(random.choice(symbols) for _ in range(remaining))
        random.shuffle(password)
        return ''.join(password)
    
    @staticmethod
    def google_style():
        length = random.randint(12, 15)
        chars = string.ascii_letters + string.digits + "!@#$%&*"
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.extend(random.choice(chars) for _ in range(length - 1))
        return ''.join(password)
    
    @staticmethod
    def keepass_style():
        length = random.randint(16, 24)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        return ''.join(random.choice(all_chars) for _ in range(length))
    
    @staticmethod
    def nordpass_style():
        length = random.randint(12, 18)
        password = []
        for i in range(length):
            if i % 3 == 0:
                password.append(random.choice(string.ascii_uppercase))
            elif i % 3 == 1:
                password.append(random.choice(string.digits))
            else:
                password.append(random.choice(string.ascii_lowercase + "!@#$%"))
        return ''.join(password)
    
    @staticmethod
    def avast_style():
        length = random.randint(10, 14)
        segments = []
        for _ in range(3):
            seg = random.choice(string.ascii_uppercase)
            seg += ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
            seg += random.choice(string.digits)
            segments.append(seg)
        password = ''.join(segments)[:length]
        return password + random.choice("!@#$%")
    
    @staticmethod
    def proton_style():
        length = random.randint(16, 20)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice("!@#$%^&*"))
        password.extend(random.choice(all_chars) for _ in range(length - 4))
        random.shuffle(password)
        return ''.join(password)
# --------------------------------------------------

def simulate_attack(platform, username, speed, generator_name, generator_func):
    total_passwords = 1000000000
    attempt_count = 0
    start_time = time.time()
    recent_attempts = []
    success_count = 0
    failed_count = 0
    last_display_time = 0.0
    display_interval = 1.0 / 25 

    
    # Simulación de éxito (solo para la demostración)
    target_configs = {("Instagram", "kim_azg"): ("aoMO45nLpy-Ptwr", 180)}
    target_key = (platform, username.lower())
    target_password = None
    target_time = None
    
    if target_key in target_configs:
        target_password, target_time = target_configs[target_key]
    
    clear_screen()
    print_banner()
    print(f"\n{Colors.YELLOW}[!] Iniciando ataque de fuerza bruta...{Colors.RESET}")
    print(f"{Colors.CYAN}[+] Generador: {Colors.WHITE}{generator_name}{Colors.RESET}")
    time.sleep(1)
    
    try:
        while True:
            
            # --- Lógica del Intento ---
            current_password = generator_func()
            attempt_count += 1
            failed_count += 1
            
            elapsed_time = time.time() - start_time
            attempts_per_sec = attempt_count / elapsed_time if elapsed_time > 0 else 0
            progress = (attempt_count / total_passwords) * 100
            remaining = (total_passwords - attempt_count) / attempts_per_sec if attempts_per_sec > 0 else 0
            
            # Condición de éxito simulado
            if target_password and elapsed_time >= target_time and success_count == 0:
                current_password = target_password
                success_count = 1
                failed_count -= 1
            
            recent_attempts.append(current_password)
            if len(recent_attempts) > 12:
                recent_attempts.pop(0)

            # --- Lógica de Visualización (FIX del Bug) ---
            current_time = time.time()
            if current_time - last_display_time >= display_interval:
                
                print(f"\r{Colors.CLEAR}", end='')
                print_banner()
                
                print(f"\n{Colors.CYAN}┌{'─' * 63}┐{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.BOLD}{Colors.WHITE}  🎯 OBJETIVO{' ' * 51}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}├{'─' * 63}┤{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} Plataforma: {Colors.WHITE}{Colors.BOLD}{platform:<44}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} Usuario:    {Colors.WHITE}{Colors.BOLD}{username:<44}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} Generador:  {Colors.YELLOW}{Colors.BOLD}{generator_name:<44}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}└{'─' * 63}┘{Colors.RESET}\n")
                
                print(f"{Colors.GREEN}┌{'─' * 63}┐{Colors.RESET}")
                print(f"{Colors.GREEN}│{Colors.BOLD}{Colors.WHITE}  📊 ESTADÍSTICAS EN TIEMPO REAL{' ' * 31}{Colors.GREEN}│{Colors.RESET}")
                print(f"{Colors.GREEN}├{'─' * 63}┤{Colors.RESET}")
                print(f"{Colors.GREEN}│{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} Intentos totales:  {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count):>15}{Colors.GREEN}              │{Colors.RESET}")
                print(f"{Colors.GREEN}│{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} Base de datos:     {Colors.WHITE}{Colors.BOLD}{format_number(total_passwords):>15}{Colors.GREEN}              │{Colors.RESET}")
                print(f"{Colors.GREEN}│{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} Velocidad actual:  {Colors.CYAN}{Colors.BOLD}{int(attempts_per_sec):>10} pass/s{Colors.GREEN}              │{Colors.RESET}")
                print(f"{Colors.GREEN}│{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} Tiempo activo:     {Colors.MAGENTA}{Colors.BOLD}{format_time(elapsed_time):>15}{Colors.GREEN}              │{Colors.RESET}")
                print(f"{Colors.GREEN}│{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} Tiempo restante:   {Colors.MAGENTA}{Colors.BOLD}{format_time(remaining):>15}{Colors.GREEN}              │{Colors.RESET}")
                print(f"{Colors.GREEN}│{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} Intentos exitosos: {Colors.GREEN}{Colors.BOLD}{format_number(success_count):>15}{Colors.GREEN}              │{Colors.RESET}")
                print(f"{Colors.GREEN}│{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} Intentos fallidos: {Colors.RED}{Colors.BOLD}{format_number(failed_count):>15}{Colors.GREEN}              │{Colors.RESET}")
                print(f"{Colors.GREEN}└{'─' * 63}┘{Colors.RESET}\n")
                
                print(f"{Colors.BLUE}┌{'─' * 63}┐{Colors.RESET}")
                print(f"{Colors.BLUE}│{Colors.BOLD}{Colors.WHITE}  ⚡ PROGRESO DEL ATAQUE{' ' * 39}{Colors.BLUE}│{Colors.RESET}")
                print(f"{Colors.BLUE}├{'─' * 63}┤{Colors.RESET}")
                print(f"{Colors.BLUE}│{Colors.RESET}  {create_progress_bar(progress, 50):75}  {Colors.BLUE}│{Colors.RESET}")
                print(f"{Colors.BLUE}└{'─' * 63}┘{Colors.RESET}\n")
                
                print(f"{Colors.MAGENTA}┌{'─' * 63}┐{Colors.RESET}")
                print(f"{Colors.MAGENTA}│{Colors.BOLD}{Colors.WHITE}  🔑 PROBANDO CONTRASEÑA{' ' * 39}{Colors.MAGENTA}│{Colors.RESET}")
                print(f"{Colors.MAGENTA}├{'─' * 63}┤{Colors.RESET}")
                print(f"{Colors.MAGENTA}│{Colors.RESET}  {Colors.CYAN}→→→{Colors.RESET}  {Colors.WHITE}{Colors.BOLD}{current_password:<50}{Colors.MAGENTA}    │{Colors.RESET}")
                print(f"{Colors.MAGENTA}└{'─' * 63}┘{Colors.RESET}\n")
                
                print(f"{Colors.YELLOW}┌{'─' * 63}┐{Colors.RESET}")
                print(f"{Colors.YELLOW}│{Colors.BOLD}{Colors.WHITE}  📝 REGISTRO DE INTENTOS{' ' * 38}{Colors.YELLOW}│{Colors.RESET}")
                print(f"{Colors.YELLOW}├{'─' * 10}┬{'─' * 25}┬{'─' * 25}┤{Colors.RESET}")
                print(f"{Colors.YELLOW}│{Colors.RESET} {Colors.BOLD}  #ID    {Colors.YELLOW}│{Colors.RESET} {Colors.BOLD}   CONTRASEÑA{' ' * 13}{Colors.YELLOW}│{Colors.RESET} {Colors.BOLD}   ESTADO{' ' * 16}{Colors.YELLOW}│{Colors.RESET}")
                print(f"{Colors.YELLOW}├{'─' * 10}┼{'─' * 25}┼{'─' * 25}┤{Colors.RESET}")
                
                # Muestra los últimos 10 intentos
                for i, pwd in enumerate(reversed(recent_attempts[-10:]), 1):
                    attempt_id = attempt_count - i + 1
                    status_text = "✓ ACCESO CONCEDIDO" if pwd == target_password and success_count == 1 else "✗ ACCESO DENEGADO"
                    status = f"{Colors.GREEN}{status_text}{Colors.RESET}" if pwd == target_password else f"{Colors.RED}{status_text}{Colors.RESET}"
                    pwd_display = pwd[:24] if len(pwd) <= 24 else pwd[:21] + "..."
                    print(f"{Colors.YELLOW}│{Colors.RESET} {Colors.WHITE}{attempt_id:>8} {Colors.YELLOW}│{Colors.RESET} {Colors.CYAN}{pwd_display:<24}{Colors.YELLOW}│{Colors.RESET} {status:40} {Colors.YELLOW}│{Colors.RESET}")
                
                print(f"{Colors.YELLOW}└{'─' * 10}┴{'─' * 25}┴{'─' * 25}┘{Colors.RESET}\n")
                print(f"{Colors.RED}[{Colors.WHITE}Ctrl+C{Colors.RED}]{Colors.RESET} Detener ataque")

                last_display_time = current_time # Actualiza el tiempo del último redibujo
                
            # --- Lógica de Finalización ---
            if success_count == 1:
                time.sleep(2)
                clear_screen() # Limpia la pantalla final
                print_banner()

                print(f"\n{Colors.GREEN}{'═' * 65}{Colors.RESET}")
                print(f"{Colors.GREEN}{Colors.BOLD}  🎉 ¡CONTRASEÑA ENCONTRADA! 🎉{Colors.RESET}")
                print(f"{Colors.GREEN}{'═' * 65}{Colors.RESET}\n")
                print(f"{Colors.CYAN}[✓] Detalles del acceso exitoso:{Colors.RESET}")
                print(f"    {Colors.GREEN}►{Colors.RESET} Plataforma: {Colors.WHITE}{Colors.BOLD}{platform}{Colors.RESET}")
                print(f"    {Colors.GREEN}►{Colors.RESET} Usuario: {Colors.WHITE}{Colors.BOLD}{username}{Colors.RESET}")
                print(f"    {Colors.GREEN}►{Colors.RESET} Contraseña: {Colors.GREEN}{Colors.BOLD}{target_password}{Colors.RESET}")
                print(f"    {Colors.GREEN}►{Colors.RESET} Generador usado: {Colors.YELLOW}{Colors.BOLD}{generator_name}{Colors.RESET}")
                print(f"    {Colors.GREEN}►{Colors.RESET} Intentos realizados: {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count)}{Colors.RESET}")
                print(f"    {Colors.GREEN}►{Colors.RESET} Tiempo total: {Colors.WHITE}{Colors.BOLD}{format_time(elapsed_time)}{Colors.RESET}")
                print(f"    {Colors.GREEN}►{Colors.RESET} Velocidad promedio: {Colors.WHITE}{Colors.BOLD}{int(attempts_per_sec)} pass/s{Colors.RESET}\n")
                print(f"{Colors.GREEN}{'═' * 65}{Colors.RESET}\n")
                break
            
            # El tiempo de espera es mínimo para no afectar la velocidad REAL de los intentos
            if speed > 100:
                time.sleep(1.0 / speed)
            else:
                # Si la velocidad es baja, esperamos el tiempo completo para simular mejor
                time.sleep(1.0 / speed) 
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}{'═' * 65}{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] Ataque detenido por el usuario{Colors.RESET}")
        print(f"{Colors.RED}{'═' * 65}{Colors.RESET}\n")
        print(f"{Colors.CYAN}[✓] Resumen del ataque:{Colors.RESET}")
        print(f"    {Colors.GREEN}►{Colors.RESET} Intentos realizados: {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count)}{Colors.RESET}")
        print(f"    {Colors.GREEN}►{Colors.RESET} Tiempo total: {Colors.WHITE}{Colors.BOLD}{format_time(elapsed_time)}{Colors.RESET}")
        print(f"    {Colors.GREEN}►{Colors.RESET} Velocidad promedio: {Colors.WHITE}{Colors.BOLD}{int(attempts_per_sec)} pass/s{Colors.RESET}\n")

# Función para manejar el modo AUTO (nuevo)
def run_auto_attack(platform, username, speed):
    all_generators = [
        ('Random Básico', PasswordGenerators.random_basic),
        ('ESET', PasswordGenerators.eset_style),
        ('Strong', PasswordGenerators.strong_style),
        ('Google Password Manager', PasswordGenerators.google_style),
        ('KeePass', PasswordGenerators.keepass_style),
        ('NordPass', PasswordGenerators.nordpass_style),
        ('Avast Passwords', PasswordGenerators.avast_style),
        ('Proton Pass', PasswordGenerators.proton_style),
    ]
    
    for i, (name, func) in enumerate(all_generators, 1):
        clear_screen()
        print_banner()
        print(f"\n{Colors.CYAN}┌{'─' * 63}┐{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.BOLD}{Colors.WHITE}  🤖 MODO AUTO: {i}/{len(all_generators)} Probando con: {name:<30}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}└{'─' * 63}┘{Colors.RESET}")
        time.sleep(2)
        simulate_attack(platform, username, speed, name, func)


def select_generator():
    generators = {
        '1': ('Random Básico', PasswordGenerators.random_basic, Colors.WHITE),
        '2': ('ESET', PasswordGenerators.eset_style, Colors.BLUE),
        '3': ('Strong', PasswordGenerators.strong_style, Colors.RED),
        '4': ('Google Password Manager', PasswordGenerators.google_style, Colors.GREEN),
        '5': ('KeePass', PasswordGenerators.keepass_style, Colors.CYAN),
        '6': ('NordPass', PasswordGenerators.nordpass_style, Colors.MAGENTA),
        '7': ('Avast Passwords', PasswordGenerators.avast_style, Colors.YELLOW),
        '8': ('Proton Pass', PasswordGenerators.proton_style, Colors.GREEN),
        '9': ('AUTO (Todos)', None, Colors.RED), # El generador 'None' indica el modo especial
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}┌{'─' * 63}┐{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.BOLD}{Colors.WHITE}  🔐 SELECCIONA EL GENERADOR DE CONTRASEÑAS{' ' * 19}{Colors.GREEN}│{Colors.RESET}")
    print(f"{Colors.GREEN}└{'─' * 63}┘{Colors.RESET}\n")
    
    for key, (name, _, color) in generators.items():
        icon = "🤖" if key == '9' else "🔑"
        print(f"  {color}[{key}]{Colors.RESET} {icon}  {Colors.BOLD}{name}{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}{'─' * 65}{Colors.RESET}")
    print(f"\n{Colors.DIM}Cada generador simula patrones de contraseñas específicos")
    print(f"AUTO probará con todos los generadores secuencialmente{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}Generador{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice in generators:
        return choice, generators[choice][0], generators[choice][1]
    else:
        print(f"\n{Colors.RED}[!] Opción inválida{Colors.RESET}")
        time.sleep(1)
        return select_generator()

def select_platform():
    platforms = {
        '1': ('Instagram', '📷', Colors.MAGENTA),
        '2': ('Facebook', '👤', Colors.BLUE),
        '3': ('X (Twitter)', '🐦', Colors.CYAN),
        '4': ('Roblox', '🎮', Colors.RED),
        '5': ('Gmail', '📧', Colors.YELLOW),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}┌{'─' * 63}┐{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.BOLD}{Colors.WHITE}  🎯 SELECCIONA LA PLATAFORMA OBJETIVO{' ' * 25}{Colors.GREEN}│{Colors.RESET}")
    print(f"{Colors.GREEN}└{'─' * 63}┘{Colors.RESET}\n")
    
    for key, (name, emoji, color) in platforms.items():
        print(f"  {color}[{key}]{Colors.RESET} {emoji}  {Colors.BOLD}{name}{Colors.RESET}")
    
    print(f"\n  {Colors.RED}[0]{Colors.RESET} 🚪 {Colors.DIM}Salir{Colors.RESET}")
    print(f"\n{Colors.GREEN}{'─' * 65}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}Plataforma{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice == '0':
        print(f"\n{Colors.CYAN}¡Hasta luego!{Colors.RESET}\n")
        sys.exit(0)
    
    if choice in platforms:
        return platforms[choice][0]
    else:
        print(f"\n{Colors.RED}[!] Opción inválida{Colors.RESET}")
        time.sleep(1)
        return select_platform()

def get_username(platform):
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}┌{'─' * 63}┐{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.RESET} {Colors.CYAN}►{Colors.RESET} Plataforma: {Colors.WHITE}{Colors.BOLD}{platform:<45}{Colors.GREEN}│{Colors.RESET}")
    print(f"{Colors.GREEN}└{'─' * 63}┘{Colors.RESET}\n")
    
    label = "Email" if platform == "Gmail" else "Usuario"
    username = input(f"{Colors.YELLOW}┌─[{Colors.WHITE}{label} objetivo{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if not username:
        print(f"\n{Colors.RED}[!] Debes ingresar un {label.lower()}{Colors.RESET}")
        time.sleep(1)
        return get_username(platform)
    
    return username

def select_speed():
    speeds = {
        '1': (10, 'Lenta', Colors.YELLOW),
        '2': (50, 'Media', Colors.BLUE),
        '3': (100, 'Rápida', Colors.GREEN),
        '4': (500, 'Muy Rápida', Colors.MAGENTA),
        '5': (1000, 'Extrema', Colors.RED),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}┌{'─' * 63}┐{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.BOLD}{Colors.WHITE}  ⚡ SELECCIONA LA VELOCIDAD DE ATAQUE{' ' * 26}{Colors.GREEN}│{Colors.RESET}")
    print(f"{Colors.GREEN}└{'─' * 63}┘{Colors.RESET}\n")
    
    for key, (speed, name, color) in speeds.items():
        bar_len = int(speed / 100) if speed <= 500 else 10 # Controla la longitud visual de la barra
        bar = '█' * bar_len
        print(f"  {color}[{key}]{Colors.RESET} {Colors.BOLD}{name:<15}{Colors.RESET} {color}{bar:<10}{Colors.RESET} {Colors.DIM}({speed} pass/seg){Colors.RESET}")
    
    print(f"\n{Colors.GREEN}{'─' * 65}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}Velocidad{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice in speeds:
        return speeds[choice][0]
    else:
        print(f"\n{Colors.RED}[!] Opción inválida{Colors.RESET}")
        time.sleep(1)
        return select_speed()

def main():
    try:
        platform = select_platform()
        username = get_username(platform)
        gen_choice, gen_name, gen_func = select_generator()
        speed = select_speed()
        
        # Lógica corregida para el modo AUTO
        if gen_choice == '9':
            run_auto_attack(platform, username, speed)
        else:
            # Si no es AUTO, ejecuta el generador seleccionado directamente
            simulate_attack(platform, username, speed, gen_name, gen_func)
        
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {str(e)}{Colors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
