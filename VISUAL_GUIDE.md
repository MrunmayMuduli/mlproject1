# 🎨 CareerPath AI - Visual Guide

## 🌟 User Journey

```
START
  ↓
┌─────────────────────────────────────┐
│   Welcome + Disclaimer              │
│   ⚠️ Clear about limitations        │
└────────────┬────────────────────────┘
             ↓
┌─────────────────────────────────────┐
│   User Input                        │
│   📍 Current Role                   │
│   📅 Years of Experience            │
│   🛠️  Skills (comma-separated)      │
│   🎯 Target Role                    │
└────────────┬────────────────────────┘
             ↓
┌─────────────────────────────────────┐
│   Analysis & Generation             │
│   🧠 LLM processes input            │
│   📊 Rule engine matches skills     │
│   ⚙️  Combines for roadmap          │
└────────────┬────────────────────────┘
             ↓
┌─────────────────────────────────────┐
│   Output: Career Roadmap            │
│   📈 Skills Gap Analysis            │
│   📅 6-Month Plan                   │
│   📅 12-Month Plan                  │
│   📅 24-Month Plan                  │
│   💡 Resources & Certifications     │
│   🚀 Motivational Message           │
└────────────┬────────────────────────┘
             ↓
┌─────────────────────────────────────┐
│   Output: Action Plan               │
│   ✅ 6 Concrete Steps               │
│   📆 Week-by-week Timeline          │
│   🎯 Expected Outcomes              │
└────────────┬────────────────────────┘
             ↓
┌─────────────────────────────────────┐
│   Governance Summary                │
│   📍 How it was generated           │
│   ⚠️  Limitations acknowledged      │
│   ✓ Recommendations                │
└────────────┬────────────────────────┘
             ↓
           END
        (Save/Export)
```

---

## 🧠 System Architecture

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           USER INTERFACE LAYER               ┃
┃  ┌──────────────────────────────────────┐   ┃
┃  │  CLI (app.py)  │  Web UI (Streamlit) │   ┃
┃  └──────────────────────────────────────┘   ┃
┗━━━━━━━━━━━━┬━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
             │
┏━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        INPUT VALIDATION LAYER               ┃
┃  - Check non-empty                          ┃
┃  - Normalize text                           ┃
┃  - Extract key info                         ┃
┗━━━━━━━━━━━━┬━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
             │
      ┌──────┴──────┐
      │             │
      ↓             ↓
  ┌─────────┐  ┌──────────────┐
  │   RULE  │  │  LLM LAYER   │
  │ ENGINE  │  │  (Groq API)  │
  │         │  │              │
  │Skill    │  │Llama-3-8B    │
  │Matching │  │Temperature:  │
  │Database │  │0.7           │
  └────┬────┘  └───────┬──────┘
       │               │
       └───────┬───────┘
               │
    ┏━━━━━━━━━▼━━━━━━━━━┓
    ┃ ROADMAP GENERATOR  ┃
    ┃ - Combine outputs  ┃
    ┃ - Format sections  ┃
    ┃ - Add structure    ┃
    ┗────────┬───────────┘
             │
    ┏━━━━━━━━▼━━━━━━━━━┓
    ┃ ACTION PLAN GEN   ┃
    ┃ - Extract steps   ┃
    ┃ - Timeline        ┃
    ┃ - Milestones      ┃
    ┗────────┬───────────┘
             │
    ┏━━━━━━━━▼━━━━━━━━━┓
    ┃ GOVERNANCE LAYER  ┃
    ┃ - Disclaimers     ┃
    ┃ - Bias warnings   ┃
    ┃ - Transparency    ┃
    ┃ - Recommendations │
    ┗────────┬───────────┘
             │
           OUTPUT
```

---

## 🎯 Skill Matching Process

```
┌─────────────────────────────────┐
│  User Target Role Input         │
│  "Data Scientist"               │
└──────────────┬──────────────────┘
               │
               ↓
┌─────────────────────────────────┐
│  Rule Engine Lookup             │
│  Search SKILL_MAPPING dict      │
└──────────────┬──────────────────┘
               │
               ↓
    ┌──────────────────────────┐
    │  Target Role Found? ✓    │
    └──────────────┬───────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
       YES                   NO
        │                     │
        ↓                     ↓
   ┌────────────┐    ┌──────────────┐
   │Use Mapped  │    │LLM-Only Mode │
   │Skills Data │    │(No rules)    │
   └────────────┘    └──────────────┘
        │                     │
        └──────────┬──────────┘
                   │
                   ↓
         ┌──────────────────┐
         │ Send to LLM with │
         │ Skill Context    │
         └──────────────────┘
```

---

## 📊 Data Transformation Flow

```
INPUT
  ├─ Current Role: "Mechanical Engineer"
  ├─ Experience: 5 years
  ├─ Skills: "CAD, MATLAB, Problem Solving"
  └─ Target: "Data Scientist"
         │
         ↓ [VALIDATION]
  ├─ Role normalized ✓
  ├─ Experience: 5 ✓
  ├─ Skills split → ["CAD", "MATLAB", "Problem Solving"] ✓
  └─ Target normalized ✓
         │
         ↓ [RULE ENGINE LOOKUP]
  ├─ Target found: Data Scientist ✓
  ├─ Required Skills: [Python, SQL, Statistics, ML, Visualization]
  ├─ Soft Skills: [Communication, Problem Solving, ...]
  ├─ Certifications: [Google Data Analytics, AWS ML, ...]
  └─ Transition Roles: [Data Analyst, ML Engineer, ...]
         │
         ↓ [LLM CALL]
  ├─ System: Career coach prompt
  ├─ User: Combined context + rule data
  ├─ Model: llama3-8b-8192
  ├─ Temperature: 0.7
  └─ Response: Full career roadmap
         │
         ↓ [FORMATTING]
  ├─ Parse response sections
  ├─ Extract 6/12/24 month plans
  ├─ Add markdown formatting
  ├─ Structure for display
  └─ Add disclaimers
         │
         ↓ [SECOND LLM CALL]
  ├─ Input: Roadmap output
  ├─ Request: 6-month action plan
  ├─ Model: Same (llama3-8b-8192)
  └─ Response: Step-by-step actions
         │
         ↓ [GOVERNANCE OVERLAY]
  ├─ Add disclaimer box
  ├─ Add limitations warning
  ├─ Add recommendations
  ├─ Explain methodology
  └─ Suggest human validation
         │
        ↓
OUTPUT
  ├─ Career Roadmap (formatted)
  ├─ 6-Month Action Plan (formatted)
  ├─ Governance Notes (formatted)
  └─ Resources & Recommendations
```

---

## 🛡️ Governance Decision Tree

```
                    START
                      │
                      ↓
            ┌─────────────────────┐
            │ Generate Content    │
            │ using LLM           │
            └──────────┬──────────┘
                       │
                       ↓
         ┌─────────────────────────┐
         │ Over-promise check?     │
         │ (e.g., "guaranteed to") │
         └────────┬────────────────┘
                  │
          ┌───────┴────────┐
         YES               NO
          │                │
          ↓                ↓
    [FLAG]            Continue
    Revise text            │
    Remove             ┌───┴────────────┐
    absolutes          │ Bias check?    │
                       │ (regional,     │
                       │  gender, etc)  │
                       └───┬────────────┘
                           │
                   ┌───────┴────────┐
                  YES              NO
                   │               │
                   ↓               ↓
              [NOTE]           Continue
              Mention              │
              validation       ┌───┴──────────────┐
              needed           │ Privacy check?   │
                               │ (personal info)  │
                               └───┬──────────────┘
                                   │
                           ┌───────┴────────┐
                          YES              NO
                           │               │
                           ↓               ↓
                    [REDACT]           Continue
                    Remove/Hash            │
                    personal               ↓
                    details         ┌──────────────────┐
                                    │ Add Disclaimers  │
                                    │ Add Governance   │
                                    │ Notes            │
                                    │ Add Resources    │
                                    └────────┬─────────┘
                                             │
                                             ↓
                                        OUTPUT
```

---

## 🎨 UI Layouts

### CLI Version
```
═══════════════════════════════════════════════════════════
🚀 CAREERPATH AI - Personalized Career Advice Generator
═══════════════════════════════════════════════════════════
⚠️ DISCLAIMER - CareerPath AI
This tool provides general career guidance based on AI...
═══════════════════════════════════════════════════════════

📍 What is your current role? > Mechanical Engineer
📅 Years of experience: > 5
🛠️  Your top 3-5 skills (comma-separated): > CAD, MATLAB, Problem Solving
🎯 What's your target role? > Data Scientist

⏳ Generating your personalized career roadmap...

═══════════════════════════════════════════════════════════
📊 YOUR PERSONALIZED CAREER ROADMAP
═══════════════════════════════════════════════════════════
[ROADMAP CONTENT HERE]

═══════════════════════════════════════════════════════════
✅ YOUR 6-MONTH ACTION PLAN
═══════════════════════════════════════════════════════════
[ACTION PLAN CONTENT HERE]
```

### Streamlit Version
```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  🚀 CareerPath AI                                       │
│  Personalized Career Advice Generator                  │
│                                                          │
│  ┌────────────────┐          ┌────────────────────┐    │
│  │  📋 Your Info  │          │  🎯 Your Goal     │    │
│  │                │          │                    │    │
│  │ Current Role   │          │ Target Role       │    │
│  │ [_________]    │          │ [Dropdown]        │    │
│  │                │          │                    │    │
│  │ Experience     │          │ Timeline          │    │
│  │ [====|------ ] │          │ ◉ Realistic       │    │
│  │                │          │ ○ Aggressive      │    │
│  │ Skills         │          │                    │    │
│  │ [_________]    │          │ [Generate Button] │    │
│  │                │          │                    │    │
│  └────────────────┘          └────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────┐        │
│  │ 📊 Your Career Roadmap                     │        │
│  │ [Roadmap content here]                     │        │
│  │                                             │        │
│  └─────────────────────────────────────────────┘        │
│                                                          │
│  ┌─────────────────────────────────────────────┐        │
│  │ ✅ Your 6-Month Action Plan                │        │
│  │ [Action plan content here]                 │        │
│  │                                             │        │
│  └─────────────────────────────────────────────┘        │
│                                                          │
└──────────────────────────────────────────────────────────┘
    SIDEBAR: ⚠️ DISCLAIMER, Config Options, Examples
```

---

## 📈 Timeline Visualization

```
START (Today)
    │
    ├─ 0-3 months
    │  ├─ Week 1-4: Python Fundamentals
    │  │  └─ [████████░░░░] 40% complete
    │  ├─ Week 5-8: SQL & Data
    │  │  └─ [██████░░░░░░░░] 25% complete
    │  └─ Week 9-12: Statistics
    │     └─ [████░░░░░░░░░░░░] 20% complete
    │
    ├─ 3-6 months
    │  ├─ Build ML projects
    │  ├─ Learn scikit-learn
    │  └─ First Kaggle competition
    │
    ├─ 6-12 months
    │  ├─ Deep learning
    │  ├─ Advanced ML projects
    │  └─ Network with DS teams
    │
    ├─ 12-18 months
    │  ├─ Interview practice
    │  ├─ Build portfolio
    │  └─ Reach out to companies
    │
    └─ 18-24 months
       └─ Target role achieved! 🎉
```

---

## 🔄 Skill Bridge Visualization

```
CURRENT STATE              TRANSITION              TARGET STATE
(Mechanical Eng)            (Learning Path)         (Data Scientist)

┌─────────────┐                                 ┌─────────────┐
│ CAD         │◄─────────────────────────────►  │ Python      │
│ MATLAB      │  Bridge: System thinking        │ R           │
│ Physics     │         + Problem solving       │ SQL         │
│ Simulation  │         = Strong foundation!    │ Machine Lng │
└─────────────┘                                 └─────────────┘

OVERLAPPING SKILLS:
├─ Problem Solving        ✓ Transfer directly
├─ Systems Thinking       ✓ Transfer directly
├─ Technical Analysis     ✓ Similar to data analysis
├─ Project Management     ✓ Valuable + transferable
└─ Communication          ✓ Always needed

NEW SKILLS TO BUILD:
├─ Python Programming     🎯 Focus area #1 (3 months)
├─ Statistics/Probability 🎯 Focus area #2 (2 months)
├─ Machine Learning       🎯 Focus area #3 (3 months)
├─ SQL & Databases        🎯 Focus area #4 (1 month)
└─ Data Visualization     🎯 Focus area #5 (2 months)

TOTAL TIMELINE: 12-18 months ⏱️
```

---

## 🎯 Example Roadmap Outline

```
Career Path: Mechanical Engineer → Data Scientist (5 years exp)

┌─ 6-MONTH PLAN ─────────────────────────────────────────┐
│                                                          │
│ Month 1-2: Python Foundations                          │
│ ├─ Learn Python syntax & fundamentals                  │
│ ├─ Practice with 10 mini-projects                      │
│ ├─ Resource: Udemy "100 Days of Code"                  │
│ └─ Expected: 8+ hours/week → 80 hours invested         │
│                                                          │
│ Month 3: Data Manipulation                             │
│ ├─ Learn Pandas & NumPy                                │
│ ├─ Work with datasets                                  │
│ ├─ Resource: DataCamp course                           │
│ └─ Expected: 50 hours invested                         │
│                                                          │
│ Month 4: Statistics & Probability                      │
│ ├─ Review statistics concepts                          │
│ ├─ Apply to real datasets                              │
│ ├─ Resource: Khan Academy + StatQuest                  │
│ └─ Expected: 60 hours invested                         │
│                                                          │
│ Month 5-6: Introduction to ML                          │
│ ├─ Learn scikit-learn                                  │
│ ├─ Build your first 3 ML models                        │
│ ├─ Resource: Andrew Ng's ML course                     │
│ └─ Expected: 80 hours invested                         │
│                                                          │
│ TOTAL: ~270 hours (≈8 hours/week) ⏱️                   │
│ DELIVERABLES: Python proficiency + ML fundamentals ✓   │
│                                                          │
└────────────────────────────────────────────────────────┘

┌─ 12-MONTH PLAN ────────────────────────────────────────┐
│                                                          │
│ Months 7-9: Advanced ML & Deep Learning               │
│ Months 10-11: Real Projects & Portfolio               │
│ Month 12: Interview Prep & Job Search                 │
│                                                          │
│ TOTAL: ~500-600 hours over 12 months                  │
│ OUTCOME: Job-ready Data Scientist 🎯                  │
│                                                          │
└────────────────────────────────────────────────────────┘

┌─ 24-MONTH PLAN ────────────────────────────────────────┐
│                                                          │
│ Months 13-18: Junior DS role + specialization          │
│ Months 19-24: Growth to mid-level, thought leadership  │
│                                                          │
│ OUTCOME: Senior Data Scientist or specialist 🏆        │
│                                                          │
└────────────────────────────────────────────────────────┘
```

---

**Visual Guide Complete! 🎨**
