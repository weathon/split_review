# Fairness-Aware Domain Generalization under Covariate and Dependence Shifts

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
Achieving the generalization of an invariant classifier from source domains to shifted target domains while simultaneously considering model fairness is a substantial and complex challenge in machine learning. Existing domain generalization research typically attributes domain shifts to concept shift, which relates to alterations in class labels, and covariate shift, which pertains to variations in data styles. In this paper, by introducing another form of distribution shift, known as dependence shift, which involves variations in fair dependence patterns across domains, we propose a novel domain generalization approach that addresses domain shifts by considering both covariate and dependence shifts. We assert the existence of an underlying transformation model can transform data from one domain to another. By generating data in synthetic domains through the model, a fairness-aware invariant classifier is learned that enforces both model accuracy and fairness in unseen domains. Extensive empirical studies on four benchmark datasets demonstrate that our approach surpasses state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of domain generalization and fairness simultaneously under covariate and sensitive dependence shifts. The authors introduce dependence shift, which implies the dependence of the sensitive attribute and the outcome variable varies across domains. The authors formulate the problem as a minimax optimization problem with demographic parity constraint. Experiments were done on several benchmark datasets.

### Strengths
- This paper addresses a domain generalization with the consideration of fairness, which is an important but less explored subject in machine learning and related fields.

### Weaknesses
 - I do not think the examples given in Figure 1 are appropriate: (1) concept shift is the disparity in $Y^e | X^e$. It doesn't mean a completely new label appears in the target domain; (2) I am unsure if such an auxiliary background or objective, such as couch or grass, is an appropriate "sensitive attribute." I think those can be spurious features; however, often, in real-world cases, sensitive attributes are more than just spurious features as they correlate with both input and output. Moreover, ensuring fairness across the images that include a couch or grass does not seem to be a convincing example of fairness.
- Also, in Figure 2, I do not think what the authors presented is "group fairness levels," as the fairness notion considered in the study is demographic parity, which is calculated as a statistical dependence of the prediction and the sensitive attributes. However, in the figure, no prediction is considered. I think what the authors presented there is the dependence (or correlation) between the true label and the sensitive attribute.
- In many applications, the sensitive attribute and outcome variable are nonbinary. The extension to such cases of the approach introduced in the study does not seem to be straightforward.
- I found the evaluation metrics are inconsistent - why do the authors evaluate the fairness in difference of AUC but the performance in accuracy? 
- The authors used so-called inter-group AUC difference as a fairness metric. There have been extensive discussions on different versions of AUC differences, and it has been demonstrated that inter-group AUC difference does not reflect all possible performance disparities. Please refer to [Kallus and Zhou (2019)](https://papers.nips.cc/paper_files/paper/2019/hash/73e0f7487b8e5297182c5a711d20bf26-Abstract.html), [Yang et al. (2023)](https://dl.acm.org/doi/abs/10.1609/aaai.v37i10.26405) and the references therein.
- It seems like the authors confuse demographic disparity (dependence of $\hat{Y}$ and $Z$) and dependence of $Y$ and $Z$. E.g., in Figure 2 and Table 1, the authors presented the degrees of dependence of $Y$ and $Z$ as if they were fairness measurements. 
- Some important related works are missing. E.g., [Rezaei et al. (2021)](https://ojs.aaai.org/index.php/AAAI/article/view/17135), [Singh et al. (2021)](https://dl.acm.org/doi/10.1145/3442188.3445865), [Giguere et al. (2022)](https://openreview.net/forum?id=wbPObLm6ueA), [Chen et al. (2022)](https://openreview.net/forum?id=U3gobB4oKv). This is not an exhaustive list.

### Questions
- Could the authors prove or give some thoughts about the existence of a non-trivial solution to Problem 1? 
- Is there any reason the authors used DP as the fairness criterion? Many previous studies revealed that the DP might not be an ideal fairness criterion. 
- The results show that the proposed method effectively reduces the AUC difference across sensitive groups in almost all cases. Could the authors kindly explain why this happened? Because, for me, the relationship between the statistical dependence of the model prediction and sensitive attribute and the AUC differences is unclear. Thus, reducing the dependence (or equivalently achieving demographic parity) does not necessarily result in smaller AUC differences. To the best of my knowledge, a similar analysis has been done by [Zhao and Gordan (2022)](https://dl.acm.org/doi/abs/10.5555/3586589.3586646). They proved that fair representation (that is, independent of the sensitive attribute, which satisfies SP) results in accuracy parity (the same accuracies across all sensitive groups) if the Bayes optimal classifiers across different groups are close.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a machine learning model designed to deliver fair predictions for an unseen target domain in a domain generalization scenario. In particular, the authors first introduce a novel concept called "dependence shift" to capture the relationship between labels and sensitive attributes. Then, they propose a two-stage approach to achieve demographic parity on the target domain while dealing with covariate and dependence shifts. In the first stage, the authors develop a transformation model to address covariate shift assumptions. In the second stage, they train the model with fairness regularizations to ensure fair predictions on the target domain in the presence of dependence shifts. Experimental results on several datasets demonstrate that the proposed method attains a more favorable trade-off between fairness and accuracy on target domains compared to baseline approaches.

### Strengths
- This paper addresses fairness in the context of distribution shifts which is an important topic in fair machine learning.

- The availability of code and supplementary documentation enhances the reproducibility of the research.

### Weaknesses
 - The motivation behind "dependence shift" is not entirely clear. The example presented in Figure 1 is somewhat ambiguous. It's unclear why attributes like "grass" and "couch" are considered sensitive. The authors should consider providing a more realistic example to better illustrate their problem setting. Specifically, the notion of dependence shift, while potentially relevant, needs a clearer grounding in real-world scenarios where the correlation between sensitive attributes and labels changes across domains. The current example, involving backgrounds like grass and couches, feels contrived and doesn't immediately resonate as a practical fairness concern.

- The authors mention the potential extension of their work to handle settings with multi-class, multi-sensitive attributes, and other fairness concepts. However, it is not straightforward how their results can be extended to these scenarios. More details are needed to clarify this aspect. The jump from binary sensitive attributes and classes to multi-class and multi-sensitive settings is non-trivial. The authors should provide a more concrete roadmap or theoretical justification for how their proposed approach can be generalized, especially considering the complexities that arise with multiple sensitive attributes and their intersections.

- There's an existing work that also deals with fairness in domain generalization [cite]. That work doesn't assume invariance of $\rho$ across domains which then imply that it can also handle the dependence shift. Thus, it's essential for the authors to differentiate their work from this previous research. Additionally, Theorem 1 appears quite similar to Theorem 3 in [cite]. The authors should highlight the novel insights offered by Theorem 1 compared to the existing result. It is crucial to clearly articulate the differences in assumptions and contributions compared to existing methods. The current discussion lacks a detailed comparison, making it difficult to assess the novelty of the proposed approach. The similarity between Theorem 1 and existing results needs to be addressed with a precise explanation of the unique aspects of the theorem.

- Assumption 1 appears more like a definition than an assumption since a mapping between two domains can always be constructed. For instance, when domains share the same support, an identity mapping fulfills this assumption. The authors need to justify why this is a non-trivial assumption and how it impacts the theoretical framework. The current explanation is insufficient to demonstrate the necessity of this assumption.

- The theoretical results lack coherency. It is not entirely clear how Theorems 1 and 2 relate to the proposed algorithm's goals, which involve learning a transformation model to address covariate shift and constructing a fairness-aware T-invariance classifier that achieves demographic parity. The connection between the theoretical results and the practical algorithm is not well-established. The authors should provide a more detailed explanation of how the theorems support the algorithm's design and its ability to achieve the stated goals.

- The authors should explain why they restrict the hypothesis class $\mathcal{F}$ to the set of invariant fairness-aware classifiers and why the max operator in the objective function can be eliminated in Problem 2. The rationale behind these design choices is not clearly explained, and the authors need to provide a more detailed justification for these restrictions and simplifications.

- To strengthen their claims, the authors should consider including comparisons of fairness-accuracy trade-off curves (Pareto frontiers) for the models in the experimental section. This would provide stronger evidence for their proposed method's effectiveness. The current experimental results lack a comprehensive analysis of the trade-offs between fairness and accuracy. The inclusion of Pareto frontiers would provide a more nuanced understanding of the method's performance.

### Questions
Please see the Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a novel approach to multi-source domain generalization, addressing not only predictive performance but also fairness guarantees. They account for distribution shifts arising from covariate shifts and variations in the relationship between the sensitive attribute and the class label (spurious correlation). Their key assumption is that all source instances result from a transformation and that instances from one domain can be transformed into instances of another. Their framework begins by training a transformation model, followed by the generation of synthetic instances from previously unseen potential target domains. The classifier is subsequently trained on a combination of synthetic and real instances.

### Strengths
S1 - The issue being investigated is of significant importance. Domain generalization, considering both covariate shift and spurious correlations, is highly relevant to real-world scenarios where such challenges frequently manifest. Their proposed approach appears to be well-suited for addressing situations commonly encountered in practical applications and can be applied under realistic conditions.

S2 - The introduction effectively substantiates all the claims made, including the contributions put forth by the authors. These assertions find validation through a thorough description of the methodology employed and the experiments conducted. The method section elaborates on the techniques and approaches considered, demonstrating how they align with the stated objectives. Furthermore, the experimental results provide empirical evidence that supports the claims made in the introduction. 

S3 - The authors have invested substantial effort to establish a rigorous and thorough evaluation process within the paper. They have taken into account an extensive set of baseline models and addressed three distinct classification tasks. Additionally, the authors have conducted meticulous ablation studies, scrutinizing various factors to guarantee a robust and comprehensive evaluation.

S4 - The authors offer robust mathematical solutions to enable the training of their approach.

S5 - The paper demonstrates commendable attention to reproducibility by providing thorough and detailed information regarding the experimental setup. Furthermore, the ablation studies provide insightful analysis.

S6 - The paper is well structured with well-defined sections and subsections, contributing to its overall readability.  The paper includes sub-sections that effectively delineate different aspects of the methodology, ensuring a coherent and structured presentation.

### Weaknesses
W1 - The paper would benefit from enhanced clarity in its writing. At times, the authors employ technical language without providing accompanying explanations, particularly in the introduction. For instance, a more thorough contextualization of spurious correlations, why they manifest in neural networks, and when they become problematic would greatly assist readers. Specifically, the paper should elaborate on how spurious correlations lead to poor generalization in unseen domains, perhaps by detailing how neural networks tend to latch onto these correlations instead of learning true causal relationships. Additionally, the paper references concepts such as the latent content space, sensitive factor, and style factor without offering any accompanying explanations or clarifications. It's unclear how these factors are defined, how they are disentangled, and what their specific roles are within the proposed framework.
W2 - Furthermore, there are certain statements that are not entirely accurate and can be misleading. For instance, the statement 'existing methods assume that the mentioned distribution shifts remain static, and there exist distinct fairness dependence between model outcomes' raises questions about the term 'fairness dependence.' Fairness guarantees are typically associated with model outcomes, so the variable component is not fairness itself, but rather the dependence between the sensitive or spurious feature and the class label. Similarly, the sentence 'the fairness patterns between domains remain constant' should ideally clarify that it is the patterns of dependence between domains that remain constant, not necessarily fairness patterns. The paper should clarify that it is the *conditional* dependence between the sensitive attribute and the class label, given the domain, that is changing, not the overall fairness concept itself.
W3 - The authors assert multiple times that they are introducing a novel form of shift. However, it's important to note that there is an extensive body of literature that has previously examined the effects of spurious correlations when the relationship between the spurious feature and the class label varies across domains. Furthermore, in the field of fairness, there has been prior research on shifts within subpopulations. Hence, the extent to which this claim holds true remains somewhat uncertain. The paper needs to more clearly differentiate its specific contribution from existing work that addresses similar issues, perhaps by focusing on the specific combination of covariate shift and spurious correlation shift, and how their method uniquely addresses this combination.
W4 - On page 5, the statement 'Enforcing constraints on deep networks is known to be a challenging problem' is made without prior reference to any specific type of model. It appears as if the authors assume that the reader implicitly understands that this approach pertains to neural networks, even though they do not explicitly mention specific models anywhere in the text. To address this, the authors could, in the introduction, specify that the presence of spurious correlations is a common issue in deep neural networks (DNNs), thereby clarifying that they are dealing with a particular family of functions. Throughout the text, especially when explaining their approach, it would be beneficial for them to explicitly mention that they are considering neural networks. The absence of such explicit references may indeed present a clear issue. The paper should also specify the type of constraints being enforced, such as regularization terms or architectural constraints.
W5 - The authors initially discuss the challenge of maintaining fairness guarantees under distribution shift, particularly when there are varying dependencies between the sensitive feature and the class feature (a particular case of spurious correlation, when the spurious feature is the sensitive attribute). However, the example they present in the introduction to motivate the problem (Figure 2) pertains to the broader issue of spurious correlations rather than being specific to fairness concerns. In this context, they consider the background as the spurious feature, not necessarily linked to any sensitive attribute. Moreover, in the experimental section, the spurious feature is not always synonymous with a sensitive attribute. As a result, the paper's objective may not be entirely clear, as it's uncertain whether it primarily addresses fairness issues in multi-source domain generalization or aims for a more general approach dealing with subgroup robustness in domain generalization when faced with varying spurious correlations across domains. The paper should clarify whether the sensitive attribute is always a spurious correlation or if the framework is designed to handle spurious correlations more generally, regardless of whether they are sensitive attributes.
W6 - I have noticed that the information provided about fairness concepts in the paper is rather limited. In the paragraph discussing fairness notions, the authors do not acknowledge the existence of various definitions for quantifying the fairness guarantees of a classifier, including statistical notions, individual notions, and mini-max notions. They focus exclusively on statistical notions and, within this category, specifically on demographic parity (DP). It is essential to note that the definition presented in the paper about statistical notions pertains solely to DP. The broader definition of a statistical notion of fairness encompasses parity in a given performance measure across different groups, with the specific terminology of these statistical notions varying based on the performance metric under consideration. Therefore, the paper's definition is not entirely accurate and should be revised. Furthermore, it is advisable for the authors to reference relevant literature that offers an extensive review of existing fairness metrics, providing readers with a more comprehensive understanding of the available fairness measures.
W7 - Also in connection with fairness notions, there are statements that could be potentially misleading. For instance, the assertion that 'the fairness notion $\rho(\hat{Y}, Z)$ is defined as the difference of demographic parity (DP)' might not be accurate. DP itself pertains to the difference in predictions, and, as such, fairness concerns relate to disparities in acceptance rates rather than the difference in DP. The paper should clarify that the fairness metric is measuring the disparity in prediction rates across different groups defined by the sensitive attribute, and not simply the difference in DP itself.
W8 - In the experimental section, the authors evaluate various domain generalization methods, including GDRO, Mixup, and CORAL, which are originally designed for single-source domain scenarios. This may result in an unfair comparison, as they are applied to multi-source data even though they were not explicitly designed for such cases. Moreover, the authors do not clarify that certain baseline domain generalization methods are intended for either single-source or multi-source domain settings, which is a crucial distinction to highlight for a fair evaluation. Additionally, the paper does not provide clear information on how they adapt single-domain methods to handle multiple domain data. The paper should explicitly state how these single-source methods are adapted to the multi-source setting, including any modifications or assumptions made.
W9 - In the section addressing related works, specifically within the paragraph titled 'Fairness learning for changing environments,' the references provided are notably limited. Notably, several domain adaptation works in fairness have been explored, but these are not mentioned in the current text. It would be beneficial to refer to [1], where readers can access a comprehensive overview of the field about approaches aimed at maintaining fairness guarantees of classifiers in evolving or changing environments. Additionally, in the context of domain generalization amidst spurious correlations, it's worth noting that the paper lacks references to more recent works, such as [2]. The related works section should be expanded to include more recent and relevant work in both fairness-aware domain adaptation and domain generalization under spurious correlations.
W10 - The paper contains several issues related to its references. Firstly, in the introduction, there is a duplication of references, specifically for Pham et al. and Robey et al. Additionally, there is a need to differentiate between explicit and implicit citations. For instance, in the sentence 'in addition to the two distribution shifts stated in (Robey et al., 2021),' the reference should appear without parentheses. Moreover, within the list of references, there are arXiv references for papers that have already been published, such as in the case of (Sagawa et al.) which was published as a conference paper at ICLR 2020.
W11 - No constraints or limitations explicitly pointed out in the main text.

### Questions
Q1 - What was the rationale behind selecting the concept of demographic parity (DP)? Why was the consideration of worst-group accuracy, a conventional fairness indicator in the literature concerning generalization challenges amid spurious correlations, not included in your study?
Q2 - Is it feasible to readily extend this approach to accommodate other fairness concepts, such as Equality of Opportunity, which requires access to true labels? Can it be adapted to address mini-max notions of fairness?
Q3 - How do you adapt single-domain methods to handle multiple domain data?
Q4 - Is the existence of T always guaranteed? Are there any limitations w.r.t.  T?
Q5 - Can this be applied in multi-dimensional sensitive attributes, or in the presence of intersectional groups? 
Q6 - Does your model have constraints or limitations?
Q7 - How does the computational burden of your method compare to state-of-the-art approaches?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
