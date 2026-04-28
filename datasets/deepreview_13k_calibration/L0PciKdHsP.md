# MoIN: Mixture of Introvert Experts to Upcycle an LLM

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 3, 3

## Abstract
The goal of this paper is to improve (upcycle) an existing large language model without the prohibitive requirements of continued pre-training of the full-model. The idea is to split the pre-training data into semantically relevant groups and train an expert on each subset. An expert takes the form of a lightweight adapter added on the top of a frozen base model. During inference, an incoming query is first routed to the most relevant expert which is then loaded onto the base model for the forward pass. Unlike typical Mixture of Experts (MoE) models, the experts in our method do not work with other experts for a single query. Hence, we dub them ``introvert'' experts. Freezing the base model and keeping the experts as lightweight adapters allows extreme parallelism during training and inference. Training of all experts can be done in parallel without any communication channels between them. Similarly, the inference can also be heavily parallelized by distributing experts on different GPUs and routing each request to the GPU containing its relevant expert. We implement a proof-of-concept version of this method and show the validity of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel way to upcycle a pre-trained language model, allowing improvement without the high costs of full model pre-training. The paper utilizes topic models and LoRA adapters to train some independent "introvert" experts to realize more efficient training and inference for the language models.

### Strengths
The paper introduces a novel way to upcycle the language models. The new structure of mixed-of-experts allows for efficient parallel inference and training, which provides a framework that could streamline LLM deployments across multiple devices or settings.

### Weaknesses
The improvement in language model performance is not obvious to me. In particular, Table 2 shows that MoIN-5k does not consistently outperform TinyLlama-2.5T across most downstream tasks, despite both being trained on the same amount of tokens. This suggests that the main contribution of MoIN may currently lie more in reducing training and inference costs through parallelism rather than in enhancing the model's performance on language tasks. The lack of clear performance gains, especially given the architectural complexity introduced by the mixture-of-experts approach, raises questions about the practical utility of the method beyond its potential for parallelization. Furthermore, the paper does not provide a detailed analysis of the computational overhead associated with routing inputs to the appropriate expert, which could negate some of the benefits of parallel inference if not handled efficiently. The absence of a comparative analysis against other methods that aim to reduce training costs, such as knowledge distillation or pruning, further limits the assessment of the proposed method's relative advantages.

### Questions
1. Out of curiosity, if the goal is to enable the language model to learn from data that falls outside the distribution of the original training set, do the authors have insights on how this might be achieved within the current framework? Additionally, would this approach offer advantages over the continual pre-training of the full model?
2. If the aim is to enhance more abstract qualities of the language model, such as helpfulness, does this framework provide any specific advantages over the original model in achieving such improvements?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose an approach called MoIN, aimed at enhancing an existing large language model without the substantial demands of continued full-model pre-training. To achieve this objective, they suggest clustering the training data into semantically related subsets. Subsequently, they train distinct expert models for each subset and direct queries to the most suitable expert using a straightforward nearest-neighbor search technique. The authors have implemented a proof-of-concept version and conducted experiments on selected models to validate their approach.

### Strengths
1. The writing in the paper is clear and accessible, allowing me to easily understand the implementation of the method and the execution of the experiments.

2.  The authors highlight a critical issue within the current MoE framework: since routing varies by token, all experts must reside in GPU memory during both training and inference. This requirement poses challenges for scaling to a large number of experts. I believe this paper could inspire the community to explore alternative strategies for increasing the number of models.

3. The experiments are promising in specific scenarios.

### Weaknesses
My main concern is that the experiments conducted are insufficient to support the main conclusions of the paper. The authors only evaluate a limited number of models and datasets. Including more diverse and realistic datasets and models would strengthen the findings and provide a more comprehensive evaluation of the proposed method.

### Questions
N/A

### Soundness
2

### Presentation
3

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
This paper introduces "mixture of introvert experts" (MoIN) for improving LLMs with LoRa adapterss. First they split the training data into semantically relevant groups using topic modeling then train LoRA adapters respectively on each data subset. At inference time, the model routes queries to the most relevant adapter using nearest neighbor search and use it to answer the problem.

### Strengths
The authors trained and deployed up to ~5000 independent LoRA adapters, exceeding the number of LoRAs used in previous research.
The inclusion of diagrams and tables with qualitative examples enhances the reader's understanding of the approach.

### Weaknesses
Motivation and Method:

1. The paper's efficiency claims primarily stem from the use of LoRA, rather than from any novel contribution of this work.

2. The deployment of thousands of LoRA adapters potentially undermines these efficiency claims, especially in inference stage. A more rigorous analysis comparing the computational requirements of this approach to traditional methods is necessary to substantiate these assertions.

Experimental Design and Results:

3. Building upon TinyLlama-2T instead of training from scratch cannot demonstrate their method's effectiveness across the entire training process.

4. The absence of results for a MoIN-3T model, trained on an equivalent number of tokens as TinyLlama-3T, hinders fair comparison and leaves gaps in understanding the method's scalability.

5. The perplexity comparisons presented in Table 1 are misleading. Achieving lower perplexity on potentially less diverse data subsets doesn't necessarily indicate superior overall learning. The fact that MoIN-5k fails to outperform TinyLlama-3T, which was trained on more diverse data, suggests that the latter may have acquired more comprehensive knowledge.

6. Table 2 reveals that the proposed method doesn't consistently outperform baseline models across various datasets. This inconsistency raises questions about the actual improvements offered by the method and its generalizability.

7. The experiments are confined to a relatively small 1.1B parameter model. Experimental results on more commonly used 7-8B parameter models are expected.

8. The lack of ablation studies makes it challenging to discern the contribution of individual components within the proposed system and how they interact.

### Questions
Same as Weaknesses.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work aims to improve / upcycle existing large language model without the prohibitive requirements of continued pre-training of the full-model. The proposed method split the pre-training data into semantically relevant groups and train an expert (LoRA) on each subset. During inference, the query is routed to the most relevant expert and loaded onto the base model for the forward pass. They claim that this design could empower extreme parallelism without any communication channels between experts.

### Strengths
I could hardly figure out the strengths of this work.

### Weaknesses
1. Although the main experiment keeps the training token the same for comparison, it would still be an unfair comparison, specifically in terms of the number of training parameters. Suppose LoRA has 1% parameters, 5K LoRAs would be 50 times larger than the base model. It would be unfair to compare the performance with the baselines, given that you have much more parameters.
2. The overall performance of perplexity and downstream tasks might not make senese. While the authors treats pretrained model with less perplexity as better models (tinyllama-3T is the best), there is a sharp decrease on its downstream performance compared to tinyllama-2.5T (~1.5%). Given the performance gain that MoIN-5k has compared to tinyllama-2.5T (0.05%), I hope the authors' further explaination on this.
3. The accessments of the proposed method is insufficient. To be specific, (1) Only one model archtecture is tested. With limited training resources, the authors should conduct more experiments on models like GPT2, OPT. (2) The impact of the number of clusters is not clear. There could be an ablation study.
4. There lacks detailed explanations on the novelty of this work, maybe the authors could add comparisons or dicussions with LoRA MoE.

### Questions
The same to weakness.

### Soundness
2

### Presentation
2

### Contribution
1
