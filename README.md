# Esfahan-rythm-Yasaman-Daram


---

# Rhythm Analysis in Architectural Walls

This project analyzes the concept of **rhythm** in the walls of a city using **Fourier series**. By extracting relevant data from these traditional structures, we have generated 98 different Fourier series. Users can input a total distance (in meters) and the desired number of peaks, and the application will select the Fourier series whose period is closest to that spacing. Additionally, users can upload an image to overlay on the peak points of the resulting curve.

## Features

1. **Rhythm Detection:**  
   - The application uses Fourier series to represent repeating patterns found in city walls or other architectural elements.
   - It selects the series that best matches the user’s desired peak spacing.

2. **Interactive Inputs:**  
   - Specify the total distance (in meters).
   - Specify the desired number of peaks.
   - Upload an optional image to place at each peak of the curve.

3. **Peak Overlay with Images:**  
   - Once the best-matching series is found, the user can overlay any uploaded image at the peak positions, making it easy to visualize repetitive elements or decorations.

## How It Works

1. **Fourier Series Data:**  
   - The project includes 100 Fourier series, each with specific parameters \(\omega\), \(A\), \(B\), and \(C\).  
   - These series were derived from analyzing traditional architecture and capturing its rhythmic properties.

2. **Selecting the Best Series:**  
   - The application calculates the period \( T = \frac{2\pi}{\omega} \) of each series.  
   - It compares \(T\) to the user’s desired spacing (based on total distance and number of peaks).  
   - The series with the closest period to the desired spacing is chosen.

3. **Plotting and Overlaying:**  
   - A plot is generated to visualize the chosen Fourier series over the specified distance.  
   - If the user uploads an image (e.g., a photo of a traditional wall), it will be placed at each peak in the curve.

## Installation and Usage

1. **Clone or Download:**  
   - Clone this repository or download the ZIP file.

2. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```
   Make sure you have Python 3.7+ installed.

3. **Run the Application (Streamlit):**  
   ```bash
   streamlit run app.py
   ```
   This will open your browser at a local URL (e.g., `http://localhost:8501`).

4. **Interact with the App:**  
   - Enter the total distance (meters).  
   - Enter the desired number of peaks.  
   - (Optional) Upload an image to place on the peak points.  
   - The application will then display the selected Fourier series and a plot showing the peaks.

## Project Structure

```
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── Procfile             # For deployment on Heroku (optional)
├── README.md            # Project documentation (this file)
└── ...
```

## Contributing

Contributions and suggestions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or ideas.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this code for personal or commercial purposes. Refer to the `LICENSE` file for details.

---

