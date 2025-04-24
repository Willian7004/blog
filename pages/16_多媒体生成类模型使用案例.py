import streamlit as st
st.set_page_config(layout="wide")
st.title("多媒体生成类模型使用案例")
st.write("相比复杂的工作流，我更偏向使用功能完善的模型通过较简单的流程做到较好的效果。由于之前生成的内容已发布到社交媒体，为了避免内容重复，这里只展示新生成的内容。之前的图片内容发布在https://www.xiaohongshu.com/user/profile/6605a535000000000b00c4d2? ，视频内容发布在https://space.bilibili.com/478036060? 和https://www.acfun.cn/u/76077623 （包含其它类型的图片和视频）")

st.subheader("1.绘画模型", divider=True)
st.write("Hunyuan Video Gallery 项目，图片部分展示使用Hunyuan Video图片，复用了之前使用Flux.1的提示词： https://william7004-hunyuan-video-gallery.streamlit.app/%E5%9B%BE%E7%89%87")
st.write("使用cogview4生成的图片在 https://william7004-gallery.streamlit.app/AI%E5%9B%BE%E7%89%87 ")
st.write("使用Pixelwave生成的图片在 https://william7004-new-gallery.streamlit.app/Pixelwave ")

st.subheader("2.视频模型", divider=True)
st.write("Hunyuan Video Gallery 项目，视频部分展示使用Hunyuan Video生成的视频： https://william7004-hunyuan-video-gallery.streamlit.app/%E8%A7%86%E9%A2%91")
st.write("https://william7004-gallery.streamlit.app/AI%E8%A7%86%E9%A2%91 展示了使用Wan2.1 1.3b生成的视频，复用了之前使用其它模型生成的发布在社交平台的视频的提示词并添加了一些新的内容。")
st.write("使用Wan2.1 14b生成的视频发布在： https://william7004-new-gallery.streamlit.app/AI%E8%A7%86%E9%A2%91 ")
st.write("使用Fast Hunyuan生成的视频发布在 https://william7004-new-gallery.streamlit.app/FastHunyuan ")

st.subheader("3.TTS模型", divider=True)
st.write("https://william7004-gallery.streamlit.app/LLM%E6%95%A3%E6%96%87%E9%9B%86 包含使用Fish Speech1.5合成的音频。")

st.subheader("4.音乐模型", divider=True)
st.write("https://william7004-gallery.streamlit.app/LLM%E6%9F%A5%E8%AF%A2 包含使用YuE生成的音乐。")

