# PADRe: A Unifying Polynomial Attention Drop-in Replacement for Efficient Vision Transformer

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8

## Abstract
\vspace{-5pt}

We present Polynomial Attention Drop-in Replacement (\textbf{\padre}), a novel and unifying framework designed to replace the conventional self-attention mechanism in transformer models. Notably, several recent alternative attention mechanisms, including Hyena, Mamba, SimA, Conv2Former, and Castling-ViT, can be viewed as specific instances of our \padre framework.  \padre leverages polynomial functions and draws upon established results from approximation theory, enhancing computational efficiency without compromising accuracy.  \padre's key components include multiplicative nonlinearities, which we implement using straightforward, hardware-friendly operations such as Hadamard products, incurring only linear computational and memory costs. \padre further avoids the need for using complex functions such as Softmax, yet it maintains comparable or superior accuracy compared to traditional self-attention. 
We assess the effectiveness of \padre as a drop-in replacement for self-attention across diverse computer vision tasks. These tasks include image classification, image-based 2D object detection, and 3D point cloud object detection. Empirical results demonstrate that \padre runs significantly faster than the conventional self-attention (\textbf{11$\!\times$$\,\sim\,$43$\times$} faster on server GPU and mobile NPU) while maintaining similar accuracy when substituting self-attention in the transformer models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel approach to replace full-attention with a unified polynomial formulation that achieves linear complexity. The authors show that various efficient attention mechanisms can be seen as special cases within the PADRe framework. They also implement a specific instance of PADRe and observe a favorable trade-off between efficiency and accuracy, even with a polynomial degree as low as 3.

### Strengths
The unified formulation proposed in this paper is intriguing, as it establishes mathematical connections across different attention variants. I believe this polynomial-based approach has great potential for impact, offering a foundation for designing more efficient attention mechanisms in the future.

### Weaknesses
1): Figure 1 illustrates a specific design within the PADRe framework, but a straightforward baseline is missing. For example, for degree-
$d$ approximation, directly ensembling $d$ MLP-Mixers can be a strong baseline, and this approach can also be efficiently parallelized. Furthermore, the computational cost of the proposed method should be compared against this baseline, considering both training and inference time, as well as memory consumption. A detailed analysis of the trade-offs between the polynomial degree $d$ and the performance of the model is also needed, particularly in comparison to the performance of an ensemble of $d$ MLP-Mixers.

2): While the paper introduces a unified formulation, it remains unclear how readers can directly leverage it to enhance existing linear attention mechanisms. In Eq. (8), the coefficients $\pi_k$ are noted to have a complex dependency on parameters, specifically on the properties of the transformation matrices $A_i$, $B_i$, $C_i$ and $D_i$.  For example, in Eq. (82), a practical approximation formulation for the softmax operation can be more concrete. The paper should provide explicit guidance on how to choose these matrices, or at least a set of heuristics, to allow practitioners to effectively use the proposed framework. The lack of clarity on how to instantiate the framework makes it difficult to assess its practical value.

3): The experimental results demonstrate comparable performance with previous methods, but the paper defines the transformation matrices as pointwise and 2D convolutions to mix channels and tokens, respectively. However, it is well-established that adding locality can boost ViT performance (e.g., LocalViT). To fully evaluate the PADRe's effectiveness, testing on NLP benchmarks and models—without adding any locality inductive bias—would provide a more compelling validation. The current results are difficult to interpret because the performance gains might be due to the added locality rather than the polynomial approximation itself. A more controlled experiment is needed to isolate the effect of the proposed method.

### Questions
See weakness.

### Soundness
2

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
This paper introduces Polynomial Attention Drop-in Replacement (PADRe), a new method which aims to replace the conventional self-attention in Transformers. Specifically, PADRe replaces self-attention with polynomial approximants. Furthermore, it adopts mobile-friendly operations such as  Hadamard products to achieve a good balance between efficiency and performance.  The authors have provided rigorous proofs that the proposed PADRe is a general approach that covers previous Hyena, Mamba, SimA, etc. Extensive experiments have also demonstrated the effectiveness of their approach.

### Strengths
1. Good insight and strong theoretical proofs. Approximating self-attention with polynomial approximants sounds interesting. The authors have provided solid proofs that the proposed PADRe can cover other special cases in recent works.

2. Experiments have well demonstrated the effectiveness of their approach, especially considering the FLOPs reduction in Table 3 and Table 4.

3. The paper is in a good structure. Figures are clear as well.

### Weaknesses
1. The paper acknowledges that model performance begins to saturate (Lines 462-463) when the polynomial degree exceeds 3, suggesting potential numerical stability issues with higher-degree polynomials. Investigating more stable polynomial bases could be beneficial. Specifically, the authors should explore orthogonal polynomial bases, such as Chebyshev or Legendre polynomials, which are known for their better numerical properties compared to the standard monomial basis, especially for higher degrees. This could potentially allow for the use of higher-degree polynomials without encountering the same saturation issues, leading to better performance.

2. As the author already states, this paper lacks experiments on LLMs. It would be great if we can know the performance of PADRe on LLMs. This could be more attractive to the community than experimenting on ViTs. The current experiments are limited to image classification tasks using ViTs, which might not fully reflect the potential of PADRe in sequence modeling tasks, where attention mechanisms are more crucial. The paper should include at least some preliminary experiments on a small-scale language model to demonstrate the applicability of PADRe in that domain.

3. In Table 1, the improvement over DeiT-Base is minor. Could it be that PADRe works more effectively for smaller Transformers? It is unclear if the minor improvements observed with DeiT-Base are due to the limitations of PADRe or if the baseline model is already close to optimal performance. It would be beneficial to test PADRe on a wider range of model sizes and architectures to better understand its effectiveness and limitations.

### Questions
See the weakness.

### Soundness
3

### Presentation
3

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
This paper proposes PADRe, a unifying framework for replacing the attention mechanism based on
polynomial approximants to provide an efficient, linear-complexity alternative to the
standard self-attention without sacrificing accuracy.

### Strengths
1. This paper addresses an important problem in vision transformer design.

2. This paper provides a theory-driven solution with a thorough mathematical justification.

### Weaknesses
1. How would the method work for large language models (LLMs), with much longer sequence lengths?

2. How to decide the optimal degree of PARDe?

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a framework for drop in self attention replacement. This framework allows for building any polynomial time self-attention module, relies on polynomial approximates at the input, uses Hadamard product to introduce non-linearities. The framework at its current stage does not look into cross-attention and/or multi-modal attention although in principal it can be extended to cross-attention

### Strengths
- Framework that helps building alternative self-attention based transformer architecture
- advantageous over Flash attention

### Weaknesses
 - The authors evaluated PADRe on DeiT. It might be a good idea to evaluate PADRe on ViT (Dosovitskiy et al.). This will demonstrate the impact of PADRe even more since ViT is widely used as an image encoder for many other models such as CLIP, Vision LLMs etc.
- Since you are evaluating on device, it would be good to show peak memory consumption, anything that shows energy efficiency improvement when running PADRe over standard self-attention

### Questions
- How does replacing self-attention with PADRe change the number of model parameters? Is there any increase or decrease? This will be helpful in understanding PADRe's impact on mobile devices since parameter count is directly correlated to storage, DRAM usage etc.

### Soundness
3

### Presentation
3

### Contribution
3
