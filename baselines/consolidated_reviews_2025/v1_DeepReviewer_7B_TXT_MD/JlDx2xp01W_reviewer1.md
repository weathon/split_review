### Summary

This paper proposes SAMRefiner, a universal and efficient framework that adapts the Segment Anything Model to the mask refinement task. The proposed SAMRefiner is composed of three components: multi-prompt excavation strategy, split-then-merge (STM) pipeline, and an optional IoU adaption step. The proposed method is evaluated on several benchmarks and achieves good performance.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed SAMRefiner is evaluated on several benchmarks and achieves good performance.
2. The proposed SAMRefiner is efficient and can refine the pseudo masks in parallel.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed SAMRefiner is not novel. The multi-prompt excavation strategy is similar to the context-aware elastic box proposed in CascadePSP. The STM pipeline is similar to the one proposed in CRM. The optional IoU adaption step is similar to the one proposed in SegRefiner.
2. The experiments are not sufficient to demonstrate the effectiveness of the proposed method. The authors should compare SAMRefiner with CascadePSP and CRM, which are the two most related methods. Besides, the authors should evaluate SAMRefiner on the LVIS dataset, which is used in CRM and SegRefiner.
3. The authors should provide the results of SAMRefiner++ in the main paper, instead of the appendix. The results in Table 1 are not consistent with the results in Table 5.

### Suggestions

The paper's primary weakness lies in its lack of novelty, as the proposed method appears to be a combination of existing techniques. While the authors claim a universal and efficient framework, the individual components, such as the multi-prompt excavation strategy, STM pipeline, and IoU adaption step, are all found in other methods like CascadePSP, CRM, and SegRefiner, respectively. The paper needs to clearly articulate the specific novel contributions beyond simply combining these existing components. The authors should provide a detailed analysis of how their approach differs from these prior works, highlighting any unique aspects of their method. For example, if the multi-prompt excavation strategy has a specific implementation that differs from CascadePSP, this should be clearly stated and justified. Similarly, the STM pipeline needs to be compared to the one in CRM, and the IoU adaption step needs to be compared to SegRefiner, with a focus on the specific differences and advantages of the proposed approach. Without a clear explanation of the novel aspects, the contribution of the paper is significantly diminished.

Furthermore, the experimental evaluation is insufficient to demonstrate the effectiveness of the proposed method. The authors should include direct comparisons with CascadePSP and CRM, which are the most directly related methods. The current comparisons with other general mask refinement methods are not sufficient to demonstrate the superiority of SAMRefiner. Additionally, the authors should evaluate SAMRefiner on the LVIS dataset, which is used in CRM and SegRefiner. This would provide a more comprehensive evaluation of the method's performance and allow for a more direct comparison with existing approaches. The lack of these comparisons makes it difficult to assess the true value of the proposed method. The authors should also provide a more detailed analysis of the performance of SAMRefiner on different types of masks, such as small, medium, and large objects, to understand its strengths and weaknesses. This would provide a more nuanced understanding of the method's capabilities.

Finally, the paper needs to address the inconsistencies in the results presented in the main paper. The results for SAMRefiner++ should be included in the main paper, as this is a key component of the proposed method. The current placement of these results in the appendix makes it difficult to understand the overall performance of the method. The authors should also ensure that the results in Table 1 are consistent with the results in Table 5. If there are differences, the authors should provide a clear explanation for these discrepancies. The authors should also provide a more detailed analysis of the performance of SAMRefiner++ compared to SAMRefiner, highlighting the specific benefits of the additional IoU adaption step. This would provide a more complete understanding of the method's capabilities and limitations.

### Questions

See weaknesses.

### Rating

5

### Confidence

4

**********
