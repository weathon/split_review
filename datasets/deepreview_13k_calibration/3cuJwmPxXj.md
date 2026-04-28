# Identifying Representations for Intervention Extrapolation

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
The premise of identifiable and causal representation learning is to improve the current representation learning paradigm in terms of generalizability or robustness.
    Despite recent progress in questions of identifiability, more theoretical results demonstrating concrete advantages of these methods for downstream tasks are needed.
    In this paper, we
    consider the task of intervention extrapolation:
    predicting how interventions affect an outcome, even when those interventions are not observed at training time, 
    and show that identifiable representations can provide an effective solution to this task even if the interventions affect the outcome non-linearly. 
    Our setup includes an outcome variable $Y$, observed features $X$, which are generated as a non-linear transformation of latent features $Z$, and exogenous action variables $A$, which influence $Z$. The objective of intervention extrapolation is then to predict 
    how 
    interventions on $A$ that lie outside the training support of $A$ affect $Y$.
    Here, extrapolation becomes possible if the effect of $A$ on $Z$ is linear and the residual when regressing Z on A has full support. As $Z$ is latent, we combine the task of intervention extrapolation with identifiable representation learning, which we call \texttt{Rep4Ex}: we aim to map the observed features $X$ into a subspace that allows for non-linear extrapolation in $A$. We show that the hidden representation is identifiable up to an affine transformation in $Z$-space, which, we prove, is sufficient for intervention extrapolation. The identifiability is characterized by a novel 
    constraint describing the linearity assumption of $A$ on $Z$. Based on this insight, we propose a flexible method that enforces the linear invariance constraint and can be combined with any type of autoencoder. We validate our theoretical findings through a series of synthetic experiments and show that our approach can indeed succeed in predicting the effects of unseen interventions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a method to learn an effect through learning a representation of latents (Z) from observed data (X) where X and Z are related through some injective function (in practice an encoder model). It is assumed that interventions in A act on Z through which they act on some required outcome variable Y through linear functions. In such a setting the authors propose a method for learning the effects of ood interventions a^* in A. They show through experiments the efficacy of their method.

### Strengths
- Important problem. Can be thought of as OOD estimation of intervention effects through learning latent representations.
- Extremely well written paper!
- Crucially E[Y | do(A=a')] \neq E[Y | A=a'] for a' not in support of A.
- The propositions are exactly at the places that the reader thinks about the question, and are easily understandeable.
- The proofs of extrapolation are not straightforward. There have been several causal tools brought together to show the validity of extrapolation (invariance principle, mixing-unmixing, instrumental variable approaches. I quite liked the work.

### Weaknesses
 - I did not see any major weakness. One model assumption that could be weakened in future work is the linearity assumption.
- The role of the Wiener’s Tauberian theorem in the proof of hidden representation being identifiable, upto affine transformation, is not clear to me. Since this has been claimed in the abstract it would be helpful to delineate where it has been used.

- Proposition 1: If for all a in the support of A, E^S1[Y|A=a]=E^S2[Y|A=a], then how is there a set with positive lebegue measure over the support s.t the do distributions are not equal? The issue is one of measure of sets outside support being 0. Some clarification remarks would be helpful as to what positive measure outside supp(A) means.
- The linear assumption is reasonably strong. Future work may be required to extend it to GLM's or non-linear representation learning.
- Is the functional form of the SCM necessary for extrapolation? Can there be such analyses on CBNs?

### Questions
- Proposition 1: If for all a in the support of A, E^S1[Y|A=a]=E^S2[Y|A=a], then how is there a set with positive lebegue measure over the support s.t the do distributions are not equal? The issue is one of measure of sets outside support being 0. Some clarification remarks would be helpful as to what positive measure outside supp(A) means.
- The linear assumption is reasonably strong. Future work may be required to extend it to GLM's or non-linear representation learning.
- Is the functional form of the SCM necessary for extrapolation? Can there be such analyses on CBNs?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**Post rebuttal update**: I'd really like to see a couple of real-world examples that might satisfy the assumptions, but my other concerns are largely addressed. I raise my score to 8 accordingly.

The paper considers the causal effect of an intervention $A=a^*$, where value $a^*$ is not observed in the data; A affects the outcome Y through unobserved variable Z, and covariates X relates to Z through an injective function g. The paper uses a conditional moment restriction (CMR) implemented by a kernel method called maximum moment restriction (MMR), and it then uses the control function (CF) approach to identify the outcome function between Z and Y. Both the CMR and CF depend on the assumption that A affects Z linearly. The approach is theoretically guaranteed, and experiments on synthetic datasets support the theoretical analysis.

### Strengths
Using CF to achieve intervention extrapolation is a nice idea.

The theoretical analysis is serious and detailed (but I did not check the proofs in Appendix).

The paper is quite well written.

### Weaknesses
 *Technical novelties seem to be weak*. Theorem 4 seems to be an adaptation of the CF approach in (Newey et al., 1999), and Theorem 6 seems to be an adaptation of the IV approach in (D’Haultfoeuille, 2011). If there are some technical novelties, they should be discussed and compared to the original works; otherwise, I suggest being more explicit about this weakness.

*Some assumptions are strong*; particularly, the linear model between Z and A, and the injective model and noiseless model between Z and X. Intuitively, X is an observable proxy of the hidden Z, and the assumption means there is no information loss in this proxy, which is strong. Moreover,  both assumptions involve hidden variable Z and add difficulty to practical judgments. Since both assumptions are inherent in the current approach, I do not expect the author(s) to address this weakness in the rebuttal, but the following could certainly be done.

*Discussion of the setting and comparison to related work*. The discussion of the relationship to reinforcement learning is interesting but does not touch on when can we possibly expect linearity and noiseless injectivity. It would be more interesting to draw and discuss a couple of real-world problems that might satisfy the assumptions. 

On the other hand, (Khemakhem et al., 2020) and [1, 2], which are based on the former, are important related work that needs more discussions, and this would clarify the current approach.  For example, (Khemakhem et al., 2020) recover Z based on exactly the same graph as A→Z→X, and also assume g is injective but *allows an additive noise on X*; the identification also relies on assumptions on the A→Z part, where p(Z|A) is assumed to be an exponential family distribution but *allows nonlinearity*. Overall, I do not think the assumptions in (Khemakhem et al., 2020) are clearly stronger than those in the current work. Further, [1, 2] uses (Khemakhem et al., 2020) to estimate treatment effects, though not considering intervention extrapolation, [2] mentioned the ideas of CMR and CF in Sec 4.4.

[1] Wu, Pengzhou Abel, and Kenji Fukumizu. "$\beta $-Intact-VAE: Identifying and Estimating Causal Effects under Limited Overlap." International Conference on Learning Representations. 2022.
[2] Wu, Pengzhou and Kenji Fukumizu. Towards Principled Causal Effect Estimation by Deep Identifiable Models”. In: arXiv preprint arXiv:2109.15062 2021

*Additional experiments could be added*.

I think the ability to deal with unobserved confounders is a strength of the work. So, why not add experiments on this? I know eq24 contains hidden confounding, but this direction is not examined, e.g., by adjusting the strength of confounding and comparing to other methods.

As indicated above, adding real-world problems in experiments can greatly strengthen the work. Also, it would be interesting to replace the CMR part with iVAE (Khemakhem et al., 2020) and see how the results would change.

### Questions
I cannot understand the importance of Proposition 3, and it seems just a trivial restatement of Def 2 and adds confusion to me.

I think the title would be better to stress the CF approach because this arguably contributes more to intervention extrapolation than “identifying representation”.

It is weird that Wiener’s Tauberian theorem is mentioned in the Abstract but not the main text.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses identification strategies for effect extrapolation when the treatment of interest is unobserved during the experiment. The key assumptions are that 

- (exogenous) treatment A affects outcome Y through and only through an unobserved mediator Z
- can observe a rich feature $X=g_0(Z)$ that is and only is a (injective) function of Z
- the relationship between A and Z is linear

Together with some other regularity assumptions, the author shows that, given an encoder that aff-identifies $g_0^{-1}$, it is possible to identify $E[Y|do(A=a^*)]$ and $E[Y|X=x,do(A=a^*)]$ for a treatment $a^*$ that has never been observed. They also propose a method for locating such an encoder.

### Strengths
- The paper studies intervention extrapolation under a well-chosen set of assumptions, which I find more appealing than the previously studied scenarios in the literature.

- To the best of my knowledge, the proposed identification strategy is novel.

- The manuscript is clear and well-written. 

- The proposed algorithm is straightforward and practical.

### Weaknesses
 - The assumptions are clear mathematically but might seem opaque to readers unfamiliar with the literature. The authors may want to give an example of what some of the key assumptions would imply in a simple setup. For instance, the assumption that $X=g_0(Z)$ is an injective function of $Z$ is crucial, and it would be helpful to illustrate what this means in practice. Does this imply that the dimensionality of $X$ must be greater or equal to the dimensionality of $Z$? What if $X$ is a high-dimensional feature vector and $Z$ is a low-dimensional latent variable? A concrete example, such as a specific type of data where $Z$ could represent a latent health status and $X$ represents observed symptoms, would be beneficial.

- Many of the structural assumptions are not testable, and it is unclear to me when one shall be comfortable using the proposed method. The assumption that treatment A affects outcome Y only through Z is a strong assumption. It is not clear how one would verify this in practice. The linear relationship between A and Z is also a strong assumption, and it would be helpful to discuss the sensitivity of the method to violations of this assumption. Furthermore, the injectivity of $g_0$ is also not testable, and it is not clear how one would assess whether this assumption is reasonable in a given application. It would be helpful to provide some guidance on how to assess the plausibility of these assumptions in practice.

- It seems that this approach relies heavily on the linear structure between A and Z. Can this structural model be extended to $M_0 t(A) + V$ for some transformation $t(A)$ (e.g., $A^2$)? What if the relationship between A and Z is not linear, but rather through a known class of models $m_{\theta}(A)+V$ with parameters $\theta$? How would this affect the result?

- Is it possible to view the linear assumption as an approximation through a Taylor expansion around supp(A)? How would this compare with an extrapolation that is solely based on Lipschitz assumptions (see, e.g., Ben-Michael et al. 2021)?

- Although this paper is only about identification, I am curious about how the errors would accumulate.

- I find the sudden change of notation in Theorem 4 confusing.

- Can there be randomness in X, i.e., can X be a noisy observation of $g_0(Z)$?

- On page 2, the authors wrote "we allow for potentially unobserved confounders between Y and Z". How could there be confounding when the action is exogenous?

- Although the goal is very different, the approach reminds me of the negative control literature. The authors may want to discuss the connection.

### Questions
- It seems that this approach relies heavily on the linear structure between A and Z. Can this structural model be extended to $M_0 t(A) + V$ for some transformation $t(A)$ (e.g., $A^2$)? What if the relationship between A and Z is not linear, but rather through a known class of models $m_{\theta}(A)+V$ with parameters $\theta$? How would this affect the result?

- Is it possible to view the linear assumption as an approximation through a Taylor expansion around supp(A)? How would this compare with an extrapolation that is solely based on Lipschitz assumptions (see, e.g., Ben-Michael et al. 2021)?

- Although this paper is only about identification, I am curious about how the errors would accumulate.

- I find the sudden change of notation in Theorem 4 confusing.

- Can there be randomness in X, i.e., can X be a noisy observation of $g_0(Z)$?

- On page 2, the authors wrote "we allow for potentially unobserved confounders between Y and Z". How could there be confounding when the action is exogenous?

- Although the goal is very different, the approach reminds me of the negative control literature. The authors may want to discuss the connection.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a type of interventional extrapolation which consists in predicting the effect of an unseen intervention. The causal model considered is given by A -> Z -> X and Z->Y where Z is latent, A -> Z is linear, Z->X is invertible and Z -> Y is an additive noise model. The goal is then to estimate E[Y | do(A = a*)] where a* is outside its training domain. The authors separate this problem in three subproblems: 1) estimation given that Z is observed, 2) estimation this given that Z is known only up to an affine transformation, and 3) how to identify the invertible map Z->X up to an affine transformation. These identifiability results are then transferred into a practical algorithm: a) The mixing function is recovered by performing SGD on a loss consisting of a reconstruction term and a regularizer based on maximum moment restriction (MMR), and b) the learned encoder is then used to estimate the desired “do” expectation following the procedure of step 2) above.  The proposed estimation procedure is then validated on a synthetic dataset.

Review Summary: I gave the main text a thorough reading and checked the large majority of the math it presents. Despite the few problems I raised in my review, I believe this work is sufficiently novel, interesting, rigorous and well written to warrant acceptance to ICLR. I was planning to give a score of 7, since this score is not available, I'm rounding up to 8. I'm giving this score assuming that a discussion of the limitations will be added, as I suggest in my review.

### Strengths
- I agree that we need more theory to demonstrate concrete benefits of identifiable representation learning. I enjoyed this perspective.
- The paper is very clearly written and structured and relatively easy to follow despite its technicality. The level of mathematical rigor in this work is very high in my opinion and the notation is always very crisp and transparent. 
- I thought the theoretical contributions were novel and interesting. 
- I appreciated that the main ideas about the proofs were provided in the main text. Most works in this literature only give very short proof sketches if any. 
- Theoretical results are well modularized to facilitate reuse.
- I thought the method to learn the encoder up to affine transformation was novel and interesting.
- I’m left with a good feeling of having learned something new.

### Weaknesses
 - The limitations of the proposed approach could be discussed further. For example, how does the method perform under various assumption violations, such as non-linear relationships in A->Z or Z->X, or violations of the additive noise model in Z->Y? A few experiments could provide some insight into this, specifically exploring the sensitivity of the method to deviations from the assumed data generating process. For instance, what happens if the invertibility of Z->X is only approximate, or if the noise distributions are not well-behaved?
- The paper ends a bit abruptly. There’s no conclusion nor discussion of limitations. I guess this is the cost of having so much technical details in the main text (which, as I said, I appreciated, but I’m unsure whether this is a good balance.)
- I think the paper could do a better job of contrasting its results with what already appears in the literature, especially regarding the affine identifiability results. How does this compare to iVAE for example, which has a very similar data generating process with an auxiliary variable (which would be A here)? The paper should clarify the specific differences in assumptions and identifiability results compared to works in nonlinear ICA and representation learning, such as those using variational autoencoders [2]. A more detailed comparison to related work on linear identifiability of learned representations [4] and methods for disentanglement and sparsity [1] would also be beneficial. The discussion should also address how the proposed approach differs from methods using additive decoders for latent variable identification [5].
- I couldn’t grasp a few reasoning steps in the main text (see Questions below).

Minor:
- $M_0$ has full row rank implies that dim(A) >=  dim(Z). Might be worth making explicit.
- I always forget which noise variable U or V is associated with which variable. How about replacing V by V_z and U by V_y?  
- Footnote one: what is $\mathcal{B}$?
- The introduction rightfully points out that the literature has almost no works giving theoretical arguments for why the identifiable representation learning is important. You might want to consider citing [1, 5] as examples of work pushing that direction.

### Questions
- Lemma 7 in Appendix A: Could you explain the argument a bit more? I’m unaware of this proof technique, so citing the result used here would be useful. Or is it an alternative definition of conditional independence that I’m not aware of?
- Paragraph after (3):
    - Could you give some insight as to why $\ell$ and $\lambda$ are not identifiable up to additive constant without further assumptions in (3)? I’m not sure I see what could go wrong since we observe Y, Z and V here (V is identifiable). Also, can you state the assumption from Newey et al. (1999) that allows you to identify $\ell$? I suspect it has something to do with the differentiability + supp(A) convex assumption from Theorem 4?
    - It is written “for all $a^* \in M_0 supp(A) + supp(V)$” somewhere, but it seems wrong since $M_0 supp(A) + supp(V)$ is an event for Z, no? I’m not sure I’m following this part of the argument and onward.
    - Same paragraph: I think we need to compute $\ell(z)$ only for $z \in M_0\mathcal{A} + supp(V)$, no? 
- Eq. (16): I’m not sure why this holds. Is it because the inside of the conditional expectation is equal to V? But we don’t assume E[V] = 0 right? What am I missing? Since this is so crucial to the algorithm, it might be worth expliciting further.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
