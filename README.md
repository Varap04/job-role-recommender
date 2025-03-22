# Job Role Recommendation Engine

A simple web application built with [Streamlit](https://streamlit.io/) that recommends the three most similar Data Science and Machine Learning job roles based on required skills. The recommendation engine uses **Jaccard similarity** to calculate overlap, comparing skill overlap between roles.

This project was developed as a quick task (approximately 30 minutes) and later extended into a web app for better user experience, deployed on [Streamlit Community Cloud](https://streamlit.io/community-cloud).

## Features
- Select a job role from a dropdown menu.
- Get the top 3 similar roles based on skill similarity.
- View the skills associated with the selected role for transparency.
- Simple, clean interface with a focus on usability.

## Live Demo
Check out the live app here:  https://job-role-recommender.streamlit.app/

## How It Works
The app uses **Jaccard similarity** to measure the similarity between job roles:
- **Formula**: `Jaccard Similarity = |A ∩ B| / |A ∪ B|`, where `A` and `B` are the skill sets of two roles.
- Skills are stored as sets (e.g., `{"Python", "Statistics", "Machine Learning"}`).
- For a given role, it calculates similarity with all other roles, sorts them (highest similarity first, alphabetical order for ties), and returns the top 3.

### Example
For "Data Scientist" (skills: Python, Statistics, Machine Learning, Data Visualization):
- Possible output: `["AI Researcher", "Data Analyst", "ML Engineer"]`.

## Dataset
The app uses the following hardcoded roles and skills:
| Role              | Skills                                              |
|-------------------|-----------------------------------------------------|
| Data Scientist    | Python, Statistics, Machine Learning, Data Visualization |
| ML Engineer       | Python, Machine Learning, Deployment, Algorithms   |
| Data Analyst      | SQL, Python, Data Visualization, Excel            |
| Data Engineer     | Python, SQL, ETL, Cloud Computing                 |
| AI Researcher     | Python, Deep Learning, Machine Learning, Algorithms |
| Business Analyst  | Excel, SQL, Data Visualization, Business Intelligence |
| NLP Engineer      | Python, NLP, Machine Learning, Deep Learning      |

## Prerequisites
- Python 3.7+
- [Streamlit](https://streamlit.io/) (`pip install streamlit`)
- A GitHub account for deployment

## Local Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/job-role-recommender.git
   cd job-role-recommender
