# Provable Representation with Efficient Planning for Partially Observable Reinforcement Learning

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
In most real-world reinforcement learning applications, state information is only partially observable, which breaks the Markov decision process assumption and  leads to inferior performance for algorithms that conflate observations with state. Partially Observable Markov Decision Processes (POMDPs), on the other hand, provide a general framework that allows for partial observability to be accounted for in \emph{learning, exploration and planning}, but presents significant computational and statistical challenges. To address these difficulties, we develop a representation-based perspective that leads to a coherent framework and tractable algorithmic approach for practical reinforcement learning from partial observations. We provide a theoretical analysis for justifying the statistical efficiency of the proposed algorithm, and also empirically demonstrate the proposed algorithm can surpass state-of-the-art performance with partial observations across various benchmarks, advancing reliable reinforcement learning towards more practical applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
While Partially Observable Markov Decision Processes (POMDPs) were introduced to address partial information in RL algorithms where full
observability is unavailable, such formulation brings computational challenges in learning, exploration, and planning, due to the non-Markovian dependence between observations. This paper aims to address the computational and statistical challenges in Partially Observable Markov Decision Processes (POMDPs). In particular, the authors develop a representation-based perspective that leads to a coherent framework and tractable algorithm.

### Strengths
This paper studies the problem of designing an efficient and practical RL algorithm for structured partial observations in RL frameworks. Authors introduce a structured POMDP with a low-rank property that allows for a linear representation, called Multi-step Latent Variable Representation (µLV-Rep), which is a counterpart of linear MDP in the POMDP context. As such, this representation overcomes computational barriers and enables a tractable representation of the value function. The extension of linear MDP to POMDP can be beneficial.

The paper also proposes a planning algorithm that can implement both the principles of optimism and pessimism in the face of uncertainty for online and offline POMDPs. 

Theoretical analysis in sample complexity and PAC guarantee are provided to justify the performance guarantee. 

Empirical comparisons are performed to demonstrate the performance on a set of benchmark environments compared to existing SOTA RL algorithms for POMDPs.

### Weaknesses
1. The theoretical analysis relies on quite a few assumptions (including (Finite Candidate Class with Realizability, Normalization Conditions, Regularity Conditions and Eigendecay Conditions), which may not always fulfilled in reality. Can authors comment on the performance of the algorithms when these assumptions break, e.g., how worse the performance is going to be, and which of the assumptions are essential to retain the performance? Specifically, the assumption of a finite candidate class with realizability is quite strong, as it implies that the true latent state representation lies within the chosen function class. This is rarely the case in real-world scenarios, and it would be beneficial to understand how the algorithm behaves when this assumption is violated, and whether there are any graceful degradation properties.

2. The theoretical analysis is mainly based on Ren et al., 2023a. It is unclear what are the technical novelties in the analysis compared to Ren et al., 2023a. Authors are expected to explain the difference and highlight the key insights in the proofs.  In particular, the proof of Theorem 12 is unclear by just claiming "This is a direct extension of the proof of Theorem 9 in Ren et al. (2023a)". The technical contribution in theory remains questionable. It would be helpful to see a more detailed breakdown of the proof, highlighting the specific modifications required to extend the results of Ren et al. to the POMDP setting, and why these modifications are non-trivial.

3. Algorithmically, the proposed main algorithms borrow lots of the elements from Ren et al., 2023a, the novelty appears to be limited. The core algorithmic structure seems to follow a similar pattern, and it is not clear what specific adaptations were made to handle the partial observability aspect of POMDPs. A more detailed explanation of the algorithmic differences and their impact on performance is needed.

4. In section 4, it is unclear how the planning algorithm implements pessimism for offline RL. The description of the pessimism mechanism is vague, and it is not clear how the algorithm ensures that it is exploring in a safe and conservative manner, especially in the offline setting where no new data can be collected. A more detailed explanation of how the pessimism is implemented and how it affects the planning process is required.

5. Can authors comment on the tightness of the sample complexity bounds in Lemma 11? It is not clear whether the sample complexity bounds are tight, and whether there is room for improvement. It would be helpful to understand the factors that contribute to the sample complexity, and whether there are any bottlenecks that can be addressed in future work.

### Questions
See above. In addition, there are some minor grammatical errors in the draft. It is suggested that authors carefully proofread the draft for improvement.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper contributes a new algorithm for RL in structured POMDPs.
It proposes to use a latent variable model to learn a linear representation of the value function in L-step decodable POMDPs.
The proposed approach shows good performance in a large set of tasks when compared with baselines.

### Strengths
- The work is highly relevant for the RL community, as it explicitly tackles problems with partial observability, a fundamental challenge for applying RL in real-world tasks.

- The method proposed is relatively novel, as it combines efficient linear representations with L-step decodable POMDPs.

- The empirical evaluation considers many tasks and shows the proposed method has strong performance compared with multiple baselines.

### Weaknesses
 - The presentation could be improved. Some technical details are inconsistent or lack an appropriate definition (see detailed comments below). This makes important parts of the paper challenging to comprehend, such as the discussion of Eq 9.

- The paper is also very dense, which makes some parts too condensed. For instance, the theoretical analysis only states the assumptions and an informal version of the sample complexity of the algorithm without including an analysis of this result.

- The empirical evaluation is limited to a comparison with other algorithms. It would be interesting to provide an ablation study to show how the different components of the algorithm contribute to its performance. For example, how the algorithm performs without optimistic exploration.
Furthermore, it would be interesting to make a hyper-parameter sensitivity analysis, for example, evaluating how the algorithm performs with different values of L.


[Detailed comments]
- wrong typesetting of the observation function in the first paragraph of the preliminaries
- in the preliminaries, should the agent receive a reward r(s_h, a_h)?
- In the belief definition, it is unclear what is P(s1\mid o1). It is also unclear what is \tau.
- Wrong index in the actions of Eq 2
- Unclear what is \theta on Eq 5?
- \mu is used for initial state distribution and as a feature map
- are Eq 6 and Eq 9 missing some <> delimiters?
- after Eq 7: an practical -> a practical
- Eq 8: R(s,a) -> r(s,a)
- Eq 2 and 3 are defined for problems with a finite horizon, then Eq 6 and 8 use discount factor \gamma.
- Eq 12 uses the latent variable z without a proper introduction

### Questions
1. After Eq 16, could you provide some intuition about what is the parameter l?

2. Could you provide a formal definition of the policy \mu_pi?

3. The experimental evaluation mentions that the algorithms were tested after running 200K environment steps. Could you comment on this choice of training time? In particular, is this training budget sufficient for the convergence of all algorithms?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work aims to leverage the L-step decodable POMDPs to tackle the linear structure of POMDPs. Specifically, by conditioning on the recent L-step history (x_h), Q value does not need to rely on belief states or full history. Further, they show that Q value can be expressed in a linear form wrt P(z_h | x_h,a_h) where z_h is a latent variable, learned by some ELBO. The algorithm uses linear structure and learns the representation and Q value together with some sampling method. On both continuous and visual benchmarks, the proposed approach outperforms baselines in the terms of sample efficiency.

### Strengths
This work is original in POMDP literature with some theoretical guarantees (but I don’t have the expertise to check) and good quality. The technical writing is mostly clear, but some clarification is still needed. 

The empirical results are persuasive that the proposed approach outperforms the other baselines in most domains in the chosen continuous and visual control benchmarks.

### Weaknesses
This work has a main issue in its story writing:

1. The title and abstract is quite vague and overly broad – basically it just said it is about a theoretical framework on RL or planning (I am confused which one) in POMDPs. 

2. Moreover, the introduction on the theoretical framework is rather limited, unclear, unstructured, and seems overly strong. The 4 bullet points are most useful, but structured.

3. The claim “applied to a real-world problem” is especially strong, as the work obviously requires some assumptions on POMDPs, and no real world (like real robots) evaluation is performed. The evaluation is limited to standard benchmarks, which are not representative of the complexities of real-world scenarios. The assumption of L-step decodability, while theoretically interesting, is not justified in the context of real-world applications where the history dependence might be more complex and non-linear.

4. The claim “state-of-the-art” is also too strong, as obviously Dreamerv2 and DrQ-v2, published in 2021, are no longer SOTA. The comparison with these baselines does not provide a strong enough justification for the claimed performance improvements. The paper should benchmark against more recent and relevant state-of-the-art methods.

5. The claim also touches "offline POMDPs" but I did not see any results.

I don’t think this work has much technical significance since it is heavily relied on recent work (Ren et al, 2023a). Also, it would be better to point out how important linear structure is in solving POMDPs more explicitly.

### Questions
1. Is L-step decodability same as (or subsumed by) L-order MDPs?
2. Lack some definition on the latent variables z. From Eq 17, the objective of representation learning is exactly the same as belief-based approach. Let k=1, it is the standard ELBO of observation reconstruction/prediction, plus a KL divergence regularization between posterior and prior. In this sense, the optimal z seems to be belief state b. Is this correct? For k > 1, z might be different from b as it involves policy. 
3. The paper talks about “low-rank POMDPs”, but no definition is provided. How is it connected to L-step decodability? 
4. How partially observable is in the visual control benchmarks? As they were also tackled by Markovian methods.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
