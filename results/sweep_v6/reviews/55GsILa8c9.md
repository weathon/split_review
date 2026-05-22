Now I have a good calibration set. Let me compose the final review.

**Key verification of the harsh critic's claims against the paper:**

1. **Claim: "Causal intervention depends on ground-truth peptide labels"** — This is TRUE, confirmed at lines 109-113: "Given that the training data includes the peptide sequence label, we can compute the theoretical spectrum...". The paper transparently admits this.

2. **Claim: "The vulnerability analysis is circular"** — PARTIALLY TRUE. The perturbation definition at test time uses the same theoretical-spectrum matching used to create training augmentations. However, the paper uses this as a diagnostic tool applied equally to all models, not as a training intervention.

3. **Claim: "The SCM framing adds no operational content"** — This is a judgment call. The paper does derive principles (independence, sufficiency) from the SCM that guide the loss design. However, the actual implementation is feature masking + contrastive learning.

4. **Claim: "Missing oracle-free baseline"** — TRUE. The paper does not include an ablation where noise peaks are identified without ground-truth labels (e.g., randomly).

5. **Claim: "Cross-species validation shows consistent gains"** — TRUE, confirmed by Table 3.

6. **Strengths from strength finder about "vulnerability analysis as diagnostic"** — This is valid as a diagnostic but not as causal validation.

Let me also check the strength finder's more questionable claims:
- "Empirical demonstration of spurious-correlation reliance" — This is legitimate, the paper shows this.
- "Attention analysis provides mechanistic evidence" — This is valid as evidence of model behavior, but it's not independent evidence.

Now let me write the review.

Score: I'll compare against the anchors. ReNovo (6.50) has somewhat cleaner methodology but faces data leakage concerns. CausalNovo has a comparable issue (oracle supervision) but stronger cross-validation and ablation. RankNovo (5.50) has modest improvements and computational concerns. I'd place CausalNovo around 5.5 as well — the oracle issue is genuine but addressable, the results are convincing, and the framework is model-agnostic and well-evaluated.## Summary

This paper introduces CausalNovo, a model-agnostic framework for *de novo* peptide sequencing that aims to learn causal rather than spurious relationships between mass spectra and peptide sequences. The framework integrates a Causality Extraction Module (CEM) that learns importance masks to disentangle signal (causal) from noise (non-causal) peaks, and uses contrastive learning between original and perturbed spectra guided by two principles derived from a Structural Causal Model: *independence* (invariance under noise perturbations) and *sufficiency* (retaining predictive power). Experiments across three datasets and three baseline models (CasaNovo, AdaNovo, π-HelixNovo) show consistent gains of up to ~10% in amino acid, peptide, and PTM-level metrics, with cross-species validation and robustness analysis under varying noise-signal ratios.

## Strengths

- **Consistent and substantial empirical gains across baselines, datasets, and metrics.** Tables 1-2 show that CausalNovo improves amino acid precision, peptide precision, and PTM precision for all three baseline models on all three datasets. For example, on Seven-species, CasaNovo's amino acid precision jumps from 0.357 to 0.477 (+12.0%); on HC-PT, π-HelixNovo's PTM precision improves from 0.632 to 0.737 (+16.6%). These are large, systematic improvements that replicate across model architectures.

- **Cross-species validation confirms generalization beyond in-distribution conditions.** Table 3 shows that CausalNovo improves CasaNovo on all nine species in a leave-one-out evaluation (e.g., peptide precision from 0.506→0.545 on Tomato, +7.7%). This is a stronger test than fixed test-set evaluation because the held-out species may have different noise characteristics, and it provides evidence that the benefits carry over to distribution shifts.

- **Comprehensive ablation and analysis.** The paper ablates each component (Independence, Purification, Symmetric training) and each design choice (Replace vs. Drop vs. Enhance) in the causal intervention, demonstrating incremental gains from each. The attention analysis (Table 7) quantifies how CausalNovo shifts focus toward causal peaks (32.87% of predictions attend all three causal peaks vs. 19.26% for baseline).

- **Model-agnostic framework.** The method is demonstrated across three different base models (CasaNovo, AdaNovo, π-HelixNovo) with consistent benefits, showing it is not tied to a single architecture.

## Weaknesses

### Fatal
None.

### Major

- **The training-time noise-peak identification uses ground-truth peptide labels (via theoretical spectrum matching, Eq. 4), creating an asymmetric information advantage over baselines that do not receive this signal.** The paper is transparent about this (lines 109-113), but it means CausalNovo receives peak-level supervision that no baseline gets. The reported improvements conflate the effect of (a) the causal disentanglement framework with (b) the additional peak-level signal from theoretical spectrum matching. A proper control would give the same oracle information to baselines (e.g., as an extra input channel) to isolate whether the CEM and contrastive objectives specifically drive the gains. Without this, the paper cannot support its central claim that the improvements come from "causal reasoning" rather than from label-guided noise suppression.

- **The vulnerability analysis and attention analysis are partially self-validating.** The vulnerability evaluation (Figures 1, 3) perturbs test-set noise peaks identified via the same theoretical-spectrum matching used during CausalNovo's training augmentations. CausalNovo is explicitly trained to be invariant to this exact perturbation type, so its better robustness is expected and does not constitute evidence of "causal understanding" beyond training-data augmentation. Similarly, the attention analysis (Table 7) defines "causal peaks" via the same theoretical spectrum — CausalNovo is trained with losses that push it to focus on these peaks, so the improved attention scores measure training fidelity, not independent evidence of causal reasoning.

- **The "causal" framing is largely decorative.** The SCM (Figure 2A) posits X = f(C,S) with C ⟂ S and Y = g(C), but the implementation never verifies or enforces this independence in a causal sense. The actual machinery is: learned feature masking (CEM), contrastive learning between original and perturbed representations (Eq. 5), and cross-entropy losses on masked and anti-masked representations (Eq. 6). These are reasonable learning objectives, but they do not require SCM formalism and could be described more simply as label-guided data augmentation with a learned importance mask.

### Minor

- **The replacement-based perturbation replaces non-causal ions with other non-causal ions sampled from the batch.** This means the perturbation changes not just the noise structure but also introduces new peaks that could belong to other peptides' signal ions. The "causality enhancement" (adding theoretical peaks) partially mitigates this, but the intervention is a hybrid augmentation rather than a clean intervention on non-causal factors. An ablation using random peaks (rather than batch-sampled non-causal peaks) as replacement targets would clarify whether the specific noise-to-noise replacement mechanism matters.

- **Table 5 shows the "Drop" operation (randomly removing noise peaks) does not improve performance.** The paper concludes replacement is better, but this is expected: removal changes the sequence length processed by the encoder, which may harm the model independent of any causal effect. This weakens the claim that replacement is "causally" better.

- **The paper notes (Section 5) that evaluation follows the NovoBench protocol, while recent methods use more realistic protocols with large-scale external training and out-of-distribution test sets.** The paper identifies this as future work, but it limits confidence in real-world applicability.

### Trivial
None of note.

## Nice-to-Haves
- An oracle-free ablation where noise peaks are identified by a heuristic not requiring ground-truth labels (e.g., random subset, intensity-based thresholding) would strengthen the claim that learned representations are genuinely causal rather than label-guided.
- A control experiment where the theoretical-spectrum information is provided to the baseline model (e.g., as an additional input channel) would isolate the causal-specific component of the gains.
- Evaluation on DIA data or datasets with real co-elution/contaminant noise (where ground-truth noise labels are unknown) would test whether the approach generalizes beyond oracle-defined perturbations.

## Removed Points

- **Criticism about "no independent verification of released code/models"**: Removed per hard rule — the paper cites code availability and the rules state that cited entities are assumed to exist.
- **Criticism about missing related works**: Removed per hard rule — I cannot verify the existence or absence of external works.
- **Formatting/style nitpicks**: Removed per hard rule.
- **Strength finder's "vulnerability analysis is a useful diagnostic tool"**: This specific claimed strength was kept (it IS a valid diagnostic), but the strength finder's more generic framing was dropped where it conflicts with verified weaknesses.
- **Strength finder's generic claims** (e.g., "addresses an important problem"): Removed — generic, not concrete.

## Novel Insights

The harsh critic's central observation — that CausalNovo's training-time noise identification uses ground-truth labels and that this confounds the evaluation — is the most penetrating insight across all reviews. Combined with the paper's own transparency about this design choice and its citation of prior works using the same approach, a nuanced picture emerges: the paper's contribution is better described as *label-guided noise-aware augmentation with learned importance masking* than as *causal disentanglement*. The genuine novelty lies in combining (a) a learned importance mask that adaptively weights peaks, (b) contrastive learning across label-guided perturbed spectra, and (c) sufficiency/purification losses on both masked representations. These are practically valuable but do not require a causal framing to justify. The cross-species validation (Table 3) is the strongest evidence that the approach captures something general — because the held-out species may have systematically different noise characteristics, and the model's gains persist — but even this is limited by the shared fragmentation physics across species.

## Suggestions
1. Add an oracle-free ablation: replace noise peaks identified *without* ground-truth labels (e.g., random subset or low-intensity threshold) and report how much performance degrades. If CausalNovo still outperforms baselines, the causal claims are on much stronger ground.
2. Provide a controlled baseline: give CasaNovo/AdaNovo/π-HelixNovo the same theoretical-spectrum information (as an extra input channel or pre-masking step) and compare against CausalNovo. If CausalNovo still wins, the CEM+contrastive components are validated.
3. Tone down the causal terminology or provide a proper causal evaluation (e.g., test on a dataset from a different instrument/different fragmentation method where the noise structure changes fundamentally, not just on the same perturbation type used during training).

## Score and Decision

**Calibration Anchors** (all from /home/wg25r/split_review/datasets/deepreview_13k_calibration/):
- **ReNovo** (uQnvYP7yX9.md, avg 6.50): Retrieval-based de novo sequencing with a clean method but concerns about data leakage. CausalNovo has stronger cross-validation but a more significant methodological confound; comparable overall quality.
- **RankNovo** (87B3zDRMjv.md, avg 5.50): Reranking framework for de novo sequencing with modest improvements and computational overhead. CausalNovo has larger improvements and a more interesting framework; slightly stronger.
- **Distilling Non-Autoregressive** (I2ZYngkRW6.md, avg 4.25): Knowledge distillation for peptide sequencing, criticized as an engineering contribution. CausalNovo is more methodologically novel and has stronger results.
- **Causal Representation Learning from Multimodal** (hjROBHstZ3.md, avg 5.80): Causal representation learning for biological data with theory concerns. CausalNovo has stronger empirical validation but weaker theoretical grounding.
- **Feature Matching Intervention** (8GhwePP7vA.md, avg 4.25): Causal representation learning with strong assumptions, criticized for overclaiming. CausalNovo has a similar gap between causal framing and actual mechanism.
- **CRL-Net** (mrBd4hyWlP.md, avg 1.67): Poorly executed MRI reconstruction. Not comparable to CausalNovo.
- **MADGEN** (78tc3EiUrN.md, avg 6.00): De novo molecular generation. CausalNovo has more thorough experiments but a less clean methodology.
- **A Unified Causal View of Instruction Tuning** (lWXedJyLuL.md, avg 5.67): Causal framing for NLP instruction tuning. Similar gap between causal framing and implementation.

Relative to these anchors, CausalNovo sits in the 5.0–6.0 range. It has genuine empirical contributions (large, consistent gains, cross-species validation, thorough ablation) that would typically merit a 6.0+, but the oracle concern — which the paper does not adequately control for — is a genuine weakness that undermines the *interpretation* of the results and prevents the paper from being a clear accept. The method is practically useful, but the claimed causal reasoning is not supported by the evidence as presented.

**Score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>