#May 20, 2016 MTM
#Formula for calculating lever Effort from the
#inputs Resistance(R), Resistance Arm(R) and Effort Arm(L)

def EffortCalculation1(Resistance, ResistanceArm, EffortArm):
    E = (l * R)/L
    return E

#resistance
R = float(input("Input Resistance(R, in lbs): "))
#resistance arm length
l = float(input("Input Resistance Arm length(l): "))
#effort arm length
L = float(input("Input Effort Arm length(L): "))

Effort = EffortCalculation(R, l, L)

print("Total effort required for lifting " + str(R) + " lbs is " + str(Effort))

