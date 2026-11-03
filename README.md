# 🛡️ CrowdShield AI

### AI-Powered Crowd Monitoring, Detection & Tracking System

## Overview

CrowdShield AI is an intelligent crowd monitoring system built using computer vision and deep learning. It uses the YOLO11 object detection model and ByteTrack object tracking to detect, count, and track people in recorded surveillance videos.

The system assigns unique tracking IDs to detected individuals, helping prevent duplicate counting and providing useful crowd analytics through an interactive Streamlit dashboard or a standalone OpenCV interface.

CrowdShield is designed for applications in smart cities, transportation hubs, public events, shopping malls, educational institutions, and other public spaces.

## Features

- **AI-Based Person Detection:** Detects people using the YOLO11 model.
- **Crowd Counting:** Displays current crowd count and total unique people detected.
- **Multi-Object Tracking:** Uses ByteTrack to assign unique IDs to individuals.
- **Duplicate Counting Prevention:** Tracks individuals across video frames.
- **Video Processing:** Supports recorded surveillance videos.
- **Bounding Box Visualization:** Displays detection boxes and unique tracking IDs.
- **Crowd Analytics:** Displays crowd statistics and processing performance.
- **Threat Monitoring:** Provides crowd-level monitoring and threshold-based alerts.
- **Interactive Dashboard:** Red-and-black cybersecurity-inspired Streamlit interface.
- **Processed Video Export:** Allows users to view and download processed videos.
- **Dual Execution Modes:** Supports standalone backend execution and a Streamlit web dashboard.
- **CPU-Friendly Processing:** Supports execution on CPU-compatible environments.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| YOLO11 | Person detection |
| Ultralytics | YOLO model framework |
| OpenCV | Video processing and visualization |
| ByteTrack | Multi-object tracking |
| NumPy | Numerical operations |
| Streamlit | Interactive web dashboard |
| imageio-ffmpeg | Processed video encoding |

## Project Structure

```text
CrowdShield/
│
├── assets/
│   └── logo.png
│
├── backend/
│   ├── alert.py
│   ├── density.py
│   ├── detect.py
│   ├── extract_frame.py
│   ├── prediction.py
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
├── models/
│   └── yolo11n.pt
│
├── uploads/
│   └── metro1.mp4
│
├── outputs/
│   └── processed videos
│
├── videos/
│   ├── .gitignore
│   └── frame.jpg
│
├── README.md
└── .gitignore
```

**Note:** Virtual environment folders such as `.venv`, `.venv312`, and `venv` are excluded from the GitHub repository.

## Installation

### 1. Clone the Repository

```powershell
git clone https://github.com/Ketoenol/CrowdShield.git
cd CrowdShield
```

### 2. Create a Virtual Environment

Python 3.12 is recommended.

```powershell
python -m venv .venv
```

### 3. Activate the Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

The requirements file is located inside the backend directory.

```powershell
pip install -r backend/requirements.txt
```

### 5. Ensure the YOLO Model Is Available

Make sure the YOLO11 model weights are present at:

```text
models/yolo11n.pt
```

## Running CrowdShield

CrowdShield supports two execution modes. Both use the same YOLO11 and ByteTrack detection backend.

### Mode 1: Standalone Backend (OpenCV)

Run the detection engine directly without launching the Streamlit dashboard.

```powershell
python backend/detect.py
```

**Features:**

- Live video processing through an OpenCV window.
- YOLO11 person detection.
- ByteTrack multi-object tracking with unique IDs.
- Real-time current crowd count.
- Total unique people tracked.
- Processing FPS display.
- Processed video export.

**Default input video:**

```text
uploads/metro1.mp4
```

**Output video:**

```text
outputs/metro1_processed.mp4
```

Press `Q` or `Esc` to close the detection window.

### Mode 2: Web Dashboard (Streamlit)

Launch the interactive CrowdShield web application.

```powershell
streamlit run frontend/app.py
```

Open the dashboard in your browser:

```text
http://localhost:8501
```

**Features:**

- Interactive CrowdShield dashboard.
- Video upload and processing.
- YOLO11 person detection.
- ByteTrack tracking visualization.
- Crowd analytics and monitoring.
- Current crowd statistics.
- Processed video playback.
- Downloadable detection results.

## How It Works

1. **Video Input:** Provide surveillance footage through the standalone backend or upload it through the Streamlit dashboard.
2. **Person Detection:** The backend processes video frames using YOLO11.
3. **Object Tracking:** ByteTrack assigns unique IDs to detected individuals across frames.
4. **Visual Tracking:** Bounding boxes and tracking IDs are displayed on the processed video.
5. **Crowd Analytics:** The system calculates crowd statistics, including current crowd count and total unique people detected.
6. **Results:** Processed footage and detection statistics are generated and made available through the selected execution mode.

## Dashboard Features

CrowdShield provides a Security Operations Centre-style interface featuring:

- Crowd intelligence overview.
- Surveillance video processing.
- Person detection and tracking visualization.
- Current crowd statistics.
- Total unique people detected.
- Processing FPS and frame statistics.
- Crowd-level monitoring and alerts.
- Processed video playback and download.

## Applications

- Smart City Surveillance
- Railway and Metro Stations
- Airports and Bus Terminals
- Public Events and Festivals
- Shopping Malls
- Educational Campuses
- Public Safety Monitoring

## Future Enhancements

- Live CCTV camera integration.
- Real-time crowd density estimation using calibrated camera regions.
- Advanced overcrowding and anomaly detection.
- Heatmap-based crowd visualization.
- Automated alert notifications.
- Multi-camera surveillance support.
- Historical crowd analytics and reporting.

## Author

**Shivam Singh**

GitHub: [@Ketoenol](https://github.com/Ketoenol)

## License

This project is developed for educational and research purposes.

---

**CrowdShield AI — Intelligent Crowd Monitoring for Safer Public Spaces.**