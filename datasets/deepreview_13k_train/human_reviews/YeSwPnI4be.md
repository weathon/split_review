# DASH: Data-Efficient Learned Cost Models for Sparse Matrix Computations on Emerging Hardware Platforms

- Decision: Reject
- Scores: 3, 6, 6, 6

## Abstract
Sparse matrix computations are becoming increasingly significant in deep learning and graph analytics, driving the development of specialized hardware systems known as accelerators to meet the growing need for optimized performance. Optimizing these computations, however, presents significant challenges due to their sensitivity to variations in input sparsity patterns and code optimizations. While ML-based cost models and search techniques have shown promise in optimizing sparse matrix computations in general-purpose hardware like CPUs, these cost models require large datasets for effective training. Collecting such extensive datasets is particularly impractical for emerging hardware platforms that only have access to expensive simulators in the early design stages. To overcome this, we propose DASH, which trains learned cost models using low-cost data samples from widely accessible general-purpose hardware (such as CPUs), followed by few-shot fine-tuning to efficiently adapt to emerging hardware platforms. DASH introduces a novel approach that leverages the homogeneity of input features across different hardware platforms while effectively mitigating heterogeneity. This enables DASH to achieve comparable accuracy using only 5% of the data samples required by a cost model trained exclusively using data samples from an accelerator. We evaluate DASH on two critical sparse operations—SpMM and SDDMM—on an emerging sparse accelerator using 715 distinct sparsity patterns. Our experimental results show that DASH outperforms existing techniques that use transfer learning by 28.44%, achieving average speedups of 1.47x (up to 5.46x) for SpMM and 1.39x (up to 4.22x) for SDDMM.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents DASH, a machine learning-based framework for constructing performance predictors to guide program transformations (e.g., loop-level optimizations) for sparse matrix computations on hardware platforms. DASH builds upon WACO, an existing ML framework tailored for sparse matrix computations, with new changes to WACO. Specifically, DASH uses a deeper neural network and maps program transformations into an embedding space to predict the execution time for a specific program transformation configuration on given input matrices and underlying hardware. DASH also leverages transfer learning to reduce the data collection overhead when adapting the trained cost model to new hardware platforms. Experimental results show that DASH delivers a higher accuracy in predicting the execution time, which leads to an overall better speedup.

### Strengths
The paper targets an important problem
Some promising results

### Weaknesses
A large part of the work relies on either strong user intervention (e.g., crafting approximate mapping of code optimizations) or existing techniques like deeper neural networks, mapping program transformation configurations into an embedding space, or transfer learning. The overall technical novelty appears to be rather limited. 

The evaluation was performed on the sparse computation kernel level using matrices from the SuiteSparse Matrix Collection. It would be useful to show the end-to-end performance improvement of a realistic program (e.g., a graph neural network) and the prediction overhead w.r.t. to the end-to-end performance improvement. 

The paper is difficult to follow at times, overly complicating simple things with math equations and formal definitions. Some of the details were not clear until reading the appendix. Important details are also missing. For example, as SparseTIR builds upon TVM, do you perform TVM schedule searching per matrix input? If so, did you include the search overhead?

### Questions
- Can you comment on the portability of the approach as it requires manually defining the mapping of code optimizations across different hardware?

- DASH benefits from a deeper DNN, mapping the code transformation configurations into an embedding space and transfer learning. These all seem to be standard ML techniques. What are the specific challenges for applying these techniques to build cost models for sparse matrix computation?

-What exactly are the default optimization used by TACO and SparseTIR as the baseline? 

-Did you use parallelization in the evaluation? In other words, does the code run in parallel using multiple threads on multi-core CPUs?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce DASH to address the sparse matrix computations when facing different input sparsity patterns and code optimizations.
DASH trains learned cost models with four components, including configuration mapper, input featurizer, latent encoder, and predictor.
From DASH, low-cost data samples from widely accessible general-purpose hardware, followed by few-shot fine-tuning to efficiently adapt to emerging hardware platforms. 
DASH introduces a novel approach that leverages the homogeneity of input features across different hardware platforms while effectively mitigating heterogeneity. 
From the evaluation, DASH can significantly outperforms existing techniques. By avoiding redundant computations and reducing optimization time, combined with the adaptability of deep learning-enhanced models, DASH paves the way for substantial hardware performance improvements.
In conclusion, the paper presents a novel framework, that could help us better understand the challenges coming from Sparse Matrix-Matrix Multiplication and Sampled Dense-Dense Matrix Multiplication. They develop learned cost models which can be leveraged across different hardware platforms.

### Strengths
* The idea from DASH is interesting. Utilizing technologies like autoencoders, DASH successfully mitigates the issue of negative transfer in heterogeneous feature spaces, outperforming traditional manual feature engineering and cost modeling methods. This approach effectively bridges different hardware platforms such as CPUs, GPUs, and sparse accelerators through heterogeneous transfer learning, making it an intuitive and efficient solution.
* DASH is not only applicable to sparse accelerators but also efficiently migrates to various hardware platforms, including GPUs, demonstrating robust generalization capabilities. Based on the WACO model, and by integrating statistical information capture with transfer learning, DASH flexibly extends to different hardware and complex computational tasks, reducing dependency on specific hardware and ensuring good adaptability for future new hardware.
* The paper has good coherence, and is well-structured. The background section explains the related work in an easy understandable way.
* The paper is also very clear with thorough experiments and analysis.

### Weaknesses
 * The first concern arises from the insufficient coverage of sparse matrix structures and different operations. There exists a variety of sparse matrix structures employed in training data configurations, which are not fully demonstrated. The widely used sparse storage formats such as CSR, COO, CSC, ELL, DIA, BSR, and BELL are highly diverse. When dealing with the same type of sparse matrix, the computational patterns of optimization operations like SpMV and SpMM can be quite varied. They exhibit different sensitivities to matrix structures. Therefore, the fine-tuning needs to consider both the sparse matrix representation, the computational operation, and the optimization strategy. However, the performance of DASH solely relies on the types of sparse matrices and computational patterns covered during training. The model may not immediately provide optimal optimizations for novel sparse matrix structures or computational requirements not encountered in the training data, necessitating further training or fine-tuning. Please clarify this point.
* Th second concern arise from limited breadth of experimental evaluation, when dealing with different emerging hardware accelerators. While DASH has demonstrated significant performance improvements in experiments, the testing platforms were primarily focused on specific sparse matrix accelerators, such as SPADE. Other emerging hardware was not included. The results presented show the migration effects from CPU to SPADE accelerators and from CPU to GPU, but there is a lack of consideration and evaluation of a more extensive range of emerging hardware platforms. Different sparse accelerators may have very distinct hardware architectures, and may limite the generalization ability of DASH’s transfer learning optimizations, is not yet sufficiently clear.
* In heterogeneous scenarios, the feature mapping of autoencoders may not be sufficient to capture all behaviors, and the use of a simple MLP predictor could be inadequate to handle complex hardware feature variations. The authors can add more evidences to prove this point.
* Although transfer learning reduces initial simulation costs, the frequent changes in emerging hardware may require timely updates to configuration mappings and fine-tuning, which can increase maintenance complexity.

### Questions
* Please see the weakness section.

### Soundness
3

### Presentation
4

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
This paper presents DASH, a framework for developing data-efficient learned cost models for sparse matrix computations on emerging hardware platforms. The key innovation is enabling effective transfer learning from widely available general-purpose hardware (e.g. CPUs) to emerging accelerator platforms that only have access to expensive simulators during early design stages. DASH introduces techniques to handle both homogeneous and heterogeneous aspects of program configurations across platforms, using approximate mapping for comparable code optimizations and latent space encoding for hardware-specific optimizations. The authors evaluate DASH on SpMM and SDDMM, showing it can achieve comparable accuracy using only 5% of the data samples required by models trained exclusively on accelerator data.

### Strengths
* The wrok addresses an important problem of the high cost of collecting training data through simulation in hardware acceleration design.
* Novel technical approach of separating program configurations into homogeneous and heterogenous components and using autoencoders for compact latent representation of hardware-specific parameters.
* Evaluation shows strong results (speedups of 1.47x for SpMM, 1.39x for SDDMM)

### Weaknesses
 * Limited theoretical analysis or justification for the design choices. For example, autoencoders are used for latent but lacking explanation for why this particular architecture was chosen over alternatives. An ablation study could help justify the chosen design. The choice of autoencoder architecture, including the number of layers, neurons per layer, and activation functions, can significantly impact the quality of the learned latent space. Without a clear rationale or exploration of alternatives, it's difficult to assess the robustness of the approach. Furthermore, the paper lacks a discussion of the potential limitations of using a fixed-size latent space, especially when dealing with highly diverse hardware configurations.
* The evaluation and results focuses heavily on SPADE. Results on other accelerator architectures would strengthen the generalizability claims. While GPU results are included, they could benefit from more details analysis, e.g. comparison of transfer learning effectiveness between CPU->GPU vs. CPU->SPADE. The paper should include a more thorough analysis of the transfer learning performance across different target architectures. The current evaluation does not fully explore the limitations of the proposed approach when applied to accelerators with significantly different architectural characteristics than SPADE. For example, the paper does not discuss how the performance of the transfer learning would be impacted by the degree of similarity between the source and target architectures.

### Questions
1. How sensitive is DASH to the choice of autoencoder architecture? What other architectures were considered?
2. How do the results on GPU compare to cuSPARSE?
3. What are the limitations of the approximate mapping approach? What are the key assumptions about the similarity between the source and target platforms? Are there cases where it breaks down? Are there certain types of optimizations that cannot be effectively mapped?
4. What modifications would be needed to handle accelerators with significantly different architectures (from SPADE)? How much effort is it to find the approximate mapping for such architectures?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Cost models are used to predict the performance of kernel programs so that more efficient kernel programs will be used to perform the computation. This papers targets at building data-efficient learned cost model for emerging hardwares by transfer learning, which requires less data samples from the new hardware that might only be only avaliable as simulators in the early stage of hardware development. The authors propose a few-shot fine-tuning technique, called DASH, to first train a cost model on widely used hardware and then fine-tune the model on the target hardware with a small number of data samples. The cost model considered the spare matrix pattern, homogenous and heterogenous kernel program configurations so that it can be trained and fine-tuned for different hardwares. Experiments show that DASH outperforms existing techniques that use transfer learning by 28.44% interms of the execution performance of found kernels on the target hardware.

### Strengths
1. A cost model architecture design that considered the heterogeneity of hardware so that it can be trained and fine-tuned for different hardware, enabling the transfer learning.
2. The paper is well written and easy to follow.

### Weaknesses
1. The motivation to have such a cost-model for an emerging hardware at the very eary stage is weak. 
2. The avaliablility of a good representation of kernel program configuration for emerging hardware is questionable.
3. The method is highly coupled with the underlying kernel generator.

See below comments for more details.

### Questions
1. The motivation for developing a cost model for emerging hardware at such an early stage is weak. The main motivation for this work is that we can only obtain a very small set of data samples to train the cost model; thus, we can use transfer learning to reduce the demand for a large number of data samples on the target hardware. However, why do we need such a cost model at such an early stage when the hardware development is still in its infancy, making it difficult to obtain sufficient data samples? The common use of a cost model in existing hardware (CPUs, GPUs, and TPUs) is to help select the best kernel from a group of kernels that is optimal for a given input and hardware. The authors claim that such a cost model can assist hardware designers in determining the optimal performance they can achieve at the design stage. However, at this early stage, a good profiler or simulator is more important than a cost model, as the hardware designer can continuously optimize the kernel (which may be written in assembly code or low-level programming) based on feedback from the profiler and simulator. At such an early stage, it is highly questionable whether there is a reliable compiler or kernel generator that can abstract the kernel into a set of tunable parameters (see point 3).

2. The availability of a good representation of kernel program configurations for emerging hardware is questionable. The proposed cost model requires that the optimizations in the kernel programs on the emerging hardware can be abstracted into a set of predefined configurations. However, this greatly limits the scope of the kernels supported by the cost model. Even for mature hardware like NVIDIA GPUs, kernels can be implemented in CUDA in various ways, making it difficult to model CUDA kernels directly. If we restrict the scope of supported kernels, we might miss many efficient kernels during kernel searching.

3. The method is highly coupled with the underlying kernel generator. DASH relies on a high-level kernel composer/generator to create the kernels, which restricts DASH to predicting only the kernel performance generated by those specific kernel generators. In the paper, DASH relies on TACO to generate CPU kernels and SparseTIR to generate NVIDIA GPU kernels. Therefore, the new hardware must have a similar high-level kernel composer to adopt DASH.

### Soundness
2

### Presentation
3

### Contribution
2
