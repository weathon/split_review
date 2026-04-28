# MoE++: Accelerating Mixture-of-Experts Methods with Zero-Computation Experts

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
In this work, we aim to simultaneously enhance the effectiveness and efficiency of Mixture-of-Experts (MoE) methods. To achieve this, we propose MoE++, a general and heterogeneous MoE framework that integrates both Feed-Forward Network~(FFN) and zero-computation experts. Specifically, we introduce three types of zero-computation experts: the zero expert, copy expert, and constant expert, which correspond to discard, skip, and replace operations, respectively. This design offers three key advantages: (i)~\textbf{Low Computing Overhead}: Unlike the uniform mixing mechanism for all tokens within vanilla MoE, MoE++ allows each token to engage with a dynamic number of FFNs, be adjusted by constant vectors, or even skip the MoE layer entirely. (ii)~\textbf{High Performance}: By enabling simple tokens to utilize fewer FFN experts, MoE++ allows more experts to focus on challenging tokens, thereby unlocking greater performance potential than vanilla MoE. (iii)~\textbf{Deployment Friendly}: Given that zero-computation experts have negligible parameters, we can deploy all zero-computation experts on each GPU, eliminating the significant communication overhead and expert load imbalance associated with FFN experts distributed across different GPUs. Moreover, we leverage gating residuals, enabling each token to consider the pathway taken in the previous layer when selecting the appropriate experts. Extensive experimental results demonstrate that MoE++ achieves better performance while delivering 1.1$\sim$2.1$\times$ expert forward throughput\footnotemark[2] compared to a vanilla MoE model of the same size, which lays a solid foundation for developing advanced and efficient MoE-related models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the MoE++, which adds zero-computation experts to enhance the efficiency of computation.
It utilizes zero-computation experts to minimize overhead by allocating fewer resources to basic tokens and concentrating on complex ones. MoE++ enhances expert selection stability by employing pathway-aware routing with gating residuals, resulting in higher performance and throughput than conventional MoE models at a reduced computational cost.

### Strengths
With the proper hyper-parameters, MoE++ introduces zero-computation experts who can reduce the computational load by bypassing or simplifying processing for certain tokens, leading to efficient resource use.
These heterogeneous experts with suitable routing designs can improve the model's efficiency and effectiveness.

### Weaknesses
1. Parameters such as $\tau$, which regulate token allocation between zero-computation experts and original, may complicate model tuning, as the performance and burden distribution are sensitive to them.  
2. The pathway-aware routing with gating residuals adds complexity to the expert selection process, which may require careful tuning for optimal results. Specifically, the interaction between the gating residuals and the base routing mechanism needs careful calibration to avoid potential instability or suboptimal routing decisions. The added complexity of this interaction may also increase the computational overhead, which should be thoroughly analyzed.
3. The dynamic routing mechanism can still result in load imbalances, especially under diverse data distributions, which may lead to underutilized or overloaded experts that affect efficiency. This is particularly concerning when some experts are consistently bypassed while others are heavily utilized, leading to a waste of computational resources and potentially limiting the model's overall capacity.

### Questions
1. How do individual components, like zero experts or gating residuals, contribute to MoE++'s overall performance?
2. Could certain components be removed or modified for specific use cases?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the addition of a new class of experts in the MoE architecture called "zero-computation" experts. The zero-computation type experts include a zero expert, a copy expert, and constant experts. Each of these experts is extremely computationally lightweight relative to a standard FFN expert. The authors demonstrate that incorporating this expert type is both GPU friendly due to the low overhead and can improve performance and throughput.

### Strengths
The authors provide a fairly simple and effective addition to the standard MoE architecture which effectively allows more heterogeneous computing in different layers with minimal overhead. The paper is written clearly and a thorough set of ablations are performed.

### Weaknesses
The empirical gains don't seem to be too significant and can only start to be seen at large scale ~7B parameters.

### Questions
Are the baseline MoE models also trained with residual gating? For each model, many experts are activated in each layer? I could not really tell.

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
5

### Summary
This paper introduces MoE++, a general and heterogeneous MoE framework that uses a fixed mixing mechanism for all tokens and optimizes computation allocation by assigning fewer FFN experts to simple tokens, allowing more FFN experts to be dedicated to challenging tokens. Extensive experimental results demonstrate the lower computational overhead and better performance of MoE++ than vanilla MoE.

### Strengths
- This work improves the existing MoE framework in terms of both efficiency (throughput) and effectiveness (performance), making it impactful for real-world applications.
- This paper is well-written and insightful, with clear motivation and illustrations.
- Figures and tables are clear and easy to read.

### Weaknesses
 - While Table 1 shows the “complexity between the proposed MoE++ and MoE” and zero-computation experts enjoy a complexity of 0, they still likely lead to some extra computation overhead. Therefore, this work lacks real-world wall-clock time demonstrations of these zero-computation expert operators, especially regarding a batch of tokens.
- This work introduces three types of zero-computation experts (i.e. zero, copy, and constant) but provides minimal justification for this specific set. From Table 5, we can see they only conducted basic combinatorial ablations.

### Questions
- How are these zero-computation experts specialized to input tokens? Specifically, it would be great to show some examples of tokens allocated to zero, copy, and constant experts, respectively.

### Soundness
3

### Presentation
4

### Contribution
3
