### Summary

This paper proposes a meta-learning method to address the challenge of learning from noisy annotations provided by multiple annotators. The approach embeds examples into a latent space using a neural network and constructs a probabilistic model to learn a classifier while estimating the abilities of annotators. The neural network is meta-learned to enhance test performance with limited annotated data, and parameters are optimized via the EM algorithm and gradient descent.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is technically sound.
2. The proposed method is performed on the meta-learning setting, which is rarely explored in the learning with Noisy Label area.

### Weaknesses

#### Some Related Works

[1] Meta-Learning with Noisy Labels by Exploring and Exploiting Multiple Embedding Subspaces

#### comment

1. The novelty of this paper is not significant. The idea of using meta-learning to address the learning with noisy labels issue has already been explored in previous works, such as [1]. 
2. The comparison methods are not appropriate. All the compared methods are mainly designed for the learning with noisy labels, not meta-learning. It is necessary to compare the proposed method with some meta-learning methods.
3. The datasets used in this paper are too small. The meta-learning methods usually perform experiments on the larger datasets, such as tiered-imagenet.
4. The authors do not discuss the limitations of the proposed method.

### Suggestions

The paper's primary weakness lies in its incremental contribution over existing meta-learning approaches for noisy labels. While the proposed method combines a Gaussian Mixture Model (GMM) with meta-learning, the core idea of using meta-learning to handle noisy labels is not novel. The authors should more clearly articulate the specific challenges they address that are not covered by existing methods, and provide a more detailed comparison to highlight the unique aspects of their approach. For instance, a more thorough analysis of how the proposed method handles different types of annotator noise compared to existing meta-learning techniques would be beneficial. Furthermore, the paper should include a more detailed discussion of the computational complexity of the proposed method, especially in comparison to other meta-learning algorithms. This would help to clarify the practical advantages and disadvantages of the proposed approach.

To address the issue of inappropriate comparisons, the authors should include a more comprehensive set of baselines from the meta-learning literature. Specifically, they should compare their method against other meta-learning algorithms that are designed to handle noisy labels, or at least demonstrate how their method compares to standard meta-learning algorithms when applied to noisy label datasets. This would provide a more robust evaluation of the proposed method's effectiveness. Furthermore, the authors should consider using a more diverse set of datasets, including larger and more complex datasets, to demonstrate the generalizability of their method. The current datasets are too small to fully evaluate the performance of the proposed method in real-world scenarios. The authors should also consider using datasets with varying levels of noise to assess the robustness of their method under different conditions.

Finally, the authors need to explicitly discuss the limitations of their proposed method. This should include a discussion of the assumptions made by the method, the potential failure cases, and the computational cost. For example, the authors should discuss how the performance of the method is affected by the number of annotators, the quality of the annotations, and the complexity of the task. They should also discuss the limitations of the EM algorithm in the context of meta-learning, and how these limitations might affect the performance of the proposed method. A thorough discussion of these limitations would provide a more balanced and realistic assessment of the proposed method's capabilities.

### Questions

1. The time complexity of the EM algorithm may be high, so how long does it take to train the proposed method on the datasets?
2. The performance of the meta-learning methods may be sensitive to the settings of the hyperparameters. How to determine the hyperparameters in the proposed method?

### Rating

3

### Confidence

4

**********
