# Concept forgetting via label annealing

- Decision: Reject
- Scores: 5, 3, 1, 3

## Abstract
The effectiveness of current machine learning models relies on their ability to grasp diverse concepts present in datasets. However, biased and noisy data can inadvertently cause these models to be biased toward certain concepts, undermining their ability to generalize and provide utility. Consequently, modifying a trained model to forget these concepts becomes imperative for their responsible deployment. We refer to this problem as *concept forgetting*. Our goal is to develop techniques for forgetting specific undesired concepts from a pre-trained classification model's prediction. To achieve this goal, we present an algorithm called **L**abel **AN**nealing (**LAN**). This iterative algorithm employs a two-stage method for each iteration. In the first stage, pseudo-labels are assigned to the samples by annealing or redistributing the original labels based on the current iteration's model predictions of all samples in the dataset. During the second stage, the model is fine-tuned on the dataset with pseudo-labels. We illustrate the effectiveness of the proposed algorithms across various models and datasets. Our method reduces *concept violation*, a metric that measures how much the model forgets specific concepts, by about 85.35\% on the MNIST dataset, 73.25\% on the CIFAR-10 dataset, and 69.46\% on the CelebA dataset while maintaining high model accuracy. Our  implementation can be found at this following link: \url{https://anonymous.4open.science/r/LAN-141B/}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
To enhance the safety and responsibility of machine learning, this paper introduces a new task, concept forgetting. To achieve the goal of forgetting specific concepts while retaining the general ability of the original model, authors develop an iterative two-stage algorithm. The core idea of the algorithm is to ensure zero concept-violation on the newly created dataset by redistribution and relabeling.

### Strengths
- This paper proposes a novel and interesting problem referred to as concept forgetting. The task is set to forget a specific undesired concept without degrading the general ability. It is similar to the opposite counterpart of catastrophic forgetting but has not been well studied.
- The coherent text and the smooth transitions strengthened the readability of this paper.

### Weaknesses
- It’s difficult to understand the explanation of Algorithm 1, eg. in line 311 to line 315.
- As shown in Table 1, there is still an obvious reduction in test accuracy. I recommend more analysis of the reasons.

### Questions
- I have doubts about whether the algorithm has achieved a good experience effect. Firstly, it is because of the lack of enough competitors. Secondly, it is about the trade-off between concept violation and accuracy: if a concept is forgotten, the network should theoretically achieve better performance on other concepts.
- Have you considered the trade-offs between increasing the number of iterations (E) and maintaining model accuracy?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a novel approach for concept forgetting in deep neural networks. For this purpose, they introduce a two-stage iterative algorithm called Label Annealing (LAN). In the first stage, pseudo-labels are assigned to the samples by annealing or redistributing the original labels based on the current iteration’s model predictions. In the second stage, the model is fine-tuned on the dataset with pseudo-labels. They also introduce a novel metric called 'concept violation' that measures how much the model forgets a specific concept. The proposed algorithm has been validated across various models and datasets.

### Strengths
- The paper addresses a very relevant topic nowadays related with data privacy, which is represented by machine unlearning
- The paper presents a novel approach for concept forgetting in deep neural networks
- The related work covers most of the relevant paper in the field

### Weaknesses
- the paper is difficult to read, the clarity of both text and figures should be significantly improved
- the experimental validation is limited and not convincing. The authors compare their approach against 3 baselines, and none of them is related with concept forgetting

### Questions
Here are my concerns:
-  The differences between concept forgetting and machine unlearning are mentioned at the end of section 2. The authors should clarify this differences much earlier, in the introduction.
- Regarding definition 1:  'c' represents a class label or a feature?
- Regarding LAN algorithm: Why do you need to assign pseudo-labels? How do you deal with errors in pseudo-label assignment? Why don't just remove the classifier head corresponding to the removed concept?
- The problem of concept forgetting relies not only in retraining the classifier. The knowledge associated with it is implicitly embedded into the network's weights. How do you remove the information related with the concept being forgotten from the network's weights? I have not seen any discussion about this. If you retrain the network with the remaining data (after extracting the concept to forget), then this solution is trivial. What if the original data (used to train initially the network) is no longer available?
- Section 5.5: What means multi-level concept forgetting? Do you assume data is multi-labeled?
- In the experimental results, compare your approach against some methods from the current state of the art.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The author proposes a new issue termed concept forgetting.
The author argues that, to forget a concept, the label proportions should be constant regardless of the concept.
The author proposes an approach in which, when the label distribution varies according to a specific attribute in a pre-trained model, this is directly adjusted before further training.

### Strengths
The author has proposed an intriguing problem.
If concept forgetting is feasible, it may also be possible to remove unwanted information from a pre-trained model.

### Weaknesses
First, the proposed problem appears to be an ill-posed problem.
According to the author’s assertion, the entire dataset must be pristine.
If there is a concept not included in the dataset or if certain concepts are overrepresented, the optimal model for concept forgetting will be defined differently.
In fact, consider the example commonly addressed in debiased classification: in the dog and cat problem, dogs are often photographed outdoors, while cats are typically photographed indoors.
If additional outdoor photos are included, the label for indoor cats would need to be even more frequently replaced with that of dogs in the author’s algorithm.

Secondly, despite the author’s algorithm being highly intuitive and straightforward, its characteristics are not well explained.
The author replaces explanations of the proposed method with figures and algorithms, which does not aid intuitive understanding.
Even concept forgetting is not well explained beyond the measure defined as concept violation.
At the very least, it would be essential to verify whether the author’s method is beneficial when solving zero-shot classification tasks that align concepts in the trained model.

Lastly, in the theoretical analysis, the gap between the two terms in the inequality is substantial.
For the theoretical analysis to be meaningful, this gap needs to be minimized; the current gap arises from using the maximum value of the loss.
In the case of cross-entropy loss, the bound is exceedingly large, and when multiplied by the concept violation values observed by the author in Table 1, the upper bound of the curated loss inevitably becomes significantly large.
In fact, it is challenging to identify a clear correlation between the concept violation values and the reduced accuracy in the experimental results.

### Questions
(Clear problem definition)
Can the author explain the purpose of the algorithm with a real-world example? I did not intuitively grasp the goal of concept forgetting. For instance, I am curious about a plausible purpose, such as removing privacy-sensitive information.
Furthermore, the issue I mentioned in the weaknesses section, where the optimal solution for concept forgetting changes if the entire dataset changes, indicates that concepts may not be fully removed when a larger, pristine global dataset exists beyond the given dataset. I am curious about the author's assumptions regarding the entire dataset in this context.

(Justification of the measure)
Additionally, while concept violation appears to be a reasonable measure, it does not necessarily reflect whether concept forgetting has truly been achieved. Cross-entropy loss is a good measure for classification tasks, but for models trained with techniques like label smoothing, the loss can increase independently of accuracy. Similarly, I believe that concept violation cannot be considered a perfect measure. Since concept violation is a measure introduced by the author, it requires thorough analysis from multiple perspectives; however, in the submitted paper, it is only used as a measure without further analysis. It seems necessary to include a qualitative analysis in the experiments demonstrating that low concept violation indeed addresses the intended purpose of concept forgetting. In addition to the analysis I suggested, any results that can further demonstrate the utility and significance of your concept violation measure would be welcome.

(Representation)
The methods for the author’s algorithm can all be represented by figures and pseudo code. This implies that Section 4.1 is somewhat redundant. Adding insights into each step of the algorithm in the main text would be beneficial. For example, is the sorting in line 4 truly meaningful? What is the reason for selecting the next label deterministically in line 9? What is an adequate range for E? Addressing questions like these would enable a deeper understanding of the author’s algorithm.
Lastly, the author’s theoretical analysis does not provide much help in interpreting the experimental results. Is it possible to define a tighter boundary under specific conditions?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a new approach to studying concept forgetting, which aims to remove some concepts from pre-trained models while preserving their performance. To achieve this goal, the authors propose an algorithm called Label ANnealing (LAN), which employs a two-stage process to align the distribution of pseudo-labels with the class distribution, as generated by the trained model's predictions. Experimental evaluations on four benchmark datasets – MNIST, CIFAR-10, miniImageNet, and CelebA – demonstrate that concept violation can be effectively mitigated.

### Strengths
1. The idea of the paper is good and important for research. 
2. The example in the introduction is also interesting that "envision a CelebA (Liu et al., 2015) image classifier that heavily relies on background color as a distinguishing feature to classify different celebrities, limiting its ability to generalize effectively".

### Weaknesses
1. Following the example provided in the introduction, I anticipated an improvement in performance after removing harmful features. Nevertheless, my findings contradict this expectation: despite claims of 'maintaining the model’s overall performance and generalization ability', I observed a significant drop in performance on all datasets, with a particularly notable 15% decrease on CelebA for the task 'Heavy makeup or not'. This discrepancy suggests that the authors should revisit their method to ensure it meets its stated objectives.
2. The concept of 'concept violation' is not rigorous, as it only evaluates model outputs without considering the nuanced effects of concepts within decision-making processes. Even when results appear identical, it is uncertain whether a particular concept has been entirely eliminated or merely masked in some way.
3. The alogrithm Label ANnealing is simple.

### Questions
1. I am not sure I fully understand the experiments. Are examples in forgetting classes removed, and examples in the rest of the classes are used to train and test? 
2. I suppose the introduction example 'background' is good; I think in experiments, the authors should give the results of the example. Does the method only work with concepts that have labels? If so, this is a strong limitation to the proposed method.

### Soundness
1

### Presentation
3

### Contribution
2
