Now I have a comprehensive understanding of the paper. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes a backdoor-based DNN watermarking method that requires only a single out-of-distribution (OoD) image (augmented into a surrogate dataset) to inject a verifiable trigger into a pre-trained model, eliminating the need for original training data. It introduces an adversarial weight-perturbation procedure during fine-tuning to improve robustness against common removal attacks (fine-tuning, pruning, model extraction). Experiments on CIFAR-10, CIFAR-100, and GTSRB demonstrate high watermark success rates with minimal accuracy degradation and resilience under several attack scenarios.

## Strengths

- **Data-free watermark injection using a single OoD image**: The paper demonstrates that high OoDWSR (e.g., 95.66% on CIFAR-10) can be achieved *without any access to the original training data*, using only patches from one public OoD image (Section 4.1, Fig. 2). This directly addresses a practical gap in backdoor-based watermarking, which typically requires i.i.d. data or costly generator training.

- **Robustness gains via adversarial weight perturbation**: The proposed weight-perturbation fine-tuning (Section 3.2) meaningfully improves post-attack OoDWSR. For example, after RT-AL on CIFAR-10, OoDWSR rises from 19.94% (without WP) to 57.52% (with WP) for trojan_wm (Table 6 / tab:wp). Against FT-AL and pruning, OoDWSR remains above 94% across multiple triggers and datasets (Table 2), and p-values are consistently near zero.

- **Time and sample efficiency**: The method requires only a few epochs of fine-tuning (20 for CIFAR-10/GTSRB, 30 for CIFAR-100) and a single OoD image. Figure 2 shows stable high OoDWSR within 10 epochs on CIFAR-10, with accuracy degradation under 3%. This contrasts favorably with data-free approaches that train a generator for hundreds of epochs.

- **Empirical comparison showing OoD injection is more robust than i.i.d. injection**: Under RT-AL (the strongest attack), OoD injection retains OoDWSR of 57.52% and 24.19% (two triggers on CIFAR-10), while i.i.d. injection drops to 4.13% and 3.42% (Table 4 / tab:id_ood). This directly supports the paper's core intuition.

- **Evaluation across three removal attack families**: The paper tests fine-tuning (FT-AL, FT-LL, RT-AL), pruning (20%/50%), and model extraction (knockoff) across three datasets, with multiple trigger patterns, providing broad coverage of the threat landscape.

## Weaknesses

### Fatal
None.

### Major

- **No experimental comparison with prior OoD or data-free watermarking methods.** The paper cites prior OoD-based approaches (Zhang et al., 2018; Wang et al., 2022) and data-free methods (Li et al., 2022) and claims to "fill a gap," yet the experimental evaluation compares only against ID-based watermark injection (Table 4 / tab:id_ood). Without benchmarking against at least one of these existing approaches under comparable conditions, it is difficult to assess whether the claimed improvements in efficiency, safety, or robustness are advances over the state of the art or merely comparable to it. The paper states that prior OoD methods still rely on ID data to maintain utility, but does not verify that its own method outperforms them when they use the same single OoD image as trigger source. This omission is the single largest gap in the evaluation.

### Minor

- **Only top-2 trigger patterns are reported in the main robustness tables.** Six trigger patterns are considered (Section 4, "Trigger patterns"), but only the two best-performing by OoDWSR and accuracy degradation are shown in Tables 2 and 5. Performance varies significantly across triggers (e.g., on CIFAR-100 after model extraction, trojan_8x8 achieves 70.40% OoDWSR while l0_inv achieves only 6.22% — Table 5). Reporting all six triggers or summary statistics (mean/std) would give a more complete picture of robustness across the design space. The selection criterion is stated transparently, which mitigates concerns, but the evidence for robustness is incomplete without seeing the full distribution.

- **The T-test verification procedure lacks a false-positive control experiment.** Ownership is claimed when the T-test between suspect-model and non-watermarked-model logits on OoD verification samples yields p < 0.05. The paper reports extremely low p-values for all suspect models, which is suggestive, but does not evaluate the test on an unrelated model (e.g., a model trained on a different dataset or with a different architecture) to show that p > 0.05 when the model is genuinely unrelated. Without this control, the possibility of false positives is not ruled out. That said, the joint use of OoDWSR (which is very low for non-watermarked models, e.g., 0.0487 on CIFAR-10) alongside the T-test mitigates this concern somewhat.

- **No sensitivity analysis on the perturbation constraint γ.** The hyperparameter γ (Eq. 3) controls the per-layer perturbation radius and is fixed at 0.1 (CIFAR-10/GTSRB) or 0.05 (CIFAR-100) without ablation. Since this parameter directly governs the strength of the robustness mechanism, a sensitivity study would help assess how robust the method is to this choice.

- **No analysis of how label noise from OoD soft labels affects injection.** The loss in Eq. (1) uses the pre-trained model's soft labels for clean OoD samples. Since the pre-trained model was trained on ID data, its predictions on OoD data may be unreliable. The paper does not analyze whether this label noise degrades injection quality or utility, nor how it compares to using ground-truth labels.

### Trivial
- Figure 3 shows the distribution of OoD and ID samples before/after injection via a visual t-SNE-style plot without quantitative measures of overlap or separation. A simple metric (e.g., MMD, centroid distance) would strengthen the qualitative claim.
- The weight perturbation ablation (Table 6) is limited to a single attack (RT-AL) on CIFAR-10. The paper notes more results are in an appendix (sec:extended_wp), which is acceptable but limits the main-text evidence.

## Nice-to-Haves
- An evaluation of attacks where the adversary also lacks ID data (e.g., fine-tunes with OoD or public data only) would align more closely with the paper's core motivation. However, the current setup (attacker has 10% ID data) is actually a harder test for the watermark, so this is not a genuine weakness.
- A brief discussion of the relationship between the proposed weight perturbation and sharpness-aware minimization (SAM) would help situate the contribution; the paper does cite relevant work (he2023sharpness) but does not elaborate on similarities or differences.
- Reporting the computational overhead of the two-step v-step/w-step optimization would help practitioners assess the trade-off.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that the attacker's access to ID data is "inconsistently motivated"** — The paper explicitly frames the attacker's access to 10% ID data as an "unfair scenario" (line 51) and uses it to demonstrate that the watermark persists even when the attacker has an advantage. Testing under conditions favorable to the attacker is standard robustness evaluation methodology; this is a strength of the experimental design, not a weakness. Moved to Nice-to-Haves.

- **Criticism about model extraction using ImageNetDS (which is OoD to all benchmarks)** — The observation is accurate but not a weakness. The model extraction attack uses an auxiliary dataset (ImageNetDS) to query the victim model; the fact that this auxiliary set is OoD to the benchmarks is a characteristic of the attack setup, not a flaw in the paper's evaluation. If anything, it aligns with the paper's OoD theme.

- **Criticism that the paper lacks comparison with prior methods when they are "allowed to use the same single OoD image as trigger source"** — This is the core of the missing-comparison weakness, which is already listed as a Major weakness. The formulation about "the same single OoD image" is preserved in spirit but the specific framing as a fatal omission is downgraded to Major (since the paper's primary comparison target — ID injection — is the most relevant baseline for its key robustness claim).

## Novel Insights

The reviewer critiques converge on a clear picture: the paper's core idea (single-OoD-image watermark injection + weight perturbation) is clever and the results are promising, but the evaluation falls short of substantiating the claimed advance over prior OoD/data-free methods. The key insight across reviews is that the paper's novelty lies in the *combination* of sample efficiency (single image, few epochs) with a robustness mechanism (weight perturbation), and the comparison against ID injection convincingly demonstrates the value of OoD-based watermarks. However, the paper overclaims relative to its comparisons: claiming to "fill a gap" without experimentally benchmarking the methods that define that gap weakens the contribution. The most actionable insight is that the paper needs exactly one well-chosen comparison experiment (e.g., Li et al. 2022's data-free method on the same models and datasets) to move from "promising" to "convincing."

## Suggestions

1. **Add a direct comparison with at least one prior OoD or data-free watermarking method** (e.g., Li et al., 2022, or Zhang et al., 2018) on the same datasets, using comparable epochs and architectures. This is the single highest-leverage revision and would substantially strengthen the paper's claim to advancing the state of the art.

2. **Report results for all six trigger patterns** (or at least mean/std across triggers) in the main robustness tables, rather than only the top-2. Alternatively, adopt a principled trigger-selection rule (e.g., maximize the OoDWSR margin relative to non-watermarked models) and apply it consistently.

3. **Add a control experiment for the T-test** by evaluating it on an unrelated model (e.g., a model trained on SVHN or a different architecture) to demonstrate that p > 0.05 when the model is not a copy. This would calibrate the false-positive rate.

4. **Ablate the γ hyperparameter** across a small range (e.g., {0.01, 0.05, 0.1, 0.2}) on at least one dataset to show that the method is not overly sensitive to this choice.

## Score and Decision

The paper proposes a genuinely practical approach to a relevant problem, with a clear method and encouraging results. The weight perturbation mechanism is a sensible contribution, and the comparison with ID injection convincingly supports the core intuition. However, the evaluation is incomplete in a way that directly affects the paper's main claim of advancing the state of the art: the absence of any experimental comparison with prior OoD/data-free methods makes it impossible to assess whether the proposed approach represents an advance or merely an alternative. Combined with the selective reporting of trigger patterns and the uncalibrated verification test, the evidence is not yet sufficient to support the claimed contributions at the level expected for acceptance. The paper could become a solid contribution with revisions centered on the missing comparison.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>