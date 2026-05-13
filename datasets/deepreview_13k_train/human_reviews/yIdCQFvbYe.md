# Bayesian Learning of Adaptive Koopman Operator with Application to Robust Motion Planning for Autonomous Trucks

- Decision: Reject
- Scores: 8, 5, 3, 8, 6, 5

## Abstract
Koopman theory has recently been shown to enable an efficient data-driven approach for modeling physical systems, offering a linear framework despite underlying nonlinear dynamics. It is, however, not clear how to account for uncertainty or temporal distributional shifts within this framework, both commonly encountered in real-world autonomous driving with changing weather conditions and time-varying vehicle dynamics. In this work, we introduce BLAK, Bayesian Learning of Adaptive Koopman operator to address these limitations. Specifically, we propose a Bayesian Koopman operator that incorporates uncertainty quantification, enabling more robust predictions. To tackle distributional shifts, we propose an online adaptation mechanism, ensuring the operator remains responsive to changes in system dynamics. Additionally, we apply the architecture to motion planning and show that it gives fast and precise predictions. By leveraging uncertainty awareness and real-time updates, our planner generates dynamically accurate trajectories and makes more informed decisions. We evaluate our method on real-world truck dynamics data under varying weather conditions—such as wet roads, snow, and ice—where uncertainty and dynamic shifts are prominent, as well as in other simulated environments. The results demonstrate our method’s ability to deliver accurate, uncertainty-aware open-loop predictions for dynamic systems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose to learn a dynamics prediction model that can adapt to different dynamical environment parameters for autonomous truck. The model leverages a transformer-based encoder of state and actions, plus Koopman-operator-based Bayesian learning for online adaptation. The method demonstrates SOTA performance compared to previous Koopman-operator-based approaches.

### Strengths
1. In 3.3 the effort to make the algorithm real-time in motion planning by using a variational encoder for action encoding such that sampling can be directly drawn from gaussian normal distribution is interesting and novel.
2. The writing of the paper is clear and easy to follow.
3. Combining Koopman operator with transformer-based encoding and adaptive control with Bayesian learning is an interesting paradigm.

### Weaknesses
1. More baselines outside of Koopman-based methods may be desired to connect the paper with other adaptive control and dynamics model learning paper, including but not limited to, models like neural ODE, PINN, or other uncertainty-aware approaches such as MC dropout.
2. No ablation study presents in the paper. See comments below.

Update in rebuttal
1. This weekness has been addressed from additional baselines that shows the author's proposed method is stronger.
2. The author now gives ablation study, but the results sometimes show only marginal performance improvement from the ablated components, which I assume is partially due to the simplicity of the environments. I encourage the authors to try on more challenging and long-horizon-demanding environments to better distinguish the effectiveness of the ablated component.

### Questions
1. (addressed in rebuttal) I assume the truck dataset would be heavily biased towards data of the vehicle driving straight with almost constant velocity, which may affect the quality of the model. If there are any effort to combat dataset imbalance, it would be beneficial to discuss.
2. (addressed in rebuttal) I’m not sure if the use of variational encoder to simplify online sampling is completely novel, but it would certainly be if this is the authors’ original idea. Otherwise maybe more related literature discussion is needed. I’ll leave this part to be answered by the authors and fellow reviewers during rebuttal phase.
3. (addressed in rebuttal, same comment as the weeknesses above) Some ablation studies may be needed. For example, BLAK without adaptation/bayesian learning. I’d like to know how much of the performance of the proposed method comes from the transformer + Koopman, versus how much is from bayesian learning.
4. (addressed in rebuttal) Additionally the authors could compare design choices with recent paper on transformer for adaptive vehicle dynamics prediction/control, such as details of how state/action are tokenized, encoding/decoding details, etc. Such as https://arxiv.org/abs/2409.15783, and https://arxiv.org/pdf/2310.08674

Other details
1. (addressed in rebuttal) Figure 1 caption is hard to follow. Suggest putting reference symbols (step A, B, C, etc.) on the plot.
2. (addressed in rebuttal) The authors start to use “BLAK” to refer to their method rather late into the paper (line 466) without first introducing what the term means.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a Bayesian framework for learning a Koopman operator-based predictive model. The model takes states and actions as inputs, allowing it to be used for planning. The authors use a transformer architecture to map the state to an embedding vector. They then use a Bayesian approach to formulate the distribution of the Koopman operator and that of the mapping from latent to state space. The posterior can be computed analytically given the data. To be able to sample efficiently during planning, the authors use a variational auto-encoder, which allows the action to be sampled in the latent space directly, as this corresponds to sampling from a Gaussian.

### Strengths
The paper is well written and easy to read. The problem is well motivated and the literature overview is adequate.

### Weaknesses
The proposed method has no theoretical guarantees. It would be interesting to at least have a discussion on what to expect without any formal result.

The algorithmic contribution is not very significant, as it consists of building blocks taken from existing methods.



### Questions
Line 145/146 has a typo.

Line 331: why does reducing the prior variance incur a broader posterior? Intuitively, the opposite is true. Do the authors mean increasing instead of reducing?

Is the method comparable to an approach that uses a nonlinear function to propagate the dynamics in the latent space, e.g., "Dream to Control: Learning Behaviors by Latent Imagination"?

How accurate  are model predictions using out-of-distribution data? An assessment with a corresponding distinction would be useful.

Can the proposed approach be used for reinforcement learning?

How does the approach compare to predictive approaches other than Koopman? It would be interesting to see how a one-step predictive method using a Bayesian neural network or Gaussian process performs.

In the appendix, the authors state that the data is collected using a TD3 agent. I feel that this is relevant and  should be mentioned in the main body of text.

Though it only uses a Gaussian process instead of a transformer, the paper "Gaussian Process-Based Representation Learning via Timeseries Symmetries" also provides a measure of model uncertainty. How does this compare to the proposed approach?

How well does the approach perform if the collected data is poor? How does the model perform out of distribution?

How well does the method scale? Eq. (11)-(13) indicate that the Gram matrix of the data needs to be inverted to compute the posterior, which scales cubically with the amount of data.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper deals with Koopman theory, where physical dynamics are modelled with data. To account for adapting dynamics, this paper proposes a Bayesian formulation. For example a model of a truck on desert or in snow results in different dynamics due to the distribution shifts, and the paper tries to incorporate uncertainty measures. The method is tested on a real data of a truck, validating the proposed framework.

### Strengths
Indeed, Koopman theory is one of the widely examined topic in robotics, and there, one needs to account for varying dynamics and incorporate uncertainty.

### Weaknesses
However, the paper needs to distinguish better between existing works. There has been active learning paradigms for Koopman theory, and how is this work better or differs? Those aspects should be taken into account for the list of contributions.
When compared to papers in robotic conferences, I think the paper fall short in terms of experimental evaluation, e.g., the paper uses a relatively small data set for the truck dynamics, while Koopman theory is more for learning complicated dynamics like soft robotic manipulators. Moreover, real world experiment should be there to indicate that the proposed method works in practice.
The paper’s topic might not also perfectly fit ICLR but rather IROS and ICRA.

### Questions
How valid is the prior being used here? Would there also be ways to incorporate the underlying physics more than isotropic Gaussians?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors propose a Koopman-based framework for robust motion planning for trucks. For modeling and prediction of nonlinear dynamics, an uncertainty-aware Koopman operator is introduced. The main idea is that a Bayesian regression model is utilized for the approximated operator, enabling uncertainty quantification based on its posterior distribution. Furthermore, distribution shifts (such as changing road conditions) are addressed by introducing a “changing variable” which detects potential shifts via a likelihood ratio test. Finally, the framework is integrated in a sampling-based motion planer. 

The main contributions are i) a novel uncertainty-aware data-driven Koopman operator (using multi-steps) based on Bayesian methods, and ii) real-time adaptation via distribution shift detections.

### Strengths
- In general, the paper is well written, the approaches are well motivated, and the presentation of the methods is clear.

- Based on my knowledge, the modeling of the approximated Koopman operator via Bayesian methods, resulting in a Wishart distribution for the posterior is novel and original. Furthermore, be combining the Koopman operator theory with transformers and the variational autoencoder for motion planning seems to be a smart and beneficial way to address the problem of robust motion planning. 

- The simulations results indicate that the proposed method can outperform other Koopman based methods and a standard MLP approach. In this way, it seems to be a significant improvement for this scenario based on this dataset.

### Weaknesses
1. The authors provide a detailed overview about the related state of the art. Reading this section, it seems that man of the “open challenges” that this paper addresses are already solved in some way in the existing literature. I assume that the authors do address existing gaps, but they missed to cleary point out these gaps. Me recommendation: Add some sentences in section 2 explaining the remaining research gaps.

2. 177: “Koopman […] under the assumption that the controls do not evolving dynamically” I’m not sure if I understand this statement correctly. My assumption is that “dynamically” refers to an input that depends on the state, i.e., a feedback controller. Even thought that might be a valid assumption, the title of the paper indicates the framework is for “autonomous trucks” where I assume we do have the feedback loop. 

3. Eq (4): From a data-driven perspective with a noise data set, etc, the extension to a multi-step input and output seems to make sense. However, based on the original Koopman theory, the extension seems to be unnecessary. 

4. While reading the paper, I stumble across Eq. (5). From my understanding, we do a non-linear mapping from the original non-linear dynamics to a high-dimensional but linear space. However, in eq (4), the authors propose to do a linear mapping form the lifted space to the original space. Maybe it is a misunderstanding, but that makes no sense to me. Furthermore, it is a general challenge to design the mapping that the inverse also exists. I do not see any evidence here that the inverse mapping might exist.

Minor:
- Citation style is often not correct (citep instead of citet, or the other way around)
-460: “Finally, While” -> while

### Questions
Weakness 2: Is this assumption still valid? What is the general problem with a dynamical input? Do you have an idea how to deal with it?

Weakness 3: Is there a theoretical justification for the multistep approach? Does it improve performance even for noise-free datasets? Could you provide more evidence on the benefit of this extension?

Weakness 4: Why is the inverse mapping model considered a linear function? Can you elaborate on the fact the inverse might even not exist?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a Bayesian Koopman operator for modeling of dynamical systems, that incorporates uncertainty quantifica-
tion. The goal is to make it flexible enough to deal with distributional shifts, which is achieved with an online adaptation mechanism, ensuring the operator remains responsive to changes in system dynamics. Distributional shifts are detected with a specific change variable. 

The approach is applied to motion planning and evaluated via a dataset of real-world truck dynamics data under varying weather conditions, and on other simulated environments. The original approach (using a transformer-based encoder), and a variant optimized for computational efficiency (variational encoder) are compared to several other Koopman operator-based approaches incorporating uncertainty quantification. The proposed approach shows best performance in the simulations, when it is not reduced for computational performance.

### Strengths
The proposed Koopman-based approach leveraging Bayesian learning for dynamic systems and distributional shifts in such systems is original. The paper is well written with clear presentation. Extending Koopman-operator based modeling to adapt to ucertainties is solving an improtant problem in plannig and control. 

The evaluation of the method is providing a comparison with state of the art methods in the field. A realistic dataset and some other simulated environments are used to benchmark the method.

### Weaknesses
1) I believe there is a piece of information which needs to be added, in particular computational times of the proposed approach. It would be interesting to directly compare the gain in computational efficiency from applying variational encoder. A table showing the corresponding computational times will help understanding the potential of the approach for realistic application. Especially for path planning, the assumptions, the time windows (how long is the sequence), the values of the tempering parameter, and the computational time will help demonstrating the efficiency of the algorithm.

2) Some justification in picking the transformer-based encoder will be helpful. Is there a real benefit of using it, given the overhead and the large amount of data needed to train it? Why using it, if afterwards they have to be reduced to variational encoders with lower performance, and with tempering parameters?

3) It would be useful to see a comparion in the path planning comparison with an approach which is not based on Koopman-representation, such as hierarchical planning (A* and RRT) or policy optimization, or any other approach.


Minor:
L.145 - repetition
L.200 - adopt --> adopt

### Questions
Under the assumption that the noise vectors are i.i.d sampled from a multivariate Gaussian distribution, the learning of the Koopman operator using Bayesian LR model proceeds. 
- How important is this assumption? Is it valid realistically for autonomous driving?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers the uncertainty and temporal distributional shift issues in the Koopman operator framework, and proposes to incorporate Bayesian learning to form adaptive Koopman operators. Experiment results on predicting truck dynamics and motion planning are shown to prove effectiveness.

### Strengths
The paper is in general clearly written, and the idea of incorporating Bayesian learning into adaptive Koopman operators seems novel. The authors also demonstrate improved results for state prediction and motion planning under uncertainties compared to several solid baseline methods.

### Weaknesses
While the idea of the paper seems novel, several key details are missing.

1. The pipeline of the proposed method does not seem clear. For instance, In Fig. 1, how is the embedding from the trajectory encoder combined with the embedding from the action encoder? How does the total loss for training look like given equation (6)?

2. Several assumptions in the theoretical part need justification, for example, in Lemma 3.2, “under the assumption that the number of datapoints N is large”, how is large defined and in practice can this condition be satisfied?

3. The experiment description is not very comprehensive. How are the baseline methods implemented? What is the goal and setting of the motion planning problem? Why were 200 and 300 chosen to be the epoch numbers? None of such information is presented in the main paper or the appendix.

A few typos in the paper:
1. ‘To mitigate these challenges, To address these challenges’ are repetitive in the Distribution Shift paragraph on page 3.
2. z_t should be \tilde z_t on page 4 before equation (3)?
3. In Table 2, BLAST is not consistent with BLAK that is used elsewhere for the proposed method?

### Questions
1. Why is \mathcal{K} of dimension \eta \times d?

2. Any comparison with adaptive Koopman operator methods? For example, the papers below.
https://arxiv.org/pdf/2202.09501
https://arxiv.org/pdf/2211.09512

3. How do you deal with error from finite dimensional approximation? This following paper considers it.
https://arxiv.org/pdf/2410.00703

### Soundness
2

### Presentation
3

### Contribution
3
