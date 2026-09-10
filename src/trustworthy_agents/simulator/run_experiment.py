from pathlib import Path
import csv

from trustworthy_agents.simulator.analysis import unauthorized_action_rate
from trustworthy_agents.simulator.runner import run_repeated_experiment
from trustworthy_agents.simulator.statistics import (
    rate_difference,
    rate_with_confidence_interval,
)


OUTPUT_PATH = Path("results/experiment_01.csv")


def write_records(records, output_path: Path) -> None:
    """Write raw experimental records to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "run_id",
                "condition",
                "seed",
                "unauthorized_action",
                "event_count",
                "message_count",
            ]
        )

        for record in records:
            writer.writerow(
                [
                    record.run_id,
                    record.condition,
                    record.seed,
                    record.unauthorized_action,
                    record.event_count,
                    record.message_count,
                ]
            )


def main() -> None:
    runs = 1000

    no_comm_records = run_repeated_experiment(
        condition="AB_NO_COMM",
        runs=runs,
    )

    comm_records = run_repeated_experiment(
        condition="AB_COMM",
        runs=runs,
    )

    all_records = no_comm_records + comm_records

    write_records(all_records, OUTPUT_PATH)

    no_comm_rate = unauthorized_action_rate(no_comm_records)
    comm_rate = unauthorized_action_rate(comm_records)

    no_comm_estimate = rate_with_confidence_interval(no_comm_records)
    comm_estimate = rate_with_confidence_interval(comm_records)

    difference = rate_difference(
        no_comm_records,
        comm_records,
    )

    print(f"Runs per condition: {runs}")
    print(
        f"AB_NO_COMM UAR: {no_comm_rate:.2%} "
        f"(95% CI: {no_comm_estimate.lower:.2%}–"
        f"{no_comm_estimate.upper:.2%})"
    )
    print(
        f"AB_COMM UAR:    {comm_rate:.2%} "
        f"(95% CI: {comm_estimate.lower:.2%}–"
        f"{comm_estimate.upper:.2%})"
    )
    print(f"Rate difference: {difference:.2%}")
    print(f"Raw results:     {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
