# HEC-RAS Flood Analysis Automation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![HEC-RAS](https://img.shields.io/badge/HEC--RAS-6.4%2B-green.svg)](https://www.hec.usace.army.mil/software/hec-ras/)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)](README.md)
[![Institution](https://img.shields.io/badge/Institution-IIT%20Madras-red.svg)](https://www.iitm.ac.in/)

**Author**: Shalini Balaram  
**Institution**: Indian Institute of Technology Madras  
**Contact**: shalinib0204@gmail.com  

A comprehensive, modular Python automation system for HEC-RAS flood analysis workflows. This professional-grade tool demonstrates advanced hydraulic modeling capabilities, Python integration, and industry-standard flood risk assessment procedures developed for academic research and professional applications.

## 🎯 Project Overview

### Purpose
This system automates complete flood analysis workflows using HEC-RAS hydraulic modeling, from data collection through technical report generation. Designed for academic research, professional consulting, and educational demonstration at IIT Madras.

### Key Capabilities
- **🔄 Complete Automation**: End-to-end flood analysis workflow
- **🧩 Modular Design**: Independent functions for flexible execution
- **📊 Professional Quality**: Industry-standard methods and documentation
- **🌐 Interactive Mapping**: Web-based flood visualization
- **📄 Technical Reports**: Comprehensive documentation generation
- **🎓 Academic Ready**: Suitable for research and portfolio applications

### Study Case: Guadalupe River, Texas
- **Location**: Victoria, Texas (Hurricane Harvey 2017)
- **Drainage Area**: 5,198 square miles
- **Analysis Type**: 1D unsteady flow modeling
- **Calibration Event**: Hurricane Harvey flood data
- **Design Storms**: 10, 25, 50, 100-year return periods

---

## 🚀 Quick Start

### Prerequisites

**Required Software:**
- Python 3.8+ with pip
- HEC-RAS 6.4+ (Windows only for COM interface)
- Git for version control

**Required Python Packages:**
```bash
pip install pandas numpy matplotlib seaborn
pip install geopandas rasterio folium plotly
pip install requests pathlib datetime
pip install pywin32  # Windows only for HEC-RAS automation
```

### Installation

1. **Clone Repository**
```bash
git clone https://github.com/username/hecras-flood-analysis.git
cd hecras-flood-analysis
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Verify Installation**
```python
from complete_hecras_automation import HECRASFloodAnalysis
project = HECRASFloodAnalysis("test_project")
print("✅ Installation successful!")
```

---

## 💡 Usage Flexibility

### 🔄 Complete Automated Workflow

**Full Analysis (Recommended for Beginners)**
```python
from complete_hecras_automation import HECRASFloodAnalysis

# Initialize project
project = HECRASFloodAnalysis(
    project_name="My_Flood_Study",
    base_dir="C:/Flood_Projects"  # Optional: specify directory
)

# Execute complete analysis (all functions automatically)
results = project.execute_complete_analysis()

# Results include:
# - Calibrated HEC-RAS model
# - Flood frequency analysis  
# - Interactive flood maps
# - Technical report (85+ pages)
# - All supporting documentation
```

### 🧩 Modular Function Execution

**Individual Functions (Advanced Users)**
```python
# Each function can run independently
project = HECRASFloodAnalysis("Modular_Study")

# Data Collection Phase
site_data = project.collect_site_data()
hydro_data = project.download_hydrologic_data()
design_storms = project.generate_design_storms([10, 25, 50, 100])

# Model Setup Phase  
terrain_data = project.process_terrain_data()
model_config = project.initialize_hecras_model()
geometry = project.setup_geometry_in_hecras()
boundaries = project.setup_boundary_conditions()

# Analysis Phase
simulation = project.execute_model_simulation()
calibration = project.calibrate_model()
frequency = project.analyze_flood_frequency()
mapping = project.create_flood_mapping()

# Documentation Phase
report = project.generate_comprehensive_report()
```

### 🎯 Workflow-Specific Execution

**1. Calibration-Focused Study**
```python
# Focus on model calibration and validation
project = HECRASFloodAnalysis("Calibration_Study")

# Essential setup
project.collect_site_data()
project.download_hydrologic_data()
project.process_terrain_data(create_synthetic=True)

# Model development
project.initialize_hecras_model()
project.setup_geometry_in_hecras()
project.setup_boundary_conditions()

# Calibration workflow
project.execute_model_simulation()
calibration_results = project.calibrate_model()

# Generate calibration report
project.generate_calibration_documentation(calibration_results)

print(f"Calibration RMSE: {calibration_results['final_rmse']:.2f} ft")
```

**2. Flood Mapping Study**
```python
# Focus on flood mapping and visualization
project = HECRASFloodAnalysis("Mapping_Study")

# Required components
project.collect_site_data()
project.generate_design_storms()
project.process_terrain_data()

# Direct to mapping
frequency_analysis = project.analyze_flood_frequency()
mapping_results = project.create_flood_mapping()

# Create interactive visualizations
interactive_maps = mapping_results['interactive_maps']
print(f"Created {len(interactive_maps)} interactive flood maps")
```

**3. Design Storm Analysis**
```python
# Focus on frequency analysis and design storms
project = HECRASFloodAnalysis("Frequency_Study")

# Generate custom design storms
return_periods = [5, 10, 25, 50, 100, 200, 500]
design_storms = project.generate_design_storms(return_periods)

# Analyze frequency relationships
frequency_results = project.analyze_flood_frequency(return_periods)

# Create frequency plots
project.create_frequency_analysis_plots(frequency_results)
```

**4. Data Collection Only**
```python
# Collect and process data without modeling
project = HECRASFloodAnalysis("Data_Collection")

# Download real USGS data
sites = ['08177500', '08178050']  # Guadalupe River gauges
start_date = '2017-08-01'
end_date = '2017-09-30'

hydro_data = project.download_hydrologic_data(
    start_date=start_date,
    end_date=end_date,
    parameters=['00060', '00065']  # discharge, stage
)

# Process Hurricane Harvey data
harvey_stats = project.analyze_hydrologic_data(hydro_data)
print(f"Harvey peak flow: {harvey_stats['peak_flow_cfs']:,.0f} cfs")
```

---

## 🔧 Advanced Configuration

### Custom Project Configuration

```python
# Custom configuration example
custom_config = {
    'site': {
        'river_name': 'Custom River',
        'study_area': 'Your Location',
        'drainage_area': 1000,  # sq miles
        'usgs_sites': ['12345678', '87654321']
    },
    'model': {
        'xs_spacing': 300,      # feet
        'n_channel_initial': 0.035,
        'simulation_hours': 72
    },
    'calibration': {
        'target_rmse': 0.8,     # feet
        'max_iterations': 25
    }
}

project = HECRASFloodAnalysis("Custom_Study")
project.config.update(custom_config)
```

### Function Parameters and Options

**Data Download Options**
```python
# Specify date ranges and parameters
hydro_data = project.download_hydrologic_data(
    start_date='2015-01-01',
    end_date='2020-12-31',
    parameters=['00060', '00065', '00045']  # discharge, stage, precipitation
)

# Custom site selection
site_data = project.collect_site_data(
    sites=['08177500', '08178050', '08176500'],
    save_metadata=True
)
```

**Design Storm Customization**
```python
# Custom return periods and duration
design_storms = project.generate_design_storms(
    return_periods=[2, 5, 10, 25, 50, 100, 200, 500],
    duration_hours=168  # 7-day storm
)
```

**Terrain Processing Options**
```python
# Use actual DEM file
terrain_data = project.process_terrain_data(
    dem_path="path/to/your/dem.tif",
    create_synthetic=False
)

# Or create synthetic data
terrain_data = project.process_terrain_data(
    create_synthetic=True
)
```

**Calibration Control**
```python
# Custom calibration parameters
calibration = project.calibrate_model(
    target_rmse=0.5,  # stricter target
    observed_data=my_observed_data  # custom observations
)
```

**Flood Mapping Options**
```python
# Specific scenarios and extent
mapping = project.create_flood_mapping(
    scenarios=['Harvey', '10yr', '100yr'],
    mapping_extent=custom_boundary
)
```

---

## 📊 Output Structure

### Generated Directory Structure
```
Your_Project_Name/
├── 📁 data/
│   ├── raw/                    # Downloaded source data
│   ├── processed/              # Processed model inputs
│   └── geometry/               # Cross-section data
├── 📁 models/
│   ├── geometry/               # HEC-RAS geometry files
│   ├── flow_data/              # Boundary condition files
│   ├── plans/                  # HEC-RAS plan files
│   └── *.prj, *.g01, *.f01     # HEC-RAS model files
├── 📁 results/
│   ├── calibration/            # Model calibration analysis
│   ├── frequency_analysis/     # Design storm results
│   ├── flood_maps/             # Inundation mapping
│   ├── plots/                  # All visualization outputs
│   └── tables/                 # Tabular results
├── 📁 documentation/
│   ├── reports/                # Technical reports
│   ├── figures/                # Report figures
│   └── README.md               # Documentation guide
├── 📁 scripts/
│   └── utilities/              # Helper functions
├── 📁 validation/
│   └── observed_data/          # Calibration datasets
├── 📄 interactive_flood_map.html    # Web-based flood map
├── 📄 project_summary.json         # Project metadata
└── 📄 requirements.txt              # Python dependencies
```

### Key Output Files

**Model Files**
- `models/*.prj` - HEC-RAS project file
- `models/*.g01` - Geometry data
- `models/*.f01` - Flow data
- `models/*.p01` - Plan configuration

**Analysis Results**
- `results/calibration/calibration_analysis.png` - Calibration plots
- `results/frequency_analysis/frequency_curves.png` - Flood frequency curves
- `results/flood_maps/depth_grid_*.csv` - Flood depth grids
- `results/plots/water_surface_profiles.png` - WSE profiles

**Documentation**
- `documentation/reports/technical_report.md` - Complete technical report (85+ pages)
- `interactive_flood_map.html` - Interactive web map
- `project_summary.json` - Project metadata and statistics

---

## 📈 Results and Deliverables

### Technical Outputs

**Model Performance**
- ✅ Calibrated HEC-RAS model (RMSE < 1.0 ft target)
- ✅ Statistical validation (R² > 0.9)
- ✅ Mass balance verification (< 0.1% error)

**Flood Analysis**
- ✅ Design storm scenarios (10, 25, 50, 100-year)
- ✅ Flood frequency curves and statistics
- ✅ Water surface elevation profiles
- ✅ Cross-section analysis plots

**Mapping Products**
- ✅ Interactive flood maps (Folium-based)
- ✅ Inundation extent boundaries
- ✅ Flood depth and velocity grids
- ✅ Static maps for documentation

**Documentation**
- ✅ Comprehensive technical report (85+ pages)
- ✅ Executive summary and conclusions
- ✅ Methodology and quality assurance
- ✅ Detailed appendices and supporting data

### Academic/Professional Value

**Demonstrates Technical Skills**
- 🎯 **HEC-RAS Expertise**: Advanced 1D unsteady flow modeling
- 🎯 **Python Programming**: Automation and data processing
- 🎯 **Statistical Analysis**: Model calibration and validation  
- 🎯 **GIS Integration**: Spatial data processing and mapping
- 🎯 **Technical Writing**: Professional documentation standards

**Suitable Applications**
- 📚 **Academic Research**: Master's/PhD thesis projects
- 💼 **Professional Portfolio**: Consulting and engineering positions
- 🏛️ **Government Applications**: Emergency management and planning
- 🎓 **Educational Use**: Teaching hydraulic modeling concepts
- 📄 **Publications**: Conference papers and journal articles

---

## 💻 System Requirements

### Hardware Requirements
- **Processor**: Intel i5 or equivalent (i7 recommended)
- **Memory**: 8 GB RAM minimum (16 GB recommended)
- **Storage**: 10 GB available space for projects
- **Operating System**: Windows 10/11 (for HEC-RAS COM interface)

### Software Dependencies
- **Python 3.8+** with scientific computing packages
- **HEC-RAS 6.4+** for hydraulic modeling
- **Git** for version control
- **Modern web browser** for interactive maps

### Optional Enhancements
- **QGIS** for advanced GIS operations
- **ArcGIS** for professional mapping (if available)
- **Jupyter Notebook** for interactive analysis
- **Visual Studio Code** for code development

---

## 🛠️ Troubleshooting

### Common Issues and Solutions

**1. HEC-RAS COM Interface Issues**
```python
# Problem: "HEC-RAS Controller not found"
# Solution: Verify HEC-RAS installation and try:
import win32com.client
try:
    hec = win32com.client.Dispatch("RAS641.HECRASCONTROLLER")
    print("✅ HEC-RAS COM available")
except:
    print("⚠️ Using simulation mode")
```

**2. Data Download Failures**
```python
# Problem: USGS API timeouts
# Solution: Add retry logic and error handling
try:
    data = project.download_hydrologic_data()
except Exception as e:
    print(f"Using synthetic data due to: {e}")
    data = project.create_synthetic_hydrologic_data()
```

**3. Memory Issues with Large Projects**
```python
# Problem: Large datasets causing memory issues
# Solution: Process data in chunks
project.config['model']['simulation_hours'] = 48  # Reduce simulation time
project.config['model']['xs_spacing'] = 1000      # Increase spacing
```

**4. Visualization Problems**
```python
# Problem: Interactive maps not loading
# Solution: Check file paths and browser settings
import folium
map_path = project.base_dir / 'results' / 'interactive_flood_map.html'
print(f"Map saved to: {map_path}")
# Open file:// URL in browser manually if needed
```

### Performance Optimization

**Speed Up Execution**
```python
# Reduce cross-sections for faster processing
project.config['model']['xs_spacing'] = 1000  # feet

# Limit return periods for initial testing
design_storms = project.generate_design_storms([10, 100])

# Use synthetic data during development
terrain_data = project.process_terrain_data(create_synthetic=True)
```

**Memory Management**
```python
# Clear large datasets when not needed
del project.data_store['large_dataset']
import gc; gc.collect()

# Process scenarios individually
for scenario in ['10yr', '25yr', '50yr', '100yr']:
    result = project.analyze_single_scenario(scenario)
    # Process and save result
    del result
```

---

## 🤝 Contributing and Support

### Academic Collaboration

This project is developed at **Indian Institute of Technology Madras** and welcomes academic collaboration:

- **Research Partnerships**: Joint studies and methodology development
- **Student Projects**: Thesis and research project support
- **Educational Use**: Classroom demonstrations and tutorials
- **International Collaboration**: Cross-institutional research

### Contact Information

**Primary Developer**: Shalini Balaram  
**Institution**: Indian Institute of Technology Madras  
**Email**: shalinib0204@gmail.com  
**LinkedIn**: [Connect for professional inquiries]  

**For Technical Support:**
- 📧 Email technical questions with specific error messages
- 📋 Include system information and configuration details
- 📁 Attach relevant log files or screenshots
- 🔍 Check troubleshooting section first

**For Academic Collaboration:**
- 🎓 Research project discussions
- 🤝 Joint publication opportunities  
- 📚 Educational material development
- 🌐 International research partnerships

### Contributing Guidelines

**Code Contributions**
1. Fork the repository
2. Create feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -m 'Add enhancement'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Open Pull Request with detailed description

**Documentation Improvements**
- Technical documentation updates
- Tutorial and example development
- Error message clarification
- Performance optimization guides

---

## 📜 License and Citation

### License
This project is released under Educational License for academic and research purposes. Commercial use requires permission.

### Citation

**Academic Papers:**
```bibtex
@software{balaram2024hecras,
  title={HEC-RAS Flood Analysis Automation: A Comprehensive Python Framework},
  author={Balaram, Shalini},
  institution={Indian Institute of Technology Madras},
  year={2024},
  url={https://github.com/username/hecras-flood-analysis}
}
```

**Technical Reports:**
```
Balaram, S. (2024). HEC-RAS Flood Analysis Automation: A Comprehensive Python 
Framework for Hydraulic Modeling and Flood Risk Assessment. Indian Institute of 
Technology Madras. https://github.com/username/hecras-flood-analysis
```

### Acknowledgments

**Data Sources:**
- USGS Water Resources: Streamflow and topographic data
- NOAA National Weather Service: Precipitation frequency data  
- FEMA: Flood insurance studies and mapping standards
- USACE: HEC-RAS software development and documentation

**Academic Support:**
- Indian Institute of Technology Madras
- Faculty advisors and research supervisors
- Peer reviewers and collaborators

**Software Dependencies:**
- Python scientific computing community
- HEC-RAS development team (USACE)
- Open-source GIS and visualization libraries

---

## 🚀 Future Development

### Planned Enhancements

**Technical Improvements**
- 🔄 2D flood modeling integration (HEC-RAS 2D)
- 🌊 Real-time flood forecasting capabilities
- 🤖 Machine learning model optimization
- ☁️ Cloud computing integration (AWS/Azure)

**Analysis Capabilities**
- 📊 Climate change impact analysis
- 🏗️ Infrastructure vulnerability assessment
- 💰 Economic damage calculation
- 🌍 Multi-hazard risk integration

**User Interface**
- 🖥️ Web-based dashboard development
- 📱 Mobile application for field use
- 🎮 Interactive model configuration
- 📈 Real-time visualization updates

**Academic Features**
- 📚 Educational module development
- 🎯 Guided tutorial system
- 📊 Comparative case study database
- 🔬 Research methodology templates

### Collaboration Opportunities

**Research Areas**
- Climate change adaptation strategies
- Urban flood management solutions
- Emergency response optimization
- Hydraulic infrastructure design

**International Partnerships**
- Joint research projects with global universities
- Student exchange programs
- Collaborative publications and conferences
- Shared database development

---

## 📚 Additional Resources

### Learning Materials

**HEC-RAS Resources**
- [Official HEC-RAS Documentation](https://www.hec.usace.army.mil/software/hec-ras/)
- [HEC-RAS User Manual](https://www.hec.usace.army.mil/software/hec-ras/documentation.aspx)
- [Hydraulic Modeling Best Practices](https://www.fema.gov/flood-maps/tools-resources)

**Python for Hydrology**
- [Scientific Python Ecosystem](https://scipy.org/)
- [Hydrological Python Packages](https://github.com/raoulcollenteur/Python-Hydrology-Tools)
- [Flood Modeling Tutorials](https://floodmodeller.com/resources/)

**Flood Risk Management**
- [FEMA Flood Risk Management](https://www.fema.gov/flood-insurance)
- [World Bank Flood Risk Management](https://www.worldbank.org/en/topic/disasterriskmanagement)
- [UN Sendai Framework](https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030)

### Example Applications

**Similar Projects**
- NOAA National Water Model
- European Flood Awareness System (EFAS)
- USGS StreamStats Applications
- FEMA Risk MAP Programs

**Research Papers**
- Recent flood modeling methodology advances
- Climate change impact assessments
- Urban flood management strategies
- Emergency response optimization studies

---

**Ready to start your flood analysis project? Choose your approach:**

🏃‍♀️ **Quick Start**: Use `execute_complete_analysis()` for full automation  
🔧 **Custom Workflow**: Pick individual functions for specific needs  
📚 **Learning Mode**: Follow step-by-step tutorials and examples  
🤝 **Collaboration**: Contact for research partnerships and support  

**Questions? Contact Shalini Balaram at shalinib0204@gmail.com**