# Multi-Customer ATM Simulator

A console-based Python application that simulates an ATM terminal capable of sequentially processing multiple customer sessions while maintaining global transactional telemetry.

##  Key Features
* **Multi-Customer Processing:** Designed to process an explicit number of distinct customer sessions in a single execution run using a sequential flow.
* **Input Validation & Guard Rails:** Includes robust recursive input validation loops to catch errors, preventing users from making negative deposits/withdrawals or overdrawing beyond their balance.
* **Core Banking Operations:** Supports balance check, input-validated cash deposits, and balance-verified cash withdrawals.
* **Comprehensive Analytics & Telemetry:** 
  * Tracks individual customer session metrics (transaction counts per user).
  * Aggregates global bank metrics (total customers processed, total banking-wide deposits, total banking-wide withdrawals, and cumulative transactions).

## Tech Stack & Programming Concepts
* **Language:** Python 3.x
* **Control Structures:** Nested loops utilizing structured `for` loops for user iteration alongside `while` loops for continuous session management and runtime data validation.
* **Conditional Logic:** Evaluates multi-branch operational paths using sequential `if-elif-else` code architecture.
* **Data Tracking:** Implements atomic counter variables to manage arithmetic logic updates across local and global scopes.

## How To Run
1. Clone or download this repository to your computer.
2. Open your terminal or command prompt in the folder containing the file.
3. Run the following command:
   ```bash
   python "ATM Simulation.py"
   ```
