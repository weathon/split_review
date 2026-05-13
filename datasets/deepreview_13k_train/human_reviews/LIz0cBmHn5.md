# Investigating Mixture Policies in Entropy-Regularized Actor-Critic

- Decision: Reject
- Scores: 5, 3, 3, 5, 5

## Abstract
We study mixture policies in entropy-regularized reinforcement learning. Mixture policies offer greater flexibility than base policies like Gaussians, which we show theoretically provides improved solution quality and robustness to the entropy scale. Despite these potential benefits, they are rarely used for algorithms like Soft Actor-Critic, potentially due to the fact that Gaussians are easily reparameterized to get lower variance gradient updates, but mixtures are not. We fill this gap, introducing reparameterization gradient estimators for the mixture policy. Through extensive experiments on environments from classic control, MuJoCo, the DeepMind Control Suite and a suite of randomly generated bandits, our results show that mixture policies explore more efficiently in tasks with unshaped rewards (across entropy scales), while performing comparably to base policies in tasks with shaped rewards, and are more robust to multimodal critic surfaces.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the use of mixture policies in entropy-regularized actor-critic algorithms for reinforcement learning in continuous action spaces. The authors present theoretical properties of mixture policies, showing they have a higher regularized objective and a higher unregularized objective if an entropy-constrained optimization is used as compared to base unimodal policies (single Gaussian policies). They derive two reparameterization gradient estimators for mixture policies: a partial "half-reparameterization" with unbiased gradients and a full reparameterization with biased gradients using the Gumbel-softmax trick. Experiments are conducted on MuJoCo, DeepMind Control Suite, OpenAI classic control environments, and continuous bandits.

### Strengths
1. The paper introduces novel reparameterization gradient estimators for mixture policies, filling a gap in the literature. Prior work [1] did not utilize a learnable weighting policy to combine the mixture components that this paper addresses.
2. It improves on existing work, SACM [1], that also investigated mixture policies and updated them using stochastic gradients. While SACM does not report any clear benefits of using it over base policies (SAC), this paper provides claims and evidence of their benefits in sparse reward settings.
3. Theoretical foundations are well-established, providing a solid basis for the proposed methods.
4. Experimental validation across diverse environments supports claims that mixture policies are comparable to unimodal policies in terms of performance.
5. The paper is well-structured, with clear explanations of the motivation, methods, and results.
6. Visualizations (Figures 1 and 5) effectively illustrate key points and findings.

[1] Baram, Nir, Guy Tennenholtz, and Shie Mannor. "Maximum entropy reinforcement learning with mixture policies." arXiv preprint arXiv:2103.10176 (2021).

### Weaknesses
1. The sparse reward environments investigated in the paper are simplistic. ‘Pendulum’, ‘MountainCar’, and ‘Acrobot’ are generally treated as toy domains. Experiments on more realistic sparse-reward domains such as ‘Fetch’ [2] and/or ‘Adroit’ [3] domains are missing. This limits the applicability and scalability of the proposed methods. Specifically, the lack of complex, high-dimensional environments with sparse rewards makes it difficult to assess the true potential of mixture policies in challenging scenarios. For example, tasks involving manipulation or locomotion in cluttered environments would provide a more rigorous test of the proposed approach.
2. Comparison of the proposed methods against existing work using mixture policies such as SACM [1] in Section 5.
3. A discussion on the benefits of using mixture policies as opposed to using a mixture of critics as done in prior work such as D4PG [4] and PMOE [5] is missing. This is a crucial omission, as the choice between mixture policies and mixture critics can significantly impact performance and sample efficiency. A detailed analysis of the trade-offs between these two approaches is needed to justify the focus on mixture policies.
4. Analysis of the potential downsides of learning mixture policies in terms of the compute requirements hasn’t been discussed, e.g., the tradeoff between wall clock time and sample complexity, etc. The computational overhead of maintaining and updating multiple policy components, along with their associated weights, could be substantial, especially in high-dimensional action spaces. A thorough investigation into the computational cost and its impact on training time is necessary to evaluate the practical viability of the proposed methods.

### Questions
1. As shown in Figure 5, the Q-value estimates are noisy for sparse-reward ‘MountainCar’. Could the authors shed some light on how learning the mixture weighting policy as opposed to a fixed weighting policy as used in [1] is particularly helpful in such cases?
2. Just out of curiosity, did the authors observe any specific benefits or have a strong motivation behind training mixture policies using stochastic gradients as opposed to deterministic gradients?

[1] Baram, Nir, Guy Tennenholtz, and Shie Mannor. "Maximum entropy reinforcement learning with mixture policies." arXiv preprint arXiv:2103.10176 (2021).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper (re-)introduces the use of mixture policies into policy gradient methods for entropy-regularized reinforcement learning (RL). The mixture policies considered consist of convex combinations of component policies, where the convex weightings are themselves a parameterized function. The primary component policies considered are Gaussian policies and modifications thereof, and the primary RL method considered is Soft Actor-Critic (SAC). Theoretical results are provided for the bandit setting showing that mixture policies perform at least as well as their component policies and any first-order stationary point of the component policies also corresponds to a stationary point of any associated mixture policy. To enable the variance reduction benefits of reparametrized policy gradients, half- and fully-reparametrized policy gradient theorems are derived, where the half reparametrization reparametrizes only the component policies, while the full reparametrization employs a Gumbel-softmax scheme to reparametrize the weighting function as well. Experimental results on MuJoCo and DeepMind control benchmark tasks are provided that compare SAC using mixture policies with vanilla SAC using non-mixture policies. The results indicate that mixture policies result in improved performance over vanilla SAC on sparse-reward tasks, likely due to improved exploration.

### Strengths
The key contributions of the paper include:
1. Mixture policies are reintroduced, primarily for use with SAC. Note that mixture policies were previously introduced (see related works in appendix), but not extensively studied.
2. The experimental results suggest that mixture policies lead to improved exploration in sparse-reward settings.
3. The theoretical results for the bandit setting provide some reassurance as to the usefulness of mixture policies.

### Weaknesses
The paper suffers from several drawbacks:
1. The experimental results are limited and inconclusive. While mixture policies are shown to lead to improved ending performance on some (not all) of the sparse-reward (I understood "shaped" as referring to dense rewards and "unshaped" as referring to sparse rewards) tasks considered, the performance improvement is marginal on most problems. Though this indicates that mixture policies are potentially promising and worth further investigation, the results are suggestive rather than conclusive. More importantly, no comparisons of the proposed mixture policies with comparable exploration-oriented methods are provided, despite the existence of many such methods in the literature (e.g., [Kobayashi, 2019] and [Bedi et al., 2024] mentioned in the introduction). Without such comparisons, it is unclear how the contribution of this work fits into the broader literature.
2. The main theoretical results of Sec. 3 are for simple bandit settings, seriously limiting the significance of the results provided. The proofs appear to be straightforward (I skimmed but did not verify in detail the appendix), containing no major technical innovation to bolster the significance of the analysis. In addition, some Sec. 3 results are not particularly helpful: Prop. 3.2 provides bounds for entropy-constrained problems (not considered elsewhere in the paper) without relating these back to the entropy-regularized problems under consideration; Prop. 3.3 shows that a simple Gaussian policy may fail to have a stationary point, while Prop. 3.4 shows that any stationary point for all component policies is also a stationary point for all corresponding mixture policies -- this does not show that mixture policies have stationary points even when component policies do not, however, which is what we appear to be promised at the beginning of Sec. 3.2. This confusion weakens the theoretical contribution of the paper.
3. The reparametrization policy gradient results of Sec. 4 are poorly motivated: variance reduction is the primary motivation for the use of reparametrized policy gradients, yet the new reparametrizations provided lack variance reduction guarantees, as admitted at the beginning of Sec. 4.1. This raises the question: why should we do reparametrization at all? The lack of clarity on this point detracts from the overall motivation of the approach.
4. Mixture policies are not new. The third paragraph of the introduction as well as the appendix provide a number of references considering them. It is hypothesized in the introduction that "lack of reparametrization estimators for mixture policies" might be the reason mixture policies have not gained more widespread use, but it is left unclear what challenges the lack of such estimators present. Overall, the paper seeks to join the existing literature on mixture policies, but it is unclear how the paper improves over that literature. Yes, reparametrization estimators are provided, but it is unclear why they are needed (and also see issue 3 above).

### Questions
1. Have you compared the use of mixture policies with other exploration-inducing policies (e.g., heavy-tailed policies)? If not, why not?
2. What are the main technical innovations that were necessary to performing the analysis?
3. How does Prop. 3.2 relate to the rest of the paper?
4. How do Prop. 3.3 and 3.4 together demonstrate that mixture policies "may have stationary points in scenarios where the base policy does not"?
5. What is the primary purpose of the reparametrization results of Sec. 4? Are they necessary for subsequent use in SAC? Are no variance bounds possible?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates mixture policies in entropy-regularized reinforcement learning, highlighting their advantages over traditional base policies like Gaussians. It provides theoretical insights into their improved solution quality and robustness, while addressing the challenges in implementing these policies effectively in algorithms such as Soft Actor-Critic.

### Strengths
a). The paper provides solid theoretical backing for the proposed methods, elucidating their benefits over conventional Gaussian policies.

b). The focus on multimodal entropy-regularized frameworks is timely, considering the current trends in reinforcement learning research.

### Weaknesses
a). There is no performance gain in complex environments (such as Hopper, Walker, Ant, Humanoid, etc.), and the effective shaped reward environments only demonstrate improvements in simpler environments (like Pendulum, Acrobot, Mountain), which is not very convincing.

b). The figures in the third row of Fig 4 actually demonstrates hyperparameter sensitivity rather than the robustness described in line 371. Although the return is higher than Rep-Squashed, the larger variation compared to Rep-Squashed when $\alpha$ changes indicates that hyperparameter sensitivity is not as good as that of Rep-Squashed. Additionally, testing for robustness should involve adding noise to the observations.

c). It is not enough to only compare with SAC. The paper should compare with Daniel (2012), Celik (2022), Nematollahi (2022), and Seyde (2022). These algorithms are all mixture policies (the author describes in Appendix A). Also, the paper should compare with Hou (2020), Baram (2021).

### Questions
In Figure 1 (left), the GM policy does not completely fit the reward function. What is the reason?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the use of mixture policies in entropy-regularized reinforcement learning, highlighting their flexibility compared to base policies like Gaussians. The authors theoretically demonstrate that mixture policies can improve solution quality and robustness to entropy scaling. They address the challenge of reparameterization for lower variance gradient updates, introducing novel reparameterization gradient estimators for mixture policies. Extensive experiments across various environments reveal that mixture policies enhance exploration efficiency in tasks with unshaped rewards while maintaining comparable performance to base policies in shaped reward scenarios, and exhibit greater robustness to multimodal critic surfaces.

### Strengths
1. The paper introduces reparameterization gradient estimators for entropy-regularized reinforcement learning.
2. Theoretical analysis demonstrates that the Gaussian mixture model (GMM) policy outperforms the base Gaussian policy.

### Weaknesses
1. The paper lacks motivation regarding the necessity of the reparameterization gradient estimator. Specifically, while the authors mention that the likelihood ratio estimator can be applied to GMM policies, they do not adequately explain why a reparameterization approach is needed. The argument that it fills a gap in the literature is not sufficient justification; a clear demonstration of the practical benefits, such as variance reduction, is required. The paper should provide a theoretical comparison of the variance of the likelihood ratio estimator and the proposed reparameterization estimator in the context of GMM policies, and empirically demonstrate this reduction. 
2. The authors should clarify the novelty of their work. While they mention that similar gradient estimators have been used in discrete action settings and multi-agent settings, it is not clear if the specific reparameterization gradient estimator proposed for mixture policies is novel in the context of entropy-regularized RL. A more detailed comparison with existing reparameterization techniques, especially those used in similar RL settings, is needed to establish the novelty of the contribution. The paper should also clarify if the proposed estimator has been used in other entropy-regularized RL contexts, and if not, why it is particularly suited for this setting.
3. In Section 3, the authors assert that "the mixture policy is at least as good as or better than the base policy." While the claim of "at least as good" is theoretically supported, the assertion of "better" lacks a rigorous theoretical backing. The counterexample provided is not a sufficient proof of the general case. A more formal theoretical analysis is needed to demonstrate the conditions under which the mixture policy provably outperforms the base policy, and this should be clearly stated in the paper.
4. The authors mention that Gumbel reparameterization introduces bias. However, there is no analysis on the scale and impact of this bias on gradient estimation. The paper should include a quantitative analysis of this bias, and discuss how it affects the convergence and stability of the learning process. It would be beneficial to see experiments that vary the temperature parameter of the Gumbel-softmax and show how this impacts the training process.
5. In Section 6, line 510, the authors state that "the primary limitation is that we used default hyperparameters for the mixture policies in MuJoCo; such defaults were tuned for SAC with the base policy." This is a significant limitation that undermines the validity of the experimental results. The authors should discuss additional limitations regarding their theoretical analysis and experimental settings, such as the limited scope of environments and the lack of analysis on the sensitivity of the method to hyperparameter choices.

### Questions
1. The motivation for this work is insufficient. Given that the basic likelihood ratio gradient estimator can be applied in the GMM context, what is the rationale for developing the reparameterization gradient estimator? If the aim is variance reduction, the authors should emphasize the theoretical improvements and provide empirical evidence supporting this reduction compared to other estimators like the likelihood ratio estimator, which is currently lacking in the paper.
2. The authors should clarify the novelty of their work. Is the proposed reparameterization gradient estimator used in other reinforcement learning contexts beyond entropy-regularized RL?
3. In Section 3, the authors assert that "the mixture policy is at least as good as or better than the base policy." While the claim of "at least as good" is theoretically supported, how is the assertion of "better" supported theoretically?
4. The authors mention that Gumbel reparameterization introduces bias. Is there any analysis on the scale and impact of this bias on gradient estimation?
5. In Section 6, line 510, the authors state that "the primary limitation is that we used default hyperparameters for the mixture policies in MuJoCo; such defaults were tuned for SAC with the base policy." The authors should discuss additional limitations regarding their theoretical analysis and experimental settings.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the role of mixture policies in entropy-regularized reinforcement learning. The authors argue that mixture policies can provide better solution quality and robustness compared to standard Gaussian policies. The study aims to bridge the gap in existing algorithms, specifically addressing the challenges associated with the reparameterization of mixture policies.

### Strengths
1. The exploration of mixture policies introduces a novel perspective in reinforcement learning, potentially enhancing performance.
2. The theoretical framework is robust, providing a solid basis for the claims made regarding performance improvements.

### Weaknesses
1. Lack of comprehensive comparisons with other advanced algorithms that also utilize multimodal policies, e.g. diffusion models that mentioned by the author in the third paragraph of introduction. These models must be considered as baselines in the experiments because the proposed mixture policy has the same aim with them, i.e. multimodal ability.
2. The algorithm seems to be effective only in shaped-reward environments, which are constructed by the authors on purpose. The effectiveness of algorithm should be tested in general environments, rather than designing a special environment tailored specifically for the algorithm after it has been proposed.
3. The computation time efficiency is not elaborated. It is important for performance to be high within acceptable time efficiency. The paper should include comparisons of network forward time, backward time, and the training wall time.
4. Lack the analysis for the number of mixture policies, i.e. $N$. In complex environments, this hyperparameter may be vital. The sensitivity analysis should be implemented.

### Questions
1. How is it compared to advanced algorithms that also utilize multimodal policies, e.g. diffusion models?
2. Are there general scenarios or tasks (not shaped-reward envs) where mixture policies significantly outperform Gaussian policies?
3. How about the computation time efficiency of the proposed mixture policy?
4. Does the hyperparameter $N$ affect a lot?

### Soundness
2

### Presentation
2

### Contribution
3
