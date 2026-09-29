# Agentic Research

An AI-powered research system that takes a topic or question, searches the web, collects useful information, analyzes it, and turns the research into a structured report.

The main idea behind this project is simple: instead of asking a single LLM to answer a question directly, the system breaks the research process into multiple stages. It searches for information, extracts content from sources, analyzes the collected information, generates a report, and then reviews the result.

## 🚀 Live Preview

https://agentic-research-pk3m.onrender.com/

## 💻 GitHub Repository

https://github.com/sahil7777-7/agentic-research

---

## What is Agentic Research?

Agentic Research is a multi-agent AI research application built to automate the process of researching a topic on the web.

For example, if you enter:

> Impact of AI on software engineering

the system doesn't simply generate an answer from the LLM's existing knowledge.

Instead, it follows a research workflow:

User Query → Web Search → Web Scraping → Analysis → Report Generation → Critic Review → Final Report

This makes the application more useful for research-oriented tasks where current web information and source content are important.

---

## ✨ Features

### 🔎 Web Search

The system uses **Tavily** to search the web and find relevant sources for the user's research query.

The search stage is responsible for discovering useful pages and information that can be used during the rest of the research process.

### 🌐 Web Scraping

After finding relevant sources, the system uses **BeautifulSoup** to extract useful content from web pages.

Instead of depending only on search snippets, the system can work with the actual content available on the source pages.

### 🤖 Multi-Agent Architecture

The project follows a multi-agent approach where different agents handle different parts of the research process.

Each part of the workflow has a specific responsibility, which makes the system easier to understand, control, and extend.

### 🧠 LLM-Powered Research

The system uses LLMs through **OpenRouter** to analyze the information collected from the web.

The model receives the researched information as context and uses it to generate the final research output.

### 📝 Structured Reports

The final research is presented as a structured report instead of returning one large block of text.

The interface separates different parts of the research such as:

- Search Findings
- Extracted Evidence
- Comprehensive Findings
- Synthesized Report
- Critic Feedback
- Sources

### 🔍 Critic Review

The generated report goes through a separate review stage.

The critic evaluates the research output and provides feedback about things such as:

- Research quality
- Coverage of the topic
- Missing information
- Possible improvements
- Overall quality of the generated research

This gives the system an additional verification and improvement stage.

### ⚡ FastAPI Backend

The backend is built using **FastAPI**.

FastAPI handles the requests coming from the frontend and connects the user interface with the research workflow.

### 🎨 Research Workspace

The frontend is designed specifically around the research process.

Instead of looking like a normal chatbot, the interface shows the different stages of the research pipeline and presents the collected information in separate sections.

---

# 🧠 How It Works

The application follows a step-by-step research pipeline.

### 1. User enters a research topic

The user enters a question or topic through the web interface.

For example:

```text
Future of renewable energy and energy storage
