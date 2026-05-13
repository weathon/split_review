# Optimal Sample Complexity for Average Reward Markov Decision Processes

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
\par We resolve the open question regarding the sample complexity of policy learning for maximizing the long-run average reward associated with a uniformly ergodic Markov decision process (MDP), assuming a generative model. In this context, the existing literature provides a sample complexity upper bound of $\widetilde O(|S||A|\tmix^2 \epsilon^{-2})$\footnote{The $\widetilde O, \widetilde \Omega, \widetilde\Theta$ hide log factors.} and a lower bound of $\Omega(|S||A|\tmix \epsilon^{-2})$.  In these expressions, $|S|$ and $|A|$ denote the cardinalities of the state and action spaces respectively, $\tmix$ serves as a uniform upper limit for the total variation mixing times, and $\epsilon$ signifies the error tolerance. Therefore, a notable gap of $\tmix$ still remains to be bridged. Our primary contribution is the development of an estimator for the optimal policy of average reward MDPs with a sample complexity of $\widetilde O(|S||A|\tmix\epsilon^{-2})$. This marks the first algorithm and analysis to reach the literature's lower bound. Our new algorithm draws inspiration from ideas in \cite{Li2020_generator_optimal}, \cite{jin_sidford2021}, and \cite{wang2023optimal}. Additionally, we conduct numerical experiments to validate our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper resolves the issue of sample complexity associated with maximizing the long-term average reward dictated by a uniformly ergodic Markov Decision Process (MDP), predicated on the assumption of a generative model. The findings of this study enhance the pre-existing results by a factor of $t_{mix} and align with the established lower bound. The algorithm introduced herein is a synthesis of the methodologies proposed by Jin & Sidford (2021) and Li et al. (2020).

### Strengths
1. The paper addresses a significant issue in the domain of Markov Decision Processes, providing a solution to the sample complexity associated with maximizing the long-term average reward. This is a valuable contribution that could potentially advance understanding and application in this area.
2. By enhancing pre-existing results by a factor of the mixing time and aligning with the established lower bound, the paper provides a comparative analysis that underscores the improvements made and the relevance of the studies.
3. This paper is well-written and easy to understand.

### Weaknesses
1. The algorithm is primarily a synthesis of methodologies from Jin & Sidford (2021) and Li et al. (2020). While this approach has its merits, the novelty of this paper is somewhat limited given its dependence on previous works. Specifically, the paper does not sufficiently articulate the novel algorithmic contributions beyond combining existing techniques. The core components appear to be derived from prior work, making it difficult to ascertain the unique insights introduced in this paper.
2. The paper could be enhanced by placing greater emphasis on the challenges addressed by the study and the innovative aspects of the proposed algorithm. Currently, the explanation of the problem's inherent difficulties and how the proposed method overcomes them is not sufficiently detailed. Highlighting these elements would help to showcase the unique contributions of the paper and further establish its significance in the field. The paper needs to more clearly demonstrate how the proposed algorithm addresses the specific challenges, and what makes it different from existing methods.

### Questions
1. The paper could benefit from a greater emphasis on the challenges addressed by the study. Could you provide more information on the specific challenges inherent to the problem you are solving and how your approach effectively addresses these issues? 
2. Could you please elaborate on the unique aspects of your algorithm and how it distinctly contributes to the field beyond the synthesis of methodologies from Jin & Sidford (2021) and Li et al. (2020)? Highlighting the novel components of your approach could significantly strengthen the impact of your paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors presents the sample complexity result for the average-reward Markov Decision Processes (AMDPs) under the assumption of ergodicity and with an access to a simulator. This sample complexity is nearly minimax optimal in the class of ergodic MDP, thus closing the gap in mixing time or desired accuracy that appears in previous works. The presented algorithm is basically applies the reduction technique from AMDP to DMDP and efficiently exploits ergodicity assumption in the DMDP setup.

### Strengths
- First minimax optimal guarantees for AMDPs under a generative model assumptions;
- As a byproduct, authors provide minimax optimal  for ergodic DMDPs
- Computationally feasible algorithm;
- Simplicity of the presented approach.

### Weaknesses
 - All the main instruments has already introduced in other papers, and thus this paper may lack of novelty.
    - Reduction of AMDP to DMDP is presented in (Jin & Sidford, 2021)
    - Optimal rates with optimal warm-up are presented in (Li et al. 2020);
    - Rates for mixing DMDP are already presented in (Wang et al. 2023) (specifically, Proposition 6.1 and Corollary 6.2.1);



### Questions
- What are main barriers to provide an algorithm with dependence not on a mixing time-type quantity but on span of optimal value? This questions has its importance because it is know that this guarantee will be strictly tighter than mixing dependent.
- Is it possible to provide an algorithm without a reduction to discounted setting?
- Is it possible to extend this approach to exploration setup and provide a feasible algorithm with guarantees like (Orther, 2020)?

Ortner, Ronald. "Regret bounds for reinforcement learning via markov chain concentration." *Journal of Artificial Intelligence Research* 67 (2020): 115-128.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors considered the sample complexity of average reward MDPs under the uniformly ergodic condition, and provided a novel analysis for the algorithm given in Li et al. 2020, which results in an upper bound that matches the known lower bound.

### Strengths
1. Theoretical paper that gives a matching bound, therefore fully establishing the optimal sample complexity for AMDP under the uniform ergodicity condition.
2. The background was explained clearly, and the context of the result to other related settings is also well explained.
3. In most places, the notations and proofs are done rigorously, more so than the average papers.

### Weaknesses
1. The result is somewhat thin in the sense that it feels like filling a small gap that was somehow overlooked by several previous groups of researchers, though I personally like the cleanness of the result. 
2. The main contribution is technical, yet the main paper does not really spend the effort to clearly explain the technical critical point that enables the authors to establish the bound. Particularly, it appears Proposition A.1 is the critical step to establish the concentration inequality. More discussion on the technical level on the difference with previous bounds should be given.
3. I'm a little confused about some notation. Is alpha in (2.6) in R^|S|? It should be, but later in the definition of \bar{alpha}, we need to choose the maximum alpha, which seems incorrect since it is a vector. 
4. Equation (2.4), where is \eta defined? It seems to appear without any context. 
5. Can you comment on the choice of distribution of Z(s,a)? Does it make a difference if another distribution (non-uniform) is used?
6. Though I can understand the result is theoretical, have the authors used any numerical results to verify the optimal algorithm behavior that suggests the sample complexity scaling?

### Questions
1. I'm a little confused about some notation. Is alpha in (2.6) in R^|S|? It should be, but later in the definition of \bar{alpha}, we need to choose the maximum alpha, which seems incorrect since it is a vector. 
2. Equation (2.4), where is \eta defined? It seems to appear without any context. 
3. Can you comment on the choice of distribution of Z(s,a)? Does it make a difference if another distribution (non-uniform) is used?
4. Though I can understand the result is theoretical, have the authors used any numerical results to verify the optimal algorithm behavior that suggests the sample complexity scaling?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the sample complexity of learning the optimal policy in average-reward Markov decision processes, under the assumption of a uniformly ergodic MDP and a generative model. The proposed algorithm improves the best sample complexity upper bound in existing works and matches the lower bound of the problem. This is achieved by combining the algorithmic ideas of two lines of existing research, by first reducing the AMDP to a discounted-reward MDP and then establishing an optimal sample complexity upper bound in the setting of uniformly ergodic discounted MDPs.

### Strengths
This paper studies an important problem in reinforcement learning theory. It closes the gap between the upper and lower bounds of the sample complexity for learning an optimal policy. The technical proofs look solid as far as I can tell. The presentation of the algorithm and analysis is also clear.

### Weaknesses
As the authors have mentioned in the paper, the algorithm is developed by combining the algorithmic ideas from two lines of existing research (Jin & Sidford, 2021) and (Li et al., 2020). While in general we would hope to see technical novelty in terms of algorithm design, it is probably okay with this work because reducing to a discounted MDP (Jin & Sidford, 2021) seems to be a standard approach, and the authors do make improvements over the analysis of (Li et al., 2020) to establish a sharper sample complexity upper bound. 

Even though I understand that the main contributions of this work are theoretical, I would still hope to see some numerical results to demonstrate some of the ideas in the paper.

### Questions
Does your work imply any new results for the case where the uniform ergodicity assumption does not hold, such as the weakly communicating AMDP setting?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
