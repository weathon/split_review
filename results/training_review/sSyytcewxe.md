Here is the consolidated meta-review after verifying all claims against the paper.

---

## Summary

SEED proposes an exemplar-free class-incremental learning method built on a fixed-size ensemble of experts (K=5) sharing a frozen backbone. The core innovation is two-fold: (1) only one expert is fine-tuned per task (selected via a KL-divergence criterion that minimizes distribution overlap), and (2) the ensemble uses multivariate Gaussian class representations combined with Bayes classification for task-agnostic inference. The method is evaluated on CIFAR-100, ImageNet-Subset, and DomainNet under equal-split, large-first-task, and task-incremental settings.

---

## Strengths

- **Selective single-expert fine-tuning mitigates forgetting and promotes diversity.** SEED updates only one expert per task while keeping all others frozen. The paper shows empirically (Fig. 4, diversity analysis) that despite no explicit diversity loss, experts specialize on different tasks, and the ensemble consistently outperforms the best individual expert by 6–10 percentage points. This is a clean and well-motivated design.

- **KL-divergence-based expert selection is empirically validated.** The selection strategy (Eq. 1) chooses the expert whose per-class Gaussian distributions overlap least for the new task's classes. Figure 5 (selection strategies) compares KL-max against random, round-robin, and KL-min across 10 runs on CIFAR-100 (T=20, T=50) with 3 experts, showing higher and more consistent accuracy for KL-max.

- **State-of-the-art results on equal-split and domain-shift scenarios.** Table 1 shows SEED surpassing the second-best method (FeTrIL) by 15.4–15.6 pp on CIFAR-100 equal splits (T=10,20,50) and by 11.5–11.7 pp on DomainNet (T=12,24,36). These are the most challenging exemplar-free settings (small initial task, substantial domain shift), and the margins are large.

- **Thorough ablation isolates each component's contribution.** Table 4 quantifies that removing multivariate Gaussians (→ mean prototypes + NMC) drops 7.2%, removing covariance structure drops 7.6%, and using a standard ensemble (all experts trained on all tasks) drops 4.8%. This confirms the specific design choices matter beyond just having an ensemble.

- **Plasticity–stability analysis with explicit trade-off control.** Figure 7 (left) uses forgetting vs. intransigence measures to show SEED achieves lower intransigence (better plasticity) than LwF/EWC while maintaining low forgetting, outperforming FeTrIL which has near-zero plasticity. The α parameter provides controllable trade-off.

- **Parameter efficiency in the task-incremental setting.** Table 3 shows SEED uses fewer parameters (2.7–3.2M) than all compared methods (HAT: 6.8M, CoSCL: 4.6M) while achieving higher accuracy (86.8% vs 79.4% for 20-split). The shared backbone design is the key enabler.

---

## Weaknesses

### Fatal
None.

### Major
- **SEED is not universally superior; it underperforms on large-first-task ImageNet-Subset.** On ImageNet-Subset with T=11 and T=21 (Table 2), SEED loses to the simple frozen-backbone method FeTrIL by 0.3 pp and 4.1 pp, respectively. While the paper acknowledges this, it only offers a high-level explanation ("SEED works better in scenarios where a strong feature extractor must be trained from scratch"). No deeper analysis is provided — e.g., per-task accuracy curves, expert utilization statistics, or a diagnostic showing whether the frozen shared backbone saturates or the selection mechanism degrades. This limits understanding of the method's failure mode and weakens the claim of "state-of-the-art across various scenarios."

### Minor
- **Selection strategy comparison is shown only with 3 experts (Fig. 5), while the main results use 5 experts.** The KL-max vs. random/round-robin/KL-min comparison is done with K=3, but Table 1 uses K=5. Since a larger ensemble provides more options for selection, the benefit of KL-max over simpler strategies (or its variance) could differ at K=5. Reporting this comparison at the operational K would strengthen the evidence for the selection mechanism.

- **Computational cost of full-covariance Gaussians is not reported.** For inference on each example, SEED computes multivariate Gaussian log-likelihoods (including matrix inverses) for every class in every expert. On the largest dataset (DomainNet, 345 classes, 5 experts, latent dimension S), this is a non-trivial cost. The paper does not report inference time or memory footprint, which is a practical concern for deployment.

- **The paper does not discuss whether the large margins in Table 1 partly reflect that baselines (designed for large-first-task settings) are operating outside their intended regime.** FeTrIL, PASS, and SSRE were all designed with the assumption of a strong initial feature extractor. The equal-split scenario is inherently unfavorable for them. This is not a flaw in SEED, but the paper frames the comparison as "SEED is better" without contextualizing that its advantage is largest precisely where other methods' design assumptions break. A brief discussion would improve scientific honesty (the limitations section already partially covers this in a different way).

### Trivial
- **In Table 3, the paper should explicitly state whether SEED's parameter counts include the shared backbone or only the expert-specific heads.** The numbers (2.7–3.2M) are compared against baselines taken from CoSCL. A clarifying footnote would prevent confusion.

---

## Nice-to-Haves

- A diagnostic analysis of why SEED underperforms on large-first-task ImageNet: e.g., per-task accuracy curves, expert selection frequency over tasks, or a study of whether the frozen backbone causes representational saturation when many tasks share the same initial features.
- A practical efficiency benchmark (inference time and memory) for the multivariate Gaussian computation on the largest datasets.
- Selection strategy comparison (KL-max vs. alternatives) repeated with K=5 to match the main experimental setup.

---

## Removed Points

These points were flagged by reviewers but are removed after cross-checking against the paper. They are listed here for completeness and should be treated with caution.

- **"Baseline comparisons in Table 1 not validated under identical conditions."** The paper explicitly states (line 121): "We reproduce results using FACIL and PyCIL benchmarks for this setting. We train all methods using random crops, horizontal flips, cutouts, and AugMix data augmentations." This is standard practice — all methods receive the same augmentations and training pipeline. The fact that FeTrIL's number (46.3%) differs from its original publication (51.3%) is expected because the experimental setup differs (equal splits + AugMix vs. large-first-task in the original paper). The comparison is fair under identical conditions.

- **"Capacity not controlled; SEED uses more parameters."** The "standard ensemble" ablation (Table 4) uses the same 5-expert architecture and same total capacity as SEED — the only difference is training protocol (all experts trained on all tasks vs. one per task). SEED outperforms it by 4.8 pp with non-overlapping standard deviations (±0.4). This is a valid capacity-controlled comparison. The reviewer's suggestion of a "single model with same total capacity" is architecturally ill-defined for an ensemble method.

- **"w/o multivariate Gauss ablation uses a different inference procedure."** This is exactly how ablation studies work — replace a component with a simpler alternative and measure the drop. The paper clearly describes the replacement (mean prototypes + NMC) and the resulting 7.2% accuracy drop. There is no flaw.

- **"Standard ensemble gap may not be statistically significant."** SEED: 61.7±0.4, standard ensemble: 56.9±0.4. The gap is ~12 standard deviations — clearly significant. The paper need not spell this out.

- **"No ablation of feature distillation loss (α) in isolation."** The plasticity-stability plot (Fig. 7, left) explicitly varies α and shows its effect on the forgetting-intransigence trade-off. This IS the ablation of α.

- **"Teaser plot needs clarification."** This is a formatting/visualization nitpick about a figure not accessible in the text.

- **"Expert selection rule not theoretically justified."** The paper provides an intuitive justification ("causes latent space to change as little as possible") and empirical validation (Fig. 5). Not every design choice in an empirical systems paper requires formal theoretical proof.

---

## Novel Insights

The most interesting observation emerging from the reviews — and one that goes beyond the paper's own framing — is that the value of SEED's mechanism is highly asymmetric across problem regimes. On equal-split and domain-shift scenarios (where plasticity is critical), SEED dominates by huge margins (14–18 pp). On large-first-task scenarios (where stability dominates and a frozen backbone suffices), SEED's advantage shrinks to near-zero or even reverses. This suggests that the selective-expert design is not a universally better way to do CIL, but rather a targeted solution to a specific failure mode: the inability of frozen-backbone methods to learn new features when little data is available upfront. The paper's own analysis (Fig. 7) showing that FeTrIL has near-zero intransigence (plasticity) but also near-zero forgetting confirms this interpretation. A crisper characterization of SEED's regime of advantage — "high plasticity needed, low initial data available" — would strengthen the paper more than claiming broad superiority.

---

## Suggestions

1. **Add a selection-strategy comparison (KL-max vs. random/round-robin/KL-min) using K=5 experts** to match the main experimental setting. This is straightforward and would close an evident gap.

2. **Provide a short diagnostic for the large-first-task ImageNet failure:** e.g., a line plot of per-task accuracy for SEED vs. FeTrIL, or a table showing how many times each expert is selected across the 11/21 tasks. This would help the community understand when and why the method degrades.

3. **Report inference throughput (examples/sec) and peak memory** for the largest configuration (DomainNet, 345 classes, K=5, full-covariance Gaussians). A brief table or footnote addresses practical deployment concerns.

4. **Rephrase the "state-of-the-art across various scenarios" claim to acknowledge the method's regime of strength** — e.g., "SEED achieves state-of-the-art accuracy on equal-split and domain-shift exemplar-free CIL settings, and remains competitive on large-first-task settings where frozen-backbone methods can excel."

---

## Score and Decision

**Originality:** 7/10 — The idea of training only one expert per task and selecting based on distribution overlap is novel and well-motivated. It moves beyond random/round-robin assignment and standard ensemble methods.

**Importance of research question:** 8/10 — Exemplar-free CIL is practically important (privacy, memory constraints), and the equal-split setting where SEED excels is the hardest and most realistic scenario.

**Claims well-supported:** 7/10 — Strong evidence for equal-split and domain-shift settings. The large-first-task weakness is acknowledged but not deeply analyzed. The capacity concern is adequately addressed via the standard ensemble ablation.

**Soundness of experiments:** 7/10 — Baseline comparisons are done under identical conditions using standard benchmarks (FACIL, PyCIL). The ablation study is thorough. Minor gaps: selection strategy comparison at K=5, no inference cost reporting.

**Clarity of writing:** 7/10 — The method is clearly explained with helpful figures. The limitations section is commendably honest. Some details (e.g., parameter counting convention) could be clearer.

**Value to the research community:** 7/10 — The core idea is likely to inspire follow-up work on selective expert training and diversity in continual learning ensembles.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>