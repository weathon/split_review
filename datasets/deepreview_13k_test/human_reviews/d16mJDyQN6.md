# Identifying latent state transitions in non-linear dynamical systems

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
This work aims to improve generalization and interpretability of dynamical systems by recovering the underlying lower-dimensional latent states and their time evolutions.		
		Previous work on disentangled representation learning within the realm of dynamical systems focused on the latent states, possibly with linear transition approximations. As such, they cannot identify nonlinear transition dynamics, and hence fail to reliably predict complex future behavior.
		Inspired by the advances in nonlinear \ica, we propose a state-space modeling framework in which we can identify not just the latent states but also the unknown transition function that maps the past states to the present.
		We introduce a practical algorithm based on variational auto-encoders and empirically demonstrate in realistic synthetic settings that we can (i) recover latent state dynamics with high accuracy, (ii) correspondingly achieve high future prediction accuracy, and (iii) adapt fast to new environments.\looseness-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a structure with a theoretical foundation for identifying latent dynamics under certain assumptions. The implementation is standard. The experiments' results show various advantages in different scenarios, even when the assumptions are violated.

### Strengths
In Table 3, the author(s) claim, "Our approach is the first to predict future states of a dynamical system by utilizing a transition function that identifies the underlying, true dynamics." As far as I know, many approaches can do similar things without a theoretical foundation for the identification.

### Weaknesses
Perhaps a theoretical or practical time complexity analysis would be more appropriate.

### Questions
1. Does the identifiability still exist when I have any external input, like the control input in the state-space model?
2. What's the exact definition of $s_t$, and what's the motivation for incorporating $s_t$ into the model?
3. (minor) For Table 1, do you use any stats test to confirm your approach is the best?

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
4

### Summary
In this paper, the authors introduce a theory under which one can identify both the latent states as well as the latent dynamics from observational data (up to permutations and invertible transformations). Next, the authors introduce a practical algorithm, based on sequential variational autoencoders, for learning identifiable state-space models. Experiments provide empirical evidence that proposed approach can correctly recover the latent states and the latent dynamics.

### Strengths
My favorite thing about this paper is the simplicity of the proposed approach. By just simply changing the form of the latent dynamics model, i.e., as opposed to additive noise, which is the standard, the noise is an input to the transition function, and assuming a dimension-dependent dynamics function, one can recover the states and dynamics (under some assumptions). I think this is a massive break through for people who learn state-space models.

### Weaknesses
While the paper is strong, there a couple of minor weaknesses. Firstly, is that assumption 2 doesn't seem to align with one of the motivating examples in the introduction, which is model-based RL. Specifically, assumption 2 does not allow for process noise/control values that are temporally correlated. But in model-based RL, the process noise *is* temporally correlated because the control value chosen at time $t$ depends on the previous state of the system. I found this contrast jarring.

Second, the experiments section is great but I think it would be great to have a seqVAE baseline that is more similar to proposed generative model. In the experiments section, the baseline seqVAE is the KalmanVAE, which is a hierarchical SSM. While the proposed approach outperforms KalmanVAE, its not clear whether it outperforms it is truly better or if there is a model mismatch between the true generative model and the one used by KalmanVAE. I think training a seqVAE using the generative model as described in section 2.1 would strengthen the results. 

Also, section 4.4 doesn't make sense at a first glance. If I had the true latents then training a model in a supervised fashion should be better than learning both in an unsupervised fashion. When doing the comparison, were the number of parameters matched? I ask because if your latent state has $K$ dimensions then one would need $K$ neural networks, so it might be the case that the proposed approach is working just because the model has more expressive power.

Lastly, I think the proofs in the appendix could benefit with a little more hand-holding to follow along!

### Questions
1. Why was such a small prediction horizon used for testing? I found this odd for the synthetic data.
2. I see that training sequences used to train the model are relatively short. Is there a reason why?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work deals with the general problem of identifying (i.e. inferring) the nonlinear transition function underlying the dynamics of complex dynamical systems. The authors extend recent theoretical work on identifiability of latent states in dynamical systems to the identifiability of their transition function. Furthermore, the authors provide a neural-based inference model that implements the key aspects of the theory and relies on neural variational inference. The authors then test their methodology on three settings: (i) a synthetic dataset that mirrors their generative model; (ii) a cartpole simulation which is represented as a video signal; and (iii) three sets of experimental motion capture data. The results demonstrate the proposed models outperform the baselines, not only on the identification of the latent variables, but also on forecasting tasks.

### Strengths
- This work tackles a key problem of (nonlinear) dynamical system modelling, namely the identifiability of the transition function underlying the dynamics;
- The authors naturally extend the identifiability theory from previous works to the identification of the nonlinear transition function of the hidden process. Their proofs are well written and easy to follow;
- The authors demonstrate that their model implementation of their theory outperforms different baselines, in different settings. The results are very convincing (see however the questions below).

### Weaknesses
In my view, the main weaknesses of the paper have to do with its presentation. The three most pressing points are:

1. There is somewhat of a disconnect between the theory section and the practical implementations, which I think could easily be improved. Especially when it comes to the experimental section. Questions 2 – 8 below point to concepts or ideas which are not clearly explained, that could be explained better or that are simply absent. In particular, it is not clear to me how the auxiliary ($\mathbf{u}$) and noise ($\mathbf{s}$) variables are used (or represented) in the experiments. To improve the readability of the paper, I'd suggest the authors explicitly describe the role of $\mathbf{u}$ and $\mathbf{s}$ in each experiment.

2. The target datasets could be explained and motivated better. It is not clear from a first reading why these datasets are relevant in the context of the model (see e.g. questions 3 and 4 below). This point is clearly related to point 1 above. I believe that if the authors explain what $\mathbf{u}$ and $\mathbf{s}$ represent in each dataset, it will become clearer why those target datasets are interesting.
 
3. The paper builds on a large collection of previous works which deal with identifiability and go all the way back to independent component analysis (ICA). The authors assumed the reader is versed in the development of ICA, from its linear to its nonlinear versions, and simply present e.g. the augmented dynamics (line 126) and the auxiliary variable (line 130), or the identifiability assumption, without any further explanations and context. There is however some nice physical interpretation underlying e.g. the conditional independence assumption of the noise process given the auxiliary variable, which can be traced back to Packard et al. [1980], and that is also nicely explained (albeit in a different sense) by e.g. Hyvarinen et al. [2019]. Even in the introduction, lines 41-49, the authors could already mention that their work builds on classical ideas of ICA. In short, I think the authors could better exploit the history of nonlinear ICA and its application to dynamical systems to better motivate their proposal. 

Note:  *I will happily increase my score once the authors answer the questions below* and explain how they will try to incorporate this information back into the paper.

**Other comments and/or typos** 
- in line 88 the authors write *the generative function*. Do the authors mean the function $\mathbf{g}$? I’d suggest, for the sake of clarity, to either stick to the “instantaneous mapping” label used later in line 112, or better use the more standard “emission model” label.  
- in your KL loss term (lines 290 inside Algorithm 1) you write that the posterior over the noise $\mathbf{s}$ is conditioned on $\mathbf{u}$. This is a typo, isn’t it?

**References**
- Packard et al. [1980]: Geometry from a time series
- Hyvarinen et al. [2019]: Nonlinear ICA Using Auxiliary Variables and Generalized Contrastive Learning

### Questions
1. Is there a reason why the noise posterior $q(\mathbf{s}\_{t} | \mathbf{\tilde x}, \mathbf{z}\_{t-1} )$ explicitly depends on $\mathbf{z}\_{t-1}$? Does this follow from your theory? If so, how?

2. In line 140 the authors write “setting $\mathbf{u}$ to an *observed regime index*...” What do you mean by observed regime index? Do you mean the time index $t$ of the observation $\mathbf{x}(t)$? Or do you mean the observation value $\mathbf{x}(t)$ itself?

3. How is $\mathbf{u}$ used in your practical implementation? Put another way, do you set $\mathbf{u}$ to be an *observed regime index* or $\mathbf{s}\_{t-1}$? Or is it only implicitly define via the prior $p(\mathbf{s}\_t| \mathbf{u})$? In Figure 6, $\mathbf{u}$ is shown as an input to the prior noise model, which is used for forecasting. Can you please explain how you choose $\mathbf{u}$ in each experiment?

4. What does $\mathbf{s}$ represent in the synthetic experiments? Similarly, what does it represent in the Cartpole dataset?

5. In Table 1, why is $\text{MCC}[\mathbf{z}] > \text{MCC}[\mathbf{s}]$ for all models? Is the noise variable harder to infer in practice? 

6. How do you interpret the inferred $\mathbf{s}$ in the MOCAP datasets? 

7. In the synthetic dataset description of the appendix (lines 1235, 1236) the authors write: the number of environments is R = 20. What do these environments represent?

8. Are the sufficient variability assumptions (A3, A4) satisfied in the synthetic and Cartpole experiments? If so, can you please explain why?

9. Why are the simulated trajectories (of the synthetic dataset) so short? Meaning: what is the motivation behind such a setting?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a framework for identifying the unknown transition function in latent dynamical systems. The authors emphasize that previous research focused on identifying latent states, and lack the ability to accurately predict future states, particularly in complex nonlinear systems.

The authors establish the theoretical identifiability of both the latent states and the transition function. They leverage the assumption of "sufficient variability," meaning that the latent noise and states exhibit enough variation across different environments to disentangle the underlying dynamics. The framework also relies on the assumption that the augmented transition function is bijective. 

The framework was tested across a range of scenarios, including synthetic datasets, a simulated cartpole environment, and real-world Mocap data. The results demonstrate that the model effectively recovers the true underlying dynamics, and is accurate in predicting future states.

After the discussion, the authors have addressed my concerns. I have decided to raise the score.

### Strengths
The identifiability was theoretically defined and justified with given assumptions.

The proposed framework was empirically evaluated and compared with existing methods across synthetic and real-world data.

### Weaknesses
The claimed contribution "the first framework that allows for the identification of the unknown transition function alongside latent states and the generative function" seems overstated. There are existing methods to identify latent states, transition and generative functions together, e.g. [Sussillo16, Schimel21, Hess23, Zhao23]. 

The proposed framework is not demonstrated as general as claimed like "... improves generalization and interpretability of dynamical systems...". The authors focused on typical RL and robotics scenario. There exist dynamical systems in other fields do not satisfy those assumptions or are in completely different regime. This could disadvantage the compared methods with weaker assumptions (e.g. NODE).
Though the authors used Mocap dataset to showcase then it violates the identifiability assumptions, the system itself is still of RL and robotics scenario. It is totally valid to narrow down problems to solve them better. However, the statements and claims should be more specific.

### Questions
Does the proposed framework requires the dimensionality of latent space and noise to be known?
If not, what would be the procedure of estimation?

Does the proposed framework allow for sparse noise?

### Soundness
3

### Presentation
3

### Contribution
2
