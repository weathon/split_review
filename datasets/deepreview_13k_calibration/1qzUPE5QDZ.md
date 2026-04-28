# Rectifying Group Irregularities in Explanations for Distribution Shift

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
It is well-known that real-world changes constituting distribution shift adversely affect model performance.
How to characterize those changes in an interpretable manner is poorly understood.
Existing techniques to address this problem take the form of shift explanations that elucidate how to map samples from the original distribution toward the shifted one by reducing the disparity between these two distributions.
However, these methods can introduce group irregularities, leading to explanations that are less feasible and robust. 
To address these issues, we propose Group-aware Shift Explanations (\ourmethod{}), a method that produces interpretable explanations by leveraging worst-group optimization to rectify group irregularities. We demonstrate how \ourmethod{} not only maintains group structures, such as demographic and hierarchical subpopulations, but also enhances feasibility and robustness in the resulting explanations in a wide range of tabular, language, and image settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes Group-aware Shift Explanations (GSE), a shift explanation method for understanding distribution shifts. The authors first identify group irregularities as a class of problems in existing shift explanation literature, and then introduce GSE, which utilizes worst-group optimization to rectify such group irregularities. A unified framework is also developed to generalize GSE from K-cluster transport to broad types of existing shift explanation methods, and from tabular data to language and image data. Experiments on tabular, language, and image datasets demonstrate that GSE preserves group structures and mitigates the feasibility and robustness of the state-of-the-art shift explanation approaches.

### Strengths
1. This work is the first shift explanation method that identifies group irregularities as a problem that negatively affects the distribution shift explanation ability of the existing approaches, both theoretically and empirically. 

2. To rectify the group irregularity issues in existing shift explanation approaches, the authors propose GSE, which leverages the worst-group optimization to optimize the worst-group PercentExplained (PE). GSE maintains group (subpopulation) structures and generates more feasible and robust shift explanations.

3. The authors did a great job adapting the counterfactual explanation methods to the shift explanation setting, developing a general framework that applies GSE to optimal transport and counterfactual explanation methods for generating more reliable shift explanations.

4. Extensive experiments on real-world tabular, language, and image datasets demonstrate the superior performance of GSE in producing more feasible and robust shift explanations while preserving group structures, both quantitatively and qualitatively.

### Weaknesses
1. The background introduction should be more clear, especially the parts related to feasibility and robustness. The authors mention several times "feasibility'' and "robustness'' when introducing the significance of group irregularity issues in shift explanation and motivation, but the formal definitions of these two terms are not introduced until Section 3.4, which may lead to confusion about these two terms. I think it would be better if the authors discuss in detail about "feasibility'' and "robustness'' in the introduction and motivation parts. Further, Figure 1(a) (Figure 3(a)) is not clear in illustrating the group irregularities and GSE's solution compared to Figure 1(b) (Figure 3(b)).

2. GSE rectifies the group irregularity issues by simply extending the optimization of PE to optimizing the worst-group PE. Such idea for tackling subpopulation shifts has already been proposed in [1], though it is not designed for shift explanations. Therefore, the idea of GSE is not very novel. Further, the authors only provide theoretical analysis in a simple 1D setting to illustrate the existence of group irregularities. Regarding the proposed GSE, there is no theoretical justification for why GSE generates a more feasible and robust shift explanation while maintaining group structures than the existing methods. It would be better if the authors could provide further theoretical analysis.

3. GSE assumes that the group information is known in the training data, which is hard to satisfy for most real-world scenarios. 

4. The authors did a great job of introducing the works related to explaining distribution shift and worst-group robustness. However, for the works related to domain generalization and adaptation, it would be great if they could discuss connections between domain generalization and adaptation and shift explanations.

### Questions
1. Please see the questions mentioned in Weaknesses.

2. As GSE requires pre-specified groups in the training data to perform worst-case optimization, I wonder how to select the proper feature that divides the group. In the paper, it seems that using unactionable features (e.g., sex) might be an option. I wonder if the authors could discuss further how to divide data into groups.

3. It is known that group imbalance (irregularity) will make the empirical risk minimization models learn spurious correlation, which is vulnerable under distribution shifts. Therefore, leveraging worst-case optimization can mitigate the spurious correlation issue. As GSE also utilizes worst-case optimization to rectify the group irregularities, I wonder if spurious correlations also cause infeasible or vulnerable shift explanations. It would be great if the authors could discuss further the connection between spurious correlations and feasible and robust shift explanations.

### Soundness
2 fair

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
The manuscript addresses the problem of explainable distribution shifts. For distributions covering changeable and unchangeable properties,  computing the shift blindly will lead to infeasible solutions. This is avoided by grouping the samples, i.e, maintaining the unchangeable properties as constraints. The proposed method is evaluated on several datasets, most of which containing language data or based on language data.

### Strengths
S1. The manuscript is well structured and illustrated.

S2. The overall problem of infeasible distribution shifts is explained exhaustively.

S3. An attempt is made to open up the method towards other types of data, e.g. images.

### Weaknesses
W1. Strong statements in the manuscript frequently lack references. Examples: beginning of abstract (if references are to be avoided here, the wording should be repeated in the introduction together with proper references), first mentioning of "shift explanation", example in figure 1, percentages given on page 3 (bottom).

W2. In many places, sentences are formed that do not make sense or are not sufficiently accurate. Examples: "map a male close to a female by changing the age feature", delineations between contributions 2 to 4, caption figure 2, explanation of setting for figure 3b.

W3. Theorem 1 (and its proof) mixes general parameters alpha and beta and numbers (10) and the meaning of the parameters / 10 is not well-defined in the theorem.

W4. The "generalization to image data" remains effectively a pure language problem. CLIP and stable diffusion are used as "translators" from image to text and back, at the text level no image-specific properties remain.


### Questions
Q1. Why is it not possible to model the problem using conditional distributions and shifts between those?

Q2. Why is sex considered unchangeable whereas age is changeable?

Q3. Why using alpha = beta =10 in theorem 1?

Q4. "Robustness" is defined in terms of changes of feasibility. Why is this aspect not covered by statistical variations over multiple runs?

The authors provided a good rebuttal and addressed most questions well, leading to an updated assessment.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
For the explanation of distribution shift, e.g., between train and test datasets, existing methods often find optimal transport between two datasets to quantify the shift. This paper considers group-based optimization and proposes to consider the distance for the worst group to achieve a reasonable explanation (i.e., avoiding overall optimal but locally undesirable transport). Experiments with tabular, language, and image datasets show reasonable explanations of the proposed method using several metrics, including the feasibility metric.

### Strengths
+ The explainability of domain shift is a core problem in machine learning that could be more actively studied.
+ The idea of introducing group robustness to the explanation of domain shift is quite natural and reasonable.
+ The experiment shows broad categories of datasets in which the proposed method is ready to use in practice.

### Weaknesses
 - Considering worst-case loss is quite a natural idea and is used in many contexts, as the paper also mentions in the related work section. This kind of loss can be easily plugged into the Wasserstein distance minimization. Readers may consider the proposed method a pure application of these methods to a specific method (i.e., the distribution shift explanation method by Kulinsky & Inouye, 2023).

- I consider that penalizing the loss of the worst group would be a simple way of achieving distributionally robust optimization (DRO), as representative related papers using worst-case losses call their methods distributionally robust (e.g., Sagawa et al., 2019). In such a sense, it is unnatural that this paper does not discuss anything about DRO. Readers would want to see the discussions about how their method can be stated as a new method of DRO for optimal transport problems. 

- (Cont'd) In such a sense, we can easily find extensive studies regarding Wasserstein DRO (WDRO) such as:

    - Kuhn, Daniel, et al. "Wasserstein distributionally robust optimization: Theory and applications in machine learning." Operations research & management science in the age of analytics. Informs, 2019. 130-166.
    - Kwon, Yongchan, et al. "Principled learning method for Wasserstein distributionally robust optimization with local perturbations." International Conference on Machine Learning, 2020.

### Questions
How is the proposed method related to Wasserstein distributionally robust optimization methods?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Group-aware Shift Explanations (GSE) to address the group irregularities in explanations for distribution shift. The key idea is to optimize for the worst-group PercentExplained (PE). Experimental results justify the effectiveness of the proposed method.

### Strengths
- The problem of group irregularities proposed is interesting.

### Weaknesses
 - The proposed method seems quite limited as it works under the assumption that the source and target are already partitioned into disjoint groups and the correspondence of the groups is available. While for many problems in practice (e.g., domain adaptation for semantic segmentation), such information is not available, which is a major challenge for many problems in CV and NLP.
- The extension to image/language data is naive and is more similar to how to use existing methods or pre-trained models to convert such data into tabular data.

### Questions
Please see weaknesses above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
