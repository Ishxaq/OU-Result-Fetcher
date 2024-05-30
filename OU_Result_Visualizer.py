import pandas as pd
import matplotlib.pyplot as plt
def Failed_Students_Bar() :
    # Load the data from the Excel file
    file_path = r"E:\student_results.xlsx"  # Use a raw string to avoid escape sequence issues
    data = pd.read_excel(file_path)

    # Print column names to verify them
    print("Column names:", data.columns.tolist())

    # Specify the subject names you want to analyze
    subjects_to_analyze = [
        "OOP USING JAVA", 
        "DISCRETE MATHEMATICS", 
        "DATA STRUCTURES AND ALGORITHMS", 
        "OPERATIONS RESEARCH", 
        "BASIC ELECTRONICS", 
        "DIGITAL ELECTRONICS"
    ]

    # Check the actual column names for "Grade Secured" and "Subject Name"
    grade_secured_col = "Grade Secured"  # Adjust this if the printed column names show a different name
    subject_name_col = "Subject Name"    # Adjust this if the printed column names show a different name

    # Filter the data to include only the rows with the specified subject names
    filtered_data = data[data[subject_name_col].isin(subjects_to_analyze)]

    # Count the number of students who failed (Grade secured is 'F') for each subject name
    failed_counts = filtered_data[filtered_data[grade_secured_col] == 'F'][subject_name_col].value_counts()

    # Create a bar chart
    plt.figure(figsize=(12, 8))
    bars = failed_counts.plot(kind='bar', color='red')
    plt.title("Number of Students Failed in Specified Subjects of CSE-B")
    plt.xlabel("Subject Name")
    plt.ylabel("Number of Students Failed")
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', linewidth=0.7)

    # Display the number of students on top of each bar
    for bar in bars.patches:
        bars.annotate(format(bar.get_height(), '.0f'),
                    (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    ha='center', va='center', xytext=(0, 8),
                    textcoords='offset points')

    plt.tight_layout()
    plt.show()

# Failed_Students_Bar()
def Overall_Passed_PieChart():


    # Load the data from the Excel file
    file_path = r"E:\student_results.xlsx"
    data = pd.read_excel(file_path)

    # Print column names to verify them
    print("Column names:", data.columns.tolist())

    # Ensure that the column names for "Hall Ticket No." and "Final Result" are correct
    hall_ticket_col = "Hall Ticket No."  # Adjust if necessary
    final_result_col = "3rd Sem"    # Adjust if necessary

    # Drop duplicate entries based on the Hall Ticket No. to ensure each student is counted only once
    unique_students = data.drop_duplicates(subset=[hall_ticket_col])

    # Count the number of students who are promoted and those who passed
    promoted_count = unique_students[unique_students[final_result_col].str.startswith('PROMOTED')].shape[0]
    total_students = unique_students.shape[0]
    passed_count = total_students - promoted_count

    # Data for the pie chart
    labels = ['Promoted', 'Passed']
    sizes = [promoted_count, passed_count]
    colors = ['lightcoral', 'lightskyblue']
    explode = (0.1, 0)  # explode the 'Promoted' slice slightly

    # Create a pie chart
    plt.figure(figsize=(8, 8))
    patches, texts, autotexts = plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%',
                                        shadow=True, startangle=140, textprops=dict(color="w"))

    # Add legend with counts
    legend_labels = [f'{label}: {count}' for label, count in zip(labels, sizes)]
    plt.legend(patches, legend_labels, loc="best")

    # Title and formatting
    plt.title('Overall Student Promotion and Passing Status of CSE-B')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

Overall_Passed_PieChart();
Failed_Students_Bar();
