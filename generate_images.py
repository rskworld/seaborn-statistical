#!/usr/bin/env python3
"""
Image Generation Script for Seaborn Statistical Visualization Project

This script runs all Jupyter notebooks to generate visualization images.
After execution, the script will delete itself.

Author: Molla Samser
Website: https://rskworld.in/
Email: help@rskworld.in
Phone: +91 93305 39277
Address: Nutanhat, Mongolkote, Purba Burdwan, West Bengal, India, 713147
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def main():
    """Generate images by executing all notebooks."""
    print("=" * 60)
    print("Seaborn Statistical Visualization - Image Generator")
    print("=" * 60)
    print("\nAuthor: Molla Samser - rskworld.in\n")
    
    # Get project root directory
    project_root = Path(__file__).parent.absolute()
    notebooks_dir = project_root / "notebooks"
    images_dir = project_root / "images"
    
    # Ensure images directory exists
    images_dir.mkdir(exist_ok=True)
    
    print(f"Project root: {project_root}")
    print(f"Notebooks directory: {notebooks_dir}")
    print(f"Images directory: {images_dir}\n")
    
    # List of notebooks to execute (in order)
    notebooks = [
        "01_distribution_plots.ipynb",
        "02_correlation_heatmaps.ipynb",
        "03_categorical_plots.ipynb",
        "04_regression_plots.ipynb",
        "05_advanced_visualizations.ipynb",
        "06_advanced_statistical_analysis.ipynb",
        "07_styling_and_themes.ipynb",
        "08_matrix_plots.ipynb",
        "complete_guide.ipynb"
    ]
    
    print("Starting image generation process...\n")
    print("This will execute all notebooks to generate visualization images.")
    print("Note: This may take several minutes depending on your system.\n")
    
    success_count = 0
    failed_notebooks = []
    
    for notebook in notebooks:
        notebook_path = notebooks_dir / notebook
        if not notebook_path.exists():
            print(f"⚠️  Warning: {notebook} not found, skipping...")
            continue
        
        print(f"📊 Processing: {notebook}")
        try:
            # Use jupyter nbconvert to execute the notebook
            result = subprocess.run(
                [
                    sys.executable, "-m", "jupyter", "nbconvert",
                    "--to", "notebook",
                    "--execute",
                    "--inplace",
                    str(notebook_path)
                ],
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout per notebook
            )
            
            if result.returncode == 0:
                print(f"✅ Successfully executed: {notebook}\n")
                success_count += 1
            else:
                print(f"❌ Error executing {notebook}:")
                print(result.stderr)
                failed_notebooks.append(notebook)
                print()
        except subprocess.TimeoutExpired:
            print(f"⏱️  Timeout executing {notebook} (exceeded 5 minutes)\n")
            failed_notebooks.append(notebook)
        except Exception as e:
            print(f"❌ Exception while executing {notebook}: {str(e)}\n")
            failed_notebooks.append(notebook)
    
    # Summary
    print("=" * 60)
    print("Image Generation Summary")
    print("=" * 60)
    print(f"✅ Successfully processed: {success_count}/{len(notebooks)} notebooks")
    
    if failed_notebooks:
        print(f"❌ Failed notebooks: {len(failed_notebooks)}")
        for nb in failed_notebooks:
            print(f"   - {nb}")
    
    # Count generated images
    image_files = list(images_dir.glob("*.png"))
    print(f"\n📸 Generated images: {len(image_files)}")
    
    if image_files:
        print("\nGenerated image files:")
        for img in sorted(image_files):
            print(f"   - {img.name}")
    
    print("\n" + "=" * 60)
    print("Image generation complete!")
    print("=" * 60)
    
    # Delete this script
    print("\n🗑️  Cleaning up: Deleting this script...")
    try:
        script_path = Path(__file__).absolute()
        if script_path.exists():
            # On Windows, we need to wait a bit before deletion
            if sys.platform == "win32":
                import time
                time.sleep(1)
            os.remove(script_path)
            print("✅ Script deleted successfully.")
        else:
            print("⚠️  Script file not found, may have already been deleted.")
    except Exception as e:
        print(f"⚠️  Could not delete script: {str(e)}")
        print("   You may need to delete it manually.")
    
    print("\n✨ All done! Check the 'images' folder for generated visualizations.")
    print("   Project by Molla Samser - https://rskworld.in/\n")

if __name__ == "__main__":
    main()

