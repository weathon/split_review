# Deep Learning with Plausible Deniability

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Deep learning models are vulnerable to privacy attacks due to their tendency to memorize individual training set examples. Theoretically-sound defenses such as differential privacy can defend against this threat, but model performance often suffers. Empirical defenses may thwart existing attacks while maintaining model performance but do not offer any robust theoretical guarantees.

In this paper, we explore a new strategy based on the concept of plausible deniability. We introduce a training algorithm called Plausibly Deniable Stochastic Gradient Descent (PD-SGD), which aims to provide both strong privacy protection with theoretical justification and maintain high performance. The core of this approach is a rejection sampling technique, which probabilistically prevents updating model parameters whenever a mini-batch cannot be plausibly denied. This ensures that no individual example has a disproportionate influence on the model parameters. We provide a set of theoretical results showing that PD-SGD effectively mitigates privacy leakage from individual data points.  Experiments also demonstrate that PD-SGD offers a favorable trade-off between privacy and utility compared to differential privacy (i.e., DP-SGD) and empirical defense methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new notion of privacy tailored to noisy SGD, called plausible deniability, inspired by prior work on synthetic data. The notion could be restated as follows. Given $k \geq 1$ mini-batch gradients $g_j$ and their noisy versions $\tilde g_j = g_j + \mathcal{N}(0, \sigma^2)$, a gradient update step satisfies $(s, \sigma, T, \gamma)$-plausible deniability if for a given $s \in [k]$, we have $|\\{ \\mathrm{LR}\_{s,i}(\tilde g_s) \leq \gamma \mid i \neq s \\}| \geq T$, where $\\mathrm{LR}\_{s,i}: \mathbb{R}^{d} \rightarrow \mathbb{R}$ is the absolute value of the Neyman-Pearson log-likelihood ratio between two simple hypotheses $H_0: \tilde g_s \sim \mathcal{N}(g_s, \sigma^2 I_d)$ and $H_1: \tilde g_s \sim \mathcal{N}(g_i, \sigma^2 I_d)$:

$ \\mathrm{LR}\_{s,i}(\tilde g_s) = |\log p(\tilde g_s \mid \mathcal{N}(g_s, \sigma^2)) - \log p(\tilde g_s \mid \mathcal{N}(g_i, \sigma^2))|,$
where $p(\cdot \mid P)$ is a pdf of the distribution P.

In other words, a noisy gradient update is plausibly deniable if there exist $T$ other mini-batches that could have produced it aside from the original mini-batch, with a given pre-specified confidence level $\gamma$. The paper proposes PD-SGD, a variant of noisy SGD which rejects gradient updates that do not pass the plausible deniability test. The paper shows that it outperforms empirical defenses in terms of the trade-off between empirical membership inference attack performance and utility.

### Strengths
This paper aims to strike a balance between provable privacy guarantees and the loss in utility and computational overhead, by introducing a new notion of privacy inspired by prior work on synthetic data. The notion should significantly improve performance of DP-SGD as it does not require clipping. The approach is novel and interesting.

The paper does a good job at positioning their work within the landscape of prior research. The usage of four attack types provides a fairly solid basis for an empirical evaluation of the proposed method.

### Weaknesses
Although I think the approach is quite interesting, I believe in the current version it misses the mark on one of the two stated goals of the paper — providing robust privacy guarantees.

This is because the definition lacks clear operational meaning, which is manifested by the following concrete issues:
   1. Crucially, what does plausible deniability mean for, e.g., membership inference, attribute inference, or reconstruction robustness? The definition does not provide a clear, quantifiable privacy guarantee against these attacks. The notion of 'plausible deniability' is not directly linked to a formal privacy definition, making it difficult to analyze its robustness against various privacy threats. For instance, while the method might obscure the specific mini-batch used, it's unclear how well it prevents an adversary from inferring membership based on the overall pattern of gradient updates over multiple iterations.
   2. By fixing the Neyman-Pearson statistic threshold $\alpha$/$\gamma$, the definition inadvertently specifies the test error rates as a function of gradient difference $d = ||g_s - g_i||_2^2$. Depending on the noise scale, and the distribution of gradient differences, the test's Type I/Type II error could be significant — and again, the definition hides this fact by fixing $\gamma$ in advance. E.g., if values of $d$ in practice happen to be close enough to the noise scale, the test will have high error rates, meaning that the $T$ plausibly deniable candidates could actually be relatively different from the seed gradient. The choice of a fixed threshold $\gamma$ does not account for the varying magnitudes of gradient differences, which can lead to inconsistent privacy guarantees. A small $\gamma$ might lead to many false positives (accepting implausible gradients), while a large $\gamma$ might lead to many false negatives (rejecting plausible gradients), both of which can compromise the intended privacy protection. The definition should explicitly consider the distribution of gradient differences and adapt the threshold accordingly.
   3. The definition concerns itself with plausible deniability of the mini-batch gradients and not individual per-sample gradients. What is the protection for individual samples? In particular, the test boils down to approximately verifying whether there exist other mini-batches within an L2 ball around the seed mini-batch. What if there exist many mini-batches with similar L2 norm, but it is the _direction_ of the gradient that is significantly impacted by a single outlier example in the seed mini-batch? The paper lacks both formal and informal discussion on the level of protection for individuals, and the discussion in Sec 4.2 does not address this sufficiently. The method's focus on mini-batch gradients fails to address the potential privacy risks associated with individual samples. An outlier sample can significantly alter the direction of the gradient, and the method does not provide a clear mechanism to prevent this information from leaking. The test only checks for similar L2 norms, which is insufficient to guarantee that the gradients are genuinely interchangeable from a privacy perspective. The definition should be extended to consider the impact of individual samples on the gradient.
  4. As the parameters are not immediately interpretable, the parameter tuning process lacks clarity. The authors give a rationale for their choices in Section 4.2 and Appendix D.2, but it’s still hard to see how someone would apply this method in real-world situations. The lack of interpretability of the parameters makes it difficult to apply the method in practice. The authors provide some guidelines, but they are not sufficiently clear to allow a practitioner to select appropriate parameters for a given dataset and privacy requirement. The tuning process should be more transparent and provide a clear mapping between the parameters and the level of privacy achieved.

### Questions
- In Fig. 2, why define advantage as 2 AUC - 1 if the standard definition is 2 balanced_accuracy - 1 = TPR - FPR?
- In Fig. 2, isn't there a parameterization of AdvReg that could be used to produce a curve instead of a single point?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose an alternative to empirical MIA defenses and DP-SGD and claims higher utility while making compromises in the theoretical guarantees in comparison to DP but in comparison to other works it still provides some. The authors provide both theoretical as well as empirical evidence that their method can be an alternative.

### Strengths
- providing a new method closing the gap between purely empirical defenses and DP-SGD by introducing a new method that has theoretical guarantees that are weaker than with DP but at the same time providing higher utility.  
- theoretical results regarding the new method
- empirical results and ablation studies comparing the method to other alternatives

### Weaknesses
I cannot recommend the acceptance of the paper at the moment as especially the empirical part is not strong enough to understand the contribution and the advantage of the method. I am willing to increase my score when the below points and questions are addressed or there are some contributions or points that I misunderstood. 

- **W1: Comparison to other defenses without any error bars.** The authors compare in Section 5 to other defenses using multiple attacks. Unfortunately, there are not error bars for test accuracy or the membership inference attack metrics. Related prior work on few-shot image-classification using fine-tuning (so exactly the same setting that the authors are operating in) by Tobaben et al. [1] found that there is quite a difference in test accuracy over multiple repeats (see e.g., Figure 1 of [1]). Other work focusing on membership inference attacks like the recent RMIA [2] use repeats for comparisons like in Table 3 of [2]. In my opinion, the proposed method performs not as clearly better to justify the bold claim in the contributions: *"Results demonstrate that PD-SGD offers a superior privacy-utility trade-off compared to alternatives."*. E.g., Table 2: DP-SGD on CIFAR-10 ($ε=8$) is nearly as good in test accuracy and comparable in the resistance to attacks. SELENA is comparable in test accuracy and resistance to attacks throughout all experiments in Table 2 and 3. Note that I am not doubting the claims of the authors entirely but I feel that without error bars the conclusions made by the authors are too strong. The authors could improve here by providing error bars.

- **W2: Runtime comparison.** One concern I have with the method is the runtime of it. The authors write in Section 3.3: *"In experiments (supplementary materials) we find that although PD-SGD is slower than
SGD, it is often much faster than DP-SGD for a single training step, in large part because it does not require calculating per-example gradients."* Table 6 compares the run time for the same amount of data and find that DP-SGD is around $38 \times$ and PD-SGD is around $15.7 \times$ slower than SGD for the same amount of data. When comparing to prior work by Bu et al. [3] and Beltran et al. [4] that the authors cite in the introduction the number for DP-SGD seems very high (Figure 3 of [3] suggests more factor 3 with opacus and [4] shows for the same model architecture as the authors use a factor of $2.8 \times$). Furthermore, both related works discuss methods that make DP training faster. The authors should discuss mention these methods (e.g., GhostClipping) and validate their runtime measurements as the gap seems strikingly large.

- **W3: Experimental Setting is not described in detail:** In is unclear from the main text how many data points are used in the experiments in Section 5 (this is a very important information), it is unclear from the paper how shadow datasets are used (e.g., for S-Attack and C-Attack), how many shadow models are trained and if the attacks are run in offline or online setting (e.g., at least C-Attack). It is unclear what the hyperparameters for all other defenses than PD-SGD are and how they were selected. Furthermore, it is not clear from the main text what subsets of the models were fine-tuned. The authors could improve their paper by providing all details to ensure reproducibility of the paper.

Minor:
- I looked at the `ml_privacy_meter` at https://github.com/privacytrustlab/ml_privacy_meter that you mentioned but I think it doesn't implement LiRA in its current form. Browsing through the commits I found that perhaps the package changed significantly in the meantime. I would recommend the authors to refer to a particular git hash and include that link to make sure that the reproducibility is ensured.

- In Line 363: There are typos with the dataset names.

- I discussed Tobaben et al. [1] in the upper part as it is a very related work on few-shot fine-tuning but it is not mentioned in the paper. I recommend the authors to include it in their discussion as a related work.

### Questions
- Q1: Why is DP-SGD so slow in your setting? I assume you implement it using off-the-shelf opacus? (Re W2)
- Q2: How are the attacks run? E.g., how many shadow models? (Re: W3)
- Q3: What are the hyperparameters for the other methods and how are they determined? (Re. W3)
- Q4: In line 158 you say that plausible deniability can be made DP. Is this applicable to your method as well?
- Q5: Could you provide some intuition on how to pick the hyperparameters in practice for your method? DP hyperparameters can be connected to MIA success bounds (e.g., Kairouz et al. [5]). How would it be for your method?
- Q6: Could you provide access to your code please? I would be interested in reviewing the details of that implementation.

[5] Kairouz, P., Oh, S., & Viswanath, P. (2015, June). The composition theorem for differential privacy. In International conference on machine learning (pp. 1376-1385). PMLR.

### Soundness
2

### Presentation
2

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
This paper introduces Plausibly Deniable SGD updates. The key concept involves randomly selecting a seed batch, and if the current update deviates significantly from this seed batch, the update is skipped. To measure the difference between the gradients of the seed batch and the current update, Gaussian noise is added to both, and the log-pdf is bounded by a parameter $\gamma$ (Eq 2). This process is repeated $m$ times for each update, and the update is considered safe if it passes the test at least $T$ times.

### Strengths
1. The concept of plausibly deniable updates is both intuitive and innovative.
2. The authors conduct experiments across multiple datasets, showing that this method can provide a favorable privacy-utility tradeoff compared to DP-SGD in some settings. The privacy protection is evaluated using empirical membership inference attacks.
3. The paper is clearly written and easy to understand.

### Weaknesses
1. The main assumption behind plausibly deniable updates is that there is no privacy leakage when an update closely resembles updates from other batches. While this assumption is intuitive, it may not hold uniformly across all scenarios.

For example, consider the training of large models with very large batch sizes, where individual sample contributions are averaged out. In this case, even tiny noise may cause the gradients of two large batches to appear deniable, but not necessarily prevent individual samples from being memorized.

Follow-up questions: 

(1) How does the rate of deniability scale with batch size across different datasets? 

(2) What impact do varying batch sizes have on the overall privacy guarantees?

2. In Table 2, the CIFAR-10 and CIFAR-100 experiments use only 500 and 1000 training samples, respectively. While the performance of plausibly deniable updates in these settings is notable, these sample sizes are too small for a fair comparison with DP-SGD.

Follow-up question: 

How do plausibly deniable updates compare with DP-SGD when scaling the training set size for CIFAR-10/CIFAR-100?

3. As discussed in Appendix F, the privacy guarantee for plausibly deniable updates applies on a per-update basis, and the composition of these guarantees over an entire training run remains unclear.

Additional Comments:

1. The intermediate results of training with plausibly deniable updates must remain private, as revealing whether an update was skipped provides side information to the adversary. This limitation may restrict the applicability of the approach in certain scenarios, such as federated learning.
2. When comparing the empirical privacy protection of plausibly deniable updates with DP-SGD, even if a fixed privacy parameter is used for DP-SGD, the clipping threshold still affects the robustness against membership inference attacks. It could be beneficial to tune the clipping threshold to identify the optimal empirical protection for DP-SGD.

### Questions
Please see "Weaknesses".

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a novel method for training private ML models using the plausibly deniable SGD. The work shows that by discarding the gradients that are not plausibly deniable, the users can obtain quantifiable guarantees of privacy and better empirical performance than the standard DP methodology (DP-SGD).

### Strengths
The approach is novel and really interesting. The work itself is well-motivated, easy-to-follow and well-written. Most of the details are sound to me and the empirical results are mostly promising. There is a large number of evaluation with respect to attacks, which is always great to see.

### Weaknesses
To start with, I am not entirely sure on how sound the algorithm is. Firstly, it is not clear what exactly happens if the gradient is implausible - do you remove it or convert all values to 0's or something else entirely? Because 'removal' in a normal sense of a word would result in different sampling for the rest of the users and would cost them more epsilon, making some of them more vulnerable (which has knock-on effects on disparate vulnerability to MIA and how the method affects that). Specifically, if the implausible gradients are simply skipped, this introduces a bias in the training process, as some samples will contribute less to the overall learning than others. This could lead to a situation where certain data points are effectively ignored, potentially impacting the model's ability to generalize across the entire dataset. Secondly, this has an effect on the fairness of the algorithm: the benchmarks you used only consider the standard (somewhat easy and mostly balanced) datasets. In order to see how the method performs with respect to privacy attacks and subgroup utility, more analysis needs to be done and I request that the authors add a section on how performance imbalance is affected under PD-SGD.

There is also an issue with the way the paper is positioned. I admit I had to re-read the work because it is not immediately clear this method is, in fact, not designed to be differentially private (primarily because of the discussion on adding the gaussian noise and the privacy guarantees afterwards). Just to make it more clear to the reader, I would suggest you point this out early in the text. Especially since following claim only gets introduced in 2.4: 'With some additional randomisation this can be made epsilon-delta DP' What is this additional randomisation and where does it come from? Where is it discussed and how do you convert the guarantees? This sounds (in crude terms) a little bit like k-anonymity here, where you have a rejection sampling based on the number of rows that could have been used to produce the synthetic row (i.e. a probabilistic notion of k). Could you elaborate on why this is/isnt the case and what exactly needs to be done to establish the mapping between the methods?

I am not fully convinced on your choice of defence mechanisms. You seem to have picked Selena, which makes sense, but follow-up works have been proposed which significantly improved the effectiveness of the method and since this method is empirical, I wonder why you did not evaluate PATE, which actually does come with privacy guarantees and is based on a similar method? If you are only doing training-based methods, then DKFD could be a good one to consider? AdvReg also does not seem like a strong candidate to compare against since it was already shown (in the original paper) to be mostly effective for data with a small number of classes (i.e. not cifar-100), making some of the comparisons less meaningful. Finally, it would be beneficial for paper's contextualisation to establish some more concrete links between the parameters of PD-SGD and the comparable DP-SGD parameters (i.e. have a simple graph comparing just these two methods as the only 'properly' quantifiable ones showing at which point PD-SGD starts showing better privacy-utility trade-off).

On the empirical results. Firstly, I would really highlight the 'best' results in bold instead of PD-SGD results, as otherwise this is misleading with respect to what the best defence is. It is clear that the method is comparable, but it is also not outperforming all of the baselines, making the abstract a bit misleading with respect to the favourable trade-offs.

### Questions
As above: what are the fairness implications of the method? This needs proper evaluation on other datasets (or the same datasets with manual imbalancing).

### Soundness
3

### Presentation
4

### Contribution
3
