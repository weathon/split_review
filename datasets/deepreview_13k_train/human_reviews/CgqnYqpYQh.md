# Merging Feed-Forward Sublayers for Compressed Transformers

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
With the rise and ubiquity of larger deep learning models, the need for high-quality compression techniques has been growing in order to deploy these models widely. The sheer parameter count of some models makes it difficult to fit them into the memory constraints of different hardware. In this work, we present a novel approach to model compression by merging similar parameter groups within a model, rather than pruning away less important parameters. Specifically, we propose a straightforward method for selecting, aligning, and merging separate feed-forward sublayers in Transformer models, and test our method on a language modeling task, image classification, and machine translation. With our method, we demonstrate performance comparable to the original models across our three diverse tasks while combining more than a third of model feed-forward sublayers. For instance, we can remove over 21\% of total parameters from a Vision Transformer, while maintaining 99\% of its original performance. Additionally, we observe that some  feed-forward sublayers often exhibit regions of high similarity between their activations, which may help explain their surprising mergeability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposed a novel model compression approach by merging parameters. Specifically, the parameters from some of the linear layers are averaged after a set of permutations, which involves to maximize overall correlation of the inputs of layers. This method aims to reduce the parameter storage costs of deep neural networks, particularly Transformers, by merging similar parameter groups within the model rather than pruning individual parameters.

### Strengths
The paper is well-written with a clear and logical structure. The paper presents a novel method to reduce the storage costs of deep Transformer-based models by merging their parameters. The experimental results provide a detailed discussion of parameter merging across multiple deep models on various tasks, demonstrating the effectiveness of the proposed approach.

### Weaknesses
As shown in Table 1, parameter merging maintains the model's inference speed but still requires fine-tuning, highlighting the drawbacks of this approach. Despite the distinct from parameter pruning, parameter merging/sharing remains a common model compression technique. However, the paper lacks of experimental comparison and discussion with other parameter pruning methods, such as [1], weakens the argument presented in this paper. Notably, [1] achieves a nearly unchanged ViT accuracy (-0.07, 83.36 → 83.29) while reducing model parameters by over 40 percent, including a 1.9x run time speedup. In contrast, the paper reports a significant ViT precision drop (-1.1, 80.3 → 79.2) with a parameter reduction of about 20 percent and no improvement in inference speed. The absence of a comparison with structured pruning techniques, which also aim to reduce model size by removing entire blocks or layers, is a notable gap. Specifically, methods that identify and remove less important layers or attention heads could provide a more relevant comparison point, as they directly address the redundancy in large models, similar to the goals of parameter merging.

### Questions
1. Have there been any attempts to directly compare the proposed method with a parameter-sharing structure trained from scratch? Essentially, the "compressed model" relies on a shared parameter structure following fine-tuning. Given that fine-tuning is an integral part of the proposed approach, could a "compression from scratch" strategy potentially yield better results?
2. Could the authors clarify the reasons behind adopting the sliding window strategy for selecting sub-layers? Are there potentially better designs for this selection process? While the sliding window approach appears straightforward, it may lack novelty and clear motivation.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposes a parameter merging technique that reduces the param count of feedforward layers with some fine-tuning for recovery. It consists of the permutation finding step, applying the transformations, merging transformed parameters, and finally tying the merged parameters. As an analysis, they compute similarity measures between feed-forward sublayers within the same model and find regions with highly similar activations.

### Strengths
- The paper does a good job delineating relevant context for neuron alignment and describing their approach. 
- Also, the summary of the comparison between compression methods helps understand the trade-off of the merging method. 
- Thorough analysis via ablation studies and visualization.

### Weaknesses
The biggest weakness is the experimental results. It seems like authors do a great job at the ablation studies and visualization, but these are secondary contributions given that this is a paper on compression method for Transformer acceleration, not interpretability research. This means the results section should cover a wider range of benchmarks and also comparisons to pruning approaches (which achieves the same end effect as merging). For example, Wanda [1] prunes 50% at one-shot (without fine-tuning) without major accuracy loss. Authors should clarify how merging is potentially more beneficial than modern pruning techniques and provide thorough comparisons & discussions. 

It is nice to have experiments covering various tasks (image classification, language modeling, translation). But, I strongly encourage adding MMLU on top of simple perplexity as it better demonstrates language modeling. Also, LLaMA models should be tested given their overwhelming popularity over GPT-2 -- it will be a bigger contribution to the community. 



### Questions
1. Typo in line 89: "These same patterns do not in counterpart attention sublayers." ?
2. As described above, authors should compare their merging method to pruning and also quantization approaches. I see that it explores how merging can be combined with quantization (Table 4), but quantization should be compared head-to-head with their merging method, as both are used to reduce storage.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper propose a new way to compress deep learning model by merging similar parameter groups within a model. The paper mainly focus on the MLP layers of the transformer model. A learned permutation is applied on to the MLP layers to be merged to minimize the difference in the merged layer output. An evaluation across all possible merging configuration is conducted to decide which layers to merge to reach the best evaluation score.

### Strengths
This paper explores layer merging, which is an interesting idea. The proposed method of permutation merging provides more capacity to the model after merging.

The experiments are conducted on both vision transformer models and language models

Detailed results are provided on merging different amount of layers and different layer locations.

### Weaknesses
Novelty-wise, weight sharing across layer is not a new concept. Early efficient language model design has explored to share weights across different transformer blocks [1], with later attemps conducted in ViTs and LLMs.

Even as a new model compression method, the proposed method seems to be not very effective, especially comparing to pruning. For example, structural pruning can achieve 2.57x lossless parameter reduction on ViT model [2], yet the proposed method can only remove 21%. Furthermore, comparing to pruning and quantization, the proposed method only reduces the amount of parameters, yet achieves no inference speedup.

One key method proposed in this work is the permute merge. Yet from the results in Figure 2 and 3, permute does not lead to significant performance improvement over the naive merging in most cases, and behave even worse on GPT-2. This leaves doubt on the effectiveness and correctness of the proposed merging technique.

The proposed method is limited to the MLP layers in the transformer model, which limits the compression ratio the model can achieve.

### Questions
Why permute FF merge behave worse than vanilla merge in the GPT-2 model?

Can the proposed method be extended to all model layers?

### Soundness
2

### Presentation
3

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
This paper proposes a method to compress Transformer models by merging similar feed-forward network (FFN) layers. The authors align and average the weights of these layers to reduce parameter count by up to 30%, without significantly impacting model performance.

### Strengths
- The paper presents a clear and straightforward idea. The authors propose reusing the Feed-Forward Network (FFN) layers in Transformer models, which makes the paper relatively easy to understand. The main novelty comes from averaging FFN weights after applying permutation to align them across layers.
- The proposed method demonstrates that model compression can be achieved by reducing the number of stored parameters through merging FFN layers. This can be useful for reducing memory usage in models deployed on hardware with storage limitations.

### Weaknesses
 - **Limited Practical Use:** The approach only reduces the number of stored parameters without reducing computational cost (no FLOP reduction). This is a significant limitation because many existing compression techniques like pruning aim to reduce both memory and computation, enabling models to run on resource-constrained devices with lower latency. The authors' method, while helpful in reducing memory, doesn't address this more practical need, limiting its applicability. Furthermore, the method's focus on parameter reduction alone neglects the energy consumption aspect, which is crucial for deployment on edge devices. A method that only reduces parameter count without addressing computational cost or energy consumption has limited practical value in many real-world scenarios.
- **Lack of Comprehensive Baselines:** The experimental evaluation is insufficient, as it misses several important baselines:
    - **Naive Baseline:** A simple baseline, such as reusing the FFN layers and fine-tuning the shared parameters from a random initialization, would be helpful to assess the effectiveness of the proposed approach. The absence of this baseline makes it difficult to determine if the permutation alignment is actually beneficial or if the performance gains are simply due to fine-tuning a model with reduced parameters.
    - **Pruning Methods**: Methods like magnitude pruning or zero-activation pruning should be included to compare accuracy under the same parameter reduction. These methods often achieve both parameter reduction and computational speedup, making them a crucial comparison point. Without these, it's unclear whether the proposed method offers any advantage over existing techniques.
    - **Methods Targeting FFN Optimization**: Other methods specifically focused on reducing computation and memory usage of FFN layers, such as MoEfication​ [1] and Go Wider Instead of Deeper​ [2], should be used as baselines as well. These methods directly address the FFN layers, which are the focus of this paper, and are therefore essential for a comprehensive evaluation. The lack of comparison to these methods makes it difficult to assess the novelty and effectiveness of the proposed approach.
- **Writing Quality:** The paper contains several writing issues. For example, line 173 states "from the output of the parameter two parameter sets," which is confusing and unclear. Similarly, line 156 misuses "elude," where "allude" would be more appropriate. These issues, while seemingly minor, detract from the overall clarity and professionalism of the paper.

### Questions
- In line 89, the authors claim that "These same patterns do not in counterpart attention sublayers." However, there are works like [3] and [4] that show how attention weights can also be reused across layers. Could the authors clarify this discrepancy?
- Equation (4): Why does the equation for the bias term $b_i^{out}$ not include the permutation matrix $P_i$?
- The "Vanilla" version in Figure 2 is described as "without the permutation step." Does this mean that the merged FFN weights are simply averaged without any alignment?
- What happens if fine-tuning is not applied after merging the FFN layers? How much does fine-tuning contribute to the performance recovery?
- Why do the authors use a sliding window to select consecutive layers for merging? Wouldn't a strategy based on similarity metrics across non-consecutive layers be more effective?

[3] Xiao T, Li Y, Zhu J, et al. Sharing attention weights for fast transformer. arXiv 2019.    
[4] Bhojanapalli S, Chakrabarti A, Veit A, et al. Leveraging redundancy in attention with reuse transformers. arXiv 2021.

### Soundness
2

### Presentation
1

### Contribution
2
