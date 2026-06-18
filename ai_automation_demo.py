import random

# --- Traditional Rule-Based Automation Example ---
def traditional_automation(input_data):
    """Simulates a traditional rule-based system.
    Always produces the same output for the same input.
    """
    if "urgent" in input_data.lower():
        return "High Priority Task"
    elif "report" in input_data.lower():
        return "Generate Standard Report"
    else:
        return "Process Standard Request"

# --- AI-Powered Automation Example ---
class AIAutomation:
    def __init__(self):
        # In a real AI, this would be a trained model.
        # Here, we simulate learning and context-awareness with randomness.
        self.learned_patterns = {
            "urgent": ["Immediate Action Required", "Critical Alert", "Expedite Processing"],
            "report": ["Compile Data for Report", "Analyze Trends", "Summarize Findings"],
            "standard": ["Handle Request", "Log Activity", "Provide Information"]
        }
        self.context_memory = [] # Simulate remembering past interactions

    def process_input(self, input_data):
        """Simulates AI-powered automation.
        Can produce different, context-aware outputs for similar inputs.
        """
        lower_input = input_data.lower()
        category = "standard"

        if "urgent" in lower_input:
            category = "urgent"
        elif "report" in lower_input:
            category = "report"

        # Simulate AI's ability to adapt and choose a slightly different response
        # based on learned patterns and simulated context.
        possible_responses = self.learned_patterns.get(category, self.learned_patterns["standard"])
        chosen_response = random.choice(possible_responses)

        # Simulate context awareness: if we've seen 'urgent' before, maybe be more direct
        if "urgent" in self.context_memory and category == "urgent":
            chosen_response = "Re-prioritize: Urgent Task - Previous context noted."

        self.context_memory.append(category) # Update context
        return chosen_response

# --- Demonstration ---
print("--- Traditional Automation ---")
inputs = ["Process customer request", "Urgent: System Down", "Generate monthly report", "Another request"]

for item in inputs:
    result = traditional_automation(item)
    print(f"Input: '{item}' -> Output: '{result}'")

print("\n--- AI-Powered Automation ---")

ai_system = AIAutomation()

# Run multiple times to show potential for different outputs
for _ in range(2):
    for item in inputs:
        result = ai_system.process_input(item)
        print(f"Input: '{item}' -> Output: '{result}'")
    print("---") # Separator for multiple runs

print("\nNotice how AI can provide varied responses for similar inputs, unlike the fixed output of traditional methods.")
