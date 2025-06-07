
import ffmpeg
import os

input_path = 'fizio_sr.mp4'
output_with_audio = 'fizio_with_audio.mp4'
output_no_audio = 'fizio_no_audio.mp4'

try:
    # Версия с аудио для десктопа
    print(f"🎬 Обработка версии со звуком: {output_with_audio}")
    (
        ffmpeg
        .input(input_path)
        .output(
            output_with_audio,
            vcodec='libx264',
            acodec='aac',
            preset='slow',
            crf=23,
            movflags='faststart'
        )
        .overwrite_output()
        .run()
    )
    print(f"✅ Готово: {output_with_audio}")

    # Версия без аудио для мобильных (автовоспроизведение)
    print(f"🎬 Обработка версии без звука: {output_no_audio}")
    (
        ffmpeg
        .input(input_path)
        .output(
            output_no_audio,
            vcodec='libx264',
            preset='slow',
            crf=23,
            movflags='faststart',
            an=None  # удаление звука
        )
        .overwrite_output()
        .run()
    )
    print(f"✅ Готово: {output_no_audio}")

except ffmpeg.Error as e:
    print("❌ Ошибка при обработке видео:")
    print(e.stderr.decode())
