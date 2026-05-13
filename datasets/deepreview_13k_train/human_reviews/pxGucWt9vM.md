# FlatQuant: Flatness Matters for LLM Quantization

- Decision: Reject
- Scores: 8, 5, 3, 5, 5

## Abstract
Recently, quantization has been widely used for the compression and acceleration of large language models~(LLMs). 
Due to the outliers in LLMs, it is crucial to flatten weights and activations to minimize quantization error with the equally spaced quantization points. Prior research explores various pre-quantization transformations to suppress outliers, such as per-channel scaling and Hadamard transformation. 
However, we observe that these transformed weights and activations can still remain steep and outspread. In this paper, we propose \name\ (\underline{\textbf{F}}ast and \underline{\textbf{L}}earnable \underline{\textbf{A}}ffine \underline{\textbf{T}}ransformation), a new post-training quantization approach to enhance flatness of weights and activations.
Our approach identifies optimal affine transformations tailored to each linear layer, calibrated in hours via a lightweight objective. 
To reduce runtime overhead, we apply Kronecker decomposition to the transformation matrices, and fuse all operations in \name\ into a single kernel.
Extensive experiments show that \name\ sets up a new state-of-the-art quantization benchmark. For instance, it achieves less than \textbf{1}\% accuracy drop for W4A4 quantization on the LLaMA-3-70B model, surpassing SpinQuant by $\textbf{7.5}\%$. 
For inference latency, \name\ reduces the slowdown induced by pre-quantization transformation from 0.26x of QuaRot to merely \textbf{0.07x}, bringing up to \textbf{2.3x} speedup for prefill and \textbf{1.7x} speedup for decoding, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces FlatQuant, a post-training quantization method for LLMs that focuses on flattening the distributions of weights and activations to reduce the quantization error. The key innovation is using learnable affine transformations optimized per layer, with Kronecker decomposition to reduce overhead. The authors also develop an efficient kernel that fuses the transformations with quantization.

The main contributions are:
1. A theoretical framework highlighting the importance of flatness in LLM quantization
2. The FlatQuant method that achieves state-of-the-art W4A4 quantization results
3. An efficient implementation that provides up to 2.3x speedup for prefill and 1.7x for decoding, with minimal overhead from transformations (0.07x vs QuaRot's 0.26x)

The approach is validated across multiple model sizes and quantization settings with comprehensive experiments and ablations.

### Strengths
1. The observation that flatness is the main influence on quantization error is insightful and well-supported. The motivation to improve flatness through learnable transformations is theoretically sound.

2. The Kronecker decomposition of the transformation matrix effectively reduces both memory and computation costs while maintaining performance. The training methodology is well-designed and practical.

3. The CUDA kernel implementation effectively reduces inference cost through fusion of operations.

4. The evaluation demonstrates that FlatQuant achieves impressive results, particularly: Less than 1% accuracy drop for W4A4 quantization on LLaMA-3-70B; Consistent improvements across different model sizes and tasks; Better speedups compared to existing methods like QuaRot.

### Weaknesses
1. Figure 3 is confusing and needs better explanation. The caption should better explain the relationships between subfigures and clarify the flow of operations.

2. While the efficient implementation and speedup is impressive, theoretical complexity analysis is crucial for algorithm development. The evaluation lacks important theoretical analysis:
- No detailed computation complexity analysis
- Missing information about total parameter counts (including decomposed transform matrices)
- No comprehensive memory consumption analysis for inference

3. Limited model architecture coverage (only LLaMA family in this paper)

4. Citation gap for learnable clipping threshold work, such as "Duanmu H, Yuan Z, Li X, et al. SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models[J]. arXiv preprint arXiv:2405.06219, 2024."

### Questions
1. Regarding the Kronecker decomposition: What is the perplexity performance without decomposition (direct training)?

2. Model generalization:
- How does the method perform on other model architectures (Gemini, Qwen, etc.)?
- Are there any architectural limitations or requirements?
- Would different model architectures require different decomposition strategies?

3. Training stability:
- How sensitive is the method to different initialization strategies?
- What is the impact of calibration data selection?

### Soundness
3

### Presentation
3

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
This paper propose FLATQUANT to enhance flatness of weight and activation. It consist of:

1) Learnable affine transformation;
2) Kronecker Decomposition to decompose the large transformation into 2 small matrix;
3) Per-Channel Scaling
4) Learnable Clipping Thresholds.

This paper is easy to follow. Experiments show relatively good performance compared to current SOTA like SpinQuant. Ablation study part explains  the effect of each technique.

### Strengths
1. This paper propose Kronecker decomposition to decompose the large matrix P into 2 small matrix. The varying size of decomposition  have limited impact on the perplexity of generated text, and the speedup peaks when P1 and P2 are of equal size.
2. This paper propose learnable clipping threshold, where current works usually adopts grid search.
3. The figures in this paper helps easy understanding of the proposed FLATQUANT.

### Weaknesses
1. In perplexity, learnable transformation and learnable scaling of FLATQUANT are borrowed from existing works. 
2. Learnable clipping threshold does not compare with existing CNN works like Leveraging Inter-Layer Dependency for Post -Training Quantization [1], also does not show detailed analysis on learnable clipping threshold  why not causing important outliers clipped, as Llm.int8() [2].
3. In speedup, Kronecker Decomposition still involves online transformation and can not achieve pure int computation.

### Questions
1. What's the perplexity improvement of pure learnable clipping threshold? In table3, in perplexity, whether the difference of SpinQuant and FLATQUANT is the learnable clipping threshold? Is the perplexity improvement mainly from pure learnable clipping threshold? 
2. In Figure5, why the speedup curve is not almost-symmetricly distributed? The speedup of 2048 is substantially slower  than  2's.

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
This paper proposes FLATQUANT, a fast learnable affine transformation used to enhance the smoothing of weights and activation values, while the authors propose the use of Kronecker decomposition and operator fusion to reduce the runtime burden. Extensive experiments demonstrate the effectiveness of FLATQUANT in the W4A4 case.

### Strengths
1. The paper was well written and clearly presented;
2. The authors show the effectiveness of the algorithm through extensive experiments;
3. The authors reduce the runtime burden by means of Kronecker decomposition and operator fusion, which is meaningful for many scenarios.

### Weaknesses
Although the author's method achieved significant gains, there were a few points that could not be ignored that contributed to my initial score:
1. The flatness and quantization error expressed in the authors' paper do not strictly correspond. A simple example [3,4,5,6] has significantly higher quantization error at 2-bit than [0,0,0,sqrt(86)]; in fact, the authors only optimize the loss in Eq. (4) in their paper, and there is no direct correlation with flatness;
2. In the paper, the authors mainly compare the method with QuaRot and SpinQuant, and from my point of view, the way that authors compare is unfair, because the computational overhead of FLATQUANT is totally different from QuaRot and SpinQuant. Taking QuaRot as an example, only the rotation matrix in Query and Key and the rotation matrix after SiLU need to participate in the online computation in QuaRot, while all other matrices can be merged into the weights, while FLATQUANT has a large number of matrix multiplications that need to participate in the matrix computation of the floating-point, which introduces quite a lot of computational burdens compared to QuaRot, so I think the author's comparison is totally unfair. Meanwhile, the authors did not clarify this part of the paper;
3. While I strongly agree that the author's use of Kronecker decomposition and operator fusion reduces the runtime burden, which is also valid for QuaRot, the author's Speed Up comparison of Online Transformations in Figure.6 leads readers to mistakenly believe that FLATQUANT's accuracy-performance of the In fact, on the one hand, QuaRot's additional floating-point computation is less than FLATQUANT's, and on the other hand, the Kronecker decomposition and operator fusion reduces Hadamard's runtime burden under GEMM computation (instead of Walsh-Hadamard Transformation), so I think the comparison in Figure.6 is biased and misleading.

### Questions
See weekness.

### Soundness
2

### Presentation
3

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
This paper builds upon AffineQuant by leveraging Kronecker decomposition to design efficient kernels that integrate affine transformations and quantization. This approach helps mitigate the doubled computation and memory access overhead caused by the pre-quantization transformation in AffineQuant. Experimental results demonstrate that FlatQuant achieves superior accuracy compared to existing methods under the W4A4 configuration.

### Strengths
* The paper employs Kronecker decomposition to design efficient kernels that integrate affine transformations and quantization, reducing the doubled computational and memory overhead caused by the pre-quantization transformation in AffineQuant.

* The paper further enhances accuracy by introducing activation clipping through learning, which yields notable improvements.

### Weaknesses
 * Even with Kronecker decomposition, FlatQuant still requires a pre-quantization step before each linear input, leading to O(n) memory accesses and O(nlogn) computational overhead, where n is the model's feature dimension. For a single block of LLaMA, this transformation needs to be applied more than six times, increasing the model’s complexity. In contrast, SpinQuant requires only one pre-quantization transformation, which may offer a more significant advantage.  I would be very grateful if more comparisons on the additional computational complexity and parameter quantity improvement brought by Spinquant and FlatQuant could be provided.

* AffineQuant ensures that affine transformations remain invertible by employing diagonal dominance, but it’s unclear how FlatQuant maintains invertibility.  This information seems to be missing from the current paper and would be important for understanding the method's robustness. 

* It is also puzzling that the paper does not report zero-shot performance for weight-only quantization. As shown in other works, LWC tends to cause overfitting, and the perplexity metric may not reflect true performance.  I would be very grateful if more weight-only results could be provided.

* OmniQuant only trains smooth parameters, while FlatQuant adds the inverse affine matrix, pre-quantization, SVD decomposition, and learnable activation clipping operations. Strangely, the paper reports that FlatQuant is 10 times faster than OmniQuant, which raises concerns. A more equitable and transparent comparison will be employed if a more detailed breakdown of the timing comparisons is provided, including information on the implementation details and the hardware used for both methods.

### Questions
* OmniQuant only trains smooth parameters, while FlatQuant adds the inverse affine matrix, pre-quantization, SVD decomposition, and learnable activation clipping operations. Strangely, the paper reports that FlatQuant is 10 times faster than OmniQuant, which raises concerns. A more equitable and transparent comparison will be employed if a more detailed breakdown of the timing comparisons is provided, including information on the implementation details and the hardware used for both methods.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
FLATQUANT, a new post-training quantization method, enhances weight and activation flatness via optimal affine transformations, calibrated quickly with minimal runtime overhead using Kronecker decomposition. It sets a new state-of-the-art with W4A4 quantization and significantly improves inference speed.

### Strengths
1. This paper sets a new state-of-the-art performance.
2. Extensive experiments validate its effectiveness.
3. Fast CUDA kernel implementation enhances its applicability.

### Weaknesses
1. The manuscript does not clearly explain how the invertibility of $\mathbf{P}$ is maintained during training. Detailing the methods used to ensure this could improve understanding of the method. Specifically, the use of a re-parameterization technique, such as SVD, should be explicitly stated and justified, along with a discussion of its stability and computational overhead compared to direct matrix inversion.
2. I notice the use of Kronecker decomposition during inference and SVD during calibration, but the specific methodologies for Kronecker decomposition are not detailed. Elaborating on these could clarify the approach. The paper should specify how the Kronecker factors are selected and how the decomposition is performed, including the dimensions of the decomposed matrices and the computational cost of the decomposition itself. It is also unclear if the Kronecker decomposition is applied to the full transformation matrix or to sub-blocks, and how this choice affects performance.
3. The potential approximation errors from Kronecker decomposition and their impact on model performance are not mentioned. Experimental results in this area would be beneficial. A detailed analysis of the approximation error introduced by the Kronecker decomposition should be included, possibly by comparing the full transformation matrix with its Kronecker approximation. This analysis should quantify the error and correlate it with the observed performance degradation, if any. Furthermore, the paper should explore how the choice of decomposition rank affects the trade-off between accuracy and computational efficiency.
4. The overhead of dynamic activation clipping during inference and the individual contributions of $\alpha_a$ and $\alpha_w$, should be explored. The paper should provide a breakdown of the computational cost of dynamic activation clipping, including the time spent on calculating the clipping bounds and applying the clipping operation. It should also include an ablation study that isolates the effects of $\alpha_a$ and $\alpha_w$ on the final performance, showing how each parameter contributes to the overall accuracy and stability of the quantization process.
5. The ablation study should include separate evaluations for "PS", "LCT", and "PS+LCT" to comprehensively demonstrate the improvements from each component.

### Questions
1. The distribution of $\mathbf{W}_d$, $\mathbf{W}_q$, $\mathbf{W}_k$, and $\mathbf{W}_v$ and their corresponding activations is not shown. Visualizations like Fig. 2 for these weights and activations would be beneficial.
2. I am curious about the speedup ratio of the method on Hopper architecture GPUs (e.g., H100, H800).
3. Could the authors explain why the per-channel scaling is employed? A proper $\mathbf{P}'$ can contain the ability to balance outliers between the weights and activations, for example,  $\mathbf{P}'=\mathbf{P}\text{dig}(\mathbf{c})$.

### Soundness
3

### Presentation
4

### Contribution
3
