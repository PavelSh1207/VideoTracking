# Football Video Tracking and Smart Zoom

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)  

A lightweight Python toolkit for detecting, tracking, and generating zoom-in replays in football (soccer) videos, powered by **YOLOv8**.

## Table of Contents

1. [Features](#features)  
2. [Directory Layout](#directory-layout)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [Usage](#usage)  
   - [Quick Start](#quick-start)  
   - [Running Modules Individually](#running-modules-individually)  
6. [Configuration](#configuration)  
7. [Contributing](#contributing)  
8. [License](#license)  

## Features

- **Object Detection & Tracking**  
  Uses Ultralytics YOLOv8 for robust player and ball detection.  
- **Automatic Moving Zoom**  
  Smoothly recenters and zooms to follow on-field action.  
- **Frame-level Video Utilities**  
  Read, write, annotate, and process individual frames with OpenCV.  
- **Pretrained Weights Included**  
  Ready-to-use `yolov8x.pt` model for immediate experimentation.

## Directory Layout

```
Football/
├── main.py                      # End-to-end demo: detection → tracking → zoom → output
├── MovingZoom.py                # Core moving-zoom logic
├── zoom.py                      # Helper functions for zoom window management
├── tracking_yolo_v8.py          # YOLOv8 detection & tracking wrapper
├── moduls_for_works_with_video.py # Video I/O and annotation utilities
├── oldmain.py                   # Legacy script (for reference)
└── yolov8x.pt                   # Pretrained YOLOv8 weights
```

## Requirements

- Python 3.9 or higher  
- [numpy](https://pypi.org/project/numpy/)  
- [opencv-python](https://pypi.org/project/opencv-python/)  
- [ultralytics](https://github.com/ultralytics/ultralytics)  
- [supervision](https://github.com/roboflow/supervision)  

Install with:

```bash
pip install numpy opencv-python ultralytics supervision
```

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/Football.git
cd Football
pip install -r requirements.txt  # or install manually as above
```

## Usage

### Quick Start

Process an input video and generate a zoomed highlight clip:

```bash
python main.py --video input.mp4
```

Output:
- `movingZoomN.mp4` in the project root, where `N` is the run index.

### Running Modules Individually

You can also invoke the core modules directly:

```bash
python MovingZoom.py --video input.mp4
python tracking_yolo_v8.py --video input.mp4
```

Each script accepts the same `--video` argument and offers additional flags; run with `-h` for details.

## Configuration

You can customize parameters by editing constants at the top of each module (e.g. zoom window size, tracking confidence thresholds). Future releases may include a centralized config file.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repo.  
2. Create a feature branch (`git checkout -b feature/YourFeature`).  
3. Commit your changes (`git commit -m "Add feature X"`).  
4. Push to the branch (`git push origin feature/YourFeature`).  
5. Open a Pull Request.  

Please ensure your code adheres to PEP8 and include tests for new functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
