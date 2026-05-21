---
job_id: 270cf8a4-aca5-424d-8363-9650c9299ec6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: BiXwSIIMIq.pdf
paper: Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play Framework
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining generative models, plug-and-play inference, optimization, and convergence analysis for inverse problems.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, method, experiments, quantitative/qualitative results, and conclusion. While I have serious concerns about novelty positioning, mathematical precision, and empirical completeness, these issues do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies how to integrate score-based denoisers into ADMM-based plug-and-play inverse problem solvers. The main proposal is an AC-DC denoiser, a three-stage procedure consisting of additive noise auto-correction, conditional Langevin directional correction, and a final score-based denoising step, together with convergence results framed via weak nonexpansiveness and bounded-denoiser arguments. Experiments on several image inverse problems, including super-resolution, inpainting, deblurring, phase retrieval, and HDR, show improved reconstruction quality over several diffusion-based and PnP baselines.

## Strengths
The paper tackles a real and important problem. Combining score-based priors with ADMM is not entirely straightforward, and the paper articulates a plausible reason, namely that the ADMM pre-denoising variable \(\tilde{\mathbf z}^{(k)}=\mathbf x^{(k+1)}+\mathbf u^{(k)}\) can be geometrically different from the noisy manifolds used for score training. That is a reasonable motivation for designing a denoiser specialized to primal-dual iterations.

The proposed AC-DC denoiser is conceptually easy to understand. The three-stage decomposition in Algorithm 1 is intuitive, and **Figure 1** helps communicate the intended role of each stage. In particular, the contrast between naive direct denoising and the proposed correction-before-denoising pipeline is a useful visual summary of the paper’s main idea. Even though the figure is schematic rather than evidential, it does clarify the advocated mechanism.

The paper does make an effort to go beyond pure empiricism. The convergence section is ambitious and tries to connect score-based denoisers to the ADMM-PnP literature through a weakened residual nonexpansiveness condition in **Assumption 1 / Equation (12)** and the resulting fixed-point-ball convergence statement in **Theorem 1**. Even if I have reservations about some assumptions and derivational details, I appreciate that the paper attempts to state explicit conditions rather than hand-wave “works in practice”.

The empirical section is fairly broad in task coverage. The main quantitative benchmark in **Table 1** spans multiple inverse problems and two datasets, FFHQ and ImageNet. Across many rows, the proposed variants are indeed competitive, often best or second-best on PSNR/SSIM/LPIPS. For example, in super-resolution and imputation, the reported PSNR/SSIM gains over DiffPIR, DDRM, and DPS are not marginal. That breadth is helpful because it suggests the method is not tuned for a single narrow setup.

The paper includes informative qualitative examples. **Figures 2, 3, and 4** show that the proposed method often produces reconstructions that look sharper and more measurement-consistent than some baselines, especially compared with DPS and DiffPIR. While qualitative figures are always selective, these examples are aligned with the claimed benefit of reducing artifacts while preserving semantic realism.

The ablation around the directional correction step is directionally useful. **Figure 5** shows that increasing the number of DC iterations \(J\) improves phase retrieval outputs relative to AC-only (\(J=0\)). This supports the claim that the DC stage is not just decorative engineering, but contributes to the final result.

The appendix also suggests the authors thought about reproducibility: task-specific hyperparameters are listed in **Table 3**, the data fidelity loss is explicitly stated in **Equation (142)**, and code availability is declared.

## Weaknesses
1. **The mathematical presentation is much sloppier than acceptable for a theory-heavy paper, and this directly affects trust in the results.**  
   There are many notation inconsistencies, malformed expressions, and likely typographical/math errors throughout Sections 3 and 4, not just in the appendix. A few examples:
   - In **Equation (9)** on Page 4, the notation is inconsistent and appears corrupted: \(\mathbf z_5^{(k)}\), \(\tilde{\mathbf s}^{(k)}\), \(\hat{\mathbf s}^{(k)}\), and the relation between these objects is unclear.
   - In **Theorem 2**, **Equations (15) and (16)** contain expressions that appear malformed, e.g. \(\sqrt{2} M \sigma_{\mathbf z^{(k)}}^2 / 1 - \sigma_{\mathbf z^{(k)}}^2 M\), \(\sigma_{\sigma^{(k)}}^2\), and \(\log \frac{2}{2}/\nu_k\). As written, these are not mathematically well-defined.
   - In **Theorem 3(a)** on Page 7, the bound for \(c_k\) is visibly corrupted, with terms like \(^{16}\sigma^{2}_{\mathbf x^{(k)}}/{}_{1-M}\sigma^{2}_{\mathbf x^{(k)}}\log{}^{2}/_{\nu_k}\).
   - Similar corruption appears repeatedly in the appendix, for example **Equations (124), (138), (140), (141)**.
   
   This matters because the central claims of the paper are convergence claims. When core theorem statements are syntactically broken, it becomes difficult to verify what has actually been proved and whether the assumptions are sufficient.

2. **Several theoretical assumptions are extremely strong, algorithmically unrealistic, or disconnected from the actual implementation.**  
   The convergence claims in **Theorem 2** and **Theorem 3** rely on assumptions such as:
   - the DC Langevin step “reaches the stationary distribution for each \(k\)”,
   - smoothness and coercivity of \(\log p_{\mathrm{data}}\) in **Assumptions 2 and 3**,
   - bounded support \(D=\mathrm{diam}(\mathcal X)<\infty\) in **Theorem 3**,
   - scheduling conditions involving \(\sigma^{(k)}\) and \(\sigma_{\mathbf z^{(k)}}\) that are not the practical schedules used in the main experiments.
   
   The biggest gap is the stationarity assumption for the DC step. In practice, **Algorithm 1** uses a finite number of DC iterations, specifically \(J=10\) according to the experimental setup on Page 9. That is very far from “reaches the stationary distribution for each \(k\)”. The appendix does include a finite-\(J\) extension, but the main-paper claims and the main-paper theorem statements do not reflect this implementation gap. As a result, the theory does not really cover the algorithm that is experimentally evaluated in the main paper.

3. **The contribution relative to existing score-based PnP methods is somewhat incremental, and the paper does not position itself sharply enough against prior noise-injection / purification / correction schemes.**  
   The manuscript itself cites several closely related lines of work, including DiffPIR, RED-diff, SNORE, diffusion purification, stochastic denoising regularization, and decoupled data consistency. The AC step, as described on Page 4, is already acknowledged by the authors to be related to purification and noise-added denoising. The DC step is then a short conditional Langevin refinement using an approximate Gaussian conditional term. This is a reasonable engineering extension, but the paper overstates the sense in which the manifold mismatch problem is uniquely addressed here.
   
   Put differently, the paper’s core recipe is: add noise, run a few correction steps, then apply the score denoiser. That is not obviously a fundamentally new paradigm compared with recent score-based PnP pipelines that already noise-inject and refine iterates before score evaluation. The paper would be stronger if it gave a much sharper comparative dissection of what exactly AC-DC adds beyond prior correction/purification heuristics, both conceptually and empirically.

4. **The empirical evaluation is broad but not fully convincing because critical controls are missing.**  
   The central scientific claim is that AC-DC specifically fixes manifold mismatch in ADMM. But the main paper does not include the most important direct comparisons needed to validate that story:
   - ADMM + naive Tweedie score denoising without AC or DC,
   - ADMM + AC only,
   - ADMM + DC only,
   - ADMM + alternative correction heuristics from prior work,
   - sensitivity to \(J\), \(\eta^{(k)}\), and \(\sigma_{\mathbf s^{(k)}}\) beyond a single qualitative illustration.
   
   **Figure 5** gives a qualitative ablation over \(J\) on phase retrieval, which is helpful, but it is too narrow. A single figure with a few cherry-picked images is not enough to support the mechanism claim. The appendix’s **Table 5** compares “with correction” vs “without correction”, which is useful, but this is absent from the main paper and still does not separate AC from DC cleanly. Since the paper’s main novelty is the correction pipeline, the main paper should have contained a proper quantitative ablation table isolating each component.

5. **The quantitative table raises fairness and interpretation questions that are not addressed.**  
   **Table 1** is large, but it is also heterogeneous in baseline coverage. Some tasks contain different subsets of baselines, and several rows are labeled in a confusing way: “Imputation”, “Monitor”, “Convergence”, “Improving”, “Phen-1” do not match the task names introduced on Pages 8-9. It is possible to infer that these correspond to inpainting, motion blur, Gaussian deblurring, box inpainting, and phase retrieval, but the mismatch is unnecessary and makes the table harder to audit.
   
   More importantly, there is no reporting of variance or statistical uncertainty in the main table, despite averaging over 100 images. Some margins are meaningful, but some are small enough that without standard deviations or paired significance testing, the “best / second-best” highlighting is less informative than it looks. The paper also does not report runtime, NFEs, or wall-clock comparisons in the main paper, even though the proposed method adds multiple score evaluations per ADMM iteration and solves the \(x\)-subproblem with Adam for up to 1000 iterations. On Page 9 the authors explicitly state this can be computationally heavy. Without cost reporting, “consistently improves solution quality” is incomplete.

6. **The algorithmic specification is underspecified in several places.**  
   The denoiser is central, yet important implementation details are vague:
   - In **Algorithm 1**, the DC update uses a variance term \(\sigma_{\mathbf z^{(k)}}^2\), but the main paper does not cleanly define how this is estimated from iterates. Page 9 later gives \(\sigma_{\mathbf s^{(k)}} = 0.1/\sqrt{\sigma^{(k)}}\), which seems to refer to a different symbol.
   - The text oscillates between \(\sigma_{\mathbf z^{(k)}}\), \(\sigma_{\mathbf x^{(k)}}\), and \(\sigma_{\mathbf s^{(k)}}\), which is more than a cosmetic issue because these parameters govern both the practical correction step and the theorem conditions.
   - The \(x\)-subproblem in **Equation (7a)** is presented as an argmin, but in experiments it is only approximately solved by Adam with an early-stopping heuristic. The convergence analysis treats proximal structure more cleanly than the actual implementation deserves.
   
   These details matter because the proposed method is not a standard black-box denoiser drop-in. Its behavior depends critically on the correction schedule and noise parameters.

7. **The connection between the proved object and the actual learned score model is weak.**  
   The theory is written as if one has access to \(\nabla \log p_t\) or at least a score function satisfying exact smoothness/coercivity properties. But the method actually uses a pretrained score network \(s_\theta\) from a separate paper. Theorems such as **Theorem 2** and **Theorem 3** do not explicitly account for approximation error in \(s_\theta \approx \nabla \log p_t\). This omission is not a minor detail. If the convergence depends on weak nonexpansiveness of the denoiser induced by the score, then score approximation error should appear somewhere in the assumptions or residual constants. As written, the paper effectively proves statements about an idealized denoiser, while experiments use a neural approximation.

8. **Some derivations are not just hard to read, they appear questionable on substance.**  
   For example, the key approximation in **Equation (10)** and the discussion right below it replace the unavailable conditional likelihood term \(\nabla \log p(\mathbf z_{\mathrm{ac}}^{(k)} \mid \mathbf z_{\sigma^{(k)}})\) by a Gaussian quadratic term under a variance-dominance heuristic. This is the heart of the DC step, but the justification is very informal: “under proper scheduling” and “mild regularity conditions” one gets a locally quadratic form. That is a large leap. The practical success may not require a rigorous derivation, but then the paper should present DC more honestly as a heuristic approximation rather than a principled conditional Langevin sampler.
   
   Similarly, in Appendix D, the composition argument leading to **Equation (76)** simply upper-bounds the denoiser residual difference by three times the sum of AC/DC/Tweedie residual differences. This is a coarse inequality, and it is not obvious that it preserves a meaningful \(\epsilon_k<1\) regime under practical parameter choices.

9. **Presentation quality is below the bar for a paper making strong theoretical claims.**  
   Beyond the formula corruption, the writing has frequent grammar issues, naming inconsistencies, and awkward sectioning. Examples include “Theorem 2 (a) establishes that the AD-DC denoiser...”, “the understanding to convergence”, “The AC step gives...” followed by malformed notation, and task names in **Table 1** not matching the text. The references section is also messy, with malformed entries and duplicated citations. This is not fatal by itself, but in aggregate it materially hinders confidence.

10. **The evidence for the motivating “manifold mismatch” story is mostly conceptual, not directly measured.**  
    The method motivation would be much stronger if the paper actually quantified how close ADMM iterates or AC/DC-corrected iterates are to the score training distribution. **Figure 6** in the appendix is only an illustration, and **Figures 7 and 8** validate assumptions about score smoothness/coercivity rather than manifold alignment. What is missing is a direct empirical diagnostic showing that AC or AC-DC reduces some discrepancy between \(\tilde{\mathbf z}^{(k)}\) and noisy data samples at the matched noise level. Right now, the key mechanism is argued, not demonstrated.

## Questions
1. The main theorems assume that the DC stage reaches the stationary distribution for each iteration, while the experiments use only \(J=10\) DC steps. Can the authors clearly explain, in the main-paper setting, why the reported convergence discussion is still informative for the actual implemented algorithm? If possible, please quantify empirically how sensitive performance is to \(J\), and whether the finite-\(J\) appendix result yields any practical parameter regime with \(\epsilon_k<1\).

2. Please cleanly restate **Theorem 2**, **Theorem 3**, and the constants in **Equations (15)-(16)** and Page 7 in corrected notation. As written, several terms appear malformed. A rebuttal that explicitly rewrites these bounds and defines every symbol would materially increase my confidence.

3. Can the authors provide a main-paper quantitative ablation separating:
   \[
   \text{ADMM + naive score denoising},\quad
   \text{ADMM + AC only},\quad
   \text{ADMM + DC only},\quad
   \text{ADMM + AC-DC}?
   \]
   This is the most direct way to verify the claimed role of each component.

4. How is \(\sigma_{\mathbf z^{(k)}}\) or \(\sigma_{\mathbf s^{(k)}}\) actually chosen in practice? The notation seems inconsistent between Algorithm 1, Section 4, and the experimental setup on Page 9. Please clarify whether these are the same quantity or different ones.

5. Since the \(x\)-subproblem in **Equation (7a)** is solved approximately with Adam rather than exactly, do the authors observe any instability from inexact inner solves? A plot of primal/dual residuals or objective surrogates over iterations would help, especially because the paper’s pitch is partly about making ADMM with score priors better behaved.

6. **Table 1** needs clarification. What exactly do the rows “Monitor”, “Convergence”, “Improving”, and “Phen-1” correspond to? Please align the naming with the task descriptions in Section 6.

7. Could the authors report compute cost, at least NFEs and approximate runtime, for the main methods in **Table 1**? Given that AC-DC adds multiple score calls plus iterative optimization for the \(x\)-step, this is important for practical assessment.

8. The central claim is that AC-DC reduces manifold mismatch. Can the authors provide a direct empirical diagnostic of this, for example a distributional distance, score consistency measure, or likelihood/energy statistic comparing \(\tilde{\mathbf z}^{(k)}\), \(z_{\mathrm{ac}}^{(k)}\), and \(z_{\mathrm{dc}}^{(k)}\) at matched noise levels?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper presents methodology for inverse problems and does not raise clear ethics concerns based on the submitted content.

## Soundness Rating
2: fair. The paper has a plausible method and broad experiments, but the central technical claims are weakened by strong assumptions, theory-practice mismatch, and multiple mathematical/formal inconsistencies in theorem statements and derivations.

## Presentation Rating
2: fair. The high-level story is understandable, and some figures are helpful, but notation drift, malformed equations, inconsistent table/task naming, and generally sloppy exposition significantly reduce clarity.

## Contribution Rating
2: fair. The paper addresses a meaningful problem and the empirical results are promising, but the methodological advance feels narrower than the framing suggests, and the evidence does not fully support the stronger claims about principled manifold alignment and convergence.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is interesting and potentially useful, but in its current form I do not think the technical presentation and validation are strong enough for a confident accept. The main reasons are the gap between theory and implementation, the number of mathematical/expository errors in the convergence section, and the lack of decisive ablations isolating the proposed correction mechanism.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I checked the main derivations and empirical claims with care, but some notation corruption in the submission makes full verification of every theorem difficult.