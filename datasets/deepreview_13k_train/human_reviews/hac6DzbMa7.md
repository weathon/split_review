# Continual Learning with Orthogonal Weights and Knowledge Transfer

- Decision: Reject
- Scores: 3, 6, 3, 6

## Abstract
Orthogonal projection has been shown highly effective at overcoming *catastrophic forgetting* (CF) in continual learning (CL). Existing orthogonal projection methods are *all* based on *orthogonal gradients* (OG) between tasks. However, this paper shows theoretically that OG cannot guarantee CF elimination, which is a major limitation of the existing OG-based CL methods. Our theory further shows that only the *weight/parameter-level orthogonality* between tasks can guarantee CF elimination as the final classification is computed based on the network weights/parameters only. Existing OG-based methods also have two other *inherent limitations*, i.e., *over-consumption of network capacity* and *limiting knowledge transfer* (KT) across tasks. KT is also a core objective of CL. This paper then proposes a novel *weight-level orthogonal projection* method (called STIL), which ensures that each task occupies a weight subspace that is orthogonal to those of the other tasks. The method also addresses the two other limitations of the OG-based methods. Extensive evaluations show that the proposed STIL not only overcomes CF better than baselines, but also, perhaps more importantly, performs KT much better than them.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an orthogonal (gradient) projection-based continual learning algorithm to address the over-consumption of network capacity per task and improve knowledge transfer.

In this method, the authors consider a task incremental learning setting to access the task boundaries and compute the weight similarity between tasks.

The proposed method extends gradient projection memory into a gradient update scheme, including the similar task which has positive transfer.

In the experiment, the proposed method STIL shows reasonably new scores in terms of average accuracy, but the backward transfer performance is somewhat limited.

### Strengths
The proposed method aims to address the following issues with orthogonal gradients:

- It cannot guarantee the elimination of catastrophic forgetting
- It limits knowledge transfer among gradient subspaces.

This paper combines gradient projection memory in terms of orthogonal important weight subspace and the log-barrier method of constrained optimization for knowledge transfer.

Through this approach, STIL can achieve better average test accuracy compared to baselines, including gradient projection memory.

### Weaknesses
The main concern I have on this paper is that the author’s claim has not been rigorously proved by theoretically and experimentally. The detailed comments on the above concern are as follows:

- Theorem 1 seems a trivial proposition, which states that the weight vector can be spanned by the graident vectors and the weght subspaces of each task are orthogonal. However, it cannot guarantee to explain the property of catastrophic forgetting in the final logit layer of DNN, which is directly connected to the output prediciton. The orthogonality of the weight vectors in the parameter space does not directly translate to the orthogonality of the activations or gradients in the final logit layer, especially with non-linear activation functions. This is a crucial point because the final logit layer is where the classification decision is made, and forgetting here directly impacts performance.
- The proposed $\mathcal{L}_{sim}$ is based on the constrained optimization, which cannot be applied to the nonconvex domain (most deep learning probelms) directly. In addition, the orthogonality of weight matrix cannot explain the orthogonality of the hidden layers with non-linear activation, so I think the author should provide more empirical evidence why this proposed loss facilitate knowldedge transfer. The log-barrier method used for constrained optimization is typically applied to convex problems, and its application to non-convex deep learning problems lacks theoretical justification. Furthermore, the paper does not provide any analysis or empirical evidence to show that the log-barrier method is effective in this non-convex setting, or why it would be preferable to other regularization techniques.
- The similarity detection based algorithm seems not novel enough to explain the task distribution distance by measuring on the online data stream. The threshold $\theta$ is too heuristic without any empirical explanation. The method for detecting task similarity based on the Wasserstein distance is not sufficiently novel, and the choice of the threshold $\theta$ appears arbitrary without any theoretical or empirical justification. The paper does not provide any analysis of how this threshold affects the performance of the algorithm or how it should be chosen in practice.

I think that this paper is a simple combination of the existing gradient projection memory method and the heuristic similiarity based update rule.

Updating scheme among orthogonal weight subspaces can be a interesting work, but this paper does not theoretically or empirically provides what happens in the non-linear activation layer.

Furthermore, the proposed method should have acheived the best performance in the both metrics, test accuracy and BWT simultaneously if the propsed pipeline succesfully works to handle catastrophic forgetting and knowledge transfer simultaneously.

### Questions
I think that the propsed method shows a reasonable performance in several benchmarks, but it is more important to address the funtamental principle of continual learning with deep neural networks.

As the paper, gradient projection memory, provides the figure of interference activations with several threshold, can the author provide an **empirical materials** what the proposed algorithm does something to prevent catastrophic forgettting and increase knowledge transfer.

The second question is that what is the main difference between gradient projection memory and the OIWS-based til strategy.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a theoretical analysis of the shortcomings of the OG method and proposes that orthogonal weight among tasks can ensure the elimination of catastrophic forgetting. The article introduces a new orthogonal weight projection method for Task-Incremental Learning (TIL) to suppress catastrophic forgetting, referred to as Self-Adaptive Task Incremental Learning (STIL). First, STIL employs a similarity/dissimilarity task detector to assess the similarity between old and new tasks. When it detects that a new task is similar to old tasks, STIL can autonomously perform knowledge transfer. However, in cases where the new task is dissimilar to all old tasks, STIL switches to address catastrophic forgetting.

### Strengths
This article examines the limitations of the orthogonal gradient method and proposes a new approach involving orthogonal weight. Through theoretical analysis, the feasibility of orthogonal weight is confirmed. Additionally, the article introduces adaptive incremental learning, which better facilitates knowledge transfer and mitigates catastrophic forgetting.

### Weaknesses
Some of the formulas lack accompanying figures and textual explanations. Certain formula derivations and images from the supplementary materials are essential and should be incorporated into the main body of the text.

In Eq.(9), two constraint conditions are imposed. It's unclear if convergence can be reliably achieved during the optimization process, or if these constraints will significantly increase the optimization difficulty, potentially leading to optimization failure. The paper should provide a more detailed analysis of the optimization landscape and convergence properties under these constraints.

This paper introduces the method of orthogonal weights to mitigate catastrophic forgetting, but it's not clear why forgetting still occurs, and what the underlying reason for this residual forgetting is. A more thorough discussion of the limitations of the proposed orthogonal weight approach, especially in the context of knowledge transfer, is needed.

Some crucial parts of the appendix should be incorporated into the main body of the text, such as Figure 2. Furthermore, it needs to be appropriately formatted to avoid potential misinterpretation. The current presentation makes it difficult to follow the key ideas without constantly referring to the supplementary material.

The proposed Self-Adaptive Task Incremental Learning (STIL) should be placed before the introduction of weight orthogonality in the paper. The current ordering makes the motivation for the orthogonal weight approach less clear, as the adaptive learning method is the primary contribution.

### Questions
1）In Eq.(9), two constraint conditions are imposed. Can convergence be achieved during the optimization process, or will it increase the optimization difficulty, potentially leading to optimization failure?
2）This paper introduces the method of orthogonal weights to mitigate catastrophic forgetting, but why does forgetting still occur, and what is the underlying reason?
3）Can the method proposed in this paper be applied to Class-Incremental scenarios?
4）Some crucial parts of the appendix should be incorporated into the main body of the text, such as Figure 2. Furthermore, it needs to be appropriately formatted to avoid potential misinterpretation.
5）The proposed Self-Adaptive Task Incremental Learning (STIL) should be placed before the introduction of weight orthogonality in the paper.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposed  weight orthogonal projection for task incremental learning. It provided theoretical analysis of catastrophic forgetting (CF) and knowledge transfer (KT)  and derived the bounds of negative forward and backward KT.  Then,  the authors proposed STIL based on weight orthogonal projection.  STIL introduces orthogonal important weight subspace (OIWS) to avoid CF, which is the key difference compared to prior gradient orthogonal works. To enhance KT, the authors further transfer the shared knowledge among similar prior tasks to the current task, where the task similarity is determined by loss distribution distance replying to data reply. 

The paper presented comprehensive experiments.

### Strengths
This paper studied a very important problem in continual learning, aiming to eliminate catastrophic forgetting.

+ It proposed a solution   to avoid catastrophic forgetting and improve knowledge transfer, respectively. 

+ It conducted comprehensive experiments in various settings and benchmarks, and consistently show better results.

### Weaknesses
It seems there is confusion about some fundamental concepts and there are some pitfalls with the proposed approach. Specifically, for each task, the model lies in some (sub)space. In the literature, the orthogonal projection method is proposed to update the model weights and learn the model for each task accordingly. This paper proposed gradient space, which  does not make much sense. Gradient descent is used to update weights in the model space, so what does gradient space refer to?  The gradient in each step is computed using input data and is stochastic; so would gradient space would be random?

This paper claims the proposed weight orthogonal method can eliminate catastrophic forgetting completely; this is overly ambitious.
For instance, when backward knowledge transfer takes place, it would change the weights for previous tasks. How to ensure the weight orthogonality all the way?

Some more detailed comments:

1. For Theorem 1, it’s not  clear why prior OG-based methods cannot guarantee zero CF.  What if the modified weights spanned by the orthogonal gradient to the previously learned tasks  happen on the whole weight space, instead of its own weight subspace? 
2. The proposed STIL seems complex: It has two steps for learning each new task with four steps to calculate the similarity between tasks.  Thus the memory and time cost need to be justified. For example,  since the proposed STIL adopts GPM method to obtain knowledge bases with additional computation and memory cost (e.g., data replay), why the proposed STIL can have less time and memory compared to GPM for some datasets (e.g., CIFAR100 Sup, 5-dataset as shown in Table 6)?  How do the authors define memory in this work? Does it include both stored bases and replay data? 
3. The experimental results compared to CUBER need to be justified.  As shown in Table.1, compared to CUBER, STIL shows better accuracy but higher forgetting which is inconsistent with the claims. 
4. The proposed method seems only can be used to Task-incremental learning. How about class-incremental learning?

### Questions
Two additional questions regarding the detailed techniques:

1. The definition of f(slashed zero, t): 1) the function f(slashed zero, t) is defined as “when learning t, it does not use the knowledge of any task”. Does the “any task” mean any prior tasks? 2) How do the authors calculate the accuracy of f(slashed zero, t) as shown in Eq(4).
2. When discussing task similarities in Section 4.2, the authors consider top-k (i.e. k = 2) prior tasks. Will the k values affect the performance for different datasets?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work tackles two problems in continual learning: catastrophic forgetting and knowledge transfer. For the first problem, the authors identify that traditional orthogonal gradient based methods cannot fully solve the problem, so they propose to use orthogonal weight space. For the second problem, the authors propose a new loss with constraint to encourage weight similarity for similar tasks. The algorithm achieves good empirical results.

### Strengths
1. The work presents a theoretically grounded analysis of the problem of CF and KT. The authors identify a key advantage of orthogonal weight compared to orthogonal gradients, which is novel.

2. The empirical performance is convincing, where the proposed algorithm consistently outperforms baseline. The ablation study demonstrates the effectiveness of both the CF and KT parts.

### Weaknesses
1. Problem (2) in the introduction section is questionable for OG. It is unclear what are the properties of important weight and important gradients, which the authors do not provide sufficient explanation. Specifically, the notion of 'importance' is not rigorously defined. Are these weights with the largest magnitude, or those that contribute most to the loss function? The authors also do not clearly explain the problem of overconsumption of network capacity, and why the performance drop in Figure 10 comes from this reason. The connection between network capacity and the observed performance degradation is not sufficiently justified. For example, it is not clear how the network's representational capacity is being exhausted, and what specific mechanisms lead to the performance drop.

2. I do not think it is a good practice to organize the paper such that important information such as pseudocode for the main algorithm is deferred to the appendix, especially in section 4 and 5. This problem is severe enough such that the text is very difficult to follow without checking the reference. Key experimental results, such as detailed per-task performance and the specific hyperparameters used, are not shown in the main text. This lack of detail makes it difficult to reproduce the results and assess the robustness of the proposed method. This essentially gains unfair advantage to exceed the page limit.

### Questions
1. In the paragraph following Eq.1, what is the notation “/” mean? What are $W_t/W_{t-1}$ and $t/t-1$?

2. Is there a way to measure how close the weights are orthogonal to each other? The ablation experiments do not indicate whether using OIWS indeed improves the performance by achieving orthogonality.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
