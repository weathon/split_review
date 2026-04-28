# Jamba: Hybrid Transformer-Mamba Language Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
We present Jamba, a novel hybrid Transformer-Mamba mixture-of-experts (MoE) architecture. Jamba interleaves blocks of Transformer and Mamba layers, enjoying the benefits of both model families. MoE is added in some of these layers to increase model capacity while keeping active parameter usage manageable. This flexible architecture allows resource- and objective-specific configurations. We implement two configurations: Jamba-1.5-Large, with 94B active parameters, and Jamba-1.5-mini, with 12B active parameters. Built at large scale, Jamba models provide high throughput and small memory footprint compared to vanilla Transformers, especially at long-context tasks, with an effective context length of 256K tokens, the largest amongst open-weight models. At the same time, they are also competitive on standard language modeling and chatbot benchmarks. We study various architectural decisions, such as how to combine Transformer and Mamba layers, and how to mix experts, and show that some of them are crucial in large scale modeling. To support cost-effective inference, we introduce ExpertsInt8, a novel quantization technique that allows fitting Jamba-1.5-Large on a machine with 8 80GB GPUs when processing 256K-token contexts without loss of quality. We also describe several interesting properties of this architecture that the training and evaluation of Jamba have revealed. The model weights are publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Jamba, a hybrid language model combining Transformer, Mamba, and Mixture-of-Experts (MoE) layers to enhance memory efficiency, throughput, and long-context handling, supporting up to 256K tokens. With ExpertsInt8 quantization, Jamba achieves scalable, cost-effective deployment on 8-GPU setups. Experimental results demonstrate competitive performance across benchmarks in language modeling, chatbot, and multilingual tasks, highlighting its adaptability to various hardware and resource constraints.

### Strengths
1.Hybrid Architecture with Enhanced Flexibility : Jamba’s combination of Transformer layers, Mamba layers, and Mixture-of-Experts (MoE) modules offers a unique balance of efficiency and performance, addressing the limitations of each component individually. This hybrid design allows for configurable trade-offs between memory usage, throughput, and model capacity, making Jamba adaptable to diverse hardware configurations.

2. Long-Context Capabilities: Jamba supports an effective context length of 256K tokens, one of the longest among open-weight models. This is particularly advantageous for long-context tasks, as demonstrated in benchmarks like RULER and ∞BENCH, where Jamba-1.5 models perform competitively, underscoring their suitability for tasks requiring extensive memory.

3. Cost-Effective Inference via ExpertsInt8 Quantization
The introduction of ExpertsInt8 quantization allows Jamba-1.5-Large to fit on hardware with 8 80GB GPUs without compromising quality, even for long-context processing. This quantization technique shows latency advantages on A100 GPUs, where FP8 isn’t available, thereby providing a cost-efficient alternative to traditional approaches.

4.Competitive Performance Across Benchmarks
Jamba models perform comparably to state-of-the-art models on standard language modeling, chatbot evaluations, and multilingual benchmarks. This includes maintaining high throughput and latency efficiency, particularly at large context lengths, further demonstrating the model’s real-world applicability.

### Weaknesses
 1. Minimal Discussion of MoE and Mamba Layer Interaction : While the hybrid design leverages both MoE and Mamba layers, the paper provides limited analysis of how these components interact to optimize performance. An in-depth exploration of how each component contributes to throughput, especially in long-context scenarios, would clarify the architectural benefits and limitations. Specifically, the paper lacks a detailed breakdown of the computational overhead introduced by the MoE layers, and how this overhead scales with increasing context length. It is unclear if the benefits of MoE are consistent across different context lengths, or if there are specific thresholds where the overhead outweighs the gains. Furthermore, the interaction between Mamba's selective state space model and the MoE layers is not well-defined, leaving questions about how these two mechanisms cooperate to handle long-range dependencies efficiently. It would be beneficial to see a more granular analysis of the activation patterns and information flow between these layers.

 2. Sparse Performance Analysis on Edge and CPU: Although Jamba is designed to balance memory and compute efficiency, its performance on edge devices and CPUs is not evaluated. Given the trend toward deploying models in low-resource environments, this data would offer practical insights into the model’s viability beyond high-end GPU setups. The paper does not discuss the potential challenges of deploying the model on devices with limited memory and compute capabilities, such as quantization effects, or the impact of custom Mamba kernels on CPU performance. A more thorough investigation into the model's performance on these platforms would be valuable for a comprehensive understanding of its applicability.

### Questions
In Section 3.2, the authors mention that “Jamba leverages a balanced mix of Transformer, Mamba, and Mixture-of-Experts (MoE) layers to optimize both throughput and model capacity, particularly in long-context scenarios.” It would be helpful if the authors could provide further insights into how the specific ratio of these layers was determined. An ablation study examining the impact of varying the number or sequence of each layer type (Transformer, Mamba, MoE) on key performance metrics such as latency, memory usage, and accuracy would lend greater clarity to the efficacy of this particular configuration and substantiate its contribution to Jamba’s overall efficiency.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Jamba-1.5-{Large, Mini} models based on a novel hybrid of Transformer, Mamba, and MoE architectures. Combining the architectural design and the novel ExpertsInt8 quantization technique, the models are efficient in serving in terms of latency, throughput, and memory footprint. Evaluations on long-context benchmarks demonstrate that the model has strong performance in its effective 256K context length. Academic and chat benchmark evaluations indicate that Jamba-1.5 models perform similarly to SOTA public models.

### Strengths
1. Serving the proposed Jamba architecture is efficient in terms of low latency, high throughput, and reduced memory footprint, especially in longer context length. 
2. The paper shares some insights found in the pre-training process, which can be beneficial to the community.
3. The performance of Jamba-1.5 models is close to other public models of similar activated parameters.

### Weaknesses
1. The details of model training are not revealed, including data source, data mixture ratio, number of tokens trained, context length, and post-training techniques. This makes the training process unclear and not reproducible. The lack of transparency around the pre-training data and methodology makes it difficult to assess the generalizability of the model and compare it fairly with other models trained on different datasets. For example, the specific data mixture ratios could significantly impact the model's performance on different downstream tasks, and without this information, it's hard to understand the model's strengths and weaknesses.

2.  A direct comparison between Jamba, Llama, and Mistral is insufficient to demonstrate the effectiveness of the proposed Jamba architecture.
	- The training of Jamba, Llama, and Mistral models are different in data, model size, and computation, making it difficult to attribute the evaluation results. A comparison between architectures (like Jamba, Mamba, and Attention; with and without MoE) under the same pre/mid/post-training condition (like with the same data and same computation or number of tokens) can better reveal the effectiveness. The current comparisons are confounded by these differences, making it unclear whether the observed performance differences are due to the architecture itself or other factors such as data or training regime. For example, if Jamba was trained on a larger dataset or with a different data mixture, it would be difficult to isolate the impact of the architectural changes.
	- Although Appendix B provides some ablation studies in architecture, the training computation, model size, and reported evaluation datasets are rather limited, and evaluation after mid/post-training is not included. This is insufficient to demonstrate the architectural effectiveness at scale and in comprehensive downstream tasks. The ablation studies, while helpful, do not cover the full range of model sizes and training regimes that would be necessary to fully understand the scaling properties of the Jamba architecture. Furthermore, the lack of post-training evaluation limits the conclusions that can be drawn about the architecture's suitability for real-world applications.

3. It would be better to demonstrate the scaling ability of the Jamba architecture. For instance, the relationship of LM loss/downstream task performance wrt. training computation. Without this, it is difficult to assess the potential of the architecture for larger-scale models and whether it can continue to improve with more compute.

### Questions
- Is it possible to provide details on training procedures? (e.g., pre-training: data source, number of tokens, training throughput, training time, training context length, training batch size; post-training: strategies used and tokens trained)
- Is it possible to provide experimental results of comparison concerning the Jamba/Mamba/Attention/MoE architectures under the same training setting at scale (like more tokens and larger model size) and for more comprehensive tasks (like all tasks in Section 7)?

### Soundness
2

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
4

### Summary
This paper presents Jamba, a hybrid MoE model with interleaved Attention and Mamba layers. They open-source Jamba-1.5-Large (94B active parameters) and Jamba-1.5-Mini (12B active parameters). The authors conduct extensive experiments on various design choices, including different ways to interleave attention and Mamba layers and mix experts. Jamba demonstrates strong results and inference efficiency on long-context tasks, and is competitive on standard language tasks (e.g., MMLU). They introduce ExpertsInt8 to save time and memory of model loading for MoE models.

### Strengths
1)	The proposed model, Jamba, is open sourced for research use.
2)	Jamba achieves strong results on long-context tasks, while offering better inference efficiency on throughput and memory footprint.
3)	The authors provide detailed ablations and insights on different ways of combining attention and Mamba layers, including the ratio of attention and Mamba layers, using Mamba-1 or Mamba-2 layers.

### Weaknesses
Lack of a fair comparison on the effectiveness of Jamba against the other hybrid attention-SSM architectures. Although Jamba achieved promising results, the paper lacks a comparison with other hybrid attention-SSM models, such as YOCO [1] and Samba [2], using the same training data and parameter scale, particularly on the long-context and standard language tasks (e.g., MMLU).



### Questions
Add more comparsion against the other hybrid attention-SSM models under a fair setting.

### Soundness
3

### Presentation
3

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
The paper introduces a model family of Transformer-Mamba models, augmented with Mixture of Expert (MoE) layers. Due to the Mamba and MoE components, the model has throughput and memory benefits on long context tasks. The authors describe a quantization method for the MoE layers which further enhances the inference performance. Finally, the authors describe some evaluations for long context, chat, and natural language benchmarks.

### Strengths
- The paper proposes a large-scale Hybrid of Mamba, Transformers, and MoE layers. The large-scale aspect of it with respect to model size is certainly novel.
- Although quantizing the Expert layers on MoE models has been explored before [1] [2] the quantization on Int8 is novel and interesting.

[1] https://neurips2023-enlsp.github.io/papers/paper_81.pdf 

[2] https://arxiv.org/abs/2406.08155

### Weaknesses
Unfortunately there are many key aspects missing from all the sections of the paper which makes it hard to quantify if the proposed approach is better than the state of the art in an apples to apples setup, or for future reproductions and/or comparisons. The most important weakness is the lack of disclosing the pre-training size (or FLOPs budget in general), which is known to be indicative of scaling trends and allows for comparing models in an standardised way [5]. While I believe the proposed protocol is novel and interesting enough, I think the following weaknesses should be addressed so that this paper is useful for the ICLR community.

**Efficient Inference details**

- Section 4.1 and 5 focus on the latency aspects of the proposed quantization method, but there is no empirical evidence to quantify the loss in model performance (if any). It is crucial to demonstrate that the quantization method does not degrade the model's accuracy on downstream tasks, especially on complex benchmarks like NarrativeQA, where quantization can often introduce significant performance drops. The absence of these results makes it difficult to assess the practical utility of the proposed quantization technique.
- Figure 2 from section 4.1 seems focused on latency and missing throughput, which is an important consideration to compare to the other approaches. Throughput is a critical metric for evaluating the efficiency of inference, especially in real-world applications. Without throughput data, it's hard to understand the overall performance benefits of the proposed method compared to alternatives.
- Relevant very similar work in MoE quantization on the experts [2] is missing from section 4.1, there should be at least a discussion, at best a latency comparison. The lack of discussion of closely related work, particularly on MoE quantization, is a significant oversight. A comparison with existing methods is essential to establish the novelty and advantages of the proposed approach.
- Section 5 lacks important details of what software stack was used to run the latency and throughput comparisons. It is not possible to assess to what degree the comparison is fair, or if it paints a good or bad picture for the proposed method. Concretely: what quantization is used in the baseline models if at all? What’s the software stack used for running these comparisons? The absence of these details makes it impossible to reproduce the results and evaluate the fairness of the comparisons. The specific versions of libraries and hardware used are crucial for ensuring reproducibility.

**Pre-training details**

- There are no meaningful details about the composition of the pre-training dataset or the ablations conducted, which makes it hard for future work to compare to this model (e.g. was Jamba trained strongly on X or Y language, or domain). The absence of details about the pre-training dataset makes it difficult to assess the model's generalization capabilities and compare it with other models trained on different datasets. The specific mix of data sources and their proportions are essential for understanding the model's biases and strengths.
- There is no indication on section 6 or the rest of the paper about either the pre-training dataset size, or the amount of tokens the model saw during pre-training. Without this information, it is simply not possible to understand if the proposed model outperforms in a FLOPs apples-to-apples comparison with other models. This makes it hard for future work to make a call of whether or not it is worth it to implement the Jamba architecture with a given FLOPs budget — which is a tradeoff often times researchers in Academia and Industry must think about.
- MoE models are known to be finicky to pre-train [3], there’s no details about the MoE pre-training protocol. Such as for example, routing loss function and/or hyperparameters. Broadly speaking, there’s no discussion about pre-training hyperparameters at all, which makes it hard to reproduce Jamba in the future, or to run sensible comparable ablations. The lack of details on the MoE training protocol, including the routing loss function and hyperparameters, is a significant omission. These details are crucial for reproducing the model and understanding its training dynamics.
- There’s no information about the tokenizer training either: the mixture of corpus size used, or software stack which is known to matter in practice [4]. The tokenizer training process is a critical aspect of language model development. The absence of details about the training corpus and software stack makes it difficult to reproduce the tokenizer and understand its impact on the model's performance.
- There is no mention at all about the pre-training effective throughput and FLOPs per step. This makes it hard for future work and practitioners to decide whether the proposed approach scales once the model performance is viewed as a function of FLOPs and wall-clock time. The absence of effective throughput and FLOPs per step during pre-training makes it difficult to assess the efficiency of the training process and compare it with other models.
- [1] is a very close recent work but is not discussed or ablated throughout the paper.

**Post-training details**

- There are no details at all about what algorithm was used during Post-training and what are their hyper-parameters and compute budget, which makes it hard to reproduce and to compare to other models. The lack of details on the post-training algorithm, hyperparameters, and compute budget makes it difficult to reproduce the model and compare it with other fine-tuned models.
- There’s a small mention of synthetic data, but there are no details about what model was used to bootstrap the synthetic data, the size, and under what protocol. This makes it hard to assess to what degree this model can be a distillation of other models. The absence of details about the synthetic data generation process, including the model used, the size of the dataset, and the generation protocol, makes it difficult to assess the impact of this data on the model's performance.

**Evaluation**

- Section 7 has this statement “We mainly compare with recent open-weight models of the same size range” . This is problematic because the delta in performance is dictated by both model size **and** data budget [5]. Since the full compute budget is not disclosed, it’s hard to draw conclusions that can inform future research ideas and questions (Eg is the Jamba architecture better than transformers for a given compute budget). The comparison based on model size alone is insufficient, as performance is also heavily influenced by the data budget. Without disclosing the compute budget, it's impossible to determine if the proposed architecture is superior for a given computational cost.
- There are no details about the inference used to compute the self-reported numbers in table 4. This is important since some models/tasks are sensible to the use of different floating point precisions and quantization schemes. This is also important to guarantee a fair comparison. The absence of details about the inference setup, including floating-point precision and quantization, makes it difficult to assess the fairness of the comparison.
- A seemingly arbitrary set of (model, tasks) are self-reported, whereas others are drawn from previous papers (without citation) or from the Huggingface OpenLLM Leaderboard. It is not clear why this is the case, which makes it harder for future work to reference this table or to compare to it. The lack of a clear rationale for selecting specific models and tasks for self-reporting makes it difficult to interpret the results and compare them with other studies. The absence of citations for results taken from previous papers also hinders reproducibility.
- Since some numbers are self-reported and for the rest there’s no citation of where they come from (except for the leaderboard) it is not clear at all if this is a fair comparison under the same setup: prompts, split sets, same shot number. While this is a very challenging area of the LLM literature, there should be at least an explanation of the setup used to evaluate Jamba so that future work is somewhat comparable. The lack of a clear description of the evaluation setup, including prompts, split sets, and shot numbers, makes it difficult to ensure a fair comparison with other models. The absence of these details hinders reproducibility and makes it challenging to interpret the results.
- The claim on Figure 5 seems overreaching, since Jamba 1.5-large is both larger in total and active parameters than llama 3.1 70b, and is well above taking into account error bars, so is not either of a similar size (the other models are smaller) or having competitive performance.

**Typos**

- quantization technique that **allows**
- Section 7.1.1: The results for key **proprietary**

### Questions
- Is there a regression downstream performance when using ExpertsInt8 Quantization?
- Why adding Gemma on Table 3 if it does not support the context window for this task?
- Section 7.2 begins with “While not our main focus” — what’s the main focus? This seems important to contextualize to what degree this model is applicable for future work.
- What is the rationale to self-report some metrics and models in table 4?
- What does strict/flexible mean in table 4?
- Why are jamba models having higher error bars than the other models in figure 5?
- There's a couple of ablations in the appendix comparing Jamba to vanilla transformers (with and without MoE) but it lacks the details to assess if it was a fair comparison. For example, a transformer and mamba models are notably different architectures, are the optimization parameters tuned for each model in figure 6 and 7? (Learning rate, scheduler, beta values if Adam, etc). Also, are the two models parameter count equivalent? If so, how is this compensated?

### Soundness
2

### Presentation
2

### Contribution
3
