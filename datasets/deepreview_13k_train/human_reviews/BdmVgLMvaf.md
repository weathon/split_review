# Adaptive teachers for amortized samplers

- Decision: Accept
- Scores: 5, 8, 8, 5

## Abstract
Amortized inference is the task of training a parametric model, such as a neural network, to approximate a distribution with a given unnormalized density where exact sampling is intractable. When sampling is implemented as a sequential decision-making process, reinforcement learning (RL) methods, such as generative flow networks, can be used to train the sampling policy. Off-policy RL training facilitates the discovery of diverse, high-reward candidates, but existing methods still face challenges in efficient exploration. We propose to use an adaptive training distribution (the \teacher) to guide the training of the primary amortized sampler (the \student) by prioritizing high-loss regions. The \teacher, an auxiliary behavior model, is trained to sample high-error regions of the \student and can generalize across unexplored modes, thereby enhancing mode coverage by providing an efficient training curriculum. We validate the effectiveness of this approach in a synthetic environment designed to present an exploration challenge, two diffusion-based sampling tasks, and four biochemical discovery tasks demonstrating its ability to improve sample efficiency and mode coverage.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed a method to improve mode coverage and training efficiency in amortized inference methods like GFlowNets. Specifically, the authors use offline RL training to encourage the discovery of diverse, high-reward candidates, and addressed the key challenge -- exploration in off-policy RL. The main idea is to use an adaptive "Teacher" model to help the "Student" sampler by focusing on regions with high loss. The teacher model is used as as an auxiliary model, is trained to target areas where the Student model has high errors. This allows it to cover unexplored modes (which usually have high errors) and provide a more efficient training process. Empirically, the authors show that this approach works well in various tasks, such as discrete sequence design and continuous diffusion sampling, with better sample efficiency and mode coverage.

### Strengths
1. The idea of exploring high-error region and increase the sampling probability of data in these region for training the student model intuitively makes sense to me, which is essentially resembles to hard-negative mining in the classic machine learning literature.

2. The experiments were well-executed and supports the main claim in the paper.

3. The math on GFlowNets and their connection to amortized inference is helpful, especially helps contextualize the significance of the contributions.

### Weaknesses
1. The idea is not new; it closely resembles hard negative mining (i.e., sampling negative examples where the model shows high error), which limits the novelty of the proposed approach.

2. While the idea of sampling more in high-error regions seems intuitively reasonable, its effectiveness may depend on whether the student model has sufficient capacity to fit the distribution. Also, I would like to see more comparisons and discussion with the active learning literature, such as uncertainty sampling, etc.

### Questions
Can the author explain why you chose GFlowNets for the experiments? Are they more effective than diffusion models for chemical or drug discovery? In my understanding, diffusion models can fairly easily to fit multimodal distributions.

### Soundness
2

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
3

### Summary
The paper presents a novel method to improve amortized inference for complex distributions using an adaptive "Teacher-Student" training framework. The Student is an amortized sampler parameterized as a generative flow network (GFlowNets) and trained using RL. The primary contribution of the work is introducing the Teacher as an auxiliary  model that acts as the 'exploration policy' for the student. It is trained to guide the Student training by focusing on high-loss regions, thereby promoting the discovery of unexplored modes of the target distribution. The proposed method is evaluated on synthetic environments, diffusion-based sampling tasks, and biochemical discovery tasks, demonstrating improved mode coverage and sample efficiency.

### Strengths
**Strengths** : 
- Addresses an important problem: Mode coverage/exploration is an important problem in the training of GFlowNets. The paper proposes a novel and interesting solution to the problem.

- Very Well written :  I really enjoyed reading the paper. The paper did an excellent job of introducing and walking through the relevant literature and the methods and putting itself in context. Although I was not myself very familiar with the specific work line of work around GFlowNets, I was easily able to follow along all the details. 

- Lots of interesting details : The training formulation was interesting, especial given I wasn't very familiar with the glownets literature before this. I also particularly liked the use of a search procedure combined with the Teacher network to reduce the teacher network induced bias in the exploration process (although this was already introduced in previous work!). This approach effectively guides the student towards more diverse solutions, improving the overall learning efficiency and robustness. 

- Impressive empirical results: The paper demonstrates the versatility of the Teacher-Student framework by applying it to a range of tasks, including synthetic benchmarks and biochemical discovery problems. The empirical results consistently show that the Teacher-Student setup leads to better mode coverage and training efficiency compared to existing methods. Especially the results in more complicated tasks with a large number of modes.

### Weaknesses
 **Weaknesses/Questions**
-  The introduction of an adaptive Teacher adds additional complexity to the training process, requiring the joint optimization of both Teacher and Student networks. At least in the RL literature, these types of exploration methods were tried and given up on as they required extensive tuning and didn't scale well enough. I'm curious how the authors think that compares with the use cases here and if the authors genuinely believe the results shown in the paper will hold the test of time?

- This is maybe a dumb question. But I do wonder how these methods compare with using standard sampling based strategies for mode discovery e.g  thompson sampling etc. My understanding is those become intractable as the problem size increases. The approach suggested seems pretty complex and I do wonder if the those standard mode discovery methods could've helped make things simpler. 

- Details on the biochemical discovery experiments were a little unclear. Eg. How do you define the reward function etc was not very clear to me.

### Questions
same as weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work focuses on the efficient exploration of RL training during amortized inference. The primary contribution lies in developing an adaptive training distribution to guide the amortized sampler in prioritizing difficult ones. The proposed method is examined in a collection of benchmarks, including both synthetic and real-world scenarios. The exploration efficiency and other benefits are reflected in both mode coverage and sample efficiency.

### Strengths
I can easily follow this work, and this work tries to amortize prediction by simply conditionally inputting some variables.

Overall, (1) I find this work easy to follow with clear motivations. Decision-making for amortized inference, particularly the development of GFlowNets, is impactful, and this work focuses on an important issue, namely efficient exploration under RL frameworks in the field. (2) The developed strategy is novel and practical in implementation. (3) The experiments are inspiring and well-supported claims.

### Weaknesses
While a lot of merits in this work, I find some parts are necessary to modify or revise.

---

(1) It seems to lack the necessity of amortized inference. In line28-30, it states the mechanism of amortized inference and related bottleneck. It is necessary to include the role of amortized inference compared with traditional methods such as MCMC, e.g., citing [1] and adding something like

"The amortized inference adopts a shared inference module for all data points instead of performing inference one by one. In this way, we can reuse the computational module for other data point's inference."

(2) There exists literature work [2] that raises similar learning modules in terms of training adaptative distributions for few-shot experimental design; it is necessary to discuss them in detail in Section 4 related work.


(3) Other suggestions or questions: (i) Figure 1 is clear enough, but I am not sure whether there should exist links between the Buffer and the Teacher or the Student to reveal the data flow. (ii) in Line-74, it says "we believe that trajectories with high loss are particularly informative for mode coverage", is this a hypothesis? Are there any explanations from either experiments or other intuitions? (iii) In Line 60, it says "the Student's target distribution does not depend on the Teacher", hence I am wondering whether the optimization pipeline is an adversarial game. (iv) In line 237, I want to know how to balance the student, the teacher or a buffer.

### Questions
See Weakness part

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method for training a neural network to approximate a distribution with a specified unnormalized density. Specifically, it proposes an adaptive training distribution, termed the "Teacher," which guides the primary amortized sampler, or "Student," by prioritizing high-loss regions.

### Strengths
The Teacher model has the potential to generalize across the Student's high-loss regions, thereby improving mode coverage. The algorithm’s effectiveness is demonstrated through both discrete and continuous tasks, comparing favorably against other GFlowNet algorithms.

### Weaknesses
This paper appears to fall slightly below the standard expected at ICLR for several reasons:

1. A critical issue is the lack of a solid theoretical foundation; the paper primarily reports numerical results without a deeper mathematical analysis. For instance, there is no mathematical description or guarantee of convergence rate for Algorithm 1. The absence of a convergence proof, or even a discussion of the conditions under which convergence might be expected, significantly weakens the theoretical contribution. Furthermore, the paper does not discuss the potential for the algorithm to get stuck in local optima, a common issue in sampling methods.

2. Regarding the experiments, the explanation of the architecture design and the choice of hyperparameters would benefit from greater clarity and justification. I will outline these concerns in more detail in the questions below. Specifically, the paper lacks a clear rationale for the specific neural network architectures used for each task. The number of layers, hidden units, and activation functions are not justified, making it difficult to assess the robustness and generalizability of the results. The choice of hyperparameters, such as learning rates, batch sizes, and optimization algorithms, is also not well explained, raising concerns about the reproducibility of the experiments.

### Questions
1. Convergence Rate of Algorithm 1: What is the convergence rate of your Algorithm 1? Although it performs well in exploring more modes in the example tasks, the convergence rate is also a key factor in sampling methods. Could you provide more details on this?

2. Selection of Behavior Policy: How did you determine the behavior policy during training (line 220)? From lines 827 to 831, it appears that different tasks require different ratios. What standard guided these choices? The explanation on lines 835 to 840 lacks proof of the algorithm’s robustness across different ratios, which raises concerns about whether these choices were made deliberately and may impact the generality of the results. The same issue applies to the choice of C in Table 5 and α in Tables 6 and 7.

3. Choice of Backward Policy: How did you select the backward policy during training? It appears that a uniform random policy is used in the deceptive grid world and biochemical design tasks. In my understanding, the backward policy in your algorithm plays a role similar to the proposed transition kernel in MCMC, which is crucial for convergence. Could you elaborate on the role of the backward policy in your algorithm and its impact on the convergence rate of Algorithm 1 across different tasks?

4. Algorithm Performance on High-Dimensional Tasks: How does the algorithm perform in high-dimensional tasks? Sampling from a specified unnormalized density is particularly challenging in high dimensions. Testing the algorithm on high-dimensional tasks could strengthen the evaluation of its effectiveness.

5. Performance in the Manywell Task: In the Manywell task, the performances of PER+LS and the Teacher-based methods appear similar (table 8). What is the underlying intuition for this?

I would be willing to increase the score if the above questions could be well clarified.

### Soundness
3

### Presentation
3

### Contribution
2
