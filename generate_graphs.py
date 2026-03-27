import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
try:
    df = pd.read_csv('logs/emotion_logs.csv')
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
except FileNotFoundError:
    print("Error: 'logs/emotion_logs.csv' not found. Make sure you run this from the project root.")
    exit()

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams.update({'figure.figsize':(10, 6), 'figure.dpi':100})

# --- GRAPH 1: Emotion Distribution (Pie Chart) ---
# Shows which emotions were most frequent during your sessions
plt.figure()
emotion_counts = df['Emotion'].value_counts()
plt.pie(emotion_counts, labels=emotion_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Distribution of Detected Emotions (Session Total)")
plt.savefig('result_emotion_distribution.png')
print("Generated: result_emotion_distribution.png")

# --- GRAPH 2: Confidence Score Distribution (Box Plot) ---
# Shows how "sure" the model was for each emotion type.
# Helps prove that 'Happy' detections were more confident than 'Sad' (or vice versa).
plt.figure()
sns.boxplot(x="Emotion", y="Score", data=df, palette="vlag")
plt.title("Model Confidence Score by Emotion")
plt.ylabel("Confidence Score (0.0 - 1.0)")
plt.savefig('result_confidence_variance.png')
print("Generated: result_confidence_variance.png")

# --- GRAPH 3: Real-Time Emotion Timeline (Line Chart) ---
# Shows how emotions changed over time (Great for proving the 'Dynamic' aspect)
# We take a sample of the last 100 frames for clarity
plt.figure(figsize=(12, 6))
recent_df = df.tail(100).copy()
sns.lineplot(x="Time", y="Score", hue="Emotion", data=recent_df, marker="o")
plt.title("Emotion Fluctuations Over Time (Last 100 Frames)")
plt.xticks(rotation=45)
plt.ylabel("Confidence Score")
plt.tight_layout()
plt.savefig('result_timeline.png')
print("Generated: result_timeline.png")