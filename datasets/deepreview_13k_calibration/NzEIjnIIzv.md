# Bitune: Leveraging Bidirectional Attention to Improve Decoder-Only LLMs

- Decision: Reject
- Avg Score: 7.25
- Scores: 6, 10, 5, 8

## Abstract
Decoder-only large language models typically rely solely on masked causal attention, which limits their expressiveness by restricting information flow to one direction. We propose Bitune, a method that enhances pretrained decoder-only LLMs by incorporating bidirectional attention into prompt processing. We evaluate Bitune in instruction-tuning and question-answering settings, showing significant improvements in performance on commonsense reasoning, arithmetic, and language understanding tasks. Furthermore, extensive ablation studies validate the role of each component of the method, and demonstrate that Bitune is compatible with various parameter-efficient finetuning techniques and full model finetuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to incorporate decoder-only language models with bidirectional attention. The authors introduce a second set of attention matrices for bidirectional understanding and integrate it with the original causal attention. Experimental results confirm the effectiveness of the proposed method, and comprehensive ablation studies offer insights into the design choices.

### Strengths
- The proposed method is simple but effective.
- Comprehensive ablation results with reasonable baselines.

### Weaknesses
Some existing works focus on prefix language models (non-causal decoder-only model) that utilize bidirectional attention for processing prefixes (i.e., inputs and instructions). Representative ones include U-PaLM [1] and UniLM [2]. How does the proposed method differ from these? While these models incorporate bidirectional attention during pre-training, the proposed method applies bidirectional attention specifically during instruction tuning. What would happen if we applied simple instruction tuning to these prefix language models (non-causal decoder-only model)? What are the advantages of bidirectional instruction tuning after causal decoder-only pre-training like the proposed method? I would like to see more discussions and even experiments on the comparison.

Another comment would be to visualize bidirectional attention on some examples. This could help highlight cases where bidirectional attention behaves differently from causal attention and therefore bring benefits.

### Questions
Would the proposed bidirectional instruction tuning affect the quality for pure generation tasks?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper looks at how to add bidriectional attention to pre-trained decoder-only LLMs. This is done by learning new Key and Value matrices used during attention without the causal masking. Instead of just replacing the original matrices, they run the "encoder" part of the network (the parts with bidirectional attention) twice, once with the original weights and causal masking and once with the new weights. The resulting KV values are then mixed with a learnable weight. These mixed values are then attended to during autoregressive generation.

They find this produces strong results on many datasets with many different LLMs. They also include a lot of ablation experiments.

### Strengths
The paper includes a lot of ablations that are very convincing of the efficacy of their approach. As I was reading, I keep thinking, I wonder if the see effect is because of X or Y instead of the bidirectional attention, and each time they had an ablation covering that possibility!

### Weaknesses
In Figure 2 they show that the initial value of the mixing ratio can cause large differences in the final average ratio once convergence is reached. Figure 3 shows some histograms of mixing ratios at different layers, and Table 6 has experiments that explore how the initial value affects performance. However, the scale of these experiments is small, and the results are inconclusive. Given the initial value causes such a large difference in the ratio, it would have been nice to see a deeper dive into this.

The experiments in the paper focus on datasets that have clear single-turn input/output pairs. Given that many LLMs these days are used for chat applications, it would have been nice to see some experiments on how bitune training effects these chat applications. As the text gets longs (more turns into the chat) does the effect of the initial bidirectional attention decrease? Does it help the model follow the initial prompt better? Can their approach be applied to mutli-turn dialogue (all of some of the user text is bidirectional which model generated text is causal?)

### Questions
Have you tried training the bitune attention matrices on a prefix language modeling task instead input/output formatted tasks? For example, randomly cutting a sequence of text in two pieces, applying bidirectional attention to the first part and then training on the second? This would also help answer the question of how much data is needed to learn the bitune matrices, which is mentioned but not answered in the paper.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to improve decoder-only LLMs' effectiveness in downstream tasks by enhancing their representation of the input prompts. To achieve that, they introduce bi-directional attention into prompt processing. An LLM learns to represent a given prompt with both causal and bi-directional attention mechanisms and then fuse two features with the learnable combination. Experiments demonstrate the effectiveness of the proposed method in instruction-tuning and question-answering settings. Further ablation study verifies the performance gain comes from the bi-directional attention instead of more parameters or the fusion of two features.

### Strengths
1. The proposed idea addresses the innate limitation of decoder-only LLMs while preserving their generation efficiency.
2. The experiments are comprehensive, covering various LLMs and downstream tasks.
3. The ablation study helps identify the contribution of different design choices.

### Weaknesses
1. As indicated by the Related Work section, there are several prior works investigating the idea of bi-directional attention in decoder-only LMs. The novelty of this work is thus somewhat limited. It might be helpful if the authors could further discuss how their method stands out. The core difference from methods like prefix-LM seems to be the fusion of causal and bi-directional features, but this incremental change may not be sufficiently novel to warrant significant attention. The method does not introduce a fundamentally new approach to incorporating bi-directional attention, but rather a specific way of combining existing attention mechanisms.
2. It is unclear why decoder-only LLMs would still face the limitation of representing language using causal attention given that they have undergone extensive pre-training and fine-tuning based on causal attention. The argument that causal attention prevents the model from 'seeing' the full context at the beginning of the sequence is not entirely convincing, as the model has been trained to understand language sequentially. A more detailed analysis of the hidden states, showing how the lack of bi-directional attention specifically hinders representation, would strengthen this point. It would be beneficial to see concrete examples where the causal attention mechanism demonstrably fails to capture necessary contextual information.
3. The proposed method only applies to the given prompt but not the generated response, which could also benefit from bi-directional attention. Also, the need to recompute the KV-cache for multi-turn scenarios makes the method less practical for widespread use. The computational overhead of recomputing the KV-cache, especially for longer sequences, could outweigh the benefits of improved representation. It is not clear how this method would scale to real-world applications with long conversational histories.

### Questions
How could this method be generalized to represent the generated tokens?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents “Bitune”, a method that enables pre-trained causal LMs (unidirectional attention), to use bidirectional attention. The proposed Bitune method makes use of sparse LoRA-based adaptors to create a bidirectional version of the model. Each prompt is passed through both the causal and bidirectional version of the model, and then both sets of features are combined into a single (key, value) cache. This cache is used to generate the rest of the sequence.

### Strengths
1. The paper does demonstrate a performance gain from Bitune compared to the baseline pre-trained model and LoRA fine-tuned model on several language modeling benchmarks (table 1,2).
2. Paper does a good job of doing a thorough ablation study to verify the necessity of different components of their proposed method in section 3.3.
3. Paper does discuss the computational cost of adapting the base model to be bi-directional and provides a reasonable solution to mitigate the computational overhead: using parameter efficient fine-tuning. They also highlight that Bitune is not tied to the specific method for updating weights, and instead can be adapted to use different types of weight updating methods.

### Weaknesses
Each round of Bitune inference effectively requires two inference passes which can be (time and memory) expensive (especially for really long sequence generation tasks). The authors do highlight this limitation in the discussion section and Appendix 6.4. According to their results, it seems that the most impacted part of the training/inference pipeline is the additional training time cost. Inference time costs did increase but to a much lesser extent. This timing increase could be reasonable if an end user of Bitune feels that the performance gains of the Bitune model warrants the extra computational time. I note that the time analysis is done for a fixed generation length of 200 tokens; I am curious to see how the time scales as generation length increases (e.g., 2000 tokens generated).

### Questions
n/a

### Soundness
4

### Presentation
4

### Contribution
3
