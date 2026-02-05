from agents.perceive_agent import perceive
from agents.plan_agent import plan
from agents.act_agent import act

patient_data = {
    "weight_change_kg": 3,
    "heart_rate": 105
}

patient_name = "John"

perception = perceive(patient_data)
planning = plan(perception)
execution = act(planning, patient_name)

print("\nFinal Output:")
print(execution)
