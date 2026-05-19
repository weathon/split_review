### Summary

This paper investigates the influence of sub-populations when learning from noisy and long-tailed data. The authors propose a fairness regularizer to improve the performance of sub-populations. Experiments conducted on multiple datasets demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide extensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not novel. The fairness regularizer is widely used in many papers, such as FERMI, FairFed, and FairFed+, etc.
2. The authors only conduct experiments on the CIFAR-10 and CIFAR-100 datasets. The authors should conduct experiments on more datasets, such as ImageNet.
3. The authors should compare the proposed method with more SOTA methods, such as FERMI, FairFed, and FairFed+.

### Suggestions

The paper introduces a fairness regularizer to improve performance on sub-populations, which is a relevant problem. However, the novelty of the approach is questionable given the existing literature on fairness regularization. While the authors demonstrate results on CIFAR-10 and CIFAR-100, these datasets are relatively small and may not fully capture the complexities of real-world scenarios. The lack of experiments on larger, more complex datasets like ImageNet limits the generalizability of the findings. Furthermore, the paper would benefit from a more thorough comparison with existing state-of-the-art methods in fairness-aware learning. Specifically, the authors should compare their method against methods like FERMI, FairFed, and FairFed+, which are designed to address similar challenges. This would provide a more comprehensive understanding of the proposed method's strengths and weaknesses.

To improve the paper, the authors should consider several key areas. First, they should clearly articulate the novelty of their approach compared to existing fairness regularizers. This could involve highlighting specific aspects of their method that are unique or more effective than previous techniques. Second, the authors should expand their experimental evaluation to include larger and more diverse datasets. This would provide a more robust assessment of the method's performance and generalizability. Third, the authors should conduct a more comprehensive comparison with state-of-the-art methods in fairness-aware learning. This would help to contextualize the proposed method's contribution and identify areas for future research. Finally, the authors should provide a more detailed analysis of the method's limitations and potential failure cases. This would help to provide a more balanced and nuanced view of the method's capabilities.

In addition to the above, the authors should also consider exploring the impact of different hyperparameter settings on the performance of their method. This would provide a more complete understanding of the method's sensitivity to different configurations. Furthermore, the authors should investigate the computational cost of their method and compare it to other fairness-aware techniques. This would be important for assessing the practical applicability of the method in real-world scenarios. Finally, the authors should consider providing a more detailed explanation of the theoretical underpinnings of their method. This would help to provide a more solid foundation for the proposed approach and make it easier for other researchers to build upon their work.

### Questions

Please see the weakness.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
