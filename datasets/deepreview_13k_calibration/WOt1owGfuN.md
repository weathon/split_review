# Probe Pruning: Accelerating LLMs through Dynamic Pruning via Model-Probing

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
We introduce Probe Pruning (PP), a novel framework for online, dynamic, structured pruning of Large Language Models (LLMs) applied in a batch-wise manner. PP leverages the insight that not all samples and tokens contribute equally to the model's output, and probing a small portion of each batch effectively identifies crucial weights, enabling tailored dynamic pruning for different batches. It comprises three main stages: probing, history-informed pruning, and full inference. In the probing stage, PP selects a small yet crucial set of hidden states, based on residual importance, to run a few model layers ahead. During the history-informed pruning stage, PP strategically integrates the probing states with historical states. Subsequently, it structurally prunes weights based on the integrated states and the PP importance score, a metric developed specifically to assess the importance of each weight channel in maintaining performance. In the final stage, full inference is conducted on the remaining weights. A major advantage of PP is its compatibility with existing models, as it operates without requiring additional neural network modules or fine-tuning. Comprehensive evaluations of PP on LLaMA-2/3 and OPT models reveal that even minimal probing—using just 1.5% of FLOPs—can substantially enhance the efficiency of structured pruning of LLMs. For instance, when evaluated on LLaMA-2-7B with WikiText2, PP achieves a 2.56 times lower ratio of performance degradation per unit of latency reduction compared to the state-of-the-art method at a 40\% pruning ratio.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles an important problem and explores saliency-aware structural pruning of neural networks. It utilizes a probing module that analyzes the L2-norm based importance for network slimming and delivers run-time inference speedup. It studies Llama2/3 and OPT LLMs and translates into performance improvements.

### Strengths
- The method seems to be easy to implement without incurring extensive hardware changes.
- Various ablations are provided.
- Real-time speed ups are observed on GPUs, that are a critical aspect for deployment.

### Weaknesses
 - The method seems not to be zero-shot as it does rely on a calibration set. I could not find the detailed calibration datasets descriptions in Section 5, making it likely that the probing is looking into the final datasets to find optimal and satisfactory combinations. This makes is fairly unfair to other methods that are zero-shot on final tests given other proxy datasets. I would like to have more clarifications whether probing is looking into the final test/target metric data for numbers. If so, it's not a fair comparison to others and calibration set used for probing shall be used kept the same as other methods and report only zero-shot test values.
- Figure 3, zero probe sequence ratios all setups are below the reference line - why is it the case?
- Overall I think the method is gradient-free, but does not seem to be completely test-time per-sentence dynamic. Rather it is using batch and sequence data for a quick analysis of the saliency and deploy pruning methods. 
- Table 5 indicates the method is not giving final speedups and performance boosts as strong as FLAP and Wanda-SP. This raises slight concerns for the true strength of the methods.
- Probing can incur overheads due to look aheads, and that may imply why the speedup is limited to <2x. It would be beneficial to see higher speedup ratios that may make the methods more attractive.

### Questions
Listed as above in the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a  framework for online dynamic structured pruning of Large Language Models (LLMs). The proposed method, called Probe Pruning (PP), utilizes a small subset of hidden states to identify crucial weights, enabling tailored pruning for different batches during inference. Key components of the framework include probing, which gathers important intermediate hidden state information, and history-informed pruning, which integrates probing states with historical data to enhance pruning decisions. The results demonstrate that PP significantly improves efficiency and performance compared to existing methods, achieving better outcomes without the need for fine-tuning or additional neural network modules. The paper highlights the potential of PP for optimizing LLMs while maintaining their effectiveness.

### Strengths
The paper demonstrates that PP can achieve substantial reductions in computational overhead while maintaining or even improving model performance. The ability to perform dynamic pruning during inference allows for tailored optimizations that adapt to the specific characteristics of each batch, enhancing overall efficiency.


The authors provide comprehensive experimental results across various tasks and models, including LLaMA-2 and OPT. The consistent outperformance of PP compared to existing baselines, including those that involve fine-tuning, underscores the effectiveness and reliability of the proposed method.

### Weaknesses
1. Unfair Comparison: This approach is a dynamic inference technique, but it is mainly compared to some static pruning techniques. The static pruning work is generally less accurate than dynamic pruning, but it reduces the LLM storage overhead and accelerates the results consistently. Dynamic pruning cannot reduce the LLM storage overhead and the acceleration result varies greatly under different inputs.

2. Lack of comparison of other dynamic inference approaches. For example, some dynamic early exits can be seen as dynamic depth pruning, but also other token-level dynamic decoding methods. Authors should present comprehensive comparisons and discussions, and clearly explain the advantages of dynamic weight pruning over other dynamic inference methods.

3. Not enough impressive novelty: The Historical States method is common operation similar to  EMA or Memory Bank in contrast learning. I consider this technique to be a trade-off strategy rather than an essential solution.


4. Absence of recent LLM evaluations: this work mainly evaluates LLMs released in 2023, the latest LLMs released in 2024 are lacking in experiments. e.g., Llama 3 70B,  Llama 3.2 1B and 3B, DeepSeekMoE，Mixtral-8x7B.

5. Lacking some discussion of recent LLM pruning efforts, such as Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models  (ICML-2024)  Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models (NeurIPS-2024) Adaptive Layer Sparsity for Large Language Models via Activation Correlation Assessment  (NeurIPS-2024)

### Questions
See Weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes an approach for on the fly pruning of LLM. On the fly means that the structure is changing depending on the prompt. The approach is motivated by observation that using different data for calibration results in different pruning structures. To make the approach more efficient, only a portion of samples and tokens is selected for importance estimation. Results are solid and show a trade-off between improvements in accuracy, but also a slowdown in throughput.

### Strengths
- The problem is interesting and novel.
- The approach is well motivated and look novel. 
- The motivation behind selective importance estimation is great.
- I like the way the importance is tracked and updated from initial states. 
- Results are solid, they show clear benefits of the pruning "on the fly"

### Weaknesses
 - The improvement in perplexity comes with reduction in model throughput as shown in Table 5.
- The method has weaknesses when compared to other techniques. For example the entire model needs to be load, whereas for other structured pruning techniques, only the pruned version is required. Limitations and weaknesses are not highlighted in Table 1 forming an incomplete story. 
- The paper is written in a complicated way, it feels that the idea and method can be described in a more intuitive and simpler way. I don't count this as a strong weakness, but rather encourage authors to improve the paper for future readers. 
- For evaluations, is it implemented as the entire batch consists of a single task? What happened when the batch is mixed? I would assume degradation of the current approach.

### Questions
Statements as on page 1 need empirical evidence to backup the statement: "Although the calibration dataset provides valuable insights for pruning by identifying non-critical weights, this approach overlooks the batch-dependent nature of outlier properties in LLMs Liu et al. (2023b); Song et al. (2023); Liu et al. (2024); Sun et al."

Paper talks about "residual importance" a lot, but this concept is not clear before page 5. It would be better to introduce it earlier. Does it mean an L2 norm of the hidden state? If yes, then it will be better to simplify description. 

How to understand "Full-Batch Probing" - is it just a standard structured pruning? How is that different from other techniques? 

From tables 2-3 it seems that full-batch probing outperforms all other techniques, is it because pruning mask changes between batches? 

What is pruned exactly? Are heads pruned, in intermediate dimension in MLP pruned, what about hidden dimension and layers?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper acknowledges challenges incurred by the majority of pruning methods:
* That relying on a calibration dataset to collect pruning statistics introduces potential bias, in that the calibration dataset cannot be perfectly representative of real-world data.
* That pruning requires access to information, such as gradients, that are not usually available during inference, precluding dynamic pruning.

The paper hints at the fact that dynamic pruning is poised to surpass dynamic pruning in performance and proposes a framework to make it practically feasible.

In the paper, the authors recognize that structured pruning is, according to most implementations, the only feasible way to effectively speed up inference.

The paper introduces probing, as a means for collecting statistics required for pruning at negligible additional cost.

The paper provides a configuration named Full-Batch Pruning that gives an upper-bound limit to the accuracy of dynamic pruning. This can be used to better measure the effect of sampling during probing. The paper shows that the selection of prunable weights is more similar to that of Full-Batch Pruning for PP than it is with the fixed-prune models.

History-informed pruning is introduced the alleviate the inaccuracy of probing when the sampling rate is small, by accumulating statistics over multiple batches.

A pruning metric is introduced. The metric is based on the Wanda metric, with an additional squaring to capture the importance of individual weights.

The paper concludes with a large amount of empirical results and detailed ablations in the appendix.

### Strengths
The challenges described in the introduction are indeed fundamental limitations of most existing pruning methods.
Dynamic Pruning is a very promising research avenue and this paper brings several novel aspects to it: probing, pruning metric.

The paper provides a good set of baselines to compare against.

The paper validates the method with several model backbones (LLaMA2, LLaMA3.1, OPT) and benchmarks that include text generation and common reasoning tasks.

Every design choice in the paper is carefully described, ablated and proven with experimental results.

### Weaknesses
The method relies on having rather large batch sizes and sequence lengths to sample from in order to generate a probe. However in many inference setups where speed matters and thus pruning is desirable, the batch size is small, sometimes down to 1. Similarly, inference time in LLMs tends to be dominated by the auto-regressive (aka generation) phase, where tokens are produced one at a time. 

The inference measurements and FLOPs calculations demonstrate the small computational complexity of running the probe. However in practice, I understand that we need to run the probe first and only then do we know which filters to prune. Potentially, the probes can run in parallel with the actual computation of earlier pruned blocks. In order to prove the point that the benefits of probing + dynamic pruning outweigh the cost of probing, it would be nice to have end-to-end inference measurements.

The paper does not compare against the Minitron baseline (https://arxiv.org/pdf/2408.11796), yet this paper shows better metrics. For example for LLaMA3.1-4B, LLaMA3.1-Minitron4B(50% pruning) has HellaSwag at 76.1, while PP has it at 65.3 with 40% pruning. Thus it is unclear whether the method beats the State of the Art.

There is empirical data to probe the superiority of the proposed pruning metric but no theoretical justification.

### Questions
1. Will history-informed pruning counterbalance the limited sampling possibilities when the batch size of sequence length are small?

2. Can you run end-to-end inference measurements with PP in order to show how much speed up we can expect from 20% and 40% pruning ratios?

3. Does PP speed up the auto-regressive phase of inference?

4. Can you compare against the Minitron baseline?

5. Can you further explain why the proposed pruning metric is superior to the Wanda metric?

### Soundness
3

### Presentation
3

### Contribution
3
