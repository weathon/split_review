# Exploring Deep Learning Parameter Space with a-GPS: Approximate Gaussian Proposal Sampler

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 3, 1

## Abstract
To trust the predictions provided by deep neural networks we need to quantify the uncertainty. This can be done with Bayesian neural networks. However, they require a trade-off between exactness and effectiveness. This paper introduces a new sampling framework: Adaptive Proposal Sampling (APS). APS is a mode seeking sampler that adapts the proposal to match a posterior mode. When modes overlap, APS will adapt to a new mode if it draws a sample that belongs to a new mode. A variant of APS is the approximate Gaussian Proposal Sampler (a-GPS). We show that it becomes a perfect sampler if it has the same score function as the posterior. With a warm-start of a pretrained model, combined with stochastic gradients it scales up to deep learning. Results show that a-GPS 1) proposes samples that are proportional to a mode, 2) explores multi-modal landscapes, 3) has fast computations, 4) scales to big data. Immediate results suggest that this framework may be a step towards having both exactness and effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a sampler that samples weights via traversing the loss landscape of a pre-trained deep neural network via a series of normal distributions. The approach is evaluated on a series of classification and out-of-distribution detection tasks.

### Strengths
The paper proposes a sampler that samples weights via traversing the loss landscape of a pre-trained deep neural network via a series of normal distributions. The approach is evaluated on a series of classification and out-of-distribution detection tasks.

### Weaknesses
 - The main weakness of the paper is in the experimental evaluation. The experiments show convincingly that the proposal works with several architectures and several classification data sets (no regression tasks were evaluated). What it does not show is that it works better than its baselines, i.e., why should it be used instead of SWAG, or SGD-MC? E.g., SGD-MC almost always outperforms it (it is missing from Table 4, but the results in Table 13, show that it clearly performs better), except for the strange behavior in Table 6.


- The presentation of the paper is rather sub-optimal. E.g.,
    - parameters such as $c$ and $\lambda$ appear in the text long before they are even introduced, if at all. The important $\lambda$, e.g., only is further detailed in Algorithm 1.
    - The writing contains a lot of typos, e.g., for the first paragraph on the second page
        - "full-gradient MCMC similar **to** SG-MCMC"
        - "SGLD **has** fast computations but **suffers** form inefficient explorations"
        - "Previous **works** on state dependent"
    - Dropout's absence in most of the results is not explained in the main text but only appears in the one table where it is present rather than absent
    - The writing is somewhat repetitive
    - The reference list is full of arxiv preprints instead of the actual publications
    - Table 4 contains wrong highlights in two columns (ECE and NLL), the same is true for several tables in the appendix.
    - On the positive side, however, other details, like definitions of performance metrics are highlighted prominently

### Minor
- SGD-MC is mentioned in the text for Table 4 but not in the actual results
- LA is missing in Table 3 without an explanation
- Sec 2.1: "the loss function, ..., typically cross-entropy is interpreted as the negative log-likelihood". Cross-entropy is typical for classification tasks, but not for any other tasks. And in this case, it is not just interpreted as a negative log-likelihood, _it is_ the negative of a categorical distribution. 
- For the posterior in  (15). A Gaussian prior is $\exp(-||\theta||)$, similarly for the loss factor. This directly provides you with (17) instead of having to redefine anything.
- Sec 3.2.2 "separated by high loss area". As Draxler et al. (2018) and Garipos et al. (2018) show there are a lot of paths of similar loss between a lot of maxima instead of a clear separation. (These motivated the SWA baseline of the present work)

### Questions
- The conclusion only discusses a-GPS' performance with respect to SWAG and Laplace. Can the authors additionally provide a deeper discussion on their relation to SGD-MC and in general summarize why their approach should be picked instead of these established baselines?
- SGLD is mentioned in the related work, but never used in the experiments. Can the authors comment on this lack of comparison? Especially since they cite Izmailov et al. (2021) who showed good results for this approach.
- A lot of approaches and networks diverged or failed otherwise throughout the experiments. Can the authors give further details? E.g., it seems rather strange that a simple model such as VGG should diverge on a straight-forward classification task such as CIFAR100.
- The method was only tested on classification tasks. What about regression problems? Do the authors expect a similar performance? 
- How is the split in CIFAR10 and CIFAR 100 in 5/50 classes decided? _(Apologies if I missed it somewhere in the appendix)_

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new sampling algorithm for multi-modal distributions, especially deep neural network posteriors. Specifically, the authors learn an adaptive Gaussian proposal along with sampling. Several experiments, including synthetic distributions and deep learning tasks, are conducted to test the proposed method.

### Strengths
1.	The studied topic of sampling on multi-modal distributions is important.
2.	The proposed algorithm is simple to implement in practice.

### Weaknesses
1.  The proposed method does not achieve what it claims to “having both exactness and effectiveness”. Apparently, the method is not exact without the MH correction step. The method is only exact when the target distribution is a Gaussian with a diagonal covariance, which is a trivial case. I’m not sure what “perfect sampler” means in the paper. Overall, I think many claims need to be modified in order to be accurate and rigorous.
2.  The methodology of the proposed method is confusing. The algorithm does not have a component to encourage exploring multiple modes. It is unclear to me how the method manages to find diverse modes.
3.  Algorithm 1 seems to find a Gaussian distribution to approximate the target distribution. How is it different from variational inference? What are the advantages?
4.  Why does the proposed method require a pretrained solution, theta_MAP? Will it work if training from scratch? 
8.  I do not follow the reason for introducing the variance limit lambda. Why does the method need it?
9.  The experimental setups and results are confusing. It is unclear if the authors also use a pre-trained solution for the baseline NUTS in S3.1. If not, then it is unfair to claim faster convergence of the proposed method than NUTS. Besides, given that the method uses a pre-trained solution, it is unsurprising that “We found that a-GPS converges so fast that a burn-in period was unnecessary”. For the time comparison, it is unclear if the authors include pre-training time.
10. For deep learning experiments, it will be better to include MCMC baselines, e.g. Zhang et al, as the proposed method belongs to MCMC methods. To show the samples are from diverse modes, the authors can visualize weight space and function space, similar to those in Zhang et al.

### Questions
1.	Why is LA’s inference time even less than MAP? Why is the proposed method’s inference time less than SWAG? Does the proposed method use Bayesian model averaging during inference?

### Soundness
1 poor

### Presentation
2 fair

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
This paper proposes an adaptive proposal sampling (APS), a mode seeking sampler that adapts the proposal to match a posterior mode.

### Strengths
The proposed ``adaptive proposal sampler'' appears to be new in the literature.

### Weaknesses
1. Extension of the proposed sampler to high-dimensional problems is questionable. As mentioned in the paper, the parameters are regarded as independent of each other, making the proposed sampler less accurate and thus less attractive. This independence assumption, while simplifying computation, neglects the complex correlations that often exist between parameters in high-dimensional spaces, potentially leading to a poor approximation of the true posterior distribution. In practice, this could manifest as the sampler exploring regions of the parameter space that are highly improbable under the true posterior, thus reducing the efficiency of the sampling process.

2. When the modes of the target distribution are well separated, it is difficult to believe that the proposed sampler can efficiently traverse the entire energy landscape because, similar to the Metropolis-Hastings algorithm, the proposed sampler lacks a mode-escaping mechanism. The proposal mechanism, which is based on local gradients, may struggle to overcome the energy barriers between distinct modes. This can result in the sampler getting trapped within a single mode, failing to explore the full posterior and thus underestimating the uncertainty.

3. For the exact Gaussian proposal sampler, the acceptance rate can be low when the dimension of \theta is high. The high dimensionality exacerbates the curse of dimensionality, causing the proposal distribution to become increasingly diffuse. This can lead to a very low acceptance probability, where the vast majority of proposed samples are rejected, making the sampling process highly inefficient and computationally expensive.

### Questions
1. If the exact GPS is applied to the numerical examples of the paper, will the reported results be improved? How much?   

2. The proposed method needs to compare with more baseline methods, such as SGHMC [1]  and adaptively weighted SGLD [2], on multi-modal and high-dimensional problems.

References: 

[1] Chen et al. (2014) Stochastic Gradient Hamiltonian Monte Carlo. ICML 2014. 

[2]  Deng et al. (2022) An adaptively weighted stochastic gradient MCMC algorithm
for Monte Carlo simulation and global optimization. Statistics and Computing, 32:58.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method to obtain Gaussian approximations of posterior distributions in Bayesian deep learning. The experiments compare the proposed method against several related approaches on toy experiments as well as classification on CIFAR-10/100 and ImageNet.

### Strengths
The authors report that their method tends to produce samples quicker than competitor methods.

### Weaknesses
The paper is definitely still a work in progress and not ready for publication at a conference like ICLR.
Thus, I vote for rejection and encourage the authors to completely revise their manuscript and submit to another venue.

The writing style and organization of the paper is very bad, which makes it extremely hard to follow. In particular, the theoretical exposition is lacking:
- The theory is mixed with the related work (Eqs. (1)-(3), last Sec. of 1.1)
- Central notions and symbols are not introduced, the exposition remains very handwavy. To name only a few examples:
  - what do the authors mean by "transforming a pretrained into a Bayesian model"?
  - background on MCMC, Metropolis-Hastings corrections
  - definition of a "perfect sampler"
  - how do the authors define a "mode-specific MH"
  - it remains unclear in which sense the proposed method better deals with multi-modal posteriors than related work
  - definition of notion of time step $t$ and $\theta_t$ in Eq. (4)
  - definition of $D_x$, $D_y$ in Eq. (15, 16)
  - definition of $\mathrm{Conf}$ in Eq. (20)
  - ...
- The experimental evaluation is not convincing.
  - While the authors report fast sampling, their approach is outperformed by competitor methods most of the time.
  - On the simplest toy example (unimodal Gaussian posterior), the authors report good results in terms of effective sample size (which is not very surprising because they use the correct approximation). However, they do not report ESS on the mixture model (Figure 2 RHS). 
  - The authors argue that their method deals well with multi-modal posteriors. Thus, they should compare
 against other methods that capture multiple modes, i.p., Deep Ensembles [1] and Multi-SWAG [2].
  - As the authors employ a Gaussian posterior approximations, they should compare against variational Gaussian approximations, e.g., BayesByBackprop [3].

### Questions
Please elaborate on the concerns raised below "Weaknesses".

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
