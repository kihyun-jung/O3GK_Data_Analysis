# O3GK Data Analysis using Hveto  
### By Kihyun Jung (Ulsan National Institute of Science and Technology, Korea)  
📧 Email: wjk9364@gmail.com  

## 📌 Overview  
This repository contains data analysis scripts and results for O3GK using Hveto.

## 📂 Folder Structure  
### 🔹 **Configuration**  
- Contains **parameter(configuration) files** for Omicron and Hveto.

### 🔹 **O3GK_Glitch**  
- Stores **images of all vetoed events** found as a result of Hveto.  
- Glitches are classified into six categories:  
  - **Blip, Dot, Helix, Line, Scratchy, and Whistle**  
- **Folder structure:**
  - O3GK_Glitch/[glitch type]/[subsystem]/[associated auxiliary channel name]/[date]
- **File naming convention:**  
  - **Glitch spectrogram:** `Main-[main channel name]-[GPS time]-[duration]`  

### 🔹 **Coherence**  
- Contains **average coherence plots** for each vetoed channel and all corresponding vetoed events.
