# Spiking Vision Transformer with Saccadic Attention

- Decision: Accept
- Avg Score: 6.60
- Scores: 6, 5, 8, 6, 8

## Abstract
The combination of Spiking Neural Networks (SNNs) and Vision Transformers (ViTs) holds potential for achieving both energy efficiency and high performance, particularly suitable for edge vision applications. However, a significant performance gap still exists between SNN-based ViTs and their ANN counterparts. Here, we first analyze why SNN-based ViTs suffer from limited performance and identify a mismatch between the vanilla self-attention mechanism and spatio-temporal spike trains. This mismatch results in degraded spatial relevance and limited temporal interactions. To address these issues, we draw inspiration from biological saccadic attention mechanisms and introduce an innovative Saccadic Spike Self-Attention (SSSA) method. Specifically, in the spatial domain, SSSA employs a novel spike distribution-based method to effectively assess the relevance between Query and Key pairs in SNN-based ViTs. Temporally, SSSA employs a saccadic interaction module that dynamically focuses on selected visual areas at each timestep and significantly enhances whole scene understanding through temporal interactions.
Building on the SSSA mechanism, we develop a SNN-based Vision Transformer (SNN-ViT). Extensive experiments across various visual tasks demonstrate that SNN-ViT achieves state-of-the-art performance with linear computational complexity. The effectiveness and efficiency of the SNN-ViT highlight its potential for power-critical edge vision applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel SNN-ViT incorporating a Saccadic Spike Self-Attention (SSSA) mechanism designed to leverage the spatio-temporal characteristics of SNNs for vision tasks. The authors identify key limitations in traditional self-attention for SNNs and introduce methods to enhance spatial relevance assessment and temporal dynamics.

### Strengths
1. The experiment results show that the provided models can outperform previous methods on various tasks.

2. The SNN-ViT’s linear computational complexity, achieved through SSSA-V2, enhances its viability for energy-critical applications and distinguishes it from previous methods that rely heavily on expensive MAC operations.

3. This paper is well written with a detailed appendix to understand their theory.

### Weaknesses
1. The attention heatmaps in Figures 5 and 7 appear noisy and lack interpretability compared to the original ViT. It is challenging to correlate these attention patterns with the final detection results. The binary nature of the SSSA module's operation, switching between focus and ignore states, likely contributes to this noisiness. However, the lack of clear spatial patterns makes it difficult to understand which features the network is actually using for detection. Additional explanation of these heatmaps would strengthen the paper’s presentation and the interpretability of the results.

2. The paper lacks ablation studies on the design of the "patch" mechanism within the saccadic interaction module. The current design uses a subset of the QK matrices, but the rationale for this specific subset selection is not thoroughly justified. Would performance improve if all values in the QK matrices were used, even if this increases computational complexity? Additionally, it would be helpful to analyze whether the "patch" design enhances generalizability across various datasets or tasks. The absence of these studies makes it difficult to assess the optimality of the chosen patch mechanism.

### Questions
1. Figure 1 lacks a clear explanation. In this figure, I assume the y-axis represents the number of samples and the x-axis represents a numerical magnitude, but this is not explicitly stated. Please add axis labels with units in the revised manuscript. Additionally, these numbers were obtained through simulation. Will there be simulation-reality gap? Would real datasets yield similar distributions or statistics? Does different dataset impact the statistics?

2. Could you provide a reference or further clarification for the statement in lines 277–278? Adding a source or further explanation here would help substantiate this claim.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The author of this paper conducted research on the architecture of introducing Vision Transformers into spiking neural networks (SNNs). By analyzing the distribution of Query and Key in vanilla self-attention mechanisms and existing self-attention mechanisms in SNNs, the author pointed out the shortcomings of current SNN+Transformer approaches. To address these shortcomings, the author introduced the method of Sacadic Spike Self-Attention and designed the SNN-ViT network framework based on this method. The performance of the proposed approach was validated on various tasks and datasets.

### Strengths
The author has a deep understanding of the existing SNN+Transformer work and has summarized the common shortcomings of these studies.

### Weaknesses
1. The theoretical derivation is insufficient; the proof related to the concept of "equivalence" provided in the paper is not included in the appendix, and there are incomplete formulas in some places, such as Eq. (7).
2. The understanding of SNNs is not profound, including the basic processes of biological spiking neurons.
3. There are insufficient ablation experiments to adequately support the effectiveness of the various new methods proposed in the paper.
4. There is a lack of understanding of the cited references, especially papers closely related to the methods in this study, and there is no comparison or discussion of these methods with the approaches presented in this paper.

### Questions
1. The author points out in the paper that the incompatibility of LayerNorm with the spike-driven characteristics of SNNs leads to a significant difference in the distribution of Query and Key, resulting in performance degradation. However, in reality, 1) many SNN studies have replaced LayerNorm with BatchNorm to allow BN to be merged into Conv during inference, thus maintaining the spike-driven characteristics, and 2) the LayerNorm operation should be mergeable into Linear during inference. In this case, is the author's analysis of the distribution of Query and Key unfair? Because there is no normalization applied to the Query and Key in this context and the normalization operation itself can be incorporated into the SNN.
2. In section 3.2, the paper points out that previous work did not introduce temporal information modeling in the design of self-attention operators. However, it is well known that SNN inherently model the temporal features of inputs by the spiking neuron, and often involve the insertion of spiking neurons across many layers of the network. Therefore, why does the author insist on adding an additional temporal modeling component to the self-attention operator?
3. In section 3.2, the author states, "However, due to the reset and decay mechanism, the residual membrane potential cannot sustain long-range dependencies, resulting in a significant loss of historical information." This assertion is inherently incorrect, as biological neurons include decay and reset mechanisms, which actually enable spiking neurons to avoid excessive firing and effectively retain memory. The author's outright dismissal of the contributions of decay and reset operations to neurons raises doubts about whether the author truly understand spiking neural networks.
4. I believe that the mechanism of the Saccadic Neuron inserted by the author in the self-attention mechanism bears a high similarity to the Parallel Spiking Neuron proposed in [1], especially in Equation (8). While I noticed that the author referenced this literature in the paper, there was no mention of the content regarding PSN in the section where Saccadic Neuron is introduced. I would like the author to address what the relationship and differences are between Saccadic Neuron and PSN. Why not use PSN directly?
5. The author presents the so-called equivalence between training and inference in Eq.(8), but I am skeptical about this equivalence. I hope the author can provide a detailed proof of the equivalence between the two processes.
6. The author introduces a new modeling method and neuron model in the SSSA module. While this may reduce complexity to some extent, it also seems to introduce MAC operations, specifically reflected in the integer vector outer product in SSSA-V1 and the Hadamard product operation in SSSA-V2.
7. Table 2 presents a performance comparison on ImageNet-1k. When compared with SpikingResformer, it can be seen that at 13.7M vs. 17.8M, the energy consumption is 14.28mJ and 3.37mJ, with corresponding performances of 74.66% and 75.95%; at 30.4M vs. 35.5M, the energy consumption is 20.83mJ and 5.46mJ, with performances of 76.87% and 77.24%. This indicates that there is an advantage in performance only when the model scale is increased, while there seems to be no significant advantage in smaller networks. Additionally, the claimed contribution of reduced computational complexity appears to remain at a theoretical level, as there is no advantage from the perspective of energy consumption.
8. In the design of the ablation experiments, the paper only provides experimental results for the SSSA and GL-SPS modules, without analyzing the contribution of the internal components of the proposed SSSA to performance. For example, it does not discuss the performance of SSSA-V1 or the effect of replacing the Saccadic Neuron with a standard LIF neuron.
[1] Fang, Wei, Zhaofei Yu, Zhaokun Zhou, Ding Chen, Yanqi Chen, Zhengyu Ma, Timothée Masquelier, and Yonghong Tian. "Parallel spiking neurons with high efficiency and ability to learn long-term dependencies." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work draws on biological saccadic attention mechanisms to design a ViT with reduced computational overhead. It proposes a novel self-attention paradigm tailored for spikes, achieving a computational complexity of O(D). Extensive experimental results validate the model's advanced accuracy and general applicability.

### Strengths
Overall, this is an interesting work. The strengths are outlined as follows:
1. The approach is thoroughly presented, including detailed explanations of the design and operational logic of all modules. The method section is also specifically tailored to address the issues raised.
2. The analysis of the correlation computation among spike sequences is good, with solid theoretical backing and substantial experimental support.
3. The complexity of the proposed SSSA is O(D), which is commendable for reducing computational complexity and further leveraging the energy efficiency of SNNs.

### Weaknesses
1.Unclear Expression: I suggest author to provide a more detailed description of the workings of the Saccadic neurons in the main text. For example, in Equation (8), what is the difference between the bolded Vth​ and the non-bolded version? Additionally, in lines 302-308, why does asynchronous inference not require dependence on historical membrane potentials? The explanation of how the membrane potential is updated and how the threshold is applied in the inference phase is not clear. Specifically, the relationship between the membrane potential H[t] at time t, and the previous membrane potential H[t-1] needs to be clarified. Furthermore, the mechanism by which the threshold Vth is dynamically adjusted during inference should be explained in more detail. I believe this is crucial for achieving lower computational complexity in SSSA.
2.The experiment details of SNN-ViT with YOLO-v3 in remote sensing target detection tasks is not clearly articulated. For example: How does the backbone network integrate with the classification head? What are the specific layers used for feature extraction and how are these features fed into the YOLO-v3 detection heads? What are the training environment and hardware requirements? These aspects should be further clarified in the appendix. The specific configurations of the YOLO-v3 model, such as the number of anchor boxes and the input image size, are also missing.
3.While the appendix is informative, it does not fully bridge the knowledge gap for those outside the specialty. I suggest adding detailed explanations for Appendices A and B.   Appendix A could be expanded to include why dot products in ANNs effectively measure Q-K correlation, along with their mathematical proof. Secondly, cross-entropy is an important method for measuring similarity in Appendix B—why is it not used in ANNs for this purpose, while dot products are preferred instead? The explanation should also include a discussion of the limitations of using cross-entropy for similarity measurement in the context of attention mechanisms.

### Questions
1. I'm interested in the author's distribution-based approach to correlation calculation. Does this method assess the similarity between Q and K based on spike firing rates？ does it ensure that non-spike computations are not introduced?
2. Were all subsequent experiments conducted on SSSA-V2? Would V1 perform better when floating-point computations are involved?

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
4

### Summary
This paper analyzes the spatial relevance and temporal interaction in vanilla SNN-based ViTs, indicating that the mismatch between vanilla self-attention mechanisms and spatio-temporal spike trains may be one of the reasons for the performance gap between SNN-based and ANN-based ViTs. To address these issues, this paper proposes a biologically inspired SSSA mechanism. In both the spatial and temporal domains, SSSA demonstrates a stronger capability for information processing. Furthermore, the SNN-ViTs built upon SSSA also achieve SOTA performance with linear computational complexity, highlighting the energy efficiency potential of SNNs in practical applications.

### Strengths
1. This paper offers a plausible explanation for the performance gap between SNN-based and ANN-based ViTs and proposes an efficient mechanism to replace the vanilla self-attention mechanism. SNN-ViTs built on the proposed method achieves both high-performance and energy-efficience.

2. The temporal interaction within SSSA addresses a significant question: What are the benefits of utilizing SNNs with temporal structures for processing image data that lacks inherent temporal structures?

### Weaknesses
1. Prior to their combination with transformer architecture, the performance gap between SNNs and ANNs already existed, suggesting that an enhanced attention mechanism alone cannot fully mitigate the performance decrement inherent to spiking neuron. Therefore, Table 1-3 ought to include the performances of SOTA ANN-based ViTs, to clearly illustrate the performance gap between SNN-based and ANN-based models. Although this reality may be discouraging, a precise comprehension of this gap is conducive to the practical implementation of SNN research.

2. The introduction to biological saccadic mechanisms is inadequate, especially due to the absence of a mathematical formulation. This results in a seemingly tenuous connection between the methodology and its biological inspiration.

### Questions
1. It is required to include the performances of SOTA ANN-based ViTs in Tables 1-3 for a direct comparison with the SNN-based ViTs results.

2. The introduction of biological saccadic mechanisms and the rationale behind the inspiration can be further elaborated. Specifically, this should include the research history of biological saccadic mechanisms, an overview of related works on algorithms inspired by other visual mechanisms, and concrete examples illustrating how the mathematical formulation of the proposed method correlates with the characteristics of biological saccades.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a biologically inspired (Spike-based ViTs) inspired by biological visual saccadic attention mechanisms. The study thoroughly investigates two challenges for current SNN-based Transformer: degraded correlation computation and limited temporal dimensionality. To address these issues, the authors propose a distribution-based method for correlation computation and a saccadic time interaction strategy. Notably, the introduced SSSA module has O(d) computational complexity.

### Strengths
1. Biological Inspiration: The model is well-motivated by biological mechanisms, which is a strong point given the effectiveness of biological systems in visual tasks.
2. Low Computational Complexity: The SSSA method achieves exceptional performance while maintaining linear computational complexity.
3. Correlation Degradation Analysis: The discussion on the degradation of correlation computation with binary spike trains is clear and comprehensible, with theoretical and experimental validations.

### Weaknesses
1. Expression Details: Although the paper is generally clear, some symbols in the equations, like the QK subscripts in Equation 1 and the bolding of H in Equation 8, should be simplified for better distinctions
2. Energy Consumption Analysis: The energy consumption in the table.3 require further clarification.
3. Experimental Validation: Results should be verified through multiple trials, including error bars to enhance data reliability.

### Questions
1. I am curious about the time cost associated with the training phase. Given that SNNs are known for their substantial training overhead. Detailed information on the resource requirements and approximate time costs during network training should be discussed in the appendix.
2. I am very interested in the "Saccadic Neurons." Could the authors explain how the saccadic attention mechanism is implemented specifically? Additionally, I would appreciate an example detailing the processes of parallel training and serial decoupling.
3. Could the authors explain if the code implementations for SSSA-V1 and SSSA-V2 are identical, given their mathematical equivalence? Which method performs better?

### Soundness
3

### Presentation
3

### Contribution
4
