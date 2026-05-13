# TRENDy: Temporal Regression of Effective Nonlinear Dynamics

- Decision: Accept
- Scores: 3, 6, 6

## Abstract
Spatiotemporal dynamics pervade the natural sciences, from the morphogen dynamics underlying patterning in animal pigmentation to the protein waves controlling cell division. A central challenge lies in understanding how controllable parameters induce qualitative changes in system behavior called bifurcations.  This endeavor is made particularly difficult in realistic settings where governing partial differential equations (PDEs) are unknown and data is limited and noisy. To address this challenge, we propose TRENDy (Temporal Regression of Effective Nonlinear Dynamics), an equation-free approach to learning low-dimensional, predictive models of spatiotemporal dynamics. Following classical work in spatial coarse-graining, TRENDy first maps input data to a low-dimensional space of effective dynamics through a cascade of multiscale filtering operations. Our key insight is the recognition that these effective dynamics can be fit by a neural ordinary differential equation (NODE) having the same parameter space as the input PDE. The preceding filtering operations strongly regularize the phase space of the NODE, making TRENDy significantly more robust to noise compared to existing methods. We train TRENDy to predict the effective dynamics of synthetic and real data representing dynamics from across the physical and life sciences. We then demonstrate how our framework can automatically locate both Turing and Hopf bifurcations in unseen regions of parameter space. We finally apply our method to the analysis of spatial patterning of the ocellated lizard through development. We found that TRENDy's predicted effective state not only accurately predicts spatial changes over time but also identifies distinct pattern features unique to different anatomical regions, such as the tail, neck, and body—-an insight that highlights the potential influence of surface geometry on reaction-diffusion mechanisms and their role in driving spatially varying pattern dynamics.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces TRENDy, a framework designed for learning low-dimensional surrogates of complex dynamical systems where underlying PDEs are unknown, and data is noisy or limited. The main contributions of TRENDy include:

1. Modeling Effective Dynamics: TRENDy maps underlying PDE using multiscale filtering into a reduced space and models the reduced representation with a neural ODE. This NODE captures the system's behavior based on its governing parameters, which enables TRENDy to predict system dynamics in new parameter spaces.

2. Predicting Bifurcation: moreover, for a parameter-dependent system, the framework is able to predict bifurcations, where a sudden qualitative change in its behaviors. TRENDy also shows robustness to noise in bifurcation localization.

3. Application to Real-World Data: authors also used the patterning in the ocellated lizard as an example to illustrate how the framework's latent space captures meaningful biological features.

### Strengths
1. Originality: 

The approach that combines scattering transform and neural ODEs to model the effective dynamics is novel, especially given its application to bifurcation prediction, a challenging task where data is limited and governing equations are unknown.

2. Quality and Clarity: 

The paper shows rigorous methodology and fruitful details in various experiments. Explanations on filtering operations, the NODE structure, and training details led the model's design to be crafty and reliable. 

3. Significance: 

TRENDy addresses a crucial question in modeling systems governed by unknown or complex PDEs, where direct analytic solutions are impractical to get. The framework’s adaptability to new parameter spaces may also have numerous applications in real-time system control and scenario exploration. In a nutshell, the authors have shown that TRENDy has the potential to significantly advance research in fields like synthetic biology, physics, climate change and ecology, where such questions regarding complex dynamical systems are pretty common.

### Weaknesses
1. Multiscale Filtering:

The use of multiscale filtering (e.g., scattering transforms) is central to TRENDy, while the specific choice and design of the filtering process are not fully explored in the paper. Authors should provide more why they prefer this type of dimension reduction technique rather than others (for example, do ablation studies on other type of techs and show the one you mentioned is the best). Moreover, compared with too  many experimental details in the main text (better go to supporting materials), it is necessary to say more on multiscale filtering details, e.g. effects of the choice on scattering coefficients. Such explanations / experiments are essential to keep novelty of the paper, since they are numerous papers working on PDE + DL topics (and some of them should be acknowledged, e.g. PDE-net by Long et al. [1], PINNs by Karniadakis et al. [2], and other papers focusing on effective dynamics, see [3] and [4]). Specifically, the paper lacks a detailed justification for using scattering transforms over other dimensionality reduction techniques like PCA or autoencoders. The impact of different scattering kernel choices and the depth of the scattering network on the performance of TRENDy should also be investigated. Furthermore, the paper should clarify how the scattering coefficients capture the relevant features of the system, and how these features relate to the underlying physics of the PDEs.

2. Reconstructing State Space:

Just like lifting and restriction in the equation-free approach, TRENDy should have the module which maps the latent dimensions back to the full PDE state space. Without such an explicit decoder, the ability to verify the reduced dynamics against full state predictions will be limited. It will also become an obstacle for researchers in other fields to explore the explainability by utilizing your model. It seems adding a mechanism for decoding reduced dynamics back into full spatial states or maybe explaining why this is not feasible in your scope is essential. The absence of a decoder limits the interpretability of the latent space and makes it difficult to validate the model's predictions against the actual PDE solutions. The paper should address how the reduced representation relates to the original high-dimensional state space and provide a method for visualizing or interpreting the latent variables in terms of physical quantities.

3. Miscellaneous:

I suggested the reviewers consider the following issues, and if time allows, do some elaboration.

a) Extending the experimental scope (e.g. systems with chaotic attractors, or discrete-time systems).

b) Discussing the model’s performance on large datasets and its computational demands in both training and inference.

c) Implementing interpretability techniques (e.g., parameter sensitivity, feature importance) to provide insights on multiscale filtering.

### Questions
Besides several concerns that mentioned in the weakness part, here are several questions regarding the paper details:

Figure 1: what is $S_i(0)$ here? And why do they have different heights?

Eq 1: it is better to use $u(x, y)$ rather than $u(r)$, as you are talking about 2D space now.

Usage of subscripts (Line 138 and other notations): the subscripts sometimes are very misleading. e.g. $u_{\theta}$ and $u_0$.

Line 139: for $u_0 \notin D$, do you mean interpolation and/or exploration?

Line 141: needs explanation of what $U$ is.

Line 148: similar as what mentioned previously, why do you assume $\Phi$ is hardwired and unlearned? Can the multiscale filtering parameters be learnable?

Figure 2: this figure needs more details to explain. For example, you should say the inset squares means PDE solutions (otherwise it is misleading).

Line 207: the approximately equal symbol here is incorrect. And moreover, what is SINDyCP? Formula of it? Does it have any assumptions? Have you cited it?

Lines 230-232: may need a figure to illustrate your conditions. For example, what is “patches”?

Line 266: need to show why $S_{1, 2}$ almost equals to $<u>$ and $<v>$.

Line 306: use def eq symbol “:=” here in $d_{\gamma} (\theta)$.

### Soundness
2

### Presentation
2

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
The framework introduced by the authors captures the dynamics of spatio-temporal parameterised PDE systems by relying on established reduced order modelling techniques and training a NODE solver. The author(s) showcase that the framework can capture the bifurcation points in various test and real datasets.

### Strengths
- The paper is well presented and clearly structured and introduces a framework which could prove to be impactful in the area of parameterised PDE modelling.
- The authors have included a strong baseline model (SINDyCP) for the Gray Scott example.

### Weaknesses
 - The lack of decoder reduces the interpretability of the approach. This point is highlighted by the authors themselves but should be made earlier in the work and ways in which it will be tackled should be outlined.


 - All references should be checked, there are various instances of spelling mistakes.
- The addition of legends to Figure 3 would improve the presentation of the results.

### Questions
- Did the authors trial any alternatives to the scattering transforms? To showcase the touted benefits of the chosen approach.  
- Is there a reason the baseline is not implemented for The Brusselator and real-world examples?
  - Have alternative types of bifurcations being considered (rate-induced bifurcations)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces TRENDy as a data-driven, low-dimensional predictive modeling approach for spatiotemporal dynamics. TRENDy uses multiscale filtering to map data into effective dynamics, then fits a NODE to this reduced space. This process robustly regularizes the NODE phase space, making TRENDy resilient to noise. The so-called TRENDy is examined on synthetic and real data across physical and life sciences. It's posed as a versatile tool for studying and controlling spatiotemporal dynamics.

### Strengths
N/A

### Weaknesses
The significance of the work is missing by authors specifically compared to the state of the art approaches. In addition, the complexities of fitting by a neural ordinary differential equation need to be justified.

### Questions
The main question is comparing with the outstanding class of operator theoretic settings.

### Soundness
2

### Presentation
3

### Contribution
2
