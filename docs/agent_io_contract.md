# Agent I/O Contract: Chronic Care Monitoring Agent (Week 1)

## Input (Telemetry / System → Agent)
- Patient identifier
- Timestamped telemetry signals (single or batch)
- Optional annotations:
  - patient-reported symptoms
  - caregiver notes
  - clinician comments

### Minimal Required Fields
- patient_id
- at least one vital signal with timestamp
- measurement source (device/manual)

---

## Internal Canonical Object: `MonitoringCase`

The agent maintains a canonical monitoring object:

- case_id
- patient_id
- monitoring_mode (routine | watchlist | high-risk)
- telemetry_window (recent signals)
- baselines (per signal)
- detected_anomalies (array)
- risk_assessment
- policy_flags
- recommended_actions
- approvals (if any)
- audit_log (timestamps, decisions, tool calls)

---

## Output (Agent → User / Clinician)

All outputs must include a structured section:

### Required Output Format

1) **Risk Level**
- low | moderate | high | critical

2) **Key Findings**
- signals involved
- anomaly or trend detected
- confidence level

3) **Clinical Context**
- relevant patient history or baseline
- why this finding matters now

4) **Policy Flags**
- within_safe_bounds: true/false
- escalation_required: true/false
- consent_valid: true/false
- hitl_required: true/false

5) **Recommended Action**
- observation
- patient prompt
- caregiver notification
- clinician task
- tele-visit suggestion
- emergency escalation (proposal only)

6) **Next Steps**
- action to be taken OR
- explicit HITL approval request

---

## HITL Language (Mandatory)
When approval is required, the agent must ask:

> "This situation meets escalation criteria. Approve proceeding with the recommended action? (approve / modify / hold)"

The agent must not act without confirmation.
