# LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
The advent of real-time large multimodal models (LMMs) like GPT-4o has sparked considerable interest in efficient LMMs. LMM frameworks typically encode visual inputs into vision tokens (continuous representations) and integrate them and textual instructions into the context of large language models (LLMs), where large-scale parameters and numerous context tokens (predominantly vision tokens) result in substantial computational overhead. Previous efforts towards efficient LMMs always focus on replacing the LLM backbone with smaller models, while neglecting the crucial issue of token quantity. In this paper, we introduce LLaVA-Mini, an efficient LMM with minimal vision tokens. To achieve a high compression ratio of vision tokens while preserving visual information, we first analyze how LMMs understand vision tokens and find that most vision tokens only play a crucial role in the early layers, where they fuse visual information into text tokens. Building on this finding, LLaVA-Mini introduces modality pre-fusion to fuse visual information into text tokens in advance, thereby facilitating the extreme compression of vision tokens fed to LLM backbone into one token. LLaVAMini can support the understanding of images, high-resolution images, and videos in an efficient manner. Experiments across 11 image-based and 7 video-based benchmarks demonstrate that LLaVA-Mini outperforms LLaVA-v1.5 with just 1 vision token instead of 576. Efficiency analyses reveal that LLaVA-Mini can reduce FLOPs by 77%, deliver low-latency responses within 40 milliseconds, and process over 10,000 frames of video on GPU hardware with 24GB of memory.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
LLaVA-Mini proposes a compute and memory efficient Multi-modal by compressing the vision tokens that is passed to the LLM. The work achieves this by introducing a technique of modality pre-fusion where visual representation is fused into the text tokens and compression of vision tokens using cross-attention with learnable compression queries. LLaVA-Mini achieves comparable performance to existing models like LLaVA-v1.5 across several benchmarks, while significantly improving efficiency in terms of FLOPs, latency, and memory usage.

### Strengths
- The finding that vision tokens are primarily crucial in early layers is key to the design of the efficient early fusion architecture, a significant contribution to reducing computational overhead in LLMs.
- Overall, the paper is well written and easy to follow. The methods, concepts are well explained and tables/ figures convey key findings. The qualitative visualization examples such as the cross-attention in compression module helps provide intuition. 
-   LLaVA-Mini achieves significant performance, reducing FLOPs by 77% and VRAM usage by more than 99% per image compared to LLaVA-v1.5, without compromising much in terms of model accuracy. This efficiency could make LLaVA-Mini highly suitable for edge devices, making it as a practical solution for real-time multimodal interactions.
- The authors provide exhaustive ablations experiments on number of pre-fusion layers/ vision tokens etc.

### Weaknesses
 - The paper does not explain the complexity of plugging this compression method to existing multi-modal pipelines. The lack of open source implementation of the code might hinder reproducibility.
- While the paper highlights successful qualitative examples, it would be valuable if it could also discuss any failure cases encountered with the compression technique, along with potential solutions for addressing them.
- It would be great to understand how model efficiency scales across different hardware platforms.

### Questions
- Have the authors done any ablation on using SOTA token pooling methods for the vision token pooling and compare against them (other than average pooling).
- Can the authors highlight results on more vision centric benchmarks and show the impact of different number of vision tokens on these e.g., CV-Bench [1]





[1] Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents LLaVA-Mini, an efficient large multimodal model that significantly reduces computational overhead while maintaining competitive performance. The key innovation lies in its ability to represent visual information with as few as one vision token, achieved through two main components: a modality pre-fusion module and a vision token compression module. The authors first conduct a layer-wise analysis of how LLMs process vision tokens, revealing that vision tokens are most crucial in early layers. Based on this insight, they design the pre-fusion module to process visual information before it enters the LLM, and employ a compression mechanism to minimize the number of vision tokens. Experimental results across 11 image and 7 video benchmarks demonstrate that LLaVA-Mini achieves comparable performance to LLaVA-v1.5 while reducing vision tokens from 576 to 1, resulting in 77% FLOPs reduction and significant memory savings (from 360MB to 0.6MB per image). This enables processing of long videos exceeding 10,000 frames and reduces inference latency from 100ms to 40ms.

### Strengths
1. Quality:
- Comprehensive empirical validation across 18 benchmarks (11 image-based and 7 video-based) demonstrates the robustness of the approach.
- The method achieves significant efficiency improvements (77% FLOPs reduction, 600x memory reduction) while maintaining competitive performance with the baseline.

2. Clarity:
- The motivation and problem formulation are well-articulated, clearly identifying the computational challenges in current LMMs.
- The paper presents a logical progression from empirical observations to proposed solutions.

3. Significance:
- The dramatic reduction in computational resources makes multimodal processing more accessible.
- The approach addresses a critical limitation in current LMMs, potentially enabling real-time applications and processing of high-resolution inputs.

### Weaknesses
1. Writing:
- The attention weight analysis lacks crucial technical details. The authors do not specify how they handle multiple attention heads (whether through averaging, individual analysis, or selective visualization), making the results difficult to reproduce. Specifically, it is unclear if the attention weights are averaged across all heads, or if a specific head is chosen for analysis. Furthermore, the paper does not clarify how the attention scores are aggregated across the multiple vision tokens, instruction tokens, and response tokens. The paper fails to clarify how attention scores are averaged among instruction, vision, and response tokens, which is essential for understanding the analysis methodology. For example, are the attention weights from each response token to all vision tokens summed, and then averaged across all response tokens? This lack of clarity makes it difficult to verify the claims made based on the attention analysis. Despite using LLaVA 1.5 and LLaVA NeXT as base models, which both incorporate high and low-resolution vision inputs, the analysis does not differentiate between these different types of vision tokens. It is not clear if the analysis treats all vision tokens equally or if there is a distinction made based on their resolution or origin.

2. Technical Inconsistencies:
- There's a discrepancy between the visualization results and claims: while the authors argue that attention to vision tokens decreases in latter layers, the entropy visualization shows persistently high values for vision tokens in these layers, creating confusion about the actual attention distribution. The paper does not adequately explain why the entropy of attention to vision tokens remains high in later layers, despite the claim that the attention weights themselves decrease. This discrepancy needs to be addressed with a more thorough explanation of the relationship between attention weights and entropy. The visualization in Figure 4, which uses a logarithmic scale, could be misleading without proper explanation in the main text.
- The paper lacks sufficient details about the pre-fusion transformer architecture and implementation, which is crucial for reproduction and understanding the method's effectiveness. The paper does not specify the number of layers, hidden dimensions, or other key hyperparameters of the pre-fusion transformer. Without these details, it is difficult to assess the computational overhead of this module and to reproduce the results.

3. Architectural Design and Claims:
- The paper's title and main claim about "one vision token" is potentially misleading. The implementation still requires processing full projected vision tokens in the pre-fusion transformer, suggesting that the computational efficiency gains are not solely from token reduction. The paper needs to clarify that the reduction to one token occurs only at the input to the LLM, and that the pre-fusion module still processes all the projected vision tokens. This distinction is crucial for accurately understanding the method's efficiency gains. The ablation studies (lines 446-457) emphasize the importance of the pre-fusion module, raising questions about the actual contribution of the token compressor. The paper should explore the effectiveness of using only the pre-fusion module without compression. It is not clear if the token compression module provides any significant benefit beyond what is achieved by the pre-fusion module alone.

4. Computational Analysis:
- The paper lacks a detailed analysis of the computational overhead introduced by the fusion module, particularly regarding the processing of N^2×5 vision tokens plus l_q text tokens. The paper should provide a breakdown of the FLOPs and memory usage of the pre-fusion module, especially considering the processing of all projected vision tokens. This analysis is necessary to fully understand the efficiency gains of the proposed method. The training costs during the instruction tuning stage, including memory and FLOPs comparisons with LLaVA, are not adequately addressed, making it difficult to assess the true efficiency gains during training. The paper should include a comparison of the training costs of LLaVA-Mini with the original LLaVA model, including memory usage and FLOPs, to provide a comprehensive view of the efficiency gains.

5. Logic:
- The presentation of "Modality Pre-fusion" and "Vision Token Compression" would benefit from a chronological reorganization to better reflect the processing pipeline (image encoder -> vision token compression -> modality pre-fusion). The current organization does not clearly reflect the actual flow of information in the model, which could lead to confusion. Presenting the modules in the order they are used in the pipeline would improve clarity.

### Questions
See "Weakness". 

Additional question:

1. Entropy Visualization Clarification:
- Could the authors explain the apparent contradiction between the claim of decreased attention to vision tokens in the latter layers and the high entropy values shown in the visualization?
- What causes high entropy in vision-related attention weights in the latter layers despite lower attention weights?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
a. The paper proposes LLaVA-Mini, an MLLM with improved efficiency via token compression. Specifically, the authors first unveil that early layers of MLLM are important for visual understanding. On top of this finding,  the efficient MLLM is then designed with 2 strategies: 1) compressing input visual tokens using the query-based resampler and 2) fusing visual tokens with text instruction tokens in early layers of LLM.The paper is well written, and delivered with clear motivation and simple yet effective methods.

b. The authors conducted comprehensive experiments to demonstrate the effectiveness of the methods. On the other hand, LLava-mini manages to achieve competitive performance with much-reduced tokens.

### Strengths
A. The paper is well written, and delivered with clear motivation and simple yet effective methods.

B. The authors conducted comprehensive experiments to demonstrate the effectiveness of the methods. On the other hand, LLava-mini manages to achieve competitive performance with much-reduced tokens.

### Weaknesses
A. Since the token numbers are substantially reduced. LLaVA-mini may achieve inferior performance under scenarios demanding fine-grained visual details, e.g., text-oriented benchmarks including Text VAQ, especially when compared with models with longer visual sequence input （e.g., LLaVA-Next)

B. The paper lacks an important baseline, namely, keeping the visual tokens in early layers of LLMs and then compressing the visual token output on the L-th (4 in the paper) layer.

### Questions
The authors claim that for video inputs, they train and infer via sampling frames at 1fps. In other words, the number of compressed visual tokens for videos of different lengths varies. I’d like to know if there’s any strategy (e.g, temporal embedding) to solve the discrepancy between training and inference (i.e., much longer videos).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes an efficient LMM with minimal vision tokens. 1/ To achieve a high compression ratio of vision tokens while preserving visual information, the authors first analyze how LMMs understand vision tokens and find that most vision tokens only play a crucial role in the early layers, where they fuse visual information into text tokens. 2/ LLaVA-Mini introduces a novel modality pre-fusion to fuse visual information into text tokens in advance before feeding into LLM and a compression module to reduce #vision tokens into minimal ones. 3/ Experiments across 11 image-based and 7 video-based benchmarks demonstrate that LLaVA-Mini outperforms LLaVA-v1.5 with just 1 vision token instead of 576. Efficiency analyses reveal that LLaVA-Mini can reduce FLOPs by 77%, deliver low-latency responses within 40 milliseconds, and process over 10,000 frames of video on GPU hardware with 24GB of memory.

### Strengths
1/ The problem of how to improve efficiency of MLLM is important. 

2/ The authors conducted a very interesting and detailed analysis of how LMMs understand vision tokens and find that most vision tokens only play a crucial role in the early layers, where they fuse visual information into text tokens. 

3/ LLaVA-Mini introduces a modality pre-fusion module to fuse visual information into text tokens in advance before feeding into LLM and a compression module to reduce #vision tokens into minimal ones. 

4/ Experimental results are strong and convincing.

### Weaknesses
1/ According to Sec 3, if I understand correctly, for each downstream task, this paper trains a new, independent compression and modality pre-fusion modules. In other words, for another task, we need to train another model. I wonder, how does this approach differ from task-specific distillation? It seems the reason why the efficiency can be improved significantly is because of removing unnecessary tokens for the target downstream task. Instead, would it be possible to train generic compression and modality pre-fusion modules in stage 1 that can be generalised to various downstream tasks?

2/ For the proposed approach, a new modality pre-fusion module has been introduced. I wonder if this is necessary. Instead, can we re-use the first few layers, which have high activation for vision tokens, as the fusion module. To further include the compression module, in the first few layers of LLM, the part digesting vision tokens can have two pathways, one pathway is to output the compressed tokens while the other pathway is to be gradually fused together with the text tokens.  

3/ When it comes to video, there are some recent streaming video LLM works such as "VideoLLM-online: Online Video Large Language Model for Streaming Video. CVPR 2024" which also advocates the idea of representing each frame with minimal vision tokens to improve efficiency. It might be worthwhile to compare or just discuss.

### Questions
Kindly refer to the weakness sec above

### Soundness
3

### Presentation
4

### Contribution
4
