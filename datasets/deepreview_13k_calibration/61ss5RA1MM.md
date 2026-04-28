# Training Free Guided Flow-Matching with Optimal Control

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Controlled generation with pre-trained Diffusion and Flow Matching models has vast applications. One strategy for guiding ODE-based generative models is through optimizing a target loss $R(x_1)$ while staying close to the prior distribution. Along this line, some recent work showed the effectiveness of guiding flow model by differentiating through its ODE sampling process. Despite the superior performance, the theoretical understanding of this line of methods is still preliminary, leaving space for algorithm improvement. Moreover, existing methods predominately focus on Euclidean data manifold, and there is a compelling need for guided flow methods on complex geometries such as SO(3), which prevails in high-stake scientific applications like protein design. We present OC-Flow, a general and theoretically grounded training-free framework for guided flow matching using optimal control. Building upon advances in optimal control theory, we develop effective and practical algorithms for solving optimal control in guided ODE-based generation and provide a systematic theoretical analysis of the convergence guarantee in both Euclidean and SO(3). We show that existing backprop-through-ODE methods can be interpreted as special cases of Euclidean OC-Flow. OC-Flow achieved superior performance in extensive experiments on text-guided image manipulation, conditional molecule generation, and all-atom peptide design.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a new framework for controlled generation using pre-trained diffusion and flow matching models, dubbed OC-Flow. The method is based on sound theory in optimal control that offers additional convergence guarantees in Proposition 1 and Theorem 2 (under two key assumptions of affince Gaussian path and Lipschitz continuity of the gradient of guided loss). Several benchmarks on guided-image manipulation, molecular generation and protein design with generative models are performed to demonstrate the effectiveness of the method.

### Strengths
- Well-motivated problem, overall nicely written paper with clear literature review.
- The methodological and theoretical parts of the paper are well-sounded. 
- Providing a framework that has convergence analysis is always welcomed.

### Weaknesses
 **Major: questionable and inconsistent baselines' results in empirical benchmarks** 

- While on the first task (section 5.1 text-guided image manipulation) the authors have report/insert exactly other baselines' results (originally in Table 2 of the FlowGrad paper); the results on two remaining tasks in section 5.2 (molecule generation) and section 5.3 (peptide design) do not match the results reported in their respective original paper. 
- More specifically, the results in Table 3 do not match those of Table 4 in D-Flow paper (Ben-Hamu et al. 2024); results in Table 5 do not match those of Table 1 in PepFlow paper (Li et al. 2024). In fact, if one instead takes into account the original results, the baseline D-Flow actually perform better in MAE metrics compared to OC-Flow in Table 3. For Table 5 the metrics reported are in different scale. 
- I am therefore request the authors to clarify this discrepancies between results reported in their paper and the results reported in the respective original works of compared baselines. Otherwise, I think the practical performance of OC-Flows remains questionable.

Ben-Hamu et al. (2024). D-Flow: Differentiating through Flows for Controlled Generation. Proceedings of the 41 st International Conference on Machine Learning, Vienna, Austria. PMLR 235, 2024.

Li et al. (2024). Full-Atom Peptide Design based on Multi-modal Flow Matching. Proceedings of the 41 st International Conference on Machine Learning, Vienna, Austria. PMLR 235, 2024.

### Questions
See weaknesses.

### Soundness
2

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
2

### Summary
This paper provides a novel approach for guided generation using pre-trained diffusion and flow matching models. Traditional methods of guiding ODE-based generative models often require expensive retraining and work mainly on Euclidean manifolds, but OC-Flow uses an optimal control training-free framework beyond Euclidean spaces to the SO(3) manifold. Experiments on tasks like text-guided image manipulation, conditional molecule generation, and peptide design validate the method’s effectiveness​.

### Strengths
- As far as I know, the approach is original in framing guided flow matching as an optimal control problem. The authors develop a general framework for non-Euclidean geometries with strong theoretical backing, which is fairly rare.
- Another strength of this work is that it is a general approach, i.e. OC-Flow can be used effectively for a variety of applications such as image and molecular data. 
- Unlike existing approaches, OC-Flow allows training-free guidance, making it computationally efficient and more applicable in real-life settings. 
- The SO(3) results such as on improved molecular generation accuracy, validate the importance of using this geometric inductive bias for generative models. 
- Through the framing of existing approaches as special cases under their optimal control formulation, this paper helps clarify the connections between gradient-based techniques like FlowGrad and D-Flow.
- The model consistently demonstrates improvement over previous work.
- I really appreciate the figures included in the paper to illustrate and compare the methods against existing approaches.

### Weaknesses
 - My main question is regarding scalability. While the model performs well on selected benchmarks, to me it is still unclear how OC-Flow scales to high-dimensional datasets such as large molecules. A discussion of potential scalability limits and memory efficiency in such cases would strengthen the paper. Specifically, the computational cost associated with solving the optimal control problem, particularly the repeated evaluation of the vector field and its gradients, needs to be addressed for high-dimensional inputs. The paper should clarify whether the computational complexity scales linearly, quadratically, or worse with the input dimension, and how this impacts practical applicability.
- Moreover, even though the formal contributions are great and well-formalized, to me the paper is still quite hard to read. Since the theoretical results are one of the main contributions, I think it would be valuable to add more intuitive explanations of the proofs and why they are there. For example, theorem one provides a bound based on VFM on KL between the model and a terminal point, but some intuition of why this bound is provided would make the paper more approachable. It would be helpful to explain the practical implications of this bound and how it relates to the performance of the guided model. Furthermore, the connection between the theoretical results and the practical algorithms should be made more explicit.
- Adding to this point, the theoretical assumptions made (e.g. Lipschitz continuity, boundedness) are clear and needed for the argument, but some reflection (perhaps on a high level) on whether these hold in practice would help to interpret the method's advantages. For instance, it would be useful to discuss whether the Lipschitz constant for the vector field encoder is likely to be large or small in typical applications, and how this affects the convergence of the method. Similarly, the boundedness assumption on the reward function and its gradients needs to be justified in the context of the specific applications considered in the paper.
- While the focus is on continuous CNFs, a brief comparison with discrete flow techniques could contextualize OC-Flow's advantages or limitations more clearly, especially as discrete methods have shown promise in similar applications. This comparison should discuss the trade-offs between continuous and discrete approaches in terms of computational cost, sample quality, and the ability to model complex distributions.

### Questions
- The paper shows promising results, but could the authors elaborate on potential ways to enhance scalability, especially when applied to e.g. large molecules or more complex target distributions in general? 
- How does OC-Flow compare to recent works in Riemannian FM? What about SO(3) and SE(3)?
- Could OC-Flow be adapted for hybrid tasks where both Euclidean and Riemannian components are present? This might extend its applicability to even broader fields where you need this hybrid. Does the method allow for this directly or not?
- Since OC-Flow is designed to be computationally efficient, could the authors comment on real-time applications requiring 'immediate' guidance?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper attempts to solve the problem of conditional generation using Flow-Matching models. In particular, they propose a unifying framework (OC-Flow) from which other approaches (such as D-Flow and FlowGrad) can be derived, and operates in Euclidean and SO(3) geometries. Subsequently, the authors provide extensive theoretical analysis of OC-flow to prove convergence and theoretical properties. Finally, the authors apply OC-Flow to text-guided image generation and peptide design tasks.

### Strengths
* The paper has a strong theoretical grounding, is well placed within the existing literature and goes to extensive efforts to prove theoretical properties of the proposed methodology. Additionally, the paper provides significant context and background, referencing existing works in Flow-Matching models. Finally, the authors provide a ton of detailed proofs in the appendix, and theoretical analysis in the main body of the text.
* The paper provides a legitimate contribution to formalizing and extending existing guided-flow matching techniques to complex geometries (such as SO(3))
* The authors compare the proposed methodology to similar existing methods to demonstrate competitive performance
* Table 1 gives a good comparison to understand the contribution of OC-flow vs D-Flow and Flow-Grad

### Weaknesses
 __Theoretical Concerns__
* The main concern with the theoretical aspects of the paper is that the authors perform all the theoretical analysis in the continuous regime, but then implement the practical algorithms in a discrete regime. They even mention this limitation in the conclusion (“we also note that our practical algorithm…”). This presents a potentially significant hole in the paper, as the objects being proved, and the objects being validated empirically are not the same, and thus the theoretical content in the paper is not necessarily applicable to the experimental results (as noted by the author). To address this, we recommend that the authors 1) provide theoretical analysis of the discrete regime of the algorithm, 2) discuss in detail how the continuous approximates or bounds the behavior of the discrete implementation, or 3) implement a continuous version of the algorithm. These additions would help bridge the gap between theory and practice.

__Experimental Concerns__
* There is a significant lack of information regarding the experiments and reproducibility. There are no details as to how these models are trained, what the architectures are, the implementation, etc. This would need to be addressed before the paper could be accepted. To address this, we recommend that the authors give detailed descriptions of the model architectures and hyperparameters, training procedures and optimization details, data preprocessing steps, computational resources used, and code availability or plans for release. This would greatly improve the reproducibility of the work.
* Similarly, no error bars/confidence intervals are reported on any of the experiments. In fact, it is unclear whether their model is better than existing baselines (i.e. in table 5, they claim 0.795 is better than 0.793, but no CI, similarly in tables 2, 3 and 4, they report outperforming existing methods but do not report CI.). Consequently, it is not possible to assess their claims that they outperform existing models, given the lack of confidence intervals and the close proximity of the performance values. To address this, we recommend that the authors 1) run multiple trials and report mean and standard deviation for all metrics, 2) perform appropriate statistical significance tests (e.g. t-tests) when comparing to baselines and 3) include error bars or confidence intervals in all tables and figures.

* Finally, one of the major claims in the paper is that OC-flow can optimize in euclidean and SO(3) space, and that optimization in SO(3) provides benefits in tasks such as protein design. However, the authors do now present results split into Euclidean and SO(3) algorithms. It is unclear how/if the extension to SO(3) is even beneficial, and additional experimental details/results are needed to validate this claim as well. This is brought up by "our OC-Flow method, fully optimized in both Euclidean and SO(3) space" on page 10.

__Presentation Concerns__
* The paper has some issues with the presentation that make it quite difficult to asses which parts are novel contributions, and which parts are existing works that are being used. The authors/paper would benefit greatly from having a clear vision of what they are proposing and why, and subsequently moving large portions of the detailed proofs to the appendix to not muddy understanding with unnecessary detours. For example, what are co-state flow and E-MSA, and why do we care about these constructs? How do these constructs factor into the actual problem of performing guided matching flow generation? Are they purely used for proving convergence analysis? And if so, then it should be framed/explained as such. In fact, the structure of the paper would greatly benefit from having a section which clearly describes the proposed methodology in terms of implementation, and a separate section for the theoretical analysis of the proposed method, since the current structure makes it very difficult to separate the method as-such, from the additional theoretical concepts only necessary for proving convergence.
  * To address these issues, we recommend that the authors clearly delineate novel contributions from existing work, as well as practical details from theoretical proofs. Adding sections such as "contributions", "proposed methodology and implementation", and "theoretical results" would greatly improve the structure of the paper.
  * Additionally, we recommend that the authors provide clearer explanations of key concepts such as co-state flow and E-MSA, as well as highlighting their importance to the key contributions in the paper.
  * Finally, by restructuring the paper to highlight the novel aspects, and moving detailed proofs to the appendix, the overall quality and clarity of the paper would be much improved.
* Furthermore, several significant objects/theorems are introduced with very little explanation. For example, co-state variables are introduced as “shadow prices representing the sensitivity of the optimal value function to changes in the state variables”. But what are shadow prices? How does this analogy help when there is little thought/exposition given to the co-state/Hamiltonian introduced by the PMP? I would like to see a much more principled approach to writing, where each theorem introduced is clearly placed within the larger context of the work, and has a clear purpose in support of theoretical results.
* Similarly, the lack of figures greatly hinders understanding. Additionally, figure 1 does not clearly articulate what it is presenting, and what the various sub-figures and equations represent.

__Contribution Concerns__:
* First of all, due to the presentation it is not clear what the contributions of the paper are, and what is preexisting work being leveraged for proving theoretical properties of the method. However, my understanding is that there are two main contributions of the paper: 1) they formulate conditional generation using flow-matching models as a control problem in equation 2, and 2) given that formulation, the authors demonstrate that OC-Flow is a generalization of D-Flow and Flow-Grad that can be optimized in SO(3), as well as proving various convergence properties.
* In light of this understanding, it seems like the contributions of the paper are limited in scope. First of all, equation 2 seems to be fairly trivial extension of existing Flow-Matching/Continuous Normalizing Flow formulations (see Fjelde et al (2024)). Furthermore, given the lack of definitive experimental results, it is unclear whether this extension provides tangible benefit over existing methods, especially when considering the additional complexity. One of the major proposed benefits of the method is optimization in SO(3), but no ablation studies are given to demonstrate that SO(3) provides additional benefits over simple euclidean optimization.
* Additionally, the experimental reproducibility of the paper is quite poor, with no experimental parameters given, and no experimental source code provided.
*Finally, the scope of the contribution is somewhat niche. In particular, this paper focuses on classifier-guided generation using flow-matching models in SO(3). While useful for certain problems, it likely does not have wide-reaching implications outside of a few target applications.


__Citations__
* Fjelde, T., Mathieu, E., & Dutordoir, V.. (2024). An Introduction to Flow Matching.

### Questions
* I would like to see a comparison of the runtime of OC-flow vs the other methods. While Table 1 suggests that the memory consumption of OC-flow is lower than D-flow and on par with Flow-Grad, I would be concerned that the additional complexity of solving in SO(3) adds significant computational costs.
* I would like to have a better understanding of what parts of the paper are core to the methodology (i.e. actually implementing OC-Flow), versus what parts of the paper are necessary for proving convergence. I would then like to see separate sections/subsections for the proposal, and the subsequent analysis.
* I would like to see a clearer presentation of a conventional flow-matching model, and how the proposed method extends this standard formulation, ideally in the form of before/after equations to get a clear and unambiguous idea of the elements being added/proposed.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a novel method based on optimal control to optimize generations obtained by ODE-based generative models (e.g. flow matching). The paper proposes algorithms for generative models in Euclidean space and in SO(3), generalizes previously existing approaches, and studies the convergence of the proposed method.

### Strengths
The paper tackles the problem of changing the generation process of ODE-based generative models in order to produce samples that maximize a certain reward, while staying close to the original ODE trajectory (through a regularization term). This problem is relevant in multiple domains where additional signals/information are available at inference time. 

To the best of my knowledge, this is the first paper to formalize this guidance and control framework in SO(3), which is a group used by many methods in structural biology.

The approach generalizes existing methods that optimize the trajectory of ODE-samplers (D-Flow, GradFlow), and outperforms them in multiple benchmarks.

### Weaknesses
 **Computational cost.** The method proposed in the paper, as well as its predecessors (D-Flow, GradFlow) all require optimizing the sampling process *for each sample* produced by the generative model. In other words, producing a single sample requires solving an optimization problem, for which computing the loss requires simulating the full ODE. This has a high cost in memory and computation time.

While GradFlow proposed a clever way of reducing the memory cost of this process, which is also adopted in this paper, this optimization process is inherently computationally expensive, significantly increasing the time cost of producing each sample. Previous work used some approaches to try to alleviate this (e.g. FlowGrad uses an adaptive solver to minimize the number of steps used during generation, by setting the step-size as a function of the estimated curvature of the flow at the current point), but simulation is still considerably slower than the baselines without this optimization process. While generation times are not discussed in this work, the D-Flow paper states that producing a single molecule takes around 3 minutes (they use 100 function evals for discretization of the ODE), and for images the time to generate a single output ranges from 4 to 15 minutes depending on the task. While the purpose of these works is not increasing generation efficiency, but generating better samples through guidance and optimization, they exacerbate the main limitation of diffusion models / flow models, which is their slow generation. In the paper I am unable to find generation time for the experiments. Given the method's nature, I think these should be reported and discussed. The lack of these values makes it difficult to assess the practical applicability of the method, especially considering that the optimization process is performed for each sample individually.

I think related to this point, experiments tend to be on the smaller end. Celeba-HQ for images, molecule generation with up to 9 heavy atoms, and peptides, which are short proteins (less than 50 residues). I understand these methods are able to produce better samples given the external guidance, while other approaches are unable to leverage such information, which is quite valuable. Still, I think providing values for computational cost / generation time, and comparing against plain approaches (baselines that do not require tuning) would be good. I would expect the cost of producing one sample is between 10x-100x more than baselines that do not optimize the sampling process (since there are ~20 optimization steps, and some gradient computation too), but happy to be shown otherwise. This does not account for the fact that lower memory requirements by the baselines would allow producing more samples in parallel too.



### Questions
Proposition 1. What is the prior terminal point $x^p$? Is it $x^p_0$ or $x^p_1$ (that is, terminal as in time $t=1$ or $t=0$). If $t=0$ then the joint $p_1(x^p, x_1)$ is a delta distribution (since ODE is deterministic)? If $t=1$ then $x^p$ and $x_1$ are independent (since $x^p$ is generated from random noise independent of $x_1$)?

GradFlow could in principle be used for manifolds too? The control terms would live in the tangent space of the manifold at the current point? They do not propose this in GradFlow so this is not something to compare against, and would even be consider a novelty and addition to the paper. But this work got me wondering if there’s any obvious reason why this would fail?

I’m not sure I completely agree with the paper’s title “Training free…”. I understand training is the same, and that this method can be used for any pre-trained flow model. But it does require solving an optimization problem, albeit with few iterations (~20) but expensive ones. The difference is that this optimization happens at inference time.

### Soundness
3

### Presentation
3

### Contribution
2
