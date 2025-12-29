"""
🏢 AGENTIC SOFTWARE HOUSE - Simple Builder
==========================================
Just tell us what to build in ONE sentence!

Usage: 
  python build.py "build me a snake game"
  python build.py "create a todo app with Flask"
  python build.py "make a calculator with GUI"
"""

import os
import sys
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import FileWriterTool, FileReadTool
from dotenv import load_dotenv

load_dotenv()

# =============================================================================
# 🧠 AI BRAIN (Groq - Fast & Reliable)
# =============================================================================

# Using smaller model to avoid rate limits
llm = LLM(
    model="groq/llama-3.1-8b-instant",  # Smaller, faster, less rate limiting
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

# =============================================================================
# 🛠️ TOOLS
# =============================================================================

file_writer = FileWriterTool()
file_reader = FileReadTool()

# =============================================================================
# 👥 THE TEAM
# =============================================================================

# 🎯 Project Manager - Takes your simple request and expands it
project_manager = Agent(
    role='Project Manager',
    goal='Transform a simple user request into a detailed project plan',
    backstory="""You are a brilliant PM who can take a vague one-liner like 
    "build me a snake game" and instantly understand what the user wants.
    You expand simple requests into clear, actionable specifications.
    You decide: what files to create, what features to include, what tech to use.""",
    verbose=True,
    llm=llm
)

# 💻 Developer - Writes the actual code
developer = Agent(
    role='Senior Developer',
    goal='Write complete, production-ready code based on the project plan',
    backstory="""You are a senior developer who writes clean, working code.
    You always save your code to files using FileWriterTool.
    You write COMPLETE code - never partial or placeholder code.
    You include proper error handling and comments.""",
    verbose=True,
    llm=llm,
    tools=[file_writer, file_reader]
)

# 🔍 QA - Reviews and validates
qa_engineer = Agent(
    role='QA Engineer',
    goal='Verify the code is complete and will actually run',
    backstory="""You check that the code is complete and functional.
    You verify all imports exist, all functions are implemented,
    and the code will run without errors.""",
    verbose=True,
    llm=llm,
    tools=[file_reader]
)

# =============================================================================
# 🎯 BUILD FUNCTION
# =============================================================================

def build(user_request: str):
    """
    Takes a simple request and builds the project.
    Example: build("make me a snake game")
    """
    
    print("\n" + "="*60)
    print("🏢 AGENTIC SOFTWARE HOUSE")
    print("="*60)
    print(f"\n📝 Your request: \"{user_request}\"\n")
    print("🚀 Starting build process...\n")
    
    # Task 1: PM expands the request
    task_plan = Task(
        description=f"""
        The user said: "{user_request}"
        
        Analyze this request and create a brief project plan:
        1. What exactly should be built?
        2. What technology/framework to use?
        3. What are the main features?
        4. What file(s) should be created?
        
        Keep it concise - max 15 lines. Focus on actionable details.
        """,
        expected_output="A brief, clear project plan with tech stack and features",
        agent=project_manager
    )
    
    # Task 2: Developer writes the code
    task_code = Task(
        description=f"""
        Based on the project plan, write COMPLETE working code.
        
        Original request: "{user_request}"
        
        REQUIREMENTS:
        1. Write the FULL code - no placeholders, no "TODO" comments
        2. Save the code to appropriate file(s) using FileWriterTool
        3. Include all necessary imports
        4. Add basic error handling
        5. The code must be runnable immediately
        
        Use FileWriterTool to save the file. Choose an appropriate filename
        based on what you're building (e.g., snake_game.py, calculator.py, app.py)
        """,
        expected_output="Complete, working code saved to file(s)",
        agent=developer
    )
    
    # Task 3: QA validates
    task_qa = Task(
        description="""
        Review the code that was written:
        
        1. Read the file(s) using FileReadTool
        2. Check that all imports are valid
        3. Check that all functions are complete (no TODO/pass)
        4. Verify the code will run
        
        If there are issues, list them clearly.
        If the code looks good, confirm it's ready to use.
        
        End with: "✅ READY TO RUN" or "❌ NEEDS FIXES: [list issues]"
        """,
        expected_output="QA validation result",
        agent=qa_engineer
    )
    
    # Assemble and run
    crew = Crew(
        agents=[project_manager, developer, qa_engineer],
        tasks=[task_plan, task_code, task_qa],
        verbose=True,
        process=Process.sequential
    )
    
    result = crew.kickoff()
    
    print("\n" + "="*60)
    print("🎉 BUILD COMPLETE!")
    print("="*60)
    print(f"\nResult: {result}\n")
    
    return result

# =============================================================================
# 🚀 MAIN
# =============================================================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""
🏢 AGENTIC SOFTWARE HOUSE
========================

Usage:
  python build.py "your request here"

Examples:
  python build.py "build me a snake game"
  python build.py "create a simple calculator"
  python build.py "make a todo list app"
  python build.py "build a weather app using an API"
        """)
    else:
        # Join all arguments as the request
        request = " ".join(sys.argv[1:])
        build(request)
