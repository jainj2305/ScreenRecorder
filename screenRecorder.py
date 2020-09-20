import numpy as np
import cv2
from PIL import ImageGrab
import screeninfo
from datetime import datetime

def main():
    screen = screeninfo.get_monitors()                                                  # Fetch display size of your system
    file_name = 'recording'+str(datetime.now().timestamp())+'.avi'                      # Time Stamp is used for saving recording not to overwrite old file.
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(file_name, fourcc, 5.0, (screen[0].width,screen[0].height))   # Creating output file
    print("Recording Started...\nPress q or ctrl+c for stop recording.")

    while True:
        try:
            img = ImageGrab.grab()                                                      # Get current screen
            img_np = np.array(img)                                                      # convert grabbed image to numpy array
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)                             # Convert BGR image to RGB image
            cv2.imshow("Screen Recording", frame)                                       # Output display, mark it as comment if you don't want to see thet what is recording.
            out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):                                       # Press q for stop recording.
                print(f"Recording Saved as {file_name}!!!")
                break
            
        except KeyboardInterrupt:                                                       # Press ctrl+c for stop recording.
            print(f"Recording Saved as {file_name}!!!")
            break

    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()