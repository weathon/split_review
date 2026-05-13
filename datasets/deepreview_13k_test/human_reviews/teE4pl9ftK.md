# Gradient-Free Generation for Hard-Constrained Systems

- Decision: Accept
- Scores: 6, 6, 5, 5, 5

## Abstract
Generative models that satisfy hard constraints are crucial in scientific applications, e.g., numerical simulations, dynamical systems, and supply chain optimization, where physical laws or system requirements must be strictly respected. However, many existing constrained generative models, especially those developed for computer vision, rely heavily on gradient information, which is often sparse or computationally expensive in other fields, e.g., partial differential equations (PDEs). Accurately solving these problems numerically demands the generated solutions to comply with strict physical constraints, e.g., conservation laws. In this work, we introduce a novel framework for adapting pre-trained, unconstrained generative models to exactly satisfy constraints in a zero-shot manner, without requiring expensive gradient computations or fine-tuning. Our framework, ECI sampling, alternates between extrapolation (E), correction (C), and interpolation (I) stages during each iterative sampling step to ensure accurate integration of constraint information while preserving the validity of the generated outputs. We demonstrate the efficacy of our approach across various PDE systems, showing that ECI-guided generation strictly adheres to physical constraints and accurately captures complex distribution shifts induced by these constraints. Empirical results show that our framework consistently outperforms baseline approaches in both zero-shot constrained generative and regression tasks, and achieves competitive results without additional fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, the authors propose ECI for gradient-free generation for constraint systems. ECI is zero-shot and doesn't need tuning the model. It works through alternating between extrapolation (E), correction (C), and interpolation (I) in each sample step. The empirical results show the model achieves competitive performance across various PDE systems compared with baseline models.

### Strengths
1. The work is well-motivated, it's important in scientific applications to have constraint generation
2. The proposed method is effective and does have constrained generation. Also, the method is zero-shot which is a big benefit for constraint sampling method. Although it's based on functional FM not FM in general
3. The experimental results show advantages over other baseline models.

### Weaknesses
1. The writing is also a bit confusing. Actually comments from reviewer KM5e help me better understand the algorithm 2. 
2. The authors are recommended to better formulate the contribution of this work. In particular, the model works in functional space and applies projection to constraint spaces to guarantee hard-constraint met. 
3. The authors mention supply chain optimization in abstract and introduction as a hard-constrained system. However, it lacks experiments on such problems. It would be better to showcase some applications beyond PDE learning (which I believe is broad).

### Questions
1. How does proposed ECI compared with FFM without ECI in experiments? It would better show the improvement from ECI in sampling. 
2. In section 3.3, the authors mention resampling noise during sampling. Can the authors explain why this helps better generative results?
3. The model assumes a perfectly trained FFM, however there is inevitable error in the trained generative model. How does such error affect the performance? Will such error break the constraint in sampling?
4. Empirical results are on low-resolution problems. Can the authors comment on how ECI work at larger scale?

### Soundness
3

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
The paper introduces ECI sampling, a framework that adapts pre-trained, unconstrained generative models to exactly satisfy hard constraints in a zero-shot manner without requiring gradient computations or fine-tuning. This framework alternates between extrapolation, correction, and interpolation stages during each iterative sampling step to integrate constraint information while preserving the validity of generated outputs. Empirical results demonstrate that ECI sampling strictly adheres to physical constraints across various PDE systems and outperforms baseline approaches in zero-shot constrained generative and regression tasks.

### Strengths
1. The paper is easy to follow with high readability. The problem setting is well motivated and important.
2. The paper provides quite comphrenseive numerical results with comparison to relevant benchmarks. The extension to regression setting is also quite impressive.
3. The paper also provides a quite detailed ablation study on the choice of algorithm hyperparameters.

### Weaknesses
*1. Clarification of Problem Setup*

The problem setup is not sufficiently explained, which may lead to confusion. Although the authors repeatedly emphasize that ECI is intended for the generative modeling of constrained PDE solutions, it remains unclear what distribution of constrained solutions ECI aims to recover. Specifically, is it targeting a uniform distribution over the space of constrained solutions $\mathcal{U}_{|\mathcal{G}}$? The authors should invest more effort in formally clarifying the problem setup.

*2. Discussion of ECI’s Advantages and Comparisons*

The paper appears to lack a section that discusses the benefits and potential sources of ECI’s superior performance, as well as comparisons with other existing approaches mentioned in the work. Including such a discussion would help readers better understand both the relevant literature and the proposed method.

*3.Validation of PDE System Satisfaction*

While ECI ensures the exact satisfaction of the constrained operator by applying a correction operator after each one-step extrapolation, it is unclear why the solution obtained at time 0 still satisfies the PDE system $\mathcal{F}_{\phi} u(x) = 0$. In Algorithm 2, the next-step solution is generated by forward noising starting from the predicted solution at time 1. Does this noising process preserve the satisfaction of the PDE system? Additionally, is the linear interpolation of two PDE solutions a valid PDE solution, implying that the PDE system is linear? Further explanations are needed to clarify these points.

*4.Missing References on Gradient-Free Guidance*

Some references on gradient-free guidance are missing, such as [1] and [2]. It appears that the proposed method is related to [2], involving functional FM and additional projection steps. Providing more clarification on these connections would be appreciated.

[1]Yujia Huang, Adishree Ghatare, Yuanzhe Liu, Ziniu Hu, Qinsheng Zhang, Chandramouli S Sastry, Siddharth Gururani, Sageev Oore, and Yisong Yue. Symbolic music generation with nondifferentiable rule guided diffusion. arXiv preprint arXiv:2402.14285, 2024.

[2]Chung, Hyungjin, et al. "Diffusion posterior sampling for general noisy inverse problems." arXiv preprint arXiv:2209.14687 (2022).

### Questions
1. This is the most critical question. How does ECI guarantee that the achieved solution satisfies the PDE system? In computer vision tasks where differences from ground truth images are permissible.  In this work, boundary conditions are guaranteed, but how does ECI ensure that the generated data truly represents solutions to the PDE? More specifically, why the linear interpolation between two PDE solutions is still a valid PDE solution?

2. Can you elaborate more on the stochasticity of generated solutions, as is discussed in Sec 3.3. Does more stocahsticity mean the generated distribution is distribution-wise closer to the uniform distribution over the space of constrained PDE solutions?
3. For the extrapolation step, will the algorithm performance be better if more a refined scheme is used? For example, mutiple step extrapolation when time $t$ is far from $1$ and one step when $t$ is close to $1$. From my understanding, the quality of predicted $\hat u_1$ is crucial to the algorithm performance. An additional ablation study could be performed here.
4. Can you comment on the computational efficiency of ECI compared with existing approaches?

The current score assumes a positive answer to the first question. My score will be adjusted accordingly based on the authors' response.

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
4

### Summary
This paper tackles the problem of conditional generation of physical systems with physical constraints (such as physical conservation laws). They propose “a framework for adapting pretrained zero-shot, unconstrainted generative models to satisfy exacts constraints” in a computationally efficient manner. Subsequently, the apply the framework to Partial Differential Equation (PDE) systems and demonstrate empirical results on a variety of 1D and 2D physical problems.

### Strengths
* The method does seem to operate as advertised. The generated results have 0 constraint error, compared to > 0 constraint error of other soft-constrained methods. At the very least, the claim that ECI guarantees hard-constraint satisfaction is well supported
* The ablation study that shows the effect of the resampling intervals and the mixing iterations is quite good.
* Reporting both generation quality as well as runtime for various experiments helps objectively evaluate the proposed methodology.
* Overall, the presentation of the paper if quite good. The problem statement and context are very clearly outlined at the start of the paper. The advantages of the methodology are plain described, and the research problem is clearly state and motivated within existing literature. Thorough and well written description of experiments and results. Nice figures though could benefit from more detailed captions describing what we are looking at.

### Weaknesses
__Theoretical Concerns__
* While the authors do a great job of citing the existing context for SciML applications and flow-matching models, they do not cite the large existing bodies of work related to constraint satisfaction/constrained optimization. In particular, many methods share many similarities with ECI in that they perform unconditional update steps, and then project back into the feasibility region. As such, the method lacks theoretical motivation and context of existing works.

__Experimental Concerns__
* Many of the experiments performed are quite simple, with either low spatial resolution, low dimensionality, or a small number of time-steps. In order to validate that the correction step is not overly destructive, it would be beneficial to perform experiments with higher resolution, and a greater number of time steps. Additionally, there is a concern that ECI performs poorly in complex settings, as it is out-performed by one model or another on all 2D experiments (in terms of MMSE), and thus it would be good to see a 3D fluid setting to evaluate how ECI performs in higher-dimension problems.
* Additionally, fluid flow can exhibit quite complex behaviour. It is not clear why an increased variance in the solutions is a sign of a bad solution, as opposed to the system exhibiting complex dynamics (such as turbulence). Thus, the justification for SMSE as an evaluation metric is not quite clear.

__Contribution Concerns__
* First, the concept of perform Extrapolate-Correct-Interpolate steps in order to solve constraint satisfaction is not a novel idea. In fact, and is well studied in constraint satisfaction settings. For example, projected gradient descent functions very similarly by first taking a step to minimize the objective (Extrapolate) and then taking a step to project back into the feasible region (Correct).
* Second, as mentioned in the paper, the extrapolate step assumes a pre-trained generative model (and thus is not a novel contribution), the interpolate step simply adds noise to the sample (and thus no novel contribution contribution), so the only real contribution is the correction step. However, the correction step is extremely trivial. In the case of the boundary conditions, the method simply sets the boundary values to the desired constraint. In the case of conservation, the method subtracts the deviation from the conserved amount from all cells equally. Both approaches are extremely simple, and don’t really capture realistic physics. We can construct pathological examples where this type of correction leads to systems which satisfy the constraints but are completely implausible and useless for any sort of SciML application. In fact, this correction step is more or less the most trivial way to project back into the feasibility region.
* Furthermore, to address new problems, you need to implement your own correction steps, which may be difficult, computationally intensive or simply intractable for more interesting problems. For example, there is no treatment for conservation of a vector quantity (i.e. momentum, angular momentum), which would occur in many settings of interest.
* Additionally, the paper deals with a pretty niche problem. Notably hard-constrained generation using flow-matching models for physical system simulation. However, when digging into the ECI framework, we note that the E and I steps come from pre-existing generative models, and the C step is incredibly simple. Thus, the overall contribution is very limited in scope of application, as being quite simple from a theoretical and practical point of view.
* Overall, given a pre-trained flow matching model, ECI is a somewhat simple extension that allows for hard constraints to be satisfied. This is guaranteed by the correction step, which is quite simplistic. In particular, we would expect that such coase correction steps would lead to poor solution quality. In fact, from the experimental results, we can see that ECI performs well in 1D settings, but under performs compared to other models in the more complex 2D problems. In fact, we would expect it to perform even worse with high spatio-temporal resolution or in 3-dimensional problems.


Overall, the paper is very well written and presented, but the ECI framework (in particular the correction step) do not present a significant theoretical or practical contribution.

### Questions
* Is it possible to address the conservation laws in a more principled way? For example, minimal local perturbations to achieve the desired conservation (rather than a global correction), or monitoring which cells are causing the violation and thus correct the violations in a more targeted manner?
* Can we apply ECI to a 3D problem/higher resolution/more complex problem to see if the correction step is much worse? It would also be good to see an experiment at a much higher resolution and with many more time-steps.
* Why are we using Frechet Poseidon Distance? For these problems, we know the physics and so would it not be better to simply compute the ground truth for evaluation?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes an ECI sampling framework that strictly satisfies hard constraints such as IC/BCs and conservation laws through extrapolation, correction, and interpolation stages. The method has gradient-free generation and zero-shot inference for parametric PDE and dynamical systems.

### Strengths
1. There are many experimental results, sufficient comparison with baselines, and complete test metrics.
2. The analysis presented in line 260 is basically confirmed by experiments: when the physical constraints are strong or contain a lot of information, the generation variance is small, and conversely the variance is large.
3. Compared with Boundary enforcing Operator Network (BOON), this work implements hard constraints more concisely. The ECI sampling framework satisfy physical laws and system requirements strictly.

### Weaknesses
1. Although the results in Table 3 is excellent, Figures 6-8 may not clearly reflect the advantages of ECI sampling, and further explanation of the figures and settings is needed.
2. This method can achieve zero-shot performance and exact satisfaction of different IC/BCs. However, Figures 5-7 are shown with IC or BC fixed. It is necessary to supplement the visualization of final predictions under different ICs. For the Stokes problem in Appendix B.1, we recommend testing more k and w values to demonstrate the generalization and applicability of ECI sampling.
3. There is a lack of an overall framework diagram, and the entire training and generating process is not clear or intuitive enough. The PDE problems considered in the experiment are limited to 2-3 dimensions. And those experimental descriptions, data formats and prediction tasks should have a clearer and unified presentation.

### Questions
For pre-trained operator networks, fusing BC/ICs to enforce hard constraints can indeed improve predictions at initial time and boundaries, but can ECI sampling directly correct or improve the prediction values in the domain? And how effective is this ability under zero-shot inference?
In addition, u_1 in line 2 of Algorithm 4 should be in brackets and needs to be corrected.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce a novel framework for adapting pre-trained, unconstrained
generative models to exactly satisfy constraints of PDEs in a zero-shot manner.
Sampling which alternates between extrapolation (E), correction (C), and interpolation
(I) stages during each iterative sampling step to ensure accurate integration of constraint information of PDEs
is proposed 
and called ECI sampling.
The new method is evaluated against various existing approaches and for different PDEs with both value constraints 
(initial and boundary conditions) and conservation conditions.
The topic is interesting, but the paper requires a complete rewriting focusing on the main contribution and towards a sound mathematical notation.

### Strengths
- interesting and relevant research question

- extensive evaluation of the new ECI sampling method versus other zero-shot guidance models for both generative and regression tasks
and experiments on various 1d/2D and one 3D PDE;
however I am not an expert in all these PDE learning methods

### Weaknesses
The writing of the paper is  unsatisfactory, everything boils down to Alg. 2 together with the
beginning of p. 5 (Extrapolation, Correction, Interpolation), 
but the authors 
try to explain something in a non understandable, fuzzy way.
In particular, often the notation is not introduced when it is needed.
For example in formula (2) it is not clear how $q$ is defined.

 The paper could be considerable shortened or better some parts from the appendix could be moved to the main part
to make the methods better understandable.\\
Prop 1 is straightforward and holds just by construction; it could go into the main part 

 Alg. 2  is obscured by notational
overload. Basically what is happening in Algorithm 2, line 6 is the
following:

- drawing $u_1\sim p_\theta(u_1|u_t^{m-1})$ amounts to computing
$$u_1=u_t^{m-1}+ (1-t)v_{t,\theta}(u_t^{m-1})$$ In particular
$p_\theta(u_1|u_t^{m-1})$ is a delta measure resulting from the one step
application of the vector field.
- then compute $\hat{u}_1:=C(u_1,\mathcal{G})$ in order to project to
a function $\hat{u}_1$ that satisfies the constraints

- sample from $q(u_t^m|\hat{u}_1)$ by sampling from $u_0\sim\mu_0$ and
calculating $u_t^m=(1-t)u_0+t\hat{u}_1$. This means that one assumes that
$q(u_t^m|\hat{u}_1)$ is distributed as $(1-t)U_0+ \hat{u}_1$ where
$U_0\sim \mu_0$.

In line 7 the only difference is that in the last step one computes
$u_{t+1\backslash N}=(1-(t+1\backslash N))u_0+(t+1\backslash N)\hat{u}_1$.

### Questions
Minor remarks:

- p. 3: PDE family is $\mathcal F_\phi$, but then $\mathcal U_{|\mathcal F}$ without $\phi$ 
(skip the $x$ in $u(x)$ in definition of $\mathcal U$ since you mean the function and not the function value);
the family could be $\mathcal F:=\{\mathcal F_\phi: \phi \in \Phi\}$

- in the definition of $\mathcal U_{|\mathcal G}$ I am missing the domain of $x$ in $\mathcal F_\phi u(x) = 0$

- what is the reason for the clumsy notation, why not calling it just $\mathcal U_{\mathcal G}$ and $\mathcal U_{\mathcal F}$

- there are errors in English, e.g. and of p. 3 ''denote'' instead of ''denotes''

- when the authors use $:=$ (push-forward measure) and when not (most of all other definitions)

- formula (2) is not readable since $q$ is not defined here; later the authors try to explain the formula

- put important formulas on an extra line

- While Alg 1 is superfluous, how Alg 3 and 4 are embedded in Alg 2

### Soundness
2

### Presentation
1

### Contribution
2
