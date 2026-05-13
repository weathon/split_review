# Deep Bayesian Filter for Bayes-Faithful Data Assimilation

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
State estimation for nonlinear state space models (SSMs) is a challenging task. Existing assimilation methodologies predominantly assume Gaussian posteriors on physical space, where true posteriors become inevitably non-Gaussian. We propose Deep Bayesian Filtering (DBF) for data assimilation on nonlinear SSMs. DBF constructs new latent variables $h_t$ in addition to the original physical variables $z_t$ and assimilates observations $o_t$. By (i) constraining the state transition on the new latent space to be linear and (ii) learning a Gaussian inverse observation operator $r(h_t|o_t)$, posteriors remain Gaussian. Notably, the structured design of test distributions enables an analytical formula for the recursive computation, eliminating the accumulation of Monte Carlo sampling errors across time steps. DBF trains the Gaussian inverse observation operators $r(h_t|o_t)$ and other latent SSM parameters (e.g., dynamics matrix) by maximizing the evidence lower bound. Experiments demonstrate that DBF outperforms model-based approaches and latent assimilation methods in tasks where the true posterior distribution on physical space is significantly non-Gaussian.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper deals with data assimilation in general state-space models (SSM) and proposes a new method for approximating the flow of marginal state posteriors, also known as filter distributions. In the case of a linear Gaussian latent state process (but a general emission density), by formulating the filter recursion in terms of a so-called inverse observation operator (IOO)—which models the law of the current state given the corresponding observation—and approximating it by a Gaussian distribution parameterized by a neural network, Gaussianity is preserved through the filter recursion, allowing the generation of a sequence of approximate Gaussian filter distributions. The IOO is trained along with the unknown model parameters using variational inference, and in the case of linear dynamics this can be done without supervision. When the state process is nonlinear, the authors introduce another level of auxiliary latent states with linear Gaussian dynamics, generating the original latent state process through an auxiliary emission density. In this case, training cannot be performed without supervision, but requires access to training data consisting of a known history of both latent states and observations. The authors illustrate their method numerically with three examples, one where the goal is to identify images from the MINST dataset that move with linear dynamics and two where the goal is to estimate parameters and states in models with non-linear dynamics describing a double pendulum and a Lorenz system.

### Strengths
The idea of learning a Gaussian, NN-parameterized IOO to obtain Gaussian approximations of the filter distributions in the case of linear state dynamics is, to my knowledge, novel. Although I am more doubtful about the relevance of the method for models with nonlinear dynamics, at least in its current form, the simplicity of the proposed method appeals to me. Furthermore, the method's performance, at least in the linear example, is promising, although it is unclear how it generalizes to other models (as the assumed Gaussianity of the IOO introduces a bias that is not easily controlled; see my comment below). The article is fairly clearly written and the methodology is not too difficult to understand. So sum up, the proposed method should have some relevance, at least in the case where the latent-state dynamics is linear.

### Weaknesses
As far as I am concerned, the proposed methodology has three major shortcomings, which makes the paper boardeline.

(i) It seems crucial to use a Gaussian IOO, which is likely to lead to poor approximations for some models, e.g. in cases where the distribution of the current state is multimodal given the corresponding observation. Moreover, the bias implied by the assumed Gaussianity seems very difficult to control. Specifically, the method does not account for potential skewness or heavy tails in the true conditional distribution of the state given the observation, which could be crucial in many real-world applications. The use of a Gaussian IOO also limits the ability of the method to capture complex dependencies between the state and the observation, potentially leading to inaccurate posterior approximations, especially when the observation operator is highly nonlinear or non-invertible.

(ii) In the case of nonlinear dynamics, the method requires that training is done in a supervised manner, i.e. with access to the observed history of the latent state process, which is only possible in a limited number of contexts. However, in many cases, these states have no direct physical counterparts, but are only a phenomenological tool to capture patterns and features in the observed data (think for example of the unobserved volatility driving the dynamics of asset prices in a stochastic volatility model), preventing the method from being used. This significantly limits the applicability of the methodology. The requirement of having access to the true latent states during training is a major limitation, as it restricts the method to scenarios where the ground truth is known, which is rarely the case in real-world data assimilation problems.

(iii) To deal with the nonlinear case, the authors introduce an auxiliary state process (the h's), and a Gaussian emission density that generates the original states (the z's) given the auxiliary ones. My concern is that this construction strips the original state process of the Markov property (in the same way as the observations of an SSM are not Markov, even if the underlying states are so), leading to a model with a significantly different dynamics than the original one. Together with point (ii), this leads me to doubt even more the relevance of the method for the nonlinear case. The introduction of the auxiliary states and the associated emission density introduces an additional layer of approximation, which may not accurately capture the true underlying dynamics of the original state process. This can lead to biased estimates and reduced performance, particularly when the relationship between the auxiliary and original states is complex or poorly modeled.

### Questions
(1) In the non-linear case, introducing auxiliary states, which fundamentally change the model and the methodology (e.g. by requiring supervised learning), seems to me a solution that is too ad hoc. Are there other ways in which nonlinearities in state dynamics could be addressed? 

 (2) A similar question concerns the Gaussianity of the IOO. Is there any way in which a slightly more flexible distribution class could be used? 

(2) If I have understood correctly, the numerical part evaluates the different filtering algorithms based on the RMSE with respect to the _true_ states? Since the goal of these algorithms is optimal filtering, i.e. to determine the posterior distributions of the states given the data and not the true, exact states, such a comparison makes it difficult, in my opinion, to claim that one algorithm is better than another. Would it not be better to compare the methods in terms of RMSE with respect to reference values calculated on the basis of a consistent algorithm, e.g. the particle filter with a massively large number (say, half a million) of particles.

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
This paper looks at state inference in non-linear state space models, that is, the problem of estimating latent "physical" variables z_t given observations o_t. The posterior of z_t given o_t is often non-Gaussian in models with a practical use, e.g., models of weather dynamics. This poses a challenge, and solutions have taken a path along using Gaussian approximations to the posterior or computationally intensive methods such as Sequential Monte Carlo. A key idea that the paper relies on is the introduction of additional latent variables (state expansion) h_t variables for which Gaussian inference is possible; these variables are later mapped to the original state variables and marginalized. In this sense, the method acts like a dynamic VAE but without the use of Monte Carlo approximations. Essentially, the assumption that the original physical variable dynamics can be linear in a sufficiently high-dimensional space when the mapping to that space is chosen correctly is taken. Two proposed training strategies are given, on the basis of a standard ELBO objective. Some standard examples with a Lorenz model and MNIST are presented to illustrate the method and good performance is shown.

### Strengths
Designing generic-purpose VAE for modeling time series is and will remain an important problem. The authors use nice illustrations to make their point. The use of the filter as opposed to the smoother is noted and that fact that it seems to be (more than) sufficient.

### Weaknesses
No idea of the computation time for the proposed method is given. Presumably, it should be faster? What if pretraining is taken into account? It is also unclear to me how to choose the dimensionality of the new state space h: is it of a comparable size to z_t or must it be much bigger? As the authors say, they need to know values of at least z_t. It is also not clear how sensitive the method is to the choice of the initial mapping from z_t to h_t. If the initial mapping is poor, will the method still converge to a good solution? Furthermore, the paper does not discuss the potential for overfitting, especially given the increased dimensionality of the latent space. How does the method perform with limited training data, and what strategies are used to mitigate overfitting?

### Questions
Can the method be used with approximate, even crude samples of z_t obtained by another method? Would it still add value there?

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
3

### Summary
The paper proposes a variational inference approach “DBF” to data assimilation, i.e. the task of obtaining the posterior over an SSM state $z_t$ given observations $o_{1:t}$. In contrast to the linear Kalman filter, DBF supports non-linear observation models, as well as non-linear SSMs. In contrast to related dynamical VAEs (DVAEs), DBF does not rely on RNNs and can be trained more easily (less training instabilities).

DBF assumes a latent state $h_t$ that evolves linearly, with a Gaussian variational distribution for the approximate posterior $q(h_t)$, ensuring that the approximate posterior remains Gaussian with analytic updates under new observations. When the true SSM dynamics are linear, $h=z$ and only the (nonlinear) mapping from observation $o_t$ to latent state $h_t$ is learned.

When true SSM dynamics are non-linear, then $h$ is a latent state with higher dimensionality than $z$, but linear dynamics $h_{t+1}=A h_t$; DBF learns these latent dynamics $A$ as well as a latent emission model from the linear state $h_t$ to the actual SSM state $z_t$ from pairs $(z_t, o_t)$ of samples of SSM state $z_t$ and corresponding observation $o_t$.

The form of the variational approximation matches the Markov properties of the underlying SSM, hence termed “Bayes-faithful”.

The paper compares DBF to classical data assimilation algorithms (e.g. ensemble Kalman filter, particle filters) and DVAE variants in three settings (1. linear dynamics on 8-dimensional state, nonlinear observation with 784 dimensions; 2. nonlinear dynamics on 4-dimensional state, nonlinear mixed observation with 2 dimensions; 3. nonlinear dynamics on 40-dimensional state, nonlinear point-wise observation).

Amongst all compared methods, DBF consistently performs best in most settings (the one exception being when the state is directly observed with low noise, thus true posteriors are almost Gaussian and ensemble Kalman methods perform best).

### Strengths
Combining a neural network model to learn nonlinearities in observation and state whilst assuming an underlying _latent_ state with linear dynamics seems original (I am not very familiar with the literature). This fills a gap between hard-to-train DVAEs, Kalman filter approaches that struggle with non-Gaussianity, and particle filters that do not scale to high dimensions. If this holds up in larger-scale experiments, it will be a significant contribution to data assimilation in applications such as weather models.

The paper clearly states the approach’s limitation to require pairs of samples and observations.

In the experiments, a wide range of different methods are included as baselines. The supplementary material provides a high level of detail on experiment settings for DBF itself (though not on the baselines).

### Weaknesses
The main weakness of this paper is that the empirical evaluation insufficiently supports the claims made about the proposed DBF.

While DBF’s assumed Gaussianity and linearity in latent space leads to analytic solutions, this can be considered to do closed-form inference in an _approximate_ model. As noted in the paper, given a sufficient number of particles, a particle filter would be able to represent the true posterior. However, the paper does not directly analyse the loss in accuracy due to the approximations made in DBF’s variational inference approach. While it does compare to particle filters, the paper only considers a single, fixed number of particles, and simply states that it is not sufficient. The evaluation that would be needed here is to compare the accuracy–compute trade-off. For particle filter, how do accuracy and resource needs scale with number of particles, and correspondingly, for DBF, how do accuracy and resource needs scale with the number of latent dimensions? Ideally, for a range of dimensions of the actual SSM.

While the paper comes with code for the DBF implementation in the supplementary material, the main text itself is short on detail of the method. For example, the ELBO training objectives are simply given, without explicit derivation.

While ‘Strategy 1’ is introduced to train solely with samples of $z_t$, not requiring pairing with observations, this is not actually included in the empirical evaluation.

### Questions
1. Is your approach identifiable? I.e., is there a unique latent (linear dynamics) state trajectory corresponding to a given physical trajectory? If not, what effect does the nonidentifiability have?

2. Can DBF represent multimodal posteriors?

3. line 273: “computations for covariance matrices become challenging in high-dimensional spaces” – can you explain why these are not needed in DBF?

4. One of your key motivations seems to be that particle filters don’t scale to high dimensions, and DBF would scale better to high dimensions. But then you also need to have a significantly larger latent dimension than the actual state space to capture the nonlinear state transitions through the linear embedding: does it still reduce computational cost overall?

5. Also, how do the _state_ dimensions vs the _observation_ dimensions affect the performance of DBF vs particle filters?

6. You mention Frerix et al. (2021), where the Inverse Observation Operator is also learned – could you have included their approach in the empirical comparison?

7. How did you set up & run the baselines – can you link to which implementation you used?

8. Baseline methods could not handle the amount of training data used for DBF. To what extent is better performance due to being able to ingest more data, i.e. how would DBF have performed at the same amount of training data as baselines?

9. line 353: “We define success as …” seems rather arbitrary, and this might bias results (surprisingly related: “Are Emergent Abilities of Large Language Models a Mirage?” by Schaeffer et al., NeurIPS 2023), what are the RMSE results themselves?

10. line 365: can you explain how learning system parameters sets DBF apart from traditional approaches? I am not intimately familiar with the field but surely there are other approaches that learn system parameters.

11. I would have liked to see some sample trajectories vs inferred of the different methods.

12. line 480–485: could you quantify the (non)Gaussianity?

13. I would have liked to see an ablation study; for example, how does the choice of latent dimension affect the accuracy and compute requirements of your approach?

## Clarity questions

14. line 90: What do you mean by “regression methods” here? In general, regression can be probabilistic as well, thus quantifying uncertainty and not only providing point estimates.

15. p.3, Eq. (1): $\mu_t$ shows up in the last term on the right-hand side; is this a mistake? What would be the correct equation?

16. line 145: what do you mean by “virtual prior”, can you explain this in more detail?

17. Eq. (6): what is the KL term of the first element in the sum ($t=1$), where there are no previous observations?

18. Would you call DBF part of the DVAE family or not? In line 224 you say “DVAEs are closely related” (implying no), in line 255 you write “apart from other DVAEs” (implying yes).

19. line 265: “LS4 replaces recurrence with convolutions, forgoing a recursive approach” - does this matter?

20. $\sigma$ in line 339 vs $\sigma_{sys}$ (NB- should be $\sigma_\text{sys}$) in line 346: I don’t understand the distinction, can you explain?

21. line 348: How can the input dimensionality exceed the GPU memory – should this not also depend on sequence length, batch size, etc.?
(NB- it was unclear from the main text where the $44 \times 44$ came from, only explicitly mentioned in supplementary. It is especially confusing as in line 359 you now discuss dimensionality of digits themselves, should this not be irrelevant?)

22. Fig. 2 (b): what are the iterations – training steps of NN ?

23. Fig. 3 (b): is this RMSE of $\omega$ alone (averaged over both velocities, see below)?

24. Table 1 and line 420, “RMSE between physical variables”: RMSE is given for $\theta$ and $\omega$ separately, but there are two of each: is this the average over the two angles / velocities?

25. line 422, excluding failed initial conditions: what is the fraction of initial conditions that failed?

26. line 426: should this be time steps (of dynamics, as opposed to training steps of model)?

27. lines 483, 485: what do you mean by “prior $q(z_t | o_{1:t-1})$” vs “prior $p(z_{t+1} | o_{1:t})$”? Are they the same (except for the shift by 1)? Why $p$ vs $q$?

## Further points for improving clarity

You refer to the “test distribution” $q(z_t)$; in variational inference, this would more commonly be referred to as ‘approximate posterior’ or ‘variational distribution’ – mentioning this equivalence explicitly would make the paper a bit more accessible.

line 62, “assuming Gaussianity”: also mention explicitly, already in the introduction, the assumption of linear dynamics for the latent variables $h$.

line 156: “LGSS” is used but not introduced what it stands for.

line 288: citations for Lorenc and Frerix should be in parentheses.

line 334, “bouncing off frame edges”: at first reading I was quite confused how this clearly non-linear behaviour would match up with underlying _linear_ dynamics; it became clear from reading the supplementary, but would be helpful to mention here already that this nonlinearity is part of the _observation_ model, not the state.

Fig. 4: “for one of data” sounds a bit odd

### Soundness
2

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
The paper presents Deep Bayesian Filtering (DBF), a method for data assimilation within nonlinear state space models (SSMs). It addresses the prevalent challenge of non-Gaussian posterior distributions encountered in many scientific applications. By incorporating new latent variables, DBF ensures Gaussianity in the latent space, facilitating linear transitions and inverse Gaussian observation operators. This approach claims that one of the advantages is to avoid errors associated with successive Monte Carlo sampling, as seen in DVAEs.

### Strengths
The paper is well-structured, making it easy to follow the ideas presented. The proposed method can be considered to be novel and could be particularly beneficial for certain generic high-dimensional dynamical systems, especially those that can offer underlying latent states for training.

### Weaknesses
The primary limitation, in my view, is that the model necessitates extensive training data, including the underlying system's latent states (nonlinear dynamics), to effectively learn the IOO. This requirement could render DBF less practical for real-time applications or in domains where data availability is limited, making model-based methods potentially more viable. Additional issues and questions are discussed in the Questions part.



### Questions
1. A discussion (or even a comparison) between the normalizing Kalman filter (NKF) and also the model mentioned in the DVAE paper, Kalman Variational Autoencoders (KVAEs), seems necessary, as in these two models, the generative structure is the same as the one shown in Panel (b), Figure 1. 

     - de Bézenac E, Rangapuram SS, Benidis K, et al. *Normalizing Kalman Filters for Multivariate Time Series Analysis*. *NeurIPS*, 2020;33:2995-3007.

2. The loss functions in Equations 6 and 7 still require Monte Carlo sampling if $p(o_t | h_t) $ is non-Gaussian. While DVAEs must sample the latent state trajectory due to the variational distribution is indeed model the smoothing distribution, the benefit of “Bayes-faithful” data assimilation highlighted here is not entirely clear. If Monte Carlo sampling is still required at each step, and if the neural network is shared and amortized over each time step $t$ (which is the same as in DVAEs), what is the specific advantage of this “Bayes-faithful” property? Are there empirical results demonstrating the practical benefit of this property?

3. Follow the question 2, the paper claims to present the first VAE-based model for time-series data that maintains a posterior structure faithful to the Markov property in SSMs. However, recent work on Auto-EnKF models also employs filtering distributions to construct the model evidence or ELBO. For example, Equation (32) in Lin et al. (2024), shares a similar loss function structure to Equation (6) in this paper. Including a discussion or comparison of these models would enhance the comprehensiveness of the proposed method's positioning. 

     - Chen Y, Sanz-Alonso D, Willett R. "Autodifferentiable Ensemble Kalman Filters," *SIAM Journal on Mathematics of Data Science*, 2022; 4(2):801-33.

     - Chen Y, Sanz-Alonso D, Willett R. "Reduced-order Autodifferentiable Ensemble Kalman Filters," *Inverse Problems*, 2023; 39(12):124001.

     - Lin Z, Sun Y, Yin F, Thiéry AH. "Ensemble Kalman Filtering Meets Gaussian Process SSM for Non-Mean-Field and Online Inference," *IEEE Transactions on Signal Processing*, 2024 Aug 22.



4. Other questions:

 - Adding derivations for Equations (1, 2, 4, and 5) in the Appendix would improve clarity.

 - Could the authors discuss potential applications for the proposed method? 

 -  In Section 3.1, the authors mention that “DVAEs are not comparable as they need to undergo supervised training,” which may need clarification. If I’m not mistaken, DVAEs typically require only observation data and do not rely on model knowledge or latent state data. Could you clarify why DVAE training is interpreted as supervised in this context?

 - Given the low latent dimension and the known model structure, it seems model-based methods (e.g., EnKF, PF) should perform reasonably well. Could you explain why DBF and other data-driven methods outperform these model-based approaches in Table 1?

### Soundness
2

### Presentation
2

### Contribution
2
