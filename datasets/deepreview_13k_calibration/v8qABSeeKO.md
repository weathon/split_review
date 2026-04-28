# MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 5, 6

## Abstract
Knowledge editing techniques have emerged as essential tools for updating the factual knowledge of large language models (LLMs) and multimodal models (LMMs), allowing them to correct outdated or inaccurate information without retraining from scratch. However, existing benchmarks for multimodal knowledge editing primarily focus on entity-level knowledge represented as simple triplets, which fail to capture the complexity of real-world multimodal information. To address this issue, we introduce MMKE-Bench, a comprehensive **M**ulti**M**odal **K**nowledge **E**diting Benchmark, designed to evaluate the ability of LMMs to edit diverse visual knowledge in real-world scenarios. MMKE-Bench addresses these limitations by incorporating three types of editing tasks: visual entity editing, visual semantic editing, and user-specific editing.  Besides, MMKE-Bench uses free-form natural language to represent and edit knowledge, offering a more flexible and effective format. The benchmark consists of 2,940 pieces of knowledge and 7,229 images across 110 fine-grained types, with evaluation questions automatically generated and human-verified. We assess five state-of-the-art knowledge editing methods on three prominent LMMs, revealing that no method excels across all criteria, and that visual and user-specific edits are particularly challenging. MMKE-Bench sets a new standard for evaluating the robustness of multimodal knowledge editing techniques, driving progress in this rapidly evolving field.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a benchmark for knowledge editing in multimodal large models, specifically targeting knowledge represented in free-form natural language. The benchmark focuses on tasks such as visual entity editing, visual semantic editing, and user-specific editing. The paper provides a detailed description of the data collection and construction process for this benchmark. Various model editing methods were evaluated on this benchmark using models like BLIP-2, MiniGPT-4, and LLaVA 1.5, revealing limitations in existing approaches.

### Strengths
1. The benchmark proposed in this paper uses knowledge represented in free-form natural language, making it more applicable to real-world scenarios. In addition to traditional visual entity editing, the benchmark incorporates visual semantic editing and user-specific editing, allowing for a more comprehensive evaluation of model editing capabilities.
2. The paper provides a detailed description of the dataset construction process, offering valuable insights and methodologies for data collection and structuring.
3. The experiments conducted on the benchmark cover a wide range of model editing methods across different types of knowledge editing tasks, resulting in an extensive and insightful evaluation.

### Weaknesses
1. I’m not sure if the workload is sufficient. If this were solely a Dataset & Benchmark Track submission, the workload would be appropriate. However, as a long paper submission to ICLR, it may require additional technical contributions. For instance, adding theoretical analysis to explain why existing methods perform poorly in multimodal knowledge editing could provide new perspectives for improving this area. Therefore, it’s recommended to include an in-depth analysis on why current methods underperform in certain aspects relevant to the proposed benchmark. It is suggested to provide related theoretical analysis or technical contributions that you believe would enhance the paper's suitability for ICLR. 

2. I didn’t find evidence in the experimental or case study sections demonstrating the necessity of this benchmark. This is not to question the value of your work, but providing examples would strengthen the case. Additionally, clarifying which scenarios would particularly benefit from using this benchmark for evaluation would be helpful. It’s recommended to add more evidence highlighting the ‘differences’ and ‘necessity’ of this benchmark. I suggest you provide comparative analyses with existing benchmarks or specific real-world scenarios where this benchmark would be particularly valuable.

### Questions
1. In line 776, “counterfactual editing” is mentioned. According to the description in lines 776-781, modifying certain facts constitutes counterfactual editing. Is this definition accurate?
2. The case study in Section 5.3 could include more analysis. Figure 5 and Figure 6 only present a relatively simple entity editing example (person-related information) and do not showcase complex cases of visual semantic editing or user-specific knowledge editing. It’s recommended to select representative and challenging cases or specific types of cases in visual semantic editing or user-specific knowledge editing. 
3. The superiority of IKE has been demonstrated in many previous works. What new perspective does your benchmark provide? Section 5.3 only states that IKE performs better than FT-LLM without explaining why IKE has stronger generalization and transferability. It would be helpful to explain the reasons for the performance differences across methods based on the proposed benchmark. It is suggested to provide a detailed analysis of how IKE's performance on this new benchmark differs from its performance on previous benchmarks, and what these differences reveal about the nature of multimodal knowledge editing tasks.
4. This benchmark is designed to uncover issues that other benchmarks cannot detect. Could you provide some examples or data to demonstrate that your benchmark is indeed more challenging and more valuable for improving models compared to other benchmarks?

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
3

### Summary
This paper introduces MMKE-Bench, a multimodal knowledge editing benchmark dataset aimed at addressing the current gap in resources for evaluating large multimodal models (LMMs) in knowledge editing tasks. MMKE-Bench is largely constructed using counterfactual samples to enhance the robustness of model evaluation and to examine their ability to perform knowledge editing across varied and challenging scenarios. The dataset includes three types of tasks: visual entity editing, visual semantic editing, and user-specific knowledge editing. Each task is represented through free-form natural language descriptions combined with images, generated by large language models (LLMs) and verified through human annotation to ensure consistency. The paper evaluates several state-of-the-art multimodal models, including BLIP-2, MiniGPT-4, and LLaVA-1.5, providing insights into the strengths and limitations of current models across different knowledge editing tasks.

### Strengths
(1) Diverse Task Setup: MMKE-Bench covers three distinct knowledge editing tasks, from entity-level editing to more complex user-specific knowledge editing. This provides a comprehensive tool for evaluating multimodal models' ability to update knowledge and handle personalized information.

(2) Free-Form Natural Language Descriptions: Unlike traditional triple-based representations, this benchmark uses natural language descriptions to represent knowledge items, enabling models to engage in editing tasks in a more realistic scenario. The free-form descriptions combined with image data make the tasks closer to the complexity of real-world semantics.

(3) Extensive Evaluation Using State-of-the-Art Multimodal Models: The paper evaluates MMKE-Bench on prominent multimodal models such as BLIP-2, MiniGPT-4, and LLaVA-1.5. These models represent the cutting edge in the multimodal field, making the experimental results widely relevant and reflective of current model capabilities in knowledge editing tasks.

(4) Systematic Experimental Analysis: The paper provides a thorough evaluation of various existing knowledge editing methods, including FT-LLM, KE, MEND, SERAC, and IKE, offering a comprehensive performance baseline for each task type. This analysis provides valuable insights into how different methods perform across the tasks presented in MMKE-Bench.

### Weaknesses
 (1) Figures 1 and 2 Could Benefit from Improved Clarity and Accessibility: Figures 1 and 2 could be refined to enhance clarity and accessibility for a broader audience. In Figure 1, the example used is soccer-related, which may not be immediately understandable to readers unfamiliar with the sport. A more universally recognizable example, such as common objects or activities, could make the data construction process clearer. For Figure 2, the visual design could better distinguish the four dataset construction steps; currently, it’s difficult to determine which modules belong to each step. Using distinct colors, numbering, or borders to separate steps would help readers follow the process more intuitively.

(2) Limitations of Counterfactual Data for Real-World Applications: The counterfactual approach used to construct MMKE-Bench may lead to a distribution that differs from real-world data. While counterfactual samples aid in testing robustness, they represent hypothetical rather than naturally occurring scenarios. As a result, models fine-tuned on this dataset might learn patterns specific to these counterfactual cases, potentially reducing their effectiveness in real-world knowledge editing tasks. A comparison of model performance on both counterfactual and real-world data would provide valuable insights. Furthermore, the method of generating counterfactuals using LLMs may introduce biases or inconsistencies that are not present in real-world data, which could skew the evaluation results.

(3) Lack of Empirical Analysis on the Impact of Human Verification: The paper mentions that human verification was conducted to improve the consistency of LLM-generated descriptions, but it does not provide examples or quantitative comparisons to illustrate the impact of this verification process. Including a before-and-after analysis would strengthen the case for the added value of human verification. Specifically, it would be beneficial to understand the types of errors that were corrected by human verification and the frequency of these corrections. Without this information, it is difficult to assess the true impact of human intervention on the dataset's quality.

### Questions
(1) Would it be more beneficial to construct knowledge editing samples using incremental, real-world updates? Although challenging, creating samples based on real-world updates, such as player transfers or recent match results sourced from news articles, could enhance dataset relevance. Using real, evolving information would help models learn to handle dynamic knowledge updates and might improve their applicability in practical knowledge editing scenarios.

(2) What impact did human verification have on the LLM-generated descriptions? An analysis or examples of descriptions before and after human verification would help demonstrate how much human intervention improved the dataset's consistency and accuracy.

(3) Is there a comparison of Visual Entity Editing data quality between MMKE-Bench and prior datasets (e.g., MC-MKE, VLKEB)? While Table 1 highlights MMKE-Bench’s increased task diversity with the addition of Visual Semantic Editing and User-Specific Editing, it would be useful to understand how MMKE-Bench compares to previous datasets in terms of data quality for Visual Entity Editing. Such a comparison could clarify whether MMKE-Bench offers improvements in data quality alongside task diversity.

(4) For additional questions, please refer to the Weaknesses section.

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
4

### Summary
This work focuses on knowledge editing in large multimodal models and introduces a new benchmark. It presents three distinct types of editing tasks: visual entity editing, visual semantic editing, and user-specific editing, using free-form natural language as input data for these edits. The benchmark also diverges from previous versions by removing the T-Gen test and adding a T-Rel test. The evaluation includes five editing methods across three large multimodal models (LMMs), effectively validating the benchmark's dataset.

### Strengths
The use of free-form natural language as input for knowledge editing tasks is a notable strength, enhancing flexibility and making the approach adaptable. The clarity of the writing aids comprehension, and the experimental setup is well-documented. Additionally, the benchmark spans diverse data sources and entity types, allowing for broad applicability across different tasks.

### Weaknesses
There is some overlap between visual entity editing and visual semantic editing, as both tasks involve understanding image content, which could blur the distinction between these editing types. Additionally, the user-specific editing scenario may lack practicality. In real-world applications, database or memory-based search might be more effective than training user-specific information for each user to achieve personalization in LLMs or LMMs.
Regarding the T-Loc test, there’s room for improvement. The results are near 100, suggest that the randomly sampled T-Loc questions are relatively easy for methods such as SERAC, FT-Alignment, and MEND. Introducing more challenging cases could enhance the evaluation’s robustness. For instance, collect similar but harder test cases, either through web crawling or using LLM-generated content (e.g., from GPT) and verify them. This could improve the test’s effectiveness.

### Questions
As mentioned in the weaknesses, the similarity of editing visual entity and semantic editing, the user-specific editing scenario and T-Loc test warrant further exploration.

Given the modest amount of training data, is the dataset volume adequate for methods that require training, like serac or mend? Additionally, how is the IKE method adapted to LMM editing? Which examples are used in context? Is target knowledge incorporated within the context, and do you include image-based examples in this context?

In Section 5.2.1, there is a claim that “5) Modern LMMs excel in producing and applying edited knowledge. For reliability, generalization, and portability evaluations, LLaVA-1.5 outperforms BLIP-2 and MiniGPT-4. This improved performance can be attributed to its larger model size and better instruction-following capability.” This raises two questions: First, is LLaVA-1.5 indeed larger than MiniGPT-4, as both use a 7B LLM, and MiniGPT-4's vision encoder appears larger? Second, this statement is not directly related to the benchmark’s core focus, which is to compare editing methods rather than models.

In Section 5.2.2, further clarification is needed regarding the meaning of “user number” and “allowed maximum items.” Additionally, what is the precise gap between editing and testing in user-specific editing, and why is the gap in the two visual editing tasks similar (1, 3, 6, 10) without larger gap?

Typo:
Figure 2, bottom-right: "G-Rel."
Table 2: "Entity Entity Editing"
Table 6: SERAC GAP 3 T-Rel, missing decimal point

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This research investigates knowledge editing within large multimodal models, introducing a novel benchmark for evaluation. It defines three specific editing tasks: modifying visual entities, altering visual semantics, and implementing user-specific adjustments, all using natural language as the input format. The benchmark is validated through an assessment of five different editing techniques across three large multimodal models, effectively confirming the dataset's applicability.

### Strengths
Utilizing free-form natural language as input for knowledge editing tasks stands out as a key advantage, offering greater flexibility and adaptability to various contexts. The data collection process is robust and comprehensive, and the benchmark supports both individual and sequential editing tasks.

### Weaknesses
The training dataset size seems to be small, which might not be enough for mend/ serac that need training. This could potentially lead to lower performance of such methods.

There is potential to enhance the T-Loc test. The current results, which are close to 100, indicate that the randomly selected T-Loc questions may be relatively simple for existing methods. Strengthening the evaluation could involve introducing more challenging cases. For instance, given that GPT was used in data collection, generating analogous but more difficult test cases and validating them could increase the test's effectiveness and robustness.

The division of the three tasks lacks clarity. Both visual entity editing and visual semantic editing require image comprehension and retention of the target knowledge provided in the text. While they may involve different data sources, they essentially fall under the same task, visual question answering. Similarly, user-specific editing could be seen as an application scenario, but it still aligns with the core task of VQA, making no real difference in “task type.” 

Additionally, I question about if this user-specific editing approach is practical. In real-world applications, creating personalized databases for each user might be more efficient and effective than modifying the model or embedded knowledge directly.

And the task generalization might not be persuasive using only one case. If you want to prove this, more comprehensive experiments and evaluations should be conducted.

### Questions
As mentioned in the weaknesses.

From figure 1, there is no T-Gen test in MMKE-Bench, and you add a T-Rel test. Why do you make this change?

Additionally, how do you adapt each method to the lmm editing?

Figure 4: why I-Gen not evaluated for MMEdit?

Section 5.2.2 requires additional clarification on the terms “user number” and “allowed maximum items.” Further, what about the mend method in your sequential editing setting? And are the gaps substantial enough for the test? In LLM knowledge editing studies and the referenced vlkeb work, this gap can be larger, reaching 100 or more.

The analysis in line 425-426 only explains possible reason for serac, leaving out mend.

Line 450, “visual knowledge” can be ambiguous, and the reliability seems to be not lower as stated.

Line 466, how do you draw the conclusion “parameter-based methods are better at applying edited knowledge to new contexts”?


Writing issue:

double quotes in line 324-327 and elsewhere: please pay attention to how to type correct left quotation mark in latex.

Figure 1: what is the difference between original and editing knowledge of user-specific editing? They are same that lead to confusion, which can be improved for btter clarity.

Figure 2: Should the "G-Rel." change to “T-Rel”? And the two question in the last box (bottom right) are same. And placing “hint” there can be confusing, as if the hint itself is part of the input.

Line 355: you use “MLLMs” here, but in other places, you use LMMs

Table 2: "Entity Entity Editing"

Table 6: missing decimal point in SERAC results, GAP 3 T-Rel column

### Soundness
2

### Presentation
2

### Contribution
2
