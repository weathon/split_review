## Human Reviewer 1

### Summary
The paper introduces a new plug-and-play ADMM framework that integrates score-based denoisers derived from pretrained diffusion models. The contribution lies in two main aspects: (1) addressing the  manifold mismatch between the noise-trained score manifolds and the actual ADMM iterates, particularly due to dual-variable effects and (2) the lack of convergence guarantees when using score-based denoisers within ADMM.

The author propose using a three-stage denoiser called AC–DC (Auto-Correction + Directional Correction + Score Denoising), where in the AC step,  Gaussian noise is added to align iterates with score manifolds, in the DC step  conditional Langevin dynamics is used to refine the direction toward the true data manifold and in the score denoising, pre-trained score model is applied. They provide theoretical results for the cases of convex data-fidelity with weakly contractive denoisers and noncovex case. 

Experiments on image inverse problems (super-resolution, inpainting, motion deblurring) show performance gains over methods like DDRM, DiffPIR, and DPS.

### Strengths
The combination of ADMM with a diffusion-based denoiser that explicitly accounts for manifold mismatch  is conceptually fresh. Previous works used diffusion models in proximal steps or as score priors, but rarely in a primal–dual ADMM context with noise manifold adjustment. 

The authors provide theoretical analysis regarding the convergence of the proposed denoiser. 

The experimental results demonstrate that the proposed denoiser is indeed effective in solving inverse problems. 

The approach tackles a real gap between diffusion-based inference and optimization-based inverse problem solvers.

### Weaknesses
Some of the assumptions are strong. Theorem 2 requires stationarity of the inner Langevin DC step at each iteration and smoothness/coercivity of –log p(x); these are hard to ensure in high-dimensional image spaces. Is there anyway authors could test this on the empirical images or a toy problem?

### Questions
Could the author comment on the computation complexity added by using the AC-DC denoiser as opposed to simply apply the score-based denoiser with adjusting to the noise manifold?

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
## Summary
This paper proposes an AC-DC denoiser within an ADMM plug-and-play (PnP) framework for inverse problems. The denoiser couples an annealed correction (AC) step with a drift-correction (DC) step inspired by score-based diffusion, and the theory aims to show convergence of ADMM-PnP with this denoiser under high-probability weak nonexpansiveness. Theoretical results include: (i) convergence under strong convexity of the fidelity term via a fixed-point argument; (ii) a high-probability weak nonexpansiveness result under a schedule for σ(k) that decays to zero, leading to convergence with fixed ρ; and (iii) a convergence result without convexity of ℓ by adopting an adaptive-ρ scheme (Chan et al., 2016), under boundedness assumptions on the data domain and the score, and an assumption of bounded gradients of ℓ.

### Strengths
## Strengths

1. The paper tackles an important and timely problem: how to safely and provably integrate score-based denoisers within PnP/ADMM. The AC-DC design is intuitive and practically relevant.

2. The high-probability analysis for weak nonexpansiveness is interesting; to my knowledge, there are relatively few works that attempt to rigorously control the stochasticity induced by score-based denoisers within PnP iterations.

3. The boundedness result under adaptive ρ and a vanishing σ(k) schedule is a useful step toward understanding convergence without convexity.

4. The empirical results suggest the method is competitive across a range of inverse problems.

### Weaknesses
## Major concerns

Despite the nice contributions, I have the following major concerns.

### 1 AC-DC denoiser

> Algorithm 1 injects noise inside the AC-DC denoiser. As implemented, Dσ is a stochastic operator: given the same input, it can return different outputs due to the injected noise (both in the AC step and in the DC sampling/evolution).
However, the convergence analysis treats Dσ as a deterministic mapping z → Dσ(z), i.e., a point-to-point operator. This is a mismatch. It seems that the current deterministic analysis does not rigorously cover the algorithm being evaluated experimentally.

### 2. Theorem 1

> 2.1 The proof strategy follows the fixed-point iteration approach of Ryu et al. This requires the fidelity ℓ to be µ-strongly convex. This is violated in many applications highlighted by the paper itself: deblurring, super-resolution, compressed sensing, MRI, and inpainting (e.g., rank-deficient A or non-strongly-convex penalties).

> 2.2 The parameter condition involving ε and µ may be restrictive. In particular, as ε → 1, the factor (1 + ε − 2ε^2) → 0, making the right-hand side ε/(µ(1 + ε − 2ε^2)) blow up. Then the condition 1/ρ > ε/(µ(1 + ε − 2ε^2)) is practically impossible to satisfy. This contradicts with the experimental setup, where Table 3 indicates ρ ≥ 100 in all cases, which violates the small-step requirement in the theorem.

### 3. Theorem 2

> The assumption “the DC step reaches the stationary distribution for each k” is strong. 

### 4. Theorem 3

> 4.1 The analysis follows Chan et al. (2016): boundedness of the denoiser, vanishing noise schedules, and adaptive ρ yield convergence to a fixed point. While this shows stability, it does not characterize the limit point as a solution to any explicit optimization problem. As a result, the algorithm’s fixed point lacks interpretability: it is not known to minimize a well-defined objective nor to satisfy an equilibrium condition like a monotone inclusion. This is a conceptual limitation of the framework that should be acknowledged and discussed more candidly.

> 4.2 The assumption may be strong: The requirement that ||∇ℓ(x)||/√d ≤ R < ∞ for all x is generally false for common inverse problems (deblurring, super-resolution, compressed sensing, MRI, inpainting) unless x is constrained to a compact set. For instance, with ℓ(x) = (1/2σ2)||Ax − y||2, the gradient norm grows with ||x|| unless constrained.


## Overall assessment
This work addresses an important problem and proposes a practically relevant denoiser within PnP/ADMM, with nontrivial theoretical attempts. However, the current theoretical results rely on assumptions that do not match the algorithm as implemented (notably, treating a stochastic denoiser as deterministic and assuming stationarity per iteration), and on conditions that are violated in key applications and in the reported experiments (strong convexity of ℓ; parameter inequalities incompatible with large ρ; bounded gradient assumptions). I believe the paper would be significantly strengthened by a proper stochastic operator analysis and by reconciling the parameter/schedule assumptions with the experimental setup. 

If the authors address some of the issues mentioned above, I would consider to increase my score.

### Questions
Please see the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes a novel Plug-and-Play (PnP) framework that integrates score-based denoisers into the ADMM optimization algorithm for solving inverse problems. The key contribution is a three-stage denoiser, termed AC-DC, designed to address the manifold mismatch problem: the fact that ADMM iterates (influenced by dual variables) do not lie on the noisy data manifolds on which the score functions were trained. The AC (Auto-Correction) stage adds Gaussian noise to the iterate, while the DC (Directional Correction) stage uses conditional Langevin dynamics to refine the iterate towards the correct noisy manifold before final score-based denoising. The authors provide a comprehensive convergence analysis, showing both fixed-point ball convergence under a constant step size and convergence under an adaptive step size schedule. Experiments across various inverse problems demonstrate improved performance over several baselines.

### Strengths
- The paper clearly identifies and addresses a significant, underexplored challenge in the PnP literature: the mismatch between the geometry of optimization iterates (especially in primal-dual methods like ADMM) and the manifolds on which score-based denoisers are trained. This is a pertinent and non-trivial issue.

- The proposed AC-DC denoiser is a novel and intuitive solution to the manifold mismatch problem. The idea of proactively "correcting" the iterate onto the score function's domain, rather than simply applying the denoiser, is innovative.

- The paper validates the method on a wide range of inverse problems (inpainting, deblurring, super-resolution, phase retrieval) and against a diverse set of modern baselines, showing consistent and often superior performance.

### Weaknesses
1. **Questionable Core Assumption**: A central weakness lies in the justification of the DC step. As outlined in the derivation leading to Eq. (10), the method assumes the residual s^(k) follows a Gaussian prior. This assumption appears to contradict the paper's primary motivation—that the noise in the ADMM iterate is not Gaussian and is off-manifold. If s^(k) can be reasonably modeled as Gaussian, the necessity of the complex DC correction is significantly undermined, as a simpler Gaussian denoiser might suffice. The paper lacks a compelling empirical or theoretical justification for this critical assumption.

2. **Lack of Clarity on Method Variants**: The distinction between the two presented variants, "Ours-tweedie" and "Ours-ode," is not clearly explained in the main text. The reader is left to infer the difference from the appendix, which is unsatisfactory. The core methodological description should explicitly state what these variants are.

3. **Insufficient Discussion of Related Work**: The proposed correction mechanism bears a conceptual resemblance to the Onsager correction in Denoising Approximate Message Passing (D-AMP) algorithms [1, 2], which also handles structured iteration noise. Furthermore, the nature of iteration noise in PnP algorithms has been explicitly studied in works like TFPnP [3] (Section 6.2 -- Iteration Noise of PnP Methods). The paper would be significantly strengthened by discussing these connections and clearly delineating how the proposed approach differs from or relates to these ideas.

4. **Inadequate Discussion of Computational Cost**: The AC-DC denoiser, particularly the DC step which involves multiple (J=10) Langevin steps, drastically increases the number of score function evaluations (NFE) per ADMM iteration compared to a standard PnP step. While the appendix includes an NFE analysis, the main text should frankly acknowledge this as a significant limitation and discuss the trade-off between performance and computational efficiency.

Given these issues, my initial rating is Borderline Reject. However, I would be inclined to raise my score if the authors can:
- Provide a convincing rationale for the Gaussian assumption in Equation (10),
- Clarify the differences between "Ours–tweedie" and "Ours–ode,"
- Thoroughly discuss relevant prior work (e.g., D-AMP and TFPnP), and 
- Acknowledge and analyze the computational limitations of the AC-DC denoiser.

### References  
[1] From Denoising to Compressed Sensing, TIT 2016  
[2] Denoising AMP for MRI Reconstruction: BM3D-AMP-MRI, 2018  
[3] TFPnP: Tuning-free Plug-and-Play Proximal Algorithms with Applications to Inverse Imaging Problems, JMLR 2022

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes a new plug-and-play (PnP) ADMM method using score-based priors. Since score networks are trained on noisy manifolds, while ADMM iterates (due to dual variables) may not lie near those manifolds, score-based denoisers perform poorly, and the convergence theory is unclear. To address this, the paper proposes the AC–DC denoiser inside ADMM, consisting of three stages:
AC: add Gaussian noise to push iterates toward score training manifolds;
DC: short Langevin update guided by both the score and a quadratic prior; and
Final denoising via Tweedie score formula. 
Under the strong convexity of the data fidelity term, the paper shows that the ADMM iteration is weakly nonexpansive and converges to a fixed point (up to a $\delta$ ball). Experiments on several inverse problems (inpainting, deblurring, SR, phase retrieval) show improvements over PnP baselines (DiffPIR, DDRM, DPS, RED-diff, DPIR, etc.).

### Strengths
- The paper addresses a real gap: score-based priors in ADMM are harder than proximal-gradient PnP, mainly due to dual variable noise geometry.
- The method conceptually simple: AC noise + short Langevin DC + score denoise.
- The paper extends PnP-ADMM convergence analysis to score models and Langevin steps. 
- Broad experiments across common inverse problems show the practical utility of the method.

### Weaknesses
- Noise addition before score application already appears in recent PnP diffusion works (which the paper also acknowledges). In this respect, the novelty seems incremental. 
- The DC step, a short Langevin refinement combining the score and a quadratic potential, structurally resembles diffusion posterior correction schemes, where noise injection is followed by brief score-based Langevin updates to pull iterates back toward the learned distribution. The paper’s approach integrates this idea into ADMM, but conceptually overlaps with prior noise-add-and-refine mechanisms.
- The AC and DC schedules appear heuristic. The issue of stability is unclear across tasks without tuning.
- Theorem 2 assumes that DC reaches the stationary distribution each iteration, which is unrealistic in practice with only a few Langevin steps.
- With strong convexity of the fidelity term, only convergence to a ball is ensured, not a point. Without strong convexity, an adaptive ADMM penalty schedule is required.
- The experiments use a pre-trained score model, so the advantages are partly dependent on that backbone.
- Many baselines are not ADMM-PnP, so the comparison may be apples-to-oranges from an optimization perspective.

### Questions
- The DC step convergence assumption seems very strong. In practice, you run a few steps; how sensitive is the method to DC iteration count?
- How is $\sigma^{(k)}$ chosen in the AC step? Is there a principled schedule, or is the choice purely empirical?
- Can the method diverge with fixed $\rho$ for non-convex cases? Any empirical failures?
- Can you provide some empirical evidence that dual variables distort score manifold geometry?
- Does AC–DC satisfy a consensus Equilibrium interpretation?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
2