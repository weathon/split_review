# Transformers Learn Temporal Difference Methods for In-Context Reinforcement Learning

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
In-context learning refers to the learning ability of a model during inference time without adapting its parameters. The input (i.e., prompt) to the model (e.g., transformers) consists of both a context (i.e., instance-label pairs) and a query instance. The model is then able to output a label for the query instance according to the context during inference. A possible explanation for in-context learning is that the forward pass of (linear) transformers implements iterations of gradient descent on the instance-label pairs in the context. In this paper, we prove by construction that transformers can also implement temporal difference (TD) learning in the forward pass, a phenomenon we refer to as in-context TD. We demonstrate the emergence of in-context TD after training the transformer with a multi-task TD algorithm, accompanied by theoretical analysis. Furthermore, we prove that transformers are expressive enough to implement many other policy evaluation algorithms in the forward pass, including residual gradient, TD with eligibility trace, and average-reward TD.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper shows that linear transformers can execute TD(0) over their context both by constructing the matrices that would do so, but also by showing a pre-training method that gives rise to such properties. Finally they show similar constructions for other Policy Evaluation algorithms like TD-lambda, Average-Reward TD etc. Besides some empirical evidences the paper presents many proofs of its statements.

### Strengths
The paper argues with proofs and empirical evidences for its results and is able to remove any possible doubt of their veracity. Furthermore it's a novel exploration of the capabilities of linear transformers and further helps the understanding of In-Context Reinforcement Learning.

### Weaknesses
The title of the paper is rather strong, not only is the paper only about Linear Attention, as opposed to the commonly used Softmax attention, but also they prove that transformers with a specific kind of training implement TD-Learning, so I believe "Transformers Can Learn Temporal Difference Methods for In-Context Reinforcement Learning" would be more appropriate.  Furthermore one must wonder how relevant is studying Reinforcement Learning implemented by linear attention over such short horizons such as 40 steps, as most RL problems involve orders of magnitude longer trajectories, whereas attention tends to become computationally expensive and lose precision as the context length grows.

### Questions
1. Would it be possible for the authors to change the paper's title to something that better reflects what is shown by the paper?
2. Could the authors better justify the study of In-Context RL, both for Linear Attention-based transformers and otherwise?

### Soundness
4

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
The authors performed a mathematical analysis of the transformer architecture commonly used in the field of in-context reinforcement learning (ICRL). They proved that when a transformer with a linear attention structure is trained to estimate value functions in a multi-task environment, the forward pass within the transformer becomes equivalent to temporal-difference (TD) learning in reinforcement learning. Even when out-of-distribution task contexts are provided as input to the transformer, this TD learning effect is induced internally, enabling it to estimate the correct value function. The authors experimentally demonstrate this in a simple Boyan's chain environment.

### Strengths
1. The authors mathematically analyze that defining a Transformer as a value function estimator and training it in a multi-task environment makes the attention mechanism within the Transformer equivalent to TD(0) learning. The proof process appears to be concrete, and the resulting application seems straightforward. Particularly, while previous reinforcement learning studies using Transformers have merely mentioned its high performance, this paper analyzes why the Transformer structure works so effectively. In this regard, this paper seems to present a notable novelty. 

2. The authors mathematically demonstrated that the internal operations of the transformer can be extended not only to TD(0) learning but also to various RL algorithms, such as TD($\lambda$), average reward TD, and residual gradient. This suggests that these algorithms can be applied in diverse ways to approximate a generalized value function through a transformer. 

3. The proposed theorems and corollaries in the paper are meticulously detailed in the appendix, where each proof is presented with clarity and rigor. This comprehensive approach allows readers to follow the logical reasoning behind each statement. This thoroughness underpins the robustness of the paper and enhances its reproducibility, which will be beneficial for future researchers.

### Weaknesses
1. The experimental setup and evaluation metrics may not effectively demonstrate the algorithm's impact. The authors defined the value function estimation error for new states in out-of-distribution (OOD) tasks as the evaluation metric in Figure 1. However, since the Boyan's chain environment is relatively simple, it's possible that generalization effects could also be achieved using standard architectures like MLPs and RNNs, resulting in graphs similar to those in Figure 1. This raises the question of whether the results in Figure 1 reflect the effects of the transformer's in-context TD learning or if they could be similarly obtained with conventional networks. To address this, it seems the authors should consider conducting comparative experiments, specifically with architectures known to struggle with in-context learning tasks, to isolate the unique contributions of the transformer architecture in this setting.

2. The comparison experiments seem insufficient. If there were experiments comparing value estimation between the authors' proposed value-estimating Transformer algorithm and existing reinforcement learning algorithms that utilize Transformers (other than behavior cloning methods), it would support the claim that the proposed algorithm is more effective. Although this paper focuses more on mathematical analysis, it seems to not have enough experiments on other algorithms or tasks. The absence of such comparisons makes it difficult to assess the practical significance of the theoretical findings. For instance, comparing against a transformer trained with a standard RL algorithm like DQN or PPO would help clarify if the in-context TD learning provides any performance advantage, or if it simply replicates the behavior of existing methods.

3. The paper appears to be written in a way that makes it difficult to read. It seems to borrow equations and results from previous studies, but the notation and equations are challenging to follow at first glance. For instance, it is hard to understand how equations like Equation (4) were derived. A brief explanation of the existing equations would be helpful, particularly clarifying the connection between the linear attention mechanism and the scalar output used for value estimation. The paper would benefit from a more self-contained presentation, with clear definitions of all symbols and a more detailed explanation of how the equations are derived from the underlying transformer architecture.

### Questions
1. The authors explain that in-context TD learning occurs when the task distribution is sufficiently challenging. I wonder why such a phenomenon occurs. They trained the transformer across thousands of Markov Reward Processes. Also, I wonder if the same TD learning effect would emerge internally within the transformer if it were trained in a single-task setup rather than a multi-task one.

2. In most prior research, transformers are directly applied to perform control tasks. However, in this paper, the transformer is used to estimate the value function. While a generalized approach to value function estimation is indeed important in reinforcement learning, this study does not directly address the control problem in RL. I would be interested to hear the authors' perspective on how their approach could be applied to control tasks in future research.

3. When a transformer estimates the value function, its internal operations align with TD learning. Most transformers, however, serve as policies rather than value function estimators. It would be interesting to know the authors’ perspective on whether, if the transformer were to act as a policy instead of estimating a value function, the internal operations would still resemble TD learning, or if another reinforcement learning algorithm would take place internally.

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
This paper provides theoretical analysis on the equivalence between a forward pass and in-context TD in a simple setting - linear single-layer transformers.

### Strengths
It is a new try and an interesting direction to investigate the equivalence between transformers and in-context TD.

### Weaknesses
1. Many of the proofs rely on strict initial conditions, like specific embeddings and matrix structures. The validity of these proofs depends heavily on these controlled setups, which may not be feasible or sustainable in more complex, real-world settings. As a result, some claims in the paper appear intuitive and unsubstantiated. Specifically, the theorems often require very particular forms for the weight matrices and embeddings, such as specific diagonal or block-diagonal structures. These constraints are not naturally guaranteed by standard training procedures, and the paper does not adequately address how these structures might emerge or be maintained during training in more complex scenarios. The reliance on these highly constrained setups makes it difficult to generalize the theoretical results to more realistic settings, where such precise parameter alignments are unlikely to occur.

2. While the paper claims the emergence of in-context TD learning through multi-task TD pretraining, the empirical analysis is constrained to quite simple tasks. The tasks used in the empirical analysis, such as simple grid-world environments, are not representative of the complexity found in real-world reinforcement learning problems. The paper needs to demonstrate the emergence of in-context TD learning on more complex tasks with higher-dimensional state spaces and more intricate dynamics. The current empirical results, while suggestive, are not sufficient to support the broad claims made about the generalizability of the proposed approach.

### Questions
1. In Corollary 3, the authors show that the transformer can implement TD(λ) updates with a specific mask matrix, $M_{TD(\lambda)}$. The matrix structure requires strict alignment of eligibility traces, which might be difficult to achieve in real tasks where temporal dependencies and eligibility traces shift dynamically. 

2. Lines 523-524 in the Conclusion are unclear. Are you trying to emphasize that policy iteration or optimization forms the key foundation?

3. In Lines 531-532, the claim seems unsupported; working well in a small-scale setting doesn’t necessarily imply the same for larger, more complex tasks.

### Soundness
3

### Presentation
2

### Contribution
3
