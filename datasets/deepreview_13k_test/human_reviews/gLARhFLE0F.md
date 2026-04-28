# LUT-GEMM: Quantized Matrix Multiplication based on LUTs for Efficient Inference in Large-Scale Generative Language Models

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Recent advances in self-supervised learning and the Transformer architecture have significantly improved natural language processing (NLP), achieving remarkably low perplexity.
However, the growing size of NLP models introduces a memory wall problem during the generation phase.
To mitigate this issue, recent efforts have focused on quantizing model weights to sub-4-bit precision while preserving full precision for activations, resulting in practical speed-ups during inference on a single GPU.
However, these improvements primarily stem from reduced memory movement, which necessitates a resource-intensive dequantization process rather than actual computational reduction.
In this paper, we introduce LUT-GEMM, an efficient kernel for quantized matrix multiplication, which not only eliminates the resource-intensive dequantization process but also reduces computational costs compared to previous kernels for weight-only quantization.
Furthermore, we proposed group-wise quantization to offer a flexible trade-off between compression ratio and accuracy.
The impact of LUT-GEMM is facilitated by implementing high compression ratios through low-bit quantization and efficient LUT-based operations.
We show experimentally that when applied to the OPT-175B model with 3-bit quantization, LUT-GEMM substantially accelerates token generation latency, achieving a remarkable 2.1$\times$ improvement on a single GPU when compared to OPTQ, which relies on the costly dequantization process

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Binary Code Quantization (BCQ) applied to large language model weights by LUT-GEMM marks an innovative step, where weight decomposition into quantized matrices and scaling factors is an offline process. This offers a flexibility to balance between compression and accuracy by varying group sizes and quantization bits. At execution time, activations are split into sub-vectors with corresponding look-up tables for sub-sum calculations, replacing the typical multiply-accumulate operations. This "multiplication" of binary matrices with activations, followed by scaling, optimizes the model's runtime efficiency. UT-GEMM's application on well-known models, including GPT-3, illustrates significant enhancements in performance, memory usage, energy consumption, and a reduction in necessary GPUs.

### Strengths
Extensive empirical evidence presented through various data visualizations confirms the efficiency of LUT-GEMM method.

The research goes further than most in addressing the real-world deployment challenges on standard hardware, which is a standout feature.

Impressive experiment section focusing on the largest open-source models and fitting them onto a single GPU.

Detailed latency insights provided in the paper lay a solid foundation for understanding the efficiency gains.

Well-written motivation and related work sections. Discussions show a deep understanding of GPU programming.

### Weaknesses
The achievement of deploying huge models on a singular GPU is undermined by the lack of reported accuracy metrics at this scale.

The paper lacks a direct accuracy and latency comparison among different models, although the OPT model family is a good choice. 

The paper does seem to have some limited technical novelty since it adapts and extends prior method in minor to moderate ways, but the analysis and implementation seem to make up for it.

### Questions
How can the method be extended to larger batches or scenarios when multiple single requests are batched into one?

Is the ability to represent uniform quantization that important in this method? Uniform methods are typically strictly worse as they over-allocate precision to the edges of the distribution.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to replace FP16 GEMM calls in weight-only-quantization neural network inference with look-up-table-based GEMMs. The proposed technique is designed to help scenarios where the bit width of weight-only-quantization is 4 or less and the weight matrix size is large enough, as is the case for large language models. The core idea is that, when the bit width of weights is low, one can pre-compute multiplication results with the activation tensor for all combinations and store them, and hence most of the multiplications are replace by table look up; the amount of sum operations remain about the same; the amount of memory reads remain about the same. Experimental results include kernel-level latency comparison in Table 2 and end-to-end latency comparison on OPT in Tables 3-5. Source code is included in the supplementary.

### Strengths
The core idea of the paper makes sense and in fact is more general and beyond the BCQ format used this paper. The key question on rating the originality is the relation to prior works. For example, how does this work relates to BiQGEMM (Jeon et al., 2020)? Section 3.1 does acknowledge this and a few other prior works but it's unclear what are the distinctions. If a satisfactory answer could be provided, then originality could be a big strength for this paper.

The experimental setup is good, particularly that perplexity test is included.

Including source code is a big plus, although I have not verified it.

### Weaknesses
As said above, the originality question is the key. Please provide detailed narrative on the differentiation. Including prior kernels in evaluations would be even stronger.

The last row of Table 2 suggests 4X speed up with 4-bit quantization at kernel level. However this does not seems to translate to the 4-bit end2end latency in Tables 3 and 4, not anywhere close to 4X. Can you explain why?

A critical property of the proposal is that the benefit gets larger as the matrix dimension increases. Right now the results only show end2end latency for OPT 66B and 175B. Could you add a plot of latency as a function of OPT model sizes, all the way from the smallest to 175B?

### Questions
Please see the weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an quantization optimization method for Transformer-like model on GEMM calculation, which uses integer weight quantization and floating-point activation values, and uses a lookup table computation scheme to achieve inference acceleration. The paper provides specific GPU implementation methods and performance analysis, explains the implementation methods of uniform quantization and non-uniform quantization in this scheme. In the experimental section, the author compared with the basic cuBLAS implementation, and the results showed that the proposed method has much better performance and does not cause significant loss of inference accuracy.

### Strengths
1. The work of this paper is of great significance, especially for optimizing the inference performance of LLM, which is currently highly concerned. Compared to the baseline cuBLAS implementation, the performance of this method has significantly improved.
2. The design, experiment, and analysis of this paper are relatively solid. For the algorithm design of GPU, this paper provides detailed explanations and time complexity analysis. This paper carefully considers the performance of different compression ratios under different bit and grouping parameters g. 
3. CUDA kernel code and performance test code is provided.

### Weaknesses
1. The novelty of this paper is ordinary. The main parts, including BCQ quantification and group-wise quantization optimization, both come from existing research. This paper proposes to convert uniform quantization into BCQ format, which is not a complex transformation. 
2. The author mentioned that the optimization here currently only focuses on the inference of a single batch, which may limit its use. 
3. The LUT-Based method requires a significant amount of memory capacity in exchange for efficiency. In Table 2, the 4-bit quantified LUT-GEMM storage footprint exceeds the 16 bit model of the cuBLAS baseline. In fact, storage resources are also the main focus of quantization in large language models, not just performance. This paper seems to focus mainly on computational efficiency, but lacks a comparison between memory resource usage. 
4. The experimental data in this paper is not enough, and the main baseline for comparison is 16 bit cuBLAS, lacking a comprehensive comparison of other quantization methods. The experiment only tested the quantization accuracy of PPL indicators using the OPT model on the LAMBADA dataset, which cannot fully demonstrate the effectiveness and universality of the method.

### Questions
1. The speed of inference is important, but it is only one part. I hope the author can compare the advantages and disadvantages of other quantization acceleration methods, including compression ratio of GPU memory requirements, the need for post training calibration, etc. 
2. The author claims that the BCQ quantization used is suitable for both uniform and non uniform quantization, but the experiment only considered uniform quantization. Theoretically, non-uniform quantization has better representation ability to achieve higher accuracy. Although testing the performance of non-uniform quantization may be difficult on current hardware, it is still possible to compare the accuracy differences between the two methods.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an interesting post-training quantization method, without needing to dequantize the integer back to FP16. In particular, they leverage binary coding quantization (BCQ) to represent the LLM weights in both uniform and non-uniform fashion, resulting in a set of scaling factor matrices A and binary weight matrices B of +1 or -1. Therefore, the multiplication between weights W and activations X will become A(BX), where BX is composed of repetitive additions with partial sums being stored on the buffer as LUT to accelerate the computation.

The author also provides a customized CUDA kernel to deploy such LUT-based GEMM on GPUs, achieving a 2.1× improvement on a single GPU when compared to OPTQ using OPT-175B models with 3-bit weight-only quantization.

### Strengths
1. Clear ideas and descriptions of representing weights with scaling factor matrices and binary weight matrices. The advantage of using LUT and grouped scaling factors is extensively evaluated. The way of leveraging fine-grained scaling factors enabled a non-uniform quantization format.

2. Solid implementation. The analysis and GPU implementation stand this idea out. I understand the importance of having it work on GPUs but I still wonder how efficient is the implemented kernel as compared to the customized hardware accelerator.

3. Plausible ablation studies. There are a lot of ablation studies to show the effectiveness of every proposed component.

### Weaknesses
One big issue in writing that prevents one from reimplementing the proposed method is how to construct the binary matrices and scaling factor matrices from the pre-trained weights. The attached code assumes randomized matrices so that part cannot provide any useful information regarding this.

For more technical questions:

1. Regarding the LUT part, what is the repetition that we can exploit form? The quantitative measurements or ablation studies on this will provide more insights into how many benefits we can get for such LUT-based GEMM instead of vanilla additions. Any theoretical analysis on the upper bound of savings brought from LUT?

2. Regarding the scaling factor part, how to determine the group size? In my understanding, if the group size is small, there are no benefits as you have as many matrices as used bits to represent weights. At what group size, do the benefits compensate the cost of the scaling factor matrices? Is there any formula to calculate this?

3. Regarding the experiments, why only consider the OPT model? How about the speedups on other candidates like LLaMa at different scales? In that way, we can also understand the scalability of the used kernel better.

### Questions
See weaknesses.

In addition, the authors did not clearly describe how you derive the scaling factors matrices and binary matrices from the pre-trained weights. I think that part is necessary and it will be better if there is any theoretical analysis of the quantization error or variance.

I am open to raising the score depending on the good answers.

--
Update: Thank you for the comprehensive response. Many of my concerns have been resolved, and I've increased the rating score.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
