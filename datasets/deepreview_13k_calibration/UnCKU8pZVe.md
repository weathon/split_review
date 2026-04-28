# BOFormer: Learning to Solve Multi-Objective Bayesian Optimization via Non-Markovian RL

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
Bayesian optimization (BO) offers an efficient pipeline for optimizing black-box functions with the help of a Gaussian process prior and an acquisition function (AF). Recently, in the context of single-objective BO, learning-based AFs witnessed promising empirical results given its favorable non-myopic nature. Despite this, the direct extension of these approaches to multi-objective Bayesian optimization (MOBO) suffer from the hypervolume identifiability issue, which results from the non-Markovian nature of MOBO problems. To tackle this, inspired by the non-Markovian RL literature and the success of Transformers in language modeling, we present a generalized deep Q-learning framework and propose BOFormer, which substantiates this framework for MOBO via sequence modeling. Through extensive evaluation, we demonstrate that BOFormer constantly achieves better performance than the benchmark rule-based and learning-based algorithms in various synthetic MOBO and real-world multi-objective hyperparameter optimization problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces BOFormer, a novel approach for tackling multi-objective Bayesian optimization (MOBO) challenges, particularly the non-Markovian nature and hypervolume identifiability issues. BOFormer employs non-Markovian reinforcement learning and sequence modeling, leveraging the Transformer architecture to optimize long-term outcomes. The method demonstrates superior performance in various synthetic and real-world multi-objective optimization scenarios.

### Strengths
The paper introduces an innovative approach by framing multi-objective Bayesian optimization (MOBO) as a non-Markovian reinforcement learning problem. This represents a creative combination of existing ideas from non-Markovian RL and Transformer-based sequence modeling, marking a fresh perspective in the field.
The use of diagrams and examples, such as the hypervolume identifiability issue, aids in understanding complex concepts.

### Weaknesses
1. The discussion of shortcomings in the paper is relatively brief and does not clearly articulate the innovative aspects of the work. Furthermore, the contributions appear to be somewhat incremental rather than groundbreaking.
2. The use of Transformers may require substantial computational resources and memory, which could limit accessibility for some users.
3. The explanations regarding the experimental section lack clarity. The paper does not specify how the proposed algorithm's time efficiency compares to that of other algorithms. Additionally, it is unclear whether the non-Markovian nature of the process consumes more time than a Markovian approach. The improvements over baseline results also do not appear to be significant.

### Questions
1. How does the time efficiency of your proposed algorithm compare to the baseline algorithms?
2. What is the intended meaning of the experimental results in your Figure 3?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces BOFormer, a novel learning-based acquisition function for multi-objective Bayesian optimization (MOBO) that combines reinforcement learning and sequence modeling with Transformers. BOFormer addresses the hypervolume identifiability issue in MOBO, which stems from its non-Markovian nature, by presenting a Generalized DQN framework and substantiating it through sequence modeling.
Several practical enhancements, such as Q-augmented observation representation and prioritized trajectory replay buffer, are incorporated to facilitate the training of BOFormer. Extensive experiments on synthetic and real-world hyperparameter optimization problems demonstrate that BOFormer consistently outperforms various benchmark methods, exhibits cross-domain transfer capabilities, and efficiently transfers learning across different numbers of objective functions.

### Strengths
One of this paper's key strengths is its novel approach to addressing the hypervolume identifiability issue in multi-objective Bayesian optimization (MOBO). By presenting the Generalized DQN framework and implementing it through BOFormer, the authors tackle MOBO's inherent non-Markovian nature. This innovative perspective of reinterpreting MOBO as a sequence modeling problem using Transformers allows for a more effective and efficient solution to the identifiability issue.
Another strength lies in the practical enhancements introduced to facilitate the training of BOFormer. The Q-augmented observation representation provides an informative indicator of the prospective improvement in hypervolume while maintaining a domain-agnostic and memory-efficient representation. The prioritized trajectory replay buffer and off-policy learning enable better convergence and data efficiency during training. Furthermore, the demo-policy-guided exploration ensures efficient search space exploration, which is particularly important given the limited sampling budget in MOBO.

### Weaknesses
Limited theoretical analysis: Although the paper introduces the Generalized DQN framework and provides empirical evidence of its effectiveness, it lacks an in-depth theoretical analysis of the proposed approach. A more rigorous theoretical foundation, including proofs of convergence and optimality, is needed to fully understand the behavior of the algorithm. Specifically, the paper should provide a more detailed analysis of how the proposed loss function relates to the Bellman optimality equations in the context of non-Markovian decision processes, and under what conditions the learned Q-function converges to the optimal Q-function. Without such analysis, it is difficult to assess the robustness and reliability of the method.

Scalability to high-dimensional problems: While BOFormer performs well on the tested problems, its scalability to high-dimensional MOBO problems is not explicitly addressed. The paper does not provide a detailed analysis of how the computational cost of the Transformer-based sequence model scales with the dimensionality of the search space. As the number of dimensions increases, the length of the input sequence to the Transformer also increases, potentially leading to higher computational costs and memory requirements. Further investigation into the scalability of BOFormer, including empirical evaluation on higher-dimensional problems and a theoretical analysis of its computational complexity, would be valuable.

### Questions
How does the Generalized DQN framework differ from the standard DQN in terms of theoretical guarantees and convergence properties? Can the authors provide more insights into the theoretical foundations of their approach?

The paper introduces several practical enhancements, such as Q-augmented observation representation and prioritized trajectory replay buffer. How do these enhancements contribute to the performance of BOFormer individually, and are there any potential synergies or trade-offs between them?

The demo-policy-guided exploration is an interesting concept. How sensitive is BOFormer's performance to the choice of the demo policy, and what are the characteristics of a good demo policy for MOBO problems?

The paper showcases BOFormer's cross-domain transfer capabilities and efficient transfer learning across different numbers of objective functions. Can the authors elaborate on the potential limitations of this transfer learning approach and discuss scenarios where it might not be applicable or effective?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces BOFormer, a novel approach to multi-objective Bayesian optimization (MOBO) that leverages non-Markovian reinforcement learning. The authors' primary contribution is addressing the hypervolume identifiability issue in MOBO through a generalized DQN framework implemented via a Transformer architecture. The work introduces several practical enhancements, including Q-augmented observation representation, prioritized trajectory replay buffer, and demo-policy-guided exploration. The method is comprehensively evaluated on both synthetic functions and real-world hyperparameter optimization tasks for 3D Gaussian Splatting, demonstrating competitive performance against existing approaches. The authors also show promising transfer learning capabilities across different numbers of objective functions.

### Strengths
The authors have identified and thoroughly addressed a fundamental issue in learning-based MOBO approaches - the hypervolume identifiability problem. This represents a significant contribution to the field. The theoretical framework connecting non-Markovian RL to MOBO is rigorously developed and mathematically sound. 

The experimental evaluation is comprehensive, comparing the method against both classical and learning-based baselines across diverse scenarios.

### Weaknesses
The contribution appears somewhat incremental relative to existing approaches like OptFormer and NAP. While the authors introduce novel elements, the core methodology builds heavily on established techniques.

The motivation for using Transformers in this context needs stronger justification. Given the small data regime typical in Bayesian optimization, the choice of a Transformer architecture, which typically requires substantial data for effective training, requires more thorough explanation. Specifically, the paper does not adequately address why a Transformer is superior to simpler architectures, such as an MLP, for learning the acquisition function in this context. The high parameter count of Transformers also raises concerns about overfitting, which is not sufficiently addressed.

The theoretical justification for computational intractability due to "curse of dimensionality" (line 244) requires more precise argumentation and supporting references. The argument that the state and action spaces are uncountably large is not unique to this method and applies to many BO approaches. The paper needs to more clearly articulate why the multi-step lookahead policy makes this problem intractable in a way that is specific to the proposed approach.

### Questions
Could you provide details about the experimental methodology, specifically:
- How many random repetitions were performed to ensure statistical significance?
- Were the same network architectures used consistently across all experiments?
- What are the specific architectural details of the Transformer implementation?
- How was stability analysis conducted? ie, stability wrt different transformer models and also different initialization.

Would it be possible to present results on more challenging problems requiring significantly more than 100 samples? The current evaluation up to 100 samples may not fully reflect real-world BO scenarios.

The method's effectiveness with limited data (approximately 10 samples) is surprising given the typically large parameter count of Transformer architectures. Could you elaborate on how this is achieved?

How does the method's performance scale with increasing problem complexity and dimensionality?

Could you provide a more detailed justification for choosing a Transformer architecture in this small data regime compared to simpler alternatives?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces BOFormer, a learning-based approach for Multi-Objective Bayesian Optimization (MOBO). The key idea is to replace the traditional handcrafted acquisition function with a Transformer-based network trained through non-Markovian reinforcement learning. The authors claim that MOBO is inherently non-Markovian due to the "hypervolume identifiability issue" and propose a generalized DQN framework incorporating historical information. The method is evaluated on both synthetic functions and real-world hyperparameter optimization tasks.

### Strengths
* While there are several existing works on meta-learned acquisition functions for single-objective BO, BOFormer is the first work to apply a learning-based acquisition function to MOBO.
* The domain-agnostic representation, which only incorporates historical query information rather than maintaining information for all domain points, enables cross-domain transfer while being memory-efficient.
* Well-structured related work with clear categorization of existing approaches and insightful comparison with similar works, especially in distinguishing the unique aspects of BOFormer from OptFormer and NAP.
* The paper provides a comprehensive evaluation on various synthetic functions and real-world hyperparameter optimization tasks, both show strong performance of BOFormer. Besides, the paper conducts an additional ablation study on sequence length.

### Weaknesses
 * I have some doubts about the non-Markovian nature of MOBO. If we define the state as the complete set of historical queries along with the posterior distribution of candidate points, the problem naturally becomes Markovian, as the hypervolume improvement can be uniquely determined from this state representation. The non-Markovian property in your approach appears to be artificially induced by your choice of a simplified state representation. Please correct me if I am wrong or if I misunderstood something, as I am not from the field of reinforcement learning.
* A major weakness lies in the methodology section, particularly in the insufficient details about BOFormer. Figure 2 is not thoroughly discussed; for instance, positional encoding appears in the architecture diagram but is never mentioned in the text, while Equation 5 already seems to contain temporal information. Moreover, it's unclear how j/t in Equation 5 is combined and encoded with other inputs, as it appears to be merely an arithmetic sequence (e.g., numbers from 0.1 to 0.9 when t=10). Additionally, the introduction of Off-Policy Learning and Prioritized Trajectory Replay Buffer feels abrupt - what problems are they addressing? There's no proper introduction or motivation. I suggest the authors improve this section to present the problems and their solutions more clearly to readers.
* Another concern is the temporal information in the history representation. In BO, the historical queries should be permutation-invariant - the order of previous queries should not affect future decisions. However, by incorporating explicit temporal information, the method might be breaking this consistency. Or have you observed any benefit of incorporating temporal information? And is there any ablation study showing the impact of it?
* The paper lacks some experimental details. E.g., no configuration of the surrogate model such as the choice of the kernel and hyperparameters; Training cost for meta-training not reported.
* The paper contains several mathematical formulation issues and inconsistencies. E.g., Line 345, shouldn't it be $max$?; Line 347, I guess it should be $i$-th objective as $j$ is the time step; Inconsistent index notation, in line 344, $i$ indexes objective functions: $i \in [1,···,K]$, while in the equation at line 374, $i$ represents time steps; Line 225, the hypervolume formula contains an unexplained $x'$ that appears redundant; Line 819, shouldn't it be uniform distribution?
* There is no discussion about Figure 3, it might be better to give an introduction about performance profiles.
* There is no experiment to support the idea of demo-policy-guided exploration, thus it is hard to see the effect of this enhancement.
* Minor issues: Line 201: Incorrect appendix reference (B.2 instead of B); Line 820: Incomplete sentence ending abruptly.

### Questions
* Regarding OptFormer Implementation, how did you adapt OptFormer for MOBO? To my understanding it was originally designed for single-objective HPO tasks. Did you retrain the model from scratch for MOBO or fine-tune the existing model? It would be great if you could add some details for the baselines you compared with.
* Have you tried to compare the direct implementation you mentioned in Section 4.1 with your proposed method?
* I assume BOFormer can only accept discrete inputs, how does the method handle continuous domains in practice? Are there any discretization issues?

### Soundness
3

### Presentation
2

### Contribution
2
