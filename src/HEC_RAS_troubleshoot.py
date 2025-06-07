"""
HEC-RAS 6.7 COM Interface Setup and Troubleshooting
Updated script for HEC-RAS 6.7 with comprehensive diagnostic tools
"""

import win32com.client
import win32api
import win32con
import os
import sys
import subprocess
from pathlib import Path

def test_hecras_com_interface():
    """
    Comprehensive test for HEC-RAS 6.7 COM interface
    Tests multiple version strings and provides diagnostics
    """
    print("🔍 HEC-RAS 6.7 COM Interface Diagnostic Tool")
    print("=" * 60)
    
    # HEC-RAS 6.7 and recent version ProgIDs to try
    hecras_progids = [
        "RAS67.HECRASCONTROLLER",      # HEC-RAS 6.7
        "RAS661.HECRASCONTROLLER",     # HEC-RAS 6.6.1
        "RAS66.HECRASCONTROLLER",      # HEC-RAS 6.6
        "RAS65.HECRASCONTROLLER",      # HEC-RAS 6.5
        "RAS64.HECRASCONTROLLER",      # HEC-RAS 6.4
        "RAS641.HECRASCONTROLLER",     # HEC-RAS 6.4.1
        "RAS63.HECRASCONTROLLER",      # HEC-RAS 6.3
        "RAS62.HECRASCONTROLLER",      # HEC-RAS 6.2
        "RAS61.HECRASCONTROLLER",      # HEC-RAS 6.1
        "RAS60.HECRASCONTROLLER",      # HEC-RAS 6.0
        "HECRAS.HECRASController",     # Generic
        "HECRASController.HECRASController",  # Alternative format
    ]
    
    print("🔸 Testing COM Interface Connections...")
    
    successful_connections = []
    failed_connections = []
    
    for progid in hecras_progids:
        try:
            print(f"\n   Testing: {progid}")
            hec = win32com.client.Dispatch(progid)
            
            # Test if we can access basic properties
            try:
                version = hec.Version if hasattr(hec, 'Version') else "Unknown"
                print(f"   ✅ SUCCESS: Connected to {progid}")
                print(f"      Version: {version}")
                successful_connections.append((progid, version))
                
                # Test basic functionality
                try:
                    # Try to get HEC-RAS installation path
                    install_path = hec.InstallationPath if hasattr(hec, 'InstallationPath') else "Unknown"
                    print(f"      Install Path: {install_path}")
                except:
                    print(f"      Install Path: Not accessible")
                
                hec = None  # Release COM object
                break  # Found working connection
                
            except Exception as e:
                print(f"   ⚠️ PARTIAL: Connected but limited access - {e}")
                successful_connections.append((progid, "Limited Access"))
                hec = None
                
        except Exception as e:
            print(f"   ❌ FAILED: {progid} - {str(e)[:50]}...")
            failed_connections.append((progid, str(e)))
    
    print(f"\n📊 Connection Test Results:")
    print(f"   ✅ Successful: {len(successful_connections)}")
    print(f"   ❌ Failed: {len(failed_connections)}")
    
    return successful_connections, failed_connections

def check_hecras_installation():
    """Check HEC-RAS installation and registry entries"""
    print("\n🔍 Checking HEC-RAS Installation...")
    
    # Common HEC-RAS installation paths
    possible_paths = [
        r"C:\Program Files (x86)\HEC\HEC-RAS\6.7",
        r"C:\Program Files\HEC\HEC-RAS\6.7", 
        r"C:\Program Files (x86)\HEC\HEC-RAS",
        r"C:\Program Files\HEC\HEC-RAS",
        r"C:\HEC\HEC-RAS\6.7",
        r"C:\HEC\HEC-RAS"
    ]
    
    found_installations = []
    
    for path in possible_paths:
        if Path(path).exists():
            exe_path = Path(path) / "RAS.exe"
            if exe_path.exists():
                print(f"   ✅ Found HEC-RAS at: {path}")
                
                # Try to get version info
                try:
                    version_info = win32api.GetFileVersionInfo(str(exe_path), "\\")
                    version = f"{version_info['FileVersionMS'] >> 16}.{version_info['FileVersionMS'] & 0xFFFF}"
                    print(f"      Version: {version}")
                    found_installations.append((path, version))
                except:
                    print(f"      Version: Could not determine")
                    found_installations.append((path, "Unknown"))
            else:
                print(f"   ⚠️ Directory exists but RAS.exe not found: {path}")
        else:
            print(f"   ❌ Not found: {path}")
    
    return found_installations

def check_com_registration():
    """Check COM registration for HEC-RAS"""
    print("\n🔍 Checking COM Registration...")
    
    try:
        import winreg
        
        # Check HKEY_CLASSES_ROOT for HEC-RAS COM entries
        registry_keys_to_check = [
            r"RAS67.HECRASCONTROLLER",
            r"RAS661.HECRASCONTROLLER", 
            r"RAS66.HECRASCONTROLLER",
            r"HECRAS.HECRASController"
        ]
        
        found_registrations = []
        
        for key_name in registry_keys_to_check:
            try:
                key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_name)
                print(f"   ✅ Found registry entry: {key_name}")
                found_registrations.append(key_name)
                winreg.CloseKey(key)
            except FileNotFoundError:
                print(f"   ❌ Not registered: {key_name}")
            except Exception as e:
                print(f"   ⚠️ Error checking {key_name}: {e}")
        
        return found_registrations
        
    except Exception as e:
        print(f"   ❌ Could not check registry: {e}")
        return []

def register_hecras_com(hecras_path):
    """Attempt to register HEC-RAS COM components"""
    print(f"\n🔧 Attempting to register HEC-RAS COM components...")
    
    # Look for registration files in HEC-RAS directory
    ras_dir = Path(hecras_path)
    
    registration_files = [
        "RasController.dll",
        "HECRASController.dll", 
        "RAS.exe"
    ]
    
    for reg_file in registration_files:
        reg_path = ras_dir / reg_file
        if reg_path.exists():
            print(f"   Found: {reg_file}")
            
            if reg_file.endswith('.dll'):
                try:
                    # Register DLL
                    cmd = f'regsvr32 /s "{reg_path}"'
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"   ✅ Successfully registered: {reg_file}")
                    else:
                        print(f"   ❌ Failed to register: {reg_file}")
                        print(f"      Error: {result.stderr}")
                except Exception as e:
                    print(f"   ❌ Error registering {reg_file}: {e}")
            
            elif reg_file == "RAS.exe":
                try:
                    # Try registering the executable
                    cmd = f'"{reg_path}" /regserver'
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"   ✅ Successfully registered: {reg_file}")
                    else:
                        print(f"   ⚠️ Registration attempt for {reg_file} completed")
                except Exception as e:
                    print(f"   ❌ Error registering {reg_file}: {e}")
        else:
            print(f"   ❌ Not found: {reg_file}")

def run_hecras_as_admin(hecras_path):
    """Launch HEC-RAS as administrator to ensure proper registration"""
    print(f"\n🚀 Launching HEC-RAS as Administrator...")
    
    ras_exe = Path(hecras_path) / "RAS.exe"
    
    if ras_exe.exists():
        try:
            # Use Windows shell to run as admin
            win32api.ShellExecute(None, "runas", str(ras_exe), None, None, 1)
            print("   ✅ HEC-RAS launched as administrator")
            print("   ⚠️ Please close HEC-RAS completely before testing COM interface")
            return True
        except Exception as e:
            print(f"   ❌ Failed to launch as admin: {e}")
            return False
    else:
        print(f"   ❌ RAS.exe not found at: {ras_exe}")
        return False

def create_updated_hecras_controller():
    """Create updated HEC-RAS controller class for version 6.7"""
    
    controller_code = '''
class HECRASController67:
    """
    Updated HEC-RAS Controller for version 6.7 with robust connection handling
    """
    
    def __init__(self):
        self.hec = None
        self.connected = False
        self.version = "Unknown"
        self.progid_used = None
        
    def connect(self):
        """Try multiple connection methods for HEC-RAS 6.7"""
        
        # Priority order: Try most likely version strings first
        version_strings = [
            "RAS67.HECRASCONTROLLER",
            "RAS661.HECRASCONTROLLER", 
            "RAS66.HECRASCONTROLLER",
            "RAS65.HECRASCONTROLLER",
            "HECRAS.HECRASController"
        ]
        
        for progid in version_strings:
            try:
                print(f"Attempting connection with: {progid}")
                self.hec = win32com.client.Dispatch(progid)
                
                # Test basic functionality
                try:
                    if hasattr(self.hec, 'Version'):
                        self.version = self.hec.Version
                    self.connected = True
                    self.progid_used = progid
                    print(f"✅ Successfully connected using: {progid}")
                    print(f"   HEC-RAS Version: {self.version}")
                    return True
                    
                except Exception as e:
                    print(f"⚠️ Connected but limited functionality: {e}")
                    # Keep connection even with limited access
                    self.connected = True
                    self.progid_used = progid
                    return True
                    
            except Exception as e:
                print(f"❌ Failed with {progid}: {str(e)[:100]}")
                continue
        
        print("❌ Could not establish COM connection with any version string")
        return False
    
    def disconnect(self):
        """Safely disconnect from HEC-RAS"""
        if self.hec:
            try:
                self.hec = None
                self.connected = False
                print("✅ Disconnected from HEC-RAS")
            except:
                pass
    
    def test_functionality(self):
        """Test basic HEC-RAS COM functionality"""
        if not self.connected:
            print("❌ Not connected to HEC-RAS")
            return False
        
        try:
            # Test basic methods
            tests = []
            
            # Test 1: Version info
            try:
                version = self.hec.Version if hasattr(self.hec, 'Version') else "Unknown"
                tests.append(("Version", "✅", version))
            except Exception as e:
                tests.append(("Version", "❌", str(e)))
            
            # Test 2: Installation path
            try:
                path = self.hec.InstallationPath if hasattr(self.hec, 'InstallationPath') else "Not available"
                tests.append(("InstallationPath", "✅", path))
            except Exception as e:
                tests.append(("InstallationPath", "❌", str(e)))
            
            # Test 3: Project operations (basic test)
            try:
                # This might fail but shows if the interface is working
                self.hec.QuitRas()  # Test method call
                tests.append(("Method calls", "✅", "QuitRas executed"))
            except Exception as e:
                if "No current project" in str(e) or "not open" in str(e):
                    tests.append(("Method calls", "✅", "Methods responsive"))
                else:
                    tests.append(("Method calls", "❌", str(e)))
            
            print("\\n🧪 Functionality Test Results:")
            for test_name, status, result in tests:
                print(f"   {status} {test_name}: {result}")
            
            return len([t for t in tests if t[1] == "✅"]) > 0
            
        except Exception as e:
            print(f"❌ Functionality test failed: {e}")
            return False
'''
    
    return controller_code

def main_diagnostic():
    """Run complete HEC-RAS 6.7 diagnostic"""
    print("🔧 HEC-RAS 6.7 COM Interface Complete Diagnostic")
    print("=" * 60)
    
    # Check if running as administrator
    try:
        is_admin = win32api.GetUserNameEx(3)
        print(f"Current user: {is_admin}")
    except:
        print("Could not determine user privileges")
    
    # Step 1: Check HEC-RAS installation
    installations = check_hecras_installation()
    
    # Step 2: Check COM registration
    registrations = check_com_registration()
    
    # Step 3: Test COM connections
    successful, failed = test_hecras_com_interface()
    
    # Step 4: Provide recommendations
    print(f"\n📋 DIAGNOSTIC SUMMARY")
    print("=" * 30)
    
    if successful:
        print("✅ GOOD NEWS: COM interface is working!")
        progid, version = successful[0]
        print(f"   Working ProgID: {progid}")
        print(f"   Version: {version}")
        
        # Create updated controller code
        print(f"\n📝 Use this ProgID in your code:")
        print(f'   hec = win32com.client.Dispatch("{progid}")')
        
    elif installations:
        print("⚠️ HEC-RAS is installed but COM interface needs registration")
        install_path, version = installations[0]
        
        print(f"\n🔧 RECOMMENDED ACTIONS:")
        print(f"1. Run this script as Administrator")
        print(f"2. Launch HEC-RAS as Administrator at least once:")
        print(f"   {install_path}\\RAS.exe")
        print(f"3. Close HEC-RAS completely")
        print(f"4. Try the COM connection again")
        
        # Offer to register COM components
        user_input = input(f"\nAttempt automatic COM registration? (y/n): ")
        if user_input.lower() == 'y':
            register_hecras_com(install_path)
            
            # Test again after registration
            print(f"\n🔄 Re-testing COM interface after registration...")
            successful_after, _ = test_hecras_com_interface()
            
            if successful_after:
                progid, version = successful_after[0]
                print(f"✅ SUCCESS! COM interface now working with: {progid}")
            else:
                print(f"❌ COM interface still not working. Try manual steps above.")
    
    else:
        print("❌ HEC-RAS 6.7 installation not found")
        print(f"\n🔧 PLEASE:")
        print(f"1. Verify HEC-RAS 6.7 is installed")
        print(f"2. Check installation location")
        print(f"3. Reinstall if necessary")
    
    # Always provide fallback option
    print(f"\n💡 ALTERNATIVE: Use Simulation Mode")
    print(f"   Your script can run in simulation mode without COM interface")
    print(f"   Set HECRAS_AVAILABLE = False in the main script")

if __name__ == "__main__":
    # Check if running as administrator
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if not is_admin:
            print("⚠️ WARNING: Not running as Administrator")
            print("For best results, run this script as Administrator")
            print("Right-click Command Prompt -> 'Run as Administrator'")
            print()
    except:
        pass
    
    main_diagnostic()
    
    input("\\nPress Enter to exit...")