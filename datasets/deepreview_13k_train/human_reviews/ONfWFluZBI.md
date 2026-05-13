# Self-supervised contrastive learning performs non-linear system identification

- Decision: Accept
- Scores: 6, 6, 6, 6, 8

## Abstract
Self-supervised learning (SSL) approaches have brought tremendous success across many tasks and domains. It has been argued that these successes can be attributed to a link between SSL and identifiable representation learning: Temporal structure and auxiliary variables ensure that latent representations are related to the true underlying generative factors of the data. Here, we deepen this connection and show that SSL can perform system identification in latent space. We propose \textsc{DynCL}, a framework to uncover linear, switching linear and non-linear dynamics under a non-linear observation model, give theoretical guarantees and validate them empirically

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The main contribution of this paper is to provide identifiability theory for contrastive learning on time-series data with non-linear mixing, in the same spirit as time-contrastive learning (Hyvärinen & Morioka, 2016) for non-linear ICA. However, the authors discard the independence assumptions typically made in non-linear ICA with respect to the latent variables, and instead define a dynamical system as the data generating process. The proof operates under the assumption that the mapping from latent states to observables is injective but not necessarily linear, which is exploited to show that the composition of mixing and de-mixing by the model is an affine transform. As such, the estimated dynamics via contrastive estimation identify the true dynamics up to affine transformation in the latent space. There are experiments that corroborate the validity of this approach.

### Strengths
Applying contrastive learning to recover latent dynamics is itself a relatively new approach and the paper is well organised. The proofs use standard jacobian analysis tools and is easy to follow.

### Weaknesses
The paper needs refinement, with minor typos and inadequately captioned figures. While studying the identifiability of time-series contrastive learning might be novel, all the technical tools require carefully controlled assumptions and specific behavior of Jacobians under contrastive loss minimization, which typically do not hold in practice. Specifically, the assumption of injectivity of the mapping from latent states to observables, while crucial for the proofs, is a strong constraint that may not be met in many real-world scenarios. Furthermore, the reliance on the Jacobian's behavior under contrastive loss minimization is concerning, as it is not guaranteed that the optimization process will lead to the desired properties of the Jacobian, such as full rank or non-singularity, which are essential for the identifiability results. The paper also lacks a thorough discussion on the limitations imposed by these assumptions, and how they might affect the practical applicability of the proposed method. The experimental section, while showing some promising results, does not fully address these concerns, and more extensive evaluations on diverse datasets are needed to validate the robustness of the approach.

### Questions
None

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores the use of self-supervised contrastive learning for dynamic system identification. It connects self-supervised learning (SSL) with identifiable representation learning, showing that SSL can identify system dynamics in latent space. The authors propose a model to uncover linear, switching linear, and non-linear dynamics under a non-linear observation model, providing theoretical guarantees and empirical validation.

### Strengths
1. The connection between contrastive learning and dynamic system identification is novel and could lead to simple encoder-only implementations favored in practice.
2. The synthetic experiments, especially the ablation studies, are extensive and investigate many aspects of the theoretical results.

### Weaknesses
In my opinion, the paper leaves quite a few critical questions unanswered, and in general suffers from a lack of polish. In its current state, I cannot recommend the paper for acceptance. The main weaknesses in my eyes are the following:

The paper claims to perform latent nonlinear system identification. This is a key desideratum in various fields such as reinforcement learning and continuous control, and thus has a rich history and literature. However, the assumptions in this paper--and notably how these inductive biases propagate to the algorithm design--severely restrict the applicability of the method without further evidence. Notably, a design assumption in this paper is that the observer function (i.e."mixing function") is invertible. This is a very strong assumption in the context of *non-linear system identification*, where even the foundational theory of linear system identification does not presume: in the Linear-Quadratic Gaussian (LQG) model, where the underlying state evolves linearly $x_{t+1} = Ax_t + Bu_t + w_t$, and observations are a linear function of state $y_t = Cx_t + v_t$ (ignoring the control input term for simplicity), the classical set-up has $d_y < d_x$, such that the observations are per-timestep a low-dimensional measurement of the underlying state. This immediately rules out the mixing function $g(x) = Cx$ being invertible, and this is precisely the motivation for notions such as observability/detectability. Partial observability presents the key challenge in non-linear sysID or reinforcement learning. In particular, it is well-known in controls and RL that ignoring partial observability and imposing a Markovian model (which this paper does implicitly by enforcing the state estimate as a function solely of the current observation) can lead to very undesirable outcomes. In the contrastive learning literature, partial observability is usually not a central issue, often because it is irrelevant for the motivating application (e.g. in computer vision), but one must address this problem for time-series data. In fact, the cited Time-Contrastive Learning method [1], despite making the same assumption in theory, actually propose a method that is more amenable to partial observability, since they predict categorical labels to *chunks* of observed data.

Regarding the polish of the paper, there are various typos and lacking definitions that make the paper hard to parse at times. The minor ones that I have caught are listed below. A particularly confusing point is the role of the control input $u_t$. The paper presents the control input as entering the latent dynamics directly. However, it is typically the case that the control input enters the state through a (possibly state-dependent) actuation matrix $\mathbf B(x_t) u_t$. In any case, how the control input enters the dynamics should be dependent on the parameterization of the dynamics, e.g. the affine ambiguity in $\mathbf L$ in the paper, which is not reflected in the authors' method as far as I can tell. Furthermore, it is unclear if the control input is available to the learner (which is usually the case in sysID), or if it is playing the role of stochastic noise, which eq (9) seems to suggest compared to eq (1). In either case, what role is the control input playing here: in the authors' set-up, there is no need to learn the actuation matrix, and the experiments involve learning a low-noise, nearly deterministic Lorenz system, which rules out some persistency of excitation effect [2].

**Minor comments/typos:**

Figure 1: x -> $x$

Page 3: "linear identifiability (...)", missing eqref?

Theorem 1: "bijective dynamics model $\mathbf f$", should probably mathematically define what that means.

Theorem 1: $\lambda$ is not defined in the main paper, only in the appendix.

Corollary 1: "$\hat{\mathbf f} :=1$", seems to be bad notation.

Beginning of Sec 4: "non-lineary" -> "non-linearly"

Equation (7): where is $g_k$ defined? Possible hash collision with mixing function notation.

Table 1: should probably introduce acronym "LDS" = Linear Dynamical System somewhere

Table 1: What does LDS$\downarrow$ mean?

Table 1: What do $\mathbf L$, $\mathbf L'$, $(\checkmark)$, $\mathbf I$ in the theory column indicate?

Between (11) and (12): "tailor" -> "Taylor"

Before Sec 5: "matices" -> "matrices"

Implementation paragraph: possibly missing number of A100 cards?

Eq (23): where is $p_u$ defined?

Eq (25): what does $p_{D}(y)$ denote precisely?

After Eq (50): "which is probably still fine because $\exp(-\|\mathbf L \cdot \|^2)$ is a valid kernel function (?)". This probably needs to be formalized/reworded.

### Questions
See the weaknesses section.

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
In this paper, the authors propose a system-identification scheme for non-linear observations of non-linear time series data. In particular, they propose a modified contrastive learning set-up that posits linear latent dynamics. Compared to prior works in (time) contrastive learning, this directly enforces a notion of sequential temporal consistency, and seems to provide some benefit in system identification settings. Some supporting theory is provided, demonstrating that if the underlying dynamics are linear and invertible, then the proposed method asymptotically recovers the true dynamics up to affine ambiguity. For general non-linear systems, a (soft) switched-linear system heuristic is proposed, where Jacobian linearizations are applied at user-provided reference points.

### Strengths
Automatic identification of latent variables or dynamics is of critical importance in modern machine / reinforcement learning. The method the authors propose follows a line of self-supervised methods in contrastive learning. In comparison to its closest relative in time-contrastive learning (Hyvarinen and Morioka, 2016), the proposed method is seemingly more well-fit for fitting non-linear time-series data by fitting a latent time-series, rather than predicting a categorical label as in the aforementioned paper.

Since a main inductive bias built into the base method is that the latent dynamics are linear, the proposed method of iterative Jacobian linearizations is a sensible adaptation, and seems to benefit performance significantly.

Numerically, the proposed method appears to make contrastive methods more robustly performant.

### Weaknesses
 - Notations are not clear. For example, in Eq (3), the meanings of $x, x', x''$ should be mentioned in advance. Specifically, it's unclear if these represent different time steps, different samples, or some other distinction. The lack of clarity makes it difficult to fully grasp the equation's implications.
- In theorem (1) and its proof, the assumption is not aligned with Equation (1-2), where all noise disappears. The theorem seems to assume the existence of noise for identifiability, yet the model equations presented do not explicitly include any noise terms. This discrepancy needs to be addressed with a more detailed discussion of how the theorem's assumptions relate to the model's formulation. It is crucial to clarify whether the noise is implicitly present or if the theorem applies under a specific noise model not explicitly stated.
- The difference in the theorem part should be compared with previous works on CL more detailed, since it is a work focusing on theorem. Making the difference more clear will make it more readable. The current discussion lacks a thorough comparison of the theoretical contributions against existing theoretical results in contrastive learning. A more detailed analysis of how this theorem advances the theoretical understanding of CL, beyond what is already known, is needed.
- In experiment parts
    - Baselines like TCL should be compared. The absence of a comparison with established baselines like TCL makes it difficult to assess the performance of the proposed DynCL model in the context of existing methods. The experimental results would be more convincing if they included a comparison with TCL and other relevant baselines.
    - By identifiability, some metrics like MCC should be compared even though they are not component-wise identifiable. While component-wise identifiability might not be achievable, metrics like MCC can still provide insights into the quality of the learned representations. Including such metrics would offer a more complete evaluation of the model's performance.
- Lots of typos:
    - line 133 (supp figure), line 145 (...), seems unfinished part
    - line 250: tailor -> talyor
    - line 637: Theorem 2 -> Theorem A1
    - footnote of page 13: broken reference  
    - line 659, 665: missing reference

### Questions
My main questions can be summarized as follows:

1. What is the marginal utility of this method rather than various other latent nonlinear dynamics estimation methods, e.g. (Watter et al., 2015) (which in fact also imposes locally linear latent dynamics), which do not make strong assumptions on identifiability?

2. How does enforcing the identifiability/invertibility conditions in this paper affect the method's performance in partially observed settings? This could be as simple as the LQG setting detailed above. Does this strong inductive bias translate to large errors when it is not satisfied (which is typically the case when only provided with observations of a ground-truth belief/latent state)?

3. As detailed above, what is the role of the control input? What is the effective difference of the proposed setting and an autonomous (latent) dynamical system $x_{t+1} = f(x_t) + \epsilon_t$?

4. From a practical perspective, how are the reference points for computing first-order linear approximation in the switching case chosen? Also, do these need to be recomputed per iteration, since the parameterization of $\hat{\mathbf{f}}$ changes per iteration? 

**References:**

Watter et al., "Embed to Control: A Locally Linear Latent Dynamics Model for Control from Raw Images", 2015.

### Soundness
3

### Presentation
3

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
The paper "Self-Supervised Contrastive Learning Performs Non-Linear System Identification" explores contrastive learning (CL) for identifying non-linear temporal representations. It presents proof of the identifiability of latent variables up to a linear transformation, removing the requirement for independent noise. The proposed model, DynCL, is validated using synthetic data to support the theoretical findings. Additionally, the authors introduce a model called delta-SLDS, designed to capture switching between linear and non-linear dynamic systems.

### Strengths
- The theorem is both interesting and novel, demonstrating that the learned latent variables can be identifiable up to linear transformations even in the absence of independent noise, provided that some other assumptions are met.
- This theorem provides valuable insights into the mechanisms underlying contrastive self-supervised learning methods.
- A lot of ablation studies and visualization experiments are conducted, which makes the paper more convincing.

### Weaknesses
- Notations are not clear. For example, in Eq (3), the meanings of $x, x', x''$ should be mentioned in advance.
- In theorem (1) and its proof, the assumption is not aligned with Equation (1-2), where all noise disappears. Further discussion is required.
- The difference in theorem part should be compared with previous works on CL more detailed, since it is a work focusing on theorem. Making the difference more clear will make it more readable.
- In experiment parts
    - Baselines like TCL should be compared
    - By identifiability, some metrics like MCC should be compared even though they are not component-wise identifiable.
- Lots of typos:
    - line 133 (supp figure), line 145 (...), seems unfinished part
    - line 250: tailor -> talyor
    - line 637: Theorem 2 -> Theorem A1
    - footnote of page 13: broken reference  
    - line 659, 665: missing reference

### Questions
- It is confusing why it requires 120 GPU days on A100 for these synthetic data. Methods like TCL require only dozens of minutes for one synthetic data. What is the detailed model structure with approximate parameter size?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper focuses on contrastive learning (CL) methods for dynamical systems.
The authors show that under certain assumptions CL performs system identification and can therefore uncover the latent dynamics of the data.
The theoretical findings are applied to switching linear dynamics and non-linear dynamics, and are demonstrated from an empirical point of view using simulated data.

### Strengths
1. Overall this is an interesting paper, that gives an insight on why CL techniques are effective for system identification
2. The introduced CL variant is well presented and theoretically grounded, and could inspire further theoretical research and models
3. DynCL can effectively identify latent states and system dynamics in the experiments on simulated data
4. The authors present a good selection of ablation studies to demonstrate the impact of the different modeling/parametric choices

### Weaknesses
MORE REALISTIC EXPERIMENTS

As stated by the authors in the limitations of this work, the focus of this paper is only on simulated data. While I understand their point of view, and I also agree that the theoretical contribution/simulated experiments are also valuable by themselves, I fear that the impact of this work in this current state will be more limited than it could be if there was a better demonstration of real world applicability.

You could for example try to apply your method to some of the datasets used in "Discovering State Variables Hidden in Experimental Data" (https://www.cs.columbia.edu/~bchen/neural-state-variables/).

If the above is too challenging to achieve, you should at least try to discuss more in detail what each of you theoretical assumptions means in practice, and what you expect to happen if they are not met in real-world experiments. For example, the fact that $p(u_t)$ is a normal distribution seems quite strict in many applications. 

BASELINE

The baseline you use in your experiment seems quite weak, as it does not even use a dynamics model. Have you tried other approaches, for example models doing next-token prediction tasks?




CLARITY

There are several missing definitions/clarifications in the paper that make it a bit harder to follow:
1. N in (3) is not defined
2. "Supp figure" in line 133 is unclear
3. Not sure what "(…)" in line 145 means
4. The name $\nabla$-SLDS is never formally defined
5. In table 1 you have a column called "theory" with different options. What do these option represent exactly?
6. The abbreviation "GT", which I assume stands for ground truth is used in many places but never defined
7. What is $\pi$ in equation (8)?
8. The vMF abbreviation is never defined
9. The DynCL results from Table 1 should be discussed more in depth.

### Questions
1. You use the Gumbel-softmax to approximate the argmin. In my experience, the proper turning of the schedule of its temperature parameter is quite challenging. Is it something you noticed as well?

### Soundness
3

### Presentation
3

### Contribution
3
