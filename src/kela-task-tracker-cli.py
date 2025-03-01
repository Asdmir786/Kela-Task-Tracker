"""
Task Tracker CLI
================

This module implements a command line interface (CLI) application for tracking and managing tasks. It provides a practical tool to add, update, delete, and list tasks, as well as mark them as in-progress or done. The project is designed for beginners to practice programming skills such as handling user inputs, working with the filesystem, and managing data with JSON.

Overview
--------
- **Project Name:** Task Tracker
- **Description:** Build a CLI app to track what you need to do, what you have done, and what you are currently working on.
- **Difficulty:** Beginner
- **Domains:** Programming Language, CLI, Filesystem

Features & Requirements
-----------------------
- Accepts user inputs via positional arguments in the command line.
- Stores tasks in a JSON file located in the current directory. The file is created if it does not exist.
- Uses only the native file system module (no external libraries) for JSON file interactions.
- Handles errors and edge cases gracefully.

Task Properties
---------------
Each task in the tracker should include:
- **id:** A unique identifier for the task.
- **description:** A short text describing the task.
- **status:** The current status of the task. Allowed values are `todo`, `in-progress`, and `done`.
- **createdAt:** The timestamp when the task was created.
- **updatedAt:** The timestamp when the task was last updated.

Usage Examples
--------------
The CLI supports commands similar to the following examples:

    # Adding a new task
    $ task-cli add "Buy groceries"
    # Expected Output: Task added successfully (ID: 1)

    # Updating a task
    $ task-cli update 1 "Buy groceries and cook dinner"

    # Deleting a task
    $ task-cli delete 1

    # Marking a task as in progress or done
    $ task-cli mark-in-progress 1
    $ task-cli mark-done 1

    # Listing tasks
    $ task-cli list
    $ task-cli list done
    $ task-cli list todo
    $ task-cli list in-progress

Getting Started
---------------
1. **Set Up Your Development Environment:** Choose your preferred programming language (e.g., Python) and ensure you have an IDE or code editor installed.
2. **Project Initialization:** 
   - Create a new project directory.
   - Initialize version control (e.g., using Git).
3. **Implementing Features:** 
   - Start by setting up the CLI structure to accept user inputs.
   - Implement adding, listing, updating, and status marking functionalities incrementally.
4. **Testing and Debugging:** 
   - Test each feature to verify the JSON file correctly stores and updates task data.
   - Handle errors and edge cases gracefully.
5. **Finalization:** 
   - Refine the code and add comments/documentation.
   - Write a comprehensive README explaining how to use the Task Tracker CLI.

By completing this project, you gain valuable hands-on experience in building a CLI application, managing JSON data, and improving overall programming proficiency.

Happy coding!
"""
