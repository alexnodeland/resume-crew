# ResumeCrew

ResumeCrew is an AI-powered tool that helps job seekers tailor their resumes and prepare for interviews using CrewAI.

## Features

- Job posting analysis
- Candidate profiling
- Resume tailoring
- Interview preparation

## How it works

1. **Research**: Analyzes the job posting to extract key requirements.
2. **Profiling**: Creates a comprehensive candidate profile using GitHub and personal information.
3. **Resume Strategy**: Tailors the resume to highlight relevant skills and experiences.
4. **Interview Preparation**: Generates potential interview questions and talking points.

## Diagram

```mermaid
graph TD
    A((Start)) --> B[Research Task]
    A --> C[Profile Task]
    B --> D[Resume Strategy Task]
    C --> D
    B --> E[Interview Preparation Task]
    C --> E
    D --> E
    D --> F[[tailored_resume.md]]
    E --> G[[interview_materials.md]]
    F --> H((End))
    G --> H
```

## Thanks

This project was adapted from an example in the course [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/). I would like to extend our gratitude to the course creators João Moura, CrewAI, and Deeplearning.AI for providing such a comprehensive and insightful resource.
