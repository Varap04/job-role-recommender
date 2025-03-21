# job-role-recommender
Recommendation Engine Documentation for Job Role Recommendation System

Approach and Methodology
-----------------------

This project is about building a simple recommendation system that helps people find job roles in Data Science and Machine Learning that are similar to a role they’re interested in. For example, if someone is looking at a "Data Scientist" role, the system will suggest other roles that have similar skills, like "ML Engineer" or "AI Researcher." The idea is to make it easier for someone to explore related career paths based on the skills required for each role. Let’s break down how this system was created, step by step, in a way that’s easy to follow.

1. Organizing the Data: Setting Up the Information
   The first step in building this system is to gather and organize the information about different job roles and the skills they require. Imagine you have a list of job roles, such as "Data Scientist," "ML Engineer," "Data Analyst," and so on. For each role, there’s a list of skills that are needed to do that job. For example, a Data Scientist might need skills like Python (a programming language), Statistics (for analyzing data), Machine Learning (for building predictive models), and Data Visualization (for creating charts and graphs). Similarly, an ML Engineer might need Python, Machine Learning, Deployment (for putting models into real-world use), and Algorithms (for designing how models work).

   In this system, the data is organized like a dictionary or a lookup table. Think of it as a notebook where each page has a job role written at the top, and below it, there’s a list of skills for that role. But instead of keeping the skills as a list of words separated by commas (like "Python, Statistics, Machine Learning"), the system stores them as a "set." A set is a special way of storing items where each item only appears once (no duplicates), and the order doesn’t matter. For example, the set of skills for a Data Scientist would be {Python, Statistics, Machine Learning, Data Visualization}. Storing skills as a set is important because it makes it easier to compare skills between roles later on. This way, the system has all the roles and their skills ready to work with.

2. Measuring Similarity Between Roles: Finding Out How Alike They Are
   The main goal of this system is to recommend roles that are similar to the one you choose. But how do we decide if two roles are similar? We do this by looking at the skills they require and seeing how many skills they have in common. The more skills two roles share, the more similar they are. To measure this similarity, the system uses a method called "Jaccard Similarity."

   Let’s break down Jaccard Similarity with an example. Imagine you have two roles: a Data Scientist with skills {Python, Statistics, Machine Learning, Data Visualization} and an ML Engineer with skills {Python, Machine Learning, Deployment, Algorithms}. To calculate Jaccard Similarity, we do the following:
   - First, find the skills that both roles share (called the "intersection"). Here, the shared skills are Python and Machine Learning, so the intersection has 2 skills.
   - Next, find all the unique skills across both roles (called the "union"). The unique skills are Python, Statistics, Machine Learning, Data Visualization, Deployment, and Algorithms, which makes 6 skills in total.
   - Finally, divide the number of shared skills by the total number of unique skills: 2 divided by 6 equals 0.33. This number, 0.33, is the Jaccard Similarity score, and it tells us how similar the two roles are. A score closer to 1 means the roles are very similar (they share most of their skills), while a score closer to 0 means they’re very different (they share few or no skills).

   The system uses this Jaccard Similarity method to compare any two roles by looking at their sets of skills. It’s a simple and effective way to measure similarity because it focuses only on the overlap of skills, which is exactly what we need for this task.

3. Recommending Similar Roles: Picking the Top 3 Matches
   Now that we have a way to measure similarity, the next step is to use it to recommend the top 3 most similar roles for any role you choose. Here’s how the recommendation process works:
   - Let’s say you pick the role "Data Scientist." The system first looks at the skills for Data Scientist, which are {Python, Statistics, Machine Learning, Data Visualization}.
   - Then, it compares these skills to the skills of every other role in the list, like "ML Engineer," "Data Analyst," "AI Researcher," and so on. It skips the Data Scientist role itself because we don’t want to recommend the same role you picked.
   - For each comparison, the system calculates the Jaccard Similarity score. For example, it might find that the similarity between Data Scientist and ML Engineer is 0.33, between Data Scientist and Data Analyst is 0.25, and so on.
   - The system makes a list of all the other roles along with their similarity scores, like this: [(ML Engineer, 0.33), (Data Analyst, 0.25), (AI Researcher, 0.40), ...].
   - Next, it sorts this list from highest to lowest similarity score, so the roles with the most similar skills come first. If two roles happen to have the same similarity score, the system sorts them alphabetically by their names to decide which one comes first.
   - Finally, the system picks the top 3 roles from this sorted list and recommends them as the most similar roles to the one you chose. For example, it might recommend "AI Researcher," "ML Engineer," and "NLP Engineer" as the top 3 matches for "Data Scientist."

   This process ensures that the recommendations are based on how much the skills overlap, which makes the suggestions relevant and useful.

4. Building the Web Application: Making It Easy to Use
   To make this recommendation system accessible to users, a simple web application was created using a tool called Streamlit. Streamlit is like a magic wand that lets you build a web page with just a few instructions, without needing to know a lot about web development. The app is designed to be very user-friendly, so anyone can use it, even if they’re not a tech expert.

   When you open the app, here’s what you see:
   - At the top, there’s a title that says "Job Role Recommendation Engine," so you know what the app is for.
   - Below the title, there’s a short instruction that says, "Select a Data Science or ML job role to see the top 3 similar roles based on required skills." This tells you exactly what to do.
   - There’s a dropdown menu (like a list you can click on) where you can choose a role, such as "Data Scientist," "ML Engineer," or "Data Analyst." The dropdown shows all the roles available in the system.
   - Under the dropdown, there’s a button labeled "Get Recommendations." When you click this button, the app does its magic and shows you the results.
   - The results appear below the button. First, there’s a heading that says something like "Top 3 Recommended Roles for 'Data Scientist'," depending on the role you picked. Then, it lists the top 3 similar roles, numbered 1, 2, and 3, like "1. AI Researcher," "2. ML Engineer," and "3. NLP Engineer."
   - Finally, the app shows the skills for the role you selected, so you can see what skills were used to make the recommendations. For example, it might say, "Skills for Data Scientist: Python, Statistics, Machine Learning, Data Visualization."

   The app is designed to be simple and focused, with no extra clutter, so you can quickly get the recommendations you need.

Why Jaccard Similarity Was Chosen
---------------------------------

The system uses Jaccard Similarity to compare roles, and there are several reasons why this method was chosen. Let’s explore these reasons in detail to understand why it’s a good fit for this project:

- It’s Simple and Easy to Understand: Jaccard Similarity is a very straightforward idea—it’s all about looking at the skills two roles share and comparing that to the total number of unique skills they have. This simplicity makes it easy to set up and explain, which is perfect for a small project like this where we don’t want things to get too complicated. For someone building or using the system, it’s easy to see how the similarity scores are calculated and why certain roles are recommended.

- It’s Perfect for Comparing Sets of Skills: In this project, the skills for each role are stored as a set, which is like a collection of items where each item (skill) is either present or not. For example, a Data Scientist either knows Python or doesn’t—there’s no in-between. Jaccard Similarity is designed specifically for comparing sets like this. It focuses on the overlap between two sets (the skills both roles share) and ignores things like the order of the skills or how many times a skill appears (since sets don’t have duplicates). This makes it a natural choice for this task, as it matches how the data is organized.

- It Doesn’t Require Complicated Adjustments: Some other methods for measuring similarity, like cosine similarity, require turning the skills into numbers (like a list of 0s and 1s) and sometimes deciding how important each skill is (called weighting). For example, you might decide that Python is more important than Excel and give it a higher weight. But in this project, we don’t have any information about which skills are more important, so we want to treat all skills equally. Jaccard Similarity does exactly that—it doesn’t need any extra adjustments or decisions about weighting, which keeps the system fair and simple.

- It Works Well Even When Roles Have Different Numbers of Skills: Some roles might have more skills than others. For example, a Data Scientist might have 4 skills, while a Data Analyst might have 3. Jaccard Similarity handles this difference easily by focusing on the overlap relative to the total unique skills. This means it can fairly compare roles regardless of how many skills they have, making it a reliable choice for this dataset.

- It Avoids Unnecessary Complexity: Other similarity methods, like cosine similarity or Euclidean distance, often require turning the data into a different format (like a vector) and doing extra math, such as normalizing the data to make sure the numbers are on the same scale. Jaccard Similarity doesn’t need any of that—it works directly with the sets of skills, which keeps the system lightweight and easy to manage. For a small project like this, where the goal is to keep things simple and efficient, Jaccard Similarity is a great choice.

In summary, Jaccard Similarity was chosen because it’s simple, works perfectly with the way the skills are stored (as sets), doesn’t require complicated adjustments, and can handle differences in the number of skills per role. It’s a practical and effective method for this recommendation system, ensuring that the recommendations are meaningful and easy to understand.
