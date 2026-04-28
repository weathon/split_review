# Benchmark Dataset for Radiology Report Generation with Instructions and Contexts

- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 5, 6, 3, 5

## Abstract
While automatic report generation has demonstrated promising results using deep learning-based methods, deploying these algorithms in real-world scenarios remains challenging, where models may be required to follow the instruction from the radiologists and consider contextual information. Such instructional report generation tasks are critical for enabling more accurate, customizable, and scalable report generation processes, but remain under-explored and lack substantial datasets for training and evaluation. However, constructing a dataset for report generation with instructions and contexts is challenging due to the scarcity of medical data, privacy concerns and the absence of recorded user-model interactions. To tackle this challenge, we propose a unified and automatic data generation pipeline which leverages large language model (LLM) to produce high-quality instructions and context for report generation tasks. We present a new benchmark dataset MIMIC-R3G that extends the largest existing radiology report generation dataset MIMIC-CXR, comprising five representative tasks pertinent to real-world medical report generation. We conducted an extensive evaluation of state-of-the-art methods using the proposed benchmark datasets. Additionally, we introduced a baseline method, the Domain-enhanced Multimodal Model (DeMMo), demonstrating that leveraging training data containing instructions and contextual information significantly improves the performance of instructional report generation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the limitations of existing medical report generation models in capturing important contextual information beyond radiology images by proposing a real-world radiology report generation model (R3G) and a new benchmark dataset, MIMIC-R3G. MIMIC-R3G comprises five sub-tasks that reflect various clinical needs, each designed to generate reports based on medical images using specific instructions and contextual information as inputs.

The five sub-tasks are as follows:

1. No Context Report Generation: Generates a report based on medical images and basic instructions as inputs.
2. Report Revision: Produces a revised report using modification instructions and the current report as inputs.
3. Template-based Report Generation: Generates a structured report by filling in a template based on provided instructions and a blank template as inputs.
4. Previous Visit as Context: Generates a report based on instructions and prior visit records to reflect the current report with historical context.
5. Medical Records and Lab Tests as Context: Generates a comprehensive report that incorporates patient medical records and lab test results provided as contextual input.

The dataset was constructed through a data generation pipeline that creates instructions and contextual information specific to each sub-task, allowing for the training and evaluation of the R3G model with the MIMIC-R3G dataset.

In conclusion, this paper introduces the MIMIC-R3G dataset, an automated data generation pipeline, and DeMMo, a Flamingo-based model, as a baseline for the R3G benchmark dataset.

### Strengths
A key strength of this study is its attempt to provide a new benchmark dataset specifically based on chest x-rays. Addressing the following weaknesses would further enhance its value and impact.

### Weaknesses
[About benchmark dataset] 

The proposed benchmark evaluates five distinct tasks using consistent metrics and baselines, which obscures the unique objectives and distinctions of each task. Task-specific metrics and baselines are needed to highlight these differences better. For instance, the evaluation of the 'Report Revision' task should not only focus on the correctness of the revised report but also on the accuracy with which the model incorporates the modification instructions. Similarly, the 'Template-based Report Generation' task should be evaluated not just on the content but also on the structural fidelity to the template. These nuances are lost when using uniform metrics across all tasks.

For the Report Generation task, the benchmark dataset CXR-PRO already exists to address temporal-changing hallucinations.

The Previous Visit as Context task lacks novelty, as it aligns closely with the inherent characteristics of chest x-ray reports. The MS-CXR-T dataset, which already enables focused comparisons of temporal changes in diseases, limits the distinctiveness of this task. The task, as it stands, does not offer a unique challenge that is not already addressed by existing datasets focusing on temporal changes in chest x-ray reports.

Furthermore, in the 3) Report Revision and 4) Template tasks, the primary focus is on compliance with instructions despite the use of chest X-ray images. For a more robust assessment, these tasks should include detailed and consistent evaluations reflecting clinical standards. Including an LLM model baseline and focusing on instruction adherence rather than traditional NLG or CE metrics would enhance the evaluation. The current evaluation overlooks the critical aspect of instruction following, which is central to these tasks. For example, in the Report Revision task, the evaluation should specifically assess how well the model adheres to the given modification instructions, not just the overall quality of the revised report. Similarly, the Template task should be evaluated on how accurately the model fills in the template based on the provided instructions, rather than just the clinical correctness of the filled report.

Finally, 5) for the Medical Records and Lab Tests as Context task, the impact of incorporating real medical records on diagnostic content should be emphasized. For example, evaluations could assess if diagnoses change from negative to positive when medical records are included. The current evaluation does not sufficiently highlight the influence of medical records on the diagnostic content of the generated reports. The evaluation should include specific metrics that measure the change in diagnostic accuracy when medical records are included, such as whether the inclusion of medical history leads to a more accurate diagnosis compared to image-based reports alone.

[About experiment part] 

The study's main contribution is the introduction of a new benchmark dataset. While DeMMo, based on Flamingo, is an incremental improvement, additional experiments are needed for thorough validation. Current comparisons are primarily with generalist models (e.g., ChatCAD+, Med-Flamingo) trained on diverse medical images, making DeMMo's advantage over these models unsurprising. However, comparisons with chest x-ray specialist models are limited to CvT2DistillGPT2. Broader comparisons with other chest x-ray-focused models, including instruction-finetuned models (ex. LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation), are essential to establish DeMMo’s validity as a baseline.

### Questions
N/A

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
4

### Summary
The paper presents MIMIC-R3G, a new benchmark dataset designed to advance automatic radiology report generation by integrating real-world clinical contexts and instructions. Radiology report generation traditionally approached as a captioning task, often lacks adaptability to complex clinical workflows that involve physician-specific instructions and patient history. The authors address this limitation by proposing a structured pipeline that utilizes large language models (LLMs) to produce high-quality instructional data, integrating contextual elements like prior patient records and lab results. MIMIC-R3G extends MIMIC-CXR by introducing five tasks that emulate practical report generation scenarios, such as report revision and template-based generation. The authors also introduce a baseline model, DeMMo (Domain-enhanced Multimodal Model), tailored for medical contexts, which incorporates a specialized medical vision encoder and pathological guidance, enhancing report accuracy by leveraging detailed domain knowledge. Extensive experiments indicate that incorporating context and instruction substantially improves report generation performance, setting a new standard for real-world radiology applications.

### Strengths
1. Automatic data generation pipeline leveraging GPT-4 to produce high-quality instructions and context for report generation tasks.
2. Extensive evaluation of state-of-the-art methods using the proposed benchmark datasets.
3.  Introduction of the Domain-enhanced Multimodal Model (DeMMo), a novel architectural modification suited for radiology report generation.

### Weaknesses
1. The synthetic data generation process, while innovative, may not fully capture the nuanced and complex nature of real-world clinical interactions and instructions. The reliance on LLMs for generating instructions and contexts might introduce biases or oversimplifications that are not present in actual clinical practice, potentially limiting the generalizability of models trained on this data.
2. The paper lacks a direct comparison of the generated data and model outputs with real-world clinical data. Without such a comparison, it is difficult to assess the clinical relevance and practical utility of the proposed benchmark and the DeMMo model. The evaluation is limited to the proposed dataset, making it unclear how well the model would perform on real-world clinical data.
3. Motivation behind architectural changes in DeMMo remains unclear. The specific design choices, such as the domain-enhanced perceiver resampler module and the gated cross-attention layers, lack detailed justification. It is not clear why these particular modifications were chosen over other potential architectural changes, and how they specifically address the challenges of radiology report generation.
4. Experiments are shown only on the proposed dataset, which does not validate the efficacy of the proposed model DeMMo. The lack of evaluation on existing radiology report datasets makes it difficult to assess the generalizability and robustness of the proposed model. It is unclear whether the performance gains observed on the proposed dataset would translate to other datasets.

### Questions
1. Could you please clarify the paragraph of report revision, there seems to be a typo where report is denoted with C.
2. How did you ensure that the types and frequencies of errors introduced in the report revision task accurately reflect real-world errors made by human radiologists or existing AI systems?
3. There are other available radiology report datasets. Does DeMMo trained on MIMIC-R3G showcase better performance on other datasets, i.e., does pertaining on MIMIC-R3G enhance performance on MIMIC-CXR, and other available datasets like IU-XRay, ROCO. 
4. Did you keep all the modules learnable while training DeMMo on MIMIC-R3G dataset? If yes, please mention the training details, i.e., whether the LLM was trained or not?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper identifies a problem with current radiology report generation datasets: they fail to evaluate models’ performance in a real-world workflow, where models might be asked to incorporate different contextual information and generate a wide range of text formats instead of a simple, image-to-text, radiology report. Its answer to this problem is a novel benchmark, MIMIC-R3G, derived from MIMIC-CXR, which evaluates generative models on five tasks: no-context report generation, generation using medical records as context, using previous visits as context, report revision, and templated generation. The paper further introduces a baseline for this benchmark: a model that fuses medical visual representations with Flamingo, and shows its competitive performance on the benchmark compared to some popular radiology report generation models.

### Strengths
I agree with the paper’s central claim that current modeling and evaluation approaches do not fully reflect models’ potential use cases in a real workflow. Evaluating models’ ability to use contextual information is a relatively new but important concern for radiology report generation.

The additional tasks to MIMIC-CXR are well-motivated, and the methodology to generate them using GPT-4 is rigorous. Another strength of this method is that it is scalable because the data for the new tasks are automatically generated using GPT-4. Most importantly, the paper validates this procedure using annotations from radiologists.

I enjoyed reading section 5! The notation is very clear and the diagram added to my understanding of the method. Furthermore, the results show the baseline’s effectiveness, as it achieves top performance in most tasks in the benchmark.

### Weaknesses
I think the most significant weakness of this paper is the low impact of the contribution. While evaluation that reflects a real-world workflow is an important problem, I think that the benchmark offers a limited approach. MIMIC-CXR already contains information about previous visits. The medical records, although validated as plausible, are still synthetic data. It is unclear how systems trained on synthetic data will perform in real settings. The report revision and template generation tasks still function within the single-turn interaction setting, whereas real-world interactions will likely be multi-turn.

Aside from that, I noticed several typos, such as:
* Line 191: I think $I_i$ is supposed to be $R_i$.
* Line 202: “posses”
* Line 430: “difference tasks”

There are more typos than just these. Please address them accordingly!

### Questions
Questions:
* Line 343: The queries are concatenated with the visual features. This means later on the queries will just attend to themselves. What benefit does this offer?

Some more suggestions (these are just suggestions to improve the paper and they do not factor into my evaluation of the paper):
* Line 222: I think “Quality Control of the Generation” should be a separate subsection because it is about validating the dataset.

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper extends the radiology report dataset MIMIC-CXR to a new benchmark dataset called MIMIC-R3G which adds instructions and context, in addition to images and radiology reports. The aim of MIMIC-R3G is to benchmark the capabilities of models on radiology report writing, revising, template-based writing, and writing with context information (previous radiology reports, medical records, lab tests), respectively. The paper also proposes a new method DeMMo which is evaluated on MIMIC-R3G and demonstrates good performance compared to baseline methods.

### Strengths
This paper presents an extension of the MIMIC-CXR dataset into more scenarios (simulating how clinicians may write radiology reports with instructions and context) which can help evaluate the capabilities of models in writing and revising radiology reports, from the technical perspective (but probably not from the clinical perspective, see Weakness).

A new method which demonstrates good performance on the new dataset MIMIC-R3G.

### Weaknesses
The paper's writing requires improvement, especially in terms of clarity. For instance, when the "pipeline" is mentioned on Page 4, it is neither defined nor illustrated, leaving readers uncertain about its components and workflow. Including an illustration or a detailed explanation of the pipeline would help understanding.

The motivation of the paper is also unclear. While it emphasizes supporting real-world clinical practice in Line 049 for radiology report generation (with instructions and context), the expectation is to collect a new dataset originating from actual clinical workflows where clinicians follow specific instructions to write radiology reports. However, the new dataset, MIMIC-R3G, is an extension of MIMIC-CXR rather than a newly collected dataset from real-world practices involving radiologists. Consequently, the setup of this work does not adequately justify its motivation and limits its overall contribution. It might be beneficial to collect a small-scale, new dataset from real-world practice and use MIMIC-R3G as a supplementary large-scale, silver-standard dataset.

Furthermore, the paper focuses on radiology report generation with a proposed method specifically designed and optimized for this purpose. It remains unclear how the pipeline used to produce this new dataset and the new method, DeMMo, can be applied to other domains, which would be of interest to a broader ICLR audience.

### Questions
What is "correction" in Line 264?

Is templated-based writing actually useful? Do radiologists write reports following templates? Figure 1 also shows a relatively low acceptance rate.

Table 2 seems to demonstrate that using previous radiology reports and medical records is not helpful (compared to no context). Any insights?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper defines a new task, instructional report generation, based on real-world clinical needs and encompassing five subtasks. Leveraging the open-source MIMIC-CXR dataset, the authors designed an automated data generation method to construct a dedicated dataset and benchmark (MIMIC-R3G) for this task. The medical multimodal model, DeMMo, was trained on this dataset and demonstrated superior performance in benchmark comparisons with existing models.

### Strengths
+ The paper demonstrates high originality and academic importance by introducing the instructional report generation task with an innovative design.
+ The task is divided into five clinically meaningful subtasks, providing practical guidance for future research on report generation, and inspiring directions that align more closely with clinical practice.
+ The paper is well-organized, with a clear sequence of task, dataset/benchmark, and model, offering a coherent and complete narrative that aids reader comprehension.

### Weaknesses
 + **Insufficient Validation of Clinical Relevance for Subtasks**: While the paper emphasizes the dataset and benchmark, it lacks fair experiments to validate the practical significance of each subtask. For instance, when comparing different contexts (such as without context, previous visit, medical records, and lab tests as context), it would be beneficial to compare the performance on the same samples across subtasks to demonstrate the actual clinical relevance of these contexts.
+ **Lack of Task-Specific Model Adaptation**: As a dataset-focused paper, the model design lacks task-specific adaptation, which might detract from the paper's primary focus.
+ **Other Issues**: The symbol $I_i$ in line 191 should be $C_i$, and the numeric values in line 406 are inconsistent; $3846$ does not equal $2246 + 600$.

### Questions
In addition to the issues mentioned in the Weaknesses section, there are also the following concerns: 
+ What is the clinical significance of report revision? Are there examples to illustrate this?

### Soundness
2

### Presentation
3

### Contribution
3
