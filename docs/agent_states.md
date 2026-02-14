# Agent States: Chronic Care Monitoring Agent (Week 1)

## Objective
Design a single-agent workflow that continuously monitors patient telemetry and context to:
1) detect anomalies and risk trends
2) contextualize findings using patient history and consent
3) recommend safe, reversible next steps
4) enforce clinical safety thresholds
5) require Human-in-the-Loop (HITL) approval for high-risk or irreversible actions

The agent optimizes for **early intervention**, **low false alarms**, and **clinical oversight**.

---


## State Machine (High Level)

### 1. **intake**
- Receive new telemetry batch or streaming signal (e.g., weight, BP, HR, SpO₂).
- Identify patient_id and care program.
- Initialize or update a monitoring episode.
- Verify data freshness and basic validity.

---

### 2. **context_load**
- Load relevant patient context:
  - baseline vitals
  - chronic conditions
  - recent trends
  - clinician-defined thresholds
  - consent and escalation preferences
- Determine monitoring mode (routine | watchlist | high-risk).

---

### 3. **signal_quality_check**
- Validate telemetry integrity:
  - missing data
  - sensor artifacts
  - implausible values
- If data is unreliable, log issue and request re-measurement.
- Do not proceed to clinical reasoning on bad data.

---

### 4. **anomaly_detection**
- Compare incoming signals against:
  - patient baseline
  - recent trend windows
  - population-safe bounds
- Detect:
  - threshold breaches
  - trend deviations (e.g., rapid weight gain)
  - multi-signal correlations
- Produce anomaly candidates with confidence scores.

---

### 5. **risk_assessment**
- Combine anomalies with patient context to compute risk:
  - clinical risk score (low | moderate | high | critical)
  - condition-specific interpretations (e.g., fluid retention risk)
- Identify potential false positives and uncertainty.
- Generate a clinical hypothesis (non-diagnostic).

---

### 6. **policy_check**
- Apply safety, consent, and escalation policies:
  - notification limits
  - escalation thresholds
  - irreversible action guards
- Determine:
  - allowed actions
  - required approvals
  - mandatory clinician review

---

### 7. **recommendation**
- Generate a structured recommendation:
  - observation only
  - patient self-check prompt
  - caregiver notification
  - clinician task creation
  - tele-visit suggestion
  - emergency escalation (proposal only)
- Include rationale, confidence, and evidence summary.

---

### 8. **human_approval (HITL)**
- Mandatory for:
  - medication-related implications
  - emergency escalation
  - repeated alerts
  - high-risk classification
- Ask explicit approval with clear options.
- Pause execution until resolved.

---

### 9. **act**
- Execute approved actions:
  - schedule follow-up
  - create clinician task
  - notify caregiver
  - log escalation
- No autonomous irreversible actions.

---

### 10. **finalize**
- Persist outcomes:
  - updated risk state
  - actions taken
  - clinician decisions
  - audit trail
- Return monitoring to idle or elevated watch mode.

---

## Stop Conditions (Must Ask Human)
- Critical or life-threatening risk
- Ambiguous signals with high impact
- Any medication-related implication
- Emergency escalation
- Conflicting telemetry vs patient history
- Consent boundary uncertainty

---

## Output Guarantee
Every agent response must include:
- Current risk level
- Detected signals/anomalies
- Policy flags
- Recommended action
- HITL question if required
