# Matryoshka Multimodal Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
\vspace{-0.1in}
Large Multimodal Models (LMMs) such as LLaVA have shown strong performance in visual-linguistic reasoning.  These models first embed images into a fixed large number of visual tokens and then feed them into a Large Language Model (LLM). However, this design causes an excessive number of tokens for dense visual scenarios such as high-resolution images and videos, leading to great inefficiency. While token pruning and merging methods exist, they produce a single-length output for each image and cannot afford flexibility in trading off information density \textit{v.s.}~efficiency.  Inspired by the concept of Matryoshka Dolls, we propose \textit{\shortname{}: \fullname{}}, which learns to represent visual content as nested sets of visual tokens that capture information across multiple coarse-to-fine granularities. Our approach offers several unique benefits for LMMs: (1) One can explicitly control the visual granularity per test instance during inference, \textit{e.g.}, adjusting the number of tokens used to represent an image based on the anticipated complexity or simplicity of the content; (2) \shortname{} provides a framework for analyzing the granularity needed for existing datasets, where we find that COCO-style benchmarks only need around 9 visual tokens to obtain an accuracy similar to that of using all 576 tokens; (3)
Our approach provides a foundation to explore the best trade-off between performance and visual token length at the sample level, where our investigation reveals that a large gap exists between the oracle upper bound and current fixed-scale representations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes Matryoshka Multimodal Models (M^3), a MLLM framework supporting variable visual token length for flexible inference cost control. The multi-scale visual features are generated in a homogeneous manner by pooling visual encoder output with different kernel sizes, and the same set of weights are jointly trained on all scales, producing a single all-in-one model for easy deployment. Models are constructed in a continual finetuning setting on top of LLaVA and LLaVA-NeXT, and evaluated on a broad range of MLLM benchmarks with extensive ablation studies.

### Strengths
* The paper tackles a meaningful problem in practice. The motivation is coherent and easy-to-follow.

* The method description is mostly clear.

* Extensive experiments with strong results and insightful analysis.

### Weaknesses
* **Comparison with Flamingo-style (i.e., cross-attention-based) methods**: Despite the popularity of LLaVa-style MLLMs which treat visual tokens as prompt, Flamingo-style MLLMs, which decode text-conditioned salient visual features with cross-attention modules, are also studied as an alternative paradigm in several previous works, e.g., [1, 2]. It's noteworthy that cross-attention alleviates most of the the performance penalty due to long visual sequences by nature, because the visual tokens do not go through the expensive MLP and quadratic-complexity self-attention in the language model part (it may still be quadratic in the visual encoder part though). Even if extensive experiments are infeasible within the rebuttal period, it might still make the argument stronger and benefit future readers if at least some discussions could be included (e.g., related works, theoretical analysis of both methods, FLOPS comparison, what if they are used together). Specifically, the cross-attention mechanism in Flamingo-style models could potentially offer a more efficient way to handle variable-length visual sequences compared to the proposed method. A theoretical comparison of the computational complexity of both approaches, particularly in the context of varying visual token lengths, would be highly beneficial.

* **Training cost**: From the description at around Line 226, it seems that *all* scales of *all* images are used for training, which means the training cost could be a few times of single-scale training. A comparison with specific numbers and some discussions on scalability would be very helpful as training data of state-of-the-art MLLMs are approaching billion-scale. The paper should provide a detailed breakdown of the training cost for different scales and discuss how the cost scales with the number of scales used. Additionally, it would be valuable to explore potential strategies for mitigating the increased training cost, such as selective sampling of scales or using a curriculum learning approach.

* **Minor writing issues**: In Table 13, the unit of FLOPs should be in T instead of TB (TB=TeraBytes is for memory). Repeated reference item: Zhang et al 2023a / Zhang et al 2023b.

### Questions
* **Symbol clarification**: At Line 203, it's stated that $X_{S_i} \subset X_{S_{i + 1}}$. However, if we consider $X_{\cdot}$ as a set of $C$-dimensional features, then this seems self-contradictory because the average of a subset of elements $\frac{1}{n} \sum_j X_{S_{i + 1}, j}$ is not necessarily one of the original elements. Could the authors provide a more rigorous definition about symbols $X_{S_i}$ and, in turn, the definition of Matryoshka property studied in this case?

### Soundness
4

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
4

### Summary
This paper proposed a multimodal LLM M3 supporting varing number of visual tokens, inspired by the Matryoshka Dolls. By changing the nbumber of visual tokens, M3 can understand the visual content at different granularity. The proposed method is simple and easy to follow, which has been verified by the experiments.

### Strengths
- The motivation is clear. Current LMMs need more and more visual tokens to enhance their performance, the study of token reduction is important for efficient LMMs.
- The method is simple and easy to implement. Instead of tuning LLM for accepting varing number of tokens, M3 shows that tuning CLIP also works.
- The main evaluation and ablation analysis confirm M3's effectiveness.

### Weaknesses
- Comparisions with dynamic sampling methods like Token Merging and Chat-Univi [1]. The performance drop is significant when reducing the number of tokens, while dynamic sampling methods like Chat-Univi can even surpass its full token baseline. Besides, M3 can be regarded as a special case of dynamic sampling. I suggest a fair comparison with these methods.
- High-resolution and long video evaluation and comparisons with other works (LLaVA-HD, SPHINX, LLaMA-VID etc.) . Since these tasks usually requires more tokens, M3 may lead to a better trade-off between performance and computation.
- Suggest to add speed and computation cost comparisions on the main paper, instead of the appendix.

[1] Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding

### Questions
- How to extend M3 to any number of tokens. Currently, it can only support a set of token numbers (576->144->xxx). If we can enlarge the set, then switching between them will be smoother.

### Soundness
3

### Presentation
3

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
This paper addresses the problem of visual representation in large multimodal models (LMMs) with a method called Matryoshka Multimodal Models (M3). M3 sequentially applies average pooling to the initial visual tokens extracted by the CLIP-ViT to obtain visual representations at different granularity levels. During training, the LMM learns to autoregressively generate the next tokens based on visual representations at each granularity level individually. In inference, the level of visual granularity can be adjusted to balance performance and efficiency. Experimental results indicate that, on a number of benchmarks, M3 achieves performance on par with LLaVA-1.5 and LLaVA-Next, while requiring significantly fewer visual tokens. Additionally, M3 provides a tool for analyzing the visual complexity of vision-language benchmarks by assessing the granularity required to arrive at correct answers. The results reveal that dense visual perception benchmarks, such as TextVQA and DocVQA, indeed require a higher number of visual tokens compared to other benchmarks.

### Strengths
- This paper is well-motivated, addressing the important capability of representing visual information at varying levels of granularity. This flexibility enables adjusting the number of visual tokens based on both computational budget and task complexity.
- The proposed method is effective, demonstrating comparable performance with the baseline LMMs (LLaVA-1.5 and LLaVA-Next) while using significantly fewer visual tokens, across benchmarks that do not demand dense visual perception.
- The empirical study offers several valuable insights:
  - A substantial gap exists between the naive use of all visual tokens and the upper-bound performance achieved by selecting the optimal number of tokens for each test instance.
  - Different vision-language tasks indeed require varying numbers of visual tokens to be addressed.
  - Reducing the number of visual tokens does not increase the level of hallucination for M3. 
  - The ablation study compressively compares different token reduction methods and suggests the advantage of average pooling.

### Weaknesses
- Although M3 can produce visual representations at multiple granularity levels, the number of visual tokens used at inference must be predefined. In other words, the method cannot adaptively adjust the number of visual tokens for different instances.
- The baseline methods used for video understanding are relatively weak. For example, recent 7B-scale VLMs have achieved over 60% accuracy on EgoSchema, while the best baseline in this work only reaches 35.8%. M3 would likely benefit from integration with more advanced video LMMs. It would also be better to explore alternative video encoding methods other than "arranging video frames into a collage".
- The method for obtaining Oracle performance is not clearly explained. In line 323, the authors state, "for each test instance, we select the scale with the fewest tokens that can answer the question correctly." However, it is unclear what happens if the model cannot produce the correct answer at any scale.
- The capability of the LMMs is not taken into account when using M3 as a tool to analyze the visual complexity of vision-language tasks. If the LMMs cannot effectively consume additional visual information, increasing the number of visual tokens may negatively impact performance, even if the task itself requires more visual information.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the VLLM domain and proposes to use average pooling to downsample the visual tokens to a hierarchy of scales for efficient computation.

### Strengths
1. Presentation is clear and concise
2. The method is simple but effective
3. Experiments are well-designed and can support the value of the proposed method
4. The large number of visual tokens in multi-modal LLMs is a significant and urgent problem

### Weaknesses
1. Whereas the paper claims that the method can ''**adaptively** and efficiently represent visual content", I think the word **adaptively** is kind of misleading here as it makes readers feel that the method per se includes some dynamic inference strategy. I can understand that the authors hope to express that the users can tradeoff computation for accuracy, but it is important to make it more clear.


(**This is actually a weakness of mine instead of the paper**) I am not able to precisely evaluate the novelty of the paper because the VLLM domain is altering from day to day and I have not been closely tracing the frontier papers in the token reduction topic, and I hope other reviews can give better novelty judgments.

### Questions
None

### Soundness
3

### Presentation
4

### Contribution
3
