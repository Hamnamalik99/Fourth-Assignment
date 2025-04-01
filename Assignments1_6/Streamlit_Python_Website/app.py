import streamlit as st  # Importing Streamlit library to create the web app interface
import time  # Importing the time module for using time-related functionality

# Page Config
st.set_page_config(page_title="Professional Python Learning Platform", page_icon="🐍", layout="wide")  # Setting the page configuration, including title, icon, and layout (wide for better space utilization)

# Title and Introduction
st.title("🐍 Python Professional Learning Platform")  # Displaying the main title of the page (Python platform)
st.image("https://www.python.org/static/community_logos/python-logo.png", width=600)  # Displaying the Python logo image with a specific width (600px)
st.markdown("""  # Markdown section to format the introduction text in a readable manner
## Professional Features:
- 📚 Comprehensive Python Curriculum
- ✍️ Industry-Standard Examples
- 📝 Professional Certification Preparation
- 🎯 Real-world Projects
- 🎮 Interactive Learning Tools
- 📱 Enterprise-level Projects
- 💻 Advanced Code Challenges
- 🏆 Industry Recognition
- 👥 Professional Network
- 📺 Expert Video Tutorials

Begin your professional Python journey today!
""")

# Sidebar
st.sidebar.title("Navigation")  # Adding a title for the sidebar
page = st.sidebar.radio("Select:", ["Home", "Learning Path", "Practice Lab", "Assessments", "Enterprise Projects", "Interactive Tools", "Professional Network", "About Us"])  # Radio buttons in the sidebar to navigate between different pages

# Home
if page == "Home":  # If the user selects 'Home' page
    st.header("Welcome to Professional Python Hub")  # Displaying a welcome header
    st.image("https://cdn.dribbble.com/users/1201592/screenshots/9078494/media/422a760a51cef7de2fa3db9daf697853.gif", width=700)  # Displaying a GIF for visual engagement
    
    # Featured Content Section
    st.subheader("🌟 Premium Features")  # Subheader for the features section
    col1, col2, col3 = st.columns(3)  # Creating three columns to display content side by side
    
    with col1:  # First column
        st.markdown("### 🎓 Enterprise Learning")  # Displaying a subheader for Enterprise Learning
        st.write("- Industry-standard tutorials")  # List of features for Enterprise Learning
        st.write("- Expert-led sessions")
        st.write("- Professional exercises")
        
    with col2:  # Second column
        st.markdown("### 🏆 Professional Development")  # Subheader for Professional Development
        st.write("- Industry challenges")  # List of features for Professional Development
        st.write("- Enterprise projects")
        st.write("- Certification prep")
        
    with col3:  # Third column
        st.markdown("### 👥 Network")  # Subheader for Professional Network
        st.write("- Professional community")  # Features related to Network
        st.write("- Expert consultation")
        st.write("- Industry connections")
    
    # Career Path
    st.subheader("🚀 Career Roadmap")  # Subheader for Career Roadmap
    st.info("Choose your specialized career path in Python development")  # Info box to help users choose a career path
    
    # Industry Updates
    st.subheader("📢 Industry Updates")  # Subheader for Industry Updates
    st.success("New Enterprise Python courses available!")  # Success message to inform the user about new courses
    st.success("Industry-recognized certification tracks open!")  # Another success message
    
    # Professional Tips
    st.subheader("💡 Professional Best Practices")  # Subheader for professional best practices
    tips = [  # List of professional tips
        "Implement design patterns effectively",
        "Follow PEP 8 style guidelines",
        "Use proper error handling",
        "Practice test-driven development",
        "Optimize code performance",
        "Implement security best practices"
    ]
    st.info(tips[int(time.time()) % len(tips)])  # Displaying a random tip from the list (using modulo with the current time to pick a different tip)

# Learning Path
elif page == "Learning Path":  # If the user selects 'Learning Path' page
    st.header("Professional Python Curriculum")  # Header for the curriculum section
    st.markdown("Enterprise-grade example:")  # Brief description for the example
    code = st.code('''  # Displaying a code snippet in a formatted box
class ProfessionalExample:
    def __init__(self, name: str):
        self.name = name
        
    def demonstrate(self) -> str:
        return f"Welcome to professional Python, {self.name}"
    ''')
    if st.button("Execute"):  # Button to execute the code
        st.write("Professional example executed successfully")  # Confirmation that the example was executed
    
    st.markdown("Interactive Development:")  # Title for interactive development section
    name = st.text_input("Enter your name")  # Text input field to collect user's name
    if name:  # If a name is entered by the user
        st.write(f"Welcome to professional Python, {name}")  # Display a personalized message
        
    # Advanced Topics
    st.subheader("🎯 Advanced Concepts")  # Subheader for advanced concepts section
    topic = st.selectbox("Select topic:", ["Design Patterns", "Advanced Data Structures", "Concurrent Programming", "System Architecture"])  # Dropdown menu to select advanced topics
    st.write(f"Exploring {topic}")  # Displaying the selected topic

# Practice Lab
elif page == "Practice Lab":  # If the user selects 'Practice Lab' page
    st.header("Professional Practice Lab")  # Header for Practice Lab
    st.markdown("Solve this enterprise challenge:")  # Challenge description
    with st.form("practice"):  # Creating a form to submit user input
        code_solution = st.text_area("Implement a singleton pattern:")  # Text area for code input
        submit = st.form_submit_button("Validate")  # Submit button to validate the code
        if submit:  # If the user submits the form
            st.info("Reviewing your implementation...")  # Informing the user that the code will be reviewed

# Assessments
elif page == "Assessments":  # If the user selects 'Assessments' page
    st.header("Professional Assessments")  # Header for Assessments
    with st.form("assessment"):  # Creating a form for the assessment questions
        st.radio("Which design pattern ensures a single instance?",  # Radio button for design pattern question
                ["Singleton", "Factory", "Observer", "Command"])
        st.radio("What is the time complexity of QuickSort?",  # Radio button for time complexity question
                ["O(n log n)", "O(n²)", "O(n)", "O(log n)"])
        st.radio("Which is not a SOLID principle?",  # Radio button for SOLID principles question
                ["Single Responsibility", "Open/Closed", "Quick Response", "Dependency Inversion"])
        submit = st.form_submit_button("Submit")  # Submit button to submit the assessment
        if submit:  # If the user submits the form
            st.success("Assessment completed!")  # Confirmation message that the assessment is complete

# Enterprise Projects
elif page == "Enterprise Projects":  # If the user selects 'Enterprise Projects' page
    st.header("Enterprise Python Projects")  # Header for the enterprise projects section
    st.subheader("🚀 Industry-Standard Projects")  # Subheader for the project section
    projects = {  # A dictionary to list various projects
        "Enterprise CRM": "Build a customer relationship management system",
        "Data Pipeline": "Create an ETL data pipeline",
        "API Gateway": "Develop a RESTful API gateway",
        "Microservices": "Implement a microservices architecture"
    }
    for project, desc in projects.items():  # Loop through each project and its description
        st.write(f"**{project}**: {desc}")  # Display each project and its description

# Interactive Tools
elif page == "Interactive Tools":  # If the user selects 'Interactive Tools' page
    st.header("Professional Development Tools")  # Header for professional development tools
    tool = st.selectbox("Select tool:", ["Code Analyzer", "Performance Profiler", "Security Scanner"])  # Dropdown menu to select a tool
    if tool == "Code Analyzer":  # If the selected tool is Code Analyzer
        st.write("Analyze your code for professional standards")  # Displaying info about the tool
        code_input = st.text_area("Enter your code:")  # Text area for the user to input their code
        if st.button("Analyze"):  # Button to analyze the code
            st.info("Analysis in progress...")  # Inform the user that the analysis is happening

# Professional Network
elif page == "Professional Network":  # If the user selects 'Professional Network' page
    st.header("Professional Python Network")  # Header for the professional network section
    st.subheader("👥 Connect with Industry Experts")  # Subheader for connecting with experts
    st.text_area("Share your professional insights:")  # Text area for sharing insights
    st.button("Publish")  # Button to publish insights
    
    st.subheader("📢 Industry Announcements")  # Subheader for industry announcements
    st.info("Join our upcoming tech conference!")  # Information about an upcoming event

# About Us
elif page == "About Us":  # If the user selects 'About Us' page
    st.header("About Our Platform")  # Header for the 'About Us' section
    st.write("We are a leading professional Python learning platform, trusted by industry experts and enterprises worldwide.")  # Text about the platform
    st.write("Our curriculum is designed to meet industry standards and prepare you for professional")
