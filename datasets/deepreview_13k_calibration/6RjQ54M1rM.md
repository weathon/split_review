# FedLWS: Federated Learning with Adaptive Layer-wise Weight Shrinking

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In Federated Learning (FL), weighted aggregation of local models is conducted to generate a new global model, and the aggregation weights are typically normalized to 1. A recent study identifies the global weight shrinking effect in FL, indicating an enhancement in the global model’s generalization when the sum of weights (i.e., the shrinking factor) is smaller than 1, where how to learn the shrinking factor becomes crucial. However, principled approaches to this solution have not been carefully studied from the adequate consideration of privacy concerns and layer-wise distinctions. To this end, we propose a novel model aggregation strategy, Federated Learning with Adaptive Layer-wise Weight Shrinking (FedLWS), which adaptively designs the shrinking factor in a layer-wise manner and avoids optimizing the shrinking factors on a proxy dataset. We initially explored the factors affecting the shrinking factor during the training process. Then we calculate the layer-wise shrinking factors by considering the distinctions among each layer of the global model. FedLWS can be easily incorporated with various existing methods due to its flexibility. Extensive experiments under diverse scenarios demonstrate the superiority of our method over several state-of-the-art approaches, providing a promising tool for enhancing the global model in FL. We include the source code of FedLWS in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies server-side aggregation algorithms for non-IID federated learning, proposing an adaptive layer-wise weight shrinking strategy. Compared to the existing weight shrinking method, the proposed approach does not require auxiliary datasets to adjust the weights and allows for different shrinkage across various layers of neural networks.

### Strengths
1. The layer-wise strategy is well-motivated, as non-IID data may have varying disparity effects on different layers/modules.

2. The proposal can be integrated into many non-IID-resistant training paradigms, such as FedProx and FedDisco.

### Weaknesses
1. The proposal presents similarities to existing concepts in federated learning, particularly the idea of layer-wise weighted aggregation (e.g., [a], [b]) and the weight shrinking technique from Li et al. (2023a). To enhance the clarity and impact of the proposed method, it would be beneficial for the authors to explicitly outline the novel aspects of their approach in comparison to these prior works. Specifically, the method needs to clarify how it differs from simply applying different learning rates to different layers, or using a hypernetwork to generate layer-specific weights. A more detailed comparison to existing layer-wise aggregation techniques, including a discussion of the computational overhead and communication costs, would be valuable. What unique contributions does this method bring to this area beyond what is already established in the literature?

2. While the proposal shows strong empirical performance, it would be more persuasive with theoretical justification. Specifically, the authors might provide a theoretical analysis of the advantages (e.g., faster convergence rate) of layer-wise shrinking compared to the original weight shrinking approach from Li et al. (2023a). The current theoretical justification is lacking, and a more rigorous analysis is needed to support the claims of improved performance, especially in heterogeneous settings. The paper should explore whether the proposed method provides any guarantees on convergence or generalization error, and if so, under what conditions.

### Questions
1. The relationship between the ratio of updating terms in Equation (4) and the gradient variance in Equation (5) is not immediately clear. It would be helpful if the authors could provide an intuitive explanation or theoretical evidence that supports this connection.

2. More guidance is needed on how to choose the hyperparameter $\beta$ and its potential impact on performance.

3. The current experiments only consider one text dataset; it would be beneficial to explore additional scenarios.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents FedLWS (Federated Learning with Adaptive Layer-wise Weight Shrinking), a novel model aggregation strategy designed to improve the generalization of global models in Federated Learning (FL). Recognizing that a shrinking factor (sum of aggregation weights) less than 1 can enhance model generalization, FedLWS adaptively adjusts the shrinking factor at each layer based on gradient dynamics without requiring a proxy dataset, thereby reducing privacy risks. The approach calculates layer-specific shrinking factors during training, leveraging the unique characteristics of each layer, and is compatible with existing FL methods. Extensive experiments demonstrate FedLWS’s consistent performance improvements over state-of-the-art methods across diverse scenarios. A noted limitation is its current applicability only to scenarios where client models share the same architecture. Future work will address this limitation by exploring heterogeneous model scenarios.

### Strengths
This paper addresses privacy concerns raised in prior research regarding the use of proxy datasets, and adopts an intuitive assumption in federated learning to dynamically adjust the shrinking factor (γ) layer-by-layer based on gradient variance. This approach aims to enhance model generalization while preserving privacy. The paper is well-structured, with extensive experimental support provided in both the main text and appendices. The key strengths of this approach are as follows:

- FedLWS avoids the need for proxy datasets, reducing potential privacy risks and making it more suitable for sensitive applications.
- The layer-wise adjustment of the shrinking factor (γ) allows FedLWS to adapt to specific layer characteristics, resulting in better model generalization across diverse and heterogeneous datasets.
- As a “plug-and-play” approach, FedLWS can be easily integrated with existing federated learning methods, improving their performance without requiring substantial modifications to the training process.

### Weaknesses
1.  The introduction does a good job of citing relevant works to contextualize the study. However, it might be beneficial to discuss more recent research on adaptive weight shrinkage and layer-wise adaptation in FL, if available. This could provide a clearer picture of how the proposed FedLWS method aligns with and advances the current research landscape in FL.
2.  This paper introduces a thoughtful approach by linking the shrinking factor to gradient variance, which allows dynamic adjustment of regularization. This concept appears promising and well-motivated, especially as it addresses practical deployment issues by eliminating the need for a proxy dataset. However, the authors could further clarify how this method stands out from other adaptive approaches. Are there any existing methods that also use gradient variance for similar adjustments, and if so, how does FedLWS provide additional benefits?
3. The paper presents an intuitive hypothesis on the relationship between regularization, optimization, and gradient variance. Additional theoretical support or references could help strengthen this hypothesis. While the authors propose a function to capture this relationship, further clarification on the rationale behind this formulation would be valuable. Could a theoretical proof or justification for this relationship be provided?
4. FedLWS employs a dynamically adjusted shrinking factor γ to balance regularization and optimization, but it is unclear whether this adjustment strategy could negatively impact convergence in federated learning. Frequent adjustments to the shrinking factor during multiple communication rounds may lead to instability or slower convergence. The authors could analyze the convergence behavior of FedLWS over multiple communication rounds, especially under varying data heterogeneity or client participation rates. Providing a convergence analysis or additional experimental results would help ensure that the method maintains stable convergence properties in federated learning.
5.  The modularity of FedLWS as a “plug-and-play” solution is a valuable contribution. However, the paper could benefit from a more detailed example of how FedLWS integrates with popular FL methods like FedAvg or FedProx. For instance, describing specific integration steps for one or two methods would help readers understand the practical applicability of FedLWS.
6. FedLWS employs a strategy of assigning different shrinking factors to different layers, based on the assumption that each layer requires a distinct level of regularization. However, in federated learning, different types of layers (e.g., convolutional layers and fully connected layers) may exhibit significantly different behaviors, and a simple layer-wise assignment may not be suitable for all types of layers. Could further experiments be conducted to verify the effectiveness of layer-wise shrinking across various types of layers? Additionally, it may be worth considering adjustments to the shrinking factor allocation based on the function or structural characteristics of each layer (e.g., differences between shallow and deep layers). This could potentially help FedLWS more effectively optimize each layer of the model.
7. The results in Tables 1 and 2 effectively demonstrate that FedLWS consistently improves accuracy across datasets and heterogeneity levels, especially for more challenging tasks. However, a more detailed explanation of why FedLWS performs differently across various datasets would be helpful. For instance, why does FedLWS perform better on datasets with higher complexity or heterogeneity? This is particularly noteworthy given that prior work had the advantage of an additional proxy dataset as prior knowledge.
8. In Figure 1(a), we observe a sudden drop when α  reaches 0.7, followed by a return to stability. Has the author considered the reasons behind this occurrence? In Figure 1(b), even a very small decrease (e.g., 0.01) has a significant impact on the results. Why is this the case?  The use of a 5-layer CNN model with uniformly decreasing values from 1 to 0.96 is an interesting experimental design choice. However, the authors could clarify the rationale for this specific range and pattern. Was the decrease from 1 to 0.96 based on empirical observation, theoretical insights, or a predetermined hypothesis? Including a brief justification for this choice could add depth to the experimental setup.
9. The calculation of layer-wise shrinking factors appears to significantly increase computational overhead, especially in deep or large models such as ViT or BERT. Could the authors provide an analysis of this aspect?
10.  Although FedLWS shows performance advantages in most experiments, it may underperform compared to FedLAW in certain cases. The authors attribute this entirely to FedLAW’s use of a proxy dataset, but this explanation seems insufficient, as FedLAW consistently uses a proxy dataset across all experimental settings. The authors should analyze under which experimental conditions FedLAW outperforms FedLWS and examine whether specific variables might explain this phenomenon.
11.  Although the paper includes multiple image and text datasets, it does not explain whether these datasets offer generalizability. In particular, AG News, as the sole text dataset, is insufficient to fully validate FedLWS’s performance on other types of text data or time-series data.
12.  Privacy is an essential consideration in FL, and the authors have addressed this well by removing the reliance on a proxy dataset. However, additional details on how FedLWS manages potential privacy risks, especially during gradient and parameter calculations, would be useful. Additionally, it would be valuable to discuss if FedLWS has any compatibility with existing privacy-preserving techniques like differential privacy.
13.  The comparison between FedLWS and adaptive weight decay methods (AWD and AdaDecay) is insightful, showing FedLWS’s advantage in FL. Adding a brief explanation of why FedLWS outperforms weight decay in the FL context (e.g., due to its layer-wise adaptability) would make this comparison more compelling. The authors do not explain this reason in Appendix A.2.

### Questions
- How does the proposed layer-wise dynamic adjustment method demonstrate superiority over traditional dynamic adjustment techniques in the context of weight aggregation?
- Can the authors provide a detailed background on prior experimental findings to help readers understand the motivation behind the approach?
- In the experimental section, why does the proposed method perform better, and can this be explained rather than just described?

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
4

### Summary
This work proposes a simple and practical model aggregation method to enhance the performance of various federated learning algorithms.

### Strengths
The proposed scheme is a direct intuitive scheme, which is easy to realize in practice. From the experimental results, the proposed algorithm can indeed play a role in improving performance.

### Weaknesses
Whether the proposed scheme is theoretically optimal is worth considering.

The proposed weighting method used to determine the model aggregation accords with intuition but lacks theoretical proof. Can a theoretical proof be given to ensure that the weighting coefficient determined from the gradient variance perspective is optimal?

In Table 1, the performance of FedProx is generally worse than that of FedAvg. What is the reason for this phenomenon? The experiment should ensure that FedProx uses appropriate hyperparameters and that the comparison between the proposed LWA-enhanced methods and other baselines is fair, that is, the hyperparameters that make baselines' performance optimal should be used.

### Questions
1. The proposed weighting method used to determine the model aggregation accords with intuition but lacks theoretical proof. Can a theoretical proof be given to ensure that the weighting coefficient determined from the gradient variance perspective is optimal?

2. In Table 1, the performance of FedProx is generally worse than that of FedAvg. What is the reason for this phenomenon? The experiment should ensure that FedProx uses appropriate hyperparameters and that the comparison between the proposed LWA-enhanced methods and other baselines is fair, that is, the hyperparameters that make baselines' performance optimal should be used.

### Soundness
2

### Presentation
2

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
This paper introduces a method, FedLWS, to overcome the limitations of previous research named FedLAW, which leverages a Global Weight Shrinking (GWS) effect using a learnable shrinking factor based on proxy data. The authors identify two key issues with FedLAW: privacy concerns and considering the divergence across different layers of a deep neural network. To address these issues, they propose an alternative approach for calculating the shrinking factor using the variance of local model gradients. This method is based on the empirically observed relationship between the ratio of the regularization term to the optimization term and local gradient variance. Furthermore, this calculation enables the authors to propose a layer-wise shrinking factor for each layer, considering inter-layer differences for improved model generalization. Extensive experiments, including ablation studies, are conducted across various scenarios to verify the effectiveness of the proposed method. Overall, the authors present an effective alternative to address the limitations of previous research, and the experimental results appear to support its effectiveness. However, a more detailed analysis of the experimental results is necessary.

### Strengths
1. By proposing an alternative method for calculating the weight shrinking factor, the authors improve performance over the previous algorithm, reduce computation time on the server side, and eliminate privacy risks associated with the use of proxy data.

2. The authors analyze the characteristics of weight updates resulting from the application of the weight shrinking factor in the model agregation process of FL, validating these characteristics through equations and experiments.

3. The effectiveness of the proposed method is validated through extensive experiments conducted in various environments, as well as ablation studies under diverse conditions.

### Weaknesses
1. The validation of the proposed method’s effectiveness across various experimental conditions is a strong point; however, the results are presented as simple listings or repetitions of earlier sections without in-depth analysis, making it difficult to gain insights into how the proposed method operates from a representation perspective. For example, in lines 388–389, the authors describe the results in Table 1 by comparing them with the baseline method, FedLAW. The authors note that in some settings, the method underperforms compared to FedLAW, attributing this to the latter’s use of proxy data. However, as FedLAW utilizes proxy data in all cases, this explanation does not fully account for the variations in performance improvement across different cases.

2. There are several typos across multiple lines, and sentences with similar meanings are repeated, leading to a lack of coherence in the overall narrative.

### Questions
1. Is it correct to use the equal sign between the left and right sides of equation (4)? Would it be more appropriate to use a proportionality sign instead?

2. What does the sudden decline in the value in the range of 0.6 - 0.7 in Fig 1(a) signify?

3. The calculation of the layer-wise shrinking factor seems to increase the computational load, yet Table 3 reports only a 0.02-second increase. Is there a technique applied to compensate for the increase in computational load?

4. In Figure 3(a), why does the value of layer-wise gamma increase monotonically from early to later layers?

5. In section 5.3, the results in Table 4 and the narrative are inconsistent. While the performance has improved model-wise compared to FedAvg, it is stated otherwise. The author insists(line 448): on the CIFAR-10 dataset with NIID (α= 0.1), the performance of model-wise weight shrinking is not as effective as FedAvg, whereas the layer-wise weight shrinking effect outperforms FedAvg.

6. In Table 5, is the result for FedLAW with WRN56_4, indicated as 18.44, correct? If so, why is the accuracy for this setting significantly lower than that of the others?

7. In Fig 6, it seems to be no effect of beta. What is the reason for selecting beta as a hyperparameter?

### Soundness
3

### Presentation
2

### Contribution
3
