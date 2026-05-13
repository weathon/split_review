# Learning Latent Structural Causal Models

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Causal learning has long concerned itself with the accurate recovery of underlying causal mechanisms. Such causal modelling enables better explanations of out-of-distribution data. Prior works on causal learning assume that the high-level causal variables are given. However, in machine learning tasks, one often operates on low-level data like image pixels or high-dimensional vectors. In such settings, the entire Structural Causal Model (SCM) -- structure, parameters, \textit{and} high-level causal variables -- is unobserved and needs to be learnt from low-level data. We treat this problem as Bayesian inference of the latent SCM, given low-level data. For linear Gaussian additive noise SCMs, we present a tractable approximate inference method which performs joint inference over the causal variables, structure and parameters of the latent SCM from random, known interventions. Experiments are performed on synthetic datasets and a causally generated image dataset to demonstrate the efficacy of our approach. We also perform image generation from unseen interventions, thereby verifying out of distribution generalization for the proposed causal model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work seeks to present a practical approach for inferring latent linear-Gaussian causal models solely from observations, utilizing a Bayesian framework. The method entails breaking down the process of inferring latent causal variables into two main components: inferring the latent weight matrix and estimating latent Gaussian noises. To validate the effectiveness of the proposed method, it conduct experiments on synthetic datasets and an image dataset.

### Strengths
My primary concerns are as follows:

1) Theoretical guarantees: It is widely recognized that identifying latent causal models is a challenging task without the incorporation of additional assumptions. Recent studies have made significant progress in demonstrating the identifiability of latent causal models by exploring the change of weights, such as hard and soft interventions [1][2], on the model's weights. Nevertheless, there has been a noticeable absence of discussion regarding how our proposed method satisfies the assumptions necessary for achieving these identifiability results.

2) Contributions: The primary contribution of this work lies in the development of a practical method for inferring latent causal models. However, from a technical perspective, the contributions are somewhat limited, as the technical details closely resemble those of previous work [3], even though this study uncovers causal models in a latent space. Additionally, as a practical method, the experiments conducted in this work are somewhat lacking in comprehensiveness. For instance, the image dataset utilized in this study is relatively simple, which may not sufficiently validate the advantages of the proposed method. To enhance the robustness of the findings, I would suggest the author consider using more complex datasets, such as Causal3DIdent in [4] and CausalCircuit in [1]. Furthermore, it is imperative to perform a comparative analysis of the proposed methods against existing approaches, such as those in [1].

3) Several critical details remain unaddressed, such as the proposed method to ensure that the learned causal models conform to a Directed Acyclic Graph (DAG) structure.


[1] Brehmer, Johann, et al. "Weakly supervised causal representation learning." Advances in Neural Information Processing Systems 35 (2022): 38319-38331.
[2] Liu, Yuhang, et al. "Identifying weight-variant latent causal models." arXiv preprint arXiv:2208.14153 (2022).
[3] Cundy, Chris, Aditya Grover, and Stefano Ermon. "Bcd nets: Scalable variational approaches for bayesian causal discovery." Advances in Neural Information Processing Systems 34 (2021): 7095-7110.
[4] Von Kügelgen, Julius, et al. "Self-supervised learning with data augmentations provably isolates content from style." Advances in neural information processing systems 34 (2021): 16451-16467.

### Weaknesses
My primary concerns are as follows:

1) Theoretical guarantees: It is widely recognized that identifying latent causal models is a challenging task without the incorporation of additional assumptions. Recent studies have made significant progress in demonstrating the identifiability of latent causal models by exploring the change of weights, such as hard and soft interventions [1][2], on the model's weights. Nevertheless, there has been a noticeable absence of discussion regarding how our proposed method satisfies the assumptions necessary for achieving these identifiability results. Specifically, the method does not discuss whether the assumptions required for identifiability, such as the faithfulness assumption or the specific forms of interventions, are met by the proposed approach. Furthermore, the paper lacks a discussion on how the choice of prior distributions over the latent variables and model parameters might influence the identifiability of the learned causal structure.

2) Contributions: The primary contribution of this work lies in the development of a practical method for inferring latent causal models. However, from a technical perspective, the contributions are somewhat limited, as the technical details closely resemble those of previous work [3], even though this study uncovers causal models in a latent space. Additionally, as a practical method, the experiments conducted in this work are somewhat lacking in comprehensiveness. For instance, the image dataset utilized in this study is relatively simple, which may not sufficiently validate the advantages of the proposed method. To enhance the robustness of the findings, I would suggest the author consider using more complex datasets, such as Causal3DIdent in [4] and CausalCircuit in [1]. Furthermore, it is imperative to perform a comparative analysis of the proposed methods against existing approaches, such as those in [1]. The paper does not explore the sensitivity of the method to various hyperparameter settings, such as the learning rate, batch size, and the number of training epochs, which are crucial for practical applications. The lack of ablation studies on these hyperparameters limits the understanding of the method's robustness and generalizability.

3) Several critical details remain unaddressed, such as the proposed method to ensure that the learned causal models conform to a Directed Acyclic Graph (DAG) structure. The paper does not explicitly state how the acyclicity constraint is enforced during the learning process. While the authors mention ancestral sampling, they do not provide sufficient detail on how the sampling process guarantees that the learned adjacency matrix represents a DAG. Specifically, the paper does not discuss how the parameterization of the lower triangle of the adjacency matrix ensures that no cycles are introduced during the sampling process, and how this parameterization relates to the underlying causal assumptions.

### Questions
See above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the learning of latent causal structures from low-level observational data with known interventions. The authors primarily concentrate on learning a linear latent causal model and employ Bayesian inference methods to tackle this learning task. Additionally, they conducted experiments using synthetic and the image dataset to validate the effectiveness of their proposed approach.

### Strengths
This paper is well written with clear motivation.

What the authors focused on is indeed an interesting yet challenging research topic in causal inference and machine learning.

### Weaknesses
Novelty: In my opinion, the authors introduced an approach for parameter estimation through deep learning methods. However, it's worth noting that they didn't provide a theoretical analysis to support their approach. That is to say, the authors did not offer an analysis of the identifiability of the latent causal model. Without theoretical identifiability results, it becomes challenging to have full confidence in the outcomes generated by their proposed method.

Experiments: The experimental results only demonstrated a basic setting with five nodes, which may not be sufficient to provide a comprehensive empirical study.

### Questions
Regarding the number of latent variables:  How can we get the number of latent variables? Do we need to know it in advance?

Regarding the intervention: Is the intervening variable only on the observed variable? Can we intervet the latent variables?

Regarding the experiments: What is the performance of different setting graphs?

### Soundness
2 fair

### Presentation
3 good

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
This paper introduces an empirical estimation method for inferring latent causal relationships within the framework of causal representation learning. It focuses on assuming linear latent causal models and formulates the problem as a Bayesian inference task for these models.

### Strengths
This paper considers the estimation of latent causal models, which is a very important task in causal representation learning.

### Weaknesses
The novelty of this work appears somewhat constrained. It focuses solely on the scenario where the latent causal model is linear, interventions on latent variables are assumed, and the intervention targets are known. Furthermore, it does not explicitly clarify whether this setting is theoretically identifiable. The assumption of linear latent causal models is a significant restriction, as many real-world systems exhibit non-linear relationships. The requirement of interventions on latent variables, with known targets, is also a strong assumption that limits the applicability of the method in scenarios where such interventions are not feasible or observable. The lack of theoretical identifiability proof is a major concern, as it is not clear whether the method can recover the true causal structure even under ideal conditions. 

The experimental validation is somewhat lacking. The paper only presents results with 5 latent variables, which is not enough for an empirical study. The experiments do not explore the sensitivity of the method to various parameters, such as the number of samples, the noise level, or the strength of causal effects. The absence of comparisons with other state-of-the-art methods in causal representation learning makes it difficult to assess the relative performance of the proposed approach.

### Questions
1. It is crucial for the authors to explicitly establish whether this setting is theoretically identifiable prior to introducing empirical estimation methods.

2. The paper would greatly benefit from a more comprehensive set of experiments. This should include exploring different numbers of latent variables, varying graph densities, and adjusting sample sizes for a more thorough assessment.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper solves a variation of the causal representation learning problem where the joint posterior over the causal variable, the causal structure, and the parameters of the latent SCM are obtained from given high-dimensional observations.
For this purpose, the paper proposes an unsupervised approach that uses variational inference with assumptions such as linear Gaussian latent SCMs with known interventions.
The authors propose a deep learning approach to learn parameters that allow sampling of the adjacency matrix and the covariance matrix which can be used to generate samples from the training distributions.

### Strengths
The paper is well written. It contains a good literature review. I appreciate the authors’ effort to discuss all the necessary theoretical points that made it easy to understand their approach. Also, the experimental results are well-presented. The plots are quite useful to understand the results.

### Weaknesses
I provide my concerns below:

1. [Figure 2] The authors should provide more explanations about the model architecture in Figure 2. Some description in the caption would help the reader to understand the whole algorithm while reading the introduction section.

2. [Section 4.2]: The authors mentioned about obtaining q_phi(G,\theta|Z) from existing Bayesian structure learning methods. A high-level description of these methods can be provided for the reader’s convenience.

3. The ancestral sampling method should be described more explicitly.

4. [Section 5: Experiments] It is not specifically mentioned about the 3-layer neural network. For example what type of layers did the authors use? What is their dimension, and what activation functions were used? The training details can be provided in the appendix section.

Major concern:

5. [Comparison with previous work]*Although the authors discussed different recent approaches in their related work section, they did not show how their approach is different from those and how their approaches outperform earlier works. For example, the authors cited Brehmer et al. (2022) who identify the causal structure and disentangle causal variables for arbitrary, unknown causal graphs with observations before and after intervention. The assumptions in this work seem to be more relaxed than the assumptions mentioned in this paper (linear Gaussian assumption, known intervention). It is not clearly specified what improvement this paper is doing compared to previous works.

6. [Theoretical guarantee] The novelty of this paper seem to be provided in section 4.2 and 4.3 where they propose a deep learning approach to learn parameters \theta and \phi. These parameters allow us to sample the adjacency matrix and the covariance matrix. However, the authors did not discuss the identifiability of the SCM and the causal structure in detail. There is no theoretical guarantee that the algorithm will learn to sample true SCM and the causal structure. For example, the author’s one cited work Brehmer et al. (2022) claims that they can find SCMs identifiable up to a relabelling and elementwise reparameterizations of the causal variables.
Without any theoretical identifiability, what is the guarantee that the algorithm will not overfit the training datasets?  What is the guarantee that the resultant SCM and structure will match the interventional distribution (ex: distribution shift) that was absent in the training data? 

7. [Baselines]: Although the authors discussed some approaches that deal with causal representation learning problems in the related work section, it is unclear why they could not find any common ground to show where they could show their comparative performance.

8. [Synthetic experiments] The authors showed their performance on a 5-node DAG with 20 random interventions. The authors should perform more intensive experiments such as: for small to large graphs with varying edge density and varying interventions.

9. [Real-world dataset] The authors used only synthetic and comparatively less complex datasets. The algorithm performance would be better observed on more complicated datasets such as Causal3DIdent [1] etc.

### Questions
Here I provide my questions to the authors about this paper.

1. How does this algorithm fail when the SCM is not linear Gaussian additive noise SCM?
2. How is d: the number of latent variables known? 
3. In a real-world setting, if Z are latent variables, how the interventions are known? How is it determined which latent variables are being intervened on? 
4. The question about overfitting and finding the unique/identifiable SCM that will match unseen interventions absent in the training data.
5. How are the loss terms being calculated in Algorithm 1 lines 14,15?
 6. How \hat{L} and \hat{\sigma} are being sampled at Algorithm 1 line 3? How is gradient descent being done without breaking the computational graph since the author performs sampling at lines 3 and 10? Is the loss terms differentiable with respect to \phi and \theta even though sampling is performed?

7. What is the role of interventional datasets? How would the algorithm’s performance change when the available data is from more or less number of interventions?  

8. How does the algorithm perform for different-sized DAGs with varying edge density and varying interventions?
9. What is the causal structure for the Chemistry dataset? It should be precisely mentioned.

I would request the authors to resolve my mentioned concerns and answer the questions. I am willing to increase the score if the issues are properly dealt with.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
