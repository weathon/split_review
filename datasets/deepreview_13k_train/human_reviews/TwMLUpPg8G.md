# Discovering Physics Laws of Dynamical Systems via Invariant Function Learning

- Decision: Reject
- Scores: 5, 6, 5, 3, 6

## Abstract
We consider learning underlying laws of dynamical systems governed by ordinary differential equations (ODE). A key challenge is how to discover intrinsic dynamics across multiple environments while circumventing environment-specific mechanisms. Unlike prior work, we tackle more complex environments where changes extend beyond function coefficients to entirely different function forms. For example, we demonstrate the discovery of ideal pendulum's natural motion $\alpha \sin{\theta_t}$ by observing pendulum dynamics in different environments, such as the damped environment $\alpha \sin(\theta_t) - \rho \omega_t$ and powered environment $\alpha \sin(\theta_t) + \rho \frac{\omega_t}{\left|\omega_t\right|}$. Here, we formulate this problem as an $invariant\ function\ learning$ task and propose a new method, known as $\mathbf{D}$isentanglement of $\mathbf{I}$nvariant $\mathbf{F}$unctions (DIF), that is grounded in causal analysis. We propose a causal graph and design an encoder-decoder hypernetwork that explicitly disentangles invariant functions from environment-specific dynamics. The discovery of invariant functions is guaranteed by our information-based principle that enforces the independence between extracted invariant functions and environments. Quantitative comparisons with meta-learning and invariant learning baselines on three ODE systems demonstrate the effectiveness and efficiency of our method. Furthermore, symbolic regression explanation results highlight the ability of our framework to uncover intrinsic laws.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
The paper proposes a novel method called Disentanglement of Invariant Functions (DIF) for discovering underlying physics laws of dynamical systems by learning invariant functions across different environments, addressing challenges with dynamics where changes extend beyond function coefficients to entirely different forms. The approach uses a hypernetwork-based encoder-decoder framework, grounded in causal analysis, to disentangle invariant functions from environment-specific dynamics, demonstrating effectiveness through comparisons with meta-learning and invariant learning baselines.

### Strengths
- Well-Written and Easy to Follow.

- Novel Method for Invariant Learning: Proposes the Disentanglement of Invariant Functions (DIF) to discover underlying physical laws, effectively disentangling invariant dynamics from environment-specific factors.

- Causal Analysis and Hypernetwork Design: Uses causal analysis and a hypernetwork-based encoder-decoder framework to handle complex environments, ensuring robustness and accuracy in discovering invariant functions.

- Comprehensive Evaluation: Validates the effectiveness of the approach through extensive comparisons with existing baselines and demonstrates its ability to uncover interpretable physical laws via symbolic regression.

### Weaknesses
I am not an expert in this field, so I will defer to other reviewers for a more informed evaluation. Based on my understanding, the theoretical contributions seem to be relatively limited, relying primarily on existing theorems in information theory. Additionally, the experimental evaluation appears limited, focusing mainly on one-dimensional pendulum systems with varying parameters, which may not sufficiently demonstrate the broader applicability of the approach.

- Limited Scope of Evaluation: The paper's experiments are primarily conducted on simple one-dimensional pendulum systems, which may limit the generalizability of the approach to more complex and diverse dynamical systems beyond ordinary differential equations (ODEs). Thus, I question the scability of this method in more complex scenarios. 

- Basic Theoretical Contributions: The presented theorems appear to be based on well-established concepts in information theory, providing limited novelty in terms of theoretical advancements.

- Dependency on Accurate Causal Graphs: The proposed method's effectiveness depends heavily on accurately formulated causal graphs, which may not always be feasible in complex real-world systems where the causal relationships are unclear or difficult to determine.

### Questions
See the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper attempts to solve the invariant learning problem in ODEs. By observing the ODE dynamics in multiple environments, the invariant dynamics can be inferred. The authors adopted a causal perspective and designed a hypernetwork to learn the invariant function of the dynamics of the ODE.

### Strengths
1. It is interesting and of practical significance how to learn the shared dynamics from data collected across different environments.
2. The authors use a causal perspective to design the method, which provides some theoretical guarantee.
3. The method demonstrates the ability to discover the form of the invariant ODE, as well as higher prediction accuracy of the invariant ODE.

### Weaknesses
1. According to Eq. 4a and 4b, one must first acquire the label of the environment to use the proposed method. This may limit the applicability of the method, as obtaining such labels might not always be feasible in real-world scenarios. The requirement for explicit environment labels restricts the method's use to settings where these labels are readily available or can be easily inferred, potentially excluding cases where the environment is unknown or changes dynamically.

2. The constraint of the independence between the environment and the learned fc is implemented in an adversarial way. This is the central component allowing the proposed method to achieve invariant function learning, so it will be better to justify the design of the adversarial training theoretically. The current justification is lacking in detail, and a more rigorous theoretical analysis is needed to understand why the adversarial training approach effectively enforces the desired independence. Without a strong theoretical foundation, it's difficult to assess the robustness and limitations of this approach.

3. The ability to discover the form of the invariant ODE is not compared to the baselines. This makes it difficult to assess the novelty and effectiveness of the proposed method in discovering the underlying dynamics. A comparison with existing symbolic regression techniques or other methods for learning ODEs would provide a clearer understanding of the method's strengths and weaknesses in this aspect.

Minor:
- line 170, 'we explicitly exposes...'
- line 275, 'In order to discovery invariant functions...'
- line 890, 'According to Lemma 3.2, we can that the negative log-likelihood...'
- line 1177, Eq. 22e, phi should be \phi

### Questions
1. What is the exact form of the normalized RMSE in the experiments? In Fig. 4b the deviation looks very small but in Table 2 the NRMSE for predicting Xc from fc is as high as about 0.35.
2. Does the proposed method have the potential to facilitate learning under noisy observations? I understand that Assumption 1 does not hold anymore and the causal graph needs to change, but can the idea of invariant function learning extend to robust learning of dynamical systems?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper suggests an approach to learn invariant functions of dynamical systems governed by ODEs. To do so, the authors present a neural network architecture that is claimed to identify an invariant function $f_c$ and an environment specific function $f_e$. Both functions are represented as neural networks.  Using trajectories of the same dynamical system under multiple interventions/perturbations, the hypernetwork is trained end-to-end and outputs a set of parameters for $f_c$ and $f_e$. By splitting the input information into two embeddings, an invariant embedding and a contextual one, the paper claims to identify the correct invariant function.

### Strengths
The paper addresses an important problem and I can follow the suggested approach and the reasoning behind. The proposed method includes an information-based principle to enforce independence between invariant functions and environment-specific dynamics. This theoretical guarantee adds rigor to the approach, suggesting a data-driven way to uncover intrinsic dynamics across varied environments.
It is well-organized, with each step building logically. The abstract introduces the problem, presents the solution (DIF), explains the methodological novelty, and provides an overview of validation results, all in a clear sequence. The figures are appealing.

### Weaknesses
Assumption 1 appears very restrictive and almost impossible to guarantee. In my opinion, assumtion 1 implies perfect similarity or deterministic knowledge, with no randomness or difference between the distributions in question. This however seems unrealistic as this would require knowledge of the dynamical system under any intervention possible. As a result, I think the proposed optimization problem might not converge to a reliable solution if $P(X_p)$ is not chosen appropriately.

Given this, the experimental evaluation seems weak and insufficient. The experiments comprise three test cases and in one of them, the suggested method is not capable to identify an invariant function that can accurately forecasts  the invariant dynamics (see Figure 9b in the Appendix). It is mentioned that the approach captures the most important frequencies on this test case, but no evidence of this claim is given. I think it is important to evaluate the approach more thoroughly and perform ablations that study the impact of available trajectories in $X_p$ and the number and types of interventions necessary to robustly identify the invariant dynamics.

Another limitation is the focus on ODEs, which I find somewhat unclear. Conceptually, the approach presented here should be adaptable to PDEs with minimal modifications, particularly given the derivative-based training method. This raises the question of why PDEs were not considered in the study.

I believe a useful baseline would involve using a slightly modified version of this architecture. To determine if there is any advantage to explicit disentanglement within a joint training framework, it would be helpful to compare this approach against two independently trained networks similar to the suggested network. Specifically, the first network would handle the invariant mechanism:$X_p \rightarrow TF \rightarrow h_{inv} \rightarrow \hat{z}_c \rightarrow decoder \rightarrow \hat{f}_c \rightarrow forecaster + X_0 \rightarrow \hat{X}^c$ The second network would focus on trajectory specific forecasting: $X_p \rightarrow  TF \rightarrow  h_{env} \rightarrow \hat{z} \rightarrow decoder \rightarrow \hat{f} \rightarrow forecaster + X_0 \rightarrow \hat{X}$

In Section 2.2.1, you identify the causal mapping $f \rightarrow X$ as injective. In the optimization problem, this translates to making $P(f∣X_p​) \rightarrow X$ injective. How do you ensure this property when using a nonlinear decoder? The encoder-decoder framework you propose for compressing invariant function representations into hidden representations is reasonable. However, in an autoencoder, the decoder is typically not injective. Since the encoder reduces dimensionality, multiple different inputs could map to the same latent representation, making it non-injective. Consequently, for the decoder, which maps from $z$ back to $\hat{X}$, multiple inputs could map to the same or similar reconstructed values, also resulting in non-injectivity. For this reason, I believe the proposed framework does not fully align with the theoretical requirements presented.

I understand the approach of implementing the independence constraint adversarially by minimizing the informativeness of the environment prediction $P(e ∣ f^{c})$. However, since the discriminator and adversarial loss work in opposition, some environmental information is likely to remain in the invariant encoding—specifically, environmental details shared across interventions, such as similar types of interventions. Consequently, this shared environmental information may still be incorporated into the invariant embedding, which in turn means that the architecture does not fully achieve the claimed independence.

To provide a more intuitive understanding of the pipeline, I suggest including the discriminator in Figure 2 and adding all loss terms. If space is limited, the bottom half could be moved to the appendix.

(typo in eq. 22e)

### Questions
The exact definition of $X$ remains unclear throughout the paper. Does $P(X)$ represent the distribution of all possible trajectories under any imaginable intervention?

Is the idea that the parameters $f_c$​ remain constant regardless of the input trajectory $X_p$​, or do you envision $f_c$​ as lying on a specific manifold within the parameter space?

Have you tried to input high-dimensional transformations, e.g. sequences of images of the different dynamical systems during training?

Could you please confirm whether the function embedding $\hat{z}$ is calculated using a linear transformation applied to the concatenation of $\hat{z}_c$​ and $\hat{z}_e$​ as input?

What is the performance difference between derivative training trick and training with an integrator? I assume that the datasets contain the ground truth derivatives of the dynamics, what is the impact on performance if numerically approximated derivatives are used?

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
3

### Summary
The paper proposes an approach to predict the dynamics functions of ordinary differential equation-based dynamical systems. The particular twist in this paper is that all observations are assumed to be governed by unique dynamics functions that are only partially shared across observations. The goal is to infer the common part of the dynamics function that is shared across all observations. The difficulty is that this shared part is not observed directly in any observation.

### Strengths
The paper proposes a novel problem setting that has not been tackled so far. The writing is for the most part very clear (with the exception of the theoretical section, see my comments below) and the figures greatly illustrate the idea of the paper. The authors propose an empirically evaluate a new computational model and also attempt to theoretically motivate their approach (see comments below though). Given the novel and innovative problem setting, there seem to not be any readily-applicable baseline models out there. The authors therefore also propose / adapt several baseline models to compare their approach to - and show empirically that the proposed approach outperforms these baseline models.

### Weaknesses
My main issue with this paper concerns the theoretical section - there are some things that I either do not understand / find hard to follow or that are incorrect.

Theorem 3.1 states that the predicted function is equivalent to the true function if and only if the invariant function learning principle of equation 2 is satisfied. However, equation 2 is not a a equation (or inequality) - it rather boils down to a real number (the mutual information between predicted and true function). I don’t really understand what it is supposed to mean to satisfy a real number.

Moreover, equation 2 compares the true function and the predicted function in terms of (conditional) mutual information. One thing that is unclear to me though is what the distribution of the true function f is supposed to be: to my mind, there is presumably exactly one true underlying function and hence the distribution is a dirac delta impulse. However, the mutual information between a dirac delta and any different function seems to be always zero, which makes me question this statement. (You can find a derivation for discrete random variables here, I believe the same derivation also works for continuous random variables: https://stats.stackexchange.com/questions/25095/mutual-information-with-a-dirac-delta-type-pdf).

In section 3.2.1 you train encode and decoder by  “apply[ing] the cross-entropy minimization.” According to the following lemma 3.2, however, it seems that you instead use the MSE as objective function. What is the reason to first say that you use CE while in practice (and theory) you actually use the MSE?

Lemma 3.2 states that under a Gaussian relaxation (which is not motivated in any way), optimizing the cross-entropy is equivalent to optimizing the MSE; this could be made more precise since what the authors mean is probably that the optimal minimizer is the same. (The actual objective values at their respective minimum, however, are most likely not the same).

(Minor:) In equation 4a, I suggest to replace $\hat{X}^c$ with $h_{\theta_c}(X_p)$ so that it is immediately clear where parameters $\theta_c$ enter the objective. Moreover, I find the statement “where $\hat{X}^c$ is the trajectory predicted by $P(X|h_{\theta_c}(X_p), X_0)$” slightly confusing since P is a distribution whereas X is a prediction (/estimate). If I understand correctly, $\hat{X}^c$ is simply the output of $h_{\theta_c}(X_p)$, integrated using a numerical solver with initial value $X_0$. (In other words, simply saying that $\hat{X}^c$ is predicted by the distribution P leaves open the question of how exactly X was obtained from the distribution.)

These issues are the main reason for the currently assigned presentation and soundness (as well as overall) scores.

It is not clear to me how the function composition $g_{comp}$ in Appendix B.1 is supposed to work. If $f_c$ and is only caused by $c$ and $f_e$ is only caused by $e$, is it even certain that you can combine them into a single function $f$? How could such a function $g_{comp}$ look like in practice? For instance, to stay with the examples of Table 2, couldn't $f_e$ be an environment-specific realization of the Lotka-Volterra function while $f_c$ is the common underlying function of the Pendulum? In essence, I do not really understand the generative process here.

I also do not fully understand the setup of the predictive model. In section 3.1 you write
> The function space $\mathcal{F}$ consists of all possible neural networks with $m$ parameters, and a function $f \in \mathcal{F}$ can be represented as a vector in $R^m$.
However, I do not see how a point in $R^m$ uniquely identifies any possible neural network (NN) with $m$ parameters: e.g. assume $m = 6$, two possible neural networks are e.g. 1) an 4-layer NN with 2-1-1-2 parameters per layer or 2) a 3-layer NN with 2-2-2 parameters per layer. These seem to model very different functions yet both could map to any point in $R^m$.

In addition I also share the concern from other reviewers that it may not be easy to group observations into environments (that is, to obtain environment labels.) This also touches on my original question about potential applications which you answere as 
> We believe invariant function learning represents an exciting hindsight for modeling dynamical systems. While this paper focuses on ODEs, the concept is more general and theoretically extensible to PDEs. However, such adaptations present challenges (e.g., sampling high-dimensional variables) that warrant further research. 

These are nice ideas for model extensions but, from my perspective, do not describe potential applications where inference from multiple minimally different environments (which after all is the main concern of this manuscript) needs to be considered.

### Questions
- The symbolic regression literature has proposed several works using transformers for dynamical systems inference [1,2,3], which I believe may also be regarded as hyper networks. I think it would be good to include a statement in the related work section on how they relate to your work.

- An interesting additional baseline to your problem could be to run PySR on the different environments directly. Since PySR predicts symbolic function, one might naively think that this should be sufficient to discover the invariant part of the equations that is shared across all systems. I.e. PySR would spit out a environment-specific equation for each environment but these might already contain the shared parts so that no additional modeling that explicitly takes this problem setting into account would be necessary. It would be good to see results on this to judge the value of your approach.

- In section 2.2.1 you mention (at the end of page 3) that “This reverse inference requires causal mapping f → X to be injective.” How reasonable is this assumption / requirement? It seems to me that this is in general (i.e. without restrictions on the function class that f comes from) is violated, since there can be multiple functions that generate the same output (especially if the output is from a finite interval, as it will be in practice.)

- Where do you see applications of your approach in practice? Have you tried evaluating it on any real world dataset that contains noise, missing data etc.? 

References:
[1] Becker et al., (2023) "Predicting Ordinary Differential Equations with Transformers"
[2] d'Ascoli et al., (2024) "Odeformer: Symbolic regression of dynamical systems with transformers"
[3] Seifner et al., (2024) "Foundational Inference Models for Dynamical Systems"

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers the problem of learning invariant mechanisms that are shared across similar dynamical systems governed by ODEs observed in multiple environments. It introduces a new method, Disentanglement of Invariant Functions, to tackle this problem using a hypernetwork for function prediction and then a separate approach for forecasting.

The numerical examples show that invariant learning techniques outperform meta-learning methods for that task, and that the proposed approach performs the best among the invariant learning techniques compared. In these examples, the invariant functions extracted are more or less aligned with the true invariant mechanisms. A new hypernetwork implementation is presented and shown to significantly improve efficiency.

### Strengths
**Problems Tackled**

- Proposes a new approach for a problem that has perhaps not been tackled enough

- Considers harder problems than in the existing literature (the environments considered cover changes beyond function coefficients and extend to entirely different functional forms)

**Results**
- The proposed approach outperforms the other existing approaches used as baselines

- Proposes a new hypernetwork implementation that can significantly improve efficiency

### Weaknesses
 **Clarity**
The proposed approach is not presented clearly. The details of the various components are scattered in different parts of the paper and its appendix and sometimes only implicitly. The reader has to piece it out together himself and sometimes guess how certain components are designed and it is easy to misunderstand the proposed approach. Here are a few examples, comments, and suggestions:

- The two-phase process should be highlighted more explicitly than hidden in a few paragraphs. Adding structure with bold keywords, or lists, or bullet points could help. Same comment about the two main challenges faced, and then later how they are addressed. 

- The details of how the forecasting phase is performed should be made more explicit. Line 164 suggests that a numerical integrator is used for that part and Line 193 suggests instead that the forecasting part is done using neural networks. The end of Section 3.2.1 suggests that the numerical integrator might be replaced during training, and the end of Section 5.2 mentions that a numerical integrator is used for the invariant dynamics. This needs to be clarified further, by stating explicitly what the different contexts are and what is used for forecasting in each context. It is unclear if the neural network is directly predicting the next state or if it is predicting the derivative which is then used by the numerical integrator.

- The paragraph around lines ~134-143 and Table 1 are not clear enough. "defining environments as discrete interventions (Pearl, 2009) and model them as a categorical environment variable" needs to be explained in more details, and these keywords should be defined for readers that are not familiar with the cited literature. What does distribution represent in the table? Need more examples of different environments for "our environment" to better grasp how much variability there is in the dataset. Using colors in the table instead of underlining could also improve readability.

- It could be useful to have a higher-level version of the upper part of Figure 2 earlier in the paper to explain the two phases ion more details.

- The lower part of Figure 2 is unclear. Why only partial assignments? What process does each of the arrows represent? I don't understand the "flow" of that figure. Are the outputs of the hypernetwork exactly in this symbolic form, or is this after applying some form of symbolic regression that is not part of the proposed approach? In the same direction, the sentence around line 163, "Intuitively, taking Fig. 1a as an example, this phase aims at the reasoning of the function basis sin(θt), −ωt, ωt/|ωt| , and the coefficients α, ρ" is too imprecise. It is unclear what the output of the hypernetwork is. The quoted sentence and the figures seem to insinuate that a symbolic function form is learnt explicitly and then used as the differential equation to solve in the forecasting phase. However, later on, in section 5.6, symbolic regression using PySR is applied to the output of the hypernetwork, which shows that a symbolic function form was not learnt explicitly. This needs to be clarified, it should be written very explicitly what the output of the hypernetwork looks like and how it is taken into account in the forecasting phase.

- I would recommend adding more details about the new hypernetwork implementation in the main text instead of the appendix, given that it could be an important contribution of the paper based on the speedups observed. This also depends on whether other similarly or more efficient hypernetwork implementations have been proposed in other works and are not mentioned here (in which case they should)

- There are also numerous grammatical and spelling errors, especially in Section 3 and Appendix B (10+ in each of them)

- Limitations and Future Work should not be relegated to Appendix G and should appear in the main text



**Results**

- Aside from the pendulum, the symbolic regression explanations are quite off from the ground truth, suggesting a certain lack of generalization capability (although it should be noted that these examples are harder than those considered in previous literature)

### Questions
Questions and suggestions were outlined made in the Weaknesses section.

Overall, I do believe this paper tackles an important problem and makes some contribution towards solving that problem, but the clarity and presentation of the paper are not good enough. 

I would be happy to revise my review if the authors significantly improve the clarity and readability of the paper

### Soundness
3

### Presentation
1

### Contribution
3
