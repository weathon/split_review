# DefNTaxS: The Inevitable Need for More Structured Description in Zero-Shot Classification

- Decision: Reject
- Scores: 3, 5, 3, 5

## Abstract
Existing approaches leveraging large pretrained vision-language models (VLMs) like CLIP for zero-shot text-image classification often focus on generating fine-grained class-specific descriptors, leaving higher-order semantic relations between classes underutilised.
We address this gap by proposing Defined Taxonomic Stratification (DefNTaxS), a novel and malleable framework that supplements per-class descriptors with inter-class taxonomies to enrich semantic resolution in zero-shot classification tasks.
Using large language models (LLMs), DefNTaxS automatically generates subcategories that group similar classes and appends context-specific prompt elements for each dataset/subcategory, reducing inter-class competition and providing deeper semantic insight.
This process is fully automated, requiring no manual modifications or further training for any of the models involved.
We demonstrate that DefNTaxS yields consistent performance gains across a number of datasets often used to benchmark frameworks of this type, enhancing accuracy and semantic interpretability in zero-shot classification tasks of varying scale, granularity, and type.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This study concentrates on zero-shot classification utilizing CLIP. To boost performance, it aggregates the class set into various clusters, termed taxonomies, which function as superclasses. By adapting the prompts to the format “{c} which is/has {d}, {g(C,T_c)}”, the model demonstrates enhanced accuracy compared to the simplistic template “a photo of {c}”. Positive results are shown in some experiments.

### Strengths
The work presents a simple and straightforward method that changes the prompts to a more carefully designed prompt using taxonomies.

### Weaknesses
1.  Employing class hierarchy is not groundbreaking in few-shot classification. As highlighted in related work, both CHiLS and D-CLIP utilize hierarchy, along with other studies not cited here, such as [Ren. NIPS 2024].
*  Ren Z, Su Y, Liu X. ChatGPT-powered hierarchical comparisons for image classification[J]. Advances in neural information processing systems, 2024, 36.

2. This paper fails to elucidate crucial details, such as the process of clustering and g(C, T_c). In addition, in experimental evaluation, it appears to compare with lower baselines instead of fair benchmarks. Specifically, the comparison to CLIP's reported performance on ImageNet is not aligned with the best reported results, suggesting a potential issue with the implementation or choice of baselines.

3. The presentation is poor.  Figure 1 occupies excessive space. Additionally, all equations lack equation numbers for reference.

### Questions
1.  The paper fails to elucidate the method for clustering classes, and what's g(C, T_c) exactly. As illustrated in 181, the superset will be refined, how is it refined? In addition, the proposed method employs numerous hyperparameters, such as |c|/10, |C| < 20. How are the hyperparameters decided?  The process appears quite handcrafted and lacks generalization.  

2.  In experimental evaluation, this work achieved an accuracy of 68.03 on ImageNet using ViT B/16.  As shown in [CLIP ICML 2021],  its enhanced version with certain prompting variations can attain an even better result of 68.6. It suggests that the benefits might be obtained through additional prompting templates, such as "an image of {}", etc. More experiments are needed to determine whether the supplementary taxonomy can compensate for CLIP's prompting templates.

### Soundness
1

### Presentation
1

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
This paper proposes to leverage LLMs to generate hierarchical taxonomic sub-categories for a specific category to augment the textual prompt of CLIP to better capture the semantic information in the text prompts as well as refine the alignment between the images and prompts. Experimental results on zero-shot classification validate the effectiveness of the proposed prompting method. Further, fine-grained investigations are conducted on several factors, e.g., the prompt lengths, and prompt formats.

### Strengths
Strengths:
- Fine-grained analysis and investigations are conducted on the different factors of building good semantic prompts, which can offer readers with some practical inspirations.
- The performance gains on some datasets are good.

### Weaknesses
Limitations:

- Does not provide detailed qualitative examples of the proposed prompt contexts.
- The technical novelty of this paper is limited, considering a bunch of existing works on augmenting the CLIP textual prompts. Therefore, the technical differences between this work and other works on LLM-based prompt augmentation methods need to be clarified.
- Lack of baselines for comparisons: two important baselines, CHiLS and MPVR, are mentioned in the related work but are not compared. Besides, there is also a line of missing related works on prompt augmentation with semantic discriminativeness, e.g., S3A[1], Meta-Prompting[2], and LLM Explainer [3].
- Technical issues: (1) It is not guaranteed that the LLM-generated subcategories can satisfy the completeness and disjoint constraints of taxonomy stated in section 3.1. In practice, to what extent these two constraints can be satisfied and what implications will it have on the results needs further investigations and discussions. (2) How many layers of generated taxonomy will there be? If only generate a single layer of subcategories, this work would have high technical similarity with CHiLS; otherwise, more ablations are needed to investigate its benefits.
- Overclaim issue: (1) the motivation of the hierarchical taxonomic prompt starts from the game theory, however, the competition and players in the categorization contexts are not clearly defined. There is no clear and direct relationship between them. (2) The claimed semantic interpretability advantage mentioned in the abstract is not supported since there are neither interpretability results and comparisons nor qualitative examples.
- Presentation issue: The motivation figure 1 covers too large areas. Can add some subtitles to the paragraphs in section 6.3.

### Questions
All my questions are listed in the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose Defined Taxonomic Stratification (DefNTaxS), a novel method that leverages the power of large language models (LLMs) to enhance zero-shot image classification in vision-language models (VLMs) like CLIP. DefNTaxS introduces a hierarchical classification framework by generating subcategories that group semantically similar classes, reducing competition between classes with overlapping features. The authors demonstrate that DefNTaxS sometimes outperforms existing methods across various benchmark datasets, including ImageNet, CUB, Oxford Pets, DTD, Food101, Places365, and EuroSAT and model sizes. Furthermore, they perform some ablation studies highlighting the importance of taxonomic refinement, prompt structure, and incorporating richer descriptors for achieving performance.

### Strengths
- The paper is clear, well-structured, and easy to follow.
- The proposed method demonstrates improved results across all CLIP sizes on certain datasets, such as Oxford Pets and EuroSAT.

### Weaknesses
 - The authors mention WaffleCLIP in the introduction but largely overlook its core finding: that adding additional words around the class name in prompts for CLIP has minimal effect, and previous works ([1],[2]) showing improvements may not provide meaningful benefits.

- The main results (Table 1) indicate some improvements on specific datasets and CLIP model sizes; however, these gains are generally minor and may be due to hyperparameter optimization rather than the method itself. Additionally, the proposed method underperforms compared to others on a substantial portion of the datasets.

- If I understand correctly, Table 2 shows that the method often does not outperform other approaches. For model sizes B/16 and L-14, D-CLIP achieves slightly better results, but the differences are negligible.

- Minor typos: Line 40 - "also" is split; Figure 1 - "visualisation" should be "visualization"; Line 47 - "labelsWhile".

### Questions
- 


[1] Sachit Menon and Carl Vondrick. Visual classification via description from large language models. ICLR, 2023.
[2] Sarah Pratt, Ian Covert, Rosanne Liu, and Ali Farhadi. What does a platypus look like? generating customized prompts for zero-shot image classification.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel method to enhance prompts for zero-shot classification tasks by leveraging a large language model (LLM) to identify taxonomic relationships between classes. By incorporating the taxonomy of a given class into the prompt, the method mitigates competition between semantically similar classes, leading to more accurate classifications. The proposed approach is rigorously evaluated against established baselines across multiple classification datasets.

### Strengths
- The paper is clearly written and easy to follow, with a logical flow that makes the concepts accessible.
- Extensive experimental evaluations provide valuable insights into the method's performance and applicability.
- The proposed method is both simple and well-motivated, making it easy to implement and understand.
- The method demonstrates consistent improvements across the majority of evaluated datasets, showcasing the method's effectiveness.

### Weaknesses
 - The proposed method offers limited novelty compared to existing literature. Specifically, WaffleCLIP already introduces the idea of incorporating one high-level concept into the prompts. If my understanding is correct, the baseline used for comparison seems to only include the random characters/words, without accounting for these high-level concepts. It would be interesting to see how the proposed method compares to WaffleCLIP under these conditions.
- [Minor, subjective] Figure 1 could benefit from a layout adjustment, such as adopting a more landscape-oriented aspect ratio.

### Questions
- CuPL is mentioned as a baseline in Section 4.2, but is never compared against. Could you explain why it was omitted from the experimental comparisons?

- The paper states in two instances that high intra-class similarity contributes to model confusion. My understanding is that high intra-class similarity means that images within the same class are visually alike, which should benefit classification. Could you clarify this point?

- In Section 5.1, it is claimed that the largest improvements occur on datasets with either high-class counts or high intra-class similarity. However, Table 1 shows that the most significant improvements are observed on Oxford Pets and EuroSAT, both of which have relatively few classes and exhibit high inter-class similarity. Did I miss something here, or could you clarify this discrepancy?

- It is claimed that appending taxonomy classes to prompts helps reduce inter-class competition and improves classification accuracy. However, since inter-class similarity typically occurs between classes within the same taxonomy, I would expect that the addition of these taxonomy-based prompts would not necessarily mitigate this issue. Could you provide more clarification on how the method addresses inter-class similarity?

- To gain insights into the above issue, a potential experiment could involve measuring the impact of DefNTaxS on the type of classification errors. Specifically, the experiment would assess how often false predictions occur within the defined taxonomy versus those occurring outside of it.

### Soundness
2

### Presentation
3

### Contribution
2
