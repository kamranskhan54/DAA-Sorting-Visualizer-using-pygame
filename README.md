# 🎯 DAA Sorting Visualizer

A graphical mini-project developed using **Python and Tkinter** for the subject **Design and Analysis of Algorithms (DAA)**. This application visually demonstrates how different sorting algorithms arrange numbers in ascending order through animated numbered boxes.

## 📌 Project Overview

Understanding sorting algorithms can be challenging when learning only through theory and code. This project provides a graphical interface that allows users to select a sorting algorithm, enter their own numbers, and observe the sorting process step by step.

## ✨ Features

* **Five Sorting Algorithms:** Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort.
* **Graphical User Interface:** A dark-themed interface built with Tkinter.
* **Animated Visualization:** Displays numbers inside boxes while sorting takes place.
* **Comparison Highlights:** Highlights numbers being compared.
* **Swap and Move Highlights:** Uses different colors to indicate changes to the array.
* **Performance Counters:** Displays the number of comparisons and moves.
* **User Input:** Allows users to enter their own numbers.
* **Playback Controls:** Start, Pause, and Reset buttons.
* **Real-Time Animation:** Uses Tkinter's `after()` method to update the visualization.

## 🛠️ Technologies Used

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Main programming language    |
| Tkinter    | Graphical user interface     |
| Canvas     | Drawing numbered boxes       |
| `after()`  | Controlling animation timing |

## 📂 Project Structure

```text
DAA-Sorting-Visualizer/
│
├── main.py
└── README.md
```

## ⚙️ Requirements

* Python 3.x
* Tkinter (usually included with standard Python installations)

**No external Python packages are required** for this project.

## 🚀 Installation and Execution

### Step 1: Install Python

Install Python 3 from the official website if it is not already installed.

### Step 2: Save the Code

Save the complete project code in a file named `main.py`.

### Step 3: Open the Terminal

Open the project folder in VS Code and open its integrated terminal.

### Step 4: Run the Application

Execute the following command:

```bash
python main.py
```

The Sorting Visualizer window will open.

## 🖥️ How to Use

1. Launch the application.
2. Select one of the five sorting algorithms from the dropdown menu.
3. Enter numbers separated by commas or spaces.
4. Click **START** to begin the animation.
5. Observe the highlighted boxes as the algorithm compares and rearranges numbers.
6. Check the comparison and move counters.
7. Click **PAUSE** to stop the animation temporarily.
8. Click **RESET** to clear the current animation and display the entered array again.

**Example input:**

```text
8, 3, 5, 1, 9, 2
```

The application supports up to 15 integers at a time.

## 🧮 Sorting Algorithms

### 1. Bubble Sort

Compares adjacent elements and swaps them when they are in the wrong order.

* Best-case time complexity: O(n) with an optimized implementation.
* Average-case time complexity: O(n²).
* Worst-case time complexity: O(n²).

### 2. Selection Sort

Finds the smallest element in the unsorted portion and places it in the correct position.

* Best-case time complexity: O(n²).
* Average-case time complexity: O(n²).
* Worst-case time complexity: O(n²).

### 3. Insertion Sort

Builds a sorted portion of the array by inserting each new element into its correct position.

* Best-case time complexity: O(n).
* Average-case time complexity: O(n²).
* Worst-case time complexity: O(n²).

### 4. Merge Sort

Divides the array into smaller parts, sorts them recursively, and merges the sorted parts.

* Best-case time complexity: O(n log n).
* Average-case time complexity: O(n log n).
* Worst-case time complexity: O(n log n).

### 5. Quick Sort

Selects a pivot element, partitions the array around the pivot, and recursively sorts the partitions.

* Best-case time complexity: O(n log n).
* Average-case time complexity: O(n log n).
* Worst-case time complexity: O(n²).

## 🎨 Color Indicators

| Color    | Meaning                       |
| -------- | ----------------------------- |
| Blue     | Normal array element          |
| Yellow   | Elements being compared       |
| Red/Pink | Element involved in a change  |
| Green    | Sorting completed             |
| Cyan     | Status and action information |

## 🎓 Educational Objectives

The objectives of this project are to:

* Understand the working of sorting algorithms.
* Compare the behavior of different sorting techniques.
* Visualize comparisons, swaps, and element movements.
* Understand the relationship between algorithms and their time complexity.
* Apply Python programming concepts to develop a graphical application.

## 🔮 Future Enhancements

Possible improvements include:

* Adding a sorting speed control.
* Displaying time complexity and space complexity in the interface.
* Showing the final sorted array separately.
* Adding execution-time measurements.
* Supporting larger arrays with a scrollable visualization.
* Adding additional algorithms such as Heap Sort and Counting Sort.

## 👨‍🎓 Academic Project

**Project Title:** DAA Sorting Visualizer
**Subject:** Design and Analysis of Algorithms
**Language:** Python
**Project Type:** Academic Mini-Project

---

*This project is intended for educational purposes and demonstrates the working of sorting algorithms through graphical animation.*
ch
