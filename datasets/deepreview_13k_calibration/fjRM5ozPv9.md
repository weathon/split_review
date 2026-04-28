# Local-Forward: Towards Biological Plausibility in Deep Reinforcement Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6

## Abstract
A lasting critique of deep learning as a model for biological intelligence and learning is the biological implausibility of backpropagation.
Backpropagation requires caching local outputs and propagating a global error via derivatives, neither of which are known to be implemented by biological neurons.
In reinforcement learning, building more biologically plausible agents would allow us to better model human cognition and social behavior, and improve computational efficiency.
We propose Local-Forward, a new temporal-difference learning algorithm (and associated architecture) that trains neural networks to predict Q-values.
Rather than backpropagating error derivates, we rely on updates that are local to each layer of the architecture and additionally use forward connections in time to pass information from upper layers to lower layers via activations. Our approach builds on the recently proposed Forward-Forward algorithm, as well as recurrence and attention in neural architectures. 
This approach no longer suffer the aforementioned contradictions with biology.
Furthermore, as a proof-of-concept, we train reinforcement learning agents with Local-Forward to solve control tasks in the MinAtar environments, and show that our method's potential warrants further investigation because it opens avenues for more computational efficient training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes "Local-Forward," a method that combines an ad-hoc neural architecture (L-F cells) and a reinforcement learning strategy, overall avoiding backpropagation of the gradients.

### Strengths
The paper is well-written, and the presentation is optimal. As a general comment on the experimental results, I think they are well-described and well-commented. 
I also particularly appreciated the "Limitations" section.

### Weaknesses
1. I would avoid making claims that are hard, if not impossible, to substantiate, such as the one in the first bullet point at the end of the introduction: "We propose an alternative to backpropagation for reinforcement learning that does not suffer contradictions with known biology." I suggest making this statement somewhat less definitive. The current phrasing implies a direct correspondence with biological neural networks, which is a strong claim that requires substantial evidence and a more nuanced discussion of the biological plausibility of the proposed mechanisms. Without such evidence, the claim appears speculative and could be misleading.

2. You initially define the value function with the symbol $\mathcal{Q}$ at the beginning of section 2.1,  but then you go on to use the symbol $Q$. Moreover in the recursive relation for $Q$ some lines below in the lhs you have $Q^\pi$ while in the rhs you dropped the "policy" superscript. Is this intentional? The inconsistent notation makes the equations harder to follow and raises questions about whether the different symbols represent distinct concepts or are simply used interchangeably. This lack of clarity can lead to confusion and misinterpretation of the mathematical framework.

3. I would spend some more words to describe who are and how the matrices $W_{\rm in}$ and $W_{\rm query}$ act; probably inserting them also in Figure~2 would help. The current description of these matrices is too brief, leaving the reader unclear about their specific roles in the computation. A more detailed explanation, possibly with a visual representation in Figure 2, would greatly enhance the understanding of the proposed architecture. Specifically, it is unclear how these matrices transform the input and what kind of operations they perform.

4. Conventionally the "argmax" indicates a set (of all the points I which the function at hands assume minimal value), but in all your formula,  you use it as if it were a real number. I would suggest to either clarify this or consider using a different notation. For instance is Algorithm 1 I would write $a_t\in {\rm arg max} \dots$ rather than $a_t = {\rm arg max} \dots$

### Questions
How do you explain that in some experiments, it is possible to achieve decent results without forward connections? If I've understood correctly, aren't the forward connections the ones that provide an information signal from higher layers?

### Soundness
3 good

### Presentation
4 excellent

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
This work employed a recently proposed algorithm known as the Forward-Forward algorithm, instead of Back-Propagation, to train deep neural networks in the context of reinforcement learning tasks.

### Strengths
The author has clearly delineated both the work already accomplished and the work that remains to be done.

### Weaknesses
The main drawback of the article lies in its lack of substantial content. Specifically, the experimental content is minimal, lacks robustness, and lacks detail or novelty. Since this paper does not introduce any novel methods, and the author simply applies the existing FF algorithm to RL tasks, it is essential for the author to thoroughly evaluate the differences between FF and BP algorithms in the context of RL tasks. In terms of experiments, there are several areas that need improvement:

1. FF algorithm - There are multiple variations of the FF algorithm, and the author should consider testing more than one rather than relying solely on a single FF algorithm. It is not clear why the authors chose this specific variant of FF, and a more thorough exploration of the design space is needed. The authors should also provide a more detailed explanation of the specific FF variant they used, including any modifications or adaptations they made for the RL setting. Without this, it is difficult to assess the validity of their results.

2. RL algorithms - Beyond just Q-learning, the author should explore other RL algorithms to provide a more comprehensive analysis. The authors should consider algorithms such as policy gradient methods (e.g., A2C, PPO) or actor-critic methods to demonstrate the generalizability of their approach. The current focus on Q-learning limits the scope of the analysis and makes it difficult to draw broad conclusions about the applicability of the FF algorithm to RL tasks.

3. RL tasks - The paper only covers five basic tasks, but it would be beneficial for the author to expand their analysis to a wider range of tasks to effectively compare FF and BP. The MinAtar suite, while useful, is limited in its complexity and diversity. The authors should consider more challenging environments, such as those found in the OpenAI Gym or DeepMind Control Suite, to provide a more robust evaluation. The current set of tasks is insufficient to demonstrate the potential of the FF algorithm in more complex scenarios.

In the analysis, the current focus is primarily on performance. However, it would be beneficial for the author to explore and compare other aspects impacted by FF and BP algorithms, thus enhancing the depth of the article. For example, the authors could analyze the computational cost, memory usage, and convergence speed of the FF algorithm compared to BP. Such an analysis would provide a more complete picture of the strengths and weaknesses of the proposed approach.

### Questions
Section 2.1, the sixth line, this formula is written incorrectly.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper "Local-Forward: Towards Biological Plausibility in Deep Reinforcement Learning" critiques the biological implausibility of backpropagation in deep learning. It introduces "Local-Forward", a temporal-difference learning algorithm that predicts Q-values without backpropagating error derivatives. Instead, it employs local updates and forward connections in time to convey information between layers. This approach, inspired by the Forward-Forward algorithm and attention mechanisms, aims to better model biological neural networks. The method is tested on MinAtar environments, emphasizing its potential for more efficient training and its alignment with biological processes.

----- After rebuttal -----

I appreciate the additional experimental results and clarification from the authors. I feel most of my concerns are addressed. I changed my rating from 3 to 6 accordingly.

### Strengths
- The paper is written clearly and smooth to follow.
- Exploring the application of Forward-Forward algorithms in various field such as deep RL is an interesting direction to explore.
- The experimental results show the effectiveness of the proposed Local-Forward algorithm, which has probably large future potential.
- The algorithm is novel to my knowledge.

### Weaknesses
## Major weakness

- Inadaquent disucssion about and comparison with related methods, especially backprop-free algorithm in Deep RL. See my questions below.

- Lack of depth in experimental evaluations. The paper could benefit from more comprehensive analysis and wider range of testbeds. See my questions below.


## Minor

- There is not enough background knowledge about the forward-forward algorithm. Sec. 2.2 only describes the rough idea of it, but not the detailed mathematics of how it works. This is important because it is the basis of the proposed Local-Forward algorithm.

- While the claim is "we do not propagate any loss signal between cells", actually the reward signal is used globally (Alg. 1). This should be clarified.

### Questions
1. There exist other backprop-free learning algorithms such as [a,b] and evolutionary algorithms like CMA-ES [c, d], which can be used for deep RL, how do your method compare with them? I believe a performance / computation cost comparison with them could consolidate the advantage of the proposed Local-Forward model. 

2. What are the design motivation of the proposed Local-Forward cell (Fig.2)? The authors state that "The concept of a cell is reminiscent of the design of a rnn". However, MinAtar tasks are MDPs and can be handled by feedforward NN, why the paper tries to solve MinAtar with recurrent connections?

3. I am also curious about the performance of Local-Forward in supervised learning tasks such as MNIST and CIFAR. It does not need to be very good since the method is designed for TD-learning, but such additional experimental results may provide better understanding of the suitable scope of the proposed model.

4. What are the computational cost of Local-Forward compared with DQN? e.g., clock time, num of model parameters, FLOPS. As each layer computes Q value, is it more computationally expensive than DQN?

5. Are there any additional biological insights of the Local-Forward model rather than it can solve MinAtar? For example, how the internal representation of neurons compare with animals' neurons and DQN's neurons.


### Reference

[a] Ororbia A, Kifer D. The neural coding framework for learning generative models[J]. Nature communications, 2022, 13(1): 2064.
[b] Ororbia A G, Mali A. Backprop-free reinforcement learning with active neural generative coding[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2022, 36(1): 29-37.
[c] Hansen N, Ostermeier A. Completely derandomized self-adaptation in evolution strategies[J]. Evolutionary computation, 2001, 9(2): 159-195.
[d] Ha D, Schmidhuber J. Recurrent world models facilitate policy evolution[J]. Advances in neural information processing systems, 2018, 31.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
