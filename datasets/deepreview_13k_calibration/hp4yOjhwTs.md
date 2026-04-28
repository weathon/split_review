# Causally Aligned Curriculum Learning

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 3, 6, 8

## Abstract
A pervasive challenge in Reinforcement Learning (RL) is the ``curse of dimensionality'' which is the exponential growth in the state-action space when optimizing a high-dimensional target task. The framework of curriculum learning trains the agent in a curriculum composed of a sequence of related and more manageable source tasks. The expectation is that when some optimal decision rules are shared across source tasks and the target task, the agent could more quickly pick up the necessary skills to behave optimally in the environment, thus accelerating the learning process. 
However, this critical assumption of invariant optimal decision rules does not necessarily hold in many practical applications, specifically when the underlying environment contains unobserved confounders. This paper studies the problem of curriculum RL through causal lenses. We derive a sufficient graphical condition characterizing causally aligned source tasks, i.e., the invariance of optimal decision rules holds. We further develop an efficient algorithm to generate a causally aligned curriculum, provided with qualitative causal knowledge of the target environment. Finally, we validate our proposed methodology through experiments in confounded environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper delves into the challenges of designing a curriculum of source tasks to tackle a complex target task in the presence of unobservable confounding variables within the environment. The authors leverage the structural causal model framework (Pearl, 2009) to define causally aligned source tasks for a given target task. They propose a causally aligned curriculum that incorporates qualitative causal knowledge of the target environment, and they validate their approach through experiments in two confounded environments.

### Strengths
The paper addresses an important problem in curriculum reinforcement learning, highlighting the potential negative impact of inadequate task space design on target task performance. 

The writing quality is commendable, even though the paper features heavy notation due to its nature. The repeated use of the Sokoban game aids comprehension and clarity regarding the paper's contributions and claims.

### Weaknesses
The strategy for avoiding misaligned source tasks, as proposed in this work, relies on causal knowledge about the underlying data-generating mechanisms within the environment. This requirement limits the broader applicability of the strategy, making it dependent on domain-specific knowledge. The practicality of obtaining a causal diagram G for a general target task remains uncertain. 

It remains unclear whether the proposed causal curriculum strategy can be extended to domains with continuous state and action spaces.

### Questions
Re. the Colored Sokoban example:

In the baseline, the context/task space is restricted to tasks where the box color remains constant throughout the game. However, considering a more extensive task space that encompasses all possible combinations of box colors might lead the state-of-the-art curriculum strategies to automatically select relevant/aligned tasks during training. In contrast, the proposed causal curriculum limits the task space to initial agent and box positions, with the environment determining box colors based on intrinsic randomness. 

Formally, let us denote the initial positions of the agent and the box as $(a_0^x, a_0^y)$ and $(b_0^x, b_0^y)$, respectively. Furthermore, let $c_t$ represent the color of the box at time step $t$, and designate $H$ as the maximum number of steps allowable in the game. In the results presented, the baseline methodology confines the context/task space to instances of the form $[a_0^x, a_0^y, b_0^x, b_0^y, c_0 = c_1 = \cdots = c_H]$. The extensive task space contains all possible task configurations denoted as $[a_0^x, a_0^y, b_0^x, b_0^y, c_0, c_1, \dots, c_H]$. The proposed causal curriculum imposes a task space restriction, characterized by tasks of the form $[a_0^x, a_0^y, b_0^x, b_0^y]$, delegating the selection of $[c_1, c_2, \dots, c_H]$ to the environment, predicated upon intrinsic randomness. 

Please provide your insights on this aspect.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Curriculum reinforcement learning is to train the agent on a sequence of simpler, related tasks in order to gradually progress the learning towards a difficult, often sparse-reward target task. The hope is that if there are common optimal decisions among these simpler intermediate tasks and the target task, the agent will learn transferrable skills during the process and accelerate the learning process. However, this assumption may not hold if there are unobserved confounders in the environment. This paper delves into this problem from a causal perspective, defining conditions under which the optimal decisions remain consistent. It also introduces a method to create a curriculum that aligns causally. The method is tested in two grid-world environments with unseen confounders to validate the effectiveness of the proposed algorithms.

### Strengths
The structure and flow of the paper are easy to follow. Several simplified examples are provided to support the argument and illustration. To my knowledge, the perspective of confounders in curriculum reinforcement learning is novel.

### Weaknesses
 * Toyish experiments. The experiments conducted are limited to grid-world environments, which significantly narrows the scope of application. For the conclusions to be generalized, the experiments should ideally be extended to a more diverse set of environments. Specifically, the current experiments do not explore the complexities of continuous state and action spaces, which are common in many real-world RL problems. The grid-world setup, while useful for initial validation, lacks the nuances of environments with high-dimensional sensory inputs or complex dynamics. This limits the practical relevance of the findings.
* Scalability. The paper does not adequately address how the proposed method scales to continuous environment variables. This is a significant concern as many practical applications in continuous or high-dimensional environment variable space. By not tackling this challenge, the authors leave a gap in understanding the full potential and limitations of their method. The method's reliance on identifying causal relationships might become computationally intractable in high-dimensional settings, and the paper does not discuss potential approximations or simplifications to address this issue. Furthermore, the paper does not discuss the sample complexity of learning these causal relationships in more complex environments.
* Missing related work:
    * Hu, Xing, et al. "Causality-driven Hierarchical Structure Discovery for Reinforcement Learning." Advances in Neural Information Processing Systems 35 (2022): 20064-20076.
    * Cho, Daesol, Seungjae Lee, and H. Jin Kim. "Outcome-directed Reinforcement Learning by Uncertainty & Temporal Distance-Aware Curriculum Goal Generation." arXiv preprint arXiv:2301.11741 (2023).
    * Huang, Peide, et al. "Curriculum reinforcement learning using optimal transport via gradual domain adaptation." Advances in Neural Information Processing Systems 35 (2022): 10656-10670.

### Questions
* In Algorithm 3, how is the actions sequence $\{X_1, \ldots, X_H\}$ obtained in the first place? If we have this optimal action sequence before the learning starts, why do we need RL?
* In Theorem 3, one of the conditions is that: For every $j=1, \ldots, N-1$, actions $\boldsymbol{X}^{(j)} \subseteq \boldsymbol{X}^{(j+1)}$. Does this mean that the transition must be deterministic and there only exists one unique optimal solution?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackled the problem of curriculum design in multi-task Reinforcement Learning. A challenge in the previous curriculum learning literature is that they all assume that the optimal decision rules are shared across different tasks. From a causal point of view, this expectation may not hold when the underlying environment contains unobserved confounders. To tackle this issue, the paper proposed a causal framework based on structural causal models and rigorously defined the notion of aligned tasks. The paper then proposed an algorithm that only generates aligned tasks. Simulation studies on Maze and Sokoban environments showed the advantage of the proposed algorithms.

### Strengths
The paper finds a significant issue in the current literature of automatic curriculum learning and provides a clear framework to discuss the issue of non-alignment. Thus, the paper has great significance.

The paper is well-written and all the important messages are clearly delivered.

### Weaknesses
1. The authors suggest that curriculum learning could overcome the curse of dimensionality. However, all the examples discussed in this paper are tabular, focusing on grid-world scenarios. This creates a significant mismatch between the claimed capabilities and the demonstrated examples. A more compelling case could be made by discussing and experimenting with an example featuring exponentially large state and action spaces, such as a continuous control task or a high-dimensional environment.

2. The computational complexity of the FindCausalCurriculum algorithm is not clearly defined. It is crucial to understand how it scales with the size of the state and action spaces. If the complexity increases significantly with larger state and action spaces, it might contradict the motivation for using curriculum learning as a tool to combat the curse of dimensionality. A detailed analysis of the algorithm's time and space complexity would be beneficial.

3. The experimental environments, namely Maze and Sokoban, are relatively simplistic. While they serve as a starting point, they do not fully represent the complexity of real-world scenarios. Furthermore, the implementation of ALP-GMM by fixing the color in the Sokoban environment seems to be an artificial constraint. A more natural approach would be to allow ALP-GMM to sample tasks from a fixed set, potentially including tasks with varying colors. This would allow ALP-GMM to adaptively adjust the weights assigned to different tasks based on their alignment with the target task. In the current setup, it is unclear whether ALP-GMM can effectively handle scenarios where the chosen color (C) acts as a proxy for the underlying unobserved confounder (U). A more complex example demonstrating the potential pitfalls of using C as a proxy in conjunction with ALP-GMM would strengthen the paper's argument.

4. The current algorithm appears to be designed for tabular MDPs, which limits its applicability to more complex environments with large or continuous state and action spaces. To enhance the paper's impact, it would be valuable to propose an algorithm or an extension of the current one that can handle such environments. This would significantly broaden the scope of the proposed approach and make it more relevant to a wider range of reinforcement learning problems.

### Questions
1. I was a bit confused by the wordings in abstract. The authors first state that invariant
optimal decision rules does not necessarily hold, then they propose condition characterizing causally aligned source tasks, i.e., the invariance of optimal decision rules holds. The flow does not seem right here.

2. Need extra clarifications on Figure 1 and 2. What does it mean by fixing the color? When the different algorithms are trained, are they only allowed to choose tasks from misaligned source tasks? Should this example be too artificial? It would be interesting to see the results when ALP-GMM can generate tasks with unknown color, while the algorithm may reuse these tasks. In this way, it is possible for ALP-GMM to discover that certain tasks can be more helpful for learning the target task. This is in fact more aligned with the situations in the real-world.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a curriculum design method that produces causally aligned curriculums. Given a causal graph, a curriculum generator, and a target task, the proposed method creates a causally aligned curriculum using two main ideas. First, the FindMaxEdit algorithm, which constructs a set of causally aligned source tasks based on the modifying the editable variables of the target task. Importantly, optimal decision rules can be transported across causally aligned source tasks. Second, the authors propose ordering causally aligned source tasks with an expansion criterion on the optimal decision rules (i.e. tasks should be ordered such that the set of optimal decision rules expands with each task).

### Strengths
i. The method is well-founded and rigorously specified. Further, the main idea of this paper - using knowledge of causal relationships to improve curriculum generation methods - is clearly useful to the community. 
ii. The paper is clear, with all details necessary to reproduce the work present in the paper. 
iii. The experimental results on Colored Sokoban and Button Maze are strong.

### Weaknesses
Most of my concerns + comments are related to the motivation + presentation of the paper.

- Motivation: Example 1's motivation for the paper is very contrived. The only reason a curriculum designer would design such a source task (where the box color is fixed to yellow) is if the curriculum designer was completely unaware of the causal dependencies of the reward. While this is possible in the case of causally-unaware automated curriculum generation methods, I find it a bit unlikely unless the crucial confounder variable U_i was either excluded from the state space (which would violate the usual Markovian reward assumption) or it is included in the state space, but the agent cannot observe it (a partial observability assumption). This leads to my questions:
	1) Can the authors experimentally verify how often existing non-causal curriculum generation methods generate causally unaligned tasks?
	2) Can the authors comment on the expected benefit of their method in a domain with Markovian reward, or a fully observable domain w/no unobserved confounders?

- Acknowledging limitations and situating their work in presence of related work
	1) I saw that the related works section was relegated to the Appendix. There should at least be a pointer in the main paper to the related works. I found it helpful to read it, to understanding the positioning of this work, and think that it should be included in the main paper. The paper provides almost too many details about the method in the main paper, and at places is rigorous to the point of being pedantic. I think that the space would be better spent on situating the work properly.
	2) The inputs/outputs of the authors' method is not presented in plain language. As I understand it, the authors' method assumes access to the SCM of the task, and a curriculum generator such as GoalGAN. Such details should be made much clearer, perhaps through a summary methods figure or by adding a discussion of limitations.

- Figures are not standalone: it is common practice to read a paper by skimming the figures + captions first, but I found that it was not possible to get the main idea of the figure, method and experimental results by doing so. Even after reading most of the accompanying text, I still found the figures + captions alone ambiguous. I had to find the specific part of the text referencing the figures -- sometimes needing to jump to other parts of the paper-- and read very carefully to understand what was happening. The authors should rewrite the figure captions and perhaps add a new "methods" figure summarizing the flow of their method. My specific comments on two figures are below, but all figures can be improved:
	1) Figure 5: Specifically, I was confused about why the curves labelled "causal" performed differently across the four columns? Also, the names of "causal" vs "original" were confusing. I think this is because the fact that the proposed method augments existing curriculum generation methods was presented only in a single sentence towards the end of the intro, and the knowledge was assumed in the rest of the paper. Seeing as this information is crucial to understand the paper, perhaps the authors can add this crucial piece
	2) Figure 3: It's confusing that figure (a) and (b) are identical except for the edit indicators. I needed to visually trace all arrows of both figures to verify this. The presence/absence of edit indicators should be explained in the caption, and the figure can be modified so that it is much quicker for the reader to notice that the only addition is the edit indicators (perhaps through the use of opacity / shading).

### Questions
See the weaknesses section for the most substantial questions and comments. 

Minor clarity comments are below: 
- Exogenous vs endogenous should be defined at some point in the preliminaries section on SCMs. 
- "che" "de" "an" meanings were not immediately clear to me. 
- In Def 1, the SCM M* is labelled with a *, yet this notation does not appear elsewhere in the paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
