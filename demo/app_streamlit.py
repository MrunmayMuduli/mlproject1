import os
import streamlit as st
from openai import OpenAI

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="CareerPath AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# GOVERNANCE & DISCLAIMERS
# ============================================================
DISCLAIMER = """
⚠️ **DISCLAIMER - CareerPath AI**

This tool provides general career guidance based on AI analysis. It is **NOT** a guarantee of employment or success.

**Important Limitations:**
- May contain biases based on training data
- Regional and industry variations not fully captured
- Personal circumstances vary greatly
- Consult real mentors, recruiters, and career coaches
- This is a supplementary tool, not professional career counseling
"""

# ============================================================
# SKILL MATCHING RULE ENGINE
# ============================================================
SKILL_MAPPING = {
    "data scientist": {
        "required_hard_skills": ["Python", "SQL", "Statistics", "Machine Learning", "Data Visualization"],
        "required_soft_skills": ["Communication", "Problem Solving", "Collaboration"],
        "common_certifications": ["Google Data Analytics", "AWS ML", "Coursera Machine Learning Specialization"],
        "typical_transition_roles": ["Data Analyst", "ML Engineer", "Business Analyst"]
    },
    "ml engineer": {
        "required_hard_skills": ["Python", "TensorFlow/PyTorch", "System Design", "Deployment (Docker/K8s)", "MLOps"],
        "required_soft_skills": ["Communication", "Problem Solving", "Attention to Detail"],
        "common_certifications": ["AWS ML", "Google Cloud ML", "Andrew Ng's ML Specialization"],
        "typical_transition_roles": ["Data Scientist", "Software Engineer", "Research Engineer"]
    },
    "software engineer": {
        "required_hard_skills": ["Programming (Python/Java/Go)", "System Design", "Data Structures", "Databases"],
        "required_soft_skills": ["Collaboration", "Communication", "Debugging"],
        "common_certifications": ["Cloud Certifications (AWS/GCP)", "System Design Course"],
        "typical_transition_roles": ["ML Engineer", "DevOps Engineer", "Solutions Architect"]
    },
    "product manager": {
        "required_hard_skills": ["Analytics", "SQL basics", "Technical Acumen", "Market Research"],
        "required_soft_skills": ["Communication", "Leadership", "Negotiation", "Storytelling"],
        "common_certifications": ["Reforge Product Management", "Prodify"],
        "typical_transition_roles": ["Senior PM", "Strategy Consultant", "Business Analyst"]
    },
    "mechanical engineer": {
        "required_hard_skills": ["Python", "Statistics", "Machine Learning", "Data Analysis", "CAD/Simulation"],
        "required_soft_skills": ["Problem Solving", "Collaboration", "Communication"],
        "common_certifications": ["Google Data Analytics", "AWS ML", "Andrew Ng's ML Course"],
        "typical_transition_roles": ["Data Engineer", "ML Engineer", "Data Scientist"]
    }
}

# Initialize OpenAI client
@st.cache_resource
def init_openai():
    return OpenAI(api_key="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")

# ============================================================
# CAREER ROADMAP GENERATOR
# ============================================================
def generate_career_roadmap(current_role, skills, experience_years, target_role):
    """Generate personalized career roadmap using LLM + rule engine"""
    
    client = init_openai()
    
    # Get skill recommendations from rule engine
    target_lower = target_role.lower()
    skill_data = SKILL_MAPPING.get(target_lower, {})
    
    # Build prompt for LLM
    system_prompt = """You are an expert career coach with 20+ years of industry experience.
    Generate detailed, actionable career roadmaps that are realistic and motivating.
    Always acknowledge the person's current achievements and build upon them.
    Provide specific, measurable milestones."""
    
    user_prompt = f"""
    Create a personalized career roadmap for:
    - Current Role: {current_role}
    - Years of Experience: {experience_years}
    - Current Skills: {skills}
    - Target Role: {target_role}
    
    Required Skills for Target: {skill_data.get('required_hard_skills', [])}
    Soft Skills Needed: {skill_data.get('required_soft_skills', [])}
    Relevant Certifications: {skill_data.get('common_certifications', [])}
    
    Please provide:
    1. SKILLS GAP ANALYSIS (what they need to learn)
    2. 6-MONTH PLAN (specific steps, projects, resources)
    3. 12-MONTH PLAN (deeper skills, more complex projects)
    4. 24-MONTH PLAN (mastery level, thought leadership)
    5. MOTIVATIONAL SUMMARY (tweet-style inspiring message)
    6. TOP 3 RESOURCES (courses, books, communities)
    
    Be realistic about timeline but encouraging about potential."""
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            model="gpt-3.5-turbo",
            max_tokens=2000
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"❌ Error generating roadmap: {str(e)}"

# ============================================================
# ACTION PLAN GENERATOR
# ============================================================
def generate_action_plan(current_role, target_role, roadmap):
    """Generate concise 3-6 step action plan for next 6 months"""
    
    client = init_openai()
    
    user_prompt = f"""
    Based on this career roadmap:
    {roadmap}
    
    Create a MAXIMUM 6-STEP ACTION PLAN for the next 6 months.
    Format each step as:
    Week X-Y: [Action Title]
    - What to do
    - Why it matters
    - Expected outcome
    
    Make it specific, achievable, and motivating."""
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            model="gpt-3.5-turbo",
            max_tokens=1000
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"❌ Error generating action plan: {str(e)}"

# ============================================================
# STREAMLIT UI
# ============================================================
st.title("🚀 CareerPath AI")
st.markdown("### Personalized Career Advice Generator")

# Sidebar - Disclaimer
with st.sidebar:
    st.warning(DISCLAIMER)
    st.markdown("---")
    st.info("💡 **Tip:** This tool combines LLM analysis with career skill matching rules for personalized guidance.")

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Your Information")
    current_role = st.text_input("Current Role", placeholder="e.g., Mechanical Engineer, Data Analyst")
    experience_years = st.slider("Years of Experience", 0, 50, 5)
    skills = st.text_area("Your Top Skills (comma-separated)", placeholder="e.g., Python, CAD, Problem Solving")

with col2:
    st.subheader("🎯 Your Goal")
    target_role = st.selectbox(
        "Target Role",
        ["Data Scientist", "ML Engineer", "Software Engineer", "Product Manager", "Other"],
        help="Or type your own target role"
    )
    if target_role == "Other":
        target_role = st.text_input("Enter your target role:")
    
    timeline_preference = st.radio("Timeline Preference", ["Realistic (24 months)", "Aggressive (12 months)", "Casual (3 years)"])

# Generate button
if st.button("🔮 Generate My Career Roadmap", use_container_width=True, type="primary"):
    if not current_role or not skills or not target_role:
        st.error("❌ Please fill in all required fields")
    else:
        with st.spinner("⏳ Generating your personalized career roadmap..."):
            roadmap = generate_career_roadmap(current_role, skills, experience_years, target_role)
        
        # Display roadmap
        st.subheader("📊 Your Personalized Career Roadmap")
        st.markdown(roadmap)
        
        # Generate action plan
        with st.spinner("⏳ Generating your 6-month action plan..."):
            action_plan = generate_action_plan(current_role, target_role, roadmap)
        
        st.subheader("✅ Your 6-Month Action Plan")
        st.markdown(action_plan)
        
        # Governance note
        st.info("""
        **📍 How This Was Generated:**
        - LLM Analysis: Groq llama3-8b-8192 model
        - Rule Engine: Skill matching against industry benchmarks
        - Data Source: Career industry best practices
        
        **✓ For Best Results:**
        - Discuss with mentors in your target field
        - Network with people in target roles
        - Validate timeline with actual job market
        - Adapt based on personal circumstances
        """)

# Example section
st.markdown("---")
with st.expander("📚 Example: Mechanical Engineer → Data Scientist"):
    st.markdown("""
    **Example Career Transition:**
    - **From:** Mechanical Engineer (5 years)
    - **To:** Data Scientist at FAANG
    - **Skills:** CAD, MATLAB, Problem Solving, Physics
    
    This is a real career path many engineers take! You already have:
    - ✅ Strong analytical thinking
    - ✅ Project management experience
    - ✅ Technical foundation
    
    You need to build:
    - 🔨 Python programming skills
    - 📊 Statistics and probability
    - 🤖 Machine learning fundamentals
    - 📈 Data visualization and SQL
    """)

# Footer
st.markdown("---")
st.caption("🛡️ CareerPath AI - Using advanced LLM + Rule-Based Career Guidance | Disclaimers apply - see sidebar for details")
