### Summary

The paper introduces a novel method called PETRA (Parallel End-to-End Training with Reversible Architectures) for parallelizing the training of reversible architectures. The key idea is to decouple the forward and backward passes, allowing stages of the network to be computed independently on different devices while only needing to communicate activations and gradients between each other. This approach eliminates the need for weight stashing and reduces memory overhead. The authors demonstrate the effectiveness of PETRA on CIFAR-10, ImageNet32, and ImageNet datasets, achieving competitive accuracies compared to backpropagation.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper introduces a novel method for parallelizing the training of reversible architectures, which is a promising direction for improving the efficiency of deep learning models.

2. The authors demonstrate the effectiveness of PETRA on multiple datasets, achieving competitive accuracies compared to backpropagation.

3. The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational overhead of PETRA compared to other methods, which is an important factor to consider when evaluating the efficiency of the proposed method.

2. The paper does not explore the potential limitations of PETRA, such as its applicability to different types of architectures or datasets.

3. The paper does not provide a thorough comparison of PETRA with other parallelization techniques, which would help to better understand the advantages and disadvantages of the proposed method.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational overhead introduced by PETRA. While the authors mention reduced memory overhead, a detailed breakdown of the computational costs, including communication costs between devices, is crucial. For instance, the paper should quantify the time spent on forward and backward passes, as well as the time spent on communication of activations and gradients. This analysis should be compared against standard backpropagation and other parallelization techniques, such as data parallelism or model parallelism, to provide a clear understanding of the trade-offs. Furthermore, the analysis should consider the impact of different hardware configurations, such as the number of GPUs and the network bandwidth, on the overall performance of PETRA. A concrete example would be to provide a table showing the time spent on each stage of the training process for PETRA and other methods, broken down by forward pass, backward pass, and communication overhead.

To address the limitations of PETRA, the authors should explore its applicability to a wider range of architectures and datasets. The current evaluation is limited to a few specific architectures and datasets. It is important to investigate how PETRA performs with different types of layers, such as convolutional layers, recurrent layers, and attention mechanisms. Additionally, the authors should evaluate PETRA on datasets with varying sizes and complexities to understand its scalability and robustness. For example, the paper could include experiments on transformer-based architectures and datasets with different input sizes and data distributions. This would provide a more comprehensive understanding of the strengths and weaknesses of PETRA and its potential for real-world applications. Furthermore, the paper should discuss the potential challenges of applying PETRA to very deep networks or networks with complex connectivity patterns.

Finally, a more thorough comparison of PETRA with other parallelization techniques is needed. The paper should provide a detailed comparison of PETRA with data parallelism, model parallelism, and pipeline parallelism. This comparison should include a discussion of the advantages and disadvantages of each technique in terms of memory overhead, computational overhead, and scalability. The authors should also discuss the potential for combining PETRA with other parallelization techniques to further improve the efficiency of training deep learning models. For example, the paper could explore the possibility of using PETRA in conjunction with data parallelism to train large models on distributed datasets. This would provide a more complete picture of the landscape of parallelization techniques and the unique contributions of PETRA.

### Questions

1. Can you provide more details on the computational overhead of PETRA compared to other methods?

2. What are the potential limitations of PETRA, and how can they be addressed?

3. How does PETRA compare to other parallelization techniques in terms of memory overhead, computational overhead, and scalability?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
