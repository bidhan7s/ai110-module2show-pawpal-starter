from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional


@dataclass
class Task:
    """Represents a single pet care task."""
    title: str
    duration_minutes: int
    priority: str          # "high", "medium", "low"
    frequency: str         # "once", "daily", "weekly"
    scheduled_time: str    # "HH:MM" e.g. "08:00"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Represents a pet with a list of care tasks."""
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from this pet's task list."""
        if task in self.tasks:
            self.tasks.remove(task)


class Owner:
    """Represents a pet owner who manages multiple pets."""

    def __init__(self, name: str):
        self.name = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def get_all_tasks(self) -> list:
        """Return every task across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    """The brain — retrieves, sorts, filters, and manages tasks."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> list:
        """Get all tasks from all pets."""
        return self.owner.get_all_tasks()

    def sort_by_time(self) -> list:
        """Return tasks sorted chronologically by scheduled_time."""
        return sorted(self.get_all_tasks(), key=lambda t: t.scheduled_time)

    def filter_tasks(self, pet_name=None, completed=None) -> list:
        """Filter tasks by pet name and/or completion status."""
        results = []
        for pet in self.owner.pets:
            if pet_name and pet.name != pet_name:
                continue
            for task in pet.tasks:
                if completed is not None and task.completed != completed:
                    continue
                results.append(task)
        return results

    def detect_conflicts(self) -> list:
        """Return warning messages for tasks scheduled at the same time."""
        seen = {}
        warnings = []
        for pet in self.owner.pets:
            for task in pet.tasks:
                key = task.scheduled_time
                if key in seen:
                    warnings.append(
                        f"⚠️ Conflict at {task.scheduled_time}: "
                        f"'{seen[key]}' and '{task.title}'"
                    )
                else:
                    seen[key] = task.title
        return warnings

    def handle_recurrence(self, task: Task, pet: Pet):
        """If a daily/weekly task is complete, schedule the next occurrence."""
        if task.frequency == "daily":
            pet.add_task(Task(
                title=task.title,
                duration_minutes=task.duration_minutes,
                priority=task.priority,
                frequency=task.frequency,
                scheduled_time=task.scheduled_time,
                due_date=task.due_date + timedelta(days=1)
            ))
        elif task.frequency == "weekly":
            pet.add_task(Task(
                title=task.title,
                duration_minutes=task.duration_minutes,
                priority=task.priority,
                frequency=task.frequency,
                scheduled_time=task.scheduled_time,
                due_date=task.due_date + timedelta(weeks=1)
            ))

    def generate_schedule(self) -> list:
        """Return today's incomplete tasks sorted by scheduled time."""
        today = date.today()
        todays_tasks = [
            t for t in self.get_all_tasks()
            if not t.completed and t.due_date == today
        ]
        return sorted(todays_tasks, key=lambda t: t.scheduled_time)