import subprocess

arg1 = "src/face_rec_cam.py"

# Run the called script with arguments
subprocess.run(['cd', 'face', '&&', 'python', arg1],shell=True)
