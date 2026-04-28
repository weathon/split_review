# RingAttention with Blockwise Transformers for Near-Infinite Context

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 3, 8, 5

## Abstract
Transformers have emerged as the architecture of choice for many state-of-the-art AI models, showcasing exceptional performance across a wide range of AI applications. However, the memory demands imposed by Transformers limit their ability to handle long sequences, thereby posing challenges in utilizing videos, actions, and other long-form sequences and modalities in complex environments. We present a novel approach, Blockwise RingAttention, which leverages blockwise computation of self-attention and feedforward to distribute long sequences across multiple devices while fully overlapping the communication of key-value blocks with the computation of blockwise attention. Our approach enables training and inference of sequences that are up to device count times longer than those achievable by prior memory-efficient Transformers, without resorting to approximations or incurring additional communication and computation overheads. Extensive experiments on language modeling and reinforcement learning tasks demonstrate the effectiveness of our approach in allowing millions of tokens context size and improving performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed an efficient distributed computation of full attention mechanism of long sequences across the sequence dimension. By leveraging the blockwise computation of full attention, the proposed Ring Attention distributes long sequences across multiple devices while overlapping the communication of key-value blocks with the computation of blockwise attention. Importantly, Ring Attention enables us to store the output of each layer across multiple devices, significantly reduces the memory demand in Transformer for long sequences.

### Strengths
The challenge the paper aims to address is well-motivated and the proposed method is well-introduced. The experimental results are strong.

### Weaknesses
 There are concerns/questions about the proposed Ring Attention:

1. If I understand correctly, the Ring Attention is based on the assumption that the blockwise computation of self-attention on different devices is well-balanced. However, in the causal mode of self-attention, which is widely used in auto-regressive LLMs, this assumption does NOT hold. It is because under the causal mode, only the lower triangular blocks are necessarily to compute, yielding around half of FLOPs of the non-causal mode with full attention. But in Ring Attention, even under causal mode, we still need to compute all the blocks in the full attention matrix. When the sequence is super long, this may require significantly more FLOPs?

2. For the results in Table 3, Ring Attention are not compared with other sequence parallel mechanism, such as Deep Speed Ulysses which leverages all-to-all communication to speed up sequence parallelism.

### Questions
NA.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes ring attention, which is a way of implementing softmax dense attention.  The attention operation is  
distributed over multiple GPUs, and computed in parallel along the sequence dimension.  Attention is also computed in a blockwise fashion, without ever instantiating the full attention matrix, which reduces memory requirements. Together, these two techniques allow dense attention to be scaled to very long sequences.

### Strengths
The paper is well-written, and it cites the appropriate literature.  The technique described in this paper does, in fact, allow transformers to be trained with very long sequences.

### Weaknesses
Unfortunately, although the paper is technically sound, it does not really contribute anything new.  The ideas presented
in this paper will already be obvious to most practitioners.  As a result, I do not feel that it is appropriate for publication at a conference. 

The fact that transformers process all elements of a sequence in parallel, (at least during training) was the whole inspiration for the original 2017 paper that introduced the transformer architecture.  Thus, the idea of distributing the computation in parallel along sequence length is most definitely nothing new.  This paper merely distributes the computation over multiple devices.

A naive implementation of attention instantiates the entire attention matrix, which is too large to fit in memory for long sequences.  The blockwise computation of dense attention avoids such instantiation, and it does involve some subtle implementation details wrt. to the handling of softmax.  However, it is also not a contribution of this paper; the authors cite the appropriate prior work. 

The remaining piece of the puzzle is to overlap the matrix multiplications for each block with the communication overhead of transferring blocks between different hosts.  However, this is also nothing new; tiled matrix multiplication, distributed over multiple GPUs, is implemented by every major machine learning library today (e.g. Jax), and existing implementations overlap matmuls and communication.

Thus, the authors merely observe that it is possible to implement long-range attention using a simple combination of well-understood and previously published techniques.  This fact should be obvious to most practitioners, and IMO, does not rise to the level of a conference paper.  I would encourage the authors to publish this work in a workshop or on arXiv.

### Questions
The authors claim that ring attention over very long sequences is suitable for both training and inference.  However, the cost of attention in both cases is still O(N^2).  For training, this is less of an issue; all elements of the (long) sequence are processed in parallel, so the sequence length is essentially just a batch dimension, and the number of tokens per training step is not excessive for an LLM.  

However, for inference, tokens are processed autoregressively, so very long sequence lengths will lead to very slow generation times, and thus very high latency when serving the model.  The authors do not discuss or even mention this problem.  How does the latency of ring attention over, e.g., 8M tokens during inference compare to a more conventional short-context model?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a distributed computing strategy for distributing self-attention computation to across multiple devices without introducing latency on host communication. The authors observed that when distributing blockwise computation of self-attention in multiple devices, the order of which block is computed first does not change the output. So, they proposed a ring style communication. Each device will take care of self-attention output of a subset of queries, and it only receives a subset of keys and values from the next device at each time, which reduces the communication cost. Also, by overlapping the computation of queries’ attention to the current subset of keys and values and the communication of the next subset of keys and values, this host communication does not introduce additional latency overhead.

### Strengths
1. The idea is simple and effective. 

2. The proposed distributed self-attention computation allows bypassing the hardware limitation of single device. 

3. The ring style communication allows the communication requirement stays constant when scaling to more devices. 

4. The overlapping of computation and communication hides the communication overhead.

### Weaknesses
1. There is only one toy experiment comparing the performance of RingAttention with other efficient attention baselines. The proposed method enables full self-attention for longer sequences, so it would be interesting to see the performance potential of full self-attention on the real world datasets. It is unclear how the method would perform on tasks that require more complex reasoning or understanding of long-range dependencies, which are often the motivation for using full attention in the first place. The lack of evaluation on standard benchmarks makes it difficult to assess the practical impact of this work.

2. It would be better to include the results on network bandwidth utilizations in Table 3. The current table only reports maximum context sizes, which is not sufficient to understand the communication overhead. Reporting the actual bandwidth utilization would provide a more complete picture of the efficiency of the proposed method, especially when scaling to more devices. This is crucial for practical deployment.

3. In causal attention (used in most LLMs), the compute cost for different queries are different. Queries at the begin of sequence require less compute. In the proposed method, since each device takes care of a subset of queries, the compute load on different devices are different. Will this method make some devices underutilized? This could lead to load imbalance and reduced overall efficiency, especially for long sequences where the difference in compute cost between early and late queries is significant. The paper should discuss this potential issue and propose solutions.

### Questions
1. I am wondering if the same idea could be adopted to distribute linear projections in Attn and FFN computations as well

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Using large context lengths poses memory challenges since it is needed to maintain the key value vectors of earlier tokens. This paper proposes to distribute these vectors across multiple nodes allowing linearly scaling the context length with number of nodes. To address the challenge that computing the attention for a token requires access to all previous key value vectors, the authors propose a scheme to move the vectors across the node. Namely, they suggest forming a ring of nodes and passing the vector to the next node in the ring continuously until all vectors pass through all nodes. Moreover, the authors point out that the communication can be overlapped with the computation, thus making the overhead negligible. The paper shows the method can be practically applied through various experiments, namely fine-tuning LLaMA with 500k token context length.

### Strengths
The method effectively allows scaling the context length with the number of nodes. The proposal to overlap communication and computation could allow hiding the communication cost. It can also be implemented in a fairly straightforward manner. The authors show Ring Attention's practicality through experiments. It is very nice to see experiments done both on GPUs and TPUs. The paper is written clearly and can be followed reasonably easily.

### Weaknesses
While the paper contains experiments showcasing that ring attention can be applied in practice, a comparison with other methods is missing. For example, if applicable, is it better to apply pipeline parallelism or ring attention? Other similar methods also include DeepSpeed Inference [1] which suggests to offload the kv cache to cpu and similarly overlap communication and computation and FlexGen [2]. Additionally, in light of these existing work (some of which are also not referenced), the novelty of the work might be limited.

Furthermore, an ablation study is missing. For example, how important is it to overlap communication and computation? It would be beneficial to see experiments that quantify the impact of overlapping communication and computation, particularly in scenarios with varying communication bandwidths. Without such an ablation, it is difficult to assess the true benefit of the proposed communication overlap strategy. Specifically, what is the performance degradation if communication and computation are not overlapped, and how does this vary with the number of nodes and context length?

I would also like to point out that while the method allows scaling the context length by increasing the number of nodes, it does not address challenges of handling long contexts by Transformers (e.g. [3]). As such, I find comparison with Claude and GPT3.5 in Figure 3 a bit misleading. In particular, we do not expect this method to improve the performance of the model on small context lengths (though a small increase is observed possibly due to more fine-tuning).

[1] Aminabadi, Reza Yazdani, Samyam Rajbhandari, Ammar Ahmad Awan, Cheng Li, Du Li, Elton Zheng, Olatunji Ruwase et al. "DeepSpeed-inference: enabling efficient inference of transformer models at unprecedented scale." In SC22: International Conference for High Performance Computing, Networking, Storage and Analysis, pp. 1-15. IEEE, 2022.

[2] Sheng, Ying, Lianmin Zheng, Binhang Yuan, Zhuohan Li, Max Ryabinin, Beidi Chen, Percy Liang, Christopher Re, Ion Stoica, and Ce Zhang. "FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU." (2023).

[3] Liu, Nelson F., Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. "Lost in the middle: How language models use long contexts." arXiv preprint arXiv:2307.03172 (2023).

Some minor suggestions:
* Table 1 is not table but a figure. 
* The last paragraph of section 2 is an almost replica of the introduction (this is not a problem on its own. I am merely pointing this out in case the authors would like to make better use of the space)

### Questions
(Please also see the weakness section.)

1. How is ring attention applied while doing auto regressive decoding (in the stage of decoding tokens one by one)?

2. How does the training time scale with number of nodes? For example, what is the rate of slowdown observed when training a model with 2k context length on two nodes in comparison with k context length on one node (expected 4x) and in comparison with using normal attention to train with 2k context length on a single node?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
