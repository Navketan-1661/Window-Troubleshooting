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

# ================= CUSTOM CSS FOR UI =================
st.markdown("""
<style>
    /* Floating button style */
    .floating-chat-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        background-color: #0078D4;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        cursor: pointer;
        z-index: 1000;
        transition: transform 0.2s;
    }
    .floating-chat-button:hover {
        transform: scale(1.1);
    }
    
    /* Chat Window Overlay Style */
    .chat-window-container {
        position: fixed;
        bottom: 90px;
        right: 20px;
        width: 380px;
        max-height: 600px;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
        z-index: 1001;
        border: 1px solid #e0e0e0;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    /* FAQ Section styling */
    .faq-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e9ecef;
    }
</style>
""", unsafe_allow_html=True)

# ================= API HELPERS =================
def call_gemini_api(prompt, system_instruction):
    # API key is provided by the environment at runtime. 
    # Must remain an empty string in the code.
    apiKey = "" 

    # Model endpoint for the preview environment
    model_name = "gemini-2.5-flash-preview-09-2025"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={apiKey}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "systemInstruction": {
            "parts": [{"text": system_instruction}]
        }
    }
    
    # Exponential backoff retry logic
    for i in range(5):
        try:
            response = requests.post(url, json=payload, timeout=20)
            
            if response.status_code == 200:
                result = response.json()
                text = result.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', "")
                if text:
                    return text
            elif response.status_code == 403:
                # If 403 occurs, wait and retry as auth might be syncing
                time.sleep(2**i)
                continue
            elif response.status_code == 429:
                time.sleep(2**i)
                continue
        except Exception:
            time.sleep(2**i)
            
    return "I'm having a bit of trouble connecting to the Tech Cafe brain. Please try your question again in a moment."

# ================= HEADER =================
st.title("☕ Tech Cafe")
st.subheader("Windows OS Troubleshooting Guide")
st.write(
    "Select an issue from the sidebar to see step-by-step fixes, or click the blue bubble to chat with our AI expert."
)

st.divider()

# ================= LAYOUT COLUMNS =================
col_main, col_faq = st.columns([0.7, 0.3], gap="large")

with col_main:
    menu = st.sidebar.radio(
        "🛠 Select an Issue",
        [
            "Boot Issue", "System Slowness", "Applications Issue", 
            "C Drive Full", "Printer Issue", "Windows Not Booting", 
            "BSOD Error", "Audio Issue", "Camera Issue", 
            "Display Issue", "Virtual Machine Issue"
        ]
    )

    # Content Map
    content_map = {
        "Boot Issue": ("🖥 Boot Issues", "blue", "1. Disable Startup Apps: Ctrl+Shift+Esc > Startup. \n2. Enable Fast Startup: Power Options > Choose what buttons do. \n3. Run Startup Repair: Shift+Restart > Troubleshoot."),
        "System Slowness": ("🐌 System Slowness", "green", "1. Check Task Manager: End high CPU tasks. \n2. Cleanup Temp: Run cleanmgr. \n3. Optimize Visuals: Search 'Appearance' > Performance."),
        "Applications Issue": ("📦 Application Issues", "blue", "1. Repair/Reset: Settings > Apps. \n2. Compatibility: Right-click > Properties > Compatibility. \n3. Update .NET: Turn Windows features on/off."),
        "C Drive Full": ("💽 C Drive Full", "green", "1. Storage Sense: Enable in Settings. \n2. Disk Cleanup: Clean up system files. \n3. Move Folders: Right-click Downloads > Location > D:."),
        "Printer Issue": ("🖨 Printer Issues", "blue", "1. Restart Spooler: services.msc > Print Spooler. \n2. Check Ports: Control Panel > Devices. \n3. Update Drivers: Official manufacturer site."),
        "Windows Not Booting": ("⚠ Windows Not Booting", "red", "1. Trigger WinRE: Force off 3x. \n2. SFC Scan: CMD > sfc /scannow. \n3. Safe Mode: Startup Settings > F5."),
        "BSOD Error": ("🔵 Blue Screen of Death", "blue", "1. Analyze Minidump: Use BlueScreenView. \n2. Update Drivers: Display and Chipset. \n3. Check RAM: Memory Diagnostic Tool."),
        "Audio Issue": ("🔊 Audio Issues", "green", "1. Verify Default: Right-click Speaker > Sound settings. \n2. Restart Audio: services.msc > Windows Audio. \n3. Enhancements: Disable in properties."),
        "Camera Issue": ("📷 Camera Issues", "blue", "1. Privacy: Settings > Privacy > Camera. \n2. Switch: Check for F-keys or slider. \n3. Reinstall: Device Manager > Cameras."),
        "Display Issue": ("🖥 Display Issues", "green", "1. Reset Driver: Win+Ctrl+Shift+B. \n2. Fix Scaling: Settings > Display. \n3. Cable Check: Reseat HDMI/DP."),
        "Virtual Machine Issue": ("🧪 Virtual Machine Issues", "blue", "1. BIOS VT-x: Enable in BIOS. \n2. Hyper-V: Disable if using VirtualBox. \n3. Guest Additions: Install in VM.")
    }

    header, color, steps = content_map[menu]
    st.header(header)
    st.subheader("Process to Fix:")
    if color == "blue": st.info(steps)
    elif color == "green": st.success(steps)
    else: st.error(steps)

with col_faq:
    st.markdown('<div class="faq-container">', unsafe_allow_html=True)
    st.markdown("### ❓ Quick FAQ")
    faqs = [
        ("How do I open CMD as Admin?", "Search 'CMD', right-click and 'Run as administrator'."),
        ("What is 'WinRE'?", "The Windows Recovery Environment for diagnostics."),
        ("Yellow screen?", "Check 'Night Light' in Display settings."),
        ("Safe to delete Temp?", "Yes, files in %temp% are safe to clear."),
    ]
    for q, a in faqs:
        with st.expander(q):
            st.write(a)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= FLOATING CHATBOT OVERLAY =================

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False
if "messages" not in st.session_state:
    st.session_state.messages = []

# Floating Button HTML (Clicks a hidden Streamlit button)
st.markdown("""
<div class="floating-chat-button" onclick="document.getElementById('hidden-chat-toggle').click()">
    <span style="font-size: 30px; color: white;">💬</span>
</div>
<div style="display:none">
    <button id="hidden-chat-toggle" onclick="document.querySelector('button[key=chat_toggle_btn]').click()"></button>
</div>
""", unsafe_allow_html=True)

# The bridge button that updates Streamlit state
if st.button("Toggle Chat", key="chat_toggle_btn", help="Click the bubble to chat"):
    st.session_state.chat_open = not st.session_state.chat_open

# Custom CSS to hide the Streamlit trigger button
st.markdown("<style>div.stButton > button[key='chat_toggle_btn'] { display: none; }</style>", unsafe_allow_html=True)

# Render the Chat Window Overlay on the right
if st.session_state.chat_open:
    # We use a container placed at the end to allow absolute positioning styling
    with st.container():
        st.markdown('<div class="chat-window-container">', unsafe_allow_html=True)
        
        # Internal Chat Layout
        st.markdown("#### 🤖 Tech Cafe Assistant")
        
        # Chat history container
        chat_box = st.container(height=350)
        with chat_box:
            for m in st.session_state.messages:
                with st.chat_message(m["role"]):
                    st.markdown(m["content"])

        # Chat Input
        if prompt := st.chat_input("Ask about Windows issues..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_box:
                with st.chat_message("user"):
                    st.markdown(prompt)
                
                with st.chat_message("assistant"):
                    sys_prompt = "You are the Tech Cafe AI Assistant. Provide helpful, numbered troubleshooting steps for Windows OS issues. Be concise."
                    with st.spinner("Expert is thinking..."):
                        response = call_gemini_api(prompt, sys_prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
        
        st.markdown('</div>', unsafe_allow_html=True)
