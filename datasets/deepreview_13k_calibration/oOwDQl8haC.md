# Towards Cheaper Inference in Deep Networks with Lower Bit-Width Accumulators

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
The majority of the research on the quantization of Deep Neural Networks (DNNs) is focused on reducing the precision of tensors visible by high-level frameworks (e.g., weights, activations, and gradients). However, current hardware still relies on high-accuracy core operations. Most significant is the operation of accumulating products. This high-precision accumulation operation is gradually becoming the main computational bottleneck. This is because, so far, the usage of low-precision accumulators led to a significant degradation in performance. In this work, we present a simple method to train and fine-tune high-end DNNs, to allow, for the first time, utilization of cheaper, $12$-bits accumulators, with no significant degradation in accuracy. Lastly, we show that as we decrease the accumulation precision further, using fine-grained gradient approximations can improve the DNN accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces an innovative approach to fine-tune the process of quantized accumulation by disregarding underflow effects, thereby simplifying the rounding process to a simple floor operation during low-precision accumulation. Employing this technique, deep learning inference with 12-bit floating-point accumulation maintains the same as FP32 accumulation on the ImageNet dataset. Additionally, the paper suggests a methodology for quantized backpropagation across the entire accumulation, demonstrating promising results with 8-bit floating-point accumulation on smaller datasets, such as MNIST.

### Strengths
1- The paper is well-written and well-organized

2- The efficacy of the methods presented in the paper is substantiated through experimental results using BERT models on the SQuAD benchmark and ResNet models on ImageNet. 

3- The backpropagation through the entire quantized accumulation is unique and has not been studied before.

### Weaknesses
1- It is recommended that the paper include a comparison of the computational complexity of MAC operations between the proposed method and the previous works [1,2,3]. Additionally, the author suggested discussing the quantization overhead associated with the new approach in comparison to [1,2,3].

2- The impact of chunk size requires further exploration to determine if reducing the chunk size also diminishes the bit size.

### Questions
Can the distribution of the accumulations (which might follow a normal or other distribution) affect the performance of the quantization approach?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In addition to low-precision inputs to a matmul, this paper proposes to use low-bitwidth accumulators (LBA) to compute the dot product. Experiments show that 12-bit LBA in the forward pass is promising for both ResNet and BERT, requiring only several epochs of finetuing. LBA for training is more difficult.

### Strengths
1. Reducing the accumulator bitwidth is a practical way of further reducing the cost of a low-precision matmul.

2. The experimental design in the main experiments in Section 3.1 is straightforward and seems to be easy to reproduce (if the CUDA kernel is open sourced).

### Weaknesses
1. The paper needs to provide more context on related works. For example, what is the key difference between the proposed method and the prior work Wrapnet? Is it training vs. non-training?

2. There is a lack of evaluation or estimation on the hardware benefits of the proposed method. What will be the gate count/computational energy/latency improvement if using 12-bit accumulators compared to FP16/BF16 accumulators?

3. Low-bitwidth accumulator under the context of integer quantization is not explored in the main experiments. Integer quantization is mentioned in Section 2.2 when introducing fixed-point quantization, but it seems to be disconnected from the rest of the evaluation.

### Questions
Questions are included in the weakness section.

### Soundness
2 fair

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
This paper explores how to reduce computing resource by quantize and reducing the bit width of neural network computing accumulators. Unlike most other works that mainly focus on the multiplier part of low bit width, this paper believes that the overhead of the accumulator cannot be ignored. Therefore, through optimization on floating-point representation, the ResNet series models can achieve fine-tuning and inference for the first time with a lower 12 bit width accumulator, without significant degradation in accuracy. This paper also explores the training methods for lower bit width scenarios, including adjusting the design selection of the backpropagation straight through estimator.

### Strengths
1. Quantization optimization of accumulators is an interesting viewpoint, as it has not been given sufficient attention.

2. The method proposed in this paper has certain reference significance for the design of floating-point accumulators in deep learning accelerators.

3. The discuss of STE used in section 4 seems to be a new and original study, can achieve better results in backpropagation of accumulated errors.

### Weaknesses
1. The method proposed in this paper is difficult to be applied to accelerate real-world low bit width neural networks. Although this paper claims that an accumulator with a low bit width of 12 bits FP can be implemented with cheaper hardware, standard hardware typically only provides floating-point bit widths of 8 bits, 16 bits, and 32 bits. Implementing such acceleration requires specialized hardware design, which requires more collaborative design and additional costs. The optimization of low bit floating-point accumulators under the same cost, as well as the accuracy that can be achieved by fixed-point quantization models with the same hardware cost, remains to be discussed. Specifically, the paper does not address the practical challenges of integrating a non-standard 12-bit floating-point accumulator into existing hardware ecosystems. The lack of readily available hardware support for this format necessitates custom hardware design, potentially negating the claimed cost benefits due to the overhead of specialized fabrication and integration. Furthermore, a comparison with fixed-point quantization methods, which are more commonly supported in hardware, is essential to justify the choice of a floating-point approach with a non-standard bit-width. The paper should provide a more detailed analysis of the trade-offs between the proposed method and existing fixed-point quantization techniques, considering both hardware cost and achievable accuracy. 

2. This paper lacks accurate evaluation and theoretical analysis of the error and accuracy requirements of floating-point models. Although Table 1 in Paper categorizes the errors in several cases of floating-point quantization, and Figure 2 shows several cases of errors, it is still not possible to quantitatively evaluate the impact of low bit width floating-point accumulation on model inference errors. It is difficult to make people believe with certainty the scalability and reliability of this scheme. Also, in the last paragraph before section 3.1, the author chooses b_acc=b_prod-1/2 log_2(chunk size) as an offset does not seem to guarantee that overflow will not occur under any condition. The paper needs to provide a more rigorous theoretical framework for understanding how the reduced bit-width of the accumulator affects the overall error accumulation during inference. The current analysis is insufficient to establish the reliability of the proposed method, especially under different network architectures and input distributions. The choice of the exponent bias offset, while seemingly intuitive, lacks a formal justification and does not guarantee overflow prevention under all circumstances. A more detailed analysis of the error propagation and the selection of appropriate bias values is needed to ensure the robustness of the approach.

3. The content of this paper only includes an evaluation of the model accuracy and does not discuss or analyze the actual cost. For example, regarding the estimation of multiplier and accumulators’ power and silicon area, how much performance improvement or resource savings can be achieved through the optimization proposed in this paper. It is interesting to discuss the benefits of these optimizations in the context of the additional accuracy loss and design complexity required by the methods presented in this paper. The paper should include a detailed hardware analysis that quantifies the power consumption, area, and latency of the proposed accumulator design compared to standard floating-point implementations. This analysis should consider the overhead of the additional logic required for the proposed quantization scheme, as well as the potential benefits in terms of reduced memory bandwidth and computational complexity. Without a concrete hardware evaluation, it is difficult to assess the practical value of the proposed method, especially when considering the trade-offs between accuracy, performance, and hardware cost.

### Questions
1. In section 3.1, a two-staged fine-tuning is proposed, what are the references for selecting hyperparameters here(e.g, 10 epochs, learning rate)?
2. In section 4, one method is using STE as recursive way on FMA. This seems to require all FMA operations to be unfolded in sequence. As far as I know, the FMA gradient of deep learning training seems to be treated equally, otherwise it will seriously affect efficiency and be unreality. This is because GEMM is a highly optimized parallel operation, and additional branches are not suitable for use here.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies quantization errors occurring in the accumulation phase of dot products. While many works have studied representation quantization in the past, the problem of accumulation rounding has largely been overlooked. Yet, others (Higham'83 & Sakr'19) who have studied this problem, have often focused on the problem of swamping, which causes an underflow in one of the two summands. In contrast, this work looks at the problem of overflow that occurs during large summations, when employing relatively low precision accumulators, e.g., FP16. Modeling accumulation as a sum of iid random variables, and invoking the central limit theorem, this paper formulates a prediction method for when such overflows can occur, and as a remedy, applies a scaling factor the the chunked summation to try and suppress the damage of said overflows. Extensive empirical results on several benchmarks are provided.

### Strengths
-- Good problem to tackle, rounding effects in accumulators are largely overlooked in a community that puts a lot of emphasis on using quantization to lower the cost of implementation.

-- Good presentation. Following concepts related to the accumulation occurring in a GEMM is often hard, due to the complexities of tensor cores and similar hardware used for DL inference and training. But the others do a good job pinpointing the problem.

-- Solid empirical results on a diverse set of benchmarks such as vision and language models.

### Weaknesses
 -- The proposed solution described in Section 3 is too qualitative. For instance, the underflow region is described as a "hard" region to "escape" from. Can the "escape" and "hardness" be presented in a mathematical manner? Specifically, the paper should define what constitutes an underflow region in the context of the accumulator's bit-width and dynamic range. Furthermore, the notion of "escaping" should be formalized, perhaps by analyzing the probability of a weight moving out of this region given the stochastic nature of gradient updates. Similar for later description of parameters being "stuck" and so on. A more rigorous treatment of these concepts is needed to fully understand the limitations of the proposed method.

-- The method only applies to feedforward, what about accumulations occurring in the GEMMs of back-propagation? The paper should acknowledge that the proposed method is limited to forward propagation and discuss the challenges of extending it to backpropagation, where gradients are also accumulated. The accumulation of gradients during backpropagation is equally important and can also suffer from quantization errors. The paper should at least discuss the potential difficulties and future research directions in this area.

-- Benchmarks employed are diverse, but relatively simple (ResNets and Berts). can the empirical results be augmented with Transformer models, such as GPTs? While the benchmarks include vision and language models, they are relatively small compared to state-of-the-art models. The paper should include experiments on larger and more complex models, such as large language models (LLMs) like the GPT family, to demonstrate the effectiveness of the proposed method on more challenging tasks. This would provide a more comprehensive evaluation of the method's generalizability and practical applicability.

### Questions
Please address the above questions. Furthermore, I am also curious if we can analyze if overflows can be allowed in a controlled manner such as to lower complexity further but maintain accuracy. Indeed, overflowing is essentially related to magnitude clipping. Recent works [1] have shown that clipping, if done properly, can significant improve the quality of quantization. Is this something we can investigate for this work?

[1] Sakr, Charbel, et al. "Optimal clipping and magnitude-aware differentiation for improved quantization-aware training." International Conference on Machine Learning. PMLR, 2022.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
