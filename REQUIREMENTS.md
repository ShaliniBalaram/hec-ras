# System Requirements for HEC-RAS Automation

## Windows Requirements for Running Actual HEC-RAS Instance

### Software Requirements
- **Windows OS**: Windows 10 or later (required for HEC-RAS COM interface)
- **HEC-RAS**: Version 6.4.1 or later must be installed
  - Download from: [HEC-RAS Official Website](https://www.hec.usace.army.mil/software/hec-ras/)
  - Must be properly installed with COM interface accessible
- **Python**: Version 3.8 or later

### Python Package Dependencies
Install the following dependencies using pip:
```bash
pip install pywin32 numpy pandas geopandas matplotlib seaborn folium plotly rasterio requests
```

### Configuration Requirements
- HEC-RAS must be registered properly in the Windows system
- Administrator privileges may be needed for initial HEC-RAS COM interface access
- For non-Windows systems, only simulation mode is available (actual hydraulic modeling disabled)

## Installation Steps for HEC-RAS

1. **Download HEC-RAS**
   - Visit the [HEC-RAS Official Website](https://www.hec.usace.army.mil/software/hec-ras/)
   - Create an account if you don't have one (free)
   - Download the latest version (currently 6.4.1)

2. **Install HEC-RAS**
   - Run the installer with administrator privileges
   - Follow the default installation options
   - Complete the installation

3. **Verify HEC-RAS Installation**
   - Open HEC-RAS from the Start menu to ensure it runs properly
   - Close HEC-RAS after verification

4. **Install Python Dependencies**
   - Open Command Prompt or PowerShell
   - Run the following command:
   ```bash
   pip install pywin32 numpy pandas geopandas matplotlib seaborn folium plotly rasterio requests
   ```

5. **Verify COM Interface**
   - You can verify the COM interface is working by running:
   ```python
   import win32com.client
   controller = win32com.client.Dispatch("RAS641.HECRASController")
   print("HEC-RAS COM interface is working!")
   ```

## Troubleshooting

### Common Issues and Solutions

1. **"win32com not available" Error**
   - Solution: Install pywin32 with `pip install pywin32`
   - Ensure you're running Python in a Windows environment

2. **HEC-RAS COM Interface Cannot Be Found**
   - Solution: 
     - Verify HEC-RAS is properly installed
     - Run Python with administrator privileges
     - Reinstall HEC-RAS if necessary
     - Ensure you're using the correct version string (e.g., "RAS641.HECRASController" for 6.4.1)

3. **Permissions Issues**
   - Solution: Run your Python script as administrator the first time you access the COM interface

4. **Python Version Compatibility**
   - Solution: Use Python 3.8 or later, but not too recent versions that might have compatibility issues with pywin32

5. **Import Errors for GIS Packages**
   - Solution: Make sure you have GDAL dependencies installed if using advanced geospatial features
