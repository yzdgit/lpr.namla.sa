import
from ultralytics import YOLO

# Paths
OUTPUT_FOLDER = 'data/output'
DETECT_WEIGHT = 'models/detect.onnx'
READ_WEIGHT = 'models/read.onnx'
LOG_FILE = 'info.log'

# Set up logging - TODO

# Load Models
try:
  detect_model = YOLO(DETECT_WEIGHT)
  read_model = YOLO(READ_WEIGHT)
except Exception as e:
  print('Failed to load models: {str(e)}')

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

id_to_char = {
  '00': '0', '01': '1', '02': '2', '03': '3', '04': '4',
  '05': '5', '06': '6', '07': '7', '08': '8', '09': '9',
  '10': 'A', '11': 'B', '12': 'D', '13': 'E', '14': 'G',
  '15': 'H', '16': 'J', '17': 'K', '18': 'L', '19': 'N',
  '20': 'R', '21': 'S', '22': 'T', '23': 'U', '24': 'V',
  '25': 'X', '26': 'Z' }

def decode_plate(predictions)
  try:
    decoded_text = ''.join(id_to_char[f"{int(pred):02d}"] for pred in predictions)
    return decoded_text
  except KeyError as e:
    print('Unknown character in plate: {str(e)}')

# Process Image - TODO

# Flask Server - TODO
