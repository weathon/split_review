### Summary

The paper proposes a novel method called AbeT for out-of-distribution (OOD) detection. AbeT combines a learned temperature and an energy score to improve OOD detection performance. The authors demonstrate the effectiveness of AbeT in classification, object detection, and semantic segmentation tasks. They also provide empirical insights into how the model learns to distinguish between in-distribution and OOD samples.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to OOD detection by combining a learned temperature and an energy score. This combination is shown to be effective in improving OOD detection performance.
2. The authors provide empirical insights into how the model learns to distinguish between in-distribution and OOD samples. This helps in understanding the behavior of the model and its ability to generalize to unseen data.
3. The paper is well-written and easy to follow. The authors provide clear explanations of the proposed method and its implementation details.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of the proposed method. It would be helpful to have a theoretical understanding of why the combination of a learned temperature and an energy score is effective in OOD detection.
2. The paper does not compare the proposed method with other state-of-the-art OOD detection methods. It would be helpful to see how AbeT performs compared to other methods in the literature.
3. The paper does not discuss the limitations of the proposed method. It would be helpful to know the scenarios where AbeT might not perform well.

### Suggestions

The lack of theoretical analysis is a significant weakness. While empirical results are valuable, a theoretical foundation would greatly enhance the paper's impact and credibility. Specifically, the authors should explore why the learned temperature parameter, when combined with the energy score, leads to improved OOD detection. A theoretical analysis could involve examining the properties of the learned temperature function, such as its smoothness, its relationship to the data distribution, and how it affects the energy score's ability to separate in-distribution and out-of-distribution samples. For instance, does the learned temperature function act as a form of adaptive scaling that amplifies the differences in energy scores between ID and OOD samples? A deeper dive into the mathematical properties of the proposed method would provide a more solid understanding of its effectiveness and limitations.

Furthermore, the absence of a comprehensive comparison with state-of-the-art OOD detection methods is a major oversight. The authors should benchmark their method against a wide range of existing techniques, including both simple and more complex approaches. This comparison should not only focus on overall performance metrics but also analyze the strengths and weaknesses of each method under different conditions. For example, how does AbeT perform on datasets with varying degrees of semantic shift between in-distribution and out-of-distribution data? Does it perform well on datasets with subtle OOD samples, or does it primarily excel on datasets with clear distinctions? A thorough comparison would provide a more nuanced understanding of the proposed method's capabilities and limitations, and would help to position it within the broader landscape of OOD detection research. The comparison should also include a discussion of the computational cost and complexity of each method.

Finally, the paper needs a more detailed discussion of the limitations of the proposed method. The authors should explore scenarios where AbeT might fail or underperform. For example, does the method rely on specific assumptions about the data distribution, and if so, how might these assumptions be violated in real-world scenarios? Does the method perform well when the OOD data is adversarial or highly similar to the in-distribution data? A thorough discussion of these limitations would provide a more balanced view of the method's applicability and would help guide future research in this area. The authors should also consider providing a sensitivity analysis of the method's hyperparameters to understand how they affect the performance of the method.

### Questions

1. Can you provide a theoretical analysis of the proposed method? Specifically, why does the combination of a learned temperature and an energy score lead to improved OOD detection performance?
2. How does AbeT compare to other state-of-the-art OOD detection methods in the literature?
3. What are the limitations of the proposed method? In what scenarios might AbeT not perform well?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
