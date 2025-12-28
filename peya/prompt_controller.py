class PromptController:
    """
    PromptController is responsible for building the final prompt
    sent to the Gemini model.

    It injects:
    - System instructions
    - Assistant role (Tutor / Coder / Mentor)
    - Conversation memory
    - User input
    """

    def __init__(self, role: str = "Tutor"):
        self.role = role

    def set_role(self, role: str):
        """
        Update assistant role dynamically.
        """
        self.role = role

    def build_prompt(self, user_input: str, memory: str) -> str:
        """
        Build the final structured prompt for Gemini.

        Args:
            user_input (str): Current user message
            memory (str): Formatted conversation history

        Returns:
            str: Complete prompt
        """

        system_instructions = self._get_system_instructions()

        prompt = f"""
{system_instructions}

--- Conversation History ---
{memory}

--- User Input ---
{user_input}

--- Assistant Response ---
"""
        return prompt.strip()

    def _get_system_instructions(self) -> str:
        """
        Internal method to define assistant behavior based on role.
        """

        base_rules = """
You are JARVIS, a highly intelligent, polite, and helpful personal AI assistant.
Always respond clearly, accurately, and professionally.
If you do not know an answer, say so honestly.
"""

        role_rules = {
            "Tutor": """
You act as a patient tutor.
Explain concepts step by step.
Use simple language and examples.
Encourage learning and curiosity.
""",
            "Coder": """
You act as an expert coding assistant.
Write clean, efficient, and well-commented code.
Explain logic when necessary.
Follow best practices.
""",
            "Mentor": """
You act as a career and life mentor.
Provide practical advice.
Be motivating, realistic, and supportive.
Focus on growth and decision-making.
"""
        }

        return base_rules + role_rules.get(self.role, "")
