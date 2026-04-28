# Variational Learned Priors for Intrinsically Motivated Reinforcement Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Efficient exploration is a fundamental challenge in reinforcement learning, especially in environments with sparse rewards. Intrinsic motivation can improve exploration efficiency by rewarding agents for encountering novel states. In this work, we propose a method called Variation Learned Priors for intrinsic motivation that estimates state novelty through variational state encoding. Specifically, novelty is measured using the Kullback-Leibler divergence between a Variational Autoencoder's learned prior and posterior distributions. When tested across various domains, our approach improves the latent space quality of the Variational Autoencoder, leading to increased exploration efficiency and better task performance for the reinforcement learning agent.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an approach to provide intrinsic rewards based on state novelty for exploration in reinforcement learning. Previous work had proposed using the KL divergence between the posterior encoding of the state (learned through a VAE with ELBO) and a fixed prior (standard Gaussian). This paper identifies the misalignment of the fixed prior with encoded states as a crucial limitation of the previous work. It suggests a solution by using VAEs with a learnable prior. The paper studies many approaches to represent and learn more expressive priors, enabling better exploration than using a standard Gaussian prior VAE.

### Strengths
**S1.** The idea of Variation Learned Priors (VaLP) is simple and motivated well through latent space visualizations in simple settings. Compared to many complex ways to generate intrinsic rewards, this approach should be simple to implement and integrate with RL algorithms.

**S2.** The paper does a great job of comparing various approaches (flow-based, mixture of Gaussians, VAMP, GTM) to learning expressive priors with VAEs. Experiments clearly show the learned prior variants outperforming the bonus from VAEs with the standard Gaussian prior.

**S3.** The paper is well-written, and the key concepts are clearly explained and flow nicely.

### Weaknesses
 **W1.** While the experiments clearly show the benefit of VaLP over using a VAE with the standard/fixed prior, it is unclear if this approach outperforms ICM, RND, and DRND as claimed in Lines 500 and 501.

In the MiniGrid experiment, all approaches seem to have similar coverage (except VaLP$_{Flow}$, which does a bit better), and none are near the final room. Could these experiments be run for longer (more interactions) to gauge how the approaches perform further? Specifically, reporting coverage at various stages of learning would better highlight the early learning benefits of the proposed approach. The current results do not clearly demonstrate a significant advantage in exploration within the multi-room environment. 

In the Mujoco experiments, many intrinsic rewards do similarly well in HalfCheetah and Walker (2/4 environments). The caption for Figure 8 mentions, “in Ant-v4, $VaLP_{Flow}$ exhibits the strongest performance, with a final mean reward approximately 1000 points higher than the Standard prior method and baseline methods such as RND and DRND.” however, DRND performance seems to be quite close to $VaLP_{Flow}$. The performance differences in Ant-v4, while present, are not as substantial as the text suggests, and the overall performance across the MuJoCo suite is not consistently superior for VaLP.

It is also unclear how informative the Atari 100K experiments are with the chosen environments. Some of the environments (Gravitar, Pitfall, and PrivateEye) are probably too challenging in this setting for all considered approaches, and performance at 100K with DQN with intrinsic rewards may not convey how the approaches truly explore and will fare in the longer run. The limited interaction budget makes it difficult to assess the true exploration capabilities of each method in these complex environments. The results at 100K timesteps may not be indicative of long-term performance.

On a separate note (but related to the Minigrid comment), it would also be helpful to see how the VaLP agents perform in the detachment spiral experiment when it is run for longer, as no agent is close to finishing the spirals yet. Similar to the multi-room environment, reporting coverage and balance metrics at various stages of learning would be beneficial to showcase the early learning advantages of VaLP.

**W2.** The paper motivates using a learned prior through the observation that a standard Gaussian prior might lead to over-regularization. With that in mind, it would be important to know if the added complexity of VaLP can be avoided by using a larger latent dimension or a more expressive decoder architecture with standard prior VAEs. Are there any experiments/arguments showing that the above approach is insufficient? Or would using learned priors continue to help even with a larger capacity?

**W3.** While not strictly necessary, it would have helped to include pseudo-count density-modeling bonuses [1, 2] in the empirical comparison due to the similarity of using a generative model of observations for deriving intrinsic rewards.

### Questions
Included in the Weaknesss section.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper revisits an earlier intrinsic motivation algorithm in reinforcement learning (RL), identifies a limitation of this algorithm and proposes and tests a solution for this limitation. 

In particular, the paper considers an algorithm where a variational autoencoder (VAE) of the observations of an agent is learned in parallel with its policy. The reason to learn the VAE is to use the Kullback-Leibler divergence term in its ELBO loss as an intrinsic reward for the agent. The idea is that if a novel state is observed, the associated latent representations will not be captured by the latent prior distribution, that is, the divergence between the sample posterior and the prior will be large, and so the agent will be rewarded to visit again the atypical state. In this manner, the KL divergence rewards the novelty of a state. The limitation that the paper points out is that the standard VAE has a fixed prior that does not reflect the knowledge of the agent and this affects the quality of its sense of novelty. 

Following an existing solution in the more general setting of generative models, the paper proposes to update the prior with an approximation of the average of the sample posterior distributions. For this, four different types of generative models are considered, including mixtures of Gaussians and flow-based density estimators.  

The paper proceeds to test the proposed solution. First, as a sanity check, it shows how good are the generative models to fit an average of sample posterior distributions in a non-RL task in contrast with the fixed normal prior. After showing that the proposed models are useful, it provides evidence of the improvement obtained in the first state visitation or state space coverage in three exploration tasks. Finally, results in MuJoCo and Atari 100K are provided to show that the extrinsic reward can be maximized as a result of improved exploration.

### Strengths
Originality:
- The paper revisits an algorithm with potential but which had no major impact nor visibility. In this sense, it is original to identify the relevance of the algorithm and to propose a way to make it fulfill its potential. 

Quality:
- The paper is thorough in its empirical evaluation, including not so popular tabular environments and challenging and popular deep RL environments. It also includes multiple intrinsic reward algorithms as baselines, showing that the proposed solution works across environments and that it is competitive with existing techniques. 
- The paper provides strong evidence to conclude that using a fixed prior to assess state novelty with VAEs is inappropriate.
- The paper includes relevant references that allows the reader to assess its novelty.

Clarity:
- The paper is well organized. The earlier work, its limitation, and the proposed solution are well motivated and follow a logical order.

Significance:
- The paper provides some evidence for the final algorithm, VaLP, being competitive with other state-of-the-art exploration algorithms like RND.

### Weaknesses
I think it is fair to say that the paper is very incremental. It focuses on a limitation of VAEs that has been identified and solved already, as the Background section explains. In this sense, most of the work should lie on proving that the already existing solution has a significant impact in the context of intrinsic motivation. While the tabular experiments are conclusive regarding the inappropriateness of using fixed priors, I consider that the paper overclaims in the interpretation of the results and that the deep RL experiments are insufficient.

Why is the paper overclaiming?
- In Section 6.3, it is stated that VaLP$ _{\text{Flow}}$ covers a "wide range of states" while RND "trails behind the learned priors VaLP$ _{\text{Flow}}$". Without seeing the plot, some reader could infer that RND is a worse exploration algorithm. However, looking at Figure 6, the *only* method that leads to explore more than RND is VaLP$ _{\text{Flow}}$, it does only cover around 70% of the state space, and it is hard to tell if much can be inferred from visiting 6 more states after 500000 steps in a single seed.

- In Section 6.3.1, it is stated that "VaLP$ _{\text{Flow}}$ demonstrates strong exploration across both spirals, avoiding detachment". As per my understanding of the phenomena of detachment, this conclusion is confusing state space coverage with even visitation of states throughout an agents life. Figure 7 has no conclusive evidence regarding how even is exploration and, if anything, results seem to suggest that VaLP$ _{\text{Flow}}$ concentrates in one of the spirals in the last steps.

- In Section 6.4, is is stated that VaLP methods "demonstrate significant and reliable improvements over the Standard prior and baseline methods", that "in Hopper, VaLP$ _{\text{Flow}}$ shows dominant performance throughout training" and that "in Ant-v4, VaLP$ _{\text{Flow}}$ exhibits the strongest performance, with a final mean reward approximately 1000 points higher than (...) baseline methods such as RND and DRND". Again, from these claims the reader might conclude that VaLP$ _{\text{Flow}}$ is superior to any other exploration method. However, looking at Figure 8, this is very unclear:

    1. There are only 5 seeds per environment, which makes it difficult to make any strong statistical claim. 
    2. The shaded regions considering the standard error of the mean greatly overlap and it is difficult to tell whether a curve is inside or outside of a shaded region for most tasks. 
    3. Performance in Hopper is only 'dominant' after 500K steps.
    4. DRND arguably has a similar final mean as VaLP$ _{\text{Flow}}$ in Ant-v4 and any difference certainly lies under the statistical error.

- Similarly to previous cases, in Section 6.4.1, the VaMP models are described by qualifiers like "achieves the highest rewards", "leads", "outperform", and "top performer". However, I just see the same issues as before and new ones. Not only 5 seeds were used again, but there is no comment on statistical significance. In addition, it is not clear what kind of scale Figure 9 is using. If the original rewards are being used, most scores are significatively low, considering the average Human scores reported in previous papers like the following:
    a. Kaiser Ł. et al., Model-Based Reinforcement Learning for Atari, ICLR, 2020.
    b. Schwarzer M. et al., Bigger, Better, Faster: Human-level Atari with human-level efficiency, ICML, 2023.
Added to this, the paper introducing RND shows that solving tasks to an acceptable level like Gravitar requires approximately 500K steps. This leads me to conclude that the results shown might correspond to noise at the beginning of a learning curve and that the obtained behavior in the games is not satisfactory for any algorithm in most of the games being considered.

- Finally, in the Discussion and Future Work section it is stated that "this adaptability enables VaLP$ _{\text{Flow}}$ to excel across diverse tasks, leading to superior exploration and policy optimization in environments like MuJoCo and Atari". Considering the previous points, saying that the method excels and is superior is a big stretch.

### Questions
Questions:
- In the Atari 100K results, are the scores normalized against the average human scores? My guess is no since there are negative values.
- In the first-to-visit plots, why not just add a different color to not visited states? The value of 1000 seems arbitrary and might affect the conclusions about the exploration abilities of each model.
- Why does the scale in Figure 7 show values not present in the subplots?
- Why is it relevant to show the non-RL results? The fact that these models can approximate distributions has already been extensively studied, including the papers mentioned in the Background.
- Can you explain what is the difference between the results 6.2, 6.3, and 6.3.1? To me, the only difference is that a different tabular environment is considered. Given that the reward for DeepSweep is so sparse, I am not convinced that there is much difference with the other two cases either.
- In the Introduction, what does "latent space coverage" mean exactly? What is the formula to calculate it?
- In Line 518, in Page 10, why are non-linear dynamics mentioned? How are dynamics related with anything else in the manuscript?
- In the last paragraph, why would the learned priors be transferable? Also, what does it mean to identify the most effective learnable prior? This sounds just like a matter of using better generative models and following hyperparameter tuning.

Additional minor suggestions:
- Improve the explanation of the notation in the VAE subsection of the Background. In particular, there is unexplained or inconsistent notation.
- Unify the color palettes for Figures 4, 6, and 7.
- The last line in Page 1, "this weakens the intrinsic reward, which can result in inefficient exploration.", should start with uppercase.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes Variational Learned Priors (VaLP) for intrinsic motivation in reinforcement learning. VaLP improves exploration by using the Kullback-Leibler divergence between a learned prior and posterior distributions in a Variational Autoencoder. Unlike standard fixed priors, the learned priors dynamically adjust to the agent's experiences, creating a more accurate latent space that enhances novelty estimation and exploration. The authors introduce four types of priors—Mixture of Gaussians, Generative Topographic Mapping, VampPrior, and Flow-based prior—and validate VaLP across environments, demonstrating improved exploration and task performance over traditional intrinsic motivation methods in both discrete (Atari) and continuous (MuJoCo) settings.

### Strengths
1. Interesting qualitative results are presented, demonstrating the effectiveness of the proposed method.
2. Hyperparameters and detailed experiment settings are provided.

### Weaknesses
1. Some parts of the paper are hard to understand: the authors spend a lot of words explaining Figure 1 in the introduction section but it's still confusing to me. For example, what is latent space coverage? The authors link it to "how well the prior aligns with the encoded states" but it's still quite abstract - more intuitive explanations will help before talking about prior, posterior and latent space. Specifically, the concept of 'holes' in the latent space is not clearly defined, and it's unclear how these relate to exploration performance. MoG, GTM etc. are not introduced until section 4 which may make the readers wonder if these are previously proposed methods and the paper proposed a new method that outperforms these. In Section 4, more explanations of the fundamental difference between the four models will also make the paper more readable. For example, while all four methods are used to model the prior, the specific parameterizations and learning procedures for each are not clearly articulated, making it difficult to understand their individual contributions and limitations.

2. As the proposed intrinsic reward is just investigating different existing ways for modeling priors I would expect a thorough experiment section. The presented qualitative results are impressive, but I would like to see the quantitative results on more hard-exploration domains. A typical example is Ant-maze, which has been investigated by many prior exploration papers. Experiments on Ant-maze are valuable also because the presented results on mujoco tasks seem to be mixed in the paper. The lack of a consistent performance boost across all MuJoCo tasks raises questions about the robustness of the proposed approach. Furthermore, the absence of error bars in the initial presentation of quantitative results makes it difficult to assess the statistical significance of the findings.

### Questions
For Figure 3 and 9, what are the standard deviations for the results? Only presenting the means may make the conclusions from these results highly biased.

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
3

### Summary
This paper investigates the problem of prior/aggregated-posterior mismatch in the setting of VAE-based intrinsic motivation exploration. The authors argue that when measuring state novelties, using KL divergence between the posterior of a state and the prior can be misguided when the prior does not faithfully represent the aggregated posterior. The authors then proposed VaLP, which utilizes learned flexible priors, to mitigate this problem. Through extensive experiments, the authors showed that variants of VaLP (with differently parametrized priors) can outperform other exploration methods.

### Strengths
1. Extensive experiments in various domains, including static datasets (MNIST/FashionMNIST), toy RL environments such as DeepSea and Minigrid, and the more popular environments such as MuJoCo and Atari.

2. The experiments with toy RL environments are especially helpful for visualizing different behaviors

### Weaknesses
1. One challenge of exploration in RL is that data distribution can shift over time as the agent’s policy continues to improve, and I think it’s important to see whether the misalignment problem would also appear for VaLP. Currently, the misalignment figures (Fig1 and Fig2) both focus on fixed datasets, and it is not clear whether VaLP can solve the misalignment problem in the RL setting. One can test this by, for example, repeating the experiments in Fig1 every T steps using the states in the replay buffer. It would be particularly insightful to see how the learned prior adapts to the changing state distribution and whether the KL divergence between the prior and the aggregated posterior remains low throughout training. This is crucial for validating the core claim of the paper that VaLP mitigates the prior/aggregated-posterior mismatch.

2. The MuJoCo experiments are not really informative. Most of the algorithms seem to achieve similar performance, making it difficult to judge the effectiveness of the proposed method. Perhaps exploration is not the main bottleneck for these environments. Also, the TD3 baseline seems to underperform other open-source baselines (e.g., CleanRL [2]). For example, CleanRL’s TD3 can achieve 9583.22 ± 126.09 on HalfCheetah at 1M steps, but the scores reported by the authors are all below 8000. This discrepancy raises concerns about the implementation details and whether the baselines are adequately tuned for a fair comparison. Specifically, it would be beneficial to provide more details on the hyperparameter settings and training procedures for the TD3 baseline to ensure reproducibility and a more robust evaluation.

3. The Atari experiments are also problematic. For example, [3] reported that random uniform policies can achieve average scores of 1.70 on Breakout, 173.0 on Gravitar, and 24.90 on Private Eye. Yet, the authors reported scores close to or worse than the random baselines. Ultimately, I think comparing exploration methods with such a tight training budget (100k interactions) is not really meaningful. As the hard exploration problems often take millions if not billions of frames to solve even for SOTA algorithms (see [4] for example). The reported scores are significantly below what is expected, even for simple random policies, suggesting potential issues with the experimental setup or the implementation of the baselines. Furthermore, the extremely limited interaction budget makes it difficult to draw any meaningful conclusions about the long-term exploration capabilities of the proposed method.

### Questions
1. How does the misalignment problem evolve over training steps in the RL setting?
2. Can the authors explain the performance of VaLP on MuJoCo and Atari?

Minor suggestions:
1. On line 95, the expectation is missing for the definition of expected return.
2. For the Deep Sea experiments, I think it would make sense to also report the training curves (cumulative rewards) to demonstrate the exploration-exploitation tradeoff, as the environment is not purely explorative (the extrinsic rewards are not zero).

### Soundness
2

### Presentation
3

### Contribution
2
