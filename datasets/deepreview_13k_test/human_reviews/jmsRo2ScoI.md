# Rethinking Homogeneity of Vision and Text Tokens in Large Vision-and-Language Models

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Large vision-and-language models (LVLMs) typically treat visual and textual embeddings as homogeneous inputs to a large language model (LLM). However, these inputs are inherently different: visual inputs are multi-dimensional and contextually rich, often pre-encoded by models like CLIP, while textual inputs lack this structure. In this paper, we propose Decomposed Attention (D-Attn), a novel method that processes visual and textual embeddings differently by decomposing the 1-D causal self-attention in LVLMs. After the attention decomposition, D-Attn diagonalizes visual-to-visual self-attention, reducing computation from $\mathcal{O}(|V|^2)$ to $\mathcal{O}(|V|)$ for $|V|$ visual embeddings without compromising performance. Moreover, D-Attn debiases positional encodings in textual-to-visual cross-attention, further enhancing visual understanding. Finally, we introduce an $\alpha$-weighting strategy to merge visual and textual information, maximally preserving the pre-trained LLM’s capabilities with minimal modifications. Extensive experiments and rigorous analyses validate the effectiveness of D-Attn, demonstrating significant improvements on multiple image benchmarks while significantly reducing computational costs. Code, data, and models will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Decomposed Attention (D-Attn), a novel framework for processing visual and textual embeddings differently within Large Vision-Language Models (LVLMs). The key insight is that visual and textual inputs are inherently different and should be treated accordingly. The paper proposes three main technical contributions: (1) diagonalization of visual-to-visual self-attention to reduce computational complexity from O(|V|²) to O(|V|), (2) debiasing of positional encodings in text-to-visual cross-attention, and (3) an α-weighting strategy for merging visual and textual information. The authors demonstrate improved performance across multiple benchmarks while significantly reducing computational costs.

### Strengths
1. **Novel Insight and Problem Formulation**
   - Clearly identifies and addresses a fundamental assumption in current LVLMs about homogeneous processing of visual and textual tokens
   - Provides compelling arguments for why visual and textual embeddings should be treated differently

2. **Technical Innovation**
   - Introduces an elegant solution for reducing computational complexity through diagonal V2V attention
   - Proposes a mathematically sound α-weighting strategy that maintains model capabilities
   - Successfully addresses positional encoding bias issues

3. **Empirical Validation**
   - Comprehensive experimental evaluation across multiple benchmarks
   - Thorough ablation studies demonstrating the contribution of each component
   - Significant computational efficiency gains while maintaining or improving performance

4. **Reproducibility**
   - Clear implementation details and hyperparameters provided
   - Uses publicly available datasets and models
   - Code and models promised to be released

### Weaknesses
1. **Limited Directional Flexibility**
   - The current formulation assumes a fixed direction of information flow (text as query, vision as key/value)
   - Does not adequately address scenarios where vision needs to query text or other vision tokens
   - May limit the model's capability in vision-centric tasks (e.g., visual search, face matching)

2. **Theoretical Foundations**
   - The justification for diagonal V2V attention could be strengthened with more theoretical analysis
   - Limited discussion on the potential information loss from diagonal approximation
   - The α-weighting derivation could benefit from more detailed mathematical exposition

3. **Input Order Dependency**
   - Current architecture may not handle cases where text follows vision in the input sequence
   - Lacks explicit discussion on maintaining causality while allowing flexible token ordering
   - Need for more experimental validation with varied input orderings

### Questions
1. How would the proposed D-Attn framework handle cases where visual tokens need to attend to text tokens (V2T attention)? Could the framework be extended to support bi-directional cross-modal attention while maintaining its computational efficiency?

2. The paper assumes text tokens as queries and visual tokens as keys/values. How would this affect tasks where visual information needs to act as queries (e.g., visual search, image matching)? Could you elaborate on potential extensions to support such scenarios?

3. In cases where text tokens appear before visual tokens in the input sequence, how does the current architecture maintain causal attention while allowing meaningful cross-modal interactions? Could you provide experimental results for such cases?

4. Have you considered a more general framework where the roles of query/key/value are dynamically assigned based on the task or context? What would be the computational implications of such an approach?

5. Could you provide more theoretical justification for the diagonal approximation in V2V attention? Specifically, what types of visual relationships might be lost, and in what scenarios might this approximation be suboptimal?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose Decomposed Attention, a novel approach that treats visual and textual information differently within Large Vision Language Models (LVLMs). By eliminating attention between different tokens related to visual data, they enhance efficiency, demonstrating significant performance improvements across various multimodal tasks.

### Strengths
1) The authors clearly articulate the rationale behind their design choices. They explain the motivation for introducing diagonal attention and the different positional embedding methods for visual and textual embeddings. This depth of reasoning strengthens the justification for their approach.

2) The proposed method is highly effective in terms of efficiency, which the authors substantiate both conceptually and empirically. They discuss the reduction in computational complexity achieved through the use of diagonal attention and illustrate improvements in metrics such as $max|V|$ and sec/it, as shown in Table 2.

### Weaknesses
1) The meaning of alpha-weighting is unclear. From the perspective of text tokens, it does not appear to differ from the existing operations. It is ambiguous why the authors refer to this as alpha-weighting and describe it as a distinct approach.

2) There is insufficient analysis of the proposed method's effectiveness. It seems that the use of debiased positional encodings significantly contributed to the performance improvement in image benchmarks, yet this is not adequately mentioned or discussed. Additionally, the varying extent of performance improvement across different image benchmarks is not addressed, leaving the discussion lacking regarding which tasks the proposed method significantly impacts.

3) The analysis of the benefits gained from treating vision embeddings and text embeddings differently is inadequate. The authors only mention performance improvements in image benchmarks, without providing insight into how the proposed method influences task execution. They claim that there is a misalignment between modalities in the embedding space of LLaVA-1.6, but do not discuss whether their method addresses this issue, making the relevance of this analysis questionable.

### Questions
1) In which specific tasks does the proposed method demonstrate improvements? Beyond the numerical performance improvements shown in Table 1, a discussion on why it is particularly effective for certain tasks is needed.

2) The authors present an analysis of the misalignment between vision and text tokens alongside Figure 5, stating, "this discrepancy cannot be easily mitigated by a simple adapter layer applied to the visual embeddings." Therefore, does the authors’ proposed method mitigate this discrepancy?

3) Line 221 states, "These approaches involve significant architectural changes..." Why is this considered a disadvantage? If the vision encoder is to be added for further training on multimodal data, then an architectural change seems acceptable.

4) While the authors describe alpha-weighting differently, the operation of text tokens attending to vision and text tokens remains the same as before. Is it valid to claim that this is a new proposal?

5) The information provided in Figure 4 duplicates what can be obtained from Table 1. Since Figure 4 only adds a visual effect without providing additional information, it may not be necessary to include it in the paper.

6) In Table 2, the term "debiased positional encodings" is used, while Line 409 refers to them as "biased positional encodings." Additionally, Section 2 uses the term "learnable positional encodings" without specifying either. The lack of consistency in terminology may confuse readers.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper explores the network architecture of LVLMs regarding visual and textual embeddings. The authors propose a Decomposed Attention mechanism that treats visual and textual embeddings differently to achieve faster training and better performance. An adaptive α-weighting method is introduced to fuse visual and textual information. Experiments on popular benchmarks demonstrate the effectiveness of the proposed methods.

### Strengths
- The problem addressed in this work is both interesting and fundamental.
- The paper is well-illustrated and easy to understand.
- The proposed Decomposed Attention and α-weighting are simple yet effective.

### Weaknesses
- Limited novelty of Decomposed Attention: Using cross-attention to fuse visual and textual embeddings is not novel, as it has been explored in previous VLMs, such as Flamingo [1]. Although this work investigates cross-attention in popular LVLM architectures, like LLaVA [2], the technical contribution appears limited.
- Lack of analysis on α-weighting: Another major contribution is the α-weighting mechanism for fusing visual and textual information, with ablation studies demonstrating its effectiveness compared to Tanh and Sigmoid. However, there is no in-depth analysis of α-weighting.
- Unclear motivation: In Figure 5, the authors suggest that the primary motivation is that textual and visual embeddings occupy different regions in the feature space of LLaVA1.6, which is already revealed in Mind the Gap[3] and well-known in this field. However, a similar feature space analysis is not presented in the proposed model with decomposed attention, which leads to uncertainty about whether the improvements are driven by other factors or the claimed ones.

Reference:

[1]Flamingo: a Visual Language Model for Few-Shot Learning.

[2]Improved Baselines with Visual Instruction Tuning.

[3]Mind the Gap: Understanding the Modality Gap in Multi-modal Contrastive Representation Learning.

### Questions
- For the first weakness, could the authors clarify the main contribution of this work?
- Regarding the second weakness, could the authors provide a deeper analysis of the underlying mechanism of the α-weighting strategy? For instance, reporting the statistics of αV across various benchmarks such as VQA-T, SQA-I, and GQA could shed light on how the DA model prioritizes visual and textual features.
- For the last weakness, could authors provide more evidence that the disentangled visual and textual feature learning benefits the model via proposed methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes the D-Attn framework for training LVLMs, with three key modifications to the standard architecture: diagonalized V2V attention, debiased positional encodings, and alpha-weighting. Experiments show superior performance relative to the standard framework under similar training settings.

### Strengths
The results show that the proposed framework boosts performance across a variety of tasks. The use of open models is appreciated. The visualizations are clear and benefit the paper’s exposition.

### Weaknesses
A number of points in the methodology raise questions:

Diagonalized V2V attention: As this is just applying FC layers to each visual input, calling this “attention” seems like a misnomer. I would expect this to impair performance on inputs containing multiple images which must be understood in context of each other – do the benchmarks tested contain multiple images interleaved with text? If they mostly contain single images, wouldn’t the proposed method be identical to standard attention?

Alpha-weighting: Section 2.4 shows that this is equivalent to standard LVLM attention, so what is being proposed? This seems to simply be another analytic expression for attention and not a novel component being proposed.

I find the demonstration in figure 5 unconvincing. The modality gap is a known phenomenon and may even be beneficial in some cases [1]. The fact that textual and visual embeddings cluster separately does not mean that a linear projection does not produce representations useful for downstream tasks ([1] is a counterexample of this).

[1] Liang et al. Mind the gap: Understanding the modality gap... NeurIPS 2022

### Questions
The paper claims diagonalized V2V attention is most advantageous e.g. with high-resolution input images – what about applying standard resizing to input images? Especially since this is a standard step for inputting images to CLIP-like visual encoders.

Debiased positional encoding: With the proposed method, what gives the LVLM information about the relative position of text and image? If there is none, doesn’t this mean the LVLM is blind to the position of an image within text?

### Soundness
2

### Presentation
3

### Contribution
2
