# CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The ability to acknowledge the inevitable uncertainty in their knowledge and reasoning is a prerequisite for AI systems to be truly truthful and reliable. In this paper, we present a taxonomy of uncertainty specific to vision-language AI systems, distinguishing between epistemic uncertainty (arising from a lack of information) and aleatoric uncertainty (due to inherent unpredictability), and further explore finer categories within. Based on this taxonomy, we synthesize a benchmark dataset, CertainlyUncertain, featuring 178K visual question answering (VQA) samples as contrastive pairs. This is achieved by 1) inpainting images to make previously answerable questions into unanswerable ones; and 2) using image captions to prompt large language models for both answerable and unanswerable questions. Additionally, we introduce a new metric confidence-weighted accuracy, that is well correlated with both accuracy and calibration error, to address the shortcomings of existing metrics. Despite the recent rapid progress in vision-language models (VLMs), evaluations on our benchmark show that they perform poorly in uncertain scenarios. Further experiments demonstrate that supervised fine-tuning with CertainlyUncertain enhances the performance of VLMs, and reduces the calibration error. These improvements extend beyond our benchmark to existing refusal-oriented datasets and show positive results on reducing hallucinations, while maintaining performance on standard VQA benchmarks. Our work underscores the importance of addressing uncertainty in vision-language AI systems to improve their reliability and trustworthiness in real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce a benchmark called CertainlyUncertain, consisting of 178K VQA pairs. This dataset consists of both answerable and unanswerable questions, where the correct answer to the latter is "I don't know". They introduce a taxonomy of five types of uncertainty, and generate questions via two methods: either caption-based prompting with GPT4 or inpainting of salient image regions for answerable questions. They show that existing VLMs do not perform well on the task; however, fine-tuning improves performance and also improves performance on other datasets that are refusal-based or test hallucinations. They also introduce a metric for measuring confidence-aware accuracy.

### Strengths
The paper focuses on an important capability of ML models, the capacity to express uncertainty when appropriate. They introduce a large and diverse dataset to explicitly assess uncertainty of VLMs in a VQA setting. Different sources of uncertainty are nicely categorized into a taxonomy, and questions are collected according to this taxonomy. Moreover the same image contains both answerable and unanswerable questions in their dataset, providing a nice contrastive setup. 

They benchmark SoTA VLMs against their dataset, and show that fine-tuning these models on their dataset leads to better performance on both their dataset and on other relevant datasets (refusal-based, hallucinations). Experiments seem reasonably thorough across different datasets and metrics are broken down for different types of uncertainty.

### Weaknesses
Dataset quality is a concern I have. As noted by the authors, this is a concern with automatically-generated datasets. They note that 20% of the samples were filtered out on a quality check, which is a reasonably high number. Was a similar filtration process applied to the training set for the extraneous questions, or were those not filtered? Also were the questions generated from image captions also quality-checked? I would like to understand more about the 93% number they quote in Ln 239.

Some qualitative analysis in the results would be helpful, e.g. showing how training on the dataset causes the model to perform better on questions that involve uncertainty, compared to the base model. The lack of qualitative examples makes the results difficult to read and it would be good to add such examples.

Clarity of the paper could be improved significantly. For example, certain terminology such as the LAVE method is introduced without proper explanation, although it is important to understand how this works. More explanation on the hallucination-based benchmarks would be helpful. The experiments section is quite dense with large tables -- as mentioned above, some qualitative results would be helpful. It is unclear whether the entirety of Table 4 needs to be presented or whether some numbers can be moved to the Appendix. 

I think the paper would benefit from a background section, which explains some key concepts such as VLMs and SoTA models, common metrics used for evaluating their uncertainty capabilities, fine-tuning strategies that you use in the experiments section, anything else that is important. Related work is dense and would also benefit from better explaining some of the previous relevant datasets and work on multimodal uncertainty or refusal that has been explored. These could be explained more clearly.

Lns 195-196 vs. 198-200: It is not clear whether the questions are from the original dataset and only the images are perturbed, or whether the questions are generated from GPT4-V after the image perturbation has been applied.

### Questions
Most of my questions/comments are elaborated on in the above section. Please take note of my comments on dataset quality and clarity/reorganization.

### Soundness
3

### Presentation
2

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
The work aims to address the uncertainty in vision-language models (VLMs). They first present a taxonomy of uncertainty resulting from a lack of information or inherent unpredictability. They then synthesize a benchmark dataset named CERTAINLYUNCERTAIN, and introduce a new metric, confidence-weighted accuracy. Besides, they further demonstrate that supervised fine-tuning with CERTAINLYUNCERTAIN enhances the performance of VLMs, and reduces the calibration error.

### Strengths
-	The work aims to address the important problem of uncertainty in VLMs. An interesting and valuable benchmark is proposed. 
-	The work shows clear experimental evidence that demonstrates the improvements from fine-tuning with the proposed dataset.
-	The experimental results provide clear evidence of the benefits of the proposed dataset. The fine-tuned model with CERTAINLYUNCERTAIN shows performance gains and improved calibration.
-	The paper is well-written with clear presentation.

### Weaknesses
-	While the process of deriving contrastive instances in CERTAINLYUNCERTAIN from image and caption sources is clearly described, it is unclear how those instances are classified into the predefined uncertainty types (i.e., Epistemic, Aleatoric). Specifically, the criteria for distinguishing between epistemic uncertainty (due to lack of knowledge) and aleatoric uncertainty (due to inherent randomness) in the generated question-answer pairs is not well-defined. This lack of clarity makes it difficult to assess the validity of the uncertainty type assignments.
-	The dataset shows bias: a high proportion of QA pairs is categorized as “extraneous awareness”. This imbalance could lead to models being over-optimized for this specific type of uncertainty, potentially hindering their ability to generalize to other types of uncertainty. The impact of this bias on the overall performance and robustness of the models needs further investigation.
-	It would be helpful to know the human performance on this benchmark for comparison. Without this baseline, it's hard to gauge how challenging the benchmark is and whether the model performance is approaching human-level capabilities or if there is still a large gap.

### Questions
See weakness

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the critical challenge of uncertainty in vision-language AI systems, providing a structured taxonomy that distinguishes epistemic (information-based) from aleatoric (inherent unpredictability) uncertainties, with finer subcategories. Leveraging this taxonomy, the authors introduce a novel dataset, CERTAINLY-UNCERTAIN, comprising 178K VQA examples organized as contrastive pairs. These pairs are generated through image inpainting and language model prompting to showcase instances where answers transition between certainty and uncertainty. The paper also proposes a new metric, confidence-weighted accuracy, to evaluate model performance by integrating both accuracy and calibration. Experiments reveal that large vision-language models (LVLMs) demonstrate significant weaknesses in uncertainty awareness, though fine-tuning on the proposed dataset mitigates calibration errors, improves refusal-based benchmarks, and reduces hallucination rates—achieving these without compromising VQA performance. This work underscores the need for uncertainty-aware AI systems to enhance their reliability and usability in real-world applications.

### Strengths
* **Well-Designed Benchmark Dataset:** The authors carefully provide a rigorous classification of uncertainties into two high-level types (epistemic and aleatoric) with six finer categories. The development of 178K samples through a synthetic data pipeline and human curation reflects commendable effort.

* **Innovative Metric:** The proposed confidence-weighted accuracy offers a comprehensive evaluation by factoring in both the correctness and confidence of predictions, penalizing overconfident errors while rewarding high-confidence correct answers.

* **Comprehensive Experiments:** The paper explores multiple training paradigms, including fine-tuning, R-tuning, and preference optimization, across a range of benchmarks. Results highlight both the importance of addressing uncertainty and the effectiveness of the proposed dataset.

### Weaknesses
 * **Limited Model Coverage:** As a benchmark, I think the number of models evaluated is not sufficient. For closed-source models, the author only evaluated GPT-4V. In some of my experiments, I found that Claude 3.5 performed significantly better than GPT-4V for IDK problems. For open-source models, recent advanced models were not tested, such as InternVL2, Qwen2-VL, and LLaVA-Onevision. Expanding model coverage would better illustrate the benchmark's importance and impact.

* **Limited Evaluation:** Most experiments focus on refusal-oriented tasks with fewer hallucination-related benchmarks. Expanding evaluations to include hallucination datasets like HalluBench [1] and SHR [2], along with general benchmarks such as MME and MMBench, would provide a better view. If models merely improve in refusal scenarios but fail on broader tasks, the contribution of the proposed dataset may appear less impactful.

* **Concern of Data Proportion:** As seen in Table 1, the "Extraneous" awareness category has a higher data ratio compared to other categories. A clearer explanation for this design choice would be beneficial.

* **Concern of "Complexity Awareness" in the benchmark:** While the taxonomy is insightful, certain examples under "complexity awareness" seem to fall into a gray area. For instance, in Figure 7, the query regarding the number of balloons forming "30" could reasonably expect an approximate answer rather than an IDK response. Similarly, for the "distance between the two cats," an estimated answer would seem more appropriate in terms of user's expectation.

### Questions
All relevant questions are listed in the “Weaknesses” section.

### Soundness
3

### Presentation
3

### Contribution
3
