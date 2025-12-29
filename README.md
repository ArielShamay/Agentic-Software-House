# 🏢 Agentic Software House

> **מערכת AI שבונה תוכנה מפרומפט אחד פשוט**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-green)
![Groq](https://img.shields.io/badge/LLM-Groq-orange)

---

## 🎯 מה זה?

**Agentic Software House** היא מערכת **ורסטילית** שמייצרת קוד מוכן להרצה מפרומפט טקסטואלי אחד בלבד.

במקום לכתוב קוד בעצמך, פשוט תגיד למערכת מה לבנות:

```bash
python build.py "build me a snake game"
python build.py "create a calculator with GUI"
python build.py "make a todo list app"
```

והמערכת תבנה את הפרויקט המלא עבורך! 🚀

---

## 🧠 איך זה עובד?

המערכת בנויה על **צוות של סוכני AI**, כל אחד עם תפקיד ייחודי ו"מוח" (מודל LLM) מותאם:

```
📝 הפרומפט שלך
      ↓
🎯 Project Manager  ← מבין את הבקשה ומתכנן
      ↓
💻 Senior Developer ← כותב קוד מלא ושומר קבצים
      ↓
🔍 QA Engineer      ← בודק שהקוד עובד
      ↓
✅ קבצים מוכנים להרצה!
```

### 👥 הסוכנים (Agents)

| סוכן | תפקיד | מה הוא עושה |
|------|--------|-------------|
| **Project Manager** | 🎯 מנהל | מקבל בקשה פשוטה ומפרק אותה לתוכנית עבודה מפורטת |
| **Product Manager** | 📋 מוצר | מגדיר דרישות, UI/UX, ו-acceptance criteria |
| **Software Architect** | 🏗️ ארכיטקט | מתכנן את המבנה הטכני, בוחר טכנולוגיות |
| **Senior Developer** | 💻 מפתח | כותב קוד מלא, שומר קבצים, מממש את הכל |
| **QA Engineer** | 🔍 בודק | מוודא שהקוד שלם, תקין, ומוכן להרצה |

### 🧠 המוחות (LLM Brains)

המערכת תומכת במספר "מוחות" שונים:

```python
# מוח מהיר - למשימות פשוטות
llm_fast = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.5  # יותר יצירתי
)

# מוח חכם - למשימות מורכבות
llm_smart = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.3  # יותר מדויק
)
```

| פרמטר | הסבר |
|-------|------|
| **model** | המודל של ה-AI (גודל, יכולות) |
| **temperature** | 0.1=מדויק, 1.0=יצירתי |

---

## 🚀 התקנה והפעלה

### 1. התקנת Dependencies

```bash
pip install crewai crewai-tools python-dotenv
```

### 2. הגדרת API Key

צור קובץ `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

קבל API Key חינמי מ: https://console.groq.com/

### 3. הרצה

```bash
# הגרסה הפשוטה - פרומפט אחד
python build.py "build me a snake game"

# הגרסה האינטראקטיבית - שיחה עם המערכת
python main.py
```

---

## 📁 מבנה הפרויקט

```
📂 agentic-software-house/
├── 📄 build.py          # ⚡ הגרסה הפשוטה - פרומפט אחד
├── 📄 main.py           # 🏢 הגרסה המלאה - אינטראקטיבית
├── 📄 agents.py         # 👥 הגדרות הסוכנים
├── 📄 tasks.py          # 📋 משימות לפרויקט ספציפי
├── 📄 .env              # 🔑 API Keys
└── 📄 README.md         # 📖 התיעוד הזה
```

### הקבצים העיקריים:

| קובץ | תיאור |
|------|--------|
| `build.py` | **הכי פשוט** - פרומפט אחד → קוד מוכן |
| `main.py` | גרסה מלאה עם 5 סוכנים ואינטראקציה |
| `agents.py` | הגדרות של כל הסוכנים והמוחות שלהם |
| `tasks.py` | דוגמה למשימות מפורטות (ValueInvestor Pro) |

---

## 💡 דוגמאות שימוש

### דוגמה 1: משחק נחש
```bash
python build.py "build a snake game with pygame"
```
**תוצאה:** קובץ `snake_game.py` מוכן להרצה

### דוגמה 2: מחשבון עם GUI
```bash
python build.py "create a calculator with GUI using tkinter"
```
**תוצאה:** 3 קבצים - `calculator.py`, `gui.py`, `operations.py`

### דוגמה 3: אפליקציית Todo
```bash
python build.py "make a todo list app with Flask"
```
**תוצאה:** אפליקציית web מלאה

---

## ⚙️ קונפיגורציה מתקדמת

### החלפת מודל AI

ב-`build.py` או `agents.py`:

```python
# Groq (מהיר וחינמי)
llm = LLM(model="groq/llama-3.3-70b-versatile", ...)

# OpenAI (איכותי יותר, בתשלום)
llm = LLM(model="gpt-4", ...)

# Anthropic Claude
llm = LLM(model="claude-3-opus", ...)
```

### התאמת Temperature

```python
temperature=0.1  # מאוד מדויק, אותה תשובה כל פעם
temperature=0.3  # מדויק עם קצת גמישות (מומלץ לקוד)
temperature=0.7  # יצירתי (מומלץ לטקסט)
temperature=1.0  # מאוד יצירתי, תוצאות מגוונות
```

---

## 🔧 הרחבת המערכת

### הוספת סוכן חדש

```python
from crewai import Agent

# סוכן חדש - מעצב UI
ui_designer = Agent(
    role='UI Designer',
    goal='Create beautiful user interfaces',
    backstory='You are a talented UI designer...',
    verbose=True,
    llm=llm_smart
)
```

### הוספת כלי חדש

```python
from crewai_tools import SerperDevTool

# כלי חיפוש באינטרנט
search_tool = SerperDevTool()

# הוספה לסוכן
architect = Agent(
    ...,
    tools=[search_tool]
)
```

---

## 📊 ארכיטקטורת המערכת

```
┌─────────────────────────────────────────────────────────────┐
│                    🏢 AGENTIC SOFTWARE HOUSE                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   📝 User Prompt                                            │
│        ↓                                                    │
│   ┌─────────────────────────────────────────────────────┐   │
│   │              🧠 CrewAI Framework                     │   │
│   │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌────────┐  │   │
│   │  │   PM    │→ │  Dev    │→ │   QA    │→ │ Output │  │   │
│   │  │  Agent  │  │  Agent  │  │  Agent  │  │ Files  │  │   │
│   │  └────┬────┘  └────┬────┘  └────┬────┘  └────────┘  │   │
│   │       │            │            │                    │   │
│   │       ↓            ↓            ↓                    │   │
│   │  ┌─────────────────────────────────────────────┐    │   │
│   │  │           🧠 LLM (Groq/OpenAI)              │    │   │
│   │  │    Llama 3.3 70B / GPT-4 / Claude          │    │   │
│   │  └─────────────────────────────────────────────┘    │   │
│   └─────────────────────────────────────────────────────┘   │
│        ↓                                                    │
│   📁 Generated Code Files                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚠️ מגבלות ידועות

| מגבלה | פתרון |
|-------|--------|
| **Rate Limiting** | Groq חינמי מוגבל ל-12K tokens/דקה. חכה דקה בין הרצות |
| **קוד ארוך** | פרויקטים מורכבים מאוד עלולים להיחתך. פצל לבקשות קטנות |
| **תלות באינטרנט** | צריך חיבור לאינטרנט לגישה ל-API |

---

## 🤝 תרומה לפרויקט

רוצה לתרום? מעולה!

1. Fork את הפרויקט
2. צור branch חדש (`git checkout -b feature/amazing-feature`)
3. Commit השינויים (`git commit -m 'Add amazing feature'`)
4. Push ל-branch (`git push origin feature/amazing-feature`)
5. פתח Pull Request

---

## 📜 רישיון

MIT License - השתמש בחופשיות!

---

## 🙏 תודות

- [CrewAI](https://github.com/joaomdmoura/crewAI) - Framework לסוכני AI
- [Groq](https://groq.com/) - API מהיר ל-LLM
- [LangChain](https://langchain.com/) - כלים ל-AI

---

<div align="center">

**נבנה עם ❤️ ו-AI**

⭐ אם אהבת את הפרויקט, תן לנו כוכב! ⭐

</div>
