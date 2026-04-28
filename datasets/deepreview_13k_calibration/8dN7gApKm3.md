# Uncertainty-aware Graph-based Hyperspectral Image Classification

- Decision: Accept
- Avg Score: 5.60
- Scores: 6, 5, 6, 6, 5

## Abstract
Hyperspectral imaging (HSI) technology captures spectral information across a broad wavelength range, providing richer pixel features compared to traditional color images with only three channels. Although pixel classification in HSI  has been extensively studied, especially using graph convolution neural networks (GCNs), quantifying epistemic and aleatoric uncertainties associated with the HSI classification (HSIC) results remains an unexplored area. These two uncertainties are effective for out-of-distribution (OOD) and misclassification detection, respectively. In this paper, we adapt two advanced uncertainty quantification models, evidential GCNs (EGCN) and graph posterior networks (GPN), designed for node classifications in graphs, into the realm of HSIC. We first reveal theoretically that a popular uncertainty cross-entropy (UCE) loss function is insufficient to produce good epistemic uncertainty when learning EGCNs. To mitigate the limitations, we propose two regularization terms. One leverages the inherent property of HSI data where each feature vector is a linear combination of the spectra signatures of the confounding materials, while the other is the total variation (TV) regularization to enforce the spatial smoothness of the evidence with edge-preserving. We demonstrate the effectiveness of the proposed regularization terms on both EGCN and GPN on three real-world HSIC datasets for OOD and misclassification detection tasks. The code is available at GitHub.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the limitations of the ENN model based on UCE loss. Additionally, the author introduces two regularization terms to alleviate these constraints, and the proposed regularization terms exhibit significant improvements on some datasets.

### Strengths
1. This article offers rich and comprehensive theoretical derivations, with strong formal proofs for the proposed regularization terms and UCE loss analysis, which makes the results quite convincing.
2. The motivation behind the article is clear, and the analysis is praiseworthy.
3. The proposed method has been tested on multiple benchmarks.
4. The entire manuscript is well-structured and logically organized.

### Weaknesses
1. The experimental section of this manuscript appears to be less robust compared to the design and discussion of the methodology.
2. The two proposed regularization terms, UR and TV, do not perform well in Table 1. I'm curious about the reasons behind this.
3. There is a lack of comparative analysis in the experimental section. I'm interested in understanding how the results compare to the latest methods.
4. The ablation experiments directly rely on the results from Tables 1 and 2 for analysis. Perhaps the author could benefit from incorporating more varied ablation designs.

### Questions
Please see the Weaknesses.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the uncertainty quantification to the Hyperspectral imaging classification (HSIC), i.e. epistemic and aleatoric uncertainties. Specifically, the paper theoretically analyzes the limitation of uncertainty cross-entropy (UCE) loss in evidential graph convolution neural networks (EGCN) and proposes two regularization terms to deal with this limitation. Experiments are performed on three real-world HSIC datasets.

### Strengths
1. This paper analyzes the reason why the UCE-based MLP layer in EGCN cannot accurately obtain evidence predictions.
2.  A solution for the above problem is also provided.

### Weaknesses
1. The rationality of the Unminxing-based Regularization part is insufficient. First, the HSIC problem containing noise will greatly affect the optimization results of Eq. (10). Specifically, the presence of noise in hyperspectral data can lead to inaccurate estimations of the abundance coefficients, which are the basis for the proposed regularization. This noise sensitivity could undermine the effectiveness of the unmixing-based regularization, especially in real-world scenarios with significant levels of noise. Secondly, even considering a simple case without noise, whether the ID class and OOD class can be split as Eq. (10) and its rationality remain to be verified. The assumption that OOD data will be orthogonal to the ID data in the feature space may not hold true in practice, as OOD data could exhibit spectral characteristics that are similar to or partially overlapping with the ID data.
2. The unmixing-baed regularization (UR) term, i.e. Eq. (11), is designed heuristically, and its rationality has not been fully explained. Specifically, the optimization trends of $\mathbf{b}^{i}(\mathbf{\theta})$ and $u^{i}(\mathbf{\theta})$ explained in the main text are consistent with the hyperspectral unmixing problem, but I think the rational explanation of this part is insufficient. The connection between the belief/vacuity and abundance coefficients is not rigorously established, and the assumption that these quantities can be directly substituted for each other needs further justification. The paper should provide a more detailed explanation of why the belief and vacuity can act as proxies for abundance coefficients in the context of OOD detection.
3. The proposed evidence-based total variation regularization term is incremental. And Proposition 2 is a relatively simple and intuitive conclusion based on Eq. (13). The contribution of this regularization term is not substantial, and the theoretical justification is not very strong. The paper could benefit from a more in-depth analysis of the impact of the total variation regularization on the uncertainty estimates.
4. The proposed improvements have not been consistently verified in experimental performance. The results show that the proposed method does not consistently outperform the baseline across all datasets and OOD settings. This inconsistency raises concerns about the robustness and generalizability of the proposed approach. The paper should provide a more detailed analysis of the scenarios where the proposed method performs well and where it does not, and discuss the potential reasons for these differences.
5. The compared softax-GCN method is an earlier method, and the author can try some of the latest methods. The paper should compare the proposed method with more recent and state-of-the-art methods for uncertainty quantification in hyperspectral image classification to better demonstrate its advantages.

### Questions
Could the author expand their analysis of the limitations and solutions related to the UCE model and apply it to the design of the EGCN model? This would provide a more coherent and insightful discussion.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel graph-based framework aimed at quantifying uncertainty in the field of HSIC. The authors analyze the limitations of the ENN models based on the UCE loss. To alleviate these limitations, this paper leverages the inherent physical properties of HS data and applies edge-preserving regularization techniques to facilitate the propagation of evidential information within the spatial domain, as a result, two regularization terms UR and evidence-based TV are proposed. The experiments on three datasets to demonstrate the effectiveness of the proposed regularizations.

### Strengths
1.	This paper introduces a graph-based uncertainty quantification framework for HSIC and presents UR and TV regularization methods based on the characteristics of HS data.
2.	The work on graph-based uncertainty quantification in the field of HSIC is novel and appears to be effective based on the provided experimental results.
3.	The research is well-motivated, theoretically grounded, and explores a graph-based uncertainty quantification framework for HSIC models, aligning with the characteristics of hyperspectral imaging.

### Weaknesses
1.	Some minor details in the writing require attention and revision. For instance, in the last paragraph of the Introduction, it should use the abbreviation 'TV' for 'total variation.' In the Conclusion, there is a shift from present tense to past tense, and it's essential to maintain consistency.
2.	In Table 1, the proposed methods show Misclassification ROC scores lower than those of softmax-GCN on the UP and UH datasets, indicating that the best results have not been achieved. The paper lacks relevant explanations, and a more comprehensive and in-depth experimental analysis is needed. Specifically, the lower ROC scores suggest that while the proposed method might identify some true positives, it struggles to effectively rank all positives higher than negatives, which is a critical aspect of classification performance. This discrepancy needs further investigation and discussion.
3.	In the comparative experiments, it's worth noting that there are instances where the introduction of TV leads to a decrease in results. For example, in Table 11 for OOD PR metric of UP-4, GPN-UR scores 99.1 and GPN-UR-TV scores 98.9. This raises questions about the robustness of these methods. It would be beneficial to provide relevant explanations and analyses. Additionally, it might be worthwhile to include separate experimental results for EGCN-TV and GPN-TV. The lack of these specific results makes it difficult to assess the individual contribution of the TV regularization when combined with different base models.
4.	The compared baselines need to be enriched. There are some more recent methods published that should be introduced and compared, such as " Hyperspectral Anomaly Detection Based on Tensor Ring Decomposition With Factors TV Regularization ", " Hyperspectral anomaly detection based on variational background inference and generative adversarial network". The absence of comparisons with these recent methods limits the assessment of the proposed method's novelty and performance relative to the state-of-the-art.

### Questions
1.	What does "ID" mean in this paper?
2.	Is 'Mis' an abbreviation for Misclassification in Table 1? It should be explained in the paper.
3.	Do the numbers following the dataset names in Table 11 to Table 16, such as '4' in 'UP-4,' represent the class numbers? It should be clarified in the paper for better understanding.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes two graph-based uncertainty quantification methods for hyperspectral image classification, incorporating advanced uncertainty quantification models (EGCN and GPN) and specific regularizations (unmixing and TV). The experimental results on three HS datasets demonstrate the advantages of the models. While the introduction of uncertainty quantification into HSIC is a valuable contribution, the overall novelty of the paper may be considered limited, and the experimental analysis could benefit from further depth and solidity.

### Strengths
1. The paper serves as a pioneering work in the exploration of uncertainty estimation within graph-based HSIC models.
2. The paper effectively presents a clear and well-defined motivation, along with a comprehensive theoretical analysis highlighting the limitations of prevalent uncertainty cross-entropy methods.
3. The inclusion of informative unmixing-based and TV-based regularizations in the context of HSIC is noteworthy, and the results successfully confirm the effectiveness of these proposed designs.

### Weaknesses
1. Recently, there has been extensive exploration of Graph-based HSIC, demonstrating its effectiveness. However, a key challenge lies in the high computation and space complexity arising from the pixel-level graph. How do the authors address this issue? Specifically, the paper does not discuss the computational cost associated with constructing and processing the graph, particularly for large hyperspectral datasets. The lack of analysis on memory usage and runtime scaling with increasing data size is a significant oversight.
2. This paper's primary contribution lies in its incremental approach, integrating various existing works, including GNN, uncertainty, unmixing, and TV. Furthermore, the growing attention towards OOD and open-set recognition in HSI underscores the need for a compelling justification of the primary contribution. The paper needs to more clearly articulate how the specific combination of these techniques provides a novel and significant advancement over existing methods, rather than just a combination of known components. The novelty of the approach needs to be more clearly justified considering the existing literature.
4. The experimental results, while promising, require additional substantiation to validate the efficacy of the proposed methods. A more comprehensive set of experiments is necessary. Furthermore, the authors should delve into a more detailed analysis of the experimental outcomes. For instance, a deeper analysis of the misclassification results, including specific examples of where the proposed method fails and why, is needed. Also, a more thorough investigation into the performance of the uncertainty quantification, especially in the context of out-of-distribution (OOD) detection, is necessary.
5. Further elucidation is needed regarding the unmixing-based regularization. For instance, a detailed explanation of how the authors concurrently optimize abundance and endmembers within a graph net would enhance understanding. The paper should clarify the optimization process, including how the endmembers for both in-distribution and out-of-distribution materials are handled and updated during training. The interaction between the unmixing loss and the graph neural network training needs to be more transparent.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript adapted two advanced uncertainty quantification models EGCN and GPN for quantifying epistemic and aleatoric uncertainties associated with the HSIC results. Specifically, two regularization terms are proposed to mitigate the limitations of UCE loss function.

### Strengths
1.	This manuscript applied uncertainty quantification models to the new field of HSIC, eliminating the limitations of the uncertainty cross-entropy loss function.
2.	Studies on the uncertainty quantification of HSIC results are extremely rare, and the author's research direction is very interesting and meaningful.
3.	This manuscript has provided clear questions and motivations, along with detailed formulae definitions and derivations.

### Weaknesses
1. This manuscript is full of hyperparameters, and although the authors list the parameter choices for each model on each data set, the key parameters are not adequately discussed. For example, parametric sensitivity analysis of parameter β, λ1, λ2, and λ3 on each data set is necessary. The analysis should explore the impact of these parameters on both in-distribution (ID) and out-of-distribution (OOD) performance, not just overall ROC. Specifically, the interaction between λ2 and λ3 needs more detailed investigation, as their combined effect on the regularization is unclear. The manuscript should also discuss how the optimal values of these parameters might vary across different datasets and why.
2. The ablation experiments in this manuscript are inadequate, for example, models using TV regularization term alone, not including UR regularization term. The ablation study should also include a comparison with a baseline model that does not incorporate any regularization terms, to clearly demonstrate the individual and combined benefits of the proposed UR and TV terms. Furthermore, the ablation should analyze the impact of each regularization term on both ID and OOD performance separately, to understand their specific contributions to each task.
3. Uncertainty has been widely studied in the previous works. This paper seems simply introduced the existed work for HSI classification. The experimental comparison is also insufficient. The manuscript should include a more thorough comparison with existing uncertainty quantification methods, particularly those applied to hyperspectral image (HSI) classification. This comparison should not only focus on overall performance metrics but also on the computational cost and complexity of each method. The authors should also discuss the specific advantages and disadvantages of their proposed approach compared to other methods.

### Questions
What are the limitations of UCE and the specific role of UR? Please describe them directly and clearly in the Abstract and contribution section.
	From Table Ⅰ, it can be found that the proposed uncertainty quantification frameworks do not reach the SOTA level on the misclassification detection tasks, especially the GPN-based variants, what is the purpose of these experiments?
	How computationally efficient is the use of UR and TV regularization terms on OOD and misclassification detection tasks.
	It is suggested that authors unify the meaning of bold and underlined numbers in each table. In addition, some bold an underlined numbers in Table 11-15 are incorrect. Please check the corresponding issues through the full manuscript.
	In the E.2-Detailed Result section, whether the proposed models are equally applicable to OOD detection for other classes in different datasets. Why are the PR values for class-10 in the UH dataset and class-7 in the KSC dataset below the baseline.
	There are some punctuation errors that should not be made in a paper. For example, "…64, 128, 256, respectively We…" and "…{10-4,10-3,10-2,10-1}(2) Number of… "in part D-Model Details. It is suggested to carefully check the textual details of the manuscript. In addition, what do parameters λ and λ' represent in the model.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
