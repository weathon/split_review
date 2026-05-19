- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 3, 5, 3
Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes RAEG, a framework that combines knowledge injection (via Knowledge Editing with MALMEN or Parameter-Efficient Fine-Tuning with LoRA) with standard Retrieval-Augmented Generation for open-domain question answering. The central idea is to internalize knowledge from retrieved paragraphs into the model's parameters and then still use RAG at inference time, creating a "dual mechanism." The paper reports experiments on Llama2-7B over NQ and TriviaQA, finding that PEFT-based RAEG outperforms standard RAG baselines, while KE-based RAEG lags and requires remediation via re-ranking and parameter pruning.

---

## Strengths

- **Systematic empirical comparison of KE vs. PEFT within a RAG context.** The paper formulates two explicit research questions (Section 3.1.2) and reports head-to-head results (Table 1) showing that PEFT (LoRA) preserves the model's reasoning ability when combined with RAG better than KE (MALMEN). This is a concrete, non-obvious finding — one might intuitively expect localized edits to be less disruptive than global fine-tuning, and the paper provides evidence to the contrary.

- **Re-ranking mechanism demonstrably improves KE-based RAEG.** Section 4.1.1 describes a trained re-ranker (Algorithm 1) trained with binary relevance labels from DPR retrieval. Table 2 reports 8%–12% performance gains for KE+RAG after applying re-ranking, showing the module addresses a real failure mode of KE in this setting.

- **Parameter pruning ablation provides granular insight into KE side effects.** Section 4.2 and Table 3 systematically compare magnitude-based and random pruning at ratios from 10%–90%. The finding that magnitude-based pruning is more effective at low ratios (below 50%) while random pruning recovers at high ratios is a practically useful characterization.

---

## Weaknesses

### Fatal
None.

### Major

- **The evaluation confound between injection data volume and the dual-mechanism claim.** The RAEG methods are fine-tuned/edited on synthetic QA pairs generated from multiple retrieved paragraphs (Top‑1, 2, 4, 8), while the RAG baselines (Direct‑RAG, Prompt‑RAG) use the *original, unmodified* model retrieving only Top‑1 at test time. This means the RAEG model has been exposed to additional relevant (synthetic) QA data during injection that the baseline has not. The paper's headline claim — that the "dual mechanism" (injection + RAG) drives improvements — is not cleanly separable from the effect of simply fine-tuning on more relevant data.

    The Top‑1 injection case partially mitigates this (injection from one paragraph, RAG from one paragraph), and the paper does report injection-only results. But the key comparison (PEFT+P‑RAG vs. P‑RAG) still compares a model fine-tuned on synthetic QA pairs against an unmodified model, making it impossible to attribute gains specifically to the dual mechanism rather than to fine-tuning per se. A proper controlled baseline — fine-tune the baseline model on the same synthetic QA pairs and then compare with vs. without RAG — is needed to support the paper's strongest claims.

- **Scope is narrower than the framing implies.** The paper presents a broad comparison of "Knowledge Editing vs. Parameter-Efficient Fine-Tuning" but tests only one method per category: MALMEN (KE) and LoRA (PEFT). Generalizations about KE vs. PEFT as categories are premature; other editing methods (ROME, MEMIT) or PEFT variants (adapter tuning, prompt tuning) could behave very differently. The title and abstract imply a broader study than the experiments support.

### Minor

- **No variance or significance estimates.** All reported numbers are single-run point estimates. Given modest differences in some comparisons (e.g., KE+P‑RAG vs. P‑RAG on NQ), it is unclear whether the observed improvements are statistically reliable. While single-run benchmarking is common in this area, the paper would be strengthened by error bars or significance tests, especially since some of the claims hinge on relatively small margins.

- **Synthetic QA quality is not assessed.** The paper relies on GPT-4o-mini for generating synthetic question-answer pairs (Section 3.2) and uses these as editing facts, but provides no human evaluation or automatic quality check of the generated pairs. Errors or biases in the synthetic data could directly affect downstream results, and the reader has no way to assess this risk.

- **Figure 3 (determining K=1 for RAG) uses the original, unedited model.** The paper selects K=1 for RAG based on experiments with the base model (Figure 3), but does not verify that the same optimal K holds for the post-injection model. This is a small oversight but relevant since the dual mechanism's effectiveness could depend on RAG configuration.

- **Re-ranker is not evaluated in isolation.** The paper describes re-ranker training (Algorithm 1) and reports its aggregate impact on the full pipeline (Table 2), but never evaluates the re-ranker's standalone performance (e.g., precision/recall of relevance classification). It is unclear how much of the 8%–12% gain comes from better retrieval vs. other factors.

- **Parameter pruning ablation is only shown for KE on NQ.** The pruning study (Table 3) covers only the KE method on the NQ dataset. Results for TQA and for PEFT would be informative, especially since the paper frames pruning as a general mitigation strategy.

- **Post-hoc explanations for KE underperformance on TQA are unsupported.** The paper attributes KE's worse performance on TriviaQA to "dataset nature, question complexity, coverage of pre-trained knowledge" without any supporting analysis (e.g., per-question breakdown, qualitative examples). These explanations are speculative.

### Trivial
- Minor wording imprecision in the abstract ("editing the retrieved paragraphs to inject necessary knowledge" — the paragraphs are not edited, the model is edited using knowledge from the paragraphs).

---

## Nice-to-Haves
- Error analysis categorizing what kinds of questions KE helps vs. hurts.
- Discussion of computational cost (KE vs. PEFT runtime/memory profiles), relevant for a practical method.
- Verification that the optimal K for RAG remains K=1 after knowledge injection.

---

## Removed Points

These points were considered and removed for the following reasons:

- **"The evidence for the dual mechanism is weak and confounded" (specific math claim):** The critic states "the gain from P-RAG alone over the base model (4.5 points)" — this is factually incorrect. The P‑RAG gain over the base model is approximately 11 points on NQ, not 4.5. The 4.5 figure corresponds to Direct‑RAG. The critic's arithmetic undermines this specific sub-claim. Removed.

- **Figure 1 framing contradiction:** The reviewer claims Figure 1 creates an unresolved "framing contradiction." The paper clearly presents Figure 1(c) as a *problem* that RAEG addresses (Section 1: "adjusting model parameters may impair its performance in RAG..."). The framing is consistent: identify problem → propose solution. Removed as a misreading.

- **Missing positioning relative to RETRO/ATLAS:** I have been instructed not to penalize missing related work citations. Removed per instructions.

- **"Novel paradigm" language is disproportionate:** This is a subjective framing judgment, not a verifiable weakness. Comparable framing language is common in the literature. Removed.

- **Statistical significance concern presented as a fatal flaw:** Downgraded from major to minor — single-run evaluation without variance is standard practice for this type of benchmark study, even if not ideal.

- **Criticisms about missing appendix content (Table 8, etc.):** The parser strips appendix content from all papers. Removed per instructions.

---

## Novel Insights

Beyond the paper's own contributions, the most interesting emergent observation from the reviews is the tension between the two reviewers' assessments of the confound. The harsh critic treats the injection-data-volume confound as a fatal flaw that invalidates the headline claims. But in reality, the paper reports injection-only results side-by-side, and the Top‑1 injection case (same number of paragraphs) does show PEFT+P‑RAG outperforming P‑RAG. This suggests the core finding — that PEFT-based injection can enhance RAG beyond what RAG alone achieves — is likely robust, even though the precise contribution of the "dual mechanism" vs. "fine-tuning on relevant data" remains untangled. The paper would benefit from an additional control condition (fine-tuned model without RAG vs. fine-tuned model with RAG) to cleanly resolve this ambiguity.

---

## Suggestions

1. **Add a controlled baseline:** Fine-tune the model on the same synthetic QA pairs (from Top‑1 paragraphs) and report results with and without RAG. This separates the effect of fine-tuning from the dual-mechanism claim and would directly address the main confound.

2. **Expand method coverage:** Test at least one additional KE method (e.g., ROME or MEMIT) and one additional PEFT method (e.g., adapter tuning) before drawing categorical conclusions about "KE vs. PEFT."

3. **Replace point estimates with multi-run results** (at least 3 seeds) with mean and standard deviation for the key comparisons.

4. **Evaluate synthetic data quality** with a small human annotation study or automatic consistency check, and report the accuracy of the generated QA pairs.

5. **Report re-ranker performance in isolation** (precision, recall, F1 on a held-out set) to help readers understand where the gains in Table 2 come from.

---
