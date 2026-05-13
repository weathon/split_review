# Analyzing and Boosting the Power of Fine-Grained Visual Recognition for Multi-modal Large Language Models

- Decision: Accept
- Scores: 5, 3, 8

## Abstract
Multi-modal large language models (MLLMs) have shown remarkable abilities in various visual understanding tasks. However, MLLMs still struggle with fine-grained visual recognition (FGVR), which aims to identify subordinate-level categories from images. This can negatively impact more advanced capabilities of MLLMs, such as object-centric visual question answering and reasoning. In our study, we revisit three quintessential capabilities of MLLMs for FGVR, including object information extraction, category knowledge reserve, object-category alignment, and position of the root cause as a misalignment problem. To address this issue, we present Finedefics, an MLLM that enhances the model's FGVR capability by incorporating informative attribute descriptions of objects into the training phase. We employ contrastive learning on object-attribute pairs and attribute-category pairs simultaneously and use examples from similar but incorrect categories as hard negatives, naturally bringing representations of visual objects and category names closer. Extensive evaluations across multiple popular FGVR datasets demonstrate that Finedefics outperforms existing MLLMs of comparable parameter sizes, showcasing its remarkable efficacy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This research paper investigates the challenges faced by multi-modal large language models (MLLMs) in fine-grained visual recognition (FGVR), a task involving identifying specific sub-categories within broader categories, such as distinguishing different types of birds. The authors pinpoint the root cause of this underperformance as a misalignment between visual object representations and corresponding category names within the model's representation space. To address this, they propose Finedefics, an MLLM architecture that uses informative attribute descriptions of objects as an intermediate point to bridge this gap. This approach effectively aligns visual objects and category names during training, leading to significant performance gains in FGVR tasks compared to existing models.

### Strengths
- Section 2 provides a thorough and engaging explanation of the problem.
- Problem formulation is straightforward and easy to understand.
- The paper demonstrates significant improvements across all tested datasets.

### Weaknesses
 - Despite the strong results, the proposed methods lack substantial novelty compared to prior works ([1], [2]) that also leverage foundation models for data augmentation and model fine-tuning.


### Questions
- In the experiment in Section 2.1, what prompts did you use? Also, to clarify, was linear probing performed after the connector or the LLM?
- Could you explain Figure 2 (c+f) in more detail?

- [1] H. Laurençon, L. Tronchon, M. Cord, and V. Sanh. *What matters when building vision-language models?*
- [2] M. Yuksekgonul, F. Bianchi, P. Kalluri, D. Jurafsky, and J. Zou. *When and Why Vision-Language Models Behave like Bags-of-Words, and What to Do About It?*

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a model called Finedefics to improve FGVR in MLLMs, which typically struggle with distinguishing subordinate-level visual categories. The authors identify misalignment between visual objects and category names as a key challenge, proposing a two-stage training approach that uses attribute-augmented contrastive learning to align objects and category descriptions more effectively. Evaluations across several FGVR datasets show that Finedefics significantly improves recognition accuracy over existing MLLMs.

### Strengths
1. The paper does an excellent job identifying the specific challenges of FGVR within MLLMs. It is worth mentioning that this paper provides valuable insights into the object-category misalignment issues in existing MLLMs. 
2. The proposed Finedefics framework introduces a creative method for addressing FGVR challenges by employing attribute-augmented alignment.
3. The paper’s methodology is thorough, with a well-delineated two-stage training process.

### Weaknesses
In general, the motivation for this submission is easy to understand and insight is interesting, but the experimental analysis is limited. In addition, there are still several weaknesses, as follows:  
1. The proposed Finedefics method was constructed and validated solely based on the Idefics2 model, with no tests conducted on other prominent MLLMs. Different MLLMs, like BLIP-2, LLaVA, or Qwen-VL-Chat, vary significantly in their abilities to process visual features, generate textual descriptions, and perform contrastive learning. Without experimental validation across these models, it’s challenging to confirm the general applicability of Finedefics. Furthermore, the reliance on a single model limits the understanding of how the proposed method interacts with different vision encoders and modality connectors, which are crucial components of MLLMs.
2. The paper contrasts "object-category" and "object-attribute-category" pairs, but it does not analyze the effects of specific attribute types (e.g., color, shape, texture). An ablation study could selectively remove particular attribute types to evaluate their contribution to performance improvement. This would help clarify which attributes are most important in fine-grained recognition tasks, particularly if certain attributes are more critical for specific datasets, like flowers or birds. The analysis should also consider the potential redundancy or overlap between different attribute types, and how this impacts the learning process.
3. While standard contrastive learning ablation is provided, the study lacks a comparison between hard negatives and simple negatives. Additional experiments could assess performance when hard negatives are removed, highlighting whether they significantly enhance alignment and fine-grained recognition capability. The analysis should also explore different strategies for selecting hard negatives, as the effectiveness of contrastive learning is highly sensitive to the choice of negative samples.
4. The current study compares one-stage and two-stage training, but more granular analysis could be performed. For example, selectively adding or removing specific training processes within each stage could reveal the individual effects of the alignment and instruction-tuning stages. This would help clarify the extent to which each stage contributes and whether they are complementary under certain conditions. The analysis should also investigate the impact of different training schedules and learning rates for each stage.
5. The methodology relies on attribute extraction from pre-trained models like GPT-4 and LLaVA. However, there’s no empirical analysis of how reliable or accurate these attributes are for all instances in the datasets, especially for categories with subtle visual differences. Since the attribute descriptions are generated by pre-trained LLM and VQA models, it would be valuable to conduct ablation studies using different quality levels of descriptions (e.g., complete descriptions, noisy descriptions, or no descriptions) to test the model’s robustness and dependency. The study should also consider the potential biases introduced by using pre-trained models for attribute extraction.
6. The paper mainly uses accuracy as an evaluation metric, which may not capture the nuanced performance differences in FGVR tasks. Metrics like confusion matrix analysis could provide more insight, especially for identifying where the model struggles across categories. Furthermore, the visualization section could include quantitative measures to assess the object-category alignment quality, rather than relying solely on visual interpretation. The study should also consider using metrics that are more sensitive to fine-grained differences, such as top-k accuracy or per-class F1 scores.
7. The paper suggests that category names alone lack discriminability within MLLMs. A test could be designed where category names are replaced with varying levels of detailed descriptions (e.g., short versus long descriptions) to analyze the impact of description length and detail on alignment effectiveness. This would verify whether the form of category information expression significantly affects model performance. The analysis should also investigate the impact of different types of textual descriptions, such as those focusing on visual attributes versus functional attributes.

### Questions
In addition to the issues mentioned in Weaknesses, there is another point  about generalization  that needs to be clarified, as follows:
Each MLLM has different levels of perceptual sensitivity to fine-grained details. For example, some models excel in low-level visual feature recognition, while others are better suited for high-level semantic understanding. The proposed approach relies heavily on the specific architecture of Idefics2, particularly the model’s vision encoder, modality connector, and alignment layers. Other MLLMs might not have identical modules or configurations, which could make direct application of the proposed training paradigm challenging.

### Soundness
3

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
5

### Summary
This paper studies the task of Fine-grained Visual Recognition (FGVR). The authors point out the underperformance of modern MLLMs on FGVR and thoroughly explore the cause. The findings suggest that the misalignment between visual objects and category names is the main reason that hinders MLLMs' performance on FGVR. To this end, a novel instruction-tuning framework named Finedeficsfor is proposed to enhance the performance of MLLMs on FGVR by leveraging attribute descriptions. Extensive comparisons, experiments, and ablation studies are conducted across six FGVR benchmarks to validate the effectiveness of the proposed method (model) and its components.

### Strengths
**Before listing the strengths of this paper point by point, I would like to first acknowledge and highlight the research approach employed by this work.**
```
The way this paper conducts its research on improving MLLMs’ capabilities for FGVR demonstrates the authors' rigorous and meticulous scientific approach: identifying the problem (MLLM underperformance in FGVR) → understanding the cause (misalignment between objects and categories) → proposing a solution (leveraging informative attribute descriptions to effectively align visual objects and category names in the representation space of LLMs) → achieving improved performance (surpassing Idefics2 and Qwen-VL-Chat by an average of +10.89% and +9.43%, respectively).

I greatly appreciate this work's research methodology. The carefully designed analysis of MLLMs in FGVR presented in Section 2 will provide valuable insights and guidance for the community and future researchers. These insights may be even more valuable than the proposed method itself and its performance improvements, as they will significantly aid further research in this area. Thank you to the authors for the contribution!
```

**Strengths Point-by-Point:**
- The preliminary exploration of revisiting MLLMs’ capabilities for FGVR shown in Figure 1 is really interesting and intuitive. **I really appreciate this experimental design**. It highlights the core issue—Object-Category Alignment—that hinders MLLMs' FGVR performance.
- The proposed instruction tuning method, consisting of Attribute-Category Contrastive, Object-Attribute Contrastive, and Category-Category Contrastive, is novel and well-designed. The design is both technically innovative and conceptually intuitive.
- The proposed method boosts MLLM performance by a significant margin and consistently outperforms other MLLMs at similar parameter scales.
- Comprehensive ablation studies are conducted to assess the effectiveness of the proposed components.

### Weaknesses
(1) Since the proposed method relies on the attributes obtained via FineR [1] cross-modal chain-of-thoughts prompting,  FineR's FGVR performance should be compared as a baseline in the main experiments. FineR can be consider as improving VLM's FGVR performance by using the attributes as a zero-shot manner. The clustering accuracy used in FineR can be compared with classification accuracy (classification accuracy can be consiered as the perfect case of Hungarian matching used to obtain clustering accuracy). Although an apple-to-apple comparison is hard since FineR consists of multiple agents, this comparison can serve as a good reference to the readers.

(2) In the study of Finedefics in Section 4.3, the influence of construction of Attribute Descriptions should also be examined since it is a crucial component for acquiring per-sample, per-class attribute descriptions. To this end, one experimental design I can suggest is comparing the current construction method with an upper-bound and a baseline on a dataset, such as CUB-200:  
  i) **Upper-bound:** The authors can use CUB-200’s ground-truth attributes, annotated by humans, for instruction tuning.  
  ii) **Tag-based baseline:** Given the class names (e.g., Blue-throated Blue Warbler), the authors can directly prompt an LLM to acquire both useful attributes (e.g., body color pattern) as tags and possible attribute descriptions (e.g., dark blue) for each class’s attribute tags, without using actual image samples. Then, these per-class sets of attribute-description pairs can be assigned to each sample belonging to the class. Since this acquisition process is not conditioned on the training images, it might be noisier. It would be interesting to see how sensitive the model performance is to this upper-bound and baseline.
  
(3) The proposed method requires instruction tuning of MLLMs. Although the main goal is to improve MLLM performance for FGVR, it is still important to investigate whether this FGVR-centric tuning hampers the performance of MLLMs on general QA or common object recognition.

**Minor:**
- At P4#L193: Similarity —> Similarly

**P.S.:** I understand that the rebuttal period provides limited time to address all the concerns and questions raised. For me, the most critical issues are Q1 (no training required) and Q2 outlined above. **If time constraints prevent the authors from addressing all my concerns, please prioritize responding to Q(1) and Q(2), and allocate time to address the other reviewers' major concerns.** It is fine for me if the authors could not address all my concerns and questions (which might take time to train) within the limited time during the rebuttal period. No worries. But it is recommended to include them in the final revision.

### Questions
(1) In the current paper, pet (dogs and cats) images are largely used as experimental subjects in the analysis of MLLMs in FGVR in Section 2. Pets, such as dogs and cats, have a unique characteristic: for the same pet category (or breed), the attribute values (e.g., “Fur Color: Brown”, “Fur Pattern: Dots”) can differ significantly (the so-called large intra-class variance in FGVR). This characteristic also applies to cars (StanfordCar196). However, I wonder: what would be the observation for birds (CUB200) or flowers (Oxford-flower)? For the same bird or flower species, the attribute values are rather fixed—i.e., the same bird species will always have the same body color pattern. In this case, would the observations and conclusions change? Would the category names still have lower discriminability in the representation space?
  
(2) Can the authors provide: 1) qualitative results; 2) failure case analysis? It is necessary to show how the model behaves towards FGVR QA since this is the way it will be used in deployment.

(3) One open question: Why is instruction-tuning MLLMs for FGVR useful and valuable? If the goal is to achieve high FGVR performance, supervising a strong pre-trained model on FGVR datasets can achieve higher performance. Since both paradigms require training, why do we use MLLMs for FGVR?

**Further Suggestions:**
- For the mining of hard negatives for each category, a suggestion is to explore using negatives that are highly similar to the target class but dissimilar in diverse attribute aspects. The current method relies on overall CLIP similarity for decision-making. Note that this is just a suggestion—I understand that it takes time to implement and train the model. The authors are not required to show this during the rebuttal period, but it would be interesting to see.

### Soundness
4

### Presentation
3

### Contribution
4
