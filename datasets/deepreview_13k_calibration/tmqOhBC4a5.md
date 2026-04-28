# Maximum Entropy Heterogeneous-Agent Reinforcement Learning

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
\vspace{-3mm}
\emph{Multi-agent reinforcement learning} (MARL) has been shown effective for cooperative games in recent years. However, existing state-of-the-art methods face challenges related to sample complexity, training instability, and the risk of converging to a suboptimal Nash Equilibrium. In this paper, we propose a unified framework for learning \emph{stochastic} policies to resolve these issues. We embed cooperative MARL problems into probabilistic graphical models, from which we derive the maximum entropy (MaxEnt) objective for MARL. Based on the MaxEnt framework, we propose \emph{Heterogeneous-Agent Soft Actor-Critic} (HASAC) algorithm. Theoretically, we prove the monotonic improvement and convergence to \emph{quantal response equilibrium} (QRE) properties of HASAC. Furthermore, we generalize a unified template for MaxEnt algorithmic design named \emph{Maximum Entropy Heterogeneous-Agent Mirror Learning} (MEHAML), which provides any induced method with the same guarantees as HASAC. We evaluate HASAC on six benchmarks: Bi-DexHands, Multi-Agent MuJoCo, StarCraft Multi-Agent Challenge, Google Research Football, Multi-Agent Particle Environment, and Light Aircraft Game. Results show that HASAC consistently outperforms strong baselines, exhibiting better sample efficiency, robustness, and sufficient exploration.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the problem of co-operative Multi-Agent Reinforcement Learning, where issues of sample complexity, training instability, and sub-optimal exploration affect leading methods. The authors propose a method for learning stochastic policies to overcome these limitations, by drawing a connection with Graphical models and deriving a familiar Maximum Entropy solution optimization approach.

The paper is well written, seems comprehensive in it's theoretical establishment of the new method, and thorough in the range of depth of empirical evaluations.

I am familiar with single-agent RL (and have a background in Inverse Reinforcement Learning theory), however am only tangentially aware of work in the multi-agent RL setting. As such, I may have overlooked details or not been aware of relevant prior work when reviewing this paper. I have read the paper, and skimmed the appendices, however did not do a detailed check of the proofs.

### Strengths
* Well written, easy to follow the argument development. Seems to engage thoroughly with prior work.
 * Empirical evaluations are strong, and results support the conclusions

### Weaknesses
 * The contribution of the method in part hinges on the limitations induced by the 'IGO' assumption from prior work (Sec 2, p2), but this is never elaborated on in the paper. Can you define IGO more clearly and explain exactly what limitations this assumption introduces? This will help the reader not intimately familiar with MARL.
* The proposed methods introduces hyper-parameters, notably the temperature term $\alpha$ and the drift functional and neighborhood operator. However any alternate method will also have hyper-parameters, so this isn't a big drawback. Some elaboration of the 'automatically adjusted' $\alpha$ schedule (citation #9) just before the heading for Sec. 6 might be helpful for the reader here. Specifically, it would be useful to understand how this adjustment is coupled to the learning dynamics, and what guarantees this provides in terms of convergence or stability.


### Questions
# Questions and comments

* It seems the design of the drift functional and neighborhood operators will be key to the success of the proposed HASAC, or MEHAML based methods (as you note in Sec. 6). Can you provide any comment on what factors should be taken into consideration in the construction of these terms? E.g. in what ways will this depend on the nature or definition of the MARL task? Some discussion of the design/selection of these terms for your empirical experiments might be helpful here.
 * The core method (e.g. end of Sec.4 on p7) seems to have high-level similarities to PPO methods for single-agent RL (e.g. constraint to keep the policies from drifting too far) - do you see any connection to this family of methods? Is this something that could be explored further in the literature or has been already?
 * The notion of Quantal Response Equilibrium is key to this optimization objective, but I'm not familiar with this term. You provide a citation (#20, also #6), but the paper would be strengthened with a little bit more explanation of this notion in Sec 4.1. E.g. can you give some intuition for what this objective means in practice compared to regular Nash Equilibrium? In what situations is QRE to be preferred over NE?
 * What is the $\omega$-limit (Point 4 in Theorem 3) - I could not find a definition and am not familiar with this terminology.

# Minor and grammatical points

 * Under heading 5.1 - '2 hundred' - could write as '200'
 * There are a lot of acronyms in this paper - please consider adding a table of acronym definitions in the appendix to aid readers.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a novel algorithm, Heterogeneous-Agent Soft Actor-Critic (HASAC), based on the Maximum Entropy (MaxEnt) framework. The paper theoretically proves the monotonic improvement and convergence properties of HASAC to a quantal response equilibrium (QRE). The authors also introduce a generalized template, Maximum Entropy Heterogeneous-Agent Mirror Learning (MEHAML), which provides any induced method with the same guarantees as HASAC. The proposed methods are evaluated on six benchmarks, demonstrating superior performance in terms of sample efficiency, robustness, and exploration.

### Strengths
1. The paper is well-structured and clearly written, making it easy to follow the authors' line of thought.
2. The authors provide a comprehensive theoretical analysis of the proposed methods, including proofs of monotonic improvement and convergence to QRE.
3. The proposed methods are evaluated on a variety of benchmarks, demonstrating their versatility and effectiveness.

### Weaknesses
1. The novelty of the paper is limited, as the main contribution is the application of the Soft Actor-Critic (SAC) algorithm to the multi-agent setting.
2. The authors should have tested their method in scenarios where sample efficiency is crucial (such as real robots, stock exchange, etc), given that their proposed method is off-policy.
3. The validity of the experimental results is questionable. The training curves show significant fluctuations, and the authors only present a selection of results in the main paper, which may give a biased view of the method's performance.
4. The authors should provide more comprehensive experimental results, including results from a larger number of seeds, to fully demonstrate the effectiveness of their method.

### Questions
1. Could the authors provide more details on how sensitive is the performance of HASAC to the choice of α?
2. How does the proposed method perform in scenarios where sample efficiency is crucial? Could the authors provide experimental results in such scenarios?
3. Could the authors provide more comprehensive experimental results, including results from a larger number of seeds ?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a MaxEnt MARL approach that employs sequential policy updates and uses a centralized Q-function. They provide the representation of QRE policies maximizing the MaxEnt objective of MARL and demonstrate that the joint policy updated through the sequential policy updates converges to the joint QRE policy. The proposed practical algorithm is simple and outperforms the baselines on various benchmarks.

### Strengths
1.	(Theoretical) With the multi-agent soft Q-value function defined in the main paper, the authors demonstrate that through the sequential policy updates, the joint policy converges to a QRE policy while monotonically improving the objectives for the policy and Q-value function.

2.	(Contribution) The authors provide remarkable combinations for the MaxEnt problem of those that exist in previous works; the monotonic improvement and the convergence to a QRE policy for the MaxEnt objective seem to be rigorous, and they extend the MaxEnt MARL problem to the general one with possible constraints.

3.	(Simplicity) The proposed practical algorithm is straightforward. The algorithm doesn’t require recomputing Q-value estimation for the sequential policy updates.

4.	(Experimental) On a bunch of benchmarks, the proposed algorithm consistently achieves superior performance and high sample efficiency, compared to the baselines.

### Weaknesses
1. (Unclear effect of the sequential updates) Although there is an example [1] to show why the sequential policy updates for the standard MARL objective are needed, an example or technical explanation for the MaxEnt MARL objective is also needed. It is because the authors define the multi-agent soft Q-function (eq. (7)) and local policy update (eq. (8)). Also, the practical objective for the policy (eq. (10)) can be reduced to the expectation of $\alpha\log\pi_{\phi_{i_m}}^{i_m}-Q_{\pi_{old}}^{i_{1:n}}$, which is consistent with the pseudocode of HASAC, since the MA soft Q-function consists of the centralized Q-function $Q_{\pi_{old}}^{i_{1:n}}$ and the entropy term of its complementary agents, which is not subject to optimize. So, in the proposed algorithm, the sequential policy update may be just additional sampling actions of some agents. The core issue is that the paper does not clearly articulate why sequential updates are necessary for the MaxEnt objective, given that the policy update appears to be optimizing a similar objective as in a simultaneous update setting, with the multi-agent soft Q-function incorporating a centralized Q-function and the entropy of other agents. The benefit of sequential updates in this specific MaxEnt context is not sufficiently justified, and it's not clear if it's more than just additional sampling.

2. (Sensitive to the entropy temperature) The Ablation study shows that the proposed algorithm may not be robust to the entropy temperature and converge to different policies according to the temperature. In this paper, each domain has a different entropy temperature; one domain has a fixed temperature, and another has an automatic temperature with a fixed target entropy. A more effective method to tune entropy terms is needed, like ADER[2]. The paper's reliance on manual tuning or a fixed target entropy for temperature adjustment is a weakness. The lack of a robust, adaptive mechanism for entropy temperature tuning across different tasks raises concerns about the practical applicability of the proposed algorithm. The sensitivity to temperature and the need for manual tuning or task-specific target entropies suggest a lack of generalizability and robustness.

### Questions
For the weaknesses, could you provide results of MASAC, which is the HASAC without the sequential policy updates, on the benchmarks and the idea of an adaptive entropy temperature tuning method for better exploration?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work addresses cooperative multiagent reinforcement learning (MARL). It builds on the idea of MaxEnt RL, and proposes the maximum entropy heterogeneous-agent reinforcement learning (MEHARL) framework for learning stochastic policies in MARL. On the theoretical/technical side, it uses the PGM to derive the MaxEnt MARL objective, and prove monotonic improvement and QRE convergence properties for the corresponding HASAC algorithm, as well as the unified MEHAML template. On the empirical side, HASAC has been implemented on six benchmark MARL tasks and it achieves the best performance in 31 out of 35 tasks across all benchmarks.

### Strengths
1. Excellent presentation. The methodology is well motivated with an illustrative matrix game example. The related work is well discussed and the contribution of this paper is clear. The paper is overall well structured and easy to follow. 

2. Clear technical contribution. The algorithmic framework MEHAML as well as the specific practical algorithm HASAC are novel and theoreticall grouned with proofs on the nonotonicity improvement and convergence to QRE. The method is not a simple combination of MaxEnt RL and MARL, but the derivation of the MARL version is built on the PGM formulation connecting from the idea of control as an inference task.

3. Superior empirical performance over a wide spectrum of benchmark tasks -- HASAC has been implemented on six benchmark MARL tasks and it achieves the best performance in 31 out of 35 tasks across all benchmarks.

### Weaknesses
I don't see a major weakness.

A minor point: the IGO assumption is not explained when first being introduced. I don't think people outside MARL are familiar with this term.

### Questions
The MEHAML framework (or HASAC) is proved to converge to QRE, but not the optimal NE. But it seems that empirically HASAC does learn a good equilibrium due to the stochastic policies. I am curious if is it possible at all to have some sort of guarantees to reach the optimal NE?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
