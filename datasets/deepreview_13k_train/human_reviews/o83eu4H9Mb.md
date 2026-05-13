# Information Retention via Learning Supplemental Features

- Decision: Accept
- Scores: 8, 6, 6, 8, 8

## Abstract
The information bottleneck principle provides an information-theoretic method for learning a good representation as a trade-off between conciseness and predictive ability, which can reduce information redundancy, eliminate irrelevant and superfluous features, and thus enhance the in-domain generalizability. However, in low-resource or out-of-domain scenarios where the assumption of i.i.d does not necessarily hold true, superfluous (or redundant) relevant features may be supplemental to the mainline features of the model, and be beneficial in making prediction for test dataset with distribution shift. Therefore, instead of squeezing the input information by information bottleneck, we propose to keep as much relevant information as possible in use for making predictions. A three-stage supervised learning framework is designed and implemented to jointly learn the mainline and supplemental features, relieving supplemental features from the suppression of mainline features. Extensive experiments have shown that the learned representations of our method have good in-domain and out-of-domain generalization abilities, especially in low-resource cases.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the principle of information retention, which stands somewhat on the opposite side of the principles of Occam’s razor and information bottleneck. It focuses on utilizing as much relevant information as possible in decision making instead of favoring simplest model. Next, this underlying idea get materialized by relieving supplemental features from the suppression of mainline features in a three-stage algorithmic framework. Extensive experimental results have manifested the effectiveness of the proposed method in both image classification and text classification tasks.

### Strengths
1) The approach overall is well-motivated and well-described. I like the organizational form of the paper, from conceptual idea to framework design and to concrete implementation, which is easy and natural to follow.
2) The principle of information retention and the method of learning supplemental features are novel and inspiring. It seems that the approach and method can be readily extended to other tasks.
3) Experimental results on image classification and text classification tasks have manifested the approach has good in-domain generalization ability, especially in poor-resource settings.

### Weaknesses
 1) The method can be better described with an overall workflow or architecture. 
 2) The paper needs further refinement of some minor details, and I have found some grammar and spelling errors in the sections of experiments and conclusions.
 3) Although I believe that the proposed approach can benefit out-of-domain generalization,it would have been better if some preliminary experiments had been conducted.

### Questions
1) Besides in-domain generalization, I wonder whether the proposed method has better out-of-domain generalization ability in some degree?
2) To my understanding, the supplemental features are learned by minimizing the conditional mutual information $I(\mathbf{x}, \mathbf{z}_S|\mathbf{x}’)$, is it right? Why not just minimizing the mutual information between $\mathbf{z}_S$ and $\mathbf{z}_M$?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes retaining supplemental features during training, as mainline features learned under the information bottleneck principle are insufficient to address out-of-distribution cases.

### Strengths
The illustration of the proposed method is easy to follow.

### Weaknesses
 - The paper is unqualified to be a top conference paper in several aspects, including novelty, contribution, and writing quality.
- The experiment design is outdated as of 2023. The choice of datasets and evaluation protocols does not reflect current standards in the field, particularly for out-of-distribution generalization. The experiments lack sufficient complexity and diversity to convincingly demonstrate the effectiveness of the proposed method.
- The writing needs improvement. For example, in the abstract, the authors mention, "relevant features may be supplemental to the mainline features of the model." However, the subsequent phrase "to address this problem" lacks coherence. Additionally, in the conclusion, verb tenses are inconsistent, alternating between "introduce" and "proposed."
- The paper lacks a comprehensive literature review. It fails to adequately contextualize the proposed method within the broader landscape of representation learning and out-of-distribution generalization techniques. Key related works are missing, and the discussion of existing approaches is superficial.

### Questions
- What contributions can the research in this paper make to the current mainstream deep learning models, such as GPT and Diffusion?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a new model architecture based on the intuition that redundant yet relevant features are also crucial, contradicting the information bottleneck principle. In detail, the authors designed a three-stage training algorithm: firstly, to learn the mainline feature; secondly, to erase the salient input; and thirdly, to learn the supplementary feature. The authors conducted classification tasks in both vision and language, and performed analyses to validate the usage of redundant features.

### Strengths
The paper starts with the intuition that the information bottleneck principle may be validated under specific situations and then formulates the idea into a training pipeline and model architecture. This is a very exciting buildup from idea to implementation. At the same time, the authors design the whole pipeline in a way that is very close to the initial idea, and they consider the details very thoughtfully. In the analysis part, they also provide sufficient evidence that the redundant yet relevant features are truly learned.

### Weaknesses
1. The presentation can be greatly improved. For instance, out-of-domain scenarios are mentioned in the abstract, but they are not explored in later experiments. The two examples in the introduction are unnecessary; they might even hinder comprehension, as some context is missing (as in example 1.1), and the usage could be restricted by the examples provided.
2. Section 3.3 shows the proposed algorithm extracts more information than other algorithms. It is also necessary to show that the extracted information is actually relevant information.
3. It would be helpful to provide some visualization to show that the second stage does erase the salient features. 
4. Some context in information theory is missing. A section of related work is needed.

### Questions
How is Equation (5) and (6) exactly derived?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel concept in supervised learning called information retention, emphasizing the importance of utilizing as much relevant information as possible for predictions. The authors introduce the InfoR-LSF framework, a three-stage learning system designed to process both mainline and supplemental features without allowing the mainline features to suppress the supplemental ones. Through experiments on the CIFAR10, IMDB, and YELP datasets, the paper demonstrates that InfoR-LSF outperforms existing methods, especially in low-resource scenarios. This research underscores the potential of InfoR-LSF to be effectively applied across various tasks, highlighting its unique approach to retaining and utilizing information.

### Strengths
1. The introduction of the concept of information retention and the development of the InfoR-LSF framework offer a fresh perspective on supervised learning. The method's focus on harnessing both mainline and supplemental features without interference distinguishes it from conventional approaches.

2. The paper conducts experiments on multiple datasets spanning different domains (CIFAR10 for image classification and IMDB and YELP for text classification). This extensive evaluation offers credibility to the method's versatility and robustness across varying types of data and tasks.

3. Beyond just presenting a novel method and its performance metrics, the paper delves deep into understanding its functioning. Through experimental verifications, like observing the model's attention distribution on input images, the authors effectively demonstrate the actual retention of information, strengthening the paper's central claim.

### Weaknesses
1. While the paper evaluates performance on both image and text classification tasks, it doesn't expand into other types of tasks (e.g., regression, segmentation, or sequence-to-sequence tasks), potentially limiting the generalizability of the findings. It would be beneficial to see how the method performs on tasks with different input and output structures, such as time-series forecasting or machine translation, to fully assess its versatility. The current evaluation leaves open the question of whether the observed benefits are specific to classification or if they extend to other learning paradigms.

2. The three-stage supervised learning framework has several components. An ablation study detailing the contribution of each component to the final performance would have given insights into the necessity and utility of each part. Specifically, it is unclear how much each stage contributes to the overall information retention and whether some stages are more critical than others. For example, the impact of the saliency erasing mechanism and the conditional mutual information constraint should be independently evaluated.

3. The paper doesn’t discuss any potential increase in computational complexity or training time introduced by the InfoR-LSF framework, which can be critical for real-world applications. The additional stages and computations involved in processing supplemental features likely add overhead, and it is important to quantify this impact. A comparison of training and inference times with baseline models would be necessary to assess the practical feasibility of the approach.

4. Apart from the sensitivity analysis of coefficient α, the paper does not deeply dive into how sensitive the model is to other hyperparameters, which can be crucial for replication and understanding model robustness. The masking ratio, for example, is a critical hyperparameter that controls the amount of information removed during the saliency erasing process. A more comprehensive sensitivity analysis is needed to understand how these parameters affect the model's performance and stability.

### Questions
1. Why were CIFAR10, IMDB, and YELP selected as the benchmark datasets? Are there plans to test the method on more diverse or domain-specific datasets?

2. How generalizable is the InfoR-LSF framework? Can it be easily adapted to other tasks or domains outside of image and text classification?

3. Given that adversarial training methods like FGSM were considered as baselines, did the authors consider evaluating the adversarial robustness of models trained with InfoR-LSF?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new paradigm of feature learning: Information Retention. The idea is to extract and keep as much *relevant* information as possible. This differs from the Information Bottleneck as such that Information Bottlenect tries to find the most compact informative features -- and this one does not focus on compactness, but keep as many relevant features. The proposed method consists of three stages that reflect the idea: (1) extract main features (2) find the most salient features -- make a copy of features with the salient ones removed (3) joint training of the features found in (1) and (2).

### Strengths
- The paper is well written
- The writers did a good job to soundly motivate why it makes sense to retain as much relevant feature as possible -- going slightly against the common paradigm to fins the most compact feature representation 
- Reasonable baselines and works on multiple modality
- I like that the authors perform verification experiment (3.3); this strengthen the claim.

### Weaknesses
 - One of my biggest concern is: in the abstract, the motivation was to enable better ood/distribution shift prediction. but none of the evaluation reflects this. in fact, the motivation seem to focus on low-resource settings. Does the authors focus is to generalize from learning on a small sample? If yes, this should be made clearer in the writing.
- An algorithm table would help a lot in method clarity
- Why does the feature erasure done in sample space, and not in feature space?

### Questions
1. In Weaknesses
2. Why does the feature erasure done in sample space, and not in feature space?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
