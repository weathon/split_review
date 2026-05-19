### Summary

The paper introduces ProvCreator, a novel framework designed to synthesize system provenance graphs with rich textual attributes, addressing the challenge of data imbalance in cybersecurity datasets. ProvCreator learns the joint distribution of node attributes and graph structures conditioned on program class labels, enabling the targeted generation of realistic provenance graphs for underrepresented programs. The framework combines a graph diffusion model for structure generation with a transformer-based model for attribute generation, ensuring both structural and attribute fidelity. The authors demonstrate that ProvCreator produces synthetic graphs with higher fidelity and improves the performance of downstream tasks such as program classification and malware detection.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. ProvCreator is the first framework to simultaneously generate both graph structure and rich textual node attributes for system provenance graphs, addressing a critical gap in existing synthetic data generation methods.
2. The paper provides a thorough evaluation of ProvCreator, demonstrating its superiority over baseline methods in terms of structural fidelity, attribute fidelity, and downstream utility. The use of multiple metrics and downstream tasks provides strong evidence for the effectiveness of the approach.
3. The methodology is well-explained, with clear descriptions of the graph diffusion model, transformer architecture, and training process. The inclusion of Algorithm 1 provides a helpful overview of the generation pipeline.

### Weaknesses

#### Some Related Works


#### comment

1. The evaluation primarily focuses on two program types (svchost.exe and powershell.exe). While these are important, demonstrating the framework's effectiveness on a more diverse set of programs would strengthen the generalizability claims. Specifically, the paper lacks an analysis of how the framework performs with programs exhibiting significantly different behavioral patterns or system call frequencies. This limited scope makes it difficult to ascertain whether the observed improvements are specific to these two programs or if they generalize to a broader range of system activities.
2. The paper acknowledges that port number generation is not effective but doesn't explore potential solutions. This is a notable limitation given the importance of network communication in many cybersecurity scenarios. The lack of a robust method for generating realistic port numbers could lead to synthetic data that does not accurately reflect real-world network activity, potentially limiting the utility of the generated graphs for tasks involving network analysis.
3. The paper could benefit from a more detailed discussion of the computational cost and scalability of ProvCreator. Generating large, complex provenance graphs with rich textual attributes is likely resource-intensive. The paper does not provide any analysis of the time and memory requirements for generating synthetic graphs of varying sizes, which is crucial for assessing the practical applicability of the framework. Furthermore, the paper does not discuss the potential bottlenecks in the generation process, such as the transformer-based attribute generation, which could limit the scalability of the approach.
4. While the paper mentions potential applications beyond cybersecurity, it lacks concrete examples or evaluations in other domains. This limits the impact of the work. The paper does not explore how the framework could be adapted to domains with different types of graph structures or node attributes, such as social networks or knowledge graphs. Without such examples, it is difficult to assess the true versatility of the proposed approach.

### Suggestions

To address the limited evaluation scope, the authors should include a more diverse set of programs in their experiments. This could involve selecting programs with varying system call patterns, resource usage, and interaction frequencies. For example, including programs that perform file I/O intensive tasks, network communication, or database interactions would provide a more comprehensive evaluation of the framework's capabilities. Furthermore, the authors should analyze the performance of ProvCreator on programs with different levels of complexity, ranging from simple utilities to more complex applications. This would help to demonstrate the generalizability of the approach and identify potential limitations. The evaluation should also include a quantitative analysis of the structural and attribute fidelity for each program, allowing for a more detailed comparison of the generated graphs. Additionally, the authors should consider evaluating the impact of the generated data on downstream tasks for these diverse programs, such as anomaly detection or intrusion detection, to further validate the utility of the synthetic data.

To improve the handling of port number generation, the authors should explore alternative methods that can generate more realistic port numbers. This could involve incorporating a separate model specifically trained for port number generation or using a conditional generation approach that takes into account the context of the network communication. For example, the model could be conditioned on the source and destination IP addresses, as well as the protocol being used, to generate more plausible port numbers. The authors should also investigate the impact of inaccurate port numbers on downstream tasks, such as malware detection, to determine the extent to which this limitation affects the overall performance of the framework. A detailed analysis of the distribution of port numbers in real-world datasets and a comparison with the distribution of generated port numbers would also be beneficial. Furthermore, the authors should consider the impact of other network-related attributes, such as TCP flags or packet sizes, and explore methods to generate these attributes more accurately.

To address the lack of discussion on computational cost and scalability, the authors should provide a detailed analysis of the time and memory requirements for generating synthetic graphs of varying sizes. This should include a breakdown of the computational cost of each step in the generation process, such as graph structure generation and attribute generation. The authors should also discuss the potential bottlenecks in the generation process and explore strategies for optimizing the performance of the framework. For example, they could investigate the use of parallel processing or distributed computing to speed up the generation process. Furthermore, the authors should evaluate the scalability of the framework by generating synthetic graphs of increasing size and analyzing the impact on performance. This would help to determine the practical limitations of the approach and identify areas for future improvement. Finally, the authors should provide concrete examples of how the framework could be applied to other domains, such as social networks or knowledge graphs, and include evaluations in these domains to demonstrate the versatility of the approach.

### Questions

1. How does ProvCreator handle programs with highly variable or complex runtime behaviors? Are there limitations on the types of program behaviors that can be effectively synthesized?
2. What are the computational requirements for generating large provenance graphs with rich textual attributes? How does the generation time scale with graph size and complexity?
3. How sensitive is ProvCreator to the choice of hyperparameters, such as the diffusion steps or transformer architecture? Is there a risk of overfitting to the training data?
4. Have you explored using ProvCreator to generate synthetic data for other security tasks, such as anomaly detection or threat intelligence?
5. What are the potential risks of using synthetic provenance data for training security models? Could adversaries exploit the characteristics of the synthetic data to evade detection?

### Rating

6

### Confidence

4

**********
