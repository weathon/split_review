# Enhancing Pre-trained Representation Classifiability can Boost its Interpretability

- Decision: Accept
- Scores: 8, 8, 8, 6, 8, 6

## Abstract
The visual representation of a pre-trained model prioritizes the classifiability on downstream tasks. However, widespread applications for pre-trained visual models have proposed new requirements for representation interpretability. It remains unclear whether the pre-trained representations can achieve high interpretability and classifiability simultaneously. To answer this question, we quantify the representation interpretability by leveraging its correlation with the ratio of interpretable semantics within representations. Given the pre-trained representations, only the interpretable semantics can be captured by interpretations, whereas the uninterpretable part leads to information loss. Based on this fact, we propose the Inherent Interpretability Score (IIS) that evaluates the information loss, measures the ratio of interpretable semantics, and quantifies the representation interpretability. In the evaluation of the representation interpretability with different classifiability, we surprisingly discover that the interpretability and classifiability are positively correlated, i.e., representations with higher classifiability provide more interpretable semantics that can be captured in the interpretations. This observation further supports two benefits to the pre-trained representations. First, the classifiability of representations can be further improved by fine-tuning with interpretability maximization. Second, with the classifiability improvement for the representations, we obtain predictions based on their interpretations with less accuracy degradation. The discovered positive correlation and corresponding applications show that practitioners can unify the improvements in interpretability and classifiability for pre-trained vision models. Codes are included in the supplement and will be released on GitHub.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes the Inherent Interpretability Score (IIS) as a novel quantitative metric for evaluating the interpretability of the pre-trained representation. The authors demonstrate the positive correlation between the interpretability and classifiability of the classifiability-oriented pre-trained representations through extensive experiments.

### Strengths
1. The authors proposed a novel evaluation metric to quantitatively evaluate the pre-trained representation's interpretability. The proposed IIS can not only be used in the research area related to post-hoc explainable approaches but also improve model classification performance and interoperability. 
2. The paper is written and well-organized. It is easy to follow the authors' ideas and understand their approaches. The authors clearly show their motivation and ideas in Figure 1 and Figure 2. The notations and experimental results are clear and easy to read.
3. The authors have conducted extensive experiments across various datasets with different pre-trained models to show the effectiveness of IIS. The experimental results support the authors' claims from several different aspects, for example, the positive correlation, factor analysis,  and applications of IIS.

### Weaknesses
1. Besides extensive experimental results, the authors should have provided clear theoretical analyses of the proposed method.
2. The proposed method IIS relies on pre-defined or generated concepts, which are usually hard to get and not applicable in real-world scenarios.

### Questions
1. How do you deal with the linear weights in the additional linear classifier, as shown in Eq. (5)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper addresses the critical question of whether high interpretability and classifiability can be achieved simultaneously in pre-trained vision models. To this end, the authors propose the Inherent Interpretability Score (IIS), a novel metric designed to quantitatively evaluate the interpretability of pre-trained representations. Through extensive experimentation, the authors find a positive correlation between interpretability and classifiability. Moreover, they observe that maximizing interpretability can further enhance model performance, which, in turn, improves the performance of interpretability-based models.

### Strengths
* This paper utilizes concept ablation method for evaluation the interpretability of the representations, which has also been adopted for evaluating the post-hoc interpretation methods [1].
* The authors utilize both visual and textual concepts for IIS.
* The paper is well-written and easy to follow.
* The authors provide code for reproducibility check.

### Weaknesses
1. **Completeness of Evaluation:** Huang et al. [2] have discussed the trustworthiness in concept bottleneck models (CBMs), noting that several concepts can be activated in irrelevant regions with regards to the input image, leading to a loss of model interpretability. However, the authors have overlooked this issue. Specifically, the paper does not address the spatial alignment between activated concepts and the corresponding image regions. This is crucial because a concept might be 'activated' by the model, but if this activation occurs in a spatially unrelated part of the image, the interpretability is questionable. For example, if the concept 'bird' is activated when the model is looking at the sky in an image, it would not be considered a trustworthy interpretation.
2. **Method:** In the IIS evaluation, in what order are concepts removed? How would the evaluation results differ if removing began with the most important concepts for the category versus the least important? The paper lacks a clear explanation of the concept removal process. It is unclear whether the concepts are removed based on their importance to the classification task or some other criteria. This ambiguity makes it difficult to assess the validity of the proposed IIS metric. Furthermore, the impact of different removal strategies on the final IIS score is not explored, which could reveal potential biases in the metric.
3. **Experiments:** If the visual model’s features have already been aligned with language, as in CLIP [3], would the interpretability be significantly higher compared to a standard ViT? The paper does not investigate the impact of pre-training strategies on the interpretability of the learned representations. Models like CLIP, which are trained with both visual and textual data, might exhibit different interpretability characteristics compared to models trained solely on visual data. This comparison is important to understand the role of pre-training in shaping the interpretability of vision models.

### Questions
My questions are listed in the Weakness section.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes the IIS metric to measure the interpretability of representations from image encoders and demonstrates a positive correlation between the interpretability and classifiability of the classifiability-based pre-trained representations.

### Strengths
1. This paper quantifies the interpretability of representations and discovers an interesting and significant positive correlation between the interpretability and classifiability of representations. The results have been demonstrated on multiple datasets and architectures.
2. The observation is used in designing IIS maximization loss, which results in improved classifiability. 
3. The paper is well-written, making it easy to follow the main ideas and claims.

### Weaknesses
1. The proposed IIS score is similar to the “average accuracy obtained at different number of effective concepts” proposed in [1]. Particularly, [1] trains the final linear classifier with elastic-net regularization in GLM-SAGA and tunes regularization strength for controlling sparsity (number of effective concepts). The average accuracy is obtained by averaging accuracy at different sparsity levels. The similarities between the metric proposed in [1] and IIS should be discussed.
2. Limited dataset results: To demonstrate the applicability of this method in wide scenarios, the results should be provided on additional datasets, including Actions: UCF-101, Textures: DTD, and Skin tumors: HAM10000 following [2].
3. Table 5 lacks comprehensive comparisons to methods [3, 4]. Particularly, [3] can work for any backbone network architecture, including ViT and Swin.

### Questions
Please see weaknesses

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Inherent Interpretability Score (IIS) to quantify interpretability within pre-trained visual models, establishing a positive correlation between classifiability and interpretability. The study shows that interpretability-oriented fine-tuning can further improve both interpretability and classifiability in vision models. Extensive evaluations across various models and datasets support these claims, positioning IIS as a metric for balancing classifiability and interpretability without sacrificing accuracy.

### Strengths
1. This paper proposes an innovative metric IIS, which provides a practical way to assess interpretability through classifiability and shows that pre-trained representations can achieve high interpretability and classifiability simultaneously.

2. Comprehensive experiments conducted have confirmed the positive correlations between interpretability and classifiability. In the meantime, authors have done thoroughly comparison experiments, showing the broad application direction in classification task.

### Weaknesses
1. The scope of this paper is limited to classifiability-oriented representations, where the fact that the representation can be applied to segmentation task is ignored.

2. There is limited discussion about the selection of textual concepts. The prompts used to generate concepts for each class appear to be basic, without addressing whether overlapping concepts might influence the results.

3. Compared to ECBM, proposed method achieves minimal improvement from 81.20% to 81.29%. Further comments will be listed below in Question section.

### Questions
1. While the paper uses segmentation as visual concepts, could the authors provide insights on whether IIS correlates with improvements in segmentation tasks?
2. In Table 4, compared with ECBM, your method improves the accuracy from 81.20% to 81.29% appears minimal. Could the authors provide a comparison between ECBM and your method when both use approximately 250 concepts?
3. Instead of concatenating both concepts together, could authors provide a comparison between using textual concepts only and visual concepts only? 
4. While DEAL [1] also claimed that improving interpretability can have positive impact on classification performance too, could author provide a comparison results between DEAL and your method with regard to the classification accuracy improvement.

[1] DEAL: Disentangle and Localize Concept-level Explanations for VLMs http://arxiv.org/abs/2407.14412

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose to quantify the interpretability of representations using the correlation with the ration of interpretable semantics. They propose the Inherent Interpretability Score to measure the interpretability and information loss of representations by checking how much a representation can retain the original accuracy after a projection into a sparse interpretable space and a sparsification process. Through this evaluation, they also analyze the correlation between classifiability and interpretability.

### Strengths
→ Proposition of an interpretability metric: I believe this is an important contribution to evaluate the interpretability of a model's representation. We know that given the subjectivity of interpretability, it is difficult to quantify this property. The authors present a consistent way to measure it using libraries of concepts and the projection of representations into concept space.

→ Testing of different concepts and validation through a variety of experiments: I appreciate the number of validation experiments, including 4 different concept libraries (visual and textual) and experiments to evaluate: accuracy vs. interpretability for different architectures, evolution through training epochs, sparsity ratio and representation dimension.

→ Two applications: The authors also provide two cases where their study can be applied, improving classifiability by maximizing interpretability and providing interpretable predictions with high accuracy.

### Weaknesses
→ I understand the positive correlation between interpretability and classifiability, but is it not too strong to assume that higher classifiability implies more interpretability in this part?:  “We discover the mutual promoting relation between the interpretability and classifiability
of the classifiability-oriented representations, indicating that improving the interpretability can further improve the classifiability, and representations with higher classifiability are more interpretable to preserve more task-relevant semantics in interpretations.”

As I understand it: There is a loss of information caused by the sparcity, which reduces the original accuracy.
    
→  I am not sure about the process of increasing sparsity. Could some of the zeroed concepts be some kind of sub-concept that gets diluted in the high dimensionality of the concept library? Or even the errors from obtaining the concept library? It would be interesting to see other ways to reduce the sparsity of these concepts.

→  In Figure 5, you can see that the model is interpretable at the beginning of training and then it loses interpretability. Why is the model interpretable when it knows nothing? The network was initialized with some pre-trained weights? Because if the weights are random, it makes no sense to be interpretable at the beginning. Do you know why this happens?

→  I think it would be important to include the standard deviation in Tables 1— 5.

→  I have not seen much difference in increasing sparsity to justify this sentence: “This indicates that the model is highly sensitive to the representation sparsity and should not employ excessively large sparsity constraints during fine-tuning.”

And another question about sparsity: if you are not able to provide a sparser representation, you are limiting the interpretability, right? Because 200 concepts with 0.1 sparsity is a lot to interpret I imagine.

→  I think Figure 1 would be more interesting if it were made with real data and real experiments (even with simplified results).

### Questions
I included some questions in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed a novel representation interpretability metric called IIS. A series of experiments are conducted which shows positive correlation between IIS and classifierbility of the representation. This observation is applied in improving classifierbility of representation and reduce accuracy loss for interpretation.

### Strengths
1. The proposed IIS metric provides an interesting way to measure representation interpretability. 
2. The observation on relation between interpretability and classifiability is novel and backed by extensive experiments.

### Weaknesses
1. Though the idea of IIS intuitively makes sense, more theoretical discussion on this metric is needed. For example, suppose there is a random representation where the prediction accuracy no better than random guess. In this case, the representation will have low classifiability while high IIS (ARR = 1 as the accuracy will not further decrease after sparsification).

2. How is Eq. (2) derived? It looks like the cos-cubed loss in [1]. More discussion on the details is needed. 

3. In sparsification in Eq.(4), besides zeroing out elements, the remaining elements are also adjusted by their distance to threshold. Is there any justification to this sparsification? How will the IIS change for different sparsification method (e.g. only masking out small absolute value elements without changing others).

4. In Table 4, how is the accuracy for your method calculated? What is the sparity ratio $s$ used here?

### Questions
1. How is Eq. (2) derived? It looks like the cos-cubed loss in [1]. More discussion on the details is needed. 
2. In sparsification in Eq.(4), besides zeroing out elements, the remaining elements are also adjusted by their distance to threshold. Is there any justification to this sparsification? How will the IIS change for different sparsification method (e.g. only masking out small absolute value elements without changing others).
3. In Table 4, how is the accuracy for your method calculated? What is the sparity ratio $s$ used here?

[1] Oikarinen, Tuomas, et al. "Label-free concept bottleneck models." arXiv preprint arXiv:2304.06129 (2023).

### Soundness
2

### Presentation
3

### Contribution
3
