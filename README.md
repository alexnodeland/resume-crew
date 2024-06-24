# 🚀 ResumeCrew

ResumeCrew is an AI-powered tool that helps job seekers tailor their resumes and prepare for interviews using [CrewAI](https://github.com/joaomdmoura/crewAI).

## 📋 Table of Contents
- [Features](#-features)
- [How it works](#-how-it-works)
- [Installation](#-installation)
- [Usage](#-usage)
- [Diagram](#-diagram)
- [Contributing](#-contributing)
- [License](#-license)
- [Thanks](#-thanks)

## ✨ Features

- 🔍 **Job posting analysis**: Analyzes job postings to extract key requirements.
- 👤 **Candidate profiling**: Creates a comprehensive candidate profile using GitHub and personal information.
- 📝 **Resume tailoring**: Tailors the resume to highlight relevant skills and experiences.
- 🎤 **Interview preparation**: Generates potential interview questions and talking points.

## 🛠️ How it works

1. **🔍 Research**: Analyzes the job posting to extract key requirements.
2. **👤 Profiling**: Creates a comprehensive candidate profile using GitHub and personal information.
3. **📝 Resume Strategy**: Tailors the resume to highlight relevant skills and experiences.
4. **🎤 Interview Preparation**: Generates potential interview questions and talking points.

## 🛠️ Installation

1. Clone the repository:

```sh
git clone https://github.com/alexnodeland/resume-crew.git
```

2. Install the dependencies:

```sh
poetry install
```

## 🚀 Usage

1. Copy the `.env.example` file to `.env` and fill in the required environment variables.

2. (Optional) Modify the `cli-default.json` file to customize defaults to your specific data, including:

    - `applicant_name`: Your full name.
    - `job_posting_url`: The URL of the job posting you are applying to.
    - `github_url`: The URL of your GitHub profile.
    - `personal_writeup`: A brief writeup about your professional background and skills.

3. Pleace your resume in the `data` directory, and name it `resume.md`.
    
4. Run the application:

```sh
poetry run resume-crew
```

5. Follow the CLI prompts to use the application, or press `Enter` to use the default values, set in `cli-default.json`.

## 📊 Diagram

```mermaid
graph TD
    A((Start)) --> B[Research Task]
    A --> C[Profile Task]
    B --> D[Resume Strategy Task]
    C --> D
    B --> E[Interview Preparation Task]
    C --> E
    D --> E
    D --> F[[output/tailored_resume.md]]
    E --> G[[output/interview_materials.md]]
    F --> H((End))
    G --> H
```

## 🤝 Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## 🙏 Thanks

This project was adapted from an example in the course [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/). I would like to extend our gratitude to the course creators [João Moura](https://github.com/joaomdmoura), [CrewAI](https://www.crewai.com/), and [Deeplearning.AI](https://www.deeplearning.ai/) for providing such a comprehensive and insightful resource.
