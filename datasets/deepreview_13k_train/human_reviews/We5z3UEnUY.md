# Stable Hadamard Memory: Revitalizing Memory-Augmented Agents for Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Effective decision-making in partially observable environments demands
robust memory management. Despite their success in supervised learning,
current deep-learning memory models struggle in reinforcement learning
environments that are partially observable and long-term. They fail
to efficiently capture relevant past information, adapt flexibly to
changing observations, and maintain stable updates over long episodes.
We theoretically analyze the limitations of existing memory models
within a unified framework and introduce the Stable Hadamard Memory,
a novel memory model for reinforcement learning agents. Our model
dynamically adjusts memory by erasing no longer needed experiences
and reinforcing crucial ones computationally efficiently. To this
end, we leverage the Hadamard product for calibrating and updating
memory, specifically designed to enhance memory capacity while mitigating
numerical and learning challenges. Our approach significantly outperforms
state-of-the-art memory-based methods on challenging partially observable
benchmarks, such as meta-reinforcement learning, long-horizon credit
assignment, and POPGym, demonstrating superior performance in handling
long-term and evolving contexts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents a memory-based architecture for partially observable RL, named Stable Hadamard Memory (SHM). SHM is evaluated on a range of POMDP environments and POPGym against recurrent and attention-based baselines, as well as some ablations and analysis.

### Strengths
The paper is well presented and the method is explained in detail. It is evaluated against a range of baselines and on multiple benchmarks.

### Weaknesses
1. The novelty of the method is not directly apparent from reading the paper. Stable Hadamard Memory is a confusing description for the method, as many existing RNNs, such as GRUs, make use of a Hadamard product as a core component. Furthermore, the Hadamard product is not the defining feature of the method, any more than addition. Instead, it would seem that the design of the calibration matrix, with random selection/dropout of update parameters, is the primary contribution of the approach. Based on this, more focus on this component in the paper and method naming would benefit the reader.

2. The method's update rule is highly similar to linear attention, which is cited but not discussed in the work. A discussion of how this method relates to linear attention and empirical evaluation against it would be compelling. Specifically, the use of a query, key, and value projection, followed by a Hadamard product and a weighted sum, bears a striking resemblance to the core operations in linear attention mechanisms. The paper should clearly articulate the differences, if any, in the mathematical formulation and the practical implications of these differences.

3. Due to the random selection of update parameters in SHM, the memory usage of SHM should be higher than methods without parameter dropout. Discussing this and adding experiments comparing SHM to baselines with the same memory usage would be useful. The paper should quantify the additional memory overhead introduced by the calibration matrix and provide a detailed analysis of how this overhead scales with the size of the memory and the number of parameters. This analysis should also consider the impact on training time and computational resources.

4. The experiments have very few repeats (3 seeds) and it is unclear how some baselines were tuned. The lack of sufficient repeats makes it difficult to assess the statistical significance of the results. Furthermore, the tuning process for the baselines should be described in detail, including the range of hyperparameters explored and the criteria used for selection. It is unclear if the baselines were tuned on the same tasks as SHM, and if not, this could introduce a bias in the comparison.

5. A paper from RLC 2024 exploring memory aggregation in Meta-RL is not cited [1].

### Questions
* Typo in the title of Section 3.3 - Stable Hadamrad Memory.

* How were the baselines tuned for each of the experiments? I could only find partial detail in the appendix. What efforts were made to normalize computational and memory cost between baselines and SHM?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work addresses memory in partially observable RL environments. The authors state that current methods fail to capture relevant past information, making it difficult to retain important memories and know when to dynamically update them in response to changes in the environment. This issue is particularly significant for continual learning.

The authors introduce a Hadamard memory framework, suggesting that it performs memory calibration and linearly adjusts memory elements by maintaining a calibration matrix used to update these elements via an update matrix. The Hadamard product allows these elements to be learned using neural networks, and this method is well-supported in the literature. The memory matrix is then formulated using the standard policy gradient method, and the authors also demonstrate stability guarantees.

This approach is based on the Hadamard product applied to the memory matrix, enabling adaptive memory rules to be learned.

The method is evaluated on various Meta-RL tasks and challenging credit assignment tasks, with results showing dramatic improvements. The authors propose that this dynamic memory writing method facilitates more efficient credit assignment. They also evaluate the method on a set of partially observable gym environments, visually demonstrating the memory and calibration matrices.

### Strengths
* As said in my summary, the results show improvements on a broad set of tasks and appear to be extremely significant.

* The method is mathematically well motivated, justified well and theoretically guarantees are given. I especially appreciate the stability guarantees.  It appears to be sound to use this for updating agent memories.

* The credit assignment benefits are justified well and empirically shown.

* The work is very well motivated and many of the theoretical guarantees are strong and supported well.

Overall this work is solid and presents and interesting way of updating memory.  I currently support acceptance of this work.  I do not have high confidence in my review as this work is a bit orthogonal to the previous works I have done on partially observably environments.

### Weaknesses
 * The paper is overly complex at times going into too many mathematical details.  I would like a very clear description of the benefits of using this update rule and why it empirically works well.


### Questions
Please see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a relatively simple recurrent model for reinforcement learning under partial observability. Their model is parallelizable in time due to a linear recurrent state update. They demonstrate that their method outperforms prior work across various benchmarks, both with PPO SAC algorithms.

All in all, this is a good paper tackling an important problem with a novel approach and thorough experimentation. In my opinion, the biggest weakness is that the authors have not provided their code.

### Strengths
- The paper is nicely structured
- The authors provide a thorough literature review
- The authors' method is very straightforward to implement
- The derivation of the linear matrix C is much shorter and easier to read than the derivation of the A and B matrices from the State Space Models paper (and yet, the authors' method performs better)
- Rather than designing linear operations to keep inputs around in the recurrent state as long as possible (State Space Models), the authors take relatively novel approach to design a linear operation that has well-behaved gradients
- Randomly sampling $\theta$ to break the dependence between inputs is a novel and interesting idea
- The authors run numerous experiments, across multiple benchmarks and RL algorithms

### Weaknesses
 - The authors do not provide code
- The writing is a bit awkward in places, hampering my understanding -- I think the paper would benefit from having another proofread
    - The initialization of $C$ is quite important (lines 259-264), but it took me a few reads to understand the process -- perhaps the authors can consider writing something like $\theta = [\theta_1, \theta_2, \dots, \theta_{L}]; \quad \theta_t \sim \mathcal{U}(\theta)$
    - Proposition 3 is poorly worded, and should be rewritten
    - Section 3.3 is misspelled (STABLE HADAMRAD MEMORY (SHM))

### Questions
- Why is $1 + \tanh(x)$ used instead of $\textrm{sigmoid}(x)$?
- How come the recurrent state is real-valued compared to methods like FFM? Did the authors try using complex-valued states to track phase information across sequences?
- Line 233: What is $m.k$?

### Soundness
3

### Presentation
2

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
This paper introduce"SHM"model, spcefically solving memory management problem in RL. SHM use a Hadamard product-based memory update mechanism to dynamically retain important information and discard irrelevant data, aiming to enhance memory stability and efficiency. The authors propose SHM as a solution to the limitations of existing memory models, such as numerical instability and inefficient memory retention, particularly in complex and long-horizon tasks. Experimental results demonstrate SHM’s superior performance compared to state-of-the-art memory models across multiple benchmarks, including meta-reinforcement learning and the POPGym suite, indicating its potential as a robust memory mechanism for RL applications.

### Strengths
This paper's got some fresh ideas that really matter in the real world. First off, they've come up with this nifty thing called the Stable Hadamard Memory (SHM) model. It's like a brain upgrade for AI in situations where it can't see everything. The unique twist is this memory update method that uses something called the Hadamard product. It's all about keeping the good memories and dumping the useless ones, which makes the AI's memory super stable and efficient.

But that's not all. The paper really shows off the SHM's chops by putting it through its paces in a bunch of tests.  It outperforms the current bigwigs in memory models by a mile. This model's got the chops to handle those tough, long-term memory tasks that other models can't touch, especially when it comes to memory-intensive tasks in reinforcement learning.

So, in a nutshell, the research in this paper could really move the needle in the field of reinforcement learning.

### Weaknesses
In reinforcement learning, especially when dealing with "partially observable" environments, effective memory management is really crucial. As task complexity increases, memory demand also skyrockets, and challenges grow alongside it. So, discussing how models "hold up" as tasks become more complex and expansive is pretty important.

### Questions
Hopefully, author interpret HaM in aspect of  "scaling law".

① Performance vs. Memory Size: How does the performance of the Hadamard Memory model scale with increases in memory size? Is there an optimal memory size at which the model's performance peaks?

② Impact of Task Complexity: As task complexity increases, how do the computational requirements and performance of the model change? Can the authors provide metrics to measure the impact of task complexity on model performance?

③ Scalability with Episode Length: Does the Hadamard Memory model maintain stable and efficient updates in longer episodes? Have the authors considered the model's stability and efficiency over extended periods?

### Soundness
4

### Presentation
3

### Contribution
3
