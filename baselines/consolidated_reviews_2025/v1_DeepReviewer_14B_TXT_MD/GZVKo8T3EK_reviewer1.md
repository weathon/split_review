### Summary

The paper introduces ProvCreator, a framework designed to synthesize provenance graphs that combine both structural and textual attribute information, addressing the limitations of existing synthetic graph generation methods. ProvCreator leverages a graph diffusion model to capture structural information and a conditional transformer model to learn and generate realistic textual attributes based on the graph’s node embeddings. The framework is evaluated on system provenance graphs for two processes—powershell.exe and svchost.exe—and demonstrates superior structural and attribute fidelity over baseline methods. Additionally, ProvCreator improves the performance of downstream machine learning tasks, such as program classification and intrusion detection.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- ProvCreator’s integration of graph diffusion with a conditional transformer for attribute generation is innovative, effectively capturing the joint distribution of structures and rich textual attributes.

- The framework demonstrates measurable improvements over baseline methods in both structural fidelity and attribute realism, as validated by multiple similarity metrics.

### Weaknesses

#### Some Related Works


#### comment

 - The paper’s scope is confined to system provenance graphs, with limited discussion on the generalizability of ProvCreator to other types of heterogeneous graphs. The framework’s effectiveness on graphs with different structural properties or attribute types remains unclear, which limits the broader applicability of the proposed method.

- The evaluation is based on only two process types (powershell.exe and svchost.exe), which may not capture the full variability of provenance graphs. Expanding the evaluation to include more diverse processes and edge cases would strengthen the claims of generalizability and robustness.

- The framework’s reliance on multiple complex models (graph transformer, GNN encoder, and transformer decoder) suggests high computational demands, yet there is limited discussion on scalability or efficiency. The paper lacks detailed analysis of training time, memory usage, and the computational cost associated with generating synthetic graphs, making it difficult to assess the practical feasibility of the approach, especially for large-scale datasets.

- The paper lacks a detailed ablation study to assess the individual contributions of the graph transformer, GNN encoder, and transformer decoder. Without such an analysis, it is unclear how much each component contributes to the overall performance and whether simpler models could achieve comparable results.

### Suggestions

The authors should provide a more thorough analysis of the framework's generalizability beyond system provenance graphs. Specifically, they should evaluate the performance of ProvCreator on heterogeneous graphs with different structural properties and attribute types, such as social networks or knowledge graphs. This would involve adapting the input data and potentially modifying the model architecture to accommodate different node and edge types. Furthermore, the authors should include a discussion on the limitations of the current approach and the potential challenges in applying it to other domains. This would help to clarify the scope of the proposed method and identify areas for future research.

To strengthen the evaluation, the authors should include a more diverse set of processes and edge cases. This could involve selecting processes with varying levels of activity, different types of system calls, and different interaction patterns. The inclusion of edge cases, such as processes with unusual behavior or rare system calls, would help to assess the robustness of the framework. Additionally, the authors should provide a detailed analysis of the synthetic graphs generated for these diverse processes, including visualizations and comparisons with real graphs. This would help to demonstrate the ability of ProvCreator to capture the full variability of provenance graphs.

The paper needs a more detailed analysis of the computational complexity and scalability of the proposed framework. The authors should provide a breakdown of the time and memory requirements for each component of the model, including the graph transformer, GNN encoder, and transformer decoder. They should also discuss the potential bottlenecks in the training process and the strategies for optimizing the performance. Furthermore, the authors should evaluate the scalability of the framework by generating synthetic graphs of varying sizes and analyzing the impact on training time and memory usage. This would help to assess the practical feasibility of the approach for large-scale datasets and identify areas for improvement.

### Questions

- How well does ProvCreator generalize to other types of heterogeneous graphs beyond system provenance data? Have you considered applying it to other domains, and if so, what adaptations would be necessary?

- What is the computational complexity of training and using ProvCreator, particularly in terms of time and memory requirements? How does the framework scale with increasing graph size?

### Rating

5

### Confidence

3

**********
