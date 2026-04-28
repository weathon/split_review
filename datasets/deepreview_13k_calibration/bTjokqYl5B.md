# On the Onset of Robust Overfitting in Adversarial Training

- Decision: Reject
- Avg Score: 3.20
- Scores: 6, 3, 3, 3, 1

## Abstract
Adversarial Training (AT) is a widely-used algorithm for building robust neural networks, but it suffers from the issue of robust overfitting, the fundamental mechanism of which remains unclear. In this work, we consider normal data and adversarial perturbation as separate factors, and identify that the underlying causes of robust overfitting stem from the normal data through factor ablation in AT. Furthermore, we explain the onset of robust overfitting as a result of the model learning features that lack robust generalization, which we refer to as non-effective features. Specifically, we provide a detailed analysis of the generation of non-effective features and how they lead to robust overfitting. Additionally, we explain various empirical behaviors observed in robust overfitting and revisit different techniques to mitigate robust overfitting from the perspective of non-effective features, providing a comprehensive understanding of the robust overfitting phenomenon. This understanding inspires us to propose two measures, attack strength and data augmentation, to hinder the learning of non-effective features by the neural network, thereby alleviating robust overfitting. Extensive experiments conducted on benchmark datasets demonstrate the effectiveness of the proposed methods in mitigating robust overfitting and enhancing adversarial robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The paper investigates the causes and mechanisms behind robust overfitting in adversarial training (AT). Robust overfitting refers to the phenomenon where a model's robust test accuracy declines as training progresses.
- Through factor ablation experiments, the authors show that the factors inducing robust overfitting originate from the normal training data, not the adversarial perturbations.
- They explain robust overfitting as arising from the model learning "non-effective" features that lack robust generalization. Specifically, due to distributional differences between training and test data, features that are robust on training data may not generalize to be robust on test data.
- As training progresses, the gap between the model's learning states on training vs test data widens. This facilitates the proliferation of non-effective features. When optimization is dominated by these features, robust overfitting occurs.
- Based on this understanding, the authors propose two measures to regulate the learning of non-effective features: 1) Attack strength - using higher attack budgets to eliminate non-effective features. 2) Data augmentation - to align the model's learning state on training and test data.
- Experiments show clear correlations between the extent of robust overfitting and the degree to which these measures suppress non-effective features. The proposed methods mitigate robust overfitting and improve adversarial robustness across different models and datasets.
- Overall, the work provides an explanation of robust overfitting from the perspective of features and learning states. The understanding and analysis seem quite intuitive and comprehensive. The paper makes a valuable contribution towards demystifying the mechanisms behind this phenomenon.

### Strengths
Originality: The paper provides a novel perspective on understanding robust overfitting by treating normal data and perturbations as separate factors. The idea of non-effective features that lack robust generalization is also an original concept proposed in this work.

Quality: The study is scientifically rigorous, with principled factor ablation experiments that isolate the effect of normal data. The analysis and explanations are intuitive yet comprehensive. The proposed methods demonstrate consistent effectiveness.

Clarity: The paper is very clearly written and structured. The background provides sufficient context. The experiments and results are well-described. The analysis logically builds up an explanation of robust overfitting in an easy to follow manner.

Significance: Robust overfitting is a major impediment in adversarial training that lacks a satisfactory explanation. This work makes significant headway by unraveling its underlying mechanisms. The insights can inform the design of more effective defenses. Overall, this is an impactful study that advances fundamental understanding of an important phenomenon in adversarial machine learning.

In summary, the originality of the conceptual framing, rigorous experimental methods, clear writing, and significance of the research problem make this a compelling paper with multiple strengths. It is a valuable contribution that sheds light on the mechanisms behind robust overfitting through a meticulous and insightful analysis.

### Weaknesses
 - While effective, the attack strength and data augmentation measures may not represent optimal or sufficient solutions. More advanced techniques informed by this analysis could further enhance robustness.
- The theoretical analysis relies on intuitive reasoning. Formalizing the notions of robust/non-robust features and quantifying the learning state gap could strengthen the conceptual framing.
- The focus is on explaining robust overfitting, less on maximizing robust accuracy. Follow-up work could build on these insights to achieve state-of-the-art robustness.
- The experiments primarily use simple CNN architectures on CIFAR datasets. Testing the analysis on larger datasets and SOTA models could reveal additional insights.
- There is limited ablation on the proposed methods themselves. Varying their hyperparameters and components could better isolate their effects.
- The writing could further improve clarity in some areas, like explicitly defining "small-loss" data earlier on.

### Questions
1. The analysis relies on the notion of a "gap" between training and test learning states. Is there a principled way to quantify this gap? Are there any theoretical bounds on the gap size that induces robust overfitting?
2. Have you experimented with more advanced data augmentation techniques like MixUp or CutMix? Could these further help with state alignment and reducing non-effective features?
3. How well do your insights transfer to larger scale problems like ImageNet? Are there any key differences in robust overfitting that you observe in such settings?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of robust overfitting in adversarial training and seeks to understand and mitigate it through empirical analysis. They conduct factor ablation experiments in adversarial training and conclude that robust overfitting stems from the normal data. They explain the onset of robust overfitting is due to the learning of non-effective features during adversarial training, and revisit different techniques for mitigating robust overfitting from this perspective. Based on these insights, they propose two methods based on the attack strength and data augmentation to suppress the learning of non-effective features, and thereby reduce robust overfitting.

### Strengths
- The paper addresses robust overfitting in adversarial training, which is an important problem and not fully understood.

- The discussion of the phenomenon of robust overfitting leading to section 3.2 is clear and well motivated.

### Weaknesses
The central discussions of the paper are vague and mainly intuitive in nature. There are no concrete equations or an algorithm for the proposed methods based on attack strength and data augmentation. Furthermore, there is no analysis to support the claims about robust overfitting.

The discussions in section 3.2 and 3.3, which form the crux of the paper, are not clear. For instance, in the following statements (in Section 3.2.1, page 5), what is meant by the similarity of the model’s learning states on the training vs test data? The paper should explain this in a more principled, mathematical way.

> “In the initial stages of adversarial training, due to the similarity in the model’s learning states between the training and test datasets, the boundary between the robust and non-robust features doesn’t significantly differ between the training and test sets.”

> “Adversarial data with small loss indicates that the model’s learning state on these data is excellent, maintaining a substantial gap compared to the learning state on the test set.”

### Questions
1. In Eqn (4), please clarify that the max is over the perturbation $\delta_i \in \Delta$, and that $x^\prime_i = x_i + \delta_i$.

2. For the factor ablation experiments in Section 3.1 and Figure 1, are the results averaged over a few trials to account for randomness?

3. Can you concretely define "effective features" and the idea of "similarity of a model's learning states between the training and test data"?

### Soundness
2 fair

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
In this paper, robust overfitting, an interesting and important phenomena in adversarial training, is investigated. The main conclusion is robust overfitting is a result of learning non-effective features, which also leads to new enhancement method.

### Strengths
Since robust-overfitting is a specific phenomena in adversarial training. Indeed, it should consider the difference of natural example and adversarial perturbation, as the authors did. To observe the difference, they design good ablation experiments, which indeed could bring new thoughts.

### Weaknesses
- the main conclusion that overfitting is because of learning non-effective features is too trivial. It may be true for any type of overfitting but specifically suitable for adversarial training.

- as I said, it is good to design interesting experiments to find something. But still it is better to also include theoretical discussions, especially on the specific properties for adversarial training.  

- the methods derived from the main conclusion is not interesting. Data augmentation is almost the most natural way to suppress overfitting. Attack strength adjustment is also common for adversarial training. For example. PGD-based on AT can be regarded as adaptive attack adjustment.

- It is OK if the authors choose to evaluate the proposed method numerically. However, the experiments should be enhanced largely. The performance should be compared not only to vanilla adversarial training but also other robust overfitting suppression method. Notice that the training time should be reported.

### Questions
please see the weakness.

### Soundness
2 fair

### Presentation
2 fair

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
Summary: 
This study is dedicated to investigating the fundamental mechanism of robust overfitting in adversarial training. First, the robust overfitting is attributed to the non-effective features that hinder the model from learning generalization ability. Then, the study proposes OROAT with attack strength and data augmentation to alleviate learning on non-effective features. Experiments validate the robustness of OROAT across several adversarial training methods to counter different attacks.

### Strengths
pros:
1. Provide an innovative view to separate adversarial training data into normal and small-loss adversarial data. And the method of composition that first dives into the problem and then proposes a solution is appealing.
2. Introduce a plug-and-play method that is experimented with many adversarial attack and training methods.

### Weaknesses
cons:
1. Chapter 3 lacks experimental results to support analysis. For example, the study mentions the gap between training and test learning state several times, which would be better accompanied by a figure illustrating the difference of robust overfitting between training and test data. Specifically, the analysis of non-effective features is not sufficiently supported by empirical evidence. The claim that these features hinder generalization requires more direct validation, perhaps through feature visualization or ablation studies that demonstrate their impact on test set performance. Furthermore, the mechanism by which adversarial perturbations amplify distribution differences between training and test sets needs more rigorous justification. It would be beneficial to see a quantitative analysis of how the perturbation magnitudes differ between the two sets and how this difference correlates with the observed robustness gap.
2. The writing of analysis and method is too lengthy, whereas the experiment part is too condensed. These sections have to be reorganized to alleviate the reading burden. The method descriptions, while detailed, could be streamlined by focusing on the core algorithmic steps and deferring less critical details to supplementary material. Conversely, the experimental section lacks sufficient detail to allow for reproducibility. For example, specific hyperparameter settings, training procedures, and the exact adversarial attack configurations used should be included. This imbalance makes it difficult to assess the practical significance of the proposed method.
3. Experiments are solely conducted on CIFAR10 and CIFAR100. Larger datasets like ImageNet should be explored. The lack of evaluation on larger, more complex datasets limits the generalizability of the findings. It is unclear whether the observed effects of OROAT would hold for models trained on datasets with higher dimensionality and more diverse feature distributions. The absence of experiments on ImageNet, a standard benchmark for adversarial robustness, is a significant limitation.
4. The ablation studies show that the effect of OROAT turns negative towards adversarial robustness and possible reasons. How to avoid this situation needs explanation. Additionally, Table2 needs to highlight the results that perform best or correspond to the argument in texts. The negative impact of OROAT under certain conditions needs further investigation. It is not sufficient to simply acknowledge the issue; the authors should provide a more detailed analysis of why this occurs and propose potential solutions. The lack of clear highlighting in Table 2 makes it difficult to quickly assess the key findings and their relation to the claims made in the text.
5. Lack comparisons with existing mitigations of robust overfitting. The authors has included various previous works in the related works/revisiting section, which is good. However, there is no empirical comparison. The absence of empirical comparisons with existing robust overfitting mitigation techniques makes it difficult to evaluate the relative effectiveness of the proposed method. While the related work section is comprehensive, it does not provide a clear picture of how OROAT compares to other state-of-the-art approaches in terms of performance and computational cost.

### Questions
Refer to the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new method to mitigate overfitting in adversarial training. The proposed method changes the magnitude of adversarial attacks in adversarial training and applies AugMix to the small-loss examples within a minibatch if the proportion of the small-loss examples is below the specified threshold. Experiments demonstrate that the proposed method improves the performance of AT, AWP, TRADES, and MLCAT.

### Strengths
- This paper addresses an important problem: overfitting in adversarial training because adversarial training suffers from overfitting more than standard training.
- Experiments use AutoAttack, which is a de-fact standard evaluation method, and several baselines are used.
- Figure 1 shows somewhat interesting results. Comparing removing small-loss adversarial examples with removing only the perturbation of small-loss adversarial examples is an interesting investigation from a new aspect. However, this result does not lead well to the proposed method.

### Weaknesses
 - There are a lot of undefined words: e.g., non-effective features and learning state. Since these words are frequently used in the analysis for developing the proposed method, readers could not understand why the proposed method is effective to mitigate overfitting.
Non-effective features and learning state should be defined by using equations and empirically evaluated or theoretically evaluated in the existence of adversarial training.
- Most parts of claim do not have objective evidence. For scientific articles, most of claims should be supported by the evidence. For example, the following states do not supported by the experimental or theoretical results:   
_"In the initial stages of adversarial training, due to the similarity in the model’s learning states between the training and test datasets, the boundary between the robust and non-robust features doesn’t significantly differ between the training and test sets. "_  
_"However, the improvement in the model’s learning state on the test dataset is relatively limited, far from matching the model’s learning state on the training dataset"_  
_" As a result, the boundary between the robust and non-robust features becomes progressively more distinct between the training and test sets."_  
_"adversarial data with small loss indicates that the model’s learning state on these data is excellent, maintaining a substantial gap compared to the learning state on the test set."_  
I suggest you to provide more empirical results or theoretical results that support your claims and the effectiveness of the proposed method.
- The proposed method is not clearly written, and its explanation does not have equations or pseudo codes.
Readers cannot reproduce the results.
I could not understand how to control the attack strength in the proposed method and how to use data augmentation.
What value of the loss do you call small loss for small-loss adversarial data?
What is the specified threshold for the proposed method?
Regarding changing adversarial budgets in adversarial training, [a] might be related work, which schedules adversarial budgets for considering loss landscapes.

### Questions
- Do you have any evidence that supports your claims as witten in Weakness?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
