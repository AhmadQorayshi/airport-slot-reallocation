# Airport Slot Reallocation under Congestion

This repository contains the GAMS optimization model, Python scripts, and sample input data accompanying the research paper:

> **A Flight Rescheduling Model at a Schedule-Coordinated Airport to Incorporate Airlines' Preferences**

## Overview

This repository presents an optimization framework for airport slot reallocation under congestion. The proposed model aims to minimize propagated delays throughout the flight network.

The repository includes the mathematical optimization model implemented in GAMS, a Python script for robustness assessment, and sample input datasets illustrating the required data structure.

## Repository Contents

```text
airport-slot-reallocation/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── src/
│   ├── airport_slot_reallocation_optimization_model.gms
│   └── Assessing_Robustness.py
│
├── data/
│   ├── README.md
│   ├── Excel_file_connection_sample.xlsx
│   ├── Input_for_py_code.xlsx
│   └── Original_Schedule_Flights.xlsx
│
└── docs/
```

## Requirements

The project was developed using:

* GAMS 24.1.2
* Python 3.8.10
* pandas

## Data

The repository contains **sample datasets** that demonstrate the required input format for both the GAMS optimization model and the Python script.

The original datasets used in the research are not included in this repository.

The sample datasets use the following specifications:

* Number of flights in each flight set (`i`, `j`, and `k`): **10**
* Number of time periods (`t`): **20**

Users may replace the sample files with their own datasets while preserving the same structure expected by the source code.


## Associated Publication

**Title**

*A Flight Rescheduling Model at a Schedule-Coordinated Airport to Incorporate Airlines' Preferences*

**Authors**

Qorayshi Karein, S. A., Seifi, A., & Ponnambalam, K.

**Journal**

Journal of Air Transportation

**Status**

Under Review

## Citation

If you use this repository in your research, please cite both the associated publication and this repository.

A GitHub citation file (`CITATION.cff`) will be added in a future update.

## License

This project is distributed under the MIT License.

## Contact

**S. Ahmad Qorayshi**

GitHub: https://github.com/AhmadQorayshi

Email: S.A.Qoreishi@gmail.com

LinkedIn: https://www.linkedin.com/in/ahmadqoreishi/

---

*This repository is maintained to promote transparency, reproducibility, and the reuse of research software in airport operations, transportation systems, and mathematical optimization.*
