# Large Multimodal Model for Real-World Radiology Report Generation

- Decision: Reject
- Scores: 5, 5, 5, 3, 8

## Abstract
While automatic report generation has demonstrated promising results using deep learning-based methods, deploying these algorithms in real-world scenarios remains challenging. Compared to conventional report generation, real-world report generation requires model to follow the instruction from the radiologists and consider contextual information. Thus, this paper focuses on developing a practical report generation method that supports real-world clinical practice. To tackle the challenges posed by the limited availability of clinical data, we propose a GPT-based unified data generation pipeline designed to produce high-quality data. Consequently, we present a new benchmark dataset MIMIC-R3G, comprising five representative tasks pertinent to real-world medical report generation. We propose Domain-enhanced Multi-modal Model (DeMMo), where an additional medical domain vision encoder is incorporated into the general domain multimodal LLM to enhance its ability on specific domains. This approach aims to harness the specialized capabilities of the medical domain vision encoder while leveraging the robustness and versatility of the general domain multi-modal LLM. Comprehensive experiments demonstrate that our approach attains competitive performance across all real-world tasks compared to existing interactive report generation frameworks and state-of-the-art encoder-decoder style report generation models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper made serveral technical contributions to mimic how a real radiologist will do the report generation process in a more realistic work environment. All these contributions as listed in section one are valid scientific contributions. I think there should be some credits for that, advancing from the previous literature. 

This paper/work is developed using Flemingo general vision encoder and ChatGPT tools. This would be reasonable but the dependency on using ChatGPT will decrease its scientific values. More detailed comments will follow in later comments.

### Strengths
This paper made serveral technical contributions to mimic how a real radiologist will do the report generation process in a more realistic work environment. All these contributions as listed in section one are valid scientific contributions. I think there should be some credits for that, advancing from the previous literature.

### Weaknesses
However I would argue, given the current technical roadmap setup as demonstrated in this paper, you can generate fairly interesting generated reports as results, but this is probably on the wrong technical path to build a automatic reporting system for reliable clinical report generation, no matter you use ChatGPT or even GPT4-V models.

The essential problem/challenges in accurate and automatic clinical report generation are at the core of detecting/localizing all pathological or clinically significant findings, then classifying/diagnosing these findings acurately and finally forming all findings with diagnosis into a report where the physician can verify and modify for the final use (as a real world clinical adoption).

1, you need be abe to extract/balidate fairly accurate finding labels from training reports using NLP tools (maybe chatGPT, maybe special bio-NLP tools).

2, you need to solve the weakly supervised localization/detection issue by mapping the labels to the image regions (which is called visual grounding).

3, Hopefully with powerful and robust NLP and vision tools, you can curate a dataset by integrating/iterating the above two steps.  Then you need to a train vision encoder/decoder to find pathologies with desirably accurate results on new images to generate an initial report.

4, Doing clinical diagnosis on these findings and comparing the current findings to previous studies to derive the temporal change information (you need to build a classifier according ontology for dignosis and image matching/alignment modules by tracking these findings over time).

5, forming a report and providing means (hyperlinks) for human physicians to inspect and accept and edit the report.

The above steps are logically impossible to bypass if you want to build a useful clinical assist tool in the real world. Your paper as currently does not do the above items. I am not convinced if the goal is to build a clinically viable report generation tool, how would you be able to achieve that.

In section 4, it's unclear how ChatGPT can modify reports with significant factual changes without directly analyzing the images and having high-quality visual grounding to confirm or reject clinically significant findings. What is the purpose of these revisions, and how reliable are they? Could these revisions potentially lead to misdiagnoses?

The use of a 'previous visit as context' raises concerns. How can a random report serve as a valid pseudo-previous report? According to information theory, if there's no new information, maintaining an empty prior is the correct approach. Injecting an incorrect previous report could potentially cause diagnostic errors.

Furthermore, using a medical professional to validate a subset of the generated data is not a robust approach. Interpreting chest X-rays is challenging for radiologists, and there can be significant inter-observer variations.

In Table 2, while the functions are convenient, the critical question is how the accuracy of the generated/modified content is guaranteed. If these reports are intended for real patient diagnosis, should we trust the clinical accuracy of the content generated from Table 2, or are these functions merely demonstrations?

### Questions
Please answer the weakness as provided above. Many if not most of report generation papers no matter where they publish do not understand underlying what are clinically essential informations where report should have, and how ....

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an automated radiology report generation system trained on the newly created MIMIC-R3G dataset. This dataset focuses on practical tasks that are somewhat overlooked in the literature. The authors employ a GPT-based data generation pipeline to synthesize training data across different R3G tasks. The experimental outcomes presented in the paper suggest that the proposed DeMMo can outperform existing approaches in radiology report generation according to evaluations on the MIMIC-R3G benchmark.

### Strengths
- The manuscript targets meaningful and less explored tasks in radiology report generation, covering a variety of scenarios. This focus is commendable as it moves the field towards clinically applicable solutions in automatic report generation.
- By utilizing ChatGPT for data generation, the authors propose a potential solution to mitigate the issue of data scarcity in complex report generation tasks.
- The adaptation of Flamingo and prompt tuning in the proposed DeMMo model demonstrate improved quantitative results over existing methods.
- The manuscript is well-written and easy to follow.

### Weaknesses
 - Despite addressing significant tasks in clinical practice, the manuscript's technical contributions appear incremental and may not align with the expectations of the ICLR community. The content might be more suited to specialized medical-related conferences like MICCAI or IPMI.
- The methodology for constructing the MIMIC-R3G dataset, particularly the generation of reports that integrate prior patient visits and additional lab test information, lacks rigorous clinical validation. To ensure the clinical relevance of the generated data, it would be beneficial to include samples that have been validated by healthcare professionals. This is also true for the generated reports. The lack of validation raises concerns about the dataset's suitability for real-world clinical applications.
- Detailed statistical validation and significance testing could strengthen the results section. While the proposed DeMMo generally performs better than baseline models in terms of NLG metrics, the recall of CE seems to be lower than ChatCAD. The absence of statistical significance tests makes it difficult to ascertain the robustness of the reported improvements.
- The paper would benefit from a more in-depth qualitative analysis. Comparative examples of reports generated by different models could offer valuable insights into each model's strengths and limitations, providing a clearer understanding of the practical implications of their use in clinical settings.

### Questions
- The manuscript would greatly benefit from the inclusion of clinical validations for the synthesized training data. Can the authors present any evaluations conducted by medical professionals to verify the clinical accuracy of the generated data? The same question applies to the generated reports; providing clinical validations would significantly enhance the paper's credibility.
- Will the constructed MIMIC-R3G benchmark be publically available?
- I would recommend a more thorough statistical analysis of the results to better elucidate the significance of the findings. Additionally, providing qualitative comparisons of the reports generated by DeMMo and other baseline models would offer deeper insights into the practical utility of the proposed model.
- It is noted that the recall for CE by DeMMo tends to be lower compared to the baseline model ChatCAD. Could the authors delve into possible reasons for this discrepancy and suggest potential improvements?

Minor:
- Citation formats in 6.2 and Supp: A are inconsistent. There is one missing citation in Supp: E.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose a new benchmark dataset for medical report generation with building a unified data generation pipeline. It also proposed a domain-specific multi-modal model (DeMMo) to improve the raw llm for medical report generation. Experiments show the method is good.

### Strengths
1. The motivation makes sense. It should be quite helpful and natural to use instruction/context to generate better medical report.
2. The paper has did plenty of experiments to show the effectiveness of the proposed method.

### Weaknesses
1. It is not clear how to generate the I, C and R', which is critical in this paper.  Also, I'm not sure if the quality of generated data by the unified pipeline is good or not, though the authors mention there are professions who help check them. 
2. The comparison in Table 3 shows the advantage of the proposed method in this paper, which is mainly due to the domain-specific encoder. However, will the computational complexity be much larger?
3. The dataset (MIMIC-R3G) is not open sourced or not mentioned to open source it in future.

### Questions
1. I'm not sure if the generated I, C and R' are fixed or can be different at different time. To me, a benchmark dataset should better be fixed.
2. Does every patient have the previous visit data in MIMIC-CXR? How do you deal with those who have no previous data?
3. "In summary, our medical professionals have determined that no significant factual discrepancies exist between the content generated by GPT and the ground-truth reports across all samples". Can you please introduce more about it? Especially considering the huge number of samples in the dataset.
4. The experiments mainly talk about the effectiveness of the method, how we can assess the quality of the data.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors introduce a novel problem setting for real-world report generation that closely simulates clinical practices by integrating various clinical interactions and contextual information. They also present DeMMo, a substantial multimodal model enriched with domain-specific capabilities achieved by integrating a general domain Flamingo model with an additional medical vision encoder.

### Strengths
(1) The incorporation of user instructions into the generation process is a valuable enhancement for improving the quality of generated reports.

### Weaknesses
 (1) The novelty of DeMMo is somewhat limited.
(2) The inclusion of user instructions may raise concerns about the trustworthiness of generated texts, necessitating careful manual review by doctors, potentially leading to increased time and effort.
(3) The test dataset sizes are notably smaller in comparison to the training datasets.
(4) Relying solely on a single self-constructed dataset for experiments lacks robustness. Additional datasets should be considered for validation.
(5) The addition of an extra encoder in DeMMo could potentially introduce computational overhead, impacting overall efficiency.

### Questions
(1) In Table 5, DeMMo's performance on BLEU@1 appears suboptimal. Could you explain the reasons for this lower performance?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduced a new problem setting, real-world radiology report generation, that focuses on interactivity, following instructions, and considering various context information. The authors constructed a new benchmark dataset for this purpose and proposed a Domain-enhanced Multi-Modal (DeMMo) model, a variant of Flamingo model, to improve the medical domain-specific abilities.

### Strengths
- The focus on real-world radiology report generation is designed to be practical and applicable in clinical settings, which is great in terms of translational impact.
- The benchmark is very useful to the community. 
- The model integrates an additional domain-specific medical encoder to the perceiver resampler, enhancing its ability to capture detailed visual features in the medical domain.

### Weaknesses
 - Lack of model efficiency analysis
- Since the proposed benchmark is one of the core contributions in this work, please describe how do you plan to make it publicly available.

### Questions
1. Could you please add the number of model parameters and flops in the result Tables?
2. How do you plan to make the dataset available to the community?
3. Where do you plan to host this benchmark? CodaLab could be a good platform.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
