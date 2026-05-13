# How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
While large language models based on the transformer architecture have demonstrated remarkable in-context learning (ICL) capabilities, understandings of such capabilities are still in an early stage, where existing theory and mechanistic understanding focus mostly on simple scenarios such as learning simple function classes. This paper takes initial steps on understanding ICL in more complex scenarios, by studying learning with \emph{representations}. Concretely, we construct synthetic in-context learning problems with a compositional structure, where the label depends on the input through a possibly complex but \emph{fixed} representation function, composed with a linear function that \emph{differs} in each instance. By construction, the optimal ICL algorithm first transforms the inputs by the representation function, and then performs linear ICL on top of the transformed dataset. We show theoretically the existence of transformers that approximately implement such algorithms with mild depth and size.  Empirically, we find trained transformers consistently achieve near-optimal ICL performance in this setting, and exhibit the desired dissection where lower layers transforms the dataset and upper layers perform linear ICL. Through extensive probing and a new pasting experiment, we further reveal several mechanisms within the trained transformers, such as concrete copying behaviors on both the inputs and the representations, linear ICL capability of the upper layers alone, and a post-ICL representation selection mechanism in a harder mixture setting. These observed mechanisms align well with our theory and may shed light on how transformers perform ICL in more realistic scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on understanding the internal mechanism by which a Transformer model solves an in-context learning task where the label $y$ for an instance $x$ linearly depends on a representation $\phi^{\star}(x)$.  A recent line of work has focused on explicitly constructing transformer models that can simulate various learning methods (e.g., gradient descent) on a training objective defined by the in-context labeled examples during a forward pass of the Transformer model. This paper extends this line of work by considering a more general data model where the final label depends on the input instance through a linear function of a representation. The paper provides explicit constructions for Transformer networks that can simulate ridge regression for 1) supervised learning with a representation, and 2) learning dynamical systems with a representation. The explicit constructions first aim to employ the underlying representation map $\phi^{\star}$ in the lower layers of the Transformer and then implement gradient descent in the upper layers of the Transformer.

Through experiments on synthetic datasets, the paper demonstrates that the performance of in-context learning via Transformers closely agrees with the performance of an optimal ridge predictor. Through probing analysis of the Transformer models, the authors show evidence that supports representation mapping following by label prediction aspects of their constructions.

### Strengths
1) The paper successfully extends the recent line of work on showing the feasibility of in-context learning via empirical risk minimization during a forward pass by considering data models where labels depend on the input feature via a representation map.
2) The paper is well-written and explains the key contributions and techniques clearly.
3) The empirical results (on synthetic datasets) do indicate the feasibility/presence of the explicit in-context learning mechanism hypothesized in the paper.

### Weaknesses
1) Novelty of the technical contributions is limited given prior works of similar flavor that provide the feasibility of empirical risk minimization during forward pass. One of the aspects which authors claim to be novel is that they allow for representation-based learning. However, the underlying assumption is that the representation map is a multi-layer MLP model, which Transformers should be easily able to simulate through its MLP layers. In that sense, the results in not very surprising. The paper does not sufficiently address the question of why explicitly constructing a representation mapping followed by gradient descent is more significant than simply relying on the universal approximation capabilities of transformers. The specific architecture choices and the way they are implemented within the transformer are not thoroughly justified in terms of their necessity or advantage over other possible approaches. The paper would benefit from a more detailed discussion on the limitations of relying on a multi-layer perceptron for the representation map, especially given the known ability of transformers to approximate complex functions.

2) The probing analysis is done only on a synthetic setup. It would be nice to get some supporting evidence for the proposed in-context learning mechanism on a real dataset. The current analysis lacks the complexity and variability of real-world data, which makes it difficult to assess the generalizability of the proposed mechanisms. The paper should include experiments on more complex datasets or provide a more detailed discussion on how the findings on synthetic data can be extrapolated to real-world scenarios. The probing analysis, while insightful, is limited by the controlled nature of the synthetic data, and it would be beneficial to see if similar patterns emerge in more realistic settings.

Minor issues:

1) The authors may want to formally introduce/discuss the pre-training phase (e.g., Eq (10)) which learns the representation map early in the section on preliminaries. 

2) In the paragraph on **In-context learning** in Section 2, $\mathcal{D}^{(j)}$ and $\mathbf{w}_{\star}^{(j)}$ are not defined before their usage.

### Questions
1) In general, the transformers are known to be universal approximators. In light of these, could authors comment on the significance of the key contributions of the paper, i.e., learning a representation map before applying gradient-descent in the representation space?

2) Could the authors elaborate on using a **linear model** for their investigation on the upper module via pasting (Figure 4)?

3) Currently the non-linearity in the true representation map is closely tied to the nonlinearity used in the Transformer network. Could the authors comment on generalizing this to broader nonlinearities in the true representation map? How would it increase the required number of layers?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Results illustrating the performance of transformers in ICL tasks that necessitate some degree of representation learning are presented. The theory can be partially validated through probing experiments.

### Strengths
Clear and well-written. 

This paper is one of the pioneering efforts to formalize how transformers execute ICL tasks that necessitate a degree of representation learning.

### Weaknesses
The theory only encompasses representational results by providing some settings of the parameters in a way that a transformer performs an ICL task. Given the transformer's highly expressive capability, these types of constructions are generally relatively straightforward.

There's no assurance that these theoretical constructs are truly internalized by the model during the training process. Although probing experiments gave us some confidence that, in specific instances, the theory can predict the model's behavior, these types of experiments generally don't offer robust guarantees. As a result, while the theory is logical and sometimes mirrors empirical events, it could be counterproductive to lean too heavily on these theoretical constructs. It might be necessary to carry out an analysis of training dynamics in order to theoretically determine under which conditions the model actually aligns with the theoretical constructs.

### Questions
The reviewer is open to learning about new evidences or analyses which address the points of the “Weaknesses” section above in this review.

### Soundness
2 fair

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
The goal of this paper is to theoretically and empirically understand the mechanism of in-context learning with underlying representations. Specifically, the setting considered is where there is a fixed representation function, chosen to be an MLP, and the ICL problem is to learn ridge regression on these representations. The transformer must learn this fixed representation function during pretraining and a regression hypothesis in-context. The authors theoretically show that it is possible to construct transformers that can perform ridge regression in supervised and linear dynamical system settings on fixed representations. Empirically, the paper verifies that transformers can learn to perform this type of ICL by probing for the emergence of mechanisms and values that should emerge according to theoretical construction.

### Strengths
- The paper well-written.
- The experiments do a good job at validating the claims by probing for the relevant information.
- The results offer valuable insights into how in-context learning, which is very relevant and timely.

### Weaknesses
 - Labels in figures and the figure captions can be more clear. For example, items like "TF_upper+1_layer_TF_embed" in Figure 4b are not very readable.
- Section 3 could be significantly condensed by considering theorem 2 as a generalization of theorem 1 instead of presenting them separately.
- Section 3.1 states that the representation function can be chosen arbitrarily, but Lemma B.3 requires a specific structure and non-linearity to work.
- Although the paper does a good job of illustrating the claimed mechanism, it does not analyze settings where the mechanism breaks. Specifically, the paper does not explore the robustness of the learned representation when the pretraining data contains spurious correlations, such as non-diagonal covariance structures in the Gaussian priors for x and z. This could lead to the transformer learning a representation that is not the true underlying function, and thus performing suboptimally when the test data is sampled from a different distribution. Furthermore, the paper does not address the compositional generalization capabilities of the learned representation function or the regression mechanism.

### Questions
- What happens when the representation function is of a different form? If either the transformer does not have enough layers or the width, is there an approximate representation function learned on which regression is performed, or does the entire mechanism fall apart?
- How robust is learning of the representation function in settings where the pretraining data contains spurious correlations? Can we say anything about the transformer's ability to compositionally generalize with either the representation function, regression, or both?
- What is OLS in Fig 1b?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This works studies in-context learning in transformers using synthetic data. It extends previous work, by studying composition of a *fixed* non-linear function (L-layer MLP) with a linear function that is learned in-context. This work provides a construction of a transformer that can solve this task, but also demonstrates it empirically on synthetic data. Additionally, the authors provide a mechanistic understanding of the algorithm implemented by a trained transformer.

### Strengths
The results extend the the setup of Garg et al. to study in-context learning with more complex function classes. In particular, transformers can learn a composition of a *fixed* non-linear function with a linear function learnt from context. The authors in Figure 1 provide evidence that a transformer matches the optimal predictor.

The mechanistic analysis is thorough, and provides compelling evidence for the underlying 3-step mechanism. It is surprising that the mechanism is consistent across multiple training runs and adds to the results of the paper. 

The results also hold when multiple different non-linear representations are used which further strengthens the main claims of the paper. I would have liked to see the results of 4.1.1 more prominently in the main paper, but I understand the authors are constrained by space. 

Overall, I think the results would be of interest to the community and the toy setup may be more representative of in-context learning in language models.

### Weaknesses
 **Why are the constructive proofs important for understanding in-context learning in transformers?**
I am aware that there are prior works that design transformers that are capable of in-context learning. However, I am not convinced of the importance and significance of these results. Couldn't we also find weights for other architectures (like large MLPs or LSTMs) and argue that they are capable of in-context learning. Is the existence of these model weights informative of what is learnt in practice?

**Choice of non-linear functions.**  I think the authors could be more rigorous in evaluating the non-linear representations used in their setup. In particular, the non-linear representations are L-layer MLPs with the matrices being random orthogonal matrices. Do the results hold for other families of functions and does it fail to work for some other classes of functions? I think it would be helpful to clarify that the results are specific to this setup.

**Is the synthetic setup an accurate toy-model to understand language models?** Like previous work, all the results are on synthetic data. It remains unclear if the toy setup is representative of in-context learning in language models. What kind real world tasks are captured by a composition of a fixed non-linear function and a linear function that is learnt from context?

### Questions
1. Could the authors add more details on how the non-linear functions are created? Can the authors also clarify in the introduction/abstract that the functions are L-layer MLPs?

2. Is it possible to show some of these results on other families of non-linear functions? For example, what happens if the functions are polynomials or exponential functions of the input? Are there scenarios where it fails empirically?

3. What happens if we increase the number of layers used to create the representation from 5 to 15. Does the model start to fail if L=15 (even if transformer has only 11) layers or does it find a good approximation to the non-linear function using just 4-5 layers?

4. Results in appendix E were very interesting! As future work, it would be great to investigate how many different non-linear functions can be learnt. I would also be interested in understanding if in-context learning becomes difficult and if the model sometimes struggles to identify the right non-linear representation.

5. Ruiqi et al. (https://arxiv.org/abs/2306.09927) show that in-context learning fails if the linear functions are selected to be out-of-distribution. Is this also the case here?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
