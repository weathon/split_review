### Summary

This paper proposes a novel framework, FedDPCont, to address the challenge of local openset noisy labels in federated learning. The authors define the openset noise problem in FL, propose a label communication mechanism with differential privacy, and demonstrate the effectiveness of FedDPCont through experiments on both synthetic and real-world datasets.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper introduces a new problem setting in federated learning, focusing on local openset noisy labels, which is more practical than the existing noisy label settings.
2. The authors provide a comprehensive theoretical analysis of FedDPCont, including convergence and robustness to label noise.

### Weaknesses

#### Some Related Works

[1] OpenFed: Open-set Federated Learning with Dynamic Client-influential Feature Representation
[2] OpenGSL: A Comprehensive Framework of Open Graph Signal Processing

#### comment

1. The paper does not compare FedDPCont with existing open-set federated learning methods, such as OpenFed [1] and OpenGSL [2]. Including these comparisons would help to better demonstrate the effectiveness of the proposed method.
2. The paper does not discuss the relationship between FedDPCont and existing federated learning methods that address label noise, such as FedProx and FedDyn. A discussion of how FedDPCont differs from these methods would help to clarify its unique contributions.
3. The paper does not provide a detailed analysis of the computational overhead of FedDPCont. This is an important consideration for practical applications of federated learning.
4. The paper does not discuss the limitations of the proposed method. A discussion of the limitations of FedDPCont would help to provide a more balanced view of its contributions.

### Suggestions

The paper introduces an interesting problem setting of local openset noisy labels in federated learning, but it needs further clarification and analysis to fully demonstrate its practical value and novelty. Specifically, the lack of comparison with existing open-set federated learning methods is a significant gap. The authors should include a thorough comparison with methods like OpenFed [1], which explicitly addresses open-set scenarios, and OpenGSL [2], which uses graph signal processing for open-set problems. This comparison should not only focus on performance metrics but also discuss the underlying assumptions and mechanisms of each method, highlighting the specific advantages and disadvantages of FedDPCont in different scenarios. For example, how does FedDPCont handle situations where the open classes are completely novel versus those where some open classes overlap with the seen classes? A detailed analysis of these aspects would help to position FedDPCont more clearly within the existing literature.

Furthermore, the paper needs to better contextualize FedDPCont within the broader landscape of federated learning methods designed for label noise. While the authors mention that FedProx and FedDyn are designed for closed-set scenarios, a more detailed discussion of how FedDPCont differs in its approach is needed. For instance, how does the contrastive learning mechanism of FedDPCont compare to the regularization techniques used in FedProx or the dynamic client selection strategies in FedDyn? A deeper analysis of these differences would help to clarify the unique contributions of FedDPCont. Additionally, the paper should include an analysis of the computational overhead of FedDPCont. This analysis should consider the computational cost of the label differential privacy mechanism and the contrastive learning component. It would be beneficial to compare the computational cost of FedDPCont with other federated learning methods, especially those that address label noise. This analysis should also consider the impact of different hyperparameter settings on the computational cost of FedDPCont.

Finally, the paper should include a more detailed discussion of the limitations of FedDPCont. For example, how does FedDPCont perform when the openset classes are highly imbalanced? Does the method have any limitations in terms of the number of clients or the size of the datasets? A discussion of these limitations would help to provide a more balanced view of the contributions of FedDPCont. The authors should also discuss potential future research directions that could address these limitations. For example, could the method be extended to handle more complex open-set scenarios, such as those involving hierarchical open classes? Could the method be combined with other techniques, such as knowledge distillation, to further improve its performance? Addressing these questions would help to provide a more complete picture of the potential of FedDPCont and its future research directions.

### Questions

1. How does FedDPCont handle situations where the openset classes are completely novel versus those where some openset classes overlap with the seen classes?
2. What are the computational costs associated with FedDPCont, and how do they compare to other federated learning methods?
3. How does FedDPCont perform when the openset classes are highly imbalanced?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
