## Summary

CausalNovo proposes a model-agnostic framework for improving noise robustness in deep learning-based *de novo* peptide sequencing. The method formalizes the problem through a Structural Causal Model, derives two principles (independence and sufficiency) for causal representations, and implements them via a Causality Extraction Module with contrastive learning and label-guided data augmentation. Applied to three strong baselines (CasaNovo, AdaNovo, π‑HelixNovo) across three standard benchmarks, CausalNovo yields consistent improvements of up to 10% in amino-acid, peptide, and PTM-level metrics, with particularly strong gains under high-noise conditions and across species.

## Strengths

- **Comprehensive empirical benchmarking**: Tables 1–2 report amino-acid, peptide, and PTM-level performance across three public datasets (Nine-species, Seven-species, HC‑PT) for all three integrated baselines. CausalNovo improves every baseline on essentially every metric — e.g., lifting π‑HelixNovo's PTM precision by +15.1% on Seven-species (Table 2). This exhaustive evidence shows the gains are not isolated or metric-specific.

- **Convincing vulnerability and robustness analyses**: Figure 1 (preliminary experiment) and Figure 3 (HC‑PT) demonstrate that baseline models degrade progressively as noise peaks are perturbed, while CausalNovo substantially mitigates this degradation, achieving relative improvements up to 28.5% (Table 6, threshold=1). Figure 4 further shows CausalNovo maintains higher precision than baselines across the entire Noise Signal Ratio range for all three architectures, confirming architecture-independent noise resilience.

- **Granular ablation studies**: Tables 4 and 5 isolate the contribution of each component (independence objective, purification loss, symmetric contrastive training, replace-based perturbation, causality enhancement), showing additive benefits from each and ruling out simpler alternatives (e.g., random drop does not help).

- **Mechanistic validation via attention analysis**: Table 7 quantifies how CausalNovo shifts model attention toward causal peaks — the fraction of predictions attending to all three causal peaks rises from 19.26% to 32.87%, and zero-causal-peak predictions drop from 12.73% to 10.76%. This directly links performance gains to the intended mechanism.

- **Cross-species generalization**: Table 3's leave-one-out validation across eight held-out species shows consistent +2.6% average peptide precision improvement, demonstrating the learned representations transfer across biological contexts.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Unexplained figure legend variants**: Figures 1 and 3 include legend entries for "Baseline +", "CausalNovo (Duo)", and "CausalNovo (Duo) +" whose meanings are never defined in the main text. The perturbation protocol for the vulnerability evaluation is described at a high level (noise peaks are replaced based on m/z proximity to the theoretical spectrum), but specific details — what replacement values are used, whether all or a fraction of non-causal peaks are replaced, and how the "+" and "Duo" variants differ — are absent. This weakens the interpretability and reproducibility of the vulnerability argument.

- **Missing hyperparameter values for α and γ in the main text**: The replace fraction α and tolerance threshold γ that control the causal intervention are introduced conceptually (Section 3.4.1, Eq. 4) but their concrete numeric values are not stated in the main paper. Practitioners cannot reproduce the intervention without these. (These may appear in the stripped appendix.)

### Trivial

- **Causal framing is partly rhetorical**: The method is more accurately described as label-guided data augmentation with a contrastive invariance objective. The paper acknowledges that the "intervention" is simulated using ground-truth labels to identify noise peaks (Section 3.4.1), and the contrastive objective approximates mutual information (Section 3.4.2). The empirical gains do not require a strong causal interpretation. A short paragraph clarifying the boundary between the causal ideal and the practical approximation would improve intellectual precision without weakening the contribution.

- **The x_intervene = x_replace ∪ x_theory union is a strong signal**: Appending the full theoretical spectrum during training provides the model with a near-ideal copy of the signal. While the contrastive objective mitigates the risk of the encoder ignoring the original spectrum, a brief remark on this architectural choice would help readers.

## Nice-to-Haves

- A comparison against a simpler augmentation baseline that *only* adds theoretical peaks (without noise-peak replacement and without the contrastive loss) would more cleanly isolate the source of improvement.
- A sensitivity analysis for α and γ to confirm the method's gains are not fragile to these choices.
- An explicit confirmation in the main text that inference uses only the original spectrum (no theoretical spectrum or peak identification step at test time), to complement the existing statement about negligible inference overhead.

## Removed Points

These points were flagged for removal from the main review. Treat them with caution.

- **Harsh Critic claim that the vulnerability evaluation is under-specified to the point of being an evidential gap**: Retained as a minor weakness, but downgraded from "critical" because the perturbation strategy is described (proximity to theoretical spectrum with m/z tolerance), the concept is clear, and the appendix (stripped) likely contains full details. Not a gap that threatens core claims.

- **Harsh Critic claim that "RCCP in its classic form does not directly imply C ⟂ S unconditionally"**: Removed. The paper asserts C ⟂ S as a structural assumption in Eq. (2) based on the SCM, not as a derived consequence of RCCP. This is a valid modeling choice, and the reviewer's concern reflects a misreading.

- **Strength Finder's generic strength about "the paper addresses an important problem"**: Removed — purely generic praise with no concrete anchor.

- **Harsh Critic's suggestion to "tone down the causal narrative" as a weakness**: Downgraded to Trivial. The paper is honest about using labels to simulate interventions, and the method's effectiveness is demonstrated regardless.

- **Harsh Critic's concern about "no comparison with simpler data-augmentation baselines"**: Moved to Nice-to-Haves. The paper ablates replace-only, replace+enhance, and drop (Table 5), which covers the space reasonably well, though the specific "add theoretical peaks only" baseline is indeed absent.

## Novel Insights

The paper's combination of vulnerability perturbation analysis with attention-based mechanistic validation is genuinely informative. By showing that baseline models degrade under systematic noise-peak replacement *and* that CausalNovo's attention patterns shift measurably toward causal ions, the paper provides a rare two-pronged validation: the method improves numbers, and the numbers improve for the hypothesized reason. This pattern of evidence — perturbation studies plus attention analysis — could serve as a template for evaluating robustness interventions in other spectroscopy domains.

## Suggestions

- Move the definitions of the "+" and "Duo" variants from the appendix into the main text or into the figure captions of Figures 1 and 3.
- State the numeric values of α and γ explicitly in Section 3.4.1 or Section 4.2.
- Add one paragraph in the discussion or methodology section acknowledging that the causal intervention is label-guided and that the empirical gains demonstrate noise-robust learning rather than full causal identification.

## Score and Decision

**Round 1 bracket**: The paper sits between ReNovo (retrieval-based de novo sequencing, 6.50) and InvMSAFold (inverse folding, 7.25), placing the plausible range at [6.5, 7.5].

**Round 2 narrowing**: Compared to ReNovo (6.50), CausalNovo offers broader evaluation (3 baselines × 3 datasets vs. narrower comparison), more thorough ablation, and stronger mechanistic validation (attention analysis). Compared to InvMSAFold (7.25), CausalNovo is comparably rigorous but has slightly more presentation gaps (unexplained figure variants, unspecified hyperparameters). It lands squarely in between — stronger than the 6.50 anchor papers in its domain but short of the 7.25 anchor. Compared to IDEA (6.25), CausalNovo is clearly more thorough and better executed within its own domain. I place it at 7.0.

### Anchors reviewed:
| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| ReNovo (uQnvYP7yX9) | 6.50 | 1,2 | Direct peer; CausalNovo is more thorough |
| RankNovo (87B3zDRMjv) | 5.50 | 1 | Clearer contribution and stronger gains |
| Distilling NAT (I2ZYngkRW6) | 4.25 | 1 | CausalNovo substantially stronger |
| IDEA (FPpLTTvzR0) | 6.25 | 2 | Similar causal framing; CausalNovo better executed |
| InvMSAFold (1iuaxjssVp) | 7.25 | 2 | Comparable rigor; CausalNovo slightly below |
| Causal Rep. Bio (hjROBHstZ3) | 5.80 | 2 | Not directly comparable domain |
| DenoiseVAE (ym7pr83XQr) | 7.00 | 1 | Similar quality tier |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>