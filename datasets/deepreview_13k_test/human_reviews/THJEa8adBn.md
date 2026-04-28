# Harnessing Density Ratios for Online Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
The theories of offline and online reinforcement learning, despite having evolved in parallel, have \dfedit{begun to show signs of the possibility for a} unification, with algorithms and analysis techniques for one setting often having natural counterparts in the other. However, the notion of \textit{density ratio modeling}, an emerging paradigm in offline RL, has been largely absent from online RL, perhaps for good reason: the very existence and boundedness of density ratios relies on access to an exploratory dataset with good coverage, but the core challenge in online RL is to collect such a dataset without having one to start.

In this work we show---perhaps surprisingly---that density ratio-based algorithms have online counterparts.  Assuming only the existence of an exploratory distribution with good coverage, a structural condition known as \emph{coverability} \citep{xie2022role}, we give a new algorithm (\Alg) that uses density ratio realizability and value function realizability to perform sample-efficient online exploration. \Alg addresses unbounded density ratios via careful use of \emph{truncation}, and combines this with optimism to guide exploration.

\Alg is computationally inefficient; we complement it with a \dfedit{more} efficient counterpart, \HyAlg, for the \emph{Hybrid RL} setting \citep{song2022hybrid} wherein online RL is augmented with additional offline data.
\HyAlg is derived as a special case of a more general meta-algorithm that provides a provable black-box reduction from hybrid RL to offline RL, which may be of independent interest.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The convergence of offline and online reinforcement learning theories has led to the emergence of density ratio modeling in offline RL. However, this concept has been absent in online RL due to the challenge of collecting a comprehensive exploratory dataset. This paper introduces GLOW, an online RL algorithm that can explore and learn efficiently when there is an exploratory distribution with good coverage (coverability condition), even in the presence of value functions and density ratios. GLOW handles unbounded density ratios through truncation and employs optimism for exploration, but it is computationally inefficient. To address this, a more efficient variant called HYGLOW is introduced for Hybrid RL, combining online RL with offline data. HYGLOW is derived from a meta-algorithm called $H_2O$, which offers a provable reduction from hybrid RL to offline RL.

### Strengths
1. The paper is fairly well organized and the problem is well motivated (to analyze the notion of density ratio in online RL). 

2. The theoretical guarantee is solid and the explanation of concepts is also very comprehensive.

### Weaknesses
While the paper primarily delves into theoretical aspects and introduces the GLOW algorithm with statistical guarantees, it's worth noting that GLOW is computationally inefficient. Therefore, there is a need to develop more computationally efficient variants to showcase the algorithm's practical effectiveness.

### Questions
The idea of using density ratios in online RL is new. However, I am still curious about the specific benefits for online RL. Does it enlarge range of MDPs which can be solved by online RL algorithms (it may be computationally inefficient)? What is the advantage of using density ratios for guiding exploration in online RL compared to other classical methods like Upper Confidence Bound ?

### Soundness
4 excellent

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper endeavors to establish a bridge between offline and online reinforcement learning. More specifically, it introduces a novel algorithm named GLOW, which excels at conducting sample-efficient online exploration while assuming the presence of value-function and density-ratio realizability. Furthermore, the authors extend these findings to encompass the hybrid reinforcement learning setting.

### Strengths
This paper is well-crafted, presenting its content in a clear and easily understandable manner. The majority of the results are extensively scrutinized and discussed, adding to the paper's overall quality. The introduction of a new density-based online algorithm effectively bridges the gap between offline and online RL. Furthermore, the paper's concerted effort to tackle the enduring and vital issue of removing the completeness assumption is a critical contribution to the field. This problem has long been a pressing concern in online reinforcement learning and is integral to the significance of this work.

### Weaknesses
- Bypassing the need for strong completeness-type assumptions by introducing an additional density ratio realizability assumption is not a novel approach, particularly in the context of offline reinforcement learning (see [Zhan et al., 2021] and a missing related work [1]). So the results in this work are not very surprising.

- Dentity-based algorithms may not be as suitable for online reinforcement learning, given the perceived strength of Assumption 2.2. While the authors have included two examples in Appendix D.1, these examples are already familiar to us and do not pose a significant challenge. If the authors could provide additional examples, such as those involving low (Bellman) eluder dimension or bilinear class, it would make the results more remarkable. 

[1] Importance Weighted Actor-Critic for Optimal Conservative Offline Reinforcement Learning. Hanlin Zhu, Paria Rashidinejad, Jiantao Jiao

### Questions
see the Weakness part.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides theoretical results adapting the idea of density ratio modeling from offline RL to the setting of online RL and provides sample complexity guarantees for the proposed algorithms. The main contribution of the paper is the algorithm called GLOW which provides polynomial sample complexity bounds in the online RL setting by minimizing the weighted average Bellman error using clipped density ratios along with realizability assumptions in function approximation. To further improve the sample efficiency, authors propose a meta-algorithm H2O that can reuse any offline algorithm to output an online exploration policy in the Hybrid RL setting (i.e. online RL with some available offline data). 



*I would also like to note here that I am perhaps not the target audience of this work and though I am aware of some of the related works on this topic, I may not be the best judge of this paper's contributions.*

### Strengths
1. This paper exhaustively compares to the relevant prior work in the field and positions the contributions of this work with the literature in offline and Hybrid RL. In several parts of the paper, authors intuitively explain some of the challenges faced in adapting the density ratio modeling to online RL and the need for certain regularization formulations to achieve desired approximation error bounds. These add to the readability of the paper. 

2. This paper claims to be the first to provide theoretical guarantees showing that value function realizability and density ratio realizability alone are sufficient for sample-efficient RL under coverability. It is a step towards unifying some of the advances made in offline RL with the requirements of sample-efficient online RL algorithms.

### Weaknesses
While the paper focuses on providing theoretical bounds regarding sample efficiency of the proposed algorithms, it lacks any attempts at empirical verification of the same. Comparing to Song et al. which the authors highlight for introducing the Hybrid RL setting, I would expect similar experiments (eg. Song et al. present experimental results in Montezuma's revenge) in this paper to demonstrate the performance of the theoretically motivated framework in practice. Perhaps it would also help to include a discussion of the practicality of the assumptions made in the theoretical proofs and what, if any, are the challenges of implementing the proposed algorithms in standard RL benchmarks.

### Questions
1. Why did the authors not consider empirical verification of their proposed framework in Sec 4? Is there any understanding of the validity of the assumptions made in the paper when applied to RL algorithms in practice?

2. In the first line on page 4, "that $\frac{d^\pi_h}{d^{\pi'}_h}$ for all ...", is there some missing text after $\frac{d^\pi_h}{d^{\pi'}_h}$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
