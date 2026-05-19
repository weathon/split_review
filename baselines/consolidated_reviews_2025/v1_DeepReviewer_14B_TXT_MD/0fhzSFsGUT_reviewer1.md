### Summary

The paper introduces PETRA, a novel method for parallelizing the training of reversible architectures. The key idea is to decouple the forward and backward passes, allowing stages of the network to be computed independently on different devices. This approach eliminates the need for weight stashing and reduces memory overhead. The authors develop a custom autograd-like training framework for PETRA and demonstrate its effectiveness on CIFAR-10, ImageNet32, and ImageNet datasets, achieving competitive accuracies compared to backpropagation.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1) The paper is well-written and easy to follow. The authors provide a clear explanation of the background, the problem they are addressing, and their proposed solution. The use of figures and tables helps to illustrate the concepts and results.

2) The proposed method is sound and well-motivated. The authors thoroughly discuss the related work and explain how their approach differs from and improves upon existing methods.

### Weaknesses

#### Some Related Works


#### comment

1) The main weakness of the paper is the absence of any timing analysis or speedup results. The authors claim that PETRA can potentially achieve linear speedup compared to standard backpropagation, but this is not demonstrated with any experimental results. Without timing results, it is difficult to assess the practical benefits of the proposed method. The lack of concrete speedup numbers makes it hard to evaluate the actual efficiency gains from the proposed parallelization strategy, especially when compared to optimized backpropagation implementations.

2) Another weakness is that the accuracy performance of PETRA is slightly worse than backpropagation, especially in the case of ImageNet. The authors mention that this is due to the use of stale gradients, but it is not clear how this issue can be addressed. The performance gap, while small, raises concerns about the practical applicability of the method in scenarios where peak accuracy is paramount. The staleness of gradients, while acknowledged, lacks a thorough investigation into its root causes and potential mitigation strategies beyond increasing the batch size.

3) The paper only considers the case where the number of stages is 2. It would be interesting to see how the method performs with a larger number of stages. It is not clear if the performance will degrade as the number of stages increases. This lack of exploration limits the understanding of the method's scalability and its behavior under different parallelization granularities. The choice of only two stages makes it difficult to assess the trade-offs between parallelism and accuracy.

### Suggestions

The paper would benefit significantly from a more thorough experimental evaluation, particularly regarding timing analysis. The authors should provide detailed timing results, including the time taken for forward and backward passes, communication overhead, and the overall training time. These results should be compared against a well-optimized backpropagation baseline, with a clear indication of the number of devices used in both cases. It is crucial to demonstrate the scaling behavior of PETRA by varying the number of devices and showing the corresponding speedup. Furthermore, the authors should investigate the impact of different stage configurations on the overall performance. This would provide a more comprehensive understanding of the method's practical benefits and limitations.

To address the accuracy gap between PETRA and backpropagation, a more in-depth analysis of the gradient staleness is needed. The authors should investigate how the staleness affects the convergence rate and the final accuracy. They could explore techniques to mitigate the staleness, such as using more frequent parameter updates or employing adaptive learning rates. A detailed study of the trade-off between batch size and accuracy is also necessary, as increasing the batch size might not be the optimal solution in all scenarios. The authors should also explore the impact of different accumulation factors on the accuracy and training time. This would provide a more complete picture of the method's performance under different training conditions.

Finally, the authors should extend their experiments to include a larger number of stages. This would help to assess the scalability of the method and its behavior under different parallelization granularities. The experiments should include a systematic analysis of the impact of the number of stages on both the accuracy and the timing performance. The authors should also investigate the trade-offs between the number of stages and the size of each stage. This would provide a more comprehensive understanding of the method's performance and its potential for use in large-scale applications. The paper should also discuss the limitations of the method and potential areas for future research.

### Questions

1) Can you provide timing results for your experiments? How does the training time of PETRA compare to standard backpropagation?

2) How does the accuracy of PETRA compare to other methods that use reversible architectures?

3) What is the impact of the number of stages on the performance of PETRA? How does the method scale with an increasing number of stages?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
