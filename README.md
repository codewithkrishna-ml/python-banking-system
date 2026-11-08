# Core Bank Account Management System 🏦💳

A robust, enterprise-inspired core banking simulation engine engineered in Python using advanced **Object-Oriented Programming (OOP)** patterns. This application models a secure financial institute's operational database, orchestrating account instantiation, deposits, transfers, and secure balance tracking via strict validation pipelines.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML) -> **Aspiring ML Engineer at Google / Microsoft** 🤖⚡
*   **Milestone:** Successfully crushed the **100 Days of Code** challenge!
*   **Current Sprint:** Learning Data Structures & Algorithms (DSA) and building data science foundations with **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Secure Data Encapsulation:** Protects internal account values and critical variables from external mutations by restricting visibility to authorized methods only.
*   **Dynamic Account Provisioning:** Dynamically handles independent runtime creation loops for specific account types (e.g., Savings, Current) backed by automated sequential account number generation.
*   **Transaction Guardrails:** Features strict double-entry verification gates that block withdrawal actions instantly if the requested amount triggers a sub-zero overdraft violation.
*   **Real-Time Statement Dashboard:** Compiles precise ledger balances on the fly, rendering clean interactive receipts and comprehensive customer logs instantly upon query.

---

## 🛠️ OOP Concepts & Engineering Architecture

This financial prototype serves as a strict proof-of-concept for secure state distribution and modular software architecture:
*   **Advanced Encapsulation:** Implements private structural properties (e.g., `__balance`, `__account_number`) using double-underscore prefixes to shield production states behind secure getter/setter mechanisms.
*   **Composition & Multi-Tier Mapping:** The master registry database orchestrates operational references seamlessly by aggregation—housing collections of autonomous `Account` and `Customer` objects inside unified system arrays.
*   **Hierarchical Constructors (`__init__`):** Relies heavily on constructors to automatically seed base interest weights, operational flags, and default verification schemas during initialization.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd python-banking-system-oop
    ```
3.  **Run the core terminal ledger script:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Runs natively on pure Python core structures without requiring external third-party library installations.
