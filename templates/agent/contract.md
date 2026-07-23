# Contract — <agent name>

The only interface other agents and the orchestrator may depend on. Depend on
this file, never on the agent's internals; if it isn't written here, it isn't
guaranteed.

## Purpose

<One sentence: the job this agent does in the system.>

## Inputs

| Field | Type / shape | Required | Notes |
|---|---|---|---|
| <name> | <schema or example> | yes/no | <constraints, size limits> |

## Outputs (guarantees)

| Field | Type / shape | Guarantee |
|---|---|---|
| <name> | <schema or example> | <what downstream may rely on> |

## Failure modes & escalation

<What the agent returns when it cannot fulfill the contract — explicit error
shape, never a silent partial answer — and where the case escalates
(orchestrator, human, retry policy).>

## Non-goals

<What this agent explicitly does not do, so nobody routes it work it will do
badly.>

## Dependencies

<Upstream agents/tools whose contracts this agent consumes. Downstream
consumers are listed by the caller, not here.>
