## Using YOLO v8 to Train HCN and Required Files

### Files Required

1. **datacollection.py**
   - **Purpose:** Collect images for training by using `pyautogui.screenshot()` to take screenshots, then crop, merge, and number them, etc. The resulting images are stored in a separate folder.

2. **trainModule.py**
   - **Requirement:** Must include the following 4 items (must have).

3. **test.yaml**
   - **Purpose:** This file is required for training.
     - It informs the program how many classes there are.
     - It stores the path to the dataset folder.

4. **dataset (folder)**
   - **Directory Structure:**
     ```
     dataset/
       ├── images/         # Contains images
       │     ├── train/    # 90% of the images
       │     └── val/      # Remaining 10% of the images
       └── labels/         # Contains labels generated using makesense.ai (number of images = number of labels)
             ├── train/    # 90% of the labels
             └── val/      # Remaining 10% of the labels
     ```

5. **useTrainedModule.py**
   - **Purpose:** As the name suggests, this module is used to run the trained model.
   - After training, the model is saved as `best.pt` in the `run` folder for use.
   - To continue training, the file `last.pt` is used to resume training.
