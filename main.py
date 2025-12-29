"""
🏢 AGENTIC SOFTWARE HOUSE - Generic Project Builder
====================================================
Run this script to build ANY software project using AI agents.
The Project Manager will ask what you want to build and orchestrate the team.

Usage: python main.py
"""

import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileReadTool, FileWriterTool
from dotenv import load_dotenv

load_dotenv()

# =============================================================================
# 🧠 AI BRAINS CONFIGURATION
# =============================================================================

print("\n" + "="*60)
print("🏢 AGENTIC SOFTWARE HOUSE")
print("   Your AI-Powered Development Team")
print("="*60 + "\n")

print("🔧 Initializing AI brains...")

# Fast Brain - for quick tasks (Groq - very fast and stable)
llm_fast = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.5
)

# Smart Brain - for complex tasks (Groq - same but with lower temperature for precision)
llm_smart = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

print("✅ AI brains ready (Powered by Groq)!\n")

# =============================================================================
# 🛠️ TOOLS INITIALIZATION
# =============================================================================

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
file_read_tool = FileReadTool()
file_write_tool = FileWriterTool()

# =============================================================================
# 👥 AGENT DEFINITIONS
# =============================================================================

print("👥 Assembling your development team...\n")

# 1. PROJECT MANAGER (The Boss) - Takes user input and creates tasks
project_manager = Agent(
    role='Project Manager',
    goal='Understand client requirements and create detailed task specifications for the development team',
    backstory="""You are a brilliant Project Manager with 15 years of experience leading software teams.
    You excel at taking vague client ideas and transforming them into crystal-clear, actionable tasks.
    You know exactly what each team member needs to succeed:
    - The Product Manager needs clear business requirements
    - The Architect needs technical constraints and preferences  
    - The Developer needs specific implementation details
    - The QA Engineer needs acceptance criteria
    
    You create comprehensive task descriptions that leave no room for ambiguity.""",
    verbose=True,
    allow_delegation=True,
    llm=llm_smart
)

# 2. PRODUCT MANAGER - Defines requirements
product_manager = Agent(
    role='Product Manager',
    goal='Transform project vision into detailed product requirements and user stories',
    backstory="""You are an experienced Product Manager who bridges business needs and technical execution.
    You create comprehensive PRDs (Product Requirements Documents) that cover:
    - User experience specifications
    - Feature requirements with acceptance criteria
    - Data formatting and display rules
    - Error handling expectations
    You ensure the final product delivers real value to users.""",
    verbose=True,
    allow_delegation=False,
    llm=llm_smart
)

# 3. SOFTWARE ARCHITECT - Designs the solution
architect = Agent(
    role='Software Architect',
    goal='Design robust, scalable technical architectures with the best technology choices',
    backstory="""You are a visionary Software Architect who stays current with the latest technologies.
    You research frameworks, libraries, and best practices to make data-driven decisions.
    Your designs include:
    - Technology stack recommendations
    - Code structure and patterns
    - API designs and data flows
    - Error handling strategies
    You never guess - you research and validate your choices.""",
    verbose=True,
    allow_delegation=False,
    llm=llm_smart,
    tools=[search_tool, scrape_tool]
)

# 4. SENIOR DEVELOPER - Writes the code
senior_developer = Agent(
    role='Senior Developer',
    goal='Write production-quality, clean, and efficient code that implements the specifications exactly',
    backstory="""You are a Senior Developer with expertise in Python, web development, and modern frameworks.
    You write code that is:
    - Clean and readable
    - Well-documented
    - Properly error-handled
    - Following best practices
    You use the FileWriterTool to save your code to actual files.
    You NEVER use deprecated or basic functions when better alternatives exist.""",
    verbose=True,
    allow_delegation=False,
    llm=llm_smart,  # Changed to smart brain for better code quality
    tools=[file_read_tool, file_write_tool]
)

# 5. QA ENGINEER - Validates the output
qa_engineer = Agent(
    role='QA Engineer',
    goal='Ensure all code meets quality standards and requirements before delivery',
    backstory="""You are a meticulous QA Engineer who catches issues others miss.
    You verify:
    - Code follows the specifications
    - No forbidden patterns are used
    - Error handling is implemented
    - The code will actually run
    You create detailed QA reports and don't approve anything that's not production-ready.""",
    verbose=True,
    allow_delegation=False,
    llm=llm_smart,
    tools=[file_read_tool]
)

print("✅ Team assembled: Project Manager, Product Manager, Architect, Developer, QA Engineer\n")

# =============================================================================
# 🎯 DYNAMIC TASK GENERATION
# =============================================================================

def create_tasks_for_project(project_description: str):
    """
    Creates dynamic tasks based on the user's project description.
    The Project Manager analyzes the request and generates specific tasks for each team member.
    """
    
    # Task 0: Project Manager analyzes the request and creates a project plan
    task_project_planning = Task(
        description=f"""
        A client has requested the following project:
        
        === CLIENT REQUEST ===
        {project_description}
        === END REQUEST ===
        
        As the Project Manager, analyze this request and create a detailed project plan.
        
        Your output must include:
        
        1. **PROJECT SUMMARY**: A clear 2-3 sentence summary of what we're building
        
        2. **KEY FEATURES**: List the main features/components needed
        
        3. **TECHNICAL CONSIDERATIONS**: 
           - Recommended frameworks/libraries
           - Any specific technical requirements mentioned
           - Data sources if applicable
        
        4. **TEAM INSTRUCTIONS**: Specific guidance for each team member:
           - What the Product Manager should focus on
           - What the Architect should research/design
           - What the Developer must implement
           - What the QA Engineer should verify
        
        5. **SUCCESS CRITERIA**: How we'll know the project is complete
        
        Be specific and actionable. The team will use your plan to execute the project.
        """,
        expected_output="A comprehensive project plan with specific instructions for each team member",
        agent=project_manager
    )
    
    # Task 1: Product Manager creates requirements
    task_requirements = Task(
        description=f"""
        Based on the Project Manager's plan, create a detailed Product Requirements Document (PRD).
        
        Original client request for context:
        {project_description}
        
        Your PRD must include:
        
        1. **USER EXPERIENCE REQUIREMENTS**
           - Who is the target user?
           - What should the UI look and feel like?
           - Key user flows and interactions
        
        2. **FUNCTIONAL REQUIREMENTS**
           - List every feature with acceptance criteria
           - Data inputs and outputs
           - Business logic rules
        
        3. **DATA & FORMATTING RULES**
           - How should numbers be displayed?
           - Date formats
           - Error messages
        
        4. **TECHNICAL CONSTRAINTS**
           - Any frameworks that MUST be used
           - Any patterns that are FORBIDDEN
           - Performance requirements
        
        5. **ACCEPTANCE CHECKLIST**
           - A clear checklist for QA to verify
        
        Be extremely specific - the developer will implement exactly what you specify.
        """,
        expected_output="A comprehensive PRD with detailed specifications and acceptance criteria",
        agent=product_manager
    )
    
    # Task 2: Architect designs the solution
    task_architecture = Task(
        description=f"""
        Based on the requirements, design the complete technical architecture.
        
        Original client request for context:
        {project_description}
        
        Your Technical Design Document must include:
        
        1. **TECHNOLOGY STACK**
           - List ALL required imports/libraries
           - Justify each choice
           - Specify versions if critical
        
        2. **CODE ARCHITECTURE**
           - File structure
           - Main functions/classes needed
           - Data flow diagrams (text-based)
        
        3. **IMPLEMENTATION PATTERNS**
           - Code snippets for complex parts
           - Helper functions to create
           - Error handling patterns
        
        4. **FORBIDDEN PATTERNS**
           - What the developer must NOT use
           - Why these are forbidden
        
        5. **CONFIGURATION**
           - Environment variables needed
           - Default settings
        
        Research current best practices if needed. Provide code templates the developer can use directly.
        """,
        expected_output="A complete technical design with code templates and architecture decisions",
        agent=architect
    )
    
    # Task 3: Developer implements the code
    task_development = Task(
        description=f"""
        Implement the complete solution based on the requirements and architecture.
        
        Original client request for context:
        {project_description}
        
        CRITICAL INSTRUCTIONS:
        
        1. **FILE OUTPUT**
           - Use FileWriterTool to save your code
           - Create all necessary files
           - The main file should be runnable
        
        2. **CODE QUALITY**
           - Clean, readable code
           - Proper comments and docstrings
           - Consistent formatting
        
        3. **FOLLOW THE SPECS**
           - Implement EXACTLY what was specified
           - Use the recommended libraries
           - Avoid forbidden patterns
        
        4. **ERROR HANDLING**
           - Wrap risky operations in try/except
           - Provide user-friendly error messages
           - Never let the app crash unexpectedly
        
        5. **TESTING**
           - Ensure the code runs without errors
           - Verify all features work
        
        Write complete, production-ready code. Do not leave TODOs or placeholders.
        """,
        expected_output="Complete, working code files saved to disk using FileWriterTool",
        agent=senior_developer
    )
    
    # Task 4: QA validates everything
    task_qa = Task(
        description=f"""
        Perform comprehensive quality assurance on all generated code.
        
        Original client request for context:
        {project_description}
        
        QA CHECKLIST:
        
        1. **CODE REVIEW**
           - Read all generated files using FileReadTool
           - Verify code syntax is correct
           - Check for obvious bugs
        
        2. **REQUIREMENTS COMPLIANCE**
           - Does the code implement all required features?
           - Are forbidden patterns avoided?
           - Is error handling implemented?
        
        3. **QUALITY STANDARDS**
           - Is the code clean and readable?
           - Are there proper comments?
           - Is the structure logical?
        
        4. **RUNABILITY CHECK**
           - Would this code run without errors?
           - Are all imports available?
           - Are there any missing dependencies?
        
        CREATE A DETAILED QA REPORT:
        - PASS/FAIL for each category
        - Specific issues found (with line numbers)
        - Recommended fixes
        - Final verdict: APPROVED or REJECTED
        
        If rejected, clearly explain what needs to be fixed.
        """,
        expected_output="A detailed QA report with PASS/FAIL status and final APPROVED/REJECTED verdict",
        agent=qa_engineer
    )
    
    return [task_project_planning, task_requirements, task_architecture, task_development, task_qa]

# =============================================================================
# 🚀 MAIN EXECUTION
# =============================================================================

def main():
    """Main function to run the Agentic Software House."""
    
    print("="*60)
    print("💬 WHAT WOULD YOU LIKE TO BUILD?")
    print("="*60)
    print("\nDescribe your project in detail. The more specific you are,")
    print("the better results you'll get. Include:")
    print("  • What the application should do")
    print("  • Target users")
    print("  • Preferred technologies (if any)")
    print("  • UI/UX preferences")
    print("  • Any specific features\n")
    print("Type your description (press Enter twice when done):")
    print("-"*60)
    
    # Collect multi-line input
    lines = []
    while True:
        line = input()
        if line == "":
            if lines and lines[-1] == "":
                break
            lines.append(line)
        else:
            lines.append(line)
    
    project_description = "\n".join(lines).strip()
    
    if not project_description:
        print("\n❌ No project description provided. Exiting.")
        return
    
    print("\n" + "="*60)
    print("📋 PROJECT RECEIVED")
    print("="*60)
    print(f"\n{project_description}\n")
    
    # Confirm with user
    confirm = input("🚀 Start building? (yes/no): ").strip().lower()
    if confirm not in ['yes', 'y', 'כן']:
        print("\n❌ Build cancelled.")
        return
    
    print("\n" + "="*60)
    print("🏗️  STARTING BUILD PROCESS")
    print("="*60)
    print("\nYour AI team is now working on your project...")
    print("This may take several minutes depending on complexity.\n")
    
    # Create dynamic tasks based on user input
    tasks = create_tasks_for_project(project_description)
    
    # Assemble the crew
    crew = Crew(
        agents=[project_manager, product_manager, architect, senior_developer, qa_engineer],
        tasks=tasks,
        verbose=True,
        process=Process.sequential
    )
    
    # Execute!
    try:
        result = crew.kickoff()
        
        print("\n" + "="*60)
        print("🎉 PROJECT COMPLETE!")
        print("="*60)
        print("\n📋 FINAL SUMMARY:")
        print("-"*60)
        print(result)
        print("-"*60)
        print("\n✅ Your project has been built!")
        print("📁 Check your project folder for the generated files.")
        
    except Exception as e:
        print("\n" + "="*60)
        print("❌ BUILD FAILED")
        print("="*60)
        print(f"\nError: {str(e)}")
        print("\nPlease check your API keys and try again.")

if __name__ == "__main__":
    main()