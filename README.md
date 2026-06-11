# Advanced Detection of Vitamin Deficiencies Through Deep Learning Techniques

## Overview

This project is a Deep Learning-based web application developed using Django, TensorFlow, and OpenCV to detect vitamin deficiencies from images.

The system analyzes visual symptoms present in different parts of the human body such as:

* Eyes
* Skin
* Lips
* Tongue
* Nails

The objective is to provide a non-invasive and low-cost preliminary screening tool for vitamin deficiency detection.

---

## Features

* Upload image through web interface
* Deep Learning-based prediction
* User-friendly interface
* Real-time image processing
* Detection of multiple vitamin deficiencies

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Django
* Python

### Deep Learning

* TensorFlow
* Keras
* OpenCV

---

## Project Structure

```text
Advanced-Vitamin-Deficiency-Detection/
│
├── web_app/
│   ├── manage.py
│   ├── model.h5
│   ├── new_app/
│   ├── new_project/
│   ├── templates/
│   └── assests/
│
├── model/
│   └── Vitamin_Defficiency.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Dataset

The model was trained using images representing various vitamin deficiency symptoms and normal conditions.

Classes include:

* Vitamin A Deficiency
* Vitamin B Deficiency
* Vitamin C Deficiency
* Vitamin D Deficiency
* Normal

---

## Future Improvements

* User authentication system
* Cloud deployment
* Improved dataset size
* Mobile application integration
* Higher prediction accuracy

---

## Author

G Pavan Kumar
