# CICD-Coder: Chinese EMRs Based ICD Coding With Multi-axial  Supported Clinical Evidence

- Decision: Reject
- Avg Score: 3.75
- Scores: 1, 5, 3, 6

## Abstract
Although automatic ICD coding has achieved some success in English, there still exist significant challenges for the Chinese electronic medical records(EMRs) based ICD coding task. The first problem is the difficulty of extracting disease code-related information from Chinese EMRs due to the concise writing style and specific internal structure content of EMRs. The second problem is that previous methods have not exploited the disease-based multi-axial knowledge and are neither associated with the corresponding clinical evidence, resulting in inaccuracy in disease coding and lack of interpretability.
In this paper, we develop a novel automatic ICD coding framework CICD-Coder for the Chinese EMRs based ICD coding task. In the presented framework, we first investigate the multi-axes knowledge (crucial for the ICD coding) of the given disease and then retrieve corresponding clinical evidence for the disease-based multi-axes knowledge from the whole content of EMRs. Finally, we present an evaluation module based on the masked language modeling strategy to ensure each knowledge under the axis of the recommended ICD code is supported by reliable evidence. The experiments are conducted on a large-scale  Chinese EMRs dataset collected from varying hospitals and the results verify the effectiveness, reliability, and interpretability of our proposed ICD coding method.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of this study concentrate on the utilization of Chinese Electronic Medical Records (EMRs) for ICD coding. They emphasize the complexity of Chinese EMRs, where information is scattered across various locations, necessitating a comprehensive approach for ICD prediction. To enhance the precision of their predictions, the authors propose incorporating additional evidence after the initial ICD prediction. They accomplish this by training a retrieval model designed to retrieve the relevant evidence corresponding to a given diagnosis. Their findings suggest an improvement in ICD coding accuracy on Chinese datasets, albeit with limited exploration. Nevertheless, the paper is deemed in need of substantial revision, and in my opinion, it is not yet ready for publication.

### Strengths
Retrieval seems to be important for ICD coding - The importance of retrieval in ICD coding is underscored by this paper, which emphasizes the potential for enhanced ICD coding accuracy through the retrieval of relevant evidence. However, it is worth noting that the execution of these ideas within the paper falls short in terms of clarity and effectiveness.

### Weaknesses
 **Poor presentation of ideas**

- The paper exhibits a deficiency in the presentation of its ideas, lacking a comprehensive methodological description that is essential for clarity and reproducibility. This shortcoming necessitates substantial reworking before the manuscript can be considered for publication.

**Lack of Motivation**

- The motivation for focusing on Chinese EMRs in the study is inadequately substantiated. The problems highlighted by the authors are not unique to Chinese EMRs and are also prevalent in other languages, including English. A stronger rationale is required to establish the relevance and significance of this specific focus.

**Poor experimentation**

- The paper's experimental approach is notably deficient as it omits comparisons with other relevant baselines. For example, it does not include comparisons with established methods like LAAT and other techniques known for their efficacy in ICD coding. This omission hinders the paper's ability to demonstrate its effectiveness and distinguish itself within the field. Addressing this issue is imperative to improve the paper's readiness for publication.

### Questions
1. ***In Section 2.2.1*** the authors mention that they obtain the ICD codes. Which method is used to obtain the initial ICD codes. 
2. ***Section 2.2.1*** mentions the use of prior knowledge to identify likely evidence for different icd codes. Is there a comprehensive list of these rules? The authors do not mention the rules

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new automatic ICD coding framework, namely CICD-Coder, for the Chinese Electronic Medical Records (EMRs). The presented framework utilizes multi-axes knowledge of the disease and retrieves clinical evidence from the EMRs. The work primarily focused on extracting ICD codes from Chinese EMR, which poses additional constraints and problems that need to be tackled in addition to extracting codes from English EMR. Experiments are conducted on real, Chinese dataset and evaluated by ICD coders as well.

### Strengths
* The paper is well-motivated in the sense that it attempts to address challenges arising from Chinese EMR that is not often present in English EMR. While I am not very familiar with existing works on Chinese EMR, this line of work might be interesting for practitioners and ML community that is interested in Chinese EMRs.
* Experiments are conducted thoroughly, using both Chinese datasets and assessments made by ICD coders.
* The proposed method does show improved performances compared with the baselines. However, there are some other concerns (see below).

### Weaknesses
1. While the proposed method in the paper does improve over its baselines. The improvement does not have a large margin and is not significant.
2.  Also, the number of baselines is too small. There are only two baselines which makes the comparison and results non-exhaustive. Unless there is a strong reason and explanation for using only two baselines, the authors could consider using more.
3. In 2.2.1, the author says that **We have prior information about the likely appearance location of the supporting evidence in the medical record by professional ICD coders**. In the last sentence, they say that this prior information makes the process **fast and efficient**. Given that the paper is application-oriented, I wonder what would happen when practitioners do not have this prior information. It seems to be that having such prior information is a strong assumption.
4. Minor issue: part of the paper contains grammar issues.

### Questions
Given that the paper's focus is on Chinese EMRs, I am not sure whether some setups made in the paper is relevant or specific to Chinese EMR. For instance, for the two principles made in the paper, the first principle is **The source of the evidence limits what the evidence can describe and how credible it is.**, and the second principle is **The number of repeating times of one piece of evidence in the Chinese EMR determines its importance**. I am not sure whether those two principles are specific to Chinese EMRs. It seems to me that those two principles could broadly apply to EMRs in most countries. Thus, it is debatable whether the design of the principles is specific to Chinese EMR, which makes those two design principles seem a bit too general. I wonder whether the authors have any idea about the specific design of the principles.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the CICD-Coder, a new framework for improving ICD coding in Chinese electronic medical records (EMRs). It addresses challenges in the unique features of Chinese EMRs. The CICD-Coder analyzes crucial disease knowledge, retrieves relevant clinical evidence from the EMRs as the additional features, and finally uses masked language prediction with prompts to perform ICD coding under the support of the retrieved evidence. The experiment results show its effectiveness is significant in a Chinese EMR dataset.

### Strengths
1. The paper pioneers the exploration of unique challenges in ICD coding within Chinese electronic medical records (EMRs), an area not extensively covered in existing literature.  
2. The authors introduce an innovative evidence retrieval module within their proposed CICD-Coder framework, marking a significant advancement in ICD coding performance. This module stands out for its potential to substantively improve coding accuracy by ensuring that codes are grounded in tangible clinical evidence.

### Weaknesses
1. The paper overlooks crucial existing research, particularly the study outlined in [1]. That seminal work similarly employs prompt-based mask prediction for ICD code probability, and its omission here represents a significant gap in the literature review. 
2. The absence of comprehensive ablation studies is a notable weakness. The paper would greatly benefit from detailed analyses that demonstrate the specific contributions and impact of the proposed mask-based prediction methodology. 
3. The explanation of key methodologies, especially the evidence retrieval module, is vague. Given its critical role in enhancing ICD coding performance, a more in-depth discussion of its design and functionality is essential for readers to fully understand and replicate the study. 
4. Certain claims appear unsubstantiated, creating potential confusion. For instance, the assertion regarding the brevity of diagnoses in Chinese EMRs contradicts common characteristics seen in datasets like MIMIC. This discrepancy necessitates clarification to maintain the paper's credibility. 
5. The paper exhibits limited novelty when viewed against the backdrop of existing studies like [1]. The underdeveloped evidence retrieval module further diminishes the perceived innovativeness of the CICD-Coder framework. A more thorough exploration of these elements could help underline the unique contributions of the current study.

### Questions
Will the dataset be available? If not, have you considered applying the proposed method to some public datasets e.g. MIMIC-III and IV? If not, what makes it impossible?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describe a novel method to identify icd code in Chinese clinical notes. The methods include fine retrieving relevant codes and translate the task to binary classification task by feeding a template prompt to a t5 model.

### Strengths
The task solved is important
The method described is novel

### Weaknesses
Lack of competitive baselines, since the task is novel it’s hard to compare to other methods , hence the validity of the method presented is unclear

### Questions
1. Will the data used for evaluation will be publicly avilable?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
