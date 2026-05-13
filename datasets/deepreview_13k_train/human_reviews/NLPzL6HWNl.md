# Improving LoRA in Privacy-preserving Federated Learning

- Decision: Accept
- Scores: 6, 5, 5, 6

## Abstract
Low-rank adaptation (\lora) is one of the most popular task-specific parameter-efficient fine-tuning (PEFT) methods on pre-trained language models for its good performance and computational efficiency.
\lora injects a product of two trainable rank decomposition matrices over the top of each frozen pre-trained model module.
However, when applied in the setting of privacy-preserving federated learning (FL), \lora may become unstable due to the following facts: 1) the effects of data heterogeneity and multi-step local updates are non-negligible, 2) additive noise enforced on updating gradients to guarantee differential privacy (DP) can be amplified and 3) the final performance is susceptible to hyper-parameters.
A key factor leading to these phenomena is the discordance between jointly optimizing the two low-rank matrices by local clients and separately aggregating them by the central server.
Thus, this paper proposes an efficient and effective version of \lora, \textbf{F}ederated \textbf{F}reeze \textbf{A LoRA} (\method), to alleviate these challenges {and further halve the communication cost of federated fine-tuning LLMs}.
The core idea of \method is to fix the randomly initialized non-zero matrices and only fine-tune the zero-initialized matrices.
Compared to \lora, \method is motivated by practical and theoretical benefits in privacy-preserved FL. 
Our experiments demonstrate that \method provides more consistent performance with better computational efficiency over vanilla \lora in various FL tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper discuss the potential discordances of applying LoRA in differentially private federated learning: (1) decompose `\DeltaW` to `BA` moves LoRA into a nonlinear regime that potentially cause trouble for aggregation/averaging in model updates (2) the nonlinearity of `BA` cause trouble for DP noise (3) LoRA introduce an extra parameter \alpha. A new algorithm FFA-LoRA is proposed, where instead of updating both `B` and `A` matrices in LoRA, FFA-LoRA only updates the matrix B and keeps A fixed at random initialization.


====== after rebuttal ======

I thank the authors for their response, and would like to maintain the borderline positive score. I really like the idea of fixing one matrix in LoRA, and appreciate the empirical evaluation. I won't provide a stronger support as the experimental setup is a bit unconventional, and it is a bit hard to justify the claims based on the current draft.

### Strengths
I like the motivation of the FFA-LoRA algorithm, and appreciate the attempt to provide some analysis on the caveats of LoRA. The experiments on two models (RoBERTa and LLaMA) fine-tuning on a subset of GLUE tasks and a GSM-8K language generation task in both non-DP and DP settings show good empirical performance of FFA-LoRA.

### Weaknesses
I thank the authors for providing details of the experimental setup. However, the federated learning setting in experiments seems a bit unconventional with a very small number of clients (only 3 clients). This might be categorized as a cross-silo setting, but it would be good to clearly discuss the targeted application (https://arxiv.org/abs/1912.04977 table 1, https://arxiv.org/abs/2107.06917 section 3.1).

While I appreciate the motivation of analyzing LoRA in section 3, none of the explanations seems to be particularly convincing. The discussion of Discordance (1) and (2) heavily focus on the nonlinear nature of LoRA, but deep neural networks suffer from more severe nonlinearity, it is a bit unclear for me why LoRA `BA` suffers more than multi-layer network `W_1 W_2`. For example, for (1), I believe it not only applies to averaging models from clients, but also to averaging gradients from examples. Specifically, the argument that averaging `B_1A_1` and `B_2A_2` is problematic seems to ignore the fact that gradients are also averaged, and these gradients are also non-linear functions of the weights. The interaction between the non-linearity of LoRA and the averaging process needs more rigorous justification. The current explanation lacks a clear distinction between the effects of non-linearity in standard neural networks and the specific challenges posed by the `BA` decomposition.

I also fail to understand why \alpha becomes an issue for LoRA in  Discordance (3) as it is only a scalar and might potentially be absorbed in learning rate. As shown in table  5, tuning the learning rate helps. The argument that \alpha introduces an extra hyperparameter seems weak, since learning rate is also a hyperparameter, and the two could potentially be tuned together. The claim that \alpha is problematic because it affects the clipping and noise in DP is not well-explained. It is unclear why the effect of \alpha on clipping and noise is more problematic than other hyperparameters that also affect the magnitude of gradients and thus clipping.

Minor:
The empirical results on local DP seem to be very good with very little accuracy drop compared to non-DP results. It is possible that DP fine-tuning is not a particularly hard task compared to training from scratch, but could the authors share more details about the privacy accounting and important privacy parameters?

FedBert seems to mainly focus on pre-training instead of fine-tuning.

Please cite “Communication-Efficient Learning of Deep Networks from Decentralized Data” for federated learning and the FedAvg algorithm.

### Questions
See weakness above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The author proposes FFA-LoRA, a LoRA variant in FL by freezing one of the LoRA weight and training only the other LoRA weight so that it's easy to do model averaging in FL. Empirical results show that FFA-LoRA achieves comparable performance compared with LoRA under different differential privacy guarantees.

### Strengths
+ The motivation is sound and the paper writing is easy to follow.
+ Empirical results show competitive performance under different differential privacy and parameter budget.
+ Empirical results are comprehensive, considering multiple tasks and ablation study.

### Weaknesses
 + The motivation is straightforward and intuitive, without theoretical insights.

 + Why rank 16 for MNLI is worse than rank 8 in Table 2?

 + Another intuitive variant is to alternative optimize the two LoRA weights. How would this perform compare with the proposed method?

 + Why non-iid performance is similar to iid performance in Table 3?

### Questions
+ Why rank 16 for MNLI is worse than rank 8 in Table 2?
+ Another intuitive variant is to alternative optimize the two LoRA weights. How would this perform compare with the proposed method?
+ Why non-iid performance is similar to iid performance in Table 3?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presented an approach called Federated Freeze A LoRA (FFA-LoRA) to address the limitations of the low-rank adaptation method in federated learning setting. The limitations of the vanila low-rank adaptation include: 1) data heterogeneity, 2) amplication of difficiential privacy noise and 3) sensitivity to hyper-parameters. Authors provide empirical results, showing that the FFA-LoRA outperforms vanilla LoRA in federated learning settings.

### Strengths
1. The study on federated LoRA is timely.
2. The proposed approach is simple to implement.
3. The authors provide case studies to highlight the limitations of the vanilla LoRA and motivate their approach.

### Weaknesses
1. The benefit of FFA-LoRA on differential privacy (DP) is not very well backed by empirical evaluation. The performance gap between the vanilla LoRA and the proposed FFA-LoRA remains the same across various privacy budgets $\epsilon$, including $\epsilon = 0$. Such an empirical result suggests that the impact of DP noise is the same on both the vanilla LoRA and the proposed FFA-LoRA.

2. I do not see why the proposed FFA-LoRA is free from tuning the hyper-parameter $\alpha$. In Section 4, the authors claim that "FFA-LoRA does not rely on $\alpha$, and is equivalent to LoRA with $\alpha = \infty$". Such a claim, in fact, suggests that the $\alpha$ is fixed in FFA-LoRA. Then, in Theorem 1, the theoretical result suggests that tuning $\alpha$ is equivalent to tuning the learning rate $\eta$. I'm not able to fully follow the discussion here.

3. There are several noticeable counter-examples in Tables 1&4. For example, we reach the largest gap between LoRA and FFA-LoRA with $\epsilon=1$ on the QQP and QNLI datasets instead of $\epsilon \in \{3, 6\}$. LoRA also outperforms FFA-LoRA by a significant margin on the SST-2 datasets with $\epsilon=1$. These results might be outliers, but we need more investigation before concluding that FFA-LoRA is more robust to DP noise.

4. The equivalence relationship between FFA-LoRA and LoRA never holds in practice and the benefit of large $\alpha$ is questionable. Theorem 1 suggests that a necessary condition for such an equivalence relationship is $\alpha_{LoRA} = \infty$. In practice, $\alpha_{LoRA} \neq \infty$. Indeed, in the provided reference (Kuang et al., 2023), the maximum $\alpha=50.0$ or $128$ if I read the tables in the appendix correctly. Also, tuning $\alpha$ does not seem to impact the accuracy much, as Figure 5(a) in Kuang et al., 2023 shows. Experiments with $\alpha = 0.5$ and $\alpha=50.0$ have almost the same average accuracy.

### Questions
1. Is the FFA-LoRA approach more sensitive to random initialization? Suppose a bad initialization sets $\mathbf{A} = \mathbf{0}$; is the model still trainable?

2. What's the variance in the experiment?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The Federated Generative Learning (FGL) framework offers a novel approach to federated learning, leveraging foundational generative models like Stable Diffusion to generate training data from prompts shared by clients. Clients contribute class-level or instance-level prompts, encapsulating key features of their local data. The server, in turn, amalgamates these prompts and synthesizes corresponding training data for global model training. This approach trims down communication costs since only concise prompts, and not bulky gradients or models, are transferred. This system also boasts robustness to data diversity and has demonstrated superior performance – with just one communication round, it outdid FedAvg's 200 rounds in accuracy. When trialed on skewed ImageNet100 distributions, FGL exceeded FedAvg's performance by 30% in just five communication rounds. Apart from being efficient, FGL also enhances privacy, as prompts reveal lesser private data than traditional methods. Evaluations confirmed no private data memorization in the synthetic images and an enhanced resilience against membership inference attacks. However, challenges persist with non-IID data, intricate domains, and the potential risks associated with prompts.

### Strengths
1.	Clearly identifies limitations of vanilla LoRA in federated learning settings and provides theoretical analysis on the causes.
2.	Provides extensive experiments that demonstrate consistent improvements of FFA-LoRA over LoRA on multiple models, datasets, and conditions.
3.	Reduces communication costs and removes reliance on scaling hyperparameters compared to LoRA.

### Weaknesses
1.	Unclear how the approach performs under other challenges like adversarial attacks, concept drift, and personalization. 
2.	The paper only evaluates NLP tasks with text data. Unclear if the benefits of FFA-LoRA generalize to other data types like image, speech, etc.
3.	The theoretical analysis and intuitions provided are informal. No formal convergence or privacy proofs given.

### Questions
please refer to the weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
