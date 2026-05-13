# Estimating Committor Functions via Deep Adaptive Sampling on Rare Transition Paths

- Decision: Reject
- Scores: 3, 8, 3, 3

## Abstract
The committor functions are central to investigating rare but important events in molecular simulations. It is known that computing the committor function suffers from the curse of dimensionality. Recently, using neural networks to estimate the committor function has gained attention due to its potential for high-dimensional problems. Training neural networks to approximate the committor function needs to sample transition data from straightforward simulations of rare events, which is very inefficient. The scarcity of transition data makes it challenging to approximate the committor function. To address this problem, we propose an efficient framework to generate data points in the transition state region that helps train neural networks to approximate the committor function. We design a Deep Adaptive Sampling method for TRansition paths (DASTR), where deep generative models are employed to generate samples to capture the information of transitions effectively. In particular, we treat a non-negative function in terms of the integrand in the loss functional as an unnormalized probability density function and approximate it with the deep generative model. The new samples from the deep generative model are located in the region of the transition and fewer samples are located in the other region, which provides effective samples for approximating the committor function and significantly improves the accuracy. We demonstrate the effectiveness of the proposed method with both simulations and realistic examples.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a method to compute the committor function of molecular rare events based on DASTR. The paper conducts experiments on multiple molecular structures that estimate the committor function and find pathways between metastable states. Specifically, the experiment shows DASTR has much lower error ranges than uniform sampling and SDE sampling methods.

### Strengths
1. The paper explains the Langevin dynamics and the problem of solving the committor function well. The background and the difficulty of the problem is clear.

2. The experiments are based on benchmarks in this field, and the paper shows many results from these experiments, such as error bounds and molecule trajectories. There are good comparisons between DASTR and uniform sampling and SDE sampling with elevated temperature.

### Weaknesses
1. The paper does not solve a difficult problem in estimating the committor function, for example, rare events with a committor function of 1e-5 scales. Based on Figure 5, the committor function has a smooth curve from 0 to 1 and requires not that many sample sizes to estimate. In this case, even uniform sampling can obtain good results. It is hard to convince the readers that the deep adaptive sampling method can save high simulation costs and be extended to difficult rare event sampling problems.

2. The paper misses many related work citations and comparisons with these methods. The experiments only have a comparison with uniform sampling and SDE sampling, and there are many other methods to compare.

Yuan, Jiaxin, et al. "Optimal control for sampling the transition path process and estimating rates." Communications in Nonlinear Science and Numerical Simulation 129 (2024): 107701.

Hua, Xinru, et al. "Accelerated Sampling of Rare Events using a Neural Network Bias Potential." AI for Accelerated Materials Design-NeurIPS 2023 Workshop. 

Khoo, Y., Lu, J. & Ying, L. Solving for high-dimensional committor functions using artificial neural networks. Res Math Sci 6, 1 (2019). https://doi.org/10.1007/s40687-018-0160-2

Lars Holdijk, Yuanqi Du, Ferry Hooft, Priyank Jaini, Bernd Ensing, and Max Welling. 2024. Stochastic optimal control for collective variable free sampling of molecular transition paths. In Proceedings of the 37th International Conference on Neural Information Processing Systems (NIPS '23). Curran Associates Inc., Red Hook, NY, USA, Article 3481, 79540–79556.

### Questions
1. From Figure 2c, DASTR sampled points are incorrect. The sampled particles are not mostly near A or B but reside in between where there is an energy barrier. Is this a mistake in visualization? 

2. Have you tried sampling with lower transition rates, such as on the scales of 1e-5? In this case, the transitions are rare events, so it is more convincing to show the effectiveness of DASTR.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper “Estimating Committor Functions via Deep Adaptive Sampling on Rare Transition Paths” addresses the computational challenges in estimating committor functions for rare events in high-dimensional molecular simulations. The committor function  q(x)  represents the probability that a system starting from a state  x  will reach metastable state  A  before metastable state  B . Accurately computing this function is crucial but suffers from the curse of dimensionality and the scarcity of transition data in rare event simulations.

To overcome these challenges, the authors propose the Deep Adaptive Sampling method for Transition paths (DASTR). This novel framework utilizes deep generative models to generate data points concentrated in the transition state regions between metastable states. By treating a non-negative function from the loss functional as an unnormalized probability density function, the method effectively samples the most informative regions for approximating the committor function. This targeted sampling enhances the efficiency and accuracy of training neural networks for this purpose.

The effectiveness of DASTR is demonstrated through numerical experiments on the Müller potential problem, standard Brownian motion, and the alanine dipeptide molecule in vacuum. The results show significant improvements in the approximation of the committor function, validating the method’s ability to handle high-dimensional systems and rare transition events more efficiently than traditional sampling techniques.

### Strengths
The paper offers a significant and innovative contribution to the estimation of committor functions in high-dimensional molecular simulations, particularly addressing the challenges associated with rare event sampling.

A standout aspect of the paper is the introduction of a novel objective function for training neural networks to approximate the committor function. Specifically, the authors present equation (3):

$$\min_\theta \int |\nabla q(x)|^2 e^{-\beta V(x)} dx,$$

where  $q(x)$  is the committor function,  $\beta$  is the inverse temperature, and  $V(x)$  is the potential energy function. This formulation is original because it directly incorporates the physics of the system into the learning objective, allowing the neural network to be trained in a way that is both mathematically rigorous and physically meaningful.

Moreover, the authors demonstrate that this variational problem is equivalent to solving the partial differential equation (PDE) that the committor function satisfies in regions outside the metastable states  A  and  B :

$$-\frac{1}{\beta} \Delta q(x) + \nabla V(x) \cdot \nabla q(x) = 0.$$

### Weaknesses
The proposed method assumes that the metastable states  A  and  B  are already identified. In practical molecular dynamics (MD) applications, especially in complex systems, identifying these states can be challenging and may require additional computational methods or expert knowledge. This reliance potentially limits the method’s applicability to systems where metastable states are not well-defined or are difficult to determine. Incorporating a mechanism or providing guidelines for identifying metastable states within the framework would enhance the method’s usability. Furthermore, the method's reliance on a predefined reaction coordinate, implicit in the choice of metastable states A and B, is a significant limitation. The committor function is highly sensitive to the choice of these states, and a poor selection can lead to inaccurate results. The method does not provide any guidance on how to choose these states, and this choice is not always obvious, especially in high-dimensional systems. The lack of a systematic approach for identifying appropriate metastable states and the associated reaction coordinate is a critical weakness that needs to be addressed to make the method more robust and widely applicable.

The current method focuses on estimating the committor function between two metastable states  A  and  B . In practical molecular systems, there are often more than two metastable states that contribute to the system’s dynamics. How can your Deep Adaptive Sampling method be adapted to handle scenarios with three or more metastable states?

### Questions
The current method focuses on estimating the committor function between two metastable states  A  and  B . In practical molecular systems, there are often more than two metastable states that contribute to the system’s dynamics. How can your Deep Adaptive Sampling method be adapted to handle scenarios with three or more metastable states?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This papers propose the framework DASTR to estimate committor functions, essential in studying rare transition events between meta-stable states in molecular dynamics simulations. Committor function $q(x)$ is the probability that a simulation starting from state $x$ reaches a target state $B$ before another state $A$. While computing the committor function is impractical due to the high-dimensional nature and rarity of transitions, the authors combine generative models and adaptive sampling in the framework for a better estimation of the committor function.

### Strengths
1. Effective sampling

In my opinion, DASTR is quite similar to active learning, updating the dataset and improving the generative model iteratively. This allows sampling in transition regions, leading to a proper committor function estimation, especially useful in molecular systems where transitions are rare events.

### Weaknesses
1. Limited baselines

The baselines that exist in the paper are only standard SDE and artificial temperature. Including comparison with other sampling techniques such as steered molecular dynamics, and transition path sampling to estimate the committor function would provide a robust result.

2. Lack of comparison with prior works

Similar to W1, the papers lack comparison or difference with prior works. The authors have noted that the proposed approach generalizes prior sampling strategies, in section 2 and have cited papers related to it. However, the the difference/novelty of DASTR seems to not have been discussed clearly, could the authors add one?



### Questions
1. Applying sampling distributions to collective variables

In section 4 sample generation, the authors imply that the sampling distribution $p_{V, q}(x)$ can be applied to collective variables. As far as I know, collective variables may represent many-to-one mapping, such as torsion angles in alanine dipeptide, so it sounds awkward to let $p_{V, q}(x) = p_{V, q}(S(x))$. Could the authors please explain this part more in detail?

2. Computation cost

Compared to prior adaptive sampling technique, what is the time & space complexity of DASTR? A brief O notation would be okay.

3. Escaping local minima

In umbrella sampling, an external bias is introduced to pull the system out of the local minima. For DASTR, is there a guarantee that it will not be trapped in a local intermediate point?


Minor

- Does the notation $\mathsf{S}^{g}_{k}$ refers to the training generated at state $k$, where ‘g’ represent generated?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a methodology, referred to as DASTR, to approximate the committor function, which is central in transition path theory (TPT). The authors adopt a variational loss to approximate the committor function, where the loss is expressed as an integral with an empirical distribution. They aim to increase sampling in the reactive (transition) region by adjusting the sampling measure. Specifically, they adjust the sampling measure to be proportional to the magnitude of the gradient field of the neural-parameterized committor function, focusing on regions with high variation that require denser learning.
They sample from the generative model $p_\text{KRnet}$ and compensate the training objective using the probability density of the generative model for unbiased training. In summary, the training process iteratively learns both the committor function $q_\theta$ and the sampling measure $p_\text{KRnet}$.
The authors evaluate the model’s accuracy (using the $L^2$ norm) by comparing it to numerically obtained committor functions on a 2D rugged Mueller potential (with eight dummy dimensions) and a standard Brownian system (without potential). Additionally, they assess the model on transition paths between the $C_{7eq}$ and $C_{ax}$ basins in alanine dipeptide as a real-world application.

### Strengths
- Proposes an efficient framework for approximating the committor function with an adaptive sampling distribution.
- Utilizes a flow-based generative model, which allows exact likelihood computation—a useful approach.

### Weaknesses
 - Using a generative model as the sampling distribution may not be scalable. Complex reaction systems requiring TPT often involve large molecules, not small systems like those addressed by TST. More investigation is needed to verify the framework’s applicability to larger systems.
- Although the authors describe the system as high-dimensional, the alanine dipeptide system is the smallest among poly-peptides. Moreover, they use collective variables for dimensionality reduction. In many cases, collective variables are not well-known and require extensive chemical analysis of the reaction path. Therefore, it would be beneficial to explore the application of a collective-variable-free model. The authors do not provide a clear justification for the cost-efficiency of their generative model in high-dimensional spaces, which is crucial for its practical application.
- Most evaluations are conducted on the 1/2-isosurface. The committor function could be potentially applied in areas like transition rate analysis or path sampling. To assess the framework’s utility, additional validation metrics such as flux comparison, path sampling quality, and rate comparison should be conducted. One suggestion is to calculate the transition rate of the forward and backward reactions using the committor function and compare it to the equilibrium constant, which could be obtained based on the energetics.
- There is no comparison with other methods. The rugged Mueller potential is widely used in studies approximating the committor function, as referenced by the authors. At minimum, a comparison of training time and accuracy with other methods on this rugged Mueller potential would be valuable.

### Questions
- What is the reason for evaluating only at the 0.5 isosurface? Wouldn't it be fairer to evaluate at other isosurfaces between 0.0 and 1.0 as well? Since your proposed sampling method focuses more on the 0.5 isosurface, wouldn’t a more refined evaluation be necessary near the A and B basins?

### Soundness
3

### Presentation
3

### Contribution
3
