import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave(frequency=1, duration=1, sampling_rate=1000):
    time = np.arange(0, duration, 1/sampling_rate)
    amplitude = np.sin(2 * np.pi * frequency * time)

    plt.plot(time, amplitude)
    plt.title('Sine Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

if __name__ == "__main__":
    plot_sine_wave()
