# TANGO: Time-Reversal Latent GraphODE for Multi-Agent Dynamical Systems

- Decision: Reject
- Scores: 3, 5, 5, 8

## Abstract
Learning complex multi-agent system dynamics from data is crucial across many domains, such as in physical simulations and material modeling.%interactions, etc.  
Extended from purely data-driven approaches, %existing data-driven\ZH{should we here call "physics-informed approach? as we later refer LG-ODE as purely data-driven approach.} 
existing physics-informed approaches such as Hamiltonian Neural Network strictly follow energy conservation law to introduce inductive bias, making their learning more sample efficiently. 
However, many real-world systems do not strictly conserve energy, such as spring systems with frictions. %In these non-isolated systems, the total energy change is usually %over time are usually within a reasonable range instead of energy explosion or vanishing sharply. 
Recognizing this, we turn our attention to a broader physical principle: \textit{Time-Reversal Symmetry}, which depicts that the dynamics of a system shall remain invariant when traversed back over time. It still helps to preserve energies for conservative systems and in the meanwhile, serves as a strong inductive bias for non-conservative, reversible systems.
To inject such inductive bias, in this paper, we propose a simple-yet-effective self-supervised regularization term as a soft constraint that aligns the forward and backward trajectories predicted by a continuous graph neural network-based ordinary differential equation (GraphODE). 
It effectively imposes time-reversal symmetry to enable more accurate model predictions across a wider range of dynamical systems under classical mechanics. 
In addition, we further provide theoretical analysis to show that our regularization %generally helps learn system dynamics more accurately from the numerical aspect via 
essentially minimizes higher-order Taylor expansion terms during the ODE integration steps, which enables our model to be more noise-tolerant and even applicable to irreversible systems.  Experimental results on a variety of physical systems demonstrate the effectiveness of our proposed method. Particularly, it achieves an MSE improvement of 11.}}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work contributes to Physically Informed NNs for the simulation of multibody/multiagent physical systems by introducing a loss regularization term that encourages reversible continuous-time trajectories in the neural feature space. The paper also provides a result showing that the regularized loss entails the minimization of higher order Taylor expansion terms in ODE integration.

### Strengths
The paper puts forward an interesting motivation when it claims that engaging with Hamiltonian-type neural models might pose too stringent requirements, both on energy preservation as well as on the learning model. The idea of focusing on symmetry/reversibility properties rather than on strict energy preservation requirements is interesting. Even more so if this can be coupled with an approach that is fairly general and computationally efficient to achieve (as it seems reasonable to assume with the proposed approach). The empirical results seems to confirm the claim (though with the limitation described in the weaknesses below).

### Weaknesses
W1) As highlighted in the “Strengths” part, the motivation of the work is compelling and the idea of addressing reversibility through a simple regularization term is interesting. Unfortunately these are not novel contributions of this paper. Rather they are adapted from Huh et al, NeurIPS 2020, essentially adding the graph NN dimension (which is straightforward extension) and the simplified reversibility regularization with associated theoretical analysis (which is a less straightforward one). Hence my issue here is that the work is perhaps a bit too incremental.

W2) Related with reversibility, I am under the impression that the paper is missing to position the work adequately with respect to some quite relevant related literature on the topic. The topic of reversible neural architectures has a good standing in some quite consolidated works which explicitly study the relationship with stability and non-dissipative diffusion [A]. At the same time, reversible graph flows are discussed when considering generative neural models [B]. More recently, few groups have been studying bracket-based dynamics as way to induce learning models (also on graphs) that mix reversible and irreversible behaviours  [C,D]. These are very relevant related works which deserve to be cited and confronted with both theoretically and empirically, especially as they take a different perspective of inducing provable reversibility as compared to “encouraged reversibility” as in this paper.

W3) The empirical analysis lacks sufficient details for reproducibility. I am missing in the main body (as well as in the appendices) a clear indication of the presence of a validation set, on which for instance one needs to identify the proper \alpha regularization weight. The empirical analysis itself is not very compelling as it is limited to few simple simulated physical systems. While this is somewhat consistent with some published earlier literature, in more recent works there is the tendency to validate models on more compelling and complex setups, e.g. involving simulation of MuJoCo dynamics or CMU human trajectory data.

### Questions
Q1) Authors are invited to expand the empirical and theoretical comparison to other works related to reversible architectures (see the sample provided in the Weakness sections)

Q2) Can the Authors clarify the model selection setting of the work, in particular as pertains the optimization of the model hyperparameters?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces TAGNO (Time-Reversal Latent GraphODE for Multi-Agent Dynamical Systems), a physics-based graph neural ODE-based model designed for learning and predicting dynamical systems. To enhance the regularization of graph ODEs, TANGO incorporates the concept of time-reversal symmetry, a well-established symmetry principle in classical mechanics. By formalizing a regularizer based on time-reversal symmetry (or, potentially, time-reversibility/invertibility), TANGO demonstrates superior learning and generalization capabilities when compared to other competing models. The authors also derive some theoretical properties, such as error bounds concerning the time step, further reinforcing the strengths of TANGO. To validate their proposed approach, the authors present empirical results involving four synthetic examples.

### Strengths
- TANGO, the model proposed in this study, consistently outperforms major competitors, including baseline Latent NODEs, Hamiltonian NODEs, TRS (Time-Reversal-Symmetric) NODEs, and graph NODEs, across a range of physics and dynamics forecasting problems.

- The paper is generally well-written and easy to follow (although there are some technically confusing points, please see the Weaknesses). Figure 1 and Figure 2 effectively summarize the motivation and core concept of this work.

### Weaknesses
**1. Reversing operator**

First, I would appreciate clarification on the precise calculation of the reversing operator $R$ for TANGO. While the reversing operator holds a significant role in addressing time-reversal symmetry, the current version of the paper lacks a detailed description and computation method for it. Considering that the reversing operator is typically defined in the phase space $(q, p)$, as mentioned in footnote 3, it remains unclear how it can be computed within the latent space $z$. At first glance, there are possible approaches, although they all have some concerns:

The first approach involves splitting $z$ into two components, $(z_0, z_1)$, with $z_0$ serving as a pseudo $q$ and $z_1$ as a pseudo $p$, defining $R: (z_0, z_1, t) \to (z_0, -z_1, -t)$. However, questions arise regarding the effectiveness of such a straightforward separation, as constraints similar to those found in variational Hamiltonian Monte Carlo literature might need to be imposed on $z_1$. Furthermore, it is unclear whether this approach truly captures the essence of time-reversal symmetry in the latent space, as it might inadvertently introduce constraints that are not physically meaningful.

Secondly, one might consider reversing the observations $y = (q, p)$ directly, i.e., $\hat{R}: (q, p, t) \to (q, -p, -t)$, and then assume $R \circ z = f_{dec}(\hat{R} \circ y)$. However, in this case, the reversing operation $R$ within the latent dynamics might not be an involution, which is a fundamental property of reversing operators in the context of time-reversal symmetry. This raises concerns about whether the proposed regularization truly enforces time-reversal symmetry or merely promotes a form of reversibility in the latent space.

Lastly, a simple identity operation, i.e., $R: (z, t) \to (z, -t)$ might be employed. Currently, it appears that this operation is used in the paper. However, assuming the use of $R: (z, t) \to (z, -t)$ raises a new question, which I will discuss in the following section.

**2. Time-reversal symmetry or time-reversibility?**

Since there is no explicit definition of the reversing operator, I will assume that it solely reverses the dynamics in the context of the time direction, as described in equation (8) (i.e., solving the latent ODE in $-t$ direction). In this case, I have reservations about whether equation (9), as implemented in the paper, indeed enforces time-reversal symmetry regularization for the learned dynamics. It appears to me that equation (9) may promote time-reversibility (invertibility) rather than time-reversal symmetry. I believe it is crucial to rigorously differentiate between these two concepts within this work.

Time-reversal symmetry implies that forward and backward time dynamics are indistinguishable. In contrast, time reversibility implies that these two dynamics can be distinguished but are one-to-one mappings of each other (i.e., the dynamics have a unique solution over a given time interval). For instance, an ideal oscillator would remain indistinguishable whether it evolves with forward or reverse time dynamics, thereby clearly exhibiting time-reversal symmetry. Conversely, a damped oscillator can be distinguished in this context. The forward time evolution reduces amplitude over time, while the backward time evolution increases it. This system lacks time-reversal symmetry but still poses time-reversibility (invertibility) because when a video of a damped oscillator is played in reverse, it returns to the initial frame due to the existence of a unique solution, i.e., well-defined dynamics.

Taking this into account, equation (9) appears to be a loss function designed to promote time reversibility, as evident from the lower middle figure in Figure 2. It is worth noting that many deterministic ODEs, including those governing physical systems, are theoretically guaranteed to exhibit invertibility (uniqueness of solutions) according to the Picard–Lindelöf theorem. However, in practice, the actual solutions computed by numerical solvers like RK45 may not always be perfectly invertible, especially in the case of chaotic systems and homoclinic orbits. It is conceivable that the proposed regularization of TANGO compensates for such deviations from the limited precision of numerical solvers or sensitivity on initial conditions for chaotic systems. Alternatively, TANGO might learn smoother and more noise-resistant dynamics thanks to matching the forward and inverse trajectories.

### Questions
Please see the Weaknesses also.

- What is the precise definition of the reversing operator employed in TANGO? More broadly, is there a standardized or canonical approach to defining the reversing operator for latent-based dynamics?

- Does the suggested reversal loss function result in time-reversal symmetry? Alternatively, does it promote time-reversibility (= invertibility, solution uniqueness, reduction of numerical divergence, ...), as previously mentioned?"

- It would be valuable to explore the influence of the solver choice, particularly for LGODE, TANGO, TANGO (gt-rev), and TANGO (rev2) models, through ablation studies. For instance, what would be the outcome when employing a higher-order solver in lieu of the conventional RK45? Or, how would lower-order solvers like Euler impact the results? How about Leapfrog? Assuming that the proposed loss function indeed promotes time-reversibility (invertiblity), it is plausible that the effectiveness of TANGO could diminish as the solver's precision increases.

- In Figure 5, it is noticeable that HODEN, a model known for strict energy conservation, exhibits energy divergence in the damped spring system. What could be the reason for this occurrence?

- Some minor typos, for example, page 3: real *worldsystems*, page 4: $\tau_1,\tau_2 \in \mathbb{R}^\textit{4}$, Theorem 1: The *reversal* loss $\mathcal{L}_{pred}$, ...

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces TANGO, a novel GraphODE model designed to model multi-agent dynamical systems by including a loss term introducing a time reversal symmetry constraint. This term aligns forward and backward trajectories of the learned GraphODE model. The authors argue that given the prevalence of time reversal symmetry in many physical systems, this introduces a useful inductive bias that can be helpful even for systems that don't adhere strictly to time reversal symmetry. They provide a theoretical treatment of the error terms introduced by this time reversal symmetry loss. They provide comparisons on 4 benchmarks between several methods for learning dynamics from irregularly sampled trajectories, several of them based on GraphODEs. The authors compare their loss in an ablation studies with 2 different implementations of a similar TRS loss.

### Strengths
The idea of integrating time reversal symmetry into machine learning models is interesting, and comparing different formulations with each other, and investigating to which extent these implementations differ in training stability and numerical errors, is a relevant area of study. I particularily appreciated the formal treatment of time reversal symmetry as accounting for numerical errors in Theorem 1 as an interesting contribution.

### Weaknesses
Main Contribution and Ablation Study

As the authors point out, closely related ideas to those one proposed here have been around for a while (see e.g. https://arxiv.org/abs/2003.02236 for Koopman operators, or, as the authors point out, in a very similar form in Huang et al. 2020). 
To my understanding, the main contribution is a slight reformulation of the consistency loss from Huang et al. 2020, Eq.11, so that the consistency is computed between forward and backward generated trajectories (as a form of self-consistency) and not between the predicted forward-and backward trajectories and the ground-truth data. They argue that when performing the comparison to ground-truth data, “such implicit regularization does not force time-reversal symmetry, but introduce more noise”.
The comparison of their approach with the alternative of the time reversal symmetry loss (gt-rev in Table 1) are not as convincing to me as the authors claim, since they appear quite close to their own results. Without provided statistics, it's challenging to gauge the robustness of this effect, especially given the unexpected four-digit precision in a stochastic optimization setting.

The whole paragraph explaining the ablation study (“Finally, we conduct two ablation by changing the implementation”) I found a little confusing, also given there are several grammatical inconsistencies here. Since this reformulation is highlighted as the main contribution, it would benefit from further elaboration and clarity.

Choice of comparisons:

Comparing to single-agent models on benchmarks that seem tailored to favor the inductive bias of multi-agent systems may not be particularly enlightening. Given the contribution is about improving performance with a specific formulation of a time reversal symmetry loss, investigating this for other dynamical systems and models, and e.g. comparing performance for several types of ODE models both with and without this time reversal symmetry loss, would make more sense in my opinion.

Limited Application:

The proposal in this paper, focusing on time reversal symmetry, isn't exclusive to latent graph ODEs or multi-agent dynamical systems, and has been studied in other contexts. As the authors mention, time reversal symmetry is a universal physical principle, and its incorporation through a time-reversal-sensitive loss is potentially more far-reaching. Merely extending it to a pre-existing architecture (GraphODEs) doesn't, in itself, signify a substantial contribution. The real value of the present study to my mind lies in the exploration of different forms of this time reversal consistency loss. This exploration could be more valuable if taken beyond the confines of multi-agent GraphODEs. Discussions about its applicability to other dynamical system architectures and other, e.g. single-agent systems, would make sense in this context. An investigation into Theorem 1's implications for the loss in Eq. 5 might also be interesting, since I'd suspect the scaling with sequence length T is different here. The conclusion could also discuss the potential of this loss in various contexts.

While there are interesting first steps taken in this paper, there is still room to extend these ideas to a wider, more generally applicable framework and theoretical investigation. Otherwise the contribution is quite limited and the experimental underpinning not fully convincing. If these concerns are addressed I am happy to adjust my score.

### Questions
Why does the MSE of the chaotic pendulum remain almost constant across prediction lengths in Fig. 4? For a chaotic system, I would expect exponential divergence of trajectories? How does the time horizon compare to the system's approximate prediction horizon, related to its maximum Lyapunov exponent?

Figure 5:
The left plot lacks x and y-axis labels, which could aid with interpretation. On the right side, including ground truth system energies, similar to Fig. 1, would be beneficial for clarity.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a novel method with a soft constraint regularization term. The term is designed following the Time-Reversal Symmetry principle, aligns the forward and backward trajectories prediction, and thus helps the whole model to learn the dynamics of a complex multi-agent system even if it does not have the law of energy conservation. The experiments show the performance of the proposed method thoroughly on simulated datasets.

### Strengths
- The proposed method introduces a novel and significant contribution to the dynamics modeling field. It tackles the challenging task of modeling systems that deviate from the conventional energy conservation principles. Notably, the introduction of TANGO appears to be a fresh addition, enriching the research landscape.
- The paper exhibits a well-organized structure, systematically introducing and showcasing the performance of TANGO, making it easily understandable for readers.
- The work is thoughtfully situated within the existing literature, providing context and relevance to the broader research landscape.
- The comprehensive and compelling experiments conducted on simulated data greatly enhance the paper's credibility and the method's efficacy.
- The inclusion of well-structured and clean code is commendable, ensuring the reproducibility of the results and making it accessible for future research endeavors.

### Weaknesses
 - The current method description appears to be somewhat confusing and would benefit from revision. For instance, in Section 3.1, Equation (6) poses challenges in understanding aspects like the derivation of $z_1^{\text{fwd}}(t)$, and it's worth noting that $g(\cdot)$ is missing in Figure 2. The description of the model input is unclear, particularly regarding the role of the adjacency matrix. The text in Section 2, stating "Model input consists of trajectories of such features...", is misleading as it does not explicitly mention the graph structure as a necessary input, leading to a misunderstanding of the methodology. This lack of clarity extends to the explanation of how the graph structure is incorporated into the GNN-based ODE framework, and whether the adjacency matrix should be considered a form of ground-truth data.
- While the experiments are well-executed on simulated data, there's a notable absence of real-world data. This could potentially be attributed to the inherent challenges associated with collecting such data, as acknowledged in the paper.

### Questions
- In the introduction, the paragraph preceding "Contributions" mentions the "time-reversal loss" not requiring additional labels beyond "ground-truth observations." Clarification is needed regarding what constitutes these "ground-truth observations."
- It's worth exploring the adaptability of TANGO to dynamic graphs, which involve nodes and edges appearing and disappearing. This could be an intriguing avenue for future research.
- Notably, the results in Table 1 reveal that TANGO exhibits a lower Mean Squared Error (MSE) on the Damped Spring dataset compared to the Simple Spring dataset, which is somewhat surprising. Investigating the underlying reasons for this discrepancy may shed light on the method's performance characteristics and potential areas for improvement.
- A suggestion: please check the references and make them up-to-date.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
