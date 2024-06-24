from resume_crew.crew import ResumeCrewCrew


def run():
    # Define the inputs for the job application process
    job_application_inputs = {
        'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund',
        'github_url': 'https://github.com/joaomdmoura',
        'personal_writeup': """Noah is an accomplished Software
        Engineering Leader with 18 years of experience, specializing in
        managing remote and in-office teams, and expert in multiple
        programming languages and frameworks. He holds an MBA and a strong
        background in AI and data science. Noah has successfully led
        major tech initiatives and startups, proving his ability to drive
        innovation and growth in the tech industry. Ideal for leadership
        roles that require a strategic and innovative approach."""
    }

    # Create the ResumeCrewCrew instance and kickoff the process
    resume_crew = ResumeCrewCrew()
    result = resume_crew.crew().kickoff(inputs=job_application_inputs)

    # You can add any post-processing or result handling here
    print(result)


if __name__ == "__main__":
    run()