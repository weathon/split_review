# Partially Observed Trajectory Inference using Optimal Transport and a Dynamics Prior

- Decision: Accept
- Avg Score: 5.67
- Scores: 3, 6, 8

## Abstract
Trajectory inference seeks to recover the temporal dynamics of a population from snapshots of its (uncoupled) temporal marginals, i.e. where observed particles are \emph{not} tracked over time. Lavenant et al. \cite{lavenant2023mathematical} addressed this challenging problem under a stochastic differential equation (SDE) model with a gradient-driven drift in the observed space, introducing a minimum entropy estimator relative to the Wiener measure. Chizat 
 et al. \cite{chizat2022trajectory} then provided a practical grid-free mean-field Langevin (MFL) algorithm using Schr\"odinger bridges. Motivated by the overwhelming success of observable state space models in the traditional paired trajectory inference problem (e.g. target tracking), we extend the above framework to a class of latent SDEs in the form of \emph{observable state space models}.    
 In this setting, we use partial observations to infer trajectories in the latent space under a specified dynamics model (e.g. the constant velocity/acceleration models from target tracking). We introduce PO-MFL to solve this latent trajectory inference problem and provide theoretical guarantees by extending the results of \cite{lavenant2023mathematical} to the partially observed setting. We leverage the MFL framework of \cite{chizat2022meanfield}, yielding an algorithm based on entropic OT between dynamics-adjusted adjacent time marginals. 
 Experiments validate the robustness of our method and the exponential convergence of the MFL dynamics, and demonstrate significant outperformance over the latent-free method of \cite{chizat2022meanfield} in key scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a latent variable model for trajectory inference, i.e., inferring a time-indexed collection of particles. We assume a latent state vector $(X_t)$ follows some trajectory driven by an SDE, and project the state vector into the observation space via a function $g$, and the objective is to recover the latent trajectories that give rise to the observations. 

To infer the latent trajectories, we formulate a minimum entropy functional (an approximation of the KL-divergence with Gaussian kernel smoothing) that can be optimized by an entropy-regularized gradient flow that can be simulated via a McKean-Vlasov process, i.e., the PO-MFL algorithm. 

The paper evaluates PO-MFL empirically via toy examples and Wikipedia traffic data, showing improvements compared to the original MFL.

### Strengths
While I can't seem to understand part of the paper, I think the overall approach of applying latent variable models to trajectory inference is is a sound and novel approach. I think trajectory inference for latent variables are also a key open problem in this field, and this paper proposes an approach to solving this problem. I also think that the paper's main idea is technically sound for the parts I am able to understand. 

The empirical illustration looks convincing and showcases the validity of the algorithm. While I have some reservations about whether or not it is a fair comparison with MFL, I think the paper's approach of inferring latent trajectories + a push-forward function g is overall more preferable than trajectory inference in the observation space.

### Weaknesses
While I think the paper presents an interesting approach to trajectory inference, I find the paper's presentation overall unsatisfactory. The explanations are hard to follow, and the notations are perplexing. I think the lack of readability makes it unsuitable to grant an acceptance for the current version, and it makes it difficult to assess the contribution.

- The paper is hard to follow overall. While there is a "notations" section, new notations appear throughout the rest of the paper. Many notation can be inferred from context, but that seems to defeat the purpose of a notation section.  
- Some of the confusing notation include 2 different ways to denote convolving variables with a Gaussian density in eq. 4, e.g., both $\mathcal{N}_\sigma$ and $\hat{\rho}_i^{T, h}$. $\gamma$ is both a multiplicative constant in eq. 3 and part of the OT formulation in eq. 6. The use of $\gamma$ in two different contexts is particularly confusing, as it suggests a connection that is not explicitly made, and it forces the reader to constantly check the context to understand its meaning. The notation $\hat{\rho}_i^{T, h}$ is also not clearly defined, and it is not clear why it is necessary to introduce a new notation for Gaussian convolution when $\mathcal{N}_\sigma$ is already defined.
- Some of the theoretical explanations in the paper, such as $C_\Psi$-ensemble observability and the general assumptions on $\mathcal{X}$ and $\mathcal{Y}$ are mentioned in the paper, but they are not really included in the discussion. The paper mentions these concepts but does not explain their relevance or how they relate to the main results. The lack of discussion makes it difficult to understand the importance of these assumptions and whether they are critical for the validity of the proposed method. 
- There are a number of "filler" type of sentences about "recall that", "note that" which often are re-statements or clarifications. I think it is helpful to reformulate the explanation in a more cogent way. Perhaps it is a good idea to dwell on the most important concepts of the paper, and relegate some less relevant but still beneficial explanation to the appendix. The frequent use of these filler sentences interrupts the flow of the paper and makes it harder to follow the main line of reasoning. 
- Some notations seem unnecessarily complex. For example, I don't understand why the time variables need to be formulated as $t_T^T$. This notation is not intuitive and it is not clear why it is necessary to use a double index for the time variable. It makes the paper harder to read and understand.
- The paper makes many references to previous works in the abstract, which makes it look more like a background overview. I think the abstract needs to be restructured in a more self-contained fashion. The abstract should focus on the main contributions of the paper and not on the background. 
- PO-MFL seems to empirically outperform other trajectory inference methods, and latent variable models are ostensibly harder to infer. But this experimental setting (e.g., Figure 4) seems more beneficial, as the latent velocity variables are easier to infer. The experimental setup seems to be biased towards the proposed method, and it is not clear whether the performance gains are due to the method itself or to the specific experimental setup.

### Questions
- I don't understand precisely how optimal transport fits into the framework -- eq. 11 is a Wasserstein gradient flow w.r.t. a convexified functional in eq. 8. Is it possible to simplify the framework via Wasserstein gradient flow?
- The paper mentions an unknown potential function $\Psi$ in eq. 1, but does not mention outside the appendix afterwards. Could you explain if inferring $\Psi$ is left for future work, or if it is omitted somewhere in the later notations?
- I don't understand the explanation at the beginning of Section 3.4. Why do we need to increase the entropy by $\epsilon$ when $G + \tau H$ is already convex?

### Soundness
3

### Presentation
1

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
This work proposes methodology for sampling trajectories of a diffusion which is only partially (but repeatedly) observed at a finite number of time points. At each iteration, the proposed methodology uses optimal-transport ideas to construct a joint distribution over the states of the diffusion at observation times from their marginal distributions (the latter are approximated via samples/"particles"). At the end of each iteration, a mean-field Langevin algorithm is then used to optimise the particle locations.

### Strengths
1. **Clarity.** I believe that this work is overall fairly well written (though see some of the comments/questions below, especially with regards to the explanation of some of the experiments).

2. **Novelty/Originality.** The proposed methodology seems new. The main innovation is the extension of a previous approach to allow for a non-zero drift term $\Xi$. This seems fairly moderate, but IMHO sufficient given that it requires non-trivial extensions to the theoretical guarantees which the authors provide.

3. **Quality/Correctness.** This paper comes with a number of rigorously derived theoretical guarantees (though I did not have time to verify all details nor check the derivations in the appendix).

### Weaknesses
 **Main issues:**


1.  **Lack of comparison with simple Monte Carlo alternatives.** I believe the method needs to be compared against a simple Monte Carlo alternative like a particle filter (with backward sampling to obtain trajectories) or a simple MCMC method. The method is currently only compared against an alternative, denoted "MFL", which seems to be so heavily biased that it makes almost anything look good by comparison.



2.  **Seemingly high computational cost.** The actual computation time and total number of iterations used in the numerical experiments should be mentioned in the main text. The only mention I found is in Appendix F.1 where it says "[s]ynthetic experiments take a few minutes to run, and Wikipedia experiments take a few hours to run." However, the phrase "a few minutes" is too vague. Further, the synthetic experiments are fairly small (the dimension of $X_t$ seems to be between 2 and 4). I would expect that a simple Monte Carlo alternative (like those mentioned above) would run in mere seconds rather than minutes. The computational cost of the Sinkhorn algorithm, which is a key component of the proposed approach, is known to scale poorly with the number of particles, and this should be addressed in the experimental evaluation. A more detailed analysis of the runtime scaling with respect to the number of particles and the dimension of $X_t$ is needed to fully assess the practical applicability of the method.


3.  **Variance of target distribution seems poorly captured.** As shown in Figure 1c, and commented on in Lines 467--469, the *average* of the sampled velocities seems to match the ground truth. However, the variance seems to be heavily overestimated (or is this just a visual artifact of using scatter plots with different numbers of points?). Additionally, Figure 1a seems to indicate that the variance of the ground truth increases over time but this does not seem to be reflected in the trajectories produced by the proposed method shown in Figure 1b. The method's ability to accurately capture the temporal evolution of the variance is crucial for reliable trajectory estimation, and the current results suggest a potential limitation in this aspect.


4.  **Lack of clarity about the real-data experiment.** I find the "Wikipedia traffic data" experiment impossible to understand. In Line 511, the dynamics(?) $x_{t+1} = \theta_1 x_t + \theta_2 x_{t-6}$ are stated. But it is not clear to me how this discrete-time autoregression relates to the SDE fro (1)? That is, what are $\Xi$ and $\tau$ here? Furthermore, are the three websites modelled/estimated separately or somehow jointly (e.g., do the trajectories shown in Figure 5b represent a single website or all three)? The connection between the stated autoregressive model and the underlying SDE framework needs to be explicitly clarified. The experimental setup of the Wikipedia experiment is not sufficiently detailed to allow for reproducibility or proper interpretation of the results. The authors should provide a more precise description of how the data was preprocessed, how the model parameters were chosen, and how the results should be interpreted in the context of the proposed methodology.


**Minor issues:**

* In Line 32, it should be explained what "unpaired observations" means.

* The term "MFL" appears multiple times throughout the manuscript but sometimes refers to the minimisation algorithm (also used within the proposed methods) and sometimes to the algorithm used as a benchmark in the numerical experiments. I found this confusing, especially because it makes it difficult to find the reference for the benchmark algorithm.

* Figure 2: The tick labels on the 1st axis in the left panel are confusing. Later in the text it is explained that these the final 500 iterations rather than Iterations 1 to 500.

* All axes need to be labelled in all figures. And the 1st-axis labels in Figure 5a are all overlapping and thus unreadable.

* Figures should not appear in the text before they are referenced. This is particularly confusing with Figure 1 which appears on Page 2 but is only referenced/used on Page 9. But there are similar problems with Figures 2 and 3.

* The number of footnotes seems excessive. Many of these, e.g., Footnote 2 an 3, should be included in the text.

* Bibliography: Most entries in the bibliography are missing the journal/conference name. There are also many typos (e.g., missing capitalisation such as "wasserstein", "schroedinger", "brownian", etc).



**Typos:**

* L135: $H(\mu|\nu)$ is defined for probability measures $\mu$ and $\nu$ here but is later used with non-probability measures.

* L144: The last line in the "notation" paragraph seems incomplete since neither $g$ nor $\xi$ have been previously defined and it should probably be stated explicitly that $g_{\sharp\mu}$ denotes the pushforward measure.

* L231: "measurement" -> "measurements"

* Equation 4: Define the "*" operator.

* L251: What is $\hat{\mu}_i^{T, h}$?

* L253: "computationally more effective" -> "computationally more efficient"

* L280: Equation 7 is referenced before it appears in the text.

* L289: Shouldn't the first term in the cost function be $-\tau_i$ rather than $-\Delta t_i$?

* L335: Shouldn't "approximate (10)" be replaced by "approximate the first two terms in (10)"?

* L338: There seems to be a space missing at the end of the sentence.

* L362: What is "$\xi$" (i.e., without a superscript) here?

* L367: Use natbib's \citet rather than \citep

* Algorithm 1, Line 8: Is there a "hat" accent missing on $\mathbf{m}$ in the comment?

* Algorithm 1, Lines 8 and 10 (and in the "Require" line): Shouldn't this be "$T$" rather than "$t$"?


### Questions
1. What can you say about how this method scales with the dimension of $X_t$?

2. What do you do if $\Xi$ and $\tau$ are unknown?

3. Having a the same diffusion parameter $\tau$ for all components of $X_t$ (e.g., for both the evolution of the positions and of the velocities) seems very limiting. Is there any hope of relaxing this assumption?

4. I didn't understand the "crossing paths" experiment discussed in Lines 477--500 and Figure 4. Can you explain this more clearly?

5. What is the real-world significance of the "Wikipedia traffic data" experiment. In this case, all the traffic data has already been observed. What is the real-world utility of the estimated trajectories?

6. In the caption of Table 1, what does "MCMC" refer to here? I didn't see MCMC methods being mentioned anywhere else.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes an extension of existing methods for the trajectory inference problem, focusing on where states are partially observed only through "snapshots" at a given timepoint. These snapshots, for example, capture position but not velocity. They are also unlabelled, for example, you cannot know whether a particle at timepoint t_1 corresponds to a particle at timepoint t_2. The objective is to infer the trajectory distribution of the particles over time. 

The authors introduce the PO-MFL (Partially observed mean field Langevin) algorithm to address this challenging problem, developing a deep theoretical contribution that robustly explores their algorithm, including a weak consistency result (section 3.1) showing that their proposed objective function minimises to the true law of the SDE, under some assumptions and in the limit, in ideal conditions. As well as a convergence result (section 3.4), indicating that the PO-MFL algorithm’s approximation of the true trajectory distribution improves over time and eventually stabilises, showing the robustness of PO-MFL.

Finally, the paper grounds their theory in robust experiments - for example, showing empirically that the convergence from Theorem 3.4 holds in Figure 2. Additional experiments show the usefulness of the method, testing robustness across various settings on synthetic and real-world data.

I congratulate the authors on a well constructed paper.

### Strengths
1. The paper introduces a well developed framework, extending mean-field Langevin dynamics with latent dynamics modelling for partially observed trajectory inference, making substantial advancements in the field. 

2. The paper is theoretically robust - providing a wealth of theory that seeks to capture the applicability and performance of the method, such as the consistency and convergence results.

3. The experiments are varied on synthetic and real-world data, provide insights into the method, and empirically back up theoretical claims.

4. The paper is extremely well written, providing a good background into the subject and gradually introducing concepts to build up to a final goal.

5. The work is framed well within the global context of the problem, highlighting relevant works and providing comparisons and gaps in the literature when needed. Applications of the problem are presented in many cases, showcasing the general applicability of the need for solving the Partially Observed Trajectory Inference problem.

### Weaknesses
1. The computational complexity of the algorithm is $O(NTm^2)$, which is not explored further than it is stated, nor is it compared against other methods in the experiments section. Some details on real-world runtime could be useful, due to its (presumably) large scaling cost. It would be beneficial to understand the practical implications of this complexity, such as how the runtime scales with increasing numbers of particles (N), time steps (T), and the dimensionality of the latent space (m). A more thorough analysis of the computational bottlenecks would also be valuable, identifying which parts of the algorithm contribute most to the overall runtime.

2. Experiments show comparisons to regular MFL, which is not suited for the unobserved case, and therefore there are no comparisons to methods that are suited for this domain. However, I am unfamiliar with the literature, so not sure if there are other methods that can be used in this case. The lack of comparison to relevant baselines makes it difficult to assess the true performance of PO-MFL in the context of partially observed trajectory inference. It is unclear if the performance gains observed against MFL are due to the method's ability to handle partial observations, or if they are simply a result of the increased complexity of the model.

3. Whilst there is some discussion on the limitation towards model misspecification in the summary section, limitations of the methodology are not discussed in great detail. The paper would benefit from a more in-depth discussion of the limitations of the proposed method. For example, how sensitive is PO-MFL to the choice of hyperparameters, and how does the performance degrade when the assumptions of the model are violated? A more thorough analysis of the limitations would provide a more balanced perspective on the applicability of the method.

### Questions
1. How does the computational complexity scale against other methods such as regular MFL?

2. It would improve the strength of the experiments to compare to other methods. Would comparing to something like rejection sampling based methods work? Even with a high computational expense, it could be worth it to compare to as a baseline?

3. Are there any scenarios (within the Partially Observed Trajectory Inference setting) in which PO-MFL will break down? What restrictions does the method have, if you know of any? Are there any limiting factors?

4. Are there any limitations or concerns related to relying on Assumption 2.1? Does the restriction for $\Xi$ to be known, divergence-free and Lipschitz continuous restrict the applicability to some real world systems that have more complex dynamics?

### Soundness
4

### Presentation
3

### Contribution
4
