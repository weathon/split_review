# Divide and Orthogonalize: Efficient Continual Learning with Local Model Space Projection

- Decision: Reject
- Scores: 5, 8, 6, 5

## Abstract
Continual learning (CL) attracts more and more research interests recently since it enables a learning model's ability to continuously learn new tasks without forgetting the previously learned knowledge. However, existing CL methods require either an extensive amount of resources for computing gradient projections or memorizing lots of old tasks as the candidates for related old tasks selection. Thus, a low-complexity CL approach is necessary for the model deployment on huge data. In this paper, we propose a local model space projection (LMSP) based efficient continual learning framework, which helps to not only reduce the complexity of computation, but also extend to several local model tasks to increase the candidate pool with strong correlations. We also theoretically show that the proposed LMSP approach enables backward knowledge transfer, which is a highly desirable feature in CL. Extensive experiments on several public datasets demonstrate the efficiency of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies an interesting topic, continual learning, which aims to learn a series of tasks without forgetting. . The existing CL methods require either an extensive amount of resources for computing gradient projections or storing a large number of old tasks’ data.  . In this paper, a local model space projection
(LMSP) is proposed to not only significantly reduce the complexity of computation, but also enables forward and backwardknowledge transfer. Extensive experiments on several public datasets demonstrate the efficiency of our approach.

### Strengths
1. This paper is well-written.
2. The research topic is very interesting.

### Weaknesses
1. Performing the forward and backward knowledge transfer has been done in the existing works.
2. The proposed approach relies on the task information, which can not be used in task-free continual learning.
3. The proposed approach does not always achieve the best performance in some datasets.
4. Although the proposed approach can reduce computational costs but would increase more parameters.

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposes Local Model Space Projection, a method in continual learning that aims at avoiding forgetting and encourage knowledge transfer by performing orthogonal updates of parameters over the sequence of tasks. The method considers three regimes: 1) forgetting avoidance, 2) forward transfer, 3) backward transfer, which can be represented as variants of the problem of finding orthogonal directions for parameter updates. The method constructs local model spaces of each task by selecting some anchoring points from the task's representation. Using these representations, a similarity between tasks can be measured across local representations to determine whether the task has local sufficient projection, local positive correlation or local relative orthogonality. Theoretical analyses along with experimental results are provided. Experiments are reported for 4 benchmark datasets, and compared to a range of SOTA continual learning methods from different families (regularization, replay, orthogonalization). Results are provided in terms of accuracy and backward transfer.

### Strengths
- The paper proposes an original method that exploits the idea of orthogonal projections to learn new tasks whilst controlling forgetting and encouraging forward and backward transfer. The consideration of particular regimes for each of these problems, and the fact that each of these regimes can be addressed with the same underlying idea of projections that consider local representations of tasks seems novel and useful. 
- The paper is very clear, easy to follow and mostly complete as it considers both theoretical and experimental demonstrations of how and why it works. 
- The paper is somewhat significant in the sense that it seemingly not only tackles forgetting but also knowledge transfer, and it presents some good results in both accuracy and backward transfer.

### Weaknesses
 - Although the proposed method seems quite competitive in terms of experimental results, there is no report on the performance of forward transfer. This is extremely relevant as forward and backward transfer are usually in trade-off (the more forward, the less backward transfer and vice-versa). How can you guarantee that the good results in backward transfer do not require sacrificing forward transfer, or even just the fact of learning the new task reasonably well?


### Questions
- Can you provide actual performance numbers for forward transfer?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Based on the basic framework of orthogonal-projection-based CL methods, this article proposes a local model space projection (LMSP) based efficient continual learning framework to help reduce the complexity of computation. The authors provide a theoretical analysis of backward knowledge transfer. Experiments based on multiple datasets demonstrate the effectiveness of the method.

### Strengths
- The paper is well-structured with clear writing.
- Leveraging the problem definition from previous research, this study presents a novel local model space projection approach, optimizing continual learning.
- The authors also provide a theoretical analysis of the convergence.

### Weaknesses
 - The problem definition, framework, and convergence analysis of this work are derived from existing work. While the efficiency approach is intuitive and easy to understand, its novelty causes me concern.
- The authors use local low-rank matrices defined by anchor points to approximate each layer parameter matrix. However, the accuracy of this approximation, and in particular how it is affected by m, is not discussed. Moreover, the proposed framework and analysis also ignore this issue. 
- The author introduces LLRA to improve computational efficiency. However, they do not perform experiments to evaluate the computational complexity and specifically do not show the saved wall-clock time compared with the LRA method.

### Questions
- The author states that there is no significant difference between the two methods in selecting anchor points. Can you give some intuitive explanation?
- Is there some relationship between ranking and the number of anchors?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper improves the efficiency of SVD decomposition in gradient-projection-based continual learning method. They introduce local model space projection (LMSP) to improve the running efficiency of SVD decomposition. At the same time, LMSP can facilitate both forward and backward transfer of gradient-projection-based methods in continual learning. The authors also provide some theoretical analysis of LMSP. Experiments on several datasets evaluate the effectiveness of the proposed method.

### Strengths
This paper introduces local model space projection to GPM to improve its running efficiency.

### Weaknesses
 * This paper writing needs to be further improved.  It would be better to directly state the intuitive idea and its illustration. This would make the main idea clearer and easier to understand. 


* The authors argue that SVD decomposition is computationally costly. This is true but it seems not an important problem in GPM since SVD decomposition only happens after finishing training each task, not every iteration. Therefore, the computation cost of SVD decomposition is minor compared to the overall training cost. 


* The authors state that their method could reduce the complexity of SVD basis computation, but there is no empirical evaluation of the overall training efficiency improvement with the proposed method compared to the GPM itself. 


* From the empirical results, LMSP improves the backward transfer, but the overall accuracy drops in some cases. The paper states that LMSP can improve both the forward and backward transfer, which does not support the claim.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
