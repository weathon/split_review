# Ladder Residual: Redefining Tensor Parallelism in Transformers for Accelerated Inference

- Decision: Reject
- Scores: 6, 5, 6, 3

## Abstract
Large language model inference is both memory-intensive and time-consuming, often requiring distributed algorithms to efficiently scale. Tensor parallelism (TP) is a common technique used in multi-gpu training and inference to partition computation across multiple devices, reducing memory load and computation time. However, such parallelism necessitates fast interconnects between the devices which has been a major bottleneck and limits the gains obtained by scaling up the number of devices. We introduce Ladder Residual, a simple architectural modification applicable to all residual-based models that enable straightforward overlapping that effectively hides the latency of communication. Our insight is that in addition to systems optimization, one can also redesign the model architecture to decouple communication from computation. For a Transformer model of 8B size, applying Ladder Residual to all its layers achieves 29\% end-to-end wall clock speed up at inference time with TP world size of 8 devices. We refer to such model as the Ladder Transformer.
We train a 1B and 3B Ladder Transformer from scratch and observe comparable performance to a standard dense transformer baseline. We also conduct adaptation experiments for our approach and show that it's possible to adapt parts of the Llama-3.1 8B model with minimal accuracy degradation by only retraining for 3B tokens. To further push the performance frontier, we propose another architectural modification which drops communications in the model, unlocking fast LLM inference in settings devoid of NVLink or other fast interconnects.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Ladder Residual and Desync Residual, two architectural modifications to the original transformer architecture. The authors aim to address the communication latency bottleneck inherent in TP by decoupling computation from communication, enabling overlapping operations. The Ladder Residual method is tested on both scratch-trained and adapted models, demonstrating competitive performance compared to traditional architectures. Additionally, the concept of Desynced Residual is introduced to further mitigate communication overhead in low-connectivity settings.

### Strengths
* Given communication is usually the bottleneck in adopting Tensor Parallelism (especially in settings with low bandwidth interconnects), the proposed methods can significantly reduce the amount of communication required and mitigate the problem. 
* The evaluations are comprehensive, conducted across various settings and benchmarks. 
* The paper is well-written and easy to follow.

### Weaknesses
* Implementing Ladder Residual may require substantial retraining or adaptation efforts for existing models, which may be challenging for larger models;
* The evaluation sections are restricted to models with relatively small sizes (up to 8B).

### Questions
Regarding the Evaluation section:
- why are the results consistently better without nvlink than with nvlink, across all three baselines? I would assume Megatron-style TP would perform better with NVlink.
- In Fig 2(2), why is there a performance degradation when TP world size =4?
- Is the baseline "standard transformer" using data parallelism or Megatron-style tensor parallelism? 

Regarding the Hybrid-Ladder technique:
- What are the considerations when deciding to apply ladder-residual on the upper half (or later half) of the transformer layers?

### Soundness
2

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
3

### Summary
This paper proposes Ladder Residual, which is a modified model architecture of Transformer models to enable better overlapping between computation and communication of the Tensor Parallelism execution.
It reroutes the output of Attention/MLP output to the block after the next block.
In this way, as for the Tensor Parallelism, one of the dependencies between the AllReduce and block computation is eliminated and thus can be overlapped to achieve better performance.
This paper trains the 1B and 3B models to show that it achieves good accuracy compared to the naive Transformer block structure.
It conducts the performance comparison of 1B, 3B and 8B models on up to 8 GPUs to demonstrate is performance efficacy.

### Strengths
- The rerouting of the residual to break the dependency of computation and communication is novel.
- It conducts the experiments of both accuracy and efficiency to show the effectiveness of both.

### Weaknesses
- It uses up to 8B model for the motivation illustration and evaluation. However, it is less likely to use 8 H100 GPUs to inference the small 8B model in practice.
- It could be better to have a discussion and comparison to the model comparison scheme, which can also serve the LLM efficiently with high accuracy.

### Questions
- Why not conduct the experiment on 70B models? I believe this can be a better model that worth the multi-GPU serving. But given the high compute-intensity of the 70B model, the ratio of the AllReduce overhead can be smaller than 8B, which can be a concern to the motivation of this paper.
- I suggest having some discussion and comparison to quantization. For example, the int4 weight quantization can make a 70B model running on a single H100 GPU, without losing too much accuracy.
- Having a comparison to the pipeline parallelism can also better demonstrate the contribution of this paper. Note some recent studies have shown good performance of pipeline parallelism than the pure TP (https://blog.vllm.ai/2024/07/23/llama31.html).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Typical implementations of large language model inference use tensor parallelism to distribute across multiple GPUs. However, tensor parallelism suffer from high communication overhead when deploying to multiple GPUs. This paper proposes a new transformer-based network architecture for large language models, which is able to reduce communication overhead in tensor parallelism without introducing significant accuracy drop. The experiments show that the proposed architecture can achieve 29% speedup on 8 GPUs.

### Strengths
* The proposed architecture can reduce communication overhead while incurring negligible overhead
* The proposed architecture is simple to implement and requires no low-level code modification

### Weaknesses
* The paper has no evaluation when scale up to more GPUs.
* The paper has no evaluation in conjunction with other existing parallelisms.

### Questions
Thanks for the submitting the excellent paper to ICLR. However, I have a few concerns about the evaluation section of the paper.

First, the paper only evaluates with TP size up to 8. However, the paper has no evaluation when scale up to more than 8 GPUs. It is thus obscure how the performance of the proposed technique when scaling up to multiple GPU nodes.

Second, the paper has no consideration how the proposed technique behave when using other parallelisms. While the proposed architecture should work orthogonally with other parallelisms, it would be much speedup the proposed method could provide when used in conjunction with other parallelisms.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents Ladder Residual, an algorithmic improvement on the traditional Transformer architecture. Ladder Residual delays each residual connection one MLP/Attention module later. This makes the communication introduced by Tensor Parallel no longer on the critical path, and can be overlapped with the computation.
The authors evaluated this method on two ways: 1. pretraining a 1B- and a 3B-parameter Ladder Residual Transformers from scratch with 100B tokens; 2. Adapting the architectural modification on a state-of-the-art Transformer model and finetune with only 3B tokens to adapt the shift. Models pretrained/finetuned from both methods show a promising performance, outperforming the parallel attn/mlp on both throughput and quality.
The authors further introduced fully desynchronized Residual, showing that it can also reach a satisfying performance with more throughput improvement in the case without NVLink.

### Strengths
- The authors introduce a clean method that can significant improve the communication-computation overlap opportunity and make the execution time shorter, while the performance shows a trivial drop.
- The authors perform a thorough evaluation on both model inference throughput/latency/pareto and the performance.
- The paper is easy to follow and clear to understand. The authors first introduced the background of tensor parallel and its communication cost, then elaborated their variant Ladder Transformer and explained why it solves the problem. Then they provides experiments on both inference throughput and model quality to prove the speedup and the performance under this method.

### Weaknesses
- Although Ladder Transformer is friendly to Tensor Parallel, it is not friendly to Pipeline Parallel, which is also necessary during the training process and the inference of large models, because both `prev_attn_out` and `prev_mlp_out` should be sent from a pipeline stage to the other. This prevents the Ladder Transformer from scaling up to a larger size. It would make the contribution more solid if the authors can discuss how to address this concern or why it may not be critical.
- The experiment details for Inference throughput/latency are not clear to me. Answering the following questions in the paper could make the experiment section easier to follow:
  - When NVLink is disabled, is NVLS still turned on?
  - What is the precision used during the inference?
  - What is the memory of a single H100 GPU? For Figure 2, when `Batch Size = 64`, why there is no number reported for TP=1 and 2?
    - I noted that the memory consumption in this case can be approximated as `8B(parameter) + 64(requests) * 1024(seq length) * 8(key/value heads) * 128(head hidden size) * 2(key and value) * 32(layers)=12B` numbers. Following the custom of using FP16 in model inference, this only consumes 24GB of memory, which leaves enough space for intermediate activations even on a single H100 GPU.
- The model size used in Figure 2 (8 billion parameters) is very small, compared to the capacity of hardware (up to 8xH100 GPUs). In this case, running the decode operation with a small batch size makes the computation very sparse, and thus the evaluation setup is not representative (as a [reference](https://lmsys.org/blog/2024-07-25-sglang-llama3/), even using A100 GPU can reach the regime of 2000 tokens/s/GPU, while the highest throughput in this paper is in Figure 3.(1), slightly above 600 tokens/s/GPU). It would make the result more convincing to measure the latency/throughput of a larger model (e.g. 65B) or batch size (e.g. 256 or 512). Besides, it would be beneficial to also report the baseline absolute number, since all other latency numbers are reported in the form of a relative improvement.
- For results in Table 3, it seems like Parallel Transformer is catching up with Ladder Transformer (Average from -0.17 to +0.12, Wikitext PPL from -0.53 to -0.06), as the number of parameters scales up from 1B to 3B, this raises concerns on the scalability of Ladder Transformer. Providing additional experiments with a larger model size or an explanation for why this trend might not continue could be helpful in supporting the significance of the Ladder Transformer.

### Questions
- In Figure 2, for the case Without NVLink, how to explain the reason of a throughput drop of batch size 4 and 16, when the TP world size shifts from 2 to 4?
- How to understand the correlation of the 3 columns in Table 2?
  - My understanding is that token/sec = 1(batch size) * 32(generation length, according to 3.3.1) / latency = 32 / (prompt + decode).
  - In this way, if the prompt improves x% and decode improves y%, the token/sec improvement is at most `1 / (1 - max(x%, y%)) - 1`, which equals `y% / (1-y%)` for all rows in this table because decode improvement is always higher. For most rows in this table, this approximation is very similar to the actual value (with less than 4% error), meaning that the decode time dominates the overall latency. However, in the first row it shows a 17% error.

Below is not relevant to my score of this paper, but only for paper readability:
- The Parallel Attn/MLP, as a commonly used baseline, is not well described. Adding more explanation/figure can improve the paper's self-completeness.
- Section 4 has too many grammar mistakes and is thus hard to follow.
- It would be better to have a breakup of computation (both MLP and Attention) and communication (both with and without NVL) to help understand the importance of the overlapping, as well as how much overlapped can be, and is achieved with Ladder Transformer.

### Soundness
4

### Presentation
1

### Contribution
2
