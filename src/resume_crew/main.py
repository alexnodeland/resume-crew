import json
import time
import subprocess
import streamlit as st
from resume_crew.crew import ResumeCrewCrew


def load_example_inputs():
    with open("data/cli-default.json", "r") as file:
        return json.load(file)


def cli():
    # ANSI escape codes for styling
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    END = "\033[0m"

    print(f"{BOLD}{BLUE}Welcome to the Resume Crew CLI!{END}")
    print(f"{BOLD}{BLUE}=============================={END}\n")

    # Add an ASCII art logo
    print(f"{YELLOW}")
    print(
        r"""
    ____                                 ______                 
   / __ \___  _______  ______ ___  ___  / ____/_______ _      __
  / /_/ / _ \/ ___/ / / / __ `__ \/ _ \/ /   / ___/ _ \ | /| / /
 / _, _/  __(__  ) /_/ / / / / / /  __/ /___/ /  /  __/ |/ |/ / 
/_/ |_|\___/____/\__,_/_/ /_/ /_/\___/\____/_/   \___/|__/|__/  
    """
    )
    print(f"{END}\n")

    # Load example inputs from config.json
    print(f"{YELLOW}Loading example inputs...{END}")
    example_inputs = load_example_inputs()
    print(f"{GREEN}Example inputs loaded successfully.{END}\n")

    # Prompt the user for inputs, using example inputs if left blank
    applicant_name = (
        input(f"{BOLD}Enter your name (leave blank for default): {END}")
        or example_inputs["applicant_name"]
    )
    job_posting_url = (
        input(f"{BOLD}Enter the job posting URL (leave blank for default): {END}")
        or example_inputs["job_posting_url"]
    )
    github_url = (
        input(f"{BOLD}Enter your GitHub URL (leave blank for default): {END}")
        or example_inputs["github_url"]
    )
    personal_writeup = (
        input(f"{BOLD}Enter your personal writeup (leave blank for default): {END}")
        or example_inputs["personal_writeup"]
    )

    # Define the inputs for the job application process
    job_application_inputs = {
        "applicant_name": applicant_name,
        "job_posting_url": job_posting_url,
        "github_url": github_url,
        "personal_writeup": personal_writeup,
    }

    print(f"\n{UNDERLINE}Inputs received:{END}")
    print(f"{BOLD}Applicant Name:{END} {applicant_name}")
    print(f"{BOLD}Job Posting URL:{END} {job_posting_url}")
    print(f"{BOLD}GitHub URL:{END} {github_url}")
    print(f"{BOLD}Personal Writeup:{END} {personal_writeup}\n")

    # Add a loading animation
    print(f"\n{YELLOW}Initializing Resume Crew...{END}")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

    # Create the ResumeCrewCrew instance
    resume_crew = ResumeCrewCrew()

    # Kickoff the process
    result = resume_crew.crew().kickoff(inputs=job_application_inputs)

    # You can add any post-processing or result handling here
    print(f"\n{GREEN}Process completed. Here are the results:{END}")
    print(result)

    # Add a fun message at the end
    print(
        f"\n{BOLD}{GREEN}🎉 Your resume is ready to impress! Go get that dream job! 🚀{END}"
    )


def app():
    st.set_page_config(page_title="Resume Crew", page_icon="📄")

    st.title("Welcome to Resume Crew! 📄✨")

    # Add file uploader for resume.md
    uploaded_file = st.file_uploader("Upload your existing resume (optional)", type="md")
    if uploaded_file is not None:
        # Save the uploaded file
        with open("data/resume.md", "wb") as f:
            f.write(uploaded_file.getvalue())
        st.success("Resume uploaded successfully!")

    # Initialize session state
    if 'files_generated' not in st.session_state:
        st.session_state.files_generated = False

    # Load example inputs
    example_inputs = load_example_inputs()

    # Create input fields
    applicant_name = st.text_input("Enter your name", value=example_inputs["applicant_name"])
    job_posting_url = st.text_input("Enter the job posting URL", value=example_inputs["job_posting_url"])
    github_url = st.text_input("Enter your GitHub URL", value=example_inputs["github_url"])
    personal_writeup = st.text_area("Enter your personal writeup", value=example_inputs["personal_writeup"])

    if st.button("Generate Resume"):
        job_application_inputs = {
            "applicant_name": applicant_name,
            "job_posting_url": job_posting_url,
            "github_url": github_url,
            "personal_writeup": personal_writeup,
        }

        with st.spinner("Generating your resume... 🚀"):
            resume_crew = ResumeCrewCrew()
            resume_crew.crew().kickoff(inputs=job_application_inputs)

        st.success("Resume generated successfully! 🎉")
        st.session_state.files_generated = True

    if st.session_state.files_generated:
        # Provide download buttons for the generated files
        with open("output/interview_materials.md", "r") as file:
            interview_materials = file.read()
        with open("output/tailored_resume.md", "r") as file:
            tailored_resume = file.read()
        with open("output/log.txt", "r") as file:
            log_content = file.read()

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="Download Interview Materials",
                data=interview_materials,
                file_name="interview_materials.md",
                mime="text/markdown",
            )

        with col2:
            st.download_button(
                label="Download Tailored Resume",
                data=tailored_resume,
                file_name="tailored_resume.md",
                mime="text/markdown",
            )

        # Add a button to download log.txt
        st.download_button(
            label="Download Log File",
            data=log_content,
            file_name="log.txt",
            mime="text/plain",
        )


def run_app():
    subprocess.run(["streamlit", "run", "src/resume_crew/main.py"])


if __name__ == "__main__":
    app()
