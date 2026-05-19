### Summary

This paper focuses on the problem of rendering for unbounded scenes. The key idea is to adaptively allocate ray samples according to scene geometry. To achieve this goal, the paper introduces 1) a p-norm-based projective mapping to transform unbounded scenes into a bounded space; 2) a new ray parameterization to properly allocate ray samples in the geometry of unbounded regions. The proposed method claims to achieve state-of-the-art novel view synthesis results on a variety of challenging datasets.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The idea of using adaptive mapping and ray parameterization for unbounded scene rendering sounds reasonable.
2. The paper is well organized and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The key contribution of the paper lies in the adaptive mapping and ray parameterization for unbounded scene rendering. However, the results in the experiments do not clearly demonstrate the advantages of the proposed method. In fact, I did not find any significant differences between the results of the proposed method and those of previous methods. The quantitative results in Table 1 are also very confusing. For example, why are the PSNR values for the proposed method lower than those of NeRF+ in the NeRF+ row? This is very strange and makes me question the reliability of the experimental results. The lack of a clear and consistent improvement across the different baselines and datasets makes it difficult to assess the true value of the proposed approach. The reported gains seem marginal and inconsistent, raising concerns about the robustness of the method.
2. The paper claims that the proposed method achieves state-of-the-art results. However, the experimental results are not convincing. The paper should provide a more comprehensive comparison with other state-of-the-art methods, such as mip-NeRF 360 and Zip-NeRF. The absence of direct comparisons with these established methods makes it difficult to validate the claim of state-of-the-art performance. The paper needs to demonstrate a clear advantage over existing methods, not just incremental improvements in specific scenarios.
3. The paper lacks a detailed analysis of the limitations of the proposed method. For example, how does the method perform in scenes with complex geometries or lighting conditions? What are the computational costs of the proposed method compared to previous methods? The paper should also include a discussion of the potential failure cases of the proposed method. A thorough analysis of the limitations is crucial for understanding the applicability and practical value of the proposed method. The absence of such analysis leaves the reader with an incomplete picture of the method's capabilities and drawbacks.
4. The writing quality of the paper needs improvement. The key ideas are not clearly presented. The paper should provide more detailed explanations and justifications for the proposed method. The paper should also include more visual aids, such as figures and diagrams, to help the reader understand the proposed method. The current presentation is somewhat vague and lacks the necessary detail to fully grasp the technical contributions.

### Suggestions

The paper needs to provide a more rigorous and comprehensive evaluation of the proposed method. Specifically, the authors should conduct experiments on a wider range of datasets, including more complex and challenging scenes. The comparison should not be limited to the contract mapping baseline, but should also include other state-of-the-art methods such as mip-NeRF 360 and Zip-NeRF. Furthermore, the authors should provide a more detailed analysis of the quantitative results, explaining the reasons behind the observed performance differences. It is crucial to show consistent and significant improvements across different scenarios to demonstrate the effectiveness of the proposed approach. The current results are not convincing enough to support the claim of state-of-the-art performance. The authors should also consider providing ablation studies to analyze the contribution of each component of the proposed method, such as the p-norm-based projective mapping and the new ray parameterization. This would help to better understand the impact of each component on the overall performance.

To address the concerns about the clarity of the presentation, the authors should provide more detailed explanations and justifications for the proposed method. The paper should clearly articulate the motivation behind the design choices and the theoretical foundations of the proposed approach. The mathematical formulations should be presented in a clear and concise manner, with sufficient explanations of the key concepts and assumptions. The paper should also include more visual aids, such as figures and diagrams, to help the reader understand the proposed method. For example, a visual illustration of the p-norm-based projective mapping and the new ray parameterization would be beneficial. The authors should also provide a more detailed discussion of the limitations of the proposed method, including its performance in scenes with complex geometries or lighting conditions, and its computational costs compared to previous methods. This would provide a more balanced and realistic assessment of the proposed approach.

Finally, the authors should carefully review the writing quality of the paper and make sure that the key ideas are clearly presented. The paper should be well-organized and easy to follow, with a logical flow of ideas. The introduction should clearly state the problem being addressed, the proposed solution, and the main contributions of the paper. The related work section should provide a comprehensive overview of the existing literature, highlighting the gaps that the proposed method aims to fill. The method section should provide a detailed description of the proposed approach, with clear explanations of the key concepts and assumptions. The experimental section should provide a rigorous evaluation of the proposed method, with clear explanations of the experimental setup, the evaluation metrics, and the results. The conclusion should summarize the main findings of the paper and discuss the potential future directions. The paper should also include a thorough proofreading to eliminate any grammatical errors or typos.

### Questions

Please refer to the weakness section.

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
