# Exploring Learning Complexity for Efficient Downstream Dataset Pruning

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
The ever-increasing fine-tuning cost of large-scale pre-trained models gives rise to the importance of dataset pruning, which aims to reduce dataset size while maintaining task performance.
However, existing dataset pruning methods require training on the entire dataset, which is impractical for large-scale pre-trained models.
In this paper, we propose a straightforward, novel, and training-free hardness score named Distorting-based Learning Complexity (\textbf{DLC}), to identify informative images and instructions from the downstream dataset efficiently.
Our method is motivated by the observation that easy samples learned faster can also be learned with fewer parameters.
Specifically, we define the Learning Complexity to quantify sample hardness and utilize a lightweight weights masking process for fast estimation, instead of the costly SGD optimization.
Based on DLC, we further design a flexible under-sampling with randomness (dubbed \textbf{FlexRand}), replacing the top-K strategy, to alleviate the severe subset distribution shift.
Extensive experiments with downstream image and instructions dataset pruning benchmarks demonstrate the effectiveness and efficiency of the proposed approach.
In the images pruning benchmark, DLC significantly reduces the pruning time by \textbf{35}$\times$ while establishing \textit{state-of-the-art} performance with FlexRand.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Distorting-based Learning Complexity (DLC), a novel training-free hardness score for efficient downstream dataset pruning. DLC quantifies sample hardness by masking pre-trained weights and approximating loss integration via the Monte Carlo method. The authors also propose FlexRand, a flexible under-sampling strategy to adapt to different data regimes and avoid distribution shift.

### Strengths
1.) The significance lies in its potential to reduce the computational burden of fine-tuning large pre-trained models while maintaining performance.
2.) The paper is well-structured, and easy to follow.
3.) The introduction of FlexRand adds another layer of adaptability to the pruning process, making it more robust across different data regimes, a valuable contribution to data pruning strategies.

### Weaknesses
1.) The paper suggests that DLC is not sensitive to the quality of pre-trained models, but this claim could be further experimented on different size level pre-trained models. Specifically, the experiments should explore a wider range of pre-trained model sizes, including very small models and very large models, to see if the DLC score remains consistent across these extremes. The analysis should also consider different pre-training strategies, such as self-supervised learning versus supervised learning, to see if the pre-training method affects the DLC score's effectiveness. Furthermore, the paper should investigate the correlation between DLC scores and the actual performance gains achieved by pruning, as it is possible that the DLC score might not always accurately predict the impact of pruning on the model's final accuracy.
2.) The method requires storing multiple masked models, which could be a limitation in environments with constrained memory resources, potentially affecting the practicality of the approach. The paper should provide a detailed analysis of the memory footprint of storing these masked models, including the number of models required and the size of each model, especially when dealing with large pre-trained models. This analysis should also consider the impact of different masking strategies on memory consumption. Furthermore, the paper should discuss potential strategies to mitigate the memory requirements, such as using more efficient data structures or techniques for storing the masked models.
3.) The paper could benefit from a more detailed discussion on scenarios where DLC might underperform or fail, providing a more comprehensive understanding of its limitations. For example, the paper should explore cases where the data distribution of the downstream task is significantly different from the pre-training data, as this could affect the accuracy of the DLC score. Additionally, the paper should analyze the impact of different types of data, such as image data versus text data, on the effectiveness of DLC. The discussion should also consider the sensitivity of DLC to the choice of hyperparameters, such as the number of masks used or the method for approximating the loss integration.

### Questions
see the Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
A novel training-free hardness score, Distorting-based Learning Complexity, is proposed to identify informative images and instructions from downstream dataset. Also, a flexible under-sampling method with randomness named FlexRand is proposed to alleviate the severe subset distribution shift. Extensive experiments demonstrate the effectiveness and efficiency of the proposed approach.

### Strengths
The proposed scoring function, Distorting based Learning Complexity, is an efficient training-free score for dataset pruning. A under-sampling strategy with randomness, FlexRand, is designed to adapt to different data regimes and avoid distribution shift. Extensive experiments demonstrate the effectiveness of the proposed approach. DLC significantly reduces the pruning time by 35× in images pruning benchmark.

### Weaknesses
Some typo: Line 021, "a flexible under-sampling with randomness" -> "a flexible under-sampling strategy with randomness"
In Figure 4(a), the MMD value of Random is missing.

### Questions
When referring masking the pre-training weights, what specific operation is performed on the network parameters?
What's the meaning of dotted line in blue(10%), green(20%) and orange(30%) in Figure(d)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work describes a novel dataset pruning method without the need of pre-training on the target dataset. Given models pre-trained on large scale datasets, this work proposes a Distorting-based Learning Complexity score to identify informative images and instructions. Sample hardness is estimated by randomly masked neural networks, representing networks with different capabilities. Then samples are randomly sampled from the easy and hard groups, respectively. The proposed method achieves effective dataset pruning with 35x less pruning time.

### Strengths
1. The design of using random masks to produce classifiers with different capabilities is interesting and practical. With the averaged feature serving as the prediction head, there is no more need to fine-tune the classifier on downstream tasks. 
2. Detailed experiments are conducted to illustrate the effetiveness of the proposed method. The method can be applied to both image and instruction datasets, both demonstrating performance improvement. 
3. The writing is generally fluent and easy to follow.

### Weaknesses
1. The authors claim that easy samples are more likely to be correctly classified by a weak classifier in the front part of the learning path. However, the overall Learning Complexity score is acquired by averaging classification loss of multiple randomly sampled networks. The definition of learning path seems not to be utilized in the method design. 
2. Can the utilization also be applied to some of previous methods? For example, the Herding method uses parameter influence as scores for each sample. Here the fine-tuned model can also be substituted by a pre-trained model with averaged features as the prediction head. Although the direct employment of pre-trained models is practical, it is not a unique design. And it will be interesting to see if applying the strategy to previous methods also leads to performance improvement. 
3. The strategy of dividing datasets into different groups and randomly sampling from each group is similar to the idea in Dataset Quantization [1]. Dataset Quantization first iteratively separate the data into multiple bins with coreset selection methods. Normally the early groups tend to cluster around the distribution center, while the later groups show more diversity. By sampling from each bin, the overall distribution will be kept similar to the original one. This paper has a similar claim that FlexRand avoids severe distribution shift. Please discuss the difference of the proposed strategy from Dataset Quantization and the advantages of it. 
4. Section 5 discusses the quality of pre-trained models. The authors claim that the method is not sensitive to the quality of pre-trained models. But weakly supervised models are not always worse than fully supervised models. Please also show the original performance comparison between these two groups of models. 
5. Minor:
    - The use of pretrain and pre-train need to be unified in the paper. 
    - The sample number is represented both by N (line 105) and |D| (line 129). Please unify the use.

### Questions
1. How is the loss integration implemented? In the integration figures, the upper bound of loss is 1.0. Is it normalized to the range of (0, 1)?
2. How is the masking applied to the neural network? 
3. How is the splitting hyper-parameter $\gamma$ determined in the actual use? If multiple values need to be tested, the tuning time should also be counted towards the pruning time in Figure 1.

### Soundness
3

### Presentation
3

### Contribution
3
