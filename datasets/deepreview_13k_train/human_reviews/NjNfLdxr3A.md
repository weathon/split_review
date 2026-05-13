# VeRA: Vector-based Random Matrix Adaptation

- Decision: Accept
- Scores: 8, 8, 5, 8

## Abstract
Low-rank adapation (LoRA) is a popular method that reduces the number of trainable parameters when finetuning large language models, but still faces acute storage challenges when scaling to even larger models or deploying numerous per-user or per-task adapted models. In this work, we present \textbf{Ve}ctor-based \textbf{R}andom Matrix \textbf{A}daptation (VeRA), which significantly reduces the number of trainable parameters compared to LoRA, yet maintains the same performance. It achieves this by using a single pair of low-rank matrices shared across all layers and learning small scaling vectors instead. We demonstrate its effectiveness on the GLUE and E2E benchmarks, image classification tasks, and show its application in instruction-tuning of 7B and 13B language models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes ELoRA, a new method for parameter-efficient finetuning that trains only the scaling vectors for low-rank parametrized versions of linear layers. The proposed method reaches the same quality as LoRA on a variety of benchmarks while having more than 10 times fewer trainable parameters.

---
Post-rebuttal update: thank you for the revised version! It addresses most of my concerns, and I am happy to increase the score to 8.

### Strengths
* The work proposes a simple idea that works quite well in practice, according to the experiments.
* Authors have a comprehensive evaluation setup, testing ELoRA across several model sizes and datasets and comparing it with baselines.
* The influence of each component of ELoRA is investigated within a detailed ablation study.
* Overall, the paper is well-written and all the contributions are easy to understand.

### Weaknesses
 * The idea of using random matrices for parameter-efficient finetuning has been proposed previously in the context of text-to-image generation [1]. Although the ideas of the submission and that paper are quite different (also, the paper is quite recent), in my opinion, it would be great to mention LiDB (Lightweight DreamBooth) in the related work section to give the reader additional context.
* My primary concern with respect to the experiments is that the instruction tuning evaluation is performed mostly through GPT-4 queries on a very small dataset. In my opinion, this approach suffers both from the lack of reproducibility (as we know, the model behind the GPT-4 API might change in the future) and a narrow coverage of possible contexts that might result in high variance of the metric. I think that using more established benchmarks (such as MMLU or BIG-Bench) would give a better picture of how instruction-finetuned models perform after PEFT.
* Similarly, I think that broader evaluation of instruction tuning should include a larger set of models than just LLaMA-2. Personally, I would move Table 4 and Table 5 to the appendix (they take a lot of space and are not directly related to the topic of the paper) and replace that with additional experiments, ideally for models with higher parameter counts.


### Questions
* Technically, it should be possible to have different random matrices in different layers (the cost of storing one random seed per layer should be negligible), which might increase the capacity of the model even further. I wonder if you have explored this idea in preliminary experiments? It is quite surprising to me that a single random structure is sufficient for PEFT across all layers in a Transformer model — perhaps there is something we can infer from that.
* I think that the work would benefit from a bit more analysis behind the reasons of why random projections work that well in the context of parameter-efficient finetuning. At the very least, it might be interesting to compare the structure of the learned weights for LoRA and ELoRA trained with a single rank: intuitively, the latter should approximate the former, but is that true in practice?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel parameter-efficient LLM finetuning algorithm which is considerably more parameter-efficient than LoRA. The idea is to use 2 random matrices shared across all of the layers in the LLM, but to use two sets of diagonal scaling matrices to modulate the shared random matrices differently for each layer. The results indicate that the proposed method requires roughly an order of magnitude less parameters while maintaining or exceeding the performance of LoRA.

### Strengths
1) The paper is very easy to read
2) The method is simple and easy to understand
3) The experimental results are extensive. All claims are backed up by experimental evidence. Ablation experiments give further insights

### Weaknesses
I don't really see any weaknesses in this paper

### Questions
1) Have you tried extending this method to finetuning large image models? What about large multimodal models?
2) What are the training time benefits of your method? Is there a GPU memory benefit? Is there a latency benefit? Does your method train faster than LoRA because it has less parameters?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose a way of reparametrization of the low-rank matrices in a LoRA method, by freezing a single pair of randomly initialized matrices shared across all adapted layers, and introducing trainable scaling vectors that allow for layer-wise adaptation.

### Strengths
- Introduced a simple but elegant way to reduce trainable parameters in a LoRA. This effectively reduces storage cost due to introduced parameters for different downstream tasks.

### Weaknesses
 - Performance can be hurted using this method, even the evaluation is only on a limited set of GLUE benchmarks.

- The method should be evaluated on generative tasks as well, including translation and question answering. Classification task and summarization task are known to be more resilient to the lose of model capacity or trainable parameters.

- The paper is not well written. Figure 3 and Figure 4 are each on a single but different task. Why not reporting a mean score on GLUE?

- The paper lacks explanation on why Table 3, with fewer tunable parameters, ELoRA has better instruction finetuning scores than LoRA. It is a bit of counterintuitive.

### Questions
- Are there any theoretical proof that random matrices with scaling vectors would work better than LoRA?

- Consider evaluating the method on Generative tasks?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
> **TL;DR:** The proposed ELoRA algorithm achieves a 10x reduction in trainable parameters compared to LoRA, while maintaining performance levels. This paper should be accepted in its current form. Addressing my concerns and questions would improve my score.

The paper introduces an efficient finetuning method, ELoRA, for pretrained language models, addressing the storage challenge when deploying numerous adapted models. ELoRA achieves a 10x reduction in trainable parameters compared to LoRA, while maintaining performance levels, as demonstrated on the GLUE benchmark. It leverages shared random low-rank matrices and small layer-wise trainable scaling vectors to reduce memory usage. This approach is ideal for scenarios requiring multiple finetuned models, such as cloud-based personalized AI services, by improving serving efficiency. The method's potential application in various domains and further optimizations like dynamic parameter allocation are areas for future research.

### Strengths
* **S.1.** The paper is well written and is easy to follow. The illustrations and results are informative and clear.
* **S.2.** The proposed ELoRA algorithm seems novel and tackles an important problem.
* **S.3.** The experiments are conducted on multiple datasets and architectures with 5 different random seeds. ELORA achieves high accuracy while requiring significantly less parameters compared to existing algorithms.
* **S.4.** The experiments are thorough and an ablation study is conducted.

### Weaknesses
 * **W.1.** The experiments are conducted solely on NLP tasks with LLMs. Adding experiments on different domains such as diffusions on CV would help. Specifically, the paper lacks an analysis of how ELoRA performs on tasks with different data modalities and model architectures. For example, it would be beneficial to see results on image classification or generation tasks using convolutional or transformer-based vision models. This would help to assess the generalizability of the proposed method.
* **W.2.** The paper does not provide a theoretical analysis on the ELoRA algorithm or its limitations. A theoretical analysis could provide insights into why ELoRA works, under what conditions it is expected to perform well, and what its limitations are compared to other methods. For example, it would be useful to analyze the expressivity of the low-rank matrices and the scaling vectors, and how they affect the optimization landscape.

### Questions
* **Q.1.** In Table 2 for the RTE dataset the LoRA algorithm achieves significantly higher results on the RoBERTa-base model compared to the the other algorithms. Is this a mistake?
* **Q.2.** Why are the PEFT algorithms achieving higher accuracy compared FT on the RTE dataset? Is this just overfitting?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
