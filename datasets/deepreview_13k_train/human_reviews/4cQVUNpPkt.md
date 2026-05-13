# FOLEYCRAFTER: BRING SILENT VIDEOS TO LIFE WITH LIFELIKE AND SYNCHRONIZED SOUNDS

- Decision: Reject
- Scores: 8, 6, 3

## Abstract
We study Neural Foley, the automatic generation of high-quality sound effects synchronizing with videos, enabling an immersive audio-visual experience.
Despite its wide range of applications, existing approaches encounter limitations when it comes to simultaneously synthesizing high-quality and video-aligned (\ie, semantic relevant and temporal synchronized) sounds.
To overcome these limitations, we propose \modelname, a novel framework that leverages a pre-trained text-to-audio model to ensure high-quality audio generation. \modelname\ comprises two key components: the \semanticmodule\ for semantic alignment and the \temporalmodule\ for precise audio-video synchronization. The \semanticmodule\ utilizes parallel cross-attention layers to condition audio generation on video features, producing realistic sound effects that are semantically relevant to the visual content. Meanwhile, the \temporalmodule\ incorporates an onset detector and a timestamp-based adapter to achieve precise audio-video alignment.
One notable advantage of \modelname\ is its compatibility with text prompts, enabling the use of text descriptions to achieve controllable and diverse video-to-audio generation according to user intents.
We conduct extensive quantitative and qualitative experiments on standard benchmarks to verify the effectiveness of \modelname.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a new video-to-audio model, featured by the semantic adapter and temporal adapter. The proposed model uses the [Auffusion](https://arxiv.org/abs/2401.01044) model as a baseline, and not only video-audio paired data but also text-audio paired data are used for training its sub-modules for connecting between the visual encoder and Auffusion. The temporal adapter, trained with the BCE loss or MSE loss to estimate the energy map of audio from video, enhances the synchronization between video and audio. The authors conducted both quantitative and qualitative comparisons with previous video-to-audio models to demonstrate that the proposed model outperforms them. They also conducted ablation studies to show that their proposed semantic and temporal adapters are effective.

### Strengths
1. Although there is room for improvement in writing style, the paper itself is well-written enough to make readers understand their motivation, the proposed method, and the experimental results.
2. The proposed video-to-audio model is well-designed to address the issue of synchronization between video and audio. There may be other designs for resolving the issue, but they conducted ablation studies to demonstrate that their designed model works well.
3. The authors quantitatively evaluated their model on the commonly used benchmarks and qualitatively analyzed the audio signals generated from the proposed and previous models for comparison. These experimental results show that the proposed model outperforms the previous models.

### Weaknesses
- L.365: "We employed several evaluation metrics to assess semantic alignment and audio quality, namely Mean KL Divergence (MKL) (Iashin and Rahtu, 2021), CLIP similarity, and Frechet Distance (FID) (Heusel et al., 2017), following the methodology of previous studies (Luo et al., 2023; Wang et al., 2024; Xing et al., 2024). MKL measures paired sample-level similarity"
  - The application of FID to audio quality evaluations is proposed by [Iashin and Rahtu (2021)](https://www.bmvc2021-virtualconference.com/conference/papers/paper_1213.html), and [Luo et al. (2023)](https://proceedings.neurips.cc/paper_files/paper/2023/hash/98c50f47a37f63477c01558600dd225a-Abstract-Conference.html) followed them. However, [Wang et al. (2024)](https://ojs.aaai.org/index.php/AAAI/article/view/29475) and [Xing et al. (2024)](https://openaccess.thecvf.com/content/CVPR2024/html/Xing_Seeing_and_Hearing_Open-domain_Visual-Audio_Generation_with_Diffusion_Latent_Aligners_CVPR_2024_paper.html) use different metrics, FD ([Liu et al., 2023](https://proceedings.mlr.press/v202/liu23f.html)) and FAD ([Kilgour et al., 2019](https://www.isca-archive.org/interspeech_2019/kilgour19_interspeech.html)). I recommend the authors additionally evaluate their proposed model with these metrics for several reasons. The FID and FAD are calculated from spectrograms and do not consider phase information of audio signals. The FD is based on the PANN network ([Kong et al., 2020](https://ieeexplore.ieee.org/document/9229505)), which takes audio waveforms and achieves better performance in classification tasks than VGGish. Plus, recent papers use FAD or FD more frequently. The evaluation on these metrics will be informative to readers, which means the authors can contribute more to the community.

### Questions
I would appreciate the authors' response to my comments in "Weaknesses".

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper introduces FoleyCrafter, a framework designed for automatically generating realistic and synchronized sound effects for silent videos. FoleyCrafter leverages a pre-trained text-to-audio model, incorporating a “semantic adapter” and “temporal adapter” to ensure that the generated audio is semantically aligned with video content and precisely synchronized over time. Additionally, it supports customizable audio generation through text prompts. The primary contributions include: 1) presenting a novel neural Foley framework for high-quality, video-aligned sound generation, 2) designing semantic and temporal adapters to improve audio-video alignment, and 3) achieving state-of-the-art performance on benchmarks through comprehensive quantitative and qualitative evaluations.

### Strengths
1.	Originality: This paper introduces an innovative framework, FoleyCrafter, which stands out in the field of sound generation for silent videos. By combining a pre-trained text-to-audio model with novel adapter designs (semantic and temporal adapters), it effectively addresses the limitations of existing methods in terms of audio quality and video synchronization, showcasing unique and original thinking.
2.	Quality: The paper demonstrates high research quality through comprehensive experimental design and implementation. It includes extensive quantitative and qualitative experiments, validating the effectiveness of FoleyCrafter on standard benchmark datasets. The results show that this method surpasses several state-of-the-art approaches in both audio quality and synchronization performance. Additionally, the availability of code and models facilitates future replication and research.
3.	Clarity: The paper is well-structured, with clear explanations of concepts and model design, allowing readers to easily understand how FoleyCrafter operates. The figures and results in the experimental section are also well-presented, enabling readers to intuitively grasp the method’s performance and advantages.
4.	Significance: FoleyCrafter holds substantial application potential in the field of video-to-audio generation. This approach not only enhances the realism and synchronization of sound effects but also offers controllability and diversity through text-based prompts. Such innovations have broad applicability in multimedia production, including film and gaming, and further advance cross-modal generation technology in the audio-visual domain.

### Weaknesses
The paper’s originality appears limited. The whole model system exploits many present models, such as Freesound Project and Auffusion.
Although the part of Quantitative Comparison includes evaluations in terms of semantic alignment, audio quality and temporal synchronization, the comparison of audio generation speed has not been expressed.
The lack of some ablation experiments for Semantic Adapter and Temporal Controller weakens persuasiveness. The Semantic Adapter could be entirely removed to observe the system’s performance without visual semantic information. The Onset Detector and Timestamp-Based Adapter could be individually removed to investigate their roles in temporal alignment and onset detection. In addition, it would be more persuasive if ablation experiments for Parallel Cross-Attention with different λ had been done.

### Questions
Refer to Weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors proposed a framework called FoleyCrafter to synthesize high-qulity audio with text prompt, which contains two key components as follows:
1.Semantic adapter condition generated audio conditioned on video features, rendering more semantically relevance.
2.Temporal adapter estimates time signals, synchronizing with audio.
The authors carried experiments on two datasets and achieved better performance compared with current powerful models.

### Strengths
1.Originality: The authors proposed two adapters to improve the audio synthesis. However, the structure inside originates from other works.
2.Quality: Although the method proposed is effective compared to others, it lacks rigorous mathematical proof.
3.Clarity: Semantic adapter has not been clarified clearly, especially the cross-attention component.
4.Significance: The significance of the method is relatively high comparing to existing methods. However, parameters to be trained is relatively high compared to others.

### Weaknesses
1.Lack of Innovation: In this article, there are two key components. However, the semantic adapter is derived from the IP-adapter[1], while the temporal adapter originates from ControlNet[2]. This article lacks substantial original contributions.
2.Inference Latency Concerns: In the articles mentioned above, the authors only add a single adapter to the original model. However, in this article, the proposed method includes two separate adapters, which may result in higher inference latency, potentially impeding efficiency and scalability.
3.Insufficient Analysis of Text Prompts: In this article, there are text prompts and video prompts for audio generation. However, The authors provide only a qualitative description of the text prompt's capabilities, without comparing it to other models.

### Questions
No

### Soundness
2

### Presentation
1

### Contribution
2
