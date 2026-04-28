# Investigating the Benefits of Projection Head for Representation Learning

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
\vspace{-2mm}
An effective technique for obtaining high-quality representations is adding a projection head on top of the encoder during training, then discarding it and using the pre-projection representations. Despite its proven practical effectiveness, the reason behind the success of this technique is poorly understood. The pre-projection representations are not directly optimized by the loss function, raising the question: what makes them better? In this work, we provide a rigorous theoretical answer to this question.
We start by examining linear models trained with self-supervised contrastive loss. We reveal that the implicit bias of 
training algorithms leads to layer-wise progressive feature weighting, where features become increasingly unequal as we go deeper into the layers. Consequently, lower layers tend to have more normalized and less specialized representations. 
We theoretically characterize scenarios where such representations are more beneficial, highlighting the intricate interplay between data augmentation and input features.  
Additionally, we demonstrate that introducing non-linearity into the network allows lower layers to learn features that are completely absent in higher layers. Finally, we show how this mechanism improves the robustness in supervised contrastive learning and supervised learning. We empirically validate our results through various experiments on CIFAR-10/100, UrbanCars and shifted versions of ImageNet. We also introduce a potential alternative to projection head, which offers a more interpretable and controllable design.
\looseness=-1
\vspace{-1mm}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzed an important technique in contrastive learning: the projection head. The authors theoretically demonstrated the benefits of the projection layer via a simplified model. The theoretical analysis showed that lower layers represent features more evenly in linear networks and can represent more features in non-linear networks, which implies better generalization performance in downstream tasks. Empirically, they verify the theoretical findings on synthetic and real-world datasets.

### Strengths
1. The projection layer is one of the most important techniques in contrastive learning and the mechanism behind it is still under-explored. Consequently, this paper addresses an important problem.
2. The theoretical analysis in this paper looks solid and insightful. And the empirical results verify the theoretical findings.

### Weaknesses
1. The theoretical analysis in this paper is based on a two-layer model. Is it possible to extend the results to multiple-layer networks? For example, should we discard other layers except for the projection head in downstream tasks in the deep networks? It would be better to provide more discussions about that.
2. This paper demonstrates the benefits of the projection head. However, we can observe that the designs of the projector (e.g., the layers and the dimensions) also have a significant influence on the downstream performance. Is it possible to provide some insights about the design of the projector based on the theoretical analysis in this paper? 
3. As stated in this paper, the pre-projection representations are preferred in three different scenarios and the findings are verified on the synthetic datasets. However, the authors do not show similar results (e.g., the influence of data augmentations) on the real-world datasets. It would be better to provide more empirical findings on real-world datasets.
4. I note that the abstract on the OpenReview website is different from that on the pdf file, which should be corrected.
5. The forms of references are inconsistent. For example, some of the conferences are full titles while others are abbreviations.

### Questions
see my comments above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper delves into a nuanced aspect of neural network architecture design, specifically the use of a projection head during the training phase. This technique has garnered attention due to its empirical success in enhancing representation quality. The core methodology involves appending a projection head atop the encoder during training, which is subsequently discarded, favoring the pre-projection layer representations for inference tasks.

Despite its proven practical effectiveness, a comprehensive theoretical understanding of why the projection head enhances representation learning remains underdeveloped. The paper aims to bridge this gap by dissecting the mechanics of the projection head and elucidating its impact on the learning dynamics of neural networks. This investigation is critical as it addresses a disconnect between empirical practices and their theoretical foundations in the field of deep learning.

The projection head's primary role is hypothesized to act as a regularization mechanism, potentially aiding in learning more generalizable and robust features. By expanding the representational capacity during training, the projection head could encourage the encoder to learn a broader set of features, some of which may be discarded during the projection phase but still contribute to a richer feature space in the pre-projection layer. Moreover, the projection head could serve to disentangle the feature space, making it easier for the network to differentiate between relevant and irrelevant features. This disentanglement might facilitate better generalization to new, unseen data by reducing overfitting to the idiosyncrasies present in the training dataset.

### Strengths
**Empirical and Theoretical Integration**:
The paper bridges the gap between empirical success and theoretical understanding by critically investigating the role of the projection head in representation learning. By scrutinizing a technique that has demonstrated practical effectiveness without a solid theoretical foundation, the paper contributes to a more profound understanding of neural network architectures, potentially guiding future designs with a better-informed rationale.

**Regularization and Feature Representation**:
It hypothesizes that the projection head is a regularization mechanism, allowing the encoder to explore a wider feature space during training. This could lead to more robust and generalizable representations, as the encoder is encouraged to capture a broader and more nuanced feature landscape. The paper's exploration of this aspect could elucidate how neural networks can be trained more effectively to learn generalizable features.

**Feature Disentanglement**:
The projection head's potential to disentangle the feature space is a significant strength of the paper's hypothesis. By facilitating a clearer separation of relevant and irrelevant features, the projection head might aid in reducing overfitting and improving the model's ability to generalize to unseen data. This aspect of the paper could contribute valuable insights into how neural networks can be made more interpretable and reliable.

### Weaknesses
 **Potential Overfitting Risks**:
The introduction of a projection head could potentially lead to overfitting, especially if not properly regularized or if used in conjunction with datasets that have a high degree of noise or variability. The paper should address these risks and propose strategies to mitigate them. Specifically, the paper lacks a discussion on how the increased parameter count introduced by the projection head might interact with the training data size, potentially leading to memorization of noise rather than learning generalizable features. Furthermore, the paper should explore the impact of different regularization techniques, such as weight decay or dropout, when used in conjunction with the projection head, and how these techniques might affect the final representation quality.

**Generalizability and Applicability**:
The projection head's effectiveness might vary across different architectures, tasks, and data modalities. The paper could benefit from a more detailed exploration of these variations to understand where the projection head is most beneficial and where it might be detrimental. This would enhance the paper's technical depth and practical applicability. For instance, the paper should investigate how the projection head performs when applied to convolutional neural networks (CNNs) versus transformer networks, and how its effectiveness changes when used for image classification versus natural language processing tasks. Additionally, the paper should consider the impact of different data modalities, such as text, images, and audio, on the projection head's performance, and whether specific adjustments are needed for each modality.

### Questions
1. **How does the architecture of the projection head influence the learning dynamics and final representation quality?**
   - The design choices within the projection head (e.g., the number of layers, types of activations, dropout rates) likely have a profound impact on its efficacy as a regularizer and feature disentangler. What are the optimal architectural configurations for different types of data and tasks? Investigating this could provide more nuanced guidelines for practitioners and lead to a deeper theoretical understanding of the projection head's role.

2. **What is the impact of the projection head on the interpretability of the learned representations?**
   - While the projection head might aid in learning more generalizable features, its impact on the interpretability of these features is unclear. Do the representations learned with a projection head offer better clarity in terms of feature importance or contribution to the final decision? Understanding this could bridge the gap between performance and explainability in neural networks.

3. **Can the benefits of the projection head be replicated or enhanced by alternative or complementary techniques?**
   - Are there other methods or architectural innovations that could either replicate the benefits of the projection head or enhance its effects? For instance, could certain types of normalization, attention mechanisms, or even different training paradigms offer similar or greater benefits regarding feature representation and generalization? Exploring this could lead to a broader set of tools for improving neural network training beyond the projection head.

Delving into these questions could significantly enhance the paper's contribution, offering both a deeper theoretical understanding and more practical guidelines for employing projection heads in neural network training.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the effectiveness of the projection head in self supervised contrastive learning, supervised contrastive learning and supervised learning. It provides theoretical analysis of the quality and robustness of the learned representations and their generalizability in simple linear and nonlinear models. Theoretical results are supported with experimental evaluation on several image datasets.

### Strengths
- Thorough theoretical analysis and interesting insights.
- Extensive related work.

### Weaknesses
 - Experimental evaluation is done on very simple networks and small datasets. Although the results nicely support the theoretical results, it might be beneficial to include one more complex experiment. Specifically, the experiments are limited to MNIST and CIFAR-10 with relatively simple architectures. While these experiments validate the theoretical claims, it is unclear how well these results generalize to more complex datasets and architectures commonly used in practice, such as those found in ImageNet or with deeper convolutional networks. The lack of experiments on larger datasets and more complex models leaves a gap in understanding the practical implications of the theoretical findings.
- The paper could benefit from a discussion on limitations and assumptions of the analysis. The theoretical analysis makes several simplifying assumptions, such as the use of a diagonalized network for non-linear models. This simplification may not accurately capture the behavior of fully connected networks, especially in terms of training dynamics and the learning of additional features. Additionally, the analysis of distribution shifts is limited to linear models, and it is unclear how these results extend to non-linear models, which are more commonly used in practice. A more thorough discussion of these limitations and assumptions would provide a more complete picture of the scope and applicability of the theoretical results.

### Questions
- In Definition 3, could you add details about $\phi_i$?
- Theorem 3.6 essentially tells us when it is beneficial to use pre and post projection representations, with concrete guidelines given in Corollary 3.7. Do these results hold for non linear models as well? As a stretch question, I was wondering how could one infer the downstream-relevant features and the weights of features in practice? In other words, is there a way to use your results to identify what features will be relevant for the downstream task? I am aware this might be out of scope of this work. 
- What is $\alpha_i$ in setting 2 in Sec 5.1? Could you comment on the results in Fig 1 right, where $\phi_i$ = 0.2 and 0.4, in particular, why do we see the spikes in weights in pre-features for $\phi_i$ = 0.2 and post-features for $\phi_i$ = 0.4?
- I do not understand the experiment in Fig 3b. In the text your say that “Figure 3b shows the downstream accuracy against $p_{drop}$ and s=1”. However, if s=1, it means that you only use MNIST images as input to the augmentation, and then you additionally drop the digit with probability $p_{drop}$. Doesn’t that mean your augmented image is completely black if $p_{drop}=1$?
- In Table 2, WaterBird SL results are almost the same, especially for no projection and pre-projection. Why is that? 
- Could you explain better what exactly is plotted in Figure 4?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studied a very interesting question: what makes pre-projection representations better if they are not directly optimized? Based on theoretical analysis on some toy models, they proposed that the implicit bias of training algorithms makes deeper features more unequal, and hence lower layers tend to have more normalized and less specialized representations. Then they showed that lower layers are better in the following cases: (1) data augmentation disrupts useful feature; (2) downstream-relevant features are too weak/strong in pre-training. They also showed how this mechanism makes lower representations better for supervised contrastive learning and supervised learning. Finally, they conducted some experiments to verify their theoretical analyses.

### Strengths
1. This paper studied a very interesting question: what makes pre-projection representations better if they are not directly optimized?
2. Based on theoretical analysis on some toy models, they proposed that the implicit bias of training algorithms makes deeper features more unequal, and hence lower layers tend to have more normalized and less specialized representations.
3. Then they showed that lower layers are better in the following cases: (1) data augmentation disrupts useful feature; (2) downstream-relevant features are too weak/strong in pre-training.
4. They also showed how this mechanism makes lower representations better for supervised contrastive learning and supervised learning.

### Weaknesses
My main concern is that their data and model are too simple. But if similar models are commonly used, it may be okay.

Most of the cases where lower representations are better arises from the inappropriate data augmentation (like Thm 4.2), namely the pre-training signal does not align with the downstream problem. In such cases, overfiting the pre-training data (what post-projection layers intend to do) may lead poor downstream performance. In addition to using pre-projection layers, can other regularization methods (weight decay, dropout, early stopping, etc.) also lead to satisfied performance even without projection head? I noticed that the author mentioned in the end of Sec 3 that the advantage of pre-projection representations diminishes when using weight decay.

The author mainly focused on two-layer neural networks. When there are multiple layers, how do the depth of representations affect the result? Is there any trade-off, like deeper layers have more representation power while less diversity/robustness? How to choose the appropriate depth of projection heads?

### Questions
1. I want to know whether their data model (Def 3.1) is commonly used in literature? Even though the authors' theoretical analysis are insightful, I am worried that this data model is too simply to be applied to practical scenarios.
2. Most of the cases where lower representations are better arises from the inappropriate data augmentation (like Thm 4.2), namely the pre-training signal does not align with the downstream problem. In such cases, overfiting the pre-training data (what post-projection layers intend to do) may lead poor downstream performance. In addition to using pre-projection layers, can other regularization methods (weight decay, dropout, early stopping, etc.) also lead to satisfied performance even without projection head? I noticed that the author mentioned in the end of Sec 3 that the advantage of pre-projection representations diminishes when using weight decay.
3. The author mainly focused on two-layer neural networks. When there are multiple layers, how do the depth of representations affect the result? Is there any trade-off, like deeper layers have more representation power while less diversity/robustness? How to choose the appropriate depth of projection heads?

Overall, I think this is an insightful work and I am glad to raise my score if the authors can clarify their over-simple model and give a slightly deeper answers to the above questions.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
