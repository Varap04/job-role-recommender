import streamlit as st
from typing import Dict, Set, List

# Define the roles and their required skills
roles: Dict[str, Set[str]] = {
    "Data Scientist": set("Python, Statistics, Machine Learning, Data Visualization".split(", ")),
    "ML Engineer": set("Python, Machine Learning, Deployment, Algorithms".split(", ")),
    "Data Analyst": set("SQL, Python, Data Visualization, Excel".split(", ")),
    "Data Engineer": set("Python, SQL, ETL, Cloud Computing".split(", ")),
    "AI Researcher": set("Python, Deep Learning, Machine Learning, Algorithms".split(", ")),
    "Business Analyst": set("Excel, SQL, Data Visualization, Business Intelligence".split(", ")),
    "NLP Engineer": set("Python, NLP, Machine Learning, Deep Learning".split(", "))
}

# Function to compute Jaccard similarity
def jaccard_similarity(set1: Set[str], set2: Set[str]) -> float:
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Function to recommend top 3 similar roles
def recommend_roles(input_role: str, roles: Dict[str, Set[str]]) -> List[str]:
    input_skills = roles[input_role]
    similarities = []
    
    for role, skills in roles.items():
        if role != input_role:
            sim = jaccard_similarity(input_skills, skills)
            similarities.append((role, sim))
    
    similarities.sort(key=lambda x: (-x[1], x[0]))
    return [role for role, sim in similarities[:3]]

# Streamlit app
st.title("Job Role Recommendation Engine")
st.write("Select a Data Science or ML job role to see the top 3 similar roles based on required skills.")

input_role = st.selectbox("Choose a job role:", list(roles.keys()))

if st.button("Get Recommendations"):
    recommended_roles = recommend_roles(input_role, roles)
    st.subheader(f"Top 3 Recommended Roles for '{input_role}':")
    for i, role in enumerate(recommended_roles, 1):
        st.write(f"{i}. {role}")
    st.write(f"**Skills for {input_role}:** {', '.join(roles[input_role])}")