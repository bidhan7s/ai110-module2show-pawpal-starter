# PawPal+ Project Reflection

## 1. System Design

### Core User Actions
1. Add a pet by entering its name and species
2. Schedule a task for a pet with a time, duration, and priority
3. View today's full schedule sorted by time and check off completed tasks

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?


I designed four classes:
- Task: holds title, duration, priority, frequency, scheduled_time, and completed status. It can mark itself complete.
- Pet: holds name and species, owns a list of Tasks. It can add or remove tasks.
- Owner: holds a name and a list of Pets. It can add pets and retrieve all tasks across pets.
- Scheduler: takes an Owner and handles all scheduling logic — sorting by time, filtering, conflict detection, and recurring tasks.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

The core class structure did not change during implementation — the final code
matches the initial UML directly, which is why `uml.mmd` and `uml_final.mmd` are
identical. The one refinement was inside `Scheduler`: I split what started as a
single `get_schedule()` idea into separate `sort_by_time()`, `filter_tasks()`,
and `generate_schedule()` methods. Keeping each responsibility in its own method
made the logic easier to test in isolation rather than verifying one large method.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers three constraints: scheduled time (HH:MM), priority 
(high/medium/low), and due date (today vs future). Time-order was chosen as 
the primary sort key because a pet owner cares most about when something needs 
to happen.

**b. Tradeoffs**

The conflict detector only flags tasks at the exact same time. It does not 
check overlapping durations — a 30-minute walk at 08:00 and a feeding at 08:20 
would not trigger a warning. This is reasonable for an MVP since exact-time 
conflicts are the clearest mistakes to catch.

---

## 3. AI Collaboration

**a. How you used AI**

I used Claude as my AI coding assistant to brainstorm the UML diagram, generate 
class skeletons, implement scheduling logic, and draft the test suite. The most 
helpful prompts were specific and attached my actual files.

**b. Judgment and verification**

I verified every AI suggestion by running the code and checking the output 
matched what I expected. For example I confirmed conflict detection worked by 
adding two tasks at 08:00 and checking the warning appeared in the UI.

**Suggestions I accepted:** I kept Claude's suggestion to use `@dataclass` for
`Task` and `Pet`. It removed a lot of boilerplate `__init__` code and made the
attributes match the UML one-to-one, which kept the diagram and code in sync.
I also accepted the idea of having `Scheduler` take an `Owner` and reach tasks
through it, rather than holding its own task list — this avoided duplicated state.

**Suggestions I rejected/changed:** Claude initially proposed storing
`scheduled_time` as a `datetime.time` object. I rejected that and kept a simple
`"HH:MM"` string, because string comparison already sorts chronologically and it
made the Streamlit text input and tests far simpler. I also declined an early
suggestion to add duration-overlap conflict detection — I scoped it down to
exact-time conflicts for the MVP and noted the tradeoff in section 2b above.

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, task count, chronological sorting, conflict detection, 
and daily recurrence. These are the core behaviors the scheduler depends on.

**b. Confidence**

4/5 — the happy paths all work. Edge cases like a pet with no tasks or invalid 
time strings are not yet tested.

---

## 5. Reflection

**a. What went well**

The CLI-first approach worked really well. Testing the backend with main.py 
before touching the UI meant I caught bugs early.

**b. What you would improve**

I would add duration-overlap detection to the conflict checker and persist data 
between sessions using a database instead of session state.

**c. Key takeaway**

AI is most useful when you give it a specific file or context to work with. 
Vague prompts return generic code — specific prompts return code that actually 
fits your design.