# Interpretable Vision-Language Survival Analysis with Ordinal Inductive Bias for Computational Pathology

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Histopathology Whole-Slide Images (WSIs) provide an important tool to assess cancer prognosis in computational pathology (CPATH). 
While existing survival analysis (SA) approaches have made exciting progress, they are generally limited to adopting highly-expressive architectures and only coarse-grained patient-level labels to learn prognostic visual representations from gigapixel WSIs. 
Such learning paradigm suffers from important performance bottlenecks, when facing present scarce training data and standard multi-instance learning (MIL) framework in CPATH. 
To overcome it, this paper, for the first time, proposes a new Vision-Language-based SA ($\ours$) paradigm. 
Concretely, (1) $\ours$ is driven by pathology VL foundation models. It no longer relies on high-capability networks and shows the advantage of \textit{data efficiency}. (2) In vision-end, $\ours$ encodes prognostic language prior and then employs it as \textit{auxiliary signals} to guide the aggregating of prognostic visual features at instance level, thereby compensating for the weak supervision in MIL. Moreover, given the characteristics of SA, we propose i) \textit{ordinal survival prompt learning} to transform continuous survival labels into textual prompts; and ii) \textit{ordinal incidence function} as prediction target to make SA compatible with VL-based prediction. 
Notably, $\ours$'s predictions can be interpreted intuitively by our Shapley values-based method. 
The extensive experiments on five datasets confirm the effectiveness of our scheme. Our $\ours$ could pave a new way for SA in CPATH by offering weakly-supervised MIL an effective means to learn valuable prognostic clues from gigapixel WSIs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a Vision-Language-based Survival Analysis (VLSA) paradigm to improve cancer prognosis prediction from histopathology whole-slide images by leveraging pathology foundation models for enhanced data efficiency and weakly-supervised learning. VLSA incorporates prognostic language priors and ordinal survival prompts to guide visual feature aggregation. The authors have conducted multiple experiments and ablation studies to evaluate the method proposed.

### Strengths
Overall, the paper is well-written and tries to address an important challenge in digital pathology. The proposed solution seems to also outperform the reported benchmark in the paper.

### Weaknesses
Major Comments:
1. The introduction to the paper highlights data scarcity for survival analysis as a major problem that this paper claims to solve. However, it seems like this paper addresses data efficiency in terms of model size and MACs, not the limited amount of training data available for survival analysis. The core issue is that the paper conflates computational efficiency (model size, MACs) with data efficiency (performance with limited training samples). The authors need to clarify how their method specifically addresses the challenge of limited training data, beyond simply using a smaller model.
2. The number of bins being set at sqrt(N events) is given little justification. It also calls into question the comparison with other models (eg. PatchGCN used 4 bins for all datasets in the original paper). Additionally in the Appendix “Comparison with Hazard-Based Survival Modeling” 4 bins were used as opposed to the number used in the original experiments. The additional experiments in Appendix E don’t provide sufficient justification for using uniform sqrt(N events). The choice of bin size significantly impacts survival analysis, and the paper needs a more thorough investigation into the impact of this parameter, including a comparison with other binning strategies.
3. PatchGCN was trained on 4 bins in the original paper. The VLSA model should be compared with the baselines with the different bin sizes being considered for a fair comparison. It is crucial to evaluate the VLSA model against baselines under identical conditions, including the number of time bins. The current comparison is not entirely fair, as the models are evaluated with different binning strategies.
4. Given the variability of survival evaluation metrics (eg c-index) and the fairly marginal improvement over the baselines the authors should do a deeper analysis to showcase the improvements of their model. This could be done by plotting the survival curves of “high-risk” vs “low-risk” cases. The c-index is a limited metric, and the authors should provide more visual and intuitive evidence of their model's performance, such as Kaplan-Meier curves for risk groups.
5. In Appendix E, there appear to be patches comprising of mostly white-space. Was any preprocessing done to filter out patches like this, or patches with significant blur or artifacts. The presence of such patches could negatively impact model performance, and the authors should clarify their preprocessing pipeline and justify the inclusion of these patches.

Minor Comments:
Spelling error at line 44 “While existing approaches have made exciting progress…”
In Appendix Table 6, there seems to be little point in labeling the maximum values.

### Questions
mentioned in weaknesses.

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
This paper aims to overcome two challenges in survival analysis including overfitting due to data scarcity in CPATH, and insufficient supervision for survival analysis. To address the challenge of scarce training data, the authors proposed to apply visual-language models to survival analysis by utilizing the power of the recent VL pathology foundation model. To compensate for supervision signals, the authors introduced some extra prior descriptions of prognosis by querying GPT-4o. Some ordinal prompts are designed to adapt VL models to survival analysis, although their performance improvements are marginal.

### Strengths
1. This is the first work to adapt the VL foundation model to survival tasks by designing ordinal prompts tailored to survival analysis tasks.
2. The introduction of prognostic prior description was empirically validated to significantly improve the performance of survival analysis.
3. The motivation is basically clear although the design of the ordinal incidence function is a bit confusing.
4. Interpretation brought by language priors for survival tasks is interesting and makes the prediction more transparent.

### Weaknesses
1. The motivation of ordinal IF is confusing. The authors assume there is a consecutive decline in probability for those classes away from the time when the event occurs, which raises doubts about its reasonableness when events occur multiple times. This assumption is only concerned with the event that first occurs. 
2. Ordinal Survival Prompt seems to ignore the status of event indicators (i.e. censorship) when designing the prompts. For different censorships, there should be different outcomes reflected in the survival prompts even when their follow-up time are the same. When the case is censored, the only thing we can know is the event didn’t occur before the follow-up time. For example, we cannot simply assign a case with a short follow-up time into a bin of “very poor prognosis”.
3. Experiment comparison is **NOT** adequate in the following aspects:

    a. To validate the effectiveness of prompts tailored to survival tasks, a stronger baseline equipped with naive prompts that simply formulate survival tasks as classification tasks, should be compared.

    b. **To support the authors’ claim that "highly-expressive modern networks may cause overfitting when facing present small WSI data”**, the current “highly-expressive” models should be compared with the proposed method. Furthermore, the extra text description generated by GPT-4o should be an additional modality. Therefore, some representative multimodal survival models should be compared, **which can validate the efficacy of utilizing the pathology foundation model**. I understand there have been a few models that integrated WSI and text data in the past. However, by replacing the gene data with text data, some multimodal survival models using WSI and gene data can be adapted for comparison, e.g. MCAT [1], MOTCat [2], MMP [3] etc.

    c. Unimodal MIL models are a bit out-of-date. More “highly-expressive” SOTA methods should be compared, such as CAMIL[4], R2T [5], etc.

4. From the results of Tables 3 and 8, performance gains from two ordinal prompts are marginal or even getting worse. The reason should be justified.
5. Comparisons in Few-shot learning may not be fair. The capability of few-shot prediction greatly relies on how the visual and text spaces are well-aligned. CONCH is a pathology VL model that aligns visual and text spaces well. However, CoOp and OrdinalCLIP are equipped with ABMIL, which is not aligned with the text space, for few-shot prediction by using such few samples. For a fair comparison, the author should replace prompts with the ones in CoOp and OrdinalCLIP only based on CONCH to validate the efficacy of survival prompts.
6. The code is unavailable which may affect the reproduction.

### Questions
1. I‘m not sure how the authors applied MI-Zero to survival analysis, which was supposed to be designed for classification.
2. What’s the difference in prompts between OrdinalCLIP and Ordinal Survival Prompt?
3. In equations 2 and 3, how can the model ensure learning multi-level representations? It seems there is no constraint to achieving this goal.
4. CONCH is a large foundation model pretrained on a great amount of data including public data. In this case, to avoid data contamination, how can the author ensure test samples never occur in the pretraining materials of CONCH in the few-shot setting?
5. I’m confused about what the specific events are referring in these experiments. If overall survival, there should be only one event. However, the authors mentioned that the events can occur multiple times. Is it longitudinal data?
6. The motivation for using EMD should be elaborated. For example, why is EMD aware of ordinality?
7. It is difficult to understand Figure 3(a) is trying to explain. What do the horizontal and vertical axes represent, respectively?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a Vision-Language-Based survival analysis (VLSA) paradigm, addressing two key challenges: data scarcity and weakly supervision of gigapixel whole slide image (WSI) analysis. The framework leverages foundational vision-language models with three key innovations: (1) language-encoded prognostic priors to guide instance aggregation, (2) ordinal survival prompt learning for encoding continuous time-to-event labels, and (3) ordinal incidence function prediction. The approach demonstrates strong performance improvements while maintaining interpretability through Shapley values.

### Strengths
1.	The authors have proposed a complete framework for VLM-compatible survival analysis, with novel components for handling continuous time labels and maintaining ordinal relationships
2.	The comprehensive experiments demonstrate the efficacy of the method and each proposed module through thorough ablation studies
3.	The method incorporates interpretability using Shapley values, which is crucial for clinical applications, and provides explanations through natural language descriptions

### Weaknesses
1.	The fundamental necessity of language priors for addressing data scarcity requires stronger justification. While the authors argue that language priors can mitigate data scarcity, they do not sufficiently demonstrate why this approach is superior to using large-scale vision-only foundation models (e.g., UNI). A direct comparison with vision-only approaches, controlling for feature dimensionality and pretraining dataset size, would strengthen this argument. The current comparison lacks a rigorous evaluation of the isolated impact of language priors.
2.	The experimental validation has some limitations in terms of baseline comparisons. The pre-trained VLMs used for comparison (CoOp, OrdinalCLIP) are trained on natural images rather than pathology data, leading to a suboptimal performance. This introduces a confounding variable, making it difficult to isolate the true contribution of the proposed method. The comparison should ideally include VLMs pre-trained or fine-tuned on pathology data to ensure a fair evaluation.
3.	The survival analysis evaluation omits standard clinical protocols, notably Kaplan-Meier analysis and statistical significance testing between risk stratification groups. It would be better to see these experimental results and analysis, including hazard ratios and confidence intervals, to assess the clinical relevance of the findings.
4.	The comparative analysis excludes several state-of-the-art methods in WSI classification, including DTFD-MIL [1], HAG-MIL [2], MHIM-MIL [3], and recent VLM approaches such as TOP [4] and ViLa-MIL [5]. The absence of these comparisons makes it difficult to contextualize the performance of the proposed method relative to the broader landscape of WSI analysis techniques.

Miscellaneous:
1.	The terminology regarding "cross-attention" in line 163 requires revision, as similarity matching differs from the so-called cross-attention mechanisms
2.	Figure 1 contains rendering issues in “context prompt” that should be addressed

### Questions
1. The paper focuses on vision-language models while foundational vision models like UNI [1] have shown strong performance in computational pathology. Could the authors discuss their rationale for prioritizing vision-language models and perhaps provide comparative experiments with vision-only foundation models to better justify this architectural choice?
2. Given the recent success of multimodal approaches in survival analysis (e.g., MCAT [2], MOTCAT [3], CMTA [4], MoME [5]), could the authors address why these methods were not included in the baseline comparisons? A comparison with these state-of-the-art multimodal methods would help better contextualize VLSA's contributions to the field.
3. To strengthen the clinical relevance of the results, could the authors provide Kaplan-Meier survival curves for risk stratification groups, along with appropriate statistical significance tests (e.g., log-rank test)? This would help validate the model's practical utility in clinical settings.
4. Regarding the experimental comparisons within the VLM group, the baseline models (CoOp and OrdinalCLIP) were originally trained on natural images rather than pathology data. Could the authors discuss how this might affect the fairness of the comparisons and perhaps provide additional experiments with VLMs specifically trained or fine-tuned on pathological images?

[1] Towards a General-Purpose Foundation Model for Computational Pathology

[2] Multimodal Co-Attention Transformer for Survival Prediction in Gigapixel Whole Slide Images

[3] Multimodal Optimal Transport-based Co-Attention Transformer with Global Structure Consistency for Survival Prediction

[4] Cross-Modal Translation and Alignment for Survival Analysis

[5] Mixture of Multimodal Experts for Cancer Survival Prediction

### Soundness
2

### Presentation
3

### Contribution
2
