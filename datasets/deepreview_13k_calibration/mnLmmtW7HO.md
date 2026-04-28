# Active Learning for Continual Learning: Keeping the Past Alive in the Present

- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 8, 3, 8, 6

## Abstract
*Continual learning (CL)* enables deep neural networks to adapt to ever-changing data distributions. In practice, there may be scenarios where annotation is costly, leading to *active continual learning (ACL)*, which performs *active learning (AL)* for the CL scenarios when reducing the labeling cost by selecting the most informative subset is preferable. However, conventional AL strategies are not suitable for ACL, as they focus solely on learning the new knowledge, leading to *catastrophic forgetting* of previously learned tasks. Therefore, ACL requires a new AL strategy that can balance the prevention of catastrophic forgetting and the ability to quickly learn new tasks. In this paper, we propose **AccuACL**, **Accu**mulated informativeness-based **A**ctive **C**ontinual **L**earning, by achieving an optimal balance between the two required capabilities of ACL, as well as alleviating the scalability issue of Fisher information-based AL. Extensive experiments demonstrate that AccuACL significantly outperforms AL baselines across various CL algorithms, increasing the average accuracy and forgetting by 23.8% and 17.0%, respectively, in average.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses Active Continual Learning (ACL) and particularly the problem of catastrophic forgetting when active learning and continual learning meet. The authors propose propose AccuACL, (Accumulated informativeness-based Active Continual Learning,) which attempts to achieve an optimal balance between learning new knowledge while preserving past knowledge in ACL. They model the accumulated informativeness via the Fisher information matrix,  through the approximation with a small memory buffer, the model parameters, and the unlabeled data pool for the new task. The are theoretical guarantees and extensive experimentation.

### Strengths
The novelty of the method is the application of active learning in continual learning. A technique that is applied in active learning is modified to balance learning and prevention of forgetting in the continual setting domain.

Since the proposed solution has a theoretical basis, this basis can be extended to continual learning. The paper includes a theoretical analysis of space and time complexity and also the Fisher Optimality preserving properties.

The proposed method and the intuition behind it are clearly explained in the paper.

The experimentation evaluates the proposed methods from a number of perspectives.

### Weaknesses
What are the open problems or future directions related to your work? Adding this to the paper would improve the paper's discussion of broader impact and potential future work. This should be additional to the limitations section in the Appendix.

Typos: Please do a grammar check on your paper. There is a typo in the Abstract “informativeness”

### Questions
What are the characteristics of problems where the method works well? Additionally, what are the characteristics of problems where the method does not perform well?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel active learning (AL) approach for active continual learning (ACL) that effectively balances the prevention of catastrophic forgetting with the capacity to quickly learn new tasks. The authors present an accumulated informativeness-based method, termed AccuACL, which extends Fisher information-based AL to a class-incremental setting. By leveraging Fisher information embeddings, AccuACL estimates informativeness through a combination of magnitude and distribution scores, offering a more efficient way to rank data for selection. Experiments across four continual learning (CL) methods on three CL benchmarks show that AccuACL significantly improves CL performance, outperforming traditional AL baselines in terms of both accuracy and forgetting metrics.

### Strengths
- The paper addresses active continual learning (ACL), an underexplored area in the intersections of AL and CL.
- In addition to promising experimental results, the paper provides a solid theoretical foundation for the proposed method, as well as an efficient approximation strategy for computing accumulated informativeness scores.
- The authors include analyses of both time and space complexity, demonstrating the feasibility of implementing AccuACL.

### Weaknesses
 -  Some experiment details like annotation budgets and number of runs are not provided, which are crucial for reproducing the results.
-  Further analysis of the specific data points chosen by each AL method across different CL settings could offer more insight into optimal query selection. Additionally, an examination of annotation budget sensitivity (as many methods peak around round 10 in Figure 2, suggesting diminishing returns) and the effect of task order (since CL can be highly sensitive to task sequencing) would add depth to the findings.

### Questions
1. In the main experiments, it’s intriguing to see ACL methods, especially AccuCL and random, outperform training on the full dataset. What annotation budget is used, and how many runs are conducted in this experiment? Also, why is there no standard deviation for the BAIT rows?
2. Figure 2 shows an interesting trend: accuracy and forgetting metrics peak around AL round 10 and then decline for all AL methods. Could you provide an explanation for this phenomenon?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an active learning method for continual learning that balances the prevention of catastrophic forgetting and the ability to quickly learn new tasks.

### Strengths
Studying active learning in the continual learning setting is interesting.

### Weaknesses
1.  The novelty of the paper is somewhat limited, as the use of the Fisher information matrix and replay mechanisms are already well-known methods in continual learning.

2.  The citations in the related work section are outdated, giving the impression that the authors may not be fully aware of the latest advancements in continual learning, particularly beyond replay and regularization-based methods. Please see the survey [1] and the related work section of [2] and [3].

3.  It would be beneficial to examine how the system and baseline models perform as the number of queries increases.

4.  The baseline methods used in this paper are also outdated. See those in [2] and [3].

5.  The current accuracy results are quite low and significantly fall short of existing state-of-the-art methods.

6.  Given that your method selects only a small number of samples, it would be essential to compare it with recent few-shot continual learning approaches [4], [5], [6], and [7].

7.  Catastrophic forgetting does not seem to be the main problem anymore. Inter-task class discrimination may pose a greater challenge. Please refer to [2] and [3].

8.  The results on the full dataset are notably low too, and it is unclear what method was used in the “full” setting. Please see the papers mentioned above for comparison.

9.     The paper is overly formal and not easy to follow. Some more descriptions of intuitions will be helpful.

10.   The space completely is very high for continual learning.

### Questions
See the previous sections

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper focuses on active continual learning (ACL) and proposes AccuACL (Accumulated Informativeness-based Active Continual Learning) to effectively balance the prevention of catastrophic forgetting and the rapid learning of new tasks. This method proposes the accumulated informativeness modeled by the Fisher information matrix, which is further approximated by the diagonal Fisher information embedding to reduce the calculation cost. Experimental results show that AccuACL outperforms existing active learning baselines across various continual learning algorithms.

### Strengths
1. The motivation is clear and well-justified, aiming to enhance previous methods by addressing both forgetting and rapid learning in subset selection for training.

2. The proposed method is based on the two theorems, making the algorithm be more confident and efficient.

3. Experimental results demonstrate the strength of the proposed method, significantly improving accuracy while reducing forgetting.

4. The paper is well-organized and most components are clear and easy to understand.

### Weaknesses
 **Major**

1. The method employs buffer data to evaluate the current parameter importance with respect to the historical task. However, a small buffer can not adequately represent the complete data distribution of historical tasks, which is easy to overfit. Then the network may memorize these buffer samples and exhibit low parameter sensitivity, leading to an incorrect Fisher information matrix. The reliance on a small buffer introduces a significant risk of the Fisher information matrix being skewed towards the buffer's specific distribution, rather than reflecting the true parameter importance across the entire historical task data. This could lead to suboptimal sample selection, as the method would be prioritizing samples that are important for the buffer, but not necessarily for the broader historical task.

2. The paper focuses solely on the Fisher information matrix of linear classifiers. However, linear classifiers in CL often exhibit task-recency bias, making them prone to favoring new classes [1,2,3]. This raises concerns about the accuracy of the Fisher information matrix calculation. How can an unbiased Fisher information matrix be derived from a biased linear classifier? The use of a linear classifier for Fisher information calculation is concerning, as these classifiers are known to be susceptible to recency bias, potentially leading to an inaccurate representation of parameter importance for older tasks. This bias could result in the model prioritizing samples that are relevant to the most recent tasks, while neglecting the importance of samples from older tasks, thus undermining the goal of continual learning.

3. The description of the greedy algorithm for subset selection is unclear (line 6 in Algorithm 1 requires further explanation). My understanding is as follows:

   a) Randomly sample a subset and calculate the Fisher information embedding according to Theorem 4.2.

   b) Calculate the magnitude score and distribution score of the current subset.

   c) Randomly sample a lot of subsets and repeat steps a) and b). After that, comparing scores across these subsets, and then, selecting the subset with the highest score as the final selection subset $X$.

4. If my understanding is correct, how to guarantee the convergence of the greedy algorithm and ensure that it can choose the optimal subset? Additionally, detailed settings should be provided, such as the subset sampling method, whether subsets intersect, and the size of the subsets. The lack of clarity regarding the greedy algorithm's convergence and optimality is a major concern. Without a guarantee of convergence, the algorithm could potentially get stuck in a local optimum, leading to suboptimal sample selection. Furthermore, the absence of detailed settings for subset sampling, such as whether subsets are disjoint or overlapping, and the specific size of the subsets, makes it difficult to reproduce the results and assess the robustness of the method.

5. Regarding the budget experiment. There is no clear definition of budget and no experiments pointing out the budget limitation.


**Minor**

1. In Table 3 (lines 472-474), how to incorporate historical knowledge into the greedy algorithm? Why use the memory buffer as the initial subset?

### Questions
1. In active learning, why is unlabeled data not utilized in an unsupervised manner to further enhance the training process?

2. In Figure 3, the choice of lambda depends on the amount of unlabeled data. Does this conclusion also hold in imbalanced datasets?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the scenario that performs Active Learning (AL) in the Continual Learning (CL) process. The paper states that previous AL methods only focus on learning new tasks, which leads to catastrophic forgetting. The authors introduce a novel method called **AccuACL** that improves fisher information-based AL to make a balance between learning new tasks while preserving old knowledge. Empirical results show that **AccuACL** outperforms existing AL methods in standard CL metrics. Overall, this paper opens an important problem and propose a reasonable method to mitigate it.

### Strengths
* The problem is important, especially for online deployed models. 
* The extensive experiments partly support paper's claims and the effective of the method. Meanwhile, ablation studies help to understand the proposed method. 
* The paper provides sufficient details and code in Appendix for readers to reproduce the experiments.

### Weaknesses
### Method and theory 
1. The proposed method only works for memory-based continual learning methods. It can not be applied on naive continual learning or regularization-based continual learning methods. I understand that memory buffer is necessary for leveraging existing AL method, but I encourage authors to add this as limitations or propose future directions to handle this issue. 
2. In Figure 1, it seems like **AccuACL** is good for selecting new samples that related to the learned *features*. However, it is not clear what are those features, and Section 4 does not explain this part clearly either. It is crucial to define what constitutes a 'feature' in the context of the Fisher information matrix and how these features are extracted or represented. The paper should clarify if these features are related to specific layers of the network, or if they are a more abstract representation derived from the Fisher information itself. Without a clear definition, the interpretation of Figure 1 and the overall method remains vague.
3. More background for Active Learning is needed for CL community readers.

### Experiment
1. While theoretical space complexity shows **AccuACL** is more efficient than BAIT, no experiment results are support this claim. An additional experiment for memory usage is needed, like Figure 2(c) for time complexity. The theoretical analysis should be complemented with empirical evidence demonstrating the actual memory footprint of the proposed method. This is especially important when comparing against other methods, as theoretical efficiency does not always translate to practical gains. The paper should provide a clear comparison of memory usage, perhaps by measuring the memory required to store the Fisher information matrix and any other auxiliary data structures used by **AccuACL** and BAIT.
2. In Introduction and Section 5.2, authors claims that:
> "these AL strategies typically pay more attention to new features...", "most AL baselines that most AL baselines that focus only on learning new tasks often perform worse the Uniform."

However, these claims are not confirmed by the experiments. Compared with the Uniform strategy, some existing AL baselines have better forgetting score, but worse average accuracy. This phenomenon might indicates that existing AL baselines are not learning new tasks well either. Learning accuracy metric [1] may be able to support paper's claim. If the claim is true, I expect to see existing AL methods might have higher Learning accuracy. But I am not sure what will the final results be. I encourage authors to do quick additional experiments on CIFAR-10 to see their claims is true or not.

### Questions
### Method
1. In Section 4.5, why uses distribution score first and then magnitude score later. Does the order of these two score matters? This is not discussed in Section 5.3 either. 
### Future work
1. Does using regularization-based methods can further improve ACL performance? Maybe the authors can consider this idea to further improve ACL.

### Soundness
3

### Presentation
2

### Contribution
3
