### Summary

The paper introduces a novel approach to address the issue of model collapse in Deep Canonical Correlation Analysis (DCCA) within the context of Multi-View Representation Learning (MVRL). The authors identify that DCCA-based methods, despite their initial promise, suffer from a significant decline in performance as training progresses, a phenomenon they define as model collapse. To tackle this challenge, they propose NR-DCCA, a method equipped with a noise regularization (NR) approach. The core idea behind NR is to enforce the Correlation Invariant Property (CIP), which ensures that the correlation with random data remains invariant before and after the transformation. The authors provide a theoretical analysis demonstrating that CIP is crucial for preventing model collapse and that their NR approach effectively induces this property. They also develop a framework for constructing synthetic data with varying degrees of common and complementary information to evaluate MVRL methods comprehensively. The empirical results on both synthetic and real-world datasets show that NR-DCCA outperforms existing methods consistently and stably. Furthermore, the authors argue that their proposed NR approach can be generalized to other DCCA-based methods, broadening its applicability.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper presents a novel approach to tackling the model collapse issue in DCCA-based methods for Multi-View Representation Learning (MVRL). The introduction of noise regularization (NR) to enforce the Correlation Invariant Property (CIP) is a creative solution that combines theoretical insights with practical implementation. The authors provide a rigorous theoretical foundation for their method, demonstrating that CIP is both necessary and sufficient for preventing model collapse. The development of a synthetic data framework for evaluating MVRL methods is another significant contribution, allowing for a more controlled and comprehensive assessment of different approaches. The empirical validation of NR-DCCA on both synthetic and real-world datasets showcases the effectiveness and stability of the proposed method. The paper is well-structured and clearly written, making it accessible to readers with a background in machine learning and representation learning. The authors also provide a thorough comparison with existing methods, highlighting the advantages of NR-DCCA in terms of performance and stability. Overall, the paper makes a valuable contribution to the field of MVRL by addressing a critical issue and proposing a robust solution with strong theoretical and empirical support.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's primary weakness lies in the limited scope of its empirical validation. While the authors demonstrate the effectiveness of NR-DCCA on several datasets, the range of applications and data modalities tested is relatively narrow. To strengthen the paper, it would be beneficial to evaluate the method on a more diverse set of real-world datasets, including those with higher dimensionality, different types of noise, and more complex relationships between views. For instance, testing on datasets with varying degrees of missing data or different types of non-linear relationships could provide a more comprehensive understanding of the method's robustness and generalizability. Additionally, the paper could explore the performance of NR-DCCA in scenarios with more than two views, as the current evaluation primarily focuses on pairwise view settings.

2. Another area for improvement is the depth of the theoretical analysis. While the authors establish the connection between CIP and the prevention of model collapse, the theoretical framework could be expanded to provide more insights into the behavior of NR-DCCA under different conditions. For example, a more detailed analysis of how the noise regularization parameter affects the convergence and stability of the method would be valuable. Furthermore, exploring the theoretical limitations of the approach, such as scenarios where CIP might not be sufficient to prevent model collapse, would add depth to the analysis. The paper could also benefit from a discussion on the computational complexity of the proposed method, especially in comparison to existing DCCA-based approaches.

3. The paper could also benefit from a more thorough discussion of the limitations of the proposed method. For instance, the authors could address the potential sensitivity of NR-DCCA to the choice of noise distribution or the computational overhead introduced by the noise regularization process. Additionally, a discussion on the interpretability of the learned representations and how they relate to the original data would be valuable. The paper should also acknowledge the potential challenges in applying NR-DCCA to very high-dimensional data or datasets with a large number of views, where the computational cost might become prohibitive.

### Suggestions

To enhance the empirical validation of NR-DCCA, the authors should consider expanding their experiments to include a wider variety of real-world datasets. This could involve incorporating datasets from different domains, such as medical imaging, natural language processing, or time-series analysis. For example, evaluating the method on datasets with varying degrees of class imbalance or different types of noise distributions would provide a more comprehensive understanding of its robustness. Furthermore, the authors should explore the performance of NR-DCCA on datasets with more than two views, as many real-world problems involve multiple sources of data. This could involve adapting the current framework to handle multi-view data or exploring alternative approaches for extending NR-DCCA to higher-order settings. Additionally, it would be beneficial to compare the performance of NR-DCCA with other state-of-the-art multi-view representation learning methods, including those that do not rely on DCCA, to provide a more comprehensive evaluation of its effectiveness.

To strengthen the theoretical analysis, the authors should delve deeper into the relationship between the noise regularization parameter and the convergence properties of NR-DCCA. This could involve analyzing the impact of different noise levels on the optimization landscape and the stability of the learned representations. Furthermore, the authors should explore the theoretical limitations of the approach, such as scenarios where the Correlation Invariant Property (CIP) might not be sufficient to prevent model collapse. This could involve identifying specific conditions under which the method might fail or providing a theoretical bound on the performance of NR-DCCA. A more detailed analysis of the computational complexity of the proposed method would also be valuable, especially in comparison to existing DCCA-based approaches. This could involve deriving the time and space complexity of the algorithm and discussing its scalability to large datasets.

Finally, the authors should provide a more thorough discussion of the limitations of the proposed method. This could involve addressing the potential sensitivity of NR-DCCA to the choice of noise distribution and the computational overhead introduced by the noise regularization process. The authors should also discuss the interpretability of the learned representations and how they relate to the original data. This could involve visualizing the learned representations or providing a qualitative analysis of their semantic meaning. Furthermore, the paper should acknowledge the potential challenges in applying NR-DCCA to very high-dimensional data or datasets with a large number of views, where the computational cost might become prohibitive. The authors could also suggest potential future directions for research, such as exploring alternative noise regularization techniques or developing more efficient algorithms for computing the correlations between multi-view data.

### Questions

1. Could the authors elaborate on the choice of noise distribution used in the noise regularization process? How sensitive is the performance of NR-DCCA to the specific type of noise used, and are there any guidelines for selecting an appropriate noise distribution for different types of data?

2. The paper primarily focuses on two-view settings. How does NR-DCCA extend to scenarios with more than two views? Are there any modifications or extensions to the framework that are needed to handle multi-view data, and how does the performance of the method scale with the number of views?

3. The authors mention that the proposed NR approach can be generalized to other DCCA-based methods. Could they provide more details on the specific steps involved in applying NR to other variants of DCCA, and are there any limitations or challenges in this generalization process?

4. How does the computational complexity of NR-DCCA compare to existing DCCA-based methods, especially when dealing with large datasets or high-dimensional data? Are there any optimizations or approximations that can be used to improve the efficiency of the method?

5. The paper introduces a framework for constructing synthetic data with varying degrees of common and complementary information. Could the authors provide more details on the specific parameters used to control the amount of common and complementary information in the synthetic data, and how do these parameters affect the performance of different MVRL methods?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
