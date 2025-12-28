class JarvisAssistant:
    """
    JarvisAssistant is the core orchestrator that connects:
    - Memory
    - PromptController
    - GeminiEngine

    It controls the full request → response workflow.
    """

    def __init__(self, engine, prompt_controller, memory):
        """
        Initialize Jarvis Assistant with required components.

        Args:
            engine (GeminiEngine): Gemini API handler
            prompt_controller (PromptController): Prompt builder
            memory (Memory): Conversation memory manager
        """
        self.engine = engine
        self.prompt_controller = prompt_controller
        self.memory = memory

    def respond(self, user_input: str) -> str:
        """
        Process user input and return AI response.

        Workflow:
        User Input
            ↓
        Load Memory
            ↓
        Build Prompt
            ↓
        Generate Response (Gemini)
            ↓
        Save to Memory
            ↓
        Return Response

        Args:
            user_input (str): User message

        Returns:
            str: Assistant response
        """

        if not user_input.strip():
            return "Please enter a valid question."

        # 1️⃣ Save user input to memory
        self.memory.add("user", user_input)

        # 2️⃣ Load conversation history
        history = self.memory.get_history()

        # 3️⃣ Build final prompt
        prompt = self.prompt_controller.build_prompt(
            user_input=user_input,
            memory=history
        )

        # 4️⃣ Generate response from Gemini
        response = self.engine.generate(prompt)

        # 5️⃣ Save assistant response to memory
        self.memory.add("assistant", response)

        return response
