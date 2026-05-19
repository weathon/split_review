- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5
Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper introduces EditMark, a training-free watermarking method for open-source LLMs that uses model editing to embed watermarks by controlling the *precision* of numerical answers to open-ended questions. The core insight—that LLMs can produce multiple correct answers to the same question, and this answer diversity can serve as a covert channel—is clever and original. EditMark embeds an 8-bit watermark in ~100 seconds with near-100% extraction success rate (ESR) while preserving model performance on standard benchmarks. The evaluation covers four models, multiple watermark capacities, fine-tuning and editing attacks, temperature variation, and alternative mapping types.

---

## Strengths

- **Training-free efficiency**: EditMark embeds an 8-bit watermark in 93–110 seconds across GPT-J-6B, LLaMA-7B, and Baichuan-7B, while KIMark requires 9,410 seconds on LLaMA-7B (Table 2, Section 5.2). This is orders of magnitude faster than training-based approaches and directly supports the paper's central claim.

- **High extraction success rate**: EditMark achieves 100% ESR for 8-bit watermarks on all three large models (Table 2) and >90% ESR across a range of capacities up to 120 bits (Table 3; Section 5.6 with sequence-based mapping). The results convincingly demonstrate the method's effectiveness.

- **Negligible fidelity impact**: Evaluation on BLiMP and MMLU benchmarks (Tables 6–7, Section 5.5) shows that EditMark introduces at most 1–2% accuracy degradation, supporting the "harmless" claim. This contrasts with backdoor-based methods, which alter model behavior.

- **Robust to fine-tuning for two of three models**: GPT-J-6B and Baichuan-7B retain 100% ESR after LoRA fine-tuning (Table 5, Section 5.4). This is a genuinely strong result that backdoor-based methods cannot match (e.g., Backdoor drops to 1.8% on LLaMA-7B under the same attack).

- **Generalizes across mapping types and editing algorithms**: The method works with both precision-based and sequence-based answer diversity (Table 9, Section 5.6) and with both MEMIT and EMMET editing algorithms (Table 10, Section 5.6), demonstrating that the approach is not tied to a specific implementation choice.

- **Robust to temperature variation**: ESR remains close to 100% at temperature=0.5 and 1.0 (Table 8, Section 5.6), confirming extraction works under sampling.

---

## Weaknesses

### Fatal
None.

### Major

- **Robustness claim is overstated for LLaMA-7B**: The paper states in the introduction (line 22) that "EditMark has proven robust, demonstrating an almost unchanged watermark extraction success rate following model fine-tuning." However, Table 5 (line 206) shows that for LLaMA-7B, ESR drops from **97.9% to 79.1%** after three rounds of fine-tuning—a ~19 percentage point decline. "Almost unchanged" is accurate for GPT-J-6B (100% → 100%) and Baichuan-7B (97.9% → 100%), but it misrepresents the LLaMA-7B result. The paper's own explanation (higher-layer edits being more susceptible to fine-tuning) is reasonable, but the blanket statement in the abstract and introduction should be qualified by model, and the drop should be explicitly reported rather than glossed over. This does not invalidate the contribution, but it must be corrected.

### Minor

- **Decoding strategy for watermark extraction is underspecified**: Section 4.3 describes extraction as "query the LLM with the same questions" but does not state which decoding strategy (greedy, temperature=0, beam search, etc.) was used in the main experiments (Tables 2, 3, 5). Temperature variation is tested separately in the ablation (Table 8), but the default extraction conditions are never specified. Since model editing outputs are deterministic only under greedy decoding, and the paper does not clarify whether extraction was always performed greedily or whether the reported numbers are averaged over sampled runs, the reader cannot fully assess the reliability of extraction in a practical black-box setting. A one-sentence clarification in Section 4.3 or Section 5.1 would resolve this.

- **False positive rate description is confusing**: Line 206 states "we also calculate the ESR of the non-watermark model extracted with watermark text... The results indicate that both EditMark and baseline methods have lower ESR, which demonstrates that EditMark has a lower false positive rate." The text appears to conflate ESR and FPR terminology, and the reasoning is hard to follow. Table 4 presumably contains the correct data, but the textual description needs revision for clarity.

- **Backdoor and BadEdit baselines at 8-bit are at a structural disadvantage**: The paper acknowledges (line 169) that an 8-bit watermark for these baselines comprises eight independent backdoors. This naturally increases conflict and reduces ESR. While the comparison is not unfair per se—it reflects real capacity limitations of these methods—the paper should explicitly discuss this asymmetry rather than leaving it implicit.

### Trivial
None.

---

## Nice-to-Haves

- Add a dedicated limitations paragraph acknowledging: (i) model-dependent robustness (LLaMA-7B vs. GPT-J-6B), (ii) dependence on the success rate of model editing, (iii) the need for diverse QA templates against informed attackers (level-3 attacks in Figure 3), and (iv) the reliance on secret key management.
- Discuss the security implications of the PRNG-based question selection: if an attacker obtains the secret key, they can reproduce the exact QA pairs and potentially remove the watermark.
- A direct fidelity check on the watermarked questions themselves (i.e., verifying that the watermarked answers are still correct) would strengthen the "harmless" claim beyond unrelated benchmarks.
- Confidence intervals or standard deviations for ESR across repeated extractions would improve the statistical grounding, though the absence is not a flaw given community norms in this area.

---

## Removed Points

These points were flagged in the reviews but are removed from the main assessment for the reasons noted:

- **Over-reliance on greedy decoding speculation**: The critic's concern about stochastic sampling (top-k/top-p) affecting extraction was not tested, but the paper does show temperature robustness in the ablation (Table 8). The main issue is that the *default extraction conditions are unspecified*, which is already captured in the Minor weaknesses above. The speculative extension to top-k/top-p is removed.
- **"The method's reliance on open-ended questions is both a strength and a limitation"**: The paper already acknowledges this implicitly by scoping the method to open-ended questions and providing multiple mapping templates. This is a feature, not a bug, and is adequately motivated.
- **"The example in Section 3.2 uses factual knowledge edit not watermark edit"**: This is a pedagogical choice to introduce model editing. The distinction is clarified by the design of the method itself in Section 4. The point is too minor to retain.
- **"α=2 should be explained"**: The paper states α is the "minimum precision" (line 111). This is sufficiently clear.
- **Statistical significance / confidence intervals**: Requesting variance measures for single-run benchmark evaluations is not standard practice for this type of empirical paper and would not change the conclusions.
- **Broader benchmark for fidelity**: Requesting evaluation on the watermarked questions themselves is a reasonable extension but goes beyond what the paper scoped. BLiMP and MMLU are standard fidelity benchmarks; the existing evaluation is adequate.
- **"Missing related works"**: Removed per instructions (no external sources to confirm existence).
- **Formatting nitpicks and parser artifacts**: Removed per instructions.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Qualify the robustness claim**: Replace "almost unchanged watermark extraction success rate" in the abstract and introduction with a model-specific characterization (e.g., "robust for GPT-J-6B and Baichuan-7B, with some degradation on LLaMA-7B—a pattern attributable to editing depth").
2. **Specify the extraction decoding strategy**: Add one sentence to Section 4.3 or Section 5.1 stating the temperature/decoding used in all main experiments (e.g., "All main experiments extract watermarks with greedy decoding (temperature=0)").
3. **Clarify the FPR description**: Rewrite the confusing sentence in Section 5.3 to correctly distinguish ESR vs. FPR and reference Table 4 clearly.
4. **Add a limitations paragraph** in the conclusion or a separate section addressing model-dependent robustness, level-3 attack vulnerability, and key management assumptions.

---
