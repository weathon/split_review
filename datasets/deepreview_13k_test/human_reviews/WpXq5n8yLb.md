# Recurrent Drafter for Fast Speculative Decoding in Large Language Models

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
We present Recurrent Drafter (ReDrafter), an advanced speculative decoding approach that achieves state-of-the-art speedup for large language models (LLMs) inference. The performance gains are driven by three key aspects: (1) leveraging a recurrent neural network (RNN) as the draft model conditioning on LLM's hidden states, (2) applying a dynamic tree attention algorithm over beam search results to eliminate duplicated prefixes in candidate sequences, and (3) training through knowledge distillation from the LLM. ReDrafter accelerates Vicuna inference in MT-Bench by up to 3.5x with a PyTorch implementation on Nvidia H100 GPUs. To demonstrate its practicality in production environments, we integrate ReDrafter into TensorRT-LLM, reaching up to 2.5x speedup on H100 GPUs. We also validated its effectiveness for on-device applications by implementing the approach in MLX and benchmarking performance on Metal GPUs in Apple Silicon chips, achieving up to 2.3x speedup. We summarize our experimental results in Figure~\ref{fig:implementation_results}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes "ReDrafter", a speculative decoding algorithm that uses an RNN as the draft model. The RNN takes as input the outputs of the LLMs last hidden layer, and then uses beam search to construct a set of possible continuations, which are then verified using an efficient "dynamic tree attention" algorithm by the target model. The RNN is trained using knowledge distillation, to maximize alignment with the target model. Empirically, ReDrafter shows large speedups (on both H100s in PyTorch/TensorRT-LLM, and on Apple Silicon in MLX), generally attaining meaningfully larger speedups than Eagle and Medusa.

**Update**: After reviewing the authors’ responses, I have lowered my score to a 3, as I remain unconvinced that beam search can be used by the draft model during stochastic decoding while maintaining the output distribution of the target model.

### Strengths
- Using an RNN as a draft model, taking as input the outputs of the target model's last hidden layer, is a nice idea. This allows introducing dependence between the draft model's speculated tokens (unlike Medusa), while also leveraging the strong representations from the target model (like Eagle), while not requiring storing a KV cache for the draft model.
- The empirical speedups attained by ReDrafter appear quite large.

### Weaknesses
- **Most importantly**: It's unclear to me how beam search can be used by the draft model while maintaining the guarantee that the output distribution of the target model is unchanged, when stochastic decoding is used. Can you please clarify?
- It seems that a large percentage of the ReDrafter speedups may come from the large beams used during decoding, as opposed to from an improved draft model architecture. I would have appreciated more careful ablations to clarify this. For example, could one use a transformer draft model (e.g., Llama-3.2-1B for Llama-3.1-70B) with beam search, and attain similar/larger speedups than the RNN draft model? Could you show the relative speeds and acceptance rates of ReDrafter vs. standalone draft models / Medusa / Eagle, to understand the relative merits of these different draft model architectures? How do these different draft model architectures compare when a simple chain of tokens is speculated (like in Leviathan et al), instead of a tree of tokens?
- Given that much of the speedups seem to come from the beam search process, it's important to compare with methods like Sequoia and Eagle2, which also perform speculative decoding using large trees of tokens (instead of simply token sequences).
- It would have been nice to see experiments with Llama 3 models.

### Questions
- In the equation in line 156, it doesn't seem $h$ or $g_t$ are used in the recurrence equation for $s_t$. Can you please clarify?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new speculative decoding algorithm (ReDrafter), that uses the final hidden state of the LLM as input to an RNN. The speedup is further enhanced by using dynamic tree attention over beam search results for the draft model. ReDrafter provides speedups over other decoding algorithms such as EAGLE and Medusa.  The algorithm is implemented and compared with other decoding techniques in multiple frameworks (Pytorch, TensorRT-LLM,  MLX on Apple M2 Ultra Metal GPU). Finally, a new training objective for the draft model is proposed based on knowledge distillation to better align the draft model with the target LLM.

### Strengths
Several ablation studies are done to show the effectiveness of all the main contributions, including ablations for the knowledge distillation training objective and the ablation for the 
dynamic tree attention. This makes the contributions more clear.

The algorithm is implemented in several frameworks, and performance improvements are shown in all frameworks, making the practical significance of the algorithm higher. 

The work is quite original while building on previous work on knowledge distillation and using tree structures to save computation. 

The ReDrafter approach gives significant speedups over EAGLE and Medusa on several frameworks and model sizes.

### Weaknesses
The paper does not seem to include details on the compute resource/time requirements to train the draft model. This is important to understand for others wanting to train ReDrafter on their local LLM. 

For many LLMs, there exist smaller LLMs from the same family that can be used as draft models. It would have been good to compare against approaches using separate draft models. 

Very minor comments: 
There is a parenthesis missing in equation 1. 
In the first sentence of the abstract, I would use LLM rather than LLMs.

### Questions
Will the code be open sourced?

Can you clarify why you are only comparing against the EAGLE and Medusa papers? 

How is the performance of ReDrafter compared to approaches that use a separate draft model?

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
This paper aims to accelerate the inference of LLMs. The proposed architecture utilized speculative decoding technology and applied a draft model with an RNN structure. They also use dynamic tree attention to further accelerate inference.

### Strengths
1.The paper is well-written and flows very smoothly. The framework and workflow of the entire method are clearly articulated.
2.This paper conduct extensive experiments to demonstrate the effectiveness of their approach, covering various models and different devices.

### Weaknesses
1. Although there is textual description of ReDrafter, providing a structural diagram would better assist readers in understanding the structure of the ReDrafter Model.
2. I believe the paper lacks sufficient explanation for the idea of using an RNN-based draft model. For example, I think it would be beneficial to include an experiment that substitutes the RNN with a single-layer decoder model to observe the resulting changes. 
3.Combining embeddings and hidden states as input is not a novel approach.[1]
4. The article mentions that tree attention is dynamic and states that it "relies on individual beam search results," but it does not explicitly explain the relationship. Alternatively, what does the author consider to be “static” tree attention? If it does indeed exist, I believe it should be compared in the ablation experiment section between dynamic TA, static TA, and without TA.

[1] EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty, ICML 2024

### Questions
1. Although there is textual description of ReDrafter, providing a structural diagram would better assist readers in understanding the structure of the ReDrafter Model.
2. I believe the paper lacks sufficient explanation for the idea of using an RNN-based draft model. For example, I think it would be beneficial to include an experiment that substitutes the RNN with a single-layer decoder model to observe the resulting changes. 
3.Combining embeddings and hidden states as input is not a novel approach.[1]
4. The article mentions that tree attention is dynamic and states that it "relies on individual beam search results," but it does not explicitly explain the relationship. Alternatively, what does the author consider to be “static” tree attention? If it does indeed exist, I believe it should be compared in the ablation experiment section between dynamic TA, static TA, and without TA.

[1] EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty, ICML 2024

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces ReDrafter, which achieves state-of-the-art speed improvements for LLM inference in speculative decoding through the use of RNNs, dynamic tree attention, and knowledge distillation from the LLM. ReDrafter demonstrates significant speed enhancements compared to baseline methods across various frameworks and chips.

### Strengths
1. This paper tackles a significant issue in LLM inference by promoting speculative decoding, demonstrating considerable speed improvements compared to state-of-the-art methods like Medusa and Eagle.
2. The method has been extensively tested across various chips and frameworks, including H100, Apple’s M2, TensorRT-LLM, MLX, and PyTorch.
3. The paper is well written and effectively conveys the main design of the algorithm.

### Weaknesses
1. Could you include a comparison with Eagle-2? It's listed in your references but isn’t included in the evaluation.

### Questions
See weakness. Thanks!

### Soundness
2

### Presentation
3

### Contribution
2
