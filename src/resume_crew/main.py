import json
import time
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


if __name__ == "__main__":
    cli()
