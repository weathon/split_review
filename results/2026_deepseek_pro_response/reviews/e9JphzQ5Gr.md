Now I have a clear calibration picture. Let me compile the final review.

**Round 1 bracket:** CaPT sits above SemiCLIP (5.80) and below the 8.00 analysis papers — plausible range **5.5–7.5**.

**Round 2 narrowing:** 
- SemiReward (6.00): CaPT is clearly stronger.
- CLIP Synergy (6.25): CaPT is stronger — more dramatic gains, better ablation.
- Demystifying CLIP Data (6.75): Comparable strength level, but CaPT has the pre-training confound and disconnected theory bringing it slightly below.
- CLIPSelf (7.00): CLIPSelf is a cleaner contribution — simple, well-executed, well-ablated. CaPT has more dramatic gains but the pre-training confound, disconnected theory, and missing methodological details place it slightly below.

**Final score: 6.5 — Accept.**

---

## Summary

This paper identifies that SSL methods are inherently label-dependent — their ability to exploit unlabeled data degrades when labeled data is scarce or low-quality. To address this, the authors propose CaPT, an asymmetric-modalities co-training framework that integrates CLIP as a "prior teacher" into SSL. CaPT jointly trains a fully fine-tuned unimodal network (UPM) and an adapter-tuned CLIP (MPM), using entropy-weighted co-pseudo labels to exchange supervision between them. The method achieves substantial gains over existing SSL methods, particularly in extreme low-label regimes (e.g., +21.38% on CIFAR-100 at 1 label/class).

## Strengths

- **Strong and consistent empirical gains in low-label regimes (Tables 1-3):** CaPT substantially outperforms all baselines across USB benchmarks, ImageNet, and extreme one-label-per-class settings. The gains are largest where label scarcity is worst (e.g., +9.33% on ImageNet at 10 labels/class, +21.38% on CIFAR-100 at 1 label/class), directly validating the central claim that CLIP's prior mitigates SSL's label dependency.

- **Well-designed ablation study (Table 6):** Every design choice is isolated and tested. The full CaPT is compared against six stripped variants. Every removal hurts performance with magnitudes consistent with claimed roles. The "only MPM" result (68.32%) being below "only UPM" (78.60%) demonstrates that CLIP's raw prior is insufficient without the co-training framework — the framework genuinely adds value.

- **Efficiency-preserving design with feature-augmented consistency regularization (Section 3.2.2, Table 4):** Instead of running CLIP's frozen but heavy encoder twice, the method performs Mixup in feature space. Table 4 quantifies the payoff: CaPT requires only 8% more memory and 11% more time than FreeMatch while delivering +6.23% accuracy, and is simultaneously faster and leaner than RegMixMatch despite outperforming it.

- **Honest reporting of failure case (Table 5, FGVCAircraft):** CaPT underperforms on FGVCAircraft (50.12% vs. FreeMatch's 51.43% at 5 labels/class), and the authors explicitly acknowledge this as a limitation (line 307). This strengthens credibility for the claims where the method does work.

- **Broad evaluation across diverse datasets:** Tested on 10 datasets spanning standard SSL benchmarks, large-scale ImageNet, six fine-grained datasets with significant domain shift, and extreme one-label-per-class settings.

- **Adapter-tuning effectively mitigates CLIP's class-preference bias (Figure 5):** On EuroSAT, frozen CLIP exhibits a highly skewed class distribution, while adapter-tuned CLIP produces a substantially more uniform distribution, validating the rationale for training adapters.

## Weaknesses

### Fatal
None.

### Major
- **Pre-training data scale not fully controlled in comparisons with SSL baselines.** CaPT's MPM uses CLIP (ViT-B/32 pre-trained on 400M image-text pairs from WIT), while the UPM and all SSL baselines use ImageNet-pre-trained or MAE-pre-trained ViTs. The headline gains reflect both (a) access to a larger pre-training corpus and (b) the proposed co-training framework. Table 6 partially addresses this — "only MPM" (68.32%) underperforms "only UPM" (78.60%), showing CLIP alone is not sufficient and the framework matters. However, a direct baseline that initializes the UPM ViT with CLIP's visual encoder weights and runs standard FreeMatch would cleanly isolate how much of the gain comes from CLIP's representations versus the co-training mechanism. The fine-grained dataset results (Table 5) partially mitigate corpus-overlap concerns but do not address the pre-training scale confound.

### Minor
- **Supervised loss on labeled data not explicitly specified in the method section.** Standard SSL methods apply cross-entropy on labeled samples alongside the unsupervised consistency loss. Section 3 describes the co-pseudo label mechanism for unlabeled data thoroughly but does not state what loss is applied to the few labeled examples in UPM, MPM, or both. This affects reproducibility.

- **Theorem 1.1 is purely motivational and disconnected from the method.** The theorem bounds pseudo-label error for a nearest-prototype classifier under a Gaussian mixture model, showing that label scarcity and low quality degrade pseudo-labels. While this cleanly motivates the problem, it does not analyze CaPT's co-training dynamics, does not characterize the effect of adding a pre-trained multimodal model, and does not produce insights that guided the method's design. The paper should not lean on this as a major theoretical contribution.

- **Co-pseudo label formulation (Eq. 13) lacks justification.** Combining one-hot pseudo-labels with scalar weights produces a target vector with at most two non-zero entries. The paper does not discuss why this is preferable to alternatives like mixing the soft probability distributions from both modules, which would preserve richer uncertainty information.

- **The title's "Breaking the Label Dependency" framing is imprecise.** CaPT substitutes scarce task-specific human labels with CLIP's web-supervision from 400M image-text pairs. The paper itself uses more measured language in several places ("mitigate the label dependency," line 305; "reducing SSL's label dependency," line 77) which is more accurate. This is a presentation imprecision rather than a methodological flaw.

### Trivial
None.

## Nice-to-Haves
- A breakdown of computational cost (time/memory) attributable to UPM vs. MPM separately would help practitioners understand the trade-off.
- The paper could discuss whether the adaptive thresholding from FreeMatch (which CaPT inherits, line 206) could be further tuned specifically for the asymmetric-modalities setting.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "Appendix references central to claims cannot be verified."** REMOVED — the parser strips appendices from all papers; they exist in the original submission.
- **Harsh Critic: "'Breaking label dependency' is a structural problem affecting contribution understanding."** PARTIALLY REMOVED — the substantive point about framing precision is retained as a Minor weakness, but the claim that this is structural/overclaiming is downgraded. The paper provides clear evidence that CaPT reduces dependency on task-specific labeled data via CLIP's prior, and uses measured language alongside the bold title.
- **Strength Finder: "Theoretical framing of SSL's label-dependency bottleneck as a core strength."** WEAKENED — the theory is clean but purely motivational; retained as context in the Novel Insights section rather than as a standalone strength.
- **Harsh Critic: "Co-pseudo label formulation is two-hot only — unclear why this form."** RETAINED as Minor — verified against Eq. 13.
- **Strength Finder: generic "important problem" claims.** REMOVED as per filtering rules.

## Novel Insights
The asymmetric-modalities design insight — that co-training a vision model with a vision-language model avoids the pattern-homogeneity bottleneck that plagues co-training of two vision models — is genuinely interesting and well-supported by the attention-map analysis (Figure 3). This goes beyond the straightforward "add CLIP to SSL" idea and provides a principled rationale for why cross-modal co-training works better than same-modality co-training. The finding that CLIP alone (adapter-tuned, 68.32%) underperforms a standard SSL baseline (FreeMatch, 78.60%) while the co-training framework achieves 84.83% is a crisp demonstration that the framework — not just the prior — drives the gains.

## Suggestions
- Add the CLIP-initialized unimodal baseline (initialize UPM ViT with CLIP visual encoder weights, run standard FreeMatch) to isolate the contribution of the co-training framework from CLIP's pre-training scale.
- Explicitly state the supervised loss on labeled data in the method section.
- Consider a brief discussion or ablation comparing the current co-pseudo label formulation (Eq. 13) against mixing soft probability distributions, or justify the design choice.
- Reconsider the title phrasing — "Mitigating the Label Dependency" would be more accurate than "Breaking the Label Dependency" while still capturing the contribution.

## Calibration Report

### Round 1 (Bracketing)
| Anchor | Score | Comparison to CaPT |
|---|---|---|
| Weak-to-Strong CLIP (3.33) | 3.33 | CaPT is vastly stronger — comprehensive evaluation, systematic ablation, dramatic gains |
| CLIPSelector + MixFix | 4.50 | CaPT is substantially stronger — more competitive results, better ablation |
| SemiCLIP | 5.80 | Most similar anchor; CaPT is clearly stronger — larger gains, better ablation, efficiency analysis |
| Modality Gap analysis | 8.00 | Different type (analysis paper); CaPT does not reach this level of rigor |

**Round 1 bracket: 5.5–7.5**

### Round 2 (Narrowing)
| Anchor | Score | Comparison to CaPT |
|---|---|---|
| SemiReward | 6.00 | CaPT is clearly stronger |
| CLIP Synergy | 6.25 | CaPT is stronger — more dramatic gains, better ablation |
| Demystifying CLIP Data | 6.75 | Comparable strength; CaPT slightly below due to pre-training confound and disconnected theory |
| CLIPSelf | 7.00 | CLIPSelf is cleaner; CaPT slightly below due to pre-training confound, missing methodological details |

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>