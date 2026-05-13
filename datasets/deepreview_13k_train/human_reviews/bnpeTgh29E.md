# Sub-Domain Aware Granular Segmentation via Fine Tuning Network

- Decision: Reject
- Scores: 3, 3, 6, 3

## Abstract
Recent advances in deep learning (DL) have led to improved vision-based algorithms. DL-based semantic segmentation, in particular, has enabled precise predictions using Convolutional Neural Networks (CNNs). State-of-the-art CNN-based networks have achieved high accuracy on various datasets in multiple fields, such as building, scene, and object segmentation. However, subdomain shifts between training and test sets within a single domain can cause degraded accuracy in fine-grained segmentation. To counter this, this paper introduces a novel Sub-Domain Adaptation (SDA) framework for fine-grained and granular segmentation, which divides one single domain into multiple sub-domains and optimizes the baseline-network for each sub-domain. The baseline-network is further fine-tuned by recognizing the domain of the input in run-time, leading to more accurate predictions. Benchmarks of scene parsing, autonomous driving, and aerial imagery demonstrate the superior performance of SDA for granular segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a new sub-domain-aware fine segmentation framework, called SDA-Net (Sub-Domain Adaptation Network), which aims to solve the problem of “soft domain gap” within the domain, which leads to a decrease in accuracy when performing fine segmentation in an image. The main methods include the following. The main methods include:

1. Sub-domain Adaptation: A large single domain is divided into multiple sub-domains, and the network is fine-tuned for each sub-domain so that the model can adapt to the features of the specific sub-domain, thus improving the segmentation accuracy.

2. Subdomain Classifier and Baseline Network: SDA-Net consists of a Subdomain Classifier (SDC) and a Baseline Network (BN). the SDC is responsible for recognizing the subdomains to which the input image belongs, while the BN fine-tunes the subdomains based on the recognized ones, thus generating more accurate predictions.

3. Self-supervised learning loss: The paper introduces a new “sieve loss” and fine-tuning loss, which aims to improve segmentation accuracy by reducing the differences between subdomains through self-supervised learning.

### Strengths
1. This paper proposes a novel sub-domain adaptation framework—SDA-Net—to address the issue of sub-domain discrepancies within a single domain. This approach differs from traditional cross-domain adaptation methods, which aim to reduce the gap between different domains; instead, it optimizes the subtle differences within a single domain.

2. SDA-Net introduces the “sieve loss” and “fine-tuning loss,” effectively reducing the differences between sub-domains and enhancing the accuracy of fine segmentation. This self-supervised fine-tuning strategy exhibits strong innovation in addressing sub-domain gaps.

3. The paper conducts comprehensive experiments on multiple benchmark datasets (e.g., WHU, BDD100K, and ADE20K), validating the model's superior performance across various tasks. The experimental results thoroughly demonstrate the generalization capabilities of SDA-Net across different datasets.

4. By addressing the “soft domain gap” issue within a single domain, this paper offers a new perspective on domain adaptation research, potentially stimulating further studies on sub-domain awareness and self-supervised fine-tuning strategies.

### Weaknesses
1. Although the sub-domain-aware framework brings some innovation to domain-specific segmentation, it relies on established techniques like self-supervised and domain adaptation methods (e.g., domain-invariant feature learning and pseudo-label generation). Strengthening the technical uniqueness of SDA-Net could improve its impact, such as by introducing an adaptive sub-domain division strategy rather than a feature-similarity-based grouping. The current approach uses a relatively simple feature similarity for sub-domain division, which may not capture the complex underlying structure of the data, potentially leading to suboptimal sub-domain groupings and limiting the effectiveness of subsequent fine-tuning. A more sophisticated approach, perhaps involving clustering algorithms that consider both feature similarity and task-specific performance metrics, could be explored.

2. While the sieve loss and fine-tuning loss are effective in refining sub-domains, similar types of loss functions have been applied in other domain adaptation tasks (e.g., Focal Loss). Integrating more unique loss functions or leveraging other self-supervised strategies, such as contrastive learning, could enhance the novelty of the proposed approach. The sieve loss, while novel in its application to sub-domain adaptation, bears resemblance to density-based loss functions. Similarly, the fine-tuning loss, which introduces a negative gradient term, shares conceptual similarities with other gradient-based optimization techniques. A more detailed analysis of how these losses differ from existing methods, particularly in their mathematical formulation and optimization behavior, would be beneficial. Furthermore, exploring alternative self-supervised strategies, such as those based on information maximization or adversarial training, could potentially lead to more robust and generalizable models.

3. Although the paper includes some ablation studies, it lacks a thorough discussion of how sub-domain count and division strategies affect model performance. Further experimentation on the sensitivity of SDA-Net to different sub-domain configurations and parameters could increase the method's applicability. The current ablation studies do not fully explore the impact of varying the number of sub-domains or the specific criteria used for sub-domain division. A more comprehensive analysis, including a sensitivity analysis of model performance with respect to these parameters, is needed to demonstrate the robustness of the proposed method. This analysis should also investigate the trade-offs between the number of sub-domains and the computational cost of training and inference.

4. The comparative experiments mainly focus on traditional domain adaptation methods and include limited comparisons with the latest fine-grained segmentation approaches. Including comparisons with state-of-the-art segmentation methods would offer a more comprehensive view of SDA-Net’s advantages and limitations. The current evaluation primarily compares SDA-Net against traditional domain adaptation techniques, which may not be the most relevant benchmarks for a fine-grained segmentation task. A more thorough comparison against state-of-the-art fine-grained segmentation methods, including those that employ attention mechanisms or multi-scale feature fusion, is needed to fully assess the performance and limitations of the proposed approach.

### Questions
1. Since the SDA-Net framework adds sub-domain classifiers and custom losses, how does its computational complexity compare to baseline methods? Could you provide more details on training and inference times relative to other methods, and whether any optimization strategies were considered to reduce overhead?

2. The sieve loss and fine-tuning loss are designed to address sub-domain differences, but they share similarities with losses from other domain adaptation works. Could you explain how these losses differ from existing methods or provide additional details on how they were tailored specifically for sub-domain adaptation?

3. The authors say that the fully trained deep learning model does not provide the highest performance when applied to each subdomain, but looking at Table 1 you can see that the superior performance in the total task is better than any subdomain training subdomain test, why is that? What does it mean?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work studies the problem of sub-domain shift between the training and testing dataset within one large domain in semantic segmentation. By hypothesizing that sub-domain gaps within one domain are much smaller than between two domains, the authors believe that precious domain adaption algorithms are ineffective. They propose a self-supervised finetuning network, SDA-Net, incorporating a novel sieve loss and an adaptive finetuning loss to deal with intra-domain gaps. Evaluations on benchmarks suggest some effectiveness.

### Strengths
- This work is well-motivated by providing preliminary experiments that demonstrate the problem of soft-domain gaps.
- The manuscript is clearly written and easy to follow. For example, the authors provide detailed illustrations and equations to present the proposed algorithms.
- Adding new loss functions or extra supervising signals can further boost the performance of deep learning networks, which is a common convention and widely used practice.

### Weaknesses
 *MAJOR* concerns: This work needs more sufficient comparisons with previous related algorithms.
-  The adopted baseline network UNet and CCNet are outdated, making the experiment less convincing. Will the proposed algorithm also applied to the prominent vision transformers? Specifically, the performance gains of the proposed method should be demonstrated on more modern architectures, such as the Swin Transformer or other transformer-based segmentation models. The current choice of baselines limits the impact and generalizability of the findings.
- Simply comparing SDA-Net with previous fully-supervised structures is unfair, as SDA-Net introduces extra supervising signals. A better comparison is expected to reflect whether the proposed framework also applied well to those existing methods. For example, the authors should consider incorporating their proposed loss functions into existing state-of-the-art segmentation models and then compare the performance gains. This would provide a more robust evaluation of the effectiveness of the proposed loss functions independent of the base architecture.
- The authors claim in the INTRODUCTION that previous domain adaption algorithms fail to solve the intra-sub-domain shift problem. However, there is also no experiment to support this fundamental claim. Comparisons with SOTA domain adaption algorithms are significant in highlighting your contribution. The authors should provide empirical evidence that demonstrates the ineffectiveness of existing domain adaptation techniques on the specific intra-domain shift problem they are addressing. This could involve comparing the performance of existing domain adaptation methods with and without the proposed SDA-Net on the same dataset.

Other *MINOR* concerns:
- SOTA is an often-used abbreviation, compared with SotA.
- It is suggested that citations be added to those reported tables for quick reader reference.

Overall, this work has a clear motivation, but the experimental part weakens the contribution. It may benefit from future thoughtful revision.

### Questions
Please refer to the WEAKNESSES part.

### Soundness
2

### Presentation
2

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
To address the issue where subdomain shifts between the training and test sets within a single domain lead to decreased accuracy in fine segmentation, this paper proposes SDA. SDA divides a single domain into multiple subdomains and optimizes the baseline network for each subdomain iteratively, refining the network continuously. The effectiveness of this approach is validated in the field of granular segmentation.

### Strengths
1. The paper finds that existing DA methods perform poorly in addressing intra-domain differences, providing valuable insight into the field.

2. The paper provides a thorough theoretical analysis of the model and offers reliable experiments. Also, The Method of the paper is logically organized, which is easy to follow.

### Weaknesses
1. The concept of "soft domain gap" is introduced for the first time in this paper, but its definition is not clearly distinguished from conventional inter-domain differences. Specifically, the paper does not provide a clear mathematical formulation or a rigorous explanation of how this "soft gap" differs from the established notion of domain shift, making it difficult to understand the novelty of this concept.

2. One concern is whether the sieve loss relies on the accuracy of subdomain division. If subdomain division is inaccurate, will it significantly degrade performance on such datasets? The paper lacks a thorough analysis of the sensitivity of the proposed method to errors in subdomain clustering. It's unclear how the method would perform if the density-based clustering misidentifies subdomains, potentially leading to incorrect pseudo-labels and degraded performance.

3. The paper is highly correlated with methods in the DA (Domain Adaptation) field, but miss important discussions with a few recent DA methods: Pipa: Pixel-and patch-wise self-supervised learning for domain adaptative semantic segmentation, and Transferring to Real-World Layouts: A Depth-aware Framework for Scene Adaptation. The absence of a detailed comparison with these methods, particularly in the context of intra-domain adaptation, limits the paper's ability to position itself within the broader landscape of domain adaptation techniques.

4. The paper provides extensive quantitative results but lacks a display of visualization results. The absence of visual examples makes it difficult to assess the qualitative performance of the proposed method, especially in terms of segmentation quality and the effectiveness of the subdomain adaptation. Visualizations could provide valuable insights into the model's behavior and potential failure cases.

5. The paper lacks an analysis of its limitations, such as scalability and constraints related to computational resource requirements. There is no discussion on how the method scales with increasing dataset size or the computational cost associated with the subdomain clustering and iterative optimization processes. This lack of analysis limits the practical applicability of the method in real-world scenarios.

### Questions
1. How can the optimal number and size of subdomains be determined across different datasets and application scenarios?

2. If applied to a completely different domain (e.g., shifting from urban scenes to natural scenes), would the model's generalization ability be significantly affected?

3. In SDA-Net, the density probability vector generated by the subdomain classifier is used to identify which subdomain the input image belongs to. How exactly is it trained?

4. The paper designs the framework based on ResNet-18. Could this be considered a weak baseline without expressing more complex details?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a novel deep learning framework termed SDA-Net, which is designed to address the challenges of subdomain shifts and soft domain gaps in fine-grained segmentation tasks. The core innovation of SDA-Net lies in its ability to recognize the subdomain of input data and fine-tune the baseline network accordingly, leading to more accurate segmentation predictions. The framework is composed of a sub-domain classifier (SDC) and a baseline-network (BN), and it employs a self-supervised fine-tuning approach to adapt to the specific subdomain characteristics of the input data.

### Strengths
1. The SDA-Net framework is an original approach that addresses the subdomain shifts in segmentation tasks.  It innovatively combines subdomain recognition with fine-tuning of a baseline network to enhance segmentation accuracy.

2. The introduction of the sieve loss and the fine-tuning loss are creative solutions to optimize the network for density-based segmentation.

3.The proposed framework is not limited to a specific domain but is applicable to various fields such as scene parsing, autonomous driving, and aerial imagery, highlighting its broad significance.

### Weaknesses
1. The paper could benefit from a more detailed comparative analysis with other domain adaptation techniques, especially those that also aim to address intra-domain variability.  This would provide a clearer picture of the advantages of the proposed approach over existing methods. What's more, the reference is not almost latest.

2. The paper could provide more depth on the theory behind the subdomain classification strategy used by the SDA-Net.  A more detailed discussion on the selection criteria for subdomains and the rationale behind the chosen number of subdomains would be beneficial.

3. While the sieve loss is a novel contribution, the paper could offer a more rigorous mathematical justification for its effectiveness.  This could include a more detailed analysis of how the sieve loss bridges the gap between predicted and actual densities.

4. While the paper mentions that the code is available， but the link is not work.

5. Considering the application of the SDA-Net framework to multimodal data (e.g., combining visual data with lidar or radar data for autonomous driving) could be a promising direction for extending the framework's capabilities.

### Questions
Please refer to Section Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
