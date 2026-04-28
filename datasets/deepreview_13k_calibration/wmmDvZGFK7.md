# PFDiff: Training-free Acceleration of Diffusion Models through the Gradient Guidance of Past and Future

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Diffusion Probabilistic Models (DPMs) have shown remarkable potential in image generation, but their sampling efficiency is hindered by the need for numerous denoising steps. Most existing solutions accelerate the sampling process by proposing fast ODE solvers. However, the inevitable discretization errors of the ODE solvers are significantly magnified when the number of function evaluations (NFE) is fewer. In this work, we propose \textit{PFDiff}, a novel \textit{training-free} and \textit{orthogonal} timestep-skipping strategy, which enables existing fast ODE solvers to operate with fewer NFE. Specifically, PFDiff initially utilizes gradient replacement from past time steps to predict a “\textit{springboard}”. Subsequently, it employs this “springboard” along with foresight updates inspired by Nesterov momentum to rapidly update current intermediate states. This approach effectively reduces unnecessary NFE while correcting for discretization errors inherent in first-order ODE solvers. Experimental results demonstrate that PFDiff exhibits flexible applicability across various pre-trained DPMs, particularly excelling in conditional DPMs and surpassing previous state-of-the-art training-free methods. For instance, using DDIM as a baseline, we achieved 16.46 FID (4 NFE) compared to 138.81 FID with DDIM on ImageNet 64x64 with classifier guidance, and 13.06 FID (10 NFE) on Stable Diffusion with 7.5 guidance scale.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel methodology to accelerate diffusion model sampling. The core concept involves reusing past score predictions to generate a preliminary estimate (springboard) for the next step. Then, future score prediction is obtained from this springboard. By leveraging this future score prediction, the method enables step skipping, directly calculating the point two steps ahead from the current position. This approach offers practical advantages as it is orthogonal to existing advanced samplers and does not require additional training. Extensive experiments demonstrate its effectiveness in significantly accelerating diffusion model sampling when integrated with various state-of-the-art samplers.

### Strengths
1. Extensive experiments conducted with diverse models and baselines underscore both the superiority and generality of the proposed methodology. Comprehensive results reveal a substantial improvement in the efficiency of diffusion sampling.
2. By approaching diffusion model acceleration through time-skipping, the authors introduce a technique that is orthogonal to existing advanced samplers. This characteristic, coupled with its training-free nature, enhances its practical applicability.
3. Despite its simplicity and ease of implementation, the methodology presented in the paper yields significant benefits.

### Weaknesses
1. The multi-step solver's exclusion of future gradients, a core component of the proposed methodology, undermines the claimed orthogonality. Specifically, while the method is presented as a general wrapper, the practical implementation seems to selectively omit future gradient information when used with higher-order solvers, raising questions about its true generality and the theoretical basis for this exclusion. Additionally, the absence of experimental results (Stable diffusion) integrating the method with the DPM-Solver series raises doubts about its performance enhancement potential and the extent of its orthogonality when applied to multi-step solvers. The lack of these results makes it difficult to assess the method's effectiveness across a broad range of solvers.
2.  While the methodology is presented as an orthogonal wrapper for arbitrary ODE solvers, its classification as a standalone ODE solver is also plausible, depending on the perspective. The method's core mechanism of predicting future scores and using them to skip steps could be interpreted as a novel discretization scheme, blurring the lines between a wrapper and a solver.
3. The use of "gradient guidance" in the title and text is potentially misleading. In the context of diffusion models, this term is typically associated with guiding the sampling process using external model gradients (e.g. classifier guidance). For better clarity, using terms like "score" or "predicted noise" would be more appropriate. This misnomer could lead to confusion about the method's actual mechanism.
4. The direct comparison between the future gradient and the springboard in Figure 2(b) is questionable. Given their different scales and the fact that the springboard is a processed version of past gradients, a direct MSE comparison might not be the most accurate approach to assess their relative reliability. A more meaningful comparison would be to evaluate the impact of each on the quality of the generated image.

### Questions
1. In the Stable diffusion experiment, why was the proposed methodology not applied to DPM-Solver? If the results were presented in the paper, please provide a reference.
2. In Equation 14, is it correct to plug the $n$ points obtained from the $\Delta t$ interval ODE solver into the $2\Delta t$ interval ODE solver? Do I understand it correctly?
3. Are the MSE scales of the future gradient and the springboard directly comparable? Would the author(s) think that using the MSE of the image updated with the future gradient instead of the future gradient in Figure 2(b) provides a more meaningful comparison?
4. Is the mention of Nesterov momentum solely due to the similarity in form between the proposed springboard prediction method and Nesterov momentum? Have any properties of Nesterov momentum, such as improved convergence speed, been leveraged in the theoretical analysis or practical implementation of the proposed method?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The PFDiff paper introduces a novel, training-free, and orthogonal timestep-skipping mechanism to improve existing ODE solvers used in Diffusion Probabilistic Models. The proposed approach helps to reach solutions with fewer NFE, with the aid of springboard along with foresight updates. This addresses a significant challenge in reducing computational cost while keeping high sample quality. Furthermore,  PFDiff improves the efficiency and quality of diffusion model samplig.

### Strengths
1). The paper is well written and easy to understand

2). The given illustrations, and provided Algorithms further helps understanding the paper.

3). The paper identifies a limitation of DPMs, which is their sampling efficiency is low as they often require multiple number of denoising steps. Existing methods tend to amplify discretization errors when NFE is below 10, often leading to convergence issues. The proposed approach, named PFDiff, is a training-free and orthogonal timestep-skipping algorithm that helps mitigating these errors while operating with fewer NFEs

4). PFDiff employed the potential for improvements in existing training free accelerated methods, and the sequence of observations that led to the development of PFDiff is remarkable. 

5). The proposed sampler can be integrated to any order of ODE solvers regardless of the type.

### Weaknesses
I believe this is a good paper as it provide valuable insights while providing solid reasoning, but I have some questions regarding the scalability, as well as about k and h values of the proposed method.

1). I would like to know how will PFDiff maintain quality across different types of diffusion models other than those mentioned in paper?

2). As the algorithm's construction is based on gradients, I would like to know what happens if gradients show a dispersion. How this kind of a scenario is handled? Also is there a possibility of accumulating errors in the proposed approach?

3). A more ablation on the parameters k and h will further enhance the paper. For instance, is it possible to further increase the value of k? At that kind of instance, how would PFDiff work?

### Questions
Please see the weaknesses section.

### Soundness
4

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
4

### Summary
This paper introduces a sampling method to accelerate the first-order ODE solvers by utilizing the past gradient ($\epsilon$) and future gradient, leading to FID improvements in the NFE regime between 4 and 20. Also, the authors accelerate the higher-order ODE solver by using the past gradients. Empirical results show that the sampling method works well for continuous and discrete diffusion models under unconditional and conditional settings.

### Strengths
1. Unlike other generic ODE solvers (e.g., Heun 2nd-order solver, DPM-solver), this paper proposes the reuse of the network output from previous time steps to accelerate the sampling based on the observation of the output similarity between two consecutive time steps.
2. Experiments on various diffusion models (continuous, discrete, conditional, unconditional) verify that PFdiff-1 outperforms other ODE solvers in the low NFE regime (4-20)

### Weaknesses
1. The proposed method lacks theoretical support and is mainly motivated by the output similarity observation shown in Figure 2a. How reliable is this similarity? How much does this observation vary in different diffusion frameworks? Please provide more details of experiments in Figures 2a and 2b, you can put the details in into appendix. I suggest the authors explore the connection between the sampling trajectory and the proposed sampling method. I think the curvature of the trajectory can explain the reuse of the gradient and your methods. Refer to [1] and [2] for details of trajectory shape.

2. the overall writing is problematic and significantly affects the readability of this paper. I list some below:
- the definition of Q is not clear, in line 222, plug in n=0 does not give $x_{t_{i-1}}$. Please rethink the expression of Q since it is used throughout the paper.
- if the proposal of using future gradients is based on Proposition 3.1, why not put the proposition at the beginning of section 3.3?
- function s() is not defined in eq 7 and eq 8
- function h() is not defined in eq 9
- line 348, notations l and h are undefined
- In Figure 2b, treating the samples derived from 1000NFE as the ground truth is not rigorous.

3. The authors claim that PFDiff is effective and orthogonal to existing ODE solvers, please provide the FID results of PFDiff in the regime NFE>20 to support the claim.

4. in Figure 4, some FID results of PFDiff are missing (NFE=4 and NFE>12). In Figure 5, some FID results of PFDiff are missing (NFE>10)

5. in Figure 4b, why PFDiff is worse than the baseline Analytic-DDIM when NFE=6? A similar outlier in Figure 4a

6. in Figure 5, the results of DPM-solver+PFDiff are missing.  

7. I encourage the authors to also compare the FID of PFDiff with [2]


others:
1. line 52, the last two papers are published in 2023, not 2024, please cite papers correctly
2. I suggest the authors move Figure 1 to the appendix to leave space for the main content.

### Questions
have the authors also tried adding the future gradient step to higher-order ODE solvers?

### Soundness
3

### Presentation
2

### Contribution
3
