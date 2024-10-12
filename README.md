# 📚 Student Management System using FastAPI

This is a simple **Student Management System** built using **FastAPI**. It supports basic CRUD operations such as adding, updating, viewing, and deleting student information. This system can be useful in educational institutes for managing student records.

---
<strong>![website](https://github.com/user-attachments/assets/54cceeb9-c11e-4746-95ca-85fa5156c7b2) Live site: </strong>: <a href="https://student-management-system-yc82.onrender.com/">@Student-Management-System</a>

---

## 🚀 Features

- **Add a new student** 📥
- **View all students** 👀
- **View a specific student by ID** 🔍
- **Update student information (partial updates)** ✏️
- **Delete a student** 🗑️

---

## 🛠️ Requirements

- Python 3.7+
- FastAPI
- Uvicorn

---

## 📦 Setup and Installation

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/naimur-naiyimu/Student-Management-System-using-FastAPI.git
cd student-management-system
```
### 2. Create and activate a virtual environment
For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
For Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install the dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the FastAPI application
```bash
uvicorn app.main:app --reload
```
<h2>Now open your browser and go to:</h2>
<ul>
    <li><strong>API documentation:</strong> <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a></li>
    <li><strong>Interactive API:</strong> <a href="http://127.0.0.1:8000/redoc">http://127.0.0.1:8000/redoc</a></li>
</ul>

<h2>📋 API Endpoints</h2>
<table>
    <thead>
        <tr>
            <th>Method</th>
            <th>Endpoint</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>POST</td>
            <td>/students/</td>
            <td>Add a new student</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/students/</td>
            <td>Retrieve all students</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/students/{student_id}</td>
            <td>Retrieve a specific student by ID</td>
        </tr>
        <tr>
            <td>PATCH</td>
            <td>/students/{student_id}</td>
            <td>Partially update student information</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>/students/{student_id}</td>
            <td>Delete a student</td>
        </tr>
    </tbody>
</table>

<h2>👨‍💻 Example Usage</h2>

<h3>1. Add a Student:</h3>
<p><strong>Request:</strong></p>
<pre><code>POST /students/</code></pre>
<p><strong>Request Body:</strong></p>
<pre><code>{
    "name": "John Doe",
    "age": 20,
    "gender": "Male",
    "Class": "10th Grade",
    "address": "123 Elm Street",
    "contact_info": "123-456-7890"
}</code></pre>

<h3>2. Get All Students:</h3>
<p><strong>Request:</strong></p>
<pre><code>GET /students/</code></pre>

<h3>3. Update a Student:</h3>
<p><strong>Request:</strong></p>
<pre><code>PATCH /students/1</code></pre>
<p><strong>Request Body (partial update):</strong></p>
<pre><code>{
    "address": "456 Oak Avenue"
}</code></pre>

<h2>📜 License</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for more details.</p>

<h2>🛡️ Contributions</h2>
<p>Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.</p>

<h2>📝 Contact</h2>
<p>For any inquiries or issues, feel free to reach out at:</p>
<ul>
    <li><strong>Email</strong>: naimur.naiyimu@gmail.com</li>
    <li><strong>GitHub</strong>: <a href="https://github.com/naimur-naiyimu">@naimur-naiyimu</a></li>
</ul>
