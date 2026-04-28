# Automated Rewards via LLM-Generated Progress Functions

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 8, 5, 5

## Abstract
Large Language Models (LLMs) have the potential to automate reward engineering by leveraging their broad domain knowledge across various tasks. However, they often need many iterations of trial-and-error to generate effective reward functions.
This process is costly because evaluating every sampled reward function requires completing
the full policy optimization process for each function.
In this paper, we introduce an LLM-driven reward generation framework that is able to produce state-of-the-art policies on the challenging \bidex benchmark \textbf{with 20$\times$ fewer reward function samples} than the prior state-of-the-art work. 
Our key insight is that we reduce the problem of generating task-specific rewards to the problem of coarsely estimating \emph{task progress}.
Our two-step solution leverages the task domain knowledge and the code synthesis abilities of LLMs to author \emph{progress functions} that estimate task progress from a given state. 
Then, we use this notion of progress to discretize states, and generate count-based intrinsic rewards using the low-dimensional state space. 
We show that the combination of LLM-generated progress functions and count-based intrinsic rewards is essential for our performance gains, while alternatives such as generic hash-based counts or using progress directly as a reward function fall short.

\begin{comment}
extract key task-relevant features by leveraging LLMs to map the simulator state to a generic notion of \emph{task progress}: how many sub-tasks are involved in completing a given task, and how much progress have we made in completing each of these sub-tasks? 
Any given \emph{progress function} is task-specific--each task has its own success conditions, so requires its own mapping from simulator state to task progress--but the output features measuring progress are task-agnostic. 
Then, we use this notion of progress to discretize states, and use count-based motivation to provide dense rewards. 
Our approach achieves achieves state-of-the-art performance on the challenging \bidex benchmark \textbf{at a 20$\times$ lower sample budget} than prior work.
We show that the combination of LLM-generated progress functions and count-based rewards is essential for our performance gains, while alternatives such as generic hash-based counts or using progress directly as a reward function fall short.
\end{comment}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel framework leveraging Large Language Models (LLMs) to automate the generation of reward functions for reinforcement learning tasks. The authors claim significant improvements in sample efficiency and performance over prior state-of-the-art methods on the Bi-DexHands benchmark.

### Strengths
1. The paper is well-organized and easy to follow, making complex concepts accessible.
2. The overall motivation behind using LLMs for automated reward engineering is compelling.
3. The experimental results are substantial, demonstrating clear performance gains over existing methods.

### Weaknesses
1. The motivation for mapping progress to bins as a representation for intrinsic rewards is not clearly articulated. A common principle in intrinsic reward design is that the representation space should effectively capture the essential aspects of the original observation space. By incrementing counters in this space, the algorithm should be able to explore the full state space effectively. The authors need to provide a clearer rationale for why progress bins are chosen over other potential representations.
2. The method for selecting the best progress function among the generated options is not detailed (Line 287-289). The authors should provide a clear selection criterion to ensure reproducibility and allow for comparison of different progress functions.
3. The paper claims that progress-based bins are superior to simhash, yet it is not evident why this should be the case. Simhash is known to provide convergence guarantees by ensuring that increasing intrinsic rewards correspond to increased visits to the original full state space, though potentially requiring longer training times.
4. On Line 427, the authors suggest using the cumulative progress as a step reward for task completion, which is misguided. The correct approach, as per reward shaping principles, is to use the difference in progress.

### Questions
see weaknesses above.

### Soundness
2

### Presentation
3

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
This work proposes an algorithm to generate progress functions with fewer samples. This is accomplished by mapping the original observation space to a lower-dimensional representation, discretizing this space, and calculating intrinsic rewards based on the inverse square root of visitation counts.

Compared to previous baselines, this approach achieves state-of-the-art (SOTA) performance while utilizing fewer samples.

### Strengths
- The use of domain-specific discretization within the projected subtask progression space is novel and yields promising results.
- The experiments are thorough, with ablation studies providing valuable insights into the function of each design component.
- The empirical results are robust, demonstrating improved performance alongside reduced sample complexity.

### Weaknesses
In Figure 4, could you also provide results from Eureka? It would be interesting to see how the proposed method and Eureka performance improve as more samples are available.

How are the additional variables $[y_1, y_2, \ldots, y_k]$ used?

### Questions
How are the additional variables $[y_1, y_2, \ldots, y_k]$ used?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This submission concerns automatic reward shaping for RL tasks by utilizing LLMs for code synthesis, i.e., generating a shaping function. In particular, it improves on prior work (EUREKA) in constraining LLM output to "progress functions", which can serve as a basis for state binning, which in turn enables the use of count-based intrinsic rewards. Putting everything together, the authors demonstrate strong performance on a robot hand manipulation benchmark while significantly reducing the required samples of EUREKA (which generates variations of shaping functions by re-prompting the LLM with feedback obtained from running an RL training algorithm with the shaping function).

### Strengths
For the most part, the paper is easy to read and follow; the motivation is clear and the method is described well. Generally, I find the link between automatically generating a symbolic notion of task progress by an LLM (task description to progress function) and utilizing it to derive count-based rewards (which can be very effective if designed well) original and interesting; the experimental results demonstrate the efficacy quite well. I also liked that the evaluation focused on required training runs and environment interactions, where the proposed method is vastly superior to EUREKA.

### Weaknesses
First, I have doubts regarding the significance of this work. The main message -- you can get more out of an LLM's ability to translate language to RL specifications by placing additional constraints and supplying further human knowledge -- is timely and line with other recent works from the code generation community. On the other hand, the paper largely follows the problem setting of EUREKA, which, to my knowledge, has yet to demonstrate value beyond being an interesting application of LLMs. The original paper on defining rewards with LLMs (https://arxiv.org/abs/2306.08647) utilized model predictive control to directly translate the reward specifications to actions; count-based exploration does not allow for this, however, and relies on training a policy over millions of time-steps.

Further points:
- In Table 1, the same number of trials should be used for all methods. From 5.1. I understand that you select the best trial run, so a fair comparison should provide the same number of trials to all methods considered.

Finally,  the presentation could benefit from additional clarity, in particular the experimental section is at times hard to follow. Some concrete suggestions:
- In the first sentence of the abstract, you might want to mention that you're ultimately concerned with RL. "Automated reward engineering" is not a term I could immediately place in a specific field.
- Please provide the `Env` class. It's not clear to me whether the progress function has access to the same state as the policy or whether additional variables are provided
- Supply hyper-parameters such as learning rate for PPO
- The claim that the feature engineering library can be authored in minute (L164) is quite bold, in particular considering new domains and a lack of guidance for non-RL experts on what this library should contain.
- In Figure 3 or in the corresponding text, be explicit on how many environment samples are used.

### Questions
- Do your progress function break the MDP assumption? E.g., the BFS helper method for MiniGrid requires full access to the full environment state?
- Did you try prompting the LLM to always supply progress variables where progress strictly means an increase in value? This way you would not need the additional variables.

These questions should be answered in the text:
- For the MiniGrid experiment, how many runs of ProgressCounts were done?
- On which data do you base the range estimation of the progress variables? I understand you need several example rollouts (ideally successful) for this?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an innovative framework that uses LLMs to generate task-specific progress functions for reinforcement learning. The proposed system aims to overcome the challenge of reward engineering in sparse-reward tasks by focusing on generating progress-based intrinsic rewards. The paper introduces a two-step approach that uses LLMs to generate progress functions and then applies count-based intrinsic rewards. The authors evaluate their approach, ProgressCounts, on the challenging Bi-DexHands benchmark, and show that it achieves comparable or better results than previous state-of-the-art methods while requiring significantly fewer samples.

### Strengths
- The idea of simplifying reward generation by reducing it to the problem of estimating task progress is innovative. Leveraging LLMs to generate task-specific progress functions is a creative application that shows promise in reducing reliance on dense reward shaping.

- The method shows significant sample efficiency gains compared to Eureka, requiring up to 20 times fewer reward function samples while achieving state-of-the-art performance on the Bi-DexHands benchmark. This demonstrates the potential of the approach in reducing the computational cost of training.

- The experimental results on Bi-DexHands are impressive, as ProgressCounts outperforms both manually designed dense reward functions and existing automated reward generation methods in terms of task success rates.

### Weaknesses
 - The evaluation is conducted solely on synthetic benchmarks like Bi-DexHands and MiniGrid, which may not be fully representative of real-world environments. The generalizability of ProgressCounts to more diverse and real-world complex environments remains uncertain. Specifically, the reliance on simulated physics and simplified task structures in these benchmarks may not capture the nuances of real-world sensor data, noise, and unpredictable environmental factors. The performance gains observed might not translate directly to robotic manipulation in unstructured settings.

- The method relies heavily on LLMs to generate progress functions, which introduces potential biases inherent to LLMs. These biases can affect the quality and reliability of progress estimates, particularly in environments where the LLM lacks specific domain knowledge or makes incorrect inferences. For instance, if the LLM is trained primarily on text data, it may struggle to understand the nuances of physical interactions and spatial relationships, leading to inaccurate progress functions. This issue is further compounded by the lack of interpretability of LLM outputs, making it difficult to diagnose and correct such biases.

- The need for a pre-defined feature engineering library for each domain limits the method's automation potential. Although the feature library is relatively simple to create, this step still requires manual intervention and domain-specific expertise, which may limit scalability and practical deployment. While the authors claim the feature library is simple, the process of selecting appropriate features that are both informative and computationally tractable still requires careful consideration and could be a bottleneck for applying this method to new domains. The lack of a systematic approach to feature selection could also lead to suboptimal performance.

- While the proposed count-based intrinsic reward framework is well-developed, the paper lacks a thorough exploration or comparison with other recent reward design techniques, such as curiosity-driven approaches or model-based reward mechanisms. This leaves open the question of whether ProgressCounts is the optimal method for all types of tasks. The paper does not provide a clear rationale for choosing count-based rewards over other alternatives, and it is unclear whether the observed performance gains are specific to this reward mechanism or if they could be achieved with other intrinsic reward methods.

- The paper does not address the scalability of ProgressCounts when moving to tasks with highly complex environments or large state-action spaces. Specifically, the discretization strategy and count-based approach may face challenges when scaling to significantly more complex scenarios, potentially reducing sample efficiency. The discretization of the progress function into bins could lead to a loss of information, especially in high-dimensional state spaces, and the count-based approach might become computationally expensive as the number of bins increases.

### Questions
How well does the proposed ProgressCounts framework generalize to more complex, real-world environments beyond synthetic benchmarks like Bi-DexHands and MiniGrid? Have any tests been conducted to validate its applicability to a broader set of domains?

Given that the progress functions are generated using LLMs, how does the framework address potential biases that the LLM may introduce, particularly in environments where LLMs may not have specific domain knowledge?

The paper relies on a discretization strategy and count-based intrinsic rewards. How scalable is this approach when applied to tasks with significantly larger state-action spaces or more complex environments? Would sample efficiency gains still hold under such conditions?

### Soundness
2

### Presentation
2

### Contribution
2
