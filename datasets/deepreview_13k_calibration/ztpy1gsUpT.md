# Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Large language models (LLMs) demonstrate remarkable medical expertise, but data privacy concerns impede their direct use in healthcare environments. 
Although offering improved data privacy protection, domain-specific small language models (SLMs) often underperform LLMs, emphasizing the need for methods that reduce this performance gap while alleviating privacy concerns. In this paper, we present a simple yet effective method that harnesses LLMs' medical proficiency to boost SLM performance in medical tasks under \textit{privacy-restricted} scenarios. Specifically, we mitigate patient privacy issues by extracting keywords from medical data and prompting the LLM to generate a medical knowledge-intensive context by simulating clinicians' thought processes. This context serves as additional input for SLMs, augmenting their decision-making capabilities. Our method significantly enhances performance in both few-shot and full training settings across three medical knowledge-intensive tasks, achieving up to a 22.57\% increase in absolute accuracy compared to SLM fine-tuning without context, and sets new state-of-the-art results in two medical tasks within privacy-restricted scenarios. Further out-of-domain testing and experiments in two general domain datasets showcase its generalizability and broad applicability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In situations where text data is subject to privacy protection constraints, this paper designs a small-scale language model to perform diagnoses of diseases. Utilizing the rich prior medical knowledge in LLM, the approach involves generating a medical knowledge-intensive context using privacy-protected text. This generated context, along with key terms extracted from the text and questions, is then input into the SLM, which is fine-tuned during training. Experiments across multiple datasets demonstrate that this fine-tuning process effectively enhances the accuracy of the diagnostic model.

### Strengths
1. This paper focuses on a very important research topic in the field of medicine: how to effectively extract more useful information from incomplete text under the conditions of privacy protection. The author has made full use of the domain knowledge in LLM to effectively fine-tune the SLM, which ensures that the lightweight models can achieve high accuracy.

2. This paper presents rich and comprehensive experiments. Beyond basic decision-making tasks, it also explores solutions for few-shot experiments and out-of-distribution (OOD) model generalization using the methods discussed in this paper.

3. This paper fully utilizes the rich domain knowledge in LLMs to expand the knowledge base of medical reports, achieving excellent diagnostic accuracy even while ensuring privacy protection.

### Weaknesses
1. The contribution of this paper to the algorithm and the significance of the clinical problems it addresses seem not to be very high.

2. The main work of this paper appears more as an engineering problem, transferring domain knowledge from LLMs to SLMs. From the perspective of algorithmic contribution, there seems to be some room for improvement.

### Questions
1. The experimental datasets in this paper are all question-and-answer test datasets, and whether the methods of this paper are applicable to medical report datasets requires additional experimentation. This is because in medical reports, how to generate high-quality questions using other LLM interfaces is a question worth studying.

2. Large language models provide additional domain knowledge, but in the context of specific medical tasks, will the direct transfer of knowledge from LLMs to SLMs lead to incorrect information leakage into SLMs? How can we ensure that LLMs only enhance information relevant to the current medical issue without introducing additional errors or irrelevant information? This is a very important issue in the medical field, as it directly relates to patient diagnosis.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studied medical QA problems by incorporating large language models (LLMs) to assist small-language models (SLMs). To protect the private information in the data, the authors propose to first extract keywords and then use the keywords to query LLMs for intermediate content which can be used for SLMs to enhance prediction accuracy.

### Strengths
1. (originality) The proposed method is novel by extracting keywords and privately incorporating LLM for SLM-based predictions.
2. (clarity) Overall, the paper is fair in presentation. The demonstrations of synthetic medical data with private information and extracted keywords are helpful for understanding the concepts.
3. (significance) Versus the compared baselines, the proposed methods significantly improve the prediction accuracy on three medical QA tasks.
4. (quality) The authors thoroughly evaluate the performance of the proposed method.

### Weaknesses
1. (Clarity) There is no specific definition of the private information. From Figure 1, it seems that privacy definition is restricted to private identifiable information (PII). The authors should clarify the scope of privacy risks. Importantly, the proposed method cannot address general private information leakage that is considered by strict formulations like differential privacy.
2. (Quality) The evaluation of privacy is not strict.
  - Risks: It is possible that the keyword extraction includes private identifiable information (PII), for instance, names and dates as shown in Figure 1. There is no theoretical guarantee for privacy protection or empirical evaluation of the leakage rates of such PII.
  - Metric: The authors used the privacy budget for quantifying privacy risks:  the ratio of the number of words provided to the LLM to the total words in the original question. However, I doubt if the metric can imply some privacy risks. There essentially lacks an intuitive explanation of the relationship between the privacy budget and privacy risks.
3. (Motivation) As the authors said, SLM presents a large gap compared to LLMs and thus there is no clear motivation to use SLM for prediction. Although the authors mention that ChatGPT requires access to data, it is essentially ignored that open-source LLMs, for example, Llama, can be used. In the paper, there is no referred evidence for the large gap between open-source LLMs and ChatGPT on the concerned medical tasks. Thus, I strongly doubt if the motivation of the paper can hold.

### Questions
* There is no clear motivation to see SLM for prediction. Although the authors mention that ChatGPT requires access to data, it is essentially ignored that open-source LLMs, for example, Llama, can be used. Is there any evidence for the large gap between open-source LLMs and ChatGPT on the concerned medical tasks?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tried to improve the performance of small medical language models by introducing knowledge from large language models, which keeps the privacy of clinical text when using large language models.  The proposed method uses keywords instead of full raw text to generate initial evidence from LLM and feed the evidence to small language model.

### Strengths
Privacy-preserving is an essential and common need when using LLM in clinical text. This paper tried to solve this problem by using keywords instead of raw text, the idea is novel and experiments demonstrated the effectiveness of this approach.

### Weaknesses
1. As this research utilized a named entity recognition model to extract keywords, it is possible that the NER model can extract privacy information such as patient names. Is there any filtering or postprocessing step to avoid that? In addition, it is not guaranteed that NER system will never extract sensitive patient information; for example, if the NER system incorrectly extracts a patient's address as a symptom, then the address may be leaked to LLM. Although it is very rare, it is still necessary to comment on this. 
2. As the LLM already provides a preliminary decision, I am curious about the performance if we only feed the preliminary decision from LLM to SLM. It is worth knowing which part of the LLM-generated information improves the SLM most. 
3. The related work section need to discuss more LLM application in the clinical area, especially the knowledge-enhanced LLM in clinical settings. For example, paper "Qualifying Chinese Medical Licensing Examination with Knowledge Enhanced Generative Pre-training Model." also utilized external knowledge for clinical questions. 
4. By adding the LLM-generated content, will the new concatenated input be too long and out of the word window in SLM? How do you deal with the long content problem?

### Questions
By adding the LLM-generated content, will the new concatenated input be too long and out of the word window in SLM? How do you deal with the long content problem?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article discusses a method to improve the application of SLM in the medical field, utilizing LLM's medical proficiency to boost SLM performance in medical tasks under privacy-restricted scenarios which has important social significance. The method was tested on MedQA, HEADQA, MedMCQA, and MMLU-professional medicine datasets, showing some improvements over existing methods. Additionally, the authors compared results across different sizes of training sets.

### Strengths
see summary

### Weaknesses
1). Imprecise example of Privacy Protection.
The example in Figure 1 indicates that personal privacy issues are only present in the first sentence, and the key words "man" and "admitted" in that sentence have almost no impact on the subsequent content. Could it then be possible to simply delete the first sentence to achieve privacy protection, as extracting key words here does not seem to play a significant role.

2). Privacy Protection as an Innovation Point
Regarding the extraction of key words for privacy protection, the paper uses a medical NER model proposed by Neumann et al in 2019. We suggest further improvement of this model, for example, considering age as a crucial keyword for certain diseases and extracting it as necessary to better enrich the innovative aspects of the paper.

3). Ambiguity of Symbols in Annotations
Annotation 13 on page 8 only appears in the content of the article but is not explained.

4) The overall innovation of the methodology needs improvement, as the majority of the content relies on existing methods, such as the medical NER (Named Entity Recognition) model.

### Questions
please see the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
