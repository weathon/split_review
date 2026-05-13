# A GRAPH-BASED REPRESENTATION LEARNING APPROACH FOR BREAST CANCER RISK PREDICTION USING GENOTYPE DATA

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Breast cancer risk prediction using genotype data is a critical task in personalized medicine. However, the high dimensionality and potential redundancy of genetic features pose challenges for accurate risk prediction. We present a graph-based representation learning pipeline for breast cancer risk prediction. Our method addresses the issue of feature redundancy by developing an ensemble-based feature selection approach. We evaluated the performance of the graph-based approach in a breast cancer risk prediction task using a dataset of 644,585 genetic variants from Biobank of Eastern Finland, consisting of 168 cases and 1558 controls and compared it with the classical machine learning models. Using 200 top-ranked genetic variants selected by the ensemble approach, the graph convolutional network
(GCN) achieved area under the ROC curve (AUC) of 0.986 ± 0.001 in discriminating cases and controls, which is better than an XGBoost model with AUC of 0.955 ± 0.0034

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors presented a graph-based representation learning framework for breast cancer risk prediction using genetic data. They selected informative SNPs by an ensemble approach aiming to capture non-linear and high-dimensional SNP-SNP interactions that aren't possible with linear feature selection approaches, and then used four ML classifiers to evaluate the efficacy of the approach which was compare with graph neural networks. Specifically, the ensemble feature selection combines Chi-square, ANNOVA, decision tree, and Lasso regression.

### Strengths
The overall problem was stated clearly, and the introduction in Section 1 was well-written. The approach itself and the figure illustrations made sense and helped readers understand the material.

### Weaknesses
I believe additional evaluation is necessary for both feature selection and risk prediction tasks (i.e., assessing performance with external datasets and comparing results with existing methods). The significance of the proposed approach remains unclear without sufficient validation and justification. I am uncertain about the extent of the method's transferability to other datasets.

There is a lack of interpretation of the results, e.g., the selected top SNPs. No evaluation or comparison was made for those predictive SNPs. The selection of the number of top SNPs also appears a bit arbitrary although the authors claim it didn't affect the results much.

It is not clear how the proposed feature selection pipeline captures higher-order SNP relationships.

The novelty of the paper seems to be limited as other reviewers mentioned from a methodological point of view.

Certain sections of the paper are unclear, please see my questions below.

1. I don't quite understand how the Hamming distance measures similarity here. If the top SNPs are entirely different between two nodes, even if they have similar values (as coded in 0, 1, 2), it doesn't necessarily mean they are similar. Could the authors clarify this measure?

2. Did the authors control for independence between the training and testing sets, given that they were from the same cohort?

3. In Figure 3, I observe 'top 1000' as the top performer for the ensemble method instead of 'top 200'. The bar doesn't appear to represent a value of 0.986. Could the authors clarify?

4. In Section 2, did the authors intend to say 'SNPs with missing variants greater than 5%' and 'kept the SNPs with linkage disequilibrium of r2 < 0.6'? Normally, people perform LD pruning to reduce the number of SNPs in high LD for feature selection, rather than keeping them.

5. In Section 5.1, which method was used for prediction?

### Questions
1. I don't quite understand how the Hamming distance measures similarity here. If the top SNPs are entirely different between two nodes, even if they have similar values (as coded in 0, 1, 2), it doesn't necessarily mean they are similar. Could the authors clarify this measure?

2. Did the authors control for independence between the training and testing sets, given that they were from the same cohort?

3. In Figure 3, I observe 'top 1000' as the top performer for the ensemble method instead of 'top 200'. The bar doesn't appear to represent a value of 0.986. Could the authors clarify? 

4. In Section 2, did the authors intend to say 'SNPs with missing variants greater than 5%' and 'kept the SNPs with linkage disequilibrium of r2 < 0.6'? Normally, people perform LD pruning to reduce the number of SNPs in high LD for feature selection, rather than keeping them.

5. In Section 5.1, which method was used for prediction?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper performs analyses single neucleotide polymorphism data from a Finnish biobank to predict “breast cancer risk”. Quotations are employed as it’s not clear to this reviewer what the dataset consists of and thus what is actually being predicted (see weaknesses). 

The model employs a range of existing methodologies as part of this analysis. This includes an ensemble of feature selection methods, conventional machine learning models and graph convolutional neural networks. 

A nested cross validation scheme for hyperparameter selection and model training is employed along with an internal test set for validation.

### Strengths
Overall, the application of graph neural networks to this application area is conceptually sensible to model the interactions and correlations between features in SNP data. 

Nested cross validation approach makes sense and should yield reliable evaluation results.

### Weaknesses
It’s not clear from the manuscript precisely what the samples are – i.e. tissue, blood, etc. – and the nature of the clinical follow-up. The paper states that it is performing “breast cancer risk prediction” however it doesn’t actually describe the dataset itself other than minimal information about case and control numbers. 

If indeed the paper is performing risk prediction, I would take this to mean that the genomic samples are all taken from healthy individuals with longitudinal follow-up to establish if they develop breast cancer in the future. There is no details on this given in the manuscript. 

The stated results with a ROC AUC of 0.986 is ludicrously high suggesting that something is not correct about the analysis or problem specification.

### Questions
End of first paragraph: “Such model such a significant amount of time and have varied limitations”. Please clarify what is meant by significant amount of time and be specific about what the limitations are and which you propose to address.

Please describe the samples which are analysed including the analyte type and the nature of the clinical follow-up. Are there any baseline approaches existing already which can establish risk prediction for this cohort using established risk factors? Examples may include: established risk factors: family history, age, HRT, parity, breast density, BMI, alcohol usage, established genentic risk scores.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The manuscript "A GRAPH-BASED REPRESENTATION LEARNING APPROACH FOR BREAST CANCER RISK PREDICTION USING GENOTYPE DATA" presents a method to perform feature selection of genetic data to train a graph neural network for breast cancer risk prediction.

In general the study is solid and introduces into state-of the-art from the domain side.

The main novelty of the manuscript is the way the features (SNPs) are selected. In this process the authors apply a three layer neural network and compare it to 4 additional standard methods (Chi-square test, ANOVA, Decision Tree, and LASSO). The ground truth label in training the ensemble neural network is however the harmonic mean of the 4 standard methods. 

The selected SNPs are then used with three different graph neural network approaches to predict breast cancer risk. 

Overall, the approach is solid, but the novelty is limited, since there have been other graph-based learning approaches for breast cancer risk prediction and the significance of the neural network feature selection is unclear. There are also some problems with the definitions (see below).

### Strengths
Very accessible introduction into the genetics field.

### Weaknesses
The main novelty of the manuscript is the way the features (SNPs) are selected. In this process the authors apply a three layer neural network and compare it to 4 additional standard methods (Chi-square test, ANOVA, Decision Tree, and LASSO). The ground truth label in training the ensemble neural network is however the harmonic mean of the 4 standard methods. In Fig. 3 the performance of the Ensemble method is compared to the single feature selection tasks. To really judge, whether the ensemble neural network approach is a significant contribution, one would however need a comparison to the SNPs ranked by the harmonic mean described above (since this is the ground truth in all supervised selection tasks). Additionally, there is a problem with the statistical evaluation of significance, since one cannot assume independence of folds over the different cross-validation runs, which would be necessary in order to apply the t-test (it is also not shown that the other assumptions of the test are fulfilled.

The SNPs are then used with three different graph neural network approaches to predict breast cancer risk. Here the performance is not compared to state-of-the-art in breast cancer risk prediction.

Furthermore, the performance metric used does not seem ideal for the task at hand, because there is a high class imbalance and (ROC) AUC can be affected in those scenarios. The authors should at least give additional metrics like area under precision recall curve.

There is also a problem with the definition of the Hamming distance. The way it is written it is a similarity, not a distance. After normalizing (dividing by K), one could turn it into a distance by subtracting it from one, but that is not how it is defined in the manuscript. Furthermore, the D_{i,j}s are used to create the labels for the graph-based approaches and there a threshold of 0.5 is applied, implying that the "normalized" D_{i,j} is used. My recommendation would be to define the distance as described above and then create an edge for the nodes with distance smaller than 0.5. One would just have to define the weights differently.

### Questions
My recommendation would be to define the distance as described above and then create an edge for the nodes with distance smaller than 0.5. One would just have to define the weights differently.

Compare performance of ENN to the baseline with the ranking based on the harmonic mean of the four other methods.

Use AUPRC and use appropriate test of significance.

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
The paper introduces a graph-based pipeline for breast cancer risk stratification, addressing the challenge of high dimensionality and feature interaction in genetic features through an ensemble-based feature selection approach. Based on testing on a dataset from the Biobank of Eastern Finland, it finds that a graph convolutional network (GCN) outperformed classical machine learning models.

### Strengths
The paper emphasizes an important problem in dealing with genomic data, namely that of handling SNP interactions and harnessing those to capture disease risk. It employs a GCN-based approach that is, at least in theory, capable of accommodating these constraints via the node features.

### Weaknesses
1. *Unclear evaluation metrics*: Could you please clarify exactly how the error bars are computed (say, in Table 2)?
  - For example, in Table 2, a rough calculation for the accuracy error bars for GCN (with 346 test cases) indicates it should be 0.95±0.050, as opposed to the reported 0.95±0.005.
- A slightly different evaluation-related question: it is not clear from the Table 2 results if employing simple FCNs would already provide a good baseline.
2. *Comparisons with extant literature are inadequate; potential lack of novelty*: Please make a clear comparison with literature employing graph-based NN approaches for cancer risk stratification using genomic data. From a methods perspective, it is hard to see the novelty of this work, so my hope was to see a more rigorous comparison with other works in this application area.
- A quick web search yields many potentially relevant papers and it is hard to tell what the differences are.
- Particular for SNP interactions, please consider comparing with [Machine learning identifies interacting genetic variants contributing to breast cancer risk](https://www.nature.com/articles/s41598-018-31573-5)
3. *The graph-based NN approach needs to be explained more clearly*: 
- Specifically, how are the node/patient embeddings learned and how does the (Hamming) distance metric come into play here?
- Please clarify whether genomic features are the only features you are using. Are you using any clinical information?
4. *SNP interactions captured?*: How exactly is your approach capturing SNP-SNP and higher-order interactions?
- You say that (paraphrasing) other approaches prune the set of features by considering SNPs one at a time, effectively not consider SNP interactions. However, isn’t that what you are also effectively doing by computing the score S_i for each SNP i?

### Questions
Please address the questions/concerns raised in "Weaknesses".

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
