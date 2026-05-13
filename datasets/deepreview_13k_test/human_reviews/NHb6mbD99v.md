# Uncertainty-aware Distributional Offline Reinforcement Learning

- Decision: Reject
- Scores: 3, 6, 6

## Abstract
Offline reinforcement learning (RL) presents distinct challenges as it relies solely on observational data. A central concern in this context is ensuring the safety of the learned policy by quantifying uncertainties associated with various actions and environmental stochasticity. Traditional approaches primarily emphasize mitigating epistemic uncertainty by learning risk-averse policies, often overlooking environmental stochasticity.
In this study, we propose an uncertainty-aware distributional offline RL method to simultaneously address both epistemic uncertainty and environmental stochasticity. We propose a model-free offline RL algorithm capable of learning risk-averse policies and characterizing the entire distribution of discounted cumulative rewards, as opposed to merely maximizing the expected value of accumulated discounted returns.
Our method is rigorously evaluated through comprehensive experiments in both risk-sensitive and risk-neutral benchmarks, demonstrating its superior performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces UDAC (Uncertainty Aware offline Distributional Actor Critic), a distrubutional algorithm that tackles the problem of risk-averse policy learning via introduction of a risk-distortion function in the actor loss.  A typical probem in offline RL is that algorithms suffer from OOD issues, an attempt to remedy this is to stay close to the data distribution. This paper achieves this by decomposing the actor into a behavior policy part and perturbation part, the behavior policy is learned by a diffusion generative model and perturbation part is learnable by the distributional risk-averse RL loss. The contribution of the policy is controlled by a hyperparameter $\lambda$. The method achieves SotA results in risk-averseness on multiple benchmarks and is comparable to risk-netural algorithms on D4RL, some sensitivity analysis is provided.

### Strengths
Fairly extensive experimental evaluation and results that beat other methods. 

Perturbation formulation for trading-off staying on data vs. doing pure RL seems novel to me, but I could be wrong here since it is a very simple modification.

The method at its core is simple to understand.

### Weaknesses
There are a lot of errors in the math that is written in the paper (see questions).

Typos are also very prevalent, I didn't enumerate all of them.

No variance of the runs is reported so I cannot judge how stable the method is.

There are a lot of technical things in the paper that are not necessary and prevent the space from being used for better analysis of the method (there are some propositions in the appendix for example that don't appear in the main text). On the other hand, there are some terms used that are not defined.

The novelty of the paper is very limited (however, since the results are signficant I don't consider this an absolutely major flaw)

Justification for score: I think that the way the paper is written doesn't meet the bar for conference publication (with the equation flaws, typos and technical details that don't focus on the main contributions).

### Questions
I think that i) Elimination of Manual Behavior Policy Specification. ii) Accurate Modeling of the behavior policy is the same statement? You use diffusion generative models to model the behavior policy, that's it?

p2.par2 - "We conducted extensive experiments in three different environments covering both risk-sensitive" - it's 3 different benchmarks, you use multiple environments of D4RL.

p3. par2 - "For simplify" - to simplify

In Section 4 and earlier you talk about "risk-distortion operators", but you do not define the concept in the background section, yet it seems essential for your method.

In Section 4.1 you talk about implicit quantile functions, yet this concept has not been defined (what is implicit about them?) and no reference is given, I suppose you need [1].

There is no citation for the quantile Huber loss, you should provide a citation for it and refer to the equations the first time it is mentioned (ideally the definition would preceed  the first usage of the function).

p3, last par - you say that you use both uniform sampling and a quantile proposal network, then you say that you don't use a quantile proposal network and leave it for future work? If you don't use it, don't mention it here or mention it as a comment (an alternative is to use a quantile proposal network such as in (xyz citation)

In eq. 5, I suppose that you have N fixed quantile levels $\tau_i$, hence the indexing. However, this was not mentioned previously, yet it is part of the methodology (also along the lines of earlier work?). Moreover, the loss is a function o $\theta$ and there is no expectation defined over s, a, s', a', though the quantile td error depends on the former. Also, "J" is commonly used as return? Also normalizing factor should be $N^2$?

eq. 6 - is it "distortion risk function" or "risk-distortion function"? I also don't understand this loss function, you have expectations wrt. marginal state distribution, however you have an action appearing in the implicit quantile function, where does the action come from? You are missing a policy here, please define this correctly.

I think that your description of diffusion generative modelling needs significant adjustments. What you call an $\epsilon$-model is the denoiser, the Gaussian reverse process transition kernel arises from a continuous treatment of diffusion and exactly because of the choice of noise schedule. Since you don't provide contributions on level of diffusion generative modelling, this shouldn't take so much space of the paper.

p6 -   CQL is not a distributional RL algorithm?

suggestion for table 1 - use colors instead of bold and *

figure 2 needs correction, y axis is not visible, also there are no error bands - how do we know what is the stability across reruns?

Is the diffusion generative model absolutely necessary in order to achieve this performance? Would you switch it out for a CVAE in order to compare?

[1] Will Dabney, Georg Ostrovski, David Silver, Rémi Munos, "Implicit Quantile Networks for Distributional Reinforcement Learning"

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a model-free RL algorithm for learning risk-averse policies in offline RL setting. This algorithm uses distributional RL framework for obtaining risk-aversion to aleatoric uncertainty and diffusion model for modelling the behavior policy.
The authors claim that the diffusion model is better able to capture the different sub-optimal behavior policies used to generate the data than VAEs.
The authors show empirically that the proposed algorithm outperforms many of the existing offline RL algorithms in many risk-sensitive D4RL and risky robot navigation task and has comparable performance on many risk-neutral D4RL environments.

### Strengths
The authors evaluate the proposed algorithm on several risk-sensitive D4RL environments , Robot Navigation Task, risk-neutral D4RL environments and compares them with several baselines from recent work.

The authors also provide ablation studies on the effect of using different distortion operators and hyperparameters on the performance of the proposed framework.

### Weaknesses
The paper is not clearly written, for example, see first 4 lines of section 4.1.

Novelty is limited since risk-averse distributional offline RL have been explored by other work like [1].  This work only extends prior work by using diffusion model to model the behavior policy instead of VAEs.

The authors claim that using their framework accurately models the behavior policy but does not provide any theoretical justification for the claim.

The proposed algorithm and baselines are compared at a single CVaR confidence level $\alpha=0.1$. It would be good to evaluate them on different confidence levels.

While reporting the performance of the proposed algorithm and baselines, the authors do not provide the errors in the mean and cvar value of returns.


[1] https://arxiv.org/pdf/2102.05371.pdf

Additional Comments:
The first line of 4.1 is grammatically incorrect.

noise policies (section 4.2)  -> noisy policies

### Questions
How does this framework guarantee robustness against epistemic uncertainty without explicitly optimizing any robust measure of expected returns?

Why choose confidence level $\alpha=0.1$ while evaluating the performance of the framework with CVaR metric?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to mitigate both epistemic and aleatoric uncertainty in offline reinforcement learning by combining risk-sensitive RL and diffusion models. Specifically, the authors used a distributional critic to estimate risk measures and a diffusion model to model behavior policy.

### Strengths
1. Although some theoretical results and methods are mainly from prior works, this paper is still well-motivated and proposes a good method.
2. The experiments generally do a good job of illustrating the more risk-sensitive performance of the algorithm. Results show that UDAC performs well on risk-sensitive and risk-neutral tasks.

### Weaknesses
Major issues:
1. The paper uses a diffusion model, for the latter performs better than VAE, under the condition of a dataset with different modalities(in Section 4.2). This part seems to lack theoretical analysis for ”denoising a noisy mixed policy. How does the diffusion model decide which part of the policy is noisy? Or it's just the diffusion model has a better representational ability? Some theoretical analysis or a numerical one would be better.
2. In eq.(7) the policy $\pi_\phi$ does not take the risk distortion parameter as an input, does this imply that the policy's risk level can't be tuned? If it can be tuned, studying this would be more innovative than studying $\lambda$.
Minor issues:
1. In last paragraph of Section 1, DR4L should be D4RL.

### Questions
1. Please clarify how diffusion model learns from the behavior policy $\pi_b$ instead of cloning it. 
2. What are $\alpha_i, \overline{\alpha}_i$ in eq.(9) (10) (11)?
3. Does the policy learn a fixed risk-averse distortion? If so, can the network be modifed to accept different risk level in test time?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
