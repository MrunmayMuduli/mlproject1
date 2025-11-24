# 🚀 Deployment & Usage Guide

## Table of Contents
1. [Local Setup](#local-setup)
2. [Running the App](#running-the-app)
3. [Deployment Options](#deployment-options)
4. [Troubleshooting](#troubleshooting)
5. [Advanced Configuration](#advanced-configuration)

---

## 🏠 Local Setup

### Prerequisites
- Python 3.8+
- Groq API key
- Windows PowerShell or Unix terminal
- ~2GB free disk space

### Installation Steps

#### Step 1: Navigate to Project
```bash
cd c:\Users\mrunm\Documents\GitHub\mlproject1
```

#### Step 2: Create Virtual Environment (if needed)
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

Expected output:
```
Successfully installed groq-0.36.0 streamlit-1.41.1 ...
```

#### Step 4: Set API Key

**Option A: Session Only (Current PowerShell)**
```powershell
$env:GROQ_API_KEY="gsk_your_actual_key_here"
```

**Option B: Permanent (System Wide)**
```powershell
[System.Environment]::SetEnvironmentVariable('GROQ_API_KEY','your_key','User')
```

**Verify it's set:**
```powershell
Write-Host $env:GROQ_API_KEY
```

---

## ▶️ Running the App

### Option 1: CLI Version (Recommended for Testing)

```bash
python demo/app.py
```

**What you'll see:**
```
🚀 CAREERPATH AI - Personalized Career Advice Generator
⚠️ DISCLAIMER...
📍 What is your current role? > 
```

**Usage:**
1. Answer all 4 prompts
2. Wait 10-30 seconds
3. Get your roadmap
4. Get your action plan
5. View governance notes

**Time required:** ~2 minutes

### Option 2: Web Interface (Streamlit)

```bash
streamlit run demo/app_streamlit.py
```

**What you'll see:**
- Browser opens to `http://localhost:8501`
- Beautiful web interface
- Form inputs on left
- Output sections below

**Usage:**
1. Fill in form fields
2. Click "Generate My Career Roadmap"
3. Watch as it generates
4. View full roadmap and action plan
5. Scroll for governance notes

**Time required:** ~2 minutes

### Option 3: Test/Demo Mode

```bash
python demo/test_example.py
```

**What it does:**
- Runs example: Mechanical Engineer → Data Scientist
- Doesn't require interactive input
- Shows full workflow
- Great for testing API connectivity

**Time required:** ~1 minute

---

## 🌐 Deployment Options

### Option 1: Local Machine (Current Setup)
✅ **Pros:** Fast, private, free
❌ **Cons:** Only accessible locally

**How:** Just run as shown above

---

### Option 2: Streamlit Cloud (Recommended)

#### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial CareerPath AI"
git remote add origin https://github.com/YOUR_USERNAME/mlproject1.git
git push -u origin main
```

#### Step 2: Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect GitHub account
3. Select repo, branch, and file
   - File: `demo/app_streamlit.py`
4. Click Deploy
5. Share public URL

**Result:** Live URL anyone can access!

---

### Option 3: Docker Deployment

#### Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV GROQ_API_KEY=${GROQ_API_KEY}

EXPOSE 8501

CMD ["streamlit", "run", "demo/app_streamlit.py"]
```

#### Build & Run
```bash
docker build -t careerpath-ai .
docker run -e GROQ_API_KEY="your_key" -p 8501:8501 careerpath-ai
```

---

### Option 4: Cloud Platforms

#### AWS Lambda
- Use CLI version as Lambda function
- API Gateway for HTTP endpoint
- Cost: ~$1/month for light usage

#### Google Cloud Run
```bash
gcloud run deploy careerpath-ai --source . --allow-unauthenticated
```

#### Heroku
```bash
heroku login
heroku create careerpath-ai
git push heroku main
```

---

## 🔧 Troubleshooting

### Issue 1: "Invalid API Key"

**Symptom:**
```
groq.AuthenticationError: Error code: 401 - {'error': {'message': 'Invalid API Key'
```

**Solutions:**
1. Check API key is correct (no spaces)
2. Verify it's set: `Write-Host $env:GROQ_API_KEY`
3. Get new key from console.groq.com
4. Ensure no special characters

---

### Issue 2: "ModuleNotFoundError"

**Symptom:**
```
ModuleNotFoundError: No module named 'groq'
```

**Solutions:**
```bash
# Option 1: Reinstall
pip install --upgrade --force-reinstall groq streamlit

# Option 2: Check virtual environment
.\.venv\Scripts\activate

# Option 3: Use absolute Python path
C:/Users/mrunm/Documents/GitHub/mlproject1/.venv/Scripts/python.exe demo/app.py
```

---

### Issue 3: "Connection Error"

**Symptom:**
```
Connection failed: Unable to reach Groq API
```

**Solutions:**
1. Check internet connection: `ping google.com`
2. Check Groq status: Visit console.groq.com
3. Try again in 5 minutes
4. Check firewall/proxy settings

---

### Issue 4: "Streamlit Port Already in Use"

**Symptom:**
```
Error: Address already in use: ('127.0.0.1', 8501)
```

**Solutions:**
```bash
# Option 1: Use different port
streamlit run demo/app_streamlit.py --server.port 8502

# Option 2: Kill existing process
# Find process on port 8501 and terminate
```

---

### Issue 5: "Rate Limit Exceeded"

**Symptom:**
```
Error: Rate limit exceeded. Please try again later.
```

**Explanation:** Groq free tier has rate limits

**Solutions:**
1. Wait 5-10 minutes
2. Use different Groq account
3. Upgrade to paid tier
4. Implement caching in app

---

## ⚙️ Advanced Configuration

### Custom Roles

Edit `SKILL_MAPPING` in `demo/app.py`:

```python
SKILL_MAPPING = {
    "your_new_role": {
        "required_hard_skills": ["Skill1", "Skill2", ...],
        "required_soft_skills": ["Soft1", "Soft2", ...],
        "common_certifications": ["Cert1", "Cert2", ...],
        "typical_transition_roles": ["Role1", "Role2", ...]
    }
}
```

Example:
```python
"cloud architect": {
    "required_hard_skills": ["AWS", "Azure", "Terraform", "System Design", "Networking"],
    "required_soft_skills": ["Communication", "Leadership", "Problem Solving"],
    "common_certifications": ["AWS Solutions Architect", "Azure Administrator", "Terraform Associate"],
    "typical_transition_roles": ["DevOps Engineer", "Solutions Architect", "Infrastructure Engineer"]
}
```

---

### Change LLM Model

In `app.py` or `app_streamlit.py`, change:

```python
model="mixtral-8x7b-32768"  # More powerful
# or
model="gemma-7b-it"         # Faster, lighter
```

Available models:
- `llama3-8b-8192` (default) - Balanced
- `mixtral-8x7b-32768` - More powerful
- `gemma-7b-it` - Faster

---

### Adjust Temperature

```python
temperature=0.5  # More consistent, less creative
temperature=0.7  # Balanced (default)
temperature=0.9  # More creative, more variation
```

---

### Increase Token Limits

```python
max_tokens=3000  # Longer responses (was 2000)
```

---

## 📊 Performance Tuning

### For CLI
```python
# Skip disclaimers for batch processing
SHOW_DISCLAIMER = False

# Add caching
@cache
def generate_career_roadmap(...):
    ...
```

### For Streamlit
```python
# Cache API calls
@st.cache_data
def init_groq():
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

# Cache skill mapping
@st.cache_data
def get_skill_mapping():
    return SKILL_MAPPING
```

---

## 🔐 Security Best Practices

### Protect API Key
```python
# ❌ BAD
api_key = "gsk_..."

# ✅ GOOD
api_key = os.getenv("GROQ_API_KEY")

# ✅ BETTER (with validation)
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not set!")
```

### Use .env File (Optional)
```bash
# Create .env
GROQ_API_KEY=gsk_your_key_here

# Load in Python
from dotenv import load_dotenv
load_dotenv()
```

### Prevent Secret Leaks
```bash
# Add to .gitignore
.env
*.key
config/secrets.json
```

---

## 📈 Scaling

### Light Traffic (< 100 users/month)
- Streamlit Cloud ✓
- Local deployment ✓
- Cost: FREE

### Medium Traffic (100-1000 users/month)
- Cloud Run / Lambda ✓
- Add caching ✓
- Database for history ✓
- Cost: $5-20/month

### Heavy Traffic (1000+ users/month)
- Kubernetes cluster
- Load balancing
- Multiple replicas
- Cost: $50-200/month

---

## 🧪 Testing Checklist

Before deployment:

- [ ] API key works
- [ ] CLI version runs without errors
- [ ] Streamlit version displays correctly
- [ ] Roadmap generation completes
- [ ] Action plan generation completes
- [ ] Disclaimers display
- [ ] Test with example (Mechanical Eng → Data Scientist)
- [ ] Test with custom role
- [ ] Check error messages are helpful
- [ ] Verify no hardcoded secrets

---

## 📝 Usage Examples

### Example 1: Mechanical Engineer

```bash
python demo/app.py
# Current Role: Mechanical Engineer
# Experience: 5
# Skills: CAD, MATLAB, Physics
# Target: Data Scientist
```

### Example 2: Software Developer

```bash
python demo/app.py
# Current Role: Backend Engineer
# Experience: 8
# Skills: Python, C++, Microservices, Docker
# Target: ML Engineer
```

### Example 3: Career Changer

```bash
python demo/app.py
# Current Role: Product Manager
# Experience: 10
# Skills: Strategy, Communication, Analytics
# Target: Data Scientist
```

---

## 🎓 Learning Resources

If you want to extend this project:

- **LLM Prompting**: [OpenAI Cookbook](https://cookbook.openai.com)
- **Groq Docs**: [console.groq.com/docs](https://console.groq.com/docs)
- **Streamlit**: [streamlit.io/docs](https://streamlit.io/docs)
- **Python**: [python.org/docs](https://python.org/docs)

---

## 📞 Support

**Something not working?**

1. Check QUICKSTART.md
2. Review TROUBLESHOOTING section above
3. Verify API key: `Write-Host $env:GROQ_API_KEY`
4. Check dependencies: `pip list | findstr -i groq`
5. Try test version: `python demo/test_example.py`

**Still stuck?**
- Visit [Groq console](https://console.groq.com)
- Check [Streamlit docs](https://streamlit.io)
- Review [Error logs](#troubleshooting)

---

## 🎉 Next Steps

1. ✅ Set up locally
2. ✅ Run test version
3. ✅ Try with your own data
4. ✅ Deploy to Streamlit Cloud
5. ✅ Share with others
6. ✅ Gather feedback
7. ✅ Iterate and improve

---

**Ready to deploy! 🚀**
