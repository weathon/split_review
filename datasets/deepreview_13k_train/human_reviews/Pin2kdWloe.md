# Is multitask learning all you need in continual learning?

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Continual Learning solutions often treat multitask learning as an upper-bound of what the learning process can achieve.  
This is a natural assumption, given that this objective directly addresses the catastrophic forgetting problem, which has been a central focus in early works. However, depending on the nature of the distributional shift in the data, the multi-task solution is not always optimal for the broader continual learning problem. In this work, we draw on principles from online learning to formalize the limitations of multitask objectives, especially when viewed through the lens of cumulative loss, which also serves as an indicator of forward transfer.
We provide empirical evidence on when multi-task solutions are suboptimal, and argue that continual learning solutions should not and do not have to adhere to this assumption. Moreover, we argue for the utility of  estimating the distributional drift as the data is being received and show preliminary results of how this could be exploited by a simple replay based method to move beyond the multitask solution.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper challenged a long-standing assumption in continual learning (CL): multi-task learning (MTL) is the upper bound for CL. Authors found that MTL is not always the upper bound for CL especially in highly non-stationary environments or long sequences. To explain their findings, theoretical results showed that the single-task system is more suitable in a volatile environment. Experiments were conducted to confirm the hypotheses and theoretical results in both synthesis and real-world environments.

### Strengths
This paper has several strengths:

- This paper questions a popular but underexplored assumption in CL: is MTL always an upper bound for CL system? The authors show that this is not true in highly complex environments both theoretically and empirically. Answering this question allows us to understand when we should ignore the MTL results in a benchmark and explain why several CL methods yield better results than MTL.

- The authors conducted a comprehensive experiment to verify their hypothesis. The empirical results verify their theoretical results.

### Weaknesses
Despite these strengths, my main concern is about the contribution of this work:

- Several parts of the paper need more clarification for smoother reading and understanding. I struggled during reading Sections 3 and 4 with several notations that were not fully explained. E.g., the $\theta^*$ in Eq.4. Many typos in paragraphs of the main paper such as in line 370. I recommend authors carefully revise the main paper during the rebuttal process.

- Since the DL models are mostly overparameterized, the theoretical results only consider the linear models in a strictly convex setting, limiting the contributions of this work. I wonder what happens if we add the regularization term in the loss function as indicated in the discussion part. Furthermore, the assumption of strict convexity is quite limiting, as many practical loss surfaces are non-convex with saddle points and local minima. The theoretical analysis should address the implications of these non-convexities on the derived results. The analysis could also benefit from a discussion of how the results might change when using different optimization algorithms, such as stochastic gradient descent (SGD) with momentum, which are commonly used in deep learning.

- Although the authors pointed out that there are some cases that the MTL is not as good as ST, I wonder: is there any recommendation, signal, or measure for practitioners to recognize these cases before training and estimate the instability? it would make this work more solid. Specifically, a more rigorous analysis of the conditions under which MTL underperforms ST would be beneficial. This could involve exploring metrics that quantify the degree of non-stationarity or task interference, and how these relate to the performance gap between MTL and ST. It would be beneficial to have a practical guideline or a diagnostic tool that a practitioner could use to assess whether their specific use case is one where ST might outperform MTL.

- Despite in Sec.3 and Sec.4, the authors emphasize that the setting of this paper is online learning. However, in the experiments, authors use h = 3000, 6000,... In my opinion, it resembles the offline continual learning setting when each task is trained for several epochs not a single one like in online continual learning. Is there any explanation for this?

### Questions
See the weaknesses.

### Soundness
3

### Presentation
2

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
This paper studies CL under a new metric borrowed from Online Learning, called dynamic regret. It is shown that under this new metric, matching a multitask learner, which is a common goal in the literature, might be suboptimal with respect to dynamic regret. Specifically, performance of a single task learner is compared  to that of a multi task learner in a linear model to gain insight into when multitask learner is optimal. Empirical analysis supporting the theoretical findings is provided.

### Strengths
This paper is studying a question that is important to the community, and is well motivated. The arguments are laid out mostly clearly and are easy to follow. The experiments are extensive.

### Weaknesses
I think the main caveat of this work is the underlying assumption that the risk of the defined multi task agent, which sequentially trains on tasks starting from the previous solution, converges (with number of steps $h \rightarrow \infty$) to the risk of true multi-task solution which is a minimizer of average risk of tasks seen so far.  Using the notation in equation (2),  the claim is that $\Delta_T^{MT} \rightarrow 0$. This assumption is not explicit, it is mentioned  in line 196, that it holds in convex settings. Looking in the appendix section B.1.2, however, it seems that MT agent defined in the linear convex setting takes gradient steps with respect to an objective that takes into account all tasks simultaneously. So this does not match the description of the MT agent given in line 169, which I think needs to be clarified. 
My understanding is that it is not easy to match the performance of a true multitask learner (that minimizes error on all tasks simultaneously ) while learning continually. 
The empirical analysis section is a little bit hard to follow. It is not always easy to follow which part of the narrative each figure/paragraph supports. Some examples:


 - Table 3 : not sure what to expect by looking at the number of tasks. What is the hypothesis here?
 - Table 1: it seems that $v_{agent}$ is tracking error while $O_{agent}$ is tracking accuracy.

Description of the algorithm Selective Replay is missing from the main text.

line 457: says instability is higher for  PC-16.

### Questions
It would be great if the authors could explain the discrepancy between the linear MT agent and then one that trains continually on one task at a time. 

Suggestions:

- I think moving equation 19 to main text and moving equation 4 would be helpful. Is there a $\Sigma_x$ subscript missing from equation 4?
- Include definition of SR in the main text (I could not find it in the appendix)
- line 457: says instability is higher for  PC-16.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper challenges the assumption that multi-task training is the upper bound for continual learning solutions that learn on a stream of such tasks. They formalize the limitations of multitask objectives and show cases where the multitask optimal solution is different from the continual optimal solution, both with a toy example and with a modified version of a "real-world" dataset.

### Strengths
- The authors propose to challenge an assumption that is often made in continual learning, bringing that topic into discussion. Challenging this assumption is reasonable and needs to be backed up preferably by both simple examples demonstrating why the assumption does not hold in some cases, and empirical results showing that this assumption can also be challenged in real world problems. The paper follows that structure which is good.
- The paper is well written and quite easy to follow.
- Many benchmarks are chosen for empirical evaluation

### Weaknesses
 - **W1**: The toy setting is too simple and does not accurately reflect what could occur in the wild. This setting assumes something similar to a label switch while keeping the same head, which means that for instance an object would have to be recognized as something and then as something else, leading to an impossible solution for the multitask loss (even in the offline learning case this loss could not learn anything but overfit since it would be asked to learn from contradictory signals). I think a better example should show that even if there is a satisfying solution for multitask loss, learning using this loss does not result in an upper bound for the CL method (at least in term of learning efficiency). Specifically, the toy example should demonstrate a scenario where a multitask model, while capable of learning all tasks, does so at a significantly slower rate or with less efficiency than a continual learning approach. This could involve a scenario where the multitask objective creates conflicting gradients that hinder convergence, while a continual learning approach, by focusing on sequential adaptation, can achieve the same performance faster.
- **W2**: As it is right now it is not clear why you split the empirical evaluation in two parts, one part using the CLEAR dataset and MD5 and another part using the CIFAR10 permuted. This needs to be explained more in details why these two parts are needed and what do you want to show in each part. The current structure makes it difficult to understand the specific contribution of each set of experiments. A clearer explanation of the experimental design is needed, detailing the specific hypotheses being tested in each part and how the results from each part contribute to the overall argument of the paper. For example, it is unclear why the CLEAR dataset and MD5 are not sufficient to demonstrate the claims, and what specific insights the CIFAR10 permuted experiments provide that the other experiments do not.
- **W3**: The main weakness of the paper in my opinion is that it is too disconnected from the rest of the online continual learning works. It is true that is online learning most metrics that you present are used and people care more about the rapidity of adaptation rather than the retaining of previous knowledge. But in most online continual learning  works, that is not the case, and metrics such as average accuracy, average anytime accuracy (area under the curve of AA) are used way more. So you need to justify why you focus only on these metrics. So far the only continual learning paper I know that used these is a paper on the CLOC dataset, where it is kind of justified to look at the adaptation metric since the knowledge needs to be "updated" and there is no need to "retain" previous knowledge. But in many of the benchmarks that you present, the retaining of previous knowledge is key to performing on the test set. So it is unfair to present the multitask baseline as "under performing" compared to the CL solution under these metrics that the MT baseline is not suppose to be the upper bound of. **In Short** , I agree that these metrics are important, but more classical metrics should also be reported and the advantage of CL methods (could be CL methods that use infinite memory) on these metrics should also be shown. The paper should include a discussion on how the proposed metrics relate to more established metrics like average accuracy and forgetting, and explain why the chosen metrics are more appropriate for the specific claims being made. This discussion should also address how the results would translate to scenarios where retaining previous knowledge is crucial.
- **W4**: You claim in the paper that most CL methods use the multitask baseline as an upper bound, which I agree on. However, you also claim that most CL methods use the ERM objective. I think this is not entirely true. First of all, when there is no replay it is not the case most of the time. Secondly, even when replay is used, in general it is not used to get a precise estimation of the ERM objective because of the different weightings applied to the memory batch and current batch. Most CL methods would just draw one batch from the current task and one batch from  the memory and sum their loss to get the training loss. This results in giving more weight to the current task data compared to the memory when num_task > 2,  and it results in a different objective than the ERM. I think this part of the story could be tuned down a bit. The paper should acknowledge that many CL methods, especially those using replay, do not strictly implement the ERM objective due to practical constraints like memory limitations and the need to prioritize learning new tasks. This discrepancy between the theoretical ERM objective and the actual training objective of CL methods needs to be addressed more explicitly.

### Questions
- In the CIFAR10 benchmark used for empirical evaluation, you say that you vary the permutation size of the two datasets, but it is not explained what entries are permuted, do you chose a random pixel set to apply the permutation on ?
- I think there is a mistake in Figure 1, caption should say "On the right, ... while on the left, reverse is true"

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper defines "average life long error" as the average error the continual model had on the task it was trained on. Then, the paper compares between single-task and multi-task agents from that perspective, showing that either agent can achieve lower error depending on the specific task sequence. The paper proves that in a convex under-parameterized case, when training the agents on each task for a long enough period of time, the single-task agent actually reach better results. The paper continues with an empirical study, showing similar results in a range of simple toy experiments.

### Strengths
Originality: The paper introduces a novel metric, which allows for original analyses. The analyses give birth to elements like "instability", which can help in giving intuition to the difficulty of task sequences.

Clarity: The paper is written in a clear way, and it is easy to follow the presented ideas. The ideas presented are simple and intuitive, and the motivation behind them is generally clear.

Significance: Studying the reliance of continual learning algorithms on multitasks solutions is interesting and with a value to the community. The paper does make you question this point, which is not often addressed in the literature.

### Weaknesses
Ultimately, continual learning is composed of both *forward transfer* - the ability to perform well on future tasks given past experience - and *backward transfer* - the ability to perform well on previous tasks given the information the network has learned.

In the original manuscript, the claims of the paper seemed to address both of these aspects, suggesting that the multitask objective is fundamentally not well-suited for continual learning. The revised manuscript now makes a clearer distinction and focuses primarily on forward transfer, arguing that the multitask objective is not optimal in this specific regard. The authors demonstrate that there are datasets where an agent optimizing a single task at a time can outperform an agent optimizing all tasks simultaneously.

While this narrower claim is more reasonable, it is also less impactful. Ultimately, the paper primarily shows that having additional out-of-distribution training data can be beneficial or detrimental depending on the degree of similarity between the data distributions. This is a well-known observation in the machine learning community and serves as the underlying rationale for why techniques such as pre-training and training on auxiliary data are effective in practice.

Moreover, I find the paper’s framing within the continual learning domain somewhat unclear. Forward transfer is traditionally the main focus of online learning, where the goal is to improve performance on future tasks. Continual learning, on the other hand, encompasses both forward and backward transfer, aiming to balance the tradeoffs between them. While the authors have added connections to online learning in the new manuscript, the primary framing of the paper remains in the context of continual learning, which feels somewhat misaligned. This focus on forward transfer alone, while valid, seems better suited to the online learning domain, where backward transfer is not a concern.

Additionally, I find that the claims of the paper remain too strong. The results suggest that the multitask solution is not optimal for forward transfer in some cases, but the manuscript appears to extrapolate this to argue that continual learning should move away from multitask solutions entirely. However, as continual learning is inherently a balance between forward and backward transfer, the findings instead seem to highlight the existence of a tradeoff between these objectives - a concept that has already been explored in previous works. Future solutions in continual learning likely need to integrate both multitask objectives and forward transfer considerations rather than abandoning multitask approaches altogether.

A minor but important note: the current manuscript exceeds the 10-page limit and does not conform to the conference template. While I have not changed my score based on this issue,  as I hope this is relatively easy to fix. However, this must be fixed in any future revision.

### Questions
What is the motivation behind ignoring the risk over the previous task in the "average lifelong error"? In which situations would we want models that perform well throughout the entire learning, ignoring the final performance? If the performance on past tasks is forgotten, what intuition can be gained for continual learning, using this measurement?

### Soundness
3

### Presentation
3

### Contribution
1
