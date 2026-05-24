Now I have enough calibration data. Let me write my consolidated review.

## Summary

This paper proposes EDPA (Embedding Disruption Patch Attack), a model-agnostic adversarial patch attack for Vision-Language-Action (VLA) models, and a complementary adversarial fine-tuning defense. EDPA operates by maximizing discrepancy in visual latent representations and disrupting visual-language alignment, requiring only access to encoder parameters (not the full VLM backbone). The attack is evaluated on OpenVLA, OpenVLA-OFT, and π0 across the LIBERO simulation benchmark, showing substantial failure rate increases. The defense fine-tunes only the visual encoder and is evaluated on OpenVLA.

## Strengths

1. **First model-agnostic adversarial patch attack for VLAs that transfers across diverse architectures without action-space or manipulator knowledge.** Table 1 and Figure 1 clearly delineate that EDPA requires only encoder parameters, while prior attacks (UADA, UPA) need action-space or robotic-manipulator knowledge. Table 3 demonstrates that EDPA successfully attacks OpenVLA-OFT (62.0% average FR increase) and π0 (31.4% average FR increase) in multi-camera settings, whereas UADA/UPA cannot be applied to these models at all. This is the paper's strongest contribution — prior attacks were architecture-specific, and EDPA genuinely relaxes these constraints.

2. **Two well-motivated and complementary loss functions.** The patch contrastive loss (Eq. 2, inspired by InfoNCE) and the image-instruction alignment loss (Eq. 3) target different aspects of the VLA's representation space. The joint optimization objective (Eq. 4) is clearly defined, and the methodology section grounds the approach in prior work on embedding-level attacks against LVLMs (Section 3.2, citing Zhang et al., Zhao et al., Bagdasaryan et al.).

3. **Defense preserves clean performance while reducing failure rates across multiple attack types.** Table 2 shows that adversarial fine-tuning on OpenVLA reduces failure rates against EDPA (avg −34.2%), UADA (−19.1%), and UPA (−36.0%), while clean failure rate increases by only 1.6%. The defense algorithm (Algorithm 1) is well-specified with practical details like periodic patch reset to prevent overfitting.

4. **Evaluation across four distinct LIBERO task suites (Spatial, Object, Goal, Long) with three random seeds and standard deviation reporting.** The experimental methodology follows community standards (Wang et al. 2024, Kim et al. 2024), using failure rate as the metric with multiple seeds for statistical reliability.

## Weaknesses

### Major

1. **Defense evaluated on only one model (OpenVLA), while claims of generality are unsubstantiated.** The paper states the defense "can be directly integrated into the VLA without any modification" (line 168) and is intended as a general defense for VLAs. Yet the defense experiments in Section 4.2 and Table 2 are exclusively on OpenVLA. The authors acknowledge OpenVLA was chosen "due to our experimental results showed that OpenVLA exhibited the weakest robustness against EDPA" (line 29), but this does not justify omitting experiments on OpenVLA-OFT or π0, for which the attack was already evaluated in Table 3. Without evidence that the same adversarial fine-tuning procedure works (or requires modification) on other models, the defense contribution is incomplete and its claimed generality overstated. This is the single most impactful gap in the paper.

2. **No real-world or physical-world validation, despite the paper's emphasis on practical applicability.** The introduction and abstract motivate EDPA by practical real-world threats ("adversarial patches placed within the camera's view"), and a key claimed advantage over prior work is that EDPA is more "practical for real-world scenarios" (line 66). Yet all experiments are entirely in simulation (LIBERO). Even a simple qualitative demonstration (e.g., printing the patch and placing it in a camera view in a controlled physical setup) would substantially strengthen credibility. This gap limits the paper's ability to support its practicality claims.

### Minor

3. **Ambiguity in access-requirement claims regarding the language encoder.** The paper states EDPA "requires only access to the VLA's encoder parameters" and marks "LVLM Parameters" as not required in Table 1. However, EDPA uses the language encoder (Section 3.2, Eq. 3, requiring $\mathcal{E}_t(t)$), which in architectures like OpenVLA is the token embedding layer of the LLM — functionally part of the LVLM. The paper's architectural decomposition in Section 3.1 treats the language encoder as a separate component from the LVLM backbone, which is a reasonable functional distinction (the embedding layer is much smaller than the full transformer). But the presentation is unclear on whether "LVLM Parameters" includes the language encoder's embedding weights. This should be explicitly addressed. It does not invalidate the contribution — EDPA still requires less access than UADA/UPA which need the full backbone plus action-space knowledge — but the lack of clarity is confusing.

4. **The defense's absolute failure rates remain very high under EDPA on harder task suites, but the paper's language overstates effectiveness.** After defense, OpenVLA still fails at 73.9% (Goal) and 91.2% (Long) under EDPA (Table 2). The abstract and conclusion state the defense "effectively mitigates this degradation," which is an overstatement for a model that fails 91% of the time on Long tasks. The paper would be more credible with calibrated language describing "partial mitigation" or "substantial improvement while absolute failure rates remain high under strong attacks."

5. **Missing ablation of the two loss components.** The patch contrastive loss (Eq. 2) uses an unusual formulation where positive and negative pairs come from the same image (p_i vs p'_j for j≠i), rather than contrasting across different samples as in standard InfoNCE. The paper does not ablate against simpler alternatives (e.g., MSE between clean and adversarial embeddings, or cosine distance). Appendix C is referenced but its contents are not visible in the extracted submission.

### Trivial

6. **No comparison to other defense methods** (e.g., adversarial training of the full model, robust vision encoders). While no prior defense exists specifically for VLA models, some comparison would contextualize results. The paper acknowledges this indirectly.

7. **The "overfitting" hypothesis in Section 5** (patches resemble robotic arms due to overfitting to arm appearance in training data) is interesting but purely speculative with no supporting analysis.

## Nice-to-Haves
- Demonstrate the defense on at least one additional model (OpenVLA-OFT or π0) to support generality claims.
- A qualitative real-world demonstration of the patch attack (e.g., printed patch held in front of a camera).
- Ablation comparing the patch contrastive loss to simpler alternatives (MSE, cosine distance).
- Statistical significance testing for defense improvements (Table 2 reports std devs but no explicit significance tests).

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"No evaluation of attack's physical-world applicability"** — this is kept in Major as weakness #2 since the paper explicitly motivates EDPA by practical real-world threats.
- **"Patch contrastive loss is unusual / not the intended effect"** — This is a valid observation but minor; I moved it to Minor weakness #5 as a missing ablation issue.
- **"Missing statistical significance for defense improvements"** — moved to Nice-to-Haves since std deviations are already reported.
- **"The discussion of overfitting in Section 5 is speculative"** — kept as Trivial #7.
- **"Attack is optimized on LIBERO itself, not tested OOD"** — The critic acknowledged this as not fatal; I've left it as a mild limitation observation. Worth noting but not a weakness per se since in-distribution evaluation is standard.
- **Strength Finder's generic strengths dropped:** "this paper addressed an important problem," "targeted an interesting question" — these are generic and removed.
- **Strength Finder's "Attack objectives grounded in prior work"** — while true, this is a supporting strength at best; the paper's novelty is in adapting embedding-level attacks to the patch setting for VLAs, which is genuinely interesting. Kept as a supporting observation but moved to the methodology context.
- **Strength Finder's claim about "evaluation across four distinct task suites and three models"** — kept as Strength #4 but rephrased to avoid overclaiming (defense is only on one model).
- **"If the access claim cannot be sustained, the paper's central contribution is undermined" (Harsh Critic)** — Verified against the paper: the paper's architectural decomposition (Section 3.1) explicitly separates language encoder from LVLM backbone. The claim is defensible, though presentation clarity is lacking. Demoted from "structural issue" to Minor.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder both correctly identified the paper's main strengths (model-agnostic attack design, evaluation across multiple architectures) and weaknesses (defense generalization gap, simulation-only evaluation). The core tension is between the novelty of the attack contribution (which is real and well-supported) and the incompleteness of the defense validation (which limits the paper's overall impact). No reviewer identified a perspective not already present in the paper itself.

## Suggestions
1. Add defense experiments on at least one additional model (OpenVLA-OFT or π0) — this is the single highest-impact change the authors can make.
2. Clarify the access-requirement language: explicitly state whether the language encoder's embedding layer is considered part of the "LVLM parameters" or not, and why this distinction is meaningful.
3. Calibrate language around defense effectiveness — replace "effectively mitigates" with more precise phrasing given the high absolute failure rates on Goal and Long suites.
4. Add an ablation of the two loss components to justify the design choices.
5. If feasible, include even a minimal physical-world demonstration of the patch attack.

## Score and Decision

After careful calibration against human-reviewed anchors:

**Round 1 — Bracketing:**
- Weak anchors (score < 3.5): BadConcepts (2.50), VLM-PTA (3.00), Don't Lag RAG (3.00) — these are about VLM security but are clearly weaker papers (backdoor attacks, weight perturbations, detection-only). The current paper is substantially stronger.
- Middle anchors (3.5–7.5): On Robustness of VLA (6.00, Accept Poster), RobustVLA (4.50, Reject), VLA-in-the-Loop (5.00, Reject), Actions as Language (5.50, Accept Poster). These are the most topically relevant.
- Strong anchors (>7.5): Embodied Navigation Foundation Model (8.00), Generative Universal Verifier (8.00), Text-to-3D (8.00) — these are on different topics and not directly comparable.

Initial bracket: **4.5 – 6.5**

**Round 2 — Narrowing:**
- On Robustness of VLA (6.00, Accept Poster)** — closely related VLA robustness paper with real-world experiments, broader evaluation (17 perturbations), accepted. Current paper is weaker: no real-world experiments, defense on only 1 model. **Current paper is below this anchor.**
- VLM4VLA (7.00, Accept Poster)** — large-scale empirical study with 7 models, 3 benchmarks. Much stronger experimental scope. **Current paper is significantly below this anchor.**
- AdPO (6.50, Accept Poster)** — adversarial defense for LVLMs with comprehensive experiments and multiple model transfer. **Current paper is below this anchor.**
- Actions as Language (5.50, Accept Poster)** — VLA training paradigm with 800+ real-world robot experiments. Novel contribution but different domain. **Current paper is roughly comparable — worse on experimental validation (sim only vs real-world), but has a genuinely novel attack contribution.**
- Vision-Language-Action Instruction Tuning (5.50, Accept Poster)** — Another VLA training paper with real-world experiments. **Current paper is roughly comparable or slightly below.**
- VLA-in-the-Loop (5.00, Reject)** — simulation-only, methodological concerns. **Current paper is stronger.**
- RobustVLA (4.50, Reject)** — simulation-only, theoretical issues. **Current paper is clearly stronger.**

Final score: **5.5**. The paper has a genuine, well-supported novel contribution in the attack (first model-agnostic adversarial patch attack for VLAs, convincingly evaluated on 3 architectures). However, the defense evaluation is incomplete (1 model only), all experiments are simulation-based despite motivation emphasizing real-world practicality, and the presentation has some overclaiming. These weaknesses prevent it from reaching the level of stronger accepted papers (6.0–6.5+) in this space. At 5.5, this is a borderline-weak-accept paper whose novelty is real but whose empirical validation has notable gaps.

**Decision:** Accept

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>