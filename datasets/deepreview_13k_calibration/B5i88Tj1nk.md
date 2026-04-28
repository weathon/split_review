# AIM: Adversarial Information Masking for Evaluating EEG-DL Interpretations

- Decision: Reject
- Avg Score: 4.67
- Scores: 8, 3, 3

## Abstract
We identify significant gaps in the existing frameworks for assessing the faithfulness of post-hoc explanation methods, which are essential for interpreting model behavior. To overcome these challenges, we propose a novel adversarial information masking (AIM) approach that enhances in-distribution information masking techniques. Our study conducts the first quantitative comparison of faithfulness assessment frameworks across different architectures, datasets, and domains, facilitating a comprehensive evaluation of post-hoc explanation methods for deep learning of human electroencephalographic (EEG) data. This work lays a foundation for further developments of reliable applications of explainable artificial intelligence (XAI).
The code and sample data for this work are available at https://anonymous.4open.science/r/EEG-explanation-faithfulness-5C05.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present approaches on how to mask EEG input data in spatial, frequency and temporal domains. The aim of this masking is faithfulness evaluation of attribution maps. The present novel ideas for masking in the temporal domain, also with likely a novelty for the frequency domain. Besides conventional approximate in-distribution masking they also evaluate masking by copying from adversarially crafted samples. The present results for several networks and several attribution methods. They investigate the question whether the sign of attribution maps carries information and investigate an unexpected result in the frequency domain.

### Strengths
It is a reasonable application study about faithfulness evaluation for a particular field - which is an acceptable type of invention. A good set of experiments in three domains, also for multiple networks. They measure also consistency in the sense of rank correlations.

### Weaknesses
In particular for the temporal domain, but also for the frequency domain, trying out different non-adversarial masking methods would make the evaluation more interesting. For the temporal domain that would be different stochastic processes.

It might be fair to cite https://www.nature.com/articles/s42256-023-00620-w .

### Questions
What are the footnotes in Table 2 ?

It might be fair to cite https://www.nature.com/articles/s42256-023-00620-w .

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the problem of evaluation of post-hoc explanations in the context of models trained on EEG decoding tasks. 
In particular, it focuses on the evaluation of faithfulness of explanations and proposes a novel framework involving multi-domain adversarial information masking (AIM) based on Multi-Domain Adversarial Robustness (mdAR), which overcomes some of the limitations of standard faithfulness evaluation approaches. The framework is validated on multiple model architectures and EEG datasets.

### Strengths
The paper addresses a relevant problem, namely evaluation of post-hoc explanations. The paper is original in the sense that it proposes two imputation techniques specifically tailored for multivariate EEG data. The proposals are based on the ROAD and AR frameworks as the  and carefully integrate the spatial, spectral and temporal dimension of multivariate EEG data. The overall originally and quality of the proposed approach is rather limited and specific to models trained for EEG analysis. It is unclear how to generalise the approach beyond this specific application domain.
The paper is well written and easy to understand. The experimental evaluation is ok, but could be more detailed and deep. Currently it is not clear how follows, e.g., from the results in Table 2 or 3.
Overall, the contribution is rather incremental and will probably be of interest / significance only to a limited (EEG) community.

### Weaknesses
The contributions of the paper are very specific and may be of interest to a limited community, mainly only researchers training and explaining NN for EEG analysis. There has been a lot of research on faithfulness evaluation of explanations. The proposed method represents an incremental contribution to this field. The experimental evaluation is not 100% convincing. It is unclear to me what follows from the evaluation results. Shall we only use some of the methods which perform well in Table 2 for the analysis of EEG-based explanations? Are the results consistent with other evaluation approaches? What are the consequences of the evaluation for the practioner?.
Currently, the paper reads to me as proposing yet another faithfulness evolution metric, here specifically for EEG analysis tasks. The overall originality of the contribution and relevance for the ICLR research community is rather limited. Therefore I recommend "reject".

### Questions
What follows from the evaluation results?
What are the consequences for the practitioner?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The manuscript aims to contribute to the evaluation of interpretations of deep learning models applied to EEG. It does so by identifying issues with traditional adversarial robustness evaluation for EEG and proposing alternative information masking methods to evaluate the faithfulness of feature attribution methods. Their framework is able to differentiate between attribution methods on spatial, temporal, and spectral domains and thereby seem to generate useful findings for the field. Such progress is valuable as explainability of neural networks in EEG data is not well-studied.

### Strengths
-	Addresses a real gap in the EEG/DL field
-	Seems to generate useful findings
-	Three EEG domains are considered

### Weaknesses
1.Writing: Unfortunately, the level of the writing of the manuscript is poor. Especially the first half of the paper, outlining the motivations, prior literature, and outline of the paper, is difficult to follow. The paper could really benefit from another thorough round of editing as the many grammatical errors lead to semantic ambiguity. A few examples that I am unable to understand:
a. L218-219: ‘ability to exert data distribution’
b. L220-221:‘computationally exhaustive while remain biased or uncontrollable’.
c. L271-273: "(…), whose value are concluded to reflect certain series trend.”
Also the experiments are hard to follow and it is difficult to assess the contributions of this work. 

2. Evaluation: Is it possible to perform some form of cross-framework comparison? It is difficult to understand the advantage of the proposed framework over existing ones. For example, why did the authors choose not to analyze where and why frameworks agree or disagree? Would synthetic data enable a comparison between frameworks? Understanding both the advantages and disadvantages of this new framework would be very valuable.

Minor:
- It might be useful to briefly describe what the the proposed metrics (AOC, ABC) conceptionally mean and how they differ.
- Recent work on EEG-DL concerns the use of large amounts of resting state data for clinical predictions (e.g. [1-3]). Do the authors believe the proposed framework could be relevant for such work as well? Understandably, task-based explanations are easier to verify and interpret. However, the datasets used by the authors are small, while it may be argued that deep learning models may be particularly interesting in case of larger datasets, which to my knowledge tend to be resting-state.

### Questions
- Improve clarity and style of writing
- Be more concise in your contributions 
- Evaluate your framework with respect to other frameworks
- Give more context regarding the EEG experiments and show more example attributions

### Soundness
2

### Presentation
1

### Contribution
2
