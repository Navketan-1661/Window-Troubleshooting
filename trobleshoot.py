import streamlit as st
import json
import time

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

# ================= LAYOUT COLUMNS =================
# We split the main area into two columns: 
# Left (Main Content) and Right (FAQ Sidebar)
col_main, col_faq = st.columns([0.7, 0.3], gap="large")

with col_main:
    # ================= SIDEBAR MENU =================
    # Note: Streamlit's sidebar remains on the far left for navigation
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

    # ================= MAIN CONTENT AREA =================
    if menu == "Boot Issue":
        st.header("🖥 Boot Issues")
        st.markdown("""
        Boot issues range from slow startup times to errors during the initial loading phase. 
        Common causes include hardware initialization delays, driver conflicts, or corrupt boot configuration data.
        """)
        st.subheader("Process to Fix:")
        st.info("""
        1.  **Disable Startup Apps:** Press `Ctrl + Shift + Esc` > Startup tab > Disable high-impact apps.
        2.  **Enable Fast Startup:** Control Panel > Power Options > Choose what power buttons do > Turn on fast startup.
        3.  **Run Startup Repair:** Shift + Restart > Troubleshoot > Advanced options > Startup Repair.
        4.  **Repair BCD:** Command Prompt > `bootrec /rebuildbcd`.
        5.  **Check Disk:** CMD as Admin > `chkdsk c: /f /r`.
        """)

    elif menu == "System Slowness":
        st.header("🐌 System Slowness")
        st.markdown("""
        System lag is often caused by resource exhaustion. This happens when background processes, malware, 
        or fragmented files consume more CPU, RAM, or Disk bandwidth than available.
        """)
        st.subheader("Process to Fix:")
        st.success("""
        1.  **Identify Resource Hogs:** Task Manager > Sort by CPU/Memory > End heavy tasks.
        2.  **System File Cleanup:** Run `cleanmgr` > Clean up system files.
        3.  **Optimize Visuals:** Search 'Adjust appearance and performance' > Best performance.
        4.  **Check for Malware:** Windows Security > Full Scan.
        5.  **Memory Diagnostic:** Search 'Windows Memory Diagnostic' > Restart and check.
        """)

    elif menu == "Applications Issue":
        st.header("📦 Application Issues")
        st.markdown("""
        Apps may fail to launch, crash randomly, or show 'Not Responding' errors. This is usually due to 
        registry errors, missing DLL files, or version incompatibility.
        """)
        st.subheader("Process to Fix:")
        st.info("""
        1.  **Reset/Repair App:** Settings > Apps > Select app > Advanced options > Repair/Reset.
        2.  **Compatibility Mode:** Right-click .exe > Properties > Compatibility > Run for Windows 8.
        3.  **Verify Dependencies:** Reinstall Visual C++ Redistributables and .NET Framework.
        4.  **Event Viewer:** Search 'Event Viewer' > Application Logs > Check Error codes.
        """)

    elif menu == "C Drive Full":
        st.header("💽 C Drive Full")
        st.markdown("""
        A full C drive prevents Windows from creating virtual memory, leading to instability. 
        It is often filled by logs, update backups, and user profile data.
        """)
        st.subheader("Process to Fix:")
        st.success("""
        1.  **Storage Sense:** Settings > System > Storage > Turn on Storage Sense.
        2.  **Update Backups:** Disk Cleanup > Clean up system files > Windows Update Cleanup.
        3.  **Redirect Folders:** Right-click Downloads/Videos > Properties > Location > Move to D:.
        4.  **Disable Hibernation:** CMD as Admin > `powercfg -h off` (saves space equal to RAM).
        """)

    elif menu == "Printer Issue":
        st.header("🖨 Printer Issues")
        st.markdown("""
        Printer issues often stem from the 'Print Spooler' service failing or communication gaps 
        between the firmware and the Windows driver stack.
        """)
        st.subheader("Process to Fix:")
        st.info("""
        1.  **Flush Spooler:** Stop 'Print Spooler' in services.msc > Delete files in `spool\\PRINTERS` > Start service.
        2.  **Check Ports:** Control Panel > Devices > Printer Properties > Ports tab.
        3.  **Manufacturer Software:** Always download the 'Full Software Package' from the official site.
        """)

    elif menu == "Windows Not Booting":
        st.header("⚠ Windows Not Booting")
        st.markdown("""
        Occurs when the Master Boot Record (MBR) is unreadable or essential kernel files are missing.
        """)
        st.subheader("Process to Fix:")
        st.error("""
        1.  **Trigger WinRE:** Force shut down 3 times during boot to enter 'Automatic Repair'.
        2.  **SFC Recovery:** Advanced Options > Command Prompt > `sfc /scannow`.
        3.  **Uninstall Updates:** Troubleshoot > Advanced options > Uninstall latest Quality Update.
        4.  **Safe Mode:** Startup Settings > Restart > Press F5 for Safe Mode.
        """)

    elif menu == "BSOD Error":
        st.header("🔵 Blue Screen of Death (BSOD)")
        st.markdown("""
        BSODs are triggered when Windows encounters a kernel-level error. Usually driver or hardware related.
        """)
        st.subheader("Process to Fix:")
        st.info("""
        1.  **Analyze Dump Files:** Use 'BlueScreenView' to read `.dmp` files in `C:\\Windows\\Minidump`.
        2.  **Update Drivers:** Focus on Display, Network, and Chipset in Device Manager.
        3.  **Check Hardware:** Reseat RAM sticks and GPU; check for CPU overheating.
        """)

    elif menu == "Audio Issue":
        st.header("🔊 Audio Issues")
        st.markdown("""
        Audio problems can be caused by disabled services, incorrect sample rates, or driver conflicts.
        """)
        st.subheader("Process to Fix:")
        st.success("""
        1.  **Verify Default:** Right-click Speaker icon > Sound Settings > Ensure correct device is default.
        2.  **Restart Services:** Open `services.msc` > Restart 'Windows Audio'.
        3.  **Disable Enhancements:** Sound Properties > Enhancements > Disable all enhancements.
        """)

    elif menu == "Camera Issue":
        st.header("📷 Camera Issues")
        st.markdown("""
        Cameras fail due to physical shutters, privacy settings, or Antivirus software blocking access.
        """)
        st.subheader("Process to Fix:")
        st.info("""
        1.  **Privacy Settings:** Settings > Privacy > Camera > Allow apps to access camera.
        2.  **Check Antivirus:** Look for 'Webcam Protection' settings in your security software.
        3.  **Driver Update:** Check 'Cameras' in Device Manager for 'Integrated Camera'.
        """)

    elif menu == "Display Issue":
        st.header("🖥 Display Issues")
        st.markdown("""
        Flickering, blurry text, or black screens are usually linked to the Graphics (GPU) driver.
        """)
        st.subheader("Process to Fix:")
        st.success("""
        1.  **Reset Driver:** `Win + Ctrl + Shift + B` (restarts graphics driver).
        2.  **Fix Scaling:** Settings > System > Display > Set Scale to '(Recommended)'.
        3.  **Cable Check:** Swap HDMI/DP cables to rule out hardware failure.
        """)

    elif menu == "Virtual Machine Issue":
        st.header("🧪 Virtual Machine Issues")
        st.markdown("""
        Usually occurs because CPU virtualization is off or there's a conflict with Windows Hyper-V.
        """)
        st.subheader("Process to Fix:")
        st.info("""
        1.  **BIOS Virtualization:** Restart > Enter BIOS > Enable VT-x or AMD-V.
        2.  **Disable Hyper-V:** Turn Windows features on/off > Uncheck Hyper-V & Virtual Machine Platform.
        3.  **Resources:** Increase VM RAM/CPU; install Guest Additions for performance.
        """)

with col_faq:
    # ================= FAQ SIDEBAR (RIGHT) =================
    st.markdown("### ❓ Quick FAQ")
    
    with st.expander("How do I open Command Prompt as Admin?"):
        st.write("Search 'CMD' in the Start menu, right-click it, and select **'Run as administrator'**.")

    with st.expander("What is 'WinRE'?"):
        st.write("The Windows Recovery Environment is a diagnostic tool accessed by holding Shift while clicking Restart.")

    with st.expander("My screen is yellow/orange?"):
        st.write("Check **'Night Light'** settings in Display. It is likely scheduled to turn on automatically.")

    with st.expander("How to check my Windows version?"):
        st.write("Press `Win + R`, type `winver`, and press Enter.")

    with st.expander("Is it safe to delete Temp files?"):
        st.write("Yes, files in `%temp%` are temporary cache files and safe to delete to free up space.")

    with st.expander("How to enter BIOS?"):
        st.write("Restart your PC and repeatedly tap `F2`, `F10`, or `Del` as soon as the logo appears.")

    st.divider()
    st.caption("Need more help? Visit our physical Tech Cafe location for hands-on support.")
