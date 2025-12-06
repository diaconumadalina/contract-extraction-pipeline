import time
import json
import pandas as pd
from pathlib import Path
from statistics import mean

from src.extraction.extractor import ContractExtractor
from src.utils.config_loader import load_settings

import matplotlib.pyplot as plt


def run_benchmark():
    settings = load_settings()

    repeat = settings.benchmark.repeat
    providers = settings.benchmark.providers

    sample_path = r"C:\Users\Madalina Diaconu\PycharmProjects\contract-extraction-pipeline\data\raw\contracts\narrative_contract_1.pdf"
    text = Path(sample_path).read_text(encoding="utf-8", errors="ignore")

    results = []

    for provider in providers:
        print(f"\n=== Running benchmark for provider: {provider} ===")

        extractor = ContractExtractor(provider_override=provider)

        latencies = []
        errors = 0

        for _ in range(repeat):
            start = time.time()
            try:
                _ = extractor.extract(text)
                latencies.append(time.time() - start)
            except Exception:
                errors += 1
                latencies.append(999)

        results.append(
            {
                "provider": provider,
                "avg_latency": mean(latencies),
                "min_latency": min(latencies),
                "max_latency": max(latencies),
                "failures": errors,
            }
        )

    return results


def save_results(results):
    out_dir = Path("benchmark/results")
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(results)
    csv_path = out_dir / "benchmark_results.csv"
    df.to_csv(csv_path, index=False)
    print(f"CSV saved to: {csv_path}")

    # plot latency
    plt.figure(figsize=(8, 5))
    plt.bar(df["provider"], df["avg_latency"], color=["#1976D2", "#C62828"])
    plt.ylabel("Average Latency (s)")
    plt.title("OpenAI vs Azure — Latency Benchmark")
    plt.savefig(out_dir / "latency.png")
    plt.close()

    # bar failures
    plt.figure(figsize=(8, 5))
    plt.bar(df["provider"], df["failures"], color=["#388E3C", "#F57C00"])
    plt.ylabel("Failures (#)")
    plt.title("OpenAI vs Azure — Stability Benchmark")
    plt.savefig(out_dir / "failures.png")
    plt.close()

    print("Graphs saved.")


if __name__ == "__main__":
    results = run_benchmark()
    save_results(results)
