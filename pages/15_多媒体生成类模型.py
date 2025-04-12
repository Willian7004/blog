import streamlit as st
st.set_page_config(layout="wide")
st.title("多媒体生成类模型")
st.write("为了调整内容分布，这里把AIGC领域较常用的几类模型放到这一部分，相比之前添加了音频类模型，统称多媒体生成类模型，移除了不常用的视频增强模型。")
st.subheader("1.绘画模型", divider=True)
st.write("闭源绘画模型中虽然有其它画质更好的选项，但支持直接通过对话生成和编辑图片的GPT 4o和Gemini2.0 Flash成为主流。开源绘画模型能对标的是Lumina mGPT2.0，但效果不太理想且进行部署的显存门槛高。")
st.write("其它开源绘画模型中cogview4比较有优势，支持横屏和竖屏1080p，光照和细节表现较好，人物结构表现一般。目前只能通过diffusers库推理，速度较慢，使用3070m开启sequential cpu offload显存占用1.4g，推理时间8分钟。")

st.subheader("2.视频模型", divider=True)
st.write("视频模型分为高成本和低成本路线。开源模型方面，Wan2.1系列在运动效果和出片率等方面有优势，14b版本使用3070m运行720p 33帧 30步推理并使用teacache的推理时间为30分钟（rel_l1_treash设为0.1，官方参数有一定画质损失），1.3b版本场景细节差一些但使用3070m运行720p 49帧推理时间为17分钟。闭源模型方面，可灵1.6成本适中，总体效果也比较好但运动物体画质差一些；Veo2成本高，在运动物体画质和分辨率方面有优势。")
st.write("长视频创作中一致性控制和上下文功能比较重要。不少闭源模型提供了一致性控制功能，开源模型少一些但在Hunyuan Video Wrapper插件也提供了主体参考等功能。Sora虽然生成效果没有优势，但提供了story board功能，可以通过上下文实现多个片段的内容一致。")

st.subheader("3.TTS模型", divider=True)
st.write("TTS模型用于语音合成。目前没有比较好的可以图形化运行TTS模型的运行框架，以前我主要使用一些模型的第三方整合包，后来看到Fish Speech可以通过官方代码以整合包形式快速部署，支持fastapi，官方还做了Windows版本的GUI应用，生成时能按句子进行分割，就在TTS模型上改用Fish Speech。虽然不完全真实但效果优于大部分同类模型。显存占用约2g，部署门槛比较低。另外，Zonos v0.1等模型搭配了LLM，可以更好地处理语气；Kokoro 82m参数量小，推理更快。不过考虑到方面部署和使用，还是继续用Fish Speech。")

st.subheader("4.音乐模型", divider=True)
st.write("开源音乐模型效果最好的是YuE，与Suno等商业模型效果相当。DiffRhythm速度更快，但上下文衔接差一些。算力不太低的话用YuE比较合适。")

st.subheader("4.模型部署", divider=True)
st.write("绘画模型、视频模型和一些其它类型的模型一般使用ComfyUI部署。主要优势是有显存优化并且可以提供插件适配更多模型。为了方便管理插件和运行环境，可以使用绘世等第三方整合包。音乐模型方面，Comfyui只能用效果比较差的Stable Audio Open，Yue s1需要用官方代码部署，显存要求10g以上并且随音轨数增加，相对难以普及。")

