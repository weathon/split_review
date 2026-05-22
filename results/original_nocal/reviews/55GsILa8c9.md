Here is the final consolidated review.

---

## Summary

CausalNovo introduces a model-agnostic framework for *de novo* peptide sequencing that uses domain knowledge about expected fragment ions (b, y, a) to identify signal versus noise peaks, then applies causal-inspired learning objectives — contrastive invariance to noise-peak perturbations, sufficiency of the causal representation for label prediction, and an auxiliary purification loss — to learn representations that focus on signal. Across three public datasets (Nine-species, Seven-species, HC-PT) and three baseline architectures (CasaNovo, AdaNovo, π‑HelixNovo), CausalNovo delivers consistent and often substantial improvements at amino-acid, peptide, and PTM levels, with strong evidence from ablation studies, cross-species validation, and noise-robustness analysis.

## Strengths

- **Consistent and substantial empirical gains.** On the Seven-species dataset, CausalNovo improves π‑HelixNovo's amino-acid precision from 0.465 to 0.536 (+7.1 pp) and peptide precision from 0.218 to 0.282 (+6.4 pp). On HC-PT, improvements range from +9.0% to +14.2% in amino-acid precision across the three baselines (Table 1). PTM-level improvements are similarly large (e.g., +15.1% precision for π‑HelixNovo on Seven-species in Table 2).

- **Model-agnostic framework.** CausalNovo is successfully integrated with three distinct architectures (CasaNovo, AdaNovo, π‑HelixNovo), with Table 1 showing improvements for every baseline on every dataset. This supports generality rather than architecture-specific tuning.

- **Systematic ablation studies.** Table 4 isolates the contribution of each component: the independence principle (+2.3% peptide precision), purification (+0.8%), and symmetric training (+0.4%). Table 5 similarly ablates replace-based perturbation and causality enhancement, showing each contributes.

- **Cross-species validation.** Table 3 shows CausalNovo improves CasaNovo on all eight species in the Nine-species dataset (peptide-precision gains from +0.8% to +3.7%), confirming generalization across diverse proteomes.

- **Robustness across noise-signal ratios.** Figure 4 shows CausalNovo maintains higher precision than baselines across the full NSR range (0–10) on HC-PT, with average improvements of +10–12%. This is a cleaner robustness test than the vulnerability analysis because NSR is a global measure the method was not explicitly trained to optimize.

- **Attention analysis provides mechanistic evidence.** Table 7 shows the proportion of predictions attending to three causal peaks increases from 19.26% (baseline) to 32.87% (CausalNovo), and the proportion ignoring causal peaks entirely drops from 12.73% to 10.76%. This directly supports the claim that the model shifts focus to signal peaks.

## Weaknesses

### Fatal

None. The paper's core empirical contributions are sound and well-supported by the experiments. The causal framing is overstated but does not invalidate the method or its results.

### Major

- **Overclaimed causal framing and partial circularity in vulnerability evaluation.** The identification of "causal" (signal) vs. "non-causal" (noise) peaks relies on computing a theoretical spectrum from the *ground-truth peptide label* during training (Section 3.4.1, Equation 4). This is valid domain-knowledge injection and follows standard practice in proteomics (the paper cites Mao et al. 2023, Klaproth-Andrade et al. 2024, Qiao et al. 2021), but it is not causal discovery from observational data — it is supervised noise masking driven by the label. The vulnerability analysis (Figures 1, 3) then evaluates by perturbing the *same oracle-defined* noise peaks, creating a test that the method was explicitly trained to pass. This confound weakens the claim that the method has a principled causal advantage. The NSR analysis (Figure 4) and cross-species validation (Table 3) are cleaner tests that partially mitigate this, but the paper should have acknowledged this circularity and presented additional evaluations (e.g., perturbing signal peaks, evaluating on datasets with substantially different noise structure) to separate the causal framing from the practical noise-masking.

- **Missing perturbation of signal peaks.** The vulnerability analysis only replaces noise peaks. Without evaluating how performance degrades when *signal* (causal) peaks are perturbed, it is impossible to determine whether CausalNovo genuinely focuses on signal or simply has generally lower sensitivity to all peaks. This experiment is a direct, falsifiable test of the core claim.

- **Strong, unverified independence assumption.** The SCM (Section 3.2, Equation 2) assumes C ⟂ S (causal and non-causal factors are independent). This structural assumption is motivated by Reichenbach's Common Cause Principle but is neither empirically verified (e.g., by measuring dependence between learned z_c and z_s) nor discussed in terms of when it might be violated (e.g., co-elution creating dependence between noise and analyte). The independence objective in practice enforces *invariance to perturbation*, not statistical independence between latent factors, which are related but not equivalent.

### Minor

- **Purification objective lacks theoretical grounding.** The claim that maximizing I(z_s; Y) "indirectly lead[s] to the purification of z_c" (Section 3.3) is stated without formal argument. The ablation (Table 4) shows only a +0.8–0.7% gain, which could arise from a simple ensemble or regularization effect rather than principled disentanglement. The paper provides no analysis of what information z_s actually captures, making the "purification" mechanism unsubstantiated.

- **No analysis of z_s content.** The non-causal representation z_s is trained to predict the label Y via cross-entropy (Equation 6), but the paper never examines what z_s encodes. If z_s captures meaningful signal (e.g., precursor charge, instrument effects), then the "non-causal" label is misleading. If it captures pure noise, training it to predict Y is counterintuitive. Either way, the lack of analysis leaves a gap in the claimed disentanglement.

- **The replace-based perturbation as an SCM intervention is approximate.** The paper acknowledges S is unobservable and uses the label to infer noise peaks. The replacement samples from noise peaks in the batch, which changes the distribution of S but does not guarantee the intervention is independent of C (new noise peaks from the batch may correlate with C). The causality-enhancement step (adding back all theoretical peaks, x_intervene = x_replace ∪ x_theory) further mixes signal and noise in the intervened spectrum. These are reasonable engineering approximations, but the paper's causal language (do(S), principled intervention) implies a rigor the method does not deliver.

### Trivial

- 2.3× training-time overhead is honestly reported but not negligible. The paper acknowledges this.

## Nice-to-Haves

- Analysis of what information z_s captures (e.g., does it encode instrument effects, precursor charge?).
- Perturbation of *signal* peaks to test whether CausalNovo truly focuses on signal rather than just having lower sensitivity to all peaks.
- Evaluation of independence between learned z_c and z_s via mutual information estimation.
- Evaluation on a dataset with a substantially different noise distribution (e.g., different instrument type, known co-elution contaminants).

## Removed Points

*These points were flagged by reviewers but are removed or demoted for the reasons given below. Treat with caution.*

- **Harsh critic's claim that "the causal framework is built on an oracle that defeats the stated purpose" as a fatal/structural issue.** The criticism is factually correct — the method uses ground-truth labels to identify noise peaks — but calling this "fatal" is too strong. The paper never claims to do causal discovery from unlabeled observational data; it states this is established domain knowledge (Section 3.4.1, lines 113), and the core contribution is an empirically effective framework. The point is retained as **Major** (overclaimed framing), not fatal.
- **Harsh critic's claim that "the model can simply route predictive information through z_s, undermining the goal of making z_c the sole carrier."** This is partially inaccurate: the decoder only uses z_c for the main prediction; z_s is trained with its own CE loss but not fed to the decoder. The concern is about the purification objective's interpretation, not about prediction routing. Merged into the Minor weakness about purification lacking theoretical grounding.
- **Harsh critic's naming of "purification objective" as a separate fatal/methodology gap.** The gains are small but real in the ablation. The criticism is demoted from "methodological gap" to Minor since the paper does present empirical evidence, even if the theoretical reasoning is thin.
- **Strength Finder's generic strengths** (e.g., "paper is well-structured and clearly written", "addresses an important problem"): removed as generic/superficial. Only concrete, evidence-backed strengths retained.
- **Strengths that conflict with verified weaknesses** (e.g., "vulnerability analysis directly supports the claim that CausalNovo learns causal rather than spurious associations"): removed because the vulnerability analysis has a partial circularity issue that weakens this claim. The practical insight (baselines rely on these noise peaks) is acknowledged, but the causal-interpretation strength is dropped.

## Novel Insights

None beyond the paper's own contributions. The key tension highlighted by the cross-reviewer analysis — that the causal framing is partly rhetorical while the practical noise-masking and data-augmentation scheme is genuinely effective — is an apt characterization of the paper's actual contribution versus its packaging.

## Suggestions

1. **Tone down the causal framing.** Reframe the contribution as "domain-informed noise-masking with causal-inspired learning objectives" rather than claiming principled causal disentanglement. The method's value is clear without overclaiming.
2. **Add signal-peak perturbation** to the vulnerability analysis. Replacing or adding noise to signal peaks would provide a direct test of whether CausalNovo genuinely focuses on signal.
3. **Analyze z_s content.** Show what the non-causal representation captures (e.g., via probing tasks or visualization) to validate the claimed disentanglement.
4. **Acknowledge the evaluation circularity explicitly** in Section 4.4 and note that the NSR and cross-species analyses provide the cleaner tests.
5. **Measure independence** between learned z_c and z_s (e.g., through simple correlation or mutual information estimation) to verify the C ⟂ S assumption at the representation level.

## Score and Decision

**Originality:** 6/10 — The causal framing and combination of objectives is novel for this domain, though the individual components (theoretical-spectrum-based noise identification, contrastive learning, cross-entropy purification) are established techniques.

**Importance of research question:** 8/10 — Robust *de novo* peptide sequencing is practically important in proteomics, and the demonstrated gains are meaningful.

**Claims well-supported:** 7/10 — Empirical support is strong and multi-faceted; the causal framing is overclaimed relative to what the experiments actually show.

**Soundness of experiments:** 8/10 — Thorough ablations, cross-species validation, NSR analysis, attention analysis. The main gap is the missing signal-perturbation experiment.

**Clarity of writing:** 8/10 — Well-structured, clear motivation, methods explained in logical order.

**Value to the community:** 7/10 — The framework is practical, model-agnostic, and delivers real gains. The code release and clear methodology support reproducibility.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>