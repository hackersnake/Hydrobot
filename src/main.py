from object_detection import ObjectDetector
from navigation import Navigator
from water_quality import WaterQualityMonitor
from data_analysis import DataAnalyzer
import time

def main():
    detector = ObjectDetector()
    navigator = Navigator()
    water_monitor = WaterQualityMonitor()
    data_analyzer = DataAnalyzer()

    try:
        while True:
            print("Detecting objects...")
            objects = detector.detect_objects()
            for obj in objects:
                print(f"Navigating to object: {obj}")
                navigator.navigate_to(obj)
                print("Collecting water quality data...")
                water_data = water_monitor.collect_data()
                print(f"Water data: {water_data}")
                data_analyzer.analyze_data(water_data)
            time.sleep(10)  # Sleep for 10 seconds before next iteration
    except KeyboardInterrupt:
        print("Terminating program.")

if __name__ == "__main__":
    main()
