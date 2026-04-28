# SoftSignSGD(S3): An Enhanced Optimize for Practical DNN Training and Loss Spikes Minimization Beyond Adam

- Decision: Reject
- Avg Score: 6.20
- Scores: 8, 6, 6, 5, 6

## Abstract
Adam has been widely successful in training deep neural networks (DNNs), yet the factors contributing to both its practical effectiveness and ineffectiveness remain largely underexplored. In this study, we  reveal that the effectiveness of Adam in training complicated DNNs stems primarily from its similarity to SignSGD in managing significant gradient variations, while we also theoretically and empirically uncover that Adam is  susceptible to loss spikes  due to potential excessively large updates. Building on these insights, we propose a novel optimizer,  SignSoftSGD (S3), which incorporates a generalized sign-like formulation with a flexible $p$-th order ($p\ge 1$) momentum in the denominator of the update, replacing the fixed $2$-order momentum. We also integrate the memory-efficient Nesterov's accelerated gradient technique into S3, enhancing convergence speed without additional memory overhead. To minimize the risk of loss spikes, we utilize the same coefficient for the momentums in both the numerator and the denominator of the update, which also practically streamlines the tuning overhead.  We conduct a theoretical analysis of S3 on a general nonconvex stochastic problem, demonstrating that  S3 achieves the optimal convergence rate under weak assumptions. Extensive experimentation across various vision and language tasks demonstrates that  S3 not only achieves rapid  convergence and improved  performance but also  rarely encounters loss spikes even at a \textbf{${10\times}$} larger learning rate. Specifically, S3 delivers performance comparable to or better than AdamW}with ${2\times}$ the training steps.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Authors present SoftSignSGD (S3), an optimizer designed to address the problem of Adam optimizer, which may cause loss spikes. S3 uses a p-order momentum which resembles the behavior of SignSGD. Authors provide strong results on ResNet/ViT on ImageNet and OpenWebText on GPT-2.

### Strengths
1. The visualization in figure 2 is insightful where authors build a connection between mean update and train loss spikes.
2. The paper is nicely motivated.
3. Experiments are solid and results are strong.
4. Loss spikes in LLM training is a long-standing problem, and this possible explanation and solution should be immediately useful for the academic community.

### Weaknesses
See questions

### Questions
1. If p is not equal to 1, how will the wall clock time per iteration change? (compared to Adam and S3 p=1)
2. How is the learning rate for different optimizers determined? Are they properly tuned for baselines?
3. Will tuning betas for Adam (and getting a smoother loss curve) close the gap between Adam and S3?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper reveals that the effectiveness of Adam in training complicated DNNs stems primarily from its similarity to SignSGD in managing significant gradient variations. The authors theoretically and empirically demonstrate that Adam is the underlying factor causing loss spikes in training large models (i.e., LLM) due to its potential to lead some parameter updates to be excessively large. Meanwhile, the authors introduce a novel optimizer, named SoftSignSGD (S3), which offers multiple distinct advantages over Adam. Finally, this paper provide theoretical analysis and extensive experiments to evaluate S3.

### Strengths
1) The paper proposes a novel optimizer, SignSoftSGD (S3), which gives smaller training loss and better test performance, and this is validated by a wide range of experiments.

2) This paper provide theoretical analysis for S3 on a general nonconvex stochastic problem and demonstrate that S3 achieves the optimal convergence rate under some assumption. This gives more evidence on the superior of the S3 optimizer.

### Weaknesses
It would be better if more experimental results are provided.

### Questions
1) Is the S3 optimizer sensitive to some parameters, such as the learning rate? 
2) Is there any drawbacks of the S3 optimizer?

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
This paper investigates Adam's strengths and limitations, revealing that its success stems from a sign-like approach rather than second-order optimization. To address Adam's susceptibility to loss spikes, the authors propose SignSoftSGD (S3), an optimizer with a flexible momentum term and integrated Nesterov acceleration. S3 enhances training stability, reduces tuning needs, and shows superior performance across tasks with faster convergence and greater stability, even at larger learning rates. The authors' theoretical insights and practical results suggest that S3 could be especially beneficial in large language model training.

### Strengths
1. The paper is clearly written and easy to follow.
2. The issue of loss spikes in LLMs is a very interesting question and warrants further investigation.
3. The paper provides valuable theoretical insights into the convergence of the S3 algorithm.
4. The paper includes a detailed empirical investigation, including experiments and an ablation study.

### Weaknesses
1. The paper "On the Variance of the Adaptive Learning Rate and Beyond" suggests that the variance in adaptive learning rates could be the reason that causes training instability in the initial stages, which I believe is highly correlated to the authors' insights in this work. Could the authors discuss this connection and, if possible, provide demonstrations to highlight how the variance of adaptive learning rates changes when using S3? Such an analysis would strengthen the understanding of why training instability happens.

2. The authors argue that large m/sqrt(v) values may lead to the emergence of loss spikes, which I agree. Could the authors consider manually setting a large m/sqrt(v) in specific coordinates to intentionally trigger a loss spike? This would provide compelling evidence to support the claim and enhance the understanding of the mechanism behind these spikes.

3. The authors claim that "S3 employs the same exponential moving average coefficient β for both mt and rt, offering the advantages of minimizing the risk of loss spikes and reducing tuning work. In theory, as demonstrated in Theorem 2, the same β guarantees that the largest value of each coordinate of the update bjtn(tpj) is minimized to 1." However, I am not convinced that reducing one hyperparameter is inherently advantageous. In fact, we could also control the bound by carefully setting a relationship between beta_1 and beta_2 in Adam. Keeping one more parameter could give on more freedom of tuning, allowing to control the decay speed of higher-order gradient statistics.

4. Adaptive optimizers like Adam often require stable gradient accumulation in the early stages of training, and warmup techniques are commonly used to facilitate this stability. However, it seems that the authors have not mentioned using a warmup technique. Considering the loss spikes are often occurred at the beginning of training, could the authors clarify the specific cases in which they applied or chose not to apply warmup? 

5. Some typos: line 205 "a excessive" -> "an excessive", line 231 "the study itself the study itself" -> "the study itself", Line 335 "Algorithm 4" -> "Theorem 4". Additionally, some aspects of the typesetting are inappropriate and need improvement, such as Line 344 - Line 345. The related work section should be in the main text.

6. It would be helpful if the authors could release the code.

### Questions
See Weakness

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
This paper is motivated by observations (as seen in previous works too) that the effectiveness of Adam for deep learning tasks is its SignSGD-like property rather than its dimension-wise adaptivity, and also, that the Adam's training instability and loss spikes can be attributed to overly large updates that may take place. To address this issue, the paper presents a new adaptive method called SoftSignSGD (S3) that incorporates three design choices: p-th order moments, same $\beta$, and Nesterov's acceleration. The paper presents theoretical analyses on update scales as well as convergence properties. S3 is evaluated for vision and language tasks, achieving improved results in terms of task performances as well as training speed.

### Strengths
Recent works suggest that the SignSGD is what makes Adam and other adaptive methods work, and this work takes a step further to incorporate algorithmic advances so as to improve training stability and numerical effectiveness. The authors evaluate the proposed method (S3) for both vision and language tasks, and based on the results it indeed appears to be achieving superior performances for standard deep learning tasks.

### Weaknesses
- The assumption under which Theorem 1 holds (the signs of gradients are the same..) seems quite strong and may not hold in general. This makes the argument (rephrased) "large changes in specific and neighboring dimensions, leading to a chain reaction that ultimately results in loss spikes” rather speculative based on ad-hoc intuition (although Figure 2 seems still valid).
- Theorem 4 still has dependency on the problem dimensionality `d`.
- The claimed advantage of flexible p doesn’t seem to render much value; there doesn’t seem to exist a clear pattern of which p yields the best result, and thus, it anyway needs to be selected with a hyperparameter search. The criticism toward other compared methods due to their need of hyperparameter tuning thus seem a bit unfair or in other words, the contribution of allowing higher/flexible p seems a bit inflated.
- The improvement made by including Nesterov acceleration seems quite obvious (and also random) rather than fitting the purpose of this work. Also, it is hard to be considered their contribution unless the authors show that other compared methods cannot be improved with a similar acceleration scheme.
- The numerical results may not be statistically robust unless provided with results over multiple runs.
- This paper needs a lot of proof-reading; there are too many typos.

### Questions
- How many runs are these results averaged over? Is it the result of 1 (or n) run(s) using the same seed across all experiments? Can authors comment on this with respect to Tables 1, 2, and 3?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a novel optimizer, SignSoftSGD (S3), which uses higher-order moment in the denominator, uses the same momentum coefficient for numerator and denominator compared with Adam, and integrates Nesterov’s accelerated gradient technique. 
These modifications are designed to address the training instability and loss spikes often encountered with Adam, while also enhancing performance. The authors provide a theoretical convergence analysis for S3 with O(1/T^{1/4}) convergence rate.
Finally, the auothers conduct extensive experiments on language and vision tasks to showcase the effectiveness and stability of S3.

### Strengths
- The authors propose an optimizer, S3, with theoretical convergence guarantee, primarily aimed at solving the training instability issues seen with Adam.
- The pretraining experiments on language and vision tasks are solid. Extensive ablation experiments clarify the contributions of each modification in S3 over Adam, with recommendations for a default setting of  \beta = 0.95  and  p = 3  in practice.

### Weaknesses
 - My primary concern is regarding the cause of loss spikes in Adam.
	- Although Section 5.5 conducts several experiments to show Adam with same \beta successfully avoid loss spikes, the experiments in Section 5.3 display some inconsistent and intriguing behaviors.
	- In Figure 5, none of the S3 runs exhibit loss spike, even for configurations like (S3, lr=3e-3, diff. \beta, w/o NAG, p=3) and (S3, lr=3e-3, diff. \beta, w/ NAG, p=2). These results suggest that higher values of  p  and the inclusion of NAG may also prevent loss spikes. Therefore, it is better to provide a more detailed analysis of how each modification (higher p, NAG, same β) contributes to loss spike prevention. 
	- Figure 5 only shows loss curve for part of the experiment setups in Table 3, thus it is not straightforward to see which part is the main factor of the loss spike. It is better to provide loss curves for all setups in Table 3.
	- Furthermore, in the GPT-2 pretraining tasks, the NAG incorporated optimizers including Adan, and NAdam both have loss spikes, which appears inconsistent with the findings in Figure 5.
	- I also suggest adding the standard deviation for all reported metrics.
- The bound in Theorem 4 depends on dimension d. Although removing such an dependence over d is technically hard, could you compare the dependence on d explicitly with other recent works on adaptive optimizers like Adam. 
- What about the performance of S3 on diffusion models pretraining.
- Writing:
	- Please use  \citep and \citet formatting correctly.
	- There appear to be some typos or incomplete statements in the submission. For example, in line 161, it states, “An illustrative example can be found in Section D.3 of the appendix,” but there is no Appendix D.
	- In line 488, it shoud refer to Figure 6.

### Questions
See weakness above

### Soundness
3

### Presentation
3

### Contribution
3
