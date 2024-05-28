import subprocess

arg1 = "src/align_dataset_mtcnn.py"
arg2 ="Dataset/FaceData/raw"
arg3 = "Dataset/FaceData/processed"
arg4 = "--image_size"
arg5 = "160"
arg6 = "--margin"
arg7 = "32"
arg8 = "--random_order"
arg9 = "--gpu_memory_fraction"
arg10 ="0.25"

# Run the called script with arguments
subprocess.run(['python', arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10])
