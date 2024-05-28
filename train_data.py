import subprocess

arg1 = "src/classifier.py"
arg2 = "TRAIN"
arg3 = "Dataset/FaceData/processed"
arg4 = "Models/20180402-114759.pb"
arg5 = "Models/facemodel.pkl"
arg6 = "--batch_size"
arg7 = "1000"

# Run the called script with arguments
subprocess.run(['cd', 'face', '&&', 'python', arg1, arg2, arg3, arg4, arg5, arg6, arg7],shell=True)
