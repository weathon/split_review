# Zeroth-Order Fine-Tuning of LLMs with Transferable Static Sparsity

- Decision: Accept
- Avg Score: 5.80
- Scores: 5, 6, 6, 6, 6

## Abstract
Zeroth-order optimization (ZO) is a memory-efficient strategy for fine-tuning Large Language Models using only forward passes. However, applying ZO fine-tuning in memory-constrained settings such as mobile phones and laptops remains challenging since these settings often involve weight quantization, while ZO requires full-precision perturbation and update. In this study, we address this limitation by combining static sparse ZO fine-tuning with quantization. Our approach transfers a small, static subset (0.1%) of "sensitive" parameters from pre-training to downstream tasks, focusing fine-tuning on this sparse set of parameters. The remaining untuned parameters are quantized, reducing memory demands. Our proposed workflow enables efficient ZO fine-tuning of an Llama2-7B model on a GPU device with less than 8GiB of memory while outperforming full model ZO fine-tuning performance and in-context learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a transferable static sparse ZO LLM fine-tuning strategy. It observes an extreme sparsity pattern in LLM parameters: a subset, determined by selecting the top k magnitude entries from the diagonal of empirical Fisher information matrix, is effective for ZO fine-tuning. Moreover, it finds this sparsity pattern can be obtained through LLM’s pre-training process and transferred to various downstream tasks without modification. Building on these insights,  it proposes SensZOQ, an on-device LLM personalization workflow
via integrating Sensitive ZO optimization with Quantization to further improve the memory efficiency of ZO fine-tuning.

### Strengths
It identifies that only an extremely small portion (0.1%) of LLM parameters should be updated during ZO LLM fine-tuning. Moreover, it observes that this sparsity pattern can be derived in LLM pre-training process and transferred across different downstream tasks while still maintaining good ZO performance without any modification.

It conducts extensive experiments across various LLMs and demonstrate that the method achieves competitive performance across various downstream tasks.

### Weaknesses
The novelty may be limited. The proposed method mainly use masks to select a small set of parameters and update these parameters with ZO method while quantizing the rest parameters. The quantization and ZO methods are very typical, following previous works. The mask construction by selecting the top k magnitude entries from the diagonal of empirical Fisher information matrix has been proposed in (Sung et al., 2021, Training Neural Networks with Fixed Sparse Masks).  The idea of updating the weights with fixed sparse masks for language models has been investigated in (Sung et al., 2021) and SparseMeZO  (Liu et al., 2024a). The technical components are not novel and their combination seems to be straightforward. The technical contribution may be limited. 

The comparison on memory usage may not be fair. The method quantize the model and it compares the memory of quantized model with other unquantized models from other methods. We are not sure whether simply quantizing models can lead to such memory reduction. Furthermore, during the mask construction, it needs to use backpropagation to obtain the gradients of all parameters. This part costs massive memory. But in the memory comparison, it does not count the memory cost for mask construction and only include the memory in ZO finetuning after the mask is obtained. And it also not count the memory cost for quantization part. Although the authors use a on-device flow to count on-device memory,  it may not be fair to compare part of the memory usage of the proposed method with the full memory usage of other methods.  

It only experiments with 7B  or smaller models. It is better to have some results on larger models such as 13B and 30B to demonstrate the general performance on larger models. It claims to be efficient with less memory usage and faster training speed. It should be easy to apply to larger models. 

It only experiments with one single finetuning dataset C4. It may be better to experiment with multiple finetuning datasets to demonstrate the general performance. 

It claims to be faster in inference with higher Token generation speed. But after finetuning, it is still a dense model, and we are not sure how the faster token generation is achieved. Though there are some discussions in appendix for the sparse operations,  there do not seem to be much details and we only see some function calls without detailed implementation for the functions to understand why it is faster.  It may be due to the quantization. But quantization in the work just follows SqueezeLLM (Kim et al., 2024). It may be better to provide some high level discussions for why the inference can be faster.

### Questions
see the weakness. 

It is better to highlight the contributions and discuss the fairness of memory comparison. It is better to have some results on larger models such as 13B and 30B to demonstrate the general performance on larger models. It may be better to provide some high level discussions for why the inference can be faster.

### Soundness
3

### Presentation
3

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
This paper proposes SensZOQ, a workflow framework sparse zeroth-order optimization with quantization for on-device fine-tuning of LLM. It identifies a small, static subset of "sensitive" parameters in pre-training, transfers them to downstream tasks, and quantizes the rest to reduce memory demands. Experiments on 7B-level LLMs show SensZOQ outperforms other methods in memory-constrained settings, achieving better performance than in-context learning and full ZO Full-FT.

### Strengths
The work enables fine-tuning of Llama2-7B model on <8GiB GPU memory by using only 0.1% static sensitive parameters and quantizing the rest, meeting memory constraints of edge/mobile devices and enabling more customization scenarios at the edge.

SensZOQ outperforms ICL and ZOFull-FT, achieving competitive results across various downstream tasks and models like SST-2, RTE, etc.

The work also conducts details theory analysis and overview of related ZO methods (Sec 2,3) and reveals that 0.1% contributes about 50% gradient norm scales.

### Weaknesses
The paper is well-presented with a clear structure. My main concerns revolve around the experiment setup and comparisons.

How does the fine-tuning fit within 8GB of memory? Does this include the memory for the model states themselves? For instance, the authors claim that LLaMA-7B fits within 8GB memory constraints. However, even when quantized to 4 bits, storing the model alone requires 3.5GB, not accounting for other intermediate buffers needed during training. The paper needs to clarify the memory breakdown, including the model weights, optimizer states (if any), and intermediate activations during forward and backward passes, to validate the claim of 8GB memory usage.

What is the transferability of the sparse mask (e.g., sensitive sparse masks), and how is it generated? Is this sparse mask generally applicable across different downstream tasks, or does SensZOQ require a new one for each task? Lines 236-240 reference a fixed work, but the authors don't provide an ablation study to support this claim. The paper should include experiments that explore the impact of using different sparse masks generated from different datasets or tasks to assess the robustness and generalizability of the proposed method.

The convergence curve or training curve is missing. As mentioned in the introduction and related work, zero-order (ZO) methods suffer from slow convergence. However, the authors only discuss the theoretical convergence rate without providing an empirical curve. Additionally, in all experiment tables, the results of full fine-tuning (Adam, BF16) are missing, and no actual memory usage or throughput data is provided. The paper needs to show empirical convergence curves, compare against full fine-tuning baselines (Adam, BF16), and provide actual memory usage and throughput data to support the claims of efficiency and effectiveness.

### Questions
What is the rank meaning in Table 1, 2? Average all ranks?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a memory-efficient zeroth-order (ZO) optimization approach for fine-tuning large language models (LLMs) in memory-limited environments, such as mobile devices. By tuning only a sparse subset of "sensitive" parameters derived from pre-training, the proposed method, SensZOQ, enables efficient on-device fine-tuning without backpropagation. SensZOQ demonstrates competitive performance compared to in-context learning and full-model ZO fine-tuning, even on GPUs with less than 8 GiB of memory. Key contributions include the identification of transferable sparse parameters and the integration of static sparsity for enhanced efficiency. While SensZOQ addresses memory limitations effectively, the ZO optimization’s slower convergence and static sparsity’s limited adaptability across tasks are noted as areas for potential improvement.

### Strengths
Intuitive and Effective Approach Supported by Theory: The paper presents an intuitive yet impactful approach by focusing on a sparse subset of sensitive parameters for zeroth-order (ZO) optimization. This idea is both straightforward and theoretically sound, and the authors support it well with theoretical analysis that adds credibility to their method.

Strong Experimental Validation: Through extensive experiments, the paper demonstrates the superiority of its proposed method. SensZOQ is shown to perform effectively across multiple tasks, validating the approach's potential for on-device fine-tuning in memory-constrained environments.

### Weaknesses
Sensitivity Assessment Limited to C4 Dataset: The authors measure sensitivity based solely on the C4 dataset, which predominantly covers natural language tasks. This raises concerns about the applicability of their sensitivity-based sparse tuning approach to tasks with different characteristics, such as code generation. It remains uncertain whether the proposed method would generalize well to tasks with substantially different data distributions and requirements.

Evaluation on Small Model Sizes Only (7B): The experiments focus on models with a maximum of 7 billion parameters, which is relatively small compared to leading models. This raises questions about whether the proposed approach would remain effective on larger models where more precise fine-tuning might be required. It would be valuable to see an assessment of SensZOQ’s applicability and performance on larger, state-of-the-art models where scaling issues might become more prominent.

Lack of Analysis on Slow Convergence Issue: The paper notes that ZO optimization can suffer from slow convergence, which is a well-documented drawback of ZO methods. However, it lacks an in-depth analysis of this issue. A discussion of potential mitigations or how this slow convergence might impact the method’s performance, especially in time-sensitive applications, would have added valuable context.

Unclear Insights from Theoretical Convergence Rate (Section 2.3): While the authors present a theoretical convergence rate, the practical implications or lessons from this analysis are unclear. It would benefit the reader to understand what actionable insights can be drawn from this theoretical result. Without this clarity, the theoretical component feels somewhat disconnected from the rest of the work.

Similarity to Existing Research on Activation Outliers: Although the paper asserts the effectiveness of using a static mask, this approach bears resemblance to previous work on activation outliers. If the sensitivity mask is closely related to known methods for identifying important model parameters, such as activation outliers, the novelty of this contribution may be limited. Further discussion comparing SensZOQ with prior work in this area could clarify its unique contributions.

Insufficient Details on Quantization Methodology: The paper does not provide adequate details regarding the specific quantization technique used. Given the potential impact of quantization on model performance, a clearer explanation is necessary to assess the reproducibility of the experiments. Without this information, readers may find it challenging to replicate the results, which is a significant drawback for scientific validation.

### Questions
Please refer to the weaknesses.

### Soundness
4

### Presentation
3

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
The paper proposes a sparsity-aware ZO fine-tuning technique and the authors point out the method can be useful in on-device fine-tuning.

### Strengths
I believe the paper has the following strength:

1. ZO can help reduce memory consumption due to gradient and optimizer. When used in combination with quantization, dense weights can also be compressed, further reducing memory consumption.

2. Supporting the "sparse sensitive parameters" assumption with cumulative normalized sum of gradient norm square is intuitive, and apply it sparse ZO fine-tuning (SensZOQ) is elegant. 

3. I appreciate detailed formulation on convergence rate of SensZOQ, along with proof for Eq.5 and Eq. 6. 

4. Solid ablation studies on the efficacy of SensZOQ versus other weight importance metrics. Detailed analysis of gradient sparsity and sparse sensitive parameter dynamics in the appendix. Implementation and experiment details for reproducibility.

### Weaknesses
I have two major concerns about the paper.

1. The first is about its experiment section and its practicality. On device personalization is an important topic. I understand the authors might want to focus on edge applications and on some easier NLP benchmarks. However, all benchmarks used are can be easily handled with decoder-encoder transformers, yet at a much smaller scale. For example, RoBERTa (see page 8 in their paper) can outperform SensZOQ applied to LLMs (numbers shown in in Table 1 and Figure 5). RoBERTa-base only consists of 125M parameters, with RoBERTa-large at 355M scale. On the other hand, even with SOTA W3/W4 quantization, LLaMA2-7B takes > 3GiB of memory, just for forward pass. And this number is significantly higher than using smaller decoder-encoder transformers like RoBERTa, T5 etc. In this case, for , why should I use SensZOQ fine-tuning + LLMs instead of regular fine-tuning + smaller decoder-encoder transformer models?

2. The second concern is about the assumption: the transferable static sparsity argument is a strong argument. In Figure 3 and Figure 5, the authors have shown empirical evidences that the hypothesis holds for some tasks including RTE, WiC, COPA. However, how well this can be generalized to some other harder tasks (math, common sense reasoning, code, MMLU etc.)?

### Questions
I will be much more convinced if the authors could provide answers to the following questions (from high to low priority):
1. What is the justification of applying SensZOQ to LLaMA2-7B vs. directly fine-tuning decoder-encoder transformers like RoBERTa? It seems those smaller transformers consume less memory (great for edge devices), yet achieve better performance.
2. Can you provide some experiment results to show how well SensZOQ performs on harder common-sense reasoning, math/code reasoning and domain-knowledge benchmarks like (PIQA, gsm8k/humaneval, MMLU etc.)? I think those are the benchmarks that LLMs can excel in comparison with those smaller models. Even if SensZOQ fine-tuning doesn't perform well on those benchmarks and there is a big gap between SensZOQ and full-parameter fine-tuning, I think it would be fruitful to inform the community about its limitations. 
3. Is the code going to be open-sourced in the future?
4. Since the loss landscapes of LLMs can be highly non-convex and complex, would assumption 2, 3 (page 17) always hold? If there are literature studies that discuss this issue, could you provide the pointers?
5. Could the authors elaborate on the concept of "fixed (gradient) features" and explain why it holds? Additionally, more evidence supporting the validity of transferable static sparsity across other tasks would be helpful.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces SensZOQ, a method that combines static sparse zeroth-order (ZO) fine-tuning with quantization to address the limitations of standard ZO. SensZOQ focuses on fine-tuning a small subset (0.1%) of "sensitive" parameters, while keeping the remaining parameters quantized to reduce memory usage and maintain competitive performance on various downstream tasks. This framework enables efficient fine-tuning of an LLaMA2-7B model on a GPU with less than 8GB of memory, outperforming traditional full-model ZO in both memory efficiency and learning performance.

### Strengths
**Memory Efficiency**: The method significantly reduces memory usage, allowing LLM fine-tuning on low-memory devices (less than 8GB).

**Quantization Integration**: Incorporating quantization further enhances memory efficiency without substantial performance loss.

**Resource-Constrained Applicability**: Designed for mobile and low-power devices, making it suitable for on-device personalization.

### Weaknesses
Some key experiment comparisons and discussions are missing; please refer to the questions for details.

Some abbreviations are not defined before their first use, making the paper somewhat challenging to follow. For example:
1. “FO” is not defined before it first appears.
2. Baseline methods listed on the x-axis of Fig. 1 are not explained in either the figure caption or the text referencing the figure, which hinders understanding of this key figure.

For **Table 1**:
1. Although the proposed method surpasses the listed methods, it would be helpful to also report the fully fine-tuned FO results as a baseline.
2. Since this paper emphasizes training efficiency in both memory and wall-clock time, providing memory and time comparisons would help to further illustrate its effectiveness.
3. Could the authors explain why the proposed method achieves better performance compared to ZO Full FT (the fourth row), despite incorporating both sparse funetuning and quantization?
4. The introduction section discusses various advanced ZQ methods; comparing the proposed method with these would better highlight and validate its effectiveness.

For **Table 2**:
1. Similarly, it would be helpful to include both memory and runtime comparisons to better demonstrate the effectiveness of the proposed method.
2. Could the authors explain why the proposed method achieves better performance than 16-bit ZO-SGD (the second row), despite using both sparsity and 4-bit quantization?
3. While this paper focuses on training efficiency and notes that the memory consumption of 16-bit FO-Adam on OPT-1.3B is higher than that of 4-bit ZO-SGD on OPT-6.7B, I am curious about their memory and runtime consumption from an inference perspective.

### Questions
For **Table 1**:
1. Although the proposed method surpasses the listed methods, it would be helpful to also report the fully fine-tuned FO results as a baseline.
2. Since this paper emphasizes training efficiency in both memory and wall-clock time, providing memory and time comparisons would help to further illustrate its effectiveness.
3. Could the authors explain why the proposed method achieves better performance compared to ZO Full FT (the fourth row), despite incorporating both sparse funetuning and quantization?
4. The introduction section discusses various advanced ZQ methods; comparing the proposed method with these would better highlight and validate its effectiveness.

For **Table 2**:
1. Similarly, it would be helpful to include both memory and runtime comparisons to better demonstrate the effectiveness of the proposed method.
2. Could the authors explain why the proposed method achieves better performance than 16-bit ZO-SGD (the second row), despite using both sparsity and 4-bit quantization?
3. While this paper focuses on training efficiency and notes that the memory consumption of 16-bit FO-Adam on OPT-1.3B is higher than that of 4-bit ZO-SGD on OPT-6.7B, I am curious about their memory and runtime consumption from an inference perspective.

### Soundness
2

### Presentation
2

### Contribution
3
