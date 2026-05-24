Now I have enough for calibration. Let me compile the final review.

**Bracket assessment:**

Round 1 placed this paper between 5.0–7.0. The model merging anchors at 5.33–5.50 (UQ-Merge, What Matters at Scale, Realistic Evaluation) have narrower scope; this paper has broader contributions (benchmark + method + comprehensive experiments). The high-score anchors (7.00–8.00) are large-scale benchmark papers (Mega-Bench, PhysBench) — this paper's benchmark is smaller in scale but adds a method contribution.

Round 2 narrowed: "Submodule Linearity" (6.00, Accept) — a method paper with modest gains and limited experiments. OptMerge is substantially stronger in experimental breadth and contribution scope. "MAP" (6.33, Accept) — clever idea but limited LLM experiments, presentation issues. OptMerge is comparable but has more comprehensive evaluation.

The paper lands at **6.0**: stronger than the 5.33–5.50 merging papers, comparable to other accepted method papers at 6.0–6.33, but with a significant Table 3 computation error and some expert-model quality concerns that prevent a higher score.

---

## Summary

This paper introduces the first benchmark for multimodal LLM (MLLM) model merging across five capability categories (VQA, Geometry, Chart, OCR, Grounding) with released checkpoints for both full fine-tuning (InternVL2.5) and LoRA (Qwen2-VL), and proposes OptMerge, a method that applies low-rank SVD denoising to task vectors and stabilizes optimization via SGD and mean initialization. The merged model is shown to match or approach mixture training baselines while being substantially cheaper, and modality merging experiments demonstrate effective cross-modal integration. The empirical scope is impressive: three model families (including 32B scale), both LoRA and full-FT settings, modality merging, and real-world HuggingFace checkpoints.

## Strengths

- **First MLLM merging benchmark with released artifacts.** The benchmark provides a fine-grained categorization of MLLM capabilities with publicly released checkpoints across two model families and both full and LoRA fine-tuning, enabling systematic comparison of 10 merging algorithms (Section 5.1, Tables 1–3). This fills a genuine gap identified by the authors: prior merging work focused on vision classifiers or LLM code/math tasks, not categorized MLLM capabilities.

- **OptMerge shows consistent, ablation-verified improvements.** The method's components (SGD, mean initialization, low-rank SVD) are individually ablated in Table 4, with each contributing measurable gains. On InternVL2.5 full-FT (Table 2), OptMerge achieves 57.44 vs. WUDI's 57.00; on HuggingFace checkpoints (Table 6), it reaches 66.70 vs. WUDI's 64.80 (+1.9%); on the large-scale Qwen2.5-VL-32B (Table 9), it attains 72.52 vs. the instruct baseline's 70.96.

- **Comprehensive experimental scope.** The evaluation spans full fine-tuning (InternVL2.5), LoRA (Qwen2-VL), modality merging (vision+audio+video, Table 5), real-world HuggingFace checkpoints (Table 6), and a 32B-scale model (Table 9) — far broader than prior MLLM merging work like UQ-Merge or AdaMMS, which were limited to single model families.

- **Compelling computational efficiency.** Table 7 demonstrates solving times of 0.22h (1B) and 3.78h (7B) with ≤22GB GPU memory vs. 24–25h and >240GB for mixture training, making a strong practical case for data-free merging.

- **Modality merging results are genuinely interesting.** The merged model (Table 5) achieves 67.00 average vs. the best single modality's 64.11, and notably matches or surpasses online composition methods (DAMC, NaiveMC) that store separate parameters per modality. This is a promising direction for Omni-model development.

## Weaknesses

### Major

- **Incorrect average computation in Table 3.** The reported average for WUDI Merging on Qwen2-VL (63.65) does not match the macro-average of the ten displayed per-task values, which computes to approximately 59.97. The other rows in the same table (Qwen2-VL-Base, individual experts, most methods) do appear to correctly reflect their macro-averages, making this a likely calculation error isolated to the WUDI row. Notably, OptMerge's displayed values yield a correct macro-average (~63.36, close to the reported 63.30), meaning OptMerge does outperform WUDI — the corrected numbers would actually *strengthen* the paper's conclusions. However, an error of this magnitude in a central results table must be corrected, and it raises concerns about verification of other reported numbers.

- **Expert model quality limits "outperforms experts" claims.** Several fine-tuned expert models degrade on their own target benchmarks. On InternVL2.5, Individual Geometry drops MathVista from 54.62 (base) to 32.80, and Individual Chart drops ChartQA from 18.42 to 10.53. On Qwen2-VL, Individual Geometry drops MathVista from 47.85 to 42.50. While the merged model does recover and often surpasses both base and experts, the claim that merging "outperforms expert MLLMs in their respective capabilities" (Section 1) is weakened when some experts are underperforming the base model on their own tasks. The benchmark would be more convincing if expert models were tuned to genuinely improve on their target tasks without catastrophic regression.

### Minor

- **The 2.48% average gain claim is untraceable.** The abstract and contributions (Section 1) claim "an average performance gain of 2.48%" from ablation studies, but this number does not obviously correspond to any computation from the reported tables (Table 4 shows gains of +4.43%, +4.65%, +2.42%, +2.35% — none of which average to 2.48%). The provenance of this headline number should be clarified.

- **No statistical backing for small-margin comparisons.** Several method comparisons involve differences of 0.5–1.0 percentage points (e.g., OptMerge vs. WUDI on InternVL2.5: 57.44 vs. 57.00, a 0.44% gap). Without multiple seeds, error bars, or variance estimates, the reliability of these margins is uncertain.

- **Theoretical justification for low-rank proxy is empirical, not proven.** The method replaces τ_i with its low-rank SVD approximation in the WUDI objective (Eq. 1 → Eq. 3), arguing that truncation removes noise and using ΣV^T as the data proxy yields better estimates. The paper does not prove or bound the error introduced by this substitution with respect to the linear-subspace property that Eq. 1 relies on. The ablation results provide empirical support, but the theoretical gap between Eq. 1 and Eq. 3 should be acknowledged.

### Trivial

- The paper's text claims SGD alone "drastically hurts performance (-9.77%)" (Table 4, Qwen2-VL: 58.65 → 48.88) and that the explanation about escaping flat optima is "not clearly supported." However, the paper does not claim SGD alone is beneficial — it explicitly states "Replacing Adam with SGD alone does not necessarily improve performance" and shows the combination with initialization is what works. The narrative is internally consistent.

## Nice-to-Haves

- Fine-tuning hyperparameters (learning rates, steps, batch sizes) that control parameter drift — central to Section 3.2 — should be reported to make the "small drift" claim verifiable and the benchmark reproducible.
- A more detailed specification of the modality merging pipeline (which LLM layers are merged, training procedures for single-modality models) would improve reproducibility.
- Cosine similarity or CKA plots between task vectors would help readers understand the claimed interference and the effect of low-rank truncation.
- Re-tuning the problematic expert models (Geometry, Chart) with better strategies would strengthen the benchmark's validity.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"WUDI is higher than OptMerge, contradicting the paper's claims" (Harsh Critic #1).** REMOVED. This criticism is partially factually wrong. The paper does *not* claim OptMerge beats WUDI on Table 3 — it specifically cites Tables 2 and 6 for that comparison ("For full fine-tuned models, Tables 2 and 6 show average improvements of 0.44% and 1.9% for OptMerge over WUDI Merging, respectively"). Furthermore, with corrected macro-averages, OptMerge (~63.36) would clearly beat WUDI (~59.97) on Table 3 as well. The valid sub-concern about WUDI's average being miscalculated is retained as a Major weakness above.

- **"The comparison with mixture training is not convincing" (Harsh Critic #3).** DEMOTED. For InternVL2.5, mixture training (57.66) edges OptMerge (57.44) by 0.22% — a negligible difference. For Qwen2-VL, OptMerge (63.30) surpasses Qwen2-VL-Instruct (62.23). The paper's claim is softened with "potentially surpasses," which is reasonable given the evidence. Using Qwen2-VL-Instruct as a proxy is defensible since it represents the result of extensive SFT on diverse data.

- **"Marginal gains with no statistical backing" (Harsh Critic #4).** RETAINED but downgraded to Minor. This is a real issue but is standard for benchmark-style papers; many accepted benchmarks do not report error bars. The larger gaps (e.g., OptMerge vs. WUDI on Qwen with corrected averages: ~63.36 vs. ~59.97, a ~3.4% gap) are clearly beyond noise.

- **"Theorem 3.1 contribution is marginal and not used later" (Harsh Critic, Section 3 notes).** REMOVED. The theorem directly motivates the benchmark's checkpoint design (keeping parameter changes small) and provides theoretical grounding for the empirical observation that less intensive fine-tuning aids merging — a point the paper explicitly uses to justify its expert training strategy (end of Section 3.2).

- **"Iso-C's catastrophic drop should be flagged as inappropriate, not simply reported" (Harsh Critic, Section 5 notes).** REMOVED. The paper does discuss this: "Iso-C fails on Qwen2-VL because the LoRA-tuned task vectors are already low-rank, and averaging singular values further reduces their Frobenius norm, creating instability in LLMs." This is a reasonable diagnosis, not a failure to flag the issue.

- **"The rank-size ablation shows the method is sensitive to this hyperparameter" (Harsh Critic, Table 8).** REMOVED. Table 8 shows stable performance for k ratios between 10% and 30% (56.93 → 57.43 → 56.63), with degradation only at 40–50%. The paper's conclusion that "OptMerge is robust to moderate changes in rank size" is accurate.

- **Strength Finder claim: "OptMerge achieves >2.4% gain over the strongest baseline."** REMOVED as stated. The 2.4% figure refers to an ablation improvement over WUDI in a specific setting, not over "the strongest baseline" (which varies by table).

- **Strength Finder claim: "Merged models match or surpass mixture training" — with unqualified "surpass."** SOFTENED. On InternVL2.5, mixture training (57.66) and OptMerge (57.44) are essentially tied; on Qwen2-VL, OptMerge leads (63.30 vs. 62.23). The "match" characterization is fair; "surpass" is only partially supported.

## Novel Insights

The paper's most interesting insight is the empirical demonstration that modality merging via static weight interpolation can match or surpass online composition methods (DAMC, NaiveMC) that require storing and dynamically routing separate parameters per modality. This suggests that modality-specific knowledge becomes embedded in shared weight space in a way that linear merging can recover — a finding with implications for efficient Omni-model development that goes beyond the paper's own contributions.

## Suggestions

- Correct the WUDI average in Table 3 to reflect the actual macro-average (~59.97). This will actually strengthen the paper's claims.
- Explicitly trace the 2.48% claim to a specific computation, or remove it and report per-setting gains.
- Re-tune the Geometry and Chart expert models to ensure they improve over the base model on their target tasks, or add a discussion of why this degradation occurs and why the merged model's recovery is still meaningful.
- Add a brief discussion acknowledging that the low-rank SVD substitution in Eq. 3 is empirically motivated and that the linear subspace property is assumed rather than proven to be preserved.

---

## Score and Decision

**Anchor comparison summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| ATM (lNtio1tdbL) | 3.00 | R1 | OptMerge is clearly stronger — ATM has fundamental misalignment issues |
| Realistic Eval (Bq3fEAGXUL) | 5.33 | R1 | OptMerge has more novelty (method + benchmark vs. evaluation only) |
| What Matters at Scale (fvUVe2gJh0) | 5.33 | R1 | OptMerge has broader scope and a novel method; this anchor is purely empirical |
| UQ-Merge (SO0manOwUF) | 5.50 | R1 | OptMerge is more comprehensive (multiple model families, data-free, benchmark) |
| MMER (WjPK2gj0xu) | 5.50 | R1 | Comparable novelty but OptMerge has broader experiments and benchmark contribution |
| Submodule Linearity (irPcM6X5FV) | 6.00 | R2 | OptMerge is stronger — broader experiments, more significant gains, benchmark added |
| MAP (1v7SRWsYve) | 6.33 | R2 | Comparable quality; OptMerge has more comprehensive evaluation but MAP has a cleaner central idea |
| MME-RealWorld (k5VHHgsRbi) | 6.80 | R2 | MME-RealWorld is a stronger pure benchmark; OptMerge adds method but at smaller benchmark scale |
| Mega-Bench (2rWbKbmOuM) | 7.00 | R2 | Mega-Bench is clearly stronger as a benchmark contribution |

**Round 1 bracket:** 5.0–7.0. **Round 2 narrowed:** 6.0–6.5. The paper is comparable to the 6.00–6.33 accepted model-merging method papers, with broader experiments but a notable calculation error. Settling at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>