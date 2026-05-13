# Anomaly Detection by Context Contrasting

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
Anomaly detection focuses on identifying samples that deviate from the norm.
When working with high-dimensional data such as images, a crucial requirement for detecting anomalous patterns is learning lower-dimensional representations that capture concepts of normality.
Recent advances in self-supervised learning have shown great promise in this regard.
However, many successful self-supervised anomaly detection methods assume prior knowledge about anomalies to create synthetic outliers during training.
Yet, in real-world applications, we often do not know what to expect from unseen data, and we can solely leverage knowledge about normal data.
In this work, we propose \loss, which learns representations through context augmentations that allow us to observe samples from two distinct perspectives while keeping the invariances of normal data.
\loss learns rich representations of context-augmented samples by clustering them according to their context while simultaneously aligning their positions across clusters.
At test time, representations of anomalies that do not adhere to the invariances of normal data then deviate from their respective context cluster.
Learning representations in such a way thus allows us to detect anomalies without making assumptions about anomalous data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Dear Authors, thanks for submitting to ICLR.

In this paper, the authors propose a novel anomaly detection method with context-aware data augmentation, termed $CON_2$. Given only normal training data, $CON_2$ augments the dataset through a generator, producing a diverse set of synthetic instances that retain similarity to the original data while introducing unique variations. This generator is designed using an AutoEncoder structure enhanced by contrastive learning and a specialized loss function.

The anomaly detection component in $CON_2$ utilizes two primary metrics: (1) it assesses the presence of similar instances to the input data, incorporating the generator’s output, and (2) it applies data augmentation to the input at test time, subsequently measuring the average similarity between the real and generated data. Evaluation on representative datasets demonstrates that $CON_2$ outperforms state-of-the-art methods in certain cases when optimally configured.

### Strengths
1. The proposed method mitigates bias introduced by synthetic anomalies by exclusively leveraging augmented normal data for anomaly detection. Rather than relying on artificially generated anomalies, it detects anomalies by augmenting the normal dataset and comparing the input against an expanded set of potential normal instances, including both real and synthetic normal data.
2. This algorithm requires no anomalous data during training, a practical approach given the rarity and unpredictability of anomalies.
3. Leveraging AutoEncoder and contrastive learning, the model effectively extracts critical information and represents it from multiple perspectives, enabling it to discern whether anomalies arise from content, context, or both.

### Weaknesses
Technical Aspect:
1. The method is sensitive to context augmentation methods, which is demonstrated in evaluation part as well. However, there is no systematic method about how to choose proper augmentation method. If use wrong augmentation, this method may perform worse than baselines. (see Table 1). Suggestion: you may consider using validation data to automatically choose augmentations, or if you could provide guidelines for selecting augmentations based on dataset characteristics.
2. Even consider optimal augmentation method only, the performance gain to baselines is marginal in many cases. For example, I cannot tell $CON_2$ is better than baselines in Figure. 4. For instance in Figure 4, UniCon-HA outperform $CON_2$ on Bird, Deer, Horse, and Ship, 4 out of 11 classes. I would suggest statistical tests to demonstrate the significance of their performance gains over baselines, such as t-Test. It would also be helpful to measure the epistemic uncertainty by runing multiple times with different random seed, so that you will know if the the 7 out 11 performance gain is the worst case or best case.
3. The second anomaly score is questionable, start from line 306, page 6. With augmentation, we should obtain different representations of the input data, some of them maybe aligned with existing normal data well. Therefore, we should use some metric like maximal score to highlight the matching, instead of averaging out the potential matching (might be sparse). Suggestion: you might compare the current approach with a max-based score and discuss the trade-offs between the two approaches.
4. Ablation study is not comprehensive. It cannot show how the loss function influence the performance, and does not mention how the anomaly detection metric influence the detection result. As a result, the loss function and metrics are not properly reasoned and tested. Suggestion: please add the experiment with solely one of two loss functions, and also add the result the anomaly detection result with just one anomaly score as metric.

Writing:
1. Figure 1 is not referred at the beginning of the paper but it is put to page 2, and it is hard to understand. The loss function is introduced on page 5, section 3.2, but it is mentioned here without any explanation or reference. To address this, the author may refer to figure 1 in the later part of introduction, when introducing the proposed solutions. Please add a cross reference to the definition of loss function in the caption of Figure 1.
2. Figure 2 and Figure 3 are not on the page they are refered to. Please nsure all figures are properly placed and referenced in the final version.
3. Page 6, line 311, the anomaly score function have a new symbol at the last component. I would suggest a clarification in the following text right after the equation to explain what the "$\circ$" means.
4. Please add number to the equations.

### Questions
1. Please correct or clarify the writing issues in the weaknesses. 
2. Can you please clarify what the "$\circ$" means in page 6 line 311?
3. Can you please explain the second metric for anomaly score? Why take the average 1/A and why sum between 1~A/2 interval? 
4. Please clarify why the average is used in the second anomaly score? From the definition, I think a maximal value based metric makes more sense. Please add this comparision in section 4, or around the ablation study.
5. Can you please add the following ablation study: (1) using L_{context} or L_{content} only, (2) show how each of the two anomaly score contribute to the anomaly detection decision.
6. In the evaluation, please add more details about the result, including a breakdown of precision, recall, and F1 score.
7. Can you please clarify if we can select optimal augmentation method automatically? Otherwise, it may not able to guarantee the performance gain.

### Soundness
2

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
4

### Summary
This paper aims to address anomaly detection in a setting where no outliers or pre-trained models are available. The author aims to use a set of augmentations such that augmented images are (i) distinct - images from different augmentations are separated (ii) aligned - augmentations are distance preserving. They use a contrastive loss to ensure (ii). Anomalies are scored using this representation in one of two ways: kNN and Mahalanobis distance. Results are better than other SSL methods in standard datasets and better than CLIP-AD on two medical datasets.

### Strengths
1. Detailing the desiderata of augmentation in terms of distinctiveness and alignment is interesting, and to the best of my knowledge, novel.
2. Results are strong w.r.t. to other SSL methods.
3. Figure 3 is a very nice illustration of the main technical point.

### Weaknesses
1. There is somewhat misleading about covering pre-trained based methods as "outlier detection". There is a vast number of papers showing that pre-trained features, while reliant on seeing images not in the training set, are much more generalizable than outlier exposure. Namely, strong visual features go beyond purely adding prior knowledge about specific anomalies [1][2]. Specifically, methods leveraging pre-trained models often demonstrate robustness to shifts in the data distribution, a property not necessarily guaranteed by methods relying solely on outlier exposure. This distinction is crucial and should be acknowledged more explicitly.
2. Only one none-SSL method is compared, and not the most standard one. The choice of a single, potentially less representative, non-SSL baseline limits the conclusions that can be drawn about the superiority of the proposed method. A more comprehensive comparison against established non-SSL techniques is needed to validate the claims.
3. The main results table, justifying the focus on SSL, shows only two datasets. The limited number of datasets, especially in the main results table, weakens the generalizability of the findings. The paper should include more diverse datasets to support the claim that the proposed method is superior to other approaches.

Minor comments:
4. The paper claims (line 46) "without assuming prior knowledge about anomalies". I find that misleading, prior are always needed in order to generalize anything to an unseen test. Even more so in unsupervised settings. In this case, the priors are the inductive biases induced by the augmentations among other things.
5. I found Figure.1 more confusing than helpful.

### Questions
1. Please compare to more pre-trained-based methods. E.g., (Cohen & Avidan, 2022; Reiss & Hoshen, 2023;
Li et al., 2023) cited by your paper.
2. Please extend this comparison to more medical datasets. E.g., ChestX-ray14, HAM10000.

### Soundness
3

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
This paper proposes an anomaly detection method, where encoders are trained such that the images with different context have separated representations while keeping the relationship among images within each context. With experiments using medical and natural images, the effectiveness of the proposed method is evaluated.

### Strengths
This paper proposes a new anomaly detection method with context augmentations.

The experiments with medical images.

### Weaknesses
The novelty of the proposed method is limited.

The advantage of the proposed method is unclear compared with the existing anomaly detection methods with data augmentation by flipping, inverting, and equalizing.

### Questions
Preparing contexts might require prior knowledge for anomaly. Can any context that fullfills distinctiveness and alignment be useful in the proposed method?

How can we tune alpha? 

How to chose LH or NND?

What are the advantages of the proposed method compared with the existing anomaly detection methods with data augmentation?

The proposed method depends on the context transformation to be used (Equalize, Invert, Flip). How can we choose appropriate transformation for given applications? 

What does happen when all transformations are included in the proposed method?

What happens when alpha is fixed at zero or one?

Why the context-specific cluster structure is important for anomaly detection? In the experiments, alpha is linearly annealed from zero to one.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an anomaly detection method that uses context contrastive learning to learn useful representations of normal data.
Specifically, this paper proposes context augmentations that are transformations satisfying two properties (distinctiveness and alignment).
Using them, the invariance of normal patterns can be encoded well into the representations. The experiments with image datasets show the effectiveness of the proposed approach.

### Strengths
- The paper is generally well-written and is easy to follow.
- The proposed method is simple and thus may be easy for practitioners to use.
- The experiments with medical image data show that the proposed approach outperforms the existing contrastive anomaly detection methods.

### Weaknesses
 - Since there are existing contrastive anomaly detection methods as described in the experiments, I think the proposed approach's novelty is not outstanding. Also, the differences between context and other ordinary transformations are not clearly explained. For example, can we use context transformations in the same way as ordinary transformations? (The same applies in reverse). I want to know the key differences between context augmentations and ordinary transformations.
- There are many anomaly detection approaches other than the contrasting-based approach described in Section 2. Thus, this paper would be improved by showing the effectiveness of the proposed method through experimental comparisons with these methods. Specifically, density ratio estimation-based, autoencoder-based, and SVDD-based methods are also widely used in anomaly detection, and a comparison with these methods would strengthen the paper's contribution.
- In Figure 4, the significant difference between the proposed and existing methods is unclear.

### Questions
- The problem settings only have unlabelled or normal data. How are the hyperparameters of the proposed method practically determined?
- Can the proposed method be applied to domains other than the image domain?

### Soundness
2

### Presentation
3

### Contribution
2
