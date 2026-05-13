# Gaussian Loss Smoothing Enables Certified Training with Tight Convex Relaxations

- Decision: Reject
- Scores: 6, 1, 3

## Abstract
Training neural networks with high certified accuracy against adversarial examples remains an open challenge despite significant efforts. 
    While certification methods can effectively leverage tight convex relaxations for bound computation, in training, these methods, perhaps surprisingly, can perform worse than looser relaxations. 
    Prior work hypothesized that this phenomenon is caused by the discontinuity, non-smoothness, and perturbation sensitivity of the loss surface induced by tighter relaxations. 
    In this work, we theoretically show that Gaussian Loss Smoothing (GLS) can alleviate these issues. 
    We confirm this empirically by instantiating GLS with two variants: a zeroth-order optimization algorithm, called PGPE, which allows training with non-differentiable relaxations, and a first-order optimization algorithm, called RGS, which requires gradients of the relaxation but is much more efficient than PGPE. 
    Extensive experiments show that when combined with tight relaxations, these methods surpass state-of-the-art methods when training on the same network architecture for many settings. 
    Our results clearly demonstrate the promise of Gaussian Loss Smoothing for training certifiably robust neural networks and pave a path towards leveraging tighter relaxations for certified training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to use a method (Gaussian Loss Smoothing) to address the paradox of certified training which is caused by the discontinuity/non-smoothness/sensitivity issues of certifiable training with tighter convex relaxations. Moreover, the authors also use a gradient-based method called Randomized Gradient Smoothing (RGS) to scale GLS to larger models.

### Strengths
I think the following strength itself is enough for accept.
- The paradox of certified training is an important subject to study.
- The proposed method (GLS) is well-motivated and backed up by theoretical results.
- The empirical results on small perturbation settings in Table 3 are quite impressive.

### Weaknesses
This paper is well-motivated, but has a minor weakness in the performance (on large perturbation) detailed as follows:
- Table 3 (Table 5 in Appendix) shows the results for small (large) perturbation settings. The results for large perturbation is not significant. IBP performs well for large perturbations and other tighter methods does well for small perturbations. This is because of the continuity, smoothness and sensitivity of the loss landscape. Thus, to check the effectiveness of GLS, I think it is crucial to check the result of tighter methods on large perturbation settings. However, setups (i) MNIST $\epsilon=0.3$ and (ii) CIFAR-10 $\epsilon=8/255$ show that 
GLS (or RGS) (i) does not show a significant performance gain (DP-RGS (IBP) vs MTL-IBP; 88.69 vs 88.68) or (ii) shows a worse performance (29.25 vs 29.62). This should be discussed in the main text (not in Appendix). I don't think the performance itself is a reason for a rejection, but it needs more discussion.
- In Table 1, "the more precise DeepPoly bounds now yield the best certified accuracy across all settings, even outperforming accuracy at low perturbation radii'', but not for the large perturbation (IBP vs DeepPoly-PGPE; 77.23 vs 74.28, 25.72 vs 22.19). The claim is misleading, as it only holds for small perturbations and not across all settings as stated.
- In GRAD Training, "IBP dominates the other methods, confirming the paradox of certified training", but in the original paper of CROWN-IBP, CROWN-IBP outperforms IBP for a larger network (see their Table 2 https://arxiv.org/pdf/1906.06316). It is important to clarify that the IBP method used in this paper may be a more recent variant, as the original IBP is known to be weaker than CROWN-IBP on larger networks.
- (For a larger model,) IBP outperforms the other methods (e.g, CROWN-IBP, CAP) for large perturbation, not for small perturbation (e.g., see Table 1 in Lee et al. (2021)). This implies that the paradox plays more important role for a larger perturbation.

Please check the Questions part together. I think unclear presentation is also a weakness.

### Questions
- There is no comparison with CROWN-IBP in Table 3. Why?
- "We remark that scaling to CNN7 used by the SOTA methods is still infeasible due to the high computatinoal cost of evaluating DeepPoly" How about applying RGS to CROWN-IBP as it is cheaper than DeepPoly?
- What do the italic numbers mean in Table 3?
- DP-RGS appears first in L480, but never defined (seems like DP-RGS = DeepPoly-RGS).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper talks about the variation in certified training; though tighter relaxations sometimes reduce performance compared to looser bounds, it shows the authors introducing Gaussian Loss Smoothing as one of the methods for smoothing the loss landscape to reduce discontinuity and sensitivity—the major hurdles in certified training with tight relaxations.

They provide two ways of realizing the different realizations of GLS: first is PGPE, a gradient-free approach based on policy gradients with parameter-based exploration; second is RGS, which is described as a gradient-based approach using randomized gradient smoothing. Experimental results on several datasets illustrate that indeed the algorithm GLS outperforms current methods relying on tight relaxations; sometimes its performance is tested along with the DEEPPOLY relaxation.

### Strengths
GLS introduces novelty in using Gaussian smoothing across the loss landscapes, strongly problematic in certified training.

### Weaknesses
## Writing Style

- **Introduction**: In some respects, the introduction could be improved about adversarial certified robustness. It is abrupt and feels more work-related.
  
- **Transitions and Structure**: Transitions from one section to another are missing; hence, making the paper hard to follow. Statements such as, "While CROWN-IBP is not strictly more or less precise than either IBP or DEEPPOLY," necessarily need references or explanations. The lack of clear transitions between ideas makes it difficult to understand the logical flow of the paper and the motivation behind the proposed method.

- **Undefined Terms**: Terms such as "soundness" and "sensitivity" are undefined. The absence of formal definitions for these terms makes it difficult to assess the validity and scope of the theoretical claims.

- **Results of experiments**: These are presented in a very untidy fashion.


## Related Work

- **Definitions**: Some more clear definitions can be provided, for instance, adversarial attack and adversarial robustness because the latter is different from certified robustness. The distinction between these concepts is crucial for understanding the paper's contribution, and the lack of precise definitions creates ambiguity.
  
- **Redundant Subsections**: Sections 2.1 would seem to represent redundant subsections: "Training for Robustness" and "Adversarial Training."


## Theoretical Findings

- **Lack of Rigor**: Theoretical statements, like Theorem 3.1, are informal and not mathematically precise. References to results, including Stein's Lemma [2], could be good in the proof. The theorem lacks the necessary mathematical formalism, making it difficult to verify its correctness and understand its implications. The connection to Stein's Lemma is not made explicit, which could strengthen the theoretical foundation.
  
- **Flaw in Proofs in Lemmas**: 
In the proof of Lemma B.1 terminology and symbols that are important are not defined (for example, \( \delta \theta\), \(P_{\epsilon_1}\), \(P_{\epsilon_2}\), \(P_{\mathcal{N}(0, \sigma^2)}\)). The authors seem to take the limit \(\delta \theta\) to \(0\) but it is never stated anywhere in the proof and the integral of the derivative of the loss  \(L^\prime\)  should be a multi dimensional integral as the input space is multi dimensional.
In Lemma B.2's proof  the simplifications are excessive,  the structure of the proof is highly defective in many places and it needs a thorough revision. The lack of clarity and precision in the proofs undermines the credibility of the theoretical results.


## Experimental Results

- **Lack of Detail**: Neither the dataset nor the architecture used in Figure 1 are specified. This lack of detail makes it difficult to reproduce the results and assess their validity.
  
- **Performance Gains**: Although the experimental results are somewhat improved, they are not very significant compared to previous methods; therefore, this added complexity is questionable in value. Presentation of the standard deviations over multiple runs would have given more robust conclusions since apparent gains are marginal.

### Questions
GLS appears to be related to Sharpness-Aware Minimization (SAM) [1], as both approaches aim to smooth the loss landscape for a more regular surface. It would be beneficial to include a discussion or a related work section to clarify this connection in the paper.

[1] Foret et al., “Sharpness-Aware Minimization for Efficiently Improving Generalization,” ICLR, 2021.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes to use Gaussian Loss Smoothing (GLS) with certified training algorithm, such as IBP, CROWN, etc. The motivation is that a previous paper pointed out that methods other than IBP, though having tighter relaxation, suffer from discontinuity, non-smoothness, perturbation sensitivity. The authors argue that GLS can make the loss surface smoother using a theoretical result and some plots as evidence. The method is tested on MNIST, Cifar-10 and TinyImagenet.

### Strengths
1. The writing is fine. There is little difficulty understanding the paper.

### Weaknesses
1. Contribution: This paper proposes to apply GLS to existing certified training methods such as IBP and DeepPoly, and one can use PGPE or RGS to compute the GLS. Note that, however, all of IBP, DeepPoly, GLS, PGPE and RGS are existing methods. Theorem 3.1 is a direct application of an existing result. So if I understand correctly, the only novelty of this submission is combining these things together, and thus the contribution is incremental.
2. Performance: How does the proposed method perform? From Table 1, it seems that the proposed method (PGPE) is not significantly better than the standard method (GRAD), if not worse. It is true that PGPE makes DeepPoly better than IBP, but the way it does that is to make IBP worse, not making DeepPoly better. On MNIST (0.3) and CIFAR-10 (8/255), the best PGPE method is worse than the best GRAD method. On the other two settings, it is only slightly better. For all settings, IBP-PGPE is worse than IBP-GRAD (standard). Thus, this result suggests that one probably should not use PGPE. There is no evidence that the proposed method works in practice.
3. Experimental results: Tables 1 and 3 seem contracting with each other. In Table 1, standard IBP on CIFAR-10 (2/255) has natural accuracy 48.05% and certified accuracy 37.69%; in Table 3, the two reported numbers are 54.92% and 45.36%. Probably this is because CNN5 is better than CNN3, but then what is the point of Table 1? Why not always use a bigger model (CNN7 seems even better). And why not compare with RGS in Table 1? I don't think there is anything preventing you from comparing with RGS in Table 1. The authors report DP-RGS to be the best method in Table 3, but since there are so many problems with the tables I do not trust this result.

### Questions
1. DeepPoly-GRAD achieves 90.04% certified accuracy on MNIST (0.1) in Table 1; in Table 2 this number is only 68.47%. Is this a typo? I don't believe that changing the model size can make such a big difference; plus, only DeepPoly-GRAD has such a huge drop in performance.
2. Is it correct that you are only changing the loss of training the model, but you are not changing the way of certifying the model?

### Soundness
2

### Presentation
3

### Contribution
1
