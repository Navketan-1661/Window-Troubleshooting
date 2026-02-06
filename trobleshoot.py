import streamlit as st
import json
import time
import requests

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Tech Cafe | Windows Troubleshooting",
    page_icon="☕",
    layout="wide"
)

# ================= API HELPERS =================
def call_gemini_api(prompt, system_instruction):
    # The environment provides the key at runtime; strictly leave as empty string.
    apiKey = "" 
    # Use the specific model version supported in the preview environment
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={apiKey}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "systemInstruction": {
            "parts": [{"text": system_instruction}]
        }
    }
    
    # Exponential backoff retry logic (Mandatory for Gemini API)
    for i in range(5):
        try:
            # Added a shorter timeout to trigger retries faster if the connection hangs
            response = requests.post(url, json=payload, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                # Safe extraction of the text content
                candidates = result.get('candidates', [])
                if candidates:
                    parts = candidates[0].get('content', {}).get('parts', [])
                    if parts:
                        return parts[0].get('text', "I received an empty response from the brain.")
                return "The brain returned a successful response but no content was found."
            
            # Handle rate limiting or server errors with backoff
            elif response.status_code in [429, 500, 503]:
                time.sleep(2**i)
                continue
            else:
                return f"Technical Error ({response.status_code}): I'm unable to process this request right now."
                
        except Exception as e:
            # On exception, wait and retry
            time.sleep(2**i)
    
    return "Connection Timeout: I'm having trouble connecting to the Tech Cafe brain. Please verify your internet connection and try again in 30 seconds."

# ================= HEADER =================
st.title("☕ Tech Cafe")
st.subheader("Windows OS Troubleshooting Guide")
st.write(
    "This technical guide explains common Windows problems, their causes, "
    "and step-by-step solutions in simple language."
)

st.divider()

# ================= SIDEBAR =================
menu = st.sidebar.radio(
    "🛠 Select an Issue",
    [
        "Boot Issue",
        "System Slowness",
        "Applications Issue",
        "C Drive Full",
        "Printer Issue",
        "Windows Not Booting",
        "BSOD Error",
        "Audio Issue",
        "Camera Issue",
        "Display Issue",
        "Virtual Machine Issue"
    ]
)

# ================= CONTENT =================

if menu == "Boot Issue":
    st.header("🖥 Boot Issues")
    st.markdown("""
    Boot issues range from slow startup times to errors during the initial loading phase. 
    Common causes include hardware initialization delays, driver conflicts, or corrupt boot configuration data.
    """)
    st.subheader("Process to Fix:")
    st.info("""
    1.  **Disable Startup Apps:**
        * Press `Ctrl + Shift + Esc` to open Task Manager.
        * Navigate to the **Startup** tab.
        * Right-click and **Disable** apps with a 'High' startup impact.
    2.  **Enable Fast Startup:**
        * Go to `Control Panel` > `Power Options` > `Choose what the power buttons do`.
        * Click `Change settings that are currently unavailable`.
        * Check `Turn on fast startup`.
    3.  **Run Startup Repair:**
        * Hold `Shift` while clicking **Restart**.
        * Select `Troubleshoot` > `Advanced options` > `Startup Repair`.
    4.  **Repair Boot Configuration (BCD):**
        * In Advanced options, open **Command Prompt**.
        * Type `bootrec /rebuildbcd` and press Enter.
    5.  **Check Disk for Errors:**
        * Open CMD as Admin and type `chkdsk c: /f /r`. 
        * Type `Y` to schedule a scan on the next restart.
    """)

elif menu == "System Slowness":
    st.header("🐌 System Slowness")
    st.markdown("""
    System lag is often caused by resource exhaustion. This happens when background processes, malware, 
    or fragmented files consume more CPU, RAM, or Disk bandwidth than available.
    """)
    st.subheader("Process to Fix:")
    st.success("""
    1.  **Identify Resource Hogs:**
        * Open Task Manager (`Ctrl + Shift + Esc`).
        * Click the **CPU** or **Memory** column to sort by usage.
        * Right-click and **End task** for unresponsive or high-usage apps.
    2.  **System File Cleanup:**
        * Press `Win + R`, type `cleanmgr`, and press Enter.
        * Select Drive C: and click `Clean up system files`.
        * Check `Temporary files`, `Recycle Bin`, and `DirectX Shader Cache`.
    3.  **Optimize Visual Effects:**
        * Search for 'Adjust the appearance and performance of Windows'.
        * Select `Adjust for best performance` or manually uncheck animations.
    4.  **Check for Malware:**
        * Go to `Settings` > `Update & Security` > `Windows Security`.
        * Run a **Full Scan** using Virus & threat protection.
    5.  **Check RAM Integrity:**
        * Search for 'Windows Memory Diagnostic' and choose `Restart now and check for problems`.
    """)

elif menu == "Applications Issue":
    st.header("📦 Application Issues")
    st.markdown("""
    Apps may fail to launch, crash randomly, or show 'Not Responding' errors. This is usually due to 
    registry errors, missing DLL files, or version incompatibility with the current Windows build.
    """)
    st.subheader("Process to Fix:")
    st.info("""
    1.  **Reset/Repair App Settings:**
        * Go to `Settings` > `Apps` > `Apps & features`.
        * Select the app > `Advanced options`.
        * Try **Repair** first; if that fails, use **Reset** (this deletes app data).
    2.  **Use Compatibility Mode:**
        * Right-click the app's `.exe` file or shortcut > `Properties`.
        * Under the **Compatibility** tab, check `Run this program in compatibility mode for`.
        * Select 'Windows 8' or 'Windows 7'.
    3.  **Verify System Dependencies:**
        * Reinstall the latest **Microsoft Visual C++ Redistributable** packages.
        * Enable **.NET Framework** features via 'Turn Windows features on or off'.
    4.  **Check Event Viewer:**
        * Search 'Event Viewer' > `Windows Logs` > `Application`.
        * Look for 'Error' level logs to find specific crash codes.
    """)

elif menu == "C Drive Full":
    st.header("💽 C Drive Full")
    st.markdown("""
    A full C drive prevents Windows from creating paging files (virtual memory), leading to system 
    instability. It is often filled by hidden system logs, update backups, and user profile data.
    """)
    st.subheader("Process to Fix:")
    st.success("""
    1.  **Automated Cleanup:**
        * Go to `Settings` > `System` > `Storage`.
        * Turn on **Storage Sense** to automatically delete old temp files.
    2.  **Remove Windows Update Backups:**
        * In 'Disk Cleanup' > 'Clean up system files', look for `Windows Update Cleanup`. 
        * *Note:* This can save 5GB+ of space but prevents rolling back recent updates.
    3.  **Analyze Space with Tools:**
        * Use a tool like 'WizTree' or 'WinDirStat' to find hidden large files.
    4.  **Redirect Large Folders:**
        * Right-click your `Downloads` or `Videos` folder > `Properties`.
        * In the **Location** tab, click `Move` and select a folder on a different drive (D: or E:).
    5.  **Disable Hibernation (Optional):**
        * Open CMD as Admin and type `powercfg -h off` to save space equal to your RAM size.
    """)

elif menu == "Printer Issue":
    st.header("🖨 Printer Issues")
    st.markdown("""
    Printer issues often stem from the 'Print Spooler' service failing or communication gaps 
    between the printer's firmware and the Windows driver stack.
    """)
    st.subheader("Process to Fix:")
    st.info("""
    1.  **Flush the Print Spooler:**
        * Press `Win + R`, type `services.msc`.
        * Right-click **Print Spooler** and select **Stop**.
        * Go to `C:\\Windows\\System32\\spool\\PRINTERS` and delete all files.
        * Back in Services, right-click **Print Spooler** and select **Start**.
    2.  **Check IP and Ports:**
        * `Control Panel` > `Devices and Printers`.
        * Right-click Printer > `Printer Properties` > `Ports` tab.
        * Ensure the correct IP address or USB port is checked.
    3.  **Remove/Add Device:**
        * Remove the printer from `Settings` > `Devices`.
        * Restart your PC and the printer, then click `Add a printer or scanner`.
    4.  **Manufacturer Software:**
        * Avoid using generic drivers. Download the 'Full Software Package' from the manufacturer's official support site.
    """)

elif menu == "Windows Not Booting":
    st.header("⚠ Windows Not Booting")
    st.markdown("""
    This state occurs when the Master Boot Record (MBR) or GUID Partition Table (GPT) is 
    unreadable, or essential kernel files (winload.efi) are missing.
    """)
    st.subheader("Process to Fix:")
    st.error("""
    1.  **Trigger WinRE:**
        * Turn on PC; when Windows logo appears, hold Power button to force off. 
        * Repeat 3 times until 'Preparing Automatic Repair' appears.
    2.  **SFC and DISM Recovery:**
        * In Advanced Options > Command Prompt:
        * Type `sfc /scannow /offbootdir=c:\\ /offwindir=c:\\windows`
        * Type `dism /image:c:\\ /cleanup-image /restorehealth`.
    3.  **Uninstall Recent Updates:**
        * Go to `Troubleshoot` > `Advanced options` > `Uninstall Updates`.
        * Remove the latest 'Quality Update' or 'Feature Update'.
    4.  **Boot to Safe Mode:**
        * `Startup Settings` > `Restart` > Press `F5` for Safe Mode with Networking.
        * If it boots here, the issue is likely a driver or startup app.
    """)

elif menu == "BSOD Error":
    st.header("🔵 Blue Screen of Death (BSOD)")
    st.markdown("""
    BSODs (Stop Errors) are triggered when Windows encounters a kernel-level error it cannot 
    recover from. These are 70% driver-related and 30% hardware-related.
    """)
    st.subheader("Process to Fix:")
    st.info("""
    1.  **Search the Stop Code:**
        * Common codes: `WHEA_UNCORRECTABLE_ERROR` (Hardware), `IRQL_NOT_LESS_OR_EQUAL` (Driver).
    2.  **Analyze Dump Files:**
        * Download 'BlueScreenView' or 'WhoCrashed' to read the `.dmp` files in `C:\\Windows\\Minidump`.
        * These tools will point to the specific `.sys` driver file causing the crash.
    3.  **Update Hardware Drivers:**
        * Right-click Start > `Device Manager`.
        * Focus on **Display Adapters**, **Network Adapters**, and **Chipset**.
    4.  **Check Hardware Connections:**
        * Reseat RAM sticks and GPU. 
        * Clean dust from fans to prevent thermal-related BSODs.
    """)

elif menu == "Audio Issue":
    st.header("🔊 Audio Issues")
    st.markdown("""
    Audio problems can be caused by disabled services, incorrect sample rates, or 'exclusive mode' 
    conflicts where one app takes total control of the sound card.
    """)
    st.subheader("Process to Fix:")
    st.success("""
    1.  **Verify Default Device:**
        * Right-click the Speaker icon > `Sounds` (or `Sound Settings`).
        * Ensure the correct device has the **Green Checkmark** as Default Device.
    2.  **Restart Audio Services:**
        * Open `services.msc`.
        * Find **Windows Audio** and **Windows Audio Endpoint Builder**.
        * Right-click each and select **Restart**.
    3.  **Disable Audio Enhancements:**
        * In Sound Properties > `Enhancements` tab > Check `Disable all enhancements`.
    4.  **Reinstall Audio Controller:**
        * `Device Manager` > `Sound, video and game controllers`.
        * Right-click 'Realtek Audio' (or similar) > `Uninstall device`. 
        * Restart PC; Windows will auto-reinstall the driver.
    """)

elif menu == "Camera Issue":
    st.header("📷 Camera Issues")
    st.markdown("""
    Cameras may fail due to privacy shutters (physical), privacy settings (software), or 
    conflicts with Antivirus software blocking the video stream.
    """)
    st.subheader("Process to Fix:")
    st.info("""
    1.  **Privacy Settings:**
        * `Settings` > `Privacy` > `Camera`.
        * Ensure 'Allow apps to access your camera' is **On**.
        * Scroll down and ensure specific apps (Teams, Zoom, etc.) are toggled **On**.
    2.  **Check Antivirus:**
        * Some AV programs (like Kaspersky or ESET) have a 'Webcam Protection' feature that blocks access by default.
    3.  **Device Manager Check:**
        * If the camera isn't listed, look for 'Unknown Device' or 'Integrated Camera' under **Cameras** or **Imaging Devices**.
    4.  **Driver Update:**
        * Update via Device Manager or the laptop manufacturer's 'Support Assistant' tool.
    """)

elif menu == "Display Issue":
    st.header("🖥 Display Issues")
    st.markdown("""
    Common display issues include screen flickering, incorrect scaling (blurry text), or black 
    screens. These are almost always linked to the Graphics Processing Unit (GPU) driver.
    """)
    st.subheader("Process to Fix:")
    st.success("""
    1.  **Graphics Driver Reset:**
        * Press `Win + Ctrl + Shift + B`. You will hear a beep and the screen will flicker; this reloads the driver.
    2.  **Fix Blurry Text:**
        * `Settings` > `System` > `Display`.
        * Ensure **Scale and layout** is set to the '(Recommended)' percentage.
    3.  **Use DDU (Display Driver Uninstaller):**
        * If drivers won't update, use 'DDU' in Safe Mode to completely wipe GPU drivers.
        * Perform a clean install of NVIDIA, AMD, or Intel drivers.
    4.  **Check External Connections:**
        * Swap HDMI/DP cables.
        * Try a different monitor port or a different monitor to rule out hardware failure.
    """)

elif menu == "Virtual Machine Issue":
    st.header("🧪 Virtual Machine Issues")
    st.markdown("""
    Virtualization issues usually occur because the CPU's hardware-level virtualization is 
    off, or there is a conflict between different hypervisors (e.g., VirtualBox vs. Hyper-V).
    """)
    st.subheader("Process to Fix:")
    st.info("""
    1.  **Enable BIOS Virtualization:**
        * Restart > Tap `F2/Del` to enter BIOS.
        * Look for **Intel VT-x**, **AMD-V**, or **SVM Mode** and set to **Enabled**.
    2.  **Manage Windows Hypervisor:**
        * If using VirtualBox, search 'Turn Windows features on or off'.
        * Uncheck **Hyper-V**, **Virtual Machine Platform**, and **Windows Hypervisor Platform**.
    3.  **Check Available RAM:**
        * Ensure your host PC has at least 2GB more RAM than what you are assigning to the VM.
    4.  **Extension Packs:**
        * Install the 'Oracle VM VirtualBox Extension Pack' for USB 3.0 and RDP support.
    """)

# ================= CHATBOT SECTION =================
st.divider()
st.subheader("🤖 Tech Cafe AI Assistant")
st.write("Ask any Windows troubleshooting question and I'll guide you through the solution.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat system prompt
SYSTEM_PROMPT = """
You are the Tech Cafe AI Assistant, a technical expert specializing in Windows Troubleshooting.
Your goal is to provide concise, step-by-step instructions for common Windows issues based on the context provided in the Tech Cafe app.
"""

# React to user input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Gemini API
    with st.chat_message("assistant"):
        with st.spinner("Connecting to Tech Cafe brain..."):
            response = call_gemini_api(prompt, SYSTEM_PROMPT)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
