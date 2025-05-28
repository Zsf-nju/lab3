import cv2
import numpy as np
import glob
import os
import networkx as nx

def stitch_case(case_name, input_dir, output_dir):
    image_paths = sorted(glob.glob(os.path.join(input_dir, case_name, "*")))
    images = [cv2.imread(p) for p in image_paths]
    if any(img is None for img in images) or len(images) < 2:
        print(f"[{case_name}] Skipped: insufficient or unreadable images.")
        return

    # Implement your algorithm here
    stitched_image = None
    #

    case_output_dir = output_dir
    os.makedirs(case_output_dir, exist_ok=True)
    output_path = os.path.join(case_output_dir, f"{case_name}.JPG")
    cv2.imwrite(output_path, stitched_image)
    print(f"[{case_name}] Done: saved to {output_path}")

def main():
    input_root = "data/task2_multiview"
    output_root = "output/task2_multiview"
    os.makedirs(output_root, exist_ok=True)
    cases = [name for name in os.listdir(input_root) if os.path.isdir(os.path.join(input_root, name))]
    if not cases:
        print("No cases found in 'data' directory.")
        return

    for case in sorted(cases):
        stitch_case(case, input_root, output_root)

if __name__ == "__main__":
    main()
