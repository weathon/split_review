### Summary

The paper proposes a framework to address the issue of "disguised procedural unfairness", where unfairness in a model's decision-making process may stem from changes to the neutral components of the data generating process, rather than the objective components. The authors propose a framework that decouples objectionable components from the data generating process, and making predictions only based on the neutral components. The framework utilizes reference points and a value instantiation rule to achieve this decoupling. The authors highlight the importance of considering all objectionable components, not just protected features, to address fairness issues comprehensively. The paper also discusses the relationship between the proposed framework and Rawls' difference principle, which is a key concept in fairness literature. The authors claim that their framework can be used to promote procedural fairness by ensuring that the data generating process is fair and unbiased.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper addresses an important and often overlooked issue in fairness literature, which is the potential for unfairness to arise from changes in the neutral components of the data generating process, rather than just the objective components. The authors propose a novel framework that decouples objectionable components from the data generating process, and makes predictions only based on the neutral components. This framework is based on the concept of Rawls' difference principle, which is a key concept in fairness literature. The authors also provide a detailed explanation of the proposed framework, including the value instantiation rule and the configuration of reference points. The paper also discusses the limitations of existing approaches that attempt to address unfairness by constraining model parameters, and argues that these approaches may not be sufficient to address the issue of disguised procedural unfairness.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed explanation of how the framework handles complex scenarios with multiple objectionable components. While the paper proposes a framework to decouple objectionable components, it does not provide sufficient details on how this framework would perform in scenarios with multiple, potentially interacting, objectionable components. The paper lacks a discussion on how the value instantiation rule and reference point configuration would be applied when multiple components are simultaneously altered. This is a significant limitation, as real-world data generating processes often involve multiple sources of bias and unfairness. The paper also does not provide a clear methodology for identifying and decoupling objectionable components from the data generating process. The paper introduces the concept of "disguaged procedural unfairness" and proposes a framework to address it, but it lacks a concrete methodology for identifying which components are objectionable and how to decouple them. The paper does not specify any criteria or techniques for determining which components are objectionable, nor does it provide a clear algorithm for decoupling them. This lack of a concrete methodology makes it difficult to apply the proposed framework in practice. The paper also does not provide a comprehensive evaluation of the proposed framework. The paper introduces a novel framework for addressing "disguaged procedural unfairness," but it does not provide a thorough evaluation of its performance. The paper lacks a comparison with existing fairness methods, and it does not provide any empirical evidence to demonstrate the effectiveness of the proposed framework. The paper should include experiments on benchmark datasets to evaluate the performance of the proposed framework and compare it with existing fairness methods.

### Suggestions

The paper should provide a more detailed explanation of how the proposed framework handles complex scenarios with multiple objectionable components. Specifically, the authors should discuss how the value instantiation rule and reference point configuration would be applied when multiple components are simultaneously altered. For example, if there are two objectionable components, A and B, the paper should explain how the framework would ensure that changes in A and B do not affect the decision-making process. The authors should also discuss the potential challenges in identifying and decoupling multiple objectionable components and provide concrete examples to illustrate these challenges. Furthermore, the paper should include a discussion on the computational complexity of the proposed framework when dealing with multiple objectionable components. This would help in understanding the scalability of the proposed approach. The authors should also consider providing a more detailed algorithm for decoupling the identified objectionable components from the data generating process. This algorithm should be detailed enough to be implemented in practice, and it should specify the steps involved in identifying and decoupling the components. The authors should also discuss the potential limitations of their methodology and provide guidance on how to overcome these limitations. A concrete example of how the methodology would be applied in a real-world scenario would also be beneficial.

The paper should provide a clear methodology for identifying and decoupling objectionable components from the data generating process. The authors should specify any criteria or techniques that can be used to determine which components are objectionable. For example, the paper could discuss how to use causal analysis or other techniques to identify the sources of bias and unfairness in the data generating process. The paper should also provide a clear algorithm for decoupling the identified objectionable components from the data generating process. This algorithm should be detailed enough to be implemented in practice, and it should specify the steps involved in identifying and decoupling the components. The authors should also discuss the potential limitations of their methodology and provide guidance on how to overcome these limitations. The paper should also include a more comprehensive evaluation of the proposed framework. The authors should conduct experiments on benchmark datasets to evaluate the performance of the proposed framework and compare it with existing fairness methods. The evaluation should include a variety of metrics to assess the effectiveness of the proposed framework in mitigating "disguaged procedural unfairness." The paper should also discuss the limitations of the evaluation and provide guidance on how to improve the framework in future work. The authors should also consider evaluating the framework under different scenarios, such as different types of bias and different levels of data quality. This would help in understanding the robustness of the proposed framework.

### Questions

1. How does the proposed framework handle complex scenarios with multiple objectionable components? Could you provide more details on how the framework would perform in such scenarios?
2. Could you provide a clear methodology for identifying and decoupling objectionable components from the data generating process? What criteria or techniques can be used to determine which components are objectionable?
3. Could you provide a comprehensive evaluation of the proposed framework? How does the framework perform compared to existing fairness methods?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
