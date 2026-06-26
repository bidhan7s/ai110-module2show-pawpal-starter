from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler

# --- Setup ---
owner = Owner("Jordan")

mochi = Pet("Mochi", "dog")
luna  = Pet("Luna", "cat")
owner.add_pet(mochi)
owner.add_pet(luna)

# --- Add tasks (out of order to test sorting) ---
mochi.add_task(Task("Evening walk", 30, "high",   "daily",  "17:00", due_date=date.today()))
mochi.add_task(Task("Morning walk", 20, "high",   "daily",  "08:00", due_date=date.today()))
mochi.add_task(Task("Medication",    5, "high",   "daily",  "08:00", due_date=date.today()))  # conflict!
mochi.add_task(Task("Feeding",      10, "high",   "daily",  "09:00", due_date=date.today()))
luna.add_task( Task("Grooming",     15, "medium", "weekly", "10:00", due_date=date.today()))
luna.add_task( Task("Playtime",     20, "low",    "daily",  "14:00", due_date=date.today()))

scheduler = Scheduler(owner)

# --- Today's Schedule ---
print(f"\n🐾 Daily Schedule for {owner.name}'s pets")
print("=" * 40)
for task in scheduler.sort_by_time():
    icon = "✅" if task.completed else "🔲"
    print(f"  {icon} {task.scheduled_time} — {task.title} ({task.duration_minutes} min) [{task.priority}]")

# --- Conflict Detection ---
print("\n⚠️  Conflict Check")
print("=" * 40)
conflicts = scheduler.detect_conflicts()
if conflicts:
    for w in conflicts:
        print(f"  {w}")
else:
    print("  No conflicts found.")

# --- Incomplete Tasks ---
print("\n📋 Incomplete Tasks")
print("=" * 40)
for task in scheduler.filter_tasks(completed=False):
    print(f"  🔲 {task.title}")