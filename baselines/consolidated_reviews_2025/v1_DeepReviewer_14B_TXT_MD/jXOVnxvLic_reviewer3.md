### Summary

This paper proposes a neural organoid simulation framework (NOSF) to realistically reconstruct various details of interaction experiments using real mature organoids. The framework employs advanced neural computing models as elements, harnessing AI methods to enable stimulation, response, and learning functionalities. An intelligent expansion platform is also established based on spiking neural network to facilitate the exploration of organoid-machine collaborative intelligence. In addition, the authors introduce a benchmark for evaluating the framework, including a set of real organoid experimental data and a series of evaluation metrics.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The authors propose the first neural organoid simulation framework to realistically reconstruct most of the details in real-world organoid interaction experiments while alleviating the enormous cost of repeated real-world experiments.
2. An organoid intelligence expansion platform is developed using the SNN algorithm to explore organoids-machine collaborative intelligence in a novel way.
3. The first benchmark is proposed for organoid simulation framework, including evaluation metrics and real-world organoid experiment data.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the proposed framework can realistically reconstruct most of the details in real-world organoid interaction experiments. However, the authors only evaluate the proposed framework on a simple classification task. It is unclear whether the proposed framework can be applied to more complex tasks. The evaluation should include tasks that probe the framework's ability to model complex spatiotemporal dynamics and non-linear interactions, which are crucial for realistic organoid simulations. For instance, the framework's performance on tasks involving pattern formation or chaotic behavior would be more convincing.
2. The authors claim that the proposed framework can alleviate the enormous cost of repeated real-world organoid experiments. However, the authors do not provide any evidence to support this claim. It is unclear how much money and time can be saved by using the proposed framework compared to conducting real-world organoid experiments. A detailed cost analysis, including the computational resources required for the simulation and the time needed to set up and run the framework, should be provided. Furthermore, a comparison with the costs associated with actual biological experiments is necessary to validate this claim.
3. The authors claim that the proposed framework is based on advanced neural computing models. However, the authors do not explain why they chose these models and how they are advanced. The specific architectural choices and the rationale behind them are not clearly articulated. For example, the authors should justify the use of specific types of neural networks (e.g., recurrent, convolutional, spiking) and explain how these choices align with the biological processes they aim to simulate. A more detailed discussion of the model's limitations and assumptions is also needed.
4. The authors claim that the proposed framework can facilitate the exploration of organoid-machine collaborative intelligence. However, the authors do not provide any concrete examples of how this can be achieved. The paper lacks a clear demonstration of how the framework can be used to generate testable hypotheses about organoid behavior or how it can be integrated with experimental data to guide future research. The authors should provide specific use cases that illustrate the potential of the framework for advancing our understanding of organoid intelligence.
5. The authors propose a benchmark for evaluating the framework. However, the authors do not compare the performance of the framework with other existing methods or frameworks. Without a comparative analysis, it is difficult to assess the relative strengths and weaknesses of the proposed framework. The authors should compare their framework with existing computational models of neural systems or other relevant simulation tools to demonstrate its advantages and limitations.

### Suggestions

To address the lack of evaluation on complex tasks, the authors should consider incorporating more challenging benchmarks that assess the framework's ability to model intricate biological phenomena. This could include tasks such as simulating the response of organoids to different types of stimuli, modeling the development of specific neural patterns, or predicting the behavior of organoids under various experimental conditions. The evaluation should not only focus on classification accuracy but also on the framework's ability to capture the underlying dynamics and non-linear interactions within the organoid system. Furthermore, the authors should provide a detailed analysis of the framework's performance on these complex tasks, including a discussion of its limitations and potential areas for improvement. This would provide a more comprehensive assessment of the framework's capabilities and its potential for real-world applications.

To substantiate the claim regarding cost reduction, the authors should provide a detailed cost analysis that compares the expenses associated with the proposed framework to those of traditional organoid experiments. This analysis should include the costs of computational resources, such as hardware and software, as well as the time required to set up and run the simulations. The authors should also consider the costs associated with consumables, personnel, and equipment maintenance in traditional experiments. A clear comparison of these costs would provide a more concrete understanding of the potential savings offered by the proposed framework. Furthermore, the authors should discuss the limitations of the cost analysis and acknowledge any assumptions made in the comparison. This would provide a more balanced and realistic assessment of the framework's economic benefits.

To clarify the choice of neural computing models, the authors should provide a more detailed explanation of the specific architectures used in the framework and the rationale behind these choices. This should include a discussion of the biological plausibility of the chosen models and how they relate to the underlying neural processes in organoids. The authors should also justify the use of specific types of neural networks (e.g., recurrent, convolutional, spiking) and explain how these choices align with the biological processes they aim to simulate. A more detailed discussion of the model's limitations and assumptions is also needed. Furthermore, the authors should compare their chosen models with other existing models and explain why their approach is more suitable for simulating organoid behavior. This would provide a more comprehensive understanding of the framework's theoretical foundations and its potential for advancing our understanding of organoid intelligence.

### Questions

Please refer to the weaknesses.

### Rating

3

### Confidence

3

**********
