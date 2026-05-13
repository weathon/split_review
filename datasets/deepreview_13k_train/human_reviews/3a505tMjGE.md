# AVOID: Alleviating VAE's Overestimation in Unsupervised OOD Detection

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Deep generative models (DGMs) aim at characterizing the distribution of the training set by maximizing the marginal likelihood of inputs 
in an unsupervised manner, making them a promising option for unsupervised out-of-distribution (OOD) detection.
However, recent works have reported that DGMs often assign higher likelihoods to OOD data than in-distribution (ID) data, i.e., **overestimation**, leading to their failures in OOD detection.
Although several pioneer works have tried to analyze this phenomenon, and some VAE-based methods have also attempted to alleviate this issue by modifying their score functions for OOD detection, the root cause of the overestimation in VAE has never been revealed to our best knowledge.
To fill this gap, this paper will provide a thorough theoretical analysis on the overestimation issue of VAE, and reveal that this phenomenon arises from two aspects: 1) the improper design of prior distribution; 2) the gap of dataset entropy-mutual integration (sum of dataset entropy and mutual information terms) between ID and OOD datasets.
Based on these findings, we propose a novel score function to **A**lleviate **V**AE's **O**verestimation **I**n unsupervised OOD **D**etection, named ``**AVOID**'', which contains two novel techniques, specifically post-hoc prior and dataset entropy-mutual calibration.
Experimental results verify our theoretical analysis, demonstrating that the proposed method is effective in alleviating overestimation and improving unsupervised OOD detection performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new approach to address overestimation in unsupervised Out-Of-Distribution (OOD) detection using Variational Autoencoders (VAEs). In their investigation, they found two main factors that contribute to overestimation in OOD, (1) improper design of the prior, and (2) gap in entropy-mutual integration between in-distribution and out-distribution. The proposed approach uses a new score function to address the two problems. 
The paper presents extensive experiments to validate the effectiveness of the proposed method, suggesting a competitive performance compared to literature methods. An ablation study is also presented to evaluate the behavior of the main components of the proposed approach: post-hoc prior and dataset entropy-mutual calibration.

### Strengths
I found the performed evaluation of the factors that cause overestimation in OOD detection very interesting. The unsupervised approach using VAEs seems promising and robust.
The authors also designed a comprehensive and extensive set of experiments, including ablation studies, to evaluate the contributions of individual components of the proposed method.
The paper is well-organized, I liked the approach of breaking down the problem, its causes, the solution, and the experimental validation in a logical sequence.
I believe that OOD detection represents a significant challenge in the field of machine learning. This is especially true for safety-critical applications as we are every day more dependent on automatic decision-making.

### Weaknesses
Besides the large number of experiments, I think the main experiments are centered on or in variations of specific datasets like FashionMNIST and CIFAR-10.

I agree with the authors that the ablation study provides insights, but I don't think the contributions of the PHP and DEC components are still clear, especially when combined.

The authors should clearly address the computational efficiency of the proposed method compared to standard VAEs and other literature approaches to the problem.

I don't like to rely on t-SNE plots to make claims about the differences between in-distribution and out-of-distribution data.  While it is a popular choice for high-dimensional data visualization, I think UMAP offers several advantages as it preserves more of the global structure of the data and is more reproducible as it offers more intuitive hyperparameters.

I was wondering, as the authors separate ensemble methods from non-ensemble methods in the "Unsupervised" category, it would be interesting to understand how the proposed method performs against ensemble methods. I was considering the performance in terms of performance and computational cost.

I do believe the authors benefit from a discussion on scenarios where the proposed method might not work well. This gives readers a more balanced view and sets expectations correctly. I suggest the authors explore more of that.

### Questions
Would the method work with more complex architectures, or is it specifically tailored to standard VAEs?

Have the authors evaluated the robustness of the proposed idea against adversarial examples or noisy datasets?

How does overestimation influence real-world decisions or systems that rely on OOD detection? I think contextualizing that in the paper will help the reader to understand better the proposed approach.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of generative models, specifically VAEs, when applied to OOD detection tasks. It is based upon the observation that the ELBO used in VAEs, even though it is a reasonable candidate, is an unreliable metric for OOD detection. Moreover, it tries to change the metric to come to a more reliable score to perform OOD detection.

The paper breaks down the ELBO of a dataset (being in- or out-of-distribution) into two components: (i) a negative KL divergence between the aggregate posterior $q(z)$ and the prior $p(z)$, and (ii) a negative term related to dataset entropy and mutual information between inputs and latent variables. 
It identifies the cause of ELBO's poor performance in OOD detection, noting that the KL divergence in (i) is often overestimated and the negative entropy term in (ii) is often inflated for simpler datasets that we perform OOD detection on (for example doing OOD detection on MNIST when a model is trained on FashionMNIST). The work proposes a post-hoc correction to adjust the former (PHP) and it introduces a method (DEC) to correct the small OOD entropies by utilizing a complexity measure inspired by Serra et al. (2020).
Implementing these adjustments successfully improves OOD detection for VAEs in challenging scenarios, such as differentiating between datasets like FashionMNIST and MNIST, or CIFAR10 and SVHN.

All in all, the study tries to address an intriguing problem, but at this stage, I cannot accept it and I will explain why in the following. I would be willing to increase my score to above the acceptance threshold if the authors can address all the important issues and suggestions that I have written in the following.

### Strengths
1) The paper is well-written and easy to follow.
2) The problem of DGMs failure in OOD detection is intriguing and has been observed not only in VAEs, but almost all the likelihood-based deep generative models. Therefore, any contribution in this field is valuable.
3) Breaking down the ELBO term is interesting from a theoretical standpoint. Although this observation is not entirely novel, as I will explain in the weaknesses, the theory is certainly sound and the method improves the OOD detection performance by large for the tasks it has considered.
4) The toy examples are very informative and interesting.

### Weaknesses
1) **(Important)** The OOD detection pathology is one-sided, meaning that it happens when you train a model on a relatively complex dataset and test it for OOD on a simpler one. However, it usually does not hold the other way around. An important feature that a good OOD detection method should have is that even though it fixes the pathological direction, it does not hinder the performance in the reverse direction. That being said, please provide the results when running the framework in the reverse direction where a VAE is trained on MNIST and tested for OOD on FashionMNIST. Similarly, when a model is trained on SVHN and tested for OOD on CIFAR10. It is well-known that many such methods hinder the performance in the other direction, one would need to make sure this does not happen for the current algorithm.
2) **(Important)** Although the entropy and KL divergence breakdown is touted as novel, it is not entirely novel! Caterini et al. (2022) have considered breaking down the likelihood term into an entropy and a KL divergence term. In fact, in the special case where ELBO equals the likelihood and the encoder and decoder provide perfect mappings, the mutual information terms cancel out and the entropy term is pointed out in Caterini et al. (2022). However, this paper is not mentioned at all. It should most certainly be added to the next iteration of the paper.
3) The PHP method needs to train an entirely new model which can be time-consuming. Ideally, your generative model already has a good understanding of what in-distribution means and should be able to perform OOD detection even without additional training. The additional training introduces a potential for overfitting to the in-distribution data, which could negatively impact OOD detection performance on unseen datasets. The computational cost of training this extra model should also be considered, especially for large datasets or complex architectures.
4) The DEC method is tested specifically on image data and the SVD-based algorithm also seems like a sort of “outside help”. Even though similar methods have been proposed in the past to fix the entropy term, such as Serra et al. (2020), I still believe that the DGM should already have the information required for OOD detection without the need for any extra model training or running modality dependent algorithms. The reliance on SVD, which is a linear dimensionality reduction technique, may not be optimal for capturing the complex non-linear structures present in the latent space of a VAE. This could limit the effectiveness of the DEC method for more complex datasets or models.
5) Performing OOD detection requires adjusting an $n_{id}$ hyperparameter which is task-dependent, and there is no guarantee that one setting of this hyperparameter generalizes to all. The sensitivity of the method to the choice of $n_{id}$ needs to be thoroughly investigated. A small change in this parameter could lead to significant variations in OOD detection performance, making the method less reliable in practice. The lack of a principled way to choose this hyperparameter is a major limitation.
6) Please cite the relevant study by Schirrmeister et al. (2020) on the reason behind the OOD detection anomaly for invertible networks.
7) This study only considers VAEs. It would be interesting to see how the method acts in a broader context when a latent space is involved. For example, latent diffusion models are such examples. Even though other generative models might be out of the scope of the paper, it should be pointed out as a limitation of this study.

### Questions
1) **(Important)** Although the PHP method is quite novel, it reminds me of the studies where an extra flow model is trained on the latent space of a VAE to alleviate the bias that the aggregate posterior should be Gaussian. Loaiza-Ganem et al. (2022) (which has not been referenced in this paper) show that a VAE model that has been trained again with a flow on top can perform much better in OOD detection. Could you provide some discussion on the connections between your study and theirs? And how yours is novel?

2) **(Important)** Could you please generate a figure similar to Figure 3 for the CIFAR10 (vs) SVHN OOD detection task where the PHP method does not improve the performance by large?

3) The computation of $C_{non}$ seems rather contrived! I might have missed it but what is the rationale behind the formula when $n_i \ge n_{id}$? Why not choose a simple fix such as the compression scores proposed by Serra et al. (2020)? I am referring to an ensemble of FLIF, JPEG, and PNG compressions and computing the bit count for the compressed images.  Also, can I ask for a runtime analysis of computing $C(x)$? This is more of a suggestion, but I believe you can improve algorithm 1 (in Appendix D) for computing $n_i$ by performing a binary search rather than iterating over all the possible values. Since the number of potential singular values $N$ can be as high as the number of pixels, it is important to be efficient.

**References**

Loaiza-Ganem, Gabriel, et al. "Diagnosing and fixing manifold overfitting in deep generative models." arXiv preprint arXiv:2204.07172 (2022).

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new anomaly score for OOD detection with VAEs: rather than use the ELBO, the paper proposes to 
1. replace the prior $p(\mathbf{z})$ in the KL divergence term in the ELBO with the aggregated posterior $\hat{q}_{id}(\mathbf{z})$, which they call the post-hoc prior (PHP) method, and 
2. add a term $\mathcal{C}(\mathbf{x}) = \mathbb{E}_{p_{id}}[PHP(\mathcal{x})] \frac{\mathcal{C}_{non}(\mathbf{x})}{\mathbb{E}_{p_{id}}[\mathcal{C}_{non}(\mathbf{x})]}$, which they call the dataset entropy-mutual calibration (DEC) method.

On the two most classic OOD detection failures for DGMs (i.e., FMNIST vs. MNIST, CIFAR-10 vs. SVHN), using just one of PHP or DEC succeeds on one benchmark but fails on the other, while using both PHP and DEC combined (which they call AVOID) succeeds on both benchmarks. On the Celeb-A vs. CIFAR-10 and Celeb-A vs. CIFAR-100 tasks, PHP, DEC, and AVOID perform better than other VAE-based detection methods. The authors also show that AVOID performs better than the ELBO on various OOD detection tasks with FMNIST, CIFAR-10, or Celeb-A as the in-distribution dataset.

### Strengths
1. Originality: To my knowledge, the proposed method is novel.
2. Quality: The experiments consider a wide range of baseline methods and ablations. 
3. Clarity: The paper does a good job of breaking down the presentation particularly for factor 1, e.g. from analysis to proposed method.
4. Significance: The paper tackles the important question of understanding and improving failures in OOD detection by VAEs. In particular, I find it interesting that OOD detection with VAEs improves when substituting in the aggregate posterior for the prior in the ELBO. This result seems to provide a good example of how accounting for estimation error can improve OOD detection.

### Weaknesses
1. The motivation behind DEC is unclear, and its presentation is a bit circuitous. For instance, the non-scaled calibration function defined in Eq 19, $\mathcal{C}_{non}(\mathbf{x}) = \frac{n_{id} - (n_i - n_{id})}{n_{id}}$, raises questions, especially when $n_i \geq n_{id}$. While the authors state that many definitions could satisfy property 1 (Eq 15), the rationale behind this particular choice, which utilizes the SVD compressor, is not adequately justified. Furthermore, the scaling factor in the DEC method, which involves the Ent-Mut of the ID distribution plus a KL divergence term, is not clearly motivated. If the aim is comparability with the Ent-Mut terms, a more direct scaling approach might be expected. A more thorough investigation into the robustness of performance to various choices in the DEC formulation, or a more rigorous justification of the current formulation, would significantly strengthen the paper.
2. The experiments show that PHP and DEC by themselves each only minimally improve OOD detection performance in some cases. In addition, the experiments only consider certain pairs but not their reverse (e.g., FMNIST vs. MNIST but not MNIST vs. FMNIST). Considering the latter can increase confidence that the proposed solution is not overfitting on a particular type of OOD detection task.

A few smaller comments:
1. The use of "counterfactual" in the third paragraph in the intro seem incorrect.
2. Eq 24 in the appendix looks wrong (though I think just due to typo; not something I noticed to affect any other part of the paper).

### Questions
1. (Repeated from above) Why is the non-scaled calibration function defined as it is in Eq 19, especially when $n_i \geq n_{id}$? There are many definitions that could satisfy property 1 (Eq 15). Also, if the point of the scaling is to be comparable to the Ent-Mut terms, why scale by Ent-Mut of the ID distribution plus a KL term rather than just the Ent-Mut term directly? 
2. Do the authors have any hypotheses as to why PHP and DEC by themselves each only minimally improve OOD detection performance in some cases?
3. What are the results of this method on "reverse" dataset pairs (e.g. ID MNIST vs. OOD FMNIST)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses the over-estimation problem in VAEs: VAEs often assign a higher likelihood to OOD datapoints than ID datapoints. In analyzing this issue, the paper brings forth two different possible reasons, namely (1) the prior choice $p(z)$ being Gaussian, (2) the entropy of ID data being much higher than OOD data. The paper does this analysis by decomposing the ELBO, and then proposes two approaches to mitigate these two factors. Combining these two approaches give an unified way of handling a VAE’s overestimation problem, and the authors evaluate their approach in a suite of unsupervised OOD detection tasks.

### Strengths
1. The decomposition of the ELBO, and the two factors given for VAEs over-estimation, is novel to the best of my knowledge. It is also a clever way of analyzing the problem.
2. Section 3.2, further analysis on Factor I. I like the simple to complex examples provided to show how $p(z)$ being a standard normal distribution can be an improper choice of prior when modeling a complex distribution.
3. The paper is well written and easy to read.
4. The authors have conducted a thorough set of experiments and ablations.

### Weaknesses
 **(Motivation)** Could the authors explain the motivation behind choosing unsupervised OOD detection and specifically VAEs? Typically, there are no shortage of labeled datapoints from the training distribution, so a few use-cases would be helpful. Also is there a particular reason for focusing on VAEs? Some prior successful unsupervised OOD detection method, such as DoSE [1], works on both VAEs and Glow, and LMD [2] uses diffusion models for OOD detection (diffusion models being the typical generative model of choice over VAEs these days).

**(Notation, section 2.1)** Why is $x = \textrm{ID}$ or $x = \textrm{OOD}$? A better notation is $D(x) = \textrm{ID}$ if $S(x) > T$, and so on, where $D$ is the ID-OOD classifier.

**(Definition 1, VAE’s overestimation)** The authors define over-estimation when the expected ELBO over the OOD distribution is larger than that on the ID distribution. This however, is a weak definition in the sense that it gives no guarantee about arbitrary samples from these distributions. For example, it is quite possible that due to overlaps between ELBO on ID and OOD data, there is no overestimation but a big fraction of the ID/OOD samples are misclassified.

For example, assume that the score function on the ID distribution has a distribution $N(10, 5)$, and that on the OOD distribution has a distribution of $N(9, 5)$. Then by definition 1, there is no overestimation issue in this case. However, it is easy to see that if we choose the threshold $T$ such that 95% of ID samples are classified as ID, then a big percentage of OOD samples would also be classified as ID. A better definition of over-confidence would take into account the threshold $T$, $P(S(x) < T | x \sim p_{id})$ and $P(S(x) < T | x \sim p_{ood})$.

While I understand that this definition is chosen to facilitate the theoretical discussion/make the proofs easier, it is important to acknowledge this weakness in the paper. 

**(More notations)** I am assuming $p_{\theta}(x|z)$ is the decoder distribution, and $p(x)$ represents the true distribution of $x$. This needs to be clearly stated and used in a careful manner. 

**(Equation 5)** Could the authors clarify the term $H_{q, p}(z|x) = -E_{p(x)q_{\phi}(z|x)} [log(p_{\theta}(z|x)]$ (equation 5)? The expectation is taken over the true distribution $p(x)$ but the term inside is the model distribution $p_{\theta}(z|x)$. This is not the conditional entropy of the variable $z|x$ in the usual sense, and some explanation/clarification of notation would be useful. It is possible the model distribution is not close to the true distribution. Is there some sort of assumption that they are?

**(Contribution 1 in introduction: dataset entropy mutual integration)** In the introduction, dataset entropy mutual integration is coined as:

>> “sum of the dataset entropy and the mutual information terms between the inputs and latent variables”

However, in page 4, we see that:

$$\textrm{Ent-mut} = H_p(x) + I_q(x, z) - I_{q, p}(x, z)$$

So it is not technically a sum of entropy and mutual information, as we subtract $I_{q, p}(x, z)$ in the expression. Also what is the relevance/meaning of $I_q(x, z) - I_{q, p}(x, z)$?

**(Table 1 and 2)** No error bar or uncertainty estimation is given. A lot of the methods have similar numbers, and without an error bar, it is hard to discern the results. I would request the authors to 

Run the experiments for 3 seeds, for each baseline, and report the standard error.
Bold the top performing method, and also any method whose average performance > lower bound on the top performing method’s performance. Any equivalent formulation is also good.

**I see that Table 10 and 11 in the appendix have the associated error bars**, but mentioning/referencing them in the main paper would be important. 

**(Lack of self-containedness)**

I was looking for limitations of the paper, and it is mentioned in the appendix K. I would request this to be moved to the conclusion section to make the paper more self-contained.


**(Nit: overclaiming)**

Section 3.2
>> the prior distribution $p(z) = N(0, I)$ is an improper choice for VAE when modeling a complex data distribution $p(x)$

This is overclaiming: 
1. what is the measure of complexity of $p(x)$? Its entropy/differential entropy? 
2. We have seen some examples when the prior being $p(z) = N(0, I)$ leads to a bad outcome. This does not prove this statement in a general sense. Better way to say this, use “may be an improper choice” instead of “is an improper choice”, unless the authors have a more specific theorem to present.

### Questions
**(Understanding Post-Hoc prior)**

Just to make sure I understand the method correctly: for PHP, one first trains a VAE using ELBO from equation 2:

$$ELBO(x) = E_{q_{\phi}(z|x)} [\text{log}p_{theta}(x|z)] - D_{KL}(q_{\phi}(z|x)||p(z))$$

And only once this is done, PHP trains a second LSTM to learn $\hat{q_{id}}(z)$ to match the learned $q_{id}(z)$ from the regular VAE training?

**(Error related to LSTM estimation)**

Does the method assume that the LSTM learned distribution $\hat{q_{id}}(z))$ matches $q_{id}(z)$? What happens when this match is not well, or $D_{KL}(\hat{q_{id}}(z)||q_{id}(z))$ is high? Then it seems that PHP should not work. This seems like a key assumption for PHP to work well.

**(Table 1)** 

Why are the methods in supervised/auxiliary column different between FashionMNIST/MNIST and CIFAR-10/SVHN?


**(Table 10 and 11)**

Why are the error rates of DEC 0 in table 10 and 11?


**(Additional experimental results)**

Would it be possible to produce table 1, but with CIFAR-100 used as the ID dataset? Most OOD detection papers report numbers on CIFAR-100, and it is regarded as a harder task than CIFAR-10.


**(Computational resources)**

How much additional computation time is required for this method, including training a separate LSTM for PHP? How does this compare with other baselines?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
