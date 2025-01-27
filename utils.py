from transformers import T5Tokenizer, T5ForConditionalGeneration, VitsModel, AutoTokenizer
import torch
import soundfile as sf

# Инициализация моделей
# Перевод
translation_model_name = 'utrobinmv/t5_translate_en_ru_zh_large_1024_v2'
translation_model = T5ForConditionalGeneration.from_pretrained(translation_model_name)
translation_tokenizer = T5Tokenizer.from_pretrained(translation_model_name)

translation_model.eval()
translation_model.to('cpu')  # Для GPU используйте 'cuda'

# Озвучивание
tts_model_name = "facebook/mms-tts-rus"
tts_model = VitsModel.from_pretrained(tts_model_name)
tts_tokenizer = AutoTokenizer.from_pretrained(tts_model_name)

def translate_text_to_russian(text):
    """Перевод текста с английского на русский."""
    prefix = 'translate to ru: '
    input_text = prefix + text
    input_ids = translation_tokenizer(input_text, return_tensors="pt")
    with torch.no_grad():
        translated_ids = translation_model.generate(**input_ids)
    translated_text = translation_tokenizer.batch_decode(translated_ids, skip_special_tokens=True)[0]
    return translated_text

def synthesize_speech_from_text(text, output_audio_path="output.wav"):
    """Озвучивание текста на русском и сохранение в аудиофайл."""
    tts_inputs = tts_tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        audio_output = tts_model(**tts_inputs).waveform

    # Сохранение аудио в файл
    sf.write(output_audio_path, audio_output.squeeze().numpy(), tts_model.config.sampling_rate)
    return output_audio_path