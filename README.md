# ⚙️ Expense Tracker Backend

A scalable and secure backend API built for the Expense Tracker application. It handles user authentication, transaction management, and financial analytics using modern backend technologies.

---

## 🚀 Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi" />
  <img src="https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb" />
  <img src="https://img.shields.io/badge/JWT-Authentication-black" />
  <img src="https://img.shields.io/badge/Pydantic-Validation-green" />
</p>

---

## ✨ Features

- 🔐 User Authentication (Register / Login)
- 🔑 Secure JWT-based Authorization
- 🔒 Password Hashing for security
- ➕ Add, Update & Delete Transactions
- 📊 Monthly, Quaterly, Yearly & Category-wise Analytics
- 🔍 Filter Transactions
- ⚡ High-performance APIs with FastAPI
- 🌐 RESTful API architecture

---

## 💡 Project Motivation

This backend was built to handle real-world challenges of managing user data and financial transactions securely and efficiently.

The goal was to create a scalable API that can:
- Handle authentication securely
- Manage structured financial data
- Provide analytics for better insights
- Support a production-ready frontend application

---

## 📡 API Endpoints

### 👤 User Routes
- `POST /user/register`
- `POST /user/login`
- `POST /user/forgot-password`
- `PUT /user/reset-password`

### 💰 Transaction Routes
- `POST /tracker/add`
- `GET /tracker/all`
- `GET /tracker/all/{id}`
- `PUT /tracker/update/{id}`
- `DELETE /tracker/delete/{id}`

### 📊 Analytics
- `GET /tracker/balance`
- `GET /tracker/filter/{type}`
- `GET /tracker/monthly`
- `GET /tracker/yearly`
- `GET /tracker/quaterly`

---

## 🌐 Live API

👉 https://your-backend-url.onrender.com

---

## 📁 Project Structure
