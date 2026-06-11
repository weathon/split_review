## Summary

The paper proposes Forget-to-Focus (F2F), a two-stage protocol that applies gradient-ascent-based unlearning on a "forget set" of general-domain text (with a retain set for stability), followed by standard fine-tuning on a domain-specific dataset. The goal is to repurpose machine unlearning from privacy to domain specialization by suppressing irrelevant pretraining knowledge before adaptation. Experiments span coding (HumanEval, MBPP), medical (PubMedQA, MedMCQA), and math (MATH, GSM8K) domains across models from 0.6B to 72B parameters.

## Strengths

1. **Consistent accuracy improvements across model scales and domains**: Table 1 shows F2F (Unl_GA+GD + SFT) achieves the best or second-best pass@1 in all 10 model–benchmark pairs for coding across five model sizes. The pattern extends to medical and math domains in Table 3. This establishes that preparatory unlearning consistently boosts downstream accuracy across architectures and scales — the paper's central empirical finding is supported.

2. **Systematic ablation of forget-set quality**: Section 4.4 and Table 3 compare three forget-set construction strategies (BC-Select, BC-Mixed, BC-Cosine) across three models and six benchmarks, showing curated forget sets outperform mixed ones. BC-Cosine (automatic similarity-based selection) approaches curated quality, providing practical deployment guidance.

3. **Multiple unlearning algorithms compared**: Section 4.3 and Figure 3 compare GA+GD, GA-only, NPO, and GA+KL across two model scales, showing GA+GD reliably outperforms GA-only and that larger models tolerate GA-only unlearning better than smaller ones.

4. **Representation geometry analysis (CKA/SVCCA)**: Section 4.5 provides mechanistic evidence that F2F reshapes internal representations, going beyond accuracy numbers to probe why the method works.

## Weaknesses

### Fatal

None.

### Major

- **Unsupported headline claim about calibration improvement**: The abstract, contributions list (bullet 3), and conclusion prominently claim that F2F "improves calibration on medical QA tasks, reducing overconfidence." Yet Sections 1–5 contain zero calibration analysis — no ECE scores, reliability diagrams, confidence histograms, or even a discussion of calibration methodology. The paper says "More analysis and ablations are given in the appendix section A" at the end of Section 4.5, but this generic statement does not specifically reference calibration, and a reader of the main text cannot verify or assess this asserted finding. Presenting calibration improvement as a headline finding in the abstract without summary evidence in the main body is a significant credibility issue.

- **Retain-set confound not controlled for**: F2F is a two-phase protocol where the unlearning phase already exposes the model to in-domain data (the retain set is "a small subset of the fine-tuning data," Section 3.3) before the fine-tuning phase begins. Standard fine-tuning baselines receive a single phase. The paper does not include a control that runs gradient descent on the retain set alone (without gradient ascent on the forget set) before fine-tuning. Without this ablation, the improvement attributed to "unlearning" could partly or entirely reflect the benefit of additional in-domain gradient steps during the unlearning phase rather than the suppression of generalist features. This threatens the causal interpretation of the paper's core claim.

### Minor

- **Abstract contains a numerical error**: The abstract claims F2F "improves HumanEval pass@1 by [...] 11.95% on Qwen 72B model compared to standard fine-tuning." From Table 1, SFT achieves 71.12 and F2F+SFT achieves 78.50; the relative improvement is (78.50−71.12)/71.12 ≈ 10.38%, not 11.95%. The 11.95% figure only matches when comparing F2F+SFT to the base model (70.12), which is not "standard fine-tuning." This error is verifiable from the paper's own data and indicates the abstract was not carefully proofread against the results.

- **Missing data point in Table 1**: The row for Qwen 72B Unl_GA+GD does not report a HumanEval value (the cell is empty). This is a data gap in a key result for the largest model.

- **Section 4.2 framing does not match content**: The section is titled "F2F w/ Fine-Tuning Variants" but Table 2 presents only baseline methods (SFT, LoRA, CurlLoRA, DAPT) without any F2F rows. The actual F2F medical results appear elsewhere (Figure 3, Table 3), but the section promises a comparison it does not directly deliver.

- **No statistical variance reported**: All results across Tables 1, 2, and 3 are single point estimates without error bars, confidence intervals, or multiple-run statistics. Several comparisons are close (e.g., F2F+SFT 72.50 vs. DAPT 71.90 on MBPP for Qwen 72B), making it impossible to assess which differences are significant.

- **CKA analysis lacks a ground-truth reference point**: Section 4.5 shows F2F diverges more from the base model than standard fine-tuning does, but does not establish whether this divergence is toward a more desirable representation. Without a reference (e.g., a model trained from scratch on domain data, or one that received extra in-domain training), lower CKA similarity could indicate arbitrary drift rather than targeted specialization.

### Trivial

None.

## Nice-to-Haves

- A control experiment comparing GA+GD vs. GD-only (retain-set gradient descent without GA on forget set) would cleanly isolate whether gains come from unlearning or extra retain-set exposure. This is the single most impactful improvement the paper could make.
- Learning curves or optimization trajectories would substantiate the claim of "stabler optimization dynamics" made in the abstract and conclusion.
- Including error bars or reporting multiple seeds for at least a subset of key comparisons would help the reader assess result reliability.
- Figure 3 would benefit from including the "no unlearning" (SFT-only) baseline as a reference bar.

## Removed Points

1. **"Theoretical analysis does not apply to neural networks"**: The paper explicitly states it uses a "convex linear surrogate" (Section 2) and acknowledges it is a simplification. The paper is transparent about this limitation.
2. **"Gemma-2B baseline degrades after SFT"**: Discussed directly in Section 4.1 (observation 5). The paper acknowledges this behavior and notes that F2F recovers performance.
3. **"Hyperparameter differences across models"**: All choices are reported transparently in Section 3.4 with rationale (higher LR for LLaMA, QLoRA for 72B, fewer epochs for larger models). Reasonable for practical GPU constraints.
4. **"Table 3 formatting hard to parse"**: A style/presentation nitpick. Removed per formatting rules.
5. **"Forget set sizes asymmetric"**: Reported transparently (100 for Qwen-0.6B, 1000 for others). A design choice the paper is open about.
6. **"Fisher/PCA analyses missing from main body"**: The paper says "More analysis and ablations are given in the appendix section A" at the end of Section 4.5. The parser removed the appendix. Per rules, weaknesses about content deferred to a stripped appendix are removed. The calibration claim is retained separately because it is presented as a headline finding in the abstract/conclusion without even a specific appendix reference.

## Novel Insights

None beyond the paper's own contributions. The central empirical finding — that preparatory unlearning (GA+GD) consistently improves downstream accuracy across diverse domains and scales — is the paper's main contribution. The insight that F2F reshapes internal representations away from generalist initialization is a useful mechanistic observation but has ambiguous interpretation without a reference point.

## Suggestions

1. **Either add calibration analysis or retract the claim.** If calibration data exists in the appendix, add a summary table/figure and explicit pointer in the main body. If not, remove the claim from the abstract, contributions list, and conclusion.
2. **Add the GD-only retain-set control ablation** to isolate whether gains come from unlearning or extra data exposure. This is critical for the paper's causal narrative.
3. **Correct the numerical error in the abstract** (11.95% → 10.38%, or clarify the comparison baseline).
4. **Fill the missing HumanEval value for Qwen 72B Unl_GA+GD** in Table 1.
5. **Add error bars or multi-run statistics** for at least a subset of key comparisons.
6. **Re-title Section 4.2 or restructure it** so the table includes the promised F2F comparisons.
7. **Add a reference point to the CKA analysis** (e.g., comparison to a model with extra in-domain training) to help interpret whether the observed divergence is directionally correct.

## Calibration Anchors

**Round 1 — Bracketing (3 queries)**:
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `ijwYWoChN9.md` (Domain Shift Tuning) | 3.00 | R1-low | Weaker than our paper; rejected for limited scope |
| `ZbOSRZ0JXH.md` (Data-free OOD Generalization) | 3.00 | R1-low | Weaker; different topic but same band |
| `BJfIDS5LsS.md` (MASIMU Unlearning) | 2.50 | R1-low | Much weaker; rejected |
| `nA9SCxGy2M.md` (Model-Driven Fine-tuning) | 2.50 | R1-low | Much weaker |
| `J9Ofr1PmvX.md` (UnSTAR Unlearning) | 5.50 | R1-mid | Comparable scope; UnSTAR is narrower (1 dataset) but cleaner execution |
| `CIN2VRxPKU.md` (Evaluating Deep Unlearning) | 5.33 | R1-mid | Comparable; evaluation paper with clearer framing |
| `uDjuCpQH5N.md` (Do Unlearning Methods Remove Info) | 5.50 | R1-mid | Comparable; rejected despite one strong review |
| `6ESRicalFE.md` (FLAT Unlearning) | 6.50 | R1-mid | Stronger than our paper; cleaner execution, accepted |
| `jOmk0uS1hl.md` (Training on Test Task) | 8.00 | R1-high | Much stronger; different topic |
| `SPS6HzVzyt.md` (Context-Parametric Inversion) | 8.00 | R1-high | Much stronger; different topic |
| `WbWtOYIzIK.md` (Knowledge Card) | 8.00 | R1-high | Much stronger; different topic |
| `f4gF6AIHRy.md` (Combatting Dimensional Collapse) | 8.00 | R1-high | Much stronger; different topic |

**Round 2 — Narrowing (2 queries, bracket ~4.5–7.5)**:
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `RQz7szbVDs.md` (Theory of Initialisation's Impact) | 6.00 | R2 | Not directly comparable (theory paper); higher score |
| `huo8MqVH6t.md` (Rethinking LLM Unlearning Objectives) | 6.00 | R2 | Stronger execution; accepted despite mixed reviews (8,6,3,8,5,6) |
| `1ExfUpmIW4.md` (Robust and Cost-Efficient Unlearning) | 6.00 | R2 | Cleaner execution; consistent 6s, accepted |
| `3p4raemLAH.md` (SLUG Targeted Unlearning) | 5.75 | R2 | Rejected despite one 8; our paper has broader scope but more structural issues |
| `e6xFKjo4Cp.md` (Learn while Unlearn) | 4.75 | R2 | Weaker; iterative unlearning framework |

**Round 1 bracket**: 4.5–6.5 (topically similar papers between 5.33 and 6.50).  
**Round 2 narrowing**: Our paper is weaker than the accepted anchors at 6.00–6.50 (FLAT, Rethinking LLM Unlearning, Robust/Cost-Efficient) due to the unsupported calibration claim and uncontrolled retain-set confound. It is stronger than the weakest rejected papers (Learn while Unlearn at 4.75) and comparable to mid-range rejected papers (UnSTAR at 5.50, SLUG at 5.75).  
**Final score**: **5.0** — a borderline paper with an interesting idea and broad experiments, but the two major weaknesses (unsupported headline claim about calibration, uncontrolled retain-set confound) significantly undermine its reliability in its current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>