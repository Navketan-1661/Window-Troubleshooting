import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Tech Cafe | Windows Troubleshooting",
    page_icon="☕",
    layout="wide"
)

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
    st.subheader("Process to Fix:")
    st.info("""
    1. **Disable Startup Apps:** Press `Ctrl+Shift+Esc` > Startup tab > Disable high-impact apps.
    2. **Run Startup Repair:** Shift + Restart > Troubleshoot > Advanced Options > Startup Repair.
    3. **Check Disk Health:** Open Command Prompt as Admin > Type `chkdsk c: /f` > Restart.
    4. **Update BIOS/Drivers:** Visit manufacturer's site for the latest chipset updates.
    """)

elif menu == "System Slowness":
    st.header("🐌 System Slowness")
    st.subheader("Process to Fix:")
    st.success("""
    1. **Check Task Manager:** `Ctrl+Shift+Esc` > Sort by CPU/Memory > End heavy tasks.
    2. **Cleanup Temp Files:** Press `Win + R` > Type `%temp%` > Delete all files.
    3. **Adjust Performance:** Search 'Appearance and Performance' > Select 'Adjust for best performance'.
    4. **Check for Updates:** Settings > Update & Security > Check for Windows Updates.
    """)

elif menu == "Applications Issue":
    st.header("📦 Application Issues")
    st.subheader("Process to Fix:")
    st.info("""
    1. **Repair App:** Settings > Apps > Apps & Features > Select App > Advanced Options > Repair/Reset.
    2. **Compatibility Mode:** Right-click app shortcut > Properties > Compatibility > Run for Windows 7/8.
    3. **Install Dependencies:** Ensure .NET Framework and Visual C++ Redistributables are updated.
    4. **Reinstall:** Uninstall the app, restart PC, and install the latest version from the official site.
    """)

elif menu == "C Drive Full":
    st.header("💽 C Drive Full")
    st.subheader("Process to Fix:")
    st.success("""
    1. **Disk Cleanup:** Search 'Disk Cleanup' > Select C: > Clean up system files.
    2. **Storage Sense:** Settings > System > Storage > Turn on 'Storage Sense'.
    3. **Uninstall Large Apps:** Settings > Apps > Sort by 'Size' > Remove what you don't need.
    4. **Move Folders:** Right-click 'Downloads' or 'Documents' > Properties > Location > Move to D: Drive.
    """)

elif menu == "Printer Issue":
    st.header("🖨 Printer Issues")
    st.subheader("Process to Fix:")
    st.info("""
    1. **Restart Spooler:** `Win+R` > `services.msc` > Right-click 'Print Spooler' > Restart.
    2. **Check Connection:** Ensure USB is firm or Wi-Fi is on the same network as the PC.
    3. **Clear Queue:** Open Printer Queue > Printer Menu > Cancel All Documents.
    4. **Update Driver:** Device Manager > Printers > Right-click your printer > Update Driver.
    """)

elif menu == "Windows Not Booting":
    st.header("⚠ Windows Not Booting")
    st.subheader("Process to Fix:")
    st.error("""
    1. **Access WinRE:** Force shut down 3 times during boot to enter 'Automatic Repair' mode.
    2. **System Restore:** Advanced Options > System Restore > Pick a date when it worked.
    3. **SFC Scan:** Advanced Options > Command Prompt > Type `sfc /scannow`.
    4. **Safe Mode:** Advanced Options > Startup Settings > Restart > Press 5 for Safe Mode with Networking.
    """)

elif menu == "BSOD Error":
    st.header("🔵 Blue Screen of Death (BSOD)")
    st.subheader("Process to Fix:")
    st.info("""
    1. **Note the Error Code:** Look for text like `CRITICAL_PROCESS_DIED` or `MEMORY_MANAGEMENT`.
    2. **Update Graphics Driver:** Most BSODs are caused by Display drivers; update them via Device Manager.
    3. **Memory Diagnostic:** Search 'Windows Memory Diagnostic' > Restart and check for RAM errors.
    4. **Remove New Hardware:** Unplug recently added USB devices or RAM and test again.
    """)

elif menu == "Audio Issue":
    st.header("🔊 Audio Issues")
    st.subheader("Process to Fix:")
    st.success("""
    1. **Check Output:** Click Speaker icon on Taskbar > Ensure correct device is selected.
    2. **Privacy Settings:** Settings > Privacy > Microphone > Allow apps to access microphone.
    3. **Troubleshoot:** Settings > System > Sound > Troubleshoot.
    4. **Generic Driver:** Device Manager > Sound > Right-click device > Update > 'Browse my computer' > 'Let me pick' > Select 'High Definition Audio Device'.
    """)

elif menu == "Camera Issue":
    st.header("📷 Camera Issues")
    st.subheader("Process to Fix:")
    st.info("""
    1. **Physical Switch:** Check for a sliding cover or a Function key (F6/F10) with a camera icon.
    2. **Privacy Access:** Settings > Privacy > Camera > Enable 'Allow apps to access your camera'.
    3. **Reset Camera App:** Settings > Apps > Camera > Advanced Options > Reset.
    4. **Roll Back Driver:** Device Manager > Cameras > Properties > Driver tab > Roll Back Driver.
    """)

elif menu == "Display Issue":
    st.header("🖥 Display Issues")
    st.subheader("Process to Fix:")
    st.success("""
    1. **Reset Driver:** Press `Win + Ctrl + Shift + B` (restarts the graphics driver).
    2. **Check Refresh Rate:** Settings > System > Display > Advanced Display > Set to 60Hz.
    3. **Night Light:** If screen is yellow, turn off 'Night Light' in Display settings.
    4. **Cable Check:** Ensure HDMI/DisplayPort cables are fully plugged in or try a different cable.
    """)

elif menu == "Virtual Machine Issue":
    st.header("🧪 Virtual Machine Issues")
    st.subheader("Process to Fix:")
    st.info("""
    1. **Enable VT-x/AMD-V:** Restart PC > Enter BIOS > Enable 'Virtualization Technology'.
    2. **Disable Hyper-V:** (If using VirtualBox/VMware) Search 'Turn Windows features on/off' > Uncheck Hyper-V.
    3. **Increase Resources:** Shut down VM > Settings > Increase RAM and CPU cores.
    4. **Guest Additions:** Inside the VM, go to Devices menu > Insert Guest Additions Image > Install and Restart.
    """)
