I've now verified all claims from both reviewers against the paper. Let me write the consolidated review.

## Summary

This paper challenges the prevailing multi-component paradigm in LoRA-based multi-task learning (MTL). The authors first show that a simplified multi-head variant (M-LoRA), despite exhibiting high inter-head similarity, outperforms complex diversity-enforcing counterparts like HydraLoRA and R-LoRA. They then demonstrate that a standard single-adapter LoRA with increased rank can match the performance of multi-component architectures. Based on these findings, the authors hypothesize that learning task-shared representations is more effective than architecturally isolating task-specific features. They propose Align-LoRA, which adds a KL-divergence or MK-MMD based alignment loss to explicitly align task representations in the shared low-rank space. Experiments across Qwen2.5 (3B/7B/14B), LLaMA2 (7B/13B), and LLaMA3-8B on both in-domain and out-of-domain (BBH) benchmarks show consistent improvements.

## Strengths

- **M-LoRA challenges the necessity of head diversity.** The paper empirically demonstrates that a simplified multi-head variant with median inter-head cosine similarity exceeding 0.85 outperforms HydraLoRA and R-LoRA, which explicitly enforce diversity. Table 1 shows M-LoRA achieving the highest average score (75.45) across five tasks. Figure 2 directly visualizes this paradox, contradicting the prevailing assumption that component diversity is required for multi-task adaptation.

- **High-rank single-adapter LoRA matches multi-component architectures.** The paper shows that a standard LoRA with sufficiently increased rank (e.g., rank 30 on LLaMA2-7B, rank 10 on Qwen2.5-7B) achieves performance competitive with complex multi-adapter and multi-head systems. Table 2 shows LoRA† (rank 30) reaching 42.24 on LLaMA2-7B, exceeding HydraLoRA (40.30). This questions the fundamental necessity of multi-component designs.

- **Align-LoRA achieves consistent improvements across model families and scales.** The proposed method consistently outperforms all baselines across Qwen2.5 (3B/7B/14B), LLaMA3-8B, and LLaMA2 (7B/13B) on both BBH generalization (Table 4) and in-domain benchmarks (Table 5), while using fewer trainable parameters. A-LoRA-K achieves 50.28 on Qwen2.5-7B BBH vs. the best multi-head baseline at 48.44, and these gains replicate across multiple model scales.

- **Zero inference overhead.** Unlike multi-component variants with non-mergeable routers, Align-LoRA retains full mergeability with the backbone, a practical advantage for deployment.

## Weaknesses

### Major

- **No measures of variance or statistical significance are reported for any result.** Every table reports single-run point estimates. Given that some performance gaps are modest (e.g., Table 3: LoRA^10=49.51 vs. M-LoRA=49.74 on Qwen2.5-7B; Table 2: LoRA†=42.24 vs. M-LoRA=42.83), it is impossible to assess whether improvements are reliable or within noise. Without multi-seed reporting or significance tests, the empirical claims — especially the more nuanced comparisons — are unsubstantiated. This is a standard expectation in LLM fine-tuning work and is the single most impactful weakness.

- **The alignment loss relies on a strong, unvalidated parametric assumption.** The paper models each task's low-dimensional representation distribution as a multivariate Gaussian with diagonal covariance, estimated from a single batch (Section 5.1). This assumption is neither justified (e.g., via normality tests) nor validated (e.g., by comparing with a non-parametric alternative). The diagonal covariance ignores cross-dimension correlations. If the Gaussian assumption is violated, the KL divergence is not measuring what it claims, and the alignment loss could be optimizing a spurious objective. While the MK-MMD variant (A-LoRA-M) is non-parametric and partially mitigates this concern, A-LoRA-K (which shows stronger results) depends on this assumption.

- **The central causal claim is supported by circumstantial evidence.** The paper argues that "learning task-shared representations" causes the observed improvements. However: (a) M-LoRA's success could come from removing the router (simplifying optimization) rather than from shared representations; (b) the high-rank LoRA's success could come from increased capacity rather than shared features. While Align-LoRA provides a more direct test by explicitly aligning representations, it does not compare against a method that *explicitly* enforces task-specific separation under a fair experimental setup, leaving the causal claim somewhat undersupported.

### Minor

- **The dropout mechanism is claimed as critical but never ablated.** The paper states that "multi-head dropout is the critical factor" (Section 3.3) for M-LoRA's success. However, the only ablation performed is removing the router from HydraLoRA (which lacks dropout). To properly validate that dropout is critical, the paper should test M-LoRA *without* dropout — if performance drops, the claim is supported; if not, the mechanism is misattributed.

- **The theoretical analysis is a standard domain adaptation bound, not a genuine LoRA-specific contribution.** The generalization bound in Appendix F is a standard bound (e.g., Ben-David et al., 2006) repackaged for multi-task learning. It does not incorporate any LoRA-specific properties (rank constraints, parameter count) and does not provide actionable insight beyond what is already known from domain adaptation theory. The derivation also uses unverified assumptions (balanced task sizes for the confidence term simplification, an undefined Lipschitz constant Λ). It does not meaningfully strengthen the paper.

- **Some results in Table 2 are not re-run locally.** Table 2 marks results for LoRAHub* and LoRA MoE* as taken from Tian et al. (2024). While HydraLoRA, R-LoRA, and M-LoRA are re-run, cited results may use different hyperparameters or data splits, making comparisons uneven.

- **The M-LoRA+Align experiment (Appendix I) partially complicates the narrative.** Adding alignment to M-LoRA (M-LoRA+Align in Table 9) further improves performance, sometimes matching or exceeding A-LoRA-K alone. If M-LoRA's success is due to heads already learning shared representations, explicit alignment should not help much. That it does suggests M-LoRA was not fully aligned, weakening the claim that implicit shared representations alone explain its performance. The paper acknowledges this but does not fully reconcile the tension.

- **Figure 3 (λ sensitivity) lacks baseline markers for direct comparison.** The text claims Align-LoRA "consistently outperforms baselines across various λ values," but the figure does not include baseline performance lines (e.g., LoRA, R-LoRA). The y-axis range (74.0–75.75) is also narrow, so the performance variation across λ is modest, which undercuts the strong claim of sensitivity analysis.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- Multi-seed runs with standard deviations for all key tables would resolve the primary statistical concern.
- Validating the Gaussian assumption (e.g., QQ plots or normality tests for the A-output representations) would strengthen the alignment loss's legitimacy.
- Testing on more heterogeneous task sets (e.g., including code generation or translation tasks) would probe the limits of the shared-knowledge hypothesis.
- Analyzing the "over-alignment" phenomenon (mentioned in Appendix I.1) more quantitatively — e.g., by tracking pairwise KL between tasks as a function of λ.
- Including baselines on Figure 3 would make the hyperparameter sensitivity analysis clearer.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *Criticism about Figure 2 y-axis inconsistency*: The harsh critic claimed the text says medians exceed 0.85 but the plot shows lower values. The figure rendering from the PDF parser is garbled, making independent verification impossible. This may be a parser artifact rather than a real discrepancy.
- *Complaint about "matches or even outperforms" being overstated*: The data in Tables 2-3 show approximate parity with slight advantages in different settings. The paper's phrasing "competitive with, and at times superior to" is factually accurate.
- *Claim that the alignment choice (output of A) is unfounded*: The paper explicitly cites prior work (Agiza et al., 2024; Wang et al., 2024; Tian et al., 2024) showing that A learns task-general features. While independent verification would strengthen the paper, this criticism overstates the issue.
- *Strength Finder claim about "comprehensive theoretical validation"*: The theoretical bound is standard and not genuinely LoRA-specific. This strength is dropped as inflated.
- *Strength Finder's claim about "attention-only structures" (Appendix H.1) confirming robustness*: This is a genuine supporting experiment, but the descriptor "comprehensive" overstates it.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report multi-seed means and standard deviations for all key experiments.** This is the single highest-priority revision. Without it, the paper's quantitative claims cannot be properly evaluated.

2. **Validate or relax the Gaussian assumption for the KL-based alignment loss.** Either show that the per-task representations are approximately Gaussian (e.g., via statistical tests) or replace the KL divergence with a non-parametric alternative (the MK-MMD variant already partially addresses this, but A-LoRA-K is the stronger performer).

3. **Add an ablation of M-LoRA without dropout** to directly test the claim that multi-head dropout is the critical mechanism.

4. **Include baseline performance lines in Figure 3** to support the claim of "consistently outperforming baselines across various λ values."

5. **Temper the causal claim** from "shared representations cause improvements" to "shared representations are a correlate of improved performance, and explicit alignment is an effective strategy" — this better matches the evidence.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| **MeTA-LoRA** (`x6c72680uD.md`) | 4.50 | Similar topic (LoRA MTL). Both lack CIs and have incremental methods. This paper has a stronger central empirical challenge (M-LoRA paradox) and cleaner motivation. |
| **Scalable MTL LoRA** (`L3RSb9yTlL.md`) | 5.50 | More technically sophisticated method with SVD-based analysis. Accepted (poster). This paper has a simpler but clearer contribution; however, the statistical rigor is inferior. |
| **ThanoRA** (`6XoyxxAfv3.md`) | 4.00 | Also about multi-task LoRA. Criticized for limited task scale. This paper has broader model coverage but similar methodological concerns. |
| **Rethinking Parameter Sharing** (`noNpK9Vt8l.md`) | 3.50 | Criticized for contradictory motivation and missing CIs. This paper has a more coherent narrative and more extensive experiments. |
| **Neural Collapse in MTL** (`M4t2JUMlfI.md`) | 6.50 | Strong theoretical contribution. Accepted (poster). This paper is empirical rather than theoretical, making direct comparison difficult, but it lacks the foundational novelty of this anchor. |
| **Mechanistic Interpretability Variance** (`YD1P4DVtdk.md`) | 3.00 | Different topic. Low score due to thin contribution. Far weaker than the current paper. |

The paper sits between the 4.0–5.5 range on the anchor scale. It is stronger than ThanoRA (4.0) and MeTA-LoRA (4.5) due to cleaner motivation and more consistent experimental results across model families. However, it is clearly weaker than the 5.5-level accepted paper (Scalable MTL LoRA), which had more technical sophistication and depth despite sharing the missing-CI issue. The central empirical finding (M-LoRA paradox) is genuinely interesting, but the statistical rigor gap and unvalidated assumptions in the main proposed method prevent it from reaching acceptance level.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>