# Unifying Specialized Visual Encoders for Video Language Models

- Decision: Reject
- Scores: 8, 5, 5, 6

## Abstract
The recent advent of Large Language Models (LLMs) has ushered sophisticated reasoning capabilities into the realm of video through Video Large Language Models (VideoLLMs). However, VideoLLMs currently rely on a single vision encoder for all of their visual processing, which limits the amount and type of visual information that can be conveyed to the LLM. Our method, MERV, Multi-Encoder Representation of Videos, instead leverages multiple frozen visual encoders to create a unified representation of a video, providing the VideoLLM with a comprehensive set of specialized visual knowledge. Spatio-temporally aligning the features from each encoder allows us to tackle a wider range of open-ended and multiple-choice video understanding questions and outperform prior state-of-the-art works on their data mixes. MERV is up to 3.79% better in accuracy than Video-LLaVA across the standard suite video understanding benchmarks, while also having a better Video-ChatGPT score. We also improve upon SeViLA, the previous best on zero-shot Perception Test accuracy, by 2.21%. MERV introduces minimal extra parameters and trains faster than equivalent single-encoder approaches. Finally, we provide qualitative evidence that our model captures domain knowledge from each encoder simultaneously, such as on the motion classification tasks found in Something-Something v2. Our results offer promising directions for future research in utilizing multiple vision encoders for comprehensive video understanding.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper focuses on the vision encoder designs of VideoLLMs and proposes MERV (Multi-Encoder Representation of Videos) that utilizes multiple visual encoders to enhance the VideoLLMs' capabilities. MERV utilizes a spatial expert (DINOv2), a temporal expert (ViViT), an image-language contrastive expert (SigLIP), and a video-language contrastive expert (LanguageBind) as mixed video encoders and designs a pre-fusion projection to align their embedding size, then use cross-attention to perform spatial-temporal fusion as LLM's input. Extensive experiments demonstrate MERV's effectiveness and efficiency on multiple benchmarks.

### Strengths
1. This paper is well-written and easy to follow. The paper is well-motivated and the discussion of related works is clear, the method and experiment sections provide details for the proposed methods.
2. The proposed method MERV effectively combines multiple visual encoders to capture a wider range of video understanding capabilities is a significant advancement. The experiments and comparisons on multiple benchmarks show the effectiveness of such multi-encoder structures. Meanwhile, MERV introduces minimal extra parameters and computational overhead compared to existing single-encoder approaches, making it more suitable for practical use.
3. The paper includes well-conducted ablation studies on feature fusion strategies, pre-fusion projectors, and encoder combinations, providing insight into the effectiveness of design choices.

### Weaknesses
1. This paper shows that combining 4 typical encoders improves the capability of the VideoLLMs, I'm wondering if such gain from integrating more encoders further exists when more encoders are utilized.
2. It would provide more interpretability if the authors could do some analysis on how is each encoder chosen and utilized by the fusion module in some typical tasks.

### Questions
Please see the weakness section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper propose a encoder ensembing method to mitigate the shortcoming of a single visual encoder for video understanding. The fusion module is based on cross-attention layers. Extensive experiments are conducted on multimodal benchmarks like MSRVTT, TGIF, and motion-oriented visual benchmark, SSV2. Quantitatively and qualitatively reulsts verifies the skill specializations of different visual experts and better performance is achieved compared with state-of-the-art methods.

### Strengths
- The motivation is reasonable. As videos contain both static and dynamic cues across diverse objects and scenes, different video encoders may capture different parts of the video and could help each other. 

- The presentation is mostly clear.

- Technical details are clearly described and the reproducibility is good.

### Weaknesses
 - While a performance boost is observed, my primary concern is that the novelty of this paper is limited. Similar to [1], the paper presents an empirical solution for ensembling multiple visual encoders in multimodal models. The feature fusion operation relies on cross-attention and linear projection layers, lacking an in-depth analysis of feature interactions. As ensembling is the basic idea in machine learning, this paper does not provide new insights, and the performance improvement is unsurprising given the increased computational costs.

 - Scalability of the proposed method is unclear. According to the experiments in Table 4, it appears that the only video backbone, ViViT, has a slight influence on the final performance. Combined with the results in Figure 5, there seems to be a contradiction regarding the effectiveness of a temporal-oriented feature encoder when applied to videoMLLM benchmarks. In light of this, I am concerned about the extensibility of the proposed method. To what extent can the model be applied to additional visual backbones?

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes using multiple specialized visual encoders as ensembles to enhance the representation of videos in visual language models. The goal is to improve the model's ability to capture diverse visual information by leveraging the strengths of different encoders. The authors incorporate visual encoders such as SigLIP, DinoV2, ViViT, and LanguageBind, each contributing unique spatial, temporal, and multimodal understanding capabilities, making the ensemble more comprehensive. A feature fusion module is introduced to combine features from these visual encoders. The fusion process involves a cross-attentive encoder mixer, which aligns and integrates features from different encoders, allowing for a unified representation that retains important spatio-temporal details. The authors evaluated different combinations of visual encoders using the proposed fusion module on multiple video understanding benchmarks, including MSVD-QA, ActivityNet-QA, and Something-Something v2. Improvements in accuracy were observed, demonstrating the potential of the multi-encoder approach.

### Strengths
1. **Multi-Encoder Approach:** The use of multiple specialized visual encoders aims to provide a more comprehensive understanding of video content by leveraging the capabilities of each encoder. This approach attempts to capture diverse types of visual information, including spatial, temporal, and multimodal aspects, which may enhance the model's performance on video language tasks.

2. **Experimental Design:** The authors provide an extensive experimental study of the combination of visual encoders, considering individual and joint usage. This exploration offers insights into practitioners into the effectiveness of different encoder combinations. Additionally, the authors analyze the impact of training stages in LLaVa-style VLM training for videos, providing observations on the importance of each stage in the two-stage training process.

3. **Performance on Benchmarks:** The proposed method demonstrates improvements in video understanding accuracy across multiple tested benchmarks. The reported accuracies outperform existing baselines, suggesting the potential benefits of the multi-encoder fusion strategy.

4. **Efficiency and Implementation:** The proposed fusion module is designed to be lightweight and straightforward to implement, which makes it accessible for integration into existing systems. This ease of implementation could facilitate adoption without requiring substantial computational resources or complex modifications.

### Weaknesses
1. **Novelty Concerns:** The use of multiple visual encoders has become a common paradigm for visual language models [R1, R2, R3], primarily for image-based visual input. The authors have not provided sufficient reasoning to demonstrate the novelty of extending this approach to video. The method mainly involves passing multiple video frames through image-based visual encoders, with ViViT being the only video-specific embedding model. This limits the originality of the proposed multi-encoder approach. While the inclusion of ViViT is noted, the core mechanism still relies heavily on adapting image-based encoders to video data, which is not a novel contribution. The paper does not adequately address how the proposed method differs fundamentally from existing multi-encoder techniques applied to video, beyond simply including a video-specific encoder. The authors should provide a more detailed explanation of the unique challenges and solutions associated with extending multi-encoder approaches to video, rather than just stating that they have included a video model.

2. **Feature Fusion Module Effectiveness:** The proposed feature fusion module lacks a clear advantage. Table 2 indicates that the cross-attention feature fusion yields nearly the same accuracy as a simple channel concatenation approach. Additional statistical significance testing might be needed to substantiate the performance difference if it is considered significant by the authors. Without stronger evidence, the proposed fusion module may not provide enough of a meaningful contribution. The paper lacks a rigorous statistical analysis to demonstrate the superiority of the cross-attention mechanism over simpler concatenation. The current results suggest that the added complexity of the cross-attention module may not be justified, given the marginal performance gains. Furthermore, the analysis of the fusion module should include an investigation into the computational cost and parameter overhead associated with the cross-attention mechanism compared to concatenation, which could further justify or undermine its use.

### Questions
1. **Computational Trade-offs:** Given that using multiple visual encoders improves accuracy at the cost of increased computational demands, can the authors provide a detailed analysis of the runtime differences between using a single encoder versus multiple encoders?

2. **Fusion Module Significance:** Can the authors clarify the significance of the proposed feature fusion module in comparison to simpler methods? What specific scenarios or tasks benefit most from this module compared to other straightforward techniques like concatenation?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Video Large Language Models (VideoLLMs) currently use only a single vision encoder while different vision encoders have their own strengths. This leads to limited capabilities of resulting VideoLLMs on various downstream tasks. The paper proposes a well-established framework for training VideoLLMs using multiple vision encoders. It empirically ablates the following four aspects: i) which visual encoders to use, ii) how to align and fuse visual features from different vision encoders, and iii) training recipes and data mixture. The authors also implement an efficient feature extraction and projection pipeline for efficiently using multiple vision encoders.

### Strengths
This paper is one of the pioneering work that establish the training framework for using multiple vision encoders for VideoLLMs
- by demonstrating the model's superiority on multiple downstream tasks
- through a bunch of ablation studies for validating the design choices and answering the key questions

Although the paper does not propose novel methodologies, I think it is quite valuable because there are a flood of VideoLLMs that are trained using their own data mixture and recipes. Researchers are quite confused and have questions like which vision encoder to use, whether to pretrain the adapter between the vision encoder and LLM, whether to unfreeze the vision encoder or LLM in Stage 1 training, etc. The paper provides extensive empirical results answering these questions especially for VideoLLMs using multiple vision encoders.

### Weaknesses
Overall the paper is quite good but answering the following concerns would make the paper better and more self-contained:

- After finishing reading, I am still not sure when I should use the MERV training recipe and when to use the MERV-Full. It would be great to give some general instructions on this.
- The chosen video model, ViViT, was published in 2021. It would be great to provide the empirical results with other recent methods including both supervised and unsupervised (self-supervised), e.g., Video Swin Transformer [1], MViTv2 [2] for supervised and VideoMAE v2 [3] for unsupervised.
- Figure 4 (b) and Figure 5 illustrate and disentangle the individual contributions of contrastive methods and the video model, ViViT, to model performance, but I cannot figure out whether there are distinct differences between contrastive methods from the figures. I cannot even find noticeable trends in Figure 3, e.g., DINOv2 outperforms SigLIP on MSRVTT-Who while it lags behind SigLIP on MSVD-Who.
- In Section 3.4, it would be great to elaborate on how to make feature extraction and projection happen in parallel.
- The authors often claimed in the paper that they found video-language alignment was not very strong for the MERV recipe, e.g., L393-L394. How did the authors observe or verify that?

[1] Ze Liu et al., Video Swin Transformer, CVPR 2022.
[2] Yanghao Li et al., MViTv2: Improved Multiscale Vision Transformers for Classification and Detection, CVPR 2022.
[3] Limin Wang et al., VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking, CVPR 2023.

### Questions
Please address the above concerns, and there are some minor questions:

- Are single encoder models in Figure the variants of MERV?
- What is the role of P_e: to differentiate between different encoder features? If then, why did the authors name it "positional" embeddings? And why does MERV need this explicit differentiation between the encoder features?
- L254-L255: Does it take 24 hours with 8 L40-48GB GPUs for MERV or MERV-Full?
- Table 1: Please add the columns to specify which vision encoder and llm are used for each method, and TGIF score for Video-ChatGPT is missing in Table 1 (3.0, L309)
- L338: Does 3D Conv in Table 2 (a) apply a 2D 3x3 convolution? Naming is confusing.

Also, please fix typos in the paper.

### Soundness
3

### Presentation
3

### Contribution
3
