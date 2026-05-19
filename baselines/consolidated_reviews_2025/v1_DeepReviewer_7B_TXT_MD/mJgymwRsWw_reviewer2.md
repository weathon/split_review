### Summary

The paper presents a method for active probabilistic drug discovery (APDD) which iteratively updates the binding probabilities of molecules to a target protein of interest. The method consists of three consecutive steps: (1) molecules are partitioned into clusters using probabilistic clustering algorithms with substructure similarity as the similarity metric; (2) representative molecules from each cluster are selected for molecular docking simulations using VinaGPU+; (3) the binding probabilities of the molecules are updated based on the results of the molecular docking simulations and wet lab experiments. The authors demonstrate the effectiveness of their method using two benchmark datasets.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The authors propose a novel method for active probabilistic drug discovery (APDD) which is a novel combination of three consecutive steps: (1) molecules are partitioned into clusters using probabilistic clustering algorithms with substructure similarity as the similarity metric; (2) representative molecules from each cluster are selected for molecular docking simulations using VinaGPU+; (3) the binding probabilities of the molecules are updated based on the results of the molecular docking simulations and wet lab experiments. The authors demonstrate the effectiveness of their method using two benchmark datasets.

### Weaknesses

#### Some Related Works


#### comment

The authors propose a novel method for active probabilistic drug discovery (APDD) which is a novel combination of three consecutive steps: (1) molecules are partitioned into clusters using probabilistic clustering algorithms with substructure similarity as the similarity metric; (2) representative molecules from each cluster are selected for molecular docking simulations using VinaGPU+; (3) the binding probabilities of the molecules are updated based on the results of the molecular docking simulations and wet lab experiments. The authors demonstrate the effectiveness of their method using two benchmark datasets.

The authors propose a novel method for active probabilistic drug discovery (APDD) which is a novel combination of three consecutive steps: (1) molecules are partitioned into clusters using probabilistic clustering algorithms with substructure similarity as the similarity metric; (2) representative molecules from each cluster are selected for molecular docking simulations using VinaGPU+; (3) the binding probabilities of the molecules are updated based on the results of the molecular docking simulations and wet lab experiments. The authors demonstrate the effectiveness of their method using two benchmark datasets.

The authors propose a novel method for active probabilistic drug discovery (APDD) which is a novel combination of three consecutive steps: (1) molecules are partitioned into clusters using probabilistic clustering algorithms with substructure similarity as the similarity metric; (2) representative molecules from each cluster are selected for molecular docking simulations using VinaGPU+; (3) the binding probabilities of the molecules are updated based on the results of the molecular docking simulations and wet lab experiments. The authors demonstrate the effectiveness of their method using two benchmark datasets.

### Suggestions

The paper introduces an interesting approach to active probabilistic drug discovery by combining clustering, molecular docking, and wet lab experiments. However, the current presentation lacks sufficient detail to fully understand the method's implementation and potential. Specifically, the description of the clustering algorithm is vague. While the authors mention using probabilistic clustering, they do not specify the exact algorithm (e.g., PAM, k-means, hierarchical clustering) or the distance metric used to measure substructure similarity. This lack of detail makes it difficult to reproduce the results and assess the method's robustness. Furthermore, the paper does not provide a clear explanation of how the clusters are used in the subsequent steps. For example, how are the representative molecules selected from each cluster? Is it based on some criteria like centroid distance or random selection? The paper should also clarify how the molecular docking results are integrated with the wet lab experiments to update the binding probabilities. A more detailed description of the experimental setup, including the number of molecules tested in each round, the criteria for selecting molecules for wet lab experiments, and the statistical methods used to analyze the results, is needed to fully evaluate the method's effectiveness.

To improve the paper, the authors should provide a more detailed description of the clustering algorithm, including the specific algorithm used, the distance metric, and any parameters involved. They should also clarify how the clusters are used in the subsequent steps, including the selection of representative molecules and the integration of docking and wet lab results. The authors should also provide more details about the experimental setup, including the number of molecules tested in each round, the criteria for selecting molecules for wet lab experiments, and the statistical methods used to analyze the results. For example, what is the distribution of the number of molecules tested per round? What is the criteria for selecting molecules for wet lab experiments (e.g., based on docking scores, or randomly)? What statistical tests were used to compare the results of different rounds? Providing these details would significantly improve the reproducibility and credibility of the results. Furthermore, the authors should consider including a more detailed discussion of the limitations of their method, such as the computational cost of molecular docking and the potential for bias in wet lab experiments.

Finally, the authors should consider including a more detailed discussion of the potential impact of their method on the field of drug discovery. For example, how does their method compare to existing approaches in terms of efficiency and effectiveness? What are the potential advantages and disadvantages of their method? What are the potential future directions for research in this area? Addressing these questions would help to contextualize the contribution of their work and highlight its potential impact. The authors should also consider including a more detailed discussion of the potential ethical implications of their method, such as the potential for misuse of the method to accelerate the discovery of harmful compounds. Addressing these ethical considerations would help to ensure that the method is used responsibly and ethically.

### Questions

1. The authors propose a novel method for active probabilistic drug discovery (APDD) which is a novel combination of three consecutive steps: (1) molecules are partitioned into clusters using probabilistic clustering algorithms with substructure similarity as the similarity metric; (2) representative molecules from each cluster are selected for molecular docking simulations using VinaGPU+; (3) the binding probabilities of the molecules are updated based on the results of the molecular docking simulations and wet lab experiments. The authors demonstrate the effectiveness of their method using two benchmark datasets.
2. The authors propose a novel method for active probabilistic drug discovery (APDD) which is a novel combination of three consecutive steps: (1) molecules are partitioned into clusters using probabilistic clustering algorithms with substructure similarity as the similarity metric; (2) representative molecules from each cluster are selected for molecular docking simulations using VinaGPU+; (3) the binding probabilities of the molecules are updated based on the results of the molecular docking simulations and wet lab experiments. The authors demonstrate the effectiveness of their method using two benchmark datasets.
3. The authors propose a novel method for active probabilistic drug discovery (APDD) which is a novel combination of three consecutive steps: (1) molecules are partitioned into clusters using probabilistic clustering algorithms with substructure similarity as the similarity metric; (2) representative molecules from each cluster are selected for molecular docking simulations using VinaGPU+; (3) the binding probabilities of the molecules are updated based on the results of the molecular docking simulations and wet lab experiments. The authors demonstrate the effectiveness of their method using two benchmark datasets.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
