# Unveiling AI's Blind Spots: An Oracle for In-Domain, Out-of-Domain, and Adversarial Errors

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 5, 8

## Abstract
AI models make mistakes when recognizing images—whether in-domain, out-of-domain, or adversarial. Predicting these errors is critical for improving system reliability, reducing costly mistakes, and enabling proactive corrections in real-world applications such as healthcare, finance, and autonomous systems. However, understanding what mistakes AI models make, why they occur, and how to predict them remains an open challenge. Here, we conduct comprehensive empirical evaluations using a "mentor" model —a deep neural network designed to predict another model’s errors. Our findings show that the mentor model excels at learning from a mentee's mistakes on adversarial images with small perturbations and generalizes effectively to predict in-domain and out-of-domain errors of the mentee. Additionally, transformer-based mentor models excel at predicting errors across various mentee architectures. Subsequently, we draw insights from these observations and develop an "oracle" mentor model, dubbed SuperMentor, that achieves 78\% accuracy in predicting errors across different error types. Our error prediction framework paves the way for future research on anticipating and correcting AI model behaviours, ultimately increasing trust in AI systems. All code, models, and data will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work uses a dedicated neural network to detect 3 classes of error sources
in image classification, including adversarial examples, image distortion, and
in-distribution prediction error. The detection model is analyzed in various
ablation studies, including the effect of the strength of the different error
sources in accuracy, the accuracy under different architectures for both
detector and predictor (ResNet and ViT), and the distillation loss. A t-SNE
embedding is shown for the features of the detector.

### Strengths
- The work is well written and clearly presents its contributions.

- The work introduces a novel comparison for detection difficulty between
  different error sources in image classification.

- Various ablation studies are conducted for the proposed model.

### Weaknesses
 - Novelty: Adversarial Examples are an extremely well researched topic. (see, e.g., Yuan et al., 2019) for a survey). Hence, the idea of detecting adversarial examples by using a classifier has been done before (see, e.g., Metzen et al., 2017). This limits the novel contribution of this work to the comparison of the detection of the different error types.

- Contribution: Although the work references other approaches for the detection of
  adversarial attacks and other presented error sources, there is no baseline
  comparison at all. For a significant contribution, it is necessary to compare
  it to previous work which attempts to solve the same issue. The work reports
  some accuracy of up to 83%, yet it is difficult to quantify this without
  analyzing the detection accuracy achieved through other approaches.

- Clarity: The work presents multiple ablation studies to compare how different
  architectures perform under the discussed error sources. While interesting,
  it is not quite clear to me why this is relevant unless compared to other
  baselines. I also did not understand how the t-SNE embeddings support the
  claim that the proposed neural network-based detector is a good idea.

In total, this work requires a more thorough literature search concerning
different approaches to errors in image classification. It is very difficult to
justify a method when it is not compared to previous work.

### Questions
- Did you compare your approach to other baselines to detect model error?

- How does your approach differ from (Metzen et al., 2017), except for the different error types?

- What purpose do the t-SNE embeddings serve?

### Soundness
3

### Presentation
3

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
Focusing on the vulnerability of DNN models regarding the wrongly predicted samples, this work proposes a framework to predict the errors of trained DNNs over (1) in-domain, (2) out-of-domain, and (3) adversarial samples. The framework trains a “mentor” model to minimize the combination of two losses to (i) mimic the mentee’s prediction and (ii) predict the mentee’s correctness.

### Strengths
1. This work focuses on an interesting topic of predicting the errors of trained models over in-domain, out-of-domain, and adversarial errors. This is an important task given the vulnerability and nonlinearity of DNNs.
2. The paper is well-written and very easy to follow.
3. Extensive experiments are carried out.

### Weaknesses
 1. Main concern: The idea of training another DNN model to predict the vulnerability of another DNN model can be risky. The problems that exist in the training process of the mentee may also exist in the training process of the mentor. For example, what if the backbone of the mentor model is already suffering from these problems? Furthermore, the mentor network is also a black box, making it difficult to understand why it makes certain predictions about the mentee's errors. This lack of interpretability further compounds the risk of relying on a potentially flawed mentor.
2. The motivations of the two loss terms are contradicting. $L_d$ encourages the mentor to mimic the mentee’s predictions, including wrong ones. However, $L_r$ encourages the mentor to distinguish the wrong predictions from the correct predictions. This creates a tension in the training process, where the mentor is simultaneously trying to replicate and correct the mentee's behavior. The balance between these two objectives is not clearly defined, and it is unclear how this trade-off affects the overall performance of the mentor.
3. The out-of-distribution genre studied in this work is very limited. In this work, only synthetic corruptions such as noise, blur, etc. are included, while important natural distribution shifts such as spurious correlations, styles shift, etc. are completely overlooked. This significantly undermines the real-world contribution of the experimental results. The lack of evaluation on natural distribution shifts limits the applicability of the proposed framework to real-world scenarios where such shifts are common.
4. It is observed in the experiments that adversarially trained mentor performs better. However, this could be the benefit of adversarial training as it leads to a smoother and more robust model. If the mentee model is already trained in the adversarial way, the testing accuracy under OOD, and AA could already be improved (e.g. [1]). The paper does not explore the impact of adversarial training on the mentee model, which could potentially mitigate the need for a mentor model.
5. Due to the aforementioned issues, the contributions of this work remain unclear. It is not straightforward how real-world applications can benefit from this framework. The authors may consider elaborating more on the “high-stakes real-world applications” claimed in L539.

[Minor]

1. Figure 1 can be misleading. Since the authors focus only on the synthetic out-of-distribution samples, the “out-of-distribution images” (middle) look like an adversarial image. Furthermore, the “adversarial images” (bottom) show an attacked sample whose raw image differs from the other two images. This can be easily misunderstood as the out-of-distribution sample with a natural distribution shift. It is strongly suggested that the same raw input be used.
2. The specific formulation of the distillation loss $Distill$ should be given.

### Questions
1. Built also by DNNs, the mentor shall suffer the same problems such as the black-box nature, the high nonlinearity, etc. Does this require another mentor’s mentor to predict whether the mentor can correctly predict the mentee’s prediction? How does the author justify this cyclic scenario?
2. If the mentor can be able to predict the correctness of the mentor with higher accuracy than reconstructing the mentee’s prediction accurately, does this mean that the backbone of the mentor is capable of correctly predicting the true classes of those true negative samples (wrongly predicted by the mentee but recognized by the mentor)? The representations learned from the backbone of the mentor should be an interesting direction to explore.
3. The logistic regression loss $L_r$ is for the binary classification of whether the mentee makes the correct classification. This can be a very imbalanced task. How is this affecting the results?
4. In Figure 2, what is the “average accuracy”? Is it the average of the testing accuracy of the mentor with three ID, OOD, and AA?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes using mentor model to predict the error of AI models (mentee models). It mainly considers image classification task with two architectures, ResNet50 and ViT. The basic idea of the paper is similar to membership inference attack(MIA), which treats the mentor as a binary classifier. The paper conducts decent empirical studies on different setup of data distribution, including in-domain, out-of-domain, and adversarial examples. The paper makes several interesting conclusions, including: 1. adversarial examples with small perturbations are most beneficial to mentor model training. 2. Mentor models can generalize across different mentee models.

### Strengths
1. The formulation of the problem is interesting. The paper proposes using an AI model to predict the error of another, which can open new possibility for understanding DNNs.
2. The experiments are decent and comprehensive. The paper conducts experiments on multiple setup of model architecture and data distribution. It also includes experiments like generalizability of the model. In particular, the incorporation of AA data provides interesting insights.
3. The paper is generally well written and easy to follow.

### Weaknesses
1. The paper lacks a comprehensive assessment of relationship to previous works. Monitoring errors of AI model seem crucial, but how previous approach attempts to address the problem is not clear (although it is presented in related work). The paper also does not compare its performance to previous methods, nor does it explicitly claim that the it is formalizing a new problem, which makes understanding the position and results of the paper in the area relatively difficult.

2. This is like my main concern -- I am very willing to discuss this further with the authors. It is not clear to me what the possible applications of the method is/what possible insights we could draw from the mentor.  For example, is it possible to give insights on interpretation of the mentee model based on the mentor model?

3. (minor) The accuracy of the mentor model seems not high "enough" -- although it outperforms random guessing by a large amount, it seems not high enough to safely draw more insights independently from it. Again it is related to first point as the position of the paper is unclear.

### Questions
1. See Weaknesses, especially weakness 2.

2. In the results section, why is it sometimes possible that mentor model trained on ID data can outperform that trained on OOD data?

3. Is it possible that a mixture of ID, OOD and AA data can achieve better performance? AA data is like outliers for the mentee model, which, in turn, may lack some information of the in-domain distribution that the mentee model holds.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explores the utilization of a “mentor” model to predict the errors of a “mentee” model in a supervised image classification task. The strategy implies training the mentor on the frozen mentee by inputing the image, the mentee’s logits, and the correctness of the mentee in order to extract insight about the mentee’s decision patterns. The mentee’s logits are introduced in a distillation loss to incorporate its behaviour, while the prediction “correctness” (mentee's correctness vs. metor's prediction of mentee correctness) is supervised by a logistic regression loss.
In the experiments two types of architectures are used, ResNet50 and ViT. The latter corresponds to the powerful backbone since it is a transformer architecture based on self-attention mechanisms. Authors differentiate between 3 types of errors: In Domain errors, Out-of-domain errors and Adversarial Attack errors. Experiments are carried on these 3 types of errors to explore which reveals the mentee’s learning patterns better. According to the authors, it is important to remember that the mentor is expected to detect errors, not the source of them.
The experiments are carried over 3 datasets: CIFAR10, CIFAR100 and ImageNet-1K. For ID errors they use 3 different subsets of the original ones; for OOD they use 4 different corruptions for each dataset; and for the AA errors they use 4 different white-box attacks for each dataset.
The results show interesting findings: 

1. **AA errors** offer deeper insights into the mentee’s decision-making process compared to OOD and ID errors.
2. Mentors benefit from having more **complex architectures** than the mentees, particularly transformer-based models.
3. The mentor's performance **degrades with increasing perturbation** in AA examples.
4. Most notably, **mentors generalize across different mentee architectures**, allowing them to predict errors even when mentees change.

As a final contribution, authors propose an “oracle” mentor based on the findings from the experiments. This SuperMentor is trained on AA with small perturbation and its architecture correponds to ViT. An ablation study is performed on this mentor to determine the contribution of the distillation loss and the mentee’s logits on its performance. This SuperMentor is able to correctly separate most of the correct/incorrect points of different mentees over different datasets and sources of errors.

### Strengths
- The problem assessed in the paper is an important one. Even though there exist other approaches for selective classification like, for example, Learning to Defer and Rejection Learning, the presented framework allows working with pretrained models and uses convex losses, thus avoiding the use of surrogate losses.
- The experiments are numerous and well chosen. The use of different error sources helps to understand the mentor’s understanding of the mentee. The use of different architectures is also an important one and the conclusion over them is insightful.
- Experimental results are exhaustive, well explained and supported in the text.

### Weaknesses
 - I miss a bit of mathematical formulation in Section 3. I would like to see the complete loss function somewhere (even though it can be easily understood in the text).

- Since the framework is intended to detect potential errors regardless of their domain, I miss some references on Selective Classification, Rejection Learning [1] and Learning to Defer [2]. 

- The paper would benefit from comparing and discussing supervised and unsupervised strategies to solve the issues dealt by their mentor system. See the next point.

- The authors try to distinguish and characterize three types of errors, but there is conflict in OOD errors and AA. For instance AA are not necessarily mutually exclusive with OOD, moreover trying to describe OOD errors with a set of perturbations on original images is not exhaustive or representative of OOD behaviour. In the literature on OOD detection there is justified skepticism towards using supervised examples of OOD, issue that is completely ignored across the paper and not mentioned as a possible limitation.

- When accuracy is measured as the average of the mentor's accuracy on the samples that the mentee classified correctly and those that the mentee classified incorrectly, it can be misleading. For example, a mentor that correctly classifies all correctly classified samples but none of the misclassified ones will achieve a 50% accuracy, which is not a reliable metric. This metric does not faithfully represent a reliable mentor, and a mentor that detects all errors but misclassifies all correct predictions would also achieve 50% accuracy, which is a safer but still unreliable alternative.

### Questions
- Can you elaborate on how does your model respond in multi-class setting in which two classes could be equally likely but the model makes a mistake in choosing the correct label?
- Did authors consider what to do next once the mentor predicts an error? How could the information be used?
- Are there any external baselines to compare against? If so, why aren’t they included?
- How would you tackle the calibration of the mentor’s predictions?
- Considering that the mentor is trained on examples of OOD or AA, there is a chance that the mentor learns to detect these kinds of data but nothing actually related to the mentee. This is similar to the faithfulness issue in explainability, where we might learn plausible explanations that have nothing to do with the method to explain. Could you comment on this point?

### Soundness
3

### Presentation
4

### Contribution
4
