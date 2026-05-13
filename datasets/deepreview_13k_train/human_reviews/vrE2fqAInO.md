# Fixed-Budget Differentially Private Best Arm Identification

- Decision: Accept
- Scores: 8, 6, 8, 5, 8

## Abstract
We study best arm identification (BAI) in linear bandits in the fixed-budget regime under differential privacy constraints, when the arm rewards are supported on the unit interval. 
Given a finite budget $T$ and a privacy parameter  $\varepsilon>0$, the goal is to minimise the error probability in finding the arm with the largest mean after $T$ sampling rounds, subject to the constraint that the policy of the decision maker satisfies a certain {\em $\varepsilon$-differential privacy} ($\varepsilon$-DP) constraint. We construct a policy satisfying the $\varepsilon$-DP constraint (called {\sc DP-BAI}) by proposing the principle of {\em maximum absolute determinants}, and derive an upper bound on its error probability. Furthermore, we derive a minimax lower bound on the error probability, and demonstrate that the lower and the upper bounds decay exponentially in $T$, with exponents in the two bounds matching order-wise in (a) the sub-optimality gaps of the arms, (b) $\varepsilon$, and (c) the problem complexity that is expressible as the sum of two terms, one characterising the complexity of standard fixed-budget BAI (without privacy constraints), and the other accounting for the $\varepsilon$-DP constraint. Additionally, we present some auxiliary results that contribute to the derivation of the lower bound on the error probability. These results, we posit, may be of independent interest and could prove instrumental in proving lower bounds on error probabilities in several other bandit problems.
Whereas prior works provide results for BAI in the fixed-budget regime without privacy constraints or in the fixed-confidence regime with privacy constraints, our work fills the gap in the literature by providing the results for BAI in the fixed-budget regime under the $\varepsilon$-DP constraint.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper is the first to study best arm identification (BAI) in linear bandits under a fixed DP budget budget. With extensive research focusing on DP MAB, this paper tries to answer this problem through a different lens of "pure exploration". This work serves as a valuable complement to the current body of literature.

### Strengths
To this end, the paper proposes a policy satisfying $\epsilon$-DP, thus providing an upper bound of the decaying speed of the error probability. The paper also provides an almost-matching lower bound. Empirical evaluation is also provided to show the effectiveness of the algorithm.

### Weaknesses
Although this is a nice work, I still suggest the paper provide more discussion on the connections between this problem to 1) BAI in the fixed-confidence regime, 2) and generally, MAB under DP. I understand superficially speaking they are different problems, but it is not very clear (to me) whether or not there exist some connections  deeper. For example, there might be a simple adaptation of previous algorithms to suit this setting.

### Questions
Please refer to weakness

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the best arm identification (BAI) problem in multi-armed bandits with differential privacy (DP) guarantees. It focuses on the fixed-budget BAI setting, aiming to minimize the error probability of selecting a suboptimal arm within a set number of arm pulls (budget). Notably, the paper introduces DP-BAI, the first algorithm to achieve DP guarantees in the fixed-budget BAI context. This algorithm outperforms a naive approach that directly incorporates a DP mechanism into the existing state-of-the-art non-private BAI algorithm.

### Strengths
This paper introduces the first algorithm to solve the BAI problem within a fixed-budget constraint and under DP guarantees. The paper also offers an extensive theoretical analysis, establishing an upper bound on the error probability for the new algorithm, which is adaptive to the complexity of the problem measured by $H_{BAI}, H_{pri}$. Furthermore, it provides a matching lower bound, demonstrating that the algorithm attains optimal performance in this specific setting.

### Weaknesses
The paper lacks a detailed comparison with existing non-private fixed-budget BAI works. For example, a natural question is: Does the error probability of DP-BAI converge to that of the state-of-the-art non-private counterpart when $\epsilon \to \infty$? Such an analysis would be valuable in understanding the trade-offs between privacy and performance.

Moreover, I personally believe that the writing of this paper, especially in the algorithm description section, could be improved. Currently the presentation has a lot of notations, many without adequate explanations. A more detailed explanation of each notation and some high-level insights would significantly improve the paper's readability and effectively convey the core ideas.

### Questions
- see Weakness 1: How does DP-BAI compare to OD-LinBAI, especially when $\epsilon\to\infty$? 

- Page 4, Definition 3.1: Why is a Max-Det collection of $\mathcal{A}$ always linearly independent raises questions. Does this implicitly assume that $\mathcal{A}$ spans $\mathbb{R}^{d'}$? 

- Regarding Algorithm 1:
  - Lines 8, 14: The phrasing in these lines is confusing and seems inconsistent with earlier descriptions. The term "pull each arm XX times" is ambiguous. From the description, it appears that, in line 8, every arm in $B_p$ is pulled $T'/Md_p$ times, totaling $T'/M$ arm pulls. Meanwhile, in line 14, it seems there are a total of $T'/Ms_p$ arm pulls, with each pull randomly choosing an arm from $A_p$. 
  - Can the authors provide some high-level intuition behind the choice of $g_i$ and $h_i$ as described in equations (5) and (6)?

### Soundness
3 good

### Presentation
2 fair

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
The authors propose and analyze an algorithm for the fixed-budget best-arm identification problem with differential privacy constraints. The algorithm is based on differentially private version of MAX-DET rather than adapting established fixed-budget BAI algorithms. In the appendix the authors provide a general analysis of natural possible extension of one such algorithm and clearly benchmark their algorithm with this extension. The lower bounds also depend on new notions of complexity which incorporate differential privacy as a constraint in policy design.

### Strengths
I think the authors provide fundamental analysis of the problem in terms of the upper and lower bound. The main strength of the contribution is demonstrated by proving that the algorithm matches instance optimal bounds. Further, the algorithm idea is new itself and clearly outperforms existing benchmarks (and straightforward adaptations thereof).

### Weaknesses
I think the paper can be written more intuitively given that it has a lot of parameters. For example, while the algorithm is stated clearly, I am unsure why it works intuitively. What makes the apparent dimension go down for the first few rounds? How does decreasing the span basis vectors of the arm space lead to convergence to the optimal arm.

I am skeptical about their definition of DP since it is defined over length $T$ sequences. I would expect that in the online setting this definition would only be defined over a sample of sequence starting from the time when the reward sequences differ as done in joint differential privacy.

Finally, the central idea of the paper is to use D-optimal design rather than G-optimal design. These ideas are theoretically equivalent (see Proposition~3 in Soare et al. NeurIPs 2014) but  this paper demonstrates a dramatic performance improvement in their numerical experiments. What is the intuitive explanation for this?

### Questions
--
I am skeptical about their definition of DP since it is defined over length $T$ sequences. I would expect that in the online setting this definition would only be defined over a sample of sequence starting from the time when the reward sequences differ as done in joint differential privacy. 

--
I would like an intuitive explanation of why their algorithm works on a small example somewhere in the paper (maybe, in an appendix).

-- 
Finally, the central idea of the paper is to use D-optimal design rather than G-optimal design. These ideas are theoretically equivalent (see Proposition~3 in Soare et al. NeurIPs 2014) but  this paper demonstrates a dramatic performance improvement in their numerical experiments. What is the intuitive explanation for this?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studied the way to adopt differential privacy on the Best Arm Identification policy. The main trick is to append each arm's empirical mean with proper Laplace distribution.

### Strengths
The work provide comprehensive details on establishing its theoretical claims.

### Weaknesses
The empirical evaluation is limited on a particular synthetic data instance.



### Questions
1. Motivation to consider DP-BAI algorithm. For my understanding, DP is for preventing potential privacy risk when sharing statistics of a dataset. I would be great for the author to provide motivation to consider DP in bandit problem, especially on the best arm identification task. 

2. Intuition on scheme (7). I had difficulty to make sense on  the scheme (7) and would be thankful is author can provide explanations.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of identifying the best arm in a differentially private manner. This paper focuses on the pure DP setting. Here, the privacy model is as follows. At each time step T, there are K arms. Each arm has a potential reward x_{t, k}. The algorithm is DP if, changing only one of the x_{t, k} causes the trajectory of arms that are selected to satisfy the usual eps-DP property.

The authors prove tight upper and lower bounds for this problem. In particular, they determine a parameter, similar to the parameter in the non-private setting, which essentially governs the error rate of the algorithm.

### Strengths
This paper studies an interesting problem and will be of interest to researchers working on DP and bandits. The authors also prove tight results so I believe this is a significant contribution to the literature. The writing quality and clarity is good. The lower bound is a nice technical contribution.

### Weaknesses
Unless I misunderstood, two datasets are neighboring if the set of possible rewards differ in only one location. I'm curious what the motivation for this is. For example, if we use clinical trials as the motivating example then each arm may correspond to a different treatment. In this case, I would view two datasets as neighboring if the set of observations differ at one step which could mean that all K arms at a single time step have different rewards. I am curious how this impacts the results of the paper. It seems that the current definition of neighboring datasets is quite restrictive, as it only allows for a single reward to change across all time steps and arms. This raises concerns about the practical applicability of the results, since real-world scenarios often involve more substantial data variations. For instance, in a clinical trial, a change in patient characteristics or measurement protocols could affect the rewards of all treatments at a given time, not just a single reward. This discrepancy between the theoretical model and practical use cases needs further clarification.

### Questions
See weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
