# Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Pre-trained transformers are often fine-tuned to aid clinical decision-making using limited clinical notes. Model interpretability is crucial, especially in high-stakes domains like medicine, to establish trust and ensure safety, which requires human engagement. We introduce SUFO, a systematic framework that enhances interpretability of fine-tuned transformer feature spaces. SUFO utilizes a range of analytic and visualization techniques, including Supervised probing, Unsupervised similarity analysis, Feature dynamics, and Outlier analysis to address key questions about model trust and interpretability (e.g. model suitability for a task, feature space evolution during fine-tuning, and interpretation of fine-tuned features and failure modes).
We conduct a case study investigating the impact of pre-training data where we focus on real-world pathology classification tasks, and validate our findings on MedNLI. We evaluate five 110M-sized pre-trained transformer models, categorized into general-domain (BERT, TNLR), mixed-domain (BioBERT, Clinical BioBERT), and domain-specific (PubMedBERT) groups.
Our SUFO analyses reveal that: (1) while PubMedBERT, the domain-specific model, contains valuable information for fine-tuning, it can overfit to minority classes when class imbalances exist. In contrast, mixed-domain models exhibit greater resistance to overfitting, suggesting potential improvements in domain-specific model robustness; (2) in-domain pre-training accelerates feature disambiguation~\footnote{We refer to the clustering of the feature space according to the labels of the input datapoint.} during fine-tuning; and (3) feature spaces undergo significant sparsification during this process, enabling clinicians to identify common outlier modes among fine-tuned models as demonstrated in this paper. These findings showcase the utility of SUFO in enhancing trust and safety when using transformers in medicine, and we believe SUFO can aid practitioners in evaluating fine-tuned language models~(LMs) for other applications in medicine and in more critical domains

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper conducts a case study on the Transformer model on clinical notes, including model fine-tuning, supervised probing, unsupervised similarity analysis, feature dynamics,  and outlier analysis. Results show several interesting points including the usefulness of mixed-domain models, in-domain pre-training helps faster feature disambiguation, and improved identification of missing medical information.

### Strengths
- The study offers a deep dive into understanding the interpretability of pre-trained Transformers within the crucial field of medical data.
- Most of the presented claims can be suppored by experiment results, shedding light on model selection, evaluation, and in-depth analysis processes.
- The paper is well written and easy to follow.

### Weaknesses
 - The datasets used for fine-tuning are somewhat limited in their volume. Exploration with larger datasets, such as the MIMIC-IV clinical notes, might add more depth.
- While the author contends that PubMedBERT is brimming with pertinent data for the tasks at hand even before fine-tuning, the model displays unpredictability when predicting lesser-represented classes post-fine-tuning. Could enlarging the fine-tuning dataset address this challenge?
- The conclusion for Table 2 seems vague. PubMedBERT and BERT perform very similarly and it is hard to conclude that PubMedBERT contains much useful information for the tasks. Also, why the mixed-domian models BioBERT and Clinical BioBERT perform even worse than BERT?

### Questions
See weakness.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a systematic framework, SUFO, to analyze and visualize the utility of five pre-trained transformers towards a pathology classification task, with validation on a public data MedNLI. SUFO is named after the following four aspects in diagnosing transformers: 1) Supervised probing 2) Unsupervised similarity analysis, 3) Feature dynamics visualization and 4) Outlier analysis.

### Strengths
- Originality: the paper proposed a novel evaluation/diagnosing framework, that combines multiple existing ideas and approaches, for the application of five popular pre-trained transformer on a real-world data problem.
- Quality: the paper is well-organized with meaningful and inspiring research questions connecting each part of the paper. Technical analysis is sound with multiple metrics and various comparison aspects, along with intuitive plots to support the claims and conclusions. The hypothesis testing of whether domain-specific transformer will outperform general-trained BERT (even only on a single case study) is very interesting and inspiring. 
- Clarity: the paper is easy to understand with nice writing flows throughout the problem construction, related work, experiment design, results discussion and conclusions. Assumptions and experiment design details are well-documented. 
- Significance: the paper demonstrates solid results and meaningful discussions about application of pre-trained transformers/models for other researchers to refer to, test new hypotheses and build new experiments upon.

### Weaknesses
1. No significant technical weakness, but some weakness or unfulfilled audience expectations in terms of results inclusion/exclusion in the main paper. It is somehow disappointing when the highly expected results are in the Appendix, e.g. feature dynamics comparison mentioned in page 7, but in Appendix A.9 (is it possible to quantify the feature dynamics and compare them in plots like Figure 1, e.g. limit to first and last layer); sparsity comparison of top 2 PCs on page 8 but results in Appendix A.7 (same suggestion to include e.g. 1-2 plots of last layer), etc. 
2. The potential application utility weakness of SUFO might lie in at the end of the transformer diagnosis towards a specific dataset, it is still unclear what transformer should an end user e.g. data scientist, choose from the five? How will SUFO provide robust and actionable insights based on the supervised and unsupervised analysis?

### Questions
1. Since the paper is based on a single datasets, could SUFO evaluate more benchmark datasets and data tasks to perform meta learning and automatically suggest the best pre-trained model given a dataset?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work provides a comprehensive framework for analyzing the pretrained and fine-tuned feature spaces of clinical transformers. The provided analyses include supervised probing, unsupervised similarity analysis, feature dynamics, and outlier analysis.

### Strengths
The authors evaluate five pre-trained transformer models on real-world pathology tasks, offering a multifaceted perspective on the subject. The paper is generally well-written, and the results provide insights for researchers in the medical NLP field.

### Weaknesses
My major comments are:

1. The choice to evaluate the results predominantly on a private dataset, rather than well-established clinical NLP datasets such as MIMIC-III, raises concerns about the reliability and generalizability of the drawn conclusions. Although the authors did incorporate the public MedNLI dataset, they pointed out certain imbalance issues. The principal analyses still predominantly focus on the private pathology dataset.

2. The paper contains an extensive number of tables and figures. It is noted that even some key conclusions are presented in the Appendix. It might be beneficial for the authors to relocate some of the less important content to the Appendix and highlighting major results within the main text.

3. The section evaluating clinical practitioners' perspectives appears to only incorporate feedback from a single practitioner, which is hard to support the claim that the findings in this work increase the interpretability to domain practioners.

### Questions
Please see the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
