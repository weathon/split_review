# Energy-based Automated Model Evaluation

- Decision: Accept
- Scores: 6, 6, 3, 8, 8

## Abstract
\vspace{-5pt}
The conventional evaluation protocols on machine learning models rely heavily on a labeled, i.i.d-assumed testing dataset, which is not often present in real-world applications.
The Automated Model Evaluation (AutoEval) shows an alternative to this traditional workflow, by forming a proximal prediction pipeline of the testing performance without the presence of ground-truth labels.
Despite its recent successes, the AutoEval frameworks still suffer from an overconfidence issue, substantial storage and computational cost.
In that regard, we propose a novel measure --- \textbf{M}eta-\textbf{D}istribution \textbf{E}nergy \textbf{(MDE)} that allows the AutoEval framework to be both more efficient and effective.
The core of the MDE is to establish a \emph{meta-distribution} statistic, on the information (energy) associated with individual samples, then offer a smoother representation enabled by energy-based learning.
We further provide our theoretical insights by connecting the MDE with the classification loss.
We provide extensive experiments across modalities, datasets and different architectural backbones to validate MDE's validity, together with its superiority compared with prior approaches.
We also prove MDE's versatility by showing its seamless integration with large-scale models, and easy adaption to learning scenarios with noisy- or imbalanced- labels

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper intends to solve the auto evaluation problem of a well-trained classification model on a test dataset with domain shift and without labels. The proposed method is based on an energy-based framework to estimate the Meta-Distribution Energy, which is used to train a regression model on synthesized dataset for prediction of classification accuracy on unlabelled test data.

### Strengths
This paper introduces an energy-based automatic evaluation framework designed to enhance efficiency and mitigate overconfidence in existing methodologies. The proposed approach indicates better prediction on unseen test data over the other measurement methods on dataset in different modalities and with different classification models.

### Weaknesses
1. It is recommended to use a different symbol for the normalization term E(x) in Eq(2) to avoid confusion, like Z(x).
2. In Eq(5) and Eq(6), the font of matchcal is usually used for a single letter.
3. I cannot see a clear relationship between the proposed method and the energy-based model except that "energy" specifies the logits from the classification model. 
4. The performance of the proposed framework relies on the regression between MDE on the synthesized dataset and its accuracy. However, the type of domain shift is more complicated in the real world in most cases, thus very unpredictable. 
5. The experiment on adjusting temperature T should be conducted on a broader range, like from 0.01 to 100. The change from 1 to 10 is relatively small.
6. A real dataset for evaluation needs to be included. The operation of shear, equalization, and color temperature adjustment is easy to synthesize, while the domain shift could come from more complex sources like [1][2].
7. Some missing EBM references can be considered to be included into this paragraph to make it more complete for the readers. For example, [3] is the first EBM using CNN for energy function and trains it with Langevin dynamics. [3] is also the first one to point out that EBM and a classifier can be derived from each other. The EBM applications not only include video as you have mentioned in your paper, but also include point cloud [4], voxel [5], trajectory [6] and molecules [7].

### Questions
1. For Eq(5), is MDE defined on specific data $x_n$, where MDE(x; f) should be MDE($x_n$, f)? Or does it miss an expectation term over the dataset?
2. How is the synthesized test data generated when training the regression model for accuracy prediction?
3. If the proposed method indicates a significant drop in a new dataset, is there any way to correct this bias based on the proposed MDE?
4. How is the correlation evaluated in Table 1 on a specific dataset? 
5. How to determine the best hyper-parameter of T on a new dataset? Is the best parameter related to the dataset or the classification model?
6. Will the selection of different regression models affect the prediction accuracy?
7. Is there any comparison on the evaluation of domain-shift data with real labels?

### Soundness
2 fair

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
- Authors propose a method for a problem called 'AutoEval'. The problem is described as evaluating the effectiveness of a model on data without ground truth labels.
- The proposed method is very simple. It is based on energy models.
- Authors perform experiments on datasets like CIFAR-10/100, TinyImagenet to validate their method.

### Strengths
The authors have performed a wide range of analysis experiments.

### Weaknesses
1. The problem addressed
-  Authors motivate some new problem called Automated model evaluation. The definition is not very clear as they define it in many different ways.
- I am not sure about the relevance of the problem. Or to phrase it better - I don't know much about this problem.

2. Proposed method
- The proposed method just use energy based model equation to create a simple function of the energy expressed in terms of logits. 
- One concern here is that it might be very similar to some method in Uncertanity estimation.
- Can authors mathematically compare this method to some common methods in uncertainity estimation.

3. Experimental validation
- While the introduction had motivated the problem in a broad setting. Authors discussed OOD to motivate the problem. But I could not find the experiments on OOD.
- The claims should match the experiments on which the method is validated. Maybe the authors can provide experiments on OOD.

### Questions
Please see the weakness section

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on AutoEval, where the goal is to estimate classifier performance on unlabeled test sets. To this end, this work proposes to use energy score (MDE) as the statistic of each test set for inferring the corresponding classification accuracy. The experimental results on several benchmarks such as CIFAR-10 and CIFAR-100 show the proposed can achieve reasonable accuracy estimation.

### Strengths
+ Algorithm 1 clearly shows the proposed method. The whole pipeline is well-introduced
+ The experiment includes MNLI, a natural language inference task.

### Weaknesses
 - *1. Overstated claims*: The paper asserts that "the AutoEval frameworks still suffer from an overconfidence issue" without providing clear, empirical examples. Additionally, the statement regarding "substantial storage" lacks a comparison with existing methods such as DoC and ATC, leaving the reader unconvinced of any real advantage of the proposed method. Furthermore, the claim that the proposed MDE method is superior in terms of "computational cost" is not substantiated, especially considering that unlike ATC, MDE requires the training of a linear regression model. To move forward, it would be essential to clarify these issues with specific data and comparative analysis.

- *2. Limited contribution*: The novelty of your work is questioned due to the similarity with existing methods in the field. The use of Energy score as a replacement for Softmax score, without significant insights or enhancements, is seen as insufficient for constituting a substantial contribution. Prior works [Detecting Errors and Estimating Accuracy on Unlabeled Data with Self-training Ensembles] have already discussed the connection between OOD detection and AutoEval, which the current submission does not appear to extend beyond.

- *3. Unconvincing theoretical analysis*: The theoretical grounding provided in Section 3.3 is deemed unclear and unconvincing. The methodology for ascertaining model accuracy needs to account for scenarios where an image is correctly classified with a low Softmax score. A more robust theoretical framework is necessary to support the claims made.

- *4. Experimental results are not solid*: The absence of results for ImageNet-1K in Table 1, along with other test datasets like ImageNet-S/A/V2, raises concerns about the comprehensiveness of the experimental evaluation. Moreover, the omission of recent relevant works, such as "Characterizing Out-of-Distribution Error via Optimal Transport," and the lack of comparison with methods like Nuclear Norm on ImageNet setup, call into question the thoroughness of the analysis.

- *5. Limited Dataset Diversity*: The paper does not report on more natural shifts, which are included in benchmarks provided by methods like ATC. While BREEDs are mentioned in the supplementary material, results are not presented, and expectations for insights on datasets like i-WILDS are not met.

### Questions
- Please clarify the claims on overconfidence issue, substantial storage, and computation cost 
- Please report the results on the ImageNet setup and the estimates of ImageNet-A/V2/S
- Please clearly compare with existing works such as ATC, DoC, and Nuclear Norm on ImageNet. Moreover, [Characterizing Out-of-Distribution Error via Optimal Transport] should be included for comparison.
- Other related works: Estimating and explaining model performance when both covariates and labels shift. In NeurIPS 2022

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel measure called Meta-Distribution Energy (MDE) for automated model evaluation (AutoEval), which is a method for assessing the performance of machine learning models on unlabeled test data. The core idea of MDE is to convert the energy information of the model's output into a probability distribution statistic, which enables a smoother data representation. The paper also provides theoretical analysis connecting MDE with classification loss, proving its effectiveness. Experimental results demonstrate MDE's superior performance across various modalities, datasets, and model architectures, especially in noisy and class-imbalanced scenarios.

### Strengths
* The research topic of this paper -- AutoEval is valuable in the real world deployment of DNNs. I believe this area may shed some novel light on the unsupervised evaluation community.
* This paper establishes a connection between MDE and classification loss through a mathematical theorem, providing theoretical justification for the effectiveness of the proposed method.
* MDE demonstrates strong performance across a variety of modalities, datasets, and model architectures, and these detailed analyzes make it as a versatile solution for automated model evaluation.
* MDE remains effective even in challenging scenarios such as strong noise and class imbalance, showcasing its robustness in practical applications.

### Weaknesses
 * The paper does not provide source code, making re-implementation challenging. Please provide the code later to dispel this concern.
* Interpretability can be further explored. While MDE provides strong correlation with classification accuracy, further research could focus on enhancing the interpretability of the method, making it easier for users to understand and trust the results.
* Different methods seems to have different (wall-clock?) time required to come up with such evaluation -- perhaps some notes on that would be helpful as well.
* Grammar should be thoroughly checked. For example, in the first paragraph, "the information (energy) associated with individual samples, then offer a smoother representation enabled by energy-based learning." should be changed to "xxxx, and then offers...". Similarly, in the second paragraph, "the correct classified data are given low energies, and vice versa" should be changed to "the correctly classified..."

### Questions
Please refer to the weakness section mentioned above.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a metric called Meta-Distribution Energy (MDE) for automated model evaluation (assessing model performance on unlabeled datasets). The method involves extracting energy scores from the model's output and extending them into a statistical representation at the dataset level. The paper demonstrates a strong linear relationship between MDE and classification accuracy on datasets with differing extents of distribution shifts. This allows for predicting model performance based on the MDE of an unlabeled test set, and the authors provide theoretical proof of this concept. In the experimental section, the paper presents the outstanding performance of MDE across different backbones, datasets, and modalities, even in scenarios with noise and class imbalance.

### Strengths
1) The task of AutoEval is crucial when deploying neural network models in real-world scenarios. It can help avoid the issue of not knowing the actual performance in practical applications and is also beneficial for model selection."
2) The method MDE in the paper exhibits a relatively high level of novelty by introducing the statistical distribution of energy scores into the field of AutoEval for the first time. Furthermore, the paper extends the approach to improving energy scores, which can be applied to a wider range of tasks. Additionally, the authors provide detailed theoretical proof that strongly illustrates the effectiveness of the method.
3) The paper conducts extensive experiments on different backbones, different datasets, and different modalities. The experimental results indicate a significant performance improvement compared to other methods in the field.
4) The paper is of high writing quality, with a smooth and easy-to-grasp presentation of the key points.

### Weaknesses
1) It seems that the paper does not provide a more detailed explanation of the parameter T in MDE. Is T just an ordinary parameter, or does it have a more intuitive meaning? In Figure 3(a), only the trend of T from 1 to 10 is displayed. What is the impact of a wider range of T values on the results? Specifically, how does the performance of MDE change when T approaches zero or becomes significantly large, and what are the implications for the method's robustness?
2) In the paper, the authors categorized relevant methods into 'training-free' and 'training-must.' How much progress does MDE, as a 'training-free' method, make compared to 'training-must' methods in terms of evaluation time and memory usage? It would be ideal to conduct an experiment to illustrate this. A more detailed analysis, perhaps including a breakdown of the computational steps and memory requirements for both types of methods, would be beneficial. This would provide a clearer understanding of the practical advantages of MDE.

### Questions
Please try to address the questions I raised in the 'Weaknesses' chapter.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
