# Utilization of Neighbor Information for Image Classification with Different Levels of Supervision

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3

## Abstract
We propose to bridge the gap between semi-supervised and unsupervised image recognition with a flexible method that performs well for both generalized category discovery (GCD) and image clustering. Despite the overlap in motivation between these tasks, the methods themselves are restricted to a single task – GCD methods are reliant on the labeled portion of the data, and deep image clustering methods have no built-in way to leverage the labels efficiently. We connect the two regimes with an innovative approach that Utilizes Neighbor Information for Classification (UNIC) both in the unsupervised (clustering) and semisupervised (GCD) setting. State-of-the-art clustering methods already rely heavily on nearest neighbors. We improve on their results substantially in two parts, first with a sampling and cleaning strategy where we identify accurate positive and negative neighbors, and secondly by finetuning the backbone with clustering losses computed by sampling both types of neighbors. We then adapt this pipeline to GCD by utilizing the labelled images as ground truth neighbors. Our method yields state-of-the-art results for both clustering (+3% ImageNet-100, Imagenet- 200) and GCD (+0.8% ImageNet-100, +5% CUB-200).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the problem of image classification, tackling both the unsupervised clustering and partially supervised Generalised Category Discovery (GCD) problems. The proposed method is a simple one which first uses a pre-trained DINO backbone to mine positive and negative training samples in a dataset using (unsupervised) nearest neighbour search. 

These positive and negative samples are then used to learn a parametric classifier (which provides a distribution over the ground truth number of classes in the dataset) with a positive and negative classification loss. The positive loss is the cross-entropy between model predictions on the anchor and those on the mined positives, while the negative loss is the inverse of this on the negative samples (though this is not clear to me). 

The authors show state of the art results on both unsupervised clustering and GCD tasks on some standard benchmarks.

### Strengths
* The proposed method seems to be very simple and provide substantial gains over existing baselines in the GCD and unsupervised clustering literature. 
* The simplicity of the approach means the solution can be readily extended to other partially supervised settings (e.g standard semi-supervised learning). The authors already demonstrate strong results on two popular tasks, but it is a positive that the method may find broader applicability. 
* As far as I can see, the main hyper-parameters (size of the neighbourhood for the nearest neighbour mining, loss term weighting, steps in the mining) have been properly ablated.

### Weaknesses
 * My main concern is over the formulation of the learning algorithm. Particularly, I find it difficult to understand Eq 6. The entropy here is computed between two scalar values rather than a distribution. Is this standard binary cross entropy / log loss? This would be more easily understood if written out in full, in my opinion (given that this is not a multi-class entropy problem). Specifically, the use of 'entropy' in this context is confusing, as entropy is typically defined over a probability distribution, not between two scalar probabilities. A clearer explanation of how the scalar values are being used to compute the loss is needed, perhaps by explicitly stating the binary cross-entropy formula.
* As mentioned in "Strengths", the method is simple and can be easily extended. Did the authors consider adding the positive/negative mining strategy directly to existing methods (e.g it might fit naturally on top of the GCD baseline). It is unclear how the proposed mining strategy compares to the nearest neighbor mining already used in the baselines, and whether the gains are solely due to the neighbor cleaning step or the overall training framework. A more detailed discussion of this point would be beneficial.
* The authors could have evaluated on more datasets. For instance, it is common practise to evaluate on the full "SSB" suite (including Stanford Cars and FGVCAircraft) in GCD. The authors could also include a long-tail evaluation like Herbarium19, where the positive/negative mining strategy may behave differently. The current evaluation lacks the breadth to fully demonstrate the robustness of the method across different data distributions and dataset sizes. A long-tail dataset would be particularly useful to see how the method handles imbalanced class distributions.

Misc:
* I believe the presentation of this paper could be improved. e,g: Table 2 is small and difficult to read; Table 6 in uncentered, etc.

### Questions
* Did the authors consider adding the mining strategy on top of existing contrastive GCD methods (e.g the GCD baseline). 
* Did the authors consider long-tail evaluations of their method?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel neighbor mining strategy (UNIC) for both image clustering and generalized category discovery (GCD). The main idea is to firstly mine nearest neighbors as positive and negative ones, and then refine the positive neighbors based on second-order neighborhoods. Experiments show the proposed method has achieved promising performance on clustering and GCD settings.

### Strengths
The motivation for bridging clustering and GCD is interesting and reasonable.
The paper is well written and it is easy to follow the proposed method.
Competitive results on several benchmarks are achieved by the proposed method.

### Weaknesses
The main contribution in this work lies in how to mine positive and negative neighbors. However, the implementation details in the proposed UNIC are not innovative a lot. There have many related methods about improving the positive and negative candidates
for both clustering and GCD field. It is unclear about the main difference and contribution proposed in UNIC. Also, it is unclear why UNIC
can achieve significant improvements over prior works.

The experiments are not comprehensive. It is needed to compare with other positive/negative mining strategies directly.

Moreover, the experiments lack insightful analysis. For example, in Table 3, why the contrastive loss harms the performance of clustering;  
For the GCD ablations in Table 4, it is curious why the labeled negative neighbors are inferior to the mined ones (when comparing the results in the second and third rows).

### Questions
It is encouraged to clarify the novelty in the proposed UNIC, as its implementation looks very common and similar to some existing works.

The experiments are not comprehensive. It is needed to compare with other positive/negative mining strategies directly.

Moreover, the experiments lack insightful analysis. For example, in Table 3, why the contrastive loss harms the performance of clustering;  
For the GCD ablations in Table 4, it is curious why the labeled negative neighbors are inferior to the mined ones (when comparing the results in the second and third rows).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper approaches image clustering and Generalized Category Discovery (GCD) with a proposed union framework, named Utilizes Neighbor Information for Classification (UNIC). 
A novel neighbor mining strategy is introduced to clean noise data points among the set of positive neighbors, and a general pipeline that can be trained end-to-end is designed as well.

### Strengths
S1. They design a simple and effective strategy to exclude noise data points in the set of positive neighbors, which utilizes the information of second-order Euclidean distance.
S2. The proposed method addresses image clustering and GCD simultaneously.
S3. The authors demonstrate the effectiveness of UNIC in their framework with sufficient experimental analysis. Their in-depth analysis shows that their proposed method clearly contributes to performance improvement.

### Weaknesses
W1. When encountered with fine-grained classes, proposed methods show significant reduction with a less powerful backbone, e.g., DINOv1. Could the authors analyze the bounds on the backbone’s feature extraction capabilities that make the proposed approach fail? For example, when the basic K-means clustering accuracy drops to 60% or 50%, the proposed UNIC will not work?

W2. For a comprehensive clustering ablation, could the author replace the proposed positive mining strategy with a simplified one or existing one and show it in Tab. 3 to validate the effectiveness of the proposed positive mining strategy?

W3. There should be more ablations on GCD in Tab. 4, such as “Labeled, Mined for D_L and D_U of positive neighbors, and Labeled-Mined for D_L and D_U of negative neighbors”

W4. Could the author explain the selection of τ_2 for ImageNet and STL? For CUB, what is the parameter τ_2 set to?

W5. For fine-grained image benchmarks, the experiments are only conducted based on the CUB dataset, which cannot demonstrate the generation ability of the model. The author should conduct experiments on other fine-grained like Stanford Cars and FGVC-Aircraft. If the proposed UNIC framework can well-mind clean neighbors, it should also achieve comparable performance with state-of-the-art benchmarks as well.

W6. There are several typos, such as Line 258 “y ̂_i,y ̂_p,y ̂_p”

### Questions
Please justify the issues in Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents **UNIC** (Utilizing Neighbor Information for Classification), a method designed to improve performance in both image clustering (unsupervised learning) and generalized category discovery (GCD) (semi-supervised learning setting). The key contributions and insights from the paper include: 1) Unified Framework for Clustering and GCD: UNIC bridges the gap between clustering and GCD by utilizing a shared pipeline, where it leverages nearest-neighbor relationships in the feature space. For clustering tasks, UNIC identifies and refines positive (same class) and negative (different class) neighbors to improve cluster quality. In the GCD setting, available labels serve as perfect neighbors for known classes, enhancing the model's performance on labeled and unlabeled data alike. 2) Innovative Neighbor Mining and Cleaning Strategy: The method introduces a neighbor-cleaning mechanism, which refines positive neighbors by filtering based on the union size of second-order neighbors, thus ensuring higher purity in the selected neighbor sets. 3) End-to-End Learning Pipeline: Unlike previous multi-stage clustering approaches, UNIC uses an end-to-end training pipeline that enhances representation learning without self-labeling steps, which can be inefficient.

The approach involves two key stages: 1) Neighbor Mining, which identifies positive and negative neighbors by proximity in the feature space. 2) Model Training, which fine-tunes a backbone model (ViT-B/16 pretrained with DINO) using classification and entropy-based regularization losses. Positive neighbors are pulled together, and negative ones are pushed apart to encourage meaningful clustering. UNIC demonstrates state-of-the-art performance across multiple datasets. For the clustering task, it achieves superior accuracy and normalized mutual information (NMI) on benchmarks like STL-10 and ImageNet-100. For the GCD task, it outperforms competing methods on datasets like ImageNet-100 and CUB-200, particularly excelling in settings with high-resolution images and diverse classes.

### Strengths
It's intriguing to see how this paper unifies image clustering and generalized category discovery within a single pipeline. Building on this concept, the authors propose a clustering approach that leverages the mining of positive and negative neighbors. This unified framework enhances model performance across various downstream tasks.

The paper includes extensive evaluations on several benchmarks, demonstrating clear performance improvements. Additionally, the ablation studies offer valuable insights into the contributions of each component in the framework.

End-to-End Learning Pipeline: Unlike previous multi-stage clustering approaches, UNIC uses an end-to-end training pipeline that enhances representation learning without self-labeling steps, which can be inefficient.

### Weaknesses
I have several concerns regarding the technical contributions of this paper. While I agree that positive and negative neighbor mining can improve clustering methods, this approach has already been extensively explored in previous contrastive learning research, such as in [1 ICLR2021] and [2 NeurIPS 2020].

The selection methods for positive and negative samples also appear somewhat simplistic. Using the nearest samples as positives and the furthest as negatives might not be a robust strategy. For instance, previous works, including [1], have shown that employing “hard” negative samples (those that are more challenging to distinguish from positives) can significantly improve model performance. Given the existing research on positive and negative sample mining, there are likely many unexplored approaches that could yield interesting results. It would be beneficial to explore how the selection of positive and negative samples could be refined for this task setting to improve efficiency and effectiveness.

Additionally, some key baselines, such as DeepDPM [3], are missing, and testing on larger datasets, like ImageNet-1k, would strengthen the evidence for model improvements. Many of the baselines included in this paper are not the latest or most competitive, which further limits the impact of the comparisons presented.

The paper’s presentation could also benefit from some adjustments. Placing additional figures, particularly those referenced in the main text, after the summary section disrupts readability. 

Consistency in formatting could be improved as well; for instance, Table 2 contains results with varying decimal places, with some values displayed to two decimals and others to only one.

### Questions
I am curious if authors have tried various representation learning methods (such as MAE, Supervised ViT, iBot, etc) beyond these ones presented in the paper? What kind of self-supervised learning strategy can achieve the best performance? Do you have any insights on it?

### Soundness
2

### Presentation
1

### Contribution
2
