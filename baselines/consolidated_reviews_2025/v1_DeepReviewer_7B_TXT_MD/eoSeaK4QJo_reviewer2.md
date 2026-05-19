### Summary

This paper presents a pruning framework that combines unstructured weight and neuron pruning to enhance the energy efficiency of SNNs. The authors argue that existing pruning methods do not fully exploit the sparsity of neuromorphic computing, and they introduce a novel approach that combines unstructured weight and neuron pruning to maximize energy savings. The paper presents a detailed analysis of the energy consumption of SNNs and designs a penalty term to address the ill-posed problem of combining weight and neuron pruning. Experimental results demonstrate the effectiveness of the proposed method in reducing energy consumption while maintaining comparable performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow. The motivation is clear and the authors provide a detailed analysis of the energy consumption of SNNs and design a penalty term to address the ill-posed problem of combining weight and neuron pruning.
2. The proposed method is technically sound and innovative. The authors combine unstructured weight and neuron pruning to enhance the energy efficiency of SNNs, which is a novel approach.
3. The experimental results demonstrate the effectiveness of the proposed method in reducing energy consumption while maintaining comparable performance. The authors also provide a detailed ablation study to validate the effectiveness of combining weight and neuron pruning.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the implementation of the proposed method, such as the specific pruning ratios for weights and neurons, and the hardware platform used for evaluation. Specifically, the paper lacks details on how the pruning masks are generated and applied, and whether the pruning is performed in a layer-wise or filter-wise manner. The absence of details regarding the hardware platform makes it difficult to assess the practical relevance of the reported energy savings.
2. The authors should compare their method with more state-of-the-art pruning methods for SNNs, such as those based on magnitude-based pruning or gradient-based pruning. The current comparison is limited, and it is unclear how the proposed method compares to other advanced pruning techniques in terms of both performance and energy efficiency. A more comprehensive comparison would strengthen the paper's claims.
3. The authors should discuss the limitations of their method and potential future directions. For example, the authors could discuss the impact of pruning on the robustness of the SNNs or the potential for further energy savings. The paper would benefit from a more thorough discussion of the trade-offs involved in the proposed pruning approach and its potential impact on the overall performance of the SNN.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the implementation specifics. The authors should provide a clear description of how the pruning masks are generated, including the exact mathematical operations and the criteria used to determine which weights and neurons to prune. It is crucial to specify whether the pruning is performed on a per-layer basis, per-filter basis, or at a more granular level. Furthermore, the paper should detail the hardware platform used for the energy consumption measurements. This should include the specific type of neuromorphic processor or the simulated environment, as well as the clock speed and other relevant parameters. Without this information, it is difficult to assess the practical relevance and the validity of the reported energy savings. The authors should also clarify how the energy consumption is measured, for example, whether it is based on the number of synaptic operations or the actual power consumption of the hardware.

To strengthen the paper's claims, the authors should include a more comprehensive comparison with existing state-of-the-art pruning methods for SNNs. This comparison should not only focus on the final performance metrics but also on the energy efficiency achieved by each method. The authors should consider including methods that use different pruning strategies, such as magnitude-based pruning, gradient-based pruning, or other advanced techniques. A detailed comparison should also discuss the trade-offs between performance and energy efficiency for each method. This would provide a more complete picture of the advantages and disadvantages of the proposed approach. Furthermore, the authors should discuss the computational overhead associated with the proposed pruning method. While the energy consumption is reduced, it is important to consider the computational cost of the pruning process itself, especially during training. This would provide a more complete understanding of the overall efficiency of the proposed method.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method and potential future research directions. The authors should discuss the impact of pruning on the robustness of the SNNs, for example, how pruning affects the model's performance under noisy inputs or adversarial attacks. The paper should also explore potential future research directions, such as exploring different pruning strategies, investigating the impact of pruning on the training process, or extending the pruning method to other types of spiking neural networks. A more comprehensive discussion of the limitations and future directions would enhance the paper's overall impact and provide valuable insights for future research in this area.

### Questions

Please see the weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
