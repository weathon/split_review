## Summary

This paper investigates the role of pooled CLIP text embeddings (modulation-based conditioning) in diffusion transformers (DiTs). Section 4 provides an empirical analysis showing that CLIP is partially inactive in FLUX schnell (for long prompts) and fully inactive in HiDream-Fast in standard usage. Building on this, Section 5 proposes *modulation guidance*: a training-free technique that repurposes the pooled embedding as a directional steering signal by computing y(p₊,t) − y(p₋,t) and adding it to the baseline, improving generation quality across diverse tasks (T2I, T2V, image editing) without fine-tuning. The method is extended to CLIP-free models (COSMOS, CausVid) via lightweight fine-tuning.

---

## Strengths

- **Convincing empirical demonstration that the pooled CLIP embedding is largely inactive in current diffusion transformers**: Table 1 quantifies this for FLUX schnell and HiDream-Fast. For HiDream-Fast, CLIP Score (32.9), PickScore (21.5), and ImageReward are completely unchanged by zeroing CLIP for both short and long prompts. For FLUX schnell long prompts, CLIP Score drops only 0.3 points vs. a 2.4-point drop when removing T5. Figure 1 shows DreamSim deviation falling to near zero as prompt length exceeds ~40 tokens. This is a clean, reproducible empirical finding with practical implications.

- **Strong multi-model quantitative evidence for the proposed modulation guidance**: Table 2 reports statistically significant human preference win rates across five diverse models (FLUX schnell, FLUX dev, SD3.5 Large, HiDream, COSMOS). Aesthetics guidance achieves 72% win rate on FLUX schnell, 56% on FLUX dev, 62% on SD3.5, and 60% on HiDream. Automatic metrics (PickScore, ImageReward, HPSv3) show consistent improvements across models. The fact that COSMOS "+CLIP" rows show no improvement while "Modulation guidance" rows do confirms that gains stem from guidance, not just reintroducing CLIP.

- **Dynamic modulation guidance provides a better quality–fidelity trade-off than constant scale**: Figure 3(a) directly compares dynamic vs. constant guidance on the aesthetics/CLIP score Pareto frontier. Dynamic guidance at w=2 achieves PickScore ~21.72 while maintaining CLIP Score ~30.9 (matching the original model), whereas constant guidance at comparable scale degrades CLIP Score to ~30.6. The design (a simple layer-wise step function, Figure 3b) is easy to implement and reportedly generalizes across tasks.

- **Applicability to CLIP-free models (COSMOS, CausVid) via lightweight fine-tuning**: Table 4 shows CausVid with modulation guidance achieves dynamic degree 86.59 vs. 75.25 baseline and 74.22 for Normalized Attention Guidance, with total score 65.43 vs. 62.72. Only 1K fine-tuning iterations are required. This demonstrates the technique's broad reach.

- **Attention-map analysis provides mechanistic interpretability**: Figure 4 shows that modulation guidance shifts mean attention toward the token "hands" and hand-related tokens (from ~0.15 to ~0.25 mean attention) in a categorized token analysis, offering a plausible mechanistic window into what the method does beyond raw metrics.

---

## Weaknesses

### Fatal
None.

### Major

- **Specific-change evaluation is limited to a single model (FLUX schnell) with uncharacterized prompt sensitivity (Table 3)**: The most practically significant results—+9 GenEval points for object counting, +22% win rate for object counting, +18% win rate for hands correction—are reported only for FLUX schnell. The general-change results (Table 2) cover five models, providing generalization evidence; Table 3 does not. More critically, Section 5 states the only requirement is "to select a suitable prompt for each category" and defers the actual prompts to Appendix D (stripped). The paper never characterizes how sensitive the +22%/+18% improvements are to the specific prompt formulation chosen. This gap means the practical improvement available to a new practitioner with different prompt choices is unknown. Given that these results headline the specific-change narrative, the absence of a prompt-sensitivity ablation is a genuine evidential weakness.

- **Key baseline comparisons (NAG by 34%, Concept Sliders by 16%) are absent from the main body**: Section 6.1 states: "Results in Appendix E (Tables 8 and 9) show that our approach outperforms Normalized Attention Guidance by 34% and Concept Sliders by 16%." These are the most directly comparable training-free baselines, and the margin claims are among the strongest in the paper—yet they appear only in the appendix. The main text characterizes these comparisons only by their conclusions. Reviewers evaluating the main contribution cannot assess these numbers without access to the appendix. A summary table or row in Table 2 would substantiate these claims where they can be scrutinized.

### Minor

- **The mechanism behind CLIP inactivity is unaddressed**: Section 4 documents the empirical phenomenon (CLIP zeroing has negligible effect for long prompts) but proposes no explanation. Multiple plausible mechanisms predict different implications: (a) the MLP learned to suppress CLIP's contribution during training, (b) T5 and CLIP encode overlapping information and T5 dominates for long prompts, or (c) training dynamics made CLIP redundant. If explanation (a) is correct, then modulation guidance (which amplifies y(p₊) − y(p₋) via the same MLP) should also be suppressed, creating a mild internal tension the paper does not resolve. The paper's empirical success of modulation guidance implies (a) is not the full story, but no analysis clarifies why. This gap weakens the paper's analytical contribution, though it does not undermine the method's demonstrated efficacy.

- **Video result (CausVid) trade-off is not acknowledged**: Table 4 shows CausVid modulation guidance achieves dynamic degree 86.59 (+11.34 over baseline) but motion smoothness drops from 98.76 to 98.45. The Section 6.2 text characterizes the results as an improvement without mentioning the smoothness decline: "we observe improvements in dynamic degree for both models." For video generation, motion smoothness is a genuine quality dimension. A single sentence acknowledging this trade-off would be appropriate.

- **Image editing application (Section 6.3) lacks quantitative results in the main body**: Section 6.3 explicitly states quantitative results are in "Appendix F." Two qualitative examples (Figure 8) are provided in the main text. Given that this is presented as a distinct application with a specific benchmark (SEED-Data), the absence of even a summary metric in the main body leaves the editing claim at the "qualitative demonstration" level within the page limit.

### Trivial

- **The "defects" dimension in Table 2 shows mostly neutral or slightly negative results** (45–52%), which the paper acknowledges briefly ("We note slight drops...in defects for COSMOS"). The prose could be more transparent that defects are not systematically improved rather than framing results as broadly positive.

---

## Nice-to-Haves

- The paper's most interesting analytical finding—CLIP inactivity—would be substantially stronger if paired with a mechanistic investigation, e.g., layer-wise ablations correlating which modulation layers are most responsive to CLIP, or probing whether the MLP weights on the CLIP branch differ between active and inactive models.
- A small ablation over plausible positive/negative prompt variants for one specific-change task (e.g., hands correction) would validate the practical claim that a new practitioner can "select a suitable prompt" and see gains, rather than requiring the exact prompts the authors used.
- Extending Table 3 (specific changes) to at least one additional model (e.g., FLUX dev) would substantially strengthen the generalization claim for the most headline-worthy results.
- The paper states the method "incurs negligible computational overhead" but does not specify the exact cost in wall-clock terms or FLOPs. Even one sentence (e.g., "three MLP forward passes per denoising step, adding <0.1% latency") would satisfy practitioners.

---

## Removed Points

*These points are flagged to be removed — treat them with caution.*

1. **"The core technique is CFG applied in a different space and this needs to be stated plainly"** [Harsh Critic, framed as significant framing failure]: While the structural similarity to CFG is real, the paper does explicitly situate the method against "CFG modifications" and "attention guidance methods" in Section 2, and states "Our approach also relies on guidance in feature space but applies it through a small MLP rather than through attention." The paper does not claim conceptual novelty over CFG mechanics; it claims novelty in applying guidance in modulation space with demonstrated cross-model efficacy. Framing this as a failure of honesty is overstated — demoted to a nice-to-have.

2. **"Dynamic guidance layer hyperparameter i sensitivity is uncharacterized"** [Harsh Critic]: The paper notes the step-function strategy "generalizes well across tasks." This is a standard hyperparameter in any guidance approach. The paper refers to Appendix B and C for further ablations. Not having this in the main body is typical for such a paper.

3. **Generic strengths without concrete grounding** [Strength Finder]: "The paper addresses an important problem" and "the method is simple to implement" — removed as generic without standalone evidential weight. The method's simplicity is evidenced concretely by Equation 3, so that part is retained in the method description rather than as a separate strength.

---

## Novel Insights

The most genuinely novel insight in this paper—beyond the method itself—is the cross-model demonstration that the pooled CLIP embedding is structurally inactive in contemporary diffusion transformers under standard usage (Section 4, Table 1, Figure 1). This is not an architectural design claim (several models already removed CLIP) but a behavioral measurement that had not been cleanly quantified: CLIP's influence disappears almost entirely at prompt lengths exceeding ~40 tokens in FLUX schnell, and is completely absent in HiDream-Fast regardless of prompt length. The corollary insight—that this inactivity reflects a *usage failure* rather than an intrinsic limitation, since modulation guidance can reactivate the embedding's influence—reframes the "CLIP is unnecessary" conclusion of recent architecture trends as premature. Together these observations suggest that the modulation space in DiTs is an underutilized resource for steering generation quality without fine-tuning.

---

## Suggestions

1. Include a compact version of Appendix E's baseline comparison (NAG, Concept Sliders results) in the main paper as a table row or short sub-table in Section 6, so reviewers can evaluate the strongest competing methods without appendix access.
2. Add a prompt-sensitivity ablation for at least one specific-change task (e.g., test 5 plausible hand-correction positive/negative prompt formulations and report the variance in win rate) to validate the practitioner promise.
3. In Section 6.2, acknowledge the motion smoothness trade-off for CausVid explicitly and discuss whether this is an acceptable cost for the dynamic degree gain.
4. Add one sentence to Section 4 clarifying the internal tension: if MLP suppresses CLIP, why does modulation guidance work? A hypothesis (e.g., "the directional difference between two non-zero CLIP embeddings circumvents the suppression that zeroing incurs") would suffice.

---

## Score and Decision

**Axis-by-axis assessment:**

- *Originality*: Moderate. The idea of applying CFG-style directional guidance in the modulation (rather than denoising output or attention) space is a natural extension of known principles. The empirical finding of CLIP inactivity is original and clean.
- *Importance*: High. Training-free improvements to state-of-the-art generation models are directly useful; the CLIP inactivity finding is relevant to architecture design decisions.
- *Claims supported*: Mostly yes, for general-change claims (Table 2, 5 models). The specific-change claims (Table 3) are supported for one model only and rely on prompt choices that are not sensitivity-analyzed.
- *Soundness*: Good overall. The methodology is appropriate, metrics are standard, and human evaluation is included. The main gap is the one-model specific-change evaluation.
- *Clarity*: Good. The paper is readable and well-organized. Key results are appropriately tabulated.
- *Community value*: High. The technique is immediately applicable, training-free, and the CLIP inactivity finding is independently valuable.

The paper is a solid empirical contribution. Its central claims about general-change improvements are well-supported across five models with both automatic and human evaluation. The specific-change results are promising but evidentially weaker. The paper falls short of being a top contribution due to the major issues above (single-model specific evaluation, appendix-relegated key baseline comparisons), but it is a clear accept at a major venue.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>