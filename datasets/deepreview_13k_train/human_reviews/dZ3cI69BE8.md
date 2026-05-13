# FlexBCQ: Flexible Binary-coding Quantization for Large Language Models

- Decision: Reject
- Scores: 6, 5, 5, 3, 6

## Abstract
How can we compress large language models without compromising accuracy?
Quantization, which reduces the number of bits for representing weights, is an essential technique to utilize large language models (LLMs) in real-world applications.
Specifically, binary-coding quantization (BCQ) is a promising approach since it has extensive representation space, which encompasses the representation space of uniform quantization (UQ), and fast inference speed.
However, because of the lack of accurate optimization techniques, BCQ shows inferior performance compared to UQ algorithms, failing to leverage their powerful expressive power.
In this paper, we propose FlexBCQ (Flexible Binary-coding Quantization), an accurate optimization algorithm for BCQ.
We leverage the sophisticated optimization techniques of UQ by decomposing the quantization process of BCQ into the composition of a UQ and an inner BCQ.
As a result, we take advantage of both the sophisticated optimizing techniques of UQ, specifically the flexible mapping technique, and the powerful expressive capability of BCQ.
Through extensive experiments, we find that FlexBCQ provides 3.24%p higher accuracy than existing UQ and BCQ algorithms on MMLU 5-shot benchmark when quantizing a Llama-3 70B model into 3 bits.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a combination of two popular techniques: FlexRound for uniform quantization (UQ), and Alternating for Binary-Coded Quantization (BCQ). In UQ, the quantization points are uniformly spaced within a pre-specified range, and the scalar value being quantized, is scaled, by a parameter called "scale" and shifted by a parameter called "zero-point" (to make it zero-centered). For UQ, prior work FlexRound introduces two additional scaling parameters ($s$ and $s_r$ in the paper) that are learnable -- which is shown to improve the performance of vanilla UQ.

On the other hand, BCQ expresses a scalar as sums and differences of a fixed set of scale factors. In theory, BCQ has a larger representation space, and it can be shown that UQ is a special case of BCQ. However, in practice, BCQ is not seen to perform well for LLM quantization practices, primarily due to the difficulty in optimizing its hyperparameters.

This work proposes a combination of both UQ and BCQ steps for quantization, and proposes FlexBCQ -- which has a unified initialization strategy that combines the initialization of both UQ and BCQ. In FlexBCQ, BCQ is applied after an application of FlexRound's transformation (for UQ). The hyper-parameters in FlexBCQ are optimized using a small calibration dataset, and some results show that they better aligns with the distribution of the weights (It is essential to use a quantization scheme that aligns well with the distribution of model weights). Eventually, the combined quantization process does not add any additional memory or latency overhead.

### Strengths
The combination of UQ and BCQ is pretty neat, and also seems to be promising based on the set of experiments evaluated on in the paper. LLM compression is an important topic, and the contribution of this work is useful in light of the fact that custom kernels such as LUT-GEMM exist, that leverage BCQs for faster throughput.

The experiments are done on a reasonably wide set of models and tasks. Moreover, additional studies that show the alignment of the (learned) quantization levels with the distribution of weights is also highly appreciable. For the most part, the paper is generally well-written.

### Weaknesses
I have some concerns which are mentioned below:

1. It is claimed that prior work on BCQ (Xu et. al., 2018) independently updates $\alpha_{(k)}$ and $\mathbf{b}_{(k)}$ are updated independently. Are there any ablation results that show how it performs for LLM quantization?

2. It might be worth considering ablations on the choice of calibration dataset, especially for Llama-3 models. Can you provide some justification as to how these datasets were chosen? Usually, for compression, subsets of the pre-training datasets are presumed to be good choices as calibration dataset. So was there any particular reason why C4 was chosen and not RedPajama (which is the pre-training dataset for OpenLlama)? Also, any ablations on the size of the pre-training dataset?

3. Is it possible to provide a comparison of the average number of bits per parameter used by FlexBCQ, along with the other strategies it is being benchmarked against?

4. Is it possible to use the kernels from LUT-GEMM to see an actual improvement in inference throughput?

I would be more than happy to reconsider my score contingent on other reviews, and the authors' rebuttal.

### Questions
In addition to the concerns mentioned above in the "Weaknesses" section, I have some more queries, and would be grateful if the authors could address them: 

1. I initially had about why despite its greater expressive power, BCQ significantly underperforms compared to UQ, which has limited expressive capabilities for LLM compression (as mentioned in lines 67-68)? This was perhaps answered in 199-200 -- Is this a hypothesis and are there concrete datapoints to support this? I might have missed this in the reading of the paper.

2. There is a potential typo in the definition of $\Delta_{(k)}$. Perhaps it should be $(w_{M,c} - w_{m,c})/2^{k-1}$?

3. In Line 195 - 196, please point to a more precise Theorem/Lemma in Park et. al. for reference.

4. How is $\boldsymbol{\alpha}_{(k)}$ chosen? Is it optimized for each group of weights separately?

5. How is the blockwise output reconstruction done? For each weight matrix independently, or for each entire decoder layer at once?

6. The gradient filtering section can benefit from a little more explanation. Does it mean that when the mapping error exceeds epsilon, the gradients are zeroed out?

7. Please specify all the learnable parameters in FlexBCQ explicitly in a sentence somewhere.

8. The LLM quantization problem formalization in the beginning of Sec. 2.1 needs more description.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents FLEXBCQ (Flexible Binary Coding Quantization), a method for compressing neural networks using a UQ and an inner BCQ, allowing advantage of both the sophisticated optimizing techniques of UQ, specifically the flexible mapping technique, and the powerful expressive capability of BCQ. Especially, the approach employs unified initialization algorithm for initializaiton and apply Straight-Through Estimator (STE) for non-differetiable steps with blockwise output reconstruction error to optimize quantization accuracy per block. Compared to FlexRound and other baselines, this method demonstrates significant compression rates while maintaining model performance.

### Strengths
1. Effective Combination of UQ and BCQ: The integration of Uniform Quantization (UQ) and Binary Coding Quantization (BCQ) leverages the strengths of both approaches, providing flexible mapping and expressive representation capabilities. The paper demonstrates the effectiveness of this combination, especially in experiments with the Llama-3 70B model.

2. Unified Initialization and Blockwise Output Reconstruction: The unified initialization approach, combined with blockwise output reconstruction, enhances quantization accuracy by aligning each block more closely with the original model output. This method strengthens the reliability of the quantization process and contributes to maintaining model performance post-compression

### Weaknesses
1. Readability Issues: The reading experience could be improved; please refer to the Questions section for specific details.

2. Additional Bits for Hyperparameters: Both quantization algorithms in FLEXBCQ require additional bits to store hyperparameters. Please include the bitwidth calculations for FLEXBCQ and list them when comparing against baselines in Table 1. Compared to FlexRound and UCB, FLEXBCQ uses additional storage, which contributes to its better performance. A fair comparison with the baselines should account for these extra storage requirements.

3. Clipping Strategy in Algorithm 1: In Algorithm 1, only the minimal values are iteratively clipped, rather than clipping both minimal and maximal values. Given that outliers could also appear on the maximal side, this may not be the optimal strategy. Please provide further explanation or an ablation study to justify this design choice

### Questions
1. I assume that the terms weight group and blockwise refer to the same concept in the context of FLEXBCQ, correct?

2. In Section 3.3 (Line 303) and Section 3.4 (Line 324), $M_U$ is mentioned as part of the algorithm. However, it is not reflected in Equation (4) or in Algorithm 1 (after Line 279). Could you clarify this?

3. Please have more details regarding the optimization for $\delta(k), z_U(k), s, s_r$, and $\alpha(k)$ when minimizing blockwise output reconstruction error. Is this process similar to Algorithm 1, using a grid search approach?
 
4. Please provide more details regarding the optimization of $\Delta(k),z_U(k),s,s_r$, and $\alpha(k)$when minimizing blockwise output reconstruction error. Is this process similar to Algorithm 1, using a grid search approach?

5. Line 140: $W_{M,c} - W_{M,c}$ →  $W_{M,c} - W_{m,c}$

6. Could you provide more details in your figures to clarify their meaning? These adjustments would help clarify the figures and strengthen the visual argument for FLEXBCQ’s effectiveness.

        a. Figure 1: What do the gray bars and blue arrows represent? This figure seems to suggest that a point can be attributed to quantized values, but I'm not entirely certain. Could you explain if this interpretation is correct?

        b. Figure 4: Are 4.(a) and 4.(b) for the same weight? Are there any correspondences between their distributions? It’s unclear if Figure 4(b) alone sufficiently demonstrates that FLEXBCQ outperforms FlexRound. It is best to explain the y-axis of Fig. 4(b) in the title. 

7. In lines 160-161, is $s, s_r$ for a whole weight like $W_k$ or a single weight block?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents FLEXBCQ, a novel binary-coded quantization (BCQ) algorithm that enhances the compression efficiency of large language models without compromising accuracy. FLEXBCQ combines Unified Quantization (UQ) and internal BCQ, benefiting from UQ’s advanced optimization while preserving BCQ's expressive power. The paper also introduces a unified initialization method for more accurate quantization parameter initialization and an optimization technique based on block output reconstruction to improve model accuracy. Experimental results demonstrate improvements over existing UQ and BCQ algorithms on the MMLU 5-shot benchmark.

### Strengths
1.	This method leverages UQ's advanced optimization techniques while maintaining BCQ's strong expressive power, which shows its novelty.
2.	Its unified initialization method and block output reconstruction optimization techniques are innovative approaches, making sense for future research in the quantization field.
3.	The experimental data in the paper is comprehensive, and the visual analysis is clear and concrete.

### Weaknesses
1.	Some of FLEXBCQ's optimization techniques, such as gradient filtering and periodic remapping, require tuning additional hyperparameters, which could increase the complexity of usage. May authors could explore ways to automatically set these hyperparameters. Specifically, the gradient filtering introduces a threshold hyperparameter that needs careful selection, and the periodic remapping requires tuning the remapping interval, both of which add to the practical burden of using the method. The paper lacks a clear discussion on how sensitive the final performance is to these hyperparameters, and what strategies could be used to find optimal values without extensive grid searches.
2.	The unified initialization method proposed by FLEXBCQ is specifically designed for this algorithm and does not offer alternative initialization methods, potentially limiting its applicability to other quantization algorithms. It is unclear whether this initialization method can be adapted or generalized to other quantization schemes, or if it is tightly coupled to the specific structure of FLEXBCQ. This lack of flexibility could hinder the broader adoption of the proposed initialization technique.
3.	The writing needs improvement in the sequence of formula derivations and other
details, as the readability of the derivation process is poor. For example, the formulas in Eq1 and Eq4 appear somewhat disorganized and need a more concise and clear description. The current presentation makes it difficult to follow the mathematical reasoning and understand the core mechanisms of the proposed method. The lack of clear definitions for each term in the equations and the absence of step-by-step derivations further complicate the understanding.

### Questions
1.	Could you please discuss the sensitivity of tuning these hyperparameters and provide guidelines for tuning them? 
2.	It may help to discuss the potential generaliiability of the unified initialization method to other quantization algorithms
3.	Are there any related works beyond UQ and BCQ that perform similar large model quantization, which could further enrich the experimental data?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces FLEXBCQ, a method that integrates FlexRound (UQ) and Binary-Coding Quantization (BCQ). The authors demonstrate promising performance enhancements with FLEXBCQ on the MMLU 5-shot and 0-shot tasks.

### Strengths
1. This paper provides a foundational overview of the UQ and BCQ methods. Although some sections could benefit from clearer explanations, the background information is useful for readers in general.

2. The integration of UQ and BCQ is clearly presented in Figure 3, offering a straightforward conceptual outline that supports the paper’s logic.

### Weaknesses
1. Figures 1 and 2 fail to clarify the logic and pipeline of FlexBCQ. A more abstract diagram that highlights the main innovations of FlexBCQ and outlines its functionality would be beneficial. Unfortunately, Figures 1 and 2 are quite confusing as currently presented.

2. The main purpose of Theorem 1 (Composition Theorem) is unclear. The theorem lacks subsequent analysis or illustration, making it difficult to understand its application to BCQ or FlexBCQ. The section appears to discuss results related to FlexBCQ, but the text refers to BCQ. Further clarification on the detransformation function and analysis of these results is needed to grasp their significance.

3. The empirical results presented are not compelling. According to Table 1, FlexBCQ shows only marginal improvements and, in some cases, underperforms compared to the simpler FlexRound.

4. The absence of code and insufficient implementation details in Appendix B raise concerns about reproducibility. Providing the code or more comprehensive details would significantly aid in evaluating the robustness and applicability of the proposed method.

### Questions
1. How does FlexBCQ perform under extreme quantization conditions, such as using only 2 bits or fewer? Is such a level of quantization feasible, and if so, what can be expected in terms of performance?

2. If I understand correctly from Figure 3, FlexBCQ combines BCQ and UQ. Could the authors clarify the key innovations behind this integration? It would be beneficial if the benefits could be explicitly demonstrated through theoretical measures, such as convergence rates or other relevant criteria. Additionally, the primary challenges of this combination are not entirely clear to me.

3. How do the running time and inference speed of FlexBCQ compare with those of baseline methods? I am particularly interested in whether this method is both time and memory efficient.

4. In addition to the 5-shot and 0-shot MMLU results, could the authors also provide perplexity scores to give a more comprehensive view of the model's performance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes an approach to improve the performance of binary-coding quantization (BCQ) via flexible mapping of quantization levels and dedicated optimization procedure. The introduced approach is evaluated on several modern language models at 3 and 4 bit compression targets.

### Strengths
* FlexBCQ manages to significantly improve the performance of BCQ and becomes competitive with state-of-the-art algorithms for uniform quantization.

* This work identifies the issues with prior approaches to BCQ for LLM quantization and proposes nontrivial, yet sensible solutions, to stabilize the fine-tuning of BCQ parameters.

* The presentation quality is good. The main points, challenges and experimental results are stated clearly.

### Weaknesses
 * Something is wrong with Mistral 7B scores. According to the table, all methods show significant performance drop relative to fp16 baselines, whereas for other models underconsideration 4 bit models are close to the original model. In addition, Mistral 7B should have inferior performance to Llama 3 8B.

**Minor**

I3 (line 224) Typo Blokwise -> Blockwise

 * The paper claims that GPTQ and AWQ yield significantly worse performance than OmniQuant. However, in my personal experience, GPTQ and AWQ appear to be pretty robust at 4 bit quantization and typically lose only 1-2% relative to the original model on MMLU and GSM8k. I would suggest checking experimental setup for these methods.

* MMLU and GSM8k are quite representative benchmarks. However, for a comparison with prior art, I would suggest reporting Wikitext2/C4 perplexity for quantized models (or a subset of 0-shot benchmarks from lm-eval-harness).

* What is the best value for periodic remapping? In the main experimental section, p=2 is adopted for all models except Llama-3 70B. Does even less frequent remapping help? It would be good to have a plot performance vs p for the sake of completeness.

* How was the duration of the optimization procedure chosen? 20 epochs could be excessive, as the amount of data is small and the model may start to overfit (the number of trainable parameters is small either). I would suggest adding an ablation on this. 
What is the runtime of the method for the models considered?

* It would be insightful to present aggregated statistics over different weights of the value $|I(w) - I(w_f)|$ across model - i.e percentage of weights for each value.

### Questions
* The paper claims that GPTQ and AWQ yield significantly worse performance than OmniQuant. However, in my personal experience, GPTQ and AWQ appear to be pretty robust at 4 bit quantization and typically lose only 1-2% relative to the original model on MMLU and GSM8k. I would suggest checking experimental setup for these methods.

* MMLU and GSM8k are quite representative benchmarks. However, for a comparison with prior art, I would suggest reporting Wikitext2/C4 perplexity for quantized models (or a subset of 0-shot benchmarks from lm-eval-harness).

* What is the best value for periodic remapping? In the main experimental section, p=2 is adopted for all models except Llama-3 70B. Does even less frequent remapping help? It would be good to have a plot performance vs p for the sake of completeness.

* How was the duration of the optimization procedure chosen? 20 epochs could be excessive, as the amount of data is small and the model may start to overfit (the number of trainable parameters is small either). I would suggest adding an ablation on this. 
What is the runtime of the method for the models considered?

* It would be insightful to present aggregated statistics over different weights of the value $|I(w) - I(w_f)|$ across model - i.e percentage of weights for each value.

### Soundness
2

### Presentation
3

### Contribution
2
