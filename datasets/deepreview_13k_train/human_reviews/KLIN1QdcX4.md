# PopAlign: Population-Level Alignment for Fair Text-to-Image Generation

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
Text-to-image (T2I) models achieve high-fidelity generation through extensive training on large datasets. However, these models may unintentionally pick up undesirable biases of their training data, such as over-representation of particular identities in gender or ethnicity neutral prompts. Existing alignment methods such as Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) fail to address this problem effectively because they operate on pairwise preferences consisting of individual \textit{samples}, while the aforementioned biases can only be measured at a \textit{population} level. For example, a single sample for the prompt ``doctor" could be male or female, but a model generating predominantly male doctors even with repeated sampling reflects a gender bias. To address this limitation, we introduce PopAlign, a novel approach for population-level preference optimization, while standard optimization would prefer entire sets of samples over others. We further derive a stochastic lower bound that directly optimizes for individual samples from preferred populations over others for scalable training.
Using human evaluation and standard image quality and bias metrics, we show that PopAlign significantly mitigates the bias of pretrained T2I models while largely preserving the generation quality.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the issue of inherent biases in generative models, which often stem from biased large-scale training data. The authors propose a method to reduce these biases through population-level preference optimization. Specifically, they generate multiple win-lose pairs for each prompt, which are then used for fine-tuning via preference optimization. Empirical results suggest that this method can help mitigate gender and race biases across a set of 100 prompts.

### Strengths
1. The paper is straightforward and easy to follow.

### Weaknesses
1. **Lengthy Background and Related Work Sections:** These sections are overly detailed, detracting from the main methodology and potentially causing readers to lose focus on the core contributions of the paper.
2. **Limited Novelty:** The proposed method is relatively straightforward, primarily offering a way to create a fairness-focused pairwise dataset for preference learning. The training technique resembles the approach introduced in Diffusion-DPO, raising concerns about the extent of novelty. Much of the performance gain may be attributed to the newly generated dataset rather than the proposed population-level alignment, which essentially involves using multiple sample sets for each prompt.
3. **Lack of Transparency in Evaluation:** Details about the evaluation process are sparse, with only a mention of 300 prompts used for training and 100 for evaluation. A more transparent evaluation approach would enhance the paper’s credibility.
4. **Narrow Focus on Fairness Issues:** The paper only addresses gender and race biases, which is a limited scope. Expanding to other categories of bias could significantly strengthen the impact and generalizability of the proposed method.

### Questions
See weaknesses.

### Soundness
3

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
4

### Summary
This work aims at tackling biases of text-to-image (T2I) models that appear at the population. As shown by multiple previous work, T2I models tend to over-represent certain parts of the learned distribution when prompted with underspecified prompts. This work focuses on the societal implications this phenomena might have, aiming at tackling gender and ethnicity biases. To do so, the authors proposed PopAlign, an alignment strategy for pre-trained T2I models that goes beyond pairwise comparisons as common approaches for incorporating human preferences such as RLHF and DPO. Empirical evaluation was carried out considering the SDXL model and variants obtained by incorporating other bias mitigation techniques. The resulting models were compared in terms of fairness metrics, as well as other aspects of generation quality, such as prompt-image alignment. Overall, results showed that PopAlign was able to improve fairness of generated images while maintaining quality with respect to the other evaluated dimensions.

### Strengths
- S1: The work proposes a solution to a critical and open research problem.
- S2: Although previous work has shown that there is an inherent trade-off between diversity and quality [1], PopAlign was shown to improve fairness while not greatly harming other quality aspects.
- S3: The authors compared a PopAlign with a diverse set of techniques to mitigate biases in T2I models.
- S4: Beyond autoeval metrics, the authors also evaluated the proposed approach via human evaluation.


[1] Astolfi et al., Consistency-diversity-realism Pareto fronts of conditional image generative models, 2024

### Weaknesses
 - W1: Unclear generalization of findings to other text-to-image models. The authors only performed experiments with a single base model, namely SDXL, which makes it impossible to assess to what extent the efficacy of PopAlign would transfer to other models.

- W2: Choice of evaluation metrics. CLIP has been extensively shown to not correlate well with human perception of text-to-image alignment [1], making it a poor metric to evaluate prompt-image alignment. Authors could consider, for example, VQA-based metrics such as Gecko and VQAScore [1, 2].  

- W3: Lack of statistical significance in the presented results. Results presented in Tables 1, 2, and 3 do not show any notion of dispersion in the reported values, nor statistical significance evaluation. Without this information it is impossible to perform a rigorous comparison of the evaluated methods, making it unclear whether PopAlign is actually being effective in its goal of mitigating gender and ethnicity biases.

- W4: Soundness of human evaluation. In the main text there is no information about how the human evaluation was conducted. Details such as the number of annotators, sample size, annotation template, quality metrics such as inter-annotator agreement are missing. Without these details it is not possible to judge how solid the results are. 

- W5: Conflating race and ethnicity. Throughout the text, the authors seem to use the terms race and ethnicity interchangeably, but there are several references pointing out to differences between both identity dimensions, e.g. [3, 4].

### Questions
- Q1: It is unclear to me how the CLIP metric is being computed. CLIP score values fall in the [-1, 1] interval, so it is not clear to me what the CLIP metric on Tables 1, 2, 3, which is greater than 1, is accounting for.

- Q2: Please add details about how the results in Tables 1, 2, and 3 are being computed. What exactly is being presented in the tables? Average scores across all prompts? Also, include confidence intervals and perform statistical significance to allow for proper interpretation of the presented results. 

- Q3: Please refer to weakness W4 for missing details on the human evaluation.

- Minor but also relevant: the work has several typos and many words/characters are missing the space between them and the next word/character. For example: 
  - Line 101: Space between populations. and Fig. 2. 
  - Line 190: noises -> noise.
  - Equations also need punctuation, e.g. commas in Eqs. 2 and 4.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces PopAlign, an approach to align Text-to-image models towards population-level preferences. This is done by extending the direct preference optimization objective that works on pairs of images, to sets of images that represents population preferences. Experimental results show that the method is able to generate less biased (in terms of racial and gender attributes) images while maintaining high image quality.

### Strengths
- The paper was well written and easy to follow.
- The method is clear and easy to use and does not degrade the quality of the generations.

### Weaknesses
 - More details are needed on how well the method generalizes to new prompts. Sec 6.3 mentions that 100 prompts are manually written for evaluation, how similar are these prompts to those used for training? Does it generalize to actions, or the more general prompts from LAION Aesthetics dataset, style and personal descriptors used by Shen et al., or to multiple people? Sec 6.5 evaluates on generic prompts but not for fairness.
- Scalability of the method. The categorial attributes of gender and race were used in the paper, it would have been useful to demonstrate the method with other types of attributes.
    - A classifier and face detector are used to filter out inconsistent or ambiguous images. There may be other attributes where such models need to be trained separately. An ablation study of the importance of this step would also be useful. 
    - It is not clear how prompt augmentation is done, e.g., manually or with another language model, and how this it should be done for continuous attributes e.g., age.
- The method seems to be computationally expensive, compared to the baselines as it requires generating additional data and finetuning. An additional column specifying the costs of the method and baselines would be useful in understanding the tradeoffs.

### Questions
- What are some of the challenges in scaling the method to more attributes or non binary attributes (e.g., age, culture norms) and to more complicated generations where there are multiple entities? Is the bottleneck mostly in the generation (compositional generation, sanity check) step?
- How sensitive is the method to the filtering stage described in  Sec. 4.1? E.g., what would be the performance of the method without the sanity checks?
- What is the computation cost of the entire pipeline for the methods in Tab. 1?
- How many sets of images were evaluated in Fig. 5’s study and how many users were involved?

### Soundness
3

### Presentation
2

### Contribution
2
