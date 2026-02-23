# core/logger.py
import logging

# Create a logger
logger = logging.getLogger("AI_Text_Engine")
logger.setLevel(logging.DEBUG)  # Capture everything from DEBUG and above

# Create handlers
c_handler = logging.StreamHandler() # Terminal
f_handler = logging.FileHandler("app.log", encoding="utf-8") # File

# Set levels for terminal
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.DEBUG)

# Format
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(log_format)
f_handler.setFormatter(log_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)