import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Tech Cafe | Windows Troubleshooting",
    page_icon="☕",
    layout="wide"
)

# ================= HEADER =================
st.title("☕ Tech Cafe")
st.subheader("Windows OS Troubleshooting Blog")
st.write(
    "A simple technical blog focused on diagnosing and fixing common "
    "Windows operating system issues."
)

st.divider()

# ================= SIDEBAR MENU =================
menu = st.sidebar.selectbox(
    "🛠 Select Issue Category",
    [
        "Boot Issue",
        "System Slowness",
        "Apps Issue",
        "C Drive Full",
        "Printer Issue",
        "Windows Not Boot",
        "BSOD Error",
        "Audio Issue",
        "Camera Issue",
        "Display Issue",
        "VM Issue"
    ]
)

# ================= CONTENT =================
if menu == "Boot Issue":
    st.header("Boot Issues")
    st.write("""
    - Slow boot time  
    - Startup repair errors  
    - Corrupted boot files  
    - Recovery mode fixes  
    """)

elif menu == "System Slowness":
    st.header("System Slowness")
    st.write("""
    **Steps to improve performance:**

    1. Restart the system  
       Clears temporary memory and stuck processes.

    2. Check CPU / RAM usage  
       - Press **Ctrl + Shift + Esc**  
       - CPU > 80%, Memory > 80%, Disk 100%  

    3. Disable startup programs  
       Task Manager → Startup → Disable unnecessary apps

    4. Free disk space  
       - Keep at least 20% free  
       - Run `cleanmgr`
    """)

elif menu == "Apps Issue":
    st.header("Application Issues")
    st.write("""
    - App crashes or not opening  
    - Compatibility issues  
    - Missing dependencies  
    - Microsoft Store app errors  
    """)

elif menu == "C Drive Full":
    st.header("C Drive Full")
    st.write("""
    - Disk cleanup  
    - Remove temporary files  
    - Uninstall unused software  
    - Move data to another drive  
    """)

elif menu == "Printer Issue":
    st.header("Printer Issues")
    st.write("""
    - Driver problems  
    - Printer offline  
    - Spooler service errors  
    - Network printer issues  
    """)

elif menu == "Windows Not Boot":
    st.header("Windows Not Booting")
    st.write("""
    - Startup repair  
    - Safe mode recovery  
    - System restore  
    - Command Prompt fixes  
    """)

elif menu == "BSOD Error":
    st.header("BSOD Errors")
    st.write("""
    - Analyze stop codes  
    - Driver conflicts  
    - Hardware issues  
    - Memory dump analysis  
    """)

elif menu == "Audio Issue":
    st.header("Audio Issues")
    st.write("""
    - No sound  
    - Driver missing  
    - Microphone not working  
    - Audio services stopped  
    """)

elif menu == "Camera Issue":
    st.header("Camera Issues")
    st.write("""
    - Webcam not detected  
    - Permission issues  
    - Driver conflicts  
    """)

elif menu == "Display Issue":
    st.header("Display Issues")
    st.write("""
    - Black screen  
    - Flickering display  
    - Resolution problems  
    - Multiple monitor issues  
    """)

elif menu == "VM Issue":
    st.header("Virtual Machine Issues")
    st.write("""
    - VMware / VirtualBox errors  
    - VM not booting  
    - Network issues  
    - Performance tuning  
    """)