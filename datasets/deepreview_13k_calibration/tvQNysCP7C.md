# In-context KV-Cache Eviction for LLMs via Attention-Gate

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 5, 3, 5, 5

## Abstract
The KV-Cache technique has become the standard for the inference of large language models (LLMs).
It caches states of self-attention to avoid recomputation. 
Yet, it is widely criticized that KV-Cache can become a bottleneck of the LLM inference system, especially when confronted with ultra-large models and long-context queries. 
A natural remedy is to discard the KV-Cache for less important tokens, with StreamingLLM~\citep{xiao2024efficientstreaminglanguagemodels} as an example, but the used static eviction strategies cannot flexibly adapt to varying contexts. 
Remedies like H2O~\citep{zhang2024h2o} leverage accumulative attention scores to perform dynamic eviction but suffer from the attention bias issue in capturing contextual information. 
This paper bridges this gap by devising a parameterized KV-Cache eviction mechanism, dubbed as \emph{Attention-Gate}, which accepts the whole context as input and yields eviction flags for each token to realize \emph{in-context} eviction. 
The subsequent self-attention module proceeds according to the flags and only the KV states for the remaining tokens need to be cached. 
The Attention-Gates can vary among different heads and layers and be trivially plugged into pre-trained LLMs, tuned by cost-effective continual pre-training or supervised fine-tuning objectives to acquire what to discard. 
The computational and memory overhead introduced by Attention-Gates is minimal.
Our method is validated across multiple tasks, demonstrating both efficiency and adaptability.
After a highly efficient continual pre-training, it achieves higher average accuracy and evicts more tokens compared to traditional training-free methods. 
In supervised fine-tuning, it not only evicts many tokens but also outperforms LoRA-finetuned LLMs on some datasets, such as RTE, where it improves accuracy by 13.9\% while evicting 62.8\% of tokens, showing that effective eviction of redundant tokens can even enhance performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper aims to reduce the memory overhead of the KV cache in LLM inference. The high-level goal is to ``evict’ ’certain tokens from the attention computation without hurting the model’s accuracy, since their key and value vectors (KV-cache) no longer need to be stored in GPU memory. Differently from previous works that find the evicted tokens through heuristics or attention pattern analysis, this work learns a binary gating function for each attention head that predicts whether a token should be attended to in a context-aware manner. Light training of these gating functions is needed.

Experiments with some tasks suggest that the proposed method can evict a substantial amount of tokens without hurting the model’s accuracy.

### Strengths
- The design choices of the proposed method are clearly motivated.
- Presentation is clear and easy-to-follow

### Weaknesses
 - Questionable choices of the evaluation benchmarks. The paper motivates the importance of KV-cache reduction by stating that “KV-cache can become a bottleneck when dealing with large models and long-context queries.” However, to the best of my knowledge, none of the benchmarks in this paper is “long-context,” nor are the models “large.” Besides, I am not sure benchmarks such as RTE and COPA are the best candidates for properly evaluating these models’ performance, compared to more “up-to-date” choices such as MMLU or BBH.
- Unconventional experimental settings. In the SFT experiment, the paper finetunes the model for each task, which was a common setting for previous-generation models such as BERT. For models such as Llama-2, it is more established to finetune the models with a mixture of a variety of datasets and evaluate the models’ general-purpose capabilities. Therefore, I am not sure whether the conclusions from this experiment would be useful for future research.
- Flawed comparisons and missing baselines. Most of the claimed gains of the proposed method, which requires training, are over zero-shot baselines. A more fair comparison would be to compare to baselines that use the same amount of training as the proposed method. Besides, these two baselines are missing: https://arxiv.org/abs/2308.16137 and https://arxiv.org/abs/2310.01801
- Unjustified claims about efficiency. The paper claims that the proposed method “demonstrate both efficiency and adaptability.” In my opinion, efficiency should be quantified using metrics such as memory overhead, latency, throughput, etc. The paper does not include any of such evaluations in its experiments.
- Limited results that make it unclear whether the proposed method can generalize. With limited selection of the base LLM and evaluation benchmarks, it is unclear whether the proposed method can be useful for models with a different size, architecture (e.g., group-query attention as in Llama-3 and Mistral), and more challenging tasks.
- Potential errors in the training objective: In Eq 1, the purpose of including $\beta$ in Eq 1 is unclear to me since it does have any impact on the gradients. This might be a typo and the paper might have missed a square of the bracket term.

### Questions
None

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a simple parameterized KV-Cache eviction mechanism called Attention-Gate, designed to enhance the efficiency of LLMs inference by selectively discarding KV-Cache states for less important tokens. This approach addresses the limitations of traditional static eviction strategies, like those in StreamingLLM, and the attention bias issues in dynamic methods such as H2O. Attention-Gate operates by generating eviction flags for tokens based on the entire context. Experiments showed the performance could be retained with even high eviction ratio compared to baselines.

### Strengths
- Attention-Gate is technically sound and easy to implement. The experiment showed its performance in both continued pre-training and lightweight fine-tuning settings with clear visualization of Attention Maps.
- Ablation studies are thoroughly conducted on the impact of the number/dimension of AG heads and the structure choice of AG.

### Weaknesses
 - The baselines like Local, StreamingLLM, and H2O are weak. As the motivation of Attention-Gate mechanism is to address the attention bias issue, some follow-up works like NACL and A2SF with the same motivation should be included as the baselines to fully show the effectiveness of AG.
- The additional training phase in Attention-Gate may influence the performance of the original LLama2-7B model, so the performance of LLama2-7B with continued training without AG mechanism should be reported.

### Questions
- Experiments are conducted on datasets with short input. In practice, the memory issue caused by the KV-Cache is severe in long-text evaluation settings. I would like to see the results reported on Longbench or Infinitebench datasets. This will make the AG more practical and widely adopted.
- I'm confused about the definition of Equation (1): The $\beta$ is task/layer-wise or not? As the authors illustrated in Figure (1), the eviction patterns changed across tasks and layers.

### Soundness
3

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
5

### Summary
The paper introduces "Attention-Gate", a parameterized mechanism for KV-Cache eviction in large language models (LLMs). Unlike traditional static or local dynamic eviction methods, Attention-Gate uses contextual inputs to decide which tokens to discard adaptively. Experimental results on continual pre-training and supervised fine-tuning scenarios suggest that the proposed method can achieve better performance than traditional approaches.

### Strengths
1. Compared to traditional static or local dynamic eviction methods, Attention-Gate offers a flexible and adaptive approach to KV-Cache eviction in LLMs, enhancing cache management by adjusting to contextual needs.
2. Attention-Gate opts for the attention-like structure to collect contextual information, which can vary among attention heads/layers and be seamlessly plugged into pre-trained LLMs.

### Weaknesses
1. Limited architectural detail: The paper lacks a thorough explanation of the detailed design of Attention-Gate, particularly regarding its network architecture and computation equations. The description of the attention-like structure is insufficient, making it difficult to understand how contextual information is processed and integrated. Specifically, the paper does not clarify the dimensions of the input and output tensors at each stage of the Attention-Gate, nor does it specify the number of heads used or the size of the hidden layers, which are crucial for reproducibility and understanding.
2. Insufficient experimental analysis: The experiments would benefit from more comprehensive analysis to better illustrate the efficiency and effectiveness of Attention-Gate, providing a clearer understanding of its practical impact and performance in different scenarios. The paper lacks a detailed analysis of the computational overhead introduced by the Attention-Gate module, especially concerning the increase in FLOPs and latency during inference. Furthermore, the evaluation is limited by the lack of comparison with other learnable eviction methods, and the analysis of eviction ratio variability is not sufficiently explored, with only a single 50% eviction ratio reported. The absence of long sequence evaluations further limits the assessment of the method's applicability in real-world scenarios.

### Questions
For the method, the following should be addressed.
1. Currently, it lacks an explanation of the attention-like structure of Attention-Gate, including the network design and computation flow. 
2. The only computation equation listed in the paper (Equation 1) is unclear and appears incorrect. 
* The definition and computation of $\bar{AG}_l$ are not explained.
* The necessity of introducing an additional threshold $\beta$ is unclear; its role seems to overlap with the probability threshold $\tau$.
* The direct subtraction of $\beta$ seems ineffective for preventing over-aggressive token eviction; an activation or truncation function may be missing.

More experimental analysis can be added.
1. Inference efficiency: including Attention-Gate before each MHA layer adds computational overhead. To assess inference efficiency, a comparison of the computation burden (in FLOPs) between the proposed method and traditional approaches is essential.
2. Comparative evaluation: as the paper mentions other learnable eviction methods like NACL and A2SF, their performance should be included for a more comprehensive comparison of effectiveness.
3. Eviction ratio variability: only a 50% eviction ratio is reported; assessing model performance across varying eviction ratios would provide a more comprehensive analysis.
4. Long sequence analysis: given that KV-cache eviction is critical for long sequences, it would be beneficial to include evaluation tasks involving longer sequences.

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
4

### Summary
This paper is concerned about KV cache compression, especially KV cache eviction. This paper claims that previous parameter-free eviction strategies either can not adapt to the context or can only adapt to the biased context. To remedy this, this paper proposes a parameterized eviction strategy, which learns to evict KV cache at prefilling stage with a trainable module termed Attention-Gate. Experimental results on both continued pretraining and supervised finetuning demonstrate that, with similar eviction proportions, Attention-Gate can achieve better performance in comparison to existing eviction baselines such as StreamingLLM and H2O. Particularly, Attention-Gate combined with LoRA can even realize better performance than LoRA itself. Further ablations indicate that the design choices of Attention-Gate is adequate.

### Strengths
- As far as I know, this paper is the first one that introduces parameterized module to achieve KV cache eviction. Previous studies usually rely on parameter-free heuristics.
- This paper is probably one of the first that achieves dynamic KV cache eviction at both layer-level and head-level. Previous studies belong to either layer-level dynamic KV cache eviction (e.g., PyramidKV) or head-level one (e.g., AdaKV).
- The design choices of Attention-Gate are thoroughly elaborated and sufficiently motivated.
- Experimental results show that Attention-Gate outperforms typical baselines with a similar KV cache budget.

### Weaknesses
 - This paper claims previous studies that can adapt to the given context (e.g., H2O) are largely biased and uses this as a core motivation of a parameterized KV cache eviction strategy (i.e., Attention-Gate). However, there is no clear evidence showcasing that Attention-Gate is not biased. Particularly, from Figure 1, we can see that there are still attention sinks in quite a few heads.
- The proposed strategy in this paper is limited to prefilling stage. There are indeed studies who are also limited to prefilling stage. However, it would be better to consider decoding stage especially in cases where the input prompt is comparably short and the output is long.
- The use of straight-through estimator is not very clear. I recommend more details on this.
- Though it is very nice to see that Attention-Gate combined with LoRA outperforms LoRA, it is not very clear why this would happen. And it is actually very interesting to uncover the reason why eviction can even lead to better results. Perhaps eviction can also serve as a sort of regularization?
- Frustratingly, while KV cache eviction is targeted at improving memory efficiency and potentially latency efficiency, this paper lacks an in-depth comparison on efficiency. And this would predominately affect the contribution and impact of this paper. The eviction ratio for memory and the FLOPs for latency are both theoretical measures, and do not provide a clear picture of practical performance.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a dynamic KV-Cache eviction mechanism called Attention-Gate (AG) for large language models. AG selectively evicts less important tokens based on attention scores, unlike static strategies. Positioned before attention layers, AG can be seamlessly integrated into pre-trained LLMs. The method is validated on various tasks, demonstrating improved efficiency compared to static eviction strategies like StreamingLLM and H2O, with benefits for long-context queries.

### Strengths
1. The authors' method is structurally simple yet highly effective, offering more flexibility and better performance compared to previous eviction strategies. It incorporates global information and demonstrates significant improvements in performance.
2. This approach avoids the redundant attention computations seen in prior methods, enabling a more thorough and efficient eviction of tokens.
3. This method requires only a few thousand samples for post-training or fine-tuning to be effective, making it easily applicable to a wide range of existing pre-trained models.
4. The authors provide a detailed analysis of attention behavior across different layers, explaining the effectiveness of their approach and illustrating its specific impact across various cases.

### Weaknesses
1. There is no detailed analysis of the data sources used for post-training if other pre-training data besides RedPajama is chosen. There is also no examination of how the amount of post-training data impacts the final results.
2. The method is only effective on Llama-2 and does not show improvement on Mistral-7B, but the paper lacks a detailed analysis of why this is the case. Additionally, there are no experiments on models of other scales besides 7B.
3. The paper lacks analysis on the inference efficiency improvement after eviction, as well as the additional time overhead introduced by the attention-gate computation compared to the original Transformer.
4. It would be helpful to detail the similarities and differences between MoD (https://arxiv.org/abs/2404.02258), which also uses a gate mechanism based on Softmax to select tokens for computation.
5. Most of the evaluation tasks are short-form, few-shot tasks, and there is a lack of comprehensive evaluation tasks that test various LLM capabilities (e.g., MMLU). Additionally, the inclusion of long-form datasets could provide more robust results.
6. There are several hyperparameters involved in AG, but there is no analysis of how these hyperparameters were selected or their impact on performance.
7. Appendices A.2 and A.3 are missing content.

### Questions
Please refer to the Weakness.

### Soundness
3

### Presentation
3

### Contribution
3
