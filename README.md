# 🎯 PrepTrack — Student Placement & Practice Tracking System

**PrepTrack** is a Python-based student assessment and placement eligibility tracking system. It collects student credentials, evaluates 7-day coding practice performance, categorizes performance levels, identifies critical score blockers, and provides a clear placement readiness decision along with recommended next actions.

---

## 👥 Team Directory (Team Lead Maintenance)

> [!IMPORTANT]
> **Notice**: Only the Team Lead must maintain and update this complete team directory.

| Member Name | GitHub Profile Link | PrepTrack Repository Link | Submission Status |
| :--- | :--- | :--- | :--- |
| **Vishnu Mavilla** *(Lead)* | [GitHub Profile](https://github.com/VishnuMavilla004) | [PrepTrack-Vishnu](https://github.com/VishnuMavilla004/PrepTrack-Vishnu) | `Completed` |
| S Rahul | [GitHub Profile](https://github.com/rahul777) | [Repository Link](https://github.com/rahul777-code/preptrack-rahul) | `Completed` |
| Ujwala Sree | [GitHub Profile](https://github.com/ujwalasree) | [Repository Link](https://github.com/ujwalasree/Preptrack-ujwala) | `Completed` |
| Ranjith | [GitHub Profile](https://github.com/Ranjith950) | [Repository Link](https://github.com/Ranjith950/Preptrack-ranjith/) | `Completed` |


---

## ✨ Features

- **Student Profile Validation**: Collects and validates student details (Name, Registration Number, Graduation Year [2025–2027], Attendance %, Project Completion, and Profile Verification).
- **7-Day Practice Evaluation**: 
  - Tracks scores ranging from `0` to `100`, or `-1` for absence.
  - Automatically handles absent days and computes total attempted vs. absent days.
  - Classifies daily scores into performance tiers:
    - 🟢 **Strong**: 75 – 100
    - 🔵 **Satisfactory**: 60 – 74
    - 🟡 **Needs Improvement**: 40 – 59
    - 🔴 **Critical**: 0 – 39
- **Performance Analytics**:
  - Calculates average score over attempted days (safely handling division by zero).
  - Tracks highest and lowest scores along with their respective days.
  - Detects and flags the first critical day and score.
- **Placement Decision Engine**:
  - Evaluates eligibility based on strict criteria (Attendance ≥ 75%, Attempts ≥ 6, Passed Days ≥ 4, Average ≥ 70, No Critical Scores, Project Completed, Profile Verified).
  - Determines the exact primary blocker and provides targeted next actions.
- **Detailed Terminal Report**: Generates a clean, formatted report summarizing student profile, practice breakdown, analytics, and final placement status.

---

## 📊 Evaluation Criteria & Thresholds

| Metric | Minimum Requirement | Description |
| :--- | :--- | :--- |
| **Graduation Year** | `2025` – `2027` | Must fall within the eligible cohort range. |
| **Attendance** | `≥ 75.0%` | Student must meet attendance requirements. |
| **Attempted Days** | `≥ 6 Days` | Must attempt at least 6 out of 7 practice days. |
| **Passed Days** | `≥ 4 Days` | A pass requires a score of `≥ 40`. |
| **Average Score** | `≥ 70.00` | Calculated across attempted practice days. |
| **Critical Score** | `None (0)` | Any score `< 40` triggers a critical support requirement. |
| **Project & Profile** | `Completed & Verified` | Both project submission and profile verification must be `True`. |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed on your system.

### Running the Application

1. Clone or download the repository:
   ```bash
   git clone https://github.com/VishnuMavilla004/PrepTrack-Vishnu.git
   cd PrepTrack-Vishnu
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. Follow the interactive prompts in your terminal to enter student details and 7-day practice scores.

---

## 🖥️ Example Terminal Output

```text
==================================================
              PREPTRACK REPORT
==================================================
Student Name           : Vishnu Mavilla
Registration Number    : KN2026
Graduation Year        : 2026
Attendance             : 75.0%

Attempted Days         : 7
Absent Days            : 0
Passed Days            : 7
Failed Days            : 0

Strong Days            : 5
Satisfactory Days      : 2
Needs Improvement Days : 0
Critical Days          : 0

Total Score            : 560
Average Score          : 80.00
Highest Score          : 95 (Day 7)
Lowest Score           : 65 (Day 1)

Final Status           : Ready for Mock Interview
Primary Blocker        : None
Next Action            : Proceed to placement mock interviews
==================================================
```

---

## 📁 Repository Structure

```text
PrepTrack-Vishnu/
├── main.py        # Core application script containing input validation, evaluation logic, and report output
└── README.md      # Project documentation
```

---

## 🛠️ Author

Developed by **Vishnu Mavilla** as part of the Placement Readiness & Practice Tracking initiative.