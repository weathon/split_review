### Summary

This paper proposes a non-interactive distributed learning algorithm called Secure Distributed DP-Helmet, which is based on the blind averaging technique. The algorithm allows each party to locally learn and add noise to their model, and then jointly compute the mean of their models via a secure summation protocol. The paper shows that blind averaging preserves privacy if the models are averaged via secure summation and the objective function is smooth, Lipschitz, and strongly convex. The paper also provides experimental evidence that blind averaging can have a strong utility-privacy tradeoff, and derives a sufficient condition for strong utility from the representer theorem.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a new non-interactive distributed learning algorithm called Secure Distributed DP-Helmet, which is based on the blind averaging technique. The algorithm allows each party to locally learn and add noise to their model, and then jointly compute the mean of their models via a secure summation protocol. This is a novel approach to distributed learning that can reduce the communication overhead and improve the privacy of the data.

2. The paper shows that blind averaging preserves privacy if the models are averaged via secure summation and the objective function is smooth, Lipschitz, and strongly convex. This is a significant result that provides a theoretical foundation for the proposed algorithm.

3. The paper provides experimental evidence that blind averaging can have a strong utility-privacy tradeoff. The results show that the algorithm can achieve high accuracy on CIFAR-10 and CIFAR-100 datasets, while maintaining a strong privacy guarantee.

4. The paper derives a sufficient condition for strong utility from the representer theorem. This condition provides a theoretical guarantee for the performance of the algorithm and can be used to guide the design of other distributed learning algorithms.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the objective function is smooth, Lipschitz, and strongly convex, which may not hold for all learning tasks. This is a significant limitation as many real-world problems involve non-convex objective functions, and the theoretical guarantees provided in the paper may not apply in such cases. The paper should discuss the implications of this assumption more thoroughly, and perhaps provide some empirical analysis on the performance of the proposed method on non-convex problems.

2. The paper only considers two specific learning algorithms, SVM and Softmax-activated single-layer perception. While these are common algorithms, the applicability of the proposed method to other learning algorithms is not clear. The paper should discuss the limitations of the proposed method in terms of the types of learning algorithms it can be applied to, and perhaps provide some guidance on how to extend the method to other algorithms. For example, it would be useful to discuss the challenges of applying blind averaging to deep neural networks, which are non-convex and have a large number of parameters.

3. The paper does not provide a detailed analysis of the communication overhead of the proposed method. While the paper claims that the method is non-interactive, it is not clear how the communication cost compares to other distributed learning methods. The paper should provide a more detailed analysis of the communication cost, including the number of communication rounds and the size of the messages exchanged. It would also be useful to compare the communication cost of the proposed method to other distributed learning methods, such as federated learning.

### Suggestions

The paper should provide a more thorough discussion of the limitations of the smooth, Lipschitz, and strongly convex assumption. It would be beneficial to include an empirical analysis of the algorithm's performance on non-convex problems, even if theoretical guarantees are not available. This could involve testing the algorithm on datasets with known non-convex loss functions, such as those arising in deep learning. Furthermore, the paper should discuss potential modifications to the algorithm that could make it more robust to non-convexity, such as using different optimization techniques or adding regularization terms. This would help to broaden the applicability of the proposed method and make it more relevant to real-world problems.

To address the limitation of only considering SVM and Softmax-activated single-layer perception, the paper should provide a more detailed discussion of the challenges of applying blind averaging to other learning algorithms. Specifically, the paper should discuss the difficulties of applying the method to deep neural networks, which are non-convex and have a large number of parameters. It would be useful to explore potential solutions to these challenges, such as using techniques for approximating the loss function or using different aggregation methods. The paper should also discuss the potential for extending the method to other types of learning algorithms, such as reinforcement learning or generative models. This would help to demonstrate the versatility of the proposed method and make it more appealing to a wider audience.

Finally, the paper should provide a more detailed analysis of the communication overhead of the proposed method. This should include a breakdown of the communication cost in terms of the number of communication rounds and the size of the messages exchanged. The paper should also compare the communication cost of the proposed method to other distributed learning methods, such as federated learning. This comparison should be done both theoretically and empirically. It would also be useful to discuss potential techniques for reducing the communication cost of the proposed method, such as using compression techniques or using asynchronous communication protocols. This would help to make the proposed method more practical for real-world applications.

### Questions

1. Can the proposed method be applied to other learning algorithms besides SVM and Softmax-activated single-layer perception? If so, what are the challenges and how can they be addressed?

2. How does the communication overhead of the proposed method compare to other distributed learning methods, such as federated learning? Can the communication cost be reduced further?

3. What are the limitations of the proposed method in terms of the types of learning tasks it can be applied to? Are there any types of learning tasks for which the proposed method is not suitable?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
