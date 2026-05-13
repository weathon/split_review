# FlashEVA: Accelerating LLM Inference via Efficient Attention

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Transformer models have revolutionized natural language processing, achieving state-of-the-art performance and demonstrating remarkable scalability. However, their memory demands, particularly due to maintaining full context in memory, pose significant challenges for inference. In this paper, we present FlashEVA, an efficient implementation of EVA (Efficient Attention via Control Variates), and demonstrate how to finetune transformers to adapt to FlashEVA attention. Our method enables fine-tuning of Transformer models with as few as $1.6B$ tokens while preserving effectiveness across various downstream tasks. Notably, FlashEVA achieves up to $6.7x$ higher throughput during inference compared to standard Transformer implementations. Despite these improvements, we observe limitations in retrieval-focused tasks. Our implementation offers control over the trade-off between throughput and accuracy through adjustable hyperparameters, providing greater flexibility. This work represents a significant step towards more efficient and adaptable Transformer-based models for inference.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes FlashEVA, an efficient implementation of EVA, aimed at addressing the high memory demands of Transformer models  during inference. FlashEVA allows for fine-tuning of large language models (LLMs) with minimal performance degradation while significantly reducing memory usage and increasing throughput. The method achieves this by maintaining a compressed cache of past context, which is less memory-intensive than computing the prefix during inference. However, it shows limitations in retrieval-focused tasks. The implementation offers adjustable hyperparameters to balance throughput, accuracy, and memory usage, providing flexibility for various applications.

### Strengths
+ The paper is well organized and presented.
+ Experimental results that the adjustable hyperparameters allow for a trade-off between throughput, accuracy and memory usage.
+ FlashEVA is compatible with existing optimized attention implementations and can leverage CUDA kernels for performance optimization.

### Weaknesses
- The proposed method is overly simplistic and unimpressive. It looks like an implementation of FlashAttention with EVA which is already proposed.
- The experimental results are not persuasive since it doesn’t show the advantages compared to Dijiang and Sliding window as in Figure1. Instead, it is only a trade-off between Dijiang and Sling window.

### Questions
- How about the performance when the model is larger such as 7B, 13B or 70B?
- Can the method compared to FlashAttention3 or combined with it?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces FlashEVA, an efficient implementation of EVA to improve Transformer model performance during inference by reducing memory usage. FlashEVA allows fine-tuning of Transformers with few tokens. While it excels in many applications, it has limitations in retrieval-focused tasks. The method also offers adjustable settings for balancing throughput and accuracy, enhancing flexibility for different use cases.

### Strengths
This paper is well-organized and clear, effectively presenting complex ideas in efficient attention mechanisms. Background and motivation are well-integrated, and the experimental results are systematically laid out, with tables and figures that clarify performance gains. The discussion of trade-offs and limitations shows a balanced approach, enhancing the paper’s readability and impact.

### Weaknesses
A primary limitation of this paper is its lack of significant novelty beyond the existing EVA framework. While FlashEVA offers efficiency gains, these improvements are largely a result of optimizing existing CUDA/Triton kernels rather than introducing new concepts. As such, the contribution may appear incremental, particularly given the relatively modest improvements in throughput and memory efficiency.

While the paper briefly compares FlashEVA with the Mamba model, it does not thoroughly examine their differences or provide a clear rationale for preferring FlashEVA. Mamba significantly outperforms FlashEVA across most tasks, even with fewer computational resources. To provide a more balanced view, the authors could explore the advantages FlashEVA may offer over Mamba, or discuss potential benefits of integrating aspects of both methods. Such a discussion could help clarify FlashEVA’s unique contribution and when it might be favored over Mamba, thereby enhancing the overall value of the work.

FlashEVA demonstrates impressive gains with long-sequence generation but shows limited improvement for shorter sequences. This restriction reduces the model's scalability, especially in applications requiring shorter or mixed-length sequences. The authors could mitigate this issue by optimizing the random feature computation or implementing adaptive techniques that reduce computational overhead for shorter sequences.

### Questions
Please address the questions raised in the weaknesses section.

### Soundness
2

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
- This paper proposes an efficient attention implementation via control variants method using custom CUDA and Triton kernels
- can be finetuned from transformer models with only 1.5b tokens
- show higher inference throughput and lower memory.
- suffers in retrieval focused tasks

### Strengths
- The motivation, and the background about different forms of attentions are clear.
- Extensive experiment results including different down-stream tasks. 
- The proposed methods achieve obvious better throughputs and memory consumption comparison compared with EVA and flash attention.
- The proposed method can be finetuned from a standard attention models which makes it easier to use.

### Weaknesses
- The contribution of this work is an incremental work based on EVA. It is not a new algorithm but an efficient implementation of EVA.
- Although the background of RFA, EVA are clearly explained, some background about flash attention could be included since it is more related and if the reader is not familiar. 
- In addition, more details should be given about the CUDA implementation, such as pseudo code and how the custom attention mask is achieved. Current presentation about the flashEVA is too simple.

### Questions
This method is claimed to suffer in retrieval focused tasks. I wonder what if the reason, is this due to the nature of linear attention?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper present FlashEVA, an efficient implementation of EVA and demonstrate how to finetune transformers to adapt to FlashEVA attention. The experimental results show that it can accelerate LLMs up to 6.7x with little performance drop.

### Strengths
- The paper is well-written and easy to understand.

- The experimental results are rich.

### Weaknesses
- I donot see any novelty in this paper. Eq.11 is derived from Eq.9 and Eq.10 in the background section and it seems that the author only define the augmented key and value set.

- Overall, this paper does not provide anything new, and it is more like an experimental report rather than an academic paper.

I think this paper is not ready for submitting to ICLR.

### Questions
See weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
1
