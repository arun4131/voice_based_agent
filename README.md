# Voice-Based-Native-Language-Service-Agent

# Overview

This project is a voice‑based native language service agent that helps users identify government jobs and government welfare schemes based on eligibility.
The system operates end‑to‑end in Telugu, supporting voice input and voice output, and follows a hybrid agentic architecture combining Generative AI with rule‑based tools.

The agent is designed to be safe, deterministic, and evaluation‑ready, avoiding hallucinations for government information.

Key Features

1.Voice Input (Telugu) using Speech‑to‑Text

2.Voice Output (Telugu) using Text‑to‑Speech

3.Generative AI (Gemini API) for intent detection

4.Agentic Workflow (Listen → Reason → Act → Respond)

4.Multiple Tools for job and scheme eligibility

5.Smart Fallback Logic (other locations / departments)

6.Conversation Memory across turns

Failure Recovery for speech recognition errors

# System Architecture

High‑Level Flow

##  System Flow (Telugu Voice Assistant)

User (Telugu Voice)
        ↓
Speech-to-Text (STT)
        ↓
Intent Detection (Gemini LLM)
        ↓
Agent Controller (main.py)
        ↓
Tools Layer (Jobs / Schemes)
        ↓
Response Builder (Telugu)
        ↓
Text-to-Speech (TTS)
        ↓
User (Telugu Voice)


# Architecture Style

Hybrid Agentic Architecture

LLM (Gemini) → Language understanding & intent classification

Rule‑Based Tools → Government job & scheme eligibility

Ensures correctness and no hallucinations

# Agent Lifecycle

LISTEN → REASON → ACT → RESPOND

LISTEN: Capture Telugu voice input

REASON: Identify intent (Job / Scheme) using Gemini

ACT: Call eligibility tools

RESPOND: Speak result in Telugu

# Tools Used

1️.Job Eligibility Tool

Filters government jobs only

Based on: Education
Department
Location

If jobs are not available in the selected location, the system:

Automatically checks other locations

Automatically checks other government departments

2️. Scheme Eligibility Tool

Determines eligibility using:

Age
Education
Gender

Returns only valid government welfare schemes

Technology Stack

Component	Technology

Voice Input	Google Speech Recognition (te‑IN)

Voice Output	gTTS (Telugu)

LLM	Gemini API

Agent Logic	Python

Tools	Rule‑Based Eligibility Engine

Language	Telugu (End‑to‑End)

# Setup Instructions
 
1️. Install Dependencies

pip install gtts pygame SpeechRecognition pyaudio google-generativeai
Make sure microphone access is enabled.

2️. Add Gemini API Key

In gemini.py:

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

3️. Run the Application

python main.py

#  Usage Instructions

Speak in Telugu when prompted

Choose:

Government Jobs

Government Schemes

Answer eligibility questions by voice

Listen to results in Telugu

#  Failure Handling

If speech is unclear:

“మీ మాటలు అర్థం కాలేదు. మళ్లీ చెప్పండి.”
If no jobs in selected location:

System suggests other locations

If no eligibility:

System responds safely without crashing

#  Evaluation Scenarios Covered

Scenario	Supported

Successful interaction	

No jobs in location	

Alternative locations	

Scheme eligibility	

Speech recognition failure	

Edge cases	

# Design Justification

Gemini API is used only for intent detection and language understanding

Government data is rule‑based to:

Prevent hallucinations

Ensure correctness

This mirrors real‑world government systems

# Future Enhancements

Integration with live government APIs

Multi‑language support

Application submission workflow

User profile persistence

# Conclusion
This project demonstrates a safe, practical, and scalable use of Generative AI for public service assistance.
By combining LLMs with deterministic tools, the system ensures accuracy, reliability, and native language accessibility.
