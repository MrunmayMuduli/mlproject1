"""
Test script for CareerPath AI - Example: Mechanical Engineer → Data Scientist
This demonstrates the full workflow without requiring user input
"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from app import (
    generate_career_roadmap,
    generate_action_plan,
    DISCLAIMER,
    SKILL_MAPPING
)

def test_mechanical_to_datascientist():
    """Test the example: Mechanical Engineer with 5 years → Data Scientist"""
    
    print("\n" + "="*70)
    print("🧪 TEST SCENARIO: Mechanical Engineer → Data Scientist")
    print("="*70)
    
    # Example user profile
    current_role = "Mechanical Engineer"
    experience_years = "5"
    skills = "CAD, MATLAB, Problem Solving, Physics, Project Management"
    target_role = "Data Scientist"
    
    print("\n📋 USER PROFILE:")
    print(f"  Current Role: {current_role}")
    print(f"  Experience: {experience_years} years")
    print(f"  Skills: {skills}")
    print(f"  Target Role: {target_role}")
    
    # Show what the rule engine knows about the target
    print("\n🧠 RULE ENGINE RECOMMENDATIONS FOR DATA SCIENTIST:")
    ds_skills = SKILL_MAPPING.get("data scientist", {})
    print(f"  Required Hard Skills: {ds_skills.get('required_hard_skills', [])}")
    print(f"  Required Soft Skills: {ds_skills.get('required_soft_skills', [])}")
    print(f"  Recommended Certs: {ds_skills.get('common_certifications', [])}")
    print(f"  Transition Roles: {ds_skills.get('typical_transition_roles', [])}")
    
    # Generate roadmap
    print("\n⏳ Generating personalized career roadmap...")
    print("   (This uses Groq LLM - ensure GROQ_API_KEY is set)")
    
    try:
        roadmap = generate_career_roadmap(
            current_role=current_role,
            skills=skills,
            experience_years=experience_years,
            target_role=target_role
        )
        
        print("\n" + "="*70)
        print("📊 GENERATED CAREER ROADMAP:")
        print("="*70)
        print(roadmap)
        
        # Generate action plan
        print("\n⏳ Generating 6-month action plan...")
        action_plan = generate_action_plan(
            current_role=current_role,
            target_role=target_role,
            roadmap=roadmap
        )
        
        print("\n" + "="*70)
        print("✅ GENERATED 6-MONTH ACTION PLAN:")
        print("="*70)
        print(action_plan)
        
        # Show governance note
        print("\n" + "="*70)
        print("💡 GOVERNANCE & TRANSPARENCY:")
        print("="*70)
        print("""
This roadmap was generated using:
  ✓ Groq LLM (llama3-8b-8192 model)
  ✓ Rule-based skill matching engine
  ✓ Career industry best practices

Limitations acknowledged:
  ⚠️ Not a guarantee of employment
  ⚠️ May contain biases from LLM training data
  ⚠️ Regional/industry variations not captured
  ⚠️ Personal circumstances vary

Recommendations:
  ✓ Discuss with Data Science mentors
  ✓ Network with current Data Scientists
  ✓ Validate timeline with job market
  ✓ Adapt based on personal situation
        """)
        
        print("\n✅ TEST COMPLETED SUCCESSFULLY\n")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nTroubleshooting:")
        print("  1. Ensure GROQ_API_KEY environment variable is set")
        print("  2. Check that you have a valid Groq API key")
        print("  3. Verify internet connection")
        print("  4. Check Groq API status at console.groq.com")
        return False

if __name__ == "__main__":
    print(DISCLAIMER)
    success = test_mechanical_to_datascientist()
    sys.exit(0 if success else 1)
