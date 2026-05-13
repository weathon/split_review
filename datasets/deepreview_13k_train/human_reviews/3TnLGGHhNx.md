# From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities

- Decision: Accept
- Scores: 5, 5, 8

## Abstract
Multimodal Large Language Models have made significant strides in integrating visual and textual information, yet they often struggle with effectively aligning these modalities. We introduce a novel image tokenizer that bridges this gap by applying the principle of Byte-Pair Encoding (BPE) to visual data. Unlike conventional approaches that rely on separate visual encoders, our method directly incorporates structural prior information into image tokens, mirroring the successful tokenization strategies used in text-only Large Language Models. This innovative approach enables Transformer models to more effectively learn and reason across modalities. Through theoretical analysis and extensive experiments, we demonstrate that our BPE Image Tokenizer significantly enhances MLLMs' multimodal understanding capabilities, even with limited training data. Our method not only improves performance across various benchmarks but also shows promising scalability, potentially paving the way for more efficient and capable multimodal foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper tried to use BPE for image tokenization. From the results shown to us, there is some improvement.

### Strengths
1. From the results shown to us, there is some improvement.
2. Experiment settings are clear

### Weaknesses
1. Performance is poor compared to any CLIP style or even DINO style MLLM as the visual encoder.
2. There is no projector in the experiments. This could be an extreme unfair setting compared to classical pipeline.
3. I do not think proofs are helpful to understand what is going on in the experiments.

### Questions
1. Why is there a 0.99 in L770 and L253? Is this made up?
2. For Figure 2 (b) (c), all settings converge after ~150 iterations. I don't think they make any difference.
3. Why vocabulary changes from 8k-> 16k, there is a performance drop? I can not find any evidence in the proof that can demonstrate this point.
4. The proposed BPE is very similar to super pixel or clustering algorithm. Authors should discuss the difference and compare the performance. 
5. In table 5.1, authors can add another classical setting: During SFT, visual encoder is frozen.

### Soundness
2

### Presentation
2

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
This paper proposes to apply Byte-Pair Encoding to visual data, which first encode image into discrete token IDs, and then train the BPE image tokenize to get image tokens with semantic prior (e.g., previously image tokens for 'a white cat' is separated in the sequence of image tokens, after BPE, one token is representing 'a white cat'). The experiments are mainly based on applying BPE image tokenizer training to LLaMA-3.1 and compare on VQAv2, MMBench, etc.

### Strengths
1. This BPE image tokenization approach is novel and that potentially help the transformer better understand alignment between text and image with a semantic image token.
2. There is a theoretical analysis on how BPE tokenize benefits transformers learning in Section 3.
3. The scaling of BPE is reflected in that the model improves when adding larger scale of data such as ShareGPT4, etc.

### Weaknesses
1. The experimental evidences are kind of weak. First, it's far behind current MLLMs SOTA on public benchmarks. For example, the best presented number of proposed model is LLM+VQ+BPE with Additional scaling (SFT) , which achieves 60.6 on VQAv2, 44.0 on MMBench, and 48.2 on VizWiz, which is far behind similar size 7B LLaMA-based MLLMs.
2. Second, the ablation is not sufficient to show the benefit of BPE image tokenizer. Only one Table results compare LLM+VQ and LLM+VQ+BPE. The details of these two models are not illustrated, e.g., what is exactly implemented for LLM+VQ.

### Questions
1. The LLM+VQ+BPE is also supervised finetuned on LLaVA-One-Vision, etc data, however, is far behind LLaVA-OneVision and other models that trained on these data. Then what's the benefit of this VQ+BPE compared with previous MLLM practices?
2. Is this VQ+BPE applied to other LLM beyond LLaMA-3.1-8B and get similar observations?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel BPE image tokenizer that brings byte-pair encoding (BPE) to image tokenization, enhancing multimodal large language models (MLLMs) in aligning visual and textual information. By embedding structural priors into image tokens, the method shows promise in cross-modal tasks and scalability, offering a new approach to unified visual and text processing.

### Strengths
1.This paper creatively adapts byte-pair encoding (BPE) for images, aiming to make visual data work more seamlessly with text in multimodal models.

2.The approach integrates structural information directly into image tokens, which could help models better understand and align visuals with text, showing solid potential in cross-modal tasks.

### Weaknesses
1.Theoretical framework has several notable limitations:
  1.1Lack of Multimodal Fusion Analysis: The paper’s theoretical analysis is focused on 2D image data alone and does not delve into how the BPE tokenizer facilitates the fusion of visual and textual information. Multimodal tasks typically require deep semantic and structural alignment across modalities, which is not sufficiently addressed in this analysis. This omission limits the theoretical support for the tokenizer’s efficacy in a multimodal model context. Specifically, the analysis does not address how the tokenization process impacts cross-modal attention mechanisms or the alignment of latent spaces between visual and textual representations. A more rigorous theoretical treatment should consider how the BPE tokenization affects the joint probability distribution of visual and textual data, and how this impacts downstream multimodal tasks.
  1.2Absence of Analysis on Information Loss in Tokenization: The paper lacks a theoretical exploration of the potential information loss from BPE tokenization, such as the simplification of high-frequency visual details. There is no quantification of how the loss of these details might impact overall model performance. This gap in the analysis leaves the question of how well the BPE tokenizer preserves image details unanswered. The analysis should include a formal treatment of the distortion introduced by the BPE process, potentially using information-theoretic measures to quantify the loss of information. Furthermore, it should explore how the choice of BPE vocabulary size and merging criteria affects the trade-off between compression and information preservation.

2.A notable limitation of this paper is its focus on evaluating the BPE image tokenizer primarily through VQA-like tasks, which generally require only broad semantic alignment across modalities. While effective for assessing general multimodal comprehension, these tasks may not fully capture the demands of applications like image segmentation or image caption, where finer-grained visual detail and spatial relationships are crucial. Without evaluation on these more intricate tasks, it remains unclear how well the method handles scenarios that require detailed visual representation, potentially limiting its applicability to real-world multimodal use cases that demand high visual fidelity. The evaluation should include tasks that require precise spatial understanding, such as object detection or instance segmentation, to fully assess the tokenizer's ability to preserve and utilize fine-grained visual information. Additionally, the paper should explore how the BPE tokenizer performs on tasks that require generating detailed visual descriptions, such as image captioning with complex scene descriptions.

### Questions
1.Applicability of the Theoretical Model: How does a simplified 2D Markov process adequately capture the complex structure of real-world image data?

2.Sensitivity to Information Loss: How is the potential impact of information loss in tokenization, especially for detail-sensitive tasks, theoretically assessed?

3.Task Representativeness and Generalization: How can results on VQA-like tasks ensure performance on precision-demanding tasks like image caption?

### Soundness
3

### Presentation
3

### Contribution
2
