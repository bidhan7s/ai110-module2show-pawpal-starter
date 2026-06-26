from datetime import date
import pytest
from pawpal_system import Owner, Pet, Task, Scheduler


@pytest.fixture
def setup():
    owner = Owner("Tester")
    pet = Pet("Buddy", "dog")
    owner.add_pet(pet)
    return owner, pet, Scheduler(owner)


def test_mark_complete_changes_status(setup):
    _, pet, _ = setup
    task = Task("Walk", 20, "high", "daily", "08:00", due_date=date.today())
    pet.add_task(task)
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_count(setup):
    _, pet, _ = setup
    before = len(pet.tasks)
    pet.add_task(Task("Feeding", 10, "high", "daily", "09:00", due_date=date.today()))
    assert len(pet.tasks) == before + 1


def test_sort_by_time_is_chronological(setup):
    _, pet, scheduler = setup
    pet.add_task(Task("Evening", 20, "low",    "daily", "17:00", due_date=date.today()))
    pet.add_task(Task("Morning", 20, "high",   "daily", "08:00", due_date=date.today()))
    pet.add_task(Task("Midday",  20, "medium", "daily", "12:00", due_date=date.today()))
    times = [t.scheduled_time for t in scheduler.sort_by_time()]
    assert times == sorted(times)


def test_conflict_detection(setup):
    _, pet, scheduler = setup
    pet.add_task(Task("Walk",       20, "high", "daily", "08:00", due_date=date.today()))
    pet.add_task(Task("Medication",  5, "high", "daily", "08:00", due_date=date.today()))
    assert len(scheduler.detect_conflicts()) > 0


def test_recurrence_creates_new_task(setup):
    _, pet, scheduler = setup
    task = Task("Daily walk", 20, "high", "daily", "08:00", due_date=date.today())
    pet.add_task(task)
    task.mark_complete()
    scheduler.handle_recurrence(task, pet)
    assert len(pet.tasks) == 2
    assert pet.tasks[1].completed is False