# Adaptive Rentention & Correction for Continual Learning

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Continual learning, also known as lifelong learning or incremental learning, refers to the process by which a model learns from a stream of incoming data over time. A common problem in continual learning is the classification layer's bias towards the most recent task. Traditionally, methods have relied on incorporating data from past tasks during training to mitigate this issue. However, the recent shift in continual learning to memory-free environments has rendered these approaches infeasible. In this study, we propose a solution focused on the testing phase. We first introduce a simple Out-of-Task Detection method, \methodood, designed to accurately identify samples from past tasks during testing. Leveraging \methodood, we then propose: (1) an \textbf{\methodR}~mechanism for dynamically tuning the classifier layer on past task data; (2) an \textbf{\methodC}~mechanism for revising predictions when the model classifies data from previous tasks into classes from the current task. We name our approach \textbf{\methodfull}~(\methodabbrev). While designed for memory-free environments, \methodabbrev~also proves effective in memory-based settings. Extensive experiments show that our proposed method can be plugged in to virtually any existing continual learning approach without requiring any modifications to its training procedure. Specifically, when integrated with state-of-the-art approaches, \methodabbrev~achieves an average performance increase of 2.7\% and 2.6\% on the CIFAR-100 and Imagenet-R datasets, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel approach to class-incremental memory-free continual learning by integrating out-of-distribution detection with model self-correction. Specifically, the authors observe that performance degradation in continual learning largely stems from the classifier head and suggest adapting it on test samples using an entropy minimization loss while refining its predictions through a modified softmax score. Experimental results on Split CIFAR and Split ImageNet-R demonstrate the method's robustness and effectiveness across both replay-based and memory-free continual learning techniques.

### Strengths
The submission offers a comprehensive analysis of the dynamics of catastrophic forgetting, with a focus on recency bias, and proposes a simple and effective method to alleviate it that can be combined with any continual learning method.

The experimental evaluation is rigorous, covering relevant baselines, standard datasets, and appropriate ablations. The new approach demonstrates robustness to method-specific hyperparameter choices and provides a performance boost across continual learning algorithms.

The paper is well-written and structured, with clearly presented arguments, consistent notation, and high-quality figures that effectively convey the main points.

### Weaknesses
The main weakness of the paper is that it makes assumptions about the continual learning setting that are not well justified. Computational constraints are often more critical than memory limitations (see Prabhu et al. 2023, *Computationally Budgeted Continual Learning: What Does Matter* and Roth et al. 2024, *A Practitioner's Guide to Continual Multimodal Pretraining*). A significant limitation of the proposed method is its requirement for additional gradient updates during inference, even if only a single update per sample is needed.

Additionally, performing a hyperparameter search for the adaptive self-retention procedure could lead to overfitting on the test samples.

To improve the evaluation, it would be best to: a) quantify the computational cost of the self-retention procedure and b) ensure hyperparameter tuning is conducted on a separate dataset from the evaluation dataset.

### Questions
Did you run the hyperparameter search for the adaptive self-retention procedure on the same dataset that was used for evaluation?

Have you tried applying your method to other continual learning algorithms, like BEEF, EASE, MEMO, and FOSTER?

In line 88, you formulate the two observations as empirical findings. However, in Section 3.3, they are called assumptions. Do you have any empirical results that show to what extent these actually hold?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors observe that the main issue of forgetting is not in model itself but the classifier layer. Base on such observation, they introduce a way to balance the calssifying layer between current task and previous task. Instead of naively mask the current task output, the authors argue that it is not suitable since the balance between previous class is also imbalance. They come up with a new algorithm to tackle the problem by two assumptions, retention and correction. With the new algorithm ARC, it gain the performance on various datasets and methods.

### Strengths
1. The observation of forgetting majorly happen in classifer sounds reasonable and inspring. The proposed method, ARC, also solve it well. 
2. ARC can be generally applied to different methods is a big advantage that it can plug and play easily with existing countinual learning techniques.

### Weaknesses
1. Need to report the training time during inference, since it might add overhead when deployed to the real-world.

2. What if the incoming sample from the past task is not allow to use during inference? For example, it is deployed to the embbedding device that need real-time inference, will additional training add much overhead? Or is it possible to not update at every step? It will be interesting to provide such results.

3. Can this approach extend to other computer vision task such as detection and segmentation? It would be great if the methods can also fix the problem in such scenario by re-balancing the classifcation head in object detection.

Minor Correction
1. At Table 1, it seems strange that for CodaPrompt, the position of the difference for Split CIFAR-100 Inc5 is oppositve. The difference sign should be 5.8 $\textcolor{red}{(+0.1)}$ instead of 5.7 $\textcolor{green}{(-0.1)}$.

### Questions
1. What if the incoming sample from the past task is not allow to use during inference? For example, it is deployed to the embbedding device that need real-time inference, will additional training add much overhead? Or is it possible to not update at every step? It will be interesting to provide such results.
2. Can this approach extend to other computer vision task such as detection and segmentation? It would be great if the methods can also fix the problem in such scenario by re-balancing the classifcation head in object detection.

Minor Correction
1. At Table 1, it seems strange that for CodaPrompt, the position of the difference for Split CIFAR-100 Inc5 is oppositve. The difference sign should be 5.8 $\textcolor{red}{(+0.1)}$ instead of 5.7 $\textcolor{green}{(-0.1)}$.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of reducing classification bias in class incremental learning (CIL) by utilizing test samples. The authors introduce a novel method called Adaptive Retention & Correction (ARC), which dynamically adjusts classifier layers using test samples confidently identified as belonging to previous tasks. Additionally, ARC corrects test samples that are mistakenly classified as part of the current task.

### Strengths
- **Originality:** The method of adaptively adjusting and correcting model predictions using test sample confidence is novel. 
- **Quality:**  Leveraging confidence scores to detect past task samples and using these pseudo-labeled samples to train the model represents a reasonable strategy for mitigating classification bias in CIL.

### Weaknesses
1. While the motivation to correct misclassified past task samples is sound, the proposed Task-based Softmax Score (TSS) may be problematic. For the earlier tasks, as the temperature $T^{(t−i)}$ increases, the probability distribution flattens, which could hinder the model’s ability to recognize samples from past tasks. Specifically, the temperature scaling, while intended to balance the softmax output, might inadvertently dilute the discriminative power of the classifier for earlier tasks, making it harder to identify samples belonging to those tasks. This could lead to inaccurate pseudo-labeling and negatively impact the overall performance of the method.

2. Although the experiments demonstrate the effectiveness of ARC, the paper lacks comparisons with other test-time adaptation (TTA) benchmarks, such as CoTTA. Additionally, the introduction of extra data for classifier training (referred to as retention) raises concerns about increased training costs that should be addressed. The paper should clarify whether the model, after being adapted by ARC, is used as the starting point for the next task. If so, the cumulative overhead of this adaptation process across all tasks needs to be considered, as it could significantly impact the overall training cost.

3. The paper lacks clarity in several areas, as detailed below:
- 3.1 The description of the experimental setup in Figure 1 is inadequate. For instance, is the class-incremental learning setup applied in this toy example? How are the two types of classifiers trained and tested? Which task’s accuracy is measured in the figure? The figure should clearly specify whether the independent classifier is trained under a task-incremental learning (TIL) setting and the shared classifier under a class-incremental learning (CIL) setting, and how the accuracy is calculated for each.
- 3.2 Does the ARC algorithm run after training each task? If so, what is the additional time required for training and inference? Additionally, should line 9 in the pseudocode be corrected to $w \leq \gamma$?
- 3.3 The scaling temperature used in $S_i$ and the total number of tasks are both denoted as $T$. Are these referring to the same setting?

### Questions
1. The hyperparameters used in the reported results are not fully detailed. Were the same hyperparameters applied across different methods and datasets? It seems that $\beta$ will influence the number of test samples used for training, and there is a trade-off between the number of samples and the accuracy of the pseudo-labels. How were the hyperparameters selected?

2. In the discussion following Assumption 2, the authors state that a low ratio of $c$ and $\hat{c}$ indicates a sample is more likely misclassified as belonging to a past task. However, Figure 5 suggests that a larger corresponds to better performance, which seems contradictory. Could the authors clarify this point?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to reduce the task-recency bias present in the last layer when training in a Continual Learning environment. This well-known problem remains under-explored in the case of memory-free methods and presents additional challenges. In particular, the authors propose to leverage test data in order to adapt the weights of the last layer by differencing old and newer data using prediction confidence. The authors also propose an alternative to the softmax to rebalance the model’s logits, which as often bias toward later tasks. Eventually, this paper shows significant improvement by combining their approach with current state-of-the-art methods.

### Strengths
- The idea of focusing on the debiasing the last layer for later prompt-based memory-free methods is interesting and under-explored
- The intuition behind focusing on test-time adaptation by taking into context the specifics behaviour of continually trained model is good and intuitive
- The method performances are appealing and it seems quite robust to hyper-parameter, which is crucial in Continual Learning where hyper-parameter search is unrealistic
- Most sections are well-written and easy to follow

### Weaknesses
### Major weaknesses
- There is a lack of detail on the overall training procedure. How many epochs are used for training? Is this correction and retention procedure applied after each task? In that case, this would correspond to storing unlabeled memory data.
- I don’t think the formulae in definition 1 is well defined. The inequality under the max does not make much sense as $s(i-1) \leq i \leq s.i$ is impossible in many cases. Also, taking $T>1$ implies that the output of the softmax will be lower (flattened) for earlier tasks (low $i$ values), but I believe the objective is the opposite; the authors want to obtain higher softmax values for earlier tasks. I also do not really understand the usage of a maximum operator here. Overall, this definition is very confusing.
- There is a lack of detail on the overall training procedure. How many epochs are used for training? Is this correction and retention procedure applied after each task? In that case, this would correspond to storing unlabeled memory data.
- This method is connected to Test-Time Adaptation and some discussion in the related work would be appreciated. While TTA methods are rightfully compared in section 4.2, such discussion could be included more thoroughly in the related work.
- The impact of the temperature is not presented in the paper
- The notation for the temperature and the number of tasks is the same, $T$, which is confusing
- in Figure 1, is the independent classifier trained for doing classification of one task only? Then is the problem a TIL problem? If this is the case, the performances are comparing a TIL problem to a CIL problem, which is unfair since the CIL problem is much harder than the TIL problem.
- l. 202 the distribution are defined as different between tasks but in 4.2, the incremental dataset are defined as IID. I believe this is a mistake, can you elaborate?
### Minor weaknesses
- The experiments of figure 3 is quite unclear. It depends on the optimization strategy and the number of epochs for instance. Also, do you use the same fixed learning rate for joint training?
- I believe a confusion matrix would be more clearer than Figure 1 at least, maybe even Figure 1 and 2
- How much data do you use for linear probe?
- I believe the difference in performances in figure 3 between finetune and probe makes sense and justifies the claim that the representation knowledge is still transferable across task.  However, I do not see why the joint training performances are lower in most cases. Could you elaborate?
- the code is not shared
### typos
- The title is spelled wrong.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
