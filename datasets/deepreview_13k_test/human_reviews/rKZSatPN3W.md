# Is classification all you need for radiology report generation?

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Automatic radiology report generation is an advanced medical assistive technology capable of producing coherent reports based on medical images, akin to a radiologist. However, current generative methods exhibit a notable gap in clinical metrics when compared to medical image classification. Recently, leveraging diagnostic results to improve report quality has emerged as a promising approach. We are curious whether training a classifier that encompasses all possible long-tailed and rare diseases could enhance the robustness of reports. To investigate this question, this study designs an evaluation framework that integrates long-tail scenarios and summarizes potential combinations of LLM-based report generation models. We assess the impact of classification on report quality across four benchmarks. Initially, we introduce LLM-based language and clinical metrics and develop a pipeline to evaluate the model's performance on both in-domain and out-of-distribution (OOD) long-tail scenarios. Subsequently, we conduct a systematic evaluation of all potential model combinations. Our findings reveal that: 1) the impact of classification on report quality is positively correlated with the performance of classifiers, but the gap still exists, and 2) while classification can enhance report quality in in-domain long-tail scenarios, its benefits for OOD scenarios are limited.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper discusses how radiology report generation is currently less clinically accurate than image classification for the purpose of medical diagnoses. It focuses on a model framework that integrates a classifier trained on common and rare diseases into an LLM with a vision encoder to generate radiology reports. The findings revealed that classification can improve report quality for in-domain diseases but struggles with out-of-domain diseases.

### Strengths
- Large range of LLMs, vision encoders, etc. tested on sufficiently representative datasets.
- Wide variety of metrics used for evaluation.
- Extensive experimentation on the specific effects of classification in report generation.

### Weaknesses
- In addition to case studies, it would be helpful to include quantitative measures of the extent of hallucinations in the OOD experiments.
- To reduce overreliance on classification outputs in particular, it might be more helpful to experiment with controlling the weight of the classifier or including other types of information (e.g. location, severity). However, this was mentioned as part of the limitations.

### Questions
- Optional suggestion: have you looked into also using the GREEN metric? https://arxiv.org/pdf/2405.03595.
- Minor edit: "purple text" on page 9 appears to be red instead of purple - it might be helpful to use a different shade.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the question: will a classifier enhance LLM-based report generation models' performance in long-tail OOD scenarios? The authors explore different architectures on the combination of vision encoders, classifiers, and LLM, and perform lots of experiments. They get the findings that classification can enhance report quality in in-domain long-tail scenarios but is bounded by the performance of the classifier.

### Strengths
1. Many research focuses on  LLM-based report generation models, which is an important task for the medical AI domain, the question this paper investigated may provide some useful information for future research.  
2. The research comprehensively evaluates different architectural combinations (vision encoders, classifiers, and LLMs) across multiple diverse datasets (MIMIC-CXR, CXR-LT, PadChest, and IU X-Ray).

### Weaknesses
1. The comparison between the four baseline models lacks analysis. The metrics give inconsistent results, how could the author get the results that C+V+LLM is better than V+LLM, and the comparison between Refining and C+V+LLM, giving statistical significance analysis of the results would be helpful.

2. The poor performance of the 'Expanding' approach may be due to the prompt rather than inherent limitations.  I do not find details about the prompts used (apologize if I overlooked them). The 'Expanding' prompt should include standard medical report templates to prove a fair comparison.

3. The classifier only provides binary disease presence information without crucial details like location and severity. This limitation makes hallucinations in LLM-generated reports inevitable when using classification-only inputs. Instead of comparing with these inherently limited training-free approaches, the paper would be more valuable if it explored different variants of end-to-end Vision + LLM full training. 

4. The paper's title 'Is classification all you need for radiology report generation?' raises a clear question, but fails to provide the answer. While the findings show that classification helps with in-domain cases but struggles with OOD scenarios, the paper leaves crucial questions unanswered: Is better classification the solution? Or should we focus on pursuing end-to-end training approaches? If the answer is ' we need better classification models', then everyone knows it.

### Questions
1.  Have you optimized the Expanding and Refining prompt? we can't tell whether the performance difference is due to this method not being good enough or the prompt being the problem.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Current RRG systems exhibit a notable gap in clinical metrics when compared to classification models. The authors investigate whether training a classifier that encompasses all possible long-tailed and rare diseases could enhance the robustness of reports. Key findings show that classification helps improve report quality in in-distribution settings but exhibits limited benefits in OOD scenarios.

### Strengths
1. The paper evaluates whether classification models can help improve the quality of radiology reports. This is a novel and interesting insight, with potential for aiding in real-world clinical workflows.
2. The authors perform extensive evaluations across different strategies for incorporating classification information as well as in-domain vs. OOD settings. 
3. The authors also introduce novel LLM-based metrics for assessing the quality of radiology reports, which evaluate how well reports capture long-tail observations. This metric is an interesting contribution and has potential for aiding future works in the domain of radiology report generation.

### Weaknesses
The key weakness of this paper is inadequate evaluations, as discussed below.

1. **Inadequate evaluations of classifier:** The incorporation of the classifier is inadequately evaluated, making it difficult to understand the settings in which incorporating a classifier is useful, as detailed below. The paper could have benefitted from more nuanced insights on when including the classifier helps vs. detracts from the quality of generated reports.

    a. **Classifier Performance:** Although the incorporation of the classifier is the key contribution of this paper, the authors do not provide any evaluations on the quality of the actual classifier. What conditions does the classifier perform well on and which conditions does the classifier perform worse on? Does this correlate with report generation performance on the subset of images with particular conditions when the classifier is included? Does improving the performance of the classifier improve report generation quality? In OOD settings, the evaluated classifier displays poor performance  (12.0-14.0 F1 points), and as a result, it is not surprising that incorporating the classifier will not result in benefits to the RRG model in OOD settings; does this result change if the classifier is instead trained on the PadChest or IU X-ray datasets? All of these questions are critical for understanding when/how classification helps in RRG, but none of these are evaluated.

    b. **Upper Bound:** It would be useful to establish an upper bound on performance of the report generation model by utilizing an “oracle” classifier (i.e. a hypothetical classifier that predicts every condition correctly). This would establish whether classification, in the optimal setting, makes useful contributions to the report generation task. As of now, the evaluations are limited by the poor performance of the evaluated classifier, and the key findings/takeaways from the paper are based on this specific classifier.

2. **Inadequate evaluations of proposed metrics:** Although several new metrics are presented as key contributions of this paper, the quality of these metrics is not evaluated. How accurate is the OpenAI GPT-4o model at extracting disease categories? Did the authors check for false negatives / positives in this extraction procedure? Does this metric align with ground-truth labels for the conditions where labels are provided? Evaluating the quality of the metrics via a dataset like ReXVal would have been useful [1].

[1] https://physionet.org/content/rexval-dataset/1.0.0/

### Questions
My questions are detailed above in the weaknesses section.

### Soundness
3

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
5

### Summary
The paper explores the use of classification models in enhancing radiology report generation, specifically examining if a classifier encompassing all possible radiological findings can improve the robustness of generated reports. The study finds that while classification models improve report quality in in-domain scenarios, their impact is limited in out-of-distribution (OOD) settings, especially for long-tail disease categories. The authors propose a comprehensive evaluation framework with novel LLM-based metrics and conduct experiments across multiple benchmarks, concluding that classification aids in in-domain accuracy but may introduce errors in OOD cases due to model biases.

### Strengths
The study tackles a critical challenge in medical AI—how to generate reliable and clinically relevant radiology reports that generalize well across diverse clinical scenarios. By showing that classification models can enhance in-domain performance while introducing potential errors in OOD settings, this paper offers valuable insights into the limitations and trade-offs of using classification-aided generation models. The paper is well-structured, with each section building logically upon the previous one. The problem formulation, methodology, and experimental setup are clearly articulated, enhancing accessibility for readers. The experimental design is thorough, incorporating multiple benchmarks and a diverse set of evaluation metrics, including novel LLM-based metrics, to assess model performance across both in-domain and OOD settings. The rigorous use of benchmarks and detailed comparisons with existing methods underscore the study's robustness and the reliability of its findings.

### Weaknesses
The primary weakness of this work lies in its motivation, or key argument, which has already been discussed in a prior publication that is not referenced in this submission. The previous study, Medical Report Generation Is A Multi-label Classification Problem (Fan et al., IEEE MedAI 2024), introduces a similar concept: that classification accuracy significantly impacts the quality of medical report generation. Both works share the same foundational idea, though they differ in specific model designs and classification categories. From a performance perspective, the previous work, which uses a cross-attention approach, demonstrates better outcomes and introduces the concept of ceiling performance. This concept suggests that the theoretical upper bound for this approach would be achieved if all ground-truth labels were provided to the model, given that real-world classifiers cannot reach 100% accuracy. 

While this submission’s strength lies in its extensive experiments, broader metrics, and a variety of models, its core insights are similar to the prior work, without addressing ceiling performance or providing a comparison to it. Additionally, the reason why the 28 classification categories used in the previous study outperform disease-based categories is not examined here. These points, along with further experimental and discussion-based additions, would significantly enhance the paper.

### Questions
please read the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2
