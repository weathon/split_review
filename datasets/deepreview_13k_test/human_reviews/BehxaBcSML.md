# CDQuant: Accurate Post-training Weight Quantization of LLMs using Greedy Coordinate Descent

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Large language models (LLMs) have recently demonstrated remarkable performance across diverse language tasks. But their deployment is often constrained by their substantial computational and storage requirements. Quantization has emerged as a key technique for addressing this challenge, enabling the compression of large models with minimal impact on performance. The recent GPTQ algorithm, a post-training quantization (PTQ) method, has proven highly effective for compressing LLMs, sparking a wave of research that leverages GPTQ as a core component. Recognizing the pivotal role of GPTQ in the PTQ landscape, we introduce CDQuant, a simple and scalable alternative to GPTQ with improved performance. CDQuant uses greedy coordinate descent to minimize the layer-wise reconstruction loss to achieve high-quality quantized weights. Our algorithm is easy to implement and scales efficiently to models with hundreds of billions of parameters. We perform extensive evaluation on Gemma, and PaLM2 model families, and demonstrate that CDQuant consistently outperforms GPTQ  in 2-4 bit weight quantization. Moreover, CDQuant improves the performance of state-of-the-art PTQ techniques such as QuIP and FrameQuant when used as a replacement for their GPTQ component, resulting in further gains in quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents CDQuant, a quantization algorithm that improves the efficiency LLM through a greedy coordinate descent approach. CDQuant is an incremental work following GPTQ, a post-training quantization method by minimizing layer-wise reconstruction loss. The authors evaluate CDQuant across multiple model families, including Gemma and PaLM2, where it shows slight performance improvements over GPTQ in 2-4 bit weight-only quantization.

### Strengths
CDQuant proposes a unique greedy coordinate descent approach for LLM quantization, offering an alternative to the cyclic method used in GPTQ. 

The experiments are comprehensive, covering multiple models and quantization settings.

The algorithmic description of CDQuant, as well as the variants, are clearly explained.

### Weaknesses
High computational cost: CDQuant’s runtime is much higher than GPTQ, especially on larger layers (e.g., FFN2). While the authors suggest mitigation strategies, further optimizations could enhance practicality.

Incremental Improvement: the idea is an incremental change to GPTQ, the improvement is also marginal compared with GPTQ, especially in the W4A16 setting which is the most practical use case.

### Questions
How does CDQuant perform in layers with extreme outliers compared to other approaches, like SqueezeLLM, which address outlier weights?

What modifications would be necessary to apply CDQuant to Quantization-Aware Training (QAT)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents CDQuant, a new quantization method for large language models that improves on GPTQ by using greedy coordinate descent to achieve better accuracy in low-bit quantization. It outperforms GPTQ in experiments on models like Gemma and PaLM2, providing lower perplexity and enhanced performance. CDQuant can also seamlessly replace GPTQ in other quantization techniques, making it a versatile and effective tool for compressing large models.

### Strengths
1. CDQuant consistently outperforms GPTQ in low-bit (2-4 bit) quantization, leading to better quantization quality and lower perplexity across various models.
2. The greedy coordinate descent approach in CDQuant provides better optimization of the layer-wise objective compared to GPTQ, leading to more efficient quantization. 
3. CDQuant demonstrates significant performance improvements, especially on smaller models like PaLM2-Gecko and Gemma-1 7B, where it reduces perplexity by up to 10%.

### Weaknesses
1. CDQuant, particularly with Block Coordinate Descent (BCD), is significantly slower than GPTQ, especially for large models. The paper presents runtime comparisons (Table 5) showing that CDQuant is about 5× slower than GPTQ for FFN1 quantization and up to 10× slower for FFN2 quantization on models like Gemma-2 27B. BCD is even slower, with runtimes an order of magnitude higher than GPTQ in some cases.
2. For larger models, such as Gemma-2 27B, the computational cost of CDQuant becomes prohibitive. The time required to quantize the FFN2 layer, which has a larger quantization axis, is significantly higher than for other layers. This is demonstrated in Table 20, where FFN2 quantization takes up to 10× longer than FFN1 quantization.
3. Experiments based on a series of new models should be included in the paper. Would the llama series models, such as llama3, also be suitable for CDQuant?

### Questions
1. What are the theoretical guarantees of CDQuant's convergence? Does the greedy coordinate descent method guarantee convergence to a global minimum, or is it more prone to local minima, especially in high-dimensional spaces like those of LLMs?
2. How does CDQuant perform on models larger than those tested (e.g., models with trillions of parameters)? The paper demonstrates results on models with up to tens of billions of parameters (like Gemma-2 27B). How would CDQuant scale to models with trillions of parameters?
3. Why was MinMax quantization chosen as the baseline for comparison? The paper mentions that CDQuant uses Optimal Weight Clipping (OWC) for initialization, which performs better than MinMax quantization. Why not compare CDQuant's initialization with other advanced techniques like SmoothQuant or AWQ?
4. How does CDQuant perform when both weights and activations are quantized? The paper primarily focuses on weight quantization. How does CDQuant perform when both weights and activations are quantized, especially in scenarios like W4A4 quantization? How do the results compare with those of some recent quantization papers [1-3]?

[1] OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models. ICLR 2024.

[2] AffineQuant: Affine Transformation Quantization for Large Language Models. ICLR 2024.

[3] QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs. Arxiv 2024.

[4] SpinQuant: LLM quantization with learned rotations. Arxiv 2024.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors present CDQuant, an alternative to GPTQ that offers better performance in LLM quantization. CDQuant uses greedy coordinate descent to minimize layer-wise reconstruction loss, resulting in high-quality quantized weights. Evaluations on models such as Gemma and PaLM2 show that CDQuant outperforms GPTQ in 2-4 bit quantization. Furthermore, when integrated into other PTQ techniques like QuIP and FrameQuant, CDQuant enhances their performance as well.

### Strengths
1. This paper presents a set of improvements to GPTQ and introduces CDQuant, a straightforward and efficient alternative.

2. CDQuant demonstrates versatility and effectiveness when integrated with other PTQ techniques, such as AWQ, QuIP, and FrameQuant.

### Weaknesses
1. Actually, GPTQ has already identified the issue that OBQ updates coordinates in a greedy manner and introduced the Arbitrary Order Insight, which significantly reduces quantization time. Although CDQuant makes several efforts to accelerate quantization speed, it remains noticeably slower than GPTQ.

2. The experimental results suggest that, compared to GPTQ, CDQuant demonstrates certain advantages only on smaller models with relatively weaker capabilities, such as Gemma-1 7B and PaLM2-Gecko. However, it does not show clear advantages on models like Gemma-2, PaLM2-Otter & Bison, and it also lacks experiments on the LLama2 & 3 families, which are more commonly used in mainstream quantization research (e.g., GPTQ, QuIP, AWQ, etc.). Given that CDQuant uses more calibration data (1280 V.S. 128) and adopts OWC method, the benefits of using the greedy coordinate descent method remain uncertain.

### Questions
1. Since the LLama family models are more commonly used in LLM quantization research, could you provide CDQuant's results on LLama 2 and LLama 3 for a more intuitive comparison?

2. Currently, rotation-based quantization methods, such as QuaRot and SpinQuant, effectively eliminate outliers and demonstrate better performance than previous methods like AWQ and QuIP. Given that both QuaRot and SpinQuant use GPTQ for weight quantization, could you assess the versatility and effectiveness of CDQuant when integrated with these methods?

3. CDQuant uses 1280 samples for calibration, while 128 is more commonly used in other methods (e.g., GPTQ, AWQ, etc.). However, the authors did not explain this choice. Could it be because CDQuant leverages second-order information for error compensation and may overfit the calibration set during reconstruction?

### Soundness
3

### Presentation
4

### Contribution
2
