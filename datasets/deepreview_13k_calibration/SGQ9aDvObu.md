# DIFAIR: Towards learning differenciated and interpretable representations

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3, 3, 3, 5

## Abstract
Neural network classifiers are generally trained to differentiate between the same classes during training and testing. In order to prevent incorrect predictions, when an input image contains a class that was not part of the training set, it should be detected. The process of detection of \`\`unknown'' classes is called Open Set Recogniton (OSR). Given that a neural network extracts a representation (a feature vector) describing an image, its capacity to detect the presence of a class in an image, through the recognition of specific features, should also imply the ability to detect the absence of a \`\`known'' class, through the absence of those features in the representation. In this article, we present DIFAIR, a novel approach introducing the key characteristics that a feature representation should exhibit to ensure: (i) class separability, through predefined class positions in the representation space; and (ii) interpretability by associating each dimension of the representation with a class. We present a loss function to optimize a model, in a supervised way, in order to produce the proposed representation. Our approach assumes that unknown classes should share only a limited number of features with known classes and therefore we evaluate its performance in OSR. Finally, we visually inspect learned representations to identify the flaws of our loss function and present directions for future improvement.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors focus on learning such that results in interpretable representation, that has class-associated features and is free from distributed representations.  To that end the authors introduce a loss function targeting an optimization of the network’s learned representation, aligning it with the constraints specified for the representation space by defining an association between specific dimensions and use OSR tasks to assess the quality of the learned representation. They evaluate the proposed approach on open-set classification problem and provide insights into the model’s behavior compared to representations derived from standard mode of learning.

### Strengths
-The exposition of the paper is well done.

-The paper seems well motivated.

-The proposed loss seems reasonable in the context of interpretability for sematic reasoning and discrimination.

### Weaknesses
 - The technical contribution is limited. The main contribution of this paper is a loss term, which however has not been extensively proved effective for a broad range of applications and for various methods. The proposed loss, while novel in its specific formulation, is essentially a form of distance-based regularization, and its effectiveness compared to other established regularization techniques is not clearly demonstrated. The paper lacks a thorough investigation into the sensitivity of the loss function to its hyperparameters, and it does not provide a clear justification for the specific choice of the threshold. A more rigorous analysis of the loss landscape and its impact on the learned representations is needed.

- The evaluation is not comprehensive. Experiments only on small small-scale datasets are conducted, making the evaluation less convincing. Results on large-scale datasets should be conducted and more extensive analysis should be performed to have a more comprehensive evaluation. Specifically, the paper should evaluate the performance of the proposed method on datasets with a significantly larger number of classes and instances, and it should also consider datasets with more complex data distributions. The experiments lack a systematic comparison against a wider range of baseline methods, including state-of-the-art approaches for open-set recognition. The evaluation should also include a more detailed analysis of the computational complexity and scalability of the proposed loss term.

-  The proposed method falls behind with many of the existing methods as shown in Table 1.

### Questions
How does the method differentiates and compares with other Self-Supervised Learning Methods or their equivalent Supervised counterparts?

### Soundness
2 fair

### Presentation
3 good

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
This paper proposes a new loss term to address the open-set recognition task. The loss term enables a more interpretable representation and the correspondence different dimensions of the learned feature and the classes can be interpreted. Experiments on the multiple datasets verify the effectiveness of the proposed method.

### Strengths
- The proposed loss term is well-motivated and technically sound. 

- Experiments on multiple datasets verify the effectiveness of the proposed method and analysis has been conducted to study of the designs. 

- The paper is overall well presented.

### Weaknesses
1.   Closed-set classification performance.

DIFAIR's fundamental premise is that each representation dimension corresponds to a specific class. To accomplish this, DIFAIR trains an anchor for each class, ensuring that only certain dimensions are activated for that class. While this might enhance Open-Set Recognition (OSR) and model interpretability, it raises the question of whether such a model could maintain the strong closed-set classification performance of conventional deep visual models, particularly when trained on large-scale datasets like ImageNet. The authors suggest that the hypersphere around each anchor provides some tolerance for activating other class features, but there seems to be a trade-off between interpretability (requiring low tolerance) and closed-set classification performance (requiring high tolerance). It's unclear if DIFAIR can easily find a balance point that provides both satisfactory closed-set classification performance and good interpretability. The reliance on a fixed anchor for each class, while promoting interpretability, may inherently limit the model's capacity to capture the full complexity and variability within each class, potentially leading to suboptimal performance when compared to models that learn more flexible representations.

2. Lack of theoretical analysis.

The paper lacks essential theoretical support and analysis. Many ideas seem to spring from intuition. While hypotheses and assumptions are discussed in Section 3.3, and some are empirically verified, none of them is well theoretically supported. The absence of a formal framework makes it difficult to understand the underlying mechanisms and limitations of the proposed approach. For instance, a theoretical analysis of how the hypersphere radius affects the trade-off between interpretability and closed-set performance would be beneficial. Furthermore, a theoretical justification for why the proposed dimensional separation leads to better OSR performance is needed.

3. Experiment and visualization limitations.

3a. The evaluation of OSR performance is solely based on one model, VGG32. The paper's claims would be more persuasive if additional models, including CNNs and ViTs, were evaluated. The choice of VGG32, a relatively older architecture, raises concerns about the generalizability of the findings to more modern and complex architectures. It is important to verify if the observed trends hold across different model families.

3b. The OSR performance of DIFAIR, as reported in Table 1, does not demonstrate significant improvement over previous OSR methods. The reported results are only comparable, not superior, which questions the practical significance of the proposed method. The lack of substantial performance gains makes it difficult to justify the increased complexity introduced by DIFAIR.

3c. Justification for the improved interpretability of DIFAIR is only provided through simple visualizations based on CIFAR10. More convincing evidence, such as visualization results from a dataset with more classes (like TinyImageNet), visualizations showing shared visual features in multiple classes and so on, would be beneficial. The current visualizations are insufficient to demonstrate the claimed interpretability, and the use of a more complex dataset would be necessary to validate the method's effectiveness in real-world scenarios. Furthermore, the visualization should show that each dimension is indeed capturing specific features, rather than just showing that different dimensions are activated for different classes.

### Questions
See the weakness above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces DIFAIR (Differentiated And Interpretable Representations), an approach designed to differentiate between known and unknown classes in Open-Set Recognition (OSR) and improve the interpretability of neural network classifiers. DIFAIR introduces class anchors in the representation space and optimizes the model to produce representations close to these anchors. Each dimension in the representation is associated with a specific class. The technique's performance is comparable to existing methods in OSR. Some simple visualization results are also provided to somehow show learned representation of DIFAIR extracts independent features on different dimensions.

### Strengths
1. The paper is generally well-structured and lucid in its exposition.

2. The concept of training a model where each dimension signifies specific visual features from certain classes is intriguing. This could not only lead to a model with strong OSR performance but also pave the way for more transparent and interpretable deep visual models.

### Weaknesses
1. It seems that the proposed method is only enforcing data representation to be within the spherical area around anchors of each class. Similar ideas have been explored in previous works such as [1] on other topics. Therefore, the author have to justify the extra insights provided by their work.
2. Empirical validation of the paper can be improved.
3. The writing of the paper can be improved. For example, in Figure 3 (a), it is not quite clear what are the x- and y- axis, and what does the value of the heatmap represents.
4. According to the Table 1 in the paper, it seems that the performance of the proposed method is far worse than the current state-of-the-arts.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an idea of disentangling features of different classes to achieve open set recognition. A training method called DIFAIR is proposed to achieve this goal. Empirical validation on DIFAIR are provided.

### Strengths
The idea of disentangling features of different classes is reasonable.

### Weaknesses
It seems that what is formulated as "fixed anchors" ($\mathcal{A}$) is actually scaled one-hot labels in supervised learning.
So the difference between the conventional $\ell_2$ regression of labels is just that the proposed method is regressing N of these scalars per class. I'm not sure if this is any interesting for ICLR audience.

Also, no performance improvement is observed, I'm not sure if the proposed offers any practical advantages.

Also, I think the paper is missing large bodies of related works.
- interpretability works, which try to disentengle representations (dimension) or associate certain dimensions to certain classes
    - Interpretable Explanations of Black Boxes by Meaningful Perturbation, Fong et al. 2017, ICCV, and many follow-ups
- metric learning works, which learn multiple linear sub-spaces for each class
    - SoftTriple Loss: Deep Metric Learning Without Triplet Sampling, Qian et al. 2017, ICCV, and many follow-ups.

Some other comments:
- Figure-2 does not offer much (if any). Why would the subplot on the left be a "standard" learning setting. If the class weights are orthogonal, it becomes what is depicted on the right. It would be nice to use this space with a figure showing the method diagram.
- Not sure if Section-3.3 offers much (if any). It would be nice to provide more experimental results, given that the current ones in Table-1 are already discouraging. Analysis on interpretability of representations could be an option.

### Questions
1. As far as I am concerned, DIFAIR only introduces an optimization objective to enforce representations being compact around anchors of each class. How can the method enforce the representations of unseen classes to be out of the spherical areas of the known classes?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In standard deep image classification models (e.g. ResNet50, ViT), there is usually a linear layer producing class scores (usually 1 score per class).
This paper proposes to output N scores per class, instead of 1.
The network is then trained with $\ell_2$-distance over scaled N-hot labels (here I abuse the one-hot vector notation by saying N-hot as there are N class scores to regress now).
This way, sparse set of features are learned for each class, which, in the end, can better suit open-set recognition tasks.
However, unfortunately, all the results achieved by the proposed method are worse than the best compared baseline.

### Strengths
Learning interpretable representations is an important research problem, especially because more and more ML-based products are interacting with humans in daily life.
The paper is making an attempt to learn such representations, and it overall reads fine.
Open-set recognition experiments are performed on 6 datasets including MNIST, SVHN, CIFAR10, CIFAR+10, CIFAR+50 and TinyImagenet.

### Weaknesses
 - Even though the authors claimed that their approach would yield "interpretable" representations, the semantic meaning of each feature dimension in the representation space is unclear. I would recommend scaling back on the claim with regard to "interpretability."
- While the proposed DIFAIR is promising and requires no "known unknowns" during training, its OSR performance is not as good as simple competing methods such as MLS (especially on CIFAR10 and CIFAR+N). Specifically, the performance gap on CIFAR10 and CIFAR+N datasets raises concerns about the method's robustness and generalizability to more complex datasets. The fact that a simpler method like MLS outperforms DIFAIR on these benchmarks suggests that the proposed approach may not be capturing the underlying data distributions as effectively as other methods, or that the training procedure may not be optimized for these datasets.

### Questions
I would like the authors to address the weaknesses I mentioned above.
Regardless, I'm not sure if ICLR is a good fit for this submission.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors proposed a method called DIFAIR for learning differentiated and interpretable representations. The proposed method involves: (1) modifying a given convolutional neural network by removing the classification head and appending a convolutional layer with N*K filters (N = the number of feature dimensions allocated for each class, K = the number of training classes) followed by a global average pooling, which results in a feature vector z of dimension N*K; (2) representing each class with a radius r hypersphere around an N*K-dimensional class anchor vector, which is 0 everywhere except the the dimensions assigned to that class; (3) training the network by minimizing the Euclidean distance between the feature vector z and the class anchor, if z lies outside the hypersphere of radius r centered at the anchor. The authors applied DIFAIR to open-set recognition (OSR) benchmarks used by Neal et al. (2018), and compared their approach with competing state-of-the-art OSR methods.

### Strengths
- The proposed DIFAIR is technically sound, and does provide promising results on OSR problems.
- The proposed method requires no additional data for "known unknowns," unlike DCHS and (ARPL+CS)+.

### Weaknesses
- Even though the authors claimed that their approach would yield "interpretable" representations, the semantic meaning of each feature dimension in the representation space is unclear. I would recommend scaling back on the claim with regard to "interpretability."
- While the proposed DIFAIR is promising and requires no "known unknowns" during training, its OSR performance is not as good as simple competing methods such as MLS (especially on CIFAR10 and CIFAR+N).

### Questions
- It is not clear to me how you applied Maximum Output Score (MOS) on DIFAIR. Can you explain that? I would recommend including this information in the main paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
