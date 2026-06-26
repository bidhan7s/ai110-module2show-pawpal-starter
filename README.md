# PawPal+ (Module 2 Project)

## ✨ Features

- **Task sorting** — schedules are always displayed in chronological order
- **Conflict warnings** — alerts you when two tasks are scheduled at the same time
- **Daily recurrence** — completing a daily task automatically creates tomorrow's occurrence
- **Weekly recurrence** — same for weekly tasks, scheduled 7 days ahead
- **Filtering** — view tasks by pet name or completion status
- **Streamlit UI** — interactive web app to manage pets, tasks, and schedules

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

Tests cover:
- **Task completion** — `mark_complete()` correctly flips the completed flag
- **Task count** — adding a task increases the pet's task list
- **Sorting** — tasks come back in chronological order regardless of insertion order
- **Conflict detection** — two tasks at the same time triggers a warning
- **Recurrence** — completing a daily task creates a new task for the next day

```
tests/test_pawpal.py::test_mark_complete_changes_status PASSED   [ 20%]
tests/test_pawpal.py::test_add_task_increases_count PASSED       [ 40%]
tests/test_pawpal.py::test_sort_by_time_is_chronological PASSED  [ 60%]
tests/test_pawpal.py::test_conflict_detection PASSED             [ 80%]
tests/test_pawpal.py::test_recurrence_creates_new_task PASSED    [100%]
========================================= 5 passed in 0.04s =========
```

Confidence level: ⭐⭐⭐⭐ (4/5)

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts all tasks chronologically by HH:MM scheduled time |
| Filtering | `Scheduler.filter_tasks(pet_name, completed)` | Filters by pet name and/or completion status |
| Conflict detection | `Scheduler.detect_conflicts()` | Warns when two tasks share the same scheduled time |
| Recurring tasks | `Scheduler.handle_recurrence(task, pet)` | Creates next occurrence for daily (+1 day) and weekly (+7 days) tasks |


## 📸 Demo Walkthrough

1. Enter your name and pet name, select species, click **Set Owner & Pet**
2. Add tasks using the task form — set a title, duration, priority, frequency, and scheduled time
3. Add two tasks at the same time to see the conflict warning appear
4. Click **Generate Schedule** to see today's tasks sorted by time
5. Conflicts appear as yellow warnings above the schedule

**Sample CLI output from `python main.py`:**
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
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
