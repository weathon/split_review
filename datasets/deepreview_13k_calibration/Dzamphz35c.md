# Ultra-Low Accumulation Precision Inference with Block Floating Point Arithmetic

- Decision: Reject
- Avg Score: 3.75
- Scores: 1, 6, 5, 3

## Abstract
Block Floating Point (BFP) quantization offers a hardware-efficient numerical range trade-off. Previous studies have quantized weights and activations to an extremely low precision using the BFP arithmetic. However, as the precision of weights and activations is reduced, we have identified that accumulation becomes a hardware bottleneck in the BFP MAC. Nevertheless, existing attempts to decrease the precision of accumulation in matrix multiplication have generally preserved model performance through training with a pre-selected, fixed accumulation precision. Nonetheless, selecting an unduly low precision leads to notable performance degradation, and these studies lack an effective approach to establish the lower precision limit, potentially incurring considerable training costs. Hence, we propose a statistical method to analyze the impact of reduced accumulation precision on the inference of deep learning applications. Due to the presence of fixed-point accumulation and floating-point accumulation in BFP matrix multiplication, we have formulated a set of equations to relate the data range of fixed-point multiply-accumulate operations and the effects of floating-point swamping to the parameters of BFP quantization, the length of accumulation, model weights, and the minimum number of bits required for accumulation, thereby determining the appropriate accumulation precision. Applied to MMLU Llama2-7B, SQuAD-v1.1 BERT-Large and BERT-Base and CIFAR-10 ResNet-50, our precision settings yield performance close to the FP32 baseline. Meanwhile, further precision reduction degrades performance, indicating our approach’s proximity to precision limits. Guided by our equations, the hardware exhibited a 13.7\%-28.7\% enhancement in area and power efficiency over high-precision accumulation under identical quantization configuration, and it demonstrated a $10.3\times$ area reduction and an $11.0\times$ power reduction compared to traditional BFP16 implementations.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper investigates the impact of accumulator precision in BFP (Block Floating Point) hardware on the accuracy of neural networks. It provides separate analyses for the two types of accumulators in BFP hardware: intra-block and inter-block accumulators. Based on this accuracy analysis, the authors reduced the precision of BFP hardware, resulting in improvements in area and power efficiency.

### Strengths
Although the motivation behind this work is interesting and valid, the paper lacks sufficient detail and evaluation, making it difficult to clearly identify its strengths at this stage.

### Weaknesses
1.	The paper does not specify the format used for low-precision floating-point numbers. While FP32 is a well-known format with 1-bit sign, 8-bit exponent, and 23-bit significand, there is no standard format for floating-point numbers with fewer than 16 bits. For instance, FP8 can have either a 4-bit exponent and 3-bit significand or a 5-bit exponent and 2-bit significand. This paper does not clarify the specific format used for low-precision FP numbers.
2.	There is a lack of detail on the hardware implementation. The paper does not describe the hardware architecture considered, nor does it specify the bitwidth of the accumulators in both the proposed approach and the baseline.
3.	Although the paper provides an analytical approach to analyze the distribution of partial sums in Sections 4.1 and 4.2, there is no clear connection between this analysis and the optimization of accumulator bitwidth. Based on the results in Table 3 and Figure 5, and the fact that the impact of accumulator bitwidth varies across networks, the optimization of bitwidth appears to be empirical rather than directly derived from the analysis in Sections 4.1 and 4.2.
4.	The explanations and definitions of several terms used in the paper remain unclear and insufficiently detailed. This lack of clarity makes it difficult to fully understand the methodology and its implications.
5.	I do not see the value or novelty of the proposed intra-block partial sum analysis and FnRR-based analysis. Both approaches utilize statistical properties of the layers, but the paper does not explain how these analyses offer any significant advantage over simpler and widely adopted methods such as min/max or 3-sigma-based truncation.
6.	The paper lacks a robust theoretical foundation to demonstrate how the proposed approach preserves accuracy. Despite this, it claims that the inter-block accumulation precision can be reduced to a bitwidth of 2–3 for BFP8 Seg (Table 3). This reduction seems overly aggressive and raises concerns about whether the baseline FP32 precision used in the comparisons is unnecessarily high, potentially skewing the evaluation.
7.	Figure 5 still lacks proper line descriptions, making it difficult to interpret the data presented.

### Questions
1.	I suggest that the authors provide details on the low-precision floating-point formats used in this study.
2.	I recommend that the authors include more detailed information about the hardware implementation. For example, please provide a block diagram of the hardware and specify the bitwidth used for each component.
3.	In Equation (2), you mention that the range of partial sums depends on $2^{A_{width}}$ and $2^{W_{width}}$. However, it’s unclear whether the bitwidth refers to the exponent or mantissa, and it doesn’t specify whether it pertains to inter-block or intra-block partial sums, or the final accumulation results of the layer. If it refers to intra-block partial sums (as BFP only handles integer terms within the block), I believe the maximum bitwidth of the partial sum should be $log(k) + A_{width} + W_{width}$. Please clarify how you derived the term in Equation (2).
4.	In Section 4.1, what is the difference between $I_e$/$W_e$ and I/W? These terms are not clearly defined, making it difficult to follow the equations in this section.
5.	Please clearly label the x and y axes in Figure 5 for better interpretation.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Block Floating Point (BFP) quantization is introduced to improve the hardware efficiency in deep learning, but its accumulation logic becomes the hardware bottleneck especially for low-bit BFP quantization. This work studies the effect of reduced accumulation precision in BFP quantization and proposes a statistical  method to determine the appropriate accumulation precision. Experiments on Llama2-7B, BERT and ResNet-50 show that proposed approach can save 13%-28% area and reduce 13%-25% power while maintaining the model performance close to FP32 baseline.

### Strengths
+ This work presents a theoretical framework for analyzing the effect of accumulation precision in quantized GEMM, especially taking both data statistics and floating-point swapping into consideration. This provides a solid foundation for further research on quantization and its hardware design.
+ This work validates the proposed approach across different models and demonstrates the actual hardware benefits including area and power savings with a complete synthesized design.

### Weaknesses
 - The proposed method relates the accumulation precision with the data range of actual workload, and thus predicts different accumulation precisions for different models. However, in real world, it is more common to run different models on the same hardware and thus it seems there is no need to specialize accumulation precision settings in hardware. Furthermore, if the hardware will be used for model training, the accumulation should also be able to handle the data range of model training, which is much larger than the inference. Therefore, it is doubtful if the proposed method is practical in the real world hardware design scenario.

### Questions
My questions are listed in the weakness section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to reduce the accumulator precision of the low-bit hardware matmul units where the accumulator becomes the hardware bottleneck. Based on the assumption that the inputs follow Laplace distribution, the paper analyzes the mean and variance for block floating-point format and proposes to use the mean with 3 standard deviations as the approximation of the largest magnitude that the accumulator should support, thus trimming down the accumulator precision. Experiments on ResNet 50, Bert-large, and llama2-7b shows the precision prediction fits well with the actual mininumal bits needed.

### Strengths
The paper shows clearly how the target of improvement and the bottleneck of accumulator in hardware in Figure 1, although more detailed description of the setup and source of the numbers shown in Figure 1(b) will be appreciated. The paper also clearly described its strategy, which is using the three standard deviations to estimate the largest output magnitude of the accumulator.

### Weaknesses
The main concern is on the experiments. Line 385 to 388 indicates that the evaluation mixes inference-only evaluation and training. It is very likely that the accumulator precision required in those two cases are very different. The accumulator precision for training can potentially be lower than inference-only approximation because overflow can serve as clipping, and model can still recover some quality through training. These two setups need to be separated and ablated.

In addition, Figure 5 is important as it shows how close the theoretical prediction matches the lower bound of the bitwidth needed for the accumulator in practice. However it is unclear in Figure 5 what the floating-point baseline is (dashed lines?). It is also unclear what the block size is. These are critical for assessing the experimental results.

### Questions
The questions are in the weakness section.

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
2

### Summary
In the block floating point quantization, this paper proposes a statistical method to analyze the impact of reduced accumulation
precision on the inference of deep learning applications,
where formulates a set of equations to relate the data range of fixed-point
multiply-accumulate operations and the effects of floating-point swamping.
The experimental results show that area costs and hardware efficiency can be achieved, 
demonstrating significant area reduction and power reduction.

### Strengths
This paper shows a contribution of arithmetic for low-cost inference.

### Weaknesses
Although this paper shows a contribution of arithmetic for low-cost inference, 
I have several serious concerns as:

1. The main idea is not explicitly shown. I think that a metric FnRR denotes the ratio of floating point swamping. 
The main idea should be focused on introduction and Figure 1, where the main idea or metric is not illustrated. In the proof of Eq. (7), the normalized values based on assumption 1 in B. Proof of Theorem 1 are considered. In the distributions of weights and activation, the assumption 1 is questionable. Specifically, the assumption of a symmetric distribution centered around zero for weights and activations may not hold in practice, especially after ReLU activations or batch normalization layers, which can introduce significant skew. The paper needs to provide a more robust justification for this assumption or explore alternative approaches that do not rely on such a strong condition. If there are any references for that, it could be better.

2. It is hard to understand this paper. Many italic and non-italic terms are mixed. For example, italic n and nonltalic n are used without discrimination. Are sigma (line 316) and symbol sigma the same? Besides, too many other typos are shown. For example, the inconsistent use of symbols and the lack of clear definitions for key terms make it difficult to follow the mathematical derivations. In Figure 5, do terms in Y axis mean the accuracy on datasets? What is the meaning of scores? The lack of clear axis labels and a detailed explanation of the performance metric makes it difficult to interpret the results.

3. The metric is only applied to inference. I think that this method can be evaluated on any training works. 
I think that in the model for image classification, the proposed idea can be applicable to the model training. (ResNet 18 on CIFAR10 or ResNet50 on ImageNet-1K) Specifically, the paper should investigate the impact of the proposed quantization method on the backpropagation process and the convergence of the training algorithm. Besides, I think that resnet50 on CIFAR10 is not suitable for the job using floating-point format. The choice of ResNet50 on CIFAR10 seems inappropriate given the relatively small size of the dataset and the potential for overfitting. The paper should justify this choice or consider more appropriate benchmarks.

4. In hardware implementation, what is the environments for hardware synthesis? The paper lacks details on the hardware synthesis environment, including the specific tools, libraries, and target technology used. This information is crucial for reproducibility and for assessing the practical relevance of the results. Without these details, it is difficult to evaluate the claimed area and power reductions.

### Questions
Please, see the above weakness.

### Soundness
2

### Presentation
1

### Contribution
1
