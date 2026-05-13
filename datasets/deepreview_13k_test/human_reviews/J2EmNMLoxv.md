# SyncFlow: Temporally Aligned Joint Audio-Video Generation from Text

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Video and audio are closely correlated modalities that humans naturally perceive together. While recent advancements have enabled the generation of audio or video from text, producing both modalities simultaneously still typically relies on either a cascaded process or multi-modal contrastive encoders. These approaches, however, often lead to suboptimal results due to inherent information losses during inference and conditioning. In this paper, we introduce SyncFlow, a system that is capable of simultaneously generating temporally synchronized audio and video from text. The core of SyncFlow is the proposed dual-diffusion-transformer (d-DiT) architecture, which enables joint video and audio modelling with proper information fusion. To efficiently manage the computational cost of joint audio and video modelling, SyncFlow utilizes a multi-stage training strategy that separates video and audio learning before joint fine-tuning. Our empirical evaluations demonstrate that SyncFlow produces audio and video outputs that are more correlated than baseline methods with significantly enhanced audio quality and audio-visual correspondence. Moreover, we demonstrate strong zero-shot capabilities of SyncFlow, including zero-shot video-to-audio generation and adaptation to novel video resolutions without further training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces SyncFlow, a text-to-video-and-audio generation model that uses rectified flow within a dual Diffusion Transformer (d-DiT) architecture to synchronize audio and video outputs. To enhance efficiency, SyncFlow employs multi-stage training. Experimental results show that SyncFlow achieves competitive performance compared to baseline methods.

### Strengths
1. The proposed approach of using a dual-diffusion transformer for joint video-audio generation sounds reasonable.
2. Modality adaptor improves audio quality and audio-video synchronization, as verified by the lower validation loss.

### Weaknesses
The principal weaknesses of this work are as follows:

1. The paper lacks a sufficient comparison with relevant baselines. Existing works (T2AV / V2A), such as Seeing&Hearing (Xing et al., 2024), Diff-Foley (Luo et al., 2024), and V2A-Mapper [1], which provide replicable results on the VGGSound dataset, are not quantitatively or qualitatively compared. Including these baselines would offer a fair evaluation of SyncFlow’s effectiveness.

2. The experiments do not fully support the paper’s claims. Since the authors argue that a one-dimensional contrastive representation lacks sufficient temporal information, relying on the IB score alone seems insufficient to validate improved synchronization between audio and video. To better substantiate claims of enhanced audio-visual synchronization, a metric like onset accuracy (Owens et al., 2016) should be included in the GreatestHits (Owens et al., 2016) benchmark. Furthermore, to support the claim that multi-stage learning is efficient and beneficial, an ablation study on the computational cost of full joint training, or on the number of datasets required for additional joint training, would be required.

3. The paper lacks important details about the experimental settings. The anonymized baselines (e.g., T2VGen, T2A-1, T2A-2, V2A-1, and V2A-2) make it difficult to assess the paper's contributions in context. For instance, there is no clarity on the training data or architecture used for T2VGen + T2A-1/2, making it hard to discern if SyncFlow’s apparent superiority is simply due to additional training on VGG data, as seen in Table 1. Moreover, the details of contrastive loss are not explained, nor are the ablation study settings. For example, in Table 4, it is unclear how the text input is incorporated in settings like "SyncFlow-GH w/o modality adaptor" or "Text-to-Audio w/ SyncFlow Audio Tower."

4. A comparison in video format alongside audio would be valuable for verifying SyncFlow’s audio-video synchronization qualitatively.

[1] Wang, H., Ma, J., Pascual, S., Cartwright, R., & Cai, W. V2a-mapper: A lightweight solution for vision-to-audio generation by connecting foundation models. In AAAI 2024.

### Questions
1. In Table 1, why is there a performance drop in FAD, KL, and CLAP scores for SyncFlow-VGG-AV-FT compared to SyncFlow-VGG?

2. Why isn’t text information directly integrated into the audio tower? As shown in Table 4, this could improve the CLAP score. Wouldn’t incorporating text into the audio tower enhance alignment and contextual accuracy? Additionally, because audio generation depends entirely on visual input, SyncFlow seems limited in generating background sound, which could be a drawback. What are authors' thoughts on this?

3. In Table 2, how does IB Gen-V achieve a higher score than the ground truth? Is this metric reliable for evaluating alignment?

4. What exactly is the training set for the model? It appears that the VGGSound training set is used for Tables 1 and 2, while the Greatest Hits training set is used for Table 3. Why were only VGGSound and Greatest Hits chosen for training? Are these datasets considered sufficient for open-domain? Did the authors consider using larger datasets like AudioSet?

5. Unlike the authors' claim in Line 48, MM-Diffusion also conducted experiments using the open-domain dataset AudioSet. The authors need to do clearer research on related work.

6. In Figure 2, Modality Adaptor, what does the concatenation $B \times (T_v \times S + 1) \times E $ represent? Which features are being concatenated?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper titled "SyncFlow: Temporally Aligned Joint Audio-Video Generation from Text", is capable of generating temporally synchronized audio and video from textual descriptions. The core innovation of SyncFlow lies in its dual-diffusion-transformer (d-DiT) architecture, which enables joint modeling of video and audio with proper information fusion. The system employs a multi-stage training strategy to manage computational costs, initially separating video and audio learning before joint fine-tuning. SyncFlow demonstrates enhanced audio quality and audio-visual correspondence over baseline methods and exhibits strong zero-shot capabilities, including video-to-audio generation and adaptation to new video resolutions without further training.

### Strengths
1. SyncFlow addresses a significant gap in the field by providing a unified approach to generate synchronized audio and video from text.
2. The dual-diffusion-transformer architecture is a creative solution that leverages the strengths of diffusion models and transformers for multimodal generation, leading to improved synchronization and quality.
3. The model's ability to perform zero-shot generation and adaptation to new video resolutions is a significant advantage, showcasing its flexibility and generalizability.
4. The designed Modality Adaptor is a reasonable strategy to connect the two modalities, and its performance is demonstrated through ablation experiments.

### Weaknesses
1. The paper does not fully mention existing work [1] in the process of storyline design. Existing work has systematically explored the text to audio-video generation task and designed corresponding baselines, but this paper does not mention it in the introduction chapter.
[1] Mao Y, Shen X, Zhang J, et al. TAVGBench: Benchmarking Text to Audible-Video Generation. ACM MM, 2024.
2. The dataset used in this paper is relatively small (VGGSound), and only uses VideoOFA to caption the video. No caption is seen for the audio. The model trained in this way maybe cannot properly represent the information of the two modalities.
3. The designed ImageBind-based score has been proposed in [1], and the author needs to elaborate on the difference between the two.

### Questions
See [Weaknesses].

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed SyncFlow to simultaneously generate audio and video from text, where the dual-diffusion transformer structure and modality adapter are designed to jointly model audio and video with temporal synchronization. The empirical evaluations show that the proposed method generates better aligned video and audio.

### Strengths
1. The paper proposes flow-matching-based models for text-to-audio-video joint generation by designing dual diffusion transformers to handle each modality. 
2. The modality-decoupled multi-stage training strategy is proposed to efficiently make use of data and improve the quality and temporal alignment between generated audio and video. 
3. The paper is generally well-written.

### Weaknesses
1. Although the modality adapter is designed to align video with audio, there are no further explanations why just considering unidirectional (video-to-audio) fusion and how the adapter achieves the temporal alignment beyond semantic alignment. 
2. It is a little confusing why text captions are only injected into the video branch rather than both video and audio branches.
3. Some experiment details are unclear and missing. For example, what are the learning rate and optimizer for (multi-stage) training? Whether the Video VAE and Audio VAE are jointly trained, individually trained, or from frozen pre-trained ones. What are the used text-to-audio (T2A-1 and T2A-1) and video-to-audio (V2A-1 and V2A-2) models? 
4. It is better to present subjective performance by providing the demo or video files.

### Questions
1. Did you compare the proposed method with MM-Diffusion and TAVGBench discussed in the part of the related work? 
2. The text caption used in the proposed method is obtained from video. It is better for T2AV to consider more suitable text captions by describing both audio and video. 
3. The ImageBind score seems to only consider the semantic alignment. Did you try other metrics to evaluate the temporal alignment performance of the proposed model?
4. Frob Table 2, why the ground truth of the ImageBind score is not optimal like IB Gen-V & GT-T?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents SyncFlow for joint audio-video generation from a given text prompt. 
To this goal, this paper introduces a dual diffusion transformer (d-DiT) and modality-decoupled multi-stage training strategy.
SyncFlow can jointly generate 16fps videos and 48kHz audio.
The authors show the superiority on the vggsound and greatest hits datasets, and compare the model with the cascaded system.

### Strengths
- The modality-decoupled multi-stage training strategy is a practical solution for training a dual diffusion transformer.
- The results show that SyncFlow outperforms the cascaded systems and codi.

### Weaknesses
- Why do we need the RFM for this task? The authors should explain the motivation and validity of this choice. As in the Introduction section, the authors only explain that 'Both the audio and video generation components of SyncFlow are built using a flow-matching latent generative model'.  

- Why don't we need an audio-to-video adapter? Moreover, we can consider an interactional two-way adapter. There is no reason or ablation study for this. 

- It's hard to understand why the authors chose anonymized models such as T2A-1, T2A-2, etc for the evaluation part. There exist open-source text-to-audio models. I think it is unreasonable to compare the performance of the joint model without knowing the configuration and basic performance of the models.

- As the authors mentioned in 524-526, text-based audio generation shows more powerful text-audio alignment, as shown in CLAP score, why SyncFlow-GH works better than SyncFlow-GH w/o modality adapter in CLAP and KL score? The results are still confusing.

- As the authors tackled, imagebind is not good for representing temporal features. So, using another av-align score [1] or synchronized model [2] to evaluate audiovisual synchronized performance.

- I understand that the author values the task of generating audio and video based on text, but for comparison of generation quality with existing simultaneous generation methods (especially to demonstrate the efficiency and effectiveness of the proposed structure, this is not a text-specific module and structure) performance comparison in landscape or aist++ is required (using null text)

[1] Diverse and Aligned Audio-to-Video Generation via Text-to-Video Model Adaptation
[2] PEAVS: Perceptual Evaluation of Audio-Visual Synchrony Grounded in Viewers’ Opinion Scores / https://github.com/amazon-science/avgen-eval-toolkit

### Questions
-  Are the base models used in the cascaded model finetuned with vggsound? Is it fair to compare this with the SyncFlow trained on vggsound?

### Soundness
3

### Presentation
2

### Contribution
3
