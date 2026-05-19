### Summary

The paper studies the problem of comparing unpaired data from different modalities. The authors show that, under certain assumptions, the probability of unpaired data can be inferred by comparing the learned representations. The authors also introduce a Monte Carlo approximation method to improve the practical application of these insights. The paper validates its theoretical claims through experiments on both synthetic and real-world datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper provides a theoretical foundation for understanding and utilizing unpaired multimodal data, which is a significant contribution to the field of multimodal learning.
- The paper presents a clear and well-structured argument, supported by rigorous mathematical derivations.
- The paper includes a variety of experiments that effectively validate the theoretical claims, demonstrating the practical applicability of the proposed methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper assumes that the marginal distribution of the representations follows a uniform distribution on the hypersphere. However, this assumption may not hold in real-world scenarios. The authors should provide more discussion on the limitations of this assumption and its potential impact on the results.
- The paper only considers three modalities. It is unclear how the proposed method can be extended to more modalities. The authors should discuss the potential challenges and limitations of extending the method to more modalities.
- The paper does not provide a detailed analysis of the computational complexity of the proposed method. The authors should discuss the computational cost of the Monte Carlo approximation method and its scalability to large datasets.

### Suggestions

The paper's reliance on a uniform hypersphere assumption for representation distributions is a significant limitation that needs further exploration. While the authors justify this assumption by referencing prior work, it is crucial to acknowledge that real-world data distributions are rarely uniform. The authors should investigate the sensitivity of their method to deviations from this assumption. For instance, they could explore scenarios where the representation distributions are concentrated in specific regions of the hypersphere or exhibit multimodal structures. Furthermore, they should consider alternative distribution models that might better capture the characteristics of real-world data, such as Gaussian mixtures or non-parametric distributions. A more thorough analysis of the impact of this assumption on the accuracy and robustness of the proposed method is necessary to establish its practical applicability. The authors should also provide a more detailed discussion on the potential consequences of using this assumption in different application scenarios, highlighting the potential for biased or inaccurate results.

Extending the method to more than three modalities is a non-trivial task that requires careful consideration. The current formulation relies on pairwise comparisons, which may not be sufficient to capture the complex relationships between more than three modalities. The authors should discuss the potential challenges in generalizing their approach, such as the increased computational complexity and the need for more sophisticated aggregation techniques. For example, they could explore the use of tensor-based methods or graph-based approaches to model the relationships between multiple modalities. Furthermore, they should investigate the impact of the number of modalities on the performance of their method, identifying the point at which the performance degrades significantly. A more detailed analysis of the scalability of the method to a larger number of modalities is needed to assess its practical feasibility.

The lack of a detailed computational complexity analysis is a notable weakness. The authors should provide a more rigorous analysis of the time and space complexity of their Monte Carlo approximation method, including a breakdown of the computational cost of each step. They should also discuss the scalability of the method to large datasets and provide guidelines for choosing the number of Monte Carlo samples based on the available computational resources. Furthermore, they should compare the computational cost of their method with other existing approaches for multimodal learning. A more thorough analysis of the computational aspects of the method is necessary to assess its practical applicability in real-world scenarios.

### Questions

See Weaknesses.

### Rating

8

### Confidence

3

**********
