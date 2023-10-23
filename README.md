# ECG-analysis-on-the-ML-algorithms

This project is designed to process ECG graphs.
An example of an input dataset on the site [physionet](https://www.physionet.org/).

You can download the datasets from the following links:
* MIT-BIH Arrhythmia Database: <pre>```wget -r -N -c -np https://physionet.org/files/mitdb/1.0.0/```</pre>
* PTB Diagnostic ECG Database: <pre>```wget -r -N -c -np https://physionet.org/files/ptbdb/1.0.0/```</pre>
* A large scale 12-lead electrocardiogram database for arrhythmia study: <pre>```wget -r -N -c -np https://physionet.org/files/ecg-arrhythmia/1.0.0/```</pre>

You should download these datasets and place them in the dataset folder.

## Analysis

You can calculate the heart rate(CCR) and error. Example of a bash command:
```
python src/ecg_analysis/main.py analysis dataset/100
```
Output:
```
75.507±0.386 Cardiac contractions rate
```

The absolute error formula takes into account statistical, instrumental and counting errors can be written as follows:

$\Delta x = \sqrt{\Delta x_{\text{stat}}^2 + \Delta x_{\text{instr}}^2 + \Delta x_{\text{coun}}^2}$

Where:
- $\Delta x$ represents the absolute error.
- $x_{\text{stat}} = \frac{\sqrt{\sum_{i=1}^{n} (x_i - \overline{x})^2}}{\sqrt{n(n-1)}}$ represents statistical error, which is associated with the variability of results over repeated measurements.
- $\Delta x_{\text{instr}}$ represents the instrumental error, which is associated with the inaccuracy and error of the measuring device.
- $\Delta x_{\text{coun}}$ represents a counting error that occurs due to the counting method or rounding of results.

In this case we took instrumental error equals counting error. Where counting error: $\frac{1}{\text{sampling frequency}}$.

This formula allows you to take into account various sources of error and determine the overall absolute measurement error.