# OmniInput: A Model-centric Evaluation Framework through Output Distribution

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
We propose a novel model-centric evaluation framework, OmniInput, to evaluate the quality of an AI/ML model's predictions on all possible inputs (including human-unrecognizable ones), which is crucial for AI safety and reliability. Unlike traditional data-centric evaluation based on pre-defined test sets, the test set in OmniInput is self-constructed by the model itself and the model quality is evaluated by investigating its output distribution. We employ an efficient sampler to obtain representative inputs and the output distribution of the trained model, which, after selective annotation, can be used to estimate the model's precision and recall at different output values and a comprehensive precision-recall curve. Our experiments demonstrate that OmniInput enables a more fine-grained comparison between models, especially when their performance is almost the same on pre-defined test sets, leading to new findings and insights for how to train more robust, generalizable models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes OMNIINPUT which utilizes the Gradient Wang–Landau sampler to sample representative data and annotate them for model evaluation. Authors validate the framework on MNIST variants. The metrics of mode evaluation involve precision and recall on the representative subpopulation.

### Strengths
1. The paper is well-presented with a fair storyline that motivates the work.
2. The topic of model evaluation with a neural sampler is important.
3. The experiment design covers a wide aspect of considerations.

### Weaknesses
1. Authors should show sufficient validation of the framework. The paper demonstrates validations from original MNIST as in-distribution samples and MNIST variants as out-distribution ones. Limited discussions on CIFAR-10 are shown in the appendix. The paper should conduct more convincing results from representative datasets (e.g., CIFAR-100, Tiny-ImageNet) to validate the framework.

2. How to generalize the framework to the state-of-the-art vision models remains a question. The paper only evaluates ResNet variants and should further involve ViT variants.

3. Existing methods of model-centric evaluations have utilized large generative models to sample OOD instances [1,2,3,4] by optimizing targeted objectives. The paper should discuss the uniqueness/effectiveness of the proposed approach compared to these baselines.

[1] (ECCV 2020) SemanticAdv: Generating Adversarial Examples via Attribute-conditional Image Editing.

[2] (ICCV 2021) Explaining in Style: Training a GAN to explain a classifier in StyleSpace.

[3] (CVPR 2023) Zero-Shot Model Diagnosis.

[4] (NeurIPS 2023) LANCE: Stress-testing Visual Models by Generating Language-guided Counterfactual Images.

### Questions
Please address the issues in the weakness section. I will consider revising the rating based on further responses from the authors.

### Soundness
1 poor

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Different from traditional data-centric evaluation methods based on the pre-defined test-set, this paper delves into model-centric evaluation, where the test-set is self-constructed by the model itself and the model performance is evaluated using the output distribution. Different from other model-centric evaluation methods, this paper leverages the output distribution as a bridge to generalize model evaluation from representative inputs to the entire input spaces.

### Strengths
- A sampler is known to estimate the output distribution over the entire input space given a trained model. This paper demonstrates the importance of the sampler in model-centric evaluation frameworks, which is meaningful and inspirable.

### Weaknesses
- The core component of the proposed framework, the sampler to estimate the output distribution over the entire input space, just simply follows the existing work [1], which makes the technique contribution not good enough. As mentioned by the authors in the paper, the proposed method is heavily relied on the sampler, while the sampler is simply borrowed from the existing works. To some extents, this paper can be viewed as an application of the sampler in the field of model evaluation. I realize the meaning of the proposed evaluation framework, but the technique contribution is not good enough to reach the bar of ICLR.

- This paper mainly focuses on a simple binary classification task to demonstrate the effectiveness of the proposed evaluation method.

[1] Gradient-based wang-landau algorithm: A novel sampler for output distribution of neural networks over the input space. ICML 2023.

### Questions
I will make my final rating after reading the rebuttal from the authors and the reviews from other reviewers.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed a new benchmark that uses the output distribution for model evaluation over the entire input space. Existing sampling algorithms such as GWL are used to sample representative inputs from the output distribution. Then the (human) evaluators annotate representative inputs. Finally, the authors compute the precision-recall curve to compare different machine learning models.

### Strengths
1. Compared with the traditional data-centric evaluations, the authors present a different evaluation benchmark based on model-centric evaluation.
2. The authors present a detailed analysis on the proposed benchmark. It is a fun read.

### Weaknesses
1. Over-fitting Concern: The benchmark, based on binary MNIST or the initial two classes of CIFAR10, leverages low-resolution images, making them relatively easy to recognize. Consequently, models tend to over-fit on this training set, as evident from the near-perfect accuracy rates in Table 1. Advanced CNN architectures might face the over-fitting issue, potentially leading to a subpar performance on the proposed benchmark.
2. Scalability Concerns: The authors may consider using a more diverse or challenging dataset to truly evaluate and validate model capabilities. However, the current approach may face challenges when extended to more complex, real-world datasets. The input space becomes considerably vast for such datasets, and there appears to be an absence of efficient sampling techniques in the current framework. It would be valuable to address how the proposed method plans to tackle these scalability issues.

### Questions
1. Benchmark Limitation: The proposed benchmark is currently restricted to binary classification. How does this benchmark be extended to handle multi-category settings?
---

Rebuttal Response:

The authors provide the CIFAR10/100 results in their rebuttal and have addressed my concerns regarding multi-class classification. However, the method's applicability to large benchmarks such as ImageNet is limited, primarily due to the inefficiency of the sampling algorithm. Despite this, the proposed method's novel approach presents a potentially significant direction for future research. Consequently, I have marginally increased my rating.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a model-centric evaluation framework to evaluate the quality of a model's predictions on **all possible inputs**.
It first uses a sampler to sample in the input space to obtain the output distribution.
Then, it annotates the representative inputs with human annotators, results in a human-annotated confidence score for each representative input.
Based on the confidence scores and model predictions, OmniInput generates a precision-recall curve and report AUC as the metric.

### Strengths
This paper first proposes a model-centric evaluation approach to evaluate the quality of a model's predictions on **all possible inputs**.

### Weaknesses
1. The authors didn't provide enough details for OmniInput (see questions). 
2. The proposed OmniInput was not applied to more challenging  / real world scenarios (large scale image classification, face recognition, etc.)

### Questions
1. More details of OmniInput need to be provided:
    1. How many samples do OmniInput samples for each experiment? Does it need to sample many data points to ensure at least 50 samples in each bin?
    2. The scales of log(recall) on precision-recall graphs need to be provided?
    3. Can this approach be applied to problems with larger scales, i.e., ImageNet classification (1000 classes)? 
2. Does the proposed metric have more advantages besides improved efficiency? For example, if a classification model achieves a higher AUC under OmniInput, can we say the model is less vulnerable to adversarial attacks (black box or white box)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
