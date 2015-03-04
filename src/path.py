import os
base_path = os.path.split(os.path.dirname(__file__))[0]
assets_path = os.path.abspath(os.path.join(base_path, 'assets'))
font_path = os.path.abspath(os.path.join(assets_path, 'fonts'))
image_path = os.path.abspath(os.path.join(assets_path, 'Images'))
download_path = os.path.abspath(os.path.join(assets_path, 'download'))