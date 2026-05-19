### Summary

This paper proposes a novel data selection method for pre-fine-tuning of large language models (LLMs). The key idea is to select data that shifts the pre-training distribution closer to the target distribution, rather than simply aligning with the target distribution. The authors prove the optimality of this approach under certain conditions and demonstrate its effectiveness across various tasks. The proposed method is significantly faster than existing techniques, scaling to millions of samples within a single GPU hour. The code is open-sourced, making the benefits of cost-effective fine-tuning more accessible.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a clear motivation for their work and explain the limitations of existing methods.
3. The proposed method is theoretically grounded and has a solid foundation.
4. The authors demonstrate the efficacy of their methodology across a diverse array of tasks, showing that it consistently surpasses other selection methods.
5. The authors show that their method is significantly faster than existing techniques, scaling to millions of samples within a single GPU hour.

### Weaknesses

#### Some Related Works


#### comment

1. The authors mention that their approach is not intended for tasks requiring domain knowledge that are very different from the scope of pre-training data. However, they do not provide any empirical evidence to support this claim. It would be beneficial to see some experiments that demonstrate the limitations of their approach in such scenarios.
2. The authors do not provide a detailed analysis of the computational cost of their method. While they mention that it is significantly faster than existing techniques, it would be helpful to see a more quantitative comparison of the computational cost of their method with other data selection methods.
3. The authors do not discuss the potential impact of the choice of the pre-training distribution on the performance of their method. It would be interesting to see how the performance of their method varies when using different pre-training distributions.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the proposed method, particularly when applied to tasks requiring domain-specific knowledge. While the authors acknowledge this limitation, they should provide empirical evidence to support their claim. For instance, they could evaluate their method on a dataset that requires specialized knowledge, such as a dataset related to medical or legal text. This would help to clarify the scope of the method and identify scenarios where it might not be applicable. Furthermore, it would be beneficial to compare the performance of the proposed method with other data selection techniques in these challenging scenarios. This would provide a more complete picture of the strengths and weaknesses of the proposed approach.

In addition to the empirical evaluation, a more detailed analysis of the computational cost of the proposed method is needed. While the authors mention that their method is faster than existing techniques, they should provide a quantitative comparison of the computational cost with other data selection methods. This comparison should include the time required for data selection and the memory usage. It would also be helpful to analyze the scalability of the method with respect to the size of the dataset. This analysis would provide a better understanding of the practical applicability of the method. Furthermore, the authors should discuss the potential impact of the choice of the pre-training distribution on the performance of their method. It would be interesting to see how the performance of their method varies when using different pre-training distributions. This analysis would help to identify the optimal pre-training distribution for the proposed method.

Finally, the authors should provide more details on the implementation of their method. This includes the specific algorithms used for data selection and the parameters used for the experiments. It would also be helpful to provide a discussion of the sensitivity of the method to different parameter settings. This would make it easier for other researchers to reproduce the results and build upon the proposed method. Furthermore, the authors should discuss the potential limitations of their method and suggest directions for future research. This would help to advance the field and encourage further exploration of data selection techniques for language models.

### Questions

1. How does the performance of the proposed method vary when using different pre-training distributions?
2. What is the computational cost of the proposed method compared to other data selection methods?
3. How does the proposed method perform on tasks requiring domain knowledge that are very different from the scope of pre-training data?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
