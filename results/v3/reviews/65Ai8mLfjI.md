Here is my final consolidated review.

---

## Summary

This paper revisits the role of pooled CLIP text embeddings in diffusion transformers. It first demonstrates through ablation experiments (zeroing out the CLIP embedding) that the pooled embedding contributes little to performance in standard usage — it is partially inactive in FLUX and fully inactive in HiDream-Fast and CLIP-free models like COSMOS. The core contribution is to repurpose this seemingly redundant signal as **modulation guidance**: a training-free extrapolation in the modulation space (Eq. 3: ŷ = y(p,t) + w·(y(p₊,t) − y(p₋,t))) that shifts generation toward desirable properties like better aesthetics or complexity. Dynamic strategies (applying guidance only after early layers) further improve the fidelity–quality trade-off. The method is evaluated across five T2I models, two video models, and an image-editing task, with both automated metrics and human side-by-side comparisons.

---

## Strengths

1. **Quantitative evidence that the pooled embedding is often inactive.** Table 1 and Figure 1 cleanly show that zeroing out the CLIP embedding has negligible effect on long prompts for FLUX and no effect at all for HiDream-Fast across both short and long prompts. This provides a clear motivation for why repurposing this signal makes sense.

2. **Consistent improvements across five text-to-image models.** Table 2 shows that modulation guidance wins human preference by up to 72% for aesthetics (FLUX schnell) and 80% for complexity (HiDream), with automatic metrics (ImageReward, HPSv3) also improving across most configurations. The COSMOS ablation (CLIP alone → 43% complexity win rate; CLIP + guidance → 70%) cleanly isolates that the guidance mechanism, not mere CLIP presence, drives gains.

3. **Dynamic guidance demonstrably improves the quality–fidelity trade-off.** Figure 3(a) plots PickScore vs. CLIP score and shows that the dynamic variant maintains prompt fidelity (CLIP score ~30.9) while raising aesthetic quality, whereas constant guidance degrades fidelity at high scales (CLIP score drops to ~30.2). This is direct evidence that the proposed layer-wise step function is beneficial beyond what constant scaling provides.

4. **Interpretability analysis shows the mechanism.** Figure 4 visualizes how modulation guidance shifts attention toward relevant tokens (e.g., "hands," hand-related tokens) and away from non-content tokens, providing a mechanistic explanation for the qualitative improvements in hands correction and other specific changes.

5. **Broad coverage across modalities and tasks.** The method is validated on five T2I models (FLUX schnell, FLUX dev, SD3.5 Large, HiDream, COSMOS), two video models (Hunyuan 13B, CausVid 1.3B), and an image-editing setting, with both automated and human evaluation. This breadth strengthens the claim that the approach is general.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The layer cutoff *i* for dynamic guidance is not stated in the main text.** Figure 3(b) defines the step function (w=0 for layers 0 to i, then constant w), and the paper claims it "generalizes well across tasks," but the value of *i* used in experiments is not reported in the main paper. For a method billed as plug-and-play, a recommended default or a brief sensitivity analysis would aid reproducibility.

2. **Human evaluation lacks key statistical details in the main text.** Table 2 marks green/red for "statistically significant" changes, but the number of annotators, the specific significance test used, p-values, and inter-rater agreement are not reported in the main paper. The paper references Appendix J for details, but the main text should at minimum state the number of annotators and the test employed.

3. **Specific changes (object counting, hands, color, position) are only evaluated on FLUX schnell.** While the general changes (aesthetics, complexity) are demonstrated across five models, the specific improvements in Table 3 are limited to a single model. Demonstrating object counting or hands correction on at least one other model (e.g., SD3.5 or HiDream) would strengthen generalizability claims.

4. **The Normalized Attention Guidance baseline is missing for Hunyuan in the video experiments.** Table 4 includes Norm. attent. guidance for CausVid but not for Hunyuan, making the comparison incomplete. The paper also does not explain why this baseline was omitted for one model but included for the other.

5. **No sensitivity analysis for prompt phrasing.** The method relies on manually chosen positive/negative prompts for each target property (listed in Appendix D). The paper does not study how sensitive the results are to the exact wording of these prompts. A small ablation (e.g., synonym variants) would help users gauge how carefully prompts must be crafted.

6. **The Defects metric shows little to no improvement (and sometimes decline) across all models and tasks.** The paper acknowledges this as "minor" but does not discuss why guidance does not reduce defects or whether there are systematic failure cases. A brief discussion would be informative.

### Trivial
- Figure 3(a) labels the y-axis as "PadScore" in the caption text (should be "PickScore").
- The paper could benefit from stating the recommended guidance scale *w* and cutoff *i* as a quick-reference default in Section 5.

---

## Nice-to-Haves

- A brief analysis of failure modes or artifacts when the guidance scale *w* is pushed too high (beyond what is shown in Appendix C). Including visual examples in the main paper would help practitioners gauge safe operating ranges.
- Reporting bootstrapped confidence intervals or binomial test p-values for the human win rates would strengthen the statistical grounding and align with standard practices for side-by-side studies.
- Extending the specific-change evaluation (object counting, hands correction) to one additional T2I model would further support the generalizability claim.

---

## Removed Points

The following points from the reviewer inputs were removed with justification:

- **"Key baseline comparisons are relegated to the appendix"** — The main paper (Section "Comparison with baselines") explicitly reports headline results: "outperforms Normalized Attention Guidance by 34% and Concept Sliders by 16%," and states that modulation guidance further improves LLM-enhanced prompts. The full tables are in Appendix E, which is standard practice for conference papers with space constraints. The main text already communicates the essential comparative findings.
- **"Token-length analysis only on FLUX schnell"** — The paper already reports HiDream results in Table 1 (CLIP has no effect on either short or long prompts). The token-length analysis in Figure 1 specifically interrogates how CLIP influence varies with prompt length, which is a FLUX-relevant phenomenon; HiDream's zero effect is already documented.
- **"Introduction is too strong"** — The paper's intro is appropriately nuanced. It says "at first glance, modulation-based text conditioning appears non-contributory" and acknowledges CLIP does influence short prompts. The claim "attention alone is generally sufficient" is qualified ("generally") and supported by the analysis.
- **"No prompt sensitivity study"** — Moved to Minor Weakness #5 with appropriate severity calibration.
- **"Some metrics decrease"** — The paper acknowledges the drops and calls them minor. This is honest reporting, not a weakness per se; it was retained as Minor #6.
- **"Reproducibility: dynamic guidance parameters not specified"** — This is now Minor #1.
- **"Missing related works"** — Removed per hard rules (cannot verify external references).
- **Formatting/style nitpicks** — Removed per hard rules.

---

## Novel Insights

The paper's key insight is that the pooled text embedding, while largely redundant for *propagating* prompt information (attention does that), can be repurposed to *guide* the model toward better generation modes. This reverses the prevailing trend of discarding the pooled embedding: rather than being useless, it is useful in a way the field had overlooked. The finding that a simple step-function dynamic (skipping early layers) improves the trade-off over constant guidance is a practical discovery that could be adopted in other guidance frameworks.

---

## Suggestions

1. Add a short table or sentence in Section 5 stating the default dynamic guidance parameters (*i* and *w* ranges) used across the experiments, so practitioners can reproduce results without consulting the appendix.
2. Include in the main text (or at least the appendix summary) the number of annotators and the significance test used for the human evaluation's "statistically significant" markers.
3. Add a brief discussion of why the Defects metric does not benefit from guidance — is there a ceiling effect, or does the guidance introduce its own artifacts?

---

## Score and Decision

**Score:** 6.0

**Decision:** Accept

The paper makes a well-motivated, clean contribution that is supported by extensive experiments across models and tasks. The weaknesses are minor and primarily relate to presentation completeness (parameters in main text, human eval statistics) and mild scope limitations (specific changes on one model). The core idea — repurposing an underutilized signal as a training-free guidance mechanism — is both novel and practical, and the empirical validation is among the most thorough I have seen for a training-free guidance paper. There are no fundamental issues with methodology or unsupported claims.

---

**Calibration Anchor Summary:**
- **Round 1 topic-low:** Papers scoring 1.5–3.4 — share no relevant failure modes with the paper under review.
- **Round 1 topic-mid:** Universal Guidance (5.25), Dreamguider (4.00), Momentum Guidance (5.33), ContextDiff (6.25). Our paper is stronger than the first three and comparable to ContextDiff with different trade-offs (less theory, broader experiments).
- **Round 1 topic-high:** Transfusion (7.60), Würstchen (8.00), CADS (8.00) — top-tier work not directly comparable.
- **Round 1 weakness queries:** Dynamic Negative Guidance (6.25) — comparable; our paper has broader evaluation. State & Image Guidance (6.00, rejected) — our paper is cleaner and has fewer methodology issues.
- **Round 2:** VDT (6.00), State & Image Guidance (6.00), Unlocking Guidance (6.50) — our paper is in the same quality band.
- **What low-band anchors failed at:** Unsupported claims, lack of novelty, poor methodology, inadequate evaluation. The paper under review shares none of these.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>