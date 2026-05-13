# Neuralized Markov Random Field for Interaction-Aware Stochastic Human Trajectory Prediction

- Decision: Accept
- Scores: 8, 5, 6, 5

## Abstract
Interactive human motions and the continuously changing nature of intentions pose significant challenges for human trajectory prediction. In this paper, we present a neuralized Markov random field (MRF)-based motion evolution method for probabilistic interaction-aware human trajectory prediction. We use MRF to model each agent's motion and the resulting crowd interactions over time, hence is robust against noisy observations and enables group reasoning. We approximate the modeled distribution using two conditional variational autoencoders (CVAEs) for efficient learning and inference. Our proposed method achieves state-of-the-art performance on ADE/FDE metrics across two dataset categories: overhead datasets ETH/UCY, SDD, and NBA, and ego-centric JRDB. Furthermore, our approach allows for real-time stochastic inference in bustling environments, making it well-suited for a 30FPS video setting. We will open-source our codes upon paper acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes a method for human trajectory prediction that incorporates interaction-awareness through a neuralized Markov Random Field (MRF) framework. By integrating MRF with neural networks, the model captures both individual movement patterns and inter-agent interactions over time, effectively addressing uncertainties in predicting human motion. This design is particularly well-suited for real-time trajectory forecasting.

### Strengths
- Novel integration of Markov Random Fields with neural networks for human trajectory prediction.
- Advances the field by combining structured probabilistic modeling with deep learning to address noisy, dynamic environments.
- Achieves strong performance on multiple datasets with short inference time.
- Transparent documentation of training and hyperparameter choices ensures reproducibility.

### Weaknesses
- Important citations about the dataset used in this paper are missing. Eg., ETH, UCY, Stanford Drone Dataset (SDD)...
- In table 1, it will be interesting to add the previous model Y-net [1] as a baseline since that model had very impressive performance on the datasets used in this paper. 
- The robustness experiment is not clear. E.g., when simulating noisy tracklets by adding Gaussian Noise, which 4 frames out of 9 observed frames are selected to add noise? Are they randomly selected or some specified 4 frames? In addition, adding noise to all 9 observed frames is more convincing to simulate sensor noise. 



[1] Mangalam, Karttikeya, et al. "From goals, waypoints & paths to long term human trajectory forecasting." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.

### Questions
- Figure 1 was never referred to in the text. It will be good to mention it in your text.
- In table 4, it seems there is a gap between the proposed method and the previous works on JRDB dataset. Please double-check if there is something wrong. (e.g., same data splits? data samples?)

### Soundness
3

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
2

### Summary
This work introduces a multi-person tracking approach. It summarizes per-frame tracks into short segments and uses a MRF to forecast those segments, rather than per-frame tracks. To initialize the first trackless, a VAE based “Bayesian update” is performed. Surprisingly, only this first step requires knowledge of the input motion, while the MRF factors out any of the input conditions. The method produces SOTA results on some benchmarks while being significantly faster than most other SOTA methods.

### Strengths
The method produces SOTA results on standard benchmarks while greatly outperforming SOTA on runtime too.

### Weaknesses
I have two main concerns: [A] the method description is unclear, and [B] the two-stage approach is not well-motivated and not well-ablated. 

[A] I find the data description in LL158-161 confusing: could the authors clearly state what the input modalities are, i.e. are those per-person trajectories in 2D, are they collections of 2D per-person trajectories, how are they normalized/standardized - in what coordinate frame are they? 
This also makes it difficult to follow the rest of the method description as it is unclear what the inputs/outputs are.
The authors make repeated use of the word “joint configuration space” (i.e. L165) - could they elaborate what that means?

L161: what are those “M individual states”?

The authors use various words to describe there tracklets and the length, i.e. “stride”, “chunk”, “period”, “time chunk” - I would suggest to stick to one to make it easier to read.

L182-L183: It is unclear here what the parameterizations are, i.e. what are the differences between \theta_u, \theta_m and \theta_j —> this needs more details here and not just in the following chapters (Maybe also reference Figure 2 here..).

Can the authors clarify what they mean by L070: “Human movements are Markovian up to certain frequencies” ?



[B] Concerns wrt Two-stage approach
I wonder if the split into Stage 1 (Bayesian Update) and Stage 2 is necessary. My main concern is that Stage 2 has no information about motion of the past beyond the previous segment S_{t-1}), while the segments seem to be rather short, as indicated in Table 7 (right side). I find it surprising that the method does not need to rely on past motion beyond a few frames to make more accurate predictions.

For example, just recursively applying the “Bayesian update” step (Stage 1) should perform better, as it has access to more historic information. I believe this is what the authors evaluated in Table 4 and 5 (“Ours (Stage 1)”) - could the authors confirm that this is indeed the case? They should more clearly describe this baseline / ablation in text. Also, it is surprising that this performs worse than the MRF as this method can exploit past motion better than the MRF. Could the authors elaborate what causes the Bayesian update step to be outperformed here?

On a similar note, if Stage 2 (self-evolution + interaction) seems to perform better, I wonder if the Stage 1 is even necessary as the initial Segment S_1 can be obtained from the historic motion sequence. I wonder how “Ours (Stage 2 only)” would perform in this case.

A two-stage approach is more complicated and brittle and thus it is important to clearly motivate each part, which has not been done in the ablation.

*Suggestions*

Add relative speeds to Table 3 where the fastest method is 1 and the others are multiples of it.

For the stride size in Table 7 (right) I would suggest to add the time in seconds as well

### Questions
In Figure 5 the method seems to predict left/right off-shoots - can the authors comment on why those are happening? They seem like very unlikely predictions.

L472: what is a “standard normal distribution”?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a neutralized Markov random field-based motion evolution method for stochastic human trajectory prediction, which explicitly models the agent’s motion dynamics and crowd interactions, with lightweight and efficient learning as well as inference. Experimental results show that the proposed method is effective on multiple datasets, with robustness under noise disturbance.

### Strengths
1. The paper proposes to use MRF and iteratively infer the stochastic distribution, which is different from existing explicit structured models.

2. The numerical results are good, and the inference speed is promising.

3. The paper is clearly written and easy to follow.

### Weaknesses
I put both of the Weaknesses and Questions here:

1. The authors should elaborate more on why MRF that iteratively infers the stochastic distribution of future motions could achieve better performance, especially compared to existing methods.

2. It appears to me that this paper clearly express what it does and how it does, but the motivation behind is not very clear, especially when readers are not in the same field, which makes it somewhat confusing why each proposed component would work.

3. I think more visualized results of more baselines and the proposed method are needed for better comparison.

### Questions
See Weakness.

### Soundness
2

### Presentation
3

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
Modeling interactions and continuously changing intentions in trajectory prediction is challenging.
To address this, the paper proposes a Markov Random Field (MRF)-based motion evolution method. The trajectory is divided into time chunks, with the assumption that each trajectory segment follows a Markov chain sequentially.
The authors derive crowd motion evolution as a probabilistic distribution, which consists of a Bayesian update term, predicting the next state from each given observation, and a transition term. The transition term is further divided into a self-evolution term, which predicts the next state from each agent’s current state, and an interaction term, modeling relations between agents.
All of these terms are implemented using Conditional Variational Autoencoders (CVAEs).
Experiments are conducted extensively on multiple pedestrian trajectory datasets, achieving state-of-the-art prediction performance and real-time inference speed.

### Strengths
* The paper is easy to follow, and the proposed method is technically well-implemented.
* The method is validated through extensive benchmark experiments. Its fast inference speed and high accuracy on the NBA and JRDB benchmarks are impressive, especially in JRDB-based experiments from an ego-centric view where noisy input was tested, and the prediction results appear plausible.
* The experiment applying the proposed method to group reasoning is intriguing, and the visual results are very plausible.

### Weaknesses
* It seems difficult to claim state-of-the-art prediction performance. There already are some prediction models showing better performance on ETH-UCY and SDD than the baselines compared here. More convincing reasoning is needed to explain why the proposed method is necessary compared to these models.
    - View Vertically (ECCV’22): 0.18/0.28, SICNet (ICCV’23): 0.19/0.33, Socialcircle (CVPR’24): 0.17/0.27  (: ADE/FDE on ETH-UCY benchmark)
* I find it hard to fully grasp the novelty of the proposed method. As mentioned in the related work, there are already trajectory prediction methods that use the Markov property. Additionally, there are existing methods that construct a dynamic graph based on agents' positions to account for interactions between them (e.g., HiVT (CVPR’22), QCNet (CVPR’23)). The proposed approach seems like a combination of these two approaches, which might not meet the standards for ICLR.
* I initially thought that using CVAE would introduce stochasticity, but it’s odd to see deterministic samplers are used during stage 2. In that case, why split it into two stages? Couldn’t deterministic sampling alone without CVAE sampling be trained and used for inference? The referenced Non-probability Sampling (Bae, CVPR’22) also suggests that deterministic sampling is preferable to random sampling, so I don’t understand why both random and deterministic sampling were used here. The ablation only compares with stage 1 alone; ablation results of state 2 only without CVAE sampling are needed.

### Questions
* On line 465, what does "precludes stationary state" mean? How is that related to robustness against noisy input? 
    - In addition, perturbation from Gaussian noise doesn’t seem related to stationarity.
* The model uses CVAE in many parts, and CVAE is known to be vulnerable to posterior collapse in autoregressive methods, which could weaken stochastic prediction. What solutions were implemented to address this issue?

### Soundness
3

### Presentation
3

### Contribution
2
