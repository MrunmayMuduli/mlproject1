# AssignmentGuard - Architecture Diagram & Technical Design

**Project:** AssignmentGuard - AI Writing Inspector
**Date:** November 24, 2025
**Version:** 1.0

---

## SYSTEM ARCHITECTURE OVERVIEW

### High-Level System Diagram

```
┌───────────────────────────────────────────────────────────────────────┐
│                          USER INTERFACE LAYER                         │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                   STREAMLIT WEB APPLICATION                 │   │
│  ├──────────────────────────────────────────────────────────────┤   │
│  │                                                              │   │
│  │  INPUT MODULE          │          OUTPUT DASHBOARD          │   │
│  │  ├─ Text Input         │          ├─ Writing Quality Tab    │   │
│  │  ├─ Author Info        │          ├─ Plagiarism Tab         │   │
│  │  ├─ Analysis Mode      │          ├─ Suggestions Tab        │   │
│  │  └─ Sidebar Controls   │          ├─ Bias Flags Tab         │   │
│  │                        │          └─ Hallucination Tab       │   │
│  │                                                              │   │
│  └───────────────────────┬────────────────────────────────────┘   │
│                          │                                         │
└──────────────────────────┼─────────────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────────┐
        │   ORCHESTRATION & CONTROL LAYER      │
        ├──────────────────────────────────────┤
        │                                      │
        │  ┌────────────────────────────────┐ │
        │  │ Analysis Mode Router            │ │
        │  │ ├─ Full Analysis                │ │
        │  │ ├─ Quality Only                 │ │
        │  │ ├─ Plagiarism Only              │ │
        │  │ └─ Suggestions Only             │ │
        │  └────────────────────────────────┘ │
        │                                      │
        │  ┌────────────────────────────────┐ │
        │  │ Parallel Processing Coordinator │ │
        │  │ (Run analysis functions in     │ │
        │  │  parallel for performance)     │ │
        │  └────────────────────────────────┘ │
        │                                      │
        └─────────┬────────────────────────────┘
                  │
        ┌─────────┴─────────────────────────┐
        │                                   │
        ▼                                   ▼
┌───────────────────────┐        ┌──────────────────────┐
│  AI/LLM LAYER         │        │  GOVERNANCE LAYER    │
│                       │        │                      │
│ ┌─────────────────┐   │        │ ┌────────────────┐   │
│ │  OpenAI Client  │   │        │ │ Bias Detection │   │
│ │  (gpt-3.5)      │   │        │ │ Engine         │   │
│ ├─────────────────┤   │        │ ├────────────────┤   │
│ │ • Quality       │   │        │ │ ┌────────────┐ │   │
│ │   Analysis      │   │        │ │ │ ESL Bias   │ │   │
│ │ • Writing       │   │        │ │ │ Detector   │ │   │
│ │   Feedback      │   │        │ │ └────────────┘ │   │
│ │ • Plagiarism    │   │        │ │ ┌────────────┐ │   │
│ │   Detection     │   │        │ │ │ Gender     │ │   │
│ │ • Rewrite       │   │        │ │ │ Bias Check │ │   │
│ │   Suggestions   │   │        │ │ └────────────┘ │   │
│ │ • General       │   │        │ │ ┌────────────┐ │   │
│ │   Analysis      │   │        │ │ │ Cultural   │ │   │
│ │                 │   │        │ │ │ Style Bias │ │   │
│ └─────────────────┘   │        │ │ └────────────┘ │   │
│                       │        │ │ ┌────────────┐ │   │
│ ┌─────────────────┐   │        │ │ │Demographic│ │   │
│ │ Prompt Library  │   │        │ │ │ Bias Flag │ │   │
│ │ (Version 1.0)   │   │        │ │ └────────────┘ │   │
│ │ ├─ Quality      │   │        │ └────────────┘   │   │
│ │ ├─ Plagiarism   │   │        │                  │   │
│ │ ├─ Suggestions  │   │        │ ┌────────────┐   │   │
│ │ └─ Analysis     │   │        │ │Hallucination    │   │
│ └─────────────────┘   │        │ │ Detection      │   │
│                       │        │ │                │   │
│ ┌─────────────────┐   │        │ │ ┌────────────┐ │   │
│ │ Error Handling  │   │        │ │ │ Confidence │ │   │
│ │ & Retry Logic   │   │        │ │ │ Scoring    │ │   │
│ └─────────────────┘   │        │ │ └────────────┘ │   │
│                       │        │ │ ┌────────────┐ │   │
└───────────────────────┘        │ │ │ Language   │ │   │
                                 │ │ │ Pattern    │ │   │
                                 │ │ │ Analysis   │ │   │
                                 │ │ └────────────┘ │   │
                                 │ └────────────┘   │   │
                                 │                  │   │
                                 └──────────────────┘   │
```

---

## DETAILED COMPONENT ARCHITECTURE

### Component 1: USER INTERFACE LAYER

```
┌─────────────────────────────────────────────────────────────┐
│              STREAMLIT APPLICATION STRUCTURE                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  HEADER SECTION                                            │
│  ├─ Application Title                                       │
│  ├─ Description & Disclaimers                               │
│  └─ Governance Banner                                       │
│                                                             │
│  SIDEBAR CONFIGURATION                                     │
│  ├─ Analysis Mode Selection (Radio Buttons)                │
│  │  ├─ Full Analysis                                       │
│  │  ├─ Writing Quality Only                                │
│  │  ├─ Plagiarism Risk Only                                │
│  │  └─ Rewrite Suggestions Only                            │
│  │                                                         │
│  ├─ Optional Author Information                            │
│  │  ├─ Author Name (optional)                              │
│  │  ├─ ESL Status (Yes/No/Unknown)                         │
│  │  ├─ Grade Level/Year (optional)                         │
│  │  └─ Assignment Type (optional)                          │
│  │                                                         │
│  ├─ Governance Disclaimers (Collapsible)                   │
│  │  ├─ AI Bias Acknowledgment                              │
│  │  ├─ Hallucination Warning                               │
│  │  ├─ Privacy Notice                                      │
│  │  ├─ Academic Integrity Reminder                         │
│  │  └─ Verification Requirement                            │
│  │                                                         │
│  ├─ Instructions & Help                                     │
│  └─ Support Contact Info                                    │
│                                                             │
│  MAIN INPUT AREA                                            │
│  ├─ Text Input Field                                        │
│  │  └─ ~2000 character capacity                            │
│  │                                                         │
│  ├─ Real-Time Metrics                                      │
│  │  ├─ Word Count                                          │
│  │  ├─ Character Count                                     │
│  │  ├─ Paragraph Count                                     │
│  │  └─ Estimated Reading Time                              │
│  │                                                         │
│  ├─ Action Buttons                                          │
│  │  ├─ [ANALYZE] (Primary)                                │
│  │  ├─ [CLEAR] (Secondary)                                │
│  │  └─ [SAMPLE ESSAY] (Demo)                              │
│  │                                                         │
│  └─ Advanced Options (Expander)                            │
│     ├─ Temperature (0.3-0.9) for LLM                       │
│     ├─ Max Tokens per Response                             │
│     └─ Retry on Error (Yes/No)                             │
│                                                             │
│  OUTPUT DISPLAY AREA (TABS)                                │
│  ├─ Tab 1: Writing Quality                                 │
│  │  ├─ Overall Score (0-100 gauge)                         │
│  │  ├─ Strengths (bullet list)                             │
│  │  ├─ Areas for Improvement (bullet list)                 │
│  │  ├─ Clarity Score (metric)                              │
│  │  ├─ Engagement Score (metric)                           │
│  │  └─ Specific Tips (expandable)                          │
│  │                                                         │
│  ├─ Tab 2: Plagiarism Risk                                 │
│  │  ├─ Risk Level (HIGH/MEDIUM/LOW badge)                  │
│  │  ├─ Consistency Analysis                                │
│  │  ├─ Citation Quality Assessment                         │
│  │  ├─ Phrasing Pattern Analysis                           │
│  │  └─ Recommendations (action items)                      │
│  │                                                         │
│  ├─ Tab 3: Rewrite Suggestions                             │
│  │  ├─ 5 Focus Areas (expandable sections)                 │
│  │  │  ├─ Clarity                                          │
│  │  │  ├─ Engagement                                       │
│  │  │  ├─ Grammar & Style                                  │
│  │  │  ├─ Structure & Flow                                 │
│  │  │  └─ Academic Tone                                    │
│  │  │                                                      │
│  │  └─ Each section includes:                              │
│  │     ├─ Current Example from Essay                       │
│  │     ├─ Suggested Revision                               │
│  │     ├─ Explanation of Why                               │
│  │     └─ Context for Application                          │
│  │                                                         │
│  ├─ Tab 4: Bias Detection                                  │
│  │  ├─ Bias Flags (with color coding)                      │
│  │  │  ├─ 🚩 ESL Bias Detected / Not Detected              │
│  │  │  ├─ 🚩 Gender Bias Detected / Not Detected           │
│  │  │  ├─ 🚩 Cultural Bias Detected / Not Detected         │
│  │  │  ├─ 🚩 Demographic Bias Detected / Not Detected      │
│  │  │  └─ 🚩 Tone Bias Detected / Not Detected             │
│  │  │                                                      │
│  │  ├─ For Each Flag:                                      │
│  │  │  ├─ Description of Bias Type                         │
│  │  │  ├─ Evidence (specific language flagged)             │
│  │  │  └─ Mitigation Strategy (action for instructor)      │
│  │  │                                                      │
│  │  └─ Overall Bias Risk Score (0-100)                     │
│  │                                                         │
│  ├─ Tab 5: Hallucination Risk                              │
│  │  ├─ Overall Risk Level (HIGH/MEDIUM/LOW)                │
│  │  ├─ Risk Factors:                                       │
│  │  │  ├─ Suggestion Volume (count + risk level)           │
│  │  │  ├─ Language Confidence (analysis)                   │
│  │  │  ├─ Absolute Statements (count of flagged phrases)   │
│  │  │  └─ Citation Reliability (analysis)                  │
│  │  │                                                      │
│  │  ├─ Hallucination Score (0-100)                         │
│  │  ├─ Red Flag Examples (if any found)                    │
│  │  └─ Verification Checklist:                             │
│  │     ├─ [ ] Cross-reference suggestions                  │
│  │     ├─ [ ] Verify citations independently              │
│  │     ├─ [ ] Check grammar rules against style guide      │
│  │     └─ [ ] Consult with instructor                      │
│  │                                                         │
│  └─ Feedback & Report Section (All Tabs)                   │
│     ├─ [DOWNLOAD PDF REPORT]                              │
│     ├─ [COPY RESULTS]                                      │
│     ├─ [REPORT BIAS ISSUE]                                │
│     ├─ [SUBMIT FEEDBACK]                                   │
│     └─ [CONTACT SUPPORT]                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Component 2: ORCHESTRATION LAYER

```
┌──────────────────────────────────────────────────────────┐
│       REQUEST PROCESSING & ANALYSIS COORDINATION          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  INPUT VALIDATION & PREPROCESSING                       │
│  ├─ Text Length Check (100-2000 chars)                  │
│  ├─ Format Validation                                   │
│  ├─ Language Detection                                  │
│  ├─ Encoding Normalization                              │
│  └─ Sensitive Data Scan                                 │
│                                                          │
│  ANALYSIS MODE ROUTER                                   │
│  ├─ FULL ANALYSIS PATH                                  │
│  │  ├─ write_quality() → Score 0-100                    │
│  │  ├─ plagiarism_risk() → Risk detection               │
│  │  ├─ rewrite_suggestions() → 5 focus areas            │
│  │  ├─ bias_detection() → Bias flags                    │
│  │  ├─ hallucination_check() → Risk warnings            │
│  │  └─ [Aggregate Results]                              │
│  │                                                      │
│  ├─ QUALITY ONLY PATH                                   │
│  │  ├─ write_quality() → Score                          │
│  │  └─ [Format & Return]                                │
│  │                                                      │
│  ├─ PLAGIARISM ONLY PATH                                │
│  │  ├─ plagiarism_risk() → Risk assessment              │
│  │  └─ [Format & Return]                                │
│  │                                                      │
│  └─ SUGGESTIONS ONLY PATH                               │
│     ├─ rewrite_suggestions() → Actionable tips          │
│     └─ [Format & Return]                                │
│                                                          │
│  PARALLEL PROCESSING COORDINATOR                        │
│  ├─ If Full Analysis:                                   │
│  │  ├─ [Parallel]                                       │
│  │  │  ├─ Quality score                                 │
│  │  │  ├─ Plagiarism check                              │
│  │  │  └─ Bias detection                                │
│  │  │                                                   │
│  │  ├─ [Sequential - depends on above]                  │
│  │  │  ├─ Suggestions (based on quality score)          │
│  │  │  └─ Hallucination check (on all outputs)          │
│  │  │                                                   │
│  │  └─ [Aggregate & Format]                             │
│  │                                                      │
│  ├─ Error Handling                                      │
│  │  ├─ API Timeout → Retry with backoff                 │
│  │  ├─ Rate Limiting → Queue request                    │
│  │  ├─ Invalid Response → Flag & return generic         │
│  │  └─ Logging → Track all errors                       │
│  │                                                      │
│  └─ Performance Optimization                            │
│     ├─ Cache common analyses                            │
│     ├─ Batch similar requests                           │
│     └─ Monitor API costs                                │
│                                                          │
│  OUTPUT FORMATTING & GOVERNANCE                         │
│  ├─ Add Disclaimers                                     │
│  ├─ Flag Bias Concerns                                  │
│  ├─ Highlight Hallucination Risks                       │
│  ├─ Include Verification Reminders                      │
│  └─ Prepare for UI Display                              │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

### Component 3: AI/LLM LAYER

```
┌──────────────────────────────────────────────────────────┐
│           LANGUAGE MODEL INTEGRATION LAYER                │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  OPENAI CLIENT CONFIGURATION                            │
│  ├─ Model: gpt-3.5-turbo                                │
│  ├─ Base URL: https://api.openai.com/v1                 │
│  ├─ API Key: [Environment Variable]                     │
│  ├─ Timeout: 30 seconds                                 │
│  ├─ Max Retries: 2                                      │
│  └─ Error Handling: Graceful degradation                │
│                                                          │
│  ANALYSIS FUNCTIONS                                     │
│  │                                                      │
│  ├─ 1. analyze_writing_quality(text)                    │
│  │   ├─ Prompt: "Analyze writing quality..."            │
│  │   ├─ Parameters:                                     │
│  │   │  ├─ temperature: 0.7 (balanced)                  │
│  │   │  ├─ max_tokens: 1000                             │
│  │   │  └─ top_p: 0.9                                   │
│  │   │                                                  │
│  │   └─ Output Structure:                               │
│  │      {                                               │
│  │        "score": 0-100,                               │
│  │        "strengths": [...],                           │
│  │        "improvements": [...],                        │
│  │        "clarity_score": 0-10,                        │
│  │        "engagement_score": 0-10,                     │
│  │        "feedback": "..."                             │
│  │      }                                               │
│  │                                                      │
│  ├─ 2. detect_plagiarism_risk(text)                     │
│  │   ├─ Prompt: "Check plagiarism risk..."              │
│  │   ├─ Analyzes:                                       │
│  │   │  ├─ Writing consistency                          │
│  │   │  ├─ Phrasing patterns                            │
│  │   │  ├─ Citation quality                             │
│  │   │  └─ Originality indicators                       │
│  │   │                                                  │
│  │   └─ Output Structure:                               │
│  │      {                                               │
│  │        "risk_level": "LOW|MEDIUM|HIGH",              │
│  │        "consistency_score": 0-100,                   │
│  │        "evidence": [...],                            │
│  │        "recommendations": [...]                      │
│  │      }                                               │
│  │                                                      │
│  ├─ 3. generate_rewrite_suggestions(text, focus)        │
│  │   ├─ Prompt: "Suggest improvements in focus area..."  │
│  │   ├─ 5 Focus Areas:                                  │
│  │   │  ├─ Clarity                                      │
│  │   │  ├─ Engagement                                   │
│  │   │  ├─ Grammar & Style                              │
│  │   │  ├─ Structure & Flow                             │
│  │   │  └─ Academic Tone                                │
│  │   │                                                  │
│  │   └─ Output Structure:                               │
│  │      {                                               │
│  │        "suggestions": [                              │
│  │          {                                           │
│  │            "original": "...",                        │
│  │            "improved": "...",                        │
│  │            "explanation": "..."                      │
│  │          }                                           │
│  │        ],                                            │
│  │        "general_tips": [...]                         │
│  │      }                                               │
│  │                                                      │
│  └─ 4. general_analysis(text)                           │
│     ├─ Comprehensive feedback                           │
│     ├─ Combines all analysis types                      │
│     └─ Aggregated insights                              │
│                                                          │
│  PROMPT ENGINEERING & OPTIMIZATION                      │
│  ├─ Base Prompts (Version 1.0)                          │
│  │  ├─ Quality Analysis Prompt                          │
│  │  ├─ Plagiarism Detection Prompt                      │
│  │  ├─ Suggestions Prompt                               │
│  │  └─ General Analysis Prompt                          │
│  │                                                      │
│  ├─ Fairness-Conscious Prompts                          │
│  │  ├─ "Consider if author is non-native English..."    │
│  │  ├─ "Avoid cultural writing style bias..."           │
│  │  ├─ "Use gender-neutral language..."                 │
│  │  └─ "Accommodate neurodivergent writing styles..."   │
│  │                                                      │
│  └─ Uncertainty Instructions                            │
│     ├─ "Include 'verify with' statements..."            │
│     ├─ "Use probabilistic language..."                  │
│     └─ "Avoid absolute statements..."                   │
│                                                          │
│  RESPONSE PARSING & VALIDATION                          │
│  ├─ JSON Extraction from LLM Output                     │
│  ├─ Schema Validation                                   │
│  ├─ Type Checking                                       │
│  ├─ Range Validation (scores 0-100)                     │
│  └─ Error Recovery (fallback templates)                 │
│                                                          │
│  COST & QUOTA MANAGEMENT                                │
│  ├─ Token Counting                                      │
│  ├─ API Cost Tracking                                   │
│  ├─ Rate Limiting                                       │
│  ├─ Daily Budget Monitoring                             │
│  └─ Cost Alerts                                          │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

### Component 4: GOVERNANCE LAYER

```
┌──────────────────────────────────────────────────────────┐
│         BIAS DETECTION & GOVERNANCE LAYER                │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  BIAS DETECTION ENGINE                                  │
│  │                                                      │
│  ├─ 1. ESL BIAS DETECTOR                                │
│  │   ├─ Purpose: Flag feedback that penalizes          │
│  │   │           non-native English speakers            │
│  │   │                                                  │
│  │   ├─ Detection Patterns:                             │
│  │   │  ├─ Language-level penalization                 │
│  │   │  │  └─ Flags: "Your English", "native speaker"  │
│  │   │  │                                               │
│  │   │  ├─ Informal language bias                       │
│  │   │  │  └─ Flags: "too informal", "formal English"  │
│  │   │  │                                               │
│  │   │  ├─ Cultural writing conventions                 │
│  │   │  │  └─ Flags: "circular logic", "indirect"      │
│  │   │  │                                               │
│  │   │  └─ Grammar overemphasis                         │
│  │   │     └─ Flags: "focus only on grammar"           │
│  │   │                                                  │
│  │   ├─ Input Factors:                                  │
│  │   │  ├─ Is author ESL? (from metadata)              │
│  │   │  └─ Feedback intensity (number of corrections)   │
│  │   │                                                  │
│  │   └─ Output:                                         │
│  │      {                                               │
│  │        "esl_bias_detected": true/false,              │
│  │        "severity": "HIGH|MEDIUM|LOW",                │
│  │        "evidence": ["..."],                          │
│  │        "mitigation": "..."                           │
│  │      }                                               │
│  │                                                      │
│  ├─ 2. GENDER BIAS DETECTOR                             │
│  │   ├─ Purpose: Detect gendered language patterns      │
│  │   │                                                  │
│  │   ├─ Detection Patterns:                             │
│  │   │  ├─ Gendered adjectives                          │
│  │   │  │  └─ "assertive" vs "aggressive",              │
│  │   │  │    "confident" vs "bossy"                     │
│  │   │  │                                               │
│  │   │  ├─ Gender-stereotyped assumptions               │
│  │   │  │  └─ "nurturing", "logical", etc.              │
│  │   │  │                                               │
│  │   │  └─ Tone consistency                             │
│  │   │     └─ Compare feedback tone across authors      │
│  │   │                                                  │
│  │   ├─ Input Factors:                                  │
│  │   │  ├─ Presumed gender (from name analysis)        │
│  │   │  └─ Feedback tone                                │
│  │   │                                                  │
│  │   └─ Output:                                         │
│  │      {                                               │
│  │        "gender_bias_detected": true/false,           │
│  │        "severity": "HIGH|MEDIUM|LOW",                │
│  │        "gendered_terms": [...],                      │
│  │        "mitigation": "..."                           │
│  │      }                                               │
│  │                                                      │
│  ├─ 3. CULTURAL WRITING STYLE DETECTOR                  │
│  │   ├─ Purpose: Recognize diverse writing conventions  │
│  │   │                                                  │
│  │   ├─ Detection Patterns:                             │
│  │   │  ├─ Linear vs circular organization              │
│  │   │  ├─ Direct vs indirect communication              │
│  │   │  ├─ Context-first vs conclusion-first            │
│  │   │  └─ Implicit vs explicit argumentation           │
│  │   │                                                  │
│  │   ├─ Cultural Awareness:                             │
│  │   │  ├─ Western academic (linear, thesis-first)      │
│  │   │  ├─ Asian academic (circular, context-first)     │
│  │   │  ├─ African narrative styles                     │
│  │   │  └─ Indigenous knowledge presentation            │
│  │   │                                                  │
│  │   └─ Output:                                         │
│  │      {                                               │
│  │        "cultural_bias_detected": true/false,         │
│  │        "writing_style_identified": "...",            │
│  │        "is_valid_alternative": true/false,           │
│  │        "mitigation": "..."                           │
│  │      }                                               │
│  │                                                      │
│  ├─ 4. DEMOGRAPHIC ASSUMPTION DETECTOR                  │
│  │   ├─ Purpose: Flag stereotypical assumptions         │
│  │   │                                                  │
│  │   ├─ Detection Patterns:                             │
│  │   │  ├─ Socioeconomic assumptions                    │
│  │   │  ├─ Geographic stereotypes                       │
│  │   │  ├─ Education background assumptions             │
│  │   │  └─ Family structure implications                │
│  │   │                                                  │
│  │   ├─ Context Analysis:                               │
│  │   │  ├─ Does feedback assume student circumstances?  │
│  │   │  └─ Are resources/support assumed?               │
│  │   │                                                  │
│  │   └─ Output:                                         │
│  │      {                                               │
│  │        "demographic_bias_detected": true/false,      │
│  │        "assumptions": [...],                         │
│  │        "mitigation": "..."                           │
│  │      }                                               │
│  │                                                      │
│  └─ 5. TONE & NEURODIVERSITY DETECTOR                   │
│     ├─ Purpose: Detect harsh tone; accommodate ND      │
│     │                                                   │
│     ├─ Detection Patterns:                              │
│     │  ├─ Harsh/condescending language                  │
│     │  ├─ Overly critical tone                          │
│     │  ├─ Dismissive language                           │
│     │  └─ Rigid rules (ND-unfriendly)                   │
│     │                                                   │
│     ├─ ND Accommodation:                                │
│     │  ├─ Acknowledge non-linear thinking               │
│     │  ├─ Value diverse organizing principles           │
│     │  └─ Support neurodivergent writing styles         │
│     │                                                   │
│     └─ Output:                                          │
│        {                                                │
│          "harsh_tone_detected": true/false,             │
│          "nd_unfriendly_rules": [...],                  │
│          "mitigation": "..."                            │
│        }                                                │
│                                                          │
│  HALLUCINATION DETECTION ENGINE                        │
│  │                                                      │
│  ├─ Confidence Scoring Analysis                         │
│  │  ├─ Flag absolute statements ("always", "never")     │
│  │  ├─ Flag overconfident language ("definitely")       │
│  │  ├─ Count definitive claims vs uncertain claims      │
│  │  └─ Output: Confidence score 0-100                   │
│  │                                                      │
│  ├─ Suggestion Volume Analysis                          │
│  │  ├─ Count suggestions provided                       │
│  │  ├─ If > 5 suggestions: elevated hallucination risk  │
│  │  └─ Output: Volume risk assessment                   │
│  │                                                      │
│  ├─ Language Pattern Detection                          │
│  │  ├─ Citation format accuracy                         │
│  │  ├─ Grammar rule correctness                         │
│  │  └─ Detect invented information                      │
│  │                                                      │
│  └─ Hallucination Risk Score                            │
│     {                                                   │
│       "hallucination_risk": 0-100,                      │
│       "confidence_level": "HIGH|MEDIUM|LOW",            │
│       "red_flags": [...],                               │
│       "verification_needed": true/false                 │
│     }                                                   │
│                                                          │
│  OUTPUT GOVERNANCE                                      │
│  ├─ Disclaimer Integration                              │
│  │  ├─ Prepend AI bias warnings                         │
│  │  ├─ Add hallucination verification notice            │
│  │  ├─ Include privacy note                             │
│  │  └─ Academic integrity reminder                      │
│  │                                                      │
│  ├─ Flag Highlighting                                   │
│  │  ├─ Color-coded bias flags (🚩)                      │
│  │  ├─ Severity levels (HIGH/MEDIUM/LOW)                │
│  │  └─ Mitigation suggestions per flag                  │
│  │                                                      │
│  ├─ Verification Checklists                             │
│  │  ├─ For hallucination risk                           │
│  │  ├─ For bias concerns                                │
│  │  └─ For academic integrity                           │
│  │                                                      │
│  └─ Feedback Collection                                 │
│     ├─ "Report Bias" mechanism                          │
│     ├─ "This feedback was unfair" button                │
│     └─ Logging of all reports for auditing              │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## DATA FLOW DIAGRAM

### Complete Data Journey

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│                    ASSIGNMENT SUBMISSION FLOW                          │
│                                                                         │
│  1. USER SUBMISSION                                                     │
│  └─ Student enters assignment text + optional author info              │
│     └─ Data: Text (string), ESL status (bool), grade level (string)   │
│                                                                         │
│  2. INPUT VALIDATION                                                    │
│  └─ Check text length (100-2000 chars), encoding, format               │
│     └─ Decision: Proceed or reject with error message                  │
│                                                                         │
│  3. ANALYSIS MODE ROUTING                                              │
│  ├─ If FULL: Go to 4A                                                  │
│  ├─ If QUALITY ONLY: Go to 4B                                          │
│  ├─ If PLAGIARISM ONLY: Go to 4C                                       │
│  └─ If SUGGESTIONS ONLY: Go to 4D                                      │
│                                                                         │
│  4A. FULL ANALYSIS PATH                                                │
│  ├─ PARALLEL EXECUTION:                                                │
│  │  ├─ Call analyze_writing_quality(text)                              │
│  │  │  └─ Send to OpenAI → receive score/feedback                      │
│  │  │                                                                  │
│  │  ├─ Call detect_plagiarism_risk(text)                               │
│  │  │  └─ Send to OpenAI → receive risk assessment                     │
│  │  │                                                                  │
│  │  └─ Call detect_potential_bias(text, author_info)                   │
│  │     └─ Run through Bias Detection Engine → flags                    │
│  │                                                                      │
│  ├─ WAIT FOR PARALLEL COMPLETION                                       │
│  │                                                                      │
│  ├─ SEQUENTIAL EXECUTION (depends on parallel results):                │
│  │  ├─ Call generate_rewrite_suggestions(text) for each focus area     │
│  │  │  └─ Send to OpenAI → receive suggestions                         │
│  │  │                                                                  │
│  │  └─ Call check_hallucination_risk(all suggestions)                  │
│  │     └─ Analyze suggestions → hallucination risk score               │
│  │                                                                      │
│  └─ AGGREGATE RESULTS → Go to 5 (Output Governance)                    │
│                                                                         │
│  4B. QUALITY ONLY PATH                                                 │
│  └─ Call analyze_writing_quality(text)                                 │
│     └─ Return score/feedback → Go to 5 (Output Governance)             │
│                                                                         │
│  4C. PLAGIARISM ONLY PATH                                              │
│  └─ Call detect_plagiarism_risk(text)                                  │
│     └─ Return risk assessment → Go to 5 (Output Governance)            │
│                                                                         │
│  4D. SUGGESTIONS ONLY PATH                                             │
│  ├─ Call generate_rewrite_suggestions(text)                            │
│  └─ Call check_hallucination_risk(suggestions)                         │
│     └─ Return suggestions + hallucination check → 5 (Output Governance)│
│                                                                         │
│  5. OUTPUT GOVERNANCE LAYER                                            │
│  ├─ Add Disclaimers                                                    │
│  │  ├─ "This is AI feedback, verify with instructor"                   │
│  │  ├─ "AI may have bias; be aware of ESL considerations"             │
│  │  ├─ "Check hallucination risks before implementing"                │
│  │  └─ "This is supplementary; not a grade or replacement"             │
│  │                                                                      │
│  ├─ Apply Bias Flags                                                   │
│  │  └─ For each bias detected: [🚩 FLAG | Description | Mitigation]    │
│  │                                                                      │
│  ├─ Highlight Hallucination Warnings                                   │
│  │  └─ If risk > 50: "⚠️ Verify these suggestions independently"       │
│  │                                                                      │
│  ├─ Add Verification Checklists                                        │
│  │  └─ Interactive checkboxes for student review                       │
│  │                                                                      │
│  └─ Format for UI Display                                              │
│     └─ Structure JSON for Streamlit tabs                               │
│                                                                         │
│  6. UI DISPLAY                                                          │
│  ├─ Tab 1: Writing Quality (Score + Feedback)                          │
│  ├─ Tab 2: Plagiarism Risk (Assessment + Recs)                         │
│  ├─ Tab 3: Rewrite Suggestions (5 focus areas)                         │
│  ├─ Tab 4: Bias Detection (Flags + Mitigations)                        │
│  ├─ Tab 5: Hallucination Risk (Warnings + Checklist)                   │
│  └─ All Tabs: Download Report, Report Bias, etc.                       │
│                                                                         │
│  7. STUDENT ACTION                                                      │
│  ├─ Review feedback critically                                         │
│  ├─ Verify suggestions with instructor/style guide                     │
│  ├─ Check bias flags for potential unfairness                          │
│  ├─ Implement improvements thoughtfully                                │
│  └─ [Optional] Report bias concerns if needed                          │
│                                                                         │
│  8. DATA CLEANUP                                                        │
│  └─ Session ends: Delete assignment text from memory                   │
│     └─ Only analysis results retained (for student records if desired)  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## API INTEGRATION DIAGRAM

```
┌─────────────────────────────────────┐
│   ASSIGNMENTGUARD APPLICATION       │
├─────────────────────────────────────┤
│  ┌───────────────────────────────┐  │
│  │  Streamlit UI Layer           │  │
│  │  (Text input, Analysis mode)  │  │
│  └───────────────────────────────┘  │
│           │                          │
│  ┌────────▼────────────────────────┐ │
│  │  Orchestration & Validation    │ │
│  │  (Check input, route analysis) │ │
│  └────────┬────────────────────────┘ │
│           │                          │
└───────────┼──────────────────────────┘
            │
  ┌─────────┴──────────────────────────────┐
  │                                        │
  ▼                                        ▼
┌──────────────────────────┐      ┌──────────────────────────┐
│   OPENAI API CLIENT      │      │   GOVERNANCE ENGINE      │
│  ┌────────────────────┐  │      │  ┌────────────────────┐  │
│  │ gpt-3.5-turbo     │  │      │  │ Bias Detection      │  │
│  ├────────────────────┤  │      │  │ (Rule-based)        │  │
│  │ Prompt 1: Quality  │  │      │  ├────────────────────┤  │
│  │ Prompt 2: Plagiarism
│  │ Prompt 3: Suggest  │  │      │  │ Hallucination       │  │
│  │ Prompt 4: General  │  │      │  │ Detection           │  │
│  │                    │  │      │  │ (Pattern analysis)  │  │
│  └────────────────────┘  │      │  └────────────────────┘  │
│           │              │      │           │               │
│  ┌────────▼────────────┐ │      │  ┌────────▼────────────┐ │
│  │ Response Parsing:   │ │      │  │ Output Governance:  │ │
│  │ ├─ Extract JSON    │ │      │  │ ├─ Add disclaimers  │ │
│  │ ├─ Validate schema │ │      │  │ ├─ Flag biases      │ │
│  │ ├─ Type check      │ │      │  │ ├─ Warn hallucinate │ │
│  │ └─ Error handling  │ │      │  │ └─ Format output    │ │
│  └────────────────────┘  │      │  └────────────────────┘  │
│                          │      │                          │
└───────┬──────────────────┘      └────────────┬─────────────┘
        │                                      │
        └──────────────────┬───────────────────┘
                           │
                ┌──────────▼──────────┐
                │  Result Aggregation │
                │  & Formatting       │
                └──────────┬──────────┘
                           │
                ┌──────────▼──────────┐
                │  Streamlit Display  │
                │  (5-tab interface)  │
                └─────────────────────┘
```

---

## Database & Storage Architecture

```
┌─────────────────────────────────────────────────────┐
│           DATA PERSISTENCE LAYER                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│  SESSION-BASED (In-Memory)                          │
│  ├─ Assignment text: [Cached during session only]  │
│  ├─ Analysis results: [Stored for UI display]      │
│  ├─ User preferences: [Session state]               │
│  └─ Cleared on session end                          │
│                                                     │
│  OPTIONAL: LOCAL STORAGE                            │
│  ├─ User settings (if saved)                        │
│  ├─ Past analysis summaries (no full text)          │
│  └─ Usage statistics                                │
│                                                     │
│  CONFIGURATION FILES                                │
│  ├─ Prompt templates (version 1.0)                 │
│  ├─ Bias detection rules                            │
│  ├─ Governance disclaimers                          │
│  └─ UI settings                                     │
│                                                     │
│  ⚠️ WHAT IS NOT STORED                              │
│  ├─ ✗ Assignment text (except during session)      │
│  ├─ ✗ Student personal data                         │
│  ├─ ✗ Student IDs or institutional records          │
│  ├─ ✗ Grades or evaluation data                     │
│  └─ ✗ Logs with identifying information             │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Deployment & Infrastructure

```
┌─────────────────────────────────────────────────────┐
│        DEPLOYMENT ARCHITECTURE                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  DEPLOYMENT OPTIONS                                │
│  ├─ Option 1: Streamlit Cloud (Recommended)        │
│  │  ├─ URL: https://assignmentguard.streamlit.app  │
│  │  ├─ Auto-scaling: Yes                           │
│  │  ├─ SSL: Yes                                    │
│  │  └─ Data location: Streamlit servers            │
│  │                                                 │
│  ├─ Option 2: University Server                    │
│  │  ├─ URL: https://university.edu/assignmentguard │
│  │  ├─ Control: Full local control                 │
│  │  ├─ SSL: Required                               │
│  │  └─ Data location: University servers           │
│  │                                                 │
│  └─ Option 3: Docker Container                     │
│     ├─ Container: Python 3.11 + Streamlit          │
│     ├─ Volume mounts: Config files                 │
│     ├─ Environment vars: API keys                  │
│     └─ Port mapping: 8501 (default Streamlit)      │
│                                                     │
│  INFRASTRUCTURE COMPONENTS                          │
│  ├─ Web Server                                     │
│  │  └─ Streamlit (Python web framework)            │
│  │                                                 │
│  ├─ LLM API Gateway                                │
│  │  └─ OpenAI API (external service)               │
│  │                                                 │
│  ├─ Governance Services                            │
│  │  └─ Bias detection (local computation)          │
│  │                                                 │
│  └─ Logging & Monitoring                           │
│     ├─ Application logs                            │
│     ├─ API usage logs                              │
│     ├─ Error tracking                              │
│     └─ Performance metrics                         │
│                                                     │
│  SECURITY CONSIDERATIONS                            │
│  ├─ API Key Management                             │
│  │  └─ Use environment variables (not hardcoded)   │
│  │                                                 │
│  ├─ HTTPS Encryption                               │
│  │  └─ All data in transit encrypted                │
│  │                                                 │
│  ├─ FERPA Compliance                               │
│  │  └─ No student data persistence                 │
│  │                                                 │
│  ├─ Authentication (Optional)                      │
│  │  └─ If institutional deployment: SSO/LDAP       │
│  │                                                 │
│  └─ Rate Limiting                                  │
│     └─ Prevent API abuse                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## System Performance & Scalability

```
┌─────────────────────────────────────────────────────┐
│    PERFORMANCE CHARACTERISTICS                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  RESPONSE TIME TARGETS                              │
│  ├─ Input validation: <100ms                       │
│  ├─ Bias detection: <200ms                         │
│  ├─ OpenAI API call: 3-10 seconds                  │
│  ├─ Result formatting: <200ms                      │
│  └─ Total: ~4-11 seconds per analysis              │
│                                                     │
│  PARALLEL PROCESSING BENEFITS                       │
│  ├─ Quality + Plagiarism + Bias run in parallel   │
│  ├─ Expected speedup: ~2x vs sequential            │
│  └─ Result: Full analysis ~6-8 seconds             │
│                                                     │
│  SCALABILITY CONSIDERATIONS                         │
│  ├─ API Rate Limiting (OpenAI tier-dependent)      │
│  ├─ Concurrent Users: Limited by API quota         │
│  ├─ Typical Deployment: 50-200 users/day           │
│  ├─ Peak Throughput: Batch during off-hours        │
│  └─ Cost Scaling: ~$0.002 per analysis             │
│                                                     │
│  OPTIMIZATION STRATEGIES                            │
│  ├─ Response caching (for identical inputs)         │
│  ├─ Batch processing (queue submissions)            │
│  ├─ Token counting (estimate costs pre-call)        │
│  └─ Error retry with backoff                       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

**Document Version:** 1.0  
**Last Updated:** November 24, 2025  
**Architecture Review:** Ready for implementation
