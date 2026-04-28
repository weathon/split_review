# Streamlining Redundant Layers to Compress Large Language Models

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
This paper introduces LLM-Streamline, a pioneer work on layer pruning for large language models (LLMs). It is based on the observation that different layers have varying impacts on hidden states, enabling the identification of less important layers to be pruned. 
LLM-Streamline comprises two parts: layer pruning, which removes consecutive layers with the lowest importance based on target sparsity, and layer replacement, a novel module that trains a lightweight network to replace the pruned layers to mitigate performance loss. Additionally, a new metric called stability is proposed to address the limitations of the widely used accuracy metric in evaluating model compression. Experiments show that LLM-Streamline outperforms both previous and concurrent state-of-the-art pruning methods in terms of both performance and training efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
This submission presented LLM-Streamline, a new model pruning method for LLMs. Besides traditional pruning, this method also proposed layer replacement, a novel module that trains a lightweight network to replace the pruned layers to mitigate performance loss. In addition, the authors also proposed stability as a new metric. Experimental results show the superiority of this method.

### Strengths
Basically, this submission has two major innovations:
1. layer replacement
2. new metric named stability.

The first one is a very good contribution that mitigates the loss of pruning only.

### Weaknesses
I didn't find any weakness of this submission.

### Questions
I'm not an expert of LLM pruning/compression field. I'm curious why you didn't compare with some knowledge distillation method for LLM, for example 
https://proceedings.mlr.press/v235/ko24c.html

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this work, the authors propose LLM-Streamline, a new approach for compressing large language models (LLMs) by pruning layers based on cosine similarity and replacing the pruned layers with a lightweight network to preserve or even enhance model performance. This two-step method is shown to effectively reduce model size with minimal loss in accuracy, as demonstrated by experiments across various classification and generation benchmarks. Additionally, the work introduces a stability metric to address limitations of traditional accuracy metrics in evaluating pruned models. Experimental results highlight the superiority of LLM-Streamline over other state-of-the-art pruning methods in terms of accuracy retention and computational efficiency, especially under hardware constraints. Overall, this work offers a novel technique with practical implications for large-scale LLM deployments.

### Strengths
1. Originality: This paper combines layer pruning with lightweight network replacement in a novel approach for compressing LLMs. This method effectively maintains model performance even after significant pruning.
2. Significance: The proposed stability metric enhances LLM compression evaluation by addressing limitations in standard accuracy metrics, providing a potentially more reliable measure of retained model performance.
3. Technical Quality: The experiments are comprehensive, covering various benchmarks that showcase the model’s effectiveness in classification and content generation. Each step of the pruning and replacement process is clearly explained, highlighting the technical soundness of the approach.
4. Practical Implications: LLM-Streamline improves model efficiency while retaining performance, making it valuable for real-world applications where computational resources are limited.

### Weaknesses
1. Metric Justification: While cosine similarity is chosen as the primary metric for layer redundancy, additional justification for this choice over other metrics (e.g., perplexity, Euclidean distance) would be beneficial. Specifically, the paper lacks a detailed analysis of how cosine similarity captures redundancy in the context of transformer layers, and why it is superior to alternatives like Euclidean distance, which might be more sensitive to the magnitude of layer activations. A more thorough investigation into the properties of these metrics, especially in relation to the specific architecture of the LLMs being pruned, is needed.

2. Comparison with Other Methods: While the authors mention alternative approaches, such as LoRA, they do not provide a detailed comparison. A more thorough discussion of how LLM-Streamline performs relative to other popular fine-tuning and compression techniques would give readers a clearer perspective. The paper should include a more granular comparison, considering factors such as the number of trainable parameters, the computational cost of training, and the sensitivity to hyperparameter tuning, in addition to the final performance metrics.

3. Explanation of Stability Metric: The paper could simplify its explanation of the stability metric, making it more accessible to readers new to model compression. Clarifying why stability offers practical advantages over accuracy would also be beneficial. The current explanation lacks a clear, intuitive definition of stability and how it is calculated. A more detailed explanation, possibly with a concrete example of how a model could have high accuracy but low stability, would significantly enhance the reader's understanding.

### Questions
1. Can you provide more detail on why cosine similarity was chosen as the primary measure for layer redundancy? How does it compare to using perplexity or other metrics?
2. For the stability metric, is there a specific scenario or task where it offers clear advantages over traditional accuracy measures? An illustrative example would help clarify this.
3. Have you considered a detailed comparison with other model compression methods, like LoRA? This would help highlight what sets LLM-Streamline apart.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents LLM-Streamline, a novel layer-wise pruning and replacement framework aimed at compressing large language models (LLMs) by identifying and removing less significant layers. The process is divided into two stages: (1) Layer Pruning to identify and prune layers with minimal impact based on cosine similarity, and (2) Layer Replacement, which trains a lightweight network to compensate for the removed layers, mitigating performance loss. Additionally, a new stability metric is introduced to more accurately reflect performance post-pruning, which is compared against existing methods across multiple benchmarks.

### Strengths
* This paper uses a lightweight network and training based on hidden states before and after compression to compensate for the loss caused by pruning, reducing the need for computing resources and leading to better precision recovery.

* The continuous layer pruning used in this paper reduces the complexity of the compressed model and is easier to accelerate on hardware than unstructured pruning and other methods.

* The paper provides an in-depth analysis of the limitations within traditional accuracy metrics, offering a well-thought-out solution to address it. Additionally, the ablation studies are exceptionally comprehensive, with thorough and insightful analysis throughout.

### Weaknesses
 * The sparsity levels explored in the paper do not exceed 25%, leaving higher sparsity scenarios untested. In contrast, methods like LLMPruner evaluate and compare performance at a 50% sparsity level. This omission raises concerns about whether the proposed contiguous layer pruning approach would remain effective at higher sparsity levels. Specifically, the paper lacks analysis on how the layer replacement network would perform when a larger number of layers are removed, potentially leading to a more significant information loss that is harder to compensate for. The current experiments do not sufficiently demonstrate the robustness of the method under more aggressive pruning conditions.

* The models selected for evaluation are all based on the LLaMA architecture, which limits the assessment of the proposed method’s generalizability. Testing on more diverse architectures (e.g., MoE, GQA) and larger models with greater sparsity requirements (such as LLaMA-30B, LLaMA-70B) would provide a more comprehensive validation of LLM-Streamline’s effectiveness across various model types and scales. The paper does not explore how the proposed layer pruning strategy interacts with different architectural features, such as the number of attention heads or the use of gated activation functions, which could significantly impact the pruning outcome. This lack of diversity in the evaluation makes it difficult to ascertain the method's applicability to a broader range of LLMs.

* The study can add comparisons of real hardware performance (e.g., inference speed, FLOPs) with other structured pruning methods, where actual hardware constraints play a critical role in model selection and pruning effectiveness. The paper should include a more detailed analysis of the computational cost associated with the layer replacement training, including the training time and the resources required. Furthermore, a comparison of the inference speed and memory footprint of the pruned models on actual hardware would provide a more practical perspective on the method's efficiency.

### Questions
Please refer to weaknesses section for questions.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work addresses the compression of LLMs through layer pruning and layer replacement. A lightweight module is trained to substitute for the pruned layers. Additionally, a new evaluation metric is proposed to mitigate the limitations of accuracy-based metrics.

### Strengths
* The concept of layer replacement for performance recovery is intriguing.
* I appreciate the detailed comparison between perplexity and cosine similarity as pruning metrics, effectively revealing the data-sensitive drawbacks of perplexity.
* The paper comprehensively covers various types of LLMs and evaluation benchmarks.
* I like the exploration of multiple designs for lightweight networks.
* Overall, the paper is well-written and easy to follow.

### Weaknesses
 * I think that replacing layers with FFN or Transformer layers may not provide the full inference speed benefits typically gained through layer pruning, even if parameter counts remain similar. Could you analyze the speedup of layer replacement and compare it with pure layer pruning?
* It’s unclear how to set the number of contiguous layers (n) in Equation (3). How many layers are typically removed at once during pruning? Could you elaborate on this aspect?
* Is this method intended as one-shot pruning (pruning-replacement once) or iterative pruning (pruning-replacement, then pruning-replacement again)? Would it be possible to compare the two approaches?
* Why is MSE chosen as the loss function for the replacement module in Equation (3)? What would happen if it were trained using the original language model loss?
* A 25% compression rate seems relatively modest. Could you provide a comparison at higher pruning ratios (e.g., 50% layer removal) against baseline methods?

### Questions
Please see the above weakness section.

### Soundness
2

### Presentation
2

### Contribution
2
