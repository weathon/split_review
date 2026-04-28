# Reassessing Layer Pruning in LLMs: New Insights and Methods

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
Although large language models (LLMs) have achieved remarkable success across various domains, their considerable scale necessitates substantial computational resources, posing significant challenges for deployment in resource-constrained environments. Layer pruning, as a simple yet effective compression method, removes layers of a model directly, reducing computational overhead. However, what are the best practices for layer pruning in LLMs? Are sophisticated layer selection metrics truly effective? Does the LoRA (Low-Rank Approximation) family, widely regarded as a leading method for pruned model fine-tuning, truly meet expectations when applied to post-pruning fine-tuning? To answer these questions, we dedicate thousands of GPU hours to benchmarking layer pruning in LLMs and gaining insights across multiple dimensions. Our results demonstrate that a simple approach, i.e., pruning the final 25\% of layers followed by fine-tuning the \texttt{lm\_head} and the remaining last three layer, yields remarkably strong performance. Following this guide, we prune Llama-3.1-8B-It and obtain a model that outperforms many popular LLMs of similar size, such as ChatGLM2-6B, Vicuna-7B-v1.5, Qwen1.5-7B and Baichuan2-7B.
We release the optimal model weights on Huggingface\footnote{\url{https://huggingface.co/YaoLuzjut/Llama-3.1-6.3B-It-Alpaca} and \url{https://huggingface.co/YaoLuzjut/Llama-3.1-6.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the author spent thousands of GPU hours to reassess the practices and insights of layer pruning in LLMs. The results showed that reverse-order pruning is simple yet effective (simply pruning the last several layers performs better than many complex pruning metrics); partial-layer fine-tuning (freezing the other layers and fine-tuning only the last few remaining layers and lm_head) can achieve higher accuracy than LoRA fine-tuning; one-shot pruning in more beneficial than iterative fine-tuning considering both training costs and performance gains.

### Strengths
+ The structure of the paper is well-designed and organized
+ The background information is rich, especially those math equations, which makes it easy for someone who is not familiar with this field to understand the concept of layer pruning and relevant techniques. 
+ Because the paper is an experiments-based publication, it is very good there are lots of diverse experiments conducted in the paper, including plenty of different datasets and models.
+ The results of the experiment are very rich in graphs and tables, and the results are clear briefly.

### Weaknesses
- Some of the metrics don’t have a mark to indicate whether the lower or the higher it is, the performance is better, especially some uncommon metrics.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

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
This paper explores layer pruning in Large Language Models (LLMs) to reduce computational overhead while maintaining performance. The authors conduct extensive experiments across multiple dimensions, including different layer selection metrics, fine-tuning methods, and pruning strategies. Their findings suggest that a simple reverse-order pruning strategy—pruning the last 25% of layers—performs as well as more sophisticated methods. Applying these insights, they prune Llama-3.1-8B-Instruct to create Llama-3.1-6.3B-It models, which outperform several popular LLMs of similar size.

### Strengths
1. The paper conducts lots of empirical study to support their findings, which may be beneficial for the community for future research.

2. By releasing the pruned model weights and code, the authors contribute to open science and facilitate reproducibility and further research in the field.

### Weaknesses
1. The main findings emphasize that simple methods can be highly effective. While valuable, this insight may be seen as incremental, confirming existing intuitions rather than introducing new methodologies. The effectiveness of pruning the last layers and fine-tuning only specific parts of the model aligns with established practices in model compression and transfer learning.

2. The study compares simple pruning metrics with Block Influence (BI) from ShortGPT [1] but does not include comparisons with more recent and advanced layer pruning methods such as SLEB [2] and FinerCut [3]. Both SLEB and FinerCut have introduced innovative approaches to layer pruning in LLMs, offering potentially significant improvements in efficiency and performance.

3. Although the paper finds that reverse-order pruning (pruning the last several layers) is effective, it does not delve into why this method outperforms other metrics. An analysis of the role and importance of the last layers in LLMs could provide valuable insights and contribute to the development of more effective pruning strategies. Furthermore, the lack of clarity regarding the specific mechanisms through which the proposed method achieves its results raises concerns about its generalizability and robustness. The reliance on specific datasets for fine-tuning also introduces a potential bias, as the observed accuracy improvements may not be consistently replicable across different datasets or tasks.

### Questions
1.  Despite the authors' efforts to provide code and models, some experimental details are insufficiently specified. For example, exact hyperparameters for all experiments, detailed configurations of the fine-tuning setup, and the procedures for selecting and processing calibration samples for the data-driven pruning metrics are not fully described.  Can the authors give more details?

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
5

### Summary
In this work, the authors conduct comprehensive empirical study on layer-wise post-training pruning across various LLMs. Specifically, they present three key conclusion: (1) reverse-order layer pruning outperforms other layer-wise pruning importance metrics, (2) fine-tuning the last few remaining layers yields better performance than LoRA, and (3) iterative layer pruning shows no advantage over one-shot layer pruning. Based on these analysis, the authors develop pruned models using Llama-3.1-Instruct, achieving better performance compared to other LLMs of the same or larger size.

### Strengths
1. The paper is well organized and easy to follow.
2. It‘s inspired to see fine-tuning last few remaining layers (e.g.,  3) can outperform LoRA. 
3. The pruned model based on LLama-3.1-Instruct shows better performance compared prior LLMs with similar model size.

### Weaknesses
1. Similar conclusions to Insight #1 and Insight #3 have been noted in prior work. Specifically, [1] demonstrates that deeper layers are less effective, so it would be helpful to clarify how this work differs from [1]. Additionally, as the authors mentioned, [2] shows that iterative pruning provides no added benefit.

2. The authors only present the results of the pruned model after fine-tuning. It would be informative to see the results prior to fine-tuning to see if the proposed method consistently outperforms others.

3. It would also be valuable to test the proposed method on the OPT model. As revealed in [3], unlike other LLMs, OPT models exhibit high redundancy in shallow layers rather than in deeper layers by using cosine similarity analysis.

### Questions
Overall, I find this work valuable for offering new insights into post-training layer-wise pruning, particularly with Insight #2. However, the work could be strengthened by addressing the questions as shown in Weakness above: (1) clarify the differences compared to [1], (2) analyze performance both before and after fine-tuning, and (3) evaluate the proposed method on the OPT model.

### Soundness
3

### Presentation
4

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
This paper mainly focuses on the ablation study of layer pruning in LLMs.
The paper first explores the different layer pruning strategies with different fine-tuning methods.
Then, they find that the reverse-order is the optimal layer pruning strategy. 
Meanwhile. they find that the partial-layer fine-tuning outperforms LoRA-based techniques.
Finally, they release two models directly pruned from Llama-3.1-8B-Instruct, which outperforms other popular models with similar sizes.

### Strengths
1. The ablation study about layer pruning and fine-tuning in this paper seems to be good.
2. The paper finds that the partial-layer fine-tuning outperforms LoRA-based techniques, which is important to the post-pruning fine-tuning research areas.

### Weaknesses
1. The novelty of this paper is limited. Most works have done in this paper are kind of ablation study. The paper does not propose any new method, the paper only provides the findings after the ablation study with its comprehensive benchmarking. The method of pruning layers in 'Reverse-order' is only the findings obtained from the ablation study compared to other methods, which is not a novel method. Meanwhile, the ablation of layer pruning methods is only conducted with models with around 7B or less parameters, which shows limited generalization to larger models.
2. The ablation study for layer pruning in Table 1 2 5 8 does not include the large models, for example LLaMA-2 30B, LLaMA-2 70B and LLaMA-3 80B, thus the generalization of this method on larger models is limited. And so does the ablation of fine-tuning. As the model becomes larger, the redundancy of the model becomes larger, which is more important to show the pruning results with large models, especially 70B or 80B models.
3. According to Table 7, it shows that the fine-tuning dataset is sensitive to the model performance, which hurts the generalization of this method. The work does not discuss the calibration dataset used for those other pruning methods, which results in the bias of the results. Meanwhile, the paper does not include the ablation study with different number of samples used in sft.

### Questions
1. How about the performance of this method when applied to large LLMs including LLaMA-2 30B, LLaMA-2 70B and LLaMA-3 80B? As it is intuitive to apply pruning techniques (especially layer pruning methods) on larger models (especially 70B or 80B) models, because there are much more redundancy compared to 7B model family.
2. How about the generation speed compared to other models with similar model size included in Table 8?
3. How about the ablation study with different number of training samples in sft?
4. What is the experiment setup for other layer pruning methods? especially, what is the number of samples for the calibration?

### Soundness
2

### Presentation
2

### Contribution
2
