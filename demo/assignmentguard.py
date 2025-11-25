import os
import streamlit as st
from openai import OpenAI
import json
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AssignmentGuard",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# GOVERNANCE & DISCLAIMERS
# ============================================================
DISCLAIMER = """
⚠️ **DISCLAIMER - AssignmentGuard**

This tool provides AI-assisted writing feedback and analysis. Important limitations:

**About AI Bias:**
- May reflect biases in training data (gender, culture, ESL writers)
- Not a replacement for human instructors
- Feedback may be overly harsh or lenient

**About Hallucinations:**
- AI may generate plausible-sounding but incorrect suggestions
- Always verify feedback with original sources
- Don't blindly implement all recommendations

**About Over-Reliance:**
- This is a supplementary tool, not the final word
- Instructors should review AI feedback
- Students should think critically about suggestions

**Privacy:**
- Assignment content is sent to OpenAI API
- Do not submit sensitive/confidential assignments
- School/institutional policy may apply

**Safe Usage:**
✓ Use for practice/learning
✓ Verify all feedback
✓ Combine with human review
✓ Report bias concerns
"""

# Initialize OpenAI client
@st.cache_resource
def init_openai():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        # Fallback to embedded key (not recommended in production)
        api_key = "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"
    return OpenAI(api_key=api_key)

# ============================================================
# BIAS DETECTION ENGINE
# ============================================================
def detect_potential_bias(text, author_info=None):
    """
    Detect potential biases in feedback that might unfairly penalize certain writers.
    Returns bias flags and recommendations.
    """
    bias_flags = []
    
    # Check for ESL-related bias
    text_lower = text.lower()
    if any(word in text_lower for word in ['informal', 'casual', 'colloquial', 'broken', 'unclear']):
        bias_flags.append({
            'type': 'ESL Bias',
            'severity': 'Medium',
            'flag': 'Feedback may unfairly penalize ESL/non-native speakers',
            'mitigation': 'Consider cultural/linguistic differences; focus on clarity over perfection'
        })
    
    # Check for tone bias (harshness toward certain groups)
    harsh_words = ['poor', 'terrible', 'awful', 'incompetent', 'sloppy']
    if any(word in text_lower for word in harsh_words):
        bias_flags.append({
            'type': 'Tone Bias',
            'severity': 'Low',
            'flag': 'Feedback uses harsh language',
            'mitigation': 'Provide constructive criticism; focus on improvement areas'
        })
    
    # Check for demographic assumptions
    if author_info:
        demographic_warnings = [
            'gender stereotypes',
            'cultural assumptions',
            'disability assumptions'
        ]
        bias_flags.append({
            'type': 'Demographic Context',
            'severity': 'Medium',
            'flag': 'Be aware of demographic context in feedback',
            'mitigation': 'Keep feedback neutral and focused on writing quality only'
        })
    
    return bias_flags

# ============================================================
# HALLUCINATION DETECTION
# ============================================================
def check_hallucination_risk(suggestions):
    """
    Check if AI suggestions might be hallucinated/plausible but incorrect.
    """
    hallucination_warnings = []
    
    suggestion_count = len(suggestions.split('\n'))
    if suggestion_count > 15:
        hallucination_warnings.append({
            'risk': 'High volume of suggestions',
            'warning': 'With many suggestions, some may be less reliable',
            'action': 'Prioritize top 5 suggestions; verify others independently'
        })
    
    if 'definitely' in suggestions.lower() or 'must' in suggestions.lower():
        hallucination_warnings.append({
            'risk': 'Overconfident language',
            'warning': 'AI used absolute language; may be expressing uncertainty as certainty',
            'action': 'Double-check these recommendations'
        })
    
    return hallucination_warnings

# ============================================================
# WRITING ANALYSIS FUNCTIONS
# ============================================================
def analyze_writing_quality(text):
    """Analyze writing quality using LLM"""
    client = init_openai()
    
    system_prompt = """You are an expert writing instructor and editor. Analyze the provided text and give:
1. Overall Writing Score (0-100)
2. Strengths (3-5 points)
3. Areas for Improvement (3-5 points)
4. Specific Actionable Suggestions
5. Clarity Score (0-100)
6. Engagement Score (0-100)

Be fair and encouraging. Consider that the writer may be ESL or have different background.
Provide specific examples from the text."""
    
    user_prompt = f"Please analyze this text for writing quality:\n\n{text}"
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            model="gpt-3.5-turbo",
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error analyzing text: {str(e)}"

def detect_plagiarism_risk(text):
    """Detect potential plagiarism indicators"""
    client = init_openai()
    
    system_prompt = """You are a plagiarism detection expert. Analyze the text for:
1. Writing consistency (same voice throughout?)
2. Unusual phrasing patterns
3. Overly formal sections vs casual sections
4. Citation quality
5. Plagiarism risk score (0-100)

Note: This is NOT a plagiarism checker tool. Just analyze for red flags.
Be fair - diverse vocabulary and formal sections are normal for good writers."""
    
    user_prompt = f"Analyze this text for plagiarism indicators:\n\n{text}"
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            model="gpt-3.5-turbo",
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

def generate_rewrite_suggestions(text, focus_area="clarity"):
    """Generate rewrite suggestions for specific areas"""
    client = init_openai()
    
    focus_prompts = {
        "clarity": "Make the text clearer and more concise. Remove ambiguity.",
        "engagement": "Make the text more engaging and interesting to read.",
        "grammar": "Fix grammar, spelling, and punctuation errors.",
        "structure": "Improve the organization and logical flow.",
        "academic": "Make the text more academically appropriate."
    }
    
    system_prompt = """You are a professional editor. Provide 3-5 specific rewrite suggestions.
For each suggestion:
1. Quote the original text
2. Explain why it needs improvement
3. Provide a rewritten version
4. Explain the improvement

Be constructive and supportive."""
    
    user_prompt = f"Text to edit:\n\n{text}\n\nFocus on: {focus_prompts.get(focus_area, focus_prompts['clarity'])}"
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            model="gpt-3.5-turbo",
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ============================================================
# STREAMLIT UI
# ============================================================
st.title("📋 AssignmentGuard")
st.markdown("### AI-Powered Writing Inspector with Bias Governance")

# Sidebar - Disclaimer & Settings
with st.sidebar:
    st.warning(DISCLAIMER)
    st.markdown("---")
    
    # Settings
    st.subheader("⚙️ Settings")
    analysis_type = st.radio(
        "What would you like to analyze?",
        ["Full Analysis", "Writing Quality", "Plagiarism Risk", "Rewrite Suggestions"]
    )
    
    if analysis_type == "Rewrite Suggestions":
        focus_area = st.selectbox(
            "Focus on:",
            ["clarity", "engagement", "grammar", "structure", "academic"]
        )
    
    st.markdown("---")
    st.info("💡 **Tip:** This tool uses AI to provide feedback. Always verify suggestions with an instructor or expert.")

# Main content
st.markdown("### 📝 Paste Your Assignment Below")

# Text input
assignment_text = st.text_area(
    "Your assignment text:",
    height=250,
    placeholder="Paste your essay, article, or assignment here...",
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns(3)

with col1:
    analyze_button = st.button("🔍 Analyze", use_container_width=True)

with col2:
    clear_button = st.button("🗑️ Clear", use_container_width=True)

with col3:
    pass

if clear_button:
    assignment_text = ""
    st.rerun()

# ============================================================
# ANALYSIS OUTPUT
# ============================================================
if analyze_button:
    if not assignment_text or len(assignment_text.strip()) < 50:
        st.error("❌ Please paste at least 50 characters of text to analyze")
    else:
        st.markdown("---")
        
        # Show word count
        word_count = len(assignment_text.split())
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Word Count", word_count)
        with col2:
            st.metric("Character Count", len(assignment_text))
        with col3:
            st.metric("Paragraph Count", len([p for p in assignment_text.split('\n\n') if p.strip()]))
        
        st.markdown("---")
        
        if analysis_type == "Full Analysis":
            # TAB 1: Writing Quality
            tab1, tab2, tab3, tab4, tab5 = st.tabs(
                ["✍️ Writing Quality", "⚠️ Plagiarism Risk", "🎯 Suggestions", "⚡ Bias Check", "🚨 Hallucination Risk"]
            )
            
            with tab1:
                st.subheader("Writing Quality Analysis")
                with st.spinner("Analyzing writing quality..."):
                    quality = analyze_writing_quality(assignment_text)
                st.markdown(quality)
            
            with tab2:
                st.subheader("Plagiarism Risk Assessment")
                with st.spinner("Checking for plagiarism indicators..."):
                    plagiarism = detect_plagiarism_risk(assignment_text)
                st.markdown(plagiarism)
            
            with tab3:
                st.subheader("Rewrite Suggestions")
                with st.spinner("Generating suggestions..."):
                    suggestions = generate_rewrite_suggestions(assignment_text, "clarity")
                st.markdown(suggestions)
            
            with tab4:
                st.subheader("⚡ Bias Detection")
                bias_flags = detect_potential_bias(quality)
                if bias_flags:
                    for flag in bias_flags:
                        with st.expander(f"🚩 {flag['type']} (Severity: {flag['severity']})"):
                            st.warning(f"**Flag:** {flag['flag']}")
                            st.info(f"**Mitigation:** {flag['mitigation']}")
                else:
                    st.success("✅ No obvious bias flags detected")
            
            with tab5:
                st.subheader("🚨 Hallucination Risk")
                hallucination_warnings = check_hallucination_risk(quality)
                if hallucination_warnings:
                    for warning in hallucination_warnings:
                        st.warning(f"**{warning['risk']}**\n\n{warning['warning']}\n\n**Action:** {warning['action']}")
                else:
                    st.success("✅ No high hallucination risks detected")
        
        elif analysis_type == "Writing Quality":
            with st.spinner("Analyzing writing quality..."):
                quality = analyze_writing_quality(assignment_text)
            st.markdown(quality)
        
        elif analysis_type == "Plagiarism Risk":
            with st.spinner("Checking for plagiarism indicators..."):
                plagiarism = detect_plagiarism_risk(assignment_text)
            st.markdown(plagiarism)
        
        elif analysis_type == "Rewrite Suggestions":
            with st.spinner(f"Generating {focus_area} suggestions..."):
                suggestions = generate_rewrite_suggestions(assignment_text, focus_area)
            st.markdown(suggestions)
        
        # Governance footer
        st.markdown("---")
        st.info("""
        **⚠️ Governance Reminder:**
        - ✓ This is supplementary feedback only
        - ✓ Always verify with human instructors
        - ✓ Report any biased feedback
        - ✓ Consider AI limitations
        - ✓ Respect privacy and academic integrity
        """)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("📋 AssignmentGuard v1.0")
with col2:
    st.caption("🛡️ Governance-First Writing Analysis")
with col3:
    st.caption(f"📅 {datetime.now().strftime('%Y-%m-%d')}")
