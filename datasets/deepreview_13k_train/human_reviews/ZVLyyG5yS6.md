# Hierarchical Analysis: Monotonicity of Layerwise performance in Large Language Models

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
We introduce a quantitative framework to evaluate how Large Language Models (LLMs) learn tasks across all layers, revealing a `monotonicity phenomenon'. Specifically: 
i) performance at each layer consistently improves from one layer to the next on the pre-training set, and 
ii) this improvement is consistently observed across various downstream tasks. This monotonicity phenomenon indicates that LLMs effectively capture complex hierarchical features across diverse datasets. For example, our study on the abstraction of concepts using linear representations in word embeddings shows that the clarity of these abstractions progressively increases with each layer.
Finally, by leveraging this monotonicity, we can significantly reduce inference time and memory requirements by selecting the most appropriate layer, thereby enhancing the efficiency of LLMs in real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, a hierarchical analysis of LLMs is presented to illustrate the phenomenon of monotonicity in layerwise performance. The study shows that this progressive improvement in test accuracy, observed across successive layer in pre-training data and generalizes to a variety of downstream tasks.

### Strengths
1. Many state-of-the-art LLMs are compared in experiments and many datasets from diverse domains are used in evaluation. 
2. The experiments are reasonable and the results are convincing.

### Weaknesses
1. It'd be great if more experiments on the application of monotonicity could be conducted, for example, using more metrics other than test accuracy, and including more datasets.

### Questions
How does the size of training data affect the monotonicity of layerwise performance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses a phenomenon the authors call "monotonicity" in large language models (LLMs). This phenomenon shows that intermediate layers of pre-trained LLMs, when fine-tuned, can achieve comparable results on downstream tasks like classification or regression, similar to using the last layer's embedding. The authors analyzed the performance of various datasets applied to LLMs such as GPT-2, Llama 3.1, Phi 3.5 mini instruct, and GPT-Neo. The results showed that while later layers enhance downstream task performance, the performance curve stagnates several layers before the final layer. Thus it might be useful to use only those layers for inference as it can save computational as well as time cost.

### Strengths
- The paper is well written with a clear structure and good to understand.
- It outlines pracical advantages which can be used as a framework that is easy to apply by saving inference costs. This can be used for further academic research when dealing with LLMs

### Weaknesses
 - While mentioned in the text no results for regression tasks are reported
- While comparing LLMs of different providers (GPT2 – OpenAI, Llama 3.1 – Meta, Phi 3.5 – Microsoft etc.) a more extensive research by comparing models of the same provider with different sizes e.g. Llama 3.1 8B vs. Llama 3.1 1B would provide even deeper insights
- More detailled information oft he dataset collection would be useful to understand the set-up (e.g. label distribution)
- The only reported performance metric was accuracy depending on the label distribution (see above) different metrics might be more valuable

### Questions
- What was the label distribution of your downsampled datasets?
- Which datasets did you used for regression tasks and what are the results?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper evaluates LLMs' layerwise performance by focusing on the phenomenon of monotonicity, that is the performance at each layer consistently improves from one layer to the next one during pretraining. With extensive experiments on different datasets, they found that the layerwise performance improvement happens also on the dataset level, showing that the ability of LLMs to learn complex features during training is not limited to the data they were initially trained on but is a more generalizable characteristic to new tasks. They use the concept of linear representation in word embeddings to focus on consistent patterns and found that the monotonic effects exist with each layer. They suggest to focus on certain layers which are most appropriate for a certain task to save time and memory requirements.

### Strengths
Proper dataset selection and task design for the experiment.

### Weaknesses
1. I am afraid the main finding of the paper could be a bit superficial, as it talks about the monotonic effect, that is the performance improvement across layers in LMs. This finding is less interesting, although extensive experiments were conducted. Readers could be more interested in the "why" of this monotonic effect. More analysis regarding the explainablility could be required.

2. There is a lack of details of experimental results, with only introducing the experiments in section 5. More content of results analysis should be conducted, with comparisons of performance of different layers (layer combinations), models, tasks.

### Questions
NA

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the layerwise performance of Large Language Models (LLMs) and uncovers a "monotonicity" phenomenon: LLMs consistently improve their performance from one layer to the next, both on pre-training data and across various downstream tasks. The authors attribute this to the LLMs’ability to capture complex hierarchical features and propose leveraging monotonicity to optimize inference time and memory usage by selecting the most appropriate layer embedding for a given task.

### Strengths
The paper introduces the concept of “monotonicity” in LLMs, and combine ideas from hierarchical analysis and linear representation to explain the emergence of monotonicity, offering a fresh perspective on LLMs’ capabilities.

### Weaknesses
1.The conclusion of "monotonicity" presented in this paper aligns with common intuition—that predictions made using deeper layer outputs generally yield better results. Therefore, proving this seems to offer limited value.

2.The paper lacks sufficient discussion and citation of related works, including studies on layer pruning[1][2][3][4] and LayerSkip[5]. All of these works consider the redundancy in the model's layers and remove the unnecessary ones to reduce the number of parameters and speed up computation.

3.The quality of the writing in the paper could be improved. For instance, the font size in the figures is too small, and Figure 3 unnecessarily includes two identical images.

### Questions
1. Why is accuracy used to evaluate the performance of pre-training GPT-2’s  checkpoints? Perplexity is a more commonly used evaluation metric for this purpose.

2. This paper highlights that only the early layers are necessary to achieve decent performance on certain downstream tasks. This is similar to LayerSkip[1], which employs a specialized training method to achieve good performance using only the first half of the model's layers. However, this paper does not mention LayerSkip. Additionally, the downstream tasks selected are simple classification tasks that could be effectively handled by a 110M BERT model. This raises the question of how well the proposed method would perform on more complex classification and generation tasks, such as MMLU, GSM8K, or HumanEval.
[1]Elhoushi, M., Shrivastava, A., Liskovich, D., Hosmer, B., Wasti, B., Lai, L., ... & Wu, C. J. (2024). Layer skip: Enabling early exit inference and self-speculative decoding. arXiv preprint arXiv:2404.16710.

### Soundness
3

### Presentation
2

### Contribution
2
