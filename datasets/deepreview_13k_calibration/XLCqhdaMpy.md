# Latent Weight Diffusion: Generating policies from trajectories

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
With the increasing availability of open-source robotic data, imitation learning has emerged as a viable approach for both robot manipulation and locomotion.
    Currently, large generalized policies are trained to predict controls or trajectories using diffusion models, which have the desirable property of learning multimodal action distributions.
    However, generalizability comes with a cost --- namely, larger model size and slower inference.
    Further, there is a known trade-off between performance and action horizon for Diffusion Policy (i.e., diffusing trajectories): fewer diffusion queries accumulate greater trajectory tracking errors.
    Thus, it is common practice to run these models at high inference frequency, subject to robot computational constraints.

    To address these limitations, we propose Latent Weight Diffusion (LWD), a method that uses diffusion to learn a distribution over policies for robotic tasks, rather than over trajectories.
    Our approach encodes demonstration trajectories into a latent space and then decodes them into policies using a hypernetwork.
    We employ a diffusion denoising model within this latent space to learn its distribution.
    We demonstrate that \ours can reconstruct the behaviors of the original policies that generated the trajectory dataset.
    \ours offers the benefits of considerably smaller policy networks during inference and requires fewer diffusion model queries.
    When tested on the Metaworld MT10 benchmark, \ours achieves a higher success rate compared to a vanilla multi-task policy, while using models up to $\sim$18x smaller during inference.
    Additionally, since \ours generates closed-loop policies, we show that it outperforms Diffusion Policy in long action horizon settings, with reduced diffusion queries during rollout.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose Latent Weight Diffusion (LWD) that learns a distribution of policy parameters and aims to capture the diversity of trajectory dataset and achieve fine-grained closed-loop control with small model size. The method is mostly based on Hedge et al., 2023, with the experiments using existing trajectory datasets instead. A variational autoencoder (VAE) is used to compress the trajectories into a compact latent space, where a diffusion model is then applied to learn the complex distribution of possible latents. The decoder decodes the network parameters for the policy. LWD is evaluated in simulated environments, and the results demonstrate that LWD can reconstruct the behavior of the original policies and achieve improved performance compared to larger models or baseline with long action chunk prediction in certain settings.

### Strengths
The question of distilling a large multi-task policy into smaller ones for fine-grained control is very relevant in current robotics research. The research proposed by the authors is well-motivated, and the overall setup of applying latent diffusion is intuitive and can potentially lead to strong individual policies while maintaining the diversity.

Based on the proposed approach, some of the experimental results are encouraging. Table 2 shows the benefit of LWD compared to undistilled MLP policies in MetaWorld and demonstrates moderate performance improvement. Figure 8 shows the resilience of LWD to longer action chunk prediction in the PushT task.

### Weaknesses
On the technical side, the paper’s novelty is fairly limited since it is a direct application of Hedge et al., 2023 using existing trajectory datasets. While the idea is promising, the experiment results are lacking and suggest important limitations. First, it is unclear how the hypernetwork setup scales up to more complex tasks. While the argument is that LWD can generate smaller policies for individual tasks as Table 2 shows, the authors have not shown convincing results on decomposing a single long-horizon task into subtasks where LWD generates a policy for each part. The experiment on action chunk size (Figure 8) alludes to such possibility but I think dedicated experiments on this setup can strengthen the story significantly and make the method much more relevant for current robotics research. Second, it is unclear how well the hypernetwork setup scales to larger model size when larger size is required, e.g., in more complex tasks. Can the hypernetwork still handle \theta of very high dimensions? e.g., on the order of millions, or can it handle pixel input?

The results with reconstructing the original policy are quite mixed and I have trouble understanding the conclusions made by the authors. It seems that the learned latent cannot differentiate the trajectories well with shorter length (Sec. 4.2). The discussion is fairly lacking. Sec. 4.2 also has a few comments that are not backed with experimental results, e.g., “Surprisingly, we noticed that after training our VAE on the snippets, the decoded policies from randomly snipped trajectories were still faithfully behaving like their original policies.”, and “we noticed that the decoded policies from the trajectory snippets did not perform as well as the original policies”. Please clarify or point to existing results if I misunderstand the comments.

I am fairly curious about the hypernetwork decoder setup, but the paper does not provide details on the architecture and how it handles very large output space (the decoded policy parameters). There is also no appendix for such experimental details.

### Questions
The paper writing can also be improved at a few places: (1) \tau is not defined when it is first introduced in Sec. 3.1, as well as \varepsilon in Sec. 3.3. (2) In Fig. 8, how is Relative Performance Change defined? Is it defined relative to the policy itself, or on an absolute scale? I find it quite misleading. Also, what is the action parameterization that LWD generates? I assume it is not diffusion?

In Sec. 3.1, it says a_t= \pi(s_t, \theta) + e, where e is normally distributed around 0. Why is the added action noise needed?

Could you comment on the other dimensions of the PCA analysis in Figure 5? Are they not very informative? It might be a good idea to show them in the appendix.

The paper is three lines over the 10-page limit. I suggest moving some of the derivations in Sec. 3 to the appendix, or try to shrink the space at places.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The proposed method, Latent Weight Diffusion (LWD), uses a two-stage process involving a variational autoencoder (VAE) coupled with a latent diffusion model. First, LWD encodes demonstration trajectories into a latent space using a VAE, then learns the distribution over these latent representations using diffusion in this latent space. A hypernetwork decodes the latent representations into policy parameters, generating closed-loop policies that are state or task conditioned. This approach leverages task-specific conditioning to maintain task generalization and efficiency, producing policy networks with reduced model sizes. The authors evaluate LWD on the Metaworld MT10 and D4RL benchmarks. They compare its performance on diverse tasks, such as multi-task learning and long-horizon robotic control, against baselines, including multi-task MLPs.

### Strengths
1. It is indeed interesting to explore the idea of latent diffusion in imitation learning following the success in [1]. The diffused latent is then decoded into policy hyperparameters via hypernetwork [3], which is significant since the diffusion model can capture diverse and multi-modality network parameter space, therefore enabling both state and multi-task conditioning. 
   - According to the experiment results, although not extensively compared with Diffusion policy in a state-conditioned setting, LWD is shown to work better than simple MLP in a multi-task setting as a proof-of-concept.

2. Sec 4.2 is a very insightful experiment. It sheds light on task difficulties and similarities. This setup can be used further to analyze/visualize task characteristics for imitation learning. 

[1] Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022.

[2] Chi, Cheng, et al. "Diffusion policy: Visuomotor policy learning via action diffusion." The International Journal of Robotics Research (2023): 02783649241273668.

[3] Ha, David, Andrew Dai, and Quoc V. Le. "Hypernetworks." arXiv preprint arXiv:1609.09106 (2016).

### Weaknesses
1. Related works on Sec. 2.2 should additionally cite [2, 3] for the statement "...to learn smooth cost functions for the joint optimization of grasp and motion plans."

2. There are some issues with the experiment outline for benchmarking LWD. For example:
    - Diffusion policy [3] should be compared with LWD in Table 2 to strongly confirm the architecture choice efficiency claimed in the paper. For example, the input of Diffusion policy [3] should be robot state concatenating with the task indicator, and Diffusion policy [3] should be trained with data from all tasks. The current comparison with a simple MLP is insufficient to demonstrate the advantage of the diffusion-based approach.
    - Ablation on network-size of LWD should be considered vs. success rate with tasks in [1]. For example, another column of LWD with 370.4k parameters should be added to Table 2 to study the effect of a bigger policy network for LWD. This is crucial to understand the trade-off between model size and performance, especially given the claim of reduced model sizes.
    - Sec 4.1. purpose is to see generalization in behaviors. However, comparing foot contact distributions between models for ablation study is not meaningful. Adding a comparison of state variances/counting different success modes of pick & place or pushing tasks in [1] between models is more insightful. The current analysis is limited to locomotion and does not fully capture the diversity of behaviors in manipulation tasks.
    - On a side note, Fig. 3 would be much clearer if merged into one figure (probably with a smaller scatter size), making it easier to see the foot contact distribution overlaps.

### Questions
1. Please address the above points in Weaknesses.
2. In all experiments, how many diffusion steps are typically needed to decode the policy network?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper "Latent Weight Diffusion (LWD): Generating Policies from Trajectories" introduces a novel approach for imitation learning in robotics. Current methods often rely on trajectory-based diffusion models, which can be computationally demanding and less effective in capturing long action sequences. To address these challenges, LWD diffuses policy parameters instead of trajectories. The model first encodes demonstration trajectories into a latent space using a Variational Autoencoder (VAE). Then, a diffusion model learns the distribution within this latent space, allowing the generation of compact, task-specific policies via a hypernetwork decoder.

### Strengths
1. This paper provides a novel method for generating the network parameters with diffusion models.
2. The experiments showing the distribution modeling of the generated network parameter is compressive.

### Weaknesses
1. Table 2 is unclear. It is not clear what is an MLP policy. Does it predict a sequence of future actions or just a single-step action? If it is the latter, it is unfair to compare these MLP policies to the proposed LWD method, since LWD predicts a sequence of future actions.

2. Figure 8 is also unclear. The authors didn't show the success rates of diffusion policy and LWD. They just show the "relative performance change" curve. I hope the author can show the success rate also.

3. Why is LWD close-loop and why does the author say diffusion policy is open-loop? I guess the authors want to say that LWD can generate a new policy every $H_a$ step. However, diffusion policy can also regenerate new action sequences after every $K$ step where $K$ is a hyperparameter. I think here the "close-loop" is an inaccurate and unprofessional word.

4. From my understanding, the author didn't compare the success rates between LWD and diffusion policy on any task. So the claimed contribution in the Abstract and Introduction (LWD offers the benefits of considerably smaller policy networks during inference and requires fewer diffusion model queries) is not supported by evidence.

### Questions
See the weakness.

### Soundness
3

### Presentation
2

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
This paper improves the online inference time of diffusion-generated policies by using diffusion to generate a hypernetwork instead of only outputting an action sequence. The policy is then reconstructed and inferred at higher frequency.

### Strengths
The combination of diffusion models with hypernetworks is quite novel and enables fast online inference. LWD is able to generate diverse behaviors while still maintaining low inference latency.

### Weaknesses
It is unclear whether policy stability is improved without further interaction with the environment. Specifically, without counterfactual reasoning or data on failed actions, how can the generated policy recover from states that deviate from the nominal path? If the author could empirically verify this or provide more rationale, it would make the approach more sound. The long-horizon experiment demonstrates closed-loop stability, but this could also be due to the diffusion model's limited capacity to capture the high-dimensional distribution fully. The paper does not sufficiently address how the learned policy would react to disturbances, which is critical for real-world deployment. The lack of analysis on the policy's robustness to perturbations in the state space makes it difficult to assess the practical value of the proposed method.

### Questions
1. The authors use the long-horizon experiment to demonstrate closed-loop stability, but this could also be due to the diffusion model's limited capacity to capture the high-dimensional distribution fully. Could the authors compare the performance of the two models under disturbances to show how the learned closed-loop policy improves stability? Can it improve stability with disturbances?
    
2. When Diffusion Policy is running online, it can use the previous solution to warm-start the next step's action sequence. Since in the neighbor state, the policy shouldn’t change drastically. In LWD, do the authors think the same design could be possible?

### Soundness
3

### Presentation
3

### Contribution
3
