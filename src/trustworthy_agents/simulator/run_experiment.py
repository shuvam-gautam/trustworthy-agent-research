from trustworthy_agents.simulator.analysis import unauthorized_action_rate
from trustworthy_agents.simulator.runner import run_repeated_experiment


def main() -> None:
    runs = 100

    no_comm_records = run_repeated_experiment(
        condition="AB_NO_COMM",
        runs=runs,
    )

    comm_records = run_repeated_experiment(
        condition="AB_COMM",
        runs=runs,
    )

    no_comm_rate = unauthorized_action_rate(no_comm_records)
    comm_rate = unauthorized_action_rate(comm_records)

    print(f"Runs per condition: {runs}")
    print(f"AB_NO_COMM UAR: {no_comm_rate:.2%}")
    print(f"AB_COMM UAR:    {comm_rate:.2%}")
    print(f"Difference:     {comm_rate - no_comm_rate:.2%}")


if __name__ == "__main__":
    main()
