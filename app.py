import math
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# List of 98 Fourier series 
fourier_series = [
    {"num": 1, "A": 1.312, "B": 1.09, "omega": 0.56, "C": -0.38},
    {"num": 2, "A": 1.126, "B": 1.09, "omega": 0.57, "C": -0.29},
    {"num": 3, "A": 0.44, "B": 0.66, "omega": 0.59, "C": -0.19},
    {"num": 4, "A": 2.12, "B": 0.53, "omega": 0.39, "C": -1.28},
    {"num": 5, "A": 1.69, "B": -0.5, "omega": 1.78, "C": 0.27},
    {"num": 6, "A": 1.38, "B": -0.01, "omega": 1.53, "C": -0.19},
    {"num": 7, "A": 1.45, "B": 0.93, "omega": 2.58, "C": 0.37},
    {"num": 8, "A": 1.12, "B": 0.17, "omega": 1.31, "C": 0.05},
    {"num": 9, "A": 0.76, "B": 0.21, "omega": 0.41, "C": -0.36},
    {"num": 10, "A": 6.92, "B": 0.49, "omega": 1.74, "C": 0.44},
    {"num": 11, "A": 2.28, "B": -0.02, "omega": 1.61, "C": 0.14},
    {"num": 12, "A": 9.02, "B": -0.38, "omega": 1.96, "C": -0.16},
    {"num": 13, "A": 3.00, "B": 0.22, "omega": 2.98, "C": -0.21},
    {"num": 14, "A": 9.75, "B": -0.32, "omega": 1.80, "C": 0.13},
    {"num": 15, "A": 7.13, "B": -0.64, "omega": 0.55, "C": 0.24},
    {"num": 16, "A": 1.96, "B": 0.03, "omega": 4.26, "C": -0.02},
    {"num": 17, "A": 0.96, "B": 1.18, "omega": 0.56, "C": -0.39},
    {"num": 18, "A": 0.62, "B": 0.57, "omega": 0.49, "C": -0.43},
    {"num": 19, "A": 1.19, "B": 0.01, "omega": 0.30, "C": -0.23},
    {"num": 20, "A": 1.76, "B": -0.12, "omega": 3.05, "C": 0.05},
    {"num": 21, "A": 1.97, "B": -0.24, "omega": 4.39, "C": 0.008},
    {"num": 22, "A": 2.17, "B": -0.76, "omega": 3.11, "C": 0.11},
    {"num": 23, "A": 1.36, "B": -0.33, "omega": 4.37, "C": -0.07},
    {"num": 24, "A": 2.53, "B": 0.006, "omega": 0.31, "C": -1.17},
    {"num": 25, "A": 1.26, "B": 1.27, "omega": 0.58, "C": -0.29},
    {"num": 26, "A": 0.99, "B": 0.95, "omega": 0.64, "C": -0.47},
    {"num": 27, "A": 0.48, "B": 0.74, "omega": 0.68, "C": -0.38},
    {"num": 28, "A": 2.25, "B": 0.41, "omega": 0.33, "C": -1.41},
    {"num": 29, "A": 1.61, "B": -0.49, "omega": 1.74, "C": 0.24},
    {"num": 30, "A": 1.42, "B": -0.15, "omega": 1.5, "C": -0.27},
    {"num": 31, "A": 1.43, "B": 1.04, "omega": 2.58, "C": 0.25},
    {"num": 32, "A": 1.16, "B": -0.01, "omega": 1.24, "C": 0.09},
    {"num": 33, "A": 0.59, "B": 0.39, "omega": 0.47, "C": -0.17},
    {"num": 34, "A": 6.84, "B": 0.33, "omega": 1.73, "C": 0.51},
    {"num": 35, "A": 2.13, "B": -0.02, "omega": 1.69, "C": -0.05},
    {"num": 36, "A": 8.92, "B": -0.31, "omega": 1.96, "C": -0.24},
    {"num": 37, "A": 3.02, "B": 0.09, "omega": 3.04, "C": -0.02},
    {"num": 38, "A": 9.93, "B": -0.16, "omega": 1.88, "C": 0.17},
    {"num": 39, "A": 6.97, "B": -0.76, "omega": 0.52, "C": 0.06},
    {"num": 40, "A": 1.92, "B": -0.06, "omega": 4.23, "C": 0.11},
    {"num": 41, "A": 0.87, "B": 1.2,  "omega": 0.62, "C": -0.53},
    {"num": 42, "A": 0.45, "B": 0.76, "omega": 0.43, "C": -0.32},
    {"num": 43, "A": 0.99, "B": 0.14, "omega": 0.35, "C": -0.15},
    {"num": 44, "A": 1.87, "B": -0.29, "omega": 2.97, "C": -0.01},
    {"num": 45, "A": 2.12, "B": -0.19, "omega": 4.3,  "C": -0.06},
    {"num": 46, "A": 2.09, "B": -0.83, "omega": 3.14, "C": 0.2},
    {"num": 47, "A": 1.51, "B": -0.34, "omega": 4.41, "C": -0.22},
    {"num": 48, "A": 2.63, "B": 0.03, "omega": 0.31, "C": -1.06},
    {"num": 49, "A": 1.32, "B": 1.06, "omega": 0.48, "C": -0.57},
    {"num": 50, "A": 0.94, "B": 1.14, "omega": 0.57, "C": -0.36},
    {"num": 51, "A": 0.60, "B": 0.56, "omega": 0.64, "C": -0.23},
    {"num": 52, "A": 2.01, "B": 0.36, "omega": 0.32, "C": -1.36},
    {"num": 53, "A": 1.86, "B": -0.38, "omega": 1.85, "C": 0.32},
    {"num": 54, "A": 1.5,  "B": -0.14, "omega": 1.54, "C": -0.03},
    {"num": 55, "A": 1.57, "B": 1.09, "omega": 2.5,  "C": 0.3},
    {"num": 56, "A": 1.01, "B": 0.14, "omega": 1.38, "C": 0.18},
    {"num": 57, "A": 0.56, "B": 0.21, "omega": 0.35, "C": -0.39},
    {"num": 58, "A": 0.67, "B": 1.02, "omega": 0.55, "C": -0.25},
    {"num": 59, "A": 0.88, "B": 1.25, "omega": 0.60, "C": -0.41},
    {"num": 60, "A": 0.72, "B": 0.89, "omega": 0.70, "C": -0.33},
    {"num": 61, "A": 2.34, "B": 0.45, "omega": 0.35, "C": -1.52},
    {"num": 62, "A": 1.75, "B": -0.51, "omega": 1.80, "C": 0.30},
    {"num": 63, "A": 1.48, "B": -0.10, "omega": 1.48, "C": -0.31},
    {"num": 64, "A": 1.62, "B": 1.15, "omega": 2.65, "C": 0.28},
    {"num": 65, "A": 1.10, "B": 0.05, "omega": 1.30, "C": 0.11},
    {"num": 66, "A": 0.60, "B": 0.42, "omega": 0.50, "C": -0.22},
    {"num": 67, "A": 7.02, "B": 0.30, "omega": 1.78, "C": 0.55},
    {"num": 68, "A": 1.88, "B": -0.65, "omega": 1.992, "C": 1.527},
    {"num": 69, "A": 9.10, "B": -0.35, "omega": 2.00, "C": -0.20},
    {"num": 70, "A": 3.08, "B": 0.12, "omega": 3.10, "C": -0.04},
    {"num": 71, "A": 10.00,"B": -0.18, "omega": 1.90, "C": 0.22},
    {"num": 72, "A": 7.10, "B": -0.79, "omega": 0.60, "C": 0.08},
    {"num": 73, "A": 1.98, "B": -0.08, "omega": 4.30, "C": 0.14},
    {"num": 74, "A": 0.92, "B": 1.30, "omega": 0.65, "C": -0.48},
    {"num": 75, "A": 0.50, "B": 0.78, "omega": 0.45, "C": -0.37},
    {"num": 76, "A": 1.05, "B": 0.16, "omega": 0.38, "C": -0.18},
    {"num": 77, "A": 1.92, "B": -0.32, "omega": 3.00, "C": -0.02},
    {"num": 78, "A": 2.18, "B": -0.22, "omega": 4.35, "C": -0.09},
    {"num": 79, "A": 2.15, "B": -0.85, "omega": 3.20, "C": 0.23},
    {"num": 80, "A": 1.55, "B": -0.36, "omega": 4.45, "C": -0.25},
    {"num": 81, "A": 2.70, "B": 0.06, "omega": 0.33, "C": -1.10},
    {"num": 82, "A": 1.40, "B": 1.08, "omega": 0.50, "C": -0.60},
    {"num": 83, "A": 1.00, "B": 1.20, "omega": 0.60, "C": -0.40},
    {"num": 84, "A": 0.68, "B": 0.58, "omega": 0.66, "C": -0.26},
    {"num": 85, "A": 2.08, "B": 0.40, "omega": 0.36, "C": -1.40},
    {"num": 86, "A": 1.92, "B": -0.40, "omega": 1.88, "C": 0.35},
    {"num": 87, "A": 1.55, "B": -0.18, "omega": 1.56, "C": -0.05},
    {"num": 88, "A": 1.63, "B": 1.12, "omega": 2.55, "C": 0.32},
    {"num": 89, "A": 1.08, "B": 0.17, "omega": 1.40, "C": 0.20},
    {"num": 90, "A": 0.60, "B": 0.24, "omega": 0.37, "C": -0.42},
    {"num": 91, "A": 1.12, "B": 0.20, "omega": 1.45, "C": 0.22},
    {"num": 92, "A": 0.64, "B": 0.27, "omega": 0.40, "C": -0.45},
    {"num": 93, "A": 2.90, "B": 0.50, "omega": 0.42, "C": -1.30},
    {"num": 94, "A": 2.00, "B": -0.45, "omega": 1.95, "C": 0.40},
    {"num": 95, "A": 1.65, "B": -0.22, "omega": 1.62, "C": -0.08},
    {"num": 96, "A": 1.75, "B": 1.18, "omega": 2.65, "C": 0.36},
    {"num": 97, "A": 1.15, "B": 0.23, "omega": 1.48, "C": 0.24},
    {"num": 98, "A": 0.68, "B": 0.30, "omega": 0.42, "C": -0.48},
    {"num": 99, "A": 1.81, "B": -0.0034, "omega": 1.598, "C": 0.025},
    {"num": 100, "A": 0.99, "B": 1.24, "omega": 0.55, "C": -1.35}
]

def compute_period(omega):
    return 2 * math.pi / omega

def compute_first_peak(omega, B, C):
    phi = math.atan2(C, B)
    adjusted_phi = phi % (2 * math.pi)
    return adjusted_phi / omega

def fourier_function(x, series):
    A = series["A"]
    B = series["B"]
    omega = series["omega"]
    C = series["C"]
    return A + B * np.cos(omega * x) + C * np.sin(omega * x)

# Streamlit App
st.title("Rhythm Analysis in Esfahan Architecture Using Fourier Series")
st.markdown("""
Welcome to this interactive tool!

Here you can:
- Specify the total distance (in meters) and the number of peaks you want.
- Upload an image (e.g., a photo ).

**Objective**:
This tool examines 98 different Fourier series, finds the one whose period (distance between peaks) is closest to your desired spacing, and plots it. Additionally, you can overlay a chosen image on the peak points of the curve if you wish.

---
""")

# User inputs
total_distance = st.number_input("Total distance (meters):", min_value=0.1, value=50.0, step=0.1)
num_peaks = st.number_input("Number of peaks:", min_value=2, value=5, step=1)

# File uploader for image
uploaded_file = st.file_uploader("Upload an image to overlay at peak points", type=["png", "jpg", "jpeg"])

if total_distance and num_peaks:
    desired_interval = total_distance / (num_peaks - 1)
    st.write(f"Desired spacing between peaks: {desired_interval:.4f} meters")
    
    best_series = None
    min_diff = float('inf')
    
    # Find the best-matching Fourier series based on period
    for series in fourier_series:
        omega = series["omega"]
        period = compute_period(omega)
        diff = abs(period - desired_interval)
        if diff < min_diff:
            min_diff = diff
            best_series = series.copy()
            best_series["period"] = period

    if best_series:
        x_first = compute_first_peak(best_series["omega"], best_series["B"], best_series["C"])
        
        st.write("### Selected Fourier Series:")
        st.write(f"**Series Number**: {best_series['num']}")
        st.latex(rf"Y = {best_series['A']} + {best_series['B']}\cos\left({best_series['omega']}x\right) + {best_series['C']}\sin\left({best_series['omega']}x\right)")
        
        st.write(f"**Calculated Period (spacing between peaks)**: {best_series['period']:.4f} meters")
        st.write(f"**Recommended x-value for the first peak (from x=0)**: {x_first:.4f} meters")
        
        # Plot the selected Fourier function
        x_vals = np.linspace(0, total_distance, 1000)
        y_vals = fourier_function(x_vals, best_series)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(x_vals, y_vals, label=f"Fourier Series #{best_series['num']}")
        ax.set_xlabel("x (meters)")
        ax.set_ylabel("Y")
        ax.set_title("Selected Fourier Series Curve")
        ax.grid(True)
        ax.legend()
        
        # Overlay the uploaded image at peak positions if available
        if uploaded_file is not None:
            try:
                img = Image.open(uploaded_file)
            except Exception as e:
                st.write("Error loading image:", e)
                img = None
            if img:
                peak_positions = []
                current_peak = x_first
                while current_peak <= total_distance:
                    peak_positions.append(current_peak)
                    current_peak += best_series["period"]
                
                zoom_factor = 0.1  # Adjust as needed
                im = OffsetImage(np.array(img), zoom=zoom_factor)
                for xp in peak_positions:
                    yp = fourier_function(xp, best_series)
                    ab = AnnotationBbox(im, (xp, yp), frameon=False)
                    ax.add_artist(ab)
                    ax.plot(xp, yp, 'ro')
                    
        st.pyplot(fig)
    else:
        st.write("No suitable Fourier series found.")
