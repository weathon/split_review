# SpinQuant: LLM Quantization with Learned Rotations

- Decision: Accept
- Avg Score: 5.80
- Scores: 5, 6, 6, 6, 6

## Abstract
Post-training quantization (PTQ) techniques applied to weights, activations, and the KV cache greatly reduce memory usage, latency, and power consumption of Large Language Models (LLMs), but may lead to large quantization errors when outliers are present. Rotating activation or weight matrices helps remove outliers and benefits quantization. In this work, we identify a collection of applicable rotation parameterizations that lead to identical outputs in full-precision Transformer architectures while enhancing quantization accuracy. In addition, we find that some random rotations lead to much better quantization than others, with an up to \emph{13 points} difference in downstream zero-shot reasoning performance. As a result, we propose \ours{}, a novel approach that incorporates learned rotation matrices for optimal quantized network accuracy. With 4-bit quantization of weight, activation, and KV-cache, \ours{} narrows the accuracy gap on zero-shot reasoning tasks with full precision to merely 2.9 points on the LLaMA-2 7B model, surpassing LLM-QAT by 19.1 points and SmoothQuant by 25.0 points. Furthermore, SpinQuant also outperforms concurrent work QuaRot, which applies random rotations to remove outliers. In particular, for LLaMA-3 8B models that are hard to quantize, \ours{} reduces the gap to full precision by up to 45.1\% relative to QuaRot.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a learned rotation based method, namely $\texttt{SpinQuant}$ to mitigate outliers in weight and activation distributions, boosting the performance of quantized LLMs. In specific, the authors  proposes optimizing rotation matrices within Stiefel manifold, directly minimizing the final loss of rotated quantized network. The authors further propose two variants, $\texttt{SpinQuant}$_easy and $\texttt{SpinQuant}$_hard without and with change of

### Strengths
The idea of learned rotation in  the context of LLM activation outlier reduction seems interesting.

The authors have done thorough analysis to justify the need of learned rotation 

$\texttt{SpinQuant}$ can outperform baseline GPTQ by significant margin!

### Weaknesses
1. The performance of $\texttt{SpinQuant}$ is similar or worse than QuIP in most of the cases. This further raises concerns on the learned rotation method as QuIP does not rely on any activation rotation method.

2. The calibration discussion (thorough) is missing. As the method needs to learn R1,R2, R3 and R4, such calibration and/or fine-tuning overhead is a concern. Specifically, the number of calibration samples, the optimization time for each rotation matrix, and the sensitivity of the method to the calibration dataset are not adequately discussed.

3. How the learning gets affected for activation rotation, when there is extremely low calibration data?

4. The can be other alternatives to learn the R1-4, why did the author chose Cayley SGD method (Li et al., 2020). The justification for using Cayley SGD over other optimization techniques for Stiefel manifolds is not clear, especially considering the computational overhead and convergence properties of alternative methods.

5. Why table 6 shows results with $\texttt{SpinQuant}$_hard even for W4A8? It is unclear why the 'hard' variant, which includes online Hadamard rotations, is evaluated for W4A8, where activation quantization is not the bottleneck.

6. What speedup benefit we may have with $\texttt{SpinQuant}$_hard and $\texttt{SpinQuant}$_easy with W4A4? The paper lacks a detailed analysis of the actual speedup achieved with the proposed methods, especially the trade-off between accuracy and speed for $\texttt{SpinQuant}$_hard and $\texttt{SpinQuant}$_easy in the W4A4 setting.

7. The contribution is primarily centered around rotation to get rid of activation outliers and smoothen out while for the quantization part the authors heavily rely on GPTQ (or RTN). The baseline GPTQ may often be considered a calibration heavy that require Hessian information. I have concerns on the calibration overhead of the method as well as the novelty. The reliance on GPTQ, which itself requires significant calibration, raises questions about the overall efficiency and novelty of the proposed approach. The paper does not adequately isolate the contribution of the learned rotations from the underlying quantization method.

### Questions
1. It would be interesting to see the performance of such dynamic quantization ($\texttt{SpinQuant}$) with static quantization alternative [1]. 

2. Is the R3, R4 needed in case someone uses block reconstruction of [2]? 

3. Also, how does $\texttt{SpinQuant}$ compare w.r.t these alternative methods?

4. Why the choice of ``optimizing these rotation matrices on Stiefel manifold", is not fully clear.

[1] PREFIXQUANT: STATIC QUANTIZATION BEATS DYNAMIC THROUGH PREFIXED OUTLIERS IN LLMS, arxiv 2024

[2] TESSERAQ: ULTRA LOW-BIT LLM POST-TRAINING QUANTIZATION WITH BLOCK RECONSTRUCTION, arxiv 2024.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work investigates post-training quantization (PTQ) for LLMs, applied to weights, activations, and KV cache. It addresses the large quantization errors issue from outliers by introducing the learned rotation matrices into the network architecture. Through experiment validations, the proposed framework shows effectiveness in extreme W4A4KV4 quantization settings on representative networks.

### Strengths
+ The paper pursues the rotation method for post training LLM quantization, which demonstrates convincing performance.

+ The authors conducted thorough investigations about random rotations to propose quantization-oriented rotation learning.

+ The proposed framework develops strategies for the challenging activation and KV cache quantization, besides weight quantization.

### Weaknesses
- While the rotation matrix method is effective in mitigating outliers in LLM quantization, it is better if more rigorous explanations/proofs are provided for the rationale behind, besides empirical results.

- Introducing rotation matrices into the inference pipeline may lead to overhead in computing. Could the authors provide analysis the overhead vs benefit from quantization?

### Questions
Although the rotation method is effective, the readers may be interested in the theoretical foundations of this methodology.

Please provide analysis on the overhead introduced by the rotation matrices into the inference pipeline vs the benefits.

The reviewer would like to know the training complexity of the proposed method comparing with other quantization approaches.

### Soundness
4

### Presentation
3

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
The paper presents SpinQuant, a quantization technique specifically designed to reduce the impact of outliers in large language models (LLMs) through learned rotations. SpinQuant introduces learned rotation matrices that can be integrated into pre-trained weights, which aids in preserving accuracy in low-bit quantization scenarios. The proposed method includes two modes: SpinQuant-easy and SpinQuant-hard—the former for more straightforward quantization with mergeable weights, and the latter for complex scenarios needing enhanced outlier suppression with non-mergeable weights. The authors validate SpinQuant across multiple models (e.g., LLaMA-2, LLaMA-3, and Mistral) using a comprehensive set of zero-shot reasoning benchmarks.

### Strengths
- By employing learned rotations, SpinQuant offers a new approach to minimizing outliers.
- The SpinQuant-easy and SpinQuant-hard modes offer flexibility, making the approach adaptable to different computational constraints and accuracy requirements through mergeable and non-mergeable weights.
- SpinQuant shows compatibility with methods like GPTQ, allowing it to integrate into established quantization pipelines.

### Weaknesses
 - The benchmarks and model selections, such as the LLaMA series, seem to focus on favorable cases for SpinQuant. Testing on a broader range of architectures (e.g., Gemma2) would provide a more thorough evaluation. Especially Gemma2 series which exhibit distinct activation characteristics—could provide a more comprehensive assessment of SpinQuant's generalizability and robustness across diverse LLM types.
- Although the authors note the optimization time (up to 3.5 hours for larger models), it remains unclear how this time impacts real-world deployment, especially on low-resource devices.
- From an outlier-aware quantization perspective, as demonstrated by methods like AWQ, SpinQuant should ideally exhibit strong performance even in weight-only quantization scenarios. However, even after examining the appendix, there is no evaluation comparing its performance under weight-only quantization. It would be beneficial to include a comparison of SpinQuant’s performance in weight-only quantization settings to provide a more comprehensive view of its robustness and effectiveness relative to other quantization techniques.
- While the paper presents promising results on zero-shot reasoning tasks, it does not evaluate SpinQuant's performance in fine-tuning or few-shot learning scenarios. Including such evaluations would strengthen the claims about SpinQuant’s overall effectiveness and versatility.

### Questions
- Have the authors considered testing alternative calibration datasets beyond WikiText2? It would be interesting to see if different calibration sets impact SpinQuant’s generalization, especially in domain-specific applications (e.g., code). While the paper describes the use of WikiText2 for calibration, further analysis on its impact and comparison with alternative calibration data could strengthen the understanding of its generalization.
- it would be interesting to know if SpinQuant has been tested on models from other domains, such as Vision Transformers (ViTs) or vision-language models, to further assess its versatility across different types of architectures.

### Soundness
2

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
2

### Summary
This paper introduces SpinQuant, a PTQ method that applies optimized rotations to reduce quantization errors from outliers, improving LLM efficiency without compromising accuracy. It achieves near full-precision performance, narrowing the accuracy gap to 2.9 points on zero-shot tasks in LLaMA-2 7B, outperforming previous works.

### Strengths
- paper is well-written
- specifically, the illustrative example in 4.4 is very helpful. Yet, it would be sensible to move this one more to the front of the paper
- experiments are extensive across models, settings and methods

### Weaknesses
 - The current rotation is not optimal, as the authors state. It would be a very valuable contribution to investigate optimal rotations further.
- a more detailed discussion on model size vs rotation-based quantization is needed. Larger models are impacted less by quantization compared to smaller models, why?
- currently, no effort to publish code or quantized models given, limiting reproducibility and usability for the community.
- the tradeoff discussion between easy and hard is too shallow. Please elaborate on which cases are useful to use one or the other.

### Questions
- Could you provide a comparison of the computation needed for the quantization? Going beyond comparing accuracies on benchmarks alone would be helpful.
- the number of rotation matrices is determined empirically. Can the authors investigate this further and explain in more detail how this can be validated better?

### Soundness
3

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
4

### Summary
This paper introduces SpinQuant, a novel approach to mitigate outliers during Large Language Model (LLM) quantization by leveraging learned rotation matrices. The paper presents two rotation strategies: 1) an "easy mode" for W4A8KV8 quantization where rotation matrices can be absorbed without impacting inference, and 2) a "hard mode" incorporating two additional online rotation matrices for more aggressive quantization scenarios (e.g., W4A4KV4). Through evaluation across various LLMs and reasoning tasks, SpinQuant demonstrates that its learned rotation matrices outperform random rotation approaches.

### Strengths
- Proposed a learned version of rotation matrices to address variance issues inherent in random rotation approaches, with demonstrated flexibility across different quantization scenarios.
- The paper is well-structured, presenting clear methodology and comprehensive diagrams that effectively illustrate the proposed approach.

### Weaknesses
 - Limited evaluation scope on complex tasks benchmarks: The evaluation would be more compelling with results from more challenging benchmark tasks, such as [MMLU](https://arxiv.org/abs/2009.03300) and [MMLU-Pro](https://arxiv.org/abs/2406.01574).
- Incomplete theoretical analysis, while Section 4.4 demonstrates Hadamard rotation's superiority over random rotation, it lacks a thorough comparative analysis between learned and random rotation matrices. The significant 10+ point improvement observed on Mistral-7B using hard mode could serve as a good case study to demonstrate the benefits of learned rotation matrices.
- Limited performance benchmarking: The end-to-end speed evaluation is confined to MacBook M1 hardware, with only basic FP8 quantization latency testing on GPU rather than comprehensive benchmarking across the paper's proposed quantization scenarios. Given recent research highlighting potential performance impacts of online rotation transformations (e.g., [QServe]( https://arxiv.org/abs/2405.04532), Part V Section C), more extensive benchmarking on modern GPU architectures would strengthen the paper's practical implications. Key speedup metrics could include time to first token (TTFT) and tokens per second (TPS).

### Questions
- Regarding Formula (1), is the clip operation missing?
- For Figure 1, there are two R3 after the `RoPE`, should one of them be the inverse of R3?
- Could you clarify which rotation type is being demonstrated in Figures 9 and 10?

### Soundness
3

### Presentation
3

### Contribution
3
