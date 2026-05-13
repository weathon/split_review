# LoLCATs: On Low-Rank Linearizing of Large Language Models

- Decision: Accept
- Scores: 8, 6, 8, 5

## Abstract
\noindent Recent works show we can linearize large language models (LLMs)---swapping the quadratic attentions of popular Transformer-based LLMs with subquadratic analogs, such as linear attention---avoiding the expensive pretraining costs.  
However, linearizing LLMs
often significantly degrades model quality, still requires training over billions of tokens, and remains limited to smaller 1.3B to 7B LLMs.
We thus propose Low-rank Linear Conversion via Attention Transfer (\name{}), a simple two-step method that improves LLM linearizing quality with orders of magnitudes less memory and compute. 
We base these steps on two findings.
First, we can replace an LLM's softmax attentions with closely-approximating linear attentions, simply by 
\textit{training} the linear attentions to match their softmax counterparts with an output MSE loss (``\textit{attention transfer}'').
Then, this enables adjusting for approximation errors and recovering LLM quality simply with \textit{low-rank} adaptation (LoRA).
\name{} significantly improves linearizing quality, training efficiency, and scalability. We significantly reduce the linearizing quality gap and produce state-of-the-art subquadratic LLMs from Llama 3 8B and Mistral 7B v0.1, leading to 20+ points of improvement on 5-shot MMLU. Furthermore, \name{} does so with only 0.2\% of past methods' model parameters and 0.4\% of their training tokens.  
Finally, we apply \name{} to create the first linearized 70B and 405B LLMs (50$\times$ larger than prior work).
When compared with prior approaches under the same compute budgets, \name{} significantly improves linearizing quality, closing the gap between linearized and original Llama 3.1 70B and 405B LLMs by 77.8\% and 78.1\% on 5-shot MMLU.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents LoLCATs, a method for converting large language models (LLMs) with quadratic attention complexity into models with linear complexity while maintaining model quality. The key innovation is a two-step approach: (1) attention transfer - training linear attention layers to directly approximate the original softmax attention outputs, and (2) low-rank adaptation (LoRA) fine-tuning to adjust for approximation errors. The authors demonstrate that LoLCATs can effectively linearize models up to 405B parameters with significantly less compute and data compared to previous methods, while better preserving model capabilities.

### Strengths
- I believe this is a good work. The paper presents a novel method for linearizing LLMs that addresses key limitations of existing techniques. By focusing on approximating softmax attention outputs and using low-rank adjustments, the authors offer a fresh perspective on reducing computational complexity without sacrificing model quality.
- The LOLCATS method reduces the amount of training required, both in terms of model parameters updated and training data used. This efficiency makes the method practical for widespread use, especially in environments with limited computational resources.
- Demonstrating the ability to linearize large models up to 405B parameters is a notable achievement. The scalability of the method suggests it can be applied to future, even larger models.  The authors provide extensive experimental results, including comparisons with existing methods on multiple benchmarks. 
- The paper delves into the reasons why previous linear attentions struggled to approximate softmax attention effectively. By identifying issues like attention entropy and layer-wise errors, the authors provide valuable insights that inform their improved architecture.

### Weaknesses
 - The introduction and analysis of the preliminaries are too lengthy, with the core improvements in LOLCATs not appearing until the seventh page, which makes the reading experience somewhat disjointed.
- The experimental results are promising given the training budgets. However, I notice that even though previous works perform significantly worse for more challenging benchmarks (like MMLU in the setting), LOLCAT still considerably underperforms the original models. What will happen when the benchmarks become more challenging? (e.g., complex reasoning).
- While the authors claim improvements in inference efficiency, quantitative metrics such as actual speedup factors, memory utilization during inference, or comparisons of throughput are not extensively reported.

### Questions
- How were the hyperparameters for the attention transfer and low-rank adaptation chosen?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the efficiency and scalability challenges of large language models (LLMs) caused by the quadratic complexity of traditional Transformer models. To overcome these limitations, it introduces LOLCATS (Low-rank Linear Conversion with Attention TranSfer), a novel method that linearizes attention mechanisms to reduce computational and memory demands. LOLCATS uses an “attention transfer” phase to approximate softmax attention efficiently and a low-rank adaptation (LoRA) to correct errors. This approach enables scalable training of LLMs with up to 405B parameters—50 times larger than previous models—while maintaining high performance. Experimental results show LOLCATS outperforms existing methods and opens new avenues for scaling LLMs further.

### Strengths
1. The LOLCATS approach significantly reduces computational and memory costs through a two-step process involving "attention transfer" and low-rank adaptation (LoRA), effectively lowering the complexity of large models. 

2. LOLCATS effectively retains the performance of the original self-attention model. Experimental results show that this method can recover much of the original model's quality after linearization, using only a small portion of the parameters and training data.

3. LOLCATS is the first to successfully apply linearization to large models with 70B and 405B parameters, expanding the applicability of linearization techniques.

### Weaknesses
1. The paper mentions the differences in errors across layers and their impact on model performance, but it does not sufficiently discuss the underlying reasons, such as why lower soft-attention entropy leads to higher errors. Specifically, the paper lacks a detailed analysis of how the approximation quality of attention mechanisms varies across different layers and how this variation affects the overall performance of the linearized model. The relationship between the entropy of the softmax attention and the resulting approximation error when using linear attention is not sufficiently explored, leaving a gap in understanding the method's limitations.

2. There is insufficient explanation for new terms, such as "attention transfer," which may lead to misunderstandings regarding specific implementation details and processes. The paper does not clearly articulate the precise steps involved in the "attention transfer" process, making it difficult to understand how the softmax attention is approximated by the linear attention. This lack of clarity hinders the reproducibility and adoption of the proposed method.

3. The paper does not provide averages, variances, or confidence intervals from multiple experiments, making it difficult for readers to assess whether performance differences in the model are statistically significant and robust. The absence of statistical measures makes it challenging to determine if the reported improvements are consistent across different runs or if they are due to random variations. This lack of statistical rigor undermines the reliability of the experimental results.

4. As indicated in [1], there is a notable difference between Linear Attention and Softmax Attention in retrieval tasks, particularly in "needle-in-a-haystack" scenarios. Therefore, assessing the performance of models on such tasks before and after the application of LoLCAT would provide a more comprehensive validation of the method's effectiveness. The paper does not evaluate the model's ability to handle long-range dependencies, which is a crucial aspect of language models, especially in retrieval tasks where the relevant information might be located far from the query.

### Questions
1. I would like the author to supplement and polish the article based on the weaknesses.

2. The authors mention that LoRA effectively reduces approximation errors. Have they considered conducting a specific error propagation analysis? This is crucial for understanding how low-rank adaptation accumulates errors across different layers in deeper models, as it is vital for controlling cumulative errors.

3. In the LoRA method, the choice of the rank parameter is critical for the model's approximation effectiveness. How have the authors taken into account the impact of low-rank parameters on performance across different layers of the model?

4. Does this approach extend to other variants of Linear Attention, such as Mamba 1/2 and Hgrn 1/2?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a novel method for linearizing large language models (LLMs) to make them more efficient in terms of memory and compute resources. The authors propose a method called Low-rank Linear Conversion via Attention Transfer (LOLCATS), which aims to replace the quadratic attention mechanisms in popular Transformer-based LLMs with subquadratic alternatives, such as linear attention. This approach avoids the expensive pretraining costs associated with traditional LLMs.

### Strengths
- The method is shown to scale to unprecedentedly large models (70B and 405B parameters), which was not possible with previous linearization techniques.
- The method is applied to various models, showing its broad applicability and potential impact on the field of natural language processing.

### Weaknesses
 - There is a lack of an overall summary description of the LOLCATS method. An algorithm description or pseudo code can be added.
- There are some writing errors, such as Line 294: APP.???

### Questions
- Why was the proposed method not validated on a smaller model, such as llama1B?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Authors proposed a new method to approximate the quadratic attention operation to semi-linear ones (with a pre-specified quadratic window). The linearized approximation seems to work with PEFT so the computational burden is partially alleviated when accelerating the computation on large models.

### Strengths
- The Introduction reads well (but unfortunately not the case for the rest)

- An interesting problem to study.

- Provide the code in the Appendix

### Weaknesses
 - The way authour present their methods interleaves many previous works, and thus it's difficult to precisely pinpoint what's their contribution. 

- Some lacking experiments make me uncertain if the claimed effectiveness is true.

- The above two factors combined make me uncertain what's the real efficacy of the method.

- My understanding is that actually there is no new technical thing proposed. Eq 5 is proposed by previous works, and sliding window attention was also proposed in the previous work. And it seems like combining this 2 idea is the only technical contribution. Is that correct? Or do you have other new proposed approximation that I overlooked? 

- In that regard, adding a sliding window to any of the previous linearization techniques should improve the performance, and this has to be validated. If not, there is a need to investigate why synergy only happens here.

- Apologize that I really don't get that's the purpose of Table 1, Figure 3 and Figure 5. What's the main point you want to convey here? 

- For ablation study I only see Table 5. Is there one with your proposed method? Or should I read it as Hedgehog == Eq 5 and your method is nothing butHedgehog + Sliding?  And somehow Hedgehog + sliding ==> 68.78 outperformed your proposed method a lot, which reads weird to me.

- Also don't know why ablation is only done on MMLU, I am interested in seeing RCV-e and PiQA too.

- I don't really see what's the help from the linearization to parameter-efficient finetuning. I still don't understand why PEFT can't work on other methods. In addition, full FT should still outweigh PEFT. I believe authors should also show their method with full parameter tuning to see what's the difference.

### Questions
1. Can authors point out which line of appended code correspond to a. Eq 7?

2. I'd like to confirm the author is doing post-training approximation or training from scratch with this specialized architecture. (It's a bit unclear to me). And for all the baseline methods, are they doing training from scratch or post-training approximation.

3. My understanding is that actually there is no new technical thing proposed. Eq 5 is proposed by previous works, and sliding window attention was also proposed in the previous work. And it seems like combining this 2 idea is the only technical contribution. Is that correct? Or do you have other new proposed approximation that I overlooked? 

3. In that regard, adding a sliding window to any of the previous linearization techniques should improve the performance, and this has to be validated. If not, there is a need to investigate why synergy only happens here.

4. Apologize that I really don't get that's the purpose of Table 1, Figure 3 and Figure 5. What's the main point you want to convey here? 

5. Is there a study of different window size?

6. For ablation study I only see Table 5. Is there one with your proposed method? Or should I read it as Hedgehog == Eq 5 and your method is nothing butHedgehog + Sliding?  And somehow Hedgehog + sliding ==> 68.78 outperformed your proposed method a lot, which reads weird to me.

7. Also don't know why ablation is only done on MMLU, I am interested in seeing RCV-e and PiQA too.

8. I don't really see what's the help from the linearization to parameter-efficient finetuning. I still don't understand why PEFT can't work on other methods. In addition, full FT should still outweigh PEFT. I believe authors should also show their method with full parameter tuning to see what's the difference.

### Soundness
2

### Presentation
2

### Contribution
2
