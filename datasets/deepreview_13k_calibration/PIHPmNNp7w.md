# Retrieval-Augmented Decision Transformer: External Memory for In-context RL

- Decision: Reject
- Avg Score: 4.67
- Scores: 8, 5, 1

## Abstract
In-context learning (ICL) is the ability of a model to learn a new task by observing a few exemplars in its context. 
While prevalent in NLP, this capability has recently also been observed in Reinforcement Learning (RL) settings.
Prior in-context RL methods, however, require entire episodes in the agent's context.
Given that complex environments typically lead to
long episodes with sparse rewards, these methods are constrained to simple environments with short episodes. 
To address these challenges, we introduce Retrieval-Augmented Decision Transformer (RA-DT).
RA-DT employs an external memory mechanism to store past experiences from which it retrieves only sub-trajectories relevant for the current situation.
The retrieval component in RA-DT does not require training and can be entirely domain-agnostic.
We evaluate the capabilities of RA-DT on grid-world environments, robotics simulations, and procedurally-generated video games.
On grid-worlds, RA-DT outperforms baselines, while using only a fraction of their context length.
Furthermore, we illuminate the limitations of current in-context RL methods on complex environments and discuss future directions. To facilitate future research, we release datasets for four of the considered environments.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper tackles the challenge of in-context learning in complex RL environments, where long episodes and sparse rewards make traditional approaches difficult to apply effectively. To address this, the authors introduce the Retrieval-Augmented Decision Transformer (RA-DT), which utilizes an external memory to store past experiences. This memory enables the selective retrieval of relevant sub-trajectories based on the current context, allowing the model to make informed decisions without relying on entire episodes. Through extensive experiments, the authors demonstrate the effectiveness of RA-DT and show its superior performance over baseline methods. Additionally, they release datasets for multiple environments to support future research in in-context RL.

### Strengths
1. The proposed RA-DT leverages an external memory mechanism to store and retrieve relevant sub-trajectories, effectively tackling the challenge of managing context in environments with long episodes and sparse rewards.
2. The authors conducted extensive experiments to showcase the method’s effectiveness and to highlight the contribution of each module.
3. The authors released datasets for multiple environments, offering valuable resources to support future research in in-context RL.

### Weaknesses
1. Although the authors explain the rationale for using each module in RA-DT and demonstrate their effectiveness through experiments, the proposed RA-DT appears to be a combination of various existing methods [1, 2, 3]. What specific innovations do each of these methods introduce compared to the original approaches?
2. The processes of searching forsimilar experiences and reweighting retrieved experiences introduce additional computational overhead, which is neither discussed in detail nor evaluated in the experiments. Could you discuss the computational overhead introduced by the search and reweighting processes, and how this compares to the baseline methods?

### Questions
1. Could you provide information on the runtime and computational resources required for the proposed method compared to the baseline methods? (The same as the second point in weaknesses)

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work introduces a variant of transformer-based offline RL by modifying the Decision Transformer architecture by an external memory component and associated retrieval mechanism. The retrieval-augmented decision transformers (RA-DT) retrieval mechanism enables retrieval of relevant sub-trajectories such that the in-context learning behavior of the DT is improved. The approach is evaluated on a variety of RL problems, though strong benefits of the proposed methods can only be shown on grid-world environments.

### Strengths
The retrieval-augmentation idea is compelling. It particularly shines in its ability of cutting down the context length that is required for in-context reinforcement learning.
Further, the idea of utilizing pre-trained language models for the domain-agnostic embedding is very interesting and could be useful in this type of in-context RL. 
Lastly, the work evaluates the approach on a broad variety of problems including more toy-like problems to larger and more complex ones.

### Weaknesses
While the work provides a broad evaluation of the proposed method, the experiments highlight the shortcomings of the method. Often the proposed method does not achieve better in-context learning abilities, particularly on problems that are not grid-worlds. Due to these shortcomings the authors provide a longer discussion section on the potential shortcomings of offline in-context RL methods, though this discussion does not provide explanations or better understanding why the proposed method did not work. In short, this section leaves many open questions about RA-DT .
Similarly, the domain agnostic embedding idea is put in the spotlight as a big benefit. However, experiments with this embedding seem to only have been conducted in the simplest setting where RA-DT works and there it does not seem to be a generally good choice. Further investigation is needed to properly understand if the domain agnostic approach actually  is a good choice or if it was simply random chance that it worked for some of the simplest cases.
As one central aspect of this work is concerned with reducing the context size needed for action prediction, I would have expected (at least a short) discussion on the work of Melo, ICML 22 ("Transformers are Meta-Reinforcement Learners") as this approach uses a "working memory" of only the five most recent transitions, when learning to reinforcement learn with a transformer. While this work might not be in the exact ICL learning regime as the work under review, I believe that they are related enough that this work warrants further comparison. Particularly of interest should be that in Melos work longer horizons become detrimental for learning and the learned agent struggles to generalize to completely unseen settings. A followup work to Melos (Shala et al. 2024 ("Hierarchical Transformers are Efficient Meta-Reinforcement Learners")) aims at improving the ICL abilities of this approach by introducing a "cross-episodic" memory where not only the most recent transitions are part of the working memory, but snippets of the most recent episodes as well. While this increases the overall used context size again, it does not require full episodes in the context and shows superior ICL on completely new test environments.

### Questions
* How does RA-DT + domain-agnostic compare to the baselines and RA-DT in the complex environments?
* Why can the works on using Transformers for Meta-RL use much shorter context-sizes?
* Which of the shortcomings of ICRL does RA-DT suffer from (the most) and which of the provided experiments show this?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper introduces Retrieval-Augmented Decision Transformer (RA-DT), a method that employs an external memory mechanism to store and retrieve relevant past experiences, enabling efficient in-context reinforcement learning in environments with long episodes and sparse rewards.

### Strengths
-Model agnostic Retrieval-Augmentation

-Smaller context length and boost in Performance

### Weaknesses
1) Novelty: The novelty of this work seems limited as it primarily leverages existing techniques like retrieval augmentation and Decision Transformers.

2) Qaulity Data Availability and Relevance: If quality relevant data is not available is in storage then it is not very helpful.

### Questions
1) Technical Challenges: Could you please elaborate on the specific technical challenges (that authors solve) in this work?  (Not including what prior works do). If Retrieval Augmentation and decision transformer already exist then what is the contribution?

2) Large Context Length and Retrieval Augmentation: How does your approach handle longer trajectories, and what are the potential limitations of using large context lengths in retrieval augmentation?

3) Domain-Agnostic Model Performance: In Figure 3b, why does the RA-DT + domain-agnostic model exhibit a performance decline compared to the RA-DT model?

4) In Figure 4, does running for more episodes ensure other approaches converge? Can you present those results to ensure baselines converge but require more samples?

5) Computational Efficiency: How does the computational cost of your approach compare to the baseline methods, especially in terms of inference time?

### Soundness
3

### Presentation
2

### Contribution
1
