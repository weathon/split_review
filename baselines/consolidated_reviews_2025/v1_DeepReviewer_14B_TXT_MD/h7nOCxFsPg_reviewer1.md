### Summary

The paper proposes a combination of probabilistic circuits and message-passing graph neural networks, leading to a model that can deal with missing data and uncertainty while being interpretable and having linear complexity in the number of edges.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The proposed method is original, with experiments showing it working better than some state-of-the-art deep graph neural networks. 
The paper is well written, with a good balance between background information and details about the proposed method. The method is also interesting from a theoretical perspective, unifying deep graph neural networks with probabilistic circuits, combining the advantages of both approaches.

### Weaknesses

#### Some Related Works


#### comment

The proposed method is quite complex, and even though the graphical model representation helps, it would be great to provide the overall architecture also in a more mathematical way, explaining the different steps needed to compute the final output. Specifically, a more detailed breakdown of the computations within the sum-product networks (SPNs), and how these are integrated with the graph neural network (GNN) message passing, would be beneficial. The paper lacks a clear, step-by-step explanation of how the probabilistic queries are answered, making it difficult to fully grasp the practical implications of the method's probabilistic nature. It would be useful to see a more explicit description of how the parameters of the SPNs are learned and how they interact with the GNN parameters during training. 

In the experiments, it would be nice to see some experiments on synthetic data where we know the true distribution to better understand how well the proposed method approximates the distribution. This is crucial for validating the method's ability to capture the underlying data generating process, rather than just achieving good performance on downstream tasks. The current experiments primarily focus on real-world datasets, which are useful for demonstrating practical applicability, but they do not provide insights into the model's accuracy in estimating the true data distribution. 

It is also hard to get an idea of how well the proposed method is performing in the experiments. In the scarce supervision setting, it is not clear to me what the baseline is - is the GIN model trained on the same set of labeled samples as the proposed GSPN? The lack of clarity regarding the baseline training procedure makes it difficult to assess the true advantage of the proposed method. Furthermore, the reported results do not provide sufficient information to understand the variance in performance, making it hard to judge the robustness of the method.

### Suggestions

To address the complexity of the proposed method, the authors should include a more detailed mathematical description of the GSPN architecture. This should include a step-by-step breakdown of the computations, starting from the input graph, through the message-passing layers, the construction and evaluation of the SPNs, and finally to the output. Specifically, the authors should provide equations that describe how the parameters of the SPNs are learned and how these parameters are used to compute the probabilistic queries. A clear explanation of how the GNN parameters and SPN parameters are jointly optimized during training is also necessary. This would greatly enhance the clarity and reproducibility of the work. Furthermore, a visual representation of the computational flow, perhaps in the form of a diagram, could complement the mathematical description and make the method more accessible.

To better evaluate the method's ability to approximate the true data distribution, the authors should conduct experiments on synthetic datasets where the ground truth distribution is known. This would allow for a more direct assessment of the model's performance in terms of likelihood estimation or other relevant metrics. For example, a synthetic dataset could be generated from a mixture of Gaussians or other well-understood distributions, and the GSPN's ability to recover these distributions could be evaluated. This would provide a more rigorous validation of the method's probabilistic modeling capabilities. Additionally, it would be beneficial to include a comparison with other probabilistic models, such as variational autoencoders or Gaussian mixture models, on these synthetic datasets to better understand the strengths and weaknesses of the proposed approach.

Finally, to improve the clarity of the experimental results, the authors should provide more details about the training procedure for the baseline models, especially the GIN model in the scarce supervision setting. It is crucial to explicitly state whether the baseline models are trained on the same labeled data as the proposed method. Furthermore, the authors should report the variance of the results across multiple runs, not just the standard deviation, to provide a more complete picture of the method's performance. This would allow for a more robust comparison between the proposed method and the baselines. It would also be beneficial to include a discussion of the limitations of the proposed method, such as its computational cost or sensitivity to hyperparameter settings, to provide a more balanced view of its practical applicability.

### Questions

- How does the proposed method compare to other probabilistic models on synthetic data where we know the true distribution? 
- How well does the proposed method approximate the true distribution on the considered datasets? 
- What is the variance of the results across multiple runs?
- How well does the proposed method perform in settings with different types of edges? 
- How does the proposed method compare to other probabilistic models in terms of expressivity?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
