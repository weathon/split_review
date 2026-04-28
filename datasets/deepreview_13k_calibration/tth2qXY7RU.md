# Super Floating-Point (SuFP): Efficient To All. Multi-Region Piecewise Quantization using Scalable Bias with Hardware Optimization

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5

## Abstract
As Deep Neural Networks (DNNs) revolutionize various application domains, their model size and computational demand also increase exponentially. In response to these challenges, various quantization techniques have emerged as highly effective solutions. However, quantization methods using conventional data types, including integer or floating-point, face certain limitations in balancing between accuracy drop and computational benefit. In light of the advent of hardware accelerator design for AI processing, quantization research has entered a new phase: custom data types and specialized hardware have emerged as innovative alternatives. Particularly, piecewise quantization and block floating-point quantization exhibit notable performance and efficiency improvements, but they still suffer from handling outliers with huge dynamic ranges. To solve this issue, we introduce Super Floating-Point (SuFP), a breakthrough data type and quantization method that improves both memory footprint and logic efficiency without compromising model accuracy. The key idea of SuFP is multi-region piecewise quantization using a tensor-wise scalable bias. It can configure an optimized precision for each region to capture both dense near-zero data and outliers. In addition, the scalable bias offers flexible adaptability to diverse data distributions, requiring only a single addition operation at the tensor level. Furthermore, the tailored hardware for SuFP employs only integer arithmetic units and shifters, facilitating a highly compact hardware realization. Our experimental results show that SuFP quantization achieved accuracy performance on par with, and in some cases even exceeded, that of full precision floating-point (FP32) across vision, language, and generative model benchmarks. Its computational capability and energy efficiency have been dramatically improved by 9.00$\times$ and 17.04$\times$ over FP32 implementations, surpassing state-of-the-art MSFP and BSFP, up to 7.20$\times$ and up to 2.06$\times$, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new data type, Super Floating-Point (SuFP), to improve both memory footprint and computational efficiency for deep neural network quantization. SuFP utilizes multi-region piecewise quantization with tensor-wise scalable bias, allowing for optimized precision for different data regions and adaptability to various data distributions. Experiments show that compared to FP8, SuFP achieves 1.58x and 1.30x improvement in computational capability and energy efficiency, respectively, without losing model accuracy performance.

### Strengths
+ The paper is well-written and easy to follow. Illustrative figures are well plotted and easy to understand.
+ Co-designing the hardware MAC architecture for the proposed data type SuFP enables better hardware efficiency.
+ The evaluation benchmarks are diverse, including both vision and language tasks.

### Weaknesses
+
The ablation study lacks the improvement breakdown on piecewise data representation and tensor-wise scalable bias. Specifically, the paper does not quantify the individual contributions of each of these components to the overall performance gains. For instance, how much of the accuracy improvement is attributable to the multi-region piecewise quantization versus the tensor-wise scalable bias? Without this breakdown, it is difficult to assess the relative importance of each design choice and to understand where further optimization efforts should be focused.

+
The accuracy evaluation experiments lack results on MSFP and BSFP for larger models (Table 3). The efficacy of the proposed SuFP on Large Language Models such as LLaMa2 is also unclear. While the paper provides results for BERT-base and Stable Diffusion v2, the performance on larger, more complex models is crucial for demonstrating the scalability and general applicability of SuFP. The absence of results for MSFP and BSFP on these larger models makes it difficult to directly compare SuFP's performance against these alternatives in a more demanding setting. Additionally, the lack of evaluation on large language models like LLaMa2 leaves a significant gap in understanding SuFP's potential for state-of-the-art natural language processing tasks.

+
The proposed SuFP saves 6% memory, with 1.05x throughput improvement and 1.03x energy savings over MSFP (MX9). The improvement is marginal. While any improvement in memory, throughput, and energy efficiency is welcome, the reported gains over MSFP (MX9) are relatively small. This raises questions about the practical significance of these improvements, especially considering the added complexity of implementing a new data type like SuFP. A more detailed analysis of the trade-offs between performance gains and implementation complexity would be beneficial.

+
MSFP have multiple versions: MX4, MX6 and MX9. It is unclear how SuFP narrows its bit width. The paper does not provide a clear explanation of how SuFP achieves bit-width reduction compared to the different versions of MSFP. A more detailed comparison, outlining the specific bit configurations of SuFP and each MSFP variant, would be helpful in understanding the advantages of SuFP in terms of bit-width optimization.

### Questions
Please answer the questions in the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
To solve the huge dynamic ranges for outliers problems in quantization, this paper introduces a new data type and corresponding quantization method to improve both memory footprint and logic efficiency. The key idea of SuFP is multi-region piecewise
quantization using a tensor-wise scalable bias which offers flexible adaptability to diverse data distributions. Furthermore, the tailored
hardware for SuFP is also provided which employs only integer arithmetic units and shifters. The evaluation has been processed in different tasks, such as vision, language, and generative models.

### Strengths
1. Good writing style. The paper is easy to follow.
2. The paper focuses on a great problem of quantization "outlier" which is critical to the quantization accuracy.
3. Multiple tasks are included in the experiments, which proves the method's flexibility.
4. The works incorporate both the algorithm with the hardware into consideration.

### Weaknesses
1. The paper mainly compares different quantization schemes but does not incorporate different quantization frameworks in the experiment comparisons. 
2. The hardware setup details are not clear. Specifically, the architecture of the Processing Elements (PEs), the memory hierarchy, and the interconnection network are not described. This lack of detail makes it difficult to assess the practical feasibility and scalability of the proposed hardware implementation.
3. The hardware efficiency evaluation only provides a normalized result without a specific number, which may cause additional difficulty for future works' comparison. For instance, reporting area and power consumption as a percentage of a baseline makes it impossible to compare against other hardware implementations or to understand the absolute resource requirements of the proposed design. It is also unclear what the baseline is and if it is a fair comparison.

### Questions
Please refer to the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces the super floating-point format (SuFP) which uses a piece-wise quantizer that better fits the standard distributions shown in modern deep neural networks. It defines these three modes for representing three regions of values and demonstrates that they outperform recently proposed floating-point formats. They evaluate across vision, language, and text-to-image models and show lower memory, area, and power than other approaches.

### Strengths
Figure 3 and Figure 4 clearly show the different data modes and hardware outlines.

This work includes evaluations across vision, language, and text-to-image models.

This work also evaluates the efficiency of its method across many performance categories.

### Weaknesses
Form 3 seems strange since by its bitwidth alone it seems to be strictly worse than Form 1. Does the different bias matter here?

The advantage of supporting difficult modes is not clear when the PEs seem to need to process the largest exponent and mantissas. It might be useful to show where the coverage is for each mode in a figure similar to Figure 2. It is not clear how the different modes are dynamically selected, and what overhead this incurs.

What is the definition for exponent baseline? Initially I thought the exponent would be added to these but the baseline for mode 2 includes the exponent bits themselves. It is still unclear how the baseline is used in the final calculation.

The paper seems to over-sell itself in many places and that space could be used to add more detail. The claims of superior performance need more rigorous justification.

-- Minor --
It would be clearer to show the bitwidth in the formats in the tables since these comparisons are across 32, 16, and 8 bits. The lack of explicit bit-width makes the comparisons difficult to interpret.

Equation 1 can could be explained better in the text. For example, are the X elements an arbitrary tensor? It is unclear what the purpose of this equation is overall. It would be useful to see how this equation relates to the piecewise quantization.

Equations 2-5 could be aligned to make them more readable.

Why is the BSFP datatype only 7 bits in Figure 2 while the others are 8 bits?

### Questions
Are there any additional floating-point quantization scale factors with this method? FP8 method often still use additional higher-precision quantization scales still.

What is the typical distributions of the SuFP modes? To justify sacrificing the bitwidth to handle different modes, it would be useful to see how often the modes are needed. The encoding seems to be a variable-bitwidth encoding so does it reflect the mode distribution? Does mode 3 show up the least often?

What FP8 variant is used for comparison? E4M3 typically has the highest accuracy.

Why not show all the formats for each category evaluation? Formats like BF16 should be simple to evaluate in the PyTorch setup for each and there is significant room in the tables.

Why is the BSFP datatype only 7 bits in Figure 2 while the others are 8 bits?
What granularity does the method operate at? For example, the bias is shared per tensor but since distributions cluster in channels why not make it shared per channel? The hardware diagram seems like there can potentially be bias per 16 elements. Is this true? Also, it seems possible to share the mode over a block of data depending on the variation there.

The ALU seems like it is purely doing standard floating-point multiplication? Or does it support additional functionality to justify its name?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
