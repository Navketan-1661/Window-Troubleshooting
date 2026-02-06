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

    st.subheader("1. Slow Boot Time")
    st.write(
        "Slow boot occurs when Windows takes a long time to reach the login screen. "
        "This usually happens due to too many startup programs, outdated drivers, "
        "or a traditional hard disk instead of an SSD."
    )

    st.subheader("2. Startup Repair Errors")
    st.write(
        "Startup Repair errors appear when Windows detects corrupted system files. "
        "It may fail to fix the issue automatically, leading to a repair loop."
    )

    st.subheader("3. Corrupted Boot Files")
    st.write(
        "Boot files such as BCD or MBR can get corrupted due to sudden power failure, "
        "malware, or disk errors. This prevents Windows from loading properly."
    )

    st.subheader("4. Recovery Mode Fixes")
    st.write(
        "Using Windows Recovery Environment (WinRE), you can access Startup Repair, "
        "System Restore, and Command Prompt to repair boot-related problems."
    )

elif menu == "System Slowness":
    st.header("🐌 System Slowness")

    st.subheader("1. High CPU or RAM Usage")
    st.write(
        "When CPU or RAM usage stays above 80%, the system becomes slow. "
        "This is usually caused by background apps, malware, or insufficient RAM."
    )

    st.subheader("2. Too Many Startup Programs")
    st.write(
        "Applications that start automatically with Windows increase boot time "
        "and consume system resources continuously."
    )

    st.subheader("3. Low Disk Space")
    st.write(
        "Windows needs free disk space for virtual memory and updates. "
        "Less than 20% free space can significantly slow down the system."
    )

    st.subheader("4. Malware or Unwanted Software")
    st.write(
        "Malware runs hidden processes that consume CPU, memory, and disk resources, "
        "causing overall system slowdown."
    )

elif menu == "Applications Issue":
    st.header("📦 Application Issues")

    st.subheader("1. Application Crashes")
    st.write(
        "Apps may crash due to corrupted installation files, missing libraries, "
        "or incompatible Windows updates."
    )

    st.subheader("2. Compatibility Problems")
    st.write(
        "Older applications may not work properly on newer Windows versions "
        "unless compatibility mode is enabled."
    )

    st.subheader("3. Missing Dependencies")
    st.write(
        "Some applications require .NET Framework, Visual C++ Redistributables, "
        "or Java to run correctly."
    )

    st.subheader("4. Microsoft Store App Errors")
    st.write(
        "Store apps may fail due to cache corruption, account sync issues, "
        "or disabled background services."
    )

elif menu == "C Drive Full":
    st.header("💽 C Drive Full")

    st.subheader("1. Temporary Files Accumulation")
    st.write(
        "Temporary files created by apps and Windows updates can occupy large "
        "amounts of disk space over time."
    )

    st.subheader("2. Windows Update Files")
    st.write(
        "Old update files remain stored after updates and are safe to remove "
        "using Disk Cleanup."
    )

    st.subheader("3. Installed Programs")
    st.write(
        "Unused software installed on the C drive consumes space and should be "
        "uninstalled if not required."
    )

    st.subheader("4. User Data Storage")
    st.write(
        "Storing videos, downloads, and documents on the C drive can quickly "
        "fill it up. Moving them to another drive is recommended."
    )

elif menu == "Printer Issue":
    st.header("🖨 Printer Issues")

    st.subheader("1. Printer Offline Error")
    st.write(
        "This occurs when the printer is not communicating with the system due to "
        "network issues or incorrect settings."
    )

    st.subheader("2. Driver Problems")
    st.write(
        "Outdated or corrupted printer drivers prevent Windows from sending "
        "print commands correctly."
    )

    st.subheader("3. Print Spooler Errors")
    st.write(
        "The print spooler manages print jobs. If it stops or crashes, printing "
        "will not work."
    )

elif menu == "Windows Not Booting":
    st.header("⚠ Windows Not Booting")

    st.subheader("1. Corrupt System Files")
    st.write(
        "Essential Windows files may become corrupt due to improper shutdowns "
        "or disk errors."
    )

    st.subheader("2. Failed Windows Updates")
    st.write(
        "Interrupted updates can prevent Windows from booting properly."
    )

    st.subheader("3. Disk or Hardware Issues")
    st.write(
        "Hard disk failure or faulty RAM can completely stop Windows from loading."
    )

elif menu == "BSOD Error":
    st.header("🔵 Blue Screen of Death (BSOD)")

    st.subheader("1. Driver Conflicts")
    st.write(
        "Incorrect or incompatible drivers are the most common cause of BSOD errors."
    )

    st.subheader("2. Hardware Failures")
    st.write(
        "Faulty RAM, overheating CPU, or failing storage devices can trigger BSODs."
    )

    st.subheader("3. Memory Dump Analysis")
    st.write(
        "Windows creates dump files during BSODs which help identify the exact cause."
    )

elif menu == "Audio Issue":
    st.header("🔊 Audio Issues")

    st.subheader("1. No Sound Output")
    st.write(
        "This can occur if the wrong playback device is selected or audio services "
        "are not running."
    )

    st.subheader("2. Audio Driver Missing")
    st.write(
        "Without proper drivers, Windows cannot communicate with sound hardware."
    )

    st.subheader("3. Microphone Not Working")
    st.write(
        "Privacy settings or disabled microphone access can block audio input."
    )

elif menu == "Camera Issue":
    st.header("📷 Camera Issues")

    st.subheader("1. Camera Not Detected")
    st.write(
        "Camera hardware may not be detected due to driver issues or BIOS settings."
    )

    st.subheader("2. Permission Denied")
    st.write(
        "Windows privacy settings may block camera access for applications."
    )

elif menu == "Display Issue":
    st.header("🖥 Display Issues")

    st.subheader("1. Black Screen")
    st.write(
        "Often caused by graphics driver issues or incorrect display output selection."
    )

    st.subheader("2. Screen Flickering")
    st.write(
        "Occurs due to incompatible refresh rate or outdated graphics drivers."
    )

    st.subheader("3. Resolution Problems")
    st.write(
        "Incorrect resolution settings can make the display appear blurry or stretched."
    )

elif menu == "Virtual Machine Issue":
    st.header("🧪 Virtual Machine Issues")

    st.subheader("1. VM Not Starting")
    st.write(
        "Occurs when virtualization is disabled in BIOS or system resources are insufficient."
    )

    st.subheader("2. Network Not Working")
    st.write(
        "Incorrect VM network adapter configuration can block internet access."
    )

    st.subheader("3. Poor Performance")
    st.write(
        "Low RAM, CPU allocation, or missing guest additions reduce VM performance."
    )
