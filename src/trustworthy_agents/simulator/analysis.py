from trustworthy_agents.simulator.runner import RunRecord


def unauthorized_action_rate(records: list[RunRecord]) -> float:
    """Calculate the proportion of runs containing an unauthorized action."""
    if not records:
        raise ValueError("records must not be empty")

    unauthorized_runs = sum(
        record.unauthorized_action
        for record in records
    )

    return unauthorized_runs / len(records)
