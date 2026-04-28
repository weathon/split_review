# Radiologist-like Progressive Radiology Report Generation and Benchmarking

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
Radiology report generation is a critical application at the intersection of radiology and artificial intelligence. It aims to reduce radiologists' workload by automating the interpretation and reporting of medical images. Previous works have employed diverse approaches, with some focusing solely on imaging data while others incorporate the indication but often neglect the interrelationships among different report sections. 
Our work identifies and harnesses the intrinsic relationships between the indication, findings, and impression sections of a radiology report.
The indication section provides the clinical context and specifies the reason for the examination, setting the stage for targeted image analysis. The findings section details the radiologist's observations from the image, including identified abnormalities and relevant normal findings. The impression section synthesizes these observations to form a diagnostic conclusion, directly addressing the clinical query presented in the indication.
By mapping these relationships, we propose a Radiologist-Like Progressive Generation (RLPG) framework that mirrors the radiologist's workflow for report generation.
Initially, an image encoder and a large language model process the imaging data alongside the indication to generate detailed findings. Subsequently, the same image, the indication, and the predicted findings are utilized to produce a concise impression. This method improves the alignment between report sections and improves the clinical relevance of the generated reports. 
To facilitate research and benchmarking in report generation, we introduce MIMIC-1V3 (i.e., 1 case vs. 3 sections), a curated dataset derived from the MIMIC-CXR by dividing each report into three sections: indication, findings, and impression.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the Radiologist-Like Progressive Generation (RLPG) framework, which mimics a radiologist's workflow for generating structured radiology reports. By sequentially generating findings and impression sections from a single input image and clinical indication, the model better aligns with clinical needs. The authors also introduce MIMIC-1V3, a dataset with structured radiology reports in distinct sections, facilitating focused benchmarking of report generation.

### Strengths
1. Alignment with Clinical Workflow: The RLPG framework emulates the actual workflow of radiologists, enhancing clinical relevance and report consistency, making it practical in real-world settings.
2. Dataset Curation: MIMIC-1V3 addresses inconsistencies in the original MIMIC-CXR dataset, providing a cleaner and more reliable benchmark for radiology report generation.

### Weaknesses
The RLPG framework seems straightforward and intuitive, especially in its logical progression and handling of radiology reports. Moreover,  aside from experimental metrics, there seems to be insufficient evidence demonstrating the innovation and superiority of this training paradigm. The framework's reliance on a sequential process, while mimicking radiologist workflow, introduces a potential bottleneck: errors in the findings generation stage could propagate and negatively impact the impression generation. The paper does not adequately explore the robustness of the model to these errors, nor does it discuss mechanisms to mitigate this propagation. Furthermore, the paper lacks a thorough analysis of the potential for redundancy between the findings and impression sections. While the authors claim these sections serve different purposes, the degree of overlap and its impact on the model's output quality needs further investigation. It is unclear if the model is simply regurgitating similar information in both sections, which would diminish the novelty of the approach.

### Questions
1. If the findings generated in the first stage contain inaccuracies, how does this affect the quality of the impression? Is there a mechanism to mitigate potential error propagation between stages?
2. Is there often overlapping information between the findings and impression sections? If so, does the model tend to produce redundant content, and could this result in outputs similar to previous frameworks?

### Soundness
2

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
5

### Summary
The authors introduce a Radiologist-Like Progressive Generation (RLPG) framework for report generation, which emulates the radiologist's workflow by first focusing on findings recognition through visual understanding, followed by diagnostic reasoning. They also present a new benchmark, MIMIC-1V3, derived from MIMIC-CXR, where each report is segmented into three sections—indication, findings, and impression—and paired with a corresponding frontal radiograph. The RLPG method is then compared with state-of-the-art LLM-based report generation models.

### Strengths
The newly developed MIMIC-1V3 benchmark serves as a standardized test bed for future report generation research.

### Weaknesses
1. The proposed framework may not fully align with real-world medical practices. Although MIMIC-CXR reports follow the order of indication, findings, and impression, clinicians may not always document in this structured sequence, which raises questions about the practical motivation for this approach. The method's reliance on a fixed order of indication, findings, and impression may not reflect the dynamic and iterative nature of clinical reasoning, where the diagnostic process can involve revisiting and revising initial impressions based on emerging findings. The assumption that the indication is always available and perfectly accurate also limits the practical applicability of the method.
2. The study lacks a detailed pipeline error analysis to assess how intermediate stages impact final output quality. This analysis should include the impact of errors in the indication, as well as how the accuracy of findings influences the generation of the impression section. A thorough error analysis should quantify how errors propagate through the pipeline, and identify the stages that are most sensitive to inaccuracies.
3. Comparisons in Table 4 may not be entirely fair, as the proposed model leverages the indication as prior knowledge in report generation. The use of the indication during training and inference gives the proposed model an advantage over methods that do not use this information. This makes it difficult to isolate the specific contributions of the model architecture from the benefit of using the indication as prior knowledge.

### Questions
1. Does this approach assume a close relationship between indication and final diagnosis? Have the authors examined how indications relate to impressions or findings in the MIMIC-CXR dataset? Additionally, how does this approach perform if provided with an incorrect indication as input?
2. To ensure fair comparisons in Table 4, could the authors evaluate their model without using indication as input? Alternatively, if using indication as input, they could first generate the indication and report its intermediate results.
3. How does the clinical accuracy of findings influence the generation of the impression section?

### Soundness
1

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
3

### Summary
The paper proposes the Radiologist-Like Progressive Generation (RLPG) framework for radiology report generation, which mirrors a radiologist's workflow by generating findings and then, based on these, producing the impression. To evaluate their approach, the paper introduce MIMIC-1V3, a dataset structured to match this workflow with separated indication, findings, and impression sections.

### Strengths
1. Easy to understand and intuitive Framework for report generation
2. Introducing a curated and refined public dataset for Chest X-Ray Report generation

### Weaknesses
1. The key experiment is missing in Table 3: Given the IMG and IND, generate the FIN and IMPR. This is critical because this is the authors' main claim: Separating the generation of each section is superior to the joint generation. Especially since in Table 2, the FIN only generation is inferior to the joint generation of FIN and IMPR on the test set. 
2. In general, I would have expected more fair comparisons to other methods. For non of the approaches in Table 4 (except the authors approach) was the IND section provided. Simple experiments as providing the the IND section to the other pretrained models would be the minimum, especially since there are approaches such as MAIRA-1 [1], which also work with the IND section given. 
3. RLPG sounds very much like a Chain-of-Thought (CoT) multi-stage approach. Comparing the approach to single-stage CoT could reveal interesting insights in how once could better guide the model in a single stage manner. 

### Questions
Will the dataset and training code be made publicly available? 
What is the reproducibility statement of the authors?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper emulates the workflow of radiologists to structure the report generation task in a sequence of indication + image → findings → impression, proposing a multi-stage generation framework. Additionally, it curates reports of the MIMIC-CXR, the largest chest X-ray dataset, into three sections: indication, findings, and impression.

### Strengths
1. Medical significance: This paper divides lengthy reports into three main sections to emulate radiologists' workflow, providing insights into the reasoning of large language models and identifying the stages that may contribute to erroneous reports.  
2. Clarity: The statistics of the created MIMIC-1V3 are provided. The figures and tables are informative and easy to understand. The proposed 2-stage report generation algorithm is easy to understand.

### Weaknesses
1. Originality and technical novelty: The proposed Radiologist-Like Progressive Generation (RLRG) is an MLLM-based 2-stage framework that feeds the output of the first stage as input of the second stage. Therefore, the overall design is not technically novel. Further, the neural network architecture is similar to existing radiology report generation methods such as R2Gen; the proposed dataset is modified from the existing publicly accessible dataset.  
2. Clarity: The authors concentrated on describing the 2-stage report generation algorithm, while the details of curating the MIMIC-1V3 dataset are not clearly stated. As the contribution of this paper heavily relies on the dataset creation, it is better to clearly address questions such as “How to handle reports without impression/finding/induction?”, “what algorithm was used to separate the report?” and “How to evaluate the correctness of the split?”.

### Questions
1. Please further highlight the technical contribution of the proposed RLRG framework, such as differences compared to existing multi-stage generation or MLLMs.  
2. From an application of MLLM’s perspective, there is not much difference between indication + image -> finding & impression and indication + image -> finding -> impression, as both findings and impressions are important and should be generated as medical reports. Please further explain the need to split the findings and impressions.

### Soundness
3

### Presentation
4

### Contribution
2
