## Summary

This paper introduces **component-controllable personalization**, a task where a text-to-image diffusion model is fine-tuned to generate a visual concept (e.g., a person) with a specific component (e.g., a particular hairstyle) sourced from separate reference images. The authors propose **MagicTailor**, which combines Dynamic Masked Degradation (DM-Deg) to suppress unwanted semantics from out-of-mask regions via noise perturbation with a descending intensity schedule, and Dual-Stream Balancing (DS-Bal) to balance learning of concept and component semantics through sample-wise min-max optimization with momentum-based selective preservation. Experiments show SOTA results against adapted personalization baselines and demonstrate applications including decoupled generation, multi-component control, and integration with ControlNet/InstantMesh.

## Strengths

- **Well-motivated technical contributions with supporting ablation.** DM-Deg's descending exponential intensity schedule (Eq. 4) is shown to outperform fixed-intensity, linear, and mask-out baselines in the ablation (Tab. ablation_deg), directly supporting the claim that it prevents noise memorization while suppressing semantic pollution. DS-Bal's momentum U‑Net with β=0.99 is shown to outperform fixed-checkpoint regularizers (Tab. ablation_bal).

- **Practical efficiency.** Each concept‑component pair requires only ~5 minutes of training on an A100 GPU using LoRA (Sec. 4.1), enabling practical deployment without full-model fine-tuning or large domain-specific training datasets.

- **Large-scale user study.** The user study collects 3,180 valid answers across three evaluation axes (text alignment, identity fidelity, generation quality). The paper reports that MagicTailor achieves the highest selection rates by a wide margin against all adapted baselines.

- **Demonstrated generality beyond the core task.** MagicTailor supports decoupled generation (concept and component generated separately), multi-component control, and seamless integration with external tools (ControlNet, CSGO, InstantMesh) as shown in Sec. 4.5 and Fig. 7.

- **Sensitivity analysis on key loss weights.** Fig. 8 (referenced in Sec. 4.4) shows that performance remains SOTA across a reasonable range of λ_pres and λ_attn, indicating robustness to these hyperparameters.

## Weaknesses

### Fatal
None.

### Major

- **No automatic metric directly evaluates component fidelity.** The paper's automatic evaluation measures identity fidelity by *"segment[ing] out the concept and component in each reference and evaluation image, and then eliminat[ing] the target component from the segmented concept"* (line 261) before computing CLIP-I/DINO/DreamSim similarity. This explicitly removes the component before measuring identity, so the quantitative results do not provide any measurement of whether the *generated component* matches the *reference component* in appearance, pose, or detail. While the user study partially captures this (users can assess overall fidelity including the component), the central claim of enabling *component* control lacks direct automatic-metric support. This is an evidential gap: the conclusions may be correct, but the reader cannot quantitatively assess component-level accuracy from the reported numbers.

### Minor

- **Cross-attention loss implementation is underspecified.** The paper defines ℒ_attn using attention maps *A_θ(p_n, z_{nk}^{(t)})* (Eq. 2, line 116) but never specifies *which* cross-attention layer(s) in the U‑Net are used, how the attention maps are aggregated across heads/layers, or whether the object-token map or the full map is taken. This is a reproducibility gap that should be documented.

- **Sensitivity analysis for γ (dynamic intensity curve) is limited.** The dynamic intensity uses γ=32, tuned within powers of two (line 161). The ablation (Tab. ablation_deg) tests only discrete powers of two. Given that the curve is extremely steep at γ=32 (α_d drops from 0.5 to near zero in ~10% of training steps), a wider sweep or a continuous interpolation would increase confidence that performance doesn't collapse under different schedule shapes.

### Trivial
- Line 261: "meafsure" → "measure" (typo).

## Nice-to-Haves

- **Add a component-fidelity metric.** Computing CLIP-I/DINO similarity on the *component region alone* (segmented from both reference and generated images) would directly quantify component fidelity and close the main evidential gap described above. This would substantially strengthen the support for the paper's central claim.

- **Report absolute metric values for the warm-up baseline in the main text.** The ablation mentions that "even without DM-Deg and DS-Bal, such a baseline framework can still have competitive performance" (line 281), but the actual numbers are only in the (parser-inaccessible) table. Adding the key absolute values in the text would improve transparency.

- **Briefly clarify the image count in the main text.** "14,720 images for each method" (line 240) is not obviously derived from 20 prompts. A short clarification (e.g., number of random seeds, inference steps) would help the reader.

## Removed Points
*These points were flagged in the reviews but are removed (with justification) as they do not belong in the final assessment.*

- **"Min-max optimization claim is misleading"** — The paper states that minimizing ℒ_diff-max "can be considered as a form of min-max optimization" (line 192) with a citation. This is technically correct: min_θ max_n L_n(θ) is a valid min-max formulation. The criticism that this is "simply hard‑example mining" sets up a false dichotomy — a technique can be both. **Removed: factually wrong criticism.**

- **"Baseline adaptation is potentially unfair"** — The paper transparently states that all baselines are adapted by adding the masked diffusion loss (line 242) and that they use the same experimental setup. This is standard and necessary for a fair task comparison. Furthermore, the paper *does* include a simple baseline (warm-up stage only) in its ablation (Tab. ablation_tech), directly addressing the concern. **Removed: claim is contradicted by the paper.**

- **Complaints about missing table content / user study numbers / ablation numbers** — All tables are included via \input commands and are stripped by the parser. They exist in the original submission. **Removed: parser artifact, not an author error.**

- **"14,720 images is suspicious"** — The paper states details are in the supplementary material (standard practice given space constraints). **Removed: speculation about a parser-inaccessible detail.**

- **"User study omits baseline rates"** — The user study table (Tab. user_study) is an \input that the parser did not render. **Removed: parser artifact.**

- **Strength: "comprehensive evaluation with user study"** — While the evaluation is indeed large-scale, the automated metrics have a significant blind spot (component fidelity), making "comprehensive" an overstatement. This strength is retained with factual accuracy about the scale but without the qualifier "comprehensive."

## Novel Insights

Both reviewers independently identified the same core tension: the paper introduces a task defined by *component* control, yet the automatic evaluation pipeline *removes* the component before measuring identity fidelity. This observation is not present in the paper itself. A secondary insight — that the min-max terminology, while technically defensible, is a communication risk — is worth noting, though the paper's usage is actually more careful than the critic's dismissal suggests.

## Suggestions

1. **Add a component-specific automatic metric.** Segment the component region from both the reference and generated images (or use the same masks already computed), then report CLIP-I or DINO similarity on that region alone. This would directly support the paper's central claim with quantitative evidence.
2. **Specify the cross-attention layer used in ℒ_attn.** Document which U‑Net layer(s), how maps are aggregated across heads, and whether the map is averaged or max-pooled across spatial dimensions.
3. **Expand the γ sweep** in the dynamic intensity ablation to include γ values between powers of two (e.g., γ ∈ {8, 16, 24, 32, 48, 64}) to demonstrate robustness more convincingly.

## Score and Decision

**Originality:** Strong — the task formulation (per-component personalization from separate references) is new and practically motivated.  
**Importance of research question:** High — fine-grained control over components significantly extends the personalization capability of T2I models.  
**Claims supported:** Partially — the main claim about enabling component control lacks direct automatic-metric support, though qualitative results and user study provide converging evidence.  
**Soundness of experiments:** Solid methodology and ablations, but the automatic evaluation has a clear blind spot regarding component fidelity.  
**Clarity of writing:** Generally clear; the method is well-structured and figures are informative.  
**Value to community:** High — the task definition, the two proposed techniques, and the demonstrated applications are useful contributions.

The paper's core weakness — the gap in automatic evaluation of component fidelity — is significant but **addressable** (a component-masked similarity metric can be added without changing the method). It does not invalidate the method or the experimental conclusions, which are further supported by a large user study. The technical contributions (DM-Deg with dynamic intensity, DS-Bal with momentum-based preservation) are novel, well-motivated, and validated through careful ablation. Overall, the paper represents a solid contribution to the personalization literature.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>