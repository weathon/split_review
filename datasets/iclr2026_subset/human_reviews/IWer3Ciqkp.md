## Human Reviewer 1

### Summary
The paper proposes a multi-stage framework for captioning complex urban scenes called PG-VLM. It introduces Hierarchical Panoptic Scene Graph (HPSG) to construct the semantic triplets, which is composed of things, stuff and the spatial connection. Based on that, it uses the T5-Large Decoder to transfer the triplets to paragraphs. The generated captioning is better than baseline like BLIP-2, and the hallucination is mitigated.

### Strengths
- The motivation is easy to understand.

### Weaknesses
- Unreliable experiments. The compared methods are out-of-time. Authors should take more closer MLLM whether open-source or close-source like Qwen series or GPT series into consideration to prove the advantages of PG-VLM.

- Limited contribution. The effect of the data from PG-VLM is unexplored. It's better to supplement the experiments like panoptic segmentation, which would strengthen the contribution of PG-VLM. The current version is more like a semi-finished research.

-Poor presentation. The presentation is poor. Like the missed reference in line 308 and line 368 for NSDR. The training detail of Teacher LLM is missed.

### Questions
- NRDS relies on the CLIP. What is the difference between NRDS and other metrics like CLIP-score or CIDEr?

- How to train teacher LLM and T5-Large Decoder? How to get the high quality supervision?

- The triplets are constructed with all the objects in the scene, the number of combination is large. Is there any filter policy to mitigate or refine the triplets?

### Soundness
2

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes PG-VLM, a multi-stage vision-language framework that introduces a symbolic bottleneck between visual perception and language generation. By converting panoptic segmentation outputs into a Hierarchical Panoptic Scene Graph and structured triplets before paragraph generation, it enhances spatial grounding, factual accuracy, and narrative coherence, outperforming prior VLMs on the Cityscapes dataset while reducing hallucination.

### Strengths
1. The proposed multi-stage pipeline (segmentation → scene graph → triplets → text) is well-motivated and improves interpretability and controllability.
2. The symbolic bottleneck effectively reduces hallucination and strengthens spatial reasoning, as evidenced by improved CIDEr, SPICE, and NRDS scores.
3. The introduction of NRDS provides a more nuanced way to assess factual and spatial alignment in generated descriptions.

### Weaknesses
1. The paper’s writing could be improved for clarity and consistency. Certain sections (e.g., Section 6.3) contain citation or formatting inconsistencies, and the overall structure would benefit from clearer transitions and more careful editing to enhance readability.
2. The paper mainly presents quantitative metrics without sufficient qualitative comparisons. Including more visual and textual examples side-by-side with baselines would help readers better understand the qualitative strengths of the proposed method.
3. The experimental comparisons focus on earlier LVM such as BLIP-2, LLaVA, and SpatialVLM. Evaluating against more recent models (e.g., Qwen-VL, InternVL) would provide a more complete and up-to-date assessment of performance.
4. While the multi-stage design is conceptually clear, most components (panoptic segmentation, scene graph construction, and T5-based generation) rely on existing architectures. The novelty lies mainly in their integration rather than in new algorithmic advances, which somewhat limits the methodological contribution.
5. The study briefly mentions human evaluation but does not detail the evaluation protocol, number of raters, or inter-rater reliability. Without this information, it’s difficult to judge the statistical validity of human assessment results.

### Questions
Please refer to weakness.

### Soundness
2

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper designs a new framework that uses an intermediate graph structure to improve the accuracy of spatial information in VLM predictions.

### Strengths
The main idea makes sense. The experiments are small, but they still show that their approach, using a smaller T5 model, managed to beat larger models.

### Weaknesses
This paper has two very significant flaws.
1. First, the writing quality is poor and suggests a rushed submission. The figures are crude, typos are frequent (like line 307), and the text is confusing. They even forgot to describe the loss function, which is a critical omission.
2. Second, the experiments are far too small to be convincing. The conclusions cannot be trusted because the scale is inadequate: the relation set is tiny (12 categories), the testset is only 50 images, and the training set is just 5000 images from one source. This is not enough to prove the method's generalizability.

Besides, I think there's another major problem: the paper relies on similarity-based metrics (e.g., BLEU), which are ill-suited for this task. These metrics fail to capture the factual correctness of critical spatial information, which is the core contribution. The reported gains may simply reflect overfitting to linguistic patterns rather than true improvements in spatial reasoning. A more robust, fact-centric evaluation is required.

### Questions
Please refer to the issues detailed in the Weakness part.

### Soundness
2

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper approaches the task of detailed image captioning on the Cityscapes dataset. The proposed model first builds a graph from panoptic segmentation outputs and their spatial positioning relationships. From graph triplets, a T5 generates the final detailed caption for the urban scene. This paper presents results on this task using pseudo-labels and compares them to those of other state-of-the-art image captioning models.

### Strengths
This review evaluates the paper's quality based on the following criteria: task relevance, related work, technical novelty, technical correctness, experimental validation, writing and presentation, and reproducibility. Each aspect is discussed and highlighted as a strength or a weakness in the sections below.
-    **Relevance of the task:**  Detailed Image Captioning is a highly relevant problem for the machine learning community.

### Weaknesses
-    **Reproducibility and Implementation Details:** It is not indicated whether the source code will be released, and it's not included as part of the submission.
-    **Related Work and Technical Novelty:** The Related Work section does not adequately contextualize the contributions. It is not clear how the proposed method addresses the limitations of current detailed image captioning methods.
-    **Writing and Presentation:** This paper is not easy to read. It lacks sections on the metric formulation. Its organization does not allow the reader to adequately understand the problem/motivation, its prevalence in current state-of-the-art methods, the proposed methodology, how this methodology solves the research gap, and finally, how well the experiments support it.
-    **Experimental Validation and Technical Correctness:** The empirical validation of this paper is not clear from the dataset used. According to the paper description (Lines 240–244), it utilizes the panoptic annotations of Cityscapes for training and pseudo-labels for the detailed image captioning task, generated using the same T5 model. Are these pseudo-labels also used for evaluation and comparison with previous state-of-the-art methods? This experimental choice will result in an obviously biased validation towards the outputs of the pretrained model, which puts the proposed method at an evident advantage against any other model not based on this generator.

### Questions
1.	Will the source code and pretrained models be released to support reproducibility? If so, what is the reason for not including them in the supplementary material?
2.	How does the method improve upon or differ from existing detailed image captioning approaches?
3.	Can the paper clarify the motivation, the gap in prior work, and how the method addresses it?
4.	What metrics are used for evaluation, and can their formulation be clarified?
5.	Are the pseudo-labels used for both training and evaluation? If so, how is evaluation bias avoided?
6.	How does the use of pseudo-labels affect fairness in comparison with other models?

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
0

### Confidence
4