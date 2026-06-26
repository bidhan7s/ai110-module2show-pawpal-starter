# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

```
🐾 Daily Schedule for Jordan's pets
========================================
  🔲 08:00 — Morning walk (20 min) [high]
  🔲 08:00 — Medication (5 min) [high]
  🔲 09:00 — Feeding (10 min) [high]
  🔲 10:00 — Grooming (15 min) [medium]
  🔲 14:00 — Playtime (20 min) [low]
  🔲 17:00 — Evening walk (30 min) [high]

⚠️  Conflict Check
========================================
  ⚠️ Conflict at 08:00: 'Morning walk' and 'Medication'

📋 Incomplete Tasks
========================================
  🔲 Evening walk
  🔲 Morning walk
  🔲 Medication
  🔲 Feeding
  🔲 Grooming
  🔲 Playtime
```

## 🧪 Testing PawPal+

```bash
python -m pytest -v
```

Tests cover: task completion, task count, chronological sorting, conflict detection, and daily recurrence.

```
======================================== test session starts ========================================
tests/test_pawpal.py::test_mark_complete_changes_status PASSED                [ 20%]
tests/test_pawpal.py::test_add_task_increases_count PASSED                    [ 40%]
tests/test_pawpal.py::test_sort_by_time_is_chronological PASSED               [ 60%]
tests/test_pawpal.py::test_conflict_detection PASSED                          [ 80%]
tests/test_pawpal.py::test_recurrence_creates_new_task PASSED                 [100%]
========================================= 5 passed in 0.04s =========================================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
