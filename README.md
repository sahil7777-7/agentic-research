# Agentic Research

An AI-powered multi-agent research system that searches the web, extracts useful information, synthesizes findings, and generates a structured research report.

## Overview

Agentic Research uses multiple AI agents and web tools to automate the research workflow.

Instead of simply asking an LLM to answer a question, the system follows a research pipeline:

**User Query → Web Search → Web Scraping → Research Synthesis → Critic Review → Final Report**

The goal is to make AI-generated research more structured, informative, and reliable.

## Features

- 🔎 Web search using Tavily
- 🌐 Web scraping using BeautifulSoup
- 🤖 Multi-agent research workflow
- 🧠 LLM-powered information synthesis
- 📝 Structured research report generation
- 🔍 AI critic/reviewer for generated research
- ⚡ FastAPI backend
- 🔗 LangGraph-based agent workflow
- 🎨 Simple web interface

## Tech Stack

- **Python**
- **FastAPI**
- **LangGraph**
- **LangChain**
- **OpenRouter**
- **Tavily**
- **BeautifulSoup**
- **HTML / CSS / JavaScript**

## Architecture

```text
                    User Query
                        │
                        ▼
                ┌───────────────┐
                │ Research Agent│
                └───────┬───────┘
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
        Tavily Search       Web Scraping
              │             BeautifulSoup
              └─────────┬─────────┘
                        ▼
                Research Synthesis
                        │
                        ▼
                  Critic Agent
                        │
                        ▼
                 Final Research
                     Report
