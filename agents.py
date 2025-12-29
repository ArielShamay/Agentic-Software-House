import os
from crewai import Agent, LLM  # 👈 שינוי חשוב: מייבאים את LLM מכאן
from dotenv import load_dotenv
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileReadTool, FileWriterTool

load_dotenv()

# --- הגדרת המוחות באמצעות Groq (מהיר ויציב) ---

# 1. המוח המהיר (Fast Brain) - Groq
llm_fast = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.5
)

# 2. המוח החכם (Smart Brain) - Groq עם temperature נמוך יותר
llm_smart = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

# --- אין צורך בבדיקה ידנית (print) כאן, הסוכנים יעשו את זה ---

print("👷 Building the Product Manager...")

# Defining the Product Manager Agent
product_manager = Agent(
    role='Product Manager',
    goal='Analyze customer requirements and define the project scope clearly',
    backstory="""You are an experienced Product Manager at a leading software firm. 
    Your expertise lies in taking high-level customer ideas and transforming them 
    into precise requirement documents that developers can work with. 
    You prioritize ensuring the final product meets the business needs.""",
    verbose=True,            
    allow_delegation=False,   
    llm=llm_smart            # עכשיו הוא מקבל אובייקט שהוא מבין!
)

print(f"✅ Agent '{product_manager.role}' created successfully!")
print("🏗️  Initializing Tools & Building the Architect...")

# Initialize the tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Defining the Software Architect Agent
architect = Agent(
    role='Software Architect',
    goal='Research and design a robust, scalable technical architecture',
    backstory="""You are a visionary Senior Software Architect.
    You love to find the latest and greatest technologies (libraries, frameworks)
    that fit the specific needs of the project.
    You don't just guess; you search the web, read documentation, and make
    data-driven decisions about the tech stack.""",
    verbose=True,
    allow_delegation=False, 
    llm=llm_smart,          
    tools=[search_tool, scrape_tool] 
)

print(f"✅ Agent '{architect.role}' created successfully!")
print("💻 Initializing File Tools & Building the Senior Developer...")

# Initialize file management tools
file_read_tool = FileReadTool()
file_write_tool = FileWriterTool() # וידאנו שזה השם הנכון

# Defining the Senior Developer Agent
senior_developer = Agent(
    role='Senior Developer',
    goal='Write efficient, clean, and error-free Python code based on specifications',
    backstory="""You are a Senior Python Developer with years of experience.
    You take the architectural design and translate it into working code.
    You care deeply about code quality, clean syntax, and proper error handling.
    You are the only one who actually writes the .py files to the disk.""",
    verbose=True,
    allow_delegation=False, 
    llm=llm_fast,           # משתמש במוח המהיר של Cerebras!
    tools=[file_read_tool, file_write_tool] 
)

print(f"✅ Agent '{senior_developer.role}' created successfully!")
print("🕵️  Building the QA Engineer...")

# Defining the QA Engineer Agent
qa_engineer = Agent(
    role='Software Quality Assurance Engineer',
    goal='Ensure the code is bug-free and meets design standards',
    backstory="""You are a meticulous QA Engineer. 
    You have an eagle eye for detail. You check the code produced by the developer,
    looking for logic errors, syntax issues, or missing requirements.
    You don't accept "good enough" - you want perfection.""",
    verbose=True,
    allow_delegation=False,  
    llm=llm_smart,          
    tools=[file_read_tool, file_write_tool]
)

print(f"✅ Agent '{qa_engineer.role}' created successfully!")