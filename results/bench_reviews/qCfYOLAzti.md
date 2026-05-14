Now I have enough context to write the final review. Let me verify one more detail from the paper — the strength finder's claim about MUSE-Books VerbMem/KnowMem going to zero.

I've now verified the key claims. Let me compile the final review.

---

## Summary

This paper identifies a failure mode in LLM unlearning called the "squeezing effect": gradient-ascent-based methods redistribute probability mass into high-likelihood alternatives (paraphrases), producing spurious unlearning where models appear to forget but still leak sensitive knowledge through semantically rephrased outputs. To address this, the authors propose a bootstrapping (BS) framework that jointly suppresses target responses and the model's own high-confidence predictions (model beliefs). BS-T operates at the token level by forming soft targets that interpolate between one-hot labels and top-k model predictions; BS-S augments the forget set with full high-confidence sequences sampled from the model. Theoretical analysis under the AKG learning dynamics framework shows how BS reshapes gradient residuals to spread forgetting pressure across belief neighborhoods. Experiments on TOFU, WMDP, and MUSE across multiple model families demonstrate consistent improvements over baselines.

## Strengths

- **Well-motivated problem identification with empirical diagnostics**: The paper demonstrates the squeezing effect through two complementary analyses — LaaJ-based semantic similarity across likelihood bands (Fig. 2a) and log-probability dynamics tracking during unlearning (Fig. 2b,c) — providing concrete evidence that NPO-based methods produce only superficial forgetting. This is a genuinely under-explored failure mode in the unlearning literature.

- **Simple, principled, and compatible method**: BS-T and BS-S are straightforward to implement on top of existing unlearning pipelines. The ablation in Table 6 (Appendix F.5) shows that BS-S improves aggregate scores when combined with GA, NPO, or WGA losses, demonstrating framework generality rather than coupling to a specific base loss.

- **Comprehensive experimental coverage**: The paper evaluates on three standard benchmarks (TOFU, MUSE, WMDP), three model families (Llama 3.2 1B/3B, Llama 3.1 8B, Llama 2 7B-Chat, Zephyr-7B-β), and multiple forget ratios (1%/5%/10% on TOFU). BS-S consistently achieves best aggregate memorization–utility balance across settings.

- **Correct theoretical analysis connecting method to mechanism**: Theorem 5.2 shows that BS-T's residual (`π - ((1-λ)e + λq)`) spreads the forgetting signal across the target token and its high-likelihood neighborhood, in contrast to GA's residual (`π - e`) which concentrates on a single token. Theorem 5.3 extends this to off-policy BS-S as kernel-weighted BS-T residual aggregation. The analysis is mathematically consistent with the defined objectives.

- **Code released and integrated into OpenUnlearning**, facilitating standardized benchmarking and reproduction.

## Weaknesses

### Fatal

None.

### Major

None. The harsh critic's claim of a sign error in the theoretical analysis is incorrect. The paper defines GA's objective as `min_θ -E[log π]` (Eq. 1), i.e., minimizing negative log-likelihood. Under this loss, the residual `G = ∇_z L` is indeed `π - e` (standard softmax gradient), which is consistent with the derivation in Appendix D.2. The BS-T residual `π - ((1-λ)e + λq)` follows identically from the BS-T loss (Eq. 6). There is no sign mismatch between the algorithm and the analysis.

### Minor

- **Modest improvements in many cells without statistical testing**: On TOFU 10% with Llama 3.1 8B, the aggregate improvement of BS-S over NPO is 0.63 → 0.64; on TOFU 5% 1B it's 0.54 → 0.55. These 1–2 percentage-point gains appear consistently but are small in absolute terms. No standard deviations, confidence intervals, or multi-seed variance is reported, making it difficult to assess whether observed differences are reliable. This is a common practice in LLM unlearning benchmarks but still worth noting.

- **LaaJ evaluation is uncalibrated**: The semantic similarity and naturalness judgments (Figs. 2a, 4c) use a single proprietary model (Gemini 2.5 Flash) with no human calibration, inter-annotator agreement analysis, or multi-judge comparison. The paper appropriately uses LaaJ as an auxiliary probe rather than the primary evaluation (Tables 1–2 use standard metrics), but the strength of conclusions drawn from the LaaJ analysis (e.g., "BS-T and BS-S achieve higher naturalness and lower similarity than baselines") would benefit from validation.

- **Theoretical analysis applies a known framework rather than developing new theory**: The AKG decomposition is imported from Ren & Sutherland (2025). The paper's contribution is applying this framework to compare GA vs. BS-T residuals, which is valuable but incremental as theory. The on-policy BS-S variant used in practice falls outside the theoretical framework (acknowledged in Appx. D.4).

### Trivial

- The term "bootstrapping" is somewhat overclaimed — the mechanism is essentially unlikelihood-style suppression using the model's own predictions as soft targets. This is a presentation issue, not a technical flaw.

## Nice-to-Haves

- A comparison of BS-S against an equally-sized dataset of external human-written paraphrases would help disentangle whether the gains come from "model beliefs" specifically or simply from having more forget examples.

- Reproducing the squeezing-effect log-probability analysis (Fig. 2) on MUSE or WMDP in addition to TOFU would strengthen the generality claim.

- The LaaJ evaluation could be strengthened with a small human validation study or at minimum multi-judge agreement analysis.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

1. **Harsh critic's sign-error claim ("Theoretical analysis is mathematically inconsistent...")**: Removed. The paper's Eq. (1) defines GA as `min_θ -E[log π]`, i.e., minimizing NLL. The gradient of this loss w.r.t. logits is `π - e`, which is exactly the residual in Theorem 5.2. Appendix D.2 (lines 1820-1825, 1853-1859) derives both residuals correctly from the respective loss functions. The harsh critic appears to have misread the sign convention.

2. **Harsh critic's loss-formulation-mismatch claim**: Removed. Same issue as above — the pseudocode (Alg. 1) performs gradient descent on `L_BST` (Eq. 6), and the residual `G_BST` is computed as `∇_z L_BST`. These are consistent.

3. **Strength Finder's claim about MUSE-Books VerbMem/KnowMem "driven to zero"**: Kept but contextualized. The zero scores are indeed achieved (Table 5), but GradDiff and WGA also achieve zero scores, so this is not unique to BS. The BS advantage is in higher UtilPres at zero forget scores.

4. **Harsh critic's demand for human evaluation**: Moved to Nice-to-Haves. The paper uses LaaJ as an auxiliary probe, not the primary evaluation. Human calibration would strengthen but is not a standard requirement in this subfield.

5. **Harsh critic's demand for squeezing analysis on multiple datasets**: Moved to Nice-to-Haves. The TOFU analysis is sufficient to establish the phenomenon; extending to other benchmarks would add value but is not a weakness of the current analysis.

## Novel Insights

The paper's central insight — that the softmax normalization constraint causes GA-based unlearning to redistribute rather than eliminate probability mass, and that incorporating model beliefs as auxiliary suppression targets directly counteracts this — is genuinely novel in the LLM unlearning literature. While the AKG framework itself is borrowed, the application to diagnose and address the squeezing effect in unlearning is original. The empirical characterization through log-probability band tracking (Fig. 2) provides an intuitive diagnostic tool for future work.

## Suggestions

- Report variance estimates across at least 3 random seeds for the main TOFU results to help readers assess the reliability of the modest gains.
- Clarify the distinction between the auxiliary LaaJ evaluation (used for diagnosing spurious unlearning) and the primary benchmark evaluations to avoid overclaiming the robustness of LaaJ-based conclusions.
- Consider tempering the "bootstrapping" terminology, as the method is more precisely described as self-distillation-style suppression.

---

**Anchor comparison for calibration:**

| Anchor | Avg Score | How it compares |
|--------|-----------|-----------------|
| `/home/wg25r/review_agent/human_reviews_2026/r6Z3BXDrzO.md` (Impossibility of Retrain Equivalence) | 4.50 | Similar theoretical+empirical scope but diagnostic only; current paper adds a constructive method, making it stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/qd9fA4LzVN.md` (Label Smoothing Improves GA) | 4.50 | Simpler method contribution with less theoretical analysis; current paper is more comprehensive. |
| `/home/wg25r/review_agent/human_reviews_2026/7cEMkTu7Lf.md` (Unlearning Isn't Deletion) | 4.00 | Identifies problem (reversibility) but offers no method; current paper is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/Sswng2ToR4.md` (Downgrade to Upgrade) | 4.50 | Accept Poster with similar strength profile; current paper has better theoretical grounding and broader experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/rzi77zNngG.md` (Leak@k) | 4.00 | Metric contribution only; current paper also provides a method and theory. |
| `/home/wg25r/review_agent/human_reviews_2026/nxMR2NGFik.md` (Full-Stack View) | 3.50 | Taxonomy/survey; current paper is a primary research contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/odMc2ZRGcw.md` (BLUR) | 2.50 | Benchmark paper; current paper is substantially stronger. |

The paper under review is clearly above the 3.50–4.00 tier and compares favorably to the 4.50 anchors, offering both problem identification and a constructive solution with theoretical grounding. The modest gains and lack of statistical testing prevent a higher score but do not undermine the core contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>