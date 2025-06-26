## 🚀 How to Run TensorFlow Document Classifier Project

---

### 🧠 Backend Setup (Flask + TensorFlow)

📂 Path:  
`D:\MACHINELEARNING\TensorFlowFinal\tensorflow-project\document_type_classifier\backend`


# Run backend server
python app.py

### 🌐 Frontend Setup (React)

📂 Path:
D:\MACHINELEARNING\TensorFlowFinal\tensorflow-project\document_type_classifier\frontend


# Start React development server(frontend)
npm start

### 🗃️ MongoDB Setup (for Learning/Testing)
## 🔗 How to Get MongoDB Atlas Connection String

To connect your FastAPI backend to MongoDB Atlas, follow these steps:

---

### 📋 Step 0: Get the Connection URI

1. Go to: [https://cloud.mongodb.com](https://cloud.mongodb.com)
2. Select your **project** and then your **cluster** (e.g., `Cluster0`)
3. Click the **"Connect"** button
4. Choose **“Connect your application”**
5. Choose:
   - **Driver**: Python
   - **Version**: 3.6 or later
6. Copy the connection string that looks like this:

mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority

---

### ✏️ Step 1: Modify the Connection String

Replace the following in the copied URI:

- `<username>` → your MongoDB username  
- `<password>` → your MongoDB password  
- Add your database name after `.net/`

✅ Example:

mongodb+srv://yourUser:yourPassword@cluster0.xxxxx.mongodb.net/taskdb?retryWrites=true&w=majority

---

### 📁 Step 2: Add to `.env` File in Backend

Create or update a `.env` file inside the backend folder:

MONGO_URI=mongodb+srv://yourUser:yourPassword@cluster0.xxxxx.mongodb.net/taskdb?retryWrites=true&w=majority


> ⚠️ Make sure `.env` is listed in `.gitignore` to keep credentials private.

---
---

## 🌐 MongoDB Atlas Access Instructions

To connect and browse your MongoDB database collections hosted on **MongoDB Atlas**, follow the steps below:

---

### 🛡️ Step 1: Configure Network Access (Allow Your IP)

 Go to: https://cloud.mongodb.com
1. Navigate to your Cluster → Network Access
2. Click "Add IP Address"
3. Click "Allow Access from Anywhere" (0.0.0.0/0) or add your own IP
4. Save

### 🗃️ Step 2: Create or Use Existing Database

   Go to: Clusters → Collections
 If the database (e.g., taskdb) already exists:
  ✔️ You can directly view collections like 'tasks'
 Else:
  ➕ Click "Add My Own Data" to create your first DB and collection

### 🔁 Step 3: Refresh or View Collection Data

 In Atlas UI:
 1. Go to Clusters → Browse Collections
 2. Select your database (e.g., taskdb)
 3. Select collection (e.g., tasks)
 4. Click "Refresh" icon to reload data


