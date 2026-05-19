### Summary

This paper proposes a molecule generation method that decomposes molecules into substructures such as rings, chains, and junctions, and then generates molecules based on these subgraphs. The experimental results demonstrate that the proposed method generates more diverse molecules compared to other methods.

### Soundness

3 good

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The proposed method generates molecules by decomposing them into rings, chains, and junctions, which enhances the diversity of the generated molecules. This approach may be particularly effective in generating molecules with large rings, which are often difficult to generate for previous methods that construct molecules atom by atom.
- The authors conducted a variety of experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper includes an ablation study to investigate the impact of removing each component, but it lacks an analysis of the importance of the order in which the components are added. I suspect that the order in which the components are added may be important. For instance, if the model were to first generate chains, then rings, and finally junctions, how would this affect the generation performance?
- The paper does not include an analysis of the model's complexity or the time required for generation. The proposed method decomposes molecules into multiple subgraphs, which could complicate the optimization process and potentially increase the time needed for molecule generation. It is essential to compare the model's complexity and generation speed with other methods to fully understand the advantages and disadvantages of the proposed approach.

### Suggestions

The paper would benefit from a more detailed investigation into the impact of the generation order of the different molecular components. While the ablation study provides some insight into the importance of each component, it does not explore the potential interactions or dependencies between them during the generation process. Specifically, the authors should consider experimenting with different generation sequences, such as starting with chains, then rings, and finally junctions, or vice-versa. This would help to determine if the model's performance is sensitive to the order in which these substructures are generated. Furthermore, analyzing the generation performance under different orderings could reveal whether certain substructures are more crucial to establish early in the process, which could lead to more effective generation strategies. For example, if generating rings first leads to better overall molecule quality, it might suggest that the model benefits from having a global structure in place early on. This analysis should include quantitative metrics to assess the impact of different generation orders on the quality and diversity of the generated molecules.

In addition to the generation order, a more thorough analysis of the model's computational complexity and generation speed is needed. The paper should provide a detailed breakdown of the computational cost associated with each step of the generation process, including the time required for subgraph decomposition, subgraph generation, and molecule assembly. This analysis should be compared against other state-of-the-art methods to understand the trade-offs between generation quality and computational efficiency. For example, the authors could compare the number of parameters in their model to other models, the time required to generate a single molecule, and the overall training time. This comparison should be done using a consistent hardware setup to ensure a fair evaluation. Furthermore, the authors should discuss the scalability of their approach, particularly how the computational cost scales with the size and complexity of the molecules being generated. This analysis would provide a more complete picture of the practical applicability of the proposed method.

Finally, the paper should also include a discussion on the limitations of the proposed approach. For instance, the authors could discuss the types of molecules that are difficult for their method to generate, or the potential biases that might be introduced by the subgraph decomposition strategy. This would provide a more balanced view of the method's strengths and weaknesses and help guide future research in this area. It would also be beneficial to explore the sensitivity of the model to different hyperparameter settings and provide guidelines for selecting appropriate values. This would make the method more accessible to other researchers and facilitate its adoption in different applications.

### Questions

- The paper includes an ablation study to investigate the impact of removing each component, but it lacks an analysis of the importance of the order in which the components are added. I suspect that the order in which the components are added may be important. For instance, if the model were to first generate chains, then rings, and finally junctions, how would this affect the generation performance?
- The paper does not include an analysis of the model's complexity or the time required for generation. The proposed method decomposes molecules into multiple subgraphs, which could complicate the optimization process and potentially increase the time needed for molecule generation. It is essential to compare the model's complexity and generation speed with other methods to fully understand the advantages and disadvantages of the proposed approach.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
