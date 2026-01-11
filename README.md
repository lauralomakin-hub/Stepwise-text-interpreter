# Stepwise Text Interpreter – PoC

## Overview
This project is a **"proof of concept"** exploring how long, compact instructional texts can be transformed into **clear, step-by-step instructions**.

The initial motivation comes from real-world contexts such as healthcare and public services, where important information is often presented in dense text that can be difficult to process — especially for people with:
- cognitive difficulties
- neurodivergence
- limited language proficiency
- mental health–related factors that can affect cognitive load

The goal is to improve **clarity, structure and accessibility**, not to change the content itself.


## What this PoC does (current scope)
At its current stage, the project experiments with taking an existing instruction text and restructuring it into a clearer step-by-step format using simple rules.

In practice, it:
- takes an input text (plain instructional text)
- applies basic structure-detection rules (e.g. sentence/line boundaries and common instruction patterns)
- outputs the same content as ordered steps with clearer separation

The intention is to make instructions easier to scan and follow and thereby reduce cognitive load for the user.

At this stage, the logic relies on simple, explicit rules, as a way to explore how instructional text can be structured into steps.


## Why this matters
Many systems focus on *what* information is provided, but not *how* it is presented.

This PoC explores how **text structure itself** can act as a form of support:
- helping users see *what to do first* 
- reducing the need to hold everything in working memory
- making instructions easier to follow in situations where stress and anxiety might cause for cognitive overload

The project is inspired by experience from education, accessibility work, and interest in human-centred AI.


## Technical approach (early stage)
- Language: Python
- Focus: readability, explainability, step-by-step transformation
- No machine learning yet

The current focus is on exploring the problem, not on applying advanced methods.


## Possible future exploration
Examples of areas that could be explored in later stages of the project:

- Exploring whether language-based text analysis methods could help identify where one instruction ends and the next begins.
- Reflecting on if and where more advanced methods could add value.
- Comparing simple rule-based approaches with more advanced techniques, to understand trade-offs.
- Experimenting with different ways of presenting the output, depending on user needs and context.



## Status
This project is in an early PoC phase and is intended as a learning and exploration project, developed step by step.