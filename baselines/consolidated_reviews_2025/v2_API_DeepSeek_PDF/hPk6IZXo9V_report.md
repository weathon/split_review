## Summary
# Final Review Report

## Summary

This paper presents Neuro2Semantic, a two-phase transfer learning framework for reconstructing semantic content of perceived speech from intracranial EEG (iEEG) recordings. The approach uses an LSTM adapter trained with contrastive and triplet losses to align neural signals with pre-trained text embeddings (text-embedding-ada-002), followed by fine-tuning a Vec2Text corrector to generate natural language from the aligned embeddings. The method is evaluated on pooled iEEG data from 3 epilepsy patients (~30 minutes of speech stimuli across 6 conversations), compared against an adapted version of an fMRI decoding method (Tang et al., 2023). Results show improvements in BERT Score (0.19 vs 0.03), BLEU (0.079 vs 0.064), and WER (0.966 vs 0.975) in in-domain evaluation, with partial zero-shot generalization to held-out stories.

**Strengths:** The paper addresses an important and challenging problem — decoding continuous language from limited iEEG data using transfer learning. The two-phase design (neural-to-embedding alignment + embedding-to-text generation) is conceptually clean and leverages existing pre-trained models effectively. The zero-shot evaluation protocol (holding out entire stories) is a rigorous test of generalization. The analysis of data scaling and electrode reduction provides useful insights into model behavior under resource constraints. The limitations section honestly acknowledges dependency on pre-trained components and hallucination issues.

**Key weaknesses:** (1) Electrode pooling across 3 subjects into a single analysis raises serious concerns about subject independence and generalization validity. (2) The baseline comparison is potentially unfair — an fMRI method adapted to iEEG without validation that it represents a strong iEEG baseline. (3) Absolute performance metrics (WER > 96% across all conditions) indicate the model is far from practical word-level decoding, yet the narrative consistently overstates results. (4) The zero-shot generalization claims are not well-supported by the evidence (BERT scores of 0.08-0.19 with WER > 95%). (5) A factual error in the loss function description (text claims MSE minimization, but Eq. 4 implements a margin-based triplet loss) undermines methodological clarity. (6) Single-step Vec2Text refinement contradicts the iterative refinement described in the method section.

## Strengths
1. **Important and well-motivated problem.** Semantic decoding from neural signals has genuine scientific and clinical value, particularly for augmentative communication. The focus on iEEG — with its high temporal resolution and signal quality — is a reasonable choice given the limitations of non-invasive modalities.

2. **Clean conceptual architecture.** The two-phase design (neural-to-embedding alignment via contrastive learning + embedding-to-text generation via pre-trained corrector) is intuitive and leverages existing pre-trained models effectively. This modular approach makes the method interpretable and each component independently testable.

3. **Rigorous zero-shot evaluation.** Holding out entire stories for zero-shot evaluation is a strong test of generalization that goes beyond simple train/test splits. The inclusion of both quantitative metrics and qualitative examples (including failure cases in Appendix A.4.2) provides a reasonably complete picture of model capabilities.

4. **Data efficiency demonstration.** The data scaling analysis (Figure 4A) showing near-linear improvement with data quantity is valuable for understanding how performance scales with dataset size in this domain. The electrode reduction analysis (Figure 4B) provides practical insights for deployment scenarios with limited electrode coverage.

5. **Hyperparameter analysis.** The ablation studies on α and τ (Appendix A.1) systematically explore the trade-off between contrastive and triplet loss components, providing useful guidance for future work. The embedding model comparison (Appendix A.3) also adds practical value.

6. **Honest limitation discussion (partial).** The limitations section acknowledges dependence on pre-trained components and hallucination risks, which is more transparent than many papers in this area. The failure case analysis (A.4.2) is particularly valuable for understanding model boundaries.

## Weaknesses
**W1. Electrode pooling invalidates subject-level independence (Critical).** Combining all 864 electrodes from 3 subjects into "a single subject for all analyses" (Section 2.2) is a fundamental methodological concern. This means (a) no per-subject results are reported, (b) electrode scaling analysis (Figure 4B) draws from a cross-subject pool that does not reflect single-subject deployment, and (c) the claimed "30 minutes of data" is pooled across subjects, effectively ~10 min/subject. This pooling may overestimate performance relative to any practical single-subject BCI scenario.

**W2. Baseline comparison confounded by modality mismatch (Major).** The baseline (Tang et al., 2023) was designed for fMRI, not iEEG. The "slight modifications" (different frequency bands, FIR delays) are not validated, and no iEEG-native baseline (e.g., direct LSTM encoder-decoder) is included. This makes it unclear whether Neuro2Semantic's gains come from genuine architectural advantage or from the baseline operating outside its intended modality.

**W3. Systematic overclaiming across narrative (Major).** The paper uses promotional language ("remarkable performance", "excels", "significant step forward") while WER remains >96% across all conditions. The "six times higher BERT scores" claim (Section 4.1) is a ratio-based inflation on a near-zero denominator. Zero-shot generalization is described as "strong performance" when BERT scores of 0.08-0.19 indicate only coarse thematic overlap.

**W4. Factual error in loss description (Major).** The text states that the triplet loss "minimizes the mean squared error (MSE) between corresponding pairs" (Section 2.1.1), but Eq. (4) implements a standard margin-based triplet ranking loss. MSE minimization and triplet ranking are fundamentally different objectives. This factual inaccuracy could mislead readers about the optimization target.

**W5. Method-implementation gap (Major).** The Vec2Text module is described (Section 2.1.2) as an iterative refinement process (Eq. 7, multiple steps until convergence), but the training uses "only one step for the refinement process" (Section 3.1). This discrepancy means the actual model does not perform the iterative refinement that is presented as a core feature.

**W6. Temporal leakage risk in in-domain evaluation (Major).** Leave-one-trial-out cross-validation uses preceding sentences from the same story for training, potentially giving the model topic-level information about held-out test sentences. This inflates in-domain metrics and makes the zero-shot results more trustworthy by comparison.

**W7. Missing reproducibility details (Minor).** Key architectural details are omitted: LSTM hidden dimension, the embedding dimension d (presumably 1536 from ada-002), temporal pooling strategy for converting variable-length iEEG segments to fixed embeddings, and the specific text truncation/length handling for the corrector.

## Key Issues
### Issue 1 (Critical): Cross-subject electrode pooling invalidates generalization claims
**Location:** Page 5 - Section 2.2 (Intracranial Recordings)
**Risk:** The pooled-electrode design makes it impossible to assess subject-level generalization, which is the primary practical requirement for BCI deployment. Without per-subject performance data, the results may overstate real-world applicability.
**Fix:** Report per-subject results separately. If performance is too low per subject, disclose this honestly. Run leave-one-subject-out cross-validation. Re-interpret all claims about "30 minutes of data" as "30 minutes of pooled data from 3 subjects."

### Issue 2 (Major): Loss function description contradicts formula
**Location:** Page 3 - Section 2.1.1 (between Eq. 4 and Eq. 5)
**Risk:** The text claims the triplet loss "minimizes the mean squared error (MSE) between corresponding pairs," but Eq. (4) implements margin-based triplet ranking. This is a factual error that could confuse readers and suggests unclear understanding of the optimization objective.
**Fix:** Replace the sentence with an accurate description: "This loss encourages each neural embedding to be closer to its corresponding text embedding than to a randomly sampled non-corresponding text embedding by a margin δ."

### Issue 3 (Major): Overclaiming across multiple sections
**Locations:** Page 1 - Abstract, Page 10 - Conclusion, Page 10 - Section 4.1 (Efficient Data Utilization), Page 10 - Zero-Shot Generalization
**Risk:** The paper uses "remarkable," "excels," "significant step forward," and "six times higher" language that is disproportionate to the evidence (WER > 96%, BERT scores 0.08-0.19 for zero-shot). This reduces scientific credibility.
**Fix:** Replace promotional language with evidence-bounded claims. Replace ratio claims with absolute deltas. Add explicit acknowledgment of high error rates in all summary statements.

### Issue 4 (Major): Method-implementation mismatch in Vec2Text refinement
**Location:** Page 4 - Section 2.1.2 vs Page 6 - Section 3.1
**Risk:** Section 2.1.2 describes iterative multi-step refinement (Eq. 7), but Section 3.1 states "the corrector used only one step." This discrepancy means the described method differs from the implemented method.
**Fix:** Either (a) update Section 2.1.2 to state that single-step refinement is used and explain why, or (b) implement and evaluate multi-step refinement and report the comparison as an ablation.

### Issue 5 (Major): Baseline comparison is potentially misleading
**Location:** Page 5 - Section 2.3, Page 10 - Section 4.1
**Risk:** The baseline (fMRI method adapted to iEEG) is compared without validating it as a competitive iEEG baseline. The "six times higher BERT scores" claim uses a ratio on near-zero values.
**Fix:** Add an iEEG-native baseline (e.g., LSTM encoder-decoder trained directly on iEEG without pretrained embeddings). Report absolute effect sizes. Acknowledge the modality adaptation confound.

### Issue 6 (Major): Temporal leakage in in-domain evaluation
**Location:** Page 5 - Section 3.1 (Training Procedure)
**Risk:** Training on preceding sentences from the same story as test sentences provides topic-level information, inflating in-domain metrics.
**Fix:** Report per-story zero-shot evaluation as the primary metric. Explicitly discuss the leakage risk in the main text.

## Actionable Suggestions
### S1. Restructure all claims to be evidence-bounded (Must)
**Affects:** Abstract, Introduction (Page 2 closing paragraph), Discussion (Section 4.1), Conclusion (Section 4.3)
Replace promotional language with precise, quantified claims:
- Replace "remarkable performance" → "improves BERT Score from 0.03 to 0.19 (Δ=0.16) and BLEU from 0.064 to 0.079 (Δ=0.015) in in-domain evaluation"
- Replace "six times higher BERT scores" → "BERT Score improvement of 0.16 absolute points" (ratios on near-zero baselines are misleading)
- Replace "excels in unconstrained text generation and zero-shot generalization" → "achieves BERT scores of 0.08-0.19 on held-out stories, indicating coarse thematic capture"
- Add explicit WER disclosure in all summary statements: "Word error rate remains 96.6%, indicating that precise word-level reconstruction is not yet achieved"

### S2. Report per-subject performance and remove pooling confound (Must)
**Affects:** Section 2.2, Section 3.4, Section 4.2, Section 4.3
- Report BERT, BLEU, ROUGE, and WER for each of the 3 subjects separately
- Add leave-one-subject-out cross-validation results
- Re-interpret electrode scaling analysis (Figure 4B) with per-subject electrode subsets
- If per-subject performance is significantly lower, disclose this as a primary limitation

### S3. Correct the triplet loss description (Must)
**Affects:** Section 2.1.1 (Page 3)
Replace: "This loss minimizes the mean squared error (MSE) between corresponding pairs of neural and text embeddings, while enforcing a margin δ"
With: "This triplet margin loss encourages each neural embedding to be closer to its corresponding text embedding than to a randomly sampled non-corresponding text embedding by at least margin δ"

### S4. Align Vec2Text description with implementation (Must)
**Affects:** Section 2.1.2 (Page 4), Section 3.1 (Page 6)
Either (a) update Section 2.1.2 to explicitly state that single-step refinement is used with a brief rationale, or (b) implement multi-step refinement and evaluate the difference as an ablation. If (a), add: "In this work, we use a single refinement step (t=1) because preliminary experiments showed diminishing returns from additional steps given the limited neural data, and to control computational cost."

### S5. Add iEEG-native baseline (Must)
**Affects:** Section 2.3 (Page 5), Table 1, Section 4.1
Add a simple LSTM-based encoder-decoder trained directly on iEEG-to-text mapping (no pre-trained embeddings). This provides a fair within-modality comparison and helps isolate the contribution of transfer learning from the contribution of the specific architecture.

### S6. Add multi-seed variance and significance reporting (Nice-to-have)
**Affects:** Table 1, Section 3.2
The reported standard deviations are large relative to the improvements (e.g., BERT SD 0.1283 vs mean 0.1947). Report results over 5 random seeds with statistical significance tests (paired t-test against baseline, with effect sizes). This is especially important given the small dataset (6 stories, ~30 minutes total).

### S7. Improve introduction narrative structure (Nice-to-have)
**Affects:** Section 1 (Page 1-2)
Restructure to: (1) state the problem and stakes (communication restoration), (2) identify the specific gap (iEEG semantic decoding with limited data), (3) explain why transfer learning addresses this gap (pre-trained components reduce neural data requirements), (4) preview key results and bounded claims.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

**S1 — Problem and domain:** "Decoding continuous language from neural signals is a central challenge for brain-computer interfaces, with potential to restore communication for individuals with severe speech impairments."

**S2 — Gap:** "Existing approaches face two key limitations: they either rely on motor intention decoding (missing semantic content) or require large neural datasets that are impractical to collect from clinical iEEG populations."

**S3 — Method:** "We introduce Neuro2Semantic, a two-phase transfer learning framework that first aligns iEEG signals with pre-trained text embeddings using an LSTM adapter trained with contrastive and triplet losses, then generates natural language from the aligned embeddings using a fine-tuned text inversion model."

**S4 — Key result (bounded):** "Evaluated on pooled iEEG from 3 subjects (~30 min total), Neuro2Semantic improves BERT Score from 0.03 to 0.19 (Δ=0.16) and BLEU from 0.064 to 0.079 over an fMRI-adapted baseline, while maintaining a word error rate of 96.6%. Zero-shot generalization to held-out stories yields BERT scores of 0.08-0.19, indicating coarse semantic capture."

**S5 — Implication:** "These results demonstrate the feasibility of low-data iEEG semantic decoding through transfer learning, while also highlighting the substantial gap to reliable word-level reconstruction needed for practical communication."

### Introduction Outline (Complete)

**P1 — Big Picture and Stakes (current: literature list → rewrite):**
"Decoding continuous language from neural signals could restore communication for individuals with locked-in syndrome or severe speech impairments. Neural decoding has been explored across fMRI, MEG, EEG, and iEEG modalities, but most work focuses on motor intention decoding or classification with fixed vocabularies, which cannot capture the full semantic richness of natural language."

**P2 — Gap and Opportunity (current: weak gap → sharpen):**
"A key open question is whether semantic content can be reliably decoded from iEEG, which offers high temporal resolution and direct cortical measurements but is limited by clinically constrained recording times—typically 30-60 minutes per subject. Transfer learning offers a potential solution: pre-trained text embeddings and language models could reduce the neural data required for decoding."

**P3 — Method Intuition (current: description without motivation → add rationale):**
"We propose Neuro2Semantic, which addresses data scarcity through two connected transfer learning steps. First, an LSTM adapter maps neural signals to a pre-trained text embedding space—learning only the neural-to-embedding mapping rather than language from scratch. Second, a pre-trained text inversion model (Vec2Text) generates natural language from the aligned embeddings, requiring adaptation only to the distribution of neural-aligned embeddings rather than full text generation learning."

**P4 — Contribution Summary and Bounded Results (current: overclaiming → tone down):**
"We demonstrate that this approach enables semantic decoding from as little as 30 minutes of iEEG data, outperforming an fMRI-adapted baseline. In-domain evaluation shows consistent gains in semantic similarity metrics, while zero-shot evaluation reveals partial thematic generalization. However, word error rates above 96% indicate that reliable word-level decoding remains an open challenge."

### Storyline Comparison

| Check | Current Storyline | Proposed Storyline |
|-------|-------------------|-------------------|
| Problem alignment | Generic "challenge in neuroscience" → specific "communication restoration" | Clear: problem → clinical need → specific technical gap |
| Variable alignment | Introduction lists modalities without linking to method variables | Introduction defines transfer learning need → method uses two pre-trained components |
| Contribution-evidence alignment | Claims "strong performance" and "remarkable" without bounds | Results preview includes absolute metrics and acknowledges WER limitations |

## Priority Revision Plan
### P0 — Must-fix before resubmission (validity-critical)

| Priority | Issue | Action | Expected Benefit | Effort |
|----------|-------|--------|-----------------|--------|
| P0.1 | Cross-subject electrode pooling | Report per-subject results; add leave-one-subject-out CV | Restores validity of generalization claims | Medium |
| P0.2 | Loss description factual error | Correct triplet loss description in text | Removes factual inaccuracy | Low |
| P0.3 | Method-implementation gap (Vec2Text) | Align description with actual 1-step refinement | Ensures reproducibility | Low |
| P0.4 | Baseline modality mismatch | Add iEEG-native baseline (LSTM encoder-decoder) | Enables fair comparison | Medium |

### P1 — Must-fix for clarity and credibility

| Priority | Issue | Action | Expected Benefit | Effort |
|----------|-------|--------|-----------------|--------|
| P1.1 | Systematic overclaiming | Rewrite Abstract, Intro closing, Discussion, Conclusion with bounded claims | Improves scientific credibility | Low |
| P1.2 | "6x" ratio claim replacement | Replace with absolute Δ and effect size | Prevents misleading interpretation | Low |
| P1.3 | Temporal leakage acknowledgment | Add explicit discussion and elevate zero-shot results as primary metric | Honest evaluation framing | Low |
| P1.4 | Missing architectural details | Report LSTM hidden dim, embedding dim, pooling strategy | Enables reproducibility | Low |

### P2 — Nice-to-have for quality improvement

| Priority | Issue | Action | Expected Benefit | Effort |
|----------|-------|--------|-----------------|--------|
| P2.1 | Multi-seed variance | Report results over 5 random seeds | Statistical reliability | Medium |
| P2.2 | Introduction narrative restructure | Follow proposed outline (stakes → gap → method → bounded results) | Reader engagement | Medium |
| P2.3 | Vec2Text step ablation | Compare 1-step vs multi-step refinement | Full understanding of trade-offs | Medium |
| P2.4 | Per-subject electrode scaling | Repeat Figure 4B within subjects | Clinical relevance | High |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Issue: Pooled electrodes]
    → [Fix: Per-subject + leave-one-subject-out]
    → [Expected: Validated generalizability claims]

[Issue: Overclaiming]
    → [Fix: Bounded language + absolute deltas + WER disclosure]
    → [Expected: Credible narrative]

[Issue: Loss description error]
    → [Fix: Replace "MSE minimization" with "margin-based triplet"]
    → [Expected: Accurate methodology]

[Issue: Unfair baseline]
    → [Fix: Add iEEG-native LSTM baseline]
    → [Expected: Fair comparison]

[Issue: Method-implementation mismatch]
    → [Fix: Align Vec2Text section with 1-step reality]
    → [Expected: Reproducible methods]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | In-domain performance vs baseline | Leave-one-trial-out CV, 6 stories, pooled iEEG (864 electrodes, 3 subjects) | BERT, BLEU, ROUGE, WER | BERT 0.19 vs 0.03 baseline; WER 0.966 vs 0.975 | Transfer learning improves semantic decoding over adapted fMRI baseline | Baseline is fMRI-adapted, not iEEG-native; pooled electrodes confound subject effects |
| E2 | Ablation: Phase 1 vs Phase 2 contributions | Same setup, individual phases evaluated separately | BERT, BLEU, ROUGE, WER | Full model > Phase 1 > Phase 2 | Both phases contribute; alignment is critical | Phase 2 alone uses random embeddings — not a fair control for comparison |
| E3 | Zero-shot out-of-domain generalization | Hold out entire stories (leave-one-story-out) | BERT, BLEU, ROUGE, 1-WER | BERT 0.08-0.19 (per story); consistently > baseline | Model captures coarse thematic content in unseen contexts | WER still >95%; qualitative examples show hallucination of specifics |
| E4 | Data scaling | Train on 20%-100% random subsets | BERT, BLEU, ROUGE, WER | Near-linear performance improvement with data | Performance scales with dataset size | Only evaluated on pooled data, not per-subject |
| E5 | Electrode scaling | Random subsets of 20%-100% of 864 pooled electrodes | BERT, BLEU, ROUGE, WER | 80% electrodes ≈ 100% in some runs | Model tolerates reduced electrode coverage | Pooled subsets ≠ per-subject subsets; misaligned with clinical relevance |
| E6 | Hyperparameter: α (loss weight) | Vary α in {0, 0.25, 0.5, 0.75, 1.0} | BERT, BLEU, ROUGE, WER | α=0.25 optimal | Balanced contrastive + triplet loss works best | — |
| E7 | Hyperparameter: τ (temperature) | Vary τ in {0.05, 0.1, 0.2, 0.3} | BERT, BLEU, ROUGE, WER | τ=0.1 optimal | Lower temperature improves alignment | — |
| E8 | Embedding model comparison | Compare text-embedding-ada-002 vs GTR-base | BERT, BLEU, ROUGE, WER | ada-002 slightly better BERT/BLEU; GTR better WER | Choice of embedding model affects performance | Only 2 models compared; limited generalizability |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Current Support | Gap |
|-------------------------|----------------|-----|
| **New knowledge** (Does the paper reveal something new about neural decoding?) | Partially — shows transfer learning works for iEEG semantic decoding with limited data | The contribution is primarily engineering (combining existing components) rather than scientific discovery; novelty verification deferred |
| **Reproducibility** (Can others replicate the method?) | Weak — missing architectural details (LSTM dim, pooling, embedding dimension), code not yet released, pooled-electrode analysis not reproducible per subject | Per-subject results, code release, and complete architectural specifications needed |
| **Change in practice** (Would this change how BCI decoding is done?) | Potentially — transfer learning could become standard for low-data neural decoding | Currently limited by (a) pooling confound, (b) no iEEG-native baseline comparison, (c) WER >96% limits practical utility |

### Proposed Research Experiments (P0/P1/P2)

| Experiment | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Quality Gain |
|-----------|-------------|-----------|---------------|-------------------|---------|-----------------|-----------|-------------|
| **P0-A: Per-subject validation** | Cross-subject generalization | Per-subject performance is lower than pooled but above chance | Train/evaluate on each subject separately (3 runs) | Pooled result as upper bound; random as lower bound | BERT, BLEU, WER per subject | At least 2/3 subjects above chance (p<0.05) | 1 day (reuse existing code) | Validity-critical: enables honest generalization claims |
| **P0-B: iEEG-native baseline** | Transfer learning benefit vs standard iEEG approach | Neuro2Semantic outperforms a direct LSTM encoder-decoder trained on iEEG only | Train LSTM encoder-decoder (no pretrained embeddings) on same data | Neuro2Semantic full model | BERT, BLEU, WER | Neuro2Semantic > baseline on all metrics | 0.5 day | Fair comparison; isolates transfer learning contribution |
| **P1-A: Vec2Text step ablation** | Multi-step refinement improves quality | More refinement steps → lower WER | Evaluate with 1, 2, 3, 5 refinement steps | 1-step as baseline | BERT, BLEU, WER, inference time | At least one metric improves ≥5% relative with 2+ steps | 0.5 day | Method-implementation gap closed |
| **P1-B: Leave-one-subject-out CV** | Model generalizes to new subjects | Zero-shot cross-subject performance above chance | Train on 2 subjects, test on held-out subject (3 folds) | Random baseline | BERT, BLEU, WER | BERT > random and >0.05 on held-out subject | 1 day | Strongest generalization test |
| **P2-A: Multi-seed significance** | Reported improvements are statistically reliable | Gains are stable across random seeds | Run full pipeline with 5 different seeds | Single-seed current results | BERT (mean±std), Cohen's d | Cohen's d ≥ 0.8 for primary comparisons | 2 days | Statistical rigor |

### ASCII Diagram — Experiment Upgrade Plan

```text
Stage 1 (Validity, ~2 days):
┌─────────────────────────────────────────────────┐
│ P0-A: Per-subject validation                    │
│ P0-B: iEEG-native baseline                      │
└──────────────────────┬──────────────────────────┘
                       ↓
Stage 2 (Robustness, ~2 days):
┌─────────────────────────────────────────────────┐
│ P1-A: Vec2Text step ablation                    │
│ P1-B: Leave-one-subject-out CV                  │
└──────────────────────┬──────────────────────────┘
                       ↓
Stage 3 (Polish, ~2 days):
┌─────────────────────────────────────────────────┐
│ P2-A: Multi-seed significance testing           │
│ P2-B: Claim/language revision (from S1/S2)      │
└─────────────────────────────────────────────────┘
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 4.5/10**

*Justification:* This score prioritizes research value and novelty as primary dimensions. The paper addresses an important problem (semantic decoding from iEEG with limited data) and the two-phase transfer learning approach is conceptually clean. However, the score is reduced due to:

- **Critical methodological concern:** Electrode pooling across subjects invalidates subject-level generalization claims and may overestimate performance.
- **Validity risks:** Unfair baseline comparison (fMRI-adapted to iEEG), temporal leakage in in-domain evaluation, factual error in loss description.
- **Overclaiming:** Systematic discrepancy between narrative language ("remarkable", "excels", "significant step forward") and evidence (WER > 96%, BERT scores 0.08-0.19 for zero-shot).
- **Limited novelty contribution:** Primarily an engineering combination of existing components (LSTM + contrastive learning + Vec2Text) applied to iEEG data. External literature verification was unavailable in this run, so novelty conclusions are deferred and conservatively marked as requiring manual verification.
- **Reproducibility gaps:** Missing architectural details (LSTM hidden size, embedding dimension d, temporal pooling strategy).

**Post-Revision Target: [6.0, 7.0]/10**

*Justification if all P0 and P1 issues are fixed:* If the authors (1) report per-subject results and demonstrate above-chance performance, (2) add an iEEG-native baseline, (3) correct all factual errors and overclaiming, (4) align the method description with implementation, and (5) acknowledge limitations transparently, the paper would present a solid empirical contribution demonstrating transfer learning for iEEG semantic decoding. The score ceiling is bounded by the inherent limitation that the core novelty rests on applying existing methods to a new modality/setting, which is incremental rather than transformative.