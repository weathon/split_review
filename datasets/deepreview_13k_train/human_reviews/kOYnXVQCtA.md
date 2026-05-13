# DeeperForward: Enhanced Forward-Forward Training for Deeper and Better Performance

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
While backpropagation effectively trains models, it presents challenges related to bio-plausibility, resulting in high memory demands and limited parallelism. Recently, Hinton (2022) proposed the Forward-Forward (FF) algorithm for high-parallel local updates. FF leverages squared sums as the local update target, termed goodness, and employs L2 normalization to decouple goodness and extract new features. However, this design encounters issues with feature scaling and deactivated neurons, limiting its application mainly to shallow networks. This paper proposes a novel goodness design utilizing **layer normalization** and **mean goodness** to overcome these challenges, demonstrating performance improvements even in 17-layer CNNs. Experiments on CIFAR-10, MNIST, and Fashion-MNIST show significant advantages over existing FF-based algorithms, highlighting the potential of FF in deep models. Additionally, a model parallel strategy is proposed to enhance training efficiency greatly.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The current paper proposes a novel design of bio-logically plausible algorithms utilizing layer normalization and mean goodness, which extends the Forward-Forward to non-trivial networks. Extensive experiments across datasets and models validate the approach.

### Strengths
The paper enables training conventional models with the FF algorithm. 

Diagrams are well designed, clear, and nice. 

The explanation of the method is clear.

This approach scales well to multiple GPUs

I like the well written background section.

### Weaknesses
I would like to see experiments on Imagenet or other large scale datasets. 

I'm interested in an experiment that shows that the portion of deactivated neurons is reduced.

### Questions
Can you show that the portion of deactivate neurons is reduced?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work aims to improve forward-forward training and enable deeper networks by providing layer normalization and mean goodness to overcome certain limitations.  Experiments show that the performance can be improved even with 17-layer CNNs.  Datasets like CIFAR-10, MNIST, and Fashion-MNIST are involved in illustrating the benefits of the proposed DeeperForward method.  In addition, a model parallel strategy and memory saving strategy are proposed to enhance training efficiency and costs.

### Strengths
The brain-inspired forward-forward approach is certainly an interesting and novel area to explore. It’s great to see efforts advancing in this direction.

The writing and presentation are easy to follow.

The experiments in the study are substantial.

### Weaknesses
The main issue of the study is the performance of the proposed DeeperForward method.   Compared with sota models using BP, DeeperForward falls behind on Fashion MNIST and has an even bigger gap on CIFAR-10.  Its accuracy on MNIST is marginally comparable to other methods. However, that is not particularly strong considering the simplicity of MNIST.  The results suggest the exploration of FF is ongoing and still faces some challenges.

Line 309, "we employ a combination strategy for selecting consecutive layers"  It is not clear what the strategy is and how this strategy reduces the complexity from O(2^L) to O(L^2). Specifically, the method for selecting the "best-performing combination" of layers is not well-defined. Is this selection performed on a validation set? What metric is used to determine the best combination? The lack of clarity here makes it difficult to assess the validity of the approach.

It is not clear how the number of layers would impact the performance.  Is 17 the top limit? Would an architecture larger than 17 layers suffer from some kind of vanishing gradient problem? The paper does not provide sufficient analysis on how the depth of the network affects the training dynamics of the forward-forward method. It is crucial to understand if the performance degradation with deeper networks is due to the inherent limitations of the method or simply a matter of hyperparameter tuning.

Despite some discussions in Section 4.5, the computational cost aspect of DeeperForward is inadequate. What is the total GPU time needed to complete a task, for example, CIFAR-10 classification?  That measure would allow comparison with other non-FF methods more comprehensively. This should be a critical part of this study. The paper should provide a detailed breakdown of the computational cost, including the time spent on forward passes, goodness calculations, and weight updates. Without this, it's difficult to assess the practical applicability of the method.

The memory-saving strategy lacks details.  Appendix H does not provide any measures or evidence on how this strategy could reduce memory usage for DeeperForward. The paper should provide a quantitative analysis of the memory usage with and without the proposed strategy, demonstrating the actual memory savings achieved. It is also unclear how this strategy interacts with the parallel training approach.

Similarly, the parallel strategy needs more details as well.  What if the number of GPUs is more than 2?  Also, what would happen if the number of GPUs is greater than the number of layers?  Would the extra GPUs stay idle? Fig 4 does not provide such insight. The paper needs to clarify how the layers are distributed across GPUs, especially when the number of GPUs exceeds the number of layers. It should also discuss the communication overhead between GPUs and how this impacts the overall training time.

### Questions
See above as the questions are mainly addressing weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The author proposed a novel approach, DeeperForward, to enhance the Forward-Forward algorithm. This paper introduced a goodness design based on layer norm and mean goodness to solve issues like feature scaling and deactivated neurons. This paper also demonstrates the effectiveness of DeeperForward using 17-layer CNN on various datasets. Additionally, this paper states a model-parallel strategy to reduce training time.

### Strengths
1. The proposed modifications, especially mean goodness and layer normalization, effectively address the limitations of the FF algorithm in deeper architectures.

2. The model-parallel strategy greatly enhances the training efficiency on multi-GPU setups, enabling the method to scale well across deeper networks.

### Weaknesses
1. **Dataset Size Limitations**: The reviewer acknowledges that DeeperForward has primarily been tested on relatively small datasets, such as CIFAR-10 and MNIST. While these datasets are widely used benchmarks, the reviewer agrees that evaluating DeeperForward on larger datasets, such as ImageNet, would provide more insight into its scalability and effectiveness. The reviewer recommends conducting experiments on larger datasets to assess their performance under different conditions thoroughly.

2. **Choice of Architecture Depth**: The reviewer notes that the 17-layer CNN was selected as a balance between computational efficiency and depth sufficient to highlight the advantages of DeeperForward over existing methods in moderately deep networks. However, the reviewer wonders if testing DeeperForward on even deeper architectures (e.g., 50 or 100 layers) would provide valuable insights. The reviewer encourages extending the evaluation to larger models to assess its performance and generalization capabilities on very deep networks.

3. **Accuracy and Comparison with Block-wise Learning**: The reviewer points out the lack of significant accuracy improvement in Table 1 compared to non-FF and other FF methods. While the method focuses on improving training efficiency and enabling deeper networks, the reviewer highlights recent works in block-wise learning[1,2] that have shown greater improvements in accuracy, surpassing backpropagation by over 5%. The reviewer is curious if DeeperForward could incorporate block-wise learning concepts to improve accuracy while retaining the benefits of the forward-forward training scheme.

4. **Scalability on Multiple GPUs**: The reviewer observes that the speedup ratios in Table 5 reflect performance gains using one and two GPUs but would like to see tests on more GPUs to provide a more comprehensive view of DeeperForward's scalability. The reviewer suggests extending parallelization experiments to include setups with more GPUs to provide a broader evaluation of how the method scales with additional hardware resources.

5. **Training Curve Convergence**: The reviewer notes concern regarding the convergence behavior shown in Figure 7. The training curve does not fully converge within the current number of epochs, and the reviewer would like to see further experiments to determine the number of epochs required for stable convergence. The reviewer recommends updating the results with extended training to provide a clearer picture of when and how the method reaches its optimal performance.

### Questions
See weakness above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the DeeperForward algorithm, extending the Forward-Forward approach to deeper networks. The paper introduces a goodness design, combining mean goodness and layer normalization, which partially addresses issues in the effective training of deep networks: feature scaling, redundant normalization, and deactivated neurons. It’s a bit innovative but not very clear in expression.

### Strengths
- The article proposes an innovative design based on the original FF method to solve the inherent problems of BP and FF.
- From the experimental results, it can be seen that DeeperForward has good performance.

### Weaknesses
 - The abstract lacks a brief description of the new parallel strategy.
- Figure 1 is confusing. Firstly, it would be more appropriate to compare the performance gap between your method and SOTA in Figure 1. Secondly, your method only has a single forward propagation path, which is inconsistent with the enhanced FF in your title.
- ‘However, this approach fails to decouple goodness and leaks goodness to the next layer, hindering deeper layers from learning new features and causing overfitting.’ Authors have repeatedly used this general and assertive conclusion in the introduction to evaluate the drawbacks of other methods, but I have not seen a specific reason. This is not very detailed and almost unconvincing. Moreover, it is evident that this conclusion has nothing to do with feature scaling.
- ‘Although CwComp (Papachristodoulou et al., 2024) improves performance using squared goodness and batch normalization, it leaks goodness information, leading to overfitting in deeper networks.’ According to your description, the omission of goodness of fit information directly leads to overfitting, which is clearly not convincing. Any defects in the model can lead to common problems of overfitting. There is a lack of deeper reasons between the two.
- ‘We adopt layer normalization for better feature scaling with identical mean and standard deviations, instead of L2 normalization.’ You have expressed the drawbacks of L2 normalization and proposed so-called alternative methods. But why do we need to use your method to replace it? What is the motivation? You cannot simply express that the original method has shortcomings but your method has advantages, and then your method can become an alternative solution without deeper motivation and logic.
- The format of subheadings under section 3.2 is inconsistent.
- From Sec4.1, it can be seen that GPU memory is sufficient, but there is a lack of experiments on large datasets such as ImageNet.
- 8.Sec4.5 only compared GPU and speed with BP, but according to what you described earlier, you have made improvements based on FF. There is a lack of results compared to FF here.

### Questions
Q1. ‘This approach addresses the bio-plausibility issues of backpropagation and overcomes the limitations of FF concerning model size.’ In the Method section, the problem solved by this method is inconsistent with the problem you mentioned in the introduction that needs to be solved. Does model size refer to feature scaling? What is the relationship between the bio funding issues of backpropagation and deactivated neurons?

Q2. ‘The pruning process aims to select an optimal combination of layers for refining the network and eliminating redundant layers.’ How is it selected and what are the criteria for selecting combinations?

Q3. Where was Xr extracted from in Figure 3? Any layer? Because deeper layers contain higher semantic information, where Xr comes from is a critical issue for performance.

Q4. The DeeperForward you proposed is similar in principle to the methods[1,2] in the Local Learning field. What are your strengths? 

[1] Xiong, Yuwen, Mengye Ren, and Raquel Urtasun. "Loco: Local contrastive representation learning." Advances in neural information processing systems 33 (2020): 11142-11153.

[2] Su, Junhao, et al. "HPFF: Hierarchical Locally Supervised Learning with Patch Feature Fusion." arXiv preprint arXiv:2407.05638 (2024).

If the author resolves my questions, I will consider raising my rating.

### Soundness
3

### Presentation
2

### Contribution
3
