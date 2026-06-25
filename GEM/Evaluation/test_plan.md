# Gem Evaluation Test Plan

## High-Rise Residential Precedent Design Assistant

## 1. Purpose

This test plan explains how to evaluate the **High-Rise Residential Precedent Design Assistant**.

The goal is to understand:

1. What the Gem can do well.
2. Where the Gem is weak.
3. Whether the Gem can use the 20-case knowledge base correctly.
4. Whether the Gem can admit its limits instead of inventing unsupported information.
5. How this tool can support architectural learning and design reflection.

This evaluation is not only a technical test. It is also used to support the final project report.

---

## 2. Evaluation Object

The evaluated object is the custom Gemini Gem:

```text
High-Rise Residential Precedent Design Assistant
```

The Gem uses the following files:

```text
GEM/gem_instructions.md
precedent data/merged/highrise_precedent_database_for_gem.txt
precedent data/index/case_index.json
```

The knowledge base contains 20 high-rise residential precedent cases.

Each case is organized through the Precedent DNA structure:

```text
Gene_A: Site Context
Gene_B: Design Issue / Concept / Strategy
Gene_C1: Architectural Vocabulary
Gene_C2: Semantic Relations / Strategy Candidates
Gene_D: Resident Behavior / Feedback / Reflection
```

---

## 3. Testing Method

The evaluation uses two testing methods.

### 3.1 Single-turn Test

For most tests, each prompt should be tested in a new conversation.

This avoids the Gem being influenced by previous questions.

Single-turn tests are used to examine:

```text
Case retrieval
Case comparison
Design strategy translation
Professional boundary awareness
Image and atmosphere interpretation
Reflection on architectural knowledge
```

### 3.2 Multi-turn Test

Multi-turn tests should be done in the same conversation.

They are used to examine:

```text
Context memory
Follow-up reasoning
Ability to clarify previous answers
Ability to separate case-based knowledge from AI inference
```

---


## 4. Evaluation Questions

Each test result should be reviewed with the following questions:

1. Did the Gem use cases from the knowledge base?
2. Did the Gem choose relevant cases?
3. Did the Gem explain why the cases are relevant?
4. Did the Gem transform case knowledge into design strategies?
5. Did the Gem clearly state what it does not know?
6. Did the Gem invent unsupported technical details?
7. Did the Gem avoid replacing professional judgment?
8. Can this response be used in the final project report?

---

## 5. Evaluation Criteria

| Criteria              | Question                                            |
| --------------------- | --------------------------------------------------- |
| Case Retrieval        | Did the Gem find relevant cases?                    |
| Case Explanation      | Did it explain the selected cases clearly?          |
| Strategy Translation  | Did it turn case knowledge into design suggestions? |
| Boundary Awareness    | Did it admit missing or uncertain information?      |
| Hallucination Control | Did it avoid inventing exact data?                  |
| Reflection Quality    | Did it provide useful architectural reflection?     |
| Report Usefulness     | Can the response support the final report?          |

---


## 6. Expected Findings

The Gem is expected to be strong in:

```text
Case retrieval
Case comparison
Design strategy extraction
Design suggestion generation
Diagram ideas
Architectural reflection
```

The Gem is expected to be weaker in:

```text
Structural calculation
Construction details
Building regulations
Fire safety calculation
Cost estimation
Post-occupancy evaluation
Real spatial comfort based only on images
```

This does not mean the Gem fails.

It means the Gem should be understood as:

```text
A precedent-based design assistant
A case knowledge translation tool
A design thinking partner
```

It should not be understood as:

```text
A structural engineer
A code consultant
A construction expert
A replacement for architectural judgment
```

---

## 7. Use in Final Report

The test results will be used in the final project report to discuss:

```text
What AI can learn from architectural cases
What AI is weak at in architectural reasoning
Whether a 20-case knowledge base limits AI or makes it more focused
How AI interprets architectural atmosphere
How AI tools may change architectural education
How the role of architects may change in the future
```

---

## 8. Summary

This evaluation tests both the ability and the limitation of the High-Rise Residential Precedent Design Assistant.

The main goal is not to prove that the Gem is always correct.

The goal is to understand how a curated architectural case knowledge base can help AI support design thinking, while also recognizing the areas where human architectural judgment is still necessary.
