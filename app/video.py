from moviepy.editor import *


def cut(source, target, internal, coordinates):
    """
    剪辑video
    :param source: 来源文件
    :param target: 目标文件
    :param internal: 定义时间段，'minutes_0,seconds_0:minutes_1,seconds_1'
    :param coordinates: 定义区域，'x1,y1:x2,y2'
        x1、y1：代表矩形区域左上角坐标
        x2、y2：代表矩形区域右下角坐标
    :return:
    """
    start, end = internal.split(':')
    start = tuple([int(x) for x in start.split(',')])
    end = tuple([int(x) for x in end.split(',')])
    left_up, right_down = coordinates.split(':')
    left_up = tuple([float(x) for x in left_up.split(',')])
    right_down = tuple([float(x) for x in right_down.split(',')])
    clip = (VideoFileClip(source).subclip(start, end).crop(x1=left_up[0], y1=left_up[1],
                                                           x2=right_down[0], y2=right_down[1]))
    clip.write_videofile(target)


def generate_images(source, target_dir, fps=None):
    """
    将video分割成一帧帧图片
    :param source: 来源文件
    :param target_dir: 存储的目标文件夹
    :param fps: 帧频
    :return:
    """
    clip = VideoFileClip(source)
    clip.write_images_sequence("%s/frame%05d.png" % target_dir, fps=fps)


def generate_videos(target, from_dir, codec=None, audio_codec=None, fps=None, audio=False, source=None, internal=None):
    """
    生成视频
    :param target: 目标文件路径及名称
    :param from_dir: 存储图片的路径
    :param codec:
    :param audio_codec:
    :param fps: 帧频
    :param audio: 是否包含声音，默认没有，若设置为True，则需同时设置source和internal
    :param source: 来源文件
    :param internal: 同函数<cut>的internal
    :return:
    """
    clip = ImageSequenceClip(from_dir, fps=fps)
    if not audio:
        clip.write_videofile(target, fps=fps, codec=codec, audio_codec=audio_codec)
    else:
        start, end = internal.split(':')
        start = tuple([int(x) for x in start.split(',')])
        end = tuple([int(x) for x in end.split(',')])
        audio_clip = (AudioFileClip(source).subclip(start, end))
        out = clip.set_audio(audio_clip)
        out.write_videofile(target, fps=fps, codec=codec, audio_codec=audio_codec)
