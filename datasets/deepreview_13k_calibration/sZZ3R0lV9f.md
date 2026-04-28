# Perturb-and-Compare Approach for Detecting Out-of-Distribution Samples in Constrained Access Environments

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 5, 3

## Abstract
Accessing machine learning models through remote APIs has been gaining prevalence following the recent trend of scaling up model parameters for increased performance. Even though these models exhibit remarkable ability, detecting out-of-distribution (OOD) samples remains a crucial safety concern for end users as these samples may induce unreliable outputs from the model. In this work, we propose an OOD detection framework, MixDiff, that is applicable even when the model's parameters or its activations are not accessible to the end user. To bypass the access restriction, MixDiff applies an identical input-level perturbation to a given target sample and a similar in-distribution (ID) sample, then compares the relative difference in the model outputs of these two samples. MixDiff is model-agnostic and compatible with existing output-based OOD detection methods. We provide theoretical analysis to illustrate MixDiff's effectiveness in discerning OOD samples that induce overconfident outputs from the model and empirically demonstrate that MixDiff consistently enhances the OOD detection performance on various datasets in vision and text domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The authors address the issue of detecting out-of-distribution (OOD) data when there is no privileged access to model parameters or their activation. They begin by introducing an intuition that features contributing to misclassified samples (both ID and OOD) are more susceptible to perturbations. Building upon this insight, the authors propose a method called MixDiff, which involves mixing target and ID samples (oracle samples) with auxiliary samples to perturb both types of samples. By comparing the model outputs of the perturbed target samples with those of the oracle samples, the authors determine whether the target samples are OOD data. Experimental results across multiple datasets demonstrate the effectiveness of their method in achieving OOD detection while solely relying on the model output.

- In summary, leveraging the observation that contributing features in misclassified samples exhibit higher sensitivity to perturbations, the authors present MixDiff, a perturbation-based approach for OOD data detection. The method combines mixed samples and model output comparisons to effectively identify OOD data, as validated through experiments on various datasets.

### Strengths
- The authors explore a practical approach to OOD detection that relies solely on model inputs and outputs, offering significant value in real-world scenarios.
- They provide explicit theoretical and empirical evidence to support their method, showcasing its applicability through experiments involving out-of-scope (OOS) detection on an intent classification task.

### Weaknesses
 - The existing experiments are not comprehensive enough. I would recommend the authors to include an additional experiment to address the following concern:
 - While the experiments and theory conducted by the authors do support the effectiveness of their method, their motivation is based on the intuition that contributing features in misclassified samples are more sensitive to perturbations. However, this intuition lacks proper support and validation. Hence, it would be beneficial for the authors to incorporate relevant verification experiments to provide further evidence and clarify this aspect.

 - The description of the algorithm section could be improved to enhance its intuitiveness. It would be helpful to include a schematic diagram illustrating the algorithm, providing readers with a clearer understanding of its workflow.
 - In the related work section, the authors mention that some methods are not suitable for black-box APIs, where only access to inputs and outputs is available. An example of such a method mentioned in the paper is:
"Decoupling maxlogit for out-of-distribution detection." In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 3388–3397, June 2023.
 - However, including a comparison with such methods would help readers understand the extent to which the proposed approach differs from ideal scenarios with more information, under the constraints of rigorous black-box conditions. This would provide further insights into the progress of OOD detection under black-box settings.

### Questions
I would like the author to supplement and polish the article based on the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new OOD detection framework called MixDiff. MixDiff does not require knowledge of target models and only considers access to the input and output of an ML model. Specifically, MixDiff applies the same perturbation to a target sample and a trustworthy example and identifies an anomaly by comparing the relative difference between the model outputs. Empirically, the authors show that MixDiff performs well on various tasks.

### Strengths
(1) The paper is overall well-written and easy to read. 

(2) The proposed method is well-motivated by Figure 1 and the following observations. Using the relevant confidence to set the threshold for OOD detection is novel and easy to implement. 

(3) I appreciate the design of MixDiff and the detailed analysis. The empirical results demonstrate the proposed method could be useful in practice, especially when the knowledge of the model is largely restricted.

### Weaknesses
(1) The observation that OOD samples are less robust to perturbations (e.g., data augmentation methods such as MixUp) seems to align with the observation in the context of data poisoning, where poisoned data (can be also regarded as OOD samples) could be screened by strong augmentation methods. Although this is not strongly correlated, I encourage the authors to add a bit of discussion regarding this.

(2) Moreover, it would be interesting to see if MixDiff can be used as a defense against data poisoning. Of course, I am not asking the authors to perform relevant experiments, but it could be an interesting future direction.

### Questions
I don't have additional questions.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an OOD detection framework, MixDiff, that is applicable even when the model parameters or its activations are not accessible to the end user. To bypass the access restriction, MixDiff applies an identical input-level perturbation to a given target sample and an in-distribution (ID) sample that is similar to the target and compares the relative difference of the model outputs of these two samples. MixDiff is model-agnostic and compatible with existing output-based OOD detection methods. We provide theoretical analysis to illustrate MixDiff’s effectiveness at discerning OOD samples that induce overconfident outputs from the model and empirically show that MixDiff consistently improves the OOD detection performance on various datasets in vision and text domains

### Strengths
1. The paper is written well and is easy to understand.
2. The studied problem is very important.
3. The results seem to outperform state-of-the-art.

### Weaknesses
1. The motivation discussed in the introduction is somewhat opposite to the existing empirical findings on OOD detection with perturbed data. see [1], which suggests that the perturbed OOD data will also be predicted with overconfident probabilities for neural networks. Specifically, the paper does not adequately address the scenario where perturbations, instead of revealing a lack of robustness, might inadvertently push OOD samples towards the decision boundary of an in-distribution class, thus increasing the confidence of the model. This is a critical oversight, as the method's core assumption is that perturbations will expose the non-robustness of OOD samples, which is not always the case.
2. The compared baselines are not state-of-the-art. The authors are suggested to compare with more recent strong methods, such as those listed in [3,4]. The current baselines, such as MSP and Entropy, are well-established but do not represent the current state-of-the-art in OOD detection, particularly in the zero-shot setting. The paper should include comparisons with methods that leverage more advanced techniques, such as those that use feature-space analysis or more sophisticated scoring functions.
3. The authors are suggested to justify the assumptions used in the theory in a formal way. The theoretical analysis lacks rigor, and the assumptions made are not sufficiently justified. For instance, the conditions under which the proposed method is guaranteed to work are not clearly defined, and the theoretical results are not directly linked to the practical performance of the method. A more thorough theoretical treatment is needed to establish the validity of the proposed approach.
4. What is the computation cost of the proposed methods? It seems like the current method will require multiple forward/backward steps of the neural net during inference. The paper does not provide a clear analysis of the computational overhead of the proposed method. The need for multiple forward passes during inference could make the method impractical for real-time applications or large-scale datasets. A detailed analysis of the computational complexity and runtime is needed.

### Questions
see above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a perturbation-based OOD detection method to detect potential OOD samples when the model parameters cannot be accessed.

### Strengths
The tasks and scenarios proposed in the paper seem to have more application value at present.

### Weaknesses
1. The core motivation of the paper is that perturbed OOD samples will reduce more confidence. But this motivation is not intuitive and cannot be verified. This motivation fails to show its competitiveness compared to maximum class probabilities or predicted entropy.
2. Compared with directly using ood detection methods such as maximum class probability or predicted entropy, the complexity of the proposed method is very high, but according to the experimental results, the performance improvement is very limited.
3. When only the predicted labels of the model can be obtained, the performance of the model is very limited. And when the predicted probability of the model is obtained, it is no different from the previous OOD method without training, and I cannot see its significant advantage.

### Questions
None

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
