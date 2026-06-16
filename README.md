# How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/BloodIGRIS/AI-Vision.git
cd AI-Vision
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

## 3. Activate the Virtual Environment

### Windows

```powershell
.\venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

```bash
pip install streamlit ultralytics opencv-python pandas pillow
```

## 5. Run the Application

```bash
streamlit run app.py
```

## 6. Open in Browser

```
http://localhost:8501
```

The application will automatically open in your browser.

## Model File

The project uses:

```
yolov8n.pt
```

Make sure this file remains in the project root directory.
