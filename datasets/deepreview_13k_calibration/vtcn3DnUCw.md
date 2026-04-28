# LASER: Attention using Exponential Transformation

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Transformers have had tremendous impact for several sequence related tasks, largely due to their ability to retrieve from any part of the sequence via softmax based dot-product attention. This mechanism plays a crucial role in Transformer's performance.  We analyze the gradients backpropagated through the softmax operation in the attention mechanism and observe that these gradients can often be small. This poor gradient signal backpropagation can lead to inefficient learning of parameters preceeding the attention operations. To this end, we introduce a new attention mechanism called LASER, which we analytically show to admit a larger gradient signal. We show that \laserattn can be implemented by making small modifications to existing attention implementations. We conduct experiments on autoregressive large language models (LLMs) with upto 2.2 billion parameters where we show upto 3.38\% and an average of $\sim$1\% improvement over standard attention on downstream evaluations. Using LASER gives the following relative improvements in generalization performance across a variety of tasks (vision, text and speech): 4.67\% accuracy in Vision Transformer (ViT) on Imagenet, 2.25\% error rate in Conformer on the Librispeech speech-to-text and 0.93\% fraction of incorrect predictions in BERT with 2.2 billion parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper first analyzed the gradient vanishing problem in the standard softmax attention. To mitigate this issue, this paper proposed LASER attention, which first apply exponential function to the values in attention then take the log of the attention output. The authors clear explain why LASER attention mitigate the small gradient issue in theory. 

Experimentally, the authors reported results in language modeling, image classification on ImageNet and speech-to-text generation. LASER attention achieved improvements over standard softmax attention on all these tasks.

### Strengths
1. The proposed LASER attention is theoretically grounded.

2. The authors provided an simple implementation of LASER attention by leveraging the log-sum-exp operation.

3. The experimental results demonstrates the effectiveness of LASER attention.

4. The paper is well-written, easy to follow.

### Weaknesses
1. In auto-regressive language modeling experiments, all the models are trained with context length 1024. No experimental results are reported for long-context training and evaluation.

2. When designing a new architecture, training stability is an important factor in consideration. However, there are no analysis in this paper to compare the training stability of LASER and the standard softmax attention.

### Questions
1. Are the language models trained using precision BF16 or FP32? Is LASER attention more stable (less training spikes)  or not?

2. Is LASER attention slower than standard softmax attention. Any efficiency analysis?

### Soundness
3

### Presentation
3

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
This paper addresses the gradient vanishing issue in transformer models, a challenge that limits the effectiveness of deep learning in capturing long-range dependencies. To tackle this, the authors introduce LASER attention, a novel adjustment to the attention mechanism that uses a log-sum-exp transformation on exponentially scaled inputs to improve gradient propagation. This approach avoids gradient vanishing more effectively than traditional softmax-based attention mechanisms. The authors provide a new implementation, Weighted-Sum-Exp trick, to prevent overflow issues and demonstrate that LASER attention improves model performance across various transformer architectures and tasks. Empirical results show notable gains in accuracy and reduction in error rates in speech, vision, and language models, making LASER attention a feasible and efficient alternative for large-scale transformer applications.

### Strengths
1. Author present a modified attention mechanism for transformers that addresses the gradient vanishing issue by utilizing a log-sum-exp transformation. 
2. LASER presented algorithm enhances gradient propagation without the need for complex changes to existing architectures.

### Weaknesses
1.	Evaluation in Table 2 of the LLM can be expanded to include retrieval and generation tasks, such as those demonstrated in Scrolls (see: https://arxiv.org/pdf/2201.03533) and Needle In A Haystack (see: https://github.com/gkamradt/LLMTest_NeedleInAHaystack).
2.	It would be interesting to know if LASER is still compatible with LoRA.
3.	A speed comparison between LASER and vanilla attention during both training and inference phases would be helpful.
4.	The author operates decoder-only causal language models ranging from 234 million to 2.2 billion parameters. A comparison of loss across all these models would help demonstrate LASER’s scalability from smaller to larger models.

### Questions
Beyond the weakness, the presentation of table and chart be imporved.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces LASER attention, a new attention mechanism designed to improve the gradient propagation in Transformers by replacing the standard softmax-based attention. The softmax operation in traditional attention mechanisms can limit learning due to small gradient backpropagation, while LASER attention uses a log-sum-exp structure to allow larger gradient signals, enhancing model training.

### Strengths
1. The motivation of this paper is insightful.
2. LASER attention is straightforward to implement, requiring minimal adjustments to current attention models.
3. The experiments are quite comprehensive, verifying the effectiveness of LASER across different modalities.

### Weaknesses
My only concern is whether this paper addresses **an issue that standard attention cannot resolve**. If standard attention is suboptimal due to small gradient backpropagation, this could potentially be improved by adjusting the temperature of the softmax (i.e., scaling its input). I suggest that the paper examine the impact of temperature both theoretically and experimentally.

### Questions
Please incorporate the temperature of softmax into the theoretical derivations and comparative experiments.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the limitation of the softmax operation, which tends to backpropagate small gradients, potentially slowing down learning. To address this, the authors introduce a new attention primitive called LASER. LASER applies attention on exponentially transformed inputs, adopting a log-sum-exp structure. The authors demonstrate LASER's effectiveness through evaluations on language modeling, vision, and speech recognition tasks.

### Strengths
The paper is well-written, with a clearly motivated problem that addresses a meaningful limitation in current attention mechanisms. The proposed solution is notably simple, requiring minimal modifications to the original attention mechanism, allowing easy integration into existing system implementations. Additionally, the authors evaluate their new attention primitive across a broad and diverse set of tasks, effectively demonstrating its versatility and effectiveness.

### Weaknesses
My primary concern is the significance of the observed improvement. In Table 2, the average improvement of LASER over the standard attention mechanism across all benchmarks is less than 1%. It would be helpful to see the natural fluctuations on these benchmarks to better assess the statistical significance of this improvement. Additionally, although LASER shows a lower loss in the training curve, it is unclear if LASER merely offers faster convergence rather than a genuinely better final performance. To clarify this, the authors could extend the training schedule to verify that both models have indeed converged, demonstrating that LASER not only converges faster but also achieves a superior end performance.

While I hesitate to bring this up, a common question for any new attention mechanism is its scalability. The autoregressive language model used in this study is still below 3B parameters. It would strengthen the paper to show efforts towards scaling this approach (I realize this is easier said than done). Additionally, I’m curious if it might be possible to adapt an existing model trained with standard attention to LASER, which would reduce the computational burden of training a larger model from scratch.

Finally, while I understand the claim that existing system implementations for standard attention can be reused, I would still like to know if any additional overhead is introduced. Presumably, log and exp operations could be fused into the kernel, but it would be helpful to see specific performance metrics to quantify any potential overhead.

### Questions
Please address the questions raised in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2
