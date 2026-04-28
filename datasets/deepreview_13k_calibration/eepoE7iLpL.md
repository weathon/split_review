# Enhancing Neural Subset Selection: Integrating Background Information into Set Representations

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Learning neural subset selection tasks, such as compound selection in AI-aided drug discovery, have become increasingly pivotal across diverse applications. The existing methodologies in the field primarily concentrate on constructing models that capture the relationship between utility function values and subsets within their respective supersets. However, these approaches tend to overlook the valuable information contained within the superset when utilizing neural networks to model set functions. In this work, we address this oversight by adopting a probabilistic perspective. Our theoretical findings demonstrate that when the target value is conditioned on both the input set and subset, it is essential to incorporate an \textit{invariant sufficient statistic} of the superset into the subset of interest for effective learning. 
This ensures that the output value remains invariant to permutations of the subset and its corresponding superset, enabling identification of the specific superset from which the subset originated. 
Motivated by these insights, we propose a simple yet effective information aggregation module designed to merge the representations of subsets and supersets from a permutation invariance perspective. 
Comprehensive empirical evaluations across diverse tasks and datasets validate the enhanced efficacy of our approach over conventional methods, underscoring the practicality and potency of our proposed strategies in real-world contexts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an optimal subset selection method based on neural networks, which is designed to learn a permutation invariant representation of both the subset of interest $S$ and the ground superset $V$. The authors highlight that prior works for neural subset selection (e.g., DeepSet) do not account for the superset $V$, and both theoretically and empirically demonstrate that jointly modeling the interactions between $S$ and $V$ leads to improved performance.

### Strengths
- The writing is generally easy to follow, and the paper includes a sufficiently comprehensive discussion of relevant prior works. Experimental results are presented well.
- The proposed method achieves strong empirical performance in terms of mean Jaccard coefficient (often with a fairly large gap) when compared against several optimal subset selection baselines (e.g., DeepSet, EquiVSet).

### Weaknesses
 - The presentation of some of the mathematical details needs improvement. In particular, it seems that some of the notations are overloaded (i.e., the same notation is used with different interpretations) or not clearly defined. For example, the notation $S$ appears as a *subset* of the ground set $V$ in the Introduction, but in Section 3.1 (Background), the notation $S$ appears as an *element* of $V$ that takes a matrix form. The relationship between elements $x_i \in \mathcal{X}$ and $S_i$ is not clearly defined either. On another note, it is not entirely clear to me what the function value $Y \in \mathcal{Y}$ is really referring to, which also appears without an explicit discussion of its meaning in the Introduction as part of the variational distribution $q(Y|S,V)$. Is $Y \in \mathcal{Y}$ supposed to be the utility function value (which was also introduced with the notation $U = F_{\theta}(S,V)$ in the Introduction)? The confusion arising from notational ambiguity makes the paper less readable.



### Questions
- Can the authors clearly define what $Y$ is? The footnote mentions that $Y_i$ is the "probability of element $i$ being selected", but this description is ambiguous.
- It looks like learning the neural network approximation in Eq. (4) is done via variational inference as in Ou et al. (2022). As I am not familiar with the cited work, it is unclear to me how $q(Y|S,V)$ is serves as an approximation for the subset likelihood $p(S|V)$ when the former is a distribution over $Y$ and the latter is a distribution over $S$. Can the authors provide clarifications on this?
- How is the neural network construction in Eq. (4) explicitly related to $p_{\theta}(S,V)$ (or $F_{\theta}(S,V)$)?

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackles neural subset selection. In particular, they tackle the issue that current methods do not consider the properties of the superset while constructing subsets. Their theoretical findings demonstrate that when the target value is conditioned on both the input set and subset, it is essential to incorporate an invariant sufficient statistic of the superset into the subset of interest for effective learning.

### Strengths
- The paper is clearly written.
- The related work covers enough ground for a new researcher to understand a high level idea of this field.
- The experiments include multiple baselines.

### Weaknesses
 - Lack of ablation studies.
- The proposed method is not evaluated on a wide distribution of datasets.
- Will similar findings hold if the dataset contains imbalance? If so, what degree of imbalance do the guarantees still hold?

### Questions
- Baselines do not consider the information from superset, but these baselines be improved by adding the invariant sufficient statistic of the superset?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a neural subset selection method based on deep sets. This model is inspired by a theoretical perspective to include information from supersets to achieve better performance. Experiments on common benchmarks show SOTA performance compared to several recent baselines.

### Strengths
1. The idea to include information from superset is simple and effective as shown by the experiment results
2. Theoretical discussions are provided.

### Weaknesses
1. Equation 4 describes the neural network construction. However, I am unclear about the objective function to optimize the neural network. Also, after optimization, how do you use this neural network to select a subset?

2. In equation 4, how do you divide a superset into several subsets? There are an exponential number of combinations.

3. What is the number of learnable parameters for each baseline method and the proposed method?

### Questions
None

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
