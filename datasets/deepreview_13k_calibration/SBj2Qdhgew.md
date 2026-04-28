# Demystifying Local & Global Fairness Trade-offs in Federated Learning Using Partial Information Decomposition

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
This work presents an information-theoretic perspective to group fairness trade-offs in federated learning (FL) with respect to sensitive attributes, such as gender, race, etc. Existing works often focus on either $\textit{global fairness}$ (overall disparity of the model across all clients) or $\textit{local fairness}$ (disparity of the model at each client), without always considering their trade-offs. There is a lack of understanding regarding the interplay between global and local fairness in FL, particularly under data heterogeneity, and if and when one implies the other. To address this gap, we leverage a body of work in information theory called partial information decomposition (PID), which first identifies three sources of unfairness in FL, namely, $\textit{Unique Disparity}$, $\textit{Redundant  Disparity}$, and $\textit{Masked Disparity}$. We demonstrate how these three disparities contribute to global and local fairness using canonical examples. This decomposition helps us derive fundamental limits on the trade-off between global and local fairness, highlighting where they agree or disagree.  We introduce the $\textit{Accuracy and Global-Local Fairness Optimality Problem}$ (AGLFOP), a convex optimization that defines the theoretical limits of accuracy and fairness trade-offs, identifying the best possible performance any FL strategy can attain given a dataset and client distribution. We also present experimental results on synthetic datasets and the ADULT dataset to support our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces information theoretic tools to interpret the relationship among multiple group fairness trade-offs in federated learning. It is commonly known that global and local fairnesses both contribute to unfairness in federated learning, but their relationship (e.g. whether one implies the other) is unknown. The authors identify three fundamental sources of unfairness, and utilize them to derive fundamental limits on the trade-offs between global and local unfairnesses.

### Strengths
This paper provides a novel "solution" for unfairness in federated learning. Even if this issue has been extensively studied, there has been few work attempting to investigate the fundamental root that causes unfairness, let alone giving a theoretical explanation. This work uses a mathematically rigorous tool to give a promising attempt to explain unfairness. The theoretical justifications are rigorous and insightful.

In particular, Theorems 1, 2 and 3 are both conclusive and powerful, so that one may predict the fairness performances based upon those three sources of unfairness.

### Weaknesses
Overall this paper is well-written, but in Section 2, it would be great if the authors could provide some more justifications for Definitions 1 and 2, both mathematically and conceptually, even if the definitions are indeed fairly intuitive. This may be immensely helpful for readers especially those who do not have a strong background in information theory.

Specifically, while the use of mutual information to quantify dependence between sensitive attributes and model predictions is not novel, the specific choice of conditional mutual information for local fairness, and the subsequent decomposition into unique, redundant, and synergistic components, could benefit from more detailed motivation. The paper would be strengthened by a discussion of why this particular decomposition is more insightful than other possible approaches. For example, how does this decomposition relate to existing notions of group fairness, such as statistical parity or equal opportunity, and what are the advantages of using this information-theoretic approach over more traditional metrics?

### Questions
1. This was mentioned in the Weaknesses section, and I would be very interested in seeing more explanations for choosing those definitions.

2. Under a concrete data set, how are Uni(), Red(), and Syn() efficiently computed? I might be wrong, but my first impression is that, since they are relevant with mutual information, such computation may be expensive?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents an information-theoretic perspective on group fairness trade-offs in federated learning (FL) with respect to sensitive attributes. This paper leverages partial information decomposition to identify three sources of unfairness in FL. They introduce AGLFOP, a convex optimization that defines the theoretical limits of accuracy and fairness trade-offs, identifying the best possible performance any FL strategy can attain given a dataset and client distribution.

### Strengths
1. This paper studies group fairness from an information theory perspective, which is valuable for the community to understand the group fairness of FL.
2. The decomposition result is interesting.

### Weaknesses
1. Although this paper proposes an optimization framework with Definition 5, it does not give any solution or algorithm for solving the problem. 
2. The experiments are somehow weak, both the baseline and dataset are rare. There are other works focusing on FL group fairness like [1,2], and also about fairness and accuracy tradeoffs, like [3], that should be compared. The lack of comparison with established group fairness baselines in FL makes it difficult to assess the practical significance of the proposed framework. The chosen datasets also seem to be limiting the scope of the experimental validation.
3. The visualization (table or figure) of accuracy and global-local fairness trade-off results is relatively insufficient relying solely on the Pareto Frontiers shown in Figure 3. The Pareto frontiers, while useful, do not provide an intuitive understanding of the trade-offs in different scenarios. A more granular analysis, perhaps using tables or additional plots, would be beneficial.
4. It seems of vital importance to properly set the hyper-parameters $\epsilon_g$ and $\epsilon_L$ for the optimal trade-off. The acc-fairness Trade-off figure displayed in Figure 3, lacks discussion based on more experimental settings and datasets. The sensitivity of the results to these parameters is not thoroughly explored, which is a significant concern for practical applications. Without a clear methodology for setting these parameters, the practical utility of the framework is questionable. 
5. The experiment setting details are not clear, for example, what is the used model and parameter settings?

Minors:
What is the formal definition of global fairness and local fairness?

### Questions
1. Could you explain the main difference from [4]?  It seems it is a trivial improvement (Apply the PID analysis on FL) compared with this paper.
2. Could you provide experiments of different baselines and different datasets, in the FL setting (partial client participation of cross-device FL.)
3. Could you provide more results for trade-offs on accuracy and global-local fairness?
4. Could you provide more details about the selection of hyperparameters to ensure optimal trade-off strategy under different data distributions and datasets?

[4] Dutta S, Hamman F. A Review of Partial Information Decomposition in Algorithmic Fairness and Explainability[J]. Entropy, 2023, 25(5): 795.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the problem of trying to achieve fairness in a federated learning setting. There are multiple data sets that are all privately held and a model is trained for each one. The questions are: When are the models fair on each data set? And, when are the models fair on all the data?

The paper relates fairness in both settings and mutual information. In particular, they show that mutual information between the  model's prediction and the sensitive attribute is an upper bound on the square of statistical parity (Lemma 1). They also define "local disparity" as mutual information conditioned on the particular machine. They then analyze mutual information and show it comes from three sources: information only in the predictions or sensitive attributes, information in both individually, or information in both together.

They prove necessary/sufficient conditions about when mutual information is low depending on the sources of mutual information. I did not check the appendix for the proofs of these results.

They introduce a convex optimization problem for minimizing classification error subject to constraints that the mutual information and local information are low. They they solve the problem experimentally for different datasets and visualize the results.

### Strengths
• The paper investigates the problem of relating global and local fairness in the federated learning setting. According to them (I have not checked), the problem has not been studied before.

• The use existing literature on partial information decomposition to identify sources of mutual information. 

• There are a ton of lemmas and theorems about when mutual information is small. It appears very comprehensive but I'd like a more direct narrative about what I should be surprised and impressed with.

• I like the idea of the convex optimization problem and optimizing for error under mutual information constraints.

• The experiments seem very comprehensive in terms of data sets and different settings of data distributions across clients.

### Weaknesses
• They don't persuade me that mutual information is the "right" notion of fairness. Lemma 1 establishes that mutual information is an *upper bound* on statistical parity but it could be a loose upper bound.

• I think the presentation is difficult to follow and the paper should be rewritten in the following ways:
- Give an example of the way the theorems and lemmas are proved.
- I was confused by the general approach until I read the examples in Section 3.1. These examples aren't results so I think they should be moved up to the preliminaries section to facilitate understanding.
- Lemma 1 and Lemma 2 are results proved by the authors but they appear in the preliminaries section. This was confusing to me especially because there was no discussion of how they were proved.
- Unique information is used in the preliminaries before it is defined in Definition 3. I didn't find this definition helpful and I don't see similar definitions for redundant information or synergistic information. It would be great if you could define these three quantities in a direct and similar way. I don't know if this is true but maybe something like I(Z,Y|A \cap B) is redundant information and I(Z,Y |A \cup B) is synergistic information. I found the notation you used excessive.
- I'm not sure from reading the main result section if the proofs of the theorems/lemmas following trivially from the definitions or not. Please make this clear with a proof of one of them.

• The convex optimization section is very short. I think you should restructure to spend more space here given that it's one of your contributions.

• I got the sense that the experiments were comprehensive but I was missing a discussion about what was interesting here. It'd be great to highlight interesting observations and findings from the experiments. Examples of how the mutual information perspective gives insight into local and global fairness would be great.

### Questions
Lemma 1 upper bounds statistical parity with mutual information, how loose is the upper bound?

What are interesting observations from your expeirments?

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent
