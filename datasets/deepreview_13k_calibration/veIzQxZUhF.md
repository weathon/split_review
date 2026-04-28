# Deep concept removal

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
We address the problem of concept removal in deep neural networks, aiming to learn representations that do not encode certain specified concepts (e.g., gender etc.) %, thereby improving model robustness, generalizability, and fairness.
We propose a novel method based on adversarial linear classifiers trained on a concept dataset, which helps remove the targeted attribute while maintaining model performance. Our approach Deep Concept Removal incorporates adversarial probing classifiers at various layers of the network, effectively addressing concept entanglement and improving out-of-distribution generalization. We also introduce an implicit gradient-based technique to tackle the challenges associated with adversarial training using linear classifiers. We evaluate the ability to remove a concept on a set of popular distributionally robust optimization (DRO) benchmarks with spurious correlations, as well as out-of-distribution (OOD) generalization tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to remove undesired concepts from neural network representations. This is done by an adversarial training process that alternates between training a concept classifier and a downstream task classifier. The novelty of their method lies in using an adversarial penalty based on TCAV, removing a concept of interest from multiple layers of the network. The paper tests its formulation across multiple settings.

### Strengths
1.	The proposed setting is novel and interesting. Concept removal is proposed as an intuitive extension to [1]. 
2.	The paper performs a comprehensive literature review and explains the relevant works needed to understand the paper in detail.
3.	The research questions proposed by the work are insightful for understanding how concepts are embedded in the network architecture. The finding that adversarial CAV helps most when applied to layers before contraction is important.
4.	The appendix provides extensive details about the implementation as well as the mathematical framework.

[1] Quantitative Testing with Concept Activation Vectors (TCAV)

### Weaknesses
1. At a high-level, the paper appears to combine aspects of two earlier works (Elazar et al, 2018 and Kim et al, TCAV, 2018), integrating the concept of TCAV [2] into the framework of adversarial concept removal. The primary novelty seems to be the use of the norm of v* as the adversarial loss. However, the motivation behind this specific choice is not thoroughly explained. A more detailed justification of why this particular loss function is optimal for concept removal, compared to other potential loss functions, would strengthen the paper.

2. The work seems more directly applicable to bias removal rather than out-of-distribution (OOD) generalization. The paper should elaborate on how the proposed method can effectively handle scenarios with significant distribution shifts, beyond the Celeb-A example.

3. The paper lacks quantitative baselines that demonstrate the effectiveness of the proposed method. For instance, in the StripedMNIST experiment, it would be valuable to see the test performance on images where stripes are at different angles or have different properties compared to those seen during training. This would provide a more rigorous evaluation of the method's ability to generalize to unseen stripe variations.

4. The results in Table 2 are not entirely convincing. The paper does not adequately address the disparity between datasets where adversarial CAV performs poorly and where it outperforms the baselines. The statement "Our results suggest that our concept removal approach is more effective at removing higher-level features, while lower-level features are deeply ingrained in the representations and harder to remove" is not sufficiently supported. The distinction between lower-level and higher-level features seems arbitrary and requires a more precise definition and further experimental validation.

5. The results from Figure 7 are not adequately explained. Specifically, it is unclear why the concept accuracy for "young" and "glasses" remains relatively unchanged, while the concept accuracy for "gender" is significantly reduced. A more in-depth analysis of these results is needed to understand the selective nature of the concept removal process.

6. The claim of OOD generalization is not fully substantiated. The numbers are only reported for Celeb-A, where blond males are considered the "unseen domain." However, these images are arguably drawn from the same support as the original data, and there is no significant covariate shift. Furthermore, the "domain invariant representation" is learned by removing the concept of gender, which essentially provides the model with prior knowledge about the desired invariant feature. This setup is somewhat artificial, as the model should ideally deduce the domain-invariant generalization without explicit guidance.

7. The limitation section does not address some of the critical challenges identified in the work, such as the disparity in performance across different datasets mentioned in point #4.

### Questions
1.	Is it trivial to extend the method to remove multiple concepts from the representations of a model? This would be closer to a realistic setting where the bias is generally a result of more than one concept.
2.	The adversarial penalty term has been used to remove unwanted concepts. Could a similar method be used to induce the usage of specific concept?
3.	[1] proposed concept activation regions to tackle the problem with TCAV, where the concept sets are not linearly separable despite the classes being linearly separable. How does this work address that issue?
4.	The formulation of the concept dataset following “...to avoid correlation between “Eyeglasses” and “Young” within the “Male” subgroup…” from appendix C.4.1 seems to imply a combination explosion as the number of concepts increases. Is this a limitation of the method?
5.	In Figure 3, for the images which do not have stripes as a concept, a reconstruction of those representations introduces stripes. This seems counterproductive.
6.	Please address the test accuracies being 100% in Table 1 even though the training accuracies are much lower. 
7.	Please provide further details about the training of the decoder mentioned in RQ2. It is unclear what data is used along with the pixel wise MSE objective to train the decoder. Does the dataset include striped and unstriped images?
8.	In fig.7, are the various solid lines obtained from training multiple instances of the model where each instance has a specific concept removed?
9.	We request that in fig 4 (a), the epochs vs accuracy performance for ResNet MNIST be shown.

PS: Please provide axes labels to improve the readability of the graphs.

[1] Concept Activation Regions: A Generalized Framework For Concept-Based Explanations

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new method called Deep Concept Removal to remove undesirable concepts or features from learned representations in neural networks. The main idea of this method is to (a) use a concept dataset to learn a concept activation vector (CAV) in representation space and (b) penalize the norm of this CAV to down-weight the concept in representation space. The first set of experiments shows that this method can effectively remove a concept from synthetic MNIST data by (a) applying it to multiple wide layers and (b) using out-of-distribution concept datasets. The second set of experiments applies this method to (a) remove spurious concepts and improve worst-group accuracy in subpop robustness benchmarks and (b) reduces tcav sensitivity to spurious concepts in a fairness task.

### Strengths
- The background on concept activation vectors and adversarial concept removal is easy to follow for readers not familiar with the topics.
- The approach is simple and decouples model training and concept erasure, so one can erase concepts in a post-hoc manner using a concept dataset instead of requiring training datapoints to have concept labels.
- The experiments in S4 that study the connection between layers and concept removal effectiveness are insightful.

### Weaknesses
 - The main experiment in S4 only demonstrates RQ1 and RQ2 on MNIST. The MNIST dataset is a good sanity check or starting point, but it is not enough to properly demonstrate the usefulness of this approach. A simple linear model can give 90% accuracy on the MNIST task and it is not representative of modern computer vision tasks. The experiments would be more convincing if the results hold on (a) “harder” tasks such as CIFAR-10 or CIFAR-100 and larger models (e.g., ResNet50 and ViTs)
- The experiments in S4 do not adequately support RQ2 (concept datasets can be OOD). The OOD concept dataset considered  (EMNIST) is in fact quite similar to the MNIST dataset. It would be useful to provide a more nuanced understanding of when OOD concept datasets fail to remove concepts for example. The current analysis does not explore the degree of dissimilarity between the concept dataset and the target dataset, which is crucial for understanding the limitations of the method.
- The experiments do not compare their results with relevant concept removal baselines such as LEACE (https://arxiv.org/abs/2306.03819) and kernel-space concept erasure (https://aclanthology.org/2022.emnlp-main.405/). There is no related work section either, so it’s hard for the readers to contextualize these findings. The lack of comparison with existing methods makes it difficult to assess the novelty and effectiveness of the proposed approach. Furthermore, the absence of a related work section makes it hard to understand the context of this work within the broader field of concept removal.
- As mentioned by the authors, the regularization term (Eq 3.2) is purely heuristic, so it is unclear if this approach of downweighting the CAV will work in general. The method lacks a theoretical justification for why penalizing the norm of the CAV is an effective way to remove concepts. This raises concerns about the generalizability of the approach to different types of concepts and datasets.
- The deep concept removal method does not work on the Waterbirds dataset. In particular, it performs *significantly* worse than ERM. The authors do acknowledge this and hypothesize that their method may be more effective at removing high-level features than low-level features. However, this explanation is not convincing at all. What makes a concept high-level? Does this definition of high-level concept distinguish CelebA and “striped MNIST” concept from waterbirds? I am not sure if subpopulation robustness is the right task to evaluate concept removal. The images in the concept dataset with and without the concept may differ in many ways other than the presence of the concept, and this may lead to a spurious CAV. The explanation of high-level vs low-level features is vague and lacks a clear definition. The authors should provide a more rigorous definition of what constitutes a high-level or low-level feature and how it relates to the effectiveness of their method. The use of subpopulation robustness as an evaluation task is questionable, as the concept dataset may introduce confounding factors that lead to a spurious CAV.
- The figures are hard to parse (missing axes labels, legend too small). The writing in the second half (experiments, details, setup) can be significantly improved as well.

### Questions
- It would be interesting to know how sample efficient this method (as RQ3 in Section 4).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper designs a novel concept removal method based on adversarial linear classifiers trained on a concept dataset, which aims to learn representations that do not encode certain specified concepts (e.g., gender etc.) Their proposed Deep Concept Removal further incorporates adversarial probing classifiers at various layers of the network, improving out-of-distribution generalization. Experiments on distributionally robust optimization (DRO) benchmarks demonstrates the advantage of their method.

### Strengths
+ originality: this paper proposed to utilize adversarial linear classifier to gain out-of-distribution robustness on the problem of concept removal

### Weaknesses
 - lack of comparison with other concept removal baseline methods in Table 2

- lack of comprehensive results on Section 6, this paper does not show the advantage of their method on practical celebrity dataset.

- lack of ablation study on their training loss modules, for example, the effect of Penalty term of Eq. 3.2, and different values of \lambda of Eq. 3.1.

### Questions
- can the method be adapted to generative model where the concept removal task is of more importance?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper achieves deep concept removal by penalizing the norm of concept activation vectors, and experimental results demonstrate the effectiveness of this method.

### Strengths
* The method in the paper is well-motivated.
* The paper is easy to follow.

### Weaknesses
 * Lack of comparative methods. Many strategies for deep concept removal have already been proposed[1], such as adversarial concept removal mentioned by the authors. However, they did not compare their method with these classic approaches during the experimental phase. Specifically, the paper lacks a comparison with methods that explicitly aim to disentangle representations or remove specific attributes from the latent space. This is a critical omission, as it's unclear how the proposed method performs relative to established techniques in terms of both concept removal and preservation of other relevant information.

* The performance of the method presented in the paper is also lacking. Table 2 shows a comparison between the authors' method and others, but it seems their method is not optimal, performing worse in some cases than methods without concept annotation. The results in Table 2 are concerning because they suggest that the proposed method might not be effectively removing the targeted concept without negatively impacting the overall performance. It is unclear if the performance drop is due to the method's inability to isolate the concept or if it's a result of the method inadvertently removing other important features.

* From the objective function of the method, it can be applicable to different downstream tasks. However, the paper only validated it on classification tasks. Is this method equally applicable to object detection or image generation tasks? The lack of experiments on other downstream tasks, such as object detection or image generation, is a significant limitation. The paper does not provide any theoretical or empirical evidence to support the claim that the method is generalizable beyond classification. It is important to investigate how the method performs in tasks where the concept might be encoded differently or where the objective function is not a simple classification loss.

### Questions
Is this method equally applicable to other downstream tasks, such as object detection or image generation tasks?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
