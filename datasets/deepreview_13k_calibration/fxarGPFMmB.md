# Reasoning with trees: interpreting CNNs using hierarchies

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Challenges persist in providing interpretable explanations for neural network reasoning in explainable AI (xAI). Existing methods like Integrated Gradients produce noisy maps, and LIME, while intuitive, may deviate from the model's reasoning. We introduce a framework that uses hierarchical segmentation techniques for faithful and interpretable explanations of Convolutional Neural Networks (CNNs). Our method constructs model-based hierarchical segmentations that maintain the model's reasoning fidelity and allows both human-centric and model-centric segmentation. This approach offers multiscale explanations, aiding bias identification and enhancing understanding of neural network decision-making. Experiments show that our framework, \ourMethod,  delivers highly interpretable and faithful model explanations, not only surpassing traditional xAI methods but shedding new light on a novel approach to enhancing xAI interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes xAiTrees, a framework that combines hierarchical segmentation algorithms, attribution techniques, and tree shaping to compute the importance of image regions and provide a multi-scale visualization. The framework first divides the image into multiple regions using hierarchical segmentation algorithms. It then computes the importance of these regions by combining attributions obtained from traditional attribution methods with the topology of the tree derived from the previous step (shaping). Finally, the most important regions are selected based on a threshold and visualized.
Depending on the algorithm used in the initial segmentation step, the framework supports explanations that align with either model-based insights or human reasoning. Across various settings and datasets, the proposed approach demonstrates performance that is comparable to or better than standard baselines. Additionally, the authors conduct a qualitative evaluation through a user study focused on bias detection and identification, highlighting the better performance of their approach.

### Strengths
- The combination of shaping, attribution, and hierarchical algorithms is novel and represents an interesting direction for future research.
- The flexibility of the framework, as it can be potentially combined with any feature attribution method to compute region importance. This means its precision can improve over time as advancements are made in feature attribution methods (see questions)
- The framework demonstrates competitive performance compared to standard baselines (with certain caveats, discussed below).

### Weaknesses
- The selection of competitors is not well justified and does not align with the authors' claim, “comparison with state-of-the-art xAI visualization methods”.  The paper mixes algorithms that support region-based explanations and pixel-wise algorithms. If pixel-wise algorithms are considered competitors, more advanced methods in the literature surpass the baselines used and are considered state-of-the-art, like Expected Gradients, FullGrad, Local Path Integration, and several variants of SHAP and LIME. The authors should either revise the text to remove references to state-of-the-art or provide further evidence to the claim.

- The related work section can be improved by referencing to more recent feature attribution methods (see the previously mentioned references, but there are many others)

- The organization and narrative flow of the paper need improvement, as highlighted by the following examples:
   - Introduction: Lines 32-41. The section on healthcare seems somewhat out of the scope of the paper and not well connected to the main topic.
   - Related Work. The section feels as if it was originally a single text that was split into three subsections without adjusting the narrative. Additionally, the first subsection lacks references and functions more as an introductory paragraph. This paragraph would be better suited as part of a “Preliminaries” section rather than the related work
  - Preliminaries: This section consists of only one subsection and might be better positioned as the opening part of Section 4. Line 157 repeats information, and lines 159-161 are unclear regarding which methods are being discussed. This is explained later in the paper, but the positioning of this sentence could be improved for clarity.
   - Methodology: 
        - it is not enough to simply take the regions with the highest attributes: there are too many of them”. This statement is not clear. What do the authors mean? Do all the regions converge to the same value?
        - Considering the importance of tree shaping, this concept deserves a longer and more detailed description.
  - Experiments 5.1: This section could be better organized.  Introducing metrics, presenting results, and explaining the motivations behind experiments in a mixed format make the section difficult to follow. I would suggest using a dedicated subsection to introduce all necessary information (e.g. all the metrics), followed by a separate analysis of results. Changing the structure of this section would improve readability.
- The definitions of the configurations (e.g. Tree-Occ) are reported in the appendix but used in the main text. I suggest moving them to the main text to make the analysis easy to digest.
- Some adjectives could be removed to make the text more concise (e.g., “complex edge patterns and produces precise edge maps”).
- Some sections (e.g., 5.1) include too many acronyms making the section less readable

### Questions
As highlighted in the weaknesses section, my main questions and concerns focus on the design choices, experimental setup, and their descriptions in the main text. Addressing these areas, either through additional experiments or clearer explanations, would strengthen the paper, and I would be open to increasing the score accordingly.
- Why do the authors include concept-based explanations in the related work? This section includes Ms-IV, which is considered a competitor for quantitative evaluations. Why was only Ms-IV chosen while other concept-based explanations were excluded? (I know the authors mentioned the case of ACE)
- Why are other state-of-the-art feature attribution methods not included in the comparisons? Is there a technical reason for their exclusion?
- There is no experiment supporting the reliability of the importance scores. All evaluations focus on the ranking and the position of regions in the ranking, as metrics are computed using the top percentage of selected regions. Does this imply that the absolute importance scores are unreliable while the ranking is valid? If the scores are reliable, the authors should explain why they did not consider evaluating the correlation between importance scores and their impact on the prediction (e.g., on logits). The discussion provided in lines 302-305 could be further elaborated for clarity and support from my point of view. 
- In terms of the framework's flexibility, is it accurate to say that any feature attribution method can be used to assign scores to the regions? If so, could the framework be viewed as a tool that enables the transformation of pixel-wise attributions into region-based attributions? A comparison showing the loss and gain in saliency between results obtained with and without the framework would significantly strengthen the paper.
- Could the authors further elaborate on the trade-off (in terms of results) between the model-based and edge-based configurations? Given the emphasis placed on this aspect earlier in the text, it would be better to include analyses/summaries of this trade-off in both section 5 and the conclusion.

### Soundness
2

### Presentation
1

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
This paper introduces xAiTrees, a framework that uses hierarchical segmentation to deliver interpretable explanations for CNNs. Unlike methods such as Integrated Gradients and LIME, xAiTrees aims to uncover the model’s reasoning structure, offering both human- and model-centric segmentations. The approach supports multiscale explanations, allowing for the identification of biases and improved insights into neural network decision-making.

### Strengths
- Gaining a deeper understanding of feature hierarchies is both highly relevant and practically insightful.
- The study includes reproducible, comprehensive experiments, in particular also including human evaluations.
- The paper is well-structured and easy to follow, with clearly presented figures and findings.

### Weaknesses
- The choice of occlusion to determine the importance of a region seems arbitrary, especially given the results of Table 1 that shows that occlusion is a weak method to evaluate feature importance.
- The comparison to other xAI methods (GradCAM, LIME, XRAI) is not particularly fair. For the Tree based method information from a secondary segmentation model is used to preselect regions. The task of pixel/region-wise attribution is therefore much more difficult. A better baseline would be to introduce the segmentation masks also for the flipping of these methods and/or use the other attribution methods to assign importance scores as part of the xAITrees method.
- The method overall appears to be an assembly of several existing methods, limiting the overall novelty of the approach. Could you clarify the key novel contributions of xAiTrees beyond the combination of existing methods? What specific insights or capabilities does this framework provide that were not possible with previous approaches?

Relevant related works currently missing:

Structured xAI:
- Q. Zhang, "Interpreting CNNs via Decision Trees," 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Long Beach, CA, USA, 2019.
- Eberle et al. “Building and interpreting deep similarity models”, IEEE Transactions on Pattern Analysis and Machine Intelligence, 44(3), 2020.
- Schnake, et al. "Higher-order explanations of graph neural networks via relevant walks." IEEE transactions on pattern analysis and machine intelligence 44.11 (2021).

### Questions
- Would it be possible to design such a hierarchy without an additional external model? I would assume that the model internally already represents some form of hierarchy that you are trying to recover using a segmentation + attribution approach.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Personally, I find this paper needs a major revision as the overall writing is difficult to follow, due to the paragraph organization and way too many boldface abbreviations (especially in the experiment section). Following are some points that might be helpful:

Strength:

    This paper proposes a model-agnostic framework that is generally applicable regardless of specific model architectures.
    The authors design will detailed experiments that showcase the superiority of the proposed method compared to several baselines.

Weakness:

    The motivation of the work is somewhat unclear. Given that previous work, e.g. LIME, already adopts feature segmentation, the exact segmentation algorithm is free of choice. What is the target problem that the paper trying to address?
    The paper misses necessary formalizations of the to-be-solved problem and the proposed method. The missing details in the methodology create barriers to reader's understanding. For example:
        At lines 204-208, how do the pixel-wise attributions contribute to the segmentation process? This can be benefited from some mathematical formalization of the segmentation process.
        The paragraph of tree shaping starting at line 216 is not sufficiently precise. It is not clear what is a "local maximum" and how the new tree T' is constructed based on G.
    It seems that the proposed framework is a combination of several existing techniques from different domains, which might explain the missing details as mentioned in the last point. However, the combination is less motivated, which appears inconsistent.

Some more points about experiments;

    In section 5.1, the authors quantify method performance by masking out a certain ratio of regions instead of pixels. How does the masking process ensure that the same number of features are removed across different explanation methods for a fair comparison?
    Regarding the test on human evaluation in bias analysis, the biased models seem to still learn (at least some) relveant features according to its performance on the validation set as presented by Table 15. How do the authors verify that the models' decisions are made upon imposed biases, especially given that those are high-level concepts?

### Strengths
Strength:

    This paper proposes a model-agnostic framework that is generally applicable regardless of specific model architectures.
    The authors design will detailed experiments that showcase the superiority of the proposed method compared to several baselines.

### Weaknesses
Weakness:

    The motivation of the work is somewhat unclear. Given that previous work, e.g. LIME, already adopts feature segmentation, the exact segmentation algorithm is free of choice. What is the target problem that the paper trying to address?
    The paper misses necessary formalizations of the to-be-solved problem and the proposed method. The missing details in the methodology create barriers to reader's understanding. For example:
        At lines 204-208, how do the pixel-wise attributions contribute to the segmentation process? This can be benefited from some mathematical formalization of the segmentation process.
        The paragraph of tree shaping starting at line 216 is not sufficiently precise. It is not clear what is a "local maximum" and how the new tree T' is constructed based on G.
    It seems that the proposed framework is a combination of several existing techniques from different domains, which might explain the missing details as mentioned in the last point. However, the combination is less motivated, which appears inconsistent.

### Questions
There are no further questions.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work proposes a hierarchical segmentation tree approach to address issues that arise from the segmentation used in popular XAI techniques, which can impact their faithfulness. The approach leverages existing XAI methods to compute attribution scores for each segment or uses occlusion-based metrics, which they demonstrate are preferable according to several metrics. The method is implemented through four steps: (1) hierarchical segmentation, (2) attribute computation, (3) tree shaping, and (4) hierarchical visualization construction. They conduct experiments on three image-based benchmarks, providing both quantitative and qualitative evaluations of their approach.

### Strengths
1. The paper addresses the significant issue of the somewhat arbitrary selection of superpixels in many widely-used XAI techniques. The authors emphasize the problems this arbitrary selection causes in previous methods.

2. The authors conduct a series of experiments, comparing their method to other XAI techniques. They provide both quantitative and qualitative analyses to evaluate their results comprehensively.

### Weaknesses
1. The proposed method consists of numerous small steps, which makes it challenging to reproduce.

2. The paper does not provide any formal, theoretical, or mathematical justifications for why their method might outperform existing approaches, focusing solely on experimental results.

3. Several choices, either in the algorithm’s procedures or in the evaluation sections, appear arbitrary and are insufficiently justified.

4. While the hierarchical segmentation approach is described as conceptually compatible with various XAI methods, the authors limit their focus to an occlusion metric for attributing segment scores. This reduces the approach’s generalizability.

5. The tables have an extremely small font, making the text difficult to read. Additionally, the appendix contains large tables with similarly tiny font, making them hard to interpret. Improving the presentation of the results in both the main text and the appendix would be beneficial.

### Questions
1. Why do the authors specifically mention CNNs in the introduction? Is there a particular link to convolutions that I may have missed, or could this approach be applied to any neural network architecture?

2. How effective is the method at enhancing the attribution of segments in existing XAI techniques, compared to relying on the occlusion metric?

### Soundness
2

### Presentation
2

### Contribution
3
