### Summary

The paper proposes Maestro, a method for training low-rank decomposed models. The method is based on ordered dropout, a method that progressively prunes the ranks of the decomposed model. The method is evaluated on several models and datasets and compared to several baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

* The paper is well written and easy to follow.
* The method is simple and seems to work well in practice.
* The method is evaluated on several models and datasets.

### Weaknesses

#### Some Related Works


#### comment

 * The method is based on ordered dropout, but the paper does not cite the ordered dropout paper. Is this method an extension of ordered dropout? If so, this should be made clear in the abstract and introduction.
* The method is compared to Pufferfish and Cuttlefish, but it is not clear how these methods work. It would be nice to have a short description of these methods in the appendix.
* The method is evaluated on several models and datasets, but the results are not always convincing. For example, the method does not seem to work well on ImageNet. It would be nice to see more results on larger datasets.
* The method is compared to several baselines, but it is not clear how the baselines are trained. It would be nice to have more details about the training procedure of the baselines.

### Suggestions

The paper should clearly articulate the relationship between the proposed method and ordered dropout. If the method is indeed an extension, this should be explicitly stated in the abstract and introduction, highlighting the specific modifications and improvements over the original ordered dropout approach. A detailed explanation of how the low-rank decomposition is integrated with the ordered dropout mechanism is crucial for understanding the novelty of the method. Furthermore, the paper should provide a more thorough comparison to existing low-rank methods, such as Pufferfish and Cuttlefish, by including a brief description of their core mechanisms in the appendix. This would help the reader understand the differences and advantages of the proposed method. Specifically, the paper should clarify how the low-rank decomposition is performed in each method, and how the rank is determined during training. This would help the reader understand the differences and advantages of the proposed method.

To strengthen the empirical evaluation, the paper should include more comprehensive results on larger datasets, such as ImageNet. The current results on ImageNet are not convincing, and it is important to demonstrate the effectiveness of the method on more challenging datasets. The paper should also provide more details about the training procedure of the baselines, including the specific hyperparameters used, the optimization algorithm, and the learning rate schedule. This would allow for a more fair comparison between the proposed method and the baselines. Furthermore, the paper should include an ablation study to analyze the impact of different components of the proposed method, such as the low-rank decomposition and the ordered dropout mechanism. This would help to understand the contribution of each component to the overall performance of the method. For example, the paper could compare the performance of the proposed method with and without the low-rank decomposition, or with different dropout rates.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed method. The paper should compare the training time and memory usage of the proposed method with the baselines. This would help to understand the trade-offs between performance and computational cost. The paper should also discuss the limitations of the proposed method and suggest future research directions. For example, the paper could discuss the sensitivity of the method to the choice of the low-rank dimension, or the potential for applying the method to other types of neural networks. Addressing these points would significantly improve the quality and impact of the paper.

### Questions

* How does the method compare to other low-rank methods, such as Pufferfish and Cuttlefish?
* How does the method perform on larger datasets, such as ImageNet?
* How are the baselines trained?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
