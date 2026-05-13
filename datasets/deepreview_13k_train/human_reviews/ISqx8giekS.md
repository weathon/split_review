# LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid

- Decision: Accept
- Scores: 6, 6, 6, 3, 5, 5

## Abstract
Large language models (LLMs) have shown immense potential across various domains, but their high memory requirements and inference costs remain critical challenges for deployment. Post-training quantization (PTQ) has emerged as a promising technique to reduce memory requirements and decoding latency. However, recent accurate quantization methods often depend on specialized computations or custom data formats to achieve better model quality, which limits their compatibility with popular frameworks, as they require dedicated inference kernels tailored to specific hardware and software platforms, hindering wider adoption. Furthermore, many competitive methods have high resource requirements and computational overhead, making it challenging to scale them to hundreds of billions of parameters. In response to these challenges, we propose LeanQuant (Loss-error-aware Network Quantization), a novel quantization method that is accurate, versatile, and scalable. In the existing popular iterative loss-error-based quantization framework, we identify a critical limitation in prior methods: the min-max affine quantization grid fails to preserve model quality due to outliers in inverse Hessian diagonals. To overcome this fundamental issue, we propose learning loss-error-aware grids, instead of using non-adaptive min-max affine grids. Our approach not only produces quantized models that are more accurate but also generalizes to a wider range of quantization types, including affine and non-uniform quantization, enhancing compatibility with more frameworks. Extensive empirical evaluations on recent LLMs demonstrate that LeanQuant is highly \textit{accurate}, comparing favorably against recent competitive baselines in model quality, and \textit{scalable}, achieving very accurate quantization of Llama-3.1 405B, one of the largest open-source LLMs to date, using two Quadro RTX 8000-48GB GPUs in 21 hours.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a method for optimizing the quantization grid in a layerwise loss-aware manner to reduce low-bit weight quantization error. Unlike previous optimization-based approaches like GPTQ, they derive expressions for the optimal settings for the quantization grid rather than the optimal weight update to apply at each step. The approach is generalizable to both non-uniform and uniform quantization grids. This method is able to preferentially preserve more sensitive values, while maintaining computational efficiency by leveraging the layerwise optimization objective. This grid-tuning approach can also be integrated with previous weight update approaches like GPTQ to attain higher accuracy. They demonstrate the accuracy benefits of their approach, and also highlight the computational and memory efficiency of applying their quantization method relative to prior works.

### Strengths
- They present an algorithm to tune the quantization grid using the layerwise loss-aware objective
- They present both non-uniform and uniform methods (the non-uniform method is flexible and leverages clustering, whereas the non-uniform method performs a constrained search over potential scale factors)
- They provide accelerated GPU kernels to solve the objective for their affine quantization approach
- They provide detailed analysis of their method against prior work in both uniform and non-uniform quantization regimes
- They provide multiple ablations demonstrating how their method reduces the loss error, as well as the impacts of K-means initialization

### Weaknesses
 - Although the method of determining weight sensitivity using the layerwise loss is distinct, the approach of performing K-Means clustering in equation (6) to derive non-uniform datatypes is the same as prior work (eg. the sensitivity-weighted clustering approach to derive non-uniform datatypes in SqueezeLLM)


### Questions
- Can you provide any intuition for why the uniform grid point spacing method helps improve accuracy for k-means than k-means++ style grid points (i.e. a visualization of where the initial grid points end up being placed in both cases, versus the “target” grid points)?
- For the efficiency results in Table 9, is the K-means non-uniform quantization grid search parallelizable on the GPU, or is it being run on the CPU?

### Soundness
4

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
4

### Summary
The paper proposes LeanQuant, an accurate, versatile, and scalable quantization approach. LeanQuant is built upon the iterative loss-error-based quantization framework and identify one of the biggest limitations of such methods: the quantization grid introduces high quantization errors due to the existence of outliers in the inverse Hessian diagonals.

### Strengths
The idea is simple and effective, compatible with iterative loss-error-based quantization approaches such as GPTQ. The calibration process is relatively lightweight, allowing for the quantization of models up to 405B. The experimental design of this paper considers the latest model series and different model sizes, which is comprehensive.

### Weaknesses
LeanQuant is built on the core idea of using "inverse Hessian diagonals" metric to quantify the importance of weights. Similar ideas are also introduced in works such as SqueezeLLM [1], which exploits the "Hessian diagonal" metric directly derived from the quantization loss function to identify important weights. Compared to the metric in SqueezeLLM, I think the derivation of the metric in LeanQuant is relatively heuristic. Although LeanQuant beats SqueezeLLM in the final performance, it would be better to directly compare the different importance metrics and show the strengths of the proposed "inverse Hessian diagonals" metric since SqueezeLLM does not leverage GPTQ to minimize the quantization error.



### Questions
1. Whether it can be compared or ablated with other importance metrics such as the "Hessian diagonal" in SqueezeLLM, these works are similar in idea. Please see the weakness part.

2. There is a lack of literature survey on uniform and non-uniform quantization in related works.

### Soundness
3

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
This paper proposes Loss-error-aware Network Quantization (LeanQuant), a method designed to learn loss-error-aware quantization grids to reduce quantization error. LeanQuant determines optimal quantization parameters, such as scaling factor and zero-point, by iteratively narrowing the weight range in discrete steps. To accelerate grid learning, custom CUDA kernels were developed for efficient grid searching. Consequently, the paper demonstrates that LeanQuant can achieve superior linguistic capabilities with quantized LLMs compared to previous methods.

### Strengths
1.	LeanQuant calibrates quantization grids, and it is a novel approach in the post-training quantization of LLMs.
2.	The development of fused CUDA kernels efficiently supports the calibration process, so it makes the complex grid learning procedure more accessible for broad application due to its enhanced efficiency.

### Weaknesses
Overall, several details and evaluation results are missing, which makes it difficult to fully understand and be convinced of the effectiveness of LeanQuant.

1.	A detailed explanation of how LeanQuant can be extended to non-uniform quantization is missing.
2.	Although Section 4 (Experiments) states that the proposed method will be compared with AWQ, GPTQ, and OmniQuant, the evaluation results for AWQ are not presented in the main text (some results for AWQ are included in the appendix only).
3.	While group-wise quantization is widely used in LLM quantization, Table 1 appears to evaluate affine quantization only with row-wise quantization. (Note that AWQ is specialized for group-wise quantization, and layer-wise quantization with AWQ sometimes results in slightly worse linguistic capabilities compared to GPTQ.)
4.	The runtime for LeanQuant is presented with and without the custom kernel in Table 5, but no comparison is made with previous methods.
5.	Peak GPU memory usage for AWQ and GPTQ is not included in Table 4.

### Questions
1.	Could you provide a step-by-step explanation of how LeanQuant is adapted for non-uniform quantization by highlighting key differences from the affine quantization process?
2.	To ensure consistency between the promised and delivered comparisons, I suggest the authors either include a summary of the AWQ results in the main text or explicitly state why they were omitted.
3.	Why did you choose row-wise quantization for the comparison in Table 1? Additionally, do you have results for group-wise quantization? Providing more analysis with various quantization methods could address potential concerns about the fairness of the comparison and offer insights into LeanQuant's performance across different quantization schemes.
4.	I recommend including runtime comparisons with GPTQ, AWQ, and OmniQuant in Table 5 to provide a more comprehensive view of LeanQuant's efficiency relative to other existing methods
5.	I recommend including peak GPU memory usage for AWQ and GPTQ in Table 4, or explaining why this information was omitted. This would offer a more complete comparison of resource requirements across methods.
6.	How are the quantization grids calibrated for non-uniform quantization? Since each grid is independent for non-uniform quantization, I assume the calibration process must differ from the loss-error-aware affine grid described in Section 3.2.2.
7.	What would happen if group-wise quantization were applied to the affine quantization method presented in Table 1?

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
The paper introduces a new quantization method, LeanQuant, designed to improve the efficiency and accuracy of large language models (LLMs) without requiring specialized hardware adaptations.

Key Contributions:
1. LeanQuant innovates on post-training quantization (PTQ) by introducing a loss-error-aware quantization grid. This grid preserves model quality better than traditional min-max grids for outliers in the inverse Hessian diagonals, which otherwise lead to significant accuracy loss.
2. The method generalizes to affine and non-uniform quantization types, making it adaptable to existing frameworks and more compatible with standard inference kernels.
3. LeanQuant demonstrates scalability with successful quantization of models up to 405 billion parameters, achieving high accuracy using limited computational resources.
4. By designing a fused GPU kernel, LeanQuant achieves substantial speedups in grid learning, making quantization efficient and suitable for a range of model sizes.

### Strengths
The strength of this paper lies in its innovative approach to addressing both accuracy and scalability in quantizing large language models, all while maintaining low hardware requirements. LeanQuant introduces a loss-error-aware quantization grid,  tackling the common issue in traditional quantization methods where accuracy is lost due to outliers in inverse Hessian diagonal elements. This approach adapts the quantization grid to preserve the precision of key weights, improving model quality, especially in low-bit quantization.

Additionally, LeanQuant’s multi-format compatibility enables it to integrate seamlessly with popular deep learning frameworks, eliminating the need for specialized inference kernels and greatly enhancing deployment flexibility.

On the scalability side, LeanQuant incorporates a fused GPU kernel design, accelerating the quantization process and allowing it to efficiently handle extremely large models (up to 405 billion parameters) with limited GPU resources. This efficiency showcases LeanQuant’s practicality under constrained computing resources, highlighting its potential for low-cost, high-efficiency AI applications. As a result, the paper presents a robust solution for large-scale model quantization, excelling in quantization quality, resource efficiency, and deployment adaptability.

### Weaknesses
1.  Quantization isn't solely about reducing memory usage or data transfer—it’s fundamentally about reducing the computational workload, which in turn decreases the size of intermediate data and the need for data movement. If the focus is only on reducing model size without addressing the computational load, it could result in diminished acceleration benefits. This is because, even if memory requirements decrease, hardware may still need to perform the same level of computation, which undermines the intended efficiency.
2. As you pointed out, while LeanQuant can quantize models down to 3-bit or 2-bit, modern GPUs often support 4-bit or 8-bit multiplications. Thus, quantizing to lower bit widths (like 3 or 2 bits) might not yield computational efficiency if, during execution, the kernel still calls for a 4-bit multiplier. This forced conversion undermines the benefits of lower-bit quantization since it fails to leverage the intended reduction in computational and resource demands.
3. Without considering the storage format of hardware, 3-bit or 2-bit weights may still be stored on the GPU in higher bit-widths (e.g., 4-bit, 8-bit, or even 16-bit), resulting in excess storage and data transfer requirements. This dilutes the benefits of quantization. Designing quantization methods with hardware-oriented data formats is essential to ensure that low-bit quantized data can be efficiently processed and stored by hardware.

### Questions
The author’s motivation is well-founded, and the experiments are thorough. However, addressing the issues I raised in the weaknesses would greatly strengthen the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes LeanQuant, a novel post-training quantization (PTQ) method that addresses the limitations of existing methods in reducing memory requirements and inference costs of large language models (LLMs). LeanQuant identifies a critical issue in prior PTQ methods, where the min-max affine quantization grid fails to preserve model quality due to outliers in inverse Hessian diagonals. To overcome this, LeanQuant learns loss-error-aware grids instead of using non-adaptive min-max affine grids, enabling accurate and versatile quantization. The method uses an iterative loss-error-based quantization framework, which involves computing the loss-error for each layer, learning a loss-error-aware grid for each layer, and quantizing the model using the learned grids. LeanQuant is evaluated on several large language models, including Llama-3.1 405B, one of the largest open-source LLMs, and achieves high accuracy, comparing favorably to recent competitive baselines. The method is also shown to be scalable, achieving accurate quantization of Llama-3.1 405B using two Quadro RTX 8000-48GB GPUs in 21 hours. LeanQuant's ability to learn loss-error-aware grids enables it to generalize to a wide range of quantization types, including affine and non-uniform quantization, making it a promising solution for reducing the memory requirements and inference costs of LLMs. Overall, LeanQuant provides a novel and effective approach to PTQ, enabling the efficient deployment of large language models in real-world applications.

### Strengths
Paper Strengths:

**Compared to existing iterative loss-error-based quantization frameworks**: LeanQuant addresses the critical limitation of min-max affine quantization grids, which fail to preserve model quality due to outliers in inverse Hessian diagonals, by proposing learning loss-error-aware grids.

**Compared to prior methods using non-adaptive min-max affine grids**: LeanQuant's approach produces quantized models that are more accurate and generalizes to a wider range of quantization types, including affine and non-uniform quantization.

**Compared to other methods in terms of scalability**: LeanQuant is scalable, achieving very accurate quantization of Llama-3.1 405B, one of the largest open-source LLMs to date, using two Quadro RTX 8000-48GB GPUs in 21 hours, which is an improvement over other methods.

### Weaknesses
Paper Weaknesses:

This paper is limited in novelty. The authors proposed two methods: (1) non-uniform loss-error-aware grid and (2) loss-error-aware affine grid. The first method, the non-uniform loss-error-aware grid, is GPTQ combined with k-means, which is similar to GPTVQ [1]. The loss-error-aware affine grid is equivalent to GPTQ with grid range search, which is implemented in the original GPTQ codebase. 
Additionally, they did not compare their work with the most recent state-of-the-art (SoTA) papers.

### Questions
The authors emphasize that range settings are important for quantized network accuracy, and GPTQ uses min-max quantization. In fact, GPTQ employs grid search (instead of SGD) to find the best range setting that minimizes the MSE error (||W-Wq||) https://github.com/IST-DASLab/gptq/blob/main/quant.py#L78-L95 Can authors compare with GPTQ with this MSE range settings? Can the author also explain the conceptual difference between loss-error-aware affine grid and GPTQ + MSE grid search?
 
Regarding the non-uniform loss-error-aware grid, since the weight value changes during iterative GPTQ quantization, it might affect the k-means centroid as well. Did the authors consider this effect? Did the authors measure how far the weight - \delta deviates from the original weight?
 
The authors provide two methods: non-uniform quantization and affine quantization. Can the authors briefly explain in which cases each quantization scheme is recommended?
 
Can authors compare the results with the most recent LLM quantization works, such as QuIP[1], QuIP#[2], QuaRot[3] and SpinQuant[4]?

[1] QuIP: 2-Bit Quantization of Large Language Models With Guarantees

[2] QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks

[3] QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs

[4] SpinQuant: LLM Quantization with Learned Rotations

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Authors propose “Loss-error-aware Network Quantization” a post-training quantization method for reducing memory requirements in addition to latency of LLMs. The method is proposed as an accurate, versatile, and scalable alternative to traditional methods which are either specific hardware and software platforms or require high resources making them unscalable for the larger models. 
The method is based on an iterative loss-error-based quantization framework, overcoming limitation in previous methods: the min-max affine quantization grid fails to preserve model quality due to outliers in inverse Hessian diagonals, instead, authors use loss-error-aware quantization grids, accounting for these outliers.

### Strengths
1.	The paper has written “BACKGROUND” sections well, giving an amazing context of quantization. 
2.	Results validate the superiority of the proposed quantized method.
3.	The claim of scalability and accuracy is satisfactorily answered, 
4.	Algorithm 1 seems to help make sense of the procedure visually. 
5.	The ablation study is written well, which helps make the paper a lot more sense, especially Q1, and Q2.

### Weaknesses
1)  **The paper assumes the readers are well-versed in quantization**. Two elementary concepts of this work: *quantization grid* and affine / non-uniform grids, are not clearly defined inside the paper.   
 a.  **What exactly is grid?** [Line 110] “representing the full-precision floating-point parameters with a limited set of grid points on the quantization grid” What does this mean? An example or visualization would be really helpful here.   
 b.  **[Line 116] “grid points are evenly spaced over the dynamic range of a group of weights”** What does this mean?  
 c.  A simpler discussion/visualization on uniform and non-uniform grids is requested.   
 d.  Equation 6, is first solved to establish a quantization grid. It's confusing to know what the solution to equation 6 means if the reader is unfamiliar with the quantization grid.   
 e.  [Line 117] Group of weights? What’s that? Quantization needs some form of grouping of weights, why? Works don’t seem to establish it.    


2)  **Page 6 needs a simpler rewrite if possible**.   
 a.  The works seem to be indicating some problems with the grouping of weights using KNN, but it's confusing to understand the problem. 
 b.  [Line 285] equation doesn’t have an equation number
 c.  It's not clear what part is already established and what parts are being proposed by the work. Equation 6: where did this equation come from or is derived in some previous work?, similarly Equation 7, and the equation on [Line 285], are authors proposing these equations. There doesn’t seem to be any explanation/derivation for these, just of out blue written as a solution. If they are already established solutions, citing works will help. 
 d.  “Efficient Fused GPU Kernel for Grid Learning” gives the 50x efficiency. Can this multi-threading technique be applied to existing work and make them more efficient as well? 

3)  The solution is based on the presence of outliers with abnormally high values in empirical distributions of inverse Hessian diagonals, (figure 1). This can be dataset-specific or model-specific. Show the presence of outliers in other datasets as well as models as well.

4)  **Contradictory results?** Table 10 shows p values as not so important for quantization. P > 0 is good enough for solving highly accurate quantization? Why does Table 10 doesn’t have p=1? Also, p >1 indicates the “extra” weightage of “outliers” in quantization, the first separation from existing work. 
[Line 259] : “The min-max affine grid employed by previous iterative loss-error-based quantization methods do not account for the existence of inverse-diagonal outliers, which may cause significant model quality degradation”
Does this mean, that just by the presence of outliers p=1, has more or less the same performance as P > 1, just accounting for outliers creates better grid formation? 
Results for other techniques (SqueezeLLM, GPTQ, OmniQuant) with p=1 or >1 (equation 6), outlier accounted grids can help validate the importance of this outlier driven gird.

5)  Minor issue: 
 a.  Table 2 & 3: please mention of vanilla FP16 accuracy. 
 b.  Table 2 & 3: Also non-uniform LeanQuant accuracy. 
 c.  Table 4: GPTQ Memory values missing

### Questions
Please address all the weakness

### Soundness
3

### Presentation
2

### Contribution
3
