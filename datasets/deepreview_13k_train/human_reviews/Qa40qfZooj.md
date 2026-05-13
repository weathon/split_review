# Bayesian Neural Networks with Domain Knowledge Priors

- Decision: Reject
- Scores: 5, 5, 5, 6, 6

## Abstract
Bayesian neural networks (BNNs) have recently gained popularity due to their ability to quantify model uncertainty. However, specifying a prior for BNNs that captures relevant domain knowledge is often extremely challenging. In this work, we propose a framework for integrating general forms of domain knowledge (i.e., any knowledge that can be represented by a loss function) into a BNN prior through variational inference, while enabling computationally efficient posterior inference and sampling. 
Specifically, our approach results in a prior over neural network weights that assigns high probability mass to models that better align with our domain knowledge, leading to posterior samples that also exhibit this behavior.
We show that BNNs using our proposed domain knowledge priors outperform those with standard priors (e.g., isotropic Gaussian, Gaussian process), successfully incorporating diverse types of prior information such as fairness, physics rules, and healthcare knowledge and achieving better predictive performance. We also present techniques for transferring the learned priors across different model architectures, demonstrating their broad utility across various settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a approach for incorporating domain knowledge into priors for Bayesian neural networks (BNNs). 
The domain knowledge is represented as a loss function phi that measures how well a model aligns with the given knowledge. Using variational inference phi is used to reweight the prior distribution over neural network weights.

### Strengths
The manuscript tries to address the important topic of informative priors for efficiently modeling Bayesian inference to incorporate domain knowledge.

### Weaknesses
 - The theoretical justification for phi loss incorporating domain knowledge is not clear; this proposed formulation resembles an empirical Bayes setup where informative priors are learned from the data.
- There is a large body of work on informative priors that considers techniques such as empirical Bayes and hierarchical Bayes to incorporate domain knowledge.
- In the results section, it is unclear why the comparison of phi values against the selected datasets indicates the incorporation of domain knowledge.
- It is unclear how to interpret whether the model has successfully incorporated domain knowledge in a Bayesian setting without comparing standard uncertainty quantification metrics.
- While the method claims low complexity, it involves learning an informative prior through variational inference, which may add computational overhead compared to using standard uninformative priors. The paper does not discuss the computational costs, aside from a brief mention in the Appendix.
- The selected problems involve very small datasets (<50 samples) and toy problems, but practical examples with approximately 1,000 samples are needed to demonstrate effectiveness.

### Questions
Please see the above section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework for incorporating general form of domain knowledge into Bayesian neural network (BNN) through learned informative priors. These domain knowledge priors are specified via loss functions that measures the alignment of a particular model to the desired domain knowledge, and learned through variational inference. Empirical evaluation is performed using Stochastic Gradient Langevin Dynamics (SGLD) as the baseline with experiments on a 2-layer feedforward neural network, demonstrating the model with domain knowledge priors achieves better predictive performance than BNNs with commonly used priors (such as isotropic, Gaussian).

### Strengths
* The paper is well-motivated to specify informed priors in BNNs that reflects the relevant domain knowledge and mitigate undesirable biases.

* The proposed framework enables the integration of generic forms of domain knowledge such as physics rules, fairness, healthcare knowledge into BNN prior, and also proposes strategy to transfer the priors to other models without the need to relearn a new prior every time.

### Weaknesses
 * One of the main objective of Bayesian neural network (BNN) is uncertainty quantification (UQ) in their predictions. However, this paper does not address the ability of BNNs to reliably quantify model uncertainty in the study and experimental evaluation. The experiments conducted in the study are limited to evaluating predictive accuracy and domain knowledge surrogate loss, neglecting the critical UQ aspect of BNNs. This raises concerns about the evaluation of BNNs with the proposed informed prior, and the reliability of the model's uncertainty estimates, which are essential. I encourage the authors to include a study evaluating the quality of model uncertainty estimates using commonly used metrics such as Expected Calibration Error, AUROC for out-of-distribution detection etc.

* The paper claims to propose a strategy for transferring learned informative priors across different neural network architectures. However, the experiments conducted to validate this claim are limited to transferring priors between two 2-layer feed forward neural networks with different hidden dimension sizes. This raises concerns about the generalizability of the proposed strategy to significantly different architectures, such as Convolutional Neural Networks (CNNs) or other architectures used in the Bayesian deep learning literature. I encourage the authors to evaluate transferring learned priors between MLPs and CNNs, or vice-versa.

* The lack of experimentation with a broader range of neural network architectures beyond a small 2-layer feedforward model leaves open questions about the effectiveness of the proposed method to other model architectures and it's scalability to larger models. Also, the motivation for the choice of datasets used in the empirical experiments is not clear. The datasets selected are uncommon in the Bayesian deep learning literature, which makes it difficult to compare the results with existing studies and to assess the relevance and robustness of the proposed method.

### Questions
* How are the variational parameters of the BNN initialized? Does initialization of the variational posterior q(w) play a role in addressing the domain knowledge awareness, or specifying the prior p(w) is sufficient? 

* The results of Folktables dataset are presented in the transferrinf priors experiments in Table 2. Any reason for not providing the results of this dataset in Table 1?

* Can the authors clarify their motivation for choosing the specific datasets used in the experiments?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework for integrating domain knowledge into a prior over neural network weights. It uses variational inference to learn a low-rank Gaussian prior in weight space, guided by a domain knowledge loss that depends only on input data. The paper proposes four practical losses that incorporate different types of domain knowledge. It also proposes methods for transferring priors between different architectures.

### Strengths
- The paper is well-motivated, and the approach is clean. Incorporating domain knowledge into informative priors is an interesting direction for Bayesian deep learning.
- The paper proposes four general domain knowledge losses that supplement the available training data in meaningful ways.
- The paper demonstrates that the learned prior is better aligned with domain knowledge and often improves predictive performance compared to standard priors.

### Weaknesses
 - My main concern is that I'm not convinced that the best way to use the proposed domain knowledge losses is to learn a prior over weights upfront. As the paper states in page 4, we could also use these losses to regularize the training process. You could similarly train a BNN with a likelihood function that incorporates these losses. Could the authors explain why learning a prior is better than these alternatives? Section A.5 empirically compares this alternative somewhat. Still, I think a more thorough comparison would be to do a wide sweep over values of the regularization coefficient and report (performance, domain loss) for each.
- The paper mentions uncertainty as a primary motivation for using BNNs (abstract, intro, ...), but the evaluation does not measure uncertainty; this is important since the prior learned by Banana may improve performance over standard priors at the cost of worse uncertainty estimation.
- Fairness loss involves subgroup information, which is known to significantly improve fairness metrics when used during training [1]. For the experiment on Folktables, I think the comparison to the baseline is not entirely fair because the baseline doesn't have access to the subgroup information.

[1] Sagawa, Shiori, et al. "Distributionally robust neural networks for group shifts: On the importance of regularization for worst-case generalization." arXiv preprint arXiv:1911.08731 (2019).

Minor comment:
- (just out of curiosity) Is Banana an acronym for something?

### Questions
Please see weaknesses section above.

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
This work presents framework to learn prior that integrates domain knowledge in BNN. In detail, it expresses domain knowledge as a loss function and optimize the variational objective. It also suggests transferring learned priors between different model architectures, based on Moment Matching and Maximum Mean Discrepancy.

### Strengths
**[S1]** The idea of incorporating general forms of domain knowledge into prior via loss function is interesting.

**[S2]** It is novel and compelling approach transferring learned priors across different model architectures.

**[S3]** The experimental results support that the proposed methodology effectively learns prior.

### Weaknesses
I believe the proposed methods are solid, but there is chance to elevate the persuasive strength with experiments.



**[W1]** All experiments were conducted on a 2-layer MLP model. Performances on larger model would give more credibility to the paper. Specifically, while it may be challenging to evaluate performance on ViT, assessing this methodology’s impact on models like ResNet would further validate its potential for performance enhancement.



**[W2]** Experiments on a larger dataset seem necessary. Although increasing the data volume reduces the influence of the prior, making it difficult to evaluate the effect of the learned prior using the proposed method, the machine learning and deep learning communities widely accept the use of larger models and datasets. The paper's contribution can further be amplified by demonstrating that this methodology remains effective under larger dataset.



**[W3]** The paper lacks recent baselines. For prior-related baselines, it employs isotropic Gaussian, Gaussian optimized via Laplace, and GP prior. However, the informative prior method *Pre-train Your Loss* [1], a significant advancement in this area, should definitely be included.



**[W4]** The writing (notations) could also be improved.

- $x_{i}^{\prime}$ is not defined before Equation (1).
- I believe that $X^\prime = \{ x_1, ..., x_m\}$ in line 283-284 can be clear by rewriting as $X^\prime = \{ x_1^\prime, ..., x_m^\prime\}$

### Questions
I appreciate for authors to conduct a good study on an intriguing topic. I have a few questions after reading this paper.

**[Q1]** What value was used for the rank $r$ in the experiments?


**[Q2]** In Figure 3, when $K = 10$, the performance is the best, then declines, and eventually rises again. What do you think causes this phenomenon?


**[Q3]** In Section 5.3, I understood that a multi-modal distribution was used to represent a complex distribution. However, I believe that the proposed methodology for learning a general informative prior is inherently complex (as shown in Figure 2). Therefore, I’m having difficulty understanding how this experiment supports the proposed methodology. Could you please explain this in more detail? If I misunderstood this section, I would appreciate any additional clarification.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method for learning an informative prior through variational inference, as an alternative to the commonly used uninformative Gaussian prior distribution in Bayesian Neural Networks (BNNs). And, it proposes a technique for incorporating various inductive biases—difficult to represent with traditional methods—by converting them into a loss form that can be learned as a prior.

### Strengths
Strengths

- The paper is well-written and easy to follow.
- Research that enables the efficient learning of human inductive biases or specific constraints in the form of a prior distribution is valuable, and the potential to create priors containing diverse information, such as fairness, is an interesting aspect of this work.

### Weaknesses
Weaknesses

- In Section 4, it’s unclear why the authors use $\phi$ as the likelihood when calculating the posterior distribution, rather than directly calculating a posterior that reflects this loss. Instead, they create a prior distribution first and then sample from the posterior using SGMCMC methods. This two-stage sampling approach seems likely to reduce computational efficiency significantly. Specifically, the paper does not provide a clear justification for why the loss function is not directly incorporated into the posterior calculation, which could potentially streamline the process and avoid the need for a separate prior learning step. The authors should clarify the specific benefits of their two-stage approach over a more direct posterior calculation.

- Another drawback is that everything must be represented in the form of a loss. This loss-based formulation can already be interpreted as a regularization term on the likelihood or as a prior distribution in standard MAP solutions or posterior sampling methods, which raises questions about whether this approach is truly novel. The paper does not adequately discuss how this approach differs fundamentally from existing regularization techniques or prior specifications in Bayesian methods. The authors should provide a more detailed explanation of the unique aspects of their method compared to these established techniques.

- In addition to [1], which the paper mentions as related work, other studies such as [2] and [3] have also explored methods for creating informative prior distributions. Adding these to the related work section would strengthen the context.

- A key and critical point that prevents me from leaning toward acceptance is that the experiments were conducted only on a simple 2-layer MLP. As model and data scales increase, various methods can behave quite differently, and the experiment on such a limited model scale does not demonstrate that the proposed prior distribution can be effectively applied to larger models. The paper lacks experiments on more complex architectures and datasets, which is crucial to validate the scalability and general applicability of the proposed method. The authors should provide empirical evidence that their approach can be effectively used with more complex models and datasets.

- The baseline should also include methods like [1] and [2]. Similar to how the authors pre-trained the model using unlabeled data to learn a prior distribution, [1] and [2] also use self-supervised learning to pre-train models, which can then be employed as informative priors. The paper should include a comparison with these methods to demonstrate the advantages of the proposed approach.

- To ensure that the proposed method can be safely used for posterior sampling or learning, we need to examine whether it experiences severe performance degradation or operates with a degree of robustness in cases where the inductive bias is incorrect, leading to a misspecified prior distribution, i.e., under model-data misspecification conditions. The paper does not investigate the behavior of the method under conditions where the inductive bias is incorrect, which is important for understanding the robustness and reliability of the approach.

### Questions
See Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
