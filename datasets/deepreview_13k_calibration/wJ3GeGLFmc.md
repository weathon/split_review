# Towards Accurate and Efficient Sub-8-Bit Integer Training

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Neural network training is a memory- and compute-intensive task. Quantization, which enables low-bitwidth formats in training, can significantly mitigate the workload. To reduce quantization error, recent methods have developed new data formats and additional pre-processing operations on quantizers. However, it remains quite challenging to achieve high accuracy and efficiency simultaneously. In this paper, we explore sub-8-bit integer training from its essence of gradient descent optimization. Our integer training framework includes two components: ShiftQuant to realize accurate gradient estimation, and L1 normalization to smoothen the loss landscape. ShiftQuant attains performance that approaches the theoretical upper bound of group quantization. Furthermore, it liberates group quantization from inefficient memory rearrangement. The L1 normalization facilitates the implementation of fully quantized normalization layers with impressive convergence accuracy. Our method frees sub-8-bit integer training from pre-processing and supports general devices. This framework achieves negligible accuracy loss across various neural networks and tasks ($0.92\%$ on 4-bit ResNets, $0.61\%$ on 6-bit Transformers). The prototypical implementation of ShiftQuant achieves more than $1.85\times/15.3\%$ performance improvement on CPU/GPU compared to its FP16 counterparts, and $33.9\%$ resource consumption reduction on FPGA than the FP16 counterparts. The proposed fully-quantized L1 normalization layers achieve more than $35.54\%$ improvement in throughout on CPU compared to traditional L2 normalization layers. Moreover, theoretical analysis verifies the advancement of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an integer training framework that involves two main steps: grouping channels to minimize quantization errors and incorporating L1 normalization layers to stabilize the loss landscape. The method is targeted at sub-8-bit integer formats and reports significant performance gains on CPU, GPU, and FPGA when compared to FP16 baselines.

### Strengths
1. The paper addresses the challenging task of low-precision, end-to-end training for neural networks.
2. The approach is straightforward and easy to understand.
3. Evaluation results are provided for three different hardware platforms.

### Weaknesses
1. The description of “fully-quantized L1 normalization” lacks clarity. Is the approach intended to replace quantized L2 normalization with a quantized L1 version?
2. While ShiftQuant helps manage a wide gradient range and quantized L1 normalization enables fully quantized normalization layers, these contributions are complementary and show limited direct interaction.
3. The comparison between INT6 and FP16 matrix multiplication on FPGA appears biased. The baseline INT6 format can outperform FP16 in terms of latency, energy, and resource usage, as shown in Table 8. It seems misleading to attribute lower resource usage solely to the proposed method.

### Questions
1. See weaknesses above. 
2. The statement, “It is intuitive that smaller channels should be grouped separately from larger channels,” could be clearer. Does this refer to the distribution of outliers within channels?
3. The proposed channel grouping strategy resembles the channel permutations strategy for weights from Pool et al.'s “Channel Permutations for N: M Sparsity” (NeurIPS, 2021). Can re-grouping weights/activations/gradients be implied across the quantization literature?
4. A more detailed comparison of L1 normalization's performance across different architectures and bit-widths would better support its advantage over traditional L2 normalization in low-bitwidth training.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to use low-bitwidth integer to train neural networks. In order to achieve integer training with less quality regression, it proposes two methods: (1) an efficient regrouping of input channels to the matmul so that the outlier issue in quantization is less significant; (2) replace L2 norm when computing the standard deviation with L1 norm in the normalization layer. The experiments show that this work can train ResNet-50 on ImageNet using int4 with about 1.6% top-1 degradation and about 0.4 BLEU degradation when training Transformer on WMT14. The paper also presents the hardware throughput analysis of the proposed ShiftQuant matmul on both GPUs and FPGAs.

### Strengths
The paper studies integer training, which is an important topic on reducing both latency and power consumption of neural network training. The paper lists its major differences compared to previous works in Table 1, which helps readers. It also explains well how channel regrouping can help with quantization in Figure 2. Hardware analysis is always appreciated when proposing a kernal that has not yet existed in commercial accelerators.

### Weaknesses
1. It is not immediately clear how the ShiftQuant method applies to the matmul, even with the help of Figure 3. Regrouping channels without rearranging the data in memory can only work when the scaling factors are power-of-two as pow2 scaling factors are naturally discrete bins. The paper does not explain directly how the quantization scaling factors are computed. It instead uses "power-of-two grouping", which is misleading. The reader has to infer that the scaling factor is power-of-two.

2. The proposed ShiftQuant method seems not hardware-friendly. Regrouping without memory rearrangement means each element in a quantized dot product has a different scaling factor. To produce a correct output, the hardware matmul unit has to scale each element back before accumulation (step 2 in Figure 3c). In commercial hardware, e.g., GPUs, there is usually no access to the intermediate matmul outputs before accumulation. If building a customized hardware, one scaling factor per channel seems infeasible in terms of chip area and power, even if it is power-of-two.

3. It is not clear how the throughput analysis on GPU is obtained. Line 451 says the performance analysis in Figure 7 is for 6-bit ShiftMM kernel, but NVIDA RTX 3090 does not have 6-bit tensor cores as far as the reader understands.

### Questions
The questions are listed in the weakness section.

### Soundness
2

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
4

### Summary
Neural network training requires significant computational resources, and quantization helps reduce this burden by enabling low-bitwidth formats. This paper presents a framework for sub-8-bit integer training that includes two main components: ShiftQuant and L1 normalization. ShiftQuant minimizes quantization errors through effective channel grouping and avoids inefficient memory rearrangement. The L1 normalization improves the loss landscape by enhancing convergence accuracy while requiring less computation than traditional methods. Experimental results demonstrate that this approach maintains high accuracy across various neural networks, with performance improvements on both CPU and FPGA platforms.

### Strengths
1.	The paper is relevant to the community.
2.	The tackled problem is useful to improve the efficiency of DNN training.

### Weaknesses
1.	In Section 1: “Our prototypical implementation of ShiftQuant achieves more than 1:85 × /15:3% performance improvement on CPU (ARMv8)/GPU (Nvidia RTX 3090) compared to Pytorch.fp16, and more than 33:9% resource consumption reduction on FPGA (ZC706) compared to FP16.” The comparison with FP16 is not very significant since FP16 is obviously more resource-hungry. It is recommended to compare the proposed method with other existing quantized approaches. Please include comparisons against the current best-performing approaches for sub-8-bit training.
2.	The proposed method should be discussed in more detail through a detailed top-level algorithm describing all the operations involved. Please add the pseudocode description of the ShiftQuant algorithm and L1 normalization procedure. Please distinguish clearly between what is novel and what is implemented based on existing methods. It is recommended to add a table that clearly delineates the novel components from existing methods, and suggests specific design decisions you'd like to see explained, such as the rationale behind the power-of-two grouping strategy or the choice of L1 over other normalization approaches.
3.	The experimental setup and tool flow used to conduct the experiments should be described in more detail. Please include all the details, such as hardware specifications used for the experiments, software frameworks and versions, training hyperparameters, quantization settings, etc.

### Questions
1.	L1 normalization is not a new concept, as it has been extensively used in prior works. What are the differences between its usage in this paper and related work?
2.	What are the potential impacts at large scale and future works derived from this paper?

### Soundness
3

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
4

### Summary
This paper presents a new approach to sub-8-bit integer training that addresses the challenges of balancing efficiency and accuracy. A key contribution is ShiftQuant, an improvement over traditional group quantization. ShiftQuant eliminates the need for costly memory rearrangements and ensures better compatibility with GEMM operations (General Matrix Multiplication), a crucial component in modern deep learning workloads. Additionally, the framework introduces L1 normalization, which smooths the loss landscape, allowing the implementation of fully quantized normalization layers without compromising convergence.

### Strengths
The method emphasizes real-world speed improvements on various hardware platforms (CPUs, GPUs, and FPGAs), rather than relying solely on theoretical speed-ups. This ensures the proposed solution is relevant and effective for practical deployment.

### Weaknesses
1. **Limited performance improvement**:

ShiftQuant uses coarser per-group quantization, capping its performance below per-group quantization, and the speed-up gains (e.g., 1.85× on CPU) are not very impressive, experiments lack speed comparison with PSQ.

2. **Unclear figures and tables**:

Some figures (fig3) and tables(table2,table3) are not well-explained, making it hard to interpret the results clearly.

### Questions
**Why is zero-point ignored in ShiftQuant’s dequantization?**

In typical per-group quantization, these parameters are essential. What adjustments were made to avoid them?

**How are all calculations performed in integer format if scale is a floating-point value?**

What techniques were used to maintain integer-only computation?

**How should "sharpen" be understood in Figure 4?**


From the figure, it seems that c appears more sharpened. Could you clarify the intended meaning here?

### Soundness
2

### Presentation
2

### Contribution
2
