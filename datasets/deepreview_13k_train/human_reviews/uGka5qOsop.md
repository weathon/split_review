# A Temporally Correlated Latent Exploration for Reinforcement Learning

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
Efficient exploration remains one of the longstanding problems of deep reinforcement learning.
Instead of depending solely on extrinsic rewards from the environments, existing methods use intrinsic rewards to enhance exploration. 
However, we demonstrate that these methods are vulnerable to \textit{Noisy TV} and stochasticity.
To tackle this problem, we propose Temporally Correlated Latent Exploration~(TeCLE), which is a novel intrinsic reward formulation that employs an action-conditioned latent space and temporal correlation.
The action-conditioned latent space estimates the probability distribution of states,
thereby avoiding the assignment of excessive intrinsic rewards to unpredictable states and effectively addressing both problems.
Whereas previous works inject temporal correlation for action selection, the proposed method injects it for intrinsic reward computation.
We find that the injected temporal correlation determines the exploratory behaviors of agents.
Various experiments show that the environment 
where the agent performs well
depends on the amount of temporal correlation.
To the best of our knowledge, the proposed TeCLE is the first approach 
to consider the action-conditioned latent space and temporal correlation for curiosity-driven exploration.
We prove that the proposed TeCLE can be robust to the Noisy TV and stochasticity in benchmark environments, including Minigrid and Stochastic Atari.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims to develop an approach to providing intrinsic rewards more robust to stochasticity (and noisy-TV scenarios) than previous approaches. The proposed approach–TeCLE–uses inverse dynamics modeling to learn a state representation and uses the action-conditioned state reconstruction loss (through a conditional VAE) as an intrinsic reward. While sampling the latent representation from the encoder’s output, temporally correlated noise is added (modulated by $\beta$). Empirical analysis shows that TeCLE outperforms bonuses such as RND and ICM in Minigrid environments with noisy-TV and some stochastic Atari environments. The authors also illustrate qualitative differences in exploration behavior based on the color of noise added.

### Strengths
S1. Using temporally correlated noise on a latent representation of inverse dynamics model features appears novel (but also see W2).

S2. The approach outperforms popular intrinsic bonuses like RND and ICM in Minigrid environments with noisy TVs and also in many of the considered atari environments.

### Weaknesses
W1. From the aggregated and normalized results in Figure 2, all noise levels seem to perform similarly (high overlap in standard errors), even white noise with $\beta=0$. This seems to indicate that colored/temporally correlated noise may not be so important to the performance of the proposed approach, which is a major theme of the paper.

W2. While the paper describes approaches that add noise in the action space, it misses comparisons with approaches that add noise in parameter space [1, 2], which would be closer to adding noise in some latent space. Similarly, another work adds temporally correlated noise to the latent state for exploration [3]. It would be helpful to compare the differences with the approach introduced here. Other forms of temporally correlated exploration, like temporally extended epsilon-greedy [4] could also be interesting to consider in the atari evaluation.

W3. The clarity of the paper requires improvement. Section 4A describes the inverse dynamics modeling task used for feature embedding. As far as I can tell, this is the same idea of feature embedding used in ICM. While the authors describe the ICM paper in the Background section, the current presentation of feature embedding in Section 4A is more likely to be incorrectly interpreted as a novel contribution of this paper. It should be clearly mentioned that the representation/feature learning part is the same as that of ICM. If there is a difference, please clarify what is new in that section. 

Further, since ICM and TeCLE use the same feature embedding (which captures the same information about states), the difference in robustness to stochasticity between the two approaches must arise from the tasks used to generate intrinsic rewards (model error vs. reconstruction error), and it is not clear why reconstruction error would work better. Perhaps the authors could comment and elaborate on why TeCLE works better than ICM.

### Questions
- In Ablation Study 1, the authors show that the CVAE's action conditioning helps one of the considered problems but not the other. In lines 503-506, the authors mention that this is because of better self-supervised learning. It is not clear to me precisely what that statement means. Could the authors elaborate on why action conditioning is helpful?  

- Is there a reason to use the Number of Updates as the x-axis in Figures 5/7 and the Number of Steps in Figures 6/8? Using the Number of Steps in all cases could be better, or specifying the correspondence between updates and steps (and frames in Atari) in the main text.

### Soundness
1

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
3

### Summary
This paper proposes to add temporal correlation to intrinsic rewards computation by learning an action conditional C-VAE for regularizing the representation of the state representation. The experiments in a few MiniGrid and Atari games show some improvements.

### Strengths
The connection between temporal correlation and the NoisyTV problem could be interesting.

### Weaknesses
## Writing
Overall, this paper only states how they implement the method but barely talks about the motivation behind them, which will make the reader lose. For example, in Line 48, the author is supposed to say how they address the noisy tv problem mentioned in the previous paragraph, but the author directly jumps in the implementation details of their method and never mentions why temporal correlation can mitigate NoisyTV problems. There are more examples like this, but it will take forever to enumerate all of them.

## Experiments
This paper lacks a lot of stronger baselines in the chosen environments (e.g., [1]). RND and ICM are not state-of-the-art in those environments. Moreover, only a fraction of Atari games are chosen, and the most classic hard-exploration problem, Montezuma Revenge, is not studied, which makes the results questionable.

- W1: Now I'm getting the idea better now, but still have some questions.
My understanding now is that TeCLE injects noises to every state, so it will not assign overly high intrinsic rewards to noisy states. I think this will require the injected noises to have the same pattern with those in noisyTV states (e.g., both are Gaussian noises). Also, how do you know the intrinsic rewards on noisy states are large than the other clean states without noises? One possibility is that noisy states are associated with constantly small intrinsic rewards. Any evidence for this? Additionally, I think the explanation on Line 253-267 is very confusing and verbose. Your explanation in the rebuttal is better. I will suggest incorporating that to the paper.

- W2: 
I don't get why the distinction between prediction-based and count-based is the reason of not comparing with it. To me, RND and NovelD are methods of generating intrinsic rewards, and noisyTV robustness was discussed in their papers, so as a practitioner that uses intrinsic rewards, I would be curious how much TeCLE can improve over both methods in noisy TV problems.

I still think you should compare it with AMA or integrate AMA with TeCLE. If AMA itself already did as well as TeCLE, then the significance of TeCLE will be undermined. On the other hand, to show that AMA is compatible with TeCLE, you need experiments to demonstrate it.

### Questions
N/A

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Temporally Correlated Latent Exploration (TeCLE), a novel curiosity-driven exploration method for reinforcement learning that uses action-conditioned latent spaces and temporal correlation, for addressing the noisy-TV issue, a long-standing problem in efficient exploration in RL. The authors propose to use action-conditioned latent space to model state distributions and compute intrinsic rewards based on reconstruction error. Temporal correlation is induced through colored noise in the latent sampling process, and different noise profiles lead to different exploratory behaviours. The method is evaluated on Minigrid and Stochastic Atari environments, showing improved robustness to the Noisy TV problem and stochasticity compared to baselines like ICM and RND.

### Strengths
- The proposed method is a novel combination of action-conditioned latent space and temporally correlated signals for addressing the noisy-TV problem.
- The empirical evaluations is comprehensive, with extensive experiments and ablation studies across multiple environments.
- The propose method empirically exhibits robustness with respect to noise.

### Weaknesses
 - Empirical evaluations on hard exploration tasks (e.g., Montezuma's Revenge) show modest improvement.
- The theoretical grounding between the injected temporal correlations and resulting exploratory behaviour requires further justification.
- The proposed method induces significant computational overhead compared to simpler methods.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a method for improving exploration in RL using intrinsic motivation. Similar to ICM, a state embedding is learned with respect to an inverse dynamics loss and the error between a predicted embedding of the next state and the actual embedding of the next state serves an auxiliary reward. However, unlike ICM, the predicted embedding of the next state is obtained by a forward model but by reconstructing the next state embedding using a VAE. The paper proposes to use an action-conditioned C-VAE and to use colored noise while sampling the latent variable of the C-VAE to induce temporal correlation (or anti-correlation). The method is evaluated on suitable gridworlds (DoorKey) and Atari environments, where it achieved better results than the baselines (ICM and RND).

### Strengths
- The description of the approach is clear.
- While colored noise was previously used for sampling temporal correlated actions for better exploration, injecting temporal correlations while sampling the latent of the VAE is novel.

### Weaknesses
 - The contributions are quite limited. The main contribution seems to be sampling the VAE latent with colored noise.
- The use of colored noise while sampling the VAE latent is not well motivated.
- Related work is insufficient discussed. For example, Kubovcik et. al used the reconstruction of an auto-encoder as intrinsic reward, Klissarov et al. also used a variational autoencoder, but used the KL between the posterior and prior for intrinsic reward, and, recently, Yan et al. also proposed to use the reconstruction error of a VAE for intrinsic reward but extended it with adaptive exploration mechanism, based on a discriminator.
- The empirical evaluation is insufficient. Table 1 does not show confidence intervals or baseline results. It is not clear how important hyperparameters (e.g. weight of the intrinsic reward) for the baseline were selected and which values were used, and, furthermore, important baselines are missing, e.g. the above mentioned related works.
- The writing could be improved and is often inaccurate. For example the abstract states that the latent space "models" the probability distribution of states, and that the environment where the agent performs best depends on the amount of temporal correlation. Some claims are also questionable, e.g. that the existing curiosity-driven methods are vulnerable to Noisy TV problems (some are, but not all of them)  


### Questions
Could you extend on your motivation for colored noise? I understand that temporal correlation and anti-correlation will affect the smoothness of the intrinsic reward. But how does it relate to the noisy TV problem?

### Soundness
2

### Presentation
2

### Contribution
1
