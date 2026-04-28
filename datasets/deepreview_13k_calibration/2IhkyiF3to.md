# Mutual Information Preserving Neural Network Pruning

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Model pruning is attracting increasing interest because of its positive implications in terms of resource consumption and costs. A variety of methods have been developed in the past years. In particular, structured pruning techniques discern the importance of nodes in neural networks (NNs) and filters in convolutional neural networks (CNNs). Global versions of these rank all nodes in a network and select the top-$k$, offering an advantage over local methods that rank nodes only within individual layers. By evaluating all nodes simultaneously, global techniques provide greater control over the network architecture, which improves performance. However, the ranking and selecting process carried out during global pruning can have several major drawbacks. First, the ranking is not updated in real time based on the pruning already performed, making it unable to account for inter-node interactions. Second, it is not uncommon for whole layers to be removed from a model, which leads to untrainable networks. Lastly, global pruning methods do not offer any guarantees regarding re-training. In order to address these issues, we introduce Mutual Information Preserving Pruning (MIPP). The fundamental principle of our method is to select nodes such that the mutual information (MI) between the activations of adjacent layers is maintained. We evaluate MIPP on an array of vision models and datasets, including a pre-trained ResNet50 on ImageNet, where we demonstrate MIPP’s ability to outperform state-of-the-art methods. The implementation of MIPP will be made available upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose MIPP to enable real-time pruning, whole-layer pruning and global re-training guarantees for improving the performance of network pruning. Through comprehensive experimental evaluation, they demonstrate that MIPP can effectively prune networks.

### Strengths
The authors provide a detailed analysis on the motivation and how the method works, especially on how the mutual information is preserved. And they conduct a lot of experiments to demonstrate the effectiveness of their methods.

### Weaknesses
1) Experimental settings and result presentation is not clear.
 - What is untrained network, trained network, pretrained network meaning in Figure 2 and Figure 4?
 - What is LC in Figure 3?
 - In Figure 2, for column 3 and 4, seems the proposed method does not perform well significantly than the baselines.
 - Besides, the latest baseline is year 2022, is there any recent works in 2023 or 2024 to compare?

2) in Figure 4, to my best knowledge, state-of-the-art ResNet50 for ImageNet achieves about 76% accuracy however the proposed approaches can achieve nearly 88% accuracy. Can you explain the settings in detail and what is the percentage of parameters reduced and what is the MACs reduced?

In summary, it is quite unclear how is the comparisons between SOTA and proposed approaches. Besides, some common metrics in comparisons are missing, e.g., FLOPS, #params, MACs. Besides, the baselines seems out-dated.  If the authors could address my concern, I can improve my rating.

As this work is mainly to prune the network, some common metrics in comparisons are missing, e.g., FLOPS, #params, MACs. Can you provide more data what are the results of these metrics? It would be nice if a method maintains accuracy while prunes a lot of neurons or saving a lot of computation costs.
Say, if your method's accuracy is higher but didn't prune a lot may not indicate your method is good.

### Questions
As mentioned in Weakness, I have posed concrete questions for authors. Thanks.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a pruning approach based on mutual information between the activations of adjacent layers. The proposed approach has been evaluated on a number of models and datasets.

### Strengths
+ The motivation of the paper is clear - global pruning approaches do have their limitations and the proposed approach can effectively avoid those. 
+ The idea of looking at the MI between activations of adjacent layers is interesting. It also makes sense to consider nodes that can maintain such MI. 
+ The theoretical analysis seems to make some good points of the observations.

### Weaknesses
 - The proposed approach has only been tested on some early architectures. It is not clear how this can be generalized to other models and datasets?
- It is also not clear if the proposed approach is sensitive to different activation functions.
- The comparison between baselines seems to be quite limited to only a few approaches.

### Questions
* Can this approach work on other types of architectures like ViT?
* How it may perform with different activation functions?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Mutual Information Preserving Pruning (MIPP), an activation-based pruning method that maintains mutual information between adjacent layers in neural networks, ensuring retrainability. Unlike traditional methods, MIPP dynamically selects nodes based on their contribution to information transfer, addressing limitations such as layer collapse and lack of adaptability. Experimental results demonstrate that MIPP outperforms state-of-the-art pruning techniques on various vision models, including ResNet50 on ImageNet, with implementation details to be released upon publication.

### Strengths
This paper provides an interesting perspective on neural network pruning. It considers the activations of the downstream layers, which allows pruning on trained and untrained networks; the idea is interesting.

### Weaknesses
1. Authors claim the method is compared with state-of-the-art techniques, yet most literature is from before 2022; many recent works, such as PHEW or NPB in Pruning at Initialization, and indeed, there are more works on pruning on trained networks in recent years. I strongly suggest that authors provide more valid reviews of recent works.
2. Although the method is interesting because it works for both trained and untrained networks, the motivation for this is not clear. 
For PaI, tasks aim to find networks before training to reduce training costs, while post-trained pruning aims to preserve the best performance on trained networks.  Is MIPP better than SoTA methods on each side?

### Questions
1. Can the author compare MIPP in PaI and post-trained pruning in separate settings with SoTA methods in recent years, such as 2023 or 2024?
2. Most experiments are performed on small datasets and networks; showing the pruning task on more computationally intensive structures or datasets, such as the Efficentnet B7 and Imagenet1K tasks, would be better. As the author claimed, the methods work for trained networks; pruning on a network that is pre-trained in a large-scale dataset such as Imagenet21K could be interesting. 
3. Will this method work in Vision transformers?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces MIPP (Mutual Information Preserving Pruning), a structured pruning method for neural networks. The key idea is to preserve mutual information between adjacent layers' activations during pruning by selecting nodes that transfer entropy to the subsequent layer. 
The method operates by iteratively pruning from outputs to inputs, using transfer entropy redundancy criterion (TERC) with MI ordering to select nodes. Comprehensive experiments validate MIPP's effectiveness on both trained and untrained networks.

### Strengths
1. The overall writing is clear for effective visualizations and well-structured presentation.
2. The paper conducts a wide range of experiments to validate the algorithm.

### Weaknesses
1. Some important references are missing, which makes the novelty of the paper questionable. For example, a recent work also uses mutual information for filter pruning. The paper does not clearly articulate the differences in methodology or performance compared to this existing work. It is unclear whether the proposed method achieves higher performance, and if so, why and how.

2. The compared methods are not state-of-the-art. The authors claim "For models trained on datasets smaller than ImageNet, we compare the performance of our method to SynFlow (Tanaka et al., 2020), GraSP (Wang et al., 2022), ThiNet (Luo et al., 2017) and SOSP-H (Non- nenmacher et al., 2022),". The selection of these methods seems arbitrary, and more recent and competitive baselines should be included. For example, why not include methods published in 2024?

3. Performance is not good. A recent paper shows significantly better performance on ResNet-50 on ImageNet than Thinet. Why does the paper only compare against Thinet in Figure 6, and not against a stronger baseline?

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
