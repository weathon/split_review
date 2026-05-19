### Summary

The paper introduces AutoCLIP, a method for auto-tuning zero-shot classifiers based on vision-language models. The authors highlight that while prior work has focused on creating descriptor sets for classes using various prompt templates, the method for deriving zero-shot classifiers from these descriptors has remained relatively unchanged. AutoCLIP addresses this by tuning per-image weights for each prompt template at inference time, based on the statistics of class descriptor-image similarities. The method is fully unsupervised, has minimal additional computation overhead, and is easy to implement. The authors demonstrate that AutoCLIP outperforms baselines across various vision-language models, datasets, and prompt templates, with improvements of up to 3 percentage points in accuracy.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper introduces a novel method, AutoCLIP, for auto-tuning zero-shot classifiers based on vision-language models. The approach of tuning per-image weights for each prompt template at inference time is innovative and addresses a limitation in prior work.
- The method is fully unsupervised, has minimal additional computation overhead, and is easy to implement, making it practical for real-world applications.
- The authors demonstrate that AutoCLIP outperforms baselines across various vision-language models, datasets, and prompt templates, with improvements of up to 3 percentage points in accuracy. This shows the effectiveness and generalizability of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - While the paper demonstrates the effectiveness of AutoCLIP, it could provide more insights into the theoretical underpinnings of the method. A more detailed analysis of why and how AutoCLIP works would enhance the paper's contribution.
- The paper could benefit from a more extensive discussion of the limitations of AutoCLIP. While the authors mention that the method has minimal additional computation overhead, a more detailed analysis of the computational cost would be beneficial. Furthermore, exploring scenarios where AutoCLIP may not perform optimally would provide a more comprehensive understanding of the method's capabilities.
- The paper could provide more details on the implementation of AutoCLIP, including the specific parameters used and the training procedure. This would make it easier for other researchers to reproduce the results and build upon the proposed method.

### Suggestions

The paper would benefit from a more rigorous theoretical analysis of the proposed AutoCLIP method. While the empirical results are promising, a deeper understanding of why the per-image weight tuning works is crucial. Specifically, the paper should explore the relationship between the similarity statistics used for weighting and the resulting classification performance. For instance, it would be valuable to analyze how the proposed weighting scheme affects the decision boundaries in the embedding space. A theoretical framework, even if simplified, could provide insights into the conditions under which AutoCLIP is expected to perform well and when it might fail. This could involve analyzing the properties of the similarity metrics used and how they interact with the optimization process. Furthermore, exploring connections to existing theoretical work on metric learning or domain adaptation could help to contextualize the method and provide a stronger theoretical foundation.

To strengthen the paper, a more detailed analysis of the computational cost of AutoCLIP is needed. While the authors claim minimal overhead, a quantitative analysis of the runtime and memory usage is necessary. This should include a breakdown of the computational cost of each step in the AutoCLIP pipeline, such as the calculation of similarity statistics and the optimization of per-image weights. The analysis should also consider the scalability of the method to larger datasets and more complex models. Furthermore, it would be beneficial to compare the computational cost of AutoCLIP with other existing methods for zero-shot classification. This would provide a more comprehensive understanding of the trade-offs between accuracy and computational efficiency. The paper should also discuss the potential for optimizing the implementation of AutoCLIP to further reduce its computational overhead.

Finally, the paper should provide more details on the implementation of AutoCLIP to ensure reproducibility. This includes specifying the exact optimization algorithm used for tuning the per-image weights, along with all relevant hyperparameters. The paper should also provide details on the initialization of the weights and the stopping criteria for the optimization process. Furthermore, it would be helpful to include a discussion of any data preprocessing steps that were used. The authors should also consider releasing the code for AutoCLIP to facilitate reproducibility and encourage further research in this area. This would allow other researchers to easily build upon the proposed method and explore its potential in different applications.

### Questions

- Could you provide more insights into the theoretical underpinnings of AutoCLIP? A more detailed analysis of why and how AutoCLIP works would enhance the paper's contribution.
- Could you provide a more extensive discussion of the limitations of AutoCLIP? Exploring scenarios where AutoCLIP may not perform optimally would provide a more comprehensive understanding of the method's capabilities.
- Could you provide more details on the implementation of AutoCLIP, including the specific parameters used and the training procedure? This would make it easier for other researchers to reproduce the results and build upon the proposed method.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
