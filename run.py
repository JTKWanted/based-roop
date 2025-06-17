from roop import core

# Cargar tu imagen fuente (cara) y destino (video o imagen)
SOURCE_PATH = '/content/source.jpg'
TARGET_PATH = '/content/target.mp4'  # Puede ser .jpg, .png o .mp4
OUTPUT_PATH = '/content/result.mp4'  # o .jpg

# Ejecutar el face swap
core.run(
    source_path=SOURCE_PATH,
    target_path=TARGET_PATH,
    output_path=OUTPUT_PATH,
    frame_processors=[],
    keep_fps=True,
    many_faces=False
)
