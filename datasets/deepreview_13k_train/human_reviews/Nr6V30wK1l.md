# Conditional Variable Flow Matching: Transforming Conditional Densities with Amortized Conditional Optimal Transport

- Decision: Reject
- Scores: 3, 3, 6, 6

## Abstract
Forecasting stochastic nonlinear dynamical systems under the influence of conditioning variables is a fundamental challenge repeatedly encountered across the biological and physical sciences. While flow-based models can impressively predict the temporal evolution of probability distributions representing possible outcomes of a specific process, existing frameworks cannot satisfactorily account for the impact of conditioning variables on these dynamics. Amongst several limitations, existing methods require training data with paired conditions and are developed for discrete conditioning variables. We propose \textit{Conditional Variable Flow Matching} (CVFM), a framework for learning flows transforming conditional distributions with amortization across continuous conditioning variables -- permitting predictions across the conditional density manifold. This is accomplished through several novel advances. In particular, simultaneous sample conditioned flows over the main and conditioning variables. In addition, motivated by theoretical analysis, a conditional Wasserstein distance combined with a loss reweighting kernel facilitating conditional optimal transport. Collectively, these advances allow for learning system dynamics provided measurement data whose states and conditioning variables are not in correspondence. We demonstrate CVFM on a suite of increasingly challenging problems, including discrete and continuous conditional mapping benchmarks, image-to-image domain transfer, and modeling the temporal evolution of materials internal structure during manufacturing processes. We observe that CVFM results in improved performance and convergence characteristics over alternative conditional variants.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
the authors present CONDITIONAL VARIABLE FLOW MATCHING (CVFM), a model for generative modeling within the flow matching framework, where a neural network learns the implicitly defined vector field between conditional distributions. They do this by pairing samples across source and target distributions by penalising cross-condition assignment and learning condition dependent flows.

### Strengths
I am drawn to the idea of extending the flow matching idea to other settings, such as conditional distributions. CVFM does so in a simple, straightforward way, which consists of smart sampling of source and target pairs, and conditioning of the neural network. The authors also extend the theory of FM and prove the holding of the continuity to the conditional case.

The paper is generally well written and the authors have put emphasis on readability and having their manuscript be easy to follow. Their empirical validations, particularly the results regarding material trajectory inference, are convincing and demonstrate the validity of their approach.

### Weaknesses
The approach presented in this paper is relatively incremental. As mentioned, CVFM consists of two improvements beyond standard FM, the first is using a conditional-attenuated distance for OT based source and target assignment, and the second is the conditioning the model's neural network via the input. While the first is cool, it is not clear to me if it holds enough merit on its own, as It's hard to claim the neural network component is all that novel, as training FM by conditioning the input (i.e. learning f(x,y,t), instead of f(x,t)) is a straightforward extension. The authors should make clear what sets their approach apart from the current state of the field.

The impact of the condition coefficient eta eq 15 needs to be better studied. As mentioned, this is distance is a key conceptual contribution of this, and demands careful ablation. In the supplement, I see values ranging for 5 to 1e5 (lines 1534 and 1549). How sensetive is the algorithm to choice of eta? In the discrete case, is this even that relevant? Can you not just sample equally from each condition and only pair within?

CVFM is only relevant when both source and target distributions are influenced by conditions. While its ubiquitous to have structured data be the target distribution (i.e. images separated by class), the source is usually chosen to be an easy to sample from noise distribution, such as the uniform or standard Gaussian. It is not immediately clear to me from this paper what are the instances when there is a need to transform structured source into structured target. This issue is somewhat palpable based on the results presented in this work, which are either simulated datasets (8 Gaussians & Moons) or a conditional transfer between MNIST and FashionMNIST images. The authors should make further attempts to demonstrate their work on real-world applications besides a single material trajectory inference example. This would serve to both further corroborate their work while also convincing the community of its relevance.

Figure 2 could be made clearer. In the 8 Gaussian and Moons datasets, what are the different conditions? This information particularly pertinent for concept behind this work. I understand the trajectories are coloured by condition but it's not clear what they are.

### Questions
The authors make note that CVFM amortises Flow Matching over conditionals. This implies an important advantage: instead of learning separate flows for each condition, it learns a single model that can handle all conditions by sharing information across them. To properly validate this claim, it would be valuable to include a comparison against a baseline where you train separate flow matching models for each condition individually. This experiment would directly test whether CVFM's unified approach actually performs better than having dedicated models for each condition.

Can the authors please share code? The main contribution of this work is algorithmic, access to code would greatly improve my ability to judge the merits of this manuscript.

Is the pseudo-code in algorithms 1 & 2 correct? As written, the values for pt(x|w) and pt(y|w) are computed before the OT assignment, but if thats so, the x and y value in lines 1476 & 1504 do not align with the regressed flow.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies flow matching in the setting of conditional simulation. The authors study conditional optimal transport as a tool for designing couplings in this setting, and empirically verify their proposed method on several 2D datasets, an image-to-image problem, and a material dynamics problem.

### Strengths
- The paper is generally clear, well-written throughout
- The problem studied is important and likely of relevance to the broader community
- Generally the derivations in the paper are sound

### Weaknesses
### Novelty / Related Work
- A major weakness of this paper seems to be novelty. There are several recent works which study conditional OT for flow matching. It was not clear to me what is new in this submission that did not appear in these prior works. In particular, both of these papers use the weighted cost in Equation 15 to build minibatch COT couplings, followed by fitting a flow matching model using these couplings. There are many more similarities as well, e.g., both papers identify the $q(y_0) = q(y_1)$ condition appearing in Theorem 3.1 of this submission. These both appeared in March/April 2024 (~5 months before the ICLR deadline), so should probably not be counted as concurrent works.
     - [Dynamic Conditional Optimal Transport through Simulation-Free Flows, NeurIPS 2024](https://arxiv.org/abs/2404.04240)
     - [Conditional Wasserstein Distances with Applications in Bayesian OT Flow Matching, arXiv](https://arxiv.org/abs/2403.18705)

- Prop. 3.1 in the submission is known, see e.g. [Carlier 2008](https://arxiv.org/abs/0810.4153), and this work should be cited for the modified loss in Equation 15 and the corresponding convergence in Prop 3.1. Moreover, the two papers above use this result and the corresponding loss function in Equation 15 to derive COT methods for flow matching. 

- In Lines 90-01, the authors write "leveraging a novel conditional Wasserstein metric..." and similar things in the abstract. 
     - The authors never explicitly describe what this metric is (or e.g. prove that it is a metric).
     - Conditional Wasserstein metrics have already been developed and are very similar to the notions discussed in the submission. Please see the two linked papers and this [PhD Thesis](https://ricerca.sns.it/retrieve/e3aacdfd-ef40-4c98-e053-3705fe0acb7e/Gigli_Nicola.pdf), Chapter 4, for previous work in this direction.

### Experiments
- There are no baselines for the MNIST-FMNIST image transfer experiment. The baselines in Table 2 are quite weak (only an LSTM and a neural ODE). Table 1 only compares against ablations of the proposed method.

### Questions
Please see weaknesses

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce conditional variable Flow Matching (CVFM), which allows for the transformation of conditional distributions across continuous conditioning variables with unpaired samples. The paper demonstrates the application of CVFM across various domains, such as image-to-image domain transfer and modeling the temporal evolution of materials' internal structures during manufacturing processes, showing improved performance and convergence characteristics over existing methods.

### Strengths
* The paper is generally well-written and easy to follow, with a few exceptions noted below.

* The experiments are well chosen, ranging from controlled synthetic scenarios to real-world material-related challenges.

* There are informative additional experiments and ablations in the appendix which demonstrate the effectiveness and superior performance of the proposed method.

### Weaknesses
 * There are typos in some equations that need correction.

* The descriptions of some experiments are unclear, particularly how discrete and continuous variables are used.

* The discussion on how the proposed model differs from or outperforms the $[SF]^2$M (Tong et al, 2023) approach is vague and requires clarification. Please refer to the questions below for specifics

* Equation 6, typo in the subscript. It should be $\mathbb{P}_0 = \nu_0$ rather than $ \nu_1$, and $\text{argmin}$ should be used instead of $\text{min}$. Please review Equation 6 carefully.

* What’s the main difference between the proposed method and  $[SF]^2$M (Tong et al, 2023)?. Section 3.1 of  (Tong et al, 2023) suggests $[SF]^2M$ model can handle general conditioning information $z$, where pair $(x_0, x_1)$ is a special case. It appears the proposed method by the authors may be a special case of  $[SF]^2$M? Can the authors clarify the difference? Or why is the proposed method better than  $[SF]^2M$ ? 

* In the experiments. I got confused about discrete and continuous conditioning used.  In Figure 2 (8 Gaussian-Moon),  what are the conditional variables $y_0$ and $y_1$ associated with $x_0$ and $x_1$ ? Intuitively, the authors might align 8 labels to $x_0$, but what are the conditional variables for $x_1$? Besides, is one-hot encoding applied to the discrete conditional variables to differentiate it from continuous conditioning variables? The same question for the material dynamics example

### Questions
* Equation 6, typo in the subscript. It should be $\mathbb{P}_0 = \nu_0$ rather than $ \nu_1$, and $\text{argmin}$ should be used instead of $\text{min}$. Please review Equation 6 carefully.

* What’s the main difference between the proposed method and  $[SF]^2$M (Tong et al, 2023)?. Section 3.1 of  (Tong et al, 2023) suggests $[SF]^2M$ model can handle general conditioning information $z$, where pair $(x_0, x_1)$ is a special case. It appears the proposed method by the authors may be a special case of  $[SF]^2$M? Can the authors clarify the difference? Or why is the proposed method better than  $[SF]^2M$ ? 

* In the experiments. I got confused about discrete and continuous conditioning used.  In Figure 2 (8 Gaussian-Moon),  what are the conditional variables $y_0$ and $y_1$ associated with $x_0$ and $x_1$ ? Intuitively, the authors might align 8 labels to $x_0$, but what are the conditional variables for $x_1$? Besides, is one-hot encoding applied to the discrete conditional variables to differentiate it from continuous conditioning variables? The same question for the material dynamics example

### Soundness
4

### Presentation
3

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
This paper propose conditional variable flow matching (CVFM), a framework for learning to transform conditional distributions between source and target distributions given unpaired samples (response and covariates are not in correspondence). This is achieved by simultaneously sample $x$ and $y$, and further incorporate $y$ into smoother (neural net) for vector field. To further stabilize and accelerate training, they further use conditional OT & mismatch. In the experiement part, they extensively study the proposed method.

### Strengths
Further extend the CGFM (guided flow), by further do sampling on covariates $y$. Therefore, we can deal with the unpaired data.

### Weaknesses
Even before the CGFM formally released, the conditional sampling strategy by incorporating $y$ into neural net has been used widely in many fields. This work further extends the CGFM, but may raise some concern for novelty? The core contribution seems to be in the specific combination of conditional flow matching with optimal transport and a reweighting kernel, but the individual components are not entirely novel. The paper claims that CGFM cannot extend to continuous conditioning, but it's not clear why simply including a continuous $y$ into the neural network wouldn't allow for conditional sampling. The argument that resampling is statistically impossible when $y$ is continuous is not fully convincing, as permutation or resampling strategies could potentially be employed, albeit perhaps with reduced efficiency. The motivation for 'unpaired data' is also not entirely clear, as many scenarios could be framed as regression problems, blurring the line between paired and unpaired data.

### Questions
1. In line 364, not sure I understand your claim that CGFM cannot extend to conitnuous conditioning. Since $y$ can be continuous, if we include $y$ into neural net, we can do conditional sampling based on continuous covariate $y$?
2. Out of curiousity: the CGFM can still used for unpaired data by simply do local permutation/ resampling of covariates $y$ during training? Is this strategy not ideal for efficiency? Just a quick idea.

### Soundness
3

### Presentation
3

### Contribution
2
