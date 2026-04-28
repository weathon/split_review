# TempMe: Video Temporal Token Merging for Efficient Text-Video Retrieval

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Most text-video retrieval methods utilize the text-image pre-trained CLIP as a backbone, incorporating complex modules that result in high computational overhead. As a result, many studies focus on efficient fine-tuning. The primary challenge in efficient adaption arises from the inherent differences between image and video modalities. 
Each sampled video frame must be processed by the image encoder independently, which increases complexity and complicates practical deployment.
Although existing efficient methods fine-tune with small trainable parameters, they still incur high inference costs due to the large token number. In this work, we argue that \textit{temporal redundancy} significantly contributes to the model's high complexity due to the repeated information in consecutive frames. Existing token compression methods for image models fail to solve the unique challenges, as they overlook temporal redundancy across frames. To tackle these problems, we propose Temporal Token Merging (TempMe) to reduce temporal redundancy. Specifically, we introduce a progressive multi-granularity framework. By gradually combining neighboring clips, we merge temporal tokens across different frames and learn video-level features, leading to lower complexity and better performance. Extensive experiments validate the superiority of our TempMe. Compared to previous efficient text-video retrieval methods, TempMe significantly reduces output tokens by $\mathbf{95\%}$ and GFLOPs by $\mathbf{51\%}$, while achieving a $\mathbf{1.8 \times}$ speedup and a $\mathbf{4.4\%}$ R-Sum improvement. Additionally, TempMe exhibits robust generalization capabilities by integrating effectively with both efficient and full fine-tuning methods. With full fine-tuning, TempMe achieves a significant $\mathbf{7.9\%}$ R-Sum improvement, trains $\mathbf{1.57\times}$ faster, and utilizes $\mathbf{75.2\%}$ GPU memory usage. Our code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To enhance the efficiency of text-video retrieval, this paper introduces Temporal Token Merging (TempMe), a parameter- and inference-efficient architecture aimed at reducing spatial-temporal redundancy. The framework primarily consists of ImageMe Blocks for image merging and ClipMe Blocks for clip merging, achieving a progressive multi-granularity approach. Extensive experiments validate the superiority of the proposed method.

### Strengths
1, The paper addresses the issue of spatial-temporal redundancy in videos for text-video retrieval and introduces an efficient method that achieves faster training times and inference.
2, Extensive experiments and analyses of TempMe demonstrate its efficiency, effectiveness, and generalization capabilities.
3, The ClipMe Block mainly involves two steps, "Intra-clip Merging" and "Cross-clip Merging", each employing distinct methods for token grouping. This design effectively aids in information merging across clips.

### Weaknesses
1, Although the paper addresses spatial-temporal redundancy in text-video retrieval, there is already substantial work on token merging and pruning in video processing. This overlap may affect the perceived uniqueness of the proposed approach.
2, A few symbols lack adequate definitions, which may hinder readability. For instance, "R_c" in Section 3.2, while defined in Figure 3 as the ratio of kept tokens, should also be described in the text when first introduced for clarity.

### Questions
The authors should clarify how this work distinguishes itself from existing methods for token pruning or merging.

### Soundness
3

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
5

### Summary
This work proposes TempMe, a temporal token merging method for T2V retrieval, designed to address two main issues: (1) high inference costs in current PEFT methods, and (2) the tendency of token merging methods to overlook temporal redundancy. TempMe introduces a PMG framework, which first merges tokens within individual images and then progressively merges across video clips. Experimental results demonstrate TEMP’s effectiveness, showing improvements in GFLOPS, training time, and retrieval performance.

### Strengths
1. **Efficient Training/Inference Acceleration**: TempMe achieves significant improvements in training efficiency by implementing image merging followed by progressive video clip merging. This approach leads to substantial reductions in GFLOPS and training time compared to previous methods.

2. **Comprehensive Ablation Studies**: Extensive ablation experiments validate the effectiveness of clip merging at different layers and intervals, as well as its applicability on stronger video-pretrained backbones like UMT and MetaCLIP. Qualitative results further show that TEMP effectively merges objects and backgrounds.

3. **Cross-Clip Merging**: TempMe introduces a relatively novel approach by incorporating cross-clip (inter-clip) merging, expanding beyond traditional intra-clip merging to capture cross-clip information, which enhances the learning of temporal relations across clips.

### Weaknesses
1. **Limited Improvement in R@1 for T2V Retrieval**: The R@1 improvement over previous methods is relatively small, especially given the advances in MLLM models. In 2023, T2V retrieval methods like HBI and Cap4video on CLIP-ViT-32/16, R@1 have reached around 48/50 (e.g., [1][2]). I suspect the limited improvement may stem from TempMe still focusing on video merging within the encoder, without further optimization after obtaining the clip-level representation. The reported R@1 of 46.1 is only a marginal improvement, and it is unclear if this gain justifies the added complexity of the proposed merging strategy. Furthermore, the comparison is made against PEFT methods, not full fine-tuning, which makes the comparison less compelling given the performance gap between these two approaches. 

2. **Lack of Memory Usage Comparison**: Efficiency is not solely about GFLOPS—memory usage for training and inference is also crucial. While TempMe provides training acceleration, memory optimization would be even more beneficial. In Table 5, the authors report memory usage for CLIP-ViT-16, but it would be helpful to see detailed comparisons for CLIP-ViT-32 as well, particularly relative to previous methods. The absence of a detailed memory analysis for CLIP-ViT-32, especially during inference, makes it difficult to assess the practical benefits of TempMe in resource-constrained environments. It is also unclear how the memory usage scales with increasing video length or batch size, which are critical factors in real-world applications.

3. **Limited Novelty**: The intra-clip merging process is highly similar to the original token merging approach [3], which limits the novelty of this method. In fact, the flowchart for intra-clip merging in Figure 3 closely resembles the diagram in Token Merging (ToMe), making it difficult to discern substantial differences. Essentially, the only distinct contribution is the cross-clip merging mechanism. The core idea of intra-clip merging appears to be a straightforward application of existing techniques, and the paper does not adequately highlight any novel modifications or adaptations to this process.

4. **Efficiency and Early Layer Merging**: Performing token merging in earlier layers of CLIP could theoretically reduce both GFLOPS and memory usage, though it might harm performance metrics like R@1. TempMe, however, only applies merging in the last three layers with a 12-6-3-1 merging pattern. A potential improvement could be to increase the input frames and match GFLOPS with previous PEFT methods, potentially enhancing R@1 without excessive memory usage. Additionally, it would be beneficial to provide memory usage details for CLIP-ViT-32 to understand whether further optimization is feasible. The choice of merging only in the last three layers seems arbitrary and lacks a clear justification. The paper does not explore the trade-offs between early and late merging in sufficient detail.

5. **Metric Suggestion**: Presenting an overall sum@R can be unclear for readers. R@1 is generally a more meaningful metric than sum@R and would offer a clearer understanding of the model's performance.

### Questions
If the memory usage of TempMe proves to be more efficient compared to previous PEFT or full finetuning methods, I would consider increasing my score.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the text-video retrieval task and specifically propose a parameter efficient method for this task. The proposed framework merges redundant tokens across adjacent video clips. The method has a good trade-off between inference and parameter efficiency and accuracy achieving state of the art results when compared to other parameter efficient methods.

### Strengths
The paper addresses an important task, namely text-video retrieval and proposes a parameter-efficient method for this. One strength of the paper is that the proposed method was extended to video foundation methods such as UMT and various backbones showcasing the extensibility of the method. Also, the method is based on a well-known fact, namely the video has a lot of redundant information from frame to frame and the method is built upon that observation and compresses the redundant information. Additionally the method achieves good results both in term of performance and inference efficiency.

### Weaknesses
 - Abstract: the abstract is hard to follow and is not clear if the method addressed inference speed-ups or training time speed-ups or both.
- overall the quality of the writing can be improved because it's not straightforward to follow the paper, for example in the introduction the transitions between paragraphs are abrupt.
- the choice of sampling 12 frames for MSRVTT and 64 frames for ActivityNet seems arbitrary.

### Questions
Is any part of the method that is specifically designed for text-video retrieval or could it be applied for other text-video tasks as well?
[1] shares a similar idea, can you please summarize the similarities and differences between the proposed method and [1]?


[1] Yao, Linli, et al. "DeCo: Decoupling Token Compression from Semantic Abstraction in Multimodal Large Language Models." arXiv preprint arXiv:2405.20985 (2024).

### Soundness
3

### Presentation
2

### Contribution
3
