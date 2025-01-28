import streamlit as st
from utils import translate_text_to_russian, synthesize_speech_from_text

# Заголовок приложения
st.title("Переводчик и озвучка текста")
st.markdown("Введите текст на английском, чтобы перевести его на русский и получить озвучку.")

# Ввод текста
user_input = st.text_area("Введите текст на английском", height=150)

if st.button("Обработать текст"):
    if user_input.strip():
        with st.spinner("Перевожу текст..."):
            translated_text = translate_text_to_russian(user_input)
        
        st.success("Перевод завершён!")
        st.markdown(f"**Переведённый текст:**\n{translated_text}")

        with st.spinner("Генерирую аудиофайл..."):
            audio_path = synthesize_speech_from_text(translated_text)

        st.success("Аудиофайл готов!")
        st.audio(audio_path, format="audio/wav")
    else:
        st.error("Введите текст для обработки!")