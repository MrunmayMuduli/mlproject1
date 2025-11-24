# 🚀 CareerPath AI - Quick Start Guide

## ⚡ 5-Minute Setup

### Step 1: Get API Key
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (free tier available)
3. Create API key
4. Copy your API key

### Step 2: Set Environment Variable

**On Windows PowerShell:**
```powershell
$env:GROQ_API_KEY="your-api-key-here"
```

**Make it permanent (Windows):**
```powershell
[System.Environment]::SetEnvironmentVariable('GROQ_API_KEY','your-api-key-here','User')
```

### Step 3: Install Dependencies

```bash
cd c:\Users\mrunm\Documents\GitHub\mlproject1
pip install -r requirements.txt
```

### Step 4: Run the App

**Option A: Interactive CLI**
```bash
python demo/app.py
```
Answer the prompts and get your career roadmap!

**Option B: Web Interface (Streamlit)**
```bash
streamlit run demo/app_streamlit.py
```
Opens at: `http://localhost:8501`

---

## 🧪 Test It (Without User Input)

```bash
python demo/test_example.py
```

This runs the Mechanical Engineer → Data Scientist example automatically.

---

## 📊 What Happens Next

1. **You enter your info** (role, skills, experience, target)
2. **LLM analyzes** your profile
3. **Rule engine** matches skills to target
4. **Roadmap generated** with 6/12/24-month plans
5. **Action plan created** with specific next steps
6. **Motivational summary** to keep you inspired

---

## ❓ Troubleshooting

### "Invalid API Key" Error
- [ ] Check your API key is correct
- [ ] Verify environment variable is set: `Write-Host $env:GROQ_API_KEY`
- [ ] Get new key from console.groq.com

### "ModuleNotFoundError"
```bash
pip install --upgrade --force-reinstall groq streamlit
```

### Streamlit not starting
```bash
streamlit run demo/app_streamlit.py --logger.level=debug
```

### Rate limit exceeded
- Groq free tier has rate limits
- Wait a few minutes and try again
- Upgrade to paid tier if needed

---

## 📝 Example Workflow

**Input:**
```
Current Role: Mechanical Engineer
Experience: 5 years
Skills: CAD, MATLAB, Problem Solving
Target Role: Data Scientist
```

**Output:**
- 📊 Skills gap analysis
- 📅 6-month action plan
- 🎯 12-month milestones
- 🏆 24-month vision
- 💡 Top resources
- 🚀 Motivational message

---

## 🛡️ Important Notes

⚠️ **This is NOT professional career counseling**
- Use as supplementary guidance
- Talk to real mentors
- Research your local job market
- AI can have biases

---

## 🔧 Next Steps

1. ✅ Run `test_example.py` to verify setup
2. ✅ Try the CLI version: `python demo/app.py`
3. ✅ Try the web version: `streamlit run demo/app_streamlit.py`
4. ✅ Enter your own profile and get roadmap
5. ✅ Validate with mentors in your field

---

## 💡 Tips

- **Mechanical Engineers:** Your MATLAB/CAD skills transfer well to data science!
- **Software Developers:** You're already partway there, focus on ML frameworks
- **Data Analysts:** Lean into ML and Python for quick transition
- **Product Managers:** Your communication skills are gold in AI/ML

---

**Happy career planning! 🚀**
