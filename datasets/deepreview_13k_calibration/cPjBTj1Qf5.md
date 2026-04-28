# Counterfactual fairness prediction:  Consistent estimation with generative models and theoretical guarantees

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
Fairness in predictions is of direct importance in practice due to legal, ethical, and societal reasons. This is often accomplished through counterfactual fairness, which ensures that the prediction for an individual is the same as that in a counterfactual world under a different sensitive attribute. However, achieving counterfactual fairness is challenging as counterfactuals are unobservable, and, because of that, existing baselines for counterfactual fairness do not have theoretical guarantees. In this paper, we propose a novel counterfactual fairness predictor for making predictions under counterfactual fairness. Here, we follow the standard counterfactual fairness setting and directly learn the counterfactual distribution of the descendants of the sensitive attribute via tailored neural networks, which we then use to enforce fair predictions through a novel counterfactual mediator regularization. Unique to our work is that we provide theoretical guarantees that our method is effective in ensuring the notion of counterfactual fairness. We further compare the performance across various datasets, where our method achieves state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce a framework called the Generative Counterfactual Fairness Network (GCFN), which is designed to produce predictions that are counterfactually fair. Their approach involves a two-step process using Generative Adversarial Networks (GANs) to learn the distribution of counterfactuals of sensitive attribute mediators. This method is unique in that it directly models counterfactual mediators without requiring latent variable inference, a step that previous methods used but lacked guarantees of fairness.

### Strengths
1. Counterfactual fairness is crucial since it directly addresses biases related to sensitive attributes. Counterfactual fairness ensures fairness at an individual level.

2. The paper is well-written and easy to follow.
3. The proposed method is evaluated through different settings on multiple datasets.

### Weaknesses
I have multiple concerns regarding the theory, objective and experiments.

 1. The objective requires training multiple GANs, which may not be feasible for lots of real-world tasks.

 2. Lemma 1: The cited Corollary 3 (Melnychuk et al., 2023) is valid only for real-valued random variables. If the mediator is assumed to be scalar, this assumption should be explicitly stated. Moreover, assuming real-valued mediators is restrictive.

 3. The performance heavily depends on the quality of the generated counterfactual mediator. How is this ensured in your objective? While the objective includes both adversarial loss and reconstruction loss, it is unclear how this setup could effectively control the quality of the generated counterfactual mediators. For example, if the generated counterfactual mediator $\tilde{M}_{a’}$ is distributionally aligned with the factual data $M$ given $A=a'$, how can a discriminator distinguish between them using your objective? If the discriminator is unable to differentiate between them, how can we assert that the generated mediators are counterfactual rather than factual samples conditioned on an alternate sensitive attribute value? In such a case, the method would likely address group fairness rather than counterfactual fairness.

 4. Why not just use some generative model to generate counterfactuals and train a classifier on top of it? Is generating the mediator M easier or more accurate compared to directly generating the counterfactual $X$?

 5. In Appendix D, why does equation 18 hold? What does $\{M, G(X,0,M)_1\}$ mean? And why $\{M, G(X,0,M)_1\}=\tilde{G}$?

### Questions
1. The objective requires training multiple GANs, which may not be feasible for lots of real-world tasks.

2. Lemma 1: The cited Corollary 3 (Melnychuk et al., 2023) is valid only for real-valued random variables. If the mediator is assumed to be scalar, this assumption should be explicitly stated. Moreover, assuming real-valued mediators is restrictive.

3. The performance heavily depends on the quality of the generated counterfactual mediator. How is this ensured in your objective? While the objective includes both adversarial loss and reconstruction loss, it is unclear how this setup could effectively control the quality of the generated counterfactual mediators. For example, if the generated counterfactual mediator $\tilde{M}_{a’}$ is distributionally aligned with the factual data $M$ given $A=a'$, how can a discriminator distinguish between them using your objective? If the discriminator is unable to differentiate between them, how can we assert that the generated mediators are counterfactual rather than factual samples conditioned on an alternate sensitive attribute value? In such a case, the method would likely address group fairness rather than counterfactual fairness.

4. Why not just use some generative model to generate counterfactuals and train a classifier on top of it? Is generating the mediator M easier or more accurate compared to directly generating the counterfactual $X$?

5. In Appendix D, why does equation 18 hold? What does $\\{M, G(X,0,M)_1\\}$ mean? And why $\\{M, G(X,0,M)_1\\}=\tilde{G}$?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses the challenge of achieving counterfactual fairness by proposing a novel approach that learns the counterfactual distribution of the descendants of sensitive attributes using specifically designed neural networks. Fair predictions are enforced through a counterfactual mediator regularization, which aims to minimize the influence of sensitive attributes. Experimental results demonstrate the effectiveness of this architecture.

### Strengths
1. The identifiability of counterfactual fairness is an important problem.

2. Experimental results showcase the effectiveness of the proposed architecture.

### Weaknesses
1. The paper assumes that the function  $f_M$  is a bijective generation mechanism, which is a strong assumption, particularly in real-world datasets where such conditions are rarely met. While this assumption holds in synthetic datasets, it limits the method’s applicability in fairness contexts that generally involve real-world data. Therefore, the claim that this is the first method for counterfactual fair predictions with theoretical guarantees might be overstated given the challenges with real data. The experiment on real data demonstrates the anticipated outcomes that the proposed GAN architecture can achieve. However, there appears to be a disconnect between the empirical application and the theoretical results; the practical implementation and theoretical guarantees seem to function as separate aspects without a relationship.

2. Lemma 1 seems to be a straightforward extension of results from previous studies (e.g., Lemma B.2 in Nasr-Esfahany et al., 2023, and Corollary 3 in Melnychuk et al., 2023) to GANs. It’s plausible that similar results could be obtained for other neural models with continuously differentiable functions, raising the question of whether the paper’s theoretical contributions are specific to GANs or could be generalized to other architectures.

3. Although the reconstruction loss is employed to ensure the similarity between generated factual mediators and observed factual mediators, there is no explicit assurance regarding the accuracy of generated counterfactuals. This limitation raises concerns about the robustness of counterfactual predictions produced by the model.

4. Lemma 2 establishes an upper bound on the effect of the sensitive attribute on the target variable by focusing on the performance of counterfactual mediator generation and regularization. However, this upper bound does not imply the model’s effectiveness in achieving counterfactual fairness. It also leaves open questions regarding the extent to which the proposed method truly guarantees counterfactual fairness in real-world applications.

### Questions
Please refer to the weaknesses above.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to address counterfactual fairness by proposing a two-step solution: (1) training a Generative Adversarial Network (GAN) to estimate counterfactual mediators and (2) training a predictor with regularization based on the estimated counterfactual mediator. Under certain assumptions, they demonstrate that their method can guarantee counterfactual fairness. They validate their method on semi-synthetic and real-world datasets.

### Strengths
1. This paper proposes theoretical results on counterfactual fairness. While I didn’t examine all the proofs in detail, their result seems solid.
2. The writing is clear, and the paper is easy to follow.
3. The empirical study is generally convincing.

### Weaknesses
 **Theoretical contribution in comparison to existing works**

While I acknowledge the theoretical contribution of this paper, I believe the authors overemphasize their contribution relative to existing baselines. For example, methods in [1][2][3][4] all provide methods that satisfy counterfactual fairness under certain conditions.
1. Could the authors clarify the differences between these methods in terms of theoretical guarantees? With regard to [1], I don’t believe the primary difference lies in the need for knowledge of the ground-truth SCM, as stated in the paper. They only need to know which variables are the descendants of the sensitive attributes, which is also necessary for the method proposed in this paper. Other papers are not discussed in the current draft.
2. The authors should discuss the significance of their unique contribution more carefully. In some sections, they describe their approach as “the first neural method with theoretical guarantees,” while in others, this claim is omitted (e.g., Line 17, Line 48). This inconsistency could be misleading to readers.



**Causal Model**

Causal-based fairness notions rely heavily on the chosen causal model. Hence, it is important to clearly present the motivation behind the selected causal model. I agree that the causal model considered in this paper is general. However, could the authors provide additional insight into this model, perhaps by offering a real-world example to illustrate the role of each variable?


**Presentation**

Here are a few places where I find the presentation to be unclear or confusing
1. Line 154 - Does the theoretical result in this paper require invertibility? If so, this should be explicitly stated alongside other assumptions, as this is a fairly strong assumption.
2. In the original Standard Fairness Model, the $X$ is considered as a hidden confounder. A similar $U$ is considered in some other existing works such as [1][2]. Why can we assume access to $X$ in this paper?
3. Line 282 - Could the authors clarify why this is described as “non-trivial” and explain how it might be advantageous (if at all) compared to existing methods that require access to counterfactuals?

### Questions
Two short questions
1. Could there be an arrow from $A$ to $Y$ in Figure1?
3. Line 206 - Could the authors clarify more carefully why avoiding the abduction-action-prediction framework reduces the possibility of estimation errors?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposed a new method to produce counterfactually fair predictions. Specifically, the authors designed a GAN-like structure (GCFN) to learn the counterfactual mediator distribution when the structural causal model (SCM) satisfies certain assumptions. Then the learned mediator together with the features is used to learn the predictor. Furthermore, the paper provided some theoretical guarantees of the method. Lemma 1 claims that GCFN is able to learn the counterfactual mediator distribution only with the factual mediator values, while Lemma 2 provides a fairness guarantee. Experiments on synthetic and real datasets verify the effectiveness of the method.

### Strengths
1. The topic is well-motivated: learning counterfactually fair predictors is important, while VAE-based methods may produce biased estimations of latent variables.

2. Using a GAN-like structure naturally makes sense to me, and the causal structure in Figure 1 is not too restricted in my opinion.

3. The theoretical analysis provides guarantee of the proposed algorithm.

### Weaknesses
1.  The conditions of Lemma 1 are restrictive. Moreover, Lemma 1 seems to say we can always identify the distribution of the counterfactual mediator. Does this mean if we directly learn $P(M|X=x, A=a)$ we can learn the distribution of $M_{a'}$ and we do not necessarily need GAN? After all, the GAN can only be trained using factual data, so it approximates the factual mediator distribution. 

(After reading the review of other reviewers, Lemma 1 has some problems and the authors downgrade it to a remark. I feel that the clarity of the contribution indeed has some problems. Considering many works in counterfactual fairness have restrictive assumptions, I still think this work has some merit and will retain a positive score)

2. It would be beneficial to include some examples to illustrate: (i) how VAE-based methods get a biased estimation of latent variables; (ii) What the mediators are in some practical example causal graphs.

3. The paper does not compare the proposed method with the counterfactually fair representation method [Zuo et al., 2023]. Basically, learning the counterfactual mediator also serves the function of preserving more information of the features, so it is worthwhile comparing the 2 methods.

4. It may help to include some proof intuition in the main paper.

### Questions
1. Could you elaborate more on Lemma 1 (see weakness 1)?

2.  Line 338:  how can we empirically measure the quality of "generated counterfactual mediator", i.e., $\|M_{A'} - \hat{M}_{A'}\|^2_2$?

### Soundness
2

### Presentation
2

### Contribution
3
