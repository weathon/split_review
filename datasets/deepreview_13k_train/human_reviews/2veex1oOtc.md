# MQuant: Unleashing the Inference Potential of Multimodal Large Language Models via Full Static Quantization

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Recently, multimodal large language models (MLLMs) have garnered widespread attention due to their ability to perceive and understand multimodal signals. However, their large parameter sizes and substantial computational demands severely hinder their practical deployment and application. While quantization is an effective way to reduce model size and inference latency, its application to MLLMs remains underexplored. In this paper, we conduct an in-depth analysis of MLLMs quantization and identify several challenges: slow inference speed of the visual tokens, distributional differences across modalities, and visual outlier clipping degrades performance.
To address these challenges, we propose **MQuant**, a quantization framework tailored for MLLMs. Specifically, 1) we design Modality-specific Quantization (MSQ) and Attention-Invariant Flexible Switching (AIFS) to support per-tensor static quantization and facilitate efficient inference. 2) we introduce a unified LayerNorm-to-RMSNorm transformation, achieving seamless integration of the MLLM vision encoder with Hadamard rotation. 3) we propose Rotation Magnitude Suppression (RMS) to mitigate outliers introduced by Hadamard rotation. Experiments conducted on five mainstream MLLMs demonstrate the superior performance and broad applicability of MQuant. For example, it maintains around 98\% of the floating-point accuracy under the W4A8 setting. To the best of our knowledge, **MQuant** is the first quantization solution for MLLMs, paving the way for future advancements in their application.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the quantization problem in Multi-modal LLMs. Specifically, the authors investigate three aspects that lead to performance degradation when applying the straightforward per-tensor static quantization for prefilling multimodal tokens. To address these challenges, this paper presents MQuant with Modality-specific Quantization (MSQ), Attention-Invariant Flexible Switching (AIFS), LayerNorm-to-RMSNorm transformation and Rotation Magnitude Suppression (RMS).

### Strengths
1. This paper focuses on a valuable question, i.e. quantization in MLLMs.
2. Well presented with figures and tables.
3. Overall performance is superior to some LLM quantization baselines.

### Weaknesses
1. MSQ and AIFS are simply trivial adaptions of per-token dynamic quantization to MLLMs. It's better that this serves as a baseline model.
2. MSQ and MSQ + AIFS exhibit marginal improvement over the per-tensor static baseline in Table 4.
3. Please discuss the overhead of MSQ, otherwise why don't we use token-specific quantization?
4. Although MSQ + AIFS is proposed to address the token increase brought by larger resolution of images, the speedup fails to exhibit great advantages over per-token dynamic baseline with resolution scaling.
5. SliceGPT [1] has already proposed converting LayerNorm to RMSNorm and provides a solution, which you do not mention in the related work. Please discuss the difference between your method in Section 4.2 and the one in SliceGPT.
6. Lack of sufficient technical contribution. Most of the techniques used are from previous work and adapt to MLLM with trivial modifications.
7. Typos. e.g. whthin in line 304 and grammatic errors, e.g. 305 (should be "to show how to transform xxx")

### Questions
Please see the weakness.

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
3

### Summary
This paper introduces several techniques to enhance the accuracy and reduce the inference latency of Multimodal Large Language Models (MLLMs), which are affected by the additional vision encoder/adaptor. Empirical results demonstrate that the quantized model obtained using the proposed method outperforms other quantization methods in terms of accuracy and inference speed under certain settings.

### Strengths
1. The paper is well-written and easy to follow.
2. The modality-specific quantization and Layernorm-to-RMSNorm transformation are well-motivated by the distributional differences of various modality modules and architectural designs.
3. Comprehensive experimental results are provided on various MLLMs, with comparisons to several popular recent LLM quantization methods.

### Weaknesses
1. Attention-Invariant Flexible Switching (AIFS) Scheme: The authors claim that the proposed AIFS scheme is computationally equivalent to the original attention computation. However, it is unclear whether the corresponding positional embeddings are adjusted accordingly. If not, the equivalence may not be ensured. Specifically, the positional embeddings are typically added to the input embeddings *before* the attention calculation, and if the token order is changed by AIFS, the positional embeddings must also be re-ordered to maintain the correct positional information. Without this adjustment, the attention mechanism would be operating on incorrect positional information, potentially leading to significant deviations from the original computation.

2. Experiment Settings: There are concerns regarding the experimental settings. In Section 5.1, the authors conducted experiments under the "text-image-text" setting with 15 textual tokens. However, inference settings can be more complex:
- In a batch, the number of textual tokens varies, resulting in different attention masks after AIFS. It is not clear how the AIFS scheme handles variable-length text sequences within a batch, especially considering that the attention masks need to be adjusted accordingly. The paper needs to clarify how the padding and masking are handled in the AIFS scheme to ensure correctness when dealing with variable-length sequences in a batch.
- There can be interleaved image-text inference with more image-text turns. The current experiments do not explore the performance of the proposed method in more complex interleaved image-text scenarios with multiple turns, which are common in real-world applications. The paper needs to provide more experimental results on such scenarios to demonstrate the robustness of the proposed method.
- There can also be multi-image inference with single or multiple turns. The paper does not provide sufficient evidence to show how the proposed method performs in multi-image inference scenarios. It is important to evaluate the method in such scenarios to demonstrate its applicability in practical settings. More clarifications under these cases are required to further show the efficacy of the proposed method.

### Questions
1. For the proposed AIFS scheme, are the positional embeddings adjusted accordingly as the attention mask changes?
2. What batch sizes were used when evaluating the inference latency?

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
This paper proposes a quantization method which is specifically tailored towards MLLM. Because of the distributional differences between visual tokens and text tokens, the authors intuitively calculate separate quantization scales for two modalities and calibrate the attention mask accordingly. Further, they adapt some techniques from the LLM quantization literature to visual encoders in MLLM. By combining these two, MQuant maintains lower performance degradation under challenging quantization settings on multiple state-of-the-art retrained MLLM models.

### Strengths
1. The paper follows an intuitive approach to study MLLM quantization. The authors identify the issues based on some observations in the experiments and resolve the problem in a step-by-step manner.
2. The efficacy of the method is supported by extensive experiments.  The paper shows the quantization performance of 5 mainstream MLLM models on various multi-modal tasks. The ablation studies demonstrate the usefulness of different components in maintaining the performance near the float-point baseline.

### Weaknesses
1. The delivery of the paper needs significant improvement. The text is highly redundant. 
- Introduction: The content of the second last paragraph mostly overlap the main contribution part. It could be beneficial if these two parts are reorganized or condensed.
- Methodology: In 4.1, there are abundant words to explain the reason why we need MSQ and AIFS and the benefits brought by these two. To me, these are intuitive and simple operations which only need concise words for explanation. For 4.2 and 4.3, which are the techniques adapted from LLM quantization, it would be better if the authors could emphasize their novel improvements or adaptations rather than putting too many words to explain other people's contributions. 
- Although using separate figures for different components are informative, it could be easier for the readers to follow without reading the algorithm 1 in Appendix first if the authors could add a figure to show the overall quantization pipeline with the novel parts highlighted. 
- For some abbreviations used in the paper, like GEDD and W4A8, it would be friendly to readers not in the area if adding the explanations in the first place.

2. The paper does not demonstrate enough novelty.  First, both LayerNorm-to-RMSNorm transformation and Hadamard rotation are borrowed from LLM quantization literature (Ashkboos et al., 2024a, b). Second, although adopting a simple Divide-and-Conquer strategy like paper does to cope with the distribution outliers or differences may be sufficient, it is worth thinking about other systematic alternatives after getting more insights from the observations in the experiments. For now, the paper is more like a technical report. The paper should be concise and highlight the actual novel contributions.

3. Experiments: It would be better to see the latency comparisons among the proposed quantization methods could be added in Table 5. 

4. Minor Errors:

- The font size of the legend in Figure 1 (left side) is too small to read.
- Line 85-87: the meaning of the sentence Is not clear. Two "slightly" exist.
- For Table 3/4. the arrow directions showing the relative difference are counter-intuitive. Showing the decrease of latency with down arrows and adding "lower is better" could be an alternative.
- In Table 5, should that be "MSQ" rather than "MDQ"?

### Questions
1. In Eq (6), should the denominator of equation $s$ be $2^b-1$? since for b-bit, the value range would be (0,  $2^b-1$).
2. In line 321, "easier to quantize". What does easy mean in this context?
3. In line 287, what do the "outliers" mean? Extremely low or high values?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes MQuant, an accurate and efficient post-training quantization solution for multimodal large language models (MLLMs). MQuant reduces the time to first token (TTFT) with per-tensor static quantization and introduces modalityspecific quantization (MSQ) to handle distribution discrepancies between visual and textual tokens. Experiments on five mainstream MLLMs demonstrate that MQuant attains state-of-the-art PTQ performance.

### Strengths
Strength：

1. Extensive experiments demonstrate the approach's effectiveness in the PTQ of MLLMs.
2. The motivation is clear and quantization for MLLM is an important topic.
3. This paper is well-organized and clearly-written.

### Weaknesses
Weakness:

1. My only concern is that i'm not familiar with quantization. So i will adjust my rating depending on the other reviewers' opinions.

### Questions
Please see the comments above.

### Soundness
3

### Presentation
3

### Contribution
3
