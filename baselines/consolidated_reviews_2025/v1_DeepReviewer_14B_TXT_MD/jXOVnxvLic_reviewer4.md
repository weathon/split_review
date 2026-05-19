### Summary

This paper introduces a neural organoid simulation framework (NOSF) designed to realistically reconstruct the details of interaction experiments with real mature organoids. The framework utilizes advanced neural computing models to enable stimulation, response, and learning functionalities. Additionally, an intelligent expansion platform based on spiking neural networks is established to facilitate the exploration of organoid-machine collaborative intelligence. The authors also present a benchmark for evaluating the framework, which includes a set of real organoid experimental data and a series of evaluation metrics. The experimental results demonstrate that the simulation framework exhibits outstanding simulation capabilities and shares similarities with real organoid experiments in various aspects. Furthermore, the performance of the combination with the intelligent expansion platform is comparable to pure AI algorithms in a basic classification task.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel neural organoid simulation framework (NOSF) that realistically reconstructs the details of interaction experiments with real mature organoids. This framework utilizes advanced neural computing models to enable stimulation, response, and learning functionalities, which is a significant contribution to the field.

2. The establishment of an intelligent expansion platform based on spiking neural networks is a notable strength of the paper. This platform facilitates the exploration of organoid-machine collaborative intelligence, opening up new avenues for research and development in this area.

3. The paper presents a benchmark for evaluating the framework, which includes a set of real organoid experimental data and a series of evaluation metrics. This benchmark provides a valuable resource for assessing the performance and capabilities of the simulation framework.

4. The experimental results demonstrate that the simulation framework exhibits outstanding simulation capabilities and shares similarities with real organoid experiments in various aspects. This validates the effectiveness of the proposed framework and its potential for practical applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed framework. While the experimental results are promising, it is important to acknowledge any potential shortcomings or areas for improvement. For instance, the paper does not delve into the computational cost associated with the simulation, which could be a significant factor in its practical applicability. Furthermore, the scalability of the framework to larger and more complex organoid models is not addressed, leaving questions about its utility in more realistic scenarios. A thorough analysis of these limitations would provide a more balanced perspective on the framework's capabilities.

2. The paper could provide more details on the specific types of neural organoids used in the experiments and how the framework can be adapted to different types of organoids. The current description lacks the necessary detail to understand the biological variability and how the framework accounts for it. For example, the paper does not specify the stage of development of the organoids, their size, or the specific cell types present. This information is crucial for assessing the generalizability of the framework and its ability to simulate diverse organoid systems. Without this, it is difficult to ascertain the framework's robustness and applicability to different experimental settings.

### Suggestions

To enhance the paper, the authors should include a detailed analysis of the computational resources required by the simulation framework. This should include metrics such as memory usage, processing time, and energy consumption, especially as the complexity of the simulated organoid increases. Furthermore, the authors should discuss the scalability of the framework, specifically addressing how the computational cost scales with the size and complexity of the organoid model. This analysis should also consider the potential for parallelization and optimization techniques to improve the framework's efficiency. Providing this information will allow readers to better understand the practical limitations and potential of the framework for large-scale simulations. Additionally, the authors should explore the framework's performance with different organoid models, including variations in size, cell type composition, and developmental stage. This could involve simulating organoids with different levels of complexity and comparing the simulation results with experimental data. Such an analysis would provide valuable insights into the framework's generalizability and its ability to capture the nuances of different organoid systems. The authors should also discuss the parameters used to define the organoid model, such as the number of cell types, the connectivity patterns, and the specific signaling pathways included in the simulation. This would help readers understand the level of detail captured by the framework and its limitations in representing the full complexity of biological organoids.

Furthermore, the authors should provide a more detailed explanation of how the framework handles the inherent variability in biological systems. This could involve discussing the stochastic elements of the simulation, such as the random firing of neurons or the probabilistic nature of synaptic transmission. The authors should also address how the framework accounts for the variability in experimental data, such as differences in organoid growth or response to stimuli. This discussion should include an analysis of the sensitivity of the simulation results to changes in the model parameters and how the framework can be calibrated to match experimental observations. This would help readers understand the robustness of the framework and its ability to provide reliable predictions. Finally, the authors should consider including a more comprehensive comparison of the framework's performance with other existing simulation tools. This comparison should not only focus on the accuracy of the simulation results but also on the computational efficiency, scalability, and ease of use of the different tools. This would provide a more complete picture of the framework's strengths and weaknesses and help readers assess its value in the context of existing approaches.

### Questions

1. Could you provide more details on the computational resources required by the simulation framework? How does the framework scale with the size and complexity of the organoid model?

2. How does the framework handle the inherent variability in biological systems? Are there any measures taken to account for this variability in the simulation results?

### Rating

6

### Confidence

3

**********
