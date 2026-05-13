# Reasoning with Latent Diffusion in Offline Reinforcement Learning

- Decision: Accept
- Scores: 6, 8, 5

## Abstract
Offline reinforcement learning (RL) holds promise as a means to learn high-reward policies from a static dataset, without the need for further environment interactions. However, a key challenge in offline RL lies in effectively stitching portions of suboptimal trajectories from the static dataset while avoiding extrapolation errors arising due to a lack of support in the dataset. Existing approaches use conservative methods that are tricky to tune and struggle with multi-modal data (as we show) or rely on noisy Monte Carlo return-to-go samples for reward conditioning. In this work, we propose a novel approach that leverages the expressiveness of latent diffusion to model in-support trajectory sequences as compressed latent skills. This facilitates learning a Q-function while avoiding extrapolation error via batch-constraining. The latent space is also expressive and gracefully copes with multi-modal data. We show that the learned temporally-abstract latent space encodes richer task-specific information for offline RL tasks as compared to raw state-actions. This improves credit assignment and facilitates faster reward propagation during Q-learning. Our method demonstrates state-of-the-art performance on the D4RL benchmarks, particularly excelling in long-horizon, sparse-reward tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel offline RL algorithm that leverages a diffusion model to plan over the learned temporally abstract latent space for action representation. The empirical results show that temporal abstraction can help distinguish latent skills and the proposed method shares competitive performance with other state-of-the-art baselines.

### Strengths
Exploring how to leverage expressive models such as diffusion models and Transformers for policy learning is an important direction in RL, especially for the offline setting. To the best of my knowledge, the idea of combining high-level diffusion planning and low-level primitive learning is novel. The paper is well-organized and clearly written.

### Weaknesses
While well-motivated, I have some questions about this work:

1. My major concern is that the results on offline RL benchmarks may be insufficient to show the advantage of planning with diffusion models on latent action space. While I appreciate that the authors have covered the most popular state-of-the-art baselines in Table 1, I think it is necessary to compare LDCQ with some literature that similarly performs planning on the learned action representation space learned by VAE [1, 2, 3, 4] or Flow [5, 6]. Specifically, a comparison with methods like OPAL [1] and PLAS [3] which use VAEs for latent action spaces, and methods like Flow to Control [6] which use normalizing flows, would be crucial to understand the relative benefits of the proposed approach. Also, I am curious about the ablation of LDCQ on diffusion models (Section 5.2 has shown some support, however, it compares the diffusion prior with the VAE conditional prior rather than a learned latent policy). It is unclear whether the performance gain is due to the diffusion model's planning capability or simply a better prior for the latent space.
2. The paper has discussed some limitations of prior works depending on VAE representations. However, it is unclear to me why introducing latent diffusion can solve these limitations, as LDCQ also requires a learned VAE embedding. Is it because the diffusion model is more expressive so you can use less KL penalty or there are some other reasons? Specifically, the paper should clarify if the diffusion model's advantage stems from its ability to model complex, multi-modal distributions in the latent space more effectively than a VAE, and how this impacts the quality of the learned policy. Furthermore, if we learn the latent action space with a flow model, which is a lossless representation, does latent diffusion planning still have some advantages? The paper should discuss the potential benefits and drawbacks of using a flow-based latent space compared to a diffusion-based one, especially considering that flows offer an exact representation, while diffusion models are approximate.

### Questions
There are some questions and concerns, which I have outlined in the previous section.

UPDATE: I updated my score from 5 to 6 as the authors addressed most of my concerns in the response.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
# Summary

This work brings together the ideas from Batch Constrained Q-Learning (BCQ) and Latent Diffusion Models (LDMs), in order to succeed in offline RL. As in LDMs, the proposed method (called LDCQ - Latent Diffusion Constrained Q-learning) has a two stage training process. (i) The first stage trains a variational autoencoder (VAE) for trajectories (sequences of state-actions), where the decoder is the policy network. This latent space is a compressed representation of trajectories, serving as a form of temporal abstraction. (ii) The second stage of the training learns an LDM on this latent space and a latent-conditioned Q-network. At inference time, multiple latents are sampled from the LDM, and the Q-function is used to score each latent based on estimated Q-value. This scoring mechanism can be replaced with any kind of goal-conditioning (e.g.: L2 distance to goal in a maze environment), to obtain a goal-conditioned variant of the proposed method.

The use of latent diffusion makes this work distinct from recent diffusion-based offline RL methods such as Diffuser and Decision Diffuser. The analysis presented in this work highlights that (i) diffusion models are superior to VAEs when dealing with multi-modal latent spaces, (ii) the proposed LDCQ method achieves state-of-the-art or similar performance when compared with prior works.

### Strengths
# Strengths

The paper proposes a novel idea: Combining BCQ and latent diffusion models can lead to an offline RL algorithm that has the best of both worlds. Overall, this idea and the execution and analysis presented in this work is significant and of high quality.

1. The proposed method aims to fill a gap in existing methods such as Diffuser and Decision Diffuser by taking inspiration from latent diffusion models (LDMs): shifting diffusion into the latent space and separating the training process into policy and trajectory auto-encoding on one side and Q-learning and diffusion on the other side. With this choice, **the method inherits the strengths of both LDMs and batch-constrained Q-learning (BCQ)**.

1. The analysis of how the diffusion model of the proposed method (LDCQ) deviates from a baseline (that uses VAEs instead), clearly supports the hypothesis that **diffusion models are better at dealing with multi-modality** in the distribution of latents.

1. The paper has shown **similar or state-of-the-art performance** on a challenging selection of environments from the D4RL benchmark, the most notable of which is the performance on Franka kitchen-partial-v0 and kitchen-mixed-v0 environments, and the Ant-Maze large-diverse and medium-diverse environments. Specifically, two of these environments -- antmaze-large-diverse-v2 and kitchen-partial-v0 show significant improvements in the state-of-the-art.

1. The source code was provided.

**Clarity**: The paper has some issues with ordering of the introduced concepts and terminology, but by the end of the paper, the reader is left with a clear understanding of the presented work. The figures and algorithms are clear and greatly help in the understanding of the proposed method and analysis.

### Weaknesses
# Weaknesses

Overall, the paper has some statements/claims that are stretched, the empirical evidence seems like a mixed bag with certain D4RL environments/tasks silently omitted, and some weaknesses inherited from choosing latent diffusion models.

## Stretched claims
1. The phrases “improves credit assignment”, “faster reward propagation” describing the proposed work should be avoided, or backed by empirical evidence. I don’t see how either of these quantities can be measured. I understand how the proposed method will intuitively achieve both of these -- however, they are just intuitions, not proven. The claim of improved credit assignment is particularly problematic, as the method does not explicitly modify the reward structure or the backpropagation process. It is unclear how the latent space manipulation inherently leads to better credit assignment without further justification.

2. The paper describes the decoder or policy as a “powerful decoder” that can handle “high-frequency details”. This is true for LDMs used for computer vision dealing with high resolution images. However, I don’t see how this translates well into RL. Training the VAE encoder-decoder model in a separate first stage seems like it will produce a rigid, fixed policy (i.e. decoder). The paper itself acknowledges that the “limited decoder capacity” is probably what is leading to the saturation of performance in Figure 4. How can the decoder be “powerful” and “limited” at the same time? Is there a way to empirically measure the strength of a decoder? The decoder's capacity is likely limited by the architecture and training data, and it is not clear how the decoder can handle high-frequency details in the action space, especially given that the action space is often low-dimensional compared to image pixel spaces. The claim of a powerful decoder needs to be substantiated with more concrete evidence, such as analysis of the frequency content of the generated actions.

## Issues with empirical evidence

1. In Table 1, not all environments/tasks from D4RL are included. For example, the medium and umaze versions of Maze-2D are missing. In my experience, despite being easier environments, performance on these environments do highlight subtle differences between algorithms. They are certainly more important than the latter category of environments that do not require trajectory stitching. The omission of these environments makes it difficult to assess the method's robustness across varying difficulty levels within the same environment family.

2. In the latter category of environments that do not require trajectory stitching, more environments/tasks seem to have been silently omitted. The “-expert” suffix versions of Adroit pen, hammer and relocate tasks have been omitted. I would like to see an explanation of why certain environments in Table 1 were omitted, as otherwise it appears as cherry picking. Note that these results were not present in the Appendix either. The lack of results on the expert datasets is a significant omission as these datasets are often used to evaluate the behavior cloning capabilities of offline RL algorithms. The absence of these results raises concerns about the completeness of the empirical evaluation.

3. Some qualitative results such as visualization of trajectories at test time would have been helpful for supporting the trajectory stitching property. Visualizing how the latent space is traversed during policy execution would provide more insight into the method's ability to generate coherent and temporally extended actions.

4. Confidence intervals (error bars) are missing in Figure 4 and Adroit environment/tasks of Table 1. The lack of error bars makes it difficult to assess the statistical significance of the results and to determine if the observed differences are meaningful or simply due to random variation.

5. Not all reported performance values are state-of-the-art, this claim should be qualified. The paper should clearly state which environments the method achieves state-of-the-art performance on, and where it does not, to avoid misleading the reader.

## Clarity

1. Batch-constrained Q (BCQ) is mentioned several times and the acronym is used once before it is explained in Section 4.2. I recommend briefly explaining BCQ as a part of “Section 3.2 Offline Reinforcement Learning”.

2. Algorithms 1 and 2 explain the second stage of training and the policy execution phase respectively. However, there is no algorithm box for the first stage of training (VAE). The policy \pi also has a subscript \theta, but \theta is not used anywhere else in the paper. For completeness, I would recommend adding an Algorithm to describe the first stage of training where the policy parameters \theta are learned.

### Questions
# Questions

Some of my questions have been merged into the weaknesses section. Here are the remaining questions.

- The policy execution first samples a latent z-i (representing a skill), and then fixes that z sample throughout the policy execution for H steps. What would happen if z-i is re-sampled after every action is taken by the policy (like model predictive control - MPC). Do you expect it to improve performance and if so, will it be much more computationally expensive given the cost of sampling z?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes using latent diffusion in offline RL as a way to compress task specific skills and information that helps learning Q-functions for improved performance in offline benchmarks. This paper provides a good instantiation for how to use latent diffusion models (LDM) in the offline RL setting. The key is to use a separate diffusion model, from which to learn a latent conditioned policy (similar to prior works using latent skills for RL). The proposed approach therefore seems quite useful for long horizon credit assignment tasks, where temporal abstraction and skills play a key role, and the work tries to justifies this through sparse reward environments for experimental evaluation.

### Strengths
This paper proposes an interesting idea that allows decoupling the diffusion model from the policy decoder; allowed the algorithm to be used for both continuous or discrete action environments. Experiment results are primarily for continuous action D4RL offline tasks, and shows relatively improved performance across few benchmarks. The execution of the algorithm is interesting, but I worry about the easy-ness of the approach. I agree with the authors that the reason that the algorithm is structured this way is to have better flexibility in terms of the latent skills from the diffusion prior, but see my comments in weaknesses. Other than that, the execution of the algorithm in the BCQ setting taking everything in the latent space (assuming the latents are good) is an interesting idea. Figure 2 shows how well the latents also get distributed across the horizons, suggesting that diverse skills can be learnt across horizons.

### Weaknesses
1. Experiment results are difficult to follow. The D4RL results are the primary ones, but the appendix claims to have results for CARLA and Goal Conditioning tasks too? It seems the goal conditioned tasks are not the standard ones in GCRL literature, and it is not clear what the key takeaway is other than the constrained offline RL results + qualitative results evaluating the latents across the horizon.

2. The proposed algorithm is interesting, but might have difficulty with the execution and easy-ness of the approach. Primarily because the Q-function is now learnt over Q(s,z) latents, and it would be helpful to do some qualitative evaluation of the Q-values over the latents. This is because the learnt Q would now heavily depend on the quality of the latents, which is coming from a beta-vae, and prior works on representation learning has showed that VAEs are not necessarily good for learning good quality latents.

3. This draws to my other worry of how good the latents are when learnt from Beta-VAE, and if there is a qualitative analysis about the structure that Beta-VAE latents recover from these tasks. Recent works have shown that with representation learning objectives, the latent structure can be well recovered - this work only shows how the latents are distributed across the horizonz, but it is not clear if these latents can itself contain useful information specific to the task?

4. Maybe not so related, but I wonder if an entropy-regularized objective can also be used in these settings to induce diverse skills learnt from the diffusion prior? The paper uses BCQ in offline, which is drawn from TD3 - so I agree that the algorithm is fundamentally using a deterministic policy approach; but for the discrete action tasks - maybe entropy regularized objectives to learn diverse skills may be introduced?

5. Paper claims that the algorithm can work for both continuous and discrete action spaces - but there aren’t enough results showing for discrete actions? Why is that so?

6. How does the claim on learning multi-modality for the diffusion approach compare with other representation objectives, rather than just the VAE? I think more baselines should be compared here, and I doubt that well tuned representation objectives would also be able to capture the multi-modality aspect similar to the diffusion model.

7. Experimental results should be better organized; appendix seems to contain more domains, but they are not referred to the main; there are figures for the environments, e.g CARLA, but I couldnt gind results for that in the paper?

### Questions
See my questions along with the weakness section. Primarily, my worries are : 

1. How does the representations learnt with beta-vae compare with other representation objectives for learning the latents? How does diffusion compare to that? 

2. How can we evaluate the quality of the latents? This is of big importance for this work, since the Q function is now learnt over the latents; I would like to see quantitivate results showing the effectiveness of the Q-function, maybe TD errors too, and qualitative results showing how good are the latents. Figure 2 only shows that latents are diverse and more skills are introduced across the horizons; but I worry about the use of Beta-VAE in the algorithm, and think better representation objectives should instead be used in the algorithm pipeline. Results justifying this would strengthen the paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
