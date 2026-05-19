### Summary

This paper proposes SAMRefiner, a universal and efficient framework to refine the quality of coarse masks. It is composed of three components: multi-prompt excavation strategy, split-then-merge (STM) pipeline, and optional IoU adaption step. The authors conduct extensive experiments on multiple benchmarks, demonstrating the effectiveness and efficiency of SAMRefiner.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed SAMRefiner is a universal and efficient framework that can refine the quality of coarse masks.
2. The authors conduct extensive experiments on multiple benchmarks, demonstrating the effectiveness and efficiency of SAMRefiner.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed SAMRefiner is not novel. The multi-prompt excavation strategy is similar to the context-aware elastic box proposed in CascadePSP. The STM pipeline is similar to the one proposed in CRM. The optional IoU adaption step is similar to the one proposed in SegRefiner.
2. The experiments are not sufficient to demonstrate the effectiveness of the proposed method. The authors should compare SAMRefiner with CascadePSP and CRM, which are the two most related methods. Besides, the authors should evaluate SAMRefiner on the LVIS dataset, which is used in CRM and SegRefiner.
3. The authors should provide the results of SAMRefiner++ in the main paper, instead of the appendix. The results in Table 1 are not consistent with the results in Table 5.

### Suggestions

The paper's primary weakness lies in its incremental contribution over existing methods. While the authors present a framework for mask refinement, the core components, such as the multi-prompt excavation strategy, split-then-merge (STM) pipeline, and IoU adaption step, bear striking similarities to techniques already employed in methods like CascadePSP, CRM, and SegRefiner. The multi-prompt excavation strategy, for instance, shares conceptual overlap with the context-aware elastic box approach in CascadePSP, which also aims to refine bounding boxes by considering contextual information. Similarly, the STM pipeline, while effective, is conceptually similar to the multi-stage refinement approach in CRM, which also aims to improve mask quality by iteratively refining regions. The IoU adaption step, while a useful addition, is also reminiscent of the IoU-based refinement in SegRefiner. The authors need to clearly articulate the novel aspects of their approach beyond these existing techniques, highlighting any unique implementation details or architectural differences that justify the proposed framework as a significant contribution. A more thorough analysis of the differences and advantages of SAMRefiner compared to these methods is necessary to establish its novelty and impact.

Furthermore, the experimental evaluation needs to be significantly strengthened to demonstrate the effectiveness of the proposed method. The authors should include direct comparisons with CascadePSP and CRM, which are the most directly related methods. These comparisons are crucial to understand the relative performance of SAMRefiner in the context of existing mask refinement techniques. The current evaluation lacks a comprehensive comparison, making it difficult to assess the true value of the proposed approach. Additionally, the authors should evaluate SAMRefiner on the LVIS dataset, which is used in CRM and SegRefiner. This would allow for a more direct comparison with these methods and provide a more robust evaluation of the proposed framework. The absence of these comparisons makes it difficult to ascertain the generalizability and effectiveness of SAMRefiner across different datasets and scenarios. The authors should also consider including more diverse datasets and evaluation metrics to provide a more comprehensive assessment of the method's performance.

Finally, the presentation of results needs to be improved. The authors should include the results of SAMRefiner++ in the main paper, rather than relegating them to the appendix. This is important because SAMRefiner++ is a key component of the proposed framework, and its performance should be highlighted in the main body of the paper. The inconsistency between the results in Table 1 and Table 5 regarding SAMRefiner also needs to be addressed. The authors should ensure that the results are consistent and accurately reflect the performance of the proposed method. This will improve the credibility and clarity of the paper. The authors should also provide a more detailed analysis of the results, including a discussion of the strengths and weaknesses of the proposed method in different scenarios. This would provide a more nuanced understanding of the method's capabilities and limitations.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

4

**********
