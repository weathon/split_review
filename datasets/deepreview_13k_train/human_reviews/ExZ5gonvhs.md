# GPS-SSL: Guided Positive Sampling to Inject Prior into Self-Supervised Learning

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
We propose \textit{\ourstrategyfullname} (\ourstrategy), a general method to inject a priori knowledge into Self-Supervised Learning (SSL) positive samples selection. 
Current SSL methods leverage Data-Augmentations (DA) for generating positive samples and incorporate prior knowledge--an incorrect, or too weak DA will drastically reduce the quality of the learned representation. 
\ourstrategy proposes instead to design a metric space where Euclidean distances become a meaningful proxy for semantic relationship. In that space, it is now possible to generate positive samples from nearest neighbor sampling. Any prior knowledge can now be embedded into that metric space independently from the employed DA. From its simplicity, \ourstrategy is applicable to any SSL method, e.g. SimCLR or BYOL.
A key benefit of \ourstrategy is in reducing the pressure in tailoring strong DAs. For example \ourstrategy reaches 85.58\% on \cifarten with weak DA while the baseline only reaches 37.51\%.  
We therefore move a step forward towards the goal of making SSL less reliant on DA.
We also show that even when using strong DAs, \ourstrategy outperforms the baselines on under-studied domains.
We evaluate \ourstrategy along with multiple baseline SSL methods on numerous downstream datasets from different domains when the models use \textit{strong} or \textit{minimal} data augmentations.
We hope that \ourstrategy will open new avenues in studying how to inject a priori knowledge into SSL in a principled manner.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes Guided Positive Sampling Self-Supervised Learning (GPS-SSL), a method that integrates prior knowledge into Self-Supervised Learning (SSL) to improve positive sample selection and reduce reliance on data augmentations. Based on pretrained visual models and target dataset, GPS-SSL creates a metric space that facilitates nearest-neighbor sampling for positive samples. The method is applicable to various SSL techniques and outperforms baseline methods, particularly when minimal augmentations are used.

### Strengths
- Extensive experiments show the effectiveness of the GPS strategy.
- The paper is easy to follow.

### Weaknesses
 - The employment of prior knowledge, specifically in the form of a pretrained visual model and the target dataset, diverges from the fundamental principles of Self-Supervised Learning (SSL). This reliance on pre-existing models and target datasets introduces a dependency that undermines the core idea of learning representations without explicit labels. The method's performance is therefore contingent on the quality and relevance of the chosen pretrained model, which might not always be available or suitable for all tasks.
- The incorporation of such prior knowledge raises concerns about the fairness of comparisons with existing SSL methods. There is a potential risk that the pretrained visual model and target dataset might leak additional information into the model, thereby skewing results and leading to issues of unfairness. The use of a pre-trained model, even if not explicitly trained on the target task labels, can implicitly encode biases or task-specific information that gives GPS-SSL an unfair advantage over methods that start from random initialization. This makes it difficult to isolate the true contribution of the proposed positive sampling strategy.
- The difference between GSP-SSL and NNCLR lies primarily in their respective positive sampling strategies. However, the novelty of the proposed strategy is limited. The core mechanism of using nearest neighbors in an embedding space for positive sample selection is already present in NNCLR, and the paper does not sufficiently demonstrate a significant conceptual leap beyond this existing approach.

### Questions
- It would be better to make prior knowledge in an unsupervised manner, except using pretrained visual model and target dataset.
- The supervised results are supposed to be shown in Table 2.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed the Guided Positive Sampling (GPS) approach to
finding positive pairs in self-supervised learning, without data
augmentation.  For each instance, a nearest neighbor is found in an
embedding space pretrained with another dataset or with a variational
autoencoder on the same dataset.  The corresponding instance becomes
the positive instance for self-supervised learning.

In their experiments, they consider using GPS with SIMCLR, BYOL,
Barlow, and VICreg on five datasets.  For GPS, they use embeddings
from supervised training, CLIP or VAE.  Generally, empirical
results indicate that using GPS outperforms, particularly with weak
augmentations.

### Strengths
Not relying on heavy handcrafting of data augmentation for
self-supervised learning is interesting.  Using prior knowledge based
on a pretrained encoder, they propose to find a nearest neighbor to
form a positive pair.  Generally, empirical results indicate that using
GPS outperforms, particularly with weak augmentations.

### Weaknesses
With prior knowledge, GPS seems to have an advantage over regular SSL,
which generally does not use prior knowledge.  According to Figure 1,
data augmentation is used in GPS-SimCLR.  So GPS seems to differ only
in the use of prior knowledge to find positive pairs.

Details are in questions below.

1.  Theorem 1: GPS-SSL: employing eq (2) or (3) into eq (1)?

2.  Table 2: why are two different kinds of prior knowledge is used?

3.  How is $Tau$ set in Equation 3?

4.  With prior knowledge from another encoder, GPS has an advantage.
    Hence, comparison with methods that don't have prior knowledge
    might not be fair.  Could the regular SSL (with augmentation) also
    use prior knowledge?  For example, the encoder is initialized by
    prior knowledge and then regular SSL is performed.

5.  Sec 4.1, how do you predict if the classes do not overlap in the
    training and test sets (unseen classes branches/chains)?

### Questions
1.  Theorem 1: GPS-SSL: employing eq (2) or (3) into eq (1)?

2.  Table 2: why are two different kinds of prior knowledge is used?

3.  How is $Tau$ set in Equation 3?

4.  With prior knowledge from another encoder, GPS has an advantage.
    Hence, comparison with methods that don't have prior knowledge
    might not be fair.  Could the regular SSL (with augmentation) also
    use prior knowledge?  For example, the encoder is initialized by
    prior knowledge and then regular SSL is performed.

5.  Sec 4.1, how do you predict if the classes do not overlap in the
    training and test sets (unseen classes branches/chains)?

--------  after response from authors ---

I think the authors performed experiments that remove the advantage of prior knowledge used in GPS and the results indicate GPS can improve performance over regular SSL.

### Soundness
3 good

### Presentation
3 good

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
A method using prior knowledge to sample the positive data is proposed. It is supposed to mitigate the importance of data augmentation in self-supervised learning. The proposed GPS-SSL has shown superior capability over the methods with existing augmentation strategies.

### Strengths
+ Studying new strategies that rely less on data augmentations in self-supervised learning is worthwhile to the representations learning fields.
+ Exploring the pre-trained models (CLIP, Supervised models, VAE) for improving SSL might be interesting.

### Weaknesses
 + The proposed method needs a heavier component (such as a neural network ResNet-50) to generate the positive data sample, which is significantly computational compared to a simple calculation of data augmentation even for strong augmentations with a series of cropping, color jittering, distortion, hue, etc... The computational overhead of using a ResNet-50 to generate positive samples is a significant practical concern, especially when compared to the efficiency of standard data augmentation pipelines. This additional computational cost should be thoroughly justified by a substantial improvement in performance, which is not clearly demonstrated.

+ With the aid of a strong knowledge (and heavy) model trained on millions or hundred million of data (CLIP, ImageNet) the performance of the proposed method brings minimal advantage even worse than the existing SSL method such as VICReg in Table 2 with strong augmentation. In the weak augmentation setting, GPS-SSL may give better performance but still lag significantly behind the optimal setting (strong augmentation) of both streams, making it questionable about the contribution of the proposed method. The reliance on pre-trained models like CLIP and ImageNet introduces a potential confounder. The marginal improvements observed with GPS-SSL, especially when compared to existing SSL methods with strong augmentations, raise concerns about whether the gains are due to the proposed method or simply leveraging the pre-trained model's knowledge. It is also unclear if the performance difference in weak augmentation settings justifies the added complexity.

+ SSL contains another branch that is also very promising with the fine-tuning accuracy on downstream tasks such as MAE [1], this approach also depends very little on data augmentation (only cropping or without any augmentation already made the very good performance). This example (MAE method) will challenge the proposed method in terms of dependency on augmentation because the proposed method could not work without augmentation. I believe that modern SSLs should include this metric (fine-tune accuracy) and compare both contrastive learning and MAE approaches. The evaluation of self-supervised learning methods should include fine-tuning performance on downstream tasks, especially given the success of methods like MAE [1] that demonstrate strong performance with minimal data augmentation. The proposed method's inability to function without augmentation is a limitation that should be addressed by comparing against methods that minimize augmentation dependency.

+ It should also include the linear evaluation of the only CLIP RN50 or supervised RN50 model when they have been used as the feature extractor for the downstream tasks on each considered dataset. It is to see without any training, how well these pre-trained model can perform, and based on that we can assess their contribution to the GPS-SSL (which is a combination of existing SSL + pre-trained CLIP/RN50). A linear evaluation of the pre-trained models (CLIP RN50 or supervised RN50) used as feature extractors is necessary to understand their contribution to the performance of GPS-SSL. Without this baseline, it is difficult to determine if the observed improvements are due to the proposed method or simply leveraging the pre-trained model's capabilities.

+ Another point is that the experimental setting is not practical and sufficient to demonstrate the effectiveness of GPS-SSL when evaluating self-supervised contrastive learn is that they only consider pretraining with 200 epochs, which is very few epochs required by SSL models to fully converge. As shown in SimSiam or many SSL (MoCo, BYOL, Barlow Twins, VICREG,... ) the performance is best achieved with long enough self-supervised pretraining (800-1000 epochs). As a result, the comparison in long training should be considered for both methods. The limited pretraining of 200 epochs is insufficient to demonstrate the effectiveness of GPS-SSL. Self-supervised learning methods typically require longer training periods (800-1000 epochs) to fully converge. The experimental results should include comparisons with longer training schedules to ensure a fair evaluation.

+ It is not clear what is the metric they have shown in Table 1. Reading its caption, it is challenging to capture what metric they are comparing, top-1 ACC or error or something else.

### Questions
See weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
