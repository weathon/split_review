## Human Reviewer 1

### Summary
This paper highlights deployment issues with layers like GELU, Softmax and LayerNorm present in transformer models due to the use of expensive operations such as div, exponential. Present solution either focuses on simplified approximation (GELU→ReLU) and/or hardware design specifically to efficiently run one or more of these blocks on hardware. Both of these solutions are limited in terms of their effectiveness and/or generalization. The Author proposed a unified framework (HARA-Hybrid Arithmetic-ReLU Networks Approximation)  to decompose these functions into simple arithmetic operators and an optimized parameter initialization pipeline for these approximations to work. The results are demonstrated by showing validation accuracy and hardware estimation for both FP32 and INT8 models (BERT, LLaMA, Swin, Stable Diffusion) 

Overall, this paper is well written and proposed solution to a very important problem related to deployment of transformers on different devices. The paper has good contribution and has potential be a good starting for others to work on top of this work. Results are conclusive (except the hardware benchmark) and shows that this method can solve both the issue of hardware complexity and quantization issues related to transformers.

### Strengths
- Authors have targeted a much needed topic in a timely manner as transformers are gaining a lot of popularity but their deployment is still limited to GPU devices and many layers need to be reworked to make it suitable for other devices.
- Approximating power/compute hungry operators has been proposed in the literature and the Authors have compared their results with few of the those (especially LUT based methods)
- The dynamic programming based initialization is a novel concept. Any model optimized with a better initialization strategy has a potential to converge fast.
- Comprehensive results on four models and comparison with other SOTA methods makes the claim stronger.
- Detailed mathematical explanation of approximation is a strong point.
- Most important contribution is to include hardware synthesis results that shows the power and area reduction achieved using HARA

### Weaknesses
- One of the main limitations (also mentioned by the Authors) is that all the benefits are based on the hardware synthesis and the impact of these changes on RAM and latency can be significantly higher (or lower).
- Authors are also encouraged to see the impact of these changes on other domains such as computer vision using ViTs.
- Minor : Citation for RMSNorm and LayerNorm for the first time is missing L037

### Questions
- How does hardware synthesis translate to real RAM/latency improvement comparing to existing architectures (a qualitative discussion would suffice) 
- Can you include the ablation study to prove that the training initialization strategy results in better accuracy of the model (end to end model evaluated on a dataset). Table 4 includes ablation study but it is based on MSE calculated from a sample ? Please clarify how the MSE is exactly calculated and if it is based on a sample, it will be good to do ablation study of validation accuracy of end to end model.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper presents HARA (Hybrid Arithmetic-ReLU Approximation), a unified framework designed to approximate diverse non-linear activation and normalization functions using a single ReLU-based computational unit. The core motivation is that AI accelerators often require dedicated hardware units for different non-linear operations, leading to inefficient area and power utilization. HARA addresses this by proposing a unified approximation architecture that leverages a ReLU-centric design combined with a dynamic programming–based parameter initialization pipeline to enable accurate functional approximation across various nonlinearities. The authors claim that HARA achieves ≤0.1% accuracy degradation on representative workloads (BERT, Swin, LLaMA, Stable Diffusion) while providing substantial projected area and power savings compared to baselines with specialized functional units for each operation.

### Strengths
- The paper introduces a clean, generalizable framework (HARA) that unifies diverse nonlinear operators (e.g., GELU, Softmax, LayerNorm) under a single reconfigurable ReLU-based architecture.

- The unified operator maintains accuracy within <0.1% of the baseline, demonstrating excellent approximation fidelity.

- Hardware synthesis projections show significant area and power savings (≈62% area, 52% power) compared to separate specialized LUT units

### Weaknesses
- Results rely on synthesis-based estimations only, with no end-to-end performance, latency, or energy measurements on real hardware (FPGA, or ASIC prototype) (noted as limitation) or simulation. Ideally, the results for area and power reported should be post place-and-route.

- Evaluations cover only standard precision settings and moderate workloads; there is no stress testing under long-sequence LLMs, mixed precision, or extreme numerical conditions.

- The paper does not compare against reconfigurable functional units (RFUs) or FPGA based designs that already provide similar arithmetic flexibility.

- Models and datasets are reasonable but small. Ideally, to convincingly portray the benefits of the method a large range of model sizes must be employed with reports of accuracy and inference performance metrics.

- Evaluation omits key runtime baselines such as GPU fused kernels or optimized accelerator designs.

### Questions
Technical Concerns/Questions and Points to Address in Rebuttal:

- Missing citations for related work in lines 119-128.

- I suggest having an extended related work section in the appendix having a round-up of quantization techniques etc. particularly the ones focused on similar co-design such as [1], [2] and [3].

- Area, power results must be post place-and-route and not post synthesis.

- Provide range-reduction proofs and error bounds, plus catastrophic-case tests (very peaky logits; near-zero variance in LayerNorm; half-precision under/overflows).

- Larger model evaluations needed. BERT and Swin are not really exciting.

- The paper does not analyze how quantization affects the approximation quality of the learned nonlinear mapping. 

- HARA is positioned as inference-time replacement. There’s no evidence on fine-tuning stability with HARA in the loop, or on co-training to reduce approximation error.

- Quantization setup (scales, accumulators, rounding) is not detailed, limiting reproducibility.

- A key limitation is, this work does not compare inference throughput with GPUs or other existing accelerators. I'd suggest the authors to do a comparison along the lines of [1], [2] using either GP-GPUSim or (if possible) real GPU results to truly evaluate how well HARA performs compared to GPUs. While the authors note the difficulty in physical implementation in the limitation section, I feel it is not unreasonable to do simulation as prior work have done to get preliminary performance evaluation. Not showing any performance results is a red flag and if performance results cannot be shown the authors must wait and re-submit a more complete work in the next iteration.

- More recent baselines must be identified for comparison. 

- How is HARA different from a scheme where you have a general-purpose computational unit with all primitive operations such as add, sub, mult etc and we can use that same unit by changing the routing to create a reconfigurable unit to perform any non-linear operation ? Please do area/power comparison with such a unit.

- When operating at low precision, why not simply employ small LUTs for each non-linear function at sub–8-bit resolution? Wouldn’t that be a more straightforward approach? Because, at lower-precision such as 4-bit  the LUT size is fairly small.

- The URN structure likely involves intermediate activations with addition/multiplication accumulation. The bit-width of these accumulators (e.g., 8-bit vs. 16-bit partial sums) is never stated, making it impossible to evaluate numerical error growth or overflow risk.

- Is the 6nm by TSMC ? 


References:

[1] Ramachandran, A., Kundu, S., & Krishna, T. (2025, June). Microscopiq: Accelerating foundational models through outlier-aware microscaling quantization. In Proceedings of the 52nd Annual International Symposium on Computer Architecture (pp. 1193-1209).

[2] Guo, C., Tang, J., Hu, W., Leng, J., Zhang, C., Yang, F., ... & Zhu, Y. (2023, June). Olive: Accelerating large language models via hardware-friendly outlier-victim pair quantization. In Proceedings of the 50th Annual International Symposium on Computer Architecture (pp. 1-15).

[3] Sharma, H., Park, J., Suda, N., Lai, L., Chau, B., Kim, J. K., ... & Esmaeilzadeh, H. (2018, June). Bit fusion: Bit-level dynamically composable architecture for accelerating deep neural network. In 2018 ACM/IEEE 45th Annual International Symposium on Computer Architecture (ISCA) (pp. 764-775). IEEE.

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper proposes HARA (Hybrid Arithmetic–ReLU Approximation Networks), which replaces diverse and power-hungry nonlinear operations with simple arithmetic primitives combined with a shallow ReLU network. In this way, a single hardware platform for HARA can flexibly support a wide range of nonlinear operations while maintaining efficiency.

### Strengths
- A single hardware framework for HARA can support various nonlinear operations, offering architectural flexibility.

### Weaknesses
- Several critical details necessary for fully understanding HARA are missing.
  1. The size of the ReLU network (e.g., hidden dimension) is not provided, making it difficult to estimate the processing cost of HARA.
  2. The conversion mechanism from GeLU to HARA is not described.
  3. The storage and memory-access overhead for the ReLU network weights is not adequately discussed. Conventional nonlinear operator implementations (including LUT-based approximation methods) do not require external memory access, so the latency and energy implications of fetching ReLU network weights should be analyzed for a fair comparison.
  4. The parameter tuning cost for HARA (via dynamic programming and fine-tuning) is not fully discussed.
- This paper does not clearly describe the hardware resource requirements of conventional LUT-based approximation methods or their impact on inference accuracy. For example, NN-LUT [1] employs a simple LUT with only 16 entries to approximate nonlinear functions, achieving low hardware cost while maintaining accuracy. Although increasing the number of LUT entries could further reduce the mean squared error (MSE), such improvement may not necessarily lead to meaningful gains in inference accuracy. Hence, improving MSE at the expense of hardware efficiency may not be justified. Consequently, directly comparing MSE values between HARA and conventional LUT-based approximation methods may not represent a fair evaluation. A more comprehensive assessment, including hardware area, power overhead, processing latency, and inference accuracy, would be necessary to establish the practical advantages of HARA.

[1] Yu, Joonsang, et al. "NN-LUT: Neural approximation of non-linear operations for efficient transformer inference." Proceedings of the 59th ACM/IEEE Design Automation Conference. 2022.

### Questions
Please check the weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper presents HARA (Hybrid Arithmetic–ReLU Approximation), a unified framework for replacing all non-linear operations in Transformers (e.g., GELU, Softmax, LayerNorm) with a single hardware-efficient ReLU–arithmetic module. The core idea is to use a dynamic programming–based parameter initialization pipeline that systematically finds near-optimal breakpoints for piecewise linear approximation, converts them analytically into ReLU parameters, and fine-tunes them. Experiments show that HARA achieves orders-of-magnitude lower MSE compared to NN-LUT and RI-LUT, while maintaining almost identical end-to-end performance with various transformer-based models.

### Strengths
- The paper is well written, detailed, and clearly organized. The methodology and experiments are described systematically, and results are easy to reproduce.
- Compared to NN-LUT and RI-LUT, HARA significantly reduces approximation error (often by several orders of magnitude), leading to more robust end-to-end accuracy across multiple Transformer models.

### Weaknesses
- **Methodological contribution seems incremental**: While the paper frames its contribution as a unified framework with an optimized DP-based initialization pipeline, the core technical novelty beyond prior work such as NN-LUT or RI-LUT appears limited. The main differentiator seems to be the use of dynamic programming for systematic breakpoint selection and analytical ReLU parameter conversion, which is a well-motivated but relatively moderate algorithmic improvement. If I have misunderstood the extent of this difference, clarification on how HARA’s optimization pipeline fundamentally departs from previous LUT-based or neural approximation methods would be helpful.

- **Lack of strong empirical motivation**: The paper does not convincingly establish that non-linear operators are the primary computational bottleneck in modern Transformer inference, especially compared to attention or matrix-multiplication components. While the proposed framework demonstrates excellent numerical approximation accuracy, it remains unclear how much practical speedup or memory benefit these approximations bring at the end-to-end system level. In addition, the experimental scope is somewhat narrow—evaluations focus on a small set of tasks and omit runtime or latency measurements that could justify the broader motivation.

 - The work’s focus and contributions are primarily hardware- and implementation-oriented, with less emphasis on learning dynamics or algorithmic understanding. Therefore, the paper may align more naturally with a hardware or systems venue (e.g., DAC, MLSys) rather than ICLR, which typically emphasizes conceptual or methodological advances in machine learning.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3