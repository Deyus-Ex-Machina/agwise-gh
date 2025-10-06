#!/usr/bin/env python3
"""
Master script to run all EDA analyses in sequence.

This script orchestrates the complete analysis pipeline:
1. Data loading and basic statistics
2. Visualizations and data quality assessment
3. Correlation analysis
4. Categorical and crop analysis
5. Advanced soil health insights

Usage:
    python run_all_analyses.py

Author: Claude Code
Date: October 5, 2025
"""

import sys
import time
from pathlib import Path

def run_script(script_name):
    """Run a Python script and report timing."""
    print(f"\n{'='*80}")
    print(f"Running: {script_name}")
    print(f"{'='*80}")

    start_time = time.time()

    try:
        # Read and execute the script
        script_path = Path(__file__).parent / script_name
        with open(script_path, 'r') as f:
            code = f.read()

        exec(code, {'__name__': '__main__'})

        elapsed = time.time() - start_time
        print(f"\n✓ {script_name} completed in {elapsed:.2f} seconds")
        return True

    except Exception as e:
        print(f"\n✗ Error in {script_name}: {str(e)}")
        return False

def main():
    """Run all analysis scripts in sequence."""

    print("="*80)
    print("AGRICULTURAL SOIL HEALTH EDA - FULL ANALYSIS PIPELINE")
    print("="*80)
    print(f"Start time: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Define analysis pipeline
    scripts = [
        '01_eda_analysis.py',
        '02_eda_visualizations.py',
        '03_eda_correlations.py',
        '04_eda_categorical_crops.py',
        '05_eda_advanced_insights.py'
    ]

    # Track results
    results = {}
    start_time = time.time()

    # Run each script
    for script in scripts:
        results[script] = run_script(script)

        # Stop if any script fails
        if not results[script]:
            print(f"\n⚠ Pipeline stopped due to error in {script}")
            sys.exit(1)

    # Summary
    total_time = time.time() - start_time

    print(f"\n{'='*80}")
    print("PIPELINE COMPLETE")
    print(f"{'='*80}")
    print(f"Total runtime: {total_time:.2f} seconds ({total_time/60:.1f} minutes)")
    print(f"\nResults:")
    for script, success in results.items():
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"  {status}: {script}")

    print(f"\nAll outputs saved to:")
    print(f"  - Visualizations: ../outputs/visualizations/")
    print(f"  - Tables: ../outputs/tables/")
    print(f"  - Reports: ../reports/")

    print(f"\nNext steps:")
    print(f"  1. Review main report: ../reports/COMPREHENSIVE_EDA_REPORT.md")
    print(f"  2. Examine visualizations in outputs/visualizations/")
    print(f"  3. Check summary tables in outputs/tables/")

    return 0

if __name__ == '__main__':
    sys.exit(main())
