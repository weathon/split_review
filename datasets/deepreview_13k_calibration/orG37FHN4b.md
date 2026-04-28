# Angle-DFQ: Angle aware data free quantization

- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 3, 1

## Abstract
Data free quantization of neural networks is a practical necessity as access to training data in many situations is restricted due to privacy, proprietary concerns, or memory issues. We present a data free weight rounding algorithm for Deep Neural Networks (DNNs) that does not require any training data, synthetic data generation, fine-tuning, or even batch norm statistics. Instead, our approach focuses on preserving the direction of weight vectors during quantization. We demonstrate that traditional weight rounding techniques, that round weights to the nearest quantized level, can result in large angles between the full-precision weight vectors and the quantized weight vectors, particularly under coarse quantization regimes. For a large class of high-dimensional weight vectors in DNNs, this angle error can approach 90 degrees. By minimizing this angle error, we significantly improve top-1 accuracy in quantized DNNs. We analytically derive the angle-minimizing rounding boundaries for ternary quantization under the assumption of Gaussian weights. Building on this, we propose a greedy data-free quantization method based on the cosine similarity between the full-precision weight vectors and the quantized weight vectors. Our approach consistently outperforms existing state-of-the-art data-free quantization techniques and, in several cases, surpasses even data-dependent methods on well-established models such as ResNet-18, VGG-16, and AlexNet with aggressive quantization levels of 3 to 6 bits on the ImageNet dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a **data-free quantization** method that preserves the **direction of weight vectors** rather than simply rounding weights to the nearest quantized value. This approach is applied to each neuron's weights in each layer. Through empirical analysis, they show that traditional nearest-neighbor rounding significantly increases the angle between quantized and original weights, leading to accuracy loss. The authors first derive a mathematical basis for ternary quantization (using \{-1, 0, 1\}) under a Gaussian weight distribution and then introduce a **cosine similarity-based method** that greedily rounds weights to minimize angle error. This technique extends effectively to mixed precision quantization as well. Experiments on popular image classification models demonstrate the method’s effectiveness in preserving model accuracy, especially in low-bit settings.

### Strengths
This paper addresses an important research area with practical applications. Its main strengths are:

- Focuses on preserving weight orientation after quantization by minimizing angle deviation, a unique approach not seen in other baselines.
- Data calibration-free, making it suitable for privacy-sensitive applications.
- Enhances low-bit quantization performance.
- Introduces an adaptive threshold specifically for ternary weights.
- Adaptable to mixed precision settings and compatible with other quantization methods.
- Achieves competitive or superior results compared to other data-free quantization approaches.

### Weaknesses
While this paper is theoretically sound, both the writing and evaluation have some notable weaknesses:

### Writing Issues:
1. Numerous spelling and grammatical errors, such as "a number or reasons" (line 043), "course weight quantization" (line 152), "The red line demarks the region" (line 184), "asymtotic" (line 323), "out preforms" (line 517), and "bench marked" (line 408), among others.

### Technical Weaknesses:
1. **Computationally Intensive**: The method requires iterative quantization for each layer and neuron, increasing computational demands. The iterative process of finding the optimal ternary values by minimizing the cosine distance for each weight vector is not only computationally expensive but also lacks a clear analysis of its convergence properties. It's unclear how many iterations are required for convergence, and whether this number varies across different layers or network architectures. Furthermore, the paper does not discuss the practical implications of this computational overhead, such as the increase in training or inference time, which is a critical factor for real-world applications.
2. **Selective Layer Application for Mixed Precision**: Mixed precision quantization requires careful layer selection, adding complexity. The paper lacks a detailed explanation of the layer selection process for mixed-precision quantization. While it mentions selecting layers with high dimensionality, it does not specify the exact criteria or provide a rationale for why this is the optimal approach. The absence of a systematic method for layer selection makes it difficult to reproduce the results and limits the generalizability of the method. Additionally, the paper does not explore the impact of different layer selection strategies on the final performance.
3. **Limited Applicability to Large Language Models (LLMs)**: The method is untested on LLMs, where quantization is highly relevant, raising questions about its broader practicality. Given the increasing importance of LLMs, the lack of experiments on these models is a significant limitation. The paper does not address the challenges of applying this method to the massive scale of LLMs, such as the increased computational cost and memory requirements. It is unclear whether the method can be scaled to handle the complexity of LLMs without significant performance degradation or modifications.
4. **Narrow Experimental Scope**: The experiments are limited to basic vision tasks, restricting insight into its effectiveness across diverse applications. The evaluation is limited to image classification tasks, which does not provide a comprehensive understanding of the method's performance across different domains. The paper should include experiments on other tasks, such as object detection, segmentation, or natural language processing, to demonstrate the method's versatility and robustness. The lack of diverse experiments raises concerns about the method's general applicability.
5.  Angle-DFQ is applied only to a limited subset of weights. The paper does not provide a clear rationale for why the method is applied to a subset of weights, and it does not explore the impact of this choice on the final performance. It is unclear whether applying the method to all weights would result in better or worse performance, and the paper should include an ablation study to investigate this aspect.

### Questions
1.It is unclear to me whether this method quantized the full weights for each experiment. could you elaborate on that?

2. Is the method computationally intensive, given that each layer requires looping through all neurons? Additionally, does it require storing an optimal scaling constant for each neuron?

3. What criteria are used to select the layers where this method is applied?

4. Does Equation (2) hold in its original form in Algorithm 1, considering that weights are scaled before quantization?

5. Can this method be applied to full large language models (LLMs)?

### Suggestions:

1. I recommend revising the writing for clarity and grammar; using an LLM for assistance may be helpful.

2. In Table 1 It would have been better to show the performance improvement/drop over the reference performance since not all methods have the same reference performance.

3. Extending this method to LLMs or larger models would be valuable, as these applications are more relevant for quantized models.

4. An ablation study could be conducted to evaluate the impact of quantizing all layers versus selected layers and to determine if the choice of scale factors should depend on the architecture or if it can be universal for this method.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to minimize the angle between the pre-trained weights and quantized weights for data-free quantization. The approach consistently outperforms existing state-of-the-art data-free quantization techniques in ImageNet classification.

### Strengths
The concept of angle minimization is intriguing, and the experiments demonstrate that it outperforms existing data-free quantization methods.

### Weaknesses
1. The significance of the angle between the pre-trained weights and the quantized weights in the context of quantization is unclear. Specifically, why would minimizing the angle help improve the quantization peformance?

2. The algorithm for implementing angle minimization is not well presented.

3. The accuracy achieved on ImageNet does not surpass that of several other state-of-the-art post-training quantization algorithms. With that said, the comparison with other post-training quantization algorithms, such as OBQ [1] and COMQ [2], is inadequate.

4. The reference Zhang et al. (2019) in line 129 is not found in References section.

### Questions
1. In the proof of Theorem 1, why the limit is equal to 0 in the last step?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper aims to establish a data-free post-training quantization algorithm for low-memory deployment of neural networks. The paper starts off with an analysis of the angle-errors of the quantized weight-vectors in a neural network, which can negatively affect the decision boundaries of the ReLU activation functions. Additionally, the paper solves the problem of the optimal decision boundary for ternary quantization. The paper then presents Angle-DFQ, an optimization algorithm that tries to greedily minimize the angle errors during quantization, and finally the papers evaluates their method on different neural networks from the computer vision community.

### Strengths
- The paper presents an intriguing approach to think about quantization in the term of angle-errors between weight vectors
- The solution to the ternary quantization problem presented in the paper is interesting and clear
- The proposed method is straightforward and easy to understand, and the motivation is made clear through earlier parts of the paper

### Weaknesses
### Presentation
- Spelling / Grammar issues ("due a number", "ect" instead of "etc";  "course weight quantization" instead of "**coarse** weight quantization";  misspelled proper nouns such as "Relu", "Alexnet", "Imagenet"; missing commas; ". ‘ We show", ...),
- Severe formatting errors (misplaced spaces, sometimes using equation environments and sometimes not for numbers,...), especially for references (References are not cited uniformly, f.e. when sources are cited in parentheses, the paper sometimes uses parentheses for the year, sometimes not; the reference on p1. Nagal et al 2020 does not even exist; "Qin et all 2023", etc). 
- Presentation is poor at times: Table 1 is a low-resolution screenshot instead of a proper latex table, the equation under Eq. (4) is out of the bounding box of the text, Equations are numbered seemingly at random (and are non-uniformly referenced, f.e. "equation 1", "equation (3)", "(1)"), the first equation in section 1 has odd formatting for the constraints on the vectors. 
- The derivations have some issues that make them harder to follow, f.e. in Appendix A p.13, the definition of the pdf should be for $|v_{i}| \geq 0$, not $v_{i} \geq 0$ (similarly for the other case), the symbol for $\varepsilon$ is switched mid-way through the derivation (from p.13 to p.14), ...

### Soundness 
- Theorem 1 itself seems to have little relevance, as it only applies to continuous probability distributions whose support is restricted to $x < |\frac{1}{2}|$. Almost all practically used continuous probability distributions that are used to model neural network weights (such as zero-centered gaussians or laplace distributions) do _not_ share this property. The paper mentions in a remark that this can be shown to hold for certain growth rates of $p$, also mentioning that it does _not_ hold for $p$ growing with $cN, c\in [0,1]$.  However, for continuous probability distributions, the growth ratio of $p$ is the mass of the probability density function $\mu_{\varepsilon}$ of $\varepsilon$ outside of $\left[ -\frac{1}{2}, \frac{1}{2} \right]$ times $N$, i.e.  $$p = N \cdot \left(  1-\int_{-\frac{1}{2}}^{ \frac{1}{2}} d\mu_{\varepsilon}\right),$$which is either $0$ for probability densities that have all of their support in $\left[ -\frac{1}{2}, \frac{1}{2} \right]$ or else equal to $cN$ with $c \in [0,1]$ (for a standard normal, $c\approx 0.62$, which is pretty high). Thus, practical probability densities such as gaussians fall exactly into the regime of probability densities for which Theorem 1 does not hold, even when the remark is considered. The condition on the support of the distribution is a very strong assumption that is not met by common weight distributions, making the theorem's practical relevance questionable.
- The results methodology makes it hard to exactly evaluate how much of the improvements come from the proposed method, as the paper combines Angle-DFQ with a mixed-precision bit allocation (which seems to be hand-tuned, so this might indicate some overfitting). This optimized bit allocation could itself be responsible for a large amount of the gains. Additionally, each network has various different methods used on it (which are not the same for each network), which again use different bit widths each. The lack of a consistent experimental setup across different networks makes it difficult to draw general conclusions about the effectiveness of the proposed method.

### Other
- Large parts of the theory seem only weakly connected to the method, as the theory section is concerned with the special case of ternary quantization (which is nicely solved in close-form), but the method itself is a simple greedy optimization on much larger than ternary grids, that decides between two possible quantization options by brute-force calculating the angle-error. The theoretical analysis focuses on a very specific scenario (ternary quantization) that does not directly translate to the general method used in the experiments, which uses a much larger quantization grid. This disconnect between theory and practice makes it difficult to understand the theoretical underpinnings of the empirical results.

### Questions
- I would advise renaming Theorem 1 to Proposition 1 (as the statement as well as the accompanying proof are quite simple).
- While Theorem 1 is very limited in its applicability (see weaknesses section), its general idea seems interesting. Maybe the authors could derive bounds on the angle error for common probability distributions such as gaussians, which would provide a more meaningful contribution
- I would suggest the paper to undergo a major revision of its presentation, using a spell and grammar-checker, using consistent naming and citing (make use of the in-built cite macros from LaTeX), and cleaning up other issues, of which I mentioned some in the weaknesses section. A comparison to some other published and well regarded papers from ICLR or similar conferences might help.
- I would propose to streamline the experiment results by reporting exactly the same configurations of layer-wise bit-widths for each of the methods. Either Angle-DFQ should therefore use uniform bit-widths per layer, or the reported methods should be re-implemented to operate with layer-wise bit allocations. Additionally, the main competitors to Angle-DFQ (which seem to be TNT and Krishnamoorthi, which are also per-layer and data-free) should ideally be reported for each of the networks, if possible.

### Soundness
1

### Presentation
1

### Contribution
2
