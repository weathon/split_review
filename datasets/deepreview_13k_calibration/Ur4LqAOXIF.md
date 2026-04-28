# SODA: Stream Out-of-Distribution Adaptation

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
In open-context environments, machine learning models require out-of-distribution (OOD) awareness to ensure safe operation. However, existing OOD detection approaches have primarily focused on the offline setting, where OOD detectors remain static and fixed after deployment. This limits their ability to perform in real-world environments with unknown and ever-shifting out-of-distribution data. To address this limitation, we propose a novel online OOD detection framework that allows for continuous adaptation of the OOD detector. Our framework updates the ID classifier and OOD detector sequentially, based on samples observed from the deployed environment, and minimizes the risk of incorrect OOD predictions at each timestep. Unlike traditional offline OOD detection methods, our online framework provides the adaptivity and practicality needed for real-world environments. Theoretical analysis demonstrates that our algorithm provably achieves sub-linear regret and converges to the optimal OOD detector over time. Empirical evaluation in various environments shows that our online OOD detector significantly outperforms offline methods, highlighting the superiority of our framework for real-world applications of OOD detection.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the out-of-distribution detection problem. It presents an online detection algorithm that keeps updating the model parameters as the stream reveals data.
The algorithm is simple, yet demonstrated experimentally to be effective.

### Strengths
The main strengths of this work are:

- The paper is simple and easy to follow and understand. It gently introduces the problem and smoothly translates to the proposed method.

- The proposed algorithm (SODA) is simple and neat.

- The provided experimental results shows the effectiveness of the proposed SODA compared to other baselines under the streaming evaluation.

### Weaknesses
The main weaknesses of this work are:

1- Paper writing: While the paper is generally easy to follow in sections (1, 2, 3), there are several missing details (for a non-expert) that made reading the experimental section harder. such as:

(1a) Definition of performance measures such as FPR and AUROC.

(1b) The rationale behind choosing the datasets in Table 1. Why I SCHN considered OOD compared to CIFAR? Is there a way to quantify how far the evaluated distribution is from the training one?

2- The experiments conducted on this work consider stationary datasets such as ImageNet and CIFAR-10 where the stream is synthetically constructed. I would advise tackling realistic benchmarks such as [A, B, C] from the online learning literature where the stream is defined with respect to time.

3- Discussion of limitation: The proposed SODA, while being effective in many cases, can fail in other scenarios. For instance, consider a stream with very small visual variations with respect to time (e.g. a survallance camera). SODA will be then presented with the same batch (with small variations) repeatedly for some time. Would this make the online updates overfit the network parameters and fail to generalize on new novel batches? A discussion on the limitations of SODA should be included.

### Questions
Please refer to the weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A novel online OOD detection framework is presented in this work to better adapt to a dynamic environment. This is crucial for its use in real-world applications. From the theoretical aspect, this study demonstrates that the proposed algorithm provably achieves sub-linear regret and converges to the optimal OOD detector over time. The proposed algorithms are also validated by empirical evaluations on commonly used offline OOD data as well as its corresponding online version (simulated).

### Strengths
This paper solves a significant and challenging research question, i.e., online OOD detection.
This paper contributes with both theoretical and empirical insights.

### Weaknesses
The solution seems less technical to me. This needs further discussion during rebuttal.
The current version seems to embed an OOD detector into a naive online learning framework.

This paper claims its novelty in online OOD detection. However, [1] is also designed for online OOD detection. Please compare the difference, and specify one what aspect this work is better than [1].

Could you specify which items in (2) and (3) are designed specially for an online non-stantioanry environment?

In the current SODA, OOD detector and classifier are updated at every new t. However, this update is not always good. Please explain why it is necessary to update OOD detector and classifier for EVERY new t, rather than retain the previous one for some t. 

Will SODA have a high computational cost? Please also specify the computational cost for update process.

### Questions
1. This paper claims its novelty in online OOD detection. However, [1] is also designed for online OOD detection. Please compare the difference, and specify one what aspect this work is better than [1].
[1] Wu, Xinheng, et al. "Meta OOD Learning For Continuously Adaptive OOD Detection." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

2. Could you specify which items in (2) and (3) are designed specially for an online non-stantioanry environment?

3. In the current SODA, OOD detector and classifier are updated at every new t. However, this update is not always good. Please explain why it is necessary to update OOD detector and classifier for EVERY new t, rather than retain the previous one for some t. 

4. Will SODA have a high computational cost? Please also specify the computational cost for update process.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies stream learning with out-of-distribution (OOD) data with $T$ rounds. At each round, In each round, the learner needs to predict whether the incoming unlabeled samples are from the OOD class. After that, the label of the sample is revealed to the learner. The paper proposes an online learning algorithm, which updates the model by performing a gradient step with the cross entropy loss.  Regret analysis and extensive experiments are conducted to validate the proposed methods.

### Strengths
The strengths of the paper are as follows:
- Problem setting: The problem of Out-Of-Distribution (OOD) detection with stream data is a relevant and interesting topic for the reliable machine learning community.
- Presentation: The paper is well-structured and clearly written in most parts.
- Experiments: Extensive experiments have been conducted in this paper to validate the proposed methods.

### Weaknesses
The weaknesses of this paper are as follows:
- Originality and Significance: My main concern about the paper is the originality of the proposed method. It seems to me that Algorithm 2 (and Algorithm 3 in the Appendix) is a direct application of the classical Online Gradient Descent (OGD) algorithm [1, Chapter 3.1] with the cross-entropy loss. The regret analysis for OGD is somewhat standard. Although the authors have provided some related work discussion, I am unconvinced by the claim "...our framework differs in that we deal with non-stationary OOD data in the context of OOD detection." For the classical online convex optimization framework, the loss function can be arbitrarily different at each round (under certain boundedness assumptions); the framework can already be used for non-stationary data.

- About the Feedback: In the main paper, the algorithm is developed based on the assumption that the labels of the OOD data are available after the learner has made the prediction. This seems like a strong assumption to me since the main challenge of OOD detection lies in the lack of supervision of OOD data. When the labeled OOD data are available, I am confused about what the difference is between the proposed framework and supervised online learning. Although the authors show in the Appendix that one can also use unsupervised loss functions to perform OOD detection, it is unclear how the proposed unsupervised loss is (theoretically) guaranteed to output a well-performing OOD detector, which makes the method less appealing.

- About the Theoretical Analysis: I think the statement of Theorem 3.1 is somewhat informal, as the conditions of the loss functions and parameter settings are not provided. It seems to me that the analysis in the Appendix crucially relies on the convexity of the loss function, and thus, the linear model is applied. However, in the main paper, the algorithm is equipped with a neural network. I think it would be better if the authors could clearly mention the discrepancy between the theory and algorithm implementation.

### Questions
- Could you provide more discussion on the differences between the proposed methods (Algorithms 2 and 3) and the online learning algorithm (e.g., OGD)?
- Could we have certain guarantees for the unsupervised OOD detection loss $\mathcal{L}_t^H$? It seems to me one can also apply similar arguments as Theorem 2 to obtain a regret bound in terms of $\mathcal{L}_t^H$, but it is unclear why minimizing $\mathcal{L}_t^H$ can lead to a well-performed detector that can eventually minimize the true loss function $\mathcal{L}_t$.
- As shown by the equation above (63), it seems to me that the setting of the learning rate $\eta$ requires the knowledge of $T$, $\mathbb{K}^{id}$ and $\mathbb{K}^{ood}$, which are unknown in practice. It would be better if the authors could provide more discussions on how to select the parameters for the algorithm.

### Soundness
3 good

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
This paper considers the problem of online learning with out-of-distribution data. In this setting, the learning model is required to learn with streaming data with OOD data, given whether a data is OOD is known. The proposed method constructs the loss function by combining the ID loss and the OOD loss, and updates the model via online gradient descent. The authors also analyze the static regret of the proposed algorithm. Empirical results show the empirical success of the proposed method.

### Strengths
1. This paper is well organized and easy to follow.

2. The proposed algorithm is simple and easy to implement with many OOD loss and shows empirical success on several benchmark datasets.

### Weaknesses
1. The proposed algorithm requires strong supervision feedback on whether each instance is OOD data in the online learning procedure, which is difficult to satisfy in real-world applications. In this problem setting (whether an instance is OOD data is available), the learning task is then over-simplified. Such a strong supervision assumption makes the proposed method straightforward, which is a simple extension of online learning algorithms with a specific loss function, that is, combine of ID loss and OOD loss in this draft. 
While the authors also offer an unsupervised version that does not require environmental feedback and shows promising empirical results, it lacks solid theoretical guarantees, which limits the applicability of the proposed method.

2. The theoretical results in this work are well established in the online learning literature, which limits the technical contribution of this research. These results are relatively straightforward to obtain when a specific convex loss function is specified. In this draft, it is the combination of the ID loss and the OOD loss. It's also worth noting that the literature typically uses adaptive regret or dynamic regret to capture the non-stationarity of the environment, as opposed to the static regret used in this draft.


3. Regarding the implementation of the algorithm, determining the hyperparameter $\lambda$ for OOD detection before and during the online learning process seems to be challenging. Furthermore, the authors do not elaborate on how $\lambda$ is determined in the experiments or how it affects the algorithm's performance. There is also no published code.

### Questions
How is $\lambda$ in the algorithm determined in the experiments and how does $\lambda$ affect the performance of the algorithm?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
