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
        pass


@dataclass
class Pet:
    """Represents a pet with a list of care tasks."""
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        pass

    def remove_task(self, task: Task):
        """Remove a task from this pet's task list."""
        pass


class Owner:
    """Represents a pet owner who manages multiple pets."""

    def __init__(self, name: str):
        self.name = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's list."""
        pass

    def get_all_tasks(self) -> list:
        """Return every task across all pets."""
        pass


class Scheduler:
    """The brain — retrieves, sorts, filters, and manages tasks."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> list:
        """Get all tasks from all pets."""
        pass

    def sort_by_time(self) -> list:
        """Return tasks sorted chronologically by scheduled_time."""
        pass

    def filter_tasks(self, pet_name=None, completed=None) -> list:
        """Filter tasks by pet name and/or completion status."""
        pass

    def detect_conflicts(self) -> list:
        """Return warning messages for tasks scheduled at the same time."""
        pass

    def handle_recurrence(self, task: Task, pet: Pet):
        """If a daily/weekly task is complete, schedule the next occurrence."""
        pass

    def generate_schedule(self) -> list:
        """Return today's incomplete tasks sorted by scheduled time."""
        pass