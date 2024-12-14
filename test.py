import pandas as pd
import streamlit as st

# Load the DataFrame
df = pd.read_csv("all_rooms_schedule.csv", encoding="utf-8-sig")

# Get unique days and hours
unique_days = df['Day Name'].unique().tolist()
unique_hours = sorted(df['Hour'].unique().tolist())
all_option = "All"

day_options = [all_option] + unique_days
hour_options = [all_option] + [str(h) for h in unique_hours]
room_prefix_options = ["Any", "(مع ح", "(ح"]

def combined_filter(
    selected_days,
    selected_hours,
    room_prefix,
    room_name_filter,
    day_name_filter,
    hour_filter,
    course_name_filter,
    instructor_filter,
    only_empty
):
    filtered = df.copy()

    # Filter by selected days
    if all_option not in selected_days:
        filtered = filtered[filtered['Day Name'].isin(selected_days)]

    # Filter by selected hours
    if all_option not in selected_hours:
        chosen_hours = [int(h) for h in selected_hours]
        filtered = filtered[filtered['Hour'].isin(chosen_hours)]

    # Filter by room prefix
    if room_prefix != "Any":
        # Here we check if the room name contains the prefix
        # (If they truly must start with it, use .startswith instead)
        filtered = filtered[filtered['Room Name'].str.contains(room_prefix, na=False, regex=False)]

    # Apply other text filters
    if room_name_filter.strip():
        filtered = filtered[filtered['Room Name'].str.contains(room_name_filter, case=False, na=False)]
    if day_name_filter.strip():
        filtered = filtered[filtered['Day Name'].str.contains(day_name_filter, case=False, na=False)]
    if hour_filter.strip():
        filtered = filtered[filtered['Hour'].astype(str).str.contains(hour_filter, case=False, na=False)]
    if course_name_filter.strip():
        filtered = filtered[filtered['Course Name'].str.contains(course_name_filter, case=False, na=False)]
    if instructor_filter.strip():
        filtered = filtered[filtered['Instructor'].str.contains(instructor_filter, case=False, na=False)]

    # Filter for empty classes
    if only_empty:
        filtered = filtered[filtered['Course Name'] == "Empty"]

    return filtered if not filtered.empty else pd.DataFrame({"Message": ["No results found."]})


# --- Streamlit UI ---
st.title("Combined Filters: Multiple Selections and Text Filters")

# Days and Hours
st.subheader("Select Days and Hours:")
selected_days = st.multiselect("Select Days (can choose multiple or 'All')", day_options, default=[all_option])
selected_hours = st.multiselect("Select Hours (can choose multiple or 'All')", hour_options, default=[all_option])

# Room Prefix
st.subheader("Select Room Prefix:")
room_prefix = st.selectbox("Room Prefix Filter", room_prefix_options, index=0)

# Text Filters
st.subheader("Text Filters (optional):")
col1, col2 = st.columns(2)
with col1:
    room_name_filter = st.text_input("Room Name Filter (substring)")
    day_name_filter = st.text_input("Day Name Filter (substring)")
with col2:
    hour_filter = st.text_input("Hour Filter (substring)")
    course_name_filter = st.text_input("Course Name Filter (substring)")

instructor_filter = st.text_input("Instructor Filter (substring)")

only_empty = st.checkbox("Show Only Empty Classes", value=False)

# Filter button
if st.button("Filter"):
    result_df = combined_filter(
        selected_days=selected_days,
        selected_hours=selected_hours,
        room_prefix=room_prefix,
        room_name_filter=room_name_filter,
        day_name_filter=day_name_filter,
        hour_filter=hour_filter,
        course_name_filter=course_name_filter,
        instructor_filter=instructor_filter,
        only_empty=only_empty
    )
    st.dataframe(result_df)
import asyncio

async def async_task(name, delay):
    print(f"Task {name}: Starting after a delay of {delay} seconds")
    await asyncio.sleep(delay)
    print(f"Task {name}: Completed after {delay} seconds")

async def main():
    # Schedule multiple tasks to run concurrently
    task1 = asyncio.create_task(async_task("One", 2))  # Task takes 2 seconds to complete
    task2 = asyncio.create_task(async_task("Two", 3))  # Task takes 3 seconds to complete
    
    print("Tasks are running asynchronously...")
    
    # Wait for all tasks to complete
    await task1
    await task2

    print("All tasks completed successfully.")

# Running the async main function properly
if __name__ == "__main__":
    asyncio.run(main())
