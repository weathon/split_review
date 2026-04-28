# Bi-Level Optimization for Pseudo-Labeling Based Semi-Supervised Learning

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Semi-supervised learning (SSL) is a fundamental task in machine learning, empowering models to extract valuable insights from datasets with limited labeled samples and a large amount of unlabeled data. 
Although pseudo-labeling is a widely used approach for  SSL that generates pseudo-labels for unlabeled data and leverages them as ground truth labels for training, traditional pseudo-labeling techniques often suffer from the problem of error accumulation, leading to a significant decrease in the quality of pseudo-labels and hence
	the overall model performance. 
	In this paper, we propose a novel Bi-level Optimization method for Pseudo-label Learning (BOPL) 
	to boost semi-supervised training. 
It treats pseudo-labels as latent variables, and optimizes the model parameters and pseudo-labels
jointly within a bi-level optimization framework. 
By enabling direct optimization over the pseudo-labels towards maximizing the prediction model performance,
the method is expected to produce high-quality pseudo-labels that are much less susceptible to error accumulation. 
To evaluate the effectiveness of the proposed approach, 
we conduct extensive experiments on 
multiple SSL benchmarks. 
The experimental results show the proposed BOPL outperforms the state-of-the-art SSL techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method to update pseudo-labels commonly used in semi-supervised learning (SSL). The "bi"-level optimization refers to one objective being the training loss with pseudo-labels as targets, which is a function of both parameters and pseudo-labels, and the other objective of refining pseudo-labels. The objective for pseudo-labels is defined to be the cross entropy on the labeled dataset + entropy of model predictions on the unlabeled dataset. The authors provide a cheap approximation to the gradients of this objective, which is optimized with projected gradient descent, where the authors experiment with different projections (ReLU vs. softmax). This procedure is combined with other SSL methods and tested on common SSL datasets.

### Strengths
* The proposed method outperforms many other SSL algorithms on common SSL benchmark datasets. 
* Ablation studies shows that pseudo-labels benefit from ReLU projections instead of softmax which is an obvious choice for projection onto the probability simplex. It's good that the paper experiments with projection methods and found that there is a better working solution that softmax.

### Weaknesses
 * The approximation in Eq. 14 still requires two parameter updates to compute the gradient; this must be slow. While the authors update parameters $\theta^+$ and $\theta^-$ using a single gradient calculation, the gradient of the outer loss with respect to the pseudo-labels requires a forward pass with both $\theta^+$ and $\theta^-$. This effectively doubles the forward pass computations for each unlabeled sample, which will increase training time and memory usage.
* Presentation could be improved. Prop. 1 is just a nice expression for the chain rule - consider combining with proposition 2 or moving it to the Appendix? I also think the description in Alg. 1 could be simplified by writing only the steps critical to the algorithm, e.g. no need to write "compute loss L_{inner}" which doesn't really help with understanding. Or if the authors feel that it's needed, write the expression again in the algorithm description to make it self-contained.
* The novelty of this method seems incremental - while it's practically useful, the only real contribution is to write the parameters $\theta_S$ as a function of $Y$ with a cross-entropy / entropy loss, from which the method naturally follows. However it's not clear why this method results in improved performance. The authors claim the method avoids cumulative errors and inconsistency, but the empirical gains are small, and it's not clear that these gains are a direct result of resolving those issues.

### Questions
Is the pseudo-label updates implemented using expression in Eq. (14) under Prop. 2 to update the labels? It isn't mentioned for sure whether this is used; Equation 17 suggests that the labels are being updated with the true gradients rather than the approximation form in Eq. 14. If so, why do the authors describe the approximation?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a Bi-level Optimization method for Pseudo-label Learning (BOPL) for Semi-Supervised Learning, which treats pseudo-labels as latent variables and formulates pseudo-labeling as a bi-level optimization problem to jointly learn the pseudo-labels and model parameters within a bi-level optimization framework. This approach simultaneously enhances the quality of pseudo-labels and the prediction consistency between labeled and unlabeled data. Experimental results validate the effectiveness of the proposed approach and show that it outperforms the state-of-the-art SSL techniques.

### Strengths
1. This paper defines the SSL problem as a novel bi-level optimization problem, which directly learns the pseudo-labels of unlabeled samples as latent variables through an outer optimization, updates pseudo-labels using teacher-student model, and learns the model parameters through an inner optimization.
2. BOPL employs a pair of bi-level objectives to ensure prediction consistency between labeled and unlabeled samples and combines Interpolation Consistency Training (ICT) to facilitate model training and improve the robustness and generalizability of the model.
3. The experiments are compared with existing SSL methods, and ablation study and sensitivity analysis are conducted. The results demonstrate the effectiveness of BOPL.

### Weaknesses
1. The pseudo-labels are simply initialized by the initial teacher model parameters and the update process is impacted by various factors, including the learning rate α, linear combination weight γ and the EMA based teaching models. Consequently, the update of the pseudo-labels tends to be slow. Are there alternative methods that can be used to initialize pseudo-labels to expedite the convergence of model training, such as employing warm-up with labeled data or using mean soft labels (1/num_classes)?
2. In the Algorithm 1, the update of $\theta^{t+1}_{S}$ in the last 3rd line is equivalent to the 7th line and it seems to be redundant.
3. Both Meta Pseudo-Labels[1] and Meta-Semi[2] formulate SSL as a bi-level optimization problem, please explain in detail the differences between BOPL and them.
4. In Table 1, there exists some unreasonable data, which is different from the original paper. For example, in ReMixMatch[3], the test error of 6.27±0.34 for 250 labels and 5.14±0.04 for 4000 labels in CIFAR-10 in original paper differs from the values presented in this paper. Is it because the experimental setup is different from the original paper? Furthermore, in BOPL, the test error for 250 labels is lower than that for 1000 labels in CIFAR-10, which seems to contradict common sense. If these results are accurate, it could imply that BOPL may not be the top-performing method under this setting. According to common expectations, SimMatch's [4] results at 1000 labels should fall within the range of 4.84 and 3.96, while BOPL's reported result of 5.12 seems less favorable by comparison.
5. Compared with existing SSL methods, it's possible that the experiments lack some widely used and important settings, particularly in more challenging conditions. It is suggested to validate the effectiveness of the BOPL approach under the setting of 40 labels in CIFAR-10, 400 labels in CIFAR-100 and 250 labels in SVHN, following the setups of FixMatch[5] and SimMatch[4]. Meanwhile, the results of BOPL+ICT are missing from the main text, please provide additional experimental data.

### Questions
Please respond to the questions mentioned above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper designs a bi-level optimization method for semi-supervised learning (SSL). In the outer loop, it optimizes the pseudo-labels by minimizing the validation loss. In the inner loop, it optimizes the model parameter by empirical risk minimization. Extensive experiments validate the effectiveness of the proposed approach.

### Strengths
- The paper is well written and easy to understand.
- The proposed method is simple yet effective, and the introduction of bi-level optimization is novel in the SSL literature.
- To solve the optimization problem in the outer loop, the approximation approach is sound and effective. The entire algorithmic process is simple and interesting.

### Weaknesses
 - The convergence of the proposed method is not revealed either theoretically or empirically. I think both theoretical and empirical analysis can be done to analyze the convergence problem. Similar theoretical analysis of convergence can be found in many bi-level optimization papers, and introducing it can improve the paper. Besides, it is also important to present the convergence figure of parameters, i.e. pseudo-labels in this paper. For example, the empirical study of the convergence property can be referred to Shu et al. (2019).

- Since the approach explicitly introduces the validation data sets in the training phase, it is not clear whether the comparison with the previous method is still fair. Previous methods at most used the validation set for tuning hyperparameters. Authors should explicitly discuss this issue. They should also discuss the number of validation data for the method, because I am afraid that the imparity problem gets worse with more validation data.

### Questions
- Can the method converge quickly?
- Is the comparison with previous SSL methods still fair?
- What's the impact of the number of validation data?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
