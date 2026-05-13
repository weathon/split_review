# SeedLM: Compressing LLM Weights into Seeds of Pseudo-Random Generators

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Large Language Models (LLMs) have transformed natural language processing, but face significant challenges in widespread deployment due to their high runtime cost. In this paper, we introduce SeedLM, a novel post-training compression method that uses seeds of pseudo-random generators to encode and compress model weights. Specifically, for each block of weights, we find a seed that is fed into a Linear Feedback Shift Register (LFSR) during inference to efficiently generate a random matrix. This matrix is then linearly combined with compressed coefficients to reconstruct the weight block. SeedLM reduces memory access and leverages idle compute cycles during inference, effectively speeding up memory-bound tasks by trading compute for fewer memory accesses. Unlike state-of-the-art compression methods that rely on calibration data, our approach is data-free and generalizes well across diverse tasks.  Our experiments with Llama 3 70B, which is particularly challenging to compress, show that SeedLM achieves significantly better zero-shot accuracy retention at 4- and 3-bit  than state-of-the-art techniques, while maintaining performance comparable to FP16 baselines. Additionally, FPGA-based tests demonstrate that 4-bit SeedLM, as model size increases to 70B, approaches a 4x speed-up over an FP16 Llama 2/3 baseline. %Our code is available at [\textcolor{blue}{URL}].

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This is an interesting method of quantization, using pseudo-random generator to point to almost evenly distributed codebook items and fast adjustments.
The paper has high quality presentation with necessary formulas and diagrams
The paper has shortcomings in comparisons with the other methods, specifically it lacks finetuning upside analysis.

The paper may qualify for acceptance if the weaknesses are reasonably addressed in the review process.

### Strengths
Novel method to store and retrieve codes with pseudo-random number generator.
High quality presentation with necessary formulas and diagrams
Attention to implementation details in Performance Analysis section.

### Weaknesses
1) Comparison with other quantization methods is incomplete. Most striking shortcoming is lack of comparison with finetuned model which is what most current SOTA models use.

2) The paper dismisses comparison with strong methods like AQ, SPQR in desire to "avoid costly training". Yet these are quite good benchmarks to compare with, they have reported figures, and to large share of practitioners the extra training time (hours actually) could be acceptable.

3) some of the results in table 2 are not consistent with those published in the respective papers.
for instance, AWQ claims 3.41 perplexity  for L2-70, (https://arxiv.org/pdf/2306.00978, table 4) while you indicate 3.5 (Table 2)

### Questions
1) Please compare your method with SOTA methods which use finetuning after quantization.
2) What is your method performance when quantizing into 1.5-2.5 bits per weight? This area is where most quantization research progress is happening, your method may be competitive there too.
3) please address the OOM situation in Quip# L2-70 benchmarks (Table2). What is different in your setup vs the original one from https://arxiv.org/pdf/2307.13304? What have you tried to avoid OOM? 
4) Add performance timing benchmarks vs other methods, this solidifies your claim of speed advantage.
5) How would speedup of the method change after post-quantization finetuning?
6) Unlike some other submission, this one has no implementation code. I wonder if a private code repository could be provided for review purposes?
7) Please provide comparison to AQ, SPQR, as these are strong and valid SOTA benchmarks

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces SeedLM, a novel post-training compression technique leveraging seeds of pseudo-random generators, specifically using Linear Feedback Shift Registers (LFSRs), to encode and compress weights in large language models (LLMs). SeedLM achieves memory efficiency by encoding model weights into compact seeds, reconstructing weights at runtime, and minimizing memory access during inference. Experimental results show its performance in zero-shot tasks, achieving competitive accuracy retention at 3- and 4-bit quantization levels, especially with the LLaMA 3 model, and demonstrating improved latency and throughput in FPGA implementations.

### Strengths
1- **Innovative Use of Arbitrary Data Formats**: The adoption of arbitrary data formats with shared exponents is a commendable design choice, enhancing the flexibility of SeedLM's quantization approach.

2- **Efficient FPGA Implementation**: Proposing an efficient FPGA implementation demonstrates the hardware viability of SeedLM and highlights potential real-world deployment in resource-constrained environments.

3- **Data-Free Compression**: SeedLM operates without calibration data, which differentiates it from many other compression methods that rely on data for fine-tuning and accuracy adjustments.

4- **Memory Efficiency**: By using seeds for reconstructing weights, SeedLM minimizes memory footprint, crucial for memory-bound applications like LLM inference, and shows considerable speedup, particularly on FPGAs.

### Weaknesses
1- **Absence of GPTQ Comparison**: The paper does not provide a comparison with GPTQ, a commonly used quantization baseline, which is a notable omission given GPTQ's relevance to LLM compression. While other baselines are included, the lack of direct comparison to GPTQ makes it difficult to assess the relative performance of SeedLM against a well-established method.

2- **Inference Efficiency Assumptions**: While the paper mentions using the latest repositories, many of these codebases likely store compressed weights in full precision during inference, leading to potential memory inefficiencies. This assumption needs to be explicitly addressed, as it could significantly impact the reported memory savings of SeedLM if not handled carefully.

3- **GPU Implementation Challenges**: Although FPGA implementation is shown, the challenges of porting SeedLM to GPUs are unaddressed. Issues like increased kernel launches for memory-bound tasks and limited support for LFSRs in recent GPU hardware could impact performance. The paper should discuss the feasibility and potential performance bottlenecks of a GPU implementation.

4- **Optimization Overhead for Parameter Selection**: The process of determining optimal parameters for each weight block, such as the seeds, coefficients, and latent dimensions, may introduce significant overhead. The computational cost of this optimization process needs to be quantified and discussed in detail.

### Questions
1- **Comparison with GPTQ** : Why was GPTQ omitted from the comparisons? Can you clarify its potential impact on results, given that it’s a standard benchmark in LLM compression?

2- **Compression Limitations for LLaMA 3**: Many methods struggle to compress LLaMA 3 effectively. Do the authors have insights on why this model, in particular, is challenging to compress?

3- **Full Precision Storage Impact**: Have the authors tested SeedLM with full precision storage during inference? If so, could this be the cause of out-of-memory issues observed with some baseline methods?

4- **GPU Implementation Challenges**: Could the authors comment on the challenges of implementing SeedLM on GPUs, specifically the support for LFSR in recent GPUs and whether additional kernel launches could reduce performance for memory-bound applications on NVIDIA hardware?

5- **Parameter Optimization Overhead**: What is the computational cost of finding optimal seeds and coefficients? Could the process be streamlined for faster deployment?

6- **Sensitivity in Compressing LLaMA 3**: Many quantization techniques, appear to struggle with LLaMA 3, indicating potential limitations in compressing this model type. What features does this family of models have that makes it difficult for other methods to quantize, and why does SeedLM perform well in this case?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes SeedLM, a novel method for compressing large language model (LLM) weights by encoding them into seeds of pseudo-random generators.  SeedLM is a data-free, post-training compression method that achieves competitive accuracy at 3/4-bit compression context, as demonstrated on models like Llama 2 and Llama 3. The technique utilizes Linear Feedback Shift Registers (LFSRs) to generate pseudo-random matrices that reconstruct weight blocks during inference. Hardware implementation on an FPGA further supports the potential of SeedLM.

### Strengths
1. Weight compression using pseudo-random generator seeds is a novel-sounding technique. It enables significant compression while maintaining high accuracy.
2. Unlike many state-of-the-art compression methods, the proposed method does not require calibration data, reducing the need for correction data acquisition and potentially further reducing the quantization offset problem caused by the calibration data distribution.
3. The authors validated the computational characteristics and efficiency of their proposed algorithm using FPGA, and the FPGA implementation verifies the SeedLM in some ideal hardware-constrained environments.

### Weaknesses
1. The author compared the AWQ, Omniquant, and QuIP# methods. However, Omniquant and QuIP# were primarily designed for ultra-low bit-width quantization compression, such as 2-bit, but the author only compared the performance of 3/4-bit and did not show the quantization results of 2-bit. In the field of LLM quantization, SOTA methods specifically designed for 4/3-bit, such as GPTQ[1], were not included in the comparison. This makes the results unconvincing.

2. The author mentions in Section 4.1, lines 356-358, that to ensure a fair comparison with QuIP# and Omniquant, no fine-tuning was performed on them. This is a fair comparison for QuIP#, which combines codebook and fine-tuning of pre-trained parameters to improve performance. However, Omniquant does not fine-tune any pre-trained parameters, instead using block-wise gradient propagation to update the quantizer parameters, including the scaling factor and zero factor. By not using this technique in the comparison, the author is essentially not using the Omniquant method, but rather a basic statistical quantization. And, AWQ also uses calibration data to pre-compute the scaling parameters. This comparison is unfair and may cause confusion for readers. Additionally, the data in Table 2 is different from what is reported in the AWQ paper, and the author should provide an explanation for this discrepancy.

3. AWQ can quickly determine the scaling of weights and perform quantization through calibration, and the compression time for a 7B model is only a few minutes. However, the LFSR technique proposed in the paper involves matrix decomposition and optimization approximation, and the efficiency of this compression process for extremely large-scale LLMs is lacking in discussion and comparison.

4. The overall writing of the article is not clear in some details. In Eq (1), I can infer that the compression matrices for LFSR are **U** and **t**, but the details of how the input activation **X** is computed with the LFSR-compressed weights during the actual inference decoding stage are not discussed in detail. The article should provide more information on how the LFSR-compressed weights are used in the inference process and how they differ from other quantization methods. This would help to clarify the advantages and characteristics of the LFSR-based method.

### Questions
Please refer to the weaknesses items.

### Soundness
3

### Presentation
2

### Contribution
2
