import streamlit as st
from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# --- Session State Setup ---
if "owner" not in st.session_state:
    st.session_state.owner = None
if "scheduler" not in st.session_state:
    st.session_state.scheduler = None

# --- Owner + Pet Setup ---
st.subheader("👤 Owner & Pet Info")
owner_name = st.text_input("Owner name", placeholder="Enter owner name")
pet_name   = st.text_input("Pet name", placeholder="Enter pet name")
species    = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Set Owner & Pet"):
    owner = Owner(owner_name)
    pet   = Pet(pet_name, species)
    owner.add_pet(pet)
    st.session_state.owner     = owner
    st.session_state.scheduler = Scheduler(owner)
    st.success(f"✅ {owner_name} and {pet_name} ({species}) are ready!")

st.divider()

# --- Add Tasks ---
st.subheader("📋 Add a Task")

if st.session_state.owner is None:
    st.info("Set your owner and pet above first.")
else:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (min)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
    with col4:
        frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

    scheduled_time = st.text_input("Scheduled time (HH:MM)", value="08:00")

    if st.button("Add Task"):
        pet = st.session_state.owner.pets[0]
        task = Task(
            title=task_title,
            duration_minutes=int(duration),
            priority=priority,
            frequency=frequency,
            scheduled_time=scheduled_time,
            due_date=date.today()
        )
        pet.add_task(task)
        st.success(f"✅ Added: {task_title} at {scheduled_time}")

    # Show current tasks
    all_tasks = st.session_state.scheduler.sort_by_time()
    if all_tasks:
        st.markdown("#### Current Tasks (sorted by time)")
        for t in all_tasks:
            status = "✅" if t.completed else "🔲"
            st.write(f"{status} {t.scheduled_time} — {t.title} ({t.duration_minutes} min) [{t.priority}]")
    else:
        st.info("No tasks yet. Add one above.")

st.divider()

# --- Generate Schedule ---
st.subheader("📅 Generate Schedule")

if st.button("Generate Schedule"):
    if st.session_state.scheduler is None:
        st.error("Please set up your owner and pet first.")
    else:
        scheduler = st.session_state.scheduler

        # Conflicts
        conflicts = scheduler.detect_conflicts()
        if conflicts:
            for w in conflicts:
                st.warning(w)

        # Schedule
        schedule = scheduler.generate_schedule()
        if schedule:
            st.success("Here is today's schedule:")
            for task in schedule:
                st.write(f"🔲 {task.scheduled_time} — {task.title} ({task.duration_minutes} min) [{task.priority}]")
        else:
            st.info("No tasks scheduled for today.")