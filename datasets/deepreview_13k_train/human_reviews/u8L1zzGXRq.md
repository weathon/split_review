# Impact of Molecular Representations on Deep Learning Model Comparisons in Drug Response Predictions

- Decision: Reject
- Scores: 5, 1, 3, 3

## Abstract
Deep learning (DL) plays a crucial role in tackling the complexity and heterogeneity of cancer, particularly in predicting drug response. However, the effectiveness of these models is often hindered by inconsistent benchmarks and disparate data sources. To address the gaps in comparisons, we introduce CoMParison workflow for Cross Validation (CMP-CV), an automated cross-validation framework that trains multiple models with user-specified parameters and evaluation metrics. The effectiveness of DL models in predicting drug responses is closely tied to the methods used to represent drugs at the molecular level. In this contribution, we benchmarked commonly leveraged drug representations (graph, molecular descriptors, molecular fingerprints, and  SMILES) to lean and understand the predictive capabilities of the models. We compare the ability of different drug representations to encode different structural properties of the drugs by using prediction errors made by models in different drug descriptor domains. We find that, in terms of the average prediction error over the entire test set, molecular descriptor and encoded SMILES representations perform slightly better than the others. However, we also observe that the rankings of the model performance vary in different regions over the descriptor space studied in this work, emphasizing the importance of domain-based model comparison when selecting a model for a specific application. Our efforts are part of CANcer Distributed Learning Environment (CANDLE), enhancing the model comparison capabilities in cancer research and driving the development of more effective strategies for drug response prediction and optimization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an automated cross-validation framework for drug response, coined CMP-CV, which trains multiple models with user-specified parameters and evaluation metrics. To achieve this, this paper benchmarked the commonly utilized drug representations (graph, molecular descriptors, molecular finger prints, and SMILES) on the proposed CMP-CV. The authors analyzed the results in various evaluation metrics, including average prediction error.

### Strengths
- The paper is well-written and easy to understand.
- The paper studies an important task of ML for drug discovery, which suffers from the lack of general benchmarks for evaluation.

### Weaknesses
 - Unclear contribution: The paper compares existing methods based on the already proposed dataset. The evaluation metrics are also common, e.g., AUC, prediction error.  It is unclear which parts are the main contribution of this work.

- Insufficient analysis: Although figure 2 and table 2,3,4 seem interesting, the paper only presents the results without analysis, e.g., hypothesis or justification.

- Lack of descriptions about core technique: This paper repeatedly refer CANDLE framework. However, the description in Section 3.2 does not provide sufficient information to understand the framework.

- Lack of comparison with other benchmarks: There are several benchmarks for drug discovery, e.g., [1], [2]. However, there is no comparison about those works.

### Questions
- What does the overlapped vertical bar mean? (in Figure 3, Morgan-ATSC7p and ExtraTrees-ATSC7p)

- Please provide the more description of CANDLE framework and the contribution of this paper upon (or based on) the CANDLE framework.

- What is the main novelty of this work? In other words, what was the main difficulty to make this benchmark? Isn't this work a simple combination of existing methods, dataset, and evaluation metrics?

- What is the main advantage of this benchmark, compared to prior benchmarks [1,2] for drug discovery?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Certain models for drug response predictions favour certain drug representation, and this is a recurring problem in feature-based drug prediction tasks. This paper studies the inductive bias of drug representation in drug response prediction tasks.

The authors demonstrate that molecular descriptors and SMILES strings are effective drug representations for drug response prediction tasks.

### Strengths
The problem of studying the inductive biases for drug response prediction is interesting and relevant in drug discovery. I found the analysis on the effectiveness of certain representations across drug domains interesting, for example, the takeaway that the descriptor and morgan representation models are more effective with highly soluble drug candidates is neat. This includes the importance measure of molecular descriptors that are tightly captured by certain representations.

### Weaknesses
The biggest weakness of this work is the writing. I found the writing to be very difficult to follow. Couple points:

- Why is the method (CMP-CV) left to the end of the paper after the results?
- It required a few reads to disambiguate between feature space, representation, molecular descriptors, drug domains, and drug regions. I think in the next iteration of this work, time needs to be invested to expand on the different terminology used in this paper. 
- In Figure 1, why are the duplicates in the x-axis and the legend?
- In Page 4, section 2.3.1, paragraph 2, is it not rather that the ML model appears to perform better when the log S of the drug is *more* than -7 ?
- In Figure 1&2, why do refer to the Area Under the Roc Curve (AUC), when the results are for the R2, RMSE and MAE ?

I am also still unsure what is the CMP-CV workflow exactly. It seems to be more of an engineering effort, that is largely handled by the CANDLE framework?

### Questions
Could the authors help me understand what is the key contribution of the CMP-CV workflow? It appears to be a hyperparameter sweep that is commonly used to evaluate machine learning models.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an empirical study aimed at analyzing the performance of existing deep learning models for drug response prediction. The authors introduce CMP-CV, a framework for cross-validating multiple deep learning models using user-specified parameters and evaluation metrics. This study utilizes the CTRPv2 dataset to compare eight models across four different molecule representations. The experimental results highlight the significant impact of molecular representation on the prediction performance of deep learning models for drug response prediction.

### Strengths
- This paper addresses an important application of machine learning in drug discovery.

- The authors provide the code necessary for reproducing the experiments.

### Weaknesses
 - While the paper offers some insights into existing machine learning models, its technical novelty within the machine learning context is somewhat restricted. In particular, its primary contribution lies in error analysis to find which areas in the drug space the ML models does not achieve good performances rather than shedding a light on developing novel methods to enhance prediction performance for drug response. This aspect may fall short of the acceptance criteria for ICLR.

- The conclusion that molecular representation significantly influences drug response prediction performance appears to be straightforward and lacks novel insights for the ML-based drug discovery community.

### Questions
Please see the Weaknesses.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Using the CTRPv2 dataset and a training orchestration system called CMP-CV, the authors train different deep learning architectures using different molecular representations, then perform an exploratory data analysis on the errors those models make, slicing up the errors by different molecular properties. They show that the error distributions are non-uniform across these properties.

### Strengths
- The authors call to attention to the fact that predictive error is typically non-uniform.

### Weaknesses
 - This paper is primarily an EDA of the errors of trained models, and does not rise to the level of making a contribution significant enough for a main track paper, and is better suited for a workshop.
- The authors use too much space describing CMP-CV, which appears to be a standard job orchestrator, and does not rise to the level of making a contribution. More writing should be dedicated to describing how the metrics were actually computed (see Questions).
- The authors point out the non-uniformity of errors, but do not provide actionable recommendations on how one ought to proceed with this knowledge.
- R2, RMSE and MAE are correlated, no need to show them all in Figure 1.
- The trends for all models in Figures 3 and 4 are roughly the same, suggesting that the non-uniformity in prediction error is due more to the dataset than any choice of architecture or molecular representation.
- The UMAPs of Figure 6 are very uninformative, and do not appear to support the author's point, unless there are many red Xs at each point in the space. The point of this figure could be expressed very differently, perhaps by tanimoto similarities of these clusters compared to average similarity or something like that.
- The point of Tables 2 and 3 could be expressed in just a few lines.
- The paper says that 10 models were trained on 10 random train/val/test splits, which is not standard practice - the test set is usually fixed across all CV splits.

### Questions
- many of the details of how metrics were obtained are left out, e.g.
  - What exactly does each model predict? It seems to be gene expression values, but it is not clear in the paper
  - If expression values, then how do the authors get to single R2, RMSE, and MAE values in Figure 1? The line "This figure delineates the areas where each model exhibited the highest number of errors" is not clear.
- How were the bins of Tables 2 and 3 chosen?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
