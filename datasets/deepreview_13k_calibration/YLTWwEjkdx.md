# What Matters in Transformers? Not All Attention is Needed

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
While scaling Transformer-based large language models (LLMs) has demonstrated promising performance across various tasks, it also introduces redundant architectures, posing efficiency challenges for real-world deployment.
Despite some recognition of redundancy in LLMs, the variability of redundancy across different architectures in transformers, such as MLP and Attention layers, is under-explored. 
In this work, we investigate redundancy across different modules within Transformers, including Blocks, MLP, and Attention layers, using a similarity-based metric. Surprisingly, despite the critical role of attention layers in distinguishing transformers from other architectures, we found that a large portion of these layers exhibit excessively high similarity and can be pruned without degrading performance. For instance, Llama-2-70B achieved a 48.4\% speedup with only a 2.4\% performance drop by pruning half of the attention layers. Furthermore, by tracing model checkpoints throughout the training process, we observed that attention layer redundancy is inherent and consistent across training stages.
Additionally, we further propose a method that jointly drops Attention and MLP layers, allowing us to more aggressively drop additional layers. For instance, when dropping 31 layers (Attention + MLP), Llama-2-13B still retains 90\% of the performance on the MMLU task.
Our work provides valuable insights for future network architecture design.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the redundancy across different modules within Transformers,
including Blocks, MLP, and Attention layers. The study shows that the redundancy mainly comes from the Attention. The authors thus propose an “Attention Drop” method for parameter pruning in LLMs. Experiments on Llama and Mistral are conducted to demonstrate the effectiveness of the proposed method.

### Strengths
- The paper is well-organized and easy to follow.
- The study on Attention redundancy is interesting. The proposed approach is reasonable.

### Weaknesses
 - The results show that Attention layers and last layers have more redundancy. However, the experiments are mainly conducted on Llama and Mistral. Is this finding valid for other LLMs? It would be interesting to show more LLMs.
- Please further clarify how the dropped layers are selected in the pruning process. If the target is to drop 4 layers, the attention layers are tested one by one to find 4 layers with lowest importance score?

### Questions
Please see above.

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
5

### Summary
This paper research into the redundancy of attention and MLP layers of transformer-based LLMs. The paper proposes a layer pruning methods with similarity-based layer redundancy measurement. By tracing model checkpoints throughout the training process, it is shown that the layer redundancy is inherent and consistent across training stages. The experiments demonstrate that the pruning method speedup the methods while preserve the performance to some extend.

### Strengths
1. The paper proposed an detailed method for Attention and MLP pruning.
2. The paper is well-written and easy to understand.

### Weaknesses
1. The comtribution of this paper is limited. There are many previous similar methods in layer pruning [1][2][3], and this paper is a simple extension to the MLP and attention layers. 
2. The author did not analyze the reason for the layer redundancy. Although extensive experiments are provided, the reason why transformer-based LLMs exhibit redundency on the MLP and Attention layers are not explained.
3. The author did not compare the experimental performance with previous block or layer pruning methods [1][2][3].

### Questions
1. Why a normally trained Transformer model exhibits redundancy in layer levels? Since there are no explicit inductive bias of layers, it is more likely that each layer learns distinct information for the final prediction. Why pruning several layers do not affect the performance?

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
- investigates the redundancy within different modules of Transformer-based large language models, including Blocks, MLP, and Attention layers.
- The redundancy is evaluated using a similarity-based metric.
- This paper validates that some model components can be pruned with obvious speedup and minor performance drop.

### Strengths
- The paper is clearly written and well organized, it provides a systematic exploration of redundancy in Transformers, focusing on Blocks, MLP, and Attention layers.
- This paper provides several useful insights, for example:
	- FFNs seem more important and Attention modules can be dropped with minimal performance impact with high efficiency
	- deeper layers seem less important compared t the shallower ones, which indicated the model has obtained anwsers in early layers.
- The findings in this paper have practical implications for deploying LLMs more efficiently in real-world applications by reducing deployment costs and resource demands.
- The experiments are extensive and the efficiency of the method is validated to be consistent on different tasks and models.

### Weaknesses
 - All experiments in this paper are conducted on a group of datasets, however these datasets are still limited and cannot represent the real-world applications and validate the generalization ability of the pruned model. For example, if the input sequence is not short, early layer attention modules can model the token-wise relationships and predict correct anwsers, but long sequence tasks such as needle in a haystack might be seriously affected by the dropping.
- In addition, the importance scores rely on calibration datasets, and the paper does not extensively explore how variations in these datasets might affect the pruning results. More details should be given, why performances degradation on some datasets are extensive but ignorable on others.

### Questions
I wonder the results on more complex tasks and long sequence tasks such as longbench and needle in a haystack.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper describes a training-free method for pruning transformers models.

A similarity measure is proposed to estimate the amount of transformation a block (or a layer) apply to their inputs. The similarity measure can be used to define an importance measure which will guide the pruning process.

The importance measure is first applied to prune entire transformer blocks (attention+MLP) from the model. The paper then explains how to apply this measure to estimate the importance of each sublock (attention or MLP) by looking at the residual element within the sublock.
The paper provides empirical block-wise importance data for several popular models, and shows that the earlier and last layer of these models typically exhibit greater importance than the shallow layers.

The paper introduces a Speedup Degradation Ratio metric to help assess the tradeoff between speed and accuracy while pruning a model.

The paper provides KV cache and latency measurements, as a function of how many blocks/layers are pruned.

### Strengths
The paper is well written, it is easy to follow and the claims are backed with empirical results, latency measurements and visual insights.

The method is simple and looks easy enough to implement and replicate.

### Weaknesses
The novelty of the paper is limited. The paper's main findings (that attention is more easily pruned than MLP, and that shallow layers are more easily pruned than first and last layers) are known, see for example "A deeper look at depth pruning of LLMs" (https://arxiv.org/pdf/2407.16286).

The importance measure is using the scale-invariant cosine similarity measure. It could be argued that this fails to capture magnitude information. Since the cosine similarity measure only depends on the orientation of the vectors, a block that doesn't change the orientation of its input but changes its magnitude could be deemed unimportant. In that case, it might be considered to replace said block with a scaling factor.

There are no comparisons against other methods in the main part of the paper. The appendix has a comparison against ShortenedLLaMA and Wanda. There is no comparison against methods such as LLMPruner, SliceGPT, ShearedLLaMA, or Minitron.

The paper does not show a study on the potential benefits of further fine-tuning after pruning, which could help recover some of the accuracy loss.

The paper does not study how to achieve a finer level of pruning, for example pruning individual attention heads.

The paper does not study the importance of the calibration dataset, or whether domain-specific datasets could be used to improve task-specific benchmarks.

### Questions
Can you add a comparison against one or more of LLMPruner, SliceGPT, ShearedLLaMA, or Minitron?

In section 5, it is stated that "For instance, in Llama-2-13B, the KV-cache is reduced from 52GB to 26GB, a 50% reduction. This memory reduction is even more pronounced in larger models like Llama-2-70B, where the KV-cache decreases from 20GB to 10GB.", and the data in the table match this statement. Is this not the other way around, that the 52GB-to-26GB reduction relates to LLama-2-70B?

Did you try to evaluate whether you can prune individual attention heads, as opposed to the whole attention layers?

Did you try to evaluate whether fine-tuning after pruning helps?

Did you try to evaluate whether a scaling factor could be introduced in lieu of a pruned block?

### Soundness
3

### Presentation
3

### Contribution
2
