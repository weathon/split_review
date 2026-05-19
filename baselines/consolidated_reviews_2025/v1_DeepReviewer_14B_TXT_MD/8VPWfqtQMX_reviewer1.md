### Summary

This paper proposes a new perspective for domain generalization, namely, in-context learning. The authors believe that in-context learning can be used as a new mechanism for domain generalization. To achieve this, the authors propose ICRM, which aims to map the problem of domain generalization to the next-token prediction problem through a specific data organization form. In this way, the model can use in-context learning to achieve domain generalization. The authors validate the performance of their method on four datasets.

### Soundness

2 fair

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The idea of using in-context learning for domain generalization is very interesting.
2. The paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works

[1] Learning an adaptive prior with in-context learning for domain generalization.

#### comment

1. The method is very simple. I like the simplicity of the method, but I am curious whether such a simple method is effective. The core idea of organizing data as sequences for next-token prediction, while novel in the context of domain generalization, lacks a clear theoretical justification for why this specific formulation should inherently lead to better generalization across domains. The method essentially repurposes the next-token prediction framework without fundamentally altering the underlying learning dynamics to address the core challenges of domain shift.
2. The experiments are not comprehensive. For example, the authors only use four datasets, two of which are very simple (FEMNIST, Rotated MNIST). The choice of datasets does not fully explore the method's robustness to diverse domain shifts. FEMNIST and Rotated MNIST are relatively easy tasks, and the performance on these datasets might not be indicative of the method's effectiveness on more complex, real-world domain generalization problems. Furthermore, the paper lacks a thorough comparison with state-of-the-art domain generalization methods, especially those that leverage similar in-context learning ideas.
3. Some works have also noticed that in-context learning can be used for domain generalization, such as [1]. The authors should discuss the differences. The paper fails to adequately position itself within the existing literature on in-context learning for domain generalization. Specifically, it does not clearly articulate how its approach differs from, and improves upon, prior work that has explored similar connections. This lack of comparative analysis makes it difficult to assess the novelty and contribution of the proposed method.

### Suggestions

The paper should provide a more rigorous theoretical analysis of why the proposed in-context learning formulation is effective for domain generalization. It is not sufficient to simply map the problem to next-token prediction; the authors need to explain why this specific mapping is beneficial. For example, they could explore the relationship between the learned context and the underlying domain structure. This could involve analyzing the attention mechanisms to understand which aspects of the context are most relevant for generalization. Furthermore, the authors should investigate the impact of different context organization strategies on the final performance. For instance, how does the order of examples within a context affect the learning process? A more detailed analysis of the method's inner workings is needed to justify its effectiveness.

The experimental evaluation needs to be significantly expanded to include more challenging and diverse datasets. The current selection of datasets is not sufficient to demonstrate the method's robustness to real-world domain shifts. The authors should include datasets with more complex domain structures and larger domain shifts, such as those used in the DomainBed benchmark. Additionally, the paper should include a thorough comparison with state-of-the-art domain generalization methods, including those that use in-context learning. This comparison should not only focus on overall performance but also on the method's efficiency, robustness, and sensitivity to hyperparameter settings. A more comprehensive experimental evaluation is crucial to establish the practical value of the proposed method.

The paper needs to provide a more detailed discussion of the relationship between the proposed method and existing work on in-context learning for domain generalization. The authors should clearly articulate the novelty of their approach and how it differs from prior work. This discussion should include a detailed comparison of the proposed method with other in-context learning based domain generalization techniques, highlighting the advantages and disadvantages of each approach. Furthermore, the authors should discuss the limitations of their method and identify potential avenues for future research. A more thorough and nuanced discussion of the related work is essential to position the paper within the broader research landscape.

### Questions

1. What is the difference between ICRM and ICL for DG?
2. What is the relationship between ICRM and meta-learning?
3. Can this method be used for natural language tasks?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
