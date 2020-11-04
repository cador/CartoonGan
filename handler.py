import sys
import re
from app.video import cut, generate_images, generate_videos

task = sys.argv[1]
args = sys.argv[2:]

if len(args) % 2 == 0:
    keys = []
    values = []
    for i in range(len(args)):
        if i % 2 == 0:
            if re.match('--[a-z]+', args[i]) is None:
                raise ValueError("参数错误，请修改！")
            keys.append(args[i][2:])
        else:
            values.append(args[i])
    args = {x[0]: x[1] for x in zip(keys, values)}
    fps = int(float(args.get('fps'))) if args.get('fps') is not None else None
    audio = True if args.get('audio') is not None and args.get('audio') in ('true', 'True') else False
    if task == 'cut':
        cut(args.get('source'),
            args.get('target'),
            args.get('internal'),
            args.get('coordinates'))
    elif task == 'generate_images':
        generate_images(args.get('source'),
                        args.get('target_dir'),
                        fps)
    elif task == 'generate_videos':
        generate_videos(args.get('target'),
                        args.get('from_dir'),
                        args.get('codec'),
                        args.get('audio_codec'),
                        fps,
                        audio,
                        args.get('source'),
                        args.get('internal'))
    elif task == 'examples':
        print("""
            
            1.风格测试案例：
            
                docker run -i -v ~/data:/work/ext cadorai/cartoongan:0.1 python cartoonize.py --input_dir ext/input_images --output_dir ext/output_images --all_styles --comparison_view horizontal
            
            2.cut 函数使用案例：
                
                docker run -i -v ~/data:/work/ext cadorai/cartoongan:0.1 python handler.py cut --source ext/a.mp4 --target ext/a_out.mp4 --internal 0,10:0,20 --coordinates 0,0:100,100
                
            3.generate_images 函数使用案例：
            
                docker run -i -v ~/data:/work/ext cadorai/cartoongan:0.1 python handler.py generate_images --source ext/a_out.mp4 --target_dir ext/input --fps 30
                
            4.风格转换案例：
            
                docker run -i -v ~/data:/work/ext cadorai/cartoongan:0.1 python cartoonize.py --input_dir ext/input --output_dir ext/output --styles shinkai --max_resized_height 576 --convert_gif_to_mp4 --skip_comparison 
            
            5.generate_videos 函数使用案例：
            
                docker run -i -v ~/data:/work/ext cadorai/cartoongan:0.1 python handler.py generate_videos --target ext/a_final --from_dir ext/ouput --codec libx264 --audio_codec acc --fps 30 --audio true, --source ext/a.mp4 --internal 0,10:0,20
            
        """)
    else:
        print("不支持的任务！")
else:
    print("args 错误，请修改！")
