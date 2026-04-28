# DMBP: Diffusion model-based predictor for robust offline reinforcement learning against state observation perturbations

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Offline reinforcement learning (RL), which aims to fully explore offline datasets for training without interaction with environments, has attracted growing recent attention. A major challenge for the real-world application of offline RL stems from the robustness against state observation perturbations, e.g., as a result of sensor errors or adversarial attacks. Unlike online robust RL, agents cannot be adversarially trained in the offline setting. In this work, we propose Diffusion Model-Based Predictor (DMBP) in a new framework that recovers the actual states with conditional diffusion models for state-based RL tasks. To mitigate the error accumulation issue in model-based estimation resulting from the classical training of conventional diffusion models, we propose a non-Markovian training objective to minimize the sum entropy of denoised states in RL trajectory. Experiments on standard benchmark problems demonstrate that DMBP can significantly enhance the robustness of existing offline RL algorithms against different scales of ran- dom noises and adversarial attacks on state observations. Further, the proposed framework can effectively deal with incomplete state observations with random combinations of multiple unobserved dimensions in the test. Our implementation is available at https://github.com/zhyang2226/DMBP.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
When facing observation perturbations, reinforcement learning agent may perform very poorly. Unlike many prior work which train a robust policy, this paper instead utilizes diffusion model as noise reduction tool to retrieve accurate state information. Then the proposed framework feeds the de-noised state to any offline RL algorithm. Additional techniques are introduced, e.g., specialized loss to facilitate multi-step diffusion accuracy. Extensive simulations are conducted on MuJoCo control tasks.

### Strengths
1. The proposed framework uses the latest diffusion model to solve offline RL with state perturbations. I believe there is a strong motivation behind this approach. Indeed, an important RL problem is studied with state-of-the-art tool.

2. The paper is well-written. The motivations behind each section is quite clear. I enjoyed reading the paper a lot.

3. I believe the contribution is solid in this paper: (a) proposed a non-Markovian loss that facilitates multi-step diffusion accuracy; (b) a tractable version of its VLB is proposed; (c) thorough simulation and ablation studies

4. The proposed framework is very flexible and can work with any good offline RL algorithm.

### Weaknesses
There is no notable weakness in my opinion.

### Questions
1. When training different algorithms, do you use the same dataset size and batch size for all algorithms? 

2. In offline RL, especially the theoretical community, we are often concerned with the data coverage problem (full coverage vs partial coverage). I am interested in the performance of DMBP in this scenario. In particular, D4RL has millions of transitions in its dataset. Although one can argue that this is not that much for a continuous control task, we sometimes see more extreme case in tabular setting where the data is extremely limited, e.g., barely supporting the optimal policy's state-action visitation. I conjecture that if DMBP is paired with algorithm like VI-LCB[1] which is proven to be statistically efficient, it can also facilitate offline RL with scarce data setting. Do you have any insight on this?

[1]Li, G., Shi, L., Chen, Y., Chi, Y., and Wei, Y. (2022a). Settling the sample complexity of model-based
offline reinforcement learning. arXiv preprint arXiv:2204.05275

Overall I think this is a great paper, and it should be a good contribution to ICLR.

### Soundness
3 good

### Presentation
4 excellent

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
This paper addresses the challenges in offline reinforcement learning (RL), particularly the robustness against state perturbations. The authors introduce the Diffusion Model-Based Predictor (DMBP), a novel framework that employs conditional diffusion models to recover actual states in state-based RL tasks and proposes a non-markovian loss function to mitigate error accumulation. The framework is designed to handle incomplete state observations and various scales of random noises and adversarial attacks, improving the robustness of existing offline RL algorithms. DMBP is empirically evaluated, demonstrating significant performance improvements in terms of robustness against different perturbations on state observations without leading to over-conservative policies.

### Strengths
1. It is significant for this paper to promote the robustness of offline RL methods.
2. This paper shows its novelty by applying diffusion method to improve the robustness of offline RL against state perturbations, especially designing the non-Markovian loss function to reduce the accumulated error in state estimation.
3. The proposed method demonstrates strong performance and has been extensively evaluated with different offline RL methods and noise types and in various benchmark tasks. 
4. This paper is generally well written and easy to follow and covers well related works.

### Weaknesses
1. One main concern is that observation perturbations can be potentially addressed by traditional methods, especially when we assume observation perturbations does not affect reward and transition functions. The reviewer is curious of how offline RL methods with Kalman Filter perform compared to DMBP?
2. Minor issue: all results in tables should be shown with standard deviations.

### Questions
1. In the experiments, results show DMBP significantly improve the robustness performance of existing offline RL methods. The review noticed that most offline RL methods used are value-based. How will DMBP perform when used with weighted imitation learning methods, e.g., IQL?
2. Is DMBP sensitive to hyperparameters (i.e., a, b, c) of the variance schedule? Any guidance to choose these hyperparameters?
3. It is intutitve that diffusion denoising can perform well for random noise. Can the authors provide insights why it also works well for adversarial attacks?

### Soundness
3 good

### Presentation
3 good

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
Offline reinforcement learning (RL) enables training without real-world interactions, but faces challenges with robustness against state observation perturbations caused by factors like sensor errors and adversarial attacks. The Diffusion Model-Based Predictor (DMBP) framework has been introduced to address these issues by predicting actual states using conditional diffusion models, focusing on state-based RL tasks. Unlike traditional methods, DMBP leverages diffusion models as noise reduction tools, enhancing the resilience of existing offline RL methods against various state observation perturbations. The framework utilizes a conditioned diffusion model to estimate current states by reversely denoising data and incorporates a non-Markovian loss function to prevent error accumulation. DMBP's advantages include improved robustness against different scales of noise and adversarial attacks, as well as the ability to manage incomplete state observations, making it suitable for real-world scenarios like robots operating with malfunctioning sensors.

### Strengths
1. DMBP strengthens the resilience of existing offline RL algorithms, allowing them to handle different scales of random noises and adversarial attacks effectively.
2. Unlike traditional approaches, DMBP leverages diffusion models primarily for noise reduction, rather than as generation models. This innovative use helps in better state prediction and recovery against observation perturbations.
3. The framework introduces a non-Markovian loss function, specifically designed to prevent the accumulation of estimation errors over the RL trajectory.
4. DMBP offers a more balanced approach than methods that train robust policies against worst-case disturbances. This ensures that policies do not become overly conservative, which can hinder performance in certain scenarios.
5. DMBP's inherent ability, derived from the properties of diffusion models, allows it to effectively manage situations with incomplete state observations. This is particularly valuable in real-world applications, such as when robots operate with compromised sensors.

### Weaknesses
1. The paper has the assumption that perturbation on state space follows a Gaussian distribution. However, in practical settings, such perturbations might be biased and skewed. For example, a water drop on a camera might lead to distortion of captured images. Therefore, it might be better if the authors could elaborate on the assumption of the perturbations and how they are produced. 
2. Introducing a diffusion model for noise reduction could increase the complexity of the model, which may lead to longer training time and resource-intensive computations. The authors might want to include more details regarding training time and computational resources.
3. Scaling to very large state spaces or handling very noisy environments might pose challenges, especially when using diffusion models. It would be better for the authors to consider testing on tasks with larger state spaces such as the humanoid. 
4. Eq.(2) is wrong as the recovered state should not be a probability.

### Questions
Same as the weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents DMBP, a novel framework for robust offline RL. DMBP addresses the challenge of handling state observation perturbations by employing conditional diffusion models to recover the true states from perturbed observations. Additionally, it proposes a non-Markovian training objective to reduce the cumulative errors by minimizing the sum entropy of denoised states along the RL trajectory. Experimental results show that DMBP significantly enhances the robustness of current offline RL algorithms, effectively addressing various perturbations and incomplete state observations.

### Strengths
* Overall, this paper is well-organized and easy to follow.

* The introduction of the diffusion model as a means to recover true states from perturbed observations, addressing the challenge of observation perturbation, is both novel and sound. Besides, the inclusion of the regularization of sum entropy for denoised states across the RL trajectory is highly meaningful in the context of sequential decision-making, effectively mitigating error accumulation.

* The proposed method can be applied to many model-free offline RL algorithms and significantly improves over prior works in terms of observation robustness and masked observations.

I believe this paper represents a significant contribution to the field and will have a substantial impact on the research community.

### Weaknesses
 * The literature review section lacks a discussion of another taxonomy: training-time and testing-time robustness. While this paper and many others focus on offline RL for testing-time robustness, there is another group of offline RL works that investigate training-time robustness [1] [2] [3]. These works involve corrupting the offline dataset and evaluating it in a clean environment. It would be beneficial to include the training-time works for a more comprehensive literature review.

* It is not clear whether the states in this paper are normalized. Normalizing the observations would ensure fair observation corruption and may potentially impact the recovery ability of the diffusion model. Specifically, without normalization, noise of the same scale will have a minimal impact on dimensions with large scale values, but a significant impact on dimensions with small scale values. The corruption is therefore biased for different dimensions.

* Currently, it seems that the diffusion model is trained using complete observations even in the experiments with incomplete observations. I am curious to know if the diffusion model can handle training with incomplete observations as well.

* Additionally, the authors are suggested to report the training time and the inference time of the proposed method. The computational cost of DMBP appears considerable compared to other algorithms, and it would be beneficial to discuss potential future strategies to mitigate this issue.

* Typo: page 2 'A diagram of the proposed approach is shown in the fight subplot of Figure 1' --> 'A diagram of the proposed approach is shown in the right subplot of Figure 1'.

### Questions
My questions are listed in the "Weakness" part:

* The authors are suggested to provide a more comprehensive literature review.

* It is necessary for the authors to clarify whether the observations are normalized. If not, it would be beneficial to include a comparison and provide further clarification.

* The reviewer is interested in knowing if the diffusion model can also handle training with incomplete observations.

* The authors are recommended to include information about the training time and inference time of the proposed method.

* Fix the typo.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
