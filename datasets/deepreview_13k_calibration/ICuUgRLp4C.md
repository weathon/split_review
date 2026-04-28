# Learning High-Order Relationships of Brain Regions

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 3, 6, 6

## Abstract
Discovering reliable and informative relationships among brain regions from functional magnetic resonance imaging (fMRI) signals is essential in phenotypic predictions. Most of the current methods fail to accurately characterize those interactions because they only focus on pairwise connections and overlook the high-order relationships of brain regions. We propose that these high-order relationships should be \textit{maximally informative and minimally redundant} (MIMR).
However, identifying such high-order relationships is challenging and under-explored due to the exponential search space and the absence of a tractable objective. %Methods that can be tailored to our context are also non-existent.
In response to this gap, we propose a novel method named \mname{} which aims to extract MIMR high-order relationships from fMRI data. \mname{} employs a \textsc{Constructor} to identify hyperedge structures, and a \textsc{Weighter} to compute a weight for each hyperedge, which avoids searching in exponential space. \mname{} achieves the MIMR objective through an innovative information bottleneck framework named \multiheadname{} with theoretical guarantees. Our comprehensive experiments demonstrate the effectiveness of our model. Our model outperforms the state-of-the-art predictive model by an average of $11.2\%$, regarding the quality of hyperedges measured by CPM, a standard protocol for studying brain connections.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposed a hypergraph inference method based on optimizing the predictive power (in the form of mutual information) of the selected ("connected by hyperedge") graph node towards certain labels and the redundancy term. The effectiveness of the inference method was evaluated based on an fMRI condition classification task with comparison to pair-wise connectivity estimation and connectivity-based cognition prediction methods and achieved superior performance.

### Strengths
Eq. 9 and 10 provide a useful solution for the MRMR-like feature selection problem.

### Weaknesses
Formulating the hyperedge inference problem into a feature selection (MRMR-like) problem is interesting, yet not valid, at least in the context of functional connectivity analysis. Regions that are predictive together towards a certain cognitive condition do not imply that they are functionally connected. It's actually easy to construct a case where two regions have very similar fMRI signals, indicating potential strong functional connectivity, but will not be considered as "hyperedge connected" in the presented model as their information is redundant for the prediction. The core issue is that the method conflates predictive power with functional connectivity, which are distinct concepts. The method selects hyperedges based on their ability to predict a cognitive score, but this does not necessarily reflect underlying neural interactions. For example, two regions might independently correlate with a cognitive score, but have no direct functional relationship. The MRMR approach, while effective for feature selection, is not appropriate for inferring functional connectivity because it prioritizes non-redundant predictive features, rather than identifying actual neural relationships. This can lead to the selection of hyperedges that are statistically predictive but neurobiologically meaningless.

### Questions
1) How is the p-value calculated for the hyperedge in Fig. 4?
2) It is recommended to discuss how the DimReduction MLP could be trained with a large number of nodes.
3) Are the linear-head Fl shared across hyperedges or trained separately for each hyperedge?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper attempts at capturing multivariate relationships among a set or random variables as would be captured by edges in a hypergraph representation. For that, the paper constructs a differentiable regression model that first applies a set of learnable square (for the number of regions) linear projection with subsequent thresholding of the output - a mask, then applies an MLP to compute a scalar value (weight) for each of the masked subsets of the nodes. The weights are used to produce a scalar value (after an inner product with the output weight vector). This model is trained in a regularized regression manner and the produces features are evaluated in an acceptable feature selection evaluation pipeline using predictive strengths of the features as final evaluations. The approach is applied to a subset of the ABCD dataset.

### Strengths
The paper contains an interesting approach to model building, where an encoder builds clustering - a representation interpretable to human experts. A glass-layer with the partition clearly visible. Potentially, a rewrite of the paper could focus on this part, instead of the unsubstantiated claims about capturing high-order interations

### Weaknesses
1.  **The positioning of the paper is a problem.** The assertion that it captures high-order interaction is not substantiated, even though the feature selection model's entire motivation hinges on this claim. Certainly, the title emphasizes high-order interaction. However, the exact type of high-order interaction that the proposed model captures remains ambiguous. I would suggest considering the following papers, which were mistakenly overlooked. These papers seek to formally define what is being captured before attempting to estimate the interactions:
    -   Rosas FE, Mediano PA, Gastpar M, Jensen HJ. [Quantifying high-order interdependencies via multivariate extensions of the mutual information](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.100.032305). Physical Review E. 2019 Sep 13;100(3):032305.
    -   Varley TF, Pope M, Faskowitz J, Sporns O. [Multivariate information theory uncovers synergistic subsystems of the human cerebral cortex](https://www.nature.com/articles/s42003-023-04843-w). Communications biology. 2023 Apr 24;6(1):451.
    -   Santoro A, Battiston F, Petri G, Amico E. [Higher-order organization of multivariate time series](https://www.nature.com/articles/s41567-022-01852-0). Nature Physics. 2023 Feb;19(2):221-9.
2.  **The clarity of the writing, with regard to the implementation**, is also inadequate in other sections. If we are estimating a hypergraph, then the edges, or node clusters, should form a cover rather than a partition. However, the regularization of the Mean Squared Error (MSE) used in Equation 11, as well as a preceding statement, both confirm the need for the edges to be disjoint, thereby suggesting a partition. This leads us back to the issue of positioning as it means that what is proposed is a clustering algorithm or the task of finding a partition. It's worth noting that node partitioning can still be conducted to recover high-order interactions, as has been exemplified in the neural imaging context, for instance, here:
    -   Plis SM, Sui J, Lane T, Roy S, Clark VP, Potluru VK, Huster RJ, Michael A, Sponheim SR, Weisend MP, Calhoun VD. [High-order interactions observed in multi-task intrinsic networks are dominant indicators of aberrant brain function in schizophrenia.](https://www.sciencedirect.com/science/article/pii/S1053811913007970) NeuroImage. 2014 Nov 15;102:35-48.
3.  Overall, **the approach feels like an ad hoc method** for grouping the feature vectors via their predictive potential for a dependent variable. Even the input features are correlation coefficients. That is, the initial input matrix for each subject is the correlation matrix of which the goal is to subselect rows (or columns, which is equivalent due to symmetry) into K different groups.
4.  **Comparisons in Table 1 are highly problematic** as well.
    1.  If the goal is to find high-order relations what does predictive quality of representations has to do with it? Table 1 in my opinion does not belong in a paper on high-order relations.
    2.  However, if the paper would be rewritten to focus on feature grouping and clustering, this approach may potentially work although not without changes. In this case, the proposed model needs to be compared with other approaches that do clustering or partition of random variables. For example, it seems appropriate to consider comparison with Deep Clustering.
5.  **Results are confusing.** They do not show individual "hyperedges" and analyze the ROIs that have grouped together and explain high-order interactions that grouped them. If the regularization enforces the partition, why are so many clusters overlap per my interpretation of Figures 5 and 4c?

### Questions
Note, I do not think answering my question below can change the problems with the way it is written which lead to experiments not supporting the claims. My comments below are to help future clarity of the work:

1.  The abstract states that CRM measures quality of hyperedges, however, CRM looks like a feature selection protocol that also has recommendations for assessing predictivity of the features. This is a disconnect between what is claimed and what is presented.
2.  The beginning of the second paragraph of the Introduction needs references to support the claim. The last phrase of that paragraph needs a rewrite "of the intricate behind brain regions"
3.  Section 2.1 "Inupt" - Do you mean Input?
4.  Section 2.2 describes feature selection - why is this tied to high-order interactions. Confusing.
5.  Section 4.1 what do you mean by "N-dimensional shallow embedding layer parameterized by". It would be best if all operations and parameters were clearly defined. I assume this is a linear transformation but that is a guess.
6.  Hyperedge weighting. MLP is not a sufficient description of the used model. Please also mention the activation function.
7.  Baselines: "standard" method mentioned there is unclear. What is standard? How is it defined?
8.  Why the model is compared with arbitrary models that solve problems different from the proposed method? How were models shown in the comparison selected?
9.  Ktena, Li, and Kan papers do not construct hypergraphs and yet used as such in the paper for comparisons. Confusing.
10. Consider fixing capitalization in your bib file. To do that, you can go over the cited papers in your .bib file and put all words you want to preserve capitalization of in additional curly braces. Like {fMRI}.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a principle to learn high-order relationships of brain regions -- high-order relationships should be maximally informative and minimally redundant (MIMR), and a method called Hypergraph of Brain Regions via multi-head Drop- bottleneck (HyBRiD) to learn such relationships from fMRI data. HyBRiD includes a constructor to identify hyperedge structures, and a weighter to compute a weight for each hyperedge. The results show that HyBRiD outperformed 8 baseline methods in 7 out of 8 fMRI datasets.

### Strengths
1. The paper is well written with clear organization, detailed theoretical explanation, and comprehensive empirical evaluation. 

2. The proposed method is intuitively simple yet effective, and could be potentially applied to learn high-order relationships of brain regions with respect to different prediction targets. 

3. The neuroimaging experiments were comprehensive. A large sample size (8 datasets with 11875 subjects) was used to evaluate the models. The proposed method HyBRiD was compared to 3 types of baseline methods including 8 methods. HyBRiD outperformed 8 baseline methods in 7 out of 8 datasets. 

4. The hyperedge profile analysis indicates interactions of multiple brain regions are more important in cognition tasks. The region importance reveals reasonable task-related brain regions under different conditions.

### Weaknesses
1. The authors mentioned that "Due to the data scarcity, training on individual datasets would result in serious overfitting." Each individual dataset includes at least 1000 subjects but the model performance is still not ideal. Can the model be applied to a dataset with less samples? Most clinical datasets are relatively small with < 1000 subjects. Is it applicable to apply the model on datasets with fewer samples? Specifically, the paper lacks a discussion on the minimum data requirements for the proposed method to achieve a reasonable level of performance, and whether the method can be adapted for smaller datasets using techniques like transfer learning or data augmentation.

2. It would be helpful if the authors could discuss potential reasons why HyBRiD failed at Rest 1 dataset. A more detailed analysis of the specific characteristics of the Rest 1 dataset that might have contributed to the performance drop would be beneficial, including potential issues with data quality, subject variability, or task-related confounds that might be present despite being a resting-state dataset. Furthermore, a comparison of the training dynamics on Rest 1 versus other datasets could provide insights into the overfitting or underfitting behavior of the model.

3. Region importance. What about region importance for resting state data? If I understand it correctly, region importance is a metric for nodes. What about edges? Can you show how edges are connected under different conditions? The analysis of edge importance and their connections across different conditions is crucial for understanding the brain's functional architecture, and the paper currently lacks a discussion on how the proposed method can be used to analyze these higher-order interactions beyond node importance.

4. I appreciate that the authors include the code in supplemental material, but a README file should be also included to explain how to replicate the results. The absence of clear instructions makes it difficult to reproduce the results and hinders the usability of the code for other researchers.

5. The notations in Section 5.1 Metric are not very clear to me.
	i. The input of CPM should include the prediction target Y, right? Maybe use CPM(E, Y)?
	ii. What is the dimension of E? Is E equivalent to H+$\mathbf{w}$ in HyBRiD?
	iii. CPM is evaluated on each model separately, right? If so, I think Eq. 13 should be defined separately for HyBRiD.

6. Minor:
	i. Typos: Section 2.1 "Inupt" should be "Input"; Section 5.2 "conducte" should be "conduct"; Figure 7: "grpahical" should be "graphical".
	ii. CPM should be defined in the abstract and introduction upon its first occurrence.
	iii. In Section 5.1 Dataset, RS (resting state) should be defined.
	iv. In Table 5, $\beta = 0.2$ instead of $0.3$ to be consistent with Section E.3?

### Questions
1. Does the model generalize well across conditions or out-of-sample data? For example, if a model is trained on resting state data, can it be applied to predict task data?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper proposes a novel method named HYBRID for extracting maximally informative and minimally redundant high-order relationships from fMRI data. The authors argue that most current methods fail to accurately characterize interactions among brain regions because they only focus on pairwise connections and overlook high-order relationships. HYBRID addresses this limitation by constructing a hypergraph where hyperedges represent high-order relationships and their weights represent the strengths of those relationships. The authors demonstrate the effectiveness of HYBRID through comprehensive experiments, outperforming the state-of-the-art predictive model by an average of 12.1%. The contributions of this paper include a novel method for extracting high-order relationships from fMRI data and a comprehensive evaluation of the proposed method.

### Strengths
Originality: The paper proposes a novel method named HYBRID for extracting maximally informative and minimally redundant high-order relationships from fMRI data. This is a significant contribution as most current methods focus on pairwise connections and overlook high-order relationships. HYBRID addresses this limitation by constructing a hypergraph where hyperedges represent high-order relationships and their weights represent the strengths of those relationships. The proposed method is original and creative, and the authors provide a comprehensive evaluation of the proposed method, demonstrating its effectiveness through experiments.

Quality & clarity: The paper presents a clear problem formulation, a detailed description of the proposed method, and a comprehensive evaluation of the proposed method. The authors provide theoretical guarantees for the proposed method and demonstrate its effectiveness through experiments. The paper is well-written, with clear and concise language, making it easy to understand.

Significance: The paper addresses an important problem in neuroscience and machine learning. Discovering reliable and informative interactions among brain regions from fMRI signals is essential in neuroscientific predictions of cognition. Most of the current methods fail to accurately characterize those interactions because they only focus on pairwise connections and overlook the high-order relationships of brain regions. The proposed method addresses this limitation and provides a new approach for extracting high-order relationships from fMRI data.

### Weaknesses
The matrix notation in SEction 4 is confusing:
Section 4.1, first line: $X = [X_1, X_2, \dots, X_N]$ should be $X = [X_1, X_2, \dots, X_N]^T$ (i.e., a transpose operator should be inserted).
Eq. (4): a transpose operator should be inserted after the square brackets.

### Questions
Can you briefly explain how to choose the number of hyperedges?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
