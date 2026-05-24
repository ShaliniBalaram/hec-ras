"""Command-line wrapper for the Guadalupe River HEC-RAS analysis workflow."""

import argparse
import sys
from pathlib import Path


def build_parser():
    parser = argparse.ArgumentParser(
        description="Run supported Guadalupe River HEC-RAS analysis workflow steps."
    )
    parser.add_argument(
        "--mode",
        choices=("full", "download", "peaks"),
        default="full",
        help="Workflow mode to run.",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory for generated data, plots, reports, and cache files.",
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    output_dir = Path(args.output_dir) if args.output_dir else None

    from main import analyze_historical_peaks, download_data_only, run_complete_analysis

    if args.mode == "full":
        return run_complete_analysis(output_dir=output_dir)
    if args.mode == "download":
        return download_data_only(output_dir=output_dir)
    if args.mode == "peaks":
        return analyze_historical_peaks(output_dir=output_dir)

    parser.error(f"Unsupported mode: {args.mode}")
    return None


if __name__ == "__main__":
    main(sys.argv[1:])
