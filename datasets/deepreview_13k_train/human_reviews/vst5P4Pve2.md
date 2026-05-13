# Towards Global Interaction Efficiency of Graph Networks

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
A graph inherently embodies comprehensive interactions among all its nodes when viewed globally. Hence, going beyond existing studies in long-range interactions, which focus on interactions between individual node pairs, we study the interactions in a graph through a global perspective. Traditional GNNs acquire such interactions by leveraging local connectivities through aggregations. While this approach has been prevalent, it has shown limitations, such as under-reaching, and over-squashing. In response, we introduce a global interaction perspective and propose interaction efficiency as a metric for assessing GNN performance. This metric provides a unified insight for understanding several key aspects of GNNs, including positional encodings in Graph Transformers, spectral graph filter expressiveness, over-squashing, and the role of nonlinearity in GNNs. Inspired by the global interaction perspective, we present Universal Interaction Graph Convolution, which exhibits superior interaction efficiency. This new architecture achieves highly competitive performance on a variety of graph-level learning tasks. Code is available at https://github.com/iclrsubmission-towards/UIGC.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors aim to investigate the global interactions in graphs. In particular, they propose a metric named global efficiency for accessing GNNs' performance. It moves beyond the traditional approach of focusing on local interactions between individual node pairs and examines GNN interactions from a global perspective. Furthermore, inspired by the insights from these investigations, they propose Universal Interaction Graph Convolution (UIGC) with very superior interaction efficiency.

### Strengths
*Originality*: The paper is original in its approach to a fundamental challenge in the field of GNNs. It introduces the novel concept of universal interaction expression within graphs, surpassing conventional limitations. The proposed solution to utilize the Jacobian matrix for quantifying interaction efficiency, distinguishing between interaction sensitivity and expressiveness, is original and useful.


*Significance*: The paper has the potential to enhance the capabilities of GNNs from a new perspective.

### Weaknesses
 *Motivation*: It would be helpful if the authors could provide better motivations for some of their arguments and designs. For instance, throughout the paper, the authors are discussing about pair interactions. However, it is not very clearly demonstrated why they are so important.

*Experiments*: The results in Table 2 and Table 3 show that the proposed method achieves strong performance on some of the datasets while falling short on some others. It would be helpful if the authors could provide more explanations on why this is the case. Some investigations into the data properties and their connections to global interactions would be especially helpful.

### Questions
Please address the questions in the Section of weakness. In addition, there are a few other questions as follows.

1. In Figure 1, why do we specifically care about pairs of nodes and their interactions? It would be better if the authors could provide more details and better descriptions. 

2. It might be helpful if the authors could provide some examples on how the proposed method is more expressive in terms of capturing patterns such as "benzene rings" (mentioned in the introduction). 

3. The setup for Section 5.1 is not very clear. It would be helpful if the authors could provide more descriptions of the synthetic interaction patterns. In particular, what is the value in the y-axis in Figure 3?

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
This paper studies the expressiveness of graph neural networks. In particular, it focuses on the "global efficiency" of GNNs, and the analytical tool this paper proposed is to study the Jacobian matrix of the graph convolution layer.

### Strengths
S1. This paper is of good presentation.

S2. The analytic tool proposed by this paper, Jacobian matrix of the graph convolution layer and its determinant, is reasonable.

S3. Experiments of this paper include broad baseline methods and datasets.

S4. This paper is open-sourced to ensure its reproducibility.

### Weaknesses
W1. A part of the theory proposed by this paper is problematic.

W2. Some existing contributions are not clearly mentioned, which somehow undermines the contribution of this paper.

W3. Writing in Section 4 can be improved to make the proposed method more clear.

W4. A minor weakness is that the baselines can be selected to only include the most SOTA baselines, and try to ensure most baselines have results on all the datasets (but not only report the results from the original papers)

Q1. Seems Proposition 5 conflicts with the core idea of this paper. If I understand correctly, the core idea of this paper is "to ensure all symmetric pairs, i.e., within the same pair partitions, learn the same interaction" (from the bottom of Page 5). However, one of the assumptions of Proposition 5 says that $\varphi$ is an injective function, which conflicts with the idea that "symmetric" but different node pairs can learn the same interaction.

Q2.The core design of the proposed UIGC is the $\varphi^{LE}$. However, it is not clearly mentioned what the specific $\varphi^{LE}$ is used in this paper. Table 4 and Figure 4 only show the $\varphi^{LE}$ of existing methods.

Q3. The study on global interaction efficiency is not new. For example, this paper cites [1], which studies “total resistance” $R_{tot}$, a quantitative measure of global interaction efficiency. Thus, the authors should revise the statement of their first contribution. Furthermore, it does not seem necessary to distinguish “global” and “local” interaction efficiency because what the authors mean by “global” is just a function (i.e., determinant, in Section 3.1) of the “local” interaction efficiency matrix ($\mathbf{J}_{\theta,W}$ in Eq. (2)).

Q4. Their UIGC might not be scalable because UIGC needs to compute graph automorphism, which seems to require at least $O(mn^2)$ time. A more efficient approach to addressing the long-distance interaction issue might be increasing the GNN depth together with techniques to alleviate oversquashing (e.g., [2,3] can train GNNs with 7~1000 layers.), or as simple as adding a supernode. Authors should compare with such methods in terms of both efficiency and performance in their experiments.

C1. The applicable scope of graph automorphism might be limited. A classic result (see, e.g., theorem 2 in [4]) shows that almost all graphs do not have non-trivial automorphism, i.e., in almost all graphs, all but at most one pair of nodes are non-equivalent. In practice, only very special graphs like locally symmetric molecules have non-trivial automorphism. This limitation is also supported by their experiments because their UIGC has at most marginal gain on IMDB and RDT (social network datasets).

C2. The discussion at the end of Section 4 looks vague. It might be more meaningful and more interesting if the authors can extend the discussions to rigorous theoretical analysis.

### Questions
Q1. Seems Proposition 5 conflicts with the core idea of this paper. If I understand correctly, the core idea of this paper is "to ensure all symmetric pairs, i.e., within the same pair partitions, learn the same interaction" (from the bottom of Page 5). However, one of the assumptions of Proposition 5 says that $\varphi$ is an injective function, which conflicts with the idea that "symmetric" but different node pairs can learn the same interaction.

Q2.The core design of the proposed UIGC is the $\varphi^{LE}$. However, it is not clearly mentioned what the specific $\varphi^{LE}$ is used in this paper. Table 4 and Figure 4 only show the $\varphi^{LE}$ of existing methods.

Q3. The study on global interaction efficiency is not new. For example, this paper cites [1], which studies “total resistance” $R_{tot}$, a quantitative measure of global interaction efficiency. Thus, the authors should revise the statement of their first contribution. Furthermore, it does not seem necessary to distinguish “global” and “local” interaction efficiency because what the authors mean by “global” is just a function (i.e., determinant, in Section 3.1) of the “local” interaction efficiency matrix ($\mathbf{J}_{\theta,W}$ in Eq. (2)).

Q4. Their UIGC might not be scalable because UIGC needs to compute graph automorphism, which seems to require at least $O(mn^2)$ time. A more efficient approach to addressing the long-distance interaction issue might be increasing the GNN depth together with techniques to alleviate oversquashing (e.g., [2,3] can train GNNs with 7~1000 layers.), or as simple as adding a supernode. Authors should compare with such methods in terms of both efficiency and performance in their experiments.

**Two comments/suggestions:**

C1. The applicable scope of graph automorphism might be limited. A classic result (see, e.g., theorem 2 in [4]) shows that almost all graphs do not have non-trivial automorphism, i.e., in almost all graphs, all but at most one pair of nodes are non-equivalent. In practice, only very special graphs like locally symmetric molecules have non-trivial automorphism. This limitation is also supported by their experiments because their UIGC has at most marginal gain on IMDB and RDT (social network datasets).

C2. The discussion at the end of Section 4 looks vague. It might be more meaningful and more interesting if the authors can extend the discussions to rigorous theoretical analysis.

[1] Black, Mitchell, Zhengchao Wan, Amir Nayyeri, and Yusu Wang. "Understanding oversquashing in gnns through the lens of effective resistance." ICML 2023.

[2] Li et al. DeepGCNs: Can GNNs go as deep as CNNs? ICCV 2019.

[3] Li et al. Training graph neural networks with 1000 layers. ICML 2021.

[4] Erd ̋os & R ́enyi. Assymetric graphs. Acta Math. Acad. Sci. Hungar., 14:295–315, 1963.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors aim to address the limitations of existing GNNs in representing interactions. They propose to study interactions between node pairs in a graph from a global perspective. They also propose a metric called interaction efficiency for assessing GNN performance. In the analysis of interaction efficiency,  two aspects - interaction sensitivity and interaction expressiveness - are discussed. Finally, a new GNN model, called Universal Interaction Graph Convolution (UIGC), is presented. The authors claim that this proposed GNN model has superior interaction efficiency.

### Strengths
Studying interactions among nodes in a graph is of significance to both theoretical foundations and practical applications of the GNN community. Thus, the paper is tackling an important topic. The intention of characterising interactions from the lens of efficiency, sensitivity, and expressiveness also has some novelty. However, the quality of the paper is a concern (see comments in the section "Weaknesses").

### Weaknesses
(W1)  The key concepts of the paper (such as global/universal interaction, interaction sensitivity, and interaction expressiveness) are not well-defined.

- The definition of global interaction is defined in terms of the channels of inputs and outputs. How does this relate to interaction patterns, e.g., the five synthetic interaction patterns in Section 5.1? Also, how does this relate to node/pair symmetry? Specifically, the connection between the $n \times n$ interaction matrix and the actual interaction patterns is unclear. The paper needs to clarify how the entries of this matrix correspond to specific interaction behaviors between node pairs, especially considering the symmetry inherent in graph structures. The notion of 'global' interaction, while presented mathematically, lacks a clear intuitive explanation in relation to the observed interaction patterns.

- For "how a model can universally express any desired interaction within a given graph", what does "universally" mean? The paper also mentions universal interaction but no formal definition is provided. The term 'universally' needs to be rigorously defined. Does it imply the ability to represent any arbitrary interaction function, or is it limited to a specific class of interaction functions? The lack of a formal definition makes it difficult to assess the scope and limitations of the proposed model. The connection to universal approximation theorems should be made explicit with a clear statement of what function space is being approximated.

- Interaction sensitivity is defined to measure the sensitivity of model outputs to perturbations in input node features. However,  perturbations in input node features are not the same as interactions between node pairs - so how are they related? Also, why is  interaction expressiveness considered as one aspect of interaction efficiency? The relationship between input feature perturbations and node pair interactions is not clearly established. The paper needs to provide a more detailed explanation of how changes in input features translate to changes in the learned interactions between nodes. Furthermore, the justification for considering interaction expressiveness as a component of interaction efficiency is not sufficiently explained. Why is the ability to express diverse interactions directly linked to efficiency, and what are the trade-offs involved?

(W2) The formulation and notations are not well presented.

- Figure 1: What does "a variable capable of taking K values (K=4 there)" mean? How do you decide such a K value? The meaning of 'K' in Figure 1 is ambiguous. It is unclear how this variable with K values relates to the interaction states between node pairs. A more precise explanation of how K is chosen and what it represents in terms of the interaction space is needed. The example given is not sufficient to understand the general case.

- What does the notation $S_{i,j,:}$ refer to? What is $\mathbb{R}^*$? The notation $S_{i,j,:}$ is not properly introduced, and the meaning of the colon is unclear. The use of $\mathbb{R}^*$ is also vague and needs to be defined precisely. Does it refer to a space of variable dimension, and if so, how is this dimension determined? The lack of clarity in these notations makes it difficult to follow the mathematical formulations.

- Equation 6 is not well defined. What do local structures mean precisely? Also the domain of $\varphi^{LE}$ is vague - this needs to be formulated and clearly defined. The definition of 'local structures' in Equation 6 is too vague. What specific graph properties are considered local, and how are they encoded? The domain of $\varphi^{LE}$ also needs to be explicitly defined. What kind of inputs does it take, and what is the nature of the output space? Without these definitions, the equation is not well-defined.

- For the statement "the discrimination ability of non-symmetry pairs of $\varphi^{LE}$ is a partial order with the injectivity to be the most discriminative one", it needs a clarification. The statement about the discrimination ability of $\varphi^{LE}$ being a partial order is not clear. What does it mean for one implementation to be more discriminative than another, and how is this partial order defined? The connection to injectivity needs to be explained in more detail.

- What is the definition of $S/\sim$? Since $S\subseteq \mathbb{R}^{n\times n}$, why is $S/\sim=\mathbb{R}^{\eta}$? The definition of $S/\sim$ is not clear. Given that $S$ is a matrix, how does the equivalence relation $\sim$ lead to a space of dimension $\eta$? The paper needs to provide a precise definition of the equivalence relation and explain how it induces a partition of the interaction space.

- In Proposition 1, is $f_{\mathcal{W}b}$ a typo? What is $\mathbf{x}_a$? The notation $f_{\mathcal{W}b}$ in Proposition 1 is unclear and may be a typo. The meaning of $\mathbf{x}_a$ is also not defined. These notations need to be clarified for the proposition to be understandable.

(W3) Some explanations are needed to improve the clarity of the paper.

- The paper mainly focuses on graph convolution networks as stated in Equation 1. But this is not clarified in the abstract and introduction which seem to consider graph neural networks in general. The abstract and introduction should clearly state that the focus is on graph convolutional networks (GCNs) rather than general graph neural networks (GNNs). This distinction is crucial because the proposed method and analysis are specific to the GCN framework. The current lack of clarity may mislead readers into thinking the results apply to all GNNs.

- It is unclear how the issues under-reaching and over-squashing mentioned in the abstract and introduction can be addressed by the proposed UIGC layer defined in Equation 7. The paper mentions under-reaching and over-squashing but does not explain how UIGC addresses these issues. The connection between the proposed UIGC layer and these problems is not clear. A more detailed explanation is needed to show how UIGC mitigates these problems.

- For the statement "UIGC infers the interaction of each pair directly through their local encodings, which will not be affected by the connectivity of graphs", I don't understand this. Why is it not affected by the connectivity of graphs? The claim that UIGC's interaction inference is not affected by graph connectivity is counterintuitive. The paper needs to explain why the local encodings are independent of the graph structure, given that GNNs are designed to leverage connectivity information. This statement needs further justification and clarification.

(W4) The setup of experiments may cause some confusions. For example,

- How many graphs are randomly selected for the experiments on learning interactions on synthetic data, only one graph? How many graphs are considered in the result presented in Table 1? The experimental setup for the synthetic data is not clear. How many graphs are used, and are the results consistent across different graphs? The paper should provide details on the number of graphs used and the variability of the results.

- For the experimental results on the five distinct interaction patterns shown in Figure 3, what are these interaction patterns? The current description in Section 5.1 is vague. Also, why are such interaction patterns selected? The description of the five interaction patterns in Section 5.1 is too vague. What are the specific functions or rules that define these patterns? The paper should provide a clear mathematical definition of each pattern. Furthermore, the rationale behind selecting these specific patterns needs to be explained. Why are these patterns representative of the types of interactions the model is designed to handle?

- The paper claims that the proposed UIGC can address the issues such as under-reaching and over-squashing of existing works. But there is no experiment provided to compare with existing works on how the proposed UIGC performs for solving such issues. The paper claims that UIGC addresses under-reaching and over-squashing, but there is no experimental validation of this claim. The paper should include experiments that compare UIGC with existing methods on tasks where these issues are known to be problematic.

- How is K selected? Why are only K=3 and K=8 considered? The choice of K values in the experiments is not justified. Why are only K=3 and K=8 considered, and how do these values relate to the complexity of the interaction patterns being modeled? The paper should provide a rationale for the selection of these specific K values and discuss the potential impact of different values on the results.

### Questions
See the questions in W1-W4.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
