import streamlit as st

from config.settings import Settings
from peya.gemini_engine import GeminiEngine
from peya.prompt_controller import PromptController
from peya.memory import Memory
from peya.assistant import JarvisAssistant



st.set_page_config(
    page_title="PEYA Personal AI Assistant",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Paye Your AI Assistant")


# -------------------- INITIALIZE COMPONENTS --------------------
@st.cache_resource
def initialize_jarvis():
    settings = Settings()
    api_key = settings.load_api_key()

    engine = GeminiEngine(api_key)
    memory = Memory()
    prompt_controller = PromptController()

    assistant = JarvisAssistant(
        engine=engine,
        prompt_controller=prompt_controller,
        memory=memory
    )
    return assistant, prompt_controller, memory


assistant, prompt_controller, memory = initialize_jarvis()


# -------------------- SIDEBAR --------------------
st.sidebar.title("⚙️ Settings")

role = st.sidebar.selectbox(
    "Select Assistant Role",
    ["Tutor", "Coder", "Mentor"]
)

prompt_controller.set_role(role)

if st.sidebar.button("🧹 Clear Memory"):
    memory.clear()
    st.success("Conversation memory cleared!")


# -------------------- CHAT HISTORY --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# -------------------- USER INPUT --------------------
user_input = st.chat_input("Ask JARVIS...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get assistant response
    response = assistant.respond(user_input)

    # Show assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)
