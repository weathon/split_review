# Data-Evolution Learning

- Decision: Reject
- Scores: 5, 1, 1, 3

## Abstract
Recent advancements in machine learning have been driven by models trained on large-scale, high-quality datasets. However, the practical application of these models faces two significant challenges: the infeasibility of acquiring precise labels in real-world settings and the substantial computational burden imposed by training large models. While existing approaches—such as self-supervised learning, weak supervision, noisy label learning, and dataset distillation—address these challenges from a model-centric perspective, they often overlook the potential benefits of optimizing the data itself.
This paper introduces a novel data-centric learning paradigm where both the dataset and the model co-evolve during the learning process.
We formalize this paradigm and propose a Data-evolution Learning Algorithm (DeLA), which offers three key advantages: optimized dataset generation, versatile dataset compatibility, and effective utilization of prior knowledge.
Extensive experiments demonstrate that DeLA enables the creation of optimized datasets for reuse in subsequent training, effectively addressing diverse datasets with varying target types. Moreover, DeLA accelerates learning by utilizing architecture-agnostic, open-source prior models for efficient data creation.
Notably, DeLA frequently outperforms traditional SOTA model-centric methods in self-supervised and noisy label learning.
Furthermore, its simplicity enables implementation in only two lines of PyTorch code, offering significant potential for advancements in representation learning.
Our code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduced Data-Evolution Learning, which is a data-centric method for simultaneous evolution both datasets and models during the learning process. The traditional model training method replies on the datasets and might be limited to the dataset quality. The DELA method proposed an iterative framework to optimize the model progressively by using various types of data, including noisy and unlabeled datasets.

### Strengths
This method enhanced the model training efficiency by creating refined datasets. In addition, it achieves comparable results to traditional training model by using prior knowledge and evolving datasets. 
This method is also performs well across different network structures and shows good results with different type of datasets.

### Weaknesses
This method partially relies on leveraging the pre-trained models, which could be restrictive for the model training without relevant prior models/datasets.

The tuning of hyper-parameters seems critical for achieving good results, which might be challenges for reproducing the results on different model structures. 

There has no comparison results with other methods on the table.

### Questions
1. Since the DELA leverages model priors, does the accuracy significantly influenced if the t-1 model performs low accuracy? If so, how to keep the prior model performs well?
	2. As the paper mentioned, this method is able to handle nosy labels, would extreme nosy level labels degrade the quality of evolved datasets? (such as adversarial noises). Are this method can detect and mitigate the extensive nose?
	3. Does this method has trade-offs between data efficiency and model performance? If so, are there any scenarios that the static dataset might still be preferable? 
	4. From the Table 1, we could see the DELA method performs good results compare to the original accuracy. Are there any baseline or state-of-the arts method can be compared with? 
	5. The paper mentioned that the standard setting of 100 epochs for full evolution is enough. Does it related to other hyper-parameters? Such as batch size, total iteration steps, model size, FLOPs, learning rate, etc.
If the dataset is super small, for example, 20 images/class, does the method still works with evolution? What's the limitations of dataset?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper proposes a new problem setting called data-evolution learning, in which data and models are updated simultaneously, and introduces the data-evolution learning algorithm (DeLA). DeLA updates data labels after updating the model in one step by calculating the exponential moving average of the labels from the previous step and the predicted labels from the training model. Through experiments, the paper shows that DeLA improves the performance of training models and that datasets updated with a model can be transferred to train other models.

### Strengths
- The paper proposes a new problem setting called Data-evolution Learning. Focusing on data-centric perspectives is important in the machine learning community.
- The paper empirically shows that data-evolution learning has the potential to improve the performance and transferability to other model training.

### Weaknesses
- The largest concern is that it is unclear why the proposed method provides improved generalization performance. The paper claims that the proposed method optimizes the dataset, but in fact, it does not define an objective function for optimizing the data; rather, it simply updates it with existing labels and pseudo-labels represented by the EMA of the model prediction. Why does this achieve the desirable properties described in Definition 1? The paper attempts to prove that the model and dataset converge at the optimal solution by Theorem 1, but the proof in Appendix A uses a different definition of the pseudo-labels and does not appear to prove the property claimed in Theorem 1. The paper should clarify why the generalization performance could be improved by the proposed method more solid evidence..
- The proposed method's design is unconvincing. It restricts the loss function to cosine similarity in updating the model in Eq. (3), but there is no sufficient explanation for this.
- The problem setting is ambiguous. In the experiments, the paper uses self-supervised learning (SSL) and weakly supervised learning (WSL) as baselines for comparison. However, the proposed method and these paradigms are orthogonal and should not be compared to each other. Therefore, comparisons with SSL and WSL are not meaningful in asserting the validity of the method.
- The paper does not compare to a simple but important baseline; the blending of labels by Eq. (4) is similar to knowledge distillation because knowledge distillation also uses the prediction of a teacher model for training student models. In this sense, the paper should be the most naive baseline for the dataset created by Eq. (4) using the trained teacher model with the original datasets.
- The proposed method is not a perfect data-centric approach. Although the paper introduces the proposed method as a data-centric approach, experimental results such as Table 1 confirm that there are model-dependent differences in accuracy. The data-centric approach [a] is a general term for methods that fix the model and improve the data. In this sense, the proposed method is a model-centric approach rather than data-centric.
- Figure 1 is misleading because it draws the input sample $x$ as if it is being optimized, but in fact, just data augmentation is applied.
- The paper emphasizes the proposed method's efficiency but ignores the cost of updating datasets. Table 1 shows that the optimal prior model for each target dataset and architecture is different, so the proposed method just adds a new hyperparameter, which does not solve the efficiency issue.
- The experimental protocol is unclear and unreliable. For example, the SSL experiment in Sec. 4.5 claims to use an unlabeled dataset. However, the DeLA results in Table 4 are the same as the DeLA* results in Table 2, and thus, it is possible that they are comparing results trained on a supervised dataset with the results on the unsupervised dataset.

[a] Zha, Daochen, et al. "Data-centric artificial intelligence: A survey." arXiv preprint arXiv:2303.10158 (2023).

### Questions
- The proposed method assumes that data extensions exist (Eq.(4)). Can this be used with modalities other than images?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces a new “data-evolution learning paradigm,” challenging the traditional deep learning approach that only the model should be updated during training. Instead, this paradigm proposes updating both the model and the data to enhance performance. To implement this idea, the paper presents the Data-Evolution Learning Algorithm (DeLA), where data is iteratively updated through model switching. The authors claim that DeLA significantly outperforms existing self-supervised learning (SSL) frameworks and other model-centric approaches, achieving superior results.

### Strengths
This paper offers a new perspective of SSL, where self-supervised learning can be viewed as model-data evolution paradigm, which can explain the SSL's performance.

### Weaknesses
Regarding the label is actually a feature map of projection head and predictor (line 918(This paper essentially rebrands several established concepts from self-supervised learning (SSL) approaches and can be seen as a minor modification of the original SSL framework, MoCo [1], which was one of the first SSL methods. The primary difference lies in how the feature map is generated. Specifically:

In MoCo:

$$y = \left(\sum_{n=1}^N (1 - \lambda)^n f_n \right)(x)$$

where $f_n$  denotes the feature map generated by the  $n$-th iterate of the student model (or a “momentum-updated” encoder). Here, the summation is applied to the model function first, and the combined model output is then applied to the input $x$ .

In DELA:

$$y = \sum_{n=1}^N (1 - \lambda)^n f_n(x)$$

where each feature map $f_n(x)$  is generated by applying the  $n$-th iterate model directly to the input $x$ , and then the outputs are summed.

This difference in parentheses placement results in effectively the same computation process. Thus, DELA lacks substantial novelty, as it simply repackages MoCo’s concept by slightly modifying the feature generation approach.

Also, in line 918, algorithm section, it says the update loss is just contrastive loss calculating the similarity. This indicates that every structructure is same except the order of parenthesis

Furthermore, this dynamic updating of feature maps could be inefficient from a memory perspective, as it requires continuously storing feature maps on the GPU in addition to the existing MoCo algorithm. In this case, the number of floating-point values would be $O(N \times d)$, where N is the number of data points, and d is the size of each feature map. This approach offers no computational advantages over MoCo in terms of efficiency.

[1] He, Kaiming, et al. "Momentum contrast for unsupervised visual representation learning." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2020.

### Questions
In line 443, the paper claims that DINO trained on ImageNet achieves a performance of 52.2 on ResNet-50. However, according to the official DINO GitHub repository, its performance is actually 75.3% on the same model [1]. How is this discrepancy come from??

[1] https://github.com/facebookresearch/dino

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
3

### Summary
This paper presents a novel training paradigm where the data evolves along with the model during the training process, allowing both the training data and the model to be optimized simultaneously. This approach can be applied to datasets containing noisy labels or unlabeled data, enabling gradual performance improvement through mutual feedback between the data and the model. Through this methodology, accelerated model training and enhanced model performance are achievable. Experiments were conducted on CIFAR-10/100 and ImageNet datasets, utilizing RN18, RN50, and ViT-T/16 architectures. When applying DELA, the model demonstrated higher performance compared to using a static dataset, suggesting potential advantages in data and computational efficiency.

### Strengths
1. The idea of simultaneously optimizing data and the model presented in the paper is highly innovative, and an appropriate methodology is suggested to achieve this.
2. A versatile methodology is proposed, applicable to both noisy labeled data and unlabeled data.
3. Compared to existing noisy-label learning methods and self-supervised learning methods, it achieved competitive performance.

### Weaknesses
1. There is a significant performance variation depending on the choice of the prior model. A method for either reducing performance discrepancies or pre-selecting prior models capable of achieving high performance is necessary.
2. In Table 2, results are reported for experiments using only 20/40/60% of the total data samples, but the intention behind these experiments is unclear. Additionally, on what criteria was the data selected?
3. While Section 4.2 emphasizes training efficiency, based on the caption in Table 1, this appears to be calculated simply by training steps (if otherwise, please provide the specific criteria used to calculate the training budget). Since DELA requires additional computation costs to evolve data labels, this may not be a fair comparison. A more reliable efficiency metric, such as wall clock time for total training duration, would be beneficial.
4. Given the nature of the methodology, where the model undergoes iterative self-learning, it seems likely that overfitting could be an issue. An analysis of overfitting would be appreciated.

### Questions
1. In the experimental results, ViT-T/16 consistently scores lower than ResNet-18 and ResNet-50 in all cases. Was this experiment conducted accurately? Providing reliable data or sources regarding the performance of ViT-T/16 would be helpful.
2. The use of the term "Original" may cause confusion. Typically, "Original" suggests ERM training that utilizes the entire dataset and labels. Since it has a different meaning in this paper, perhaps consider changing the term.
3. Please refer to the identified weaknesses.

### Soundness
3

### Presentation
1

### Contribution
3
