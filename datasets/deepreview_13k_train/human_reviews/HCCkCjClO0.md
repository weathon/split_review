# Online Weight Approximation for Continual Learning

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Continual Learning primarily focuses on studying learning scenarios that challenge a learner’s capacity to adapt to new problems, while reducing the loss of previously acquired knowledge. This work addresses challenges arising when training a deep neural network across numerous tasks. We propose an Online Weight Approximation scheme to model the dynamics of the weights of such a model across different tasks. We show that this represents a viable approach for tackling the problem of catastrophic forgetting both in domain-incremental and class-incremental learning problems, provided that the task identities can be estimated. Empirical experiments under several configurations demonstrate the effectiveness and superiority of this approach also when compared with a powerful replay strategy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a continual learning scheme named Online Weight Approximation (OWA) motivated by the theory of online function approximation. The proposed method models the dynamics of the weights in deep neural networks and aims to alleviate catastrophic forgetting in task-incremental learning scenario. It is evaluated on multiple continual learning datasets and compared with a replay strategy, demonstrating its negligible loss of performance.

### Strengths
1) The proposed method focuses on the capacity problem of continual learning, which is a core and meaningful side in the long view of CL research. Their approach tries to fix the model capacity by sampling weights rather than storing it, which is creatively motivated from function approximation.
2) The method is based on a solid theory from computational mathematics. The paper also provides certain rigorous theorems for their method.

### Weaknesses
1. The experiment lacks diversity. The authors made the same experiment repeatedly on different datasets, which resulted in similar conclusions. 
2. The datasets benchmarked by their experiment are relatively simple.
3. The experiment compared with too few and simple baselines, in which “Vanilla”is literally not a continual learning method.

### Questions
1.  It is  mentioned in the paper that memory budget in your method is constant. Could you explain that? Particularly, I wonder the number of Euler steps $S$  in the coefficients $\tilde{C}_i^S$ was fixed or not. If not, how does it evolve properly, without proportional increasing?
2. Which replay method did you compare with specifically? Replay methods have had a long history since the emergence of continual learning research, and their performances varied quite a lot. But the performance in your experiment is not so good, which is hard to believe as a state-of-the-art. It would be valuable to discuss how OWA compares to other methods.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an "online weight approximation" scheme to enable continual learning in challenging domain incremental and class incremental learning setups.

### Strengths
1. The paper is well written, and the problem setup is mostly clear.
2. Mentioned problem setups are challenging and interesting.

### Weaknesses
My main concern is the scalability of the proposed method and also the limited empirical evaluations.

1. The proposed uses $O(n^{2})$ training time for each parameter of the model, which seems quite large, considering the number of parameters present in a typical deep neural network. Therefore, I believe it is necessary to compare the time required to train the proposed method with the other baselines. The authors should provide a detailed analysis of the computational complexity, including both time and memory requirements, and compare these against the baselines. A theoretical analysis of the computational cost of updating the approximation coefficients, as well as empirical measurements of training time, would be beneficial.

2. Empirical evaluation does not include large deep neural networks. For CIFAR10 experiment, authors have used ResNet-10, however, it is not that deep. I suggest the authors to use deeper neural networks, like ResNet-34/50, Vgg-16/19, WideResNet. The current experiments do not adequately demonstrate the scalability of the proposed method to more complex architectures. The performance of the method should be evaluated on networks with a significantly larger number of parameters to assess its practical applicability.

3. Additionally, the datasets used for empirical evaluation is not large scale dataset. I suggest the authors to experiment with ImageNet-1k. If it is not possible due to limited resources, then try to evaluate on ImageNet-100. The evaluation should include more challenging datasets to fully demonstrate the effectiveness of the proposed approach. The current datasets are not sufficient to assess the method's ability to handle complex, real-world scenarios. Experiments on larger datasets with more classes and greater data variability are needed.

4. I also think that it is not fair to reduce the number of replay samples of a rehearsal based methods such as Experience Replay, as you are model (parameters) is using very limited memory. This type of comparison is unfair to a rehearsal based methods. In that case, I would suggest the authors to not to use any memory at all and simply compare with regularization based methods such as EWC[1], MAS[2] etc.

5. Finally, this paper does not compare with recent continual learning baselines, EWC[1], MAS[2], GDumb [3], REMIND[4], DER++[5], CLS-ER[6]. The paper should include comparisons with a broader range of state-of-the-art continual learning methods to better contextualize the performance of the proposed approach. This is crucial for understanding the relative strengths and weaknesses of the method compared to existing techniques.

### Questions
Refer to the weakness section.

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
The paper presents a method based on online weight approximation for task-incremental learning.

### Strengths
The proposed method is new, but I believe it is weaker than some existing methods.

### Weaknesses
The paper presents a method based on online weight approximation for task-incremental learning.

 2 fair

 2 fair

 2 fair

The proposed method is new, but I believe it is weaker than some existing methods.

As stated in the paper, “in this work we concentrate on scenarios where at test time the identifier of the distribution from which the sample was collected is predetermined or known in advance.” You are in effect solving the task-incremental learning (TIL) problem. Many TIL techniques can already achieve forgetting-free. Your method is also weaker than some existing methods. So, the value of your method is limited. Please check out the following,

(1) Serra et al. Overcoming catastrophic forgetting with hard attention to the task. ICML-2018.
(2) Wortsman et al. Supermasks in superposition. NeurIPS-2020. 
(3) Ke, et al. Achieving Forgetting Prevention and Knowledge Transfer in Continual Learning. NeurIPS-2021. 
(4) Lin et al. Trgp: Trust region gradient projection for continual learning, ICLR-2022
(5) Lin et al. Beyond not-forgetting: Continual learning with backward knowledge transfer. NeurIP-2022. 

The paper seriously lacks citations and discussion of and experimental comparisons with related literature. The systems in the above references and (6) below should be compared. 

In the later part of the paper, you stated, “Throughout this paper we will assume the more definite scenario of task incremental learning.” But in the abstract and introduction, you said domain-incremental learning and class-incremental learning. 

Your first set of experiments (section 4.1) should have some knowledge transfer. References (3), (4) and (5) can transfer knowledge across tasks. Your method by nature cannot perform knowledge transfer. 

In your second set of experiments (section 4.2), you claimed that you are doing class-incremental learning, but since you have no task identification prediction, you are doing TIL. Your evaluation metric is average incremental accuracy, and the results are weak. Please see reference (6) below, which gives the last accuracy after all tasks are trained. The last accuracy should be much lower than average incremental accuracy. A principled way for task identification prediction is also offered in (6).

(6). Kim et al. A theoretical study on solving continual learning. NeurIPS-2022

What data is used to train eq 7? It isn’t described explicitly in the paper. My understanding is that it is just the data of each task. Then, your method is very similar to SupSup (2). The size of C^j for each task j is potentially the full network size. 

Is w^i represents the set of weights for task i?

What is N is eq 3? I am unfamiliar with the order of approximation. 

Why do you use ResNet10 for some datasets and ResNet18 for some other datasets?

### Questions
The questions are included in the weakness section.

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
This paper presents Online Weight Approximation (OWA) to address the forgetting in continual learning. Specifically, OWA tries to model the dynamics of the weights across the learned task sequence to mitigate the forgetting issue. Experiments on several datasets and baselines show the effectiveness of the proposed method.

### Strengths
This paper proposes  Online Weight Approximation (OWA)  to mitigate forgetting in continual learning.

### Weaknesses
 * The paper writing needs to be further improved. In the abstract section, this section should clearly state what specific problem you are trying to address. For example, the authors state that they are trying to address catastrophic forgetting. The forgetting issue is extensively studied in existing works. The abstract should state what are the limitations that exist in CL literature. Then, this paper should state how their proposed method addresses this specific problem.  Second, the motivation of introducing Online Weight Approximation (OWA) to continual learning is unclear. After reading the paper, it is unclear how OWA addresses the forgetting issue. Third, in the related work section, not only related works should be presented, but also their limitations and relation of the proposed OWA with existing methods should be clearly presented. Lastly, the method description should be clearly connected with continual learning.


* Lack of insight into how the proposed OWA mitigates forgetting. It would be better to provide more insights and illustrations of OWA and the connection with catastrophic forgetting.


* It is unclear the advantage of the proposed method compared to other related methods. In the introduction and the method sections, the paper should state the advantages of the proposed method compared to others. This would make the positions of the paper more clear.   


* The compared baselines are too weak. OWA is only compared to a simple replay method. More recent memory-replay methods should be compared. For example, [1, 2] should be compared.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
