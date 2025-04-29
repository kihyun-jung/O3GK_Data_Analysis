# O3GK Data Analysis using Hveto  
### By Kihyun Jung (Ulsan National Institute of Science and Technology, Korea)  
📧 Email: wjk9364@gmail.com  

<<<<<<< Updated upstream
## 📌 Overview  
This repository contains data analysis scripts and results for O3GK using Hveto.

## 📂 Folder Structure  
### 🔹 **Configuration**  
- Contains **parameter(configuration) files** for Omicron and Hveto.

### 🔹 **O3GK_Glitch**  
- Stores **images of all vetoed events** found as a result of Hveto.  
- Glitches are classified into six categories:  
  - **Blip, Dot, Helix, Line, Scratchy, and Whistle**  
- **File structure:**
  - O3GK_Glitch/[glitch type]/[subsystem]/[auxiliary channel]/[date]/
- **File naming convention:**  
  - **Main event:** `Main-[main channel name]-[GPS time]-[duration]`  
  - **Auxiliary events:** `Round[x]-[auxiliary channel name]-[GPS time]-[duration]`

### 🔹 **Coherence**  
- Contains **average coherence plots** for each vetoed channel and all corresponding vetoed events.
=======
All glitches are classified as blip, dot, helix, line, scratchy, and whistle.
location: O3GK_Glitch/[glitch type]/[subsystem]/[auxiliary channel]/[date].
Image name is Main-[main channel name]-[GPS time]-[duration] and Round[x]-[auxiliary channel name]-[GPS time]-[duration].
>>>>>>> Stashed changes
