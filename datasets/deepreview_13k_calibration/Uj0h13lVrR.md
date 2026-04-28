# KL DIVERGENCE OPTIMIZATION WITH ENTROPY- RATIO ESTIMATION FOR STOCHASTIC GFLOWNETS

- Decision: Reject
- Avg Score: 1.00
- Scores: 1, 1

## Abstract
This paper introduces a novel approach for optimizing Generative Flow Networks (GFlowNets) in stochastic environments by incorporating KL divergence objectives with entropy-ratio estimation. We leverage the relationship between high and low entropy states, as defined in entropy-regularized Markov Decision Processes (MDPs), to dynamically adjust exploration and exploitation. Detailed proofs and analysis demonstrate the efficacy of this methodology in enhancing mode discovery, state coverage, and policy robustness in complex environments.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
GFlowNets are a powerful tool for producing diverse generative distributions in a sequential manner. However, they generally only work well in deterministic domains. This paper describes a method to train GFlowNets to produce diverse outcomes in stochastic domains, by incorporating a measure of entropy into the GFlowNet’s objective function, specifically into the “detailed balance” computation.

### Strengths
The problem this paper seems to try to address is an important one, since deterministic domains is a restrictive assumption and GFlowNets are a promising method.

### Weaknesses
I have had a very difficult time in general trying to figure out what this paper is trying to do. Many equations do not seem to make sense, or important terms are left under-defined. Variables are used before they are introduced. In general, I thought this paper was extremely disorganized, to the extent that I have a hard time even understanding what the contribution is. There is far too little information about the method in this paper to reproduce this work, which is the standard we should be aiming for.

Here is a list of things that confused me, or mistakes in presentation
* My biggest concern by far is, I have no idea what $H_{high}$ or $H_{low}$ means. What is a “density  related to high and low entropy states”? It seems the paper hinges on equation 3, but the terms in it are not defined, as far as I can tell.
* The algorithm figure is confusingly structured. For example, s_{t+1} on line 10 is “out of scope”. Should it be in the while loop above? Where is reward R(s_{t+1}) used? Most of all, line 15 (“adjust gamma to balance exploration and exploitation”) is extremely imprecise and does not tell the reader much.
* Section 7 is titled “impact of gamma and alpha”, but alpha is not concretely defined until section 8.1.1. Is it the same alpha? The writing on that specifically is very unclear.
* The abstract positions this paper as important because it can handle environments that are stochastic by nature, but the writing in section 7 presents stochasticity as a parameter to tune. I found this confusing.
* Related to above, none of the domains in this paper are inherently stochastic. This paper would make a stronger case if it highlighted a real problem for which existing methods were insufficient.
* A small thing: the alpha-randomness is misattributed to Machado et al – that paper introduces sticky actions, which are completely different.
* The graphs have many imperfections as well. Why do some graphs in figure 2,3,4 have different lines than others (e.g. missing PPO)? Also, there should be a Y axis label. Furthermore, the same color should always correspond to the same method. Finally, all the text in the graphs is far too small, it’s unreadable without zooming.
* The abstract promises detailed proofs, but there are no proofs in this paper.
* Equations 3 and 7 are the same? Furthermore, equation 3 has s_t, a_t on the left but not on the right – how are they equal? 
* Equation 4 should be w.r.t. Some distribution, right?
* There is no information on the learning architectures used, hyperparameters, or anything one would need to recreate these experiments. 
* I generally don't understand equation 9 -- what are we summing over?

### Questions
See weaknesses for a complete list. Most urgently, what are $H_{high}$ and $H_{low}$? Is $\gamma$ tuned in any interesting way, or just a hyperparameter?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The authors proposed a method to solve the stochastic GFlowNet problem by replacing the dynamics of the stochastic environment with an entropy ratio. This method's essential property is an additional degree of freedom to address the exploration-exploitation trade-off. The technique was empirically evaluated on Hypergrid and TFBind-8 environments with additional stochasticity and was shown to outperform the baselines.

### Strengths
- The authors address the challenging problem of training a GFlowNet model in a stochastic environment; the approach looks novel.

### Weaknesses
 - I doubt the method's theoretical justification based on equation 3. In particular, there is no explanation of what all the quantities on the right-hand side of this equation mean or why this equation holds. Even with the equation, the authors did not prove that the marginal distribution over terminal states matches the reward function, which is the goal of any GFlowNet problem. The core issue is the lack of a clear derivation or intuitive explanation for why replacing the stochastic transition dynamics with an entropy ratio is a valid operation. The paper does not clarify how this substitution preserves the fundamental properties of a Markov Decision Process, specifically how the probability mass is conserved and how the resulting distribution relates to the true environment dynamics. Furthermore, the paper does not address the potential for this substitution to introduce bias or instability in the learning process.
- The experimental setup is very toyish: for both problems, the state set can be enumerated (TFBind-8 terminal state space size is only 20^8), and the problem can be solved without any functional approximation. The motivation under the stochastic GFlowNet problem is unclear. Is there any large-scale motivational example where the stochastic aspect is essential? The experiments lack complexity and do not demonstrate the method's scalability or applicability to real-world problems. The use of small, enumerable state spaces raises concerns about the generalizability of the results. The paper should include experiments on more complex, high-dimensional environments where functional approximation is necessary to demonstrate the practical value of the proposed method. The lack of a compelling motivational example further weakens the impact of the work.
- No comparisons with stochastic GFlowNet setting by (Jiralerspong et al. 2024);
- The plots are very hard to read, especially because the colors of all lines change.

### Questions
- Could you provide any justification for why Equation 3 holds? Replacing the transition dynamics with the entropy ratio is the most crucial part of the paper. However, it is unclear why it is possible since the dynamics are defined by the environment, not by the algorithm. Additionally, I cannot understand does the expression of probability in (3) satisfy the properties of probability distribution (sum over all possible $s_{t+1}$ is equal to 1) and why the right-hand side does not depend on $(s_t, a_t)$
- What is $H_{high}$ and $H_{low}$? They are very important quantities that are not defined anywhere in the paper.
- Is there any natural example of a stochastic environment for the GFlowNet problem? In particular, the stochasticity was added artificially by uncontrollable $\alpha$-greedy exploration for both demonstrated tasks.

### Soundness
1

### Presentation
1

### Contribution
1
