code = """
from roop import core

core.roop.globals.source_path = "/content/based-roop/source.jpg"
core.roop.globals.target_path = "/content/based-roop/target.mp4"
core.roop.globals.output_path = "/content/based-roop/result.mp4"

core.roop.globals.frame_processors = ['face_swapper']
core.roop.globals.keep_fps = True
core.roop.globals.keep_audio = True
core.roop.globals.keep_frames = False
core.roop.globals.many_faces = False
core.roop.globals.video_encoder = 'libx264'
core.roop.globals.video_quality = 18
core.roop.globals.max_memory = 8
core.roop.globals.execution_providers = ['CPUExecutionProvider']
core.roop.globals.execution_threads = 4
core.roop.globals.headless = True

core.run()
"""

with open("/content/based-roop/run.py", "w") as f:
    f.write(code)
