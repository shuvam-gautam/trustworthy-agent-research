# Research Evidence Registry

Purpose: Track relevant systems, papers, benchmarks, and datasets so that
research decisions are grounded in existing work and novelty claims remain
conservative.

## Evidence standard

Capability descriptions should distinguish documented functionality from
our interpretation of research gaps.

- **Documented**: supported directly by the project's documentation, paper,
  benchmark description, or source code.
- **Assessed**: our current interpretation of what the documented system
  does not provide.
- **Unverified**: requires further primary-source investigation before being
  used in a novelty claim.

This registry is a research aid, not proof of novelty.
Any future novelty claim must be supported by direct primary-source review.

## Evaluation criteria

- What does the system observe or record?
- Does it support versioning or history?
- Does it model multiple agents?
- Does it support longitudinal analysis?
- Does it support causal or counterfactual analysis?
- What can we reuse?
- What must we not claim as novel?
- What possible research gap remains?

| Source | Type | Observes / Records | Version / History | Cross-Agent | Longitudinal | Causal / Counterfactual | Relevance to Our Research |
|---|---|---|---|---|---|---|---|
| GitAgent / OpenGAP | Agent framework / standard | Agent config, identity, rules, memory, tools, skills, workflows | Yes | Partial | Yes | No general causal-effect analysis | Do not build another "Git for agents" system; useful as an agent-state/history reference. |
| Agent-Git | Agent version-control infrastructure | Workflow state, checkpoints, messages, tool executions | Yes; checkpoint/rollback/branching | Partial | Yes | Limited; rollback is not causal attribution | Do not compete on agent version control; useful for checkpoint/state concepts. |
| AgentProvenance | Security / provenance system | Model intent, application context, runtime telemetry, tools, processes, files, network events, risks, responses | Git-like provenance DAG | Yes | Yes | Causality graph and replay; not the same as causal-effect estimation | Very close prior art. Do not claim generic provenance or causal graphs as novel. |
| A2ASecBench | Security benchmark | Agent-to-agent security behavior and protocol-level attacks | Repeated benchmark runs | Yes | Execution-level | Not the core contribution | Important prior art for agent-to-agent security benchmarking. |
| ATBench / AgentDoG | Safety benchmark / trajectory diagnosis | Long-horizon tool-using agent trajectories and safety outcomes | Trajectory-level | Limited | Yes | Diagnosis, but not our proposed interaction-effect experiment | Do not build a generic trajectory safety benchmark; use as an external baseline/reference. |
| Anthropic multi-agent research | Empirical research | Multi-agent interaction patterns and systemic outcomes | Long-running experiments | Yes | Yes | Experimental comparisons | Establishes that individually acceptable behavior can produce systemic failures. |
| ICLR 2026 MASS | Research paper | Agent workflows, prompts, topology, interdependence | Configuration-level | Yes | Not primary focus | Not primary focus | Important prior art for topology and interdependence; avoid claiming topology-aware MAS analysis as new by itself. |
| SoK: When Safe Agents Fail Together | Security survey / framework | End-to-end MAS execution paths, interaction interfaces, risks, defenses | Execution-level | Yes | Yes | Explicitly identifies interaction-effect isolation and counterfactual evaluation as open challenges | Highest-priority prior art for our current hypothesis. |
 
## Current candidate research gap

We are NOT proposing to build:

- another Git-for-agents system
- another generic provenance platform
- another generic trajectory-safety detector
- another agent-to-agent security benchmark
- another agent lifecycle manager

Current research question under investigation:

> Can controlled counterfactual experiments isolate the causal contribution of
> agent-agent interaction to security-relevant behavioral outcomes in
> autonomous multi-agent systems?

Current hypothesis:

> H1: In a controlled multi-agent environment, enabling interaction between
> agents changes the distribution of a security-relevant behavioral outcome
> beyond the corresponding single-agent effects.

Important constraint:

> This is a research hypothesis, not a novelty claim. We must test it
> experimentally and compare against existing work before claiming a gap.

## Sources

1. GitAgent / OpenGAP:
   https://github.com/open-gitagent/gitagent
   https://github.com/open-gitagent/opengap

2. Agent-Git:
   https://github.com/MAS-Infra-Layer/Agent-Git

3. AgentProvenance:
   https://github.com/ByteYellow/AgentProvenance

4. A2ASecBench:
   https://github.com/SaFo-Lab/A2ASecBench

5. ATBench:
   https://huggingface.co/datasets/AI45Research/ATBench

6. Anthropic multi-agent research:
   https://www.anthropic.com/research/multiagent-systems

7. ICLR 2026 MASS:
   https://proceedings.iclr.cc/paper_files/paper/2026/file/1ab4e0e8f35078109bc78d7b465d306f-Paper-Conference.pdf

8. SoK: When Safe Agents Fail Together:
   https://arxiv.org/abs/2609.00595
