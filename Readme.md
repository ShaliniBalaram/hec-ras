# HEC-RAS Guadalupe River Analysis Utilities

Python utilities for a Guadalupe River flood-analysis workflow using public USGS and NOAA observations, HEC-RAS controller checks, peak-flow analysis, and report-ready plots/tables.

The repository is centered on the Victoria, Texas reach of the Guadalupe River and the Hurricane Harvey period in August-September 2017. It is intended as a practical hydrology and hydraulic-modeling support project: download observations, prepare HEC-RAS-style inputs, run available HEC-RAS controller operations on Windows, and create validation, calibration, frequency-analysis, and event-summary outputs.

## What This Repository Does

- Downloads USGS streamflow, stage, peak-flow, and rating data for Guadalupe River gauges.
- Downloads NOAA daily precipitation records used in the Harvey event analysis.
- Prepares model input tables and simple geometry/boundary-condition files.
- Connects to HEC-RAS through the Windows COM controller when HEC-RAS is installed and registered.
- Falls back to simulation-mode calculations when the COM controller is unavailable, so the data and reporting workflow can still be reviewed on macOS/Linux.
- Generates calibration plots, validation CSVs, frequency-analysis plots, Harvey event plots, and a Markdown analysis report.
- Includes a troubleshooting script for checking HEC-RAS COM registration on Windows.

## Current Scope

This is not a replacement for building and reviewing a full production HEC-RAS model in the HEC-RAS interface. The Python workflow supports data preparation, controller checks, reproducible calculations, and reporting around the Guadalupe River case study. Final hydraulic model geometry, roughness, boundary conditions, and simulation plans should still be checked in HEC-RAS by a qualified modeler.

## Study Area

- River: Guadalupe River
- Focus area: Victoria, Texas
- Event: Hurricane Harvey, 2017
- Main gauges used by the scripts:
  - `08176500`
  - `08176900`
  - `08177500`

## Repository Layout

```text
.
├── Readme.md
├── REQUIREMENTS.md
├── requirements.txt
└── src/
    ├── main.py                         Core data, HEC-RAS, analysis, and report workflow
    ├── run_analysis.py                 Command-line wrapper for real workflow entry points
    ├── HEC_RAS_troubleshoot.py         Windows COM diagnostic helper
    ├── Peak_Flow_Analysis/             Cached peak-flow analysis outputs
    └── output/                         Existing generated Guadalupe River outputs
```

## Installation

Create and activate a Python environment, then install the project dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, install `pywin32` as part of the requirements so the HEC-RAS COM controller can be used. On macOS or Linux, the scripts can still run the data-processing and simulation-mode parts of the workflow, but they cannot drive the HEC-RAS desktop application.

## HEC-RAS Requirement

HEC-RAS controller automation requires:

- Windows 10 or later
- HEC-RAS 6.4.1 or later
- Python 3.8 or later
- `pywin32`
- HEC-RAS COM registration working for the installed version

Use the diagnostic script on Windows:

```bash
python src/HEC_RAS_troubleshoot.py
```

## Running the Workflow

Run the complete available workflow:

```bash
python src/run_analysis.py --mode full --output-dir Guadalupe_River_RealData_Analysis
```

Download public input data only:

```bash
python src/run_analysis.py --mode download --output-dir Guadalupe_River_RealData_Analysis
```

Run the historical peak-flow analysis only:

```bash
python src/run_analysis.py --mode peaks --output-dir Peak_Flow_Analysis
```

The wrapper calls the real functions defined in `src/main.py`:

```python
from main import run_complete_analysis, download_data_only, analyze_historical_peaks

run_complete_analysis(output_dir="Guadalupe_River_RealData_Analysis")
download_data_only(output_dir="Guadalupe_River_RealData_Analysis")
analyze_historical_peaks(output_dir="Peak_Flow_Analysis")
```

## Outputs

The workflow writes outputs beneath the selected output directory. Typical outputs include:

```text
data/cache/                         Downloaded USGS/NOAA source tables
data/processed/                     Processed flow, stage, and precipitation tables
models/flow_data.csv                Flow input table
models/geometry_info.json           Geometry summary from the workflow
results/calibration/                Calibration plots
results/validation/validation_data.csv
results/frequency/frequency_curve.png
results/plots/harvey_event.html
documentation/comprehensive_report.md
```

The existing `src/output/Guadalupe_River_RealData_Analysis/` folder contains generated outputs from a previous run of the Guadalupe River workflow.

## Validation

Validation output is written as:

```text
results/validation/validation_data.csv
```

The validation table compares available observed values against workflow-generated simulated values. It is useful for checking the reporting and calibration pipeline, but it should not be treated as final hydraulic-model validation unless the underlying HEC-RAS model setup has also been reviewed.

## Data Sources

- USGS National Water Information System streamflow, stage, peak-flow, and rating data
- NOAA/NCEI daily precipitation summaries
- HEC-RAS software and controller interface from the US Army Corps of Engineers

The scripts cache downloaded public data so later runs can reuse the same input tables.

## Notes for Review

- `src/main.py` contains the core workflow and the HEC-RAS controller wrapper.
- `src/run_analysis.py` is intentionally thin; it only dispatches to supported workflow modes.
- `src/HEC_RAS_troubleshoot.py` is for Windows HEC-RAS installation checks.
- Non-Windows systems are suitable for code review and data/report workflow checks, but not for live HEC-RAS controller execution.
