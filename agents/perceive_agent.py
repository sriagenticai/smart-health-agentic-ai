from tools.signal_analyzer import analyze_signals

def perceive(patient_data):
    analysis = analyze_signals(patient_data)

    return {
        "observations": patient_data,
        "detected_risks": analysis["risks"],
        "risk_level": analysis["risk_level"],
        "confidence": "HIGH" if patient_data else "LOW"
    }
