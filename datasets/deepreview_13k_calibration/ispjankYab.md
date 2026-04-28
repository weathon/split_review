# Action abstractions for amortized sampling

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 8, 8, 6, 6

## Abstract
As trajectories sampled by policies used by reinforcement learning (RL) and generative flow networks (GFlowNets) grow longer, credit assignment and exploration become more challenging, and the long planning horizon hinders mode discovery and generalization.
The challenge is particularly pronounced in entropy-seeking RL methods, such as generative flow networks, where the agent must learn to sample from a structured distribution and discover multiple high-reward states, each of which take many steps to reach.
To tackle this challenge, we propose an approach to incorporate the discovery of action abstractions, or high-level actions, into the policy optimization process.
Our approach involves iteratively extracting action subsequences commonly used across many high-reward trajectories and `chunking' them into a single action that is added to the action space.
In empirical evaluation on synthetic and real-world environments, our approach demonstrates improved sample efficiency performance in discovering diverse high-reward objects, especially on harder exploration problems.
We also observe that the abstracted high-order actions are interpretable, capturing the latent structure of the reward landscape of the action space.
This work provides a cognitively motivated approach to action abstraction in RL and is the first demonstration of hierarchical planning in amortized sequential sampling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a approach to incorporate action abstractions into the policy optimization process of reinforcement learning and generative flow networks. The method, termed ACTIONPIECE, aims to improve sample efficiency and mode discovery by iteratively extracting and chunking action subsequences from high-reward trajectories into a growing action space. The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
- The proposed ACTIONPIECE compatible with both RL and GFlowNets sampler.
- Empirical evaluation showing improved sample efficiency and mode discovery in different environments.

### Weaknesses
 - As mentioned in the related works section, the discovery of macro-actions has been extensively studied. The authors should provide a more detailed discussion highlighting how the proposed method differs from existing methods.

- In Line 159, the paper appears to assume a deterministic state transition, where $s'=s+a$. This assumption may be too strong and not applicable to real-world environments where state transitions involve a degree of randomness. The reviewers are concerned about the generalizability of the proposed method to stochastic environments. The authors should address whether and how the method can accommodate stochastic state transitions, which are common in many practical applications of RL and GFlowNets.

- The reviewers suggest that the authors should provide a more comprehensive introduction to the concept of "amortized samplers" in the Preliminaries section. It is essential for readers who are unfamiliar with this concept.

- The proposed Algorithm in Section 4 seems to be applicable to both GFlowNets and RL methods with discrete action spaces, as evidenced by the experiments conducted in the paper. However, the authors have chosen to focus heavily on GFlowNets as the primary background, which may not be immediately clear to readers. The reviewers recommend that the authors clarify why GFlowNets were chosen as the main framework and how the proposed method specifically leverages or addresses challenges unique to GFlowNets. 

- In Line 304, the paper mentions an action encoder but does not elaborate on how it is trained. The authors should provide details on the training process of the action encoder. 

- The experiments presented in the paper is simple. The reviewers question why the authors did not test their method in more complex environments, such as Atari games, which are known for their high dimensionality and complexity. Additionally, the paper lacks a comparison with existing methods for discovering macro-actions.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a new technique to iteratively extract action subsequences from high-reward trajectories as temporally extended skills that are then added to the action space for more efficient exploration. Applying this technique on top of generative flow networks (GFlowNets) yields improved sample efficiency in hard exploration problems. The authors experiment on three synthetic tasks and an RNA sequence generation task and show that the proposed method improves GFlowNets and outperform prior methods (e.g., RL methods like A2C and SAC) on these tasks.

### Strengths
- The idea of expanding the action space dynamically online with temporally extended action sequence is interesting and novel.
- The experiments are comprehensive and thorough with insightful analyses and visualizations that demonstrate the effectiveness of the proposed algorithm.

### Weaknesses
*Unfounded claim*
- “the abstracted high-level actions are interpretable, …” — there is no evidence presented in the paper that illustrates the high-level actions are interpretable.

*Comparison to prior chunking mechanisms is limited*
- The authors considered two new chunking mechanisms, "ActionPiece-Increment" and "ActionPiece-Replace". Both of them use heuristics to expand action space with temporally extended action sequences.
- It is unclear how these mechanisms compare to prior chunking mechanisms used in the options/unsupervised skill discovery/hierarchical RL literature (e.g., with variational formualtion [1], with clustering [2].

### Questions
N/A

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the long-planning horizon problem in credit assignment by providing a trunking method ActionPiece. This approach aims to extract high-order actions from sampled trajectories and can be plugged into any sampler. In experiments with three classic algorithms and various environments, the capability of the proposed method in mode discovery, density estimation improvement, and sample length reduction is demonstrated. Abundant discussions and information are further provided.

### Strengths
Overall, this paper is well presented and provides an articulate method. I particularly appreciate the environment selections of a real-world orientation and informative way of discussion.

### Weaknesses
(W1) Minor typos, e.g.,’the the’ at line 319.

(W2) It seems that all experiments are averaged from only three seeds per line 348 and 507, which is not enough to demonstrate statistical significance in some settings. The variance across different random seeds is crucial for assessing the robustness of the proposed method, and the current number of seeds may not be sufficient to draw strong conclusions, especially in complex environments or when comparing multiple algorithms. This is particularly concerning for the mode discovery experiments, where the number of modes found can vary significantly depending on the initialization and training process. A more thorough evaluation with a larger number of seeds is needed to ensure the reliability of the results.

### Questions
(Q1) As the two proposed chunking mechanisms show contrasting capabilities in multiple aspects, I am curious about the possibility of adaptively combining them. Do you have any related explorations?

(Q2) How does the proposed method perform with other tokenization techniques? Does the chunking method particularly fit some of the tokenization techniques such as BPE used in the paper?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the action abstraction for amortized sampling with reinforcement learning and generative flow networks. It proposes to iteratively extract high-reward action subsequences to be expanded as new actions, trading increased breadth for decreased depth of the Markov decision process.  In each iteration, it uses the byte pair encoding for generating high frequency subsequences from the high-reward sequences. Two variants are considered: one incrementally adds new subsequences, while the other periodically replaces old action abstractions.

### Strengths
**Quality**: The paper is of good methodological quality. It conducts a careful and meticulous empirical investigation of the use of action abstraction in amortized sampling.

**Significance**: The exploration of action abstraction in this manner could potentially lead to more efficient sampling techniques, although its impact remains to be fully assessed.

### Weaknesses
 **Novelty**: The use of byte pair encoding for learning action abstraction is not new, as it is already explored in the work by Zheng et al. [1]. To enhance the novelty, the authors should differentiate their approach more clearly or build upon the existing frameworks with significant innovations.

**Significance**: The proposed algorithm exhibits varied performance across different tasks and samplers, lacking a consistent indication of its promise as a robust approach. This raises questions about its generalizability and efficacy in broader applications.

**Clarity**: The conclusions are not effectively communicated. Despite thorough reading, the paper does not present clear, actionable takeaways or insights, as results appear highly case-specific. Improving the clarity of conclusions and providing more generalized insights would increase the paper's impact.

### Questions
- How does your approach specifically differ from the method proposed by Zheng et al. as well as other action abstraction methods?

- The conclusions seem case-specific. Can you provide a more generalized summary of the key takeaways from your research?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a method named ACTIONPIECE that incorporates action abstraction discovery into the policy optimization process. It leverages tokenizers to chunk action sequences, which can be viewed as a strategy for trading reduced depth of the MDP in exchange for increased breadth.

### Strengths
1. The proposed method is a novel approach to improve the performance of samplers on model discovery and capturing the latent structure of the environment.

2. The method has been validated in three different scenarios, demonstrating its broad applicability and robustness.

### Weaknesses
1. The paper lacks rigorous theoretical analysis or proofs to support the observed improvements. While empirical results are strong, a more detailed theoretical discussion would strengthen the claims about the performance of the proposed method.

2. The abstract lacks a quantitative presentation of the results.

3. Can the proposed method be applied to offline-training RL tasks? Can the authors provide some discussion on offline training?

4. As mentioned by the authors, the use of a fixed BPE tokenizer for chunking fixed target distributions in experiments may limit the method's generality and flexibility.

### Questions
Please check the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
