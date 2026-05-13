# Noise-conditioned Energy-based Annealed Rewards (NEAR): A Generative Framework for Imitation Learning from Observation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
This paper introduces a new imitation learning framework based on energy-based generative models capable of learning complex, physics-dependent, robot motion policies through state-only expert motion trajectories. Our algorithm, called Noise-conditioned Energy-based Annealed Rewards (NEAR), constructs several perturbed versions of the expert's motion data distribution and learns smooth, and well-defined representations of the data distribution's energy function using denoising score matching. We propose to use these learnt energy functions as reward functions to learn imitation policies via reinforcement learning. We also present a strategy to gradually switch between the learnt energy functions, ensuring that the learnt rewards are always well-defined in the manifold of policy-generated samples. We evaluate our algorithm on complex humanoid tasks such as locomotion and martial arts and compare it with state-only adversarial imitation learning algorithms like Adversarial Motion Priors (AMP). Our framework sidesteps the optimisation challenges of adversarial imitation learning techniques and produces results comparable to AMP in several quantitative metrics across multiple imitation settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a method to use generative adversarial networks in an imitation learning framework. The general idea is to create a reward function using the concept of energy from a generative network which is a metric for how close a sample is to being from a distribution. They directly optimize on this energy metric as a reward and perform experiments in high dimensional locomotion settings. They find their method is able to outperform baselines in some situations but ends up struggling in situations with data scarcity.

### Strengths
The research problem for this work is good. Imitation learning is a reasonable method for many control tasks where reward is difficult to specify and expert data is available. Aiming to improve the imitation policy from samples is an interesting a relevant problem.

The novelty of this work seems good but it is slightly difficult to tell (see weaknesses).

The algorithm details seem good. It is unclear to me what “until horizon” means in line 230 and 231. Other than that the algorithm description is clear.

At a high level the experimental section is good. I think the presentation could be improved slightly and have questions about the baselines and statistical rigor. The discussion is interesting and provides insight into the method.

Ablation Studies are good. The discussion on the importance of annealing is interesting and relevant.

Failure Analysis is great. I really like the analysis and discussion of the reasons for failure. I think that leads to better future work and adds to the significance of this work.

Conclusion is good. I wish there was a future work section. Maybe more work into your annealing strategy?

### Weaknesses
I feel like as well the sentences from 71-77 are pretty vague and I would appreciate you explicitly stating the challenges clearly and then comparing your work even if is just “our method has smooth distributions and…”. The related work also seems to be wrapped in the intro which is fine but I would appreciate a more explicit comparison of other methods. Currently it simply says “this is what other methods do” instead of “here is how ours is different” which would make it easier to tell novelty.

The significance of this work seems good but it would be nice if the contribution was more explicitly stated. My interpretation was that the contribution is the use of energy based diffusion to train imitation learning but it would be better not to leave it up to the reader.

Baseline comparisons are ok (see questions).

The presentation of results is ok but I wish the tables were bigger sized, I’m pretty sure the page limit is 10 so you should be able to simply increase the size.

The statistical rigor is ok. You say each is trained 5 times and it is the results are averaged across 20 trials. 5 seems low to me here. Especially since the confidence intervals seem to be sort of wide and overlapping. Doing maybe 20 or 30 would be much better unless this is prohibitively expensive.

The clarity is ok. I didn’t find this paper very easy to read. Generally, I think more intuition could have been used in the paragraphs that starts at 167, 189 and 154. I’m admittedly not extremely versed in GANs but I think it should be written to provide more intuition to non GAN experts and more RL experts (as that is the target audience in my opinion). As well, I don’t feel the figures are helpful at all. I don’t understand what figure 1 is trying to convey nor do I understand even what it means. As well figure 3 also doesn’t make sense to me.

### Questions
iI there a reason you only compare to one baseline? Is that the only state of the art method and nothing can generally do better than it? I see line 364 says that it achieves superior results but is there truly no other baseline that even comes close? If so then that is fine. 

Is this the only/first work that uses energy-based diffusion models? If it is I would appreciate you explicitly saying so.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Noise-Conditioned Energy-based Annealed Rewards (NEAR), a novel framework for imitation learning from observation using energy-based generative models. NEAR leverages denoising score matching to learn smooth representations of the expert's motion distribution and uses these energy functions as rewards. Unlike adversarial imitation learning approaches, NEAR avoids unstable min-max optimization, achieving smoother and more stable reward signals. Additionally, an annealing strategy progressively transitions between energy functions to provide more refined guidance for the agent’s policy. NEAR is evaluated on complex humanoid tasks, showing promising results when compared to state-only adversarial imitation learning baselines like Adversarial Motion Priors (AMP) in terms of motion quality, stability, and imitation accuracy.

### Strengths
1. NEAR performs well on a range of complex motion tasks, including stylized walking, running, and martial arts. The results demonstrate competitive imitation accuracy and smoothness compared to AMP, particularly in complex tasks where AMP struggles with stability.
2. The paper includes ablation studies to explore the impact of key components.

### Weaknesses
1. NEAR’s effectiveness is primarily evaluated in humanoid tasks, which are continuous and physics-driven. The framework’s applicability in other types of imitation learning tasks, especially those with discrete actions or diverse goal-oriented, is not fully explored. Specifically, the paper lacks any analysis of how the method would perform in environments with sparse rewards or where the expert demonstrations are not smooth and continuous. The reliance on denoising score matching, which assumes a smooth underlying data distribution, might be a limiting factor in such scenarios. Furthermore, the method's performance in tasks with high stochasticity or multi-modal behavior is unclear.

2. NEAR requires training a noise-conditioned energy model, which can be computationally intensive. A detailed comparison of training costs relative to other methods, particularly in terms of time and resources, would be beneficial. The paper does not provide a breakdown of the computational cost associated with training the energy model versus the RL policy, making it difficult to assess the overall efficiency of the method. It would be useful to know how the training time scales with the dimensionality of the state space and the number of expert demonstrations. The lack of a direct comparison of GPU hours or training time with AMP makes it difficult to assess the practical overhead of NEAR.

3. NEAR is only compared against one baseline - AMP and it doesn't seem to always be the winner (but has higher variance in most cases) despite the additional complexity of learning an energy network. The paper would benefit from a more comprehensive comparison against other imitation learning techniques, especially those that do not rely on adversarial training. The higher variance observed in NEAR's performance, despite its more complex reward learning mechanism, raises questions about its robustness and practical applicability. It is unclear if the increased complexity of the energy network is justified by a significant improvement in performance over simpler methods.

### Questions
Could you provide a comparison of NEAR’s computational requirements (e.g., training time, GPU hours) relative to other baselines like AMP?

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
This paper proposes a method to perform imitation learning in absence of the expert's actions (i.e., only having access to the state trajectories). The proposed algorithm, NEAR, uses noise-conditioned score networks to model the probability distribution of the trajectories in the dataset. In this way, NEAR obtains a reward signal for imitation learning that does not depend on an adversarial network, as it is the case in current state of the art methods like AMP. In this way, known issues with learning in an adversarial setting are avoided. NEAR successfully learns to imitate reference trajectories, with similar performance to AMP and with smooth motion.

### Strengths
The paper is very well written. The algorithm presented in this paper (NEAR) is explained in detail. The authors clearly explain how this work is positioned within the field of motion imitation, providing helpful context information about adversarial imitation learning and noise-conditioned score networks.

### Weaknesses
It is unclear how Figure 1 has been generated. It is used for illustration purpose, however some more information about the energy function and the adversarial reward are necessary. I also do not understand the choice of using different scales for the two rewards, and why the energy is high around the agent's trajectory while the advesarial reward is low. I would ask the authors to detail how the energy function and the adversarial reward have been learnt (also in the supplementary material if it does not fit the main text).

The comparison with adversarial imitation learning methods is clear and well done. However, another possibility for imitation learning would  be, e.g., to just provide a reward signal in the form of the L2 distance between the states visited by the policy and the ones to imitate. NEAR seems, in fact, a more sophisticated version of this simple method. It would be important to explain why other non-adversarial imitation learning methods are excluded from the evaluation, and their differences and similarities with NEAR.

The algorithm presented in this paper does not seem to be a clear improvement over the baseline method (AMP). While the evaluation metric "spectral arc length" seems to favor NEAR, motions generated with AMP are generally closer to the ground truth. The authors should motivate why NEAR is better or at least a good alternative to AMP, e.g., proving lower sensitivity to the hyperparamenter choice, faster learning, less variance, more sample efficiency ... I encourage the authors to also compare the learning curves of the two methods, possibly including the number of interactions with the environment and the wall time necessary for convergence.



### Questions
* The authors mention that they use 20 test episodes to obtain the average performance, which sounds low compared to other RL papers. How large is the variability in performance across episodes? The confidence levels are provided across random seeds, so the variability of the performance within a seed is not evident.

* You mention that AMP is less affected by data availability than NEAR. Shouldn't it also be a problem for AMP when data is scarce, since the task of the discriminator might become too easy when it can perfectly remember all the ground truth trajectories?

* I did not fully understand why the energy function works well as a reward signal. If the energy is high when a sample is likely to be generated by the probability distribution of the ground truth data, why does the policy follow a trajectory instead of just reaching a high probability state? I thought that one reason can be that the energy function depends on the current state, so it will assign high energy only to the states that, according to the dataset, follow the current one with high probability. While this concepts are likely trivial for the authors, they should be more clearly explained in the paper for the less familiar reader to fully understand why the algorithm works. I would propose to use the example from Figure 1 to qualitatively describe why the displayed energy function is a good reward signal, if the energy changes as the agent moves, and other high-level considerations.

I commit to increase the score if my questions and doubts highlighted in the "weaknesses" section are carefully addressed.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Noise-conditioned Energy-based Annealed Rewards, a new framework for inverse reinforcement learning that leverages diffusion models. Instead of using unstable and non-smooth adversarial learning to approximate reward functions, NEAR learns an energy function via score matching. NEAR provides smooth and accurate reward signals for training policies through reinforcement learning.

### Strengths
NEAR replaces adversarial learning with energy-based modeling using diffusion models and score matching. This results in a stable and smooth reward representation, addressing issues of instability and non-smooth reward landscapes inherent in adversarial methods.

### Weaknesses
 **Lack of Comparison with Related Work:** While the paper acknowledges limitations like stability with large noise levels and data requirements, a significant concern is the absence of direct comparison with other works that apply diffusion models to imitation learning from observation. Specifically, works like [1] and [2] also leverage diffusion models in inverse reinforcement learning. Since the authors claim that their work is the first to apply diffusion models for reward learning, providing further clarification (for instance, [2] is a general diffusion-based IRL algorithm, it could be helpful if the author could highlight the difference in the paper) and direct comparisons in the experiment section with these methods would greatly enhance the paper's quality and situate it within the existing literature.

### Questions
1. **Comparison with DiffAIL [1]:** [1] also applies inverse reinforcement learning using diffusion models. Could the authors explain NEAR's major advantages compared with other works that integrate diffusion models into IRL? For instance, as the authors mention that GAIL can work well with single-clip data, how does NEAR compare in such settings, especially regarding data efficiency and performance? Further justification or emperial evaluation would be appreciated. 
    
2. **Comparison with SMILING [2]:** [2] introduces a non-adversarial framework using diffusion models for imitation from observation and provides theoretical analysis. Could the authors elaborate on the differences and advantages of NEAR compared with [2]? Including further empirical results comparing NEAR with [2] would strengthen the paper and clarify NEAR's contributions relative to existing methods.
    

[1] B. Wang, G. Wu, T. Pang, Y. Zhang, and Y. Yin, “DiffAIL: Diffusion Adversarial Imitation Learning,” Dec. 12, 2023, arXiv: arXiv:2312.06348. Accessed: Oct. 19, 2024. [Online]. Available: http://arxiv.org/abs/2312.06348

[2] R. Wu, Y. Chen, G. Swamy, K. Brantley, and W. Sun, “Diffusing States and Matching Scores: A New Framework for Imitation Learning,” Oct. 17, 2024, arXiv: arXiv:2410.13855. Accessed: Oct. 19, 2024. [Online]. Available: http://arxiv.org/abs/2410.138

### Soundness
3

### Presentation
3

### Contribution
3
