import pandas as pd
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('training_rewards_20240606_023824.csv')

# Calculate the moving average
window_size = 10
data['Moving_Avg'] = data['Reward'].rolling(window=window_size).mean()

# Plot
plt.plot(data['Episode'], data['Reward'], label='Reward')
plt.plot(data['Episode'], data['Moving_Avg'], label='Moving Average', color='red')
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Reward per Episode with Moving Average')
plt.legend()
plt.show()