# Convergence and Implicit Bias of Gradient Descent on Continual Linear Classification

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
We study continual learning on multiple linear classification tasks by sequentially running gradient descent (GD) for a fixed budget of iterations per each given task. When all tasks are jointly linearly separable and are presented in a cyclic/random order, we show the directional convergence of the trained linear classifier to the joint (offline) max-margin solution. This is surprising because GD training on a single task is implicitly biased towards the individual max-margin solution for the task, and the direction of the joint max-margin solution can be largely different from these individual solutions. Additionally, when tasks are given in a cyclic order, we present a non-asymptotic analysis on cycle-averaged forgetting, revealing that (1) alignment between tasks is indeed closely tied to catastrophic forgetting and backward knowledge transfer and (2) the amount of forgetting vanishes to zero as the cycle repeats. Lastly, we analyze the case where the tasks are no longer jointly separable and show that the model trained in a cyclic order converges to the unique minimum of the joint loss function.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper considers continual learning setting in which a linear classifier is trained for a fixed number of iterations on tasks (either cyclic or random). In the separable case, the papers shows (directional) convergence to the offline (i.e., combined) max-margin classifier for cyclic and randomised ordering of tasks. In the separable, the paper also characterises (i) forgetting and (ii) backward transfer (for aligned tasks). The paper also shows convergence to overall minimum in the non-separable case.

### Strengths
Clarity : The paper is clearly written.
Soundness : The theorems are stated clearly with proofs.
Originality : Shows results under fixed budget of iterations at every stage. This is an improvement over the Sequential Max-Margin.

### Weaknesses
The main weakness is in the novelty and significance.

1) No experiment with real world dataset.

2) No experiments with realistic synthetic dataset : The paper presents only one experiment on a synthetic dataset with 6 points. Experiments should be detailed in such a way to bring out all the important results.

3) Setting may not be novel: Given that there is an overall linear classifier, the protocols of cycling training or randomised training seem superfluous. To elaborate, we are not in the online learning setting, so we have all the training data of all the tasks apriori. We also know that there is a single linear classifier. So what is wrong if we combine the datasets of all the tasks into one and train using SGD with batches of data (batches either cycled or random) as it is done always?

4) Are batches Tasks? : It is a standard practice to use SGD with batches of data (either cyclic or random). And it is not surprising/novel to know that SGD with batch converges. Is the paper just fancily calling batches as tasks?

5) No Connection to realistic/standard settings : The paper mentions that "cyclic task ordering covers search engines influenced by periodic events. Random task ordering bears resemblance to Autonomous driving in randomly recurring environments". These instances do convey meaning of cyclic, and randomised tasks for a reader who is looking at these the first time. However, the paper has to be specific in terms of specific set of standard datasets and standard real world scenarios.

6) No recommendations for practice : Theoretical results are very important and sometimes can be obtained under even restrictive assumptions. However, the results should also give rise to some recommendation in realistic scenarios. This paper fails in this aspect.

### Questions
Please see the weaknesses.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates how gradient descent (GD) converges to the joint max-margin solution for multiple tasks that are jointly linearly separable. The authors present loss and forgetting bounds under both cyclic and random task presentation orders. Theoretical results are provided for both asymptotic and non-asymptotic settings. Overall, this is a highly novel and interesting paper that offers promising insights for continual learning.

### Strengths
1. Novel analysis of continual learning: The paper contributes to the understanding of continual learning by offering new insights into the convergence behavior of gradient descent on multiple tasks.

2. The presentation is clear and easy to follow.

### Weaknesses
This is a very novel and interesting paper, but I have the following concerns,

1. The logistic loss function and linear model are somehow limited. We usually use large foundation model and cross entropy loss nowadays. So can this theorem be generalized to more practical cases. 

2. No convincing experiments and compared baselines are provided, such as deep learning experiments for continual learning.

### Questions
I have the following questions:
1. Can you provide the intuition about Assumption 3.4 Tight Exponential Tail?

2. Figure 1 present a toy example to help us to understand the motivation, but all the tasks with labels 1. It seems not realistic, so I am curious whether this setting is necessary, can you make it more general.  

3. What is the definition of task similarity in continual learning? Do $N_{p, q}$ and $\bar{N}_{p, q}$ in Theorem 3.4 measure the task similarity? I hope the author can give the clear definition of task similarity. Intuitively, task similarity will affect the forgetting as well as training loss. For example, there are two tasks with significant different optimized directions and a model is trained to learn two tasks, I think it's usually harder than learning two similar tasks, so it probably has larger training loss. So it is reasonable that task similarity would affect the training loss either, do author agree with me?

4. This paper gives a new definition about cycle-averaged forgetting $\mathcal{CF}(J)$, and also show the upper and lower bound of $\mathcal{CF}(J)$ in Theorem 3.4. I think this definition somehow restricts the forgetting measure within the current cycle. The problem is that can you guarantee the model performs better on task $m$ in the current cycle $J$ than before? If not, even if $\mathcal{CF}(J) \rightarrow 0$, we can not say the forgetting performance is good. Is it possible to change the baseline as $\min_j\mathcal{L}_{m}(w_K^{Mj+m})$, which considers the best performance of model on task $m$. Then the cycle-averaged forgetting $\mathcal{CF}(J) = \frac{1}{M}\sum\_{m=1}^{M-1}\mathcal{L}\_{m}(w_0^{MJ+M}) - \mathcal{L}\_{m}(w_K^{Mj+m})$
which is consistent with conventional definition of forgetting.

5. Line 412: $\lim_{t\rightarrow \infty} x_i^T w_k^{(t)}=\infty$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies continual linear classification tasks by sequentially running gradient descent (GD) on the unregularized (logistic) loss for a fixed budget of iterations per each given task. When all tasks are jointly linearly separable and are presented in a cyclic/random order, the full training loss asymptotically converges to zero and the trained linear classifier converges to the joint (offline) max-margin solution (i.e., directional convergence). Additionally, when tasks are given in a cyclic order, non-asymptotic analysis on cycle-averaged forgetting and loss convergence at cycle $J$ are provided, which are $O(\frac{\ln^4J}{J^2})$ and $O(\frac{\ln^2J}{J})$ respectively. Lastly, when the tasks are no longer jointly separable and presented cyclically, a fast non-asymptotic convergence rate of $\tilde{O}(J^{-2})$ towards the global minimum of the joint training loss is established.

### Strengths
1. The paper is easy to follow and clearly demonstrates the contribution of the theoretical results.

2. When all tasks are jointly linearly separable, standard GD without any regularization not only learns every task but also converges to the joint max-margin direction eventually. The implicit bias happens on both cyclic/random task ordering, which is new to my knowledge.

3. When tasks are presented in a cyclic order, non-asymptotic convergence rates are established: $O\left(\frac{\ln^4 J}{J^2}\right)$ if the tasks are jointly linearly separable, and $\tilde{O}(J^{-2})$ if they are not.

### Weaknesses
1. The theoretical framework for continual learning in this paper does not fully align with practical settings in deep learning; for example, tasks are assumed to follow a cyclic order, although this is a common setup in theoretical studies on continual learning. The assumption of a fixed budget of gradient descent iterations per task, while simplifying analysis, also deviates from typical training procedures where convergence is often monitored and training continues until a certain performance threshold is met. This fixed iteration approach might not capture the nuances of real-world continual learning scenarios where tasks may require varying amounts of training.

2. The experimental setup of the paper is quite limited. While the toy example in Figure 1 effectively illustrates the motivation, additional empirical results under more practical continual learning scenarios—or at least beyond the simplest toy example—are necessary to validate the theoretical findings, e.g., the implicit bias phenomenon for both cyclic/random order, cycled average forgetting converges faster than the joint training loss. The lack of experiments on standard benchmark datasets or with more complex models makes it difficult to assess the practical relevance of the theoretical results. Furthermore, the experiments should ideally explore the sensitivity of the results to various hyperparameters, such as the learning rate and the number of iterations per task, to better understand the robustness of the proposed approach.

3. The proofs in the Appendix are involved. Although the remark paragraphs following each theorem provide brief explanations, proof sketches or high-level technical overviews for all of the theoretical results are lacking. Specifically, it is unclear what technical novelties are introduced from a high-level perspective and how the current analysis improves upon [Evron et al. (2023)](https://arxiv.org/pdf/2306.03534). The absence of a clear narrative explaining the proof techniques and their relation to existing methods makes it challenging to appreciate the contribution of the theoretical analysis. The paper would benefit from a more detailed discussion of the key proof ideas and how they overcome the challenges posed by the continual learning setting.

### Questions
1. Could you provide a geometric interpretation or intuition of the theoretical results, just as what [Goldfarb et al. (2024)](https://arxiv.org/pdf/2401.12617), [Evron et al. (2023)](https://arxiv.org/pdf/2306.03534) and [Evron et al. (2022)](https://arxiv.org/pdf/2205.09588) did? 

2. Could you provide proof sketches and a technical overview of the theoretical analysis? In particular, it would be helpful to understand more about the connections and distinctions from prior works, such as [Evron et al. (2023)](https://arxiv.org/pdf/2306.03534) and [Evron et al. (2022)](https://arxiv.org/pdf/2205.09588), as well as what new technical contributions this work presents. Appendix A.1 provides a brief overview and comparisons with [Evron et al. (2023)](https://arxiv.org/pdf/2306.03534), but it lacks an in-depth discussion of the technical and theoretical challenges and contributions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper analyses continual learning in a linear classification setting.  
The analysis focuses on a simple unregularized setting with a fixed number of gradient steps per task (in contrast to a previous paper that studied the regularized setting when learnt to convergence).
Both asymptotic and non-asymptotic results are derived, showing that when task recur cyclically or randomly, the iterates converge to the global offline max-margin solution across all tasks.  
This paper advances the theoretical CL field by clearly showing a different behavior than the one of the weakly regularized case studied in a previous paper.

### Strengths
- **The paper is well written**.
- **The contributions are clear and significant to the theoretical CL field**.  
The main results show the implicit bias of continual linear classification when learned in a practical setup with a fixed number of gradient steps, given that tasks recur in the sequence. Consequently, they show a separation between that setup and a previously-studied weakly-regularized setup which can be considered as less practical.

### Weaknesses
 - **Results are not especially insightful**.  
The previous paper by Evron et al. (ICML 2023) proved a clear projection-like behavior ("SMM") under the weakly-regularized continual linear classification setup. Their results showed an iterative behavior that is somewhat insightful even for "arbitrary" task sequences.   
However, the paper reviewed here proves a behavior that is only informative in the presence of task repetitions.  
(This is not strictly a weakness since it might be the only behavior that one could possibly prove; but still it is only insightful given task recurrence.)

- **The appendices are hard to follow and verify.** Many steps are insufficiently explained (e.g., it's not very clear how Eq. (20) stems from (19); the steps in Eq. (26) are also unclear).  
This prevented me from quickly validating a random subset of the proofs.

### Questions
I have no questions but rather some minor remarks that I suggest that the authors address in their revisioned version. I do not expect an author response on these bullets.

- Line 62: I wouldn't say SMM *"cannot be shown to converge to the offline max-margin solution"*, but rather that it *does not always* converge to that solution (as shown in Figure 1c of Evron et al. 2023). Also, I'm not sure that it should be considered a *"limitation"* of SMM, since this is merely the behavior of the weakly-regularized setup. I wouldn't even say that it's an advantage of the unregularized setup on the weakly-regularized setup, but rather that we see here two different behaviors that can describe continual classification to some extent.
- Figure 1 could be clearer. Maybe a 2d example would be more suitable for a paper? 
- Line 105: the sentence negates the forgetting and the loss but at this point it's still unclear what the difference is.
- Line 112: is "symptotic" a word? That part of the sentence might need to be rephrased.
- Line 143: "be a set of" => "be the set of"?
- Line 212: not sure "generic" is a good choice here.
- Theorems 3.1 & 4.1: 
    - In the second result, *"Every data point is classified correctly"*; perhaps say ".. is **eventually** classified correctly"?
    - The third result seems like an auxiliary result (proposition?) that is not of any practical interest (unlike the first two). I would reconsider its current location in the main results. 
- Figure 2: not very clear. Maybe add a subfigure with the actual 2d parameter space?
- Line 432: do you really need to span the *whole* space? In linear regression we can usually ignore unused directions due to the rotation invariance. Maybe I am missing something, but please reverify this.
- Line 434: strictly or strongly?
- Line 436: *"faster rate"*, faster than what?
- Theorem 5.2: authors should explain the differences from the separable case. And also explicitly explain how the bound on the iterate gap yields a bound on the loss and forgetting.
- Line 506: "implicit bias on" => "of"?
- Line 523 say *"are no solution"* instead of "is".

- Many formulas in the Appendices exceed the page margins (e.g., Pages 19-20).
- Some citations are incomplete or inaccurate. For instance, *"Stochastic gradient descent on separable data: Exact convergence with a fixed learning rate"* was published at AISTATS 2019; and *"Continual Learning with Tiny Episodic Memories"* was published at ICML 2019.

- Line 806-809: Evron et al. (2023) already showed it (see their aforementioned Figure 1c).
- Line 828: might need rephrasing.
- Line 831 say *"contrained"*.

- Line 918: *"proposed by indicates"*, rephrase?
- Line 1152: Missing whitespace.
- Equations (74,75): It's not common to use the $O(\cdot)$ notation for negative quantities. I think the authors need instead $\log(t)-\log(t-1)=O(t^{-1})$.

### Soundness
3

### Presentation
4

### Contribution
3
