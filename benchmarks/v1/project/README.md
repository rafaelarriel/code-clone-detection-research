# Clone Detection — blind test project

This directory contains a small, deliberately synthetic Python codebase for checking whether an agent can identify duplicated code of different kinds.

## Instructions for the agent

Analyze only `src/`. Identify and explain suspected Type 1, Type 2, Type 3, and Type 4 code clones. Specify files, functions, exact line intervals, scope (whole function or body/subfragment), and reasons. Flag uncertain semantic matches. Do not modify source files. Do not read any parent directories or grading files.

## For experimenters

Run this in a fresh agent session, with the same model and prompt with/without your skill; record model/version/date, duration (if available), full output and any tool usage. Avoid giving the agent access to the answer key. This project is a smoke test, not a scientifically representative benchmark.
