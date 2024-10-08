import subprocess

# Function to generate requirements.txt
def generate_requirements():
    # List of libraries explicitly mentioned in the previous exercises
    libraries = [
        "pandas", 
        "numpy", 
        "scikit-learn", 
        "openpyxl", 
        "pickle-mixin", 
        "streamlit"
    ]

    # Write the libraries to requirements.txt
    with open("requirements.txt", "w") as f:
        for lib in libraries:
            try:
                # Capture the installed version of the library
                version = subprocess.check_output([f"pip show {lib} | grep Version"], shell=True)
                version_str = version.decode("utf-8").strip().split(": ")[1]
                f.write(f"{lib}=={version_str}\n")
            except subprocess.CalledProcessError:
                print(f"Library {lib} not found in the current environment.")
    
    print("requirements.txt file generated successfully.")