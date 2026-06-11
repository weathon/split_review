Now I have a thorough picture. Let me synthesize the comparisons.

**Anchor comparisons summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| CrossNovo (Distilling NAT) | 4.25 | R1 | Same domain, rejected. Much weaker: limited novelty, no theoretical grounding, engineering-heavy. Our paper clearly stronger. |
| RankNovo | 5.50 | R2 | Same domain, rejected. Model-agnostic reranking. Our paper: more principled causal framework, better ablations, broader evaluation, stronger improvements. |
| MADGEN | 6.00 | R2 | Mass-spec molecular generation, accepted. Similar empirical quality. Our paper: more thorough evaluation across architectures. |
| Causal RL Multimodal Bio | 5.80 | R1 | Causal + bio, accepted. More theoretical, less empirical. Our paper: more application-driven, empirically richer. |
| ReNovo | 6.50 | R1 | Same domain, accepted. Novel retrieval approach for de novo. Our paper: comparable empirical thoroughness, different innovation angle. |
| Celcomen | 6.67 | R2 | Causal disentanglement in biology, accepted. More theoretical. Our paper: more empirical breadth, comparable novelty in domain. |

**Final assessment**: CausalNovo sits between RankNovo (5.50, rejected) and ReNovo (6.50, accepted), closer to the ReNovo/Celcomen level. It has a major weakness around label-derived information in the causality enhancement step but this does not invalidate the core empirical contribution. It has strong ablation studies, cross-architecture generalization, and consistent improvements. **Score: 6.0, Accept.**

Now let me write the final review.

---

## Summary

CausalNovo is a model-agnostic framework that wraps around existing de novo peptide sequencing models to make them robust to non-causal (noise) peaks in tandem mass spectra. It formalizes the problem via a structural causal model (SCM) with two principles — independence (causal factors invariant under noise intervention) and sufficiency (causal factors contain predictive information) — and operationalizes them through a Causality Extraction Module (CEM) that learns per-peak importance masks. Training uses contrastive learning for invariance and cross-entropy losses on causal and non-causal representations. Evaluated across three architectures and three benchmarks, CausalNovo shows consistent gains up to ~10% in amino acid, peptide, and PTM-level metrics.

## Strengths

- **Strong empirical motivation via vulnerability analysis**: Figure 1 systematically demonstrates that state-of-the-art models (CasaNovo, AdaNovo, π-HelixNovo) degrade markedly when noise peaks are replaced, with tighter m/z thresholds amplifying the decline. This directly substantiates the claim that existing models rely on spurious correlations with non-causal ions.

- **Model-agnostic, cross-architecture performance gains**: Tables 1–2 show CausalNovo integrated with three architecturally distinct baselines on three datasets, with non-trivial and consistent gains (e.g., AdaNovo+CausalNovo improves AA precision by +14.2% on HC-PT; π-HelixNovo+CausalNovo achieves 0.787 on Nine-species). This cross-architecture generalization is compelling evidence the framework captures something fundamental.

- **Thorough component ablation**: Tables 4 and 5 systematically isolate each design choice — independence objective (+1.2% AA precision), replace-based perturbation (+0.6%), causality enhancement (+0.6%), purification (+0.8%), symmetric training (+0.4%). The drop-based perturbation is tested and shown ineffective, demonstrating the intervention design was carefully justified and not arbitrary.

- **Cross-species validation**: Table 3 evaluates on 8 species from the Nine-species dataset in a leave-one-out protocol, with CausalNovo improving peptide precision over CasaNovo for every single species (average +2.6%). This tests generalization beyond the standard yeast-held-out split.

- **NSR generalization analysis**: Figure 4 plots AA precision against noise-signal ratios from 0 to 10, showing CausalNovo maintains higher precision across the entire range with average improvements of +10.2% to +12.2% across baselines.

- **Interpretability evidence from attention analysis**: Table 7 shows the proportion of predictions where all three top-attended peaks are causal rises from 19.26% (baseline) to 32.87% (CausalNovo), providing mechanistic evidence that model behavior shifts in the intended direction.

## Weaknesses

### Fatal

None.

### Major

- **Label-derived information in the causality enhancement step undermines the causal narrative**: The "causality enhancement" constructs `x_intervene = x_replace ∪ x_theory`, where `x_theory` is the complete theoretical spectrum generated from the ground-truth peptide sequence Y (Section 3.4.1). This injects label-derived peaks into the contrastive branch's positive view, meaning the contrastive objective may teach the model to attend to peaks matching the theoretical spectrum heuristic rather than genuinely discovering causal mechanisms independent of the label. The ablation shows removing enhancement drops AA precision from 0.753 to 0.747 (Table 5, a 0.6% gap), so the method does not hinge on this component, but the paper's claim of learning genuine causal representations is weakened. The paper should either acknowledge this tension or provide analysis ruling out label leakage as the operative mechanism.

### Minor

- **Vulnerability evaluation partially circular with training heuristic**: The perturbation-based vulnerability analysis (Figures 1, 3, Table 6) identifies "non-causal" peaks using the same theoretical-spectrum proximity criterion that CausalNovo uses during training to construct interventions. CausalNovo is therefore trained to focus on exactly the peaks this evaluation treats as causal and to be invariant to exactly the peaks the evaluation perturbs. This means the vulnerability analysis cannot serve as fully independent corroboration of causal robustness. The standard benchmark results (Tables 1–3) and NSR analysis (Figure 4) are free of this circularity and do show genuine improvement, which is what matters most.

- **Purification objective mechanism is theoretically underspecified**: Section 3.3 argues that maximizing I(z_s; Y) "indirectly lead[s] to the purification of z_c." Since the mask M is a sigmoid-gated soft partition (not a hard allocation) and both z_c and z_s receive cross-entropy losses toward Y (Eq. 6), the model could place all Y-relevant information in both branches simultaneously without purification. The ablation shows +0.8% AA precision from this objective (Table 4), so it helps empirically, but the paper should clarify what prevents the trivial solution or acknowledge it as an effective regularization whose causal interpretation is unclear.

- **Missing parameter-matched baseline**: The CEM adds 3 Transformer layers and an MLP head with hidden dimension 512 — roughly one-third of the encoder depth (Section 4.2). The paper does not ablate whether adding equivalent extra parameters to the baseline encoder without the causal objectives yields some of the observed improvement. This is a standard control for methods that augment architectures and would disentangle the effect of additional capacity from the causal training objectives.

- **Retrained baseline discrepancies deserve discussion**: CasaNovo's reported AA precision on Nine-species is 0.697 but retrained result is 0.741 (+4.4%); AdaNovo goes from 0.698 to 0.681 (−1.7%). These discrepancies are large enough to suggest the training setup (data splits, hyperparameters, hardware, framework versions) may differ meaningfully from the original implementations, and the paper attributes these solely to "same configurations" retraining without discussion.

- **SCM figure caption inconsistency**: Figure 2's caption describes C as "charge state" and S as "spectrum augmentation," while Section 3.2 defines C as "causal factors" and S as "non-causal factors." This suggests the figure and text evolved separately and should be aligned.

### Trivial

- The attention analysis metric (counting causal peaks among top-3 attended peaks, Table 7) is somewhat coarse; the baseline already shows 19.26% of predictions fully attending to causal peaks, which is non-trivial and somewhat complicates the narrative that baselines are heavily noise-dependent.

## Nice-to-Haves

- Concrete values for α (fraction of replaced peaks) and γ (tolerance threshold) are not specified in the main text; they may be in the stripped appendix but should ideally be in the main text for reproducibility.
- No standard deviations, confidence intervals, or significance tests are reported, making it difficult to assess whether small gains (e.g., +0.4% from symmetric strategy) are meaningful — though this is common in large-scale benchmark evaluations.
- The step from the causal independence condition P(C|S)=P(C|do(S)) to the contrastive mutual information objective in Eq. 5 could be more explicitly derived beyond the citation to Chen et al. (2022).
- The replace-based intervention samples replacement peaks from the same training batch, making the intervention distribution batch-dependent — unusual for a causal intervention meant to represent an external do(S) operation.
- Vulnerability evaluation under a perturbation criterion that differs from the training criterion (e.g., intensity-based perturbation rather than m/z proximity to theoretical spectrum) would provide cleaner evidence of general causal robustness.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The claim that noise peaks introduce 'spurious correlations that risk misleading statistical models' is presented without distinguishing between genuinely spurious associations and legitimate distributional features"** (from Harsh Critic). REMOVED — this is an overly philosophical distinction; the perturbation experiment in Figure 1 empirically demonstrates model degradation under noise replacement, which is sufficient motivation regardless of the semantic framing.

- **"The paper does not discuss what C represents concretely in proteomics terms"** (from Harsh Critic). REMOVED — Section 3.2 clearly defines C as "causal factors" and S as "non-causal factors" in the SCM. The abstraction level is appropriate for a principled framework; the implementation in Section 3.4.1 makes it concrete (signal ions = causal, noise peaks = non-causal).

- **Concerns about α and γ values missing from the paper** → Moved to Nice-to-Haves since these likely appear in the stripped appendix.

- **"The contrastive approximation conditions on Y, but the justification is thin"** → Partially retained (under Nice-to-Haves as "could be more explicitly derived"), but the paper does provide a citation and the Chen et al. (2022) derivation is standard in causal representation learning.

## Novel Insights

The paper's most novel insight is the empirical demonstration that current de novo peptide sequencing models — despite their architectural sophistication — systematically rely on non-causal spectral peaks (noise), and that a relatively lightweight representation-level causal disentanglement module can substantially mitigate this vulnerability across diverse architectures and datasets. The finding that model-agnostic causal representation learning transfers across three different encoder-decoder designs suggests the vulnerability to noise is a fundamental property of the task rather than an artifact of any particular architecture.

## Suggestions

- Add a parameter-matched baseline (same 3 Transformer layers + MLP added to baseline encoder, without causal objectives) to isolate capacity effects from causal training effects.
- Either acknowledge the tension between label-derived x_theory in the enhancement step and the causal independence narrative, or provide an analysis (e.g., training without enhancement and evaluating whether causal disentanglement still occurs) that rules out label leakage as the dominant mechanism.
- Consider evaluating robustness under a perturbation criterion not aligned with the training heuristic, such as intensity-based perturbation, to provide cleaner evidence of causal generalization.
- Align the SCM figure caption (C as "causal factors" not "charge state," S as "non-causal factors" not "spectrum augmentation") with the text in Section 3.2.
- Report concrete values for α and γ in the main text.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>