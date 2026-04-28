# Unleashing the Information Flow: Graph Neural Networks are Noisy Communication Channels

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 5, 1, 3

## Abstract
Existing message-passing graph neural networks often rely on carefully designed information propagation methods to perform reasonably in graph-related mining tasks. However, this invokes the problem of whether the dimensions of learnable matrices and the depths of the networks are properly estimated. While this challenge has been attempted by others, it remains an open problem. Using the principle of maximum entropy and Shannon's theorem, we demonstrate that message-passing graph neural networks function similarly to noisy communication channels. The optimal information transmission state of graph neural networks can be reached when Shannon's theorem is satisfied, which is determined by their entropy and channel capacity. In addition, we illustrate that the widths of trainable matrices should be sufficiently large to avoid the shrinkage of model channel capacity and the increase of the channel capacity diminishes as the depth of the networks increases. The proposed approach is empirically verified through extensive experiments on five public semi-supervised node classification datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors argue that graph neural networks behave similarly to noisy communication channels. Based on information theory, they derive a nonlinear programming that maximizes the entropy of a GNN, thereby finding its optimal transmission state. By solving this optimization problem, they aim to find optimal network architecture parameters, i.e. the number of layers (network depth) and the size of the weight matrices for each layer (network width). In semi-supervised node classification experiments, they compare the optimized network architectures of some well-known GNNs to commonly used architecture configurations.

### Strengths
1) The authors have a good motivation for their work, which is solving the problem of finding optimal network widths and depths.
2) The necessary theoretical background to understand their approach (e.g. information theory, entropy, communication channels) is well explained.

### Weaknesses
Major (Content):

1) The assumption that Cl = A (see line 152) is valid for GCN only. The proposed framework is based on this assumption. However, the authors use their framework also for GAT and GDC (see Sec. 7 “Experiments”). This is a critical flaw, as the propagation mechanisms of GAT and GDC are fundamentally different from GCN and cannot be represented by a simple adjacency matrix. Specifically, GAT uses attention mechanisms to weight the aggregation of neighbor features, while GDC employs a diffusion process, neither of which are captured by the assumption Cl = A. Applying the framework to these models without addressing this discrepancy undermines the validity of the experimental results.

2) The proposed optimization problem seems to lead to a very large network width (> 1000, see App. E). This leads to a significantly larger number of parameters for the C3E-models compared to the “Plain-“ and “Deep-“ models, which have network widths of at most 64. In fact, the total number of trainable parameters for the C3E-models is larger than 1.000.000 compared to ~20.000 for the baselines, which seems to be an unfair comparison. The authors do not adequately address the computational implications of these large networks, nor do they provide a justification for why such a large increase in parameters is necessary or beneficial, especially given that the baseline models are already performing reasonably well.

3) The optimization problem in Eq. 18 does not consider computational efficiency. At some point, increasing network width and depth may not be computationally feasible anymore or the resulting performance improvement may not be worth the computational expense. The authors should incorporate a constraint that limits the number of parameters or computational cost, to make the approach more practical. Without this, the method may be limited to small datasets or require excessive resources, thus reducing its practical applicability.

Major (Formal):

a) Fig. 1-4: The subfigures are way too small and it is hard to read the axis labeling. Maybe it would be better to show these results only for one or two of the datasets and shift the other results to the Appendix.

Minor:

  1) Although the introduction contains a good motivation (how to balance receptive field and over-smoothing by finding optimal GNN width and depth), the introduction lacks information on the proposed approach. There is only one sentence from line 69-71, in which the authors mention (very briefly) what they are doing in the paper. 

2) The section “other related work” lacks some clear differentiation of the author’s work from the literature.

3) Eq. 1: Integral domain is missing.

4) Eq. 4: Please use a different index in the sums in denominator to distinguish it from the index of the outer sum.

5) Sec. 4 introduces some more information theory basics in the second paragraph. This could be shifted into Sec. 3. 

6) Eq. 19 is identical to Eq. 9 and 10. It is reader-friendly to recall these equations, but using different numbers might be confusing

### Questions
1)  Eq. 8: I do not quite understand, why the activation function was removed, which is the only difference between Eq. 8 and Eq. 7. It may not affect the maximum entropy, as the authors argue, but this is not a sufficient reason to just delete it from Eq. 7. Could you please explain this in more detail?

2)  Eq. 11: As far as I understood, Eq. 10 is used for the approximation in Eq. 11. However, I do not understand, where the second term in the second line of Eq. 11 comes from.

3)  Eq. 18: What do you mean by L=2 below the sum?

4) How do we know that there is always a solution to the optimization problem in Eq. 18?

5) The main idea of the paper is to find a GNN’s optimal transmission state by maximizing its entropy, which is defined in Eq. 11. However, in the Discussion the authors state that “… reaching the optimal information transmission state does not necessarily guarantee improvements in model performance.” This leads to the question of why the proposed optimization is necessary at all. Could you please explain what you meant by that in more detail?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
Message-passing graph neural networks are shown to function like noisy communication channels, with optimal performance achieved when Shannon's theorem balances entropy and channel capacity. The study highlights that trainable matrix widths must be large enough to maintain channel capacity, which diminishes with increasing network depth, and validates these findings through experiments on five node classification datasets.

### Strengths
I am not an expert in this field and struggled to fully understand the derivations of the theorems, so I am unable to thoroughly evaluate the strengths and weaknesses of this paper. I apologize and will defer to the insights provided by other reviewers.

### Weaknesses
The author say "This work illustrates that the expressive ability of GNNs
depends on their model capacity, which is directly determined by the widths and depths of the networks." in the introduction, but in the end they never discuss the expressive power of GNNs by the formulation provided here. They also consider rather simple GNNs whose expressiveness is already well established [1,2].

 Poor discussion of related works: while the authors discuss some relevant works like Di Giovanni et al., they do not clearly explain what is the difference between the papers and what is the main benefit of looking at the problem from the proposed perspective.

 Missing discussion of related works: for example [3] also studied the outputs of GNNs and shows similar conclusions, and the well studied phenomenon in GNNs of oversmoothing was shown to yield similar results [4,5]. I thus tend to feel that significant works in the field have been overlooking and there is lack of novelty in this paper, despite its soundness.

 Not all GNNs can be explain by Equation (7). I think that this is a limitation of the method and misses on well known and important architectures like [1,2].

 There are several typos and required improvements to the level of English, for example "Let's" -> "Let us". Another example is a missing word in line 359-360 "Unlike the graph attention mechanism
adaptively weighs the given edges..."

 The derivation in Equation (8) leads to oversmoothing and convergence to the leading eigenvector of the adjacency matrix, which is already a known result in GNNs.  Similar argument holds for lines 200-203. While the discussion is correct, it is not new.

 The experiments are not convincing. According to the authors, they used the public split on Cora/Citesser/Pubmed. However, it is known that GCN obtains better results than reported here. See for example the results reported in [6]. Also, these datasets were shown to suffer from several issues to properly evaluate GNNs, please see [7].

 It is not clear how much time it takes to solve the programming problem? Is it practical for large scale networks?

 Why not show results on additional backbones like GCNII/GIN or even graph transformers like GPS?

 With respect to my previous question, I think that the plots the authors show in Figure 1 are not a general result, because if they use GCNII which does not over smooth, the accuracy will not drop, and it might be that the entropy also doesnt increase as suggested. I would expect a more rigouruous study.

 The authors should show results on additional datasets and benchmarks, such as LRGB, OGB, TUDatasets and others to provide a more compelling paper. As it is now, the results are not convincing and the theoretical derivations while correct, do not offer a new perspective on what we already know.

 File issue: It seems that the figures used in the paper make the rendering of the paper problematic. I suggest that the authors revise them with lighter files.

### Questions
I am not an expert in this field and struggled to fully understand the derivations of the theorems, so I am unable to thoroughly evaluate the strengths and weaknesses of this paper. I apologize and will defer to the insights provided by other reviewers.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper proposes a take on GNNs by considering the enropy of the node features as a function of depth and width of the network. 
The authors present several theorems that characterize the behavior of GNNs when they depth or width increases, and based on that they propose a method called C3E to constrain this entropy.

Experiments and evaluations are provided on a few datasets.

### Strengths
The idea and analysis present here are sounds.

### Weaknesses
The main weakness I find for this paper is that the posed problem of choosing widths and depth of GNNs has been not addressed well, both theoretically and empirically. Detailed points are as follows.
- W1. The paper makes a key assumption in Line 159-160 and 173-174 that maximum entropy corresponds to optimal information transmission in GNNs, and I am not sure why or how this assumption can be considered valid (I might be missing something since I am unfamiliar with information theory). This assumption underlies most of the claims of this paper (Theorem 1, especially Line 183-184) and its validity is important.
- W2. I do not see how the results shown in Eq. (16) leads to the conclusion in Line 259-260 that "its negative effects always surpass its merits (typically reflected as model performance degradation). The equation says that adding depth leads to diminishing, but non-negative returns, as the summands are positive for any $w_{l-1}, w_l \geq 2$. This in fact means adding depth should be always beneficial (at least not detrimental).
- W3. The nonlinear programming problem in Eq. (18) which underlies the main algorithm seems to have two issues. First, it does not optimize the depth $L$ of GNNs as far as I understood, and hence does not solve the considered problem of choosing both widths and depth. Second, the termination condition is given by an offset of the constraint parameterized by a new constant $\zeta$, and what this termination condition means in the information-theoretic framework of this paper and how $\zeta$ is chosen is unclear.
- W4. Overall, I am not sure how to interpret the experimental results. For example, in Section 7.2, it is stated that "unlike real communication channels, GNNs might suffer from severe over-fitting due to extra available channel capacity" (Line 355-356), which seems to contradict the theoretical interpretation of GNNs given in this paper based on maximal entropy, as well as the usefulness of the main algorithm. In Section 7.3 the authors state that "C3E variants experience a considerable entropy increase at the first layer... Yet, these characteristics do not necessarily guarantee better performance in the downstream tasks", which raises a similar concern. Given this, I am not sure how the conclusion "GNNs perform similarly to noisy communication channels" in Line 469 can be made. Other detailed points are given in W5-8.
- W5. In Line 347, the authors argue on Figure 1 that "the accuracy curves exhibit continuous U-shaped and V-shaped patterns over the figures", and connect this to scaling laws of language models. I was unable to find the argued patterns in Figure 1, and in fact, it seems that in many cases the accuracy degrades with increased model capacity (e.g., GAT in AmazonComputers).
- W6. In Line 350, the authors say that "C3E variants reach their peak performance within [ϕ0 − log n, ϕ0 − 2log n]". I am not sure what this interval means, because the x-axis of the plots corresponds the control variable ϕ0 − log n.
- W7. In Line 372-374, The authors state that "The massive entropy reduction occurs relatively early in most Deep models, implying diverse features are collapsed into centralized or biased features." The logic behind this argument is unclear. For example, a plausible alternative explanation is that classification quickly finishes in early layers.
- W8. In Section 7.4, I was not sure what specific theoretical results the authors were trying to verify (Line 421) by measuring mean and variance of hidden features. The authors provide Eq. (19) which assumes that all weights and input features come from the standard normal distribution (Theorem 1), and then argue that GNNs with non-zero mean features have learned "biases" in the features (Line 453) by comparing the empirical mean to Eq. (19). A simpler and more plausible explanation could be that these learned GNNs deviate substantially from the assumptions of Theorem 1.
- W9. In Line 482-483, the authors claim that "in an attempt to avoid biased results, other GNNs that do not take the form of Eq. (7) and other aggregation methods are not included." It was unclear to me what kind of biased results the authors were trying to avoid with limited evaluation of model classes. I have a similar concern for Line 1113-1114, where the authors state "For a fair comparison, only deep backbone models and C3E variants have residual connections in the form of Eq. (41)." and it is unclear how this ensures a fair comparison of which models.

### Questions
What do you mean by 'graph mining' in the introduction and abstract of the paper?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper concerns with the problem of choosing the widths and depth of message-passing GNNs for semi-supervised learning. A summary is as follows:
- In Section 4, assuming implicitly that maximum entropy state corresponds to the optimal information transmission rate in GNNs (Line 159-160 and 173-174), the authors propose to analyze GNNs using the maximum entropy of hidden features and argue to choose the widths and depth to maximize entropy (Theorem 1, especially Line 183-184).
- While entropy maximization can be done by arbitrarily scaling width and depth of GNNs, in Section 5, the authors provide a rationale for regularizing depth based on a lower-bound of channel capacity (Eq. (16)), which states that increasing model depth leads to a diminishing return in increasing the lower bound.
- Based on arguments in Section 4-5, in Section 6 the authors provide an algorithm for prescribing width and depth of GNNs that maximize entropy under the lower-bound constraint on channel capacity, and an additional constraint that dimensions over depth are non-increasing.
- In Section 7, the authors experiment the algorithm compared to fixed shallow and deep architectures for representative GNNs for 5 semi-supervised learning datasets, measuring model accuracy and entropy, mean, and variance of hidden features.

### Strengths
- S1. This paper aims at an important problem of prescribing the model capacity of GNNs before learning.
- S2. The approach from the perspective of information theory taken in this paper is original as far as I am aware.
- S3. The writing is fluent and I was easily able to follow the flow of the paper.

### Weaknesses
The main weakness I find for this paper is that the posed problem of choosing widths and depth of GNNs has been not addressed well, both theoretically and empirically. Detailed points are as follows.
- W1. The paper makes a key assumption in Line 159-160 and 173-174 that maximum entropy corresponds to optimal information transmission in GNNs, and I am not sure why or how this assumption can be considered valid (I might be missing something since I am unfamiliar with information theory). This assumption underlies most of the claims of this paper (Theorem 1, especially Line 183-184) and its validity is important.
- W2. I do not see how the results shown in Eq. (16) leads to the conclusion in Line 259-260 that "its negative effects always surpass its merits (typically reflected as model performance degradation). The equation says that adding depth leads to diminishing, but non-negative returns, as the summands are positive for any $w_{l-1}, w_l \geq 2$. This in fact means adding depth should be always beneficial (at least not detrimental).
- W3. The nonlinear programming problem in Eq. (18) which underlies the main algorithm seems to have two issues. First, it does not optimize the depth $L$ of GNNs as far as I understood, and hence does not solve the considered problem of choosing both widths and depth. Second, the termination condition is given by an offset of the constraint parameterized by a new constant $\zeta$, and what this termination condition means in the information-theoretic framework of this paper and how $\zeta$ is chosen is unclear. 
- W4. Overall, I am not sure how to interpret the experimental results. For example, in Section 7.2, it is stated that "unlike real communication channels, GNNs might suffer from severe over-fitting due to extra available channel capacity" (Line 355-356), which seems to contradict the theoretical interpretation of GNNs given in this paper based on maximal entropy, as well as the usefulness of the main algorithm. In Section 7.3 the authors state that "C3E variants experience a considerable entropy increase at the first layer... Yet, these characteristics do not necessarily guarantee better performance in the downstream tasks", which raises a similar concern. Given this, I am not sure how the conclusion "GNNs perform similarly to noisy communication channels" in Line 469 can be made. Other detailed points are given in W5-8.
- W5. In Line 347, the authors argue on Figure 1 that "the accuracy curves exhibit continuous U-shaped and V-shaped patterns over the figures", and connect this to scaling laws of language models. I was unable to find the argued patterns in Figure 1, and in fact, it seems that in many cases the accuracy degrades with increased model capacity (e.g., GAT in AmazonComputers).
- W6. In Line 350, the authors say that "C3E variants reach their peak performance within [ϕ0 − log n, ϕ0 − 2log n]". I am not sure what this interval means, because the x-axis of the plots corresponds the control variable ϕ0 − log n.
- W7. In Line 372-374, The authors state that "The massive entropy reduction occurs relatively early in most Deep models, implying diverse features are collapsed into centralized or biased features." The logic behind this argument is unclear. For example, a plausible alternative explanation is that classification quickly finishes in early layers.
- W8. In Section 7.4, I was not sure what specific theoretical results the authors were trying to verify (Line 421) by measuring mean and variance of hidden features. The authors provide Eq. (19) which assumes that all weights and input features come from the standard normal distribution (Theorem 1), and then argue that GNNs with non-zero mean features have learned "biases" in the features (Line 453) by comparing the empirical mean to Eq. (19). A simpler and more plausible explanation could be that these learned GNNs deviate substantially from the assumptions of Theorem 1.
- W9. In Line 482-483, the authors claim that "in an attempt to avoid biased results, other GNNs that do not take the form of Eq. (7) and other aggregation methods are not included." It was unclear to me what kind of biased results the authors were trying to avoid with limited evaluation of model classes. I have a similar concern for Line 1113-1114, where the authors state "For a fair comparison, only deep backbone models and C3E variants have residual connections in the form of Eq. (41)." and it is unclear how this ensures a fair comparison of which models.

### Questions
- Q1. In Appendix E.4, how are the hyperparameter configurations for the plain and deep models chosen for each dataset?

### Soundness
2

### Presentation
2

### Contribution
2
