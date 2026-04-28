# Pruning Aggregation Parameters for Large Language Models

- Decision: Reject
- Avg Score: 4.80
- Scores: 6, 3, 3, 6, 6

## Abstract
Pruning is a highly effective approach for compressing large language models (LLMs). By strategically reducing model size, pruning significantly decreases both latency and GPU memory usage during inference, resulting in more efficient and cost-effective deployment of these models. Despite their effectiveness, current structured pruning algorithms have limitations. They still require extensive continued pre-training on large datasets to achieve model compression. Moreover, most of these methods are unable to reduce the memory usage of the key-value cache during generation tasks. In this work, we propose a novel pruning algorithm that requires no additional training and targets specific parameters within LLMs. We classify the model's parameters into three categories: aggregation, transformation, and normalization. Our method primarily focuses on pruning the aggregation parameters in the higher layers of the model. To further improve the performance of the pruned LLM, we also introduce a rescaling parameter that adjusts the output of the pruned block. We conduct comprehensive experiments on a wide range of LLMs, including LLaMA3.1-8B/70B, Qwen2-7B/72B, Gemma2-9B, and Mistral-7B-v0.3. Our evaluation includes both generation and discriminative tasks across various benchmarks. The results consistently demonstrate that our method outperforms recent block pruning methods. This improvement is particularly notable in generation tasks, where our approach significantly outperforms existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces AggregationPruner, a pruning algorithm designed to improve the memory efficiency of Large Language Models (LLMs) by focusing on "aggregation parameters" (queries and keys) in the higher layers, specifically targeting parameters in the attention mechanism without additional training. The authors argue that aggregation parameters contribute less unique information in higher layers, enabling their selective pruning to reduce memory demands, particularly in the key-value (KV) cache. The proposed method is experimentally tested on various LLMs, including LLaMA and Qwen models, across several tasks, reportedly outperforming other pruning strategies.

### Strengths
- The aim of reducing memory usage without retraining is practical and relevant for real-world LLM deployments.
- By exclusively targeting aggregation parameters, the authors contribute to a niche aspect of pruning in LLMs.
- Broad Experimentation: The experiments cover a wide range of tasks and models, suggesting the authors’ commitment to evaluating their approach comprehensively

### Weaknesses
 - The central idea of selectively pruning only the aggregation parameters lacks a theoretical or empirical foundation that justifies this choice over simpler alternatives. The GNN analogy is interesting but ultimately weakly connected to the experimental findings.
- The paper would be stronger with a clearer examination of how AggregationPruner performs relative to simpler or alternative pruning baselines (e.g., random initialization or whole-layer pruning). This would clarify if the exclusive focus on aggregation parameters provides a true advantage. Specifically, the absence of a comparison against random pruning, which would serve as a crucial control, makes it difficult to ascertain whether the observed performance gains are due to the specific selection of aggregation parameters or simply due to the reduction in parameter count. Furthermore, a comparison against structured pruning methods, which remove entire attention heads or layers, would provide a more comprehensive view of the method's effectiveness.
- There is limited discussion of when and why AggregationPruner might fail or struggle compared to other methods. This omission leaves the impression that the results are selectively presented to favor AggregationPruner without sufficient critical analysis. For instance, the paper does not explore the impact of varying pruning ratios across different layers or tasks, which could reveal potential limitations. The lack of analysis on how the method performs on tasks requiring long-range dependencies is also a notable gap.
- Without a clearer framework or theoretical underpinning, this method appears to offer only incremental improvements in memory efficiency rather than advancing pruning methods as a whole. The method's reliance on a grid search for the α parameter, without a clear justification for its range or granularity, also raises concerns about its practical applicability and efficiency. A more principled approach to parameter selection would enhance the method's robustness and generalizability.

### Questions
1. Could the authors explain why simpler alternatives were not included as baselines? Given the minor variation, this comparison might help illustrate the impact of targeting only aggregation parameters.
2. On what basis do the authors claim that aggregation parameters contribute less unique information in higher layers? Was this hypothesis tested directly, or is it purely derived from the analogy to GNNs?
3. How would AggregationPruner perform if applied to smaller LLMs or other architectures with different attention mechanisms? Could this method generalize across architectures?
4. Why was a grid search over the α parameter chosen rather than a more optimized approach? Could this choice be a source of inefficiency?
5. Can the authors clarify whether the effectiveness of AggregationPruner would differ between shorter and longer inference tasks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The work proposes a pruning algorithm aimed at compressing the KV cache in large language models (LLMs) without additional training. Referring to GNN, the authors classify LLM parameters into three categories: aggregation, transformation and normalization, focusing on the pruning of high-level aggregation parameters (KV cache). The authors evaluate their approach on various LLMs and benchmarks, reporting improvements over recent pruning techniques.

### Strengths
1. Pruning the KV cache is important for compressing LLMs.
2. There is something interesting about analogizing the parameters of LLM to GNN.

### Weaknesses
1. Classifying LLM parameters based on the nature of GNNs is of some interest, but lacks some theoretical and experimental support. The different layers of the LLM have their different effects, and the higher layers have their special role in some cases of work. The authors need to have more experiments to support this claim.
2. The authors lack comparisons with SOTA methods e.g. FLAP, Wanda. It would be unfair to simply compare with selfattn/ffn/layer pruner, as no control model parameter is identical. Furthermore, the authors need to compare their method with other training-free structured pruning methods, such as FLAP and SliceGPT, which have demonstrated strong performance across various models. The absence of these comparisons makes it difficult to assess the true effectiveness of the proposed approach, especially given that these methods also achieve KV cache reduction through parameter pruning. The claim that structured pruning algorithms cannot reduce the KV cache is not entirely accurate, as pruning attention heads or groups of heads, as done in GQA, also leads to a reduction in KV cache size and memory costs. Therefore, a comparison with these methods is essential.
3. Alg. 1 is redundant and can be moved to the appendix. But Alg.2 lacks a detailed description and the authors need to describe the method in more detail.

### Questions
See the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a methodology for pruning LLMs without needing to do any fine-tuning of the model, by targeting "aggregation" parameters, as defined by the authors, in the later layers of the mode. By doing so, the KV-cache can be reduced in size, which should result in cheaper inference. The authors demonstrate that accuracy losses for several popular LLMs can be manageable with this methodology.

### Strengths
Pruning techniques that don't require fine-tuning the model are always welcome, and this technique does seem to be able to change many of the layers in popular LLMs without hurting the accuracy too much. I also thought the reasoning as to why the authors wanted to prune these particular parameters was interesting.

### Weaknesses
The biggest problem with this paper is that it presents no quantitative data as to whether inference using these pruned models is actually cheaper or faster than traditional inference, and it doesn't contextualize the results against other ways of making a model cheaper to run. The strongest claim in the paper is that the KV-cache size can be reduced, which is useful, but that is not the same as a speedup. The authors did not compare against pruning methodologies that require fine-tuning, or against other forms of quantization or sparsity. Techniques like these have to be understood in context, and the paper doesn't provide it.

### Questions
1. What is the measured speedup of this approach, especially when changing the batch size to take advantage of the KV-cache compression.
2. Did you evaluate using BF16 number formats? Could you compare against PTQ with FP8?
3. Could you compare against other pruning approaches?

### Soundness
2

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
The paper introduces a pruning algorithm (AggregationPruner) which prunes the Key and Value weights (aggregation parameters) of higher layers of LLMs to reduce the GPU memory consumption during LLM inference tasks (primarily during generative tasks). The method (being post training-free) outperforms the baselines in retaining the performance on various benchmark datasets and models.

### Strengths
1. The paper is clearly motivated, very well structured and has a great value for LLM inference community.
2. The connection between GNNs and LLMs and various design choices (why they picked only higher layers, picking aggregation matrices) are well established.
3. The analysis that pruned models might be good for discriminative tasks while have effect on generative tasks (Fig 8) is pretty interesting and sort of intuitive. (Infact, I believe this statement holds true for any compression method given the nature/complexity of these tasks but might need validation). That being said, I've a question wrto AggregationPruner, refer 1st point in weakness

### Weaknesses
These are not exactly weaknesses per se, but some thoughts I've to improve the paper. 

1. [**Experiment**] Can the authors have an experiment to truly validate the claim that picking lower layers will degrade the performance due to the importance of the layers (line 3 in Algorithm 4)? While the math is quite intuitive from GNNs, an experiment/ablation on all layers (0-32) for model on various tasks can be a good addition? 
2. [**Comment**] Continuing from previous point, can the authors comment on design choice on choosing the number of layers for real time usage of the method (line 3 in Algorithm 4)? From Fig 2, it seems to be having a lot of variation for different models/datasets.  
3. [**Comment**] As mentioned in L419-420, KV cache doesn't get created for discriminative tasks. So, can the authors explain how effective AggregationPruner is for discriminative tasks? I believe authors might have to consider explaining this part more clearly in the paper!
4. [**Experiment**] The paper has been motivated to be effective on GPU memory consumption on generative tasks. Can the authors provide an actual experiment to demonstrate this? 
    - *For eg*: Pick a model, a generative task, measure the perplexity/wall-clock time/speed/memory for the baseline model vs AggregratedPruner method. If an experiment of this sort can't be perform, please comment on why that might be the case.
5. [**Experiment/Comment**] L144-146: The authors have mentioned that "given the black-box nature, we choose the KV matrices" and demonstrated the results in the paper. And I also believe Self-AttentionPruner, FFNPruner and LayerPruner are the terms introduced in this paper (please correct me if I am wrong and cite these methods accordingly). 
   - Now, given these key design choices, I would like to know if it's possible to report the sparsity ratio for these various methods? For eg: AggregationPruner might be better compared to FFNPruner because the number of parameters being pruned is very-very less in the former (similar to [1]). While I am not expecting an apples-apples comparison in terms of pruned parameters, these details will be informative. 
    - I am also aware that the total number of parameters to be pruned in AggregationPruner might be different depending on the size of KV cache which will vary; so the authors can make assumptions while reporting results in the tables. If it's not possible for some reason, please comment.
6. [**Experiment**] Can the authors perform an experiment on the choice of dataset on Greedy Search of Alpha? i.e how dependent the alpha values are with respect to dataset. Suppose it turns out to be dataset dependent, then is it safe to say that the method is calibration-dataset dependent? If so, I believe addition of these details (either in Appendix or main section) will be beneficial.

### Questions
**Possible Relevant citation**
- L464 - L468: Following the point 5 from weakness section, while not the exact relation is established, I believe this study [1] has some connection with respect to compressing the FFN blocks vs Attention blocks and the number of parameters involved while pruning different blocks. 

[1] The Cost of Compression: Investigating the Impact of Compression on Parametric Knowledge in Language Models - https://arxiv.org/abs/2312.00960

**Format**
1. [**Typo**] - L366: It is FFNPruner
2. [**Presentation Suggestion**] The authors might consider a small block diagram explaining the difference between FFNPruner, LayerPruner, AttentionPruner and AggregationPruner. Or maybe a diagram for the algorithm
3. [**Presentation Suggestion**] It seems like the assumptions/claims on GPU memory consumption has been mentioned at different places without an experiment to validate. So, the authors might reconsider text formatting.

**Note:** Suggestions are not mandatory improvements and the authors can wish to ignore it totally.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The study introduces a novel pruning algorithm that specifically targets aggregation parameters within large language models to reduce the model size and lower GPU memory usage during inference. By incorporating a rescaling parameter,  the method enhances the performance of pruned models without additional training.

### Strengths
1. This work proposes a novel pruning algorithm that requires no additional training and targets specific parameters within LLMs. 
2. This work introduces a rescaling parameter that adjusts the output of the pruned block to further improve the performance of the pruned LLM.
3. Extensive experiments demonstrate that the proposed method outperforms the recent block pruning algorithms.

### Weaknesses
1. While the experimental results support the effectiveness of the proposed method, the paper lacks theoretical analysis on why pruning aggregation parameters has minimal impact on model performance. The authors should provide more theoretical support or in-depth analysis. Specifically, the paper should explore the impact of removing these parameters on the information flow within the network. It would be beneficial to analyze how the removal of aggregation parameters affects the receptive field of the model and its ability to capture long-range dependencies. A theoretical framework explaining why these parameters are less critical than others would significantly strengthen the paper.
2. The paper bases the selection of the rescaling parameter α on grid search but does not discuss its impact on model performance in detail. The authors should further explore how the choice of α affects model performance. The paper should investigate the sensitivity of model performance to different values of α, and provide a more detailed analysis of how α interacts with the pruned parameters. For example, is there a correlation between the optimal α and the number of pruned parameters? Does the optimal α vary across different layers or model architectures? A more in-depth analysis is needed to justify the choice of α.
3. The paper focuses on model compression and acceleration but few discuss the generalization of pruned models across different domain tasks. It is crucial to evaluate the pruned model's performance on tasks that are significantly different from the training data to assess its robustness and generalization capabilities. The paper should include experiments on a wider range of datasets and tasks to demonstrate the general applicability of the proposed method. For example, how does the pruned model perform on tasks with different input modalities or tasks that require different reasoning capabilities?
4. The paper lessly discusses the model's performance and efficiency on actual hardware. The paper should include a detailed analysis of the practical performance of the pruned model on specific hardware platforms, including latency, throughput, and energy consumption. This analysis should consider the impact of pruning on memory access patterns and computational efficiency. It is important to demonstrate the real-world benefits of the proposed method.
5. To promote the study's reproducibility, authors are recommended to provide the code used in the experiment and the preprocessed data so that other researchers can reproduce the results.

### Questions
1. Existing methods bring additional training and huge computational overhead. What is the extra cost? What is the cost comparison between the proposed method and the existing method?
2. Why do existing methods maintain performance in domains not well covered by additional training data? What was the experiment? Analyze the specific reasons.
3. What is the key problem to be solved in this paper?

### Soundness
3

### Presentation
3

### Contribution
2
