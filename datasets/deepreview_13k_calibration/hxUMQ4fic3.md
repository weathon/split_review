# Neural Stochastic Differential Equations for Uncertainty-Aware Offline RL

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Offline model-based reinforcement learning (RL) offers a principled approach to using a learned dynamics model as a simulator to optimize a control policy. 
Despite the near-optimal performance of existing approaches on benchmarks with high-quality datasets, most struggle on datasets with low state-action space coverage or suboptimal demonstrations.
We develop a novel offline model-based RL approach that particularly shines in low-quality data regimes while maintaining competitive performance on high-quality datasets.
Neural Stochastic Differential Equations for Uncertainty-aware, Offline RL (NUNO) learns a dynamics model as neural stochastic differential equations (SDE), 
where its drift term can leverage prior physics knowledge as inductive bias.
In parallel, its diffusion term provides distance-aware estimates of model uncertainty by matching the dynamics' underlying stochasticity near the training data regime while providing high but bounded estimates beyond it.
To address the so-called model exploitation problem in offline model-based RL, NUNO builds on existing studies by penalizing and adaptively truncating neural SDE's rollouts according to uncertainty estimates.
Our empirical results in D4RL and NeoRL MuJoCo benchmarks evidence that NUNO outperforms state-of-the-art methods in low-quality datasets by up to 93% while matching or surpassing their performance by up to 55% in some high-quality counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents NUNO, a method for offline reinforcement learning that uses neural SDEs to model dynamics with uncertainty. The SDE structure consists of a drift term that incorporates prior physics knowledge (as an inductive bias) and a diffusion term that captures uncertainty. Further, the uncertainty term is designed to account for both aleatoric and epistemic uncertainties explicitly to obtain accurate uncertainty estimates. By incorporating physics-based inductive biases and adaptive rollout truncation, NUNO mitigates model exploitation, where policies may overfit unreliable parts of the model.

### Strengths
**Strengths**
I like the paper overall. Here are some general comments. 
- Impressive Results on Noisy Datasets: The paper achieves particularly strong performance on challenging, low-quality datasets, highlighting the robustness of NUNO’s uncertainty modeling in noisy conditions.
- Clear Presentation: The paper is well-written, with a logical structure that effectively communicates complex methods and results, making it accessible even with its technical depth.
- Novel Modeling Approaches: The decomposition of uncertainty into aleatoric and epistemic components, and learning them separately, stands out as an interesting and valuable contribution. This approach advances the understanding of uncertainty in offline RL and reinforces the model’s reliability.

### Weaknesses
 **Weaknesses**
- Lack of Ablations for Design Decisions: A detailed analysis of each design decision, particularly the separate uncertainty terms, , would clarify their individual contributions to the model’s performance. Specifically, it is unclear how the distance-aware uncertainty estimate interacts with the aleatoric uncertainty, and whether both are necessary for good performance. The paper would benefit from ablating these components to understand their individual impact on the final policy performance. For example, what happens if only aleatoric uncertainty is used, or only the distance-aware uncertainty is used? A more granular analysis of these choices is necessary.
- Limited to Low-Dimensional Environments: The experiments are confined to low-dimensional MuJoCo environments, without tests on high-dimensional settings. Such environments may reveal limitations of the approach, where ensemble-based uncertainty methods could potentially perform better. The current evaluation does not explore the scalability of the method to higher dimensional state and action spaces, which is a crucial aspect for real-world applicability. It is important to understand how the neural SDE dynamics model scales with the complexity of the environment. 
- Limited Scope on Partially Observable/Image-Based Domains: Although the paper notes the absence of experiments in partially observable or image-based environments, this remains a notable gap. These domains may challenge NUNO’s performance, and ensemble-based approaches might excel here due to their structure. Expanding experiments to these settings could provide a more comprehensive evaluation. The method's reliance on a fully observed state space is a limitation, and the paper should discuss how the method could be extended to handle partial observability, or at least acknowledge the limitations in this regard.

### Questions
same as weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this work, the authors propose a method for offline model-based reinforcement learning that leverages uncertainty to enhance performance in settings with low-quality data or limited samples. The approach involves learning a model of the environment from samples using Neural Differential Equations (NDE), incorporating uncertainty and physics-informed learning. To account for uncertainty in the NDE, the authors introduce a parametric, distance-aware uncertainty estimator. Unlike kernel k-th nearest neighbor, this estimator avoids expensive search requirements while maintaining desirable properties such as monotonicity and boundedness. The estimator is used to limit the differential equation’s rollouts when distance is sufficiently high, restricting state-action paths to high-quality model rollouts and penalizing high-uncertainty paths, thereby encouraging the agent to favor paths where the NDE model is well-behaved. Simulations on D4RL and NeoRL, varying the quality of the policy used for offline training, demonstrate that the proposed method outperforms baselines in many cases. These baselines consist of other uncertainty-aware model-based methods that also penalize and truncate paths based on uncertainty.

### Strengths
- (S1): The problem of offline training with few samples and low-quality policies is a relevant one with significant applications in real-world settings.

- (S2): Extensive simulations, including hyperparameter searches and comparisons to baselines, demonstrate promising results.

- (S3): The manuscript is well-explained and relatively easy to follow, and the authors provide a thorough literature review that clarifies the position of their proposed method within the existing body of work.

- (S4): The proposed Distance-Aware uncertainty estimator is particularly interesting and may be useful for other problems. The authors ensure that their estimator is well-behaved through mathematical analysis, and they impose desirable properties on it through careful considerations in the optimization process.

### Weaknesses
 - (W1): Some of the main contributions listed by the authors are not representative of the actual content presented in the paper. This could be improved by shifting the focus to other key aspects of the proposed method (see questions).

- (W2): The concept of uncertainty is underdeveloped in the manuscript, despite being a vital component of the proposed method. Although the authors clearly define distance-aware uncertainty, it is unclear what this concept represents in a broader context, given that the notion of uncertainty varies across applications and methods. This could be improved by examining the inner workings of their proposed uncertainty estimator in the simulated environments.

- (W3): While the results on the selected environments across different data regimes are promising (though other methods perform similarly to NUNO), there is a lack of exploration into the inner workings of the method. Obviously, simulations in these environments are computationally expensive, setting up a simpler problem with a known ground truth could enable multiple regime tests and ablation studies of the proposed method. This is especially important given the method's multiple components, and providing a thorough explanation of why and how the method works would significantly enhance the paper’s contribution.

### Questions
- Q1: How does incorporating prior physics knowledge differ from simply parameterizing the state space in a convenient way? Choosing a state representation is a standard design choice in most RL problems. How does this incorporation of prior knowledge apply to applications outside of MuJoCo? The parameterization in Equation (8) appears very specific to this case. Could you incorporate other types of physics knowledge, such as gravity, joint resistance, or environmental viscosity? One could argue that these environmental properties also represent physics knowledge.

- Q2: What are the implications of using dataset distance as an uncertainty estimator? The dynamical SDE described in Equation (5) can separate epistemic and aleatoric uncertainty in the dynamical model, where the epistemic uncertainty term depends on the distance-aware uncertainty estimation. It is possible that points further from the modes of the training set are influenced by noise, leading to high distance, and thus high epistemic uncertainty (since h in Equation 5 is monotonic). Conversely, a high-distance point could be "stable" (not noisy), with the dynamical model learning it well, so true epistemic uncertainty should be low for this point but is high according to the distance estimator.

- Q3: Related to the previous question, as the pessimistic reward is discounted by the distance-aware estimator, why isn’t aleatoric uncertainty considered here (as in Equation 5)? Highly noisy trajectories from the dynamical model cannot be learned by the agent, but they are not penalized, only those that the model hasn’t learned well enough based on distance are. This also relates to the previous question.

- Q4: How critical is this particular distance-aware uncertainty estimator? Why not use other uncertainty surrogates, such as prediction error from the dynamical model or the frequency of updates in a region (number of visits)? These other types of uncertainty estimation have been used in exploration-exploitation trade-offs in RL agents. This, and other ablation studies could be explored in a toy model.

- Q5: Typo in Equation 8: I believe the first variable should be s_{pos}? Additionally, the uncertainty penalization in Figure 1 doesn’t match the equation, and some notation in the figure is inconsistent with that used in the main text.

### Soundness
2

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
This paper introduces an offline model-based reinforcement learning method that can work well in low-quality data regimes while maintaining competitive performance on high-quality datasets. NUNO, the proposed  Neural Stochastic Differential Equations for
UNcertainty-aware Offline RL,  learns a dynamics model as neural stochastic differential equations (SDE), where the drift term integrates   physics knowledge to provide inductive bias, and the diffusion term estimates uncertainty to control the effects of uncertain predictions. Additionally, the paper addresses model exploitation by penalizing and truncating predictive rollouts, achieving strong results on several control benchmarks.

### Strengths
The paper proposes  a Neural Stochastic Differential Equation based method to address the important challenge of underrepresented state-action pairs in offline datasets and achieves strong experimental results. It has a solid theoretic foundation, and it is innovative and interesting. 

The proposed method is well thought out, and the design for the uncertainty estimator has good local theoretical properties. 

The paper is mostly well-written and easy to follow.

### Weaknesses
The proposed method relies on decomposing the state into position and velocity, and it imposes strong assumptions on the underlying environment dynamics (e.g., the dynamics must satisfy rigid body dynamics). I suggest that the authors also elaborate on how to apply the  physics-informed approach to other setting (not just position/velocity based). 
While incorporating such prior physics knowledge is beneficial in some cases, clearly it is  not possible in all RL applications. 

 Regarding the design of uncertainty estimator in 4.1, it would help to include simulation experiments under simplified settings of MDP and datasets to explicitly quantify the effects of the design choices.  This would shed light on the design of uncertainty estimator and hence the SDE model.

The computational overhead can be very high. Specifically, what is the computational overhead in training due to sampling around each data point for the uncertainty estimator? How does this affect the scalability of the method in high-dimensional datasets?

### Questions
In Equation 3, on the definition of \mathcal{L}_{\mu}, how is it guaranteed that the denominator $\mu$ is not zero in experiments?

In Equation 6, what is the intuition of the term log(det(\Sigma)) in the context of \mathcal{L}_{\text{data}}?

Could you provide examples of "unmodeled dynamics" as mentioned in Lines 342–343?

If the unmodeled dynamics are significant, would it still be beneficial to penalize the residual term?

### Soundness
3

### Presentation
3

### Contribution
3
