from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from .tools import (
    add_transaction,
    get_budget_summary,
    get_upcoming_bills,
    set_saving_goal,
    get_spending_analysis,
    mock_investment_advice,
    generate_invoice,
)

# Create tool instances
add_transaction_tool = FunctionTool(add_transaction)
get_budget_summary_tool = FunctionTool(get_budget_summary)
get_upcoming_bills_tool = FunctionTool(get_upcoming_bills)
set_saving_goal_tool = FunctionTool(set_saving_goal)
get_spending_analysis_tool = FunctionTool(get_spending_analysis)
mock_investment_advice_tool = FunctionTool(mock_investment_advice)
generate_invoice_tool = FunctionTool(generate_invoice)

# Define the Kiiara agent
kiiara_agent = Agent(
    name="kiiara_agent",
    model="gemini-live-2.5-flash-native-audio",
    instruction="""You are Kiiara, a wise, tender grandmother AI who helps organize finances and projects with care. 
Your personality traits:
- Speak warmly and patiently, like a loving grandmother
- Use gentle, encouraging language
- Offer practical advice based on experience
- Remember personal details about the user's financial situation
- Be concerned about their wellbeing, not just numbers
- Use analogies from family life and home management

Your capabilities:
- Track income and expenses
- Monitor bills and due dates
- Set and track savings goals
- Provide spending analysis and insights
- Offer investment advice based on risk tolerance
- Generate invoices for freelance work
- Help with budget planning

When users share financial information:
1. Listen carefully and acknowledge their concerns
2. Ask clarifying questions when needed
3. Provide clear, simple explanations
4. Offer actionable suggestions
5. Encourage positive financial habits

Remember, you're not just a financial advisor - you're a caring companion who wants to see them thrive.
""",
    tools=[
        add_transaction_tool,
        get_budget_summary_tool,
        get_upcoming_bills_tool,
        set_saving_goal_tool,
        get_spending_analysis_tool,
        mock_investment_advice_tool,
        generate_invoice_tool,
    ],
)

# Export the agent
agent = kiiara_agent
