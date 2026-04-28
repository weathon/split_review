# Pointwise Information Measures as Confidence Estimators in Deep Neural Networks: A Comparative Study

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 6, 6, 6, 3

## Abstract
Estimating the confidence of deep neural network predictions is crucial for ensuring safe deployment in high-stakes applications. Softmax probabilities, though commonly used, are often poorly calibrated, and existing calibration methods have been shown to be harmful for failure prediction tasks. In this paper, we propose to use information-theoretic measures to estimate the confidence of predictions from trained networks in a post-hoc manner, without needing to modify their architecture or training process. In particular, we compare three pointwise information (PI) measures: pointwise mutual information (PMI), pointwise $\mathcal{V}$-information (PVI), and the recently proposed pointwise sliced mutual information (PSI). We show in this paper that these PI measures naturally relate to confidence estimation. We first study the invariance properties of these PI measures with respect to a broad range of transformations. We then study the sensitivity of the PI measures to geometric attributes such as margin and intrinsic dimensionality, as well as their convergence rates. We finally conduct extensive experiments on benchmark computer vision models and datasets and compare the effectiveness of these measures as tools for confidence estimation. A notable finding is that PVI is better than PMI and PSI for failure prediction and confidence calibration, outperforming all existing baselines for post-hoc confidence estimation. This is consistent with our theoretical findings, which suggest that PVI is the most well-balanced measure in terms of its invariance properties and sensitivity to geometric feature properties such as sample-wise margin.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the use of information-theoretic measures for confidence estimation in deep neural networks in a post-hoc manner. It specifically compares three measures from the prior works: pointwise mutual information (PMI), pointwise $\mathcal{V}$-information (PVI), and pointwise sliced mutual information (PSI), on their effectiveness as tools for confidence estimation. The study examines the theoretical properties of these measures in terms of invariance, correlation with margin, and convergence rate. Empirical evaluations are conducted on tasks such as misclassification detection, selective prediction, and calibration error analysis, using image classification tasks. These evaluations compare the three measures against baseline methods including softmax, margin, max logit, and negative entropy. The results indicate that PVI outperforms both PMI and PSI in terms of effectiveness as a confidence estimation tool.

### Strengths
* The paper provides a comprehensive theoretical and empirical analysis of three pointwise information measures (PMI, PVI, and PSI) on their effectiveness to be used as confidence estimation tools. It demonstrates that these measures can be applied in a post-hoc manner and do not require modifying the model architecture or retraining the network.

* Empirical evaluation covers broader scope including misclassification detection, selective prediction and calibration error analysis. These aspects are crucial for thoroughly analyzing the reliability of the confidence measures in supporting model predictions.

### Weaknesses
 * Despite the use of pointwise information measures requiring the training of additional models in a post-hoc manner, both PMI and PSI perform worse than the baseline softmax measure, as evidenced by the results in Table 3 and Table 4. Additionally, the PVI estimator employs temperature scaling, a post-hoc confidence calibration method, which raises concerns about whether the improved performance of PVI is due to the PVI measure itself or the temperature scaling. The paper would benefit from further evaluation of additional benchmark methods to provide clarity on this issue, specifically: (1) PVI estimator without the temperature scaling, and (2) Softmax (SM) with temperature scaling [Guo et. al. 2017]

* Given the focus and motivation of the paper on exploring post-hoc confidence estimation tools, the empirical evaluation does not include comparisons with established post-hoc confidence calibration methods. To address this gap, it would be beneficial to compare the proposed measures with well-known methods such as Temperature Scaling (TS) [Guo et. al. 2017] and Ensemble Temperature Scaling (ETS) [Zhang et. al. 2020]. Furthermore, the performance of PMI and PSI is particularly concerning, as they require training additional models yet still underperform the softmax baseline, even without temperature scaling. This raises questions about the practical utility of these measures, especially given the computational overhead they introduce. The paper should provide a more thorough analysis of why these measures fail to achieve competitive performance, and under what conditions they might be expected to be useful.


### Questions
* Can you please address the concerns about whether the improved performance of PVI is due to the PVI measure itself or the temperature scaling in the PVI estimator?

* What is the reason for the contradictory findings where PSI is shown to be a better confidence estimator than PVI in experiments on correlation to Margin, while PVI outperforms PSI in experiments on misclassification detection, selective prediction, and calibration analysis?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The following paper conducts theoretical and experimental analysis on different pointwise information measures that serve as a metric denoting the confidence of neural network predictions. It considers three pointwise information measures: (1) pointwise mutual information (PMI), (2) pointwise $\mathcal{V}$-information (PVI), and (3) pointwise sliced mutual information (PSI). Initially, the paper introduces the formal definition of each information measure and its pointwise version, followed by analyses of each pointwise measure on (1) invariance properties, (2) geometric properties, and (3) convergence properties. There are also experiments on failure prediction and confidence calibration tasks to measure each pointwise information measure in terms of confidence estimation.

### Strengths
1. The paper is well-written and highly enjoyable to read.
2. The explanation regarding experiments in this paper goes in-depth, and I highly appreciate the authors for making Jupyter Notebook and source code available.
3. While this paper does not propose any new methods, it provides novel insights on utilizing various pointwise information measures to estimate the confidence of DNNs.

### Weaknesses
1. Experiments available in Section 4 of the paper are done on relatively small datasets and architectures. Is it possible to scale up the dataset (TinyImageNet, ImageNet) and architecture (ViT, DeIT), just like the experiments conducted by Jaeger et al., 2023 (https://arxiv.org/abs/2211.15259)? I am asking because benchmark methods used for comparison in Section 4 evaluate their method on a relatively larger scale in terms of data and architecture within their original paper.
2. More on the Questions section.

### Questions
1. In Table 2, why do $n$ for PMI and PSI differ in value? I fail to see the results to be compatible with each other if the $n$ values are not comparable.
2. I might not get 100% on the correlation between the properties of each pointwise information measure outlined in Section 3 with the results in Section 4. For example, how would you correlate the invariance property, in which PMI theoretically has an edge, with the result obtained in Section 4 for failure prediction in Section 4.1 and confidence calibration in Section 4.2?
3. For someone who is not that familiar with the following line of work, with regards to the Convergence Rate part detailed in Section 3.3, are there any possible ways to model $\mathcal{V}$ for PVI in a way such that its estimation error are comparable to $|\mathrm{pmi}(x;y) - \hat{\mathrm{pmi}}_n|$ as in PMI case?
4. Typos:
- In point 1 of \textbf{Contributions} , there should be a period between estimation and We ("estimation. We" instead of "estimation We". [Section 1]
- "from in" -> "from" [Section 4]

### Soundness
3

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
3

### Summary
Uncertainty estimation becomes essential for ensuring safety AI deployment. To estimate this, various measures, commonly based on softmax probs, are employed, but they are often poorly calibrated. The authors handle this issue by utilizing pointwise information measures - PMI, PSI, PVI. They analyze several properties of measures to validate its reliability, i.e., invariance and sensitivity to margin, and conduct empirical evaluations to support its effectiveness on several datasets. Experimental results provide some findings regarding the superiority and scalability among the measures.

### Strengths
- It provides theoretical analysis regarding the properties of several PI measures, which are supported by empirical observations.
- Effectiveness of the measures are validated via two types of experiments.

### Weaknesses
 - More comprehensive analysis with other uncertainty metrics are needed, such as MC Dropout, MCMC, or Laplace approximation. It also needs to compare with non-pointwise information measures, such as MINE [1]. Specifically, the lack of comparison with methods like MC Dropout is a significant oversight, as it is a widely used and relatively simple approach for uncertainty quantification. The authors should provide a clear justification for why these methods are not suitable benchmarks, or alternatively, include them in the experimental evaluation. Furthermore, while MINE is a measure of mutual information, its relevance to the problem should be more thoroughly discussed, as pointwise mutual information is a specific case of MI, and the authors should clarify why other MI estimators are not suitable.
- Empirical results are based only on small-scale datasets, such as MNIST or CIFAR-10, although this paper aims to address scalability. The claim of scalability is not adequately supported by the experiments. The datasets used are not representative of the complex, high-dimensional data that are often encountered in real-world applications. Experiments on larger, more challenging datasets are needed to validate the scalability of the proposed measures. For example, ImageNet or similar datasets should be considered to demonstrate the practical applicability of the proposed methods.
- To better understanding, it would be helpful to add some visualizations, such as saliency map (with more curated examples as well as Fig.5), ROC curve, or ECE diagram. The current visualizations are insufficient to fully understand the behavior of the proposed measures. Saliency maps could provide insights into which features the measures are sensitive to. ROC curves and ECE diagrams are standard tools for evaluating the performance of uncertainty quantification methods, and their absence makes it difficult to assess the effectiveness of the proposed measures.

### Questions
- In L500, why convergence rate is a crucial factor for confidence calibration?
- Why PVI is favorable for complicated dataset than other PI measures?

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
4

### Summary
This paper studies the impact of three pointwise information (PI) measures on the uncertainty quantification quality with Deep Neural Network (DNN). Through the lens of Information Theory (IT), the authors provide rigorous theoretical properties regarding the invariance, geometric, and convergence rates. Extensive experimental results confirm the theoretical arguments, and, the benchmarking suggests the pointwise V-information (PVI) outperforms the mutual information (PMI) and the sliced mutual information (PSI) in failure prediction and confidence calibration.

### Strengths
- This paper is very well-written and is clear to understand the important aspects of the algorithm.
- I like the new direction of using IT tools (e.g., mutual information, conditional entropy, etc.) to improve the reliability of DNN. I believe the benchmark results of three recent PI measures are useful for communities.
- The theoretical results are solid with clear mathematical notations, clear statements, and proof of the invariance, geometric properties, and convergence rate per each PI measure.
- The theory is also confirmed by experimental evidence, e.g., Fig.1 with the experiment on correlation to margin results in geometric properties, Table 2 with the convergence rate.
- The experimental results are extensive with several settings across different modern DNN architectures on standard benchmark datasets.

### Weaknesses
 - The novelty regarding a proposed method is weak since PMI, PSI [1], and PSI [2] have been proposed before.
- The novelty in theoretical analysis is quite weak. Specifically, the invariance properties have been mentioned in Section 3 of [1] and the convergence rate has been analyzed in Section 3 of [1] and Section 4 of [2].
- The connection between theoretical results and model uncertainty is unclear to me. Details are in Question 2.
- Three PI measures are less computationally efficient than other baselines (e.g., standard Softmax) by requiring additional models and computes either $pmi(x;y)$, $psi(x;y)$, or $pvi(x\rightarrow y)$. 
- The experimental results also lack some measurements such as sharpness and predictive entropy to assess the uncertainty quality performance.

### Questions
1. What do the authors mean by a “post-hoc manner” in L-45? Is this post-hoc recalibration technique with additional hold-out calibration data to fine-tune some learnable parameters?
2. Remark 1 is vague to me. Firstly, what kinds of uncertainty are you talking about (aleatoric or epistemic)? It would be great if the authors could explain this kind of uncertainty through the lens of IT (see Eq.1 in [3]). Secondly, why when a classifier is uncertain on X, the uncertainty about $g(X)$ should ideally be the same? Can you formally explain this argument and give some examples about this?
3. In proof of Prop.6, while [4] provides estimation error bounds on the sample marginal distribution $P(X)$, why the authors can trivially apply their results on the conditional $P(X|Y)$? 
4. Could the authors please compare methods with the sharpness score [5] in Section 4.2? I think this is important because lower ECE is only a necessary condition, it is not a sufficient condition to evaluate a good uncertainty estimation with DNN.
5. L-172 mentioned that PVI uses temperature scaling, is this the main reason PVI achieves the lowest ECE in Tab.4?
6. Can PI measures extend to other kind of dataset such as text, audio, video, etc.? Is there any challenge with this extension?

References:

[1] Goldfeld et al., Sliced mutual information: A scalable measure of statistical dependence, NeurIPS, 2021.

[2] Xu et al., A theory of usable information under computational constraints, ICLR, 2020.

[3] Mukhoti et al., Deep deterministic uncertainty: A new simple baseline, CVPR, 2023.

[4] Jiang et al., Uniform Convergence Rates for Kernel Density Estimation, ICML, 2017.

[5] Kuleshov et al., Calibrated and sharp uncertainties in deep learning via density estimation, ICML, 2022.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores the use of point-wise information measures as notions of prediction confidence for neural networks. They propose three existing information measures (PMI, PSI, PVI) with associated estimation methods, and state their theoretical properties in terms of invariance to transformations, geometric properties w.r.t. decision boundary, and convergence rates of the estimators to the true measures. The results are motivated as useful or intuitive for uncertainty quantification or confidence estimation. Then two experiments on misclassification detection and selective prediction are performed, where the measures are compared to a few simple alternative notions of model confidence. Finally, their calibration property in terms of ECE is examined. The authors suggest that their point-wise information measures provide accurate and robust measures of model confidence.

### Strengths
- Approaching confidence estimation from an information-theoretic perspective provides an interesting angle, and the suggested information measures seem relevant and somewhat practical. 
- The paper clearly outlines multiple factors of motivation for the work, which help put the approach into a broader context.
- The information measures are closely examined and various theoretical properties are studied. This is also obvious from the substantial appendix which lists many properties of the information measures and possible estimation methods.

### Weaknesses
My main concerns are with respect to the claims made by the paper, obtained insights, and the experimental design and connection to confidence estimation. I will list my points of concern under each of these categories, albeit they are connected.

Claims
- The proposed measures are motivated as a post-hoc approach to confidence estimation. All the estimation methods for PMI/PSI/PVI require custom neural network modeling and training. How is this supposed to be post-hoc? For example, how am I supposed to apply this to an existing, pre-trained neural network that I treat as a black-box and do not want to fine-tune? I do not think this qualifies as post-hoc. The requirement for custom model training, even if the base model is not retrained, limits the practical applicability of the method to scenarios where one has access to training data and the ability to train additional models. This is a significant limitation compared to true post-hoc methods that can be applied to any black-box model without retraining or access to training data.
- The proposed measures are motivated by a “Relationship to Probabilistic Causation” yet this relationship is never mentioned again or examined, and only briefly mentioned in the limitations/future work section. In that section it is then also claimed that "the PI measures are the optimal choice of explainability" but there are no proper experiments on model explainability or causality, so this claim is not backed up in any way. The lack of experimental validation for the claim that the proposed measures are optimal for explainability undermines the motivation and raises questions about the practical relevance of this theoretical connection. The absence of any concrete analysis or experiments to support this claim weakens the overall argument.
- The proposed measures are motivated by their “Direct Probability Computation”, but given their value ranges the only way to obtain probabilities is to pass them through a squashing function such as softmax, which is precisely done in the experiments. So how does the interpretation of obtained probabilities, and their associated reliability, differ in any way from just a regular softmax on logits? The associated claims on "robustness" are not examined or backed up in any way. The argument that these measures provide a more direct probability computation is not convincing, since the need for a squashing function like softmax makes them no different from logits in terms of their interpretation as probabilities. The lack of experimental validation for the claim of robustness further weakens this motivation.
- The proposed measures are motivated by the need for “uncertainty quantification” and prevalent miscalibration of neural networks. Firstly, recent research has shown that modern neural network architectures such as transformers (not considered here) can in fact be quite well calibrated [1,2], and even if this was not the case, their proposals do not address a way to remedy model miscalibration but rather just suggest another confidence measure. Their claim on having “better calibrated” confidence measures is unconvincing to me due to their experimental design (see below), and thus their very strong claim on "outperforming all existing baselines for post-hoc confidence estimation" is poorly backed up. Finally, the relationship between proposed measures and meaningful uncertainty interpretations is very speculative and does not reach beyond a few broad and high-level arguments in their remarks (see below). So overall, this angle of motivation is also lacking based on their strong claims. The paper does not adequately address the fact that modern architectures can be well-calibrated, and the proposed measures do not offer a solution to miscalibration, but rather an alternative confidence measure. The lack of a clear connection to meaningful uncertainty interpretations and the overstatement of performance claims further weaken the motivation.

Insights
- I have a key question: By the invariance properties in sec 3.1 we have that PMI is best, by the geometric and convergence properties in sec 3.2. and 3.3 we have that PSI is best, but in the performed experiments we find that PVI is best. How can you reconcile this and claim that theory and experiments are in line with each other? The paper fails to reconcile the conflicting theoretical results with the empirical findings. The theoretical analysis suggests that PMI and PSI are superior based on different properties, yet the experiments show that PVI performs best, which raises questions about the validity and practical relevance of the theoretical analysis.
- To re-iterate on the connection to uncertainty quantification: it is repeatedly stated that there is a high relevance for “model uncertainty”, which equates to a notion of epistemic uncertainty. But then, Remark 1 motivates that uncertainty should be invariant to data transformations, which now relates to notions of data (aleatoric) uncertainty. Yet overall, the quantity of interest is in fact p(y|x) which is simply predictive uncertainty of the model given an input. So, it does not seem to me like there is a principled association between the information measures and actual notions of uncertainty, and the authors are not clear about what kind of uncertainties we are trying to address. Overall, the connections to uncertainty are mainly contained in the motivating introduction, and in Remark 1 and Remark 2, and are all very high-level and speculative. The paper does not clearly distinguish between epistemic and aleatoric uncertainty, and the connection between the proposed measures and these notions remains unclear. The motivation for invariance to data transformations seems to contradict the goal of capturing predictive uncertainty, which further confuses the interpretation of the results.
- Regarding Remark 1: the quantity of interest is p(y|x), whereas data transformations are applied to features X. Since we then have that $g(X) \neq X$, I don't necessarily see an issue if $p(y| g(X)) \neq p(y|X)$ because we are conditioning on a different quantity. The argument for invariance to data transformations is not well-justified, as the transformations are applied to the input features, which changes the conditioning variable and thus the conditional probability. The paper does not adequately address this point and its implications for the proposed measures.
- Regarding Remark 2: The provided interpretation for confidence estimation does not take into account data atypicality or OOD'ness [3]. These samples may lay far away from the decision boundary/margin but also in the tail of the data support, and thus should ideally exhibit low confidence. Also, the interpretation on confidence correlating with margin distance is only desirable for overlapping supports. If e.g. $P(X|Y=0)$ and $P(X|Y=1)$ are clearly separated (as e.g. used in Prop. 4) then we would desired maximum confidence everywhere. So, it is unclear to me how Remark 2 follows from the stated results and how directly applicable/useful these results are. The interpretation of confidence as a function of margin distance does not consider data atypicality or out-of-distribution samples, which can be far from the decision boundary but should exhibit low confidence. The paper also does not adequately address the issue of non-overlapping class distributions, where maximum confidence would be desirable everywhere, which further limits the applicability of the proposed measures.
- Regarding sec 3.2: The section seems to borrow different tools from different papers to show results for the different information measures. However, the assumptions (which seem very strong), conditions of validity, and form of results are all very different, and no interpretations are given. How do they relate to each other in terms of strength and the individual components influencing them? For example, what is Prop. 4 for PMI useful for and why do we not have a similar result in regards to "sample-wise margin" as for PSI and PVI? Similar questions also apply to sec 3.3 on convergence results. The paper presents theoretical results for different measures using different tools, assumptions, and conditions of validity, without providing a clear interpretation or comparison of their strengths and limitations. The lack of explanation about the practical implications of these results and the absence of similar results for all measures make it difficult to understand their relevance and utility.
- Regarding L228: based on the wording it is unclear what the “sample-wise margin” is supposed to be. A mathematical definition seems necessary here. The term "sample-wise margin" is not clearly defined, which makes it difficult to understand the theoretical results and their practical implications. A precise mathematical definition is needed to clarify this point.
- Regarding the margin correlation experiment: The results are confusing to me because in Table 1 it seems like the results between different measures are quite different (e.g., PMI has lower and more volatile correlations than PSI), yet the UMAPs virtually all look the same. How should I understand that? The discrepancy between the correlation results in Table 1 and the UMAP visualizations raises questions about the reliability and interpretability of the margin correlation experiment. The paper does not adequately explain this discrepancy, which makes it difficult to understand the practical implications of the results.

Experiments
- My main concern is about the fact that their information measures are passed through a softmax function and *calibrated with temperature scaling* before benchmarking against other methods. This seems like a very biased comparison, since we observe in App D.1 that these operations significantly alter the distributions of the information measures, and improve upon the considered performance metrics. It seems unreasonable to me to *scale and calibrate* your measures beforehand, and then claim afterwards that they provide "direct probabilities" and "well-calibrated" confidence estimates. How is this a fair comparison to any baselines that are not subject to the same transformations, e.g. ML, LM? In that context, do you also apply temperature scaling to any of the other baselines such as softmax (MSP, SM)? I feel like any performance claims should rather be reported for the raw information measures instead, since it otherwise becomes unclear where any benefits stem from. The use of softmax and temperature scaling on the proposed measures before benchmarking against other methods introduces a bias in the comparison. The paper does not adequately justify this approach, which raises questions about the validity of the performance claims. The lack of a comparison with raw information measures makes it difficult to assess the true contribution of the proposed approach.
- In the experiments on confidence calibration only two simplistic baselines are considered, and they are marginally outperformed. To claim that they are "outperforming all existing baselines" seems like a very strong claim in that light. It would be more meaningful to consider other baselines for confidence estimation, including those that have been subjected to a similar approach of re-calibration as they do for their own measures (using temperature scaling), e.g. isotonic regression [4], regularization [5], or other uncertainty methods like models with variance predictor [6] etc. The comparison with only two simplistic baselines is insufficient to support the claim of outperforming all existing post-hoc methods. The paper should include more robust baselines that have been subjected to similar calibration procedures, such as isotonic regression, regularization, or models with variance predictors, to provide a more comprehensive evaluation.
- Relatedly, the results in Table 3 are often within each other's margin of error, so there are some questions on the reliability or significance of “outperforming”. The statistical significance of the results in Table 3 is questionable, as many of the reported improvements are within the margin of error. This undermines the claim of outperforming existing baselines.
- In L401-403, what is the intuition for only working with features from the last layers? This is not clearly explained. The paper does not clearly explain the rationale for using features from the last layers only, which raises questions about the methodology and its potential limitations.
- Are there any clear principles guiding the choices of estimation methods for the information measures, and associated transformations (i.e., softmax or temperature scaling)? Based on the appendix it seems like purely based on hold-out performance. If so, why not consider other squashing functions or re-calibration procedures? The choices are not well documented and seem primarily motivated for their simplicity. The paper does not provide clear principles for the choices of estimation methods and transformations, which seem to be based on hold-out performance. The lack of a systematic approach for choosing these parameters and the absence of exploration of other squashing functions or re-calibration procedures raise questions about the robustness and generalizability of the proposed approach.
- I am personally missing a more detailed and meaningful interpretation of the results beyond stating what can be seen in the provided results tables.

Summary
- In conclusion, I find that the paper makes overly strong claims and motivates the work from multiple angles which are then left unexplored or never properly analyzed. The experimental design raises some questions and combined with the marginal improvements in experiments casts doubts on the practicality and usefulness of the approach. I am struggling to see the real novelty of the paper. The proposed information measures and their estimation methods are all taken from existing papers, and many of the theoretical results rely strongly on these papers as well. Is the theoretical analysis novel? Personally, it is hard for me to say since I am unfamiliar with this research domain. Is the novelty then in its application/use for confidence estimation? The experiments are unconvincing, and the connections to uncertainty do not go beyond some high-level arguments. In addition, their theoretical insights and empirical results seem somewhat contradictory on what the best information measure is supposed to be. For example, they conclude that "This superior performance is likely due to PVI being the most well-rounded metric, particularly in terms of its invariance and margin sensitivity”, even though Remarks 1, 2 and 3 on these properties rank PVI lowly. While the paper explores some interesting information-theoretic tools, their use for robust and reliable confidence estimation is substantially lacking in my opinion.

### Questions
Please observe and address my questions and comments in the weakness section, such as on the strength of claims, usefulness of theoretical results for confidence estimation, experimental design, and others.

### Soundness
1

### Presentation
2

### Contribution
1
