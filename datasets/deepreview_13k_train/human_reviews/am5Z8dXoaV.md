# LazyLLM: DYNAMIC TOKEN PRUNING FOR EFFICIENT LONG CONTEXT LLM INFERENCE

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
The inference of transformer-based large language models consists of two sequential stages: 1) a \prefilling stage to compute the KV cache of prompts and generate the first token, and 2) a \decoding stage to generate subsequent tokens.
For long prompts, the KV cache must be computed for all tokens during the \prefilling stage, which can significantly increase the time needed to generate the first token. Consequently, the \prefilling stage may become a bottleneck in the generation process. An open question remains whether all prompt tokens are essential for generating the first token. To answer this, we introduce a novel method, \methodname, that selectively computes the KV for tokens important for the next token prediction in both the \prefilling and \decoding stages. Contrary to static pruning approaches that prune the prompt at once, \methodname allows language models to dynamically select different subsets of tokens from the context in different generation steps, even though they might be pruned in previous steps. Extensive experiments on standard datasets across various tasks demonstrate that \methodname is a generic method that can be seamlessly integrated with existing language models to significantly accelerate the generation \textbf{without fine-tuning}. For instance, in the multi-document question-answering task, \methodname accelerates the \prefilling stage of the LLama 2 7B model by $2.34\times$ while maintaining accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, authors propose to selectively calculate KV cache instead of computing KV cache of all tokens. Unlike static pruning one in prior work, this work provide dynamic pruning of tokens in different generation steps..

### Strengths
* Evaluated the proposed method in diverse task.

### Weaknesses
 * Problem seems not very general and universal to all context. Authors should be clear about when TTFT becomes x21 compared to decoding. In a large scale system, decoding and prefilling is happening in a different server so it is not a big problem. Also prefilling usually computes more token than decoding so if we normalize the latency by number of tokens, we can’t say it is completely doing wrong although optimizing it helps anyway. 
* Figures are confusing especially fig 4. 
* Methods are compared to Token drop, static token prune, prompt compression but standard technique to reduce TTFT is using parallel computation. Paper lacks comparing the method with those method. [2] These method does not lose any accuracy and effectively accelerate TTFT.
* I feel like caching hidden states of pruned tokens in AuxCache is similar to prior work LESS [1]. how is AuxCache different from the prior work?
* In tab 2, code completion computes more tokens in llama2 (68.57%) compared to single-document QA (87.31%) but speedup is marginal (x1.01) compared to single-doc QA(x1.34). Why is it so? is the saving not linear?

### Questions
* I feel like caching hidden states of pruned tokens in AuxCache is similar to prior work LESS [1]. how is AuxCache different from the prior work?
* In tab 2, code completion computes more tokens in llama2 (68.57%) compared to single-document QA (87.31%) but speedup is marginal (x1.01) compared to single-doc QA(x1.34). Why is it so? is the saving not linear?

[1] https://arxiv.org/pdf/2402.09398v2

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the inference latency at the prefilling stage of long-context LLM inference. 

The authors propose LazyLLM, a training-free method that enables dynamic token pruning across transformer layers and at different decoding steps. 

Through experiments on various long-context inference datasets, they demonstrate that LazyLLM significantly reduces inference time while maintaining performance levels comparable to baseline models.

### Strengths
* **Sharp focus on dynamic token pruning for the prefilling stage**.
This paper proposes an innovative approach to tackle the TTFT problem by shifting part of the prompt token computation to the decoding stage. The dynamic token pruning at different decoding steps allows for the selective retention of previously pruned but relevant tokens.

* **Effective and flexible layer-wise pruning strategy**.
The progressive token pruning from earlier to later layers is well-justified, offering a flexible approach to managing the trade-offs between efficiency and performance.

* **Comprehensive analysis and convincing results**.
The experiments span multiple datasets and models, providing a convincing case for LazyLLM’s efficiency. The ablation study on token drop rates and locations offers insights into the performance-speedup trade-offs and memory and computation needs.

### Weaknesses
 * **Limited detail on hyperparameter settings and implementation strategies**.
The approach introduces numerous hyperparameters, particularly with progressive token pruning and token revival, which could impact implementation. Providing additional details on the decision-making process for these hyperparameters would enhance transparency and offer insights into LazyLLM’s effectiveness and generalizability.
    - Top-$k$ percentile selection strategy: Unless I missed something, it appears that different values of $k^l$ are set at the corresponding layer $l$. Clarifying how these values were determined and their generalizability across different tasks and decoding steps would be beneficial. The lack of a clear, principled method for setting these layer-specific $k$ values raises concerns about the robustness of the approach, especially across diverse datasets and model architectures. A more detailed explanation of the search space and the sensitivity of performance to these parameters is needed.
    - For reviving tokens, the authors skip the KV updating of tokens before and after the revived tokens, instead appending the revived tokens to simplify KV computation. This strategy, however, breaks the sequential dependency of tokens, potentially affecting performance due to misalignment with training data. An extended discussion on the effect and trade-offs behind this implementation could be beneficial and provide insights into the role of token orders in inference speed and performance. The authors should investigate the potential impact of this approximation on the model's ability to capture long-range dependencies and contextual nuances.

* **Lack of discussion of the potential bias enhanced by attention-based pruning**.
Selecting tokens to prune based on attention scores could inadvertently amplify inherent biases in LLMs, particularly when uncertainty is high.
    - Pruning a fixed number of tokens according to attention scores can lead to unintentional bias, as high-entropy distributions may cause equally significant tokens to be pruned due to marginal differences in scores. This issue could be exacerbated in challenging tasks, where hyperparameter sensitivity may impact LazyLLM’s reliability. The authors should explore the potential for this pruning strategy to disproportionately remove tokens associated with minority or underrepresented groups, leading to biased outputs.
    - Previous works (Li et al. 2023) suggest that the attention mechanism in transformers may focus on different tokens across layers. LazyLLM’s early pruning might inadvertently exclude tokens relevant at later stages. Exploring this potential limitation would strengthen the analysis and illuminate LazyLLM’s effectiveness across diverse text generation tasks. The paper should include an analysis of how the pruning decisions at early layers affect the model's ability to attend to relevant information in subsequent layers, especially for long-context inputs.

* **Possible memory overhead from the Aux Cache during decoding**.
The authors propose Aux Cache to store the hidden states of pruned tokens for efficient future KV computation. However, this can pose challenges to further reducing the memory footprint in the subsequent decoding stage. Given the utilization of the attention mechanism of LazyLLM in common with existing works on optimizing KV cache (Xiao et al. 2024; Liu et al. 2023, Zhang et al. 2023), perhaps the authors could further discuss how we can optimize the Aux cache for long context inference in general.

### Questions
* Regarding the progressive token pruning by attention-based top-k percentile selection, could the authors consider measures to prevent the unintentional removal of tokens that might prove essential in later layers? Accumulating attention scores across multiple layers could potentially address inconsistencies in token selection. Would such an approach be integrated in LazyLLM and mitigate issues associated with layer-wise pruning?

* How many previously evicted tokens can be revived in later decoding steps, and does this impact the semantic structure of the input sequence? Understanding the limitations on reviving tokens would help clarify whether token revival affects the semantic coherence of the sequence.

* Does the Aux Cache and subsequent KV computation for revived tokens introduce memory or latency overhead during decoding?
Would it be possible to apply additional pruning or compression techniques at decoding time to further optimize inference speed with LazyLLM?

### Soundness
3

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
5

### Summary
The paper introduces LazyLLM, a dynamic token pruning technique designed to improve the efficiency of large language model (LLM) inference, particularly in long-context scenarios. LazyLLM selectively computes key-value (KV) pairs for tokens that are crucial for the prediction of the next token, thereby deferring the computation of less important tokens to later stages. Unlike static pruning, LazyLLM dynamically selects subsets of tokens at each generation step, allowing it to maintain accuracy while achieving speed improvements.

This approach requires no additional training and can be integrated with existing transformer-based models seamlessly. Experimental results demonstrate that LazyLLM significantly accelerates the inference process, especially in the initial token generation phase (prefilling). For instance, in multi-document question-answering tasks on the LLaMA 2 7B model, LazyLLM achieves a 2.34x speedup during prefilling with minimal accuracy loss

### Strengths
A key strength of LazyLLM lies in its dynamic, training-free approach to token pruning, which allows it to be easily integrated into existing transformer-based LLMs without requiring model fine-tuning or architectural changes. By selectively computing only the most important tokens for each generation step, LazyLLM not only optimizes the time-to-first-token (TTFT) but also reduces the overall computation during inference. This results in significant speedups across various tasks and model configurations while maintaining accuracy. Furthermore, the method’s adaptive token selection and use of an auxiliary cache (Aux Cache) enable the model to “revive” previously pruned tokens when needed, ensuring that efficiency gains do not come at the cost of degraded model performance.

### Weaknesses
1.	**Additional GPU memory usage for Aux Cache**: If the Aux Cache is retained on the GPU, it will increase GPU memory consumption. As a result, the actual GPU memory footprint of LazyLLM should account for both the retained KV cache and the Aux Cache. This design might limit LazyLLM’s applicability in scenarios with high memory demands.

2.	**Alignment of GPU memory costs in experiments**: It is crucial to clarify whether the GPU memory usage for each method was fairly aligned in the experiments, especially if LazyLLM’s actual GPU memory footprint surpasses that of the baseline methods. Any advantages in speed and efficiency for LazyLLM need to be re-evaluated under fair memory cost comparisons to ensure experimental fairness.

3.	**Lack of comparisons with more advanced baselines**: The paper does not compare LazyLLM with recent efficient cache management methods, such as H2O[1] and SnapKV[2]. These methods offer innovations in areas like KV cache reduction strategies and generation speed optimization. Comparing LazyLLM with them would more comprehensively illustrate its performance strengths and limitations.

### Questions
Please check the weaknesses section.

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
3

### Summary
The paper proposes a new method to speed up the LLM inference via selectively computing the KV for tokens important for the next token prediction in both the prefilling and decoding stages. The method is training-free. The author also conducts experiments on Llama 2 and XGen.

### Strengths
The following are the strengths.
* The paper introduces an efficient way to speed up LLM inference.
* The paper involves an aux cache to be sure that each token is calculated at once at most.
* The author conducts experiments to support their claims.

### Weaknesses
My concerns mainly come from two parts

First, it seems that the paper template has some problems. To be more specific, the "Anonymous authors Paper under double-blind review" at the Top of Page 1 is in the middle, where it actually should be on the left side. I wonder whether such template change is allowed or not.

Second, there are several parts that the author needs to explain further.
* If possible, could the author provide Python code or pseudo code to explain the idea? This will make it easier for the reader to understand the core idea.
* Question for the KV cache part. 
   * If for the previous generation step, Layer i has tokens [T1, T4, T5, T7] and Layer i+1 has tokens [ T4, T5]. 
   * And for the current generation step,  Layer i has tokens [T1, T2, T4, T5], and Layer i+1 has tokens [ T4, T5]. 
   * **Question**: for the current generation step, do we directly use the [T4, T5] from the KV cache?
   * The paper claims that "each token is computed at most once along
the whole generation" so it seems that the answer is Yes. Then it seems that the previous generation step  Layer i+1 tokens representation [ T4, T5] is different from the current generation step  Layer i+1 tokens representation [ T4, T5]. Why the work could directly use it?
* For Table 1, LazyLLM could even achieve better performance than the baseline which is standard LLM inference. Could you explain such an observation because the baseline should be the performance upper bound of LazyLLM?

### Questions
Please check the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
