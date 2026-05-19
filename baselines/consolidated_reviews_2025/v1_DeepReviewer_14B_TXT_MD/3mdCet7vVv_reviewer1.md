### Summary

The paper proposes a new method for finding low-rank factorizations of weights in neural networks. The method works by factorizing all weights in the network and then progressively reducing the rank of each factorized weight matrix throughout training. The reduction in rank is done with a hierarchical group lasso penalty that encourages entire columns/rows to become zero, corresponding to reducing the rank. The end result is a network with a reduced number of parameters that should require less memory to store and less FLOPs to evaluate.

The authors demonstrate their method on a number of networks (ResNet-18, VGG-19, and a 6 layer transformer) on a number of tasks (MNIST, CIFAR-10, translation en-de).

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well written and easy to follow. The method is a logical extension of the previous ordered dropout method, and the authors clearly explain the differences between the two.

The experiments are reasonable and demonstrate the method can be applied to multiple network architectures and tasks. The experiments also include ablations of the different components of the method.

### Weaknesses

#### Some Related Works


#### comment

I am not convinced by the argument that the method is better than SVD because it is done during training and so adapts to the data. For one thing, any method that works by penalizing weights can be said to adapt to the data during training. More importantly, I don't think there is any reason to believe that the ordering of the ranks should change throughout training. Once the data has been projected into the space spanned by the initial singular vectors, that structure shouldn't change. It seems like the method is just adding unnecessary complexity.

I'm not convinced by the experimental results. The authors only show results for a single rank for each network. I think they should show the Pareto frontier of their method, i.e., results for a range of ranks. From the single point they show, the results are worse than Pufferfish for VGG-19, but potentially better for ResNet-18. The lack of a clear advantage across multiple rank settings makes it hard to assess the true potential of the method.

The experiments are missing some key baselines. First, how does the method compare to a standard network with structured pruning applied? This would help to isolate the benefit of the low-rank factorization versus simply reducing the number of parameters through pruning. Second, how does the method compare to a one-time SVD decomposition followed by unstructured pruning? This would help to understand if the iterative nature of the proposed method is truly beneficial compared to a simpler approach. Finally, how does the method compare to a one-time SVD decomposition without any additional pruning? This is the simplest baseline, and it's not clear why the authors don't compare to it. Without these baselines, it's hard to know if the method is actually better than simpler alternatives.

### Suggestions

The core argument for the proposed method hinges on its ability to adapt the low-rank factorization during training, but this claim needs more rigorous justification. While the method does adapt to the data, so do other regularization techniques. The authors need to provide a more compelling reason why the rank ordering should change during training, and why this is superior to a one-time SVD decomposition. The current explanation that the data is transformed by earlier layers is not sufficient. The authors should provide a theoretical analysis or empirical evidence that demonstrates the benefit of dynamically adjusting the rank during training, rather than relying on a static decomposition. For example, they could analyze the singular values of the weight matrices at different stages of training to show how the rank structure evolves and why this is beneficial.

To address the lack of a clear performance advantage, the authors should present a more comprehensive set of experimental results. Instead of just showing a single rank for each network, they should show the entire Pareto frontier, i.e., the trade-off between accuracy and model size for a range of ranks. This would allow for a more thorough comparison with other methods and would make it clear under which conditions the proposed method is most effective. Furthermore, the authors should include a comparison with structured pruning applied to a standard network. This would help to isolate the benefits of the low-rank factorization from the benefits of simply reducing the number of parameters. The authors should also compare against a one-time SVD decomposition followed by unstructured pruning, and a one-time SVD decomposition without any additional pruning. These comparisons are essential to understand if the iterative nature of the proposed method is truly beneficial compared to simpler alternatives.

Finally, the authors should provide more details on the hyperparameter tuning process, especially for the $\lambda_{gl}$ parameter. The current description is vague and does not provide enough information to reproduce the results. The authors should also clarify what they mean by 'relative GMACs' and why the GMACs increase when the hierarchical group lasso penalty is removed. It is also important to clarify the difference between progressive shrinking and unstructured pruning. While both methods reduce the number of parameters, they do so in different ways, and the authors should explain why progressive shrinking is more beneficial in this context. The authors should also provide a more detailed analysis of the computational cost of their method, including the overhead of the progressive shrinking and the SVD decomposition.

### Questions

How much hyperparameter tuning is required for the $\lambda_{gl}$ parameter? How do the results change for different values of $\lambda_{gl}$? What is the value of $\lambda_{gl}$ for each of the results in the paper?

What is the difference between progressive shrinking and unstructured pruning? Unstructured pruning should be just as effective at reducing the number of FLOPs during inference as progressive shrinking.

What is "relative GMACs"? Why does the GMACs increase when the hierarchical group lasso penalty is removed?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
