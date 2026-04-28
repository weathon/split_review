# Microcanonical Langevin Ensembles: Advancing the Sampling of Bayesian Neural Networks

- Decision: Accept
- Avg Score: 5.75
- Scores: 3, 6, 6, 8

## Abstract
Despite recent advances, sampling-based inference for Bayesian Neural Networks (BNNs) remains a significant challenge in probabilistic deep learning. While sampling-based approaches do not require a variational distribution assumption, current state-of-the-art samplers still struggle to navigate the complex and highly multimodal posteriors of BNNs. As a consequence, sampling still requires considerably longer inference times than non-Bayesian methods even for small neural networks, despite recent advances in making software implementations more efficient. Besides the difficulty of finding high-probability regions, the time until samplers provide sufficient exploration of these areas remains unpredictable. To tackle these challenges, we introduce an ensembling approach that leverages strategies from optimization and a recently proposed sampler called Microcanonical Langevin Monte Carlo (MCLMC) for efficient, robust and predictable sampling performance. Compared to approaches based on the state-of-the-art No-U-Turn Sampler, our approach delivers substantial speedups up to an order of magnitude, while maintaining or improving predictive performance and uncertainty quantification across diverse tasks and data modalities. The suggested Microcanonical Langevin Ensembles and modifications to MCLMC additionally enhance the method's predictability in resource requirements, facilitating easier parallelization. All in all, the proposed method offers a promising direction for practical, scalable inference for BNNs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This interesting paper considers the application of microcanonical Langevin Monte Carlo, a variant of HMC, to sample from Bayesian neural network posteriors. The main idea of microcanonical LMC is that the velocity's norm is fixed and not changing unlike in HMC, which is supposedly helping with more stable exploration and allows for larger step sizes in the presence of steep landscapes. The original algorithm was proposed in the 2023 paper "Fluctuation without dissipation: Microcanonical Langevin Monte Carlo". The main contribution here is to consider an ensembled variant of that algorithm, and extensive numerical experiments on various Bayesian neural networks to show the practical performance of this method.

### Strengths
Microcanonical Langevin Monte Carlo is an interesting idea, and the numerical performance shows good improvements over NUTS, with impressive results in terms of predictive log posterior values.

### Weaknesses
The only novelty in terms of algorithmic development is the use of ensembling, Microcanical LMC was already proposed in the previous paper "Fluctuation without dissipation: Microcanonical Langevin Monte Carlo".

The method is not using minibatches, but instead, each step needs a full gradient, meaning that the cost of Bayesian neural networks is at least 2-3 orders of magnitude higher than using deterministic neural networks. Hence the practicality of the algorithm at this point is questionable.

There was no comparison done with the earlier method "Scaling Hamiltonian Monte Carlo inference for Bayesian neural networks with symmetric splitting" by Cobb et al., who managed to get HMC working with no bias using minibatches at each step, and an accept/reject step. It would be interesting to explore whether such a variant could be extended to Microcanonical LMC.

A major problem is that the implemented algorithm is not clearly described in the paper, and it's not clear whether a Metropolis/Hastings step is used or not, but the authors did not claim they used one so I presume it's not used. The previous paper "Fluctuation without dissipation: Microcanonical Langevin Monte Carlo", (https://arxiv.org/pdf/2303.18221) claims that their Euler-Mayurama discretization (15) exactly preserves the invariant distribution, so there is no need for accept/reject step. The precise form of the implementation of (15) is not stated there either. I am very skeptical that an explicit discretization only using a single gradient evaluation per iteration can exactly preserve the invariant distribution, hence I am on the opinion that this is not a fully explicit scheme, unless the authors convince me otherwise in the rebuttal.

### Questions
State the implemented algorithm precisely, including how many gradient evaluations are used per step, and state whether it preserves the invariant distribution. State whether accept/reject step is needed or not.

How does the method compares with "Scaling Hamiltonian Monte Carlo inference for Bayesian neural networks with symmetric splitting"?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose an adaptation of the Microcanonical Langevin Monte Carlo method for Bayesian Neural Networks.

### Strengths
Clarity:
The paper is clearly written and well-organized.

Quality:
The evaluation is conducted meticulously, with numerous ablations considered. The results effectively justify the proposed method.

### Weaknesses
Novelty:
The paper appears to be an incremental modification of the Microcanonical Langevin Monte Carlo method.

Significance:
Proposing efficient sampling methods for Bayesian Neural Networks is an important problem. However, the main results of the paper are achieved through careful parameter settings, particularly in establishing ensemble methods, tuning size, step size, energy variance scheduler, sample size, and so on. Each of these parameters is known to be crucial for obtaining better results. This makes the paper seem somewhat ad-hoc to me, lacking sufficient significance for developing improved BNN samplers.



### Questions
The authors proposed a set of techniques to adapt the sampler for Bayesian Neural Network solvers. Is my understanding correct that to adapt Microcanonical Langevin Monte Carlo to BNNs, all we need to do is configure the parameters of the MCLMC and treat it as an ensemble method to reduce initialization error?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper adapts the MCLMC algorithm to sample from BNN posteriors. The authors propose a series of changes to the 3-stage tuning scheme in the original paper of MCLMC algorithm and name the adapted algorithm MILE. The authors show that by doing these, MILE demonstrates superior predictive performance, improved uncertainty quantification and improved runtime.

### Strengths
1. The paper is clear and detailed in terms of related work and the method.
2. The empirical results look comprehensive and solid.

### Weaknesses
1. The authors claim that their method is “tuning-free”, but in 3.2, several parameters are still tuned. Maybe I misunderstood what the authors mean by “tuning-free”

2. I feel that the author could elaborate more on which of the benefits of MILE mentioned in section 4 is inherited from the MCLMC algorithm, and which of them result from the authors’ adaptation. 

Minor:
1. The acronym ESS first appear in 3.2.3 without any explanation

### Questions
1. What is d in $(d-1)^{-1}$ in Eq. 3?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a Microcanonical Langevin Ensemble (MILE) approach which adapts the MCLMC to high-dimensional posteriors common in modern Bayesian deep neural networks (BNN). The paper integrates optimization strategies from deep ensembles to carefully adjust components of MCLMC to make it scalable. Through extensive experiments, the paper shows the superiority of MILE in prediction and UQ on popular benchmarks.

### Strengths
I enjoyed reading the paper. Extensive experiments have been conducted where MILE has shown superior performance compared to its competitors. The main strengths of this paper are –
1.	This paper is a significant step towards scalable full Bayesian inference with deep neural networks.
2.	The paper explains the key contributions clearly.
3.	The paper is well written. The authors presented their approach clearly with an intuitive explanation of the key components. 
4.	The authors presented extensive experiments to support their key claim which is the scalability of their approach for sampling high-dimensional Bayesian posteriors.

### Weaknesses
The paper can significantly improve if the authors can discuss/expand on the following points –
(1)	The paper discusses careful tunings of the components of MCLMC.  An ablation study is needed to understand which adjustments are more important than others. My guess is the main speed-up is due to the warm starting using the DE. However, this demands a proper study.
(2)	The work lacks theoretical justification. However, this is not a critical point for the paper as the authors have presented extensive experiments in support of their key claims. However, a discussion related to the convergence of the approach can improve the paper.   
(3)	The numerical section seems to be lacking more competitive methods. “Path-Guided Particle-based Sampling” (ICML 24) can be another competitor approach that is proven to draw efficient samples from multi-modal Bayesian posteriors.

### Questions
In the “Performance results” paragraph the last sentence claims that “It is noteworthy that this is a big step for sampling-based inference, yielding a time complexity comparable to DE, while providing better and more principled uncertainty measures.” However, the time measured is on top of the DE fit as claimed in the caption of Table 1. Then the total time for MILE should be twice of DE. Please clarify.

### Soundness
3

### Presentation
3

### Contribution
3
