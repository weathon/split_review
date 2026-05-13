# Attention-aware Post-training Quantization without Backpropagation

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
Quantization is a promising solution for deploying large-scale language models (LLMs) on resource-constrained devices. 
Existing quantization approaches, however, rely on gradient-based optimization, regardless of it being post-training quantization (PTQ) or quantization-aware training (QAT), which becomes problematic for hyper-scale LLMs with billions of parameters.
This overhead can be alleviated via recently proposed backpropagation-free PTQ methods; however, their performance is somewhat limited by their lack of consideration of inter-layer dependencies.
In this paper, we thus propose a novel PTQ algorithm that considers inter-layer dependencies without relying on backpropagation. 
The fundamental concept involved is the development of attention-aware Hessian matrices, which facilitates the consideration of inter-layer dependencies within the attention module.
Extensive experiments demonstrate that the proposed algorithm significantly outperforms conventional PTQ methods, particularly for low bit-widths.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel post-training quantization (PTQ) method, termed BOA (Backpropagation-free Optimization for Attention-aware PTQ), targeting large language models (LLMs) without relying on backpropagation. The approach introduces attention-aware Hessian matrices that capture inter-layer dependencies within the attention module, aiming to improve quantization accuracy, especially at low bit-widths (e.g., INT2). BOA incorporates techniques like Hessian relaxation and efficient computation of inverse Hessians to mitigate the high computational costs. The method is benchmarked against existing PTQ approaches on LLMs, demonstrating improved performance in terms of perplexity and zero-shot task accuracy.

### Strengths
1. The proposed BOA consider inter-layer dependencies within the attention module when optimize a weight-rounding mechanism. It is beneficial to maintain higher quantization accuracy, especially at low-bit precision.

2. The proposed BOA method demonstrates impressive results, especially in the low-bit regime (e.g., INT2 quantization).

3. The paper includes extensive experiments across multiple model types and sizes, demonstrating  scalability across LLMs of different parameter counts.

### Weaknesses
1. Novelty Limitations: The primary contribution, the attention-aware Hessian matrix, is an incremental improvement over existing Hessian-based PTQ methods. While capturing inter-layer dependencies within the attention module is beneficial, the idea is not a novel quantization paradigm. 

2. The authors introduce optimizations approaches like Hessian relaxation and efficient computation of inverse Hessians, but the results did not show the effect of these optimization methods.

### Questions
Refer to 2 in weakness. What is the effectiveness of proposed approaches in terms of efficiency?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduced the BOA post-training quantization algorithm designed for LLMs that overcomes the limitations of traditional quantization methods, which struggle with inter-layer dependencies and backpropagation requirements in LLMs. BOA leveraged attention-aware Hessian matrices to better capture inter-layer interactions within the attention module, enhancing performance, especially at low bit-widths. The algorithm employed Hessian relaxation and head-wise simultaneous quantization, to attempt to reduce computational and memory costs, making it feasible for quantizing LLMs without backpropagation.

### Strengths
The topic of this paper is of significant importance and represents one of the most active and rapidly evolving research areas in the field. As LLMs grow increasingly complex, their deployment on resource-constrained devices requires innovative solutions to reduce computational and memory demands. Quantization, as a compression technique, has gained considerable traction for enabling efficient deployment of LLMs without sacrificing model accuracy.

### Weaknesses
The technical approach of this paper is relatively straightforward, lacking intricate or highly novel methodologies. Additionally, certain English terminology within the paper is used imprecisely, which may affect clarity and readability. The comparison methods are somewhat limited, providing a narrow benchmark for evaluating the proposed technique. Moreover, while the experimental results demonstrate some improvements, the advantage over existing methods is not substantial, suggesting the need for further validation, such as, SmoothQuant, LLMC,QuIP etc.

### Questions
The advantage over existing methods is not substantial, suggesting the need for further validation, such as, SmoothQuant, LLMC,QuIP etc.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a post-training quantization method called BOA that incorporates inter-layer dependencies without relying on backpropagation. BOA leverages attention-aware Hessian matrices to capture dependencies within the attention module, a relatively rare approach in existing PTQ methods. Additionally, BOA demonstrates compatibility with techniques like SmoothQuant and Z-FOLD, allowing for further enhancements in quantization performance. However, despite these strengths, BOA does not show sufficient memory and processing time benefits compared to existing PTQ methods. The experiments are conducted on outdated models, and the comparison methods lack recent advancements. Adding more experiments with up-to-date models and techniques would strengthen the paper.

### Strengths
1.	The paper introduces an innovative PTQ method that cleverly captures inter-layer dependencies within attention modules through attention-aware Hessian matrices while avoiding backpropagation overhead. 
2.	BOA is compatible with other techniques, such as SmoothQuant and Z-FOLD, enabling further improvements in quantization accuracy by integrating different quantization strategies.

### Weaknesses
1.	The experiments are primarily conducted on BLOOM, LLaMA1, and OPT models, which are somewhat outdated compared to current state-of-the-art models. The paper lacks validation on more recent models, such as the LLaMA3 series.
2.	Although the paper introduces various techniques to reduce computational overhead and claims to use a Hessian-based strategy to avoid time-consuming gradient-based optimization, as shown in Table 13, BOA’s actual overhead in terms of memory and processing time is greater than GPTQ. Additionally, in Tables 3, 4, and 5, even under 2-bit quantization, BOA's improvement over GPTQ is marginal. For Table 6, it’s worth noting that GPTQ can also integrate certain quantization algorithms, like QuaRot [1] and SpinQuant [2], to achieve better results. Including comparisons with these methods is recommended.	

### Questions
1.How does the performance of BOA compare when tested on more advanced models, such as the LLaMA3 series, instead of the relatively outdated models used in the paper?
2.How does BOA's accuracy compare to more recent quantization methods, such as QuaRot and SpinQuant?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a training-free post-training quantization method based on GPTQ. It introduces inter-layer interaction by calculating Hessian matrices using an attention module instead of a simple linear module in LLMs. Additionally, the paper proposes techniques to improve the efficiency of Hessian matrix calculations.

### Strengths
1. Introducing inter-layer interaction in a training-free manner is innovative.
2. The paper is well-written.

### Weaknesses
1. The experimental setup is somewhat outdated. Additional experiments on newer models, such as LLama-2 and LLama-3, are needed.
2. Although the paper introduces a training-free PTQ method, it may be slower than training-based methods. For example, Table 2 shows that BOA takes 1 hour to quantize 2.7B models, while GPTQ quantizes larger 13B models in only 21 minutes. OmniQuant, a training-based method, requires only ~1.1 hours for 7B models. The paper should provide comprehensive comparisons of quantization times to demonstrate the proposed method's effectiveness.
3. The paper focuses on 2-bit per-channel quantization and mentions that "group-wise parameters result in additional memory costs and processing time during inference." However, weight-only quantization aims to alleviate memory constraints during the decoding stage. Group-wise quantization introduces negligible overhead but significantly improves performance and is a common practice in existing inference engines. Therefore, the paper should include results for group-wise quantization.

### Questions
Please refer weaknesses for details.

### Soundness
3

### Presentation
2

### Contribution
2
