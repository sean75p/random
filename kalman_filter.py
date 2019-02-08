import pandas

print("This is my one-dimensional Kalman filter example.\n")

# initial values and constants
true_temperature = 72
initial_error_estimate = 2
error_in_meas = 4
measurement = [75, 71, 70, 74]
initial_estimate = 68
initial_error_estimate1 = 2


def kalman_gain(error_estimate, error_meas):
    # This is the equation for the Kalman Gain
    return error_estimate/(error_estimate + error_meas)


def current_estimate(est_tminus1, KG, measurement):
    # current estimate is the previous estimate plus the KG * (measured_value - previous estimate)
    return est_tminus1 + KG*(measurement - est_tminus1)


def error_estimate(KG, error_estimate_tminus1):
    # current error in estimate = (1-KG) * (previous error in estimate)
    return (1-KG)*(error_estimate_tminus1)

estimate=[]
kg = []
error_in_estimate = []

print('estimate,', 'Kalman Gain,', 'error in estimate')
for measure in measurement:
    kalman_gain1 = kalman_gain(initial_error_estimate1, error_in_meas)
    current_estimate1 = current_estimate(initial_estimate, kalman_gain1, measure)
    initial_error_estimate1 = error_estimate(kalman_gain1, initial_error_estimate1)

    estimate.append(current_estimate1)
    kg.append(kalman_gain1)
    error_in_estimate.append(initial_error_estimate1)

    initial_estimate = current_estimate1

    print(current_estimate1, kalman_gain1, initial_error_estimate1)

print("\n")
df = pandas.DataFrame({'measurement': measurement,'estimate': estimate, 'Kalman_Gain': kg, 'Error in Estimate': error_in_estimate})
print(df)