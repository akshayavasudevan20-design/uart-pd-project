import csv
import os

def read_metrics(run_path):
    metrics_file = os.path.join(run_path, "reports", "metrics.csv")
    with open(metrics_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            return row

def print_comparison(runs):
    print("=" * 70)
    print(f"{'UART TX — Multi-Run PD Comparison':^70}")
    print("=" * 70)
    print(f"{'Metric':<20} {'Run1 (0.5)':>15} {'Run2 (0.6)':>15} {'Run3 (0.7)':>15}")
    print("-" * 70)

    metrics_list = []
    for run_path in runs:
        metrics_list.append(read_metrics(run_path))

    def get(m, key):
        return m.get(key, 'N/A')

    wns = [float(get(m, 'wns')) for m in metrics_list]
    areas = [get(m, 'DIEAREA_mm^2') for m in metrics_list]
    cells = [get(m, 'cells_pre_abc') for m in metrics_list]
    drc = [get(m, 'Magic_violations') for m in metrics_list]
    runtime = [get(m, 'total_runtime') for m in metrics_list]

    print(f"{'WNS (ns)':<20} {wns[0]:>15} {wns[1]:>15} {wns[2]:>15}")
    print(f"{'Area (mm²)':<20} {areas[0]:>15} {areas[1]:>15} {areas[2]:>15}")
    print(f"{'Total Cells':<20} {cells[0]:>15} {cells[1]:>15} {cells[2]:>15}")
    print(f"{'DRC Violations':<20} {drc[0]:>15} {drc[1]:>15} {drc[2]:>15}")
    print(f"{'Runtime':<20} {runtime[0]:>15} {runtime[1]:>15} {runtime[2]:>15}")
    print("=" * 70)

base = os.path.expanduser("~/OpenLane/designs/uart_tx/runs")

runs = [
    os.path.join(base, "RUN_2026.05.30_16.18.58"),
    os.path.join(base, "RUN_2026.05.30_16.54.42"),
    os.path.join(base, "RUN_2026.05.30_17.01.18")
]

print_comparison(runs)
