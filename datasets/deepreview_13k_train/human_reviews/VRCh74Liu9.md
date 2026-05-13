# Federated Generalization via Information-Theoretic Distribution Diversification

- Decision: Reject
- Scores: 5, 6, 3, 3

## Abstract
Federated Learning (FL) has surged in prominence due to its capability of collaborative model training without direct data sharing. However, the vast disparity in local data distributions among clients, often termed the non-Independent Identically Distributed (non-IID) challenge, poses a significant hurdle to FL's generalization efficacy. The scenario becomes even more complex when not all clients participate in the training process, a common occurrence due to unstable network connections or limited computational capacities. This can greatly complicate the assessment of the trained models' generalization abilities. While a plethora of recent studies has centered on the generalization gap pertaining to unseen data from participating clients with diverse distributions, the divergence between the training distributions of participating clients and the testing distributions of non-participating ones has been largely overlooked.
In response, our paper unveils an information-theoretic generalization framework for FL. Specifically, it quantifies generalization errors by evaluating the information entropy of local distributions and discerning discrepancies across these distributions. Inspired by our deduced generalization bounds, we introduce a weighted aggregation approach and a duo of client selection strategies. These innovations aim to bolster FL's generalization prowess by encompassing a more varied set of client data distributions. Our extensive empirical evaluations reaffirm the potency of our proposed methods, aligning seamlessly with our theoretical construct.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considered the problem of generalization performance in federated learning (FL) with non-i.i.d. data and partial client participation. The authors proposed an information-theoretic framework for FL that quantifies the generalization error by evaluating the information entropy of local distributions and discerning discrepancies across these distributions. Based on their derived generalization error bounds, the authors proposed a weighted aggregation approach and two client selection strategies. The authors also conducted numerical experiments to verify their proposed methods.

### Strengths
1. The authors focused on the divergence between the training distributions of participating clients and the testing distributions of the non-participating clients, which is less studied in the literature. 

2. This paper has good theoretical depth and provides interesting insights with information-theoretic generalization error bounds.

### Weaknesses
1. The tightness of the information-theoretic generalization error bound is unknown. Thus, the weighted aggregation and client selection strategies based on the generalization error bound are unclear. Also, several notions in the derived information-theoretic generalization error bound are unclear. Specifically, the practical implications of using self-information weighted expected risk, as opposed to standard empirical risk, are not well-defined. The bound relies on the optimal model parameter \(\hat{h}^*\), which is generally unattainable in practice due to the non-convex nature of the problem. Furthermore, the connection between the derived information-theoretic quantities and concrete optimization procedures is not sufficiently established, making it difficult to assess the practical relevance of the proposed bounds.

2. The numerical experimentations may be inadequate. The experiments are limited to relatively simple datasets and models, which might not fully capture the complexities of real-world federated learning scenarios. The lack of experiments with more challenging datasets, such as those with higher dimensionality or more complex data distributions, and more sophisticated models, such as larger transformer networks, raises concerns about the generalizability of the empirical findings.

### Questions
1. It's unclear how tight the proposed joint self-information generalization error bounds in Theorems 1 and 2 are. Also, it is known in the literature that the VC-dimension-based generalization error bound, which is also used in Theorems 1 and 2, could be loose. Could the authors provide corresponding lower bounds for the proposed joint self-information-based generalization error bounds to show the tightness of the upper bounds? This paper could benefit tremendously from such insights and provide theoretical guarantees for the subsequent aggregation weighting and client selection strategies.

2. In Definition 3, the information theoretic-generalization gap is based on the $\hat{h}^*$, which is the optimal model parameter corresponding to the proposed self-information weighted expected risk. A similar notion of $\hat{h}_t^*$ is used for the selected participating clients in Theorem 2. However, in practice, such optimal model parameters are rarely found due to the non-convexity of the problem. Instead, the model parameters in use are highly dependent on the problem setting (e.g., non-convexity, smoothness, etc.) and the optimization methods (e.g., a large number of FedAvg-type variants) and the associated hyper-parameters (e.g., learning rates, batch sizes, etc.). Thus, the generalization error bounds derived in Theorems 1 and 2 based on the optimal parameters might not be very meaningful. Could the authors further characterize generalization error bounds for commonly used FL algorithms (e.g., FedAvg-type)?

3. The numerical experiments in this paper are largely based on CNN EMNIST-10 and CIFAR-10, which are considered relatively simple in the literature. Could the authors conduct more comprehensive experiments and evaluate their proposed weighted aggregation and client selection strategies with more challenging models (e.g., larger ResNet-type models) and datasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies generalization of Federated Learning in the non-IID setting. The main result is a generalization bound of a so-called 'self-information weighted expected risk', i.e., the expected risk weighted by the empirical entropy of data. Based on this result, the paper proposes an entropy-weighted aggregation method and client selection methods to improve FL training. On EMNIST-10,  Shakespeare, and CIFAR-10 datasets, the proposed methods are observed to improve Out-Of-Distribution generalization.

### Strengths
1. This paper defines a seemingly new objective called Information theoretic-generalization gap. This objective captures the uncertainty in data distributions and client dropout, which are absent in the classical notions of generalization error.

2. The theoretical framework appears to potentially have relevant, and positive impact to FL practice, as it leads to some new methods for gradient aggregation and client selection. It is good to see that the authors perform experiments on their algorithms and compare with baseline.

3. The paper is mostly clear and easy to read.

### Weaknesses
1. First of all, it is unclear what it the meaning of bounding the self-information weighted expected risk. In practice, we care about the accuracy over the generalization dataset, which is different from the information-weighted risk. Therefore, the fundamental question is: why bounding the information theoretic-generalization gap means good generalization accuracy? I didn't found in this paper an answer to this question or any solid explanations on this connection.

2. The upper bound in Theorem 1 lacks examples to explain each term in concrete cases. Given its current form, it is nearly impossible to compare with existing bounds and reasoning about tightness.

3. VC dimension is usually too large for modern neural networks to make it a useful complexity measure. Unfortunately, theorem 1 involves VC dimension.

4. The experiment section seems also quite limited in that only some simple and small-scale datasets are tested.

### Questions
1. What is the connection of information theoretic-generalization gap and generalization accuracy?

2. What are some examples to explain each term of the upper bound in Theorem 1, in concrete cases?

3. How to compare with existing bounds and reasoning about tightness on Theorem 1?

4. Speaking about OOD generalization, is there anywhere in the framework that captures the distribution shift? I thought something like mutual information should appear?

5. In Table 1, why is your methods' ID accuracy on CIFAR-10 worse than MaxSim, Power-of-Choice, and Full Sampling?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the out-of-distribution generalization challenge in federated learning through a client-sampling approach inspired by information theory. Specifically, the authors propose to minimize the “self-information weighted empirical risk” function whose generalization bound leads to two client sampling strategies. These strategies aim to maximize the cross entropy between a participating client and a new client, assuming that novel clients very different data distributions. Empirical results suggest that the proposed sampling method works better than a range of baselines.

### Strengths
The paper presents a nice and clear definition of the new risk functions (Definitions 1 and 2).
The information-theoretic generalization bounds (Theorems 1 and 2) are presented well and explained with useful remarks.
In particular, the authors show that, from the client participation perspective, the bounds can be minimized by careful client sampling and setting the right the participation weights \alpha_i.

### Weaknesses
 - There are a lot of unaccounted-for notations in this paper, beginning especially at Section 4. For example, the authors have not sufficiently explained what $F_i(.)$ and $w$ are in Assumption 3. Is $F_i(.)$ the usual empirical risk or information-theoretic version? Similarly, what is the local gradient $g_i^t$ with respect to?
- This notational ambiguity makes me unable to understand Algorithm 2 fully. At line 5, especially, what local loss function does client i try to minimize? It is unclear if this is the same loss function used to compute the gradients in the previous step, or if it is a different objective.
- In Section 4.2.2, again, I do not fully understand what the convex hull is with respect to. The description lacks details on how the gradients are represented as points in a space for the convex hull computation. Specifically, what is the dimensionality of the space, and how are the gradients mapped to coordinates in this space? It is also unclear how the quickhull algorithm is applied in this context.
- Empirically speaking, it is quite rare to update clients’ parameters through only one round of gradient descent as the authors propose in Algorithm 2, due to the cost of communication relative to local computation. This raises concerns about the practical applicability of the proposed method, as most real-world FL scenarios involve multiple local update steps.

### Questions
- The authors aim to optimize the participation-dependent term in the generalization bound. However, the relationship between this problem and the formulations in (11) and (12) and insufficiently clear. For example, what do the authors mean by the claim that cosine similarity is “suitable for FL”? Similarly, I do not see any proof for the equivalence of this optimization problem and that in (12).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the effect of partial client participation in the training phase on generalization performance. The paper considers the non-i.i.d. (or heterogeneous) case, where all distributions of clients are different from each other. Moreover, instead of the classical generalization error, a new notion of "information-theoretic generalization gap" is introduced and studied. Following the established theoretical results, the authors proposed several variations of model aggregation in FL and showed the advantage of their methods through numerical simulations.

### Strengths
The generalization error in federated learning, and in particular the effect of client participation, is poorly understood theoretically. This work is one of the first to address this issue. Moreover, the proposed variations of FL aggregation seem to have some potential, as verified by experiments.

### Weaknesses
The main weaknesses of the paper are as follows (please see Questions for details).

- The considered setup does not well capture the FL setup

- The paper studies a newly defined "information-theoretic-generalization gap".  However, the concrete justification for studying that term is missing.

- The proof techniques are simple and the resulted bounds “seem” to be loose.

- Some related works are missing, including https://arxiv.org/abs/2303.01215, https://arxiv.org/abs/2304.12216, https://arxiv.org/abs/2306.05862, https://arxiv.org/abs/2306.05862.

For these reasons, I am unfortunately inclined to reject the paper. I would be willing to raise the score if the comments below can be addressed.

### Questions
It would be appreciated if the authors could clarify the following points.

1. One of the main weaknesses of the paper is that only the discrete alphabet is considered, which is not a realistic case. This limitation is mentioned only once in the Preliminary Section. However, it must also be emphasized in the abstract and the introduction. How the results would change in case of continuous alphabets and why this assumption is made?

2. Another major limitation is that, similar to some previous works, this work assumes that the FL algorithms used by the participating clients manage to find the "global minimizer" of the self-information weighted semi-empirical risk. This consequently means that the FL algorithm (considered for the participating clients), is "equivalent" to a centralized algorithm that has all training data of all participating clients in one place. In a sense, the paper assumes that there is no such thing as "distributed learning". While much of the work in the literature shows the different behavior of these architectures. In other words, it seems that the paper is not really about the federated learning setup. But rather the "mismatch" between test and training data.

3. My main concern is that, unless I have missed something, it seems that all results are in terms of the "information-theoretic-generalization gap". However, except for some "intuitions", it has not been shown concretely what is the relation between such a definition and the true "generalization error". In other words, what are the concrete implications of these results for the true generalization error? If this relation cannot be established, I am not sure about the usefulness of the results.

4. Considering Theorem 1, this result is obtained by almost purely algebraic manipulations (e.g., proofs of Lemmas 1 and 2) and excessive use of the triangle inequality. Besides the simplicity of the techniques used (except perhaps the proof of Lemma 3, which is inspired by and similar to previous work), the bounds using such techniques are susceptible to being very loose. Similar comments apply to Theorem 2. Therefore, considering the terms appearing in the bound as optimization proxies does not seem very justified.

5. The authors mentioned that “Our hypothesis is grounded in the notion that a model exhibiting proficiency with low-probability examples from training distributions might demonstrate adaptability to unfamiliar testing distributions.” In a sense, intuitively, the goal here is to consider the "worst case" scenarios. However, it seems to me that the information-theoretic approach is not appropriate for this goal. In essence, information theory relies heavily on the probabilistic behavior of the learned model and data distribution, and the associated concentration of measures. Could the authors intuitively justify their information-theoretic approach and consider "self-information-weighted expected risk"?

6. I think there are some mistakes in the definition of "semi-empirical risk" of Hu et al., 2023, just before section 3.2. In fact, they never considered "self-information-weighted semi-empirical risk" and in that paper $\hat{h}^* = \text{arg inf } \mathcal{L}_{\mathcal{D}}$. Do authors change their definitions to conform to the new measure "information-theoretic-generalization gap"? If so, what is the relationship to what was originally defined there?

7.  Describing the first term in the RHS of equation (4) as overfitting could be misleading. In fact, if, for example, $\hat{h}^*$ is the minimizer of the self-information weighted expected risk for the set $\mathcal{I}$, this term can still be large. What exactly is the intuition behind this term?

8.  Remark 1 simply rewrites the RHS of equation (5). But could you please give some intuition about the behavior described and why it makes sense?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
