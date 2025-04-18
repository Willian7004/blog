import streamlit as st
st.set_page_config(layout="wide")
st.title("多媒体生成类模型")
st.write("为了调整内容分布，这里把AIGC领域较常用的几类模型放到这一部分，相比之前添加了音频类模型，统称多媒体生成类模型，移除了不常用的视频增强模型。")
st.subheader("1.绘画模型", divider=True)
st.write("闭源绘画模型中虽然有其它画质更好的选项，但支持直接通过对话生成和编辑图片的GPT 4o和Gemini2.0 Flash成为主流。开源绘画模型能对标的是Lumina mGPT2.0，但效果不太理想且进行部署的显存门槛高。另外，如果只需要实现快速调用一致性控制功能，可以用Omnigen，光照还行但结构表现差不少，建议分辨率720p。")
st.write("对于其它开源绘画模型，我尝试了Cogview4等模型，虽然光照有优势但细节不如Flux.1，并且由于缺乏生成速度优化，生成也慢不少。后来决定找Flux.1的微调模型，由Flux.1 dev微调的Pixelwave把光照和材质表现提高到了可用水平，基本满足要求。")

st.subheader("2.视频模型", divider=True)
st.write("闭源视频模型分为高成本和低成本路线，可灵1.6成本适中，总体效果也比较好但运动物体画质差一些，后面推出的可灵2.0效果好一些但成本也高不少；Veo2成本高，在运动物体画质和分辨率方面有优势。")
st.write("开源视频模型中，虽然此前不少模型运行成本也较高，但Controlnet的作者改进了的Hunyuan Video图生视频版本，推出了FramePack，使用6g显存即可实现任意长度推理但实用长度约为1分钟，我使用3070m的单帧生成时间约20秒。由于从尾帧开始生成，大范围运动的场景生成效果不好，非固定场景建议把生成长度控制在4秒。")
st.write("长视频创作中一致性控制和上下文功能比较重要。不少闭源模型提供了一致性控制功能，开源模型少一些但在Hunyuan Video Wrapper插件也提供了主体参考等功能。Sora虽然生成效果没有优势，但提供了story board功能，可以通过上下文实现多个片段的内容一致。")

st.subheader("3.TTS模型", divider=True)
st.write("TTS模型用于语音合成。目前没有比较好的可以图形化运行TTS模型的运行框架，以前我主要使用一些模型的第三方整合包，后来看到Fish Speech可以通过官方代码以整合包形式快速部署，支持fastapi，官方还做了Windows版本的GUI应用，生成时能按句子进行分割，就在TTS模型上改用Fish Speech。虽然不完全真实但效果优于大部分同类模型。显存占用约2g，部署门槛比较低。另外，Zonos v0.1等模型搭配了LLM，可以更好地处理语气；Kokoro 82m参数量小，推理更快。不过考虑到方面部署和使用，还是继续用Fish Speech。")

st.subheader("4.音乐模型", divider=True)
st.write("开源音乐模型效果最好的是YuE，与Suno等商业模型效果相当。DiffRhythm速度更快，但上下文衔接差一些。算力不太低的话用YuE比较合适。")

st.subheader("4.模型部署", divider=True)
st.write("绘画模型、视频模型和一些其它类型的模型一般使用ComfyUI部署。主要优势是有显存优化并且可以提供插件适配更多模型。为了方便管理插件和运行环境，可以使用绘世等第三方整合包。音乐模型方面，Comfyui只能用效果比较差的Stable Audio Open，Yue s1需要用官方代码部署，显存要求10g以上并且随音轨数增加，相对难以普及。")
