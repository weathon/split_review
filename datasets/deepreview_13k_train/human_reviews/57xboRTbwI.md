# Bias Analysis in Unconditional Image Generative Models

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
The widespread usage of generative AI models raises concerns regarding fairness and potential discriminatory outcomes. In this work, we define the bias of an attribute (e.g., gender or race) as the difference between the probability of its presence in the observed distribution and its expected proportion in an ideal reference distribution. Despite efforts to study social biases in these models, the origin of biases in generation remains unclear. Many components in generative AI models may contribute to biases. This study focuses on the inductive bias of unconditional generative models, one of the core components, in image generation tasks. We propose a standardized bias evaluation framework to study bias shift between training and generated data distributions. We train unconditional image generative models on the training set and generate images unconditionally. To obtain attribute labels for generated images, we train a classifier using ground truth labels. We compare the bias of given attributes between generation and data distribution using classifier-predicted labels. This absolute difference is named bias shift. Our experiments reveal that biases are indeed shifted in image generative models. Different attributes exhibit varying bias shifts' sensitivity towards distribution shifts. We propose a taxonomy categorizing attributes as $\textit{subjective}$ (high sensitivity) or $\textit{non-subjective}$ (low sensitivity), based on whether the classifier's decision boundary falls within a high-density region. We demonstrate an inconsistency between conventional image generation metrics and observed bias shifts. Finally, we compare diffusion models of different sizes with Generative Adversarial Networks (GANs), highlighting the superiority of diffusion models in terms of reduced bias shifts.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates how inductive bias in unconditional generative models affects bias in generated results. The authors define bias shift as the difference between the probability of attribute presence in the training and generated distributions, and train a classifier to categorize attributes to quantify bias shift. Furthermore, attributes are categorized as subjective or non-subjective based on the position of the classifier's decision boundary. The author validates multiple models including diffusion models and GAN on two datasets, CelebA and DeepFusion, revealing related patterns.

### Strengths
1. Problem Definition: The paper focuses specifically on studying the inductive bias of generative models themselves, avoiding other factors such as dataset bias and prompts, providing a novel perspective for analyzing bias sources.

2. Methodology: Proposes a standardized bias evaluation framework that uses the same classifier for all label predictions, ensuring consistency in evaluation.

3. Writing: The paper is well-structured and explains complex concepts in an understandable way.

### Weaknesses
1. Some of the discussion in the method section (sec. 3) seems to be redundant or not tied to the paper. For example, what is the purpose of introducing $P^{ideal}$? Although it is canceled in the final equation, I don't think it is necessary to introduce such a term because, intuitively, $|{P^{gen} - P^{val}}|$ itself is sufficient to measure the bias shift. Introducing extra and probably unnecessary assumptions may overcomplicate the method and lead to confusion. Also, Section 3.1 also introduces a definition of "conditional bias," which is not discussed or studied in the rest of the paper. What is the purpose of introducing this definition?

2. The paper claims (L142) that "pre-trained models introduce their own biases, rendering the predicted labels unreliable for accurate bias evaluation." However, I disagree with this argument. I agree that the pre-trained model may be biased, but this reason does not invalidate them for performing attribute classification. Such a classifier serves as the expert in labeling attributes so that the most important criterion, if not the only criterion, should be classification accuracy. If any pre-trained models have outstanding attribute classification performance on the training/val dataset, I don't see why they shouldn't be used. Further, those pre-trained models can be finetuned on the training dataset (which this paper did) for an even better classification performance on specific datasets (e.g., CelebA), which can only benefit the bias shift analysis.

3. Further, the accuracy of the classifier is not sufficient for the analysis. Although the accuracies of the majority of attributes are 90%+, there is still a considerable amount of attributes on which the classifier performs unsatisfying. This fact is critical to the analysis, considering the listed subjective attribute examples are placed in the lower portion of the performance list. Lower accuracy may suggest higher analysis noise and larger ABS measuring error. Since the ABS for non-subjective attributes and subjective attributes are ~1% and 3-5%, the classifier with 91.7% (lowest attribute: 68.34%) or 90.5% (lowest attribute: 71.65%) accuracy is not good enough.

4. Further, the classifier is trained on the training set and directly applied to both training, valid, and generation sets. However, unlike training and valid sets are sampled from the same distribution, the generation set may have a different distribution than the original dataset. Thus, the classifier may suffer from distribution shift and/or visual domain generalization challenges, so the classifier may not be reliable on the generation set. This issue can further weaken the paper's analysis and conclusion.

5. Although the attempt to split the attribute into subjective and non-subjective groups is interesting, I am not convinced that the splitting method used in the paper (decision boundary-based) is valid. The decision boundary is closely connected with classifier accuracy, which can be further connected with analysis noise and measuring errors. Thus, those attributes with unclear boundaries are more likely to have higher ABS errors. Additionally, this splitting may not match human's definition of "subjective." Those "subjective attributes" to human definition (e.g., wearing glasses) may be easier to be classified so that they may have clearer boundaries. However, there is no guarantee of this, and the paper also does not have a complete list of subjective and non-subjective attributes to verify.

### Questions
Do the accuracy rates reported in Figures 4 and 5 of the appendix refer to training set or validation set performance?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a framework for bias evaluation of unconditional image generative models. The authors measured the bias shift in the original and synthetic data and tested their framework in publicly available datasets. They found that, bias shift happens in image generative models and proposed two taxonomies to categorize the bias shift for different attributes. The paper is well-written and well-formulated. However, a comparison with the existing bias evaluation framework needs to be made.

### Strengths
1. This work presents a bias evaluation framework for unconditional image generative models.
2. The authors proposed two taxonomies for categorizing bias shifts for different attributes.
3. The authors experimented with different sizes of diffusion models to observe how bias shift is happening.

### Weaknesses
1. As this paper presents a bias evaluation framework for image dataset, it needs to be compared with other evaluation framework, i.e. compare with [1]. How is the presented framework differ with the [1]?

2. Limitations of this evaluation framework should be discussed in the paper.

#### References:

[1] Wang, Angelina, et al. "REVISE: A tool for measuring and mitigating bias in visual datasets." _International Journal of Computer Vision_ 130.7 (2022): 1790-1810.

### Questions
See weakness point 1

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
This paper proposes an evaluation pipeline to analyze the bias shift of different generative models. The generative models are trained on the training dataset, and an attribute classifier is also pretrained on the same dataset. The attribute prediction difference between the original dataset and the generated images measures the bias shift. The paper also separates the attribute into two categories, subjective and non-subjective, to further analyze the insight of the bias shift.

### Strengths
In general, the analysis of the bias shift of different generative models is interesting, and the pipeline's high-level idea seems to be sound. The subjective/non-subjective study is also interesting. The paper includes a vast amount of empirical results for the analysis.

### Weaknesses
1. Some of the discussion in the method section (sec. 3) seems to be redundant or not tied to the paper. For example, what is the purpose of introducing $P^{ideal}$? Although it is canceled in the final equation, I don't think it is necessary to introduce such a term because, intuitively, $|{P^{gen} - P^{val}}|$ itself is sufficient to measure the bias shift. Introducing extra and probably unnecessary assumptions may overcomplicate the method and lead to confusion. Also, Section 3.1 also introduces a definition of "conditional bias," which is not discussed or studied in the rest of the paper. What is the purpose of introducing this definition? 

2. The paper claims (L142) that "pre-trained models introduce their own biases, rendering the predicted labels unreliable for accurate bias evaluation." However, I disagree with this argument. I agree that the pre-trained model may be biased, but this reason does not invalidate them for performing attribute classification. Such a classifier serves as the expert in labeling attributes so that the most important criterion, if not the only criterion, should be classification accuracy. If any pre-trained models have outstanding attribute classification performance on the training/val dataset, I don't see why they shouldn't be used. Further, those pre-trained models can be finetuned on the training dataset (which this paper did) for an even better classification performance on specific datasets (e.g., CelebA), which can only benefit the bias shift analysis. 

3. Further, the accuracy of the classifier is not sufficient for the analysis. Although the accuracies of the majority of attributes are 90%+, there is still a considerable amount of attributes on which the classifier performs unsatisfying. This fact is critical to the analysis, considering the listed subjective attribute examples are placed in the lower portion of the performance list. Lower accuracy may suggest higher analysis noise and larger ABS measuring error. Since the ABS for non-subjective attributes and subjective attributes are ~1% and 3-5%, the classifier with 91.7% (lowest attribute: 68.34%) or 90.5% (lowest attribute: 71.65%) accuracy is not good enough. 

4. Further, the classifier is trained on the training set and directly applied to both training, valid, and generation sets. However, unlike training and valid sets are sampled from the same distribution, the generation set may have a different distribution than the original dataset. Thus, the classifier may suffer from distribution shift and/or visual domain generalization challenges, so the classifier may not be reliable on the generation set. This issue can further weaken the paper's analysis and conclusion. 

5. Although the attempt to split the attribute into subjective and non-subjective groups is interesting, I am not convinced that the splitting method used in the paper (decision boundary-based) is valid. The decision boundary is closely connected with classifier accuracy, which can be further connected with analysis noise and measuring errors. Thus, those attributes with unclear boundaries are more likely to have higher ABS errors. Additionally, this splitting may not match human's definition of "subjective." Those "subjective attributes" to human definition (e.g., wearing glasses) may be easier to be classified so that they may have clearer boundaries. However, there is no guarantee of this, and the paper also does not have a complete list of subjective and non-subjective attributes to verify.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces an analysis of non-conditional generative models, GANs and Diffusions, for image generation. By using a classifier trained on the same dataset, biases are identified as subjective and non-subjective attributes.

### Strengths
The paper analyzes an important topic of bias in generative models. These models have been shown to learn the biases from their datasets, and this paper proposes a new angle towards understanding these biases.

The paper is generally well written and easy to follow.

The detailed analysis of logits seems to not have been studied before.

### Weaknesses
As a preliminary, I have reviewed this paper before for the NeurIPS SafeGEN workshop. I have reread this version of the paper, and my opinion has not changed. 

Here's my concerns:
 - Calling attributes subject vs non-subjective is very strange. For example, "Pale skin" or "male" in CelebA being a non-subjective attribute is surprising. I would be convinced if there were a user study to validate these attributes are similarly subjective to humans, but as it stands I'm not convinced.
 - The raw bias shift is strikingly small. The subjective logits on figure 5c look extremely similar between the synthetic versus real data. Especially when comparing 5c to 5e, it's surprising that Male landed in non-subjective and Smiling did not.
 - Using the same dataset for training the generator and classifier is very problematic: it's self-contamination. The bias studied in this paper could come from: the dataset itself, the generator's training/architecture, or the classifier's training/architecture. Given the generator and classifier are mapped to the same data distribution, the inherit biases are muddled between the two. I would have liked to seen dataset splits where half the data is used to train the generator and half the classifier. That would improve the self contamination issue substantially.
 - Finally, the actual take-aways from the paper are fairly limited. Assuming my previous point were address, the fundamental why question is not answered: why are some attributes represented more/less in the synthetic distribution. It is somewhat useful to know that some attributes are, but I would be very interested to know how to predict which attributes would be over/under represented by just training a classfier.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
1
