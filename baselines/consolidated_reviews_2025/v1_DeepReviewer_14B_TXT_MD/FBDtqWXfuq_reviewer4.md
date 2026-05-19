### Summary

This paper proposes a new setting, Modality-Collaborated Federated Learning (MCFL), designed to facilitate collaboration among uni-modal clients with different data modalities. The authors also propose a framework called FedCola, based on a modality-agnostic transformer, to address the challenges of model heterogeneity and modality gaps in MCFL. The experimental results show that FedCola outperforms existing solutions in comprehensive scenarios.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel setting in federated learning (FL), called Modality-Collaborated Federated Learning (MCFL), which is an interesting and practical problem.
2. The authors propose a framework called FedCola, based on a modality-agnostic transformer, to address the challenges of model heterogeneity and modality gaps in MCFL. The proposed framework is well-motivated and technically sound.
3. The experimental results show that FedCola outperforms existing solutions in comprehensive scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed MCFL setting and FedCola framework are evaluated on a limited number of datasets and scenarios. It would be beneficial to conduct more experiments on a wider range of datasets and scenarios to further validate the effectiveness and generalizability of the proposed approach. Specifically, the current evaluation lacks diversity in terms of data modalities and task complexity. For instance, the datasets used seem to focus on relatively simple classification tasks, and it is unclear how the proposed method would perform on more complex tasks such as object detection or sequence-to-sequence learning. Furthermore, the evaluation does not explore scenarios with a larger number of modalities or more heterogeneous data distributions across clients, which are common in real-world applications.
2. The paper does not provide a detailed analysis of the computational complexity and communication overhead of the proposed FedCola framework. It is important to analyze the scalability and efficiency of the proposed approach, especially when dealing with large-scale datasets and a large number of clients. The analysis should include a breakdown of the computational cost associated with the modality-agnostic transformer, the parameter sharing mechanism, and the aggregation process. Additionally, the communication overhead should be quantified in terms of the number of parameters transmitted between clients and the server, and how this scales with the number of clients and modalities.

### Suggestions

To address the limitations in the evaluation, the authors should consider expanding their experiments to include a more diverse set of datasets and scenarios. This should include datasets with more complex tasks, such as object detection, semantic segmentation, or sequence-to-sequence learning. Furthermore, the evaluation should include scenarios with a larger number of modalities and more heterogeneous data distributions across clients. For example, the authors could explore datasets where each client has access to a different subset of modalities, or where the data distributions within each modality vary significantly across clients. This would provide a more comprehensive assessment of the proposed method's effectiveness and generalizability. Additionally, the authors should consider evaluating the performance of FedCola under different levels of data heterogeneity and client availability, as these factors can significantly impact the performance of federated learning algorithms.

To address the lack of computational and communication complexity analysis, the authors should provide a detailed breakdown of the computational cost associated with each component of the FedCola framework. This should include the cost of the modality-agnostic transformer, the parameter sharing mechanism, and the aggregation process. The analysis should also consider the impact of different hyperparameter settings on the computational cost. Furthermore, the authors should quantify the communication overhead in terms of the number of parameters transmitted between clients and the server. This analysis should consider how the communication overhead scales with the number of clients and modalities. The authors should also compare the computational and communication costs of FedCola with those of existing federated learning methods, such as Uni-FedAVG and CreamFL, to demonstrate the efficiency of the proposed approach. This analysis should be presented in a clear and concise manner, with appropriate tables and figures to facilitate understanding.

Finally, the authors should also consider providing a more detailed discussion of the limitations of the proposed approach. This should include a discussion of the potential challenges and limitations of applying FedCola to real-world scenarios, such as the impact of data privacy regulations, the potential for bias in the data, and the challenges of deploying the method in resource-constrained environments. This discussion should also include a comparison of the proposed method with other approaches for multi-modal federated learning, highlighting the advantages and disadvantages of each approach. This would provide a more balanced and comprehensive assessment of the proposed method and its potential impact on the field.

### Questions

1. How does the proposed MCFL setting and FedCola framework perform on a wider range of datasets and scenarios?
2. What is the computational complexity and communication overhead of the proposed FedCola framework, and how does it compare to existing methods?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
