# Stutter makes large language models smarter

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Large language models (LLMs) have achieved remarkable success in generating coherent and contextually relevant text. However, their large parameters and high memory requirements limit their efficiency and adoption in industry and academia. Recent studies have shown that dynamically adjusting inference operations can improve model performance without significantly increasing size. In this paper, we introduce the stutter mechanism, a novel method that enhances transformer models by selectively applying additional layers to more challenging tokens. This approach mimics a human speaker’s stutter, allocating more computational effort where needed, thus improving
language capabilities without generating excessive tokens. Our experiments with various Pythia models demonstrate that the stutter mechanism consistently enhances performance across benchmark datasets. Specifically, the Pythia-410M model, enhanced by our method, outperforms the larger Pythia-1B model on WinoGrande and WSC. Additionally, our method is data-efficient, requiring only less than 1% of the pretraining data for the additional training. These results highlight the stutter mechanism’s potential to enhance LLMs’ efficiency and performance in real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposed a new mechanism called "stutter" to allow the model to use more compute during the inference time. The mechanism works in the following way: for every token, the model encodes it twice, and the second time, each layer has a module that attends to the last step's last layer representation. This allows the model to "think twice". The design is very simple and minimalistic and requires as few as 1B tokens to train. 

The proposed method has huge extensibility: future work can explore when to "stutter" (for example, at more difficult prediction steps) and can stutter for multiple steps. This is similar to the recently popular "inference scaling" scheme. With almost no increase in the model parameters, the method allows the model to use more compute in the inference time, hence better results.

The authors conducted experiments on several small-scale Pythia models, which show some improvement on standard benchmarks in both few-shot/zero-shot settings. There are also ablations on the effect of which layer that stutter modules attend to and how many times to stutter. While this is still a very initial exploration (no experiments on potential stutter location selection; no experiments on truly generative tasks), the idea is very interesting and holds a lot of potential.

### Strengths
(1) The proposed method is clear, intuitive, and simple. The method holds a lot of potential in the inference-scaling scheme. 

(2) The empirical gain on small models are significant on certain tasks.

### Weaknesses
(1) The selected tasks mostly don't require complex reasoning (unlike tasks like GSM8K). It is unclear how this method will perform on tasks that truly require reasoning. I understand that tasks like coding/GSM8K will have only trivial results at this scale (1B), but maybe the authors can explore some more synthetic tasks that require multi-hop reasoning. 

(2) The gain is not very consistent or significant across different tasks. In this case, the authors should also report variance to show the significance of the results.

(3) **My biggest concern** is that the method is extremely inefficient in inference. The current setting is that the model stutters at every token; since each stutter step needs to look at the last step's last layer, this essentially turns the parallel prefix filling (encoding the context) into an autoregressive procedure, which will be extremely slow, especially when the prefix is long. To the best of my knowledge, the authors did not discuss this. One remedy I can think of is to only stutter at the last token before the model outputs the answer. 

(4) The authors did not include discussion/comparison to a very relevant method: pause tokens (Goyal et al.). In fact, pause tokens are more efficient because they can still encode the prefix in parallel like standard transformers instead of the autoregressive style.

Goyal et al. Think before you speak: Training Language Models With Pause Tokens

### Questions
Please see the weakness section.

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
3

### Summary
The paper proposes a parameter-sharing method to achieve deeper Transformer-based language models (LMs) without significantly increasing the number of total model parameters.

To achieve that, the authors aim to continually upcycle existing pretrained LMs (base LMs)  by introducing a light-weight adapter module, termed as token-retrospect map (linear attention).
For efficiency purposes, the base LM is kept frozen during the adaptation, which provides the initial hidden states of the input tokens.
Based on those initial hidden states, a second adapted LM is applied atop with the adapter network to re-aggregate context information with deeper layer representations.
This technique can also be reviewed as another means of recurrency mechanism.
The particular implementation considered in this paper achieves an adapted LM with twice depth as that of the base LM with roughly additional 10% more parameters.

The paper applies the proposed technique to the Pythia LM family with model sizes ranging from 160M to 1B. A collection of language understanding datasets are used for evaluation.
Compared with the corresponding base LMs, the adapted LMs based on the proposed method are observed to have at-odds performance improvements.

### Strengths
Enhancing/upcycling existing pretrained LMs with parameter-efficient methods to achieve new capabilities is an important research topic.
The proposed method is a reasonable technique.

### Weaknesses
The exposition of the paper requires substantial improvements:

*The cross layer parameter sharing is a widely studied technique in previous work (e.g., albert [1] inter alia). It is necessary to cite and discuss properly.

*Please update the citation based on ICLR recommendations, e.g., using \citep.

*Please provide proper citations for models/methods/datasets used in the paper, e..g, line 066, line 287. Without proper citations, it is hard to evaluate whether the experiment set up is properly and the comparison is meaningful.

*As the entire input token sequence is used for the second pass, it is good to reflect that in Fig 1.

The experiment setup is problematic without enough convincing evidences:

*Across all considered LMs with varying sizes and datasets, the improvements of the proposed method over base LM are at odds. Even for cases where there are certain improvements (e.g., WSC), the paper fails to include any insights, e.g., what are those improved cases and are those results statistically significant?

*As the proposed techniques trade-off the computation complexity for parameter efficiency, it is good to picture the performance vs computation costs between base LMs and the proposed method. Without, it is hard to justify whether the extra costs are truly worthy.

*It is good to test the robustness of those chosen hyperparameters. For example, It is unclear how those few-shot examples are chosen and how sensitive those decisions are. How the 1B token training dataset is selected from Pile and what domains are included?

*Although it is good to consider LMs of varying sizes, it is better to include LMs from other families. This could provide more insights on the generalizability of the proposed method, e.g., Transformer architecture variants, pretraining corpus and tokenizers.

### Questions
For the second pass, is the token retrospect allowed to attend over previously generated token hiddens in the second pass? Why or why not?

Can you provide more info on the continual pretraining? What hardware is used? For the 1B token training dataset, how many epochs are used? Do you see any benefit with more tokens or longer training?

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
The paper presents a stutter mechanism on transformer models by applying additional token-retrospect layers ( newly trained additional attention layer) and repeating the token twice. Experiments are conducted on Pythia models with an additional training of 1 billion token, and are evaluated on several LLM benchmarks.

### Strengths
The motivation of stutter mechanism is intriguing, by correcting the possible wrong tokens with a new token-retrospect map layer to do correction. The presentation and writing are clear and easy to follow. The authors conducted comprehensive benchmarks across multiple datasets, including LAMBDA, PIQA, WinoGrande, WSC, ARC, SciQ, and LogiQA, using Pythia models of three different parameter sizes—160M, 410M, and 1B.  Additionally, it analyzes the effectiveness of chosen layers in sec4.4.2, showing that attending to specific layers could improve the performance.

### Weaknesses
1.  **The reported performance improvement is not convincing**. Specifically, for example, we can see from Table 2 that base model vs stutter methods are 0.230 vs 0.215 on LogiQA, 0.892 vs 0.894 on SciQ. Similar results can be found at Table 3. The performance differences are marginal, and in some cases, the stutter model performs worse than the base model. This raises concerns about the practical significance of the proposed method. The improvements are not consistent across all datasets, suggesting that the stutter mechanism might not be universally beneficial and may even be detrimental in certain scenarios. A more detailed analysis is needed to understand the conditions under which the stutter mechanism provides a genuine advantage.

2.  **The experimental design is not quite fair**. As stutter models are pretrained 1 billion tokens more than base models, it is unknown whether such fluctuation of performance is due to the continual training, or the inclusion of extra 10% token-retrospect layers. It is required to continual-train the base model for the similar token compute. The additional training introduces a confounding variable, making it difficult to isolate the effect of the stutter mechanism. Without a control where the base model is also trained on the same additional data, it is impossible to determine if the observed performance differences are due to the stutter mechanism or simply the increased training. This lack of a proper control group undermines the validity of the experimental results.

3.  **The details of implementation are missing**. As in Line#252, each token is stutter once, doubling the sequence length of the language model. It lacks discussion about the sequence length of this point. The paper does not specify how the model handles the increased sequence length during the stutter process. This is a critical detail, as doubling the sequence length could have significant implications for memory usage and computational cost. The absence of this discussion makes it difficult to assess the practical feasibility of the proposed method, especially for longer sequences.

4.  **Extra time cost**. The stutter methods require the forward process twice in both training and evaluation process. It is required to report the time and complexity cost versus base models. The paper does not provide a detailed analysis of the computational overhead introduced by the stutter mechanism. Running the forward pass twice will undoubtedly increase the training and inference time. Without a clear understanding of this overhead, it is difficult to evaluate the practical trade-offs between performance gains and increased computational cost.

### Questions
1. How does the stutter handle with the sequence length problem?

2. As the paper mentioned, each token stutters once, and the strategy of stutter token selection is out of the scope of the paper, why stuttering/repeating each token once can work? 

3. How does the stutter methods impact the time complexity in both training and inference?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel method called the "stutter mechanism" that enhances transformer models by selectively applying additional layers to more challenging tokens. This approach mimics a human speaker's stutter, allocating more computational effort where needed, thus improving language capabilities without generating excessive tokens. Experiments with various Pythia models demonstrate that the stutter mechanism consistently enhances performance across benchmark datasets. Specifically, the Pythia-410M model, enhanced by this method, outperforms the larger Pythia-1B model on WinoGrande and WSC. Additionally, the method is data-efficient, requiring less than 1% of the pretraining data for additional training.

### Strengths
1. The motivation is strong, the hypothesis that not all tokens are equally easy to generate and for at least some of them, a transformer can do better by ”giving more thought” to an in-flight token by ”transforming” it with more operations. The stutter mechanism you propose is a creative and novel method to enhance the capabilities of large language models (LLMs) without significantly increasing their size. This addresses a critical need in the field for more efficient and adaptable models.

2. The paper presents a well-structured approach to implementing the stutter mechanism, with clear explanations of the architecture and the token-retrospect map. The mathematical formulations are sound and the integration with existing transformer architectures is well-justified.

3.  The experimental results are compelling, demonstrating significant performance improvements across various benchmarks. The fact that a smaller model (Pythia-410M) can outperform a larger one (Pythia-1B) with the stutter mechanism is particularly noteworthy.

### Weaknesses
1. Comparison with State-of-the-Art LLMs: The paper could be strengthened by comparing the stutter mechanism against other recent methods aimed at improving LLM efficiency or performance. Meanwhile, the used LLMs (Pythia) are limited, LLAMA is the important series of LLMs to conduct the experiments . This would provide a clearer picture of how your approach stands out in the current research landscape.

2. Scalability Analysis: Although the paper mentions the potential for the stutter mechanism to be applied to larger models, an analysis of how the mechanism scales with model size would be valuable. How does the performance and efficiency change as model size increases? Specifically, it would be beneficial to see a breakdown of the computational overhead introduced by the stutter mechanism, including the additional parameters and FLOPs required for the second pass. Furthermore, the paper should discuss whether the benefits of the stutter mechanism diminish or plateau as model size increases, and if there are any architectural modifications needed to maintain its effectiveness in larger models.

3. Long-Term Training Stability: The paper focuses on the training with 1 billion tokens, but it would be beneficial to understand the long-term training dynamics and stability of the stutter mechanism, especially when applied to larger datasets or over more training epochs. It is important to investigate if the token retrospect part of the model converges stably over extended training periods, and whether there is any risk of overfitting or catastrophic forgetting. The paper should also discuss the potential for the stutter mechanism to introduce instability or oscillations in the training process, and how these issues can be mitigated.

### Questions
None.

### Soundness
3

### Presentation
2

### Contribution
3
