# MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
The capability to process multiple images is crucial for Large Vision-Language Models (LVLMs) to develop a more thorough and nuanced understanding of a scene. Recent multi-image LVLMs have begun to address this need. However, their evaluation has not kept pace with their development. To fill this gap, we introduce the Multimodal Multi-image Understanding (MMIU) benchmark, a comprehensive evaluation suite designed to assess LVLMs across a wide range of multi-image tasks. MMIU encompasses 7 types of multi-image relationships, 52 tasks, 77K images, and 11K meticulously curated multiple-choice questions, making it the most extensive benchmark of its kind. Our evaluation of 24 popular LVLMs, including both open-source and proprietary models, reveals significant challenges in multi-image comprehension, particularly in tasks involving spatial understanding. Even the most advanced models, such as GPT-4o, achieve only 55.7\% accuracy on MMIU. Through multi-faceted analytical experiments, we identify key performance gaps and limitations, providing valuable insights for future model and data improvements. We aim for MMIU to advance the frontier of LVLM research and development, moving us toward achieving sophisticated multimodal multi-image user interactions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Multimodal Multi-image Understanding (MMIU) benchmark, a comprehensive evaluation suite designed to assess Large Vision-Language Models (LVLMs) across a wide range of multi-image tasks. MMIU encompasses seven types of multi-image relationships, including semantic, temporal, and spatial aspects, and consists of 52 tasks, 77K images, and 11K meticulously curated multiple-choice questions. The authors evaluate 24 popular LVLMs, including both open-source and proprietary models, on the MMIU benchmark and identify significant challenges in multi-image comprehension, particularly in tasks involving spatial understanding. Through multi-faceted analytical experiments, they provide valuable insights for future model and data improvements.

### Strengths
1. The paper is well-organized and clearly presented, with a detailed background section, methodological descriptions, and experimental results. 
2. MMIU is the first benchmark to comprehensively evaluate the performance of LVLMs on multi-image tasks. It covers a wide range of multi-image relations and tasks, including semantic, temporal and spatial relations, as well as various image modalities.
3. The design of the MMIU allows it to be easily extended to new multi-image tasks and image modalities. This makes it a useful tool for future research.

### Weaknesses
1. MMIU is large in scale, including 77,659 images and 11,698 multiple-choice questions. This may require a lot of computing resources to run experiments and perform analysis.
2. The paper shows that multi-graph understanding requires the capabilities of semantic, temporal and spatial relations. However, most current models do not model the latter two capabilities in the pre-training phase, which can lead to a lack of practical significance in the comparison of various models

### Questions
1. The authors mention how they collected and standardized the data to create the MMIU. However, they do not provide detailed information about the data collection process, such as which data sources and data processing techniques they used. 
2. The strong capability in single-image understanding is the foundation of multi-image comprehension. As we know, the ability of single-image understanding comes from powerful language models, such as MMMU benchmark, can you give some performance of pure language models.
3. I hope to provide some model performance that add interleave data or video data in the pre-training or post-training stage.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces MMIU, a benchmark to evaluate a LVLM's capability of understanding information when given multiple images simultaneously. MMIU covers a wide range of established cognitive tasks on semantics and compositionality in fine categories.

### Strengths
This work offers meticulous details to the design of the benchmark. The authors have shown great effort in the data curation process while following a logical main plot line. I particularly find the results that show the LVLMs pre-trained with only single-image content may outperform their multi-image counterparts of great research insight.

### Weaknesses
Please find my two major concerns down below:

1. My bigger issue about this paper is regarding the presentation of experimental results. **I find the benchmarking results are presented in a very cumbersome way.** Table 3 is the best example to illustrate this major weakness. The authors put in all the fine-category results by every single subtask. Although the comprehensiveness is appreciated, such overkill-style of presentation makes it hard to follow, so that we readers may not obtain a clear intuition about where and how well each baseline model thrives or lags against one another. This 'way-too-much-details' problem is also present in Figure 4 of the task maps. I highly recommend the authors show more summarized performance on the coarse categories, such the 3 big ones of Semantic/Spatial/Temporal in the main text, while leaving the finer categories in the Appendix.

2. **Potential position bias in the unanswerable set is unaddressed.** . MMIU's QA test cases are all multiple-choices. However, according to Zheng et al, 2023, the position bias is a significant issue when constructing benchmarks for evaluating LLMs (esp. on non-GPT methods). Basically speaking, the position bias will be prominent if the 'None of the above' option for the unanswerable set is always Option D, while known LLMs tend to favor the first option. This means models intend to give away deflated results shown in Table 12 for the unanswerable tasks. Have the authors tried shuffling the option orders? I am not seeing particular evidence for addressing the position bias in Section 3.2 as supposed to be.


### Questions
Please find my concerns and suggestions in the Weakness section above.

Typo: Line 1389, Table reference is missing.

Update (Nov 23): Raising my ratings according to the authors' response

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents MMIU, a comprehensive benchmark designed to evaluate large vision-language models (LVLMs) on multi-image tasks, addressing limitations in existing single-image-focused evaluations. MMIU includes 52 tasks spanning seven image relationship types, such as semantic, spatial, and temporal, with a total of 77,659 images and 11,698 multi-choice questions.

### Strengths
- Originality: The paper introduces a novel benchmark, MMIU, specifically designed for evaluating large vision-language models (LVLMs) on multi-image tasks. This fills a critical gap, as existing benchmarks predominantly focus on single-image understanding. The inclusion of diverse image relationships—semantic, spatial, and temporal—is a creative approach that highlights areas where LVLMs struggle, especially in tasks requiring complex multi-image reasoning.

- Quality: The experimental methodology is robust and thorough. The authors test 24 popular LVLMs, both open-source and closed-source, providing a comprehensive view of current capabilities. Their use of multi-dimensional analysis tools, including supervised fine-tuning (SFT) and task maps, provides depth to the evaluation, highlighting model strengths and weaknesses across various task types. This approach demonstrates rigorous scientific methodology and enhances the reliability of the conclusions drawn.

- Significance: MMIU has high potential impact for the vision-language research community, particularly given the increasing relevance of multi-image tasks in real-world applications (e.g., video understanding, 3D reasoning). By providing a benchmark with a broad set of tasks and image relationships, MMIU allows for a more nuanced understanding of LVLMs’ strengths and limitations. The insights from this benchmark can guide future LVLM improvements, pushing the field towards more sophisticated models that handle complex visual contexts and multi-image data effectively.

### Weaknesses
 - Reliability of GPT-4o-Generated Data: Although MMIU’s large dataset is a significant contribution, its reliance on GPT-4o for generating questions and responses raises concerns about potential bias. Given that GPT-4o itself may have inherent preferences or limitations in multi-image reasoning, this could inadvertently affect the construction of questions and answer choices. Additionally, if GPT-4o has limitations in multi-image reasoning (as noted by the authors), this brings into question whether the generated tasks and responses are fully reliable. While human verification can ensure the accuracy of correct answers, it may not catch subtle model biases embedded in the answer choices, potentially skewing results. A clearer discussion or additional safeguards against GPT-4o’s influence on task design would improve the benchmark’s objectivity and robustness.

- Limited Discussion on Practical Applicability: While MMIU’s tasks are inspired by real-world applications, the paper could strengthen its relevance by addressing practical implications more explicitly. For instance, the authors could highlight specific MMIU tasks that align with high-stakes applications—such as high-level reasoning and long-term memory tasks relevant to autonomous driving, surveillance, and medical imaging. Connecting benchmark tasks to these domains would make the work more relatable and impactful for applied researchers. Additionally, discussing how MMIU might be adapted or extended to cover emerging application areas would further enhance the benchmark’s future-facing value and adaptability.

### Questions
- Clarification on GPT-4o’s Role in Data Generation: Could you elaborate on how GPT-4o’s limitations in multi-image reasoning are managed during data generation? Specifically:

- How do you ensure that GPT-4o’s generated questions and answer choices are unbiased and accurately reflect the task complexity, given that it might have inherent reasoning limitations?

- To what extent was human verification involved, especially in preventing GPT-4o's possible biases from influencing the multiple-choice options? Further clarification on this process would strengthen confidence in the benchmark’s objectivity.

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
3

### Summary
The paper introduces the Multimodal Multi-Image Understanding (MMIU) benchmark, which evaluates large vision-language models (LVLMs) on complex multi-image tasks, including spatial, semantic, and temporal relationships. Covering 52 task types with 77,000 images and 11,000 curated questions, MMIU is a comprehensive benchmark that reveals significant challenges, particularly in spatial and temporal tasks, for leading models such as GPT-4o.

### Strengths
1. Multi-image understanding is indeed a meaningful and impactful problem within multimodal research, this paper effectively addresses this need by establishing MMIU, a benchmark specifically designed to evaluate large vision-language models (LVLMs) across diverse multi-image tasks.

2. The presentation is clear and well-structured, figures and tables are effectively used to enhance understanding.

### Weaknesses
1. The benchmark evaluates numerous LVLMs but could benefit from deeper comparisons across models with distinct visual encoding strategies. This would provide more specific insights into how different architectures impact performance on complex spatial and temporal tasks, which is particularly valuable for the multi-image context.

2. While MMIU successfully identifies gaps in LVLM performance, the paper does not sufficiently explore or propose alternative methods to address these gaps, such as novel training techniques or architectural adjustments. This limits the benchmark’s practical utility for guiding future model development.

### Questions
This paper is overall good, it would be better to present deeper analysis on model performance variations across specific multi-image relationships, particularly spatial, temporal, and high-level semantic tasks. Currently, the analysis highlights general performance trends but could benefit from a more granular examination of how and why certain models excel or struggle with specific relationship types.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The article introduces the MMIU benchmark for evaluating large vision-language models on multi-image tasks. It includes various tasks and a large dataset with over 77K images and 11K questions. The study finds that even advanced models struggle with complex multi-image understanding

### Strengths
1、Comprehensive Evaluation: The MMIU benchmark provides a thorough assessment of LVLMs by covering a wide range of multi-image tasks and relationships, making it one of the most extensive benchmarks in this domain.

2、Diverse Task Coverage: It includes a variety of tasks that require different cognitive processes, from low-level visual perception to high-level reasoning, offering a holistic view of a model's capabilities.

3、Insightful Analysis: The article presents detailed analytical experiments that identify key performance gaps and limitations in current models, providing valuable insights for future research and development in the field of multimodal AI.

### Weaknesses
1、Typo: 173 line multimodal large language models (LVLMs), abbreviation error.

2、The details of writing can be further polished, such as using Fig. in some places, Some places use Figure

### Questions
1、Are there any duplicates between the samples in your dataset and the current multi graph dataset?

2、Why do models without multi-imgae SFT perform better than those with multi-imgae SFT on your benchmark?

### Soundness
3

### Presentation
3

### Contribution
3
