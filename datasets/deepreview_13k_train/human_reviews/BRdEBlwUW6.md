# DAFA: Distance-Aware Fair Adversarial Training

- Decision: Accept
- Scores: 5, 6, 8, 6

## Abstract
The disparity in accuracy between classes in standard training is amplified during adversarial training, a phenomenon termed the robust fairness problem. Existing methodologies aimed to enhance robust fairness by sacrificing the model's performance on easier classes in order to improve its performance on harder ones. However, we observe that under adversarial attacks, the majority of the model's predictions for samples from the worst class are biased towards classes similar to the worst class, rather than towards the easy classes. Through theoretical and empirical analysis, we demonstrate that robust fairness deteriorates as the distance between classes decreases. Motivated by these insights, we introduce the Distance-Aware Fair Adversarial training (DAFA) methodology, which addresses robust fairness by taking into account the similarities between classes. Specifically, our method assigns distinct loss weights and adversarial margins to each class and adjusts them to encourage a trade-off in robustness among similar classes. Experimental results across various datasets demonstrate that our method not only maintains average robust accuracy but also significantly improves the worst robust accuracy, indicating a marked improvement in robust fairness compared to existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the author introduced a class-distanced method aimed at enhancing fairness in Adversarial Training. To be more specific, the methods designs the robust sample loss weights and adversarial margins based on the class similarities to penalize more for hard similar classes. The author argue that the error of hard samples are mainly caused by falsely predicted as other similar classes, rather than disimilar classes. To verify this, the author first show that for the hard class, the accuracy is much improved dramatically if it trained with classes that not similar to it. Then the author derive theoretical analysis quantitively shows that the robust errors for each class, and predict error between different classes is monotonically decreasingly correlated with the gap between different classes. The large the class gap, the smaller the predictions error. Further more,  in section 4.1, the author present "an example illustrating that improving
a hard class’s performance is more effectively achieved by moving the decision boundary (DB)
between the hard class and its neighboring class than that between the hard class and a distant class". Then empirical studies on several datasets verifies the effectiveness of the proposed methods.

### Strengths
Please refer the summary.
Moreover, the method proposed by the author is agnostic and is empirically validated by combining it with Trades framework and an PGD to demonstrate its advantages.

### Weaknesses
 The paper is well written. But

 1) It rambling too much until the Page 6.

2) The author only mentioned  once that  it used class prediction probability to measure the class similarities. "Our proposed method quantifies the similarity between classes in a dataset by utilizing the model output prediction probability. " When it comes to class similarity, the first idea that came to my mind is embedding similarities between different classes. It is confusing.

### Questions
1) What's the "red" and "blue" arrows in Figure 1 represents?
2) Are all the figures when it comes to measure the class similarities using the average class soft max probabilities you described in section 4.2 when you proposing your methods?
3) Please proofread the paper and simplify the sentences for better comprehension such as "Allocating a larger adversarial margin to the hard class than to adjacent classes has the effect of pushing the DB away from the hard class’s center by an amount corresponding to the difference in their adversarial margins."

### Soundness
2 fair

### Presentation
2 fair

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
This paper focuses on the robust fairness problem, they empirically find that  the majority of the model’s predictions for samples from the worst class are biased towards classes similar to the worst class. Inspired by this, they show a theoretical result that a class is hard to learn and exhibits lower performance when it is close to other classes. They then propose a novel method, it use class-wise probability to measure the difficulty of the class. Based on this, they computing the weights which is used to reweight the loss and adjust the margin. Empirically, they show the proposed method outperforms other baselines in three different datasets.

### Strengths
1. The authors use experiments to show that the misclassified samples from worst class are biased towards classes similar to the worst class, and they provide a theoretical analysis on this.
2. They propose a novel method, adjusting the weights and margins based on the class-wise probability, which is used to measure the difficulty of the class.
3. The authors show experiments on three widely used datasets to show the superiority of the proposed method.

### Weaknesses
1. The update rule for $\mathcal{W}$ may result in negative values in some cases. For instance, when the performance of a class consistently remains the best, this issue arises. The authors do not address this problem or discuss its implications. If $\mathcal{W}$ becomes negative, it would lead to negative robust radii ($\mathcal{W}_y\epsilon$), which is unreasonable.
2. The update process for $\mathcal{W}$ appears to be time-inefficient, particularly when dealing with datasets that contain a large number of classes. It is suggested that the authors provide information on the time costs of the proposed method compared to other baselines.

### Questions
1. What is the theoretical and empirical range of $\mathcal{W}$? A clarification of the possible values for $\mathcal{W}$ is necessary.
2. Does the proposed method require more time for experimentation compared to other baselines? 
3. What distinguishes the proposed method from other baselines, considering that these methods also adjust weights? Can the authors elaborate on the differences in the weight curves between the proposed method and the baselines?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to mitigate the class-wise fairness issue in adversarial training (AT) by proposing a DAFA framework, which first theoretically and empirically investigates the impact of the distance between classes on worst-class robustness and then proposes dynamically adjusting the weights and margins deployed in AT for better robust fairness.

### Strengths
1. The motivation of this paper is clear. Figure 1-3 illustrates what similar and dissimilar classes are and how they affect class-wise performance.
2. The claims of the influence of class-wise distance on their robustness are supported by both theoretical analysis and empirical verification.
3. This paper further refines the state-of-the-art understanding of class-wise accuracy and robustness. As CFA [4] shows, different classes should use specific training configurations in AT to strengthen class-wise performance, the proposed DAFA further takes the interaction of classes into consideration and highlights the role of similarity between classes.

### Weaknesses
1. My major concern with this work is the unfair comparison with baselines in terms of experiment settings. Here, I take CFA [4] as an example, and please also check other baselines.
    - CFA includes a Fairness-Aware Weight-Average (FAWA) strategy to mitigate the fluctuating effect of worst-class robustness. Weight average requires more epochs to converge after learning rate decay, and in the original paper of CFA, the learning rate decays at the 100th and 150th epoch in a 200-epoch training. Therefore, the learning rate schedule in your setting significantly decreases the performance of CFA.
    
    I suggest using the original settings of different baselines to ensure fair comparisons. I will change my rating based on how this issue is addressed.
    
2. Page 1. The research thread of the robust fairness problem seems to be confusing. Based on my expertise in robust fairness research, the main thread [1-5] on this problem focuses more on how to adjust objective functions and configurations in AT, and the long-tailed classification is a minor perspective. I suggest revising the introduction of this paper by focusing on more related work [1-5].
3. Page 4. Some of the Theorems seem to be very close to previous work [1, 3]. I suggest clarifying which theorems are a re-deduction of previous results and which are proposed new ones.
4. There may be a mismatch between the motivation and the proposed method. It seems that the schedule in equation (6)-(9) still pays more attention to easy or hard, though class-wise similarity is involved. I suggest adding theoretical analysis on how these configurations improve class-wise robustness.

### Questions
1. Page 5, Section 3. Why is class-wise distance defined as the average distance of a class to other classes? In my opinion, for classification tasks, the distance between a class and its closest one plays the most important role in determining the decision boundary, and the influences of classes that are far away are negligible.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This research addresses the "robust fairness problem" in adversarial training, where there's a significant difference in model accuracy between classes. Current methods sacrifice performance on easier classes to improve harder ones. However, the study observes that the model's predictions for the worst class often favor similar classes instead of the easy ones under adversarial attacks. As the distance between classes decreases, robust fairness deteriorates. To mitigate this, the Distance-Aware Fair Adversarial training (DAFA) approach is introduced. It assigns distinct loss weights and adversarial margins to each class and adjusts them to balance robustness among similar classes. Experiments show that DAFA not only maintains average robust accuracy but also significantly enhances fairness, especially for the worst-performing class, compared to existing methods.

### Strengths
1. The paper is easy to follow

2. The motivation is clear

### Weaknesses
1. Experiments on the sensitivity of trade-off hyperparameter $\beta$ is missing. 

2. The experiments only based on TRADES are very limited.

3.  Several baselines are missing. For example, Group-DRO [1]

### Questions
See Weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
