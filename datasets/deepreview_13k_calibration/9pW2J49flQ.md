# DeepLTL: Learning to Efficiently Satisfy Complex LTL Instructions

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Linear temporal logic (LTL) has recently been adopted as a powerful formalism for specifying complex, temporally extended tasks in reinforcement learning (RL). However, learning policies that efficiently satisfy arbitrary specifications not observed during training remains a challenging problem. Existing approaches suffer from several shortcomings: they are often only applicable to finite-horizon fragments of LTL, are restricted to suboptimal solutions, and do not adequately handle safety constraints. In this work, we propose a novel learning approach to address these concerns. Our method leverages the structure of B\"uchi automata, which explicitly represent the semantics of LTL specifications, to learn policies conditioned on sequences of truth assignments that lead to satisfying the desired formulae. Experiments in a variety of discrete and continuous domains demonstrate that our approach is able to zero-shot satisfy a wide range of finite- and infinite-horizon specifications, and outperforms existing methods in terms of both satisfaction probability and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a method that leverages linear temporal logic (LTL) to formulate reinforcement learning (RL) tasks. The authors claim that their method is applicable to infinite-horizon tasks and are non-myopic. The preliminaries and problem setting are presented in a clear and logical flow, and the experimental results are well-reported. However, the authors seem to have completely missed highly relevant literature in this area (see references below).

### Strengths
1) The paper presents an interesting approach to learn policies to satisfy omega-regular specifications based on visiting accept states in an automaton without discounting states between the visits. 
2) It incorporates policies parameterized as neural networks.
3) It uses the structure of the automaton specification.

### Weaknesses
The main weakness of this paper is that it ignores significant body of literature that deals with training policies for omega-regular objectives. Without a detailed comparison, it is difficult to evaluate the novelty in this paper. In fact, the technique of discounting seems quite similar to the zeta parameter used in the Hahn et al. paper from TACAS 2019. The authors should clarify how their approach is different.

References:
1. Hahn, E. M., Perez, M., Schewe, S., Somenzi, F., Trivedi, A., & Wojtczak, D. (2019, April). Omega-regular objectives in model-free reinforcement learning. In International conference on tools and algorithms for the construction and analysis of systems (pp. 395-412).
2. Hahn, E. M., Perez, M., Schewe, S., Somenzi, F., Trivedi, A., & Wojtczak, D. (2020). Faithful and effective reward schemes for model-free reinforcement learning of omega-regular objectives. In Automated Technology for Verification and Analysis: 18th International Symposium, ATVA 2020, Hanoi, Vietnam, October 19–23, 202
3. Le, Xuan-Bach, Dominik Wagner, Leon Witzman, Alexander Rabinovich, and Luke Ong. "Reinforcement Learning with LTL and $\omega $-Regular Objectives via Optimality-Preserving Translation to Average Rewards." arXiv preprint arXiv:2410.12175 (2024).
4. Hahn, E. M., Perez, M., Schewe, S., Somenzi, F., Trivedi, A., & Wojtczak, D. (2021). Mungojerrie: Reinforcement learning of linear-time objectives. arXiv preprint arXiv:2106.09161.

### Questions
Questions:
1) In section 4.2 and 4.3, the explanation of the sequence module, which encodes reach-avoid sequence, is unclear. What are the inputs and the outputs of this module?  Could you provide an example to clarify?
2) Why did you use an RNN? Transformer-based NN architectures outperform RNNs in many problems.
3) In section 4.5, the statement “the value function is a lower bound of the discounted probability of reaching an accepting state k times via…” does not sound correct. How is the right hand side of the inequality equal to “the discounted probability of reaching an accepting state k times” ? Can you explain your reasoning? 
4) GCRL-LTL also works for infinite-horizon tasks. The experiment results imply that your method outperforms GCRL-LTL. Is there a theoretical explanation for why your method is better than GCRL-LTL? 
5) It is difficult to evaluate the novelty of this paper without a thorough comparison to approaches such as those used in the tool Mungojerrie [4]. Will such a comparison be possible in a short time?

(See further questions in the post-rebuttal review)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose a multi-task RL approach using goals specified in Linear Temporal Logic. The approach builds on recent work by reasoning about *accepting cycles* in the form of reach-avoid sequences and learns a goal-conditioned policy that can generalize to unseen specifications by finding the highest-valued reach-avoid sequence in the new specification('s automata), where the reach-avoid sequence goals are cast as learned embeddings. The approach is trained in a multi-task setting with a simple curriculum, and experimental results demonstrate that the DeepLTL approach outperforms previous approaches to goal-conditioned LTL-modulo-RL.

### Strengths
* The paper is overall well-written and nicely constructed. 
* The problem of multi-task RL is, in my opinion, one of the most salient applications of using structured logical specifications. I think the paper does a nice job of trying to extend this.
* The paper does a god job contextualizing some of the recent theory (e.g. regarding the eventual discounting objective) and discussing the relevance of it in a practical context.
* The idea of using embeddings, cyclical acceptance, and predicate-conditioned learning builds directly on recent work [1] [2] [3] and I think these principles are helpful in the aim to scale automata-driven RL further to large scale applications.

[1] Compositional Automata Embeddings for Goal-Conditioned Reinforcement Learning. Yalcinkaya et. al 2024.

[2] LTL-Constrained Policy Optimization with Cycle Experience Replay. Shah et. al 2024.

[3] Instructing Goal-Conditioned Reinforcement Learning Agents with Temporal Logic Objectives. Qiu et. al. 2023

### Weaknesses
Although building on very recent work is a good way to step the field forward, it does also beg a bit the question of significance. This work bears strong similarities to [3], with the primary change being to condition over reach-avoid sequences rather than individual atomic propositions or predicates that represent transitions within an automaton. The latter approach, which is what is done in [3], requires a planning-based approach each time a new automaton is seen. The authors do compare against [3] experimentally, and show that on individual challenging tasks their approach is better, which is appreciated. However, I'd like to see a more thorough experimental analysis of the DeepLTL approach itself. Since the DeepLTL approach is quite similar to prior work, this analysis-style work would greatly benefit the field. At what level of complexity of specification does the approach break down? Does a larger alphabet (and therefore a larger class of reach-avoid sequences) make the problem harder by expanding the space of possible embeddings?

Regarding the writing: I don't think including the discussion on eventual discounting [4] (problem 3.1 and theorem 3.1) is totally necessary and the small extension of the theory that the authors provide is more or less orthogonal to their main contribution, which obscures the writing a bit. The authors use a discounted version of LTL as their objective but do not cite recent work that thoroughly explores this problem setting [5]. In section 4.1, the authors discuss reasoning over pre-computed accepting cycles, which bears strong similarities to an identical approach in [2]. Although [2] is cited it would be good for the authors to mention it in section 4.1 given these similarities.

Lastly, the approach from [1] is a highly similar approach to automata-goal-conditioned RL that also uses an embedding based approach. Although this work is contemporaneous, a previous version did appear [6] earlier and I think some sort of comparison, if not an explicitly direct one, would be important in strengthening this work.

### Questions
* Can the authors compare against [1]/[6] in the previous section(s) and reason about why their approach may be preferable? The approaches are different in how they condition and compute embeddings but an argument by the authors advocating their own approach is important given the similarity of the work.
* The authors include a curriculum-based ablation in the appendix that supports the presence of a curriculum. What other choices of curricula were considered? Do the authors have ideas on how a choice of curriculum would affect learning? 
* Section D.3 in the appendix seems to be missing. Can the authors provide this?
* At what level of complexity of specification does the deepLTL approach break down? Does a larger alphabet (and therefore a larger class of reach-avoid sequences) make the goal-conditioned RL problem harder by expanding the space of possible embeddings?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel approach, called DeepLTL, to address the challenge of learning policies that ensure the satisfaction of arbitrary LTL specifications over an MDP. This approach reduces the myopic tendencies found in previous works by representing each specification as a set of reach-avoid sequences of truth assignments. It then leverages a general sequence-conditioned policy to execute arbitrary LTL instructions at test time. Extensive experiments demonstrate the practical effectiveness of this approach.

### Strengths
The proposed approach is tailored to address key challenges of quality, clarity, and significance. Unlike existing techniques, this method is designed to handle infinite-horizon specifications and mitigate the non-myopic tendencies of previous approaches that often lead to sub-optimality. Additionally, it naturally incorporates safety constraints, represented through negative assignments, to guide the policy on propositions to avoid, which is an essential concept for effective planning. In general, the paper is well-written and effectively presented.

### Weaknesses
The approach proposed by the authors is compelling and aims to address an important problem. However, one concern is that the authors appear unaware of works like [1], [2], and [3], which introduced model-free reinforcement learning (RL) methods to tackle the same challenge of maximizing the probability of satisfaction for LTL specifications, expressed as Büchi automata and deterministic parity automata. These methods have even been extended to nondeterministic, adversarial environments (expressed as stochastic games) where nonrandom actions are taken to disrupt task performance, beyond standard MDPs. In such approaches, the LTL specifications are translated into limit-deterministic Büchi automata (LDBAs) to form product MDPs. Rewards are derived from automata using a repeated reachability acceptance condition, allowing controller strategies that maximize cumulative discounted rewards to also maximize satisfaction probabilities; standard RL algorithms are then used to learn these strategies. In my opinion, these results appear to weaken the authors’ claim that ‘Our method is the first approach that is also non-myopic, as it is able to reason about the entire structure of a specification via temporally extended reach-avoid sequences.’ Please discuss how your approach compares to and differs from the methods in [1], [2], and [3], with particular attention to handling non-myopic reasoning and addressing infinite-horizon specifications.

### Questions
The examples provided by the authors are all based on 2D grid-world environments. To evaluate the approach's performance in higher-dimensional settings, it would be valuable to experiment with environments like the 5-dimensional Carlo environment from [1], as well as other high-dimensional settings, such as the Fetch environment in [2], as utilized in [3]. Additionally, as a minor note, there is a typo on line 066 of the paper; it should read (c) instead of (b).

[1] Cameron Voloshin, Abhinav Verma, and Yisong Yue. Eventual Discounting Temporal Logic Counterfactual Experience Replay. In Proceedings of the 40th International Conference on Machine Learning, pp. 35137–35150. PMLR, July 2023. 

[2] M. Plappert et al., “Multi-goal reinforcement learning: Challenging robotics environments and request for research,” 2018, arXiv:1802.09464.

[3] Learning Optimal Strategies for Temporal Tasks in Stochastic Games Alper Kamil Bozkurt , Yu Wang , Michael M. Zavlanos , and Miroslav Pajic

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a reinforcement learning based policy synthesis method for a robot to satisfy a Linear Temporal Logic (LTL) specification. The salient features that distinguish this paper from prior work are the following: (1) the proposed method does not aim to generate a policy for a fixed LTL formula but rather to deal with any arbitrary one, (2) it can deal with specifications that can be satisfied only through infinite length execution,  and (3) it ensures the satisfaction of the safety requirements, and (4) it optimizes the length of the trajectory. The proposed method is based on the observation that the satisfaction of a specification primarily depends on the loops including the final states in the Buchi automaton equivalent to the given specification. For a given LTL formula, the sequence of the sets of actions that lead to the satisfaction and violation of the specification is identified and the policy is trained based on those sequences. On the test time, the policy for the target LTL formula can utilize the policy learnt based on many different LTL specifications and thus the learnt policy can be used in a zero-shot manner. The authors evaluate their method on three benchmark environments and compare it with two baselines. Experimental results establish the proposed method to be superior to the state-of-the-art methods both in terms of the rate of success in satisfying the test specifications and the optimality of the length of the trajectories.

### Strengths
This paper improves the state-of-the-art for reinforcement learning with LTL specifications in several directions. Unlike the earlier methods, the proposed technique can deal with arbitrary LTL specifications at test time, supports infinite-horizon LTL specifications, ensures the satisfaction of the safety constraints, and attempts to optimize the trajectory length. Thus the technical contribution of the paper is significant.

The experimental evaluation is quite exhaustive, establishing the efficacy of the proposed method compared to the state-of-the-art.

### Weaknesses
The presentation in some parts of the paper could be improved. Specifically, a running example could help understand several complex ideas. For example, Section 4.2 could be easier to understand had an example been provided. Similarly, the paragraph on representing the reach-avoid sequence on page 6 could also be accompanied by an example. Furthermore, an example of how the negative assignments help could help convince readers about their necessity.

In Example 1, why can’t we replace the transition on $\epsilon_{q_2}$ by a transition on the action $a$ to generate an equivalent Buchi automata?

In Line 252, in $\delta(q_i, a) \ne q_i$, wouldn’t the second $q_i$ be $q_{i+1}$?

Is it not the case that restricting the actions in the set $A_i^+$ will ensure that the actions are not from the sets $A_i^-$?  These two sets appear to be mutually exclusive. Then why do we need to keep track of both?

Some of the terms used in the paper have never been introduced. For example, what is $sup(\xi)$? How to interpret $\tau \sim \pi | \varphi$?

On Line 107, please use $\equiv$ instead of “=“ to denote formula equivalence.

### Questions
In Example 1, why can’t we replace the transition on $\epsilon_{q_2}$ by a transition on the action $a$ to generate an equivalent Buchi automata?

In Line 252, in $\delta(q_i, a) \ne q_i$, wouldn’t the second $q_i$ be $q_{i+1}$?

Is it not the case that restricting the actions in the set $A_i^+$ will ensure that the actions are not from the sets $A_i^-$?  These two sets appear to be mutually exclusive. Then why do we need to keep track of both?

Some of the terms used in the paper have never been introduced. For example, what is $sup(\xi)$? How to interpret $\tau \sim \pi | \varphi$?

On Line 107, please use $\equiv$ instead of “=“ to denote formula equivalence.

### Soundness
3

### Presentation
3

### Contribution
4
