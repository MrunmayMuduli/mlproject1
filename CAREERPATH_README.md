# 🚀 CareerPath AI - Personalized Career Advice Generator

A sophisticated AI-powered career guidance system that combines LLM analysis with rule-based skill matching to generate personalized career roadmaps.

## 🎯 What It Does

Users enter:
- **Current Role** (e.g., "Mechanical Engineer")
- **Years of Experience**
- **Top Skills** (comma-separated)
- **Target Role** (e.g., "Data Scientist at FAANG")

The app generates:
1. **Personalized Career Roadmap**
   - Skills gap analysis
   - 6-month, 12-month, and 24-month plans
   - Specific certifications and resources
   - Motivational summary

2. **6-Month Action Plan**
   - 3-6 concrete steps
   - Week-by-week breakdown
   - Why each step matters
   - Expected outcomes

## 📂 Project Structure

```
mlproject1/
├── demo/
│   ├── app.py              # CLI version (LLM + rule engine)
│   ├── app_streamlit.py    # Streamlit web UI version
│   ├── helper.py           # Utility functions
│   └── __pycache__/
├── .venv/                  # Virtual environment
└── README.md
```

## 🏗️ Architecture

### Components

#### 1. **LLM Layer** (Groq)
- Uses `llama3-8b-8192` model from Groq
- Generates contextual, detailed career guidance
- Temperature: 0.7 (creative but consistent)

#### 2. **Rule Engine** (`SKILL_MAPPING`)
```python
SKILL_MAPPING = {
    "data scientist": {
        "required_hard_skills": [...],
        "required_soft_skills": [...],
        "common_certifications": [...],
        "typical_transition_roles": [...]
    },
    ...
}
```

Covers: Data Scientist, ML Engineer, Software Engineer, Product Manager, Mechanical Engineer

#### 3. **Governance Layer**
- **Disclaimers**: Clear about AI limitations
- **Bias Awareness**: Acknowledges potential biases in training data
- **Privacy**: Doesn't store personal career information
- **Transparency**: Explains how roadmap was generated

## 🛡️ Governance & Risk Mitigation

### Risks Identified
1. **Over-promise** → Mitigated with explicit disclaimers
2. **Bias** → Acknowledged and recommended human mentorship
3. **Privacy** → No data storage (CLI/Local only)
4. **Mis-guidance** → Recommends professional validation

### Safeguards Implemented
✅ Prominent disclaimer on startup
✅ Warning about limitations and biases
✅ Recommendation to consult mentors
✅ Transparency note on LLM + rule engine usage
✅ Validation with real market data recommended

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Groq API key (get from [console.groq.com](https://console.groq.com))
- Virtual environment

### Installation

1. **Clone/Navigate to project**
```bash
cd mlproject1
```

2. **Create virtual environment** (if not already done)
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install groq streamlit
```

4. **Set Groq API Key**
```powershell
# On Windows PowerShell
$env:GROQ_API_KEY="your-actual-groq-api-key"

# Or set permanently in system variables
```

### Usage

#### CLI Version (app.py)
```bash
python demo/app.py
```
Interactive terminal interface - answers questions and displays roadmap.

#### Streamlit Web UI (app_streamlit.py)
```bash
streamlit run demo/app_streamlit.py
```
Opens web interface at `http://localhost:8501`

## 📊 Example: Mechanical Engineer → Data Scientist

**Input:**
```
Current Role: Mechanical Engineer
Years of Experience: 5
Skills: CAD, MATLAB, Problem Solving, Physics
Target Role: Data Scientist
```

**Generated Output Example:**
```
SKILLS GAP ANALYSIS:
- Strong: Analytical thinking, project management, technical foundation ✓
- To Build: Python, SQL, Statistics, Machine Learning
- Timeline: 12-24 months with dedicated learning

6-MONTH PLAN:
Week 1-4: Complete Python fundamentals course
Week 5-8: Learn SQL and basic statistics
...

MOTIVATIONAL SUMMARY:
"Your engineering background is a hidden advantage! You have the 
systematic thinking data science needs. Focus on Python + ML frameworks 
and you'll transition successfully in 12-18 months."
```

## 🔑 Key Features

✨ **Personalized Roadmaps** - Not generic, tailored to YOU
🎯 **Realistic Timelines** - Based on industry experience
📚 **Actionable Steps** - Week-by-week breakdown
🏆 **Motivation** - Tweet-style encouraging messages
🛡️ **Governance-First** - Disclaimers and transparency
🔧 **Rule Engine** - Matches skills to requirements
🌐 **Dual UI** - CLI and Streamlit options

## 🧠 LLM Prompting Strategy

### System Prompt
```
"You are an expert career coach with 20+ years of industry experience.
Generate detailed, actionable career roadmaps that are realistic and motivating.
Always acknowledge the person's current achievements and build upon them.
Provide specific, measurable milestones."
```

### User Prompt Flow
1. Provides current state (role, skills, experience)
2. Provides target state (desired role)
3. Provides context (required skills from rule engine)
4. Requests structured output (6-month, 12-month, 24-month plans)

## ⚙️ Configuration

### Groq Settings
```python
temperature=0.7          # Balance between creativity and consistency
model="llama3-8b-8192"  # Fast, accurate, open-weight model
max_tokens=2000         # Enough for detailed roadmap
```

### Customization
- **Add new roles**: Add to `SKILL_MAPPING` dictionary
- **Change LLM**: Modify `model` parameter (e.g., `mixtral-8x7b-32768`)
- **Adjust output**: Modify `user_prompt` template

## 🧪 Testing

### Test Case 1: Mechanical Engineer → Data Scientist
```bash
# CLI: Answer prompts with:
# Current Role: Mechanical Engineer
# Experience: 5
# Skills: CAD, MATLAB, Problem Solving
# Target: Data Scientist
```

### Test Case 2: Custom Role (Rule Engine Fallback)
```bash
# If target role not in SKILL_MAPPING, falls back to LLM-only analysis
# Current Role: Chef
# Experience: 10
# Skills: Leadership, Creativity, Time Management
# Target: Product Manager
```

## 📋 Prompts Used

### Career Roadmap Generation
```
Create a personalized career roadmap for:
- Current Role: [user role]
- Years of Experience: [years]
- Current Skills: [skills]
- Target Role: [target]

Required Skills: [from rule engine]

Please provide:
1. Skills Gap Analysis
2. 6-Month Plan
3. 12-Month Plan
4. 24-Month Plan
5. Motivational Summary
6. Top 3 Resources
```

### Action Plan Generation
```
Based on this career roadmap:
[roadmap text]

Create a MAXIMUM 6-STEP ACTION PLAN for the next 6 months.
Format: Week X-Y: [Title], What to do, Why it matters, Expected outcome
```

## 🚨 Disclaimer

⚠️ **This tool provides GENERAL career guidance based on AI analysis.**

**It is NOT:**
- A guarantee of employment or success
- Professional career counseling
- A replacement for mentorship
- Fully aware of regional/industry variations

**To use effectively:**
1. ✅ Treat as supplementary guidance
2. ✅ Validate with real mentors in your target field
3. ✅ Research actual job market in your region
4. ✅ Adapt timeline based on personal circumstances
5. ✅ Consider potential biases in AI training data

## 🔮 Future Enhancements

- [ ] Database to track user progress over time
- [ ] Integration with job market data APIs
- [ ] Multi-language support
- [ ] PDF export for roadmaps
- [ ] Mentorship matching based on roadmap
- [ ] Real-time salary data integration
- [ ] Skill validation through assessments
- [ ] Career pivot suggestions

## 📝 Notes

- API key required: Get from [console.groq.com](https://console.groq.com)
- Models available: llama3-8b-8192, mixtral-8x7b-32768, gemma-7b-it
- Cost: Free tier available from Groq
- No data persistence: Each session is independent

## 📞 Support

For issues with:
- **Groq API**: Check [console.groq.com](https://console.groq.com) dashboard
- **Streamlit**: Run `streamlit run --logger.level=debug demo/app_streamlit.py`
- **Dependencies**: `pip install --upgrade groq streamlit`

---

**Built with ❤️ using Groq LLM + Rule-Based AI**
