### Summary

This paper proposes a new perspective on domain generalization (DG) by establishing a connection between the concept of "environment" in DG and the concept of "context" in large language models (LLMs). The authors argue that in-context learning (ICL) in LLMs can be leveraged to address the DG problem. They propose a new algorithm called In-Context Risk Minimization (ICRM) that trains a machine to predict the target label based on the input and the context of previously observed examples from the same environment. The authors provide theoretical results that show that ICRM can zoom-in on the empirical risk minimizer of the test environment and achieve competitive out-of-distribution performance. They also conduct extensive experiments to demonstrate the efficacy of ICRM on several DG benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel perspective on DG by connecting it to ICL in LLMs, which is a relatively new and under-explored area. This perspective opens up new possibilities for addressing the DG problem.
2. The authors provide a thorough theoretical analysis of ICRM, including several theorems and propositions that demonstrate its properties and performance guarantees. The theoretical results are well-supported by the experiments.
3. The experimental results show that ICRM outperforms several state-of-the-art DG algorithms on multiple benchmarks. The authors also conduct extensive ablations to analyze the impact of different components of ICRM.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the test environments are sufficiently similar to the training environments, which may not always be the case in real-world scenarios. The authors should discuss the limitations of ICRM when the test environments are significantly different from the training environments. Specifically, the paper lacks a discussion on the potential for negative transfer when the test environment exhibits distributions that are drastically different from the training environments, which could lead to a degradation in performance rather than the claimed outperformance. The theoretical guarantees provided may not hold under such conditions, and this needs to be explicitly addressed.
2. The paper does not provide a detailed analysis of the computational complexity of ICRM. The authors should discuss the computational cost of ICRM compared to other DG algorithms. The analysis should include not only the training time but also the inference time, especially considering the sequential nature of processing context examples. A comparison with other methods in terms of FLOPs or memory usage would also be beneficial.
3. The paper does not discuss the potential ethical implications of using ICL for DG. For example, if the context contains biased or discriminatory information, ICRM may learn to make biased or discriminatory predictions. The paper should address this concern and propose ways to mitigate it. Specifically, the paper should discuss how the selection of context examples could inadvertently introduce bias and how to ensure that the context is representative and fair.

### Suggestions

The paper should include a more thorough discussion on the limitations of ICRM when faced with significant distribution shifts between training and testing environments. It is crucial to analyze scenarios where the test environment exhibits distributions that are drastically different from the training environments, potentially leading to negative transfer. The authors should explore the conditions under which the theoretical guarantees of ICRM might break down and provide empirical evidence to support these claims. This could involve experiments with datasets that have more pronounced domain shifts, or by introducing synthetic shifts to existing datasets. Furthermore, the paper should discuss potential strategies to mitigate negative transfer, such as using domain adaptation techniques or incorporating regularization methods that encourage robustness to distribution shifts. A more detailed analysis of the sensitivity of ICRM to the degree of distribution shift would greatly enhance the paper's practical relevance.

To address the computational complexity concerns, the authors should provide a detailed analysis of the time and space complexity of ICRM, including both training and inference phases. This analysis should compare ICRM with other state-of-the-art domain generalization algorithms, considering factors such as the number of parameters, the number of training iterations, and the cost of processing context examples. The authors should also discuss the scalability of ICRM to large datasets and complex models. Furthermore, the paper should include a discussion of potential optimizations that could reduce the computational cost of ICRM, such as using efficient attention mechanisms or model compression techniques. A clear understanding of the computational trade-offs is essential for assessing the practical applicability of ICRM.

Finally, the paper needs to address the potential ethical implications of using ICL for DG. The authors should discuss how the selection of context examples could inadvertently introduce bias and how to ensure that the context is representative and fair. This discussion should include concrete examples of how biased context could lead to discriminatory predictions. The authors should also propose methods to mitigate these risks, such as using debiasing techniques or incorporating fairness constraints into the training process. It is important to consider the potential for ICRM to amplify existing biases in the data and to develop strategies to prevent this from happening. A thorough discussion of these ethical considerations is crucial for responsible research and development.

### Questions

1. Can the authors provide more insights into the relationship between ICL and DG? How does ICL help to address the DG problem?
2. Can the authors provide more details about the implementation of ICRM? What are the key design choices and hyperparameters?
3. How does ICRM perform on other DG benchmarks? Can the authors provide more experimental results to demonstrate the generalizability of ICRM?
4. How does the choice of context affect the performance of ICRM? What are the best practices for selecting the context examples?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
