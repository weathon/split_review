# Interaction Makes Better Segmentation: An Interaction-based Framework for Temporal Action Segmentation

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Temporal action segmentation aims to classify the action category of each frame in untrimmed videos, primarily using RGB video and skeleton data. Most existing methods adopt a two-stage process: feature extraction and temporal modeling. However, we observe significant limitations in their spatio-temporal modeling: (i) Existing temporal modeling modules conduct frame-level and action-level interactions at a fixed temporal resolution, which over-smooths temporal features and leads to blurred action boundaries; (ii) Skeleton-based methods generally adopt temporal modeling modules originally designed for RGB video data, causing a misalignment between extracted features and temporal modeling modules. In this paper, we propose a novel Interaction-based framework for Action segmentation (InterAct) to address these issues. Firstly, we propose multi-scale frame-action interaction (MFAI) to facilitate frame-action interactions across varying temporal scales. This enhances the model's ability to capture complex temporal dynamics, producing more expressive temporal representations and alleviating the over-smoothing issue. Meanwhile, recognizing the complementary nature of different spatial modalities, we propose decoupled spatial modality interaction (DSMI). It decouples the modeling of spatial modalities and applies a deep fusion strategy to interactively integrate multi-scale spatial features. This results in more discriminative spatial features that are better aligned with the temporal modeling modules. Extensive experiments on six large-scale benchmarks demonstrate that InterAct significantly outperforms state-of-the-art methods on both RGB-based and skeleton-based datasets across diverse scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel Interaction-based framework for Action segmentation,  which integrates multiple temporal resolutions
for frame-action modeling, thereby enhancing temporal interactions. Extensive experimental results demonstrate its effectiveness.

### Strengths
This paper is well-written and it achieves good performance on the benchmarks.

### Weaknesses
 - The contribution of multi-scale temporal modeling have been studied well by many previous works. So this paper has limited novelty.
- Missing recent SOTA methods, like Semantic2Graph and ASPnet.
- Whether the two modal data (RGB and skeleton data) fusion can be used as the input of the model, the experimental results can provide help to the author.

### Questions
See Weaknesses.

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
To enhance skeleton-based action segmentation by extracting more discriminative features, the authors propose multi-scale spatial modeling to fuse different modalities. To improve action segmentation by capturing complex temporal dynamics, the authors propose a MFAI that facilitates frame-action interactions across multiple temporal scales.

### Strengths
This paper clearly outlines its motivations, proposing a MFAI for frame-action interactions and a DSMI for fusing spatial features, with a certain degree of originality.

### Weaknesses
1.	The motivations outlined in the Introduction assume that iterative frame-action interactions at a constant temporal resolution would result in over-smoothing. To substantiate this, a visualization experiment is conducted, which shows that boundaries become more visually discernible. However, the effect may be due to the boundary prediction module and the existing label smoothing method. When aiming to elucidate the precise role of a structure, it is advisable to conduct a single-variable analysis. Regrettably, the paper lacks ablation experiments about both the boundary prediction module and the operations at a fixed temporal resolution. Therefore, the experimental support is insufficient for the conclusion, and the analysis is not rigorous, which makes the motivation speculative and lacks persuasiveness. Suggestions: 
(1) Conduct a comparative analysis of t-SNE visualization results, where one is derived from InterAct and another is from a modified version of InterAct devoid of the BPM.
(2) To ascertain whether a fixed temporal resolution poses a limitation, compare t-SNE visualization outcomes between InterAct and a variant where the encoder-decoder is substituted with MS-TCN.
(3) To evaluate the impact of label smoothing, eliminate the BPM and replace label smoothing with the Average employed by FACT.

2.	Some SOTA methods are not compared in this paper, such as ASPnet, Semantic2Graph, and BIT. I suggest not to ignore these methods that perform better than the proposed one, because some methods also adopt frame-action interaction, such as BIT, and multiply modalities fusion, such as ASPnet. Comparing your method with the above SOTA methods can effectively underscore the merits of your solution, particularly because: (1) Your DSMI serves as a fusion strategy, echoing similar strategies proposed by ASPNet and Semantic2Graph in feature fusion. (2) Your MFAI constitutes a frame-action interaction module, paralleling the frame-action interaction module introduced by BIT.

3.	Many grammar errors need to be corrected, for example,
    (1) The last line of page 4, “suffers from” should be “suffer from”.
    (2) In Section 2.1, “frame and action level” should be revised to “frame and action levels”. 
    (3) In the line before equation (8), “as follow” should be revised to “as follows”.
    (4) Line -5 of page 5, “D is the feature dimensions” should be revised. 
We suggest that the authors have the paper professionally proofread or reviewed by a native English speaker to address language issues comprehensively.

4.	Both MFAI and MAFI are used in this paper, which makes me confused about the paper. We suggest consistently use one acronym throughout the paper and include it in a list of abbreviations for clarity.

### Questions
Did you experiment with replacing the encoder-decoder with models like MS-TCN or ASFormer that operate on fixed full temporal resolution? If yes, please add the descriptions. If not, your motivation for multi-scale analysis in the introduction lacks support.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces **InterAct**, a framework that advances temporal action segmentation by enhancing frame-action interactions and aligning spatial modalities in RGB and skeleton data. It targets limitations in existing temporal modeling techniques that over-smooth temporal features and blur action boundaries. The framework's two key components are Multi-scale Frame-Action Interaction (MFAI) and Decoupled Spatial Modality Interaction (DSMI). MFAI enables frame-action interaction at various temporal scales, and DSMI decouples spatial modeling for RGB and skeleton data to create better-aligned spatial representations. Extensive experimentation demonstrates InterAct’s effectiveness in improving state-of-the-art results across multiple datasets.

### Strengths
The idea of using a shared backbone for both skeleton-based and RGB-feature action segmentation is promising. The method is evaluated on six diverse datasets, showing substantial improvements over competitive benchmarks.

### Weaknesses
### 1. Unsupported Claims on Over-Smoothing and Blurred Boundaries
The authors assert that RGB-based TAS methods suffer from over-smoothing, which they argue leads to blurred action boundaries. However, this claim lacks convincing evidence:
- More thorough proof is necessary to validate that over-smoothing indeed causes boundary detection issues. Specifically, the paper does not provide a quantitative measure of feature smoothness and directly correlate it with boundary detection performance. The argument relies on a visual interpretation of Figure 4, which is insufficient to establish a causal link.
- It is unclear how the results presented in Figure 4 support the claim of over-smoothing. Further clarification is needed to explain the causal link between the observed effects in Figure 4 and the issue of over-smoothing. The visualization shows feature embeddings, but it does not demonstrate that these embeddings are smoother near boundaries compared to other regions.
- Table 6 shows that three stages of frame-action modeling yield optimal results, yet the authors do not adequately explain why this stage limit would prevent oversmoothing, despite assuming it as an issue. The paper needs to clarify why a specific number of stages inherently prevents over-smoothing, rather than just empirically observing a performance peak.

### 2. Limited Novelty and Borrowed Ideas
The paper presents limited novelty, appearing to draw heavily on ideas from prior works. Notably:
- The use of multiple temporal resolutions within an encoder-decoder model, along with multi-scale outputs for prediction, has already been explored in previous work (Singhania et al., 2023). The paper needs to clearly articulate the differences in how it utilizes multi-scale temporal modeling compared to existing approaches, particularly in the context of frame-action interaction.
- Similarly, the implementation of segment-level learnable queries and cross-attention closely resembles techniques described in Behrmann et al. (2022). The paper should clarify how its query-based approach differs from, or improves upon, the specific mechanisms used in prior work, especially in terms of how queries are generated and used for temporal modeling.
The authors should clarify how their approach differs from or improves upon the multi-scale techniques used by Singhania et al. (2023) or the query-based methods proposed by Behrmann et al. (2022).
### 3. Inadequate Explanation on Addressing Spatial and Temporal Misalignment
The paper claims to address the misalignment between spatial features and temporal modules in skeleton-based TAS, yet it does not provide a satisfactory explanation of how the proposed method mitigates this issue. Specific details on how the approach prevents or corrects spatial-temporal misalignment would strengthen the paper’s argument. The paper should elaborate on the specific mechanisms within the DSMI module that ensure better alignment, going beyond the general claim of interactive fusion.

### 4. Inconsistent Ablation Study and Limited Scope
The ablations presented in Tables 4 and 5 are conducted on different datasets, which weakens the comparison. Additional issues include:
- Table 5 appears to focus on skeleton data, suggesting that there is no ablation specifically on RGB-based action segmentation. It is necessary to see ablation results on the Breakfast dataset, a large RGB action segmentation dataset, to assess the robustness of the proposed method. The absence of RGB-specific ablations raises concerns about the generalizability of the method.
### 5. Missing Benchmark Results
In Table 1, results are missing for MCFS-130 on the DiffAct, UVAST, and LTContext benchmarks, despite the authors of these approaches making code available. The inclusion of these results would provide a more complete comparison. The lack of these comparisons makes it difficult to assess the true performance of the proposed method against state-of-the-art techniques.

### 6. Missing Ablation for Encoder and Decoder Layers
An ablation on the number of encoder and decoder layers is missing, which would be important to evaluate. Layer depth directly influences the granularity of temporal resolution, a factor critical to the proposed framework. Without this ablation, it is unclear how the depth of the encoder and decoder impacts the overall performance and the multi-scale temporal modeling.

### Questions
Several important ablations and experiments are missing; see weaknesses for further details.

### Soundness
2

### Presentation
2

### Contribution
2
