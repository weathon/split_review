### Summary

This paper investigates the effect of measurement scale on the structure learning of DAGs. The authors show that the measurement scale can affect the structure learning of DAGs, and provide theoretical results on the conditions under which the measurement scale can lead to incorrect structure learning. The authors also propose a new loss function, the Scale Robust Loss (SRL), which is designed to be robust to the effects of measurement scale. The paper provides empirical results on both synthetic and real-world data to demonstrate the effectiveness of the proposed SRL.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper addresses an important and relevant problem in the field of structure learning of DAGs. The effect of measurement scale on structure learning is a crucial issue that has not been adequately addressed in the literature.

2. The paper provides a comprehensive theoretical analysis of the effect of measurement scale on structure learning. The authors provide theoretical results on the conditions under which the measurement scale can lead to incorrect structure learning, and show that the measurement scale can affect the structure learning of DAGs even when the data is normalized.

3. The paper proposes a new loss function, the Scale Robust Loss (SRL), which is designed to be robust to the effects of measurement scale. The authors provide empirical results on both synthetic and real-world data to demonstrate the effectiveness of the proposed SRL.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on the effect of measurement scale on structure learning of DAGs, but does not provide a comprehensive comparison with other methods that address the same problem. It would be beneficial to compare the proposed SRL with other existing methods that aim to address the issue of measurement scale in structure learning.

2. The paper assumes that the data is generated from a DAG, which may not always be the case in real-world applications. It would be beneficial to discuss the limitations of the proposed method when the data is not generated from a DAG, and provide some insights on how the method can be extended to handle non-DAG data.

3. The paper does not provide a detailed analysis of the computational complexity of the proposed SRL. It would be beneficial to provide a detailed analysis of the computational complexity of the proposed SRL, and compare it with other existing methods.

### Suggestions

The paper would be significantly strengthened by a more thorough comparison with existing methods that address the issue of measurement scale in structure learning. While the authors introduce the Scale Robust Loss (SRL), they do not adequately position it within the broader landscape of techniques designed to mitigate scale-related problems. For instance, methods that explicitly normalize or whiten data before structure learning could be considered as baselines. A detailed comparison should not only focus on performance metrics but also on the computational cost and the sensitivity to different types of data distributions. Furthermore, the authors should discuss the limitations of their approach in comparison to these methods, highlighting scenarios where SRL might be preferred and where it might fall short. This would provide a more complete picture of the contribution of the proposed method and its practical applicability.

Additionally, the assumption that the data is generated from a DAG is a significant limitation that needs to be addressed more thoroughly. While the authors acknowledge this limitation, they do not provide a detailed discussion of the potential impact of this assumption on the performance of their method. In real-world applications, the underlying data generating process may not always be a DAG, and the proposed method might not be directly applicable. The authors should explore the robustness of their method to violations of this assumption, and discuss potential strategies for extending their approach to handle non-DAG data. This could involve exploring alternative graph representations or incorporating mechanisms to detect and correct for cyclic dependencies. A more detailed discussion of these limitations would provide a more realistic assessment of the method's applicability and guide future research directions.

Finally, a more detailed analysis of the computational complexity of the proposed SRL is needed. While the authors mention that the computational complexity is similar to that of the MMSE, they do not provide a formal analysis of the time and space complexity of the algorithm. This analysis should include a breakdown of the computational cost of each step of the algorithm, and a comparison with the computational cost of other existing methods. Furthermore, the authors should discuss the scalability of their method to large-scale datasets, and provide insights on how to optimize the implementation for practical applications. This would provide a more complete understanding of the computational trade-offs associated with the proposed method and its suitability for different types of applications.

### Questions

1. How does the proposed SRL compare to other existing methods that address the issue of measurement scale in structure learning?

2. How does the proposed method perform when the data is not generated from a DAG?

3. What is the computational complexity of the proposed SRL, and how does it compare to other existing methods?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
