# BISIMULATION METRIC FOR MODEL PREDICTIVE CONTROL

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Model-based reinforcement learning has shown promise for improving sample efficiency and decision-making in complex environments. However, existing methods face challenges in training stability, robustness to noise, and computational efficiency. In this paper, we propose Bisimulation Metric for Model Predictive Control (BS-MPC), a novel approach that incorporates bisimulation metric loss in its objective function to directly optimize the encoder. This time-step-wise direct optimization enables the learned encoder to extract intrinsic information from the original state space while discarding irrelevant details and preventing the gradients and errors from diverging. BS-MPC improves training stability, robustness against input noise, and computational efficiency by reducing training time. We evaluate BS-MPC on both continuous control and image-based tasks from the DeepMind Control Suite, demonstrating superior performance and robustness compared to state-of-the-art baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new method for model-based reinforcement learning (MBRL) called BS-MPC. The key innovation lies in incorporating a bisimulation metric loss into the objective function to improve encoder stability, robustness to noise, and computational efficiency. By using the bisimulation metric, BS-MPC aims to ensure behavioral equivalence in the latent space, maintaining key characteristics of the original state space. The method is benchmarked against the Temporal Difference Model Predictive Control (TD-MPC) and other model-free and model-based methods on various tasks, showing superior stability and resilience to noise.

### Strengths
The paper provides a new perspective by integrating the bisimulation metric to address known challenges in MBRL, particularly around stability and robustness to noise. The experimental results demonstrate how BS-MPC performs well in both state-based and image-based tasks, showing increased resilience to noise and achieving faster training times due to parallel computation. The theoretical analysis adds depth by bounding cumulative rewards in the learned latent space, suggesting that BS-MPC retains meaningful state information effectively.

### Weaknesses
While the theoretical foundations are thorough, certain explanations, particularly on encoder stability and noise resilience, could be made clearer to broaden accessibility. The parameters require extensive tuning, which may be impractical for real-world applications lacking automated parameter selection. Additionally, the approach to introducing perturbations, particularly with visual distractions, doesn’t seem entirely effective. It would be beneficial to test perturbations that are more representative of realistic environmental changes, which could better showcase BS-MPC’s resilience. Specifically, the paper lacks a detailed discussion on how the bisimulation metric loss interacts with the dynamics model learning, and how this interaction affects the overall stability of the learned latent space. Furthermore, the experimental section does not provide sufficient detail on the specific types of noise used, making it difficult to assess the generalizability of the results. The claim of faster training times due to parallel computation is not fully substantiated with concrete timing comparisons against other methods under similar hardware conditions.

### Questions
Could the authors expand on the sensitivity of BS-MPC to the parameter c4 and potential ways to reduce this dependency?

How does BS-MPC perform in scenarios with dynamic backgrounds that align with the movement instead of pure noise?

Are there additional computational costs associated with bisimulation metric loss, especially in high-dimensional latent spaces?

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
4

### Summary
This paper proposes BS-MPC, a model-based reinforcement learning approach that introduces bisimulation metrics (loss) on top of TD-MPC. Compare to TD-MPC, BS-MPC has an explicit encoder loss term, the adaptation of bisimulation metric, and parallelizing the BS loss. The authors found that their approach can improve training stability, robustness against input noise, and computation efficiency, which is validated on a set of simulation environments.

### Strengths
The paper is well-written and easy to follow. The overall presentation is good. The approach is sound and makes sense to the reviewer. The experimental results look promising, compared to TD-MPC.

### Weaknesses
However, the major weakness is its novelty.
1. The whole framework is based on TD-MPC. The difference is the authors introduce the Bisimulation metric and its corresponding loss design, which are from the existing literature, as stated in the paper.
2. It is also a common way to introduce additional regularization loss terms for the encoder of model-based RL.
3. The theoretical analysis mainly borrows from the existing work and does not have any major significant result. It would be great if the authors could provide "Under the BS loss training error, what's the performance gap between the final converged policy by their approach and the ideally optimal policy", and "Theoretically, how much performance gain could their approach improve, compared to TD-MPC."

### Questions
When you say BS-MPC improves computation efficiency, what does it mean? Is it compared to TD-MPC?
It is surprising to me because BS-MPC has one additional loss term compared to TD-MPC and why is BS-MPC faster to run? 

With the above question, I'd like to know the latency overhead of BS loss term in the training.

### Soundness
3

### Presentation
3

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
This paper considers model based reinforcement learning and proposes bisimulation metric to improve over temporal differential MPC method. The authors show theoretical analysis of the expected cumulative rewards in the latent space, and empirically demonstrate enhancement over TD-MPC and other baselines on several continuous control tasks.

### Strengths
The paper is clearly written and well presented. The proposed bisimulation metric seems to work well on the experiments considered, compared to TD-MPC and other baselines. The supplementary sections are comprehensive.

### Weaknesses
The novelty of the paper seems ambiguous. It seems that both on-policy bisimulation and TD-MPC methods are well studied for model based RL, and the authors plug bisimulation into TD-MPC.

There are several typos in the paper.
“In BS-MPC, the latent dynamics are modeled using an MLP. We also model the latent dynamics model with an MLP” I believe BS-MPC should be TD-MPC.
“we sample M action sets from Gaussian distribution N (μ0, σ0) based on the initial meanμ0 and standard deviation σ0” Missing spacing between mean and \mu_0

“We assume that the learned policy in BS-MPC continuously improves throughout training and eventually converges to the optimal policy π∗, which supports Theorem 1.”
This seems to be a very strong assumption. For example, by looking at the training curve, the return does not improve monotonically, and we have no information about if the learned policy is converging to the optimal policy. How do you explain such a strong assumption? Is it possible to remove it for the theoretical results?

In Fig. 4, why do all non-MPC based methods only have results till 10M steps?

### Questions
“We assume that the learned policy in BS-MPC continuously improves throughout training and eventually converges to the optimal policy π∗, which supports Theorem 1.”
This seems to be a very strong assumption. For example, by looking at the training curve, the return does not improve monotonically, and we have no information about if the learned policy is converging to the optimal policy. How do you explain such a strong assumption? Is it possible to remove it for the theoretical results?

In Fig. 4, why do all non-MPC based methods only have results till 10M steps?

### Soundness
3

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
4

### Summary
This paper is concerned with a new, model-based reinforcement learning method, which utilizes bi-simulation metric. This formulation helps with the stability of training and helps with the robustness of the controller. General idea is that they seek to find states that "behave" similarly, and intuition behind it is that one can use similar control input for similar states, which simplifies the controller and make it more interpretable. Authors learn an encoder which maps states of the environment to another domain, in which similar states are identified, and are mapped to the same representation (roughly speaking). Then, this representation is utilized to train a controller. Novelty of this work is to add the encoder loss directly into the training procedure.

### Strengths
Paper is well written, all ideas are clearly explained. Overall, paper is mathematically rigorous. Authors do a good job in walking the reader through the preliminaries, highlighting distinctions, and presenting their work.

Furthermore, paper presents more than 20 case studies, which helps immensely in comparing their performance to the state of the art methods.

### Weaknesses
Improvements and contributions seem incremental, and overall not that beneficial according to the case studies (Figure 6), one only sees improvements in few case studies (such as humanoid walk, dog walk and trot), and basically identical to TD-MPC in others (such as humanoid stand, pendulum, cheetah).
The only major contribution is adding the bi-simulation metric loss to the loss function, the other two contribution naturally follow from this addition.

As authors have mentioned, the hyper parameters play a huge role, and one wonders how much time is needed to tune these parameters.

I believe this theorem was added in haste, I originally asked the authors that if you are claiming robustness, you should do Lipschitz constant analysis. To which authors responded that it is intractable/computationally expensive, without knowing the Lipschitz constants, how can you claim you are more robust?

Moreover, equation 20 is misleading, Lipschitz continuity also applies to your encoding, and you also suffer from noise, if you employ global Lipschitz continuity. I personally think this theorem would hurt your paper rather than helping it.

### Questions
1- Based on your case studies, your method does not seem to change the episode return that much, except for a few cases like dog walk, dog trot and humanoid walk. In your Appendix, you provide a rough explanation of why that may be. Looking at Figure 7 and 8, it appears that loss, and consequently the gradient, explode (in TD-MPC), however, in RL, gradient clipping is used to tackle this issue. When you compared your method to TD-MPC, did you employ gradient clipping for it or not? It does not appear to be a fair comparison if you didn't, and perhaps that is why your method did not do significantly better in other case studies; as loss did not *explode*.  

2- I suggest you revise the experiments' section, and run all case studies on TD-MPC2 rather than TD-MPC. I realize it is touched upon in appendix D, however since TD-MPC2 is the updated version, I suspect it would make for a more fair comparison. Moreover, adding a thorough comparison would certainly present your method better; between training time, sample complexity, number of parameters used, and hyper parameter tuning and different configurations; it will strengthen your case if you could show how it might fail. I would also like to know the rationale behind using TD-MPC in the main body and mentioning TD-MPC2 in the appendix.  
To the best of my knowledge, TD-MPC2 can have many parameters, since it can be used on different domains. Thus, it is not an apple to apple comparison, unless it is specifically mentioned in the paper.


3- Is there any theoretical results on why your method requires less parameters, and converges faster? or is it mainly based off of experiments? Since Theorem 3 only offers an upper bound for expected cumulative rewards for the optimal policy. 

4- I suggest a more rigorous approach for robustness, such as comparing the Lipschitz constant of your controller to TD-MPC's.

5- I believe if you can theoretically confirm in which case studies your method is going to perform better than TD-MPC, it will strengthen your paper significantly.

### Soundness
3

### Presentation
3

### Contribution
2
