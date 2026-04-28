# Mol-Instructions: A Large-Scale Biomolecular Instruction Dataset for Large Language Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Large Language Models (LLMs), with their remarkable task-handling capabilities and innovative outputs, have catalyzed significant advancements across a spectrum of fields. However, their proficiency within specialized domains such as biomolecular studies remains limited. To address this challenge, we introduce {\molins}, a comprehensive instruction dataset designed for the biomolecular domain. {\molins} encompasses three key components: molecule-oriented instructions, protein-oriented instructions, and biomolecular text instructions. Each component aims to improve the understanding and prediction capabilities of LLMs concerning biomolecular features and behaviors. Through extensive instruction tuning experiments on LLMs, we demonstrate the effectiveness of {\molins} in enhancing large models' performance in the intricate realm of biomolecular studies, thus fostering progress in the biomolecular research community. {\molins} is publicly available for ongoing research and will undergo regular updates to enhance its applicability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a valuable new dataset called Mol-Instructions for instruction-tuning large language models (LLMs) on biomolecular tasks. The authors gather and collect high-quality biomolecular data from various licensed sources, such as PubChem and USPTO. Mol-Instructions covers a diverse range of instruction types across molecules, proteins, and biomedical text, aiming to enhance LLMs' capabilities in the biomolecular domain. Through fine-tuning on the Mol-Instructions dataset, the authors show that LLMs' abilities on diverse biomolecular tasks can be improved.

### Strengths
- The proposed dataset, Mol-Instructions, is large-scale and comprehensive, covering a diverse range of tasks across molecules, proteins, and text. I appreciate the significant efforts in curating such a valuable dataset for pushing the research of LLMs for scientific domains.
- Visualization and analysis of key dataset statistics are available, providing insights for other researchers in the field. The long-tail distribution analysis is informative.

* The paper is well-written and provides a comprehensive description of the dataset construction process and baseline experiments.

### Weaknesses
 **Main concern on experiments:**

My major concern is the experiment part. Specifically, the current comparison and presentation scheme can lead to overestimated results and misleading conclusions because it ignores some important domain-adapted baselines and mainly compares them with domain-agnostic baselines, which are not fine-tuned or designed for scientific tasks. The authors are encouraged to appropriately acknowledge and compare these tasks with previous methods and datasets in order to improve their potential impact. Here I list the important baselines below:

1. An easier molecule instruction tuning dataset: Text+Chem T5 [1]. [1] has included most of the tasks/datasets in Mol-Instructions, including forward reaction prediction, retrosynthesis, description-guided molecule design, and molecule description generation. However, the discussion and comparison to Text+Chem T5 are missing. 
2. Scientific language models: Galactica [2]. Compared to the general-purpose LLMs (e.g., Vicuna and Alpaca) reported in the experiments, Galactica is specifically designed and pretrained for the science corpus and should be considered an important baseline.
3. Molecular Language Models: MoMu [3] and MolT5 [4]. These models are designed for description-guided molecule design and molecule description generation
4. The recent methods for reagent prediction [7], forward reaction prediction [5,6], and retrosynthesis [5]. Note that, the baselines in these domains employ different evaluation metrics compared to those reported in the paper. 
5. Baselines for protein-related tasks.

I understand that incorporating all these methods for empirical comparison is challenging, and an LLM is not expected to outperform all the state-of-the-art methods in every task to be a valuable contribution. However, I think the comparison to Text+Chem T5 [1] and Galactica [2] is essential and important, considering their similar purposes to this submission. It would also be valuable to report the performances of the single-task state-of-the-art methods in the Tables and Figures (you may not have to outperform these methods) to help empirical comparisons in follow-up works.


**Other weaknesses:**

- The quality control and curation process for constructing the dataset should be described more thoroughly. More details in data processing would strengthen confidence in the dataset.
- Table 5 lists the sources of data used in this paper, but it does not detail the availability or the methods for programmatic access to these data sources. Disclosing these particulars may aid researchers in replicating this paper.
- The Mol-Instructions dataset integrates various tasks in the field of biochemistry, such as the molecular and protein-related characteristics shown in Table 2. However, the experiments only conduct tests on a limited number of biomolecular tasks. Such an evaluation approach may not fully reflect performance on complex biomolecular problems.

### Questions
- Have the authors considered any other representation formats besides SELFIES for molecules? I'm curious how will SELFIES perform against alternative descriptors.
- The authors use BLEU, Levenshtein distance, and other text similarity metrics for evaluating molecule generation. Would more domain-specific metrics better depict the molecule generation capacity of the models? 
- Do you intend to expand Mol-Instructions with more task types and data in the future? What directions are you considering to continue improving it as a resource?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces "Mol-Instructions," a novel dataset specifically designed for biomolecular research, with the primary objective of enhancing the effectiveness of Large Language Models (LLMs) within this domain. The dataset is generously shared as an open-source resource, encouraging extensive utilization in future endeavors. It encompasses diverse tasks and incorporates information from existing data sources, complemented by template-driven instructions. Covering a wide range of topics, the dataset encompasses molecular description, property prediction, protein design, question answering, and more. Stringent quality assurance measures have been implemented to ensure the dataset's authenticity and comprehensive diversity.

### Strengths
+ The paper introduces "Mol-Instructions," a novel dataset specifically designed for biomolecular research, with the aim of enhancing the capabilities of Large Language Models (LLMs) in the field of AI for Science.

+ The authors employ this dataset to fine-tune an LLM, followed by a comprehensive evaluation of the obtained results.

+ This paper exhibits a well-structured and well-motivated approach. The figures presented are clear and easily comprehensible, facilitating easy understanding and follow-through.

### Weaknesses
I do not see a major weakness in this paper. Please see my question below.

### Questions
I appreciate the authors' efforts in collecting such a comprehensive benchmark for biomolecular research. However, recent work[1] showed that a large number of instructions may not be necessary to obtain a well-finetuned model.

Therefore, is it possible to investigate how the performance of Large Language Models (LLMs) using Mol-Instructions is affected by varying the number of training data instances, checking the redundancy, and possibly employing different sampling methods?

[1]: LIMA: Less Is More for Alignment

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Mol-Instructions, a new instruction dataset tailored specifically for the biomolecular domain. Mol-Instructions comprises three pivotal segments: molecule-centric instructions, protein-focused instructions, and overarching biomolecular text directives. Each segment is constructed carefully to bolster the interpretative and predictive prowess of LLMs pertaining to intricate biomolecular characteristics and dynamics. Through extensive instruction tuning experiments on LLMs, the authors demonstrate the effectiveness of Mol-Instructions in enhancing large models’ performance in the intricate realm of biomolecular studies, thus fostering progress in the biomolecular research community.

### Strengths
1. This paper presents "Mol-Instructions" which is a helpful instruction dataset for LLMs in AI4Science. 

2. Via comprehensive evaluations using LLMs, the authors demonstrate the effectiveness of Mol-Instructions in enhancing large models’ performance in the intricate realm of biomolecular research. 

3. The paper underscores the importance of reproducibility, guaranteeing open access to both the dataset and the accompanying code. Such transparency empowers the community to verify and expand upon the findings, catalyzing cooperative efforts and propelling new works in biomolecular research.

### Weaknesses
The evaluation maybe a small issue, however, I know it is not easy to evaluate the molecule generation tasks.

### Questions
See Weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this study, the authors present Mol-Instructions, a comprehensive molecular instruction dataset designed specifically for Large Language Models (LLMs). Mol-Instructions incorporates pre-existing tasks, information gleaned from established data sources, and template-based instructions. Rigorous quality control measures have been implemented to ensure the dataset's validity and encompassing diversity.

This dataset encompasses a wide spectrum of tasks, including property prediction, molecular description, protein design, and Q&A, among others. Furthermore, it introduces an LLaMA model finetuned on the collected instructions, showcasing its exceptional performance improvements over the original model across multiple case studies.

### Strengths
[Comprehensive Dataset Development] It creates an instruction-tuning dataset that can be used for the community of AI4Science and Large Language Models. This dataset addresses a critical need in the field and serves as a valuable resource for the broader scientific community.

[Performance Improvement with tuned LLaMA Model]: The paper's demonstration of the LoRA-tuned LLaMA model's superior performance over the original model in multiple case studies is a significant strength. 

[Broad Range of Applications]: The paper's emphasis is on covering a wide range of applications, including property prediction, molecular description, protein design, etc, which has great potential to be adopted for many downstream applications.

### Weaknesses
[Limited Quality Control] In the initial phase of the study, there is an absence of information regarding quality control procedures for the generated task descriptions. A more detailed explanation or discussion of quality control measures, even if briefly mentioned in section 3.2, would enhance the transparency and reliability of the research. Specifically, it is unclear what metrics were used to assess the quality of the generated instructions, and whether human evaluation was involved in this process. The lack of clarity around the quality control process makes it difficult to assess the overall reliability of the dataset.

[Less Meaningful Experiments] While the performance improvements observed when fine-tuning the LLaMa model on the collected data are promising, it's essential to acknowledge that this setup resembles a supervised learning scenario. Consequently, the comprehensiveness of the performance assessment may be somewhat limited. To provide a more comprehensive evaluation, additional comparisons with domain-specific Large Language Models (LLMs), such as those mentioned in references [1] and [2], would be valuable. Additionally, incorporating more challenging datasets such as ScienceQA [3] could further strengthen the paper's empirical results. The current evaluation does not adequately demonstrate the model's ability to generalize to unseen tasks or datasets, which is a critical aspect of evaluating instruction-tuned models.

[Insufficient Analysis on Text Generation] The paper would benefit from a more in-depth analysis of the factuality of the generated text. The current evaluation primarily focuses on performance metrics, but it does not address whether the generated text is factually correct and consistent with scientific knowledge. This is particularly important in the context of scientific applications, where accuracy and reliability are paramount. A more detailed analysis of the generated text, including error analysis and comparison with ground truth data, would be necessary to fully assess the model's capabilities.

### Questions
1. Could the authors provide more details about the quality control measures applied to the generated task descriptions in their study?

2. Are there plans to include comparisons with domain-specific Large Language Models (LLMs) to provide a more robust evaluation?

3. Is it possible to incorporate more challenging datasets from the ScienceQA to improve the paper's findings and conclusions?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
