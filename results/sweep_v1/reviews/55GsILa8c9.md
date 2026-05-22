## Summary

CausalNovo introduces a model-agnostic framework for de novo peptide sequencing that uses causal representation learning principles to encourage models to focus on true signal fragment ions (b/y/a ions) rather than spurious noise peaks. The method operationalizes an SCM-based formalization via a Causality Extraction Module that disentangles causal and non-causal representations, a replace-based causal intervention on noise peaks, and information-theoretic objectives (independence, sufficiency, purification). Experiments across three public benchmarks and three strong baselines (CasaNovo, AdaNovo, π-HelixNovo) show consistent gains of up to 10%+ in amino acid, peptide, and PTM-level metrics, with particularly compelling robustness results under noise perturbation and across varying noise-signal ratios.

## Strengths

1. **Consistent and sizable empirical gains across multiple baselines and datasets.** CausalNovo improves all three baseline models (CasaNovo, AdaNovo, π-HelixNovo) on all three benchmarks (Nine-species, Seven-species, HC-PT). Gains are material — e.g., +12.4% amino acid precision on HC-PT for π-HelixNovo (Tables 1–2) — and cover amino acid, peptide, and PTM-level metrics. This model-agnostic effectiveness is the paper's strongest empirical result.

2. **Robustness evidence from vulnerability analysis and NSR analysis.** Under systematic noise-peak perturbation (Figures 1, 3; Table 6), baseline models degrade sharply while CausalNovo variants maintain far higher precision — achieving up to 28.5% relative improvement on HC-PT (threshold=1). The NSR analysis (Figure 4) further shows that CausalNovo maintains higher precision across the full range of noise-signal ratios. These analyses directly support the claim that the model learns to rely on signal rather than noise.

3. **Component ablation validates each design choice.** Ablation (Table 4) shows that removing the independence principle, purification objective, or symmetric contrastive training each degrades performance. The causal intervention ablation (Table 5) separates the contributions of replacement vs. enhancement. This provides clear evidence that the framework's components are individually meaningful.

4. **Cross-species validation confirms generalization.** Leave-one-out experiments over 9 species (Table 3) show CausalNovo improves peptide precision on every species (average +2.6%), indicating the framework does not overfit to a specific biological source.

5. **Attention analysis provides mechanistic evidence of behavioral change.** Table 7 shows CausalNovo increases the fraction of predictions attending to three causal peaks from 19.26% to 32.87%, and reduces total neglect of causal peaks from 12.73% to 10.76%. This links the performance improvement to the intended mechanism.

## Weaknesses

### Fatal
None. No verified weakness invalidates the core claims.

### Major

1. **Conditional mutual information objective is not implemented with proper conditioning on Y.** The paper formulates the independence principle as maximizing $I(z_c; z_c' \mid Y)$, then approximates it with a standard contrastive loss (Eq. 5) where the negative set $\mathcal{N}$ is simply the current batch — not samples matched on $Y$. The paper provides no argument or ablation showing that this unadjusted contrastive loss actually approximates the *conditional* mutual information. This creates a clear gap between the stated theoretical objective and what is actually optimized, weakening the causal grounding claim. The approach may still work as a practical regularization, but the claimed theoretical justification is unsupported.

2. **Label-based noise identification during training conflates causal intervention with oracle knowledge.** The identification of non-causal ions (Eq. 4) uses the ground-truth peptide sequence to compute the theoretical spectrum. Both the training-time intervention (noise replacement) and the vulnerability analysis therefore depend on oracle knowledge of the label. The paper notes this is standard domain practice (citing prior work), and it certainly does not invalidate the empirical results, which compare fairly against baselines evaluated under the same protocol. However, it undercuts the strict causal framing: the "intervention on $S$" is not truly independent of the effect $Y$ — it uses $Y$ to define which peaks to perturb. Removing or relaxing this dependence (e.g., using a pretrained model to estimate noise) would substantially strengthen the causal claims.

3. **Disconnect between the SCM formalization and the learning objectives.** The transition from the structural equations (Eq. 2) to the specific contrastive and cross-entropy losses is abrupt. The property $C \perp S$ justifies the independence objective, but no formal derivation connects the SCM to the particular losses used. The paper could benefit from a clear theoretical chain: SCM → principles → objectives → practical losses. As presented, the SCM feels decorative rather than operational.

### Minor

1. **No error bars or statistical significance tests.** All tables report point estimates without variance. Given that many improvements are modest in absolute terms (2–5% on some metrics), it is unclear whether gains are statistically significant. While single-run evaluation is standard in the de novo sequencing literature, reporting results across multiple seeds (even for a subset of experiments) would improve confidence.

2. **The purification objective ($\max I(z_s; Y)$) has a confusing justification.** The paper claims maximizing mutual information between the non-causal representation $z_s$ and the label $Y$ "indirectly leads to the purification of $z_c$." The mechanism for this is not well explained. If $z_s$ is supposed to carry non-causal (noise) information, encouraging it to also predict $Y$ seems counterintuitive. The argument that this forces the model to separate shared information under the independence constraint could be clarified with a toy example or formal reasoning. While the ablation study confirms this objective helps empirically, the current explanation is hand-wavy.

3. **Attention analysis has a mild self-fulfillment concern.** The attention metric counts how often the model attends to peaks identified as "causal" by the same theoretical spectrum used during training. It is therefore unsurprising that the trained model attends more to these peaks. This does not invalidate the analysis — it confirms the training works as intended — but the claim that this provides independent evidence of learned causal focus is weakened.

### Trivial
None beyond typical formatting artifacts (parser issues, not author errors).

## Nice-to-Haves

- **Large-corpus evaluation protocol.** The paper acknowledges that recent methods (ContraNovo, RankNovo) use a more realistic protocol training on large external corpora and evaluating on OOD test sets. Adding this evaluation would substantially strengthen real-world relevance claims.
- **Label-free noise identification control experiment.** Training CausalNovo with noise peaks identified without ground-truth labels (e.g., using a pretrained model's uncertainty or spectral quality metrics) would directly address the label-leakage concern.
- **t-SNE/PCA visualizations** of $z_c$ vs. $z_s$ representations to confirm that causal and non-causal representations separate in latent space.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Label leakage fatally undercuts the causal claim"** — The paper openly acknowledges using ground-truth labels for noise identification (Section 3.4.1), notes this is standard in the field (citing prior works), and the evaluation is fair since baselines are tested under the same protocol. This is a limitation of the causal framing, not a fatal flaw. Demoted to Major.
- **"Purification objective is logically inconsistent"** — While the explanation is confusing, the ablation study shows it works empirically and similar ideas appear in Chen et al. (2022). The logic (shared information separated under independence constraint) is plausible even if under-explained. Demoted from Major to Minor.
- **"Related work draws no concrete line to proposed architecture"** — Generic; the related work section cites relevant CausalML papers and the connection (invariant representation learning, disentanglement) is clear.
- **"Replace-based perturbation may introduce systematic biases"** — Speculative without evidence; the empirical results consistently improve, suggesting any bias is not harmful.
- **"Attention analysis is self-fulfilling"** — This is a mechanistic validation, not a circular argument. The model is trained to attend to signal peaks, and the analysis confirms it does. Demoted from major concern to minor.
- **"Evaluation doesn't test most realistic setting"** — Acknowledged as future work. This is a limitation but not a weakness. Moved to Nice-to-haves.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's causal framing and its actual implementation: the method works well empirically as a domain-informed data augmentation and representation learning technique, but the strongest arguments for its effectiveness do not actually require the full causal inference apparatus. The vulnerability analysis (Table 6) and NSR analysis (Figure 4) convincingly show that the model learns noise-invariant representations, and the component ablations confirm each piece contributes. However, the claimed justification — maximizing conditional mutual information, performing genuine causal interventions — is not fully realized in practice. This suggests the paper would be better positioned as a robustness method that leverages domain knowledge (theoretical spectra) and representation-level regularization, rather than as a strictly causal framework. The empirical contributions are solid enough that they stand on their own without overclaiming the causal formalization.

## Suggestions

1. **Tone down the causal inference claims** and reframe the method as "causality-inspired" or "robustness-oriented" rather than strictly causal. The empirical results are strong enough that they do not need overclaimed theoretical grounding.
2. **Provide a label-agnostic noise identification baseline** (e.g., using a pretrained model) in a control experiment to decouple the causal framing from the label leakage.
3. **Replace or augment the conditional MI claim** with a proper justification for the unadjusted contrastive loss, or add an ablation where negatives are explicitly matched on $Y$.
4. **Add error bars** (at least 3 seeds) for the main results in Table 1 to establish statistical significance.
5. **Clarify the purification objective** with a formal argument or toy example showing why $\max I(z_s; Y)$ helps separate rather than conflate information streams.

---

## Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zMPHKOmQNb.md` (Protein Discovery with DWJS) | 8.00 | Stronger theory and wet-lab validation; CausalNovo is weaker on theoretical rigor |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3cuJwmPxXj.md` (Identifying Representations for Intervention Extrapolation) | 8.00 | Much stronger causal representation theory; CausalNovo has better applied results |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uQnvYP7yX9.md` (ReNovo) | 6.50 | Comparable task and gains; CausalNovo has more novel framework but more theoretical gaps |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/87B3zDRMjv.md` (RankNovo) | 5.50 | Modest improvements, less original approach; CausalNovo is stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/I2ZYngkRW6.md` (Distilling Non-Autoregressive) | 4.25 | Limited novelty; CausalNovo is substantially stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qac43AwuL9.md` (Optimal Causal Representations) | 6.00 | Similar causal representation theme but toy experiments; CausalNovo has more extensive evaluation |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/G536mmC2HL.md` (TorSeq) | 3.00 | Weak contribution; CausalNovo is much stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yIRtu2FJvY.md` (Matrix VAE) | 3.00 | Does not outperform baselines; CausalNovo has clear positive results |

**Score rationale**: CausalNovo sits above the mid-range peptide-sequencing papers (RankNovo at 5.5, Distilling at 4.25) due to its novel framework, model-agnostic nature, and thorough robustness analysis. It is comparable to ReNovo (6.5) — both achieve substantial improvements — but the theoretical gaps (unconditioned MI, label leakage) prevent it from reaching the 7+ band occupied by papers with rigorous theory or wet-lab validation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>