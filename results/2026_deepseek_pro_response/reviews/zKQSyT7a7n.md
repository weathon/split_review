Now I have a solid calibration. Let me finalize.

**Round 1 bracket:** 5.5 to 7.5

**Round 2 narrowing:** The closest comparators are:
- **DINO-WM** (5.75, REJECTED): world model with CEM planning, but simulation-only 2D tasks, no real robot, no tactile. VT-WM is clearly stronger.
- **RCWM** (5.50, REJECTED): world model with pre-training, MetaWorld only, no real robot. VT-WM significantly stronger.
- **"Jointly Understand Visual and Tactile"** (6.00, ACCEPTED): cross-modal visuo-tactile manifold, but no robot manipulation or planning evaluation. VT-WM goes further with real-robot planning.
- **UltraTouch** (7.00, ACCEPTED): unified visuo-tactile representation learning across sensors, comprehensive. VT-WM has real-robot planning that UltraTouch doesn't match in depth, but UltraTouch has a stronger dataset contribution and more comprehensive evaluation.

VT-WM is stronger than the 6.00 anchor (has real-robot planning that anchor lacks) but weaker than the 7.00 anchor (has notable methodological gaps: under-specified baseline, small planning trials, missing ablation). **Final score: 6.5**.

---

## Summary
This paper proposes VT-WM, a multi-task world model that integrates exocentric vision (Cosmos tokenizer) with fingertip tactile sensing (Digit 360 + Sparsh-X encoder) through a 12-layer transformer predictor with factorized spatio-temporal attention and action-conditioned cross-attention. The authors evaluate VT-WM against a vision-only world model (V-WM) on three fronts: imagination quality via CoTracker-based Fréchet distances with statistical testing, zero-shot open-loop CEM planning on a real robot across five tasks, and data-efficient fine-tuning on a new task. Results show VT-WM improves object permanence and causal compliance, achieves up to 35% higher planning success on contact-rich tasks, and outperforms behavioral cloning by over 3× with limited demonstrations.

## Strengths
- **First principled multi-task visuo-tactile world model architecture.** The integration of frozen Cosmos visual latents and Sparsh-X tactile latents through factorized spatio-temporal self-attention followed by action cross-attention (Section 3.2.1, Fig. 3) is a genuine architectural contribution. Prior visuo-tactile dynamics models (Zhang & Demiris, 2023; Ai et al., 2024) were task-specific; prior multi-task world models (Agarwal et al., 2025; Assran et al., 2025) were vision-only. This paper bridges that gap with a clean design.
- **Rigorous quantitative evaluation of imagination quality with full statistical testing.** The use of CoTracker keypoints and normalized Fréchet distance (Section 4.1) backed by paired t-tests with explicit t-statistics and p-values across five tasks provides credible evidence. For example, push fruits object permanence: t=6.06, p<10⁻⁶; place fruits causal compliance: t=3.66, p<0.001. This statistical rigor is a genuine strength over typical qualitative-only world model evaluations.
- **Real-robot zero-shot planning validates imagination-to-reality transfer.** The CEM planning results (Fig. 8, Section 4.2) show VT-WM delivering 35% higher success on reach & push (93% vs 69%) and 31% higher on wipe cloth (92% vs 70%), while both models achieve 100% on free-space reaching. This gradient — negligible gain on kinematics-heavy tasks, large gain on contact-heavy tasks — is exactly what the motivation predicts.
- **Thoughtful multimodal temporal design.** The architecture gives vision a 1.5s context window (9 frames at 6fps) while tactile receives only 0.16s (2 frames per sensor, Section 3.2.2, lines 101-105). This reflects the higher temporal frequency and local nature of contact, showing careful engineering rather than naive modality concatenation.
- **Clean planning formulation isolates the world model's contribution.** The planner uses only visual latent ℓ₂ distance as cost — touch is never provided as a goal signal (Section 3.2.3, line 125). This cleanly isolates the benefit of tactile sensing to improved dynamics modeling, making the causal chain from better imagination to better planning interpretable.

## Weaknesses

### Fatal
None.

### Major
- **V-WM baseline architecture and parameter count are unspecified in the main text.** The paper compares VT-WM to a "multi-task vision-only world model (V-WM)" but the main text never describes how V-WM is constructed (Section 4.1, line 140). If V-WM is architecturally identical minus tactile tokens, it has fewer input tokens and potentially fewer parameters, making the comparison unfair in VT-WM's favor. If V-WM was given additional capacity to match parameter count, this needs to be stated. Since all three experimental sections depend on this comparison, the ambiguity weakens the paper's core empirical claim.
- **Planning evaluation uses only 5 trials per task with no statistical testing.** The zero-shot planning results (Section 4.2, Fig. 8, line 239) report success rates from 5 trials per task. For tasks where differences are small (stack cubes: 75% vs 83%; push fruits: 83% vs 92%), these differences are well within binomial sampling noise. This contrasts with the careful t-tests applied to the Fréchet distance metrics, making the planning evaluation appear under-powered for the claims made.
- **Data efficiency experiment conflates world-model pre-training benefit with tactile benefit.** Section 4.3 compares VT-WM fine-tuned on 20 demos against a BC policy (ACT) trained from scratch on the same data. The paper attributes the gain to tactile-informed contact priors, but the experiment lacks a critical ablative condition: fine-tuning V-WM (the vision-only world model) on the same 20 demos. Without this, the result demonstrates data efficiency of multi-task world models generally, not of visuo-tactile world models specifically.

### Minor
- **Scribble-with-marker degradation is reported but never analyzed.** Fig. 6 shows VT-WM produces worse causal compliance than V-WM on scribble with marker (normalized Fréchet ~0.50 vs ~0.35, t=−1.22, p=0.23). While not statistically significant, the paper never discusses why tactile information might hurt on this task, limiting the generality of the claimed improvement.
- **CoTracker reliability under occlusion is not addressed.** The object permanence metric uses CoTracker keypoints on ground-truth video, but the primary claim is that VT-WM maintains object representations precisely under occlusion — when CoTracker is most likely to fail on the ground truth. The paper does not discuss how it handles CoTracker failures or report tracker confidence/visibility scores (Section 4.1, line 144).
- **Abstract overstates uniformity of gains.** The abstract claims "33% better performance at maintaining object permanence and 29% better compliance" as if these gains are uniform. Section 4.1 reveals that wipe with cloth and scribble with marker do not reach significance for object permanence, and cube stacking and scribble with marker do not reach significance for causal compliance.
- **No limitations discussion.** Section 5 (Discussion and Conclusion) restates experimental findings but does not discuss limitations — reliance on a specific tactile sensor (Digit 360), open-loop execution, task-dependent benefits, or the purely visual planning objective.
- **"Zero-shot" could be clarified.** The paper uses "zero-shot" to mean zero-shot plan generation (CEM with no task-specific planner training). However, the evaluated tasks appear to overlap with training tasks, so this is not zero-shot generalization to unseen tasks. The distinction matters for significance claims.

### Trivial
- Training hyperparameters (parameter count, CEM population size, planning horizon) are deferred to the appendix; core numbers like parameter count should appear in the main text for reader context.
- The appendices are referenced for key content (action controllability evaluation in Appendix B, experimental setup in Appendix C), making the main-text evaluation incomplete without them.

## Nice-to-Haves
- Inference time analysis: CEM with autoregressive rollouts per iteration is computationally intensive; even rough timing numbers would help readers assess deployability.
- Discussion of whether closed-loop replanning was attempted, or whether open-loop was dictated by inference speed constraints.
- Broader discussion of how results might transfer to other tactile sensors beyond Digit 360.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Missing related work on multimodal sensor fusion for dynamics learning** — REMOVED. This is a speculative "missing reference" claim that cannot be verified without external sources. The paper's related work coverage is adequate for the scope.
- **Demand for confidence intervals on all metrics including those already reported with CIs** — REMOVED. The Fréchet distance figures already report 95% CIs (Figs. 4 and 6 captions). The specific issue about planning success rates lacking statistical testing is retained under Major.
- **Criticism about planning cost being purely vision-based** — REMOVED as a formal weakness. The paper explicitly acknowledges this limitation at line 125: "We do not provide the tactile modality as a goal signal, thus the planning objective remains purely vision-based." This is a design choice the paper is forthright about, not an oversight.
- **Open-loop execution as a flaw** — MOVED to Nice-to-Haves. The paper is explicit about open-loop execution (Section 3.2.3, line 123) and this is standard practice for model-based planning evaluations in robotics.
- **Demand for closed-loop replanning discussion** — MOVED to Nice-to-Haves. This is a reasonable suggestion but not a flaw.
- **Missing appendix / deferred details** — MOVED to Trivial. The paper explicitly references the appendix for these details; the stripped appendix is a parser artifact, not an author error.

## Novel Insights
The paper's task-difficulty gradient in the planning results — where VT-WM matches V-WM on free-space reaching (100% vs 100%) but substantially outperforms on contact-rich tasks (up to 35% on reach & push and 31% on wipe cloth) — provides a clean empirical demonstration that tactile grounding matters specifically where contact physics are at play. This gradient pattern is more informative than raw success rate averages and aligns tightly with the paper's motivation.

## Suggestions
- Add the V-WM fine-tuning condition to the data efficiency experiment to cleanly attribute the gain to tactile sensing rather than world-model pre-training.
- Increase planning trials to at least 10 per task and report binomial confidence intervals, matching the statistical rigor applied to the Fréchet distance metrics.
- Analyze the scribble-with-marker degradation to characterize when tactile helps vs. when it doesn't, which would strengthen the paper's generality claims.
- Move key architectural numbers (at minimum parameter count for both models) into the main text, and specify the V-WM architecture explicitly.

## Score and Decision

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Small features matter: WM | Qr9TjKYzjl | 3.00 | R1 (weak) | Much weaker — DreamerV3 on Atari, no real robot |
| From Appearance to Motion | wl1Kup6oES | 3.00 | R1 (weak) | Much weaker — visual pre-training for BC only |
| The Power of the Senses | FMsmo01TaI | 4.33 | R1 (middle) | Clearly weaker — simulation-only, 3 tasks, no planning |
| VTDexManip | jf7C7EGw21 | 5.50 | R1 (middle) | Weaker — dataset+benchmark, limited real-robot quantitative results |
| RCWM | DJw1JBTmuk | 5.50 | R2 (narrow) | Weaker — simulation-only MetaWorld, no real robot, no tactile |
| DINO-WM | GARbxyCV13 | 5.75 | R2 (narrow) | Weaker — 2D tasks, no real robot, no tactile, rejected |
| Jointly Understand V+T | NtQqIcSbqv | 6.00 | R1/R2 | Slightly weaker — cross-modal manifold, no robot planning |
| UltraTouch | XToAemis1h | 7.00 | R1/R2 | Slightly stronger — more comprehensive evaluation, strong dataset contribution |
| Thin-Shell Object Manipulations | KsUh8MMFKQ | 8.00 | R1 (strong) | Different topic — differentiable physics simulation |
| Geometry-aware RL | 7BLXhmWvwF | 8.00 | R1 (strong) | Different topic — heterogeneous graph RL |

**Round 1 bracket:** 5.5 to 7.5  
**Round 2:** VT-WM is clearly stronger than DINO-WM (5.75) and RCWM (5.50), stronger than "Jointly Understand" (6.00 — VT-WM has real-robot planning that anchor lacks), but somewhat weaker than UltraTouch (7.00 — VT-WM has notable methodological gaps). **Final score: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>