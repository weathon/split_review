Now I have all the evidence I need. Let me write the final review.

---

## Summary

This paper proposes a self-evolution framework in which a single language model serves as both generator and verifier to construct preference data for DPO fine-tuning, eliminating reliance on external supervision. The key technical contribution is thresholded majority voting to extract reliable signals from noisy self-verification. Two variants are explored: SimpleGV (single-turn verification) and RevisionGV (multi-turn feedback-driven revision). The method is evaluated on the Knights and Knaves (KK) logical reasoning benchmark and four standard math benchmarks.

## Strengths

- **Thresholded majority voting demonstrably improves verification accuracy and enables co-evolution:** Figure 2 shows that SimpleGV-trained models achieve consistently higher verification accuracy than the base model across all thresholds on the KK training set (e.g., ~74% vs. ~62% at τ=0.50), directly supporting the claim that verification capability co-evolves with generation capability through self-training.

- **Clean easy-to-hard generalization results:** Table 3 demonstrates that training only on KK instances with 2–3 people and evaluating on 4–5 and 6–8 person test sets yields substantial transfer (45.4% on 4–5, 17.5% on 6–8 vs. base model's 31.1% and 10.3%). This experimental design convincingly rules out memorization and provides evidence of genuine reasoning improvement.

- **RevisionGV consistently outperforms SimpleGV for capable models, with honest reporting of failure cases:** Table 4 shows RevisionGV beats the best SimpleGV threshold on 4B (42.2% vs. 40.7%) and 12B (52.8% vs. 51.1%) models, while transparently reporting that the 1B model does not benefit (7.8% vs. 8.4%). The 12B RevisionGV result (52.8%) approaches the oracle verifier's 53.6%.

- **Comprehensive ablation studies:** The cost analysis (Figure 5) provides actionable guidance that scaling verifier computation is more cost-effective than scaling generator computation. The data size analysis (Figure 4) honestly reports diminishing returns and regression at 40K samples. Iterative DPO (Table 2) and curriculum learning (Table 3) each provide incremental, measurable gains without overclaiming.

- **The method operates under minimal assumptions:** Unlike baselines that require online RL, code execution environments, or supervised reward models, SimpleGV uses only unlabeled prompts with offline DPO and no external tools.

## Weaknesses

### Fatal
None.

### Major

- **Math benchmark gains are marginal and the paper's framing overstates them.** The abstract foregrounds the KK result of 31.0% → 40.7% (achieved when training specifically on KK data), but the math benchmark results in Table 1 (trained on OpenThoughts3) show gains of only +1.4 to +2.9 percentage points for gemma-3-4b-it and +0.4 to +2.5 pp for Qwen2.5-7B-Instruct. The paper claims SimpleGV "consistently improves over base models" (line 104), but gemma-3-4b-it on GSM8K drops from 89.2% to 89.0% and Qwen2.5-7B-Instruct on KK drops from 18.1% to 17.6%. While these regressions are within the reported standard deviations, the claim of consistent improvement is not strictly supported. More importantly, the abstract's statement that "similar improvements are observed across diverse mathematical reasoning benchmarks" (line 31) is misleading given the magnitude discrepancy between the KK-specific training gains (+9.7 pp for SimpleGV on gemma-4b) and the OpenThoughts3 math gains (+1–3 pp).

- **RevisionGV is never evaluated on math benchmarks.** Section 4 presents RevisionGV as the more powerful variant and reports consistent gains over SimpleGV on KK, but provides zero results on GSM8K, MATH500, MATHHard, or TabMWP. Given that SimpleGV's gains on these benchmarks are already marginal, this omission leaves open whether RevisionGV — the paper's strongest method — actually helps on realistic reasoning tasks or only on the synthetic KK benchmark.

- **Baseline comparison in Table 1 is confounded by different training data and compute.** SimpleGV is compared against released models from INUITOR, AZR, and GRPO, each trained on their own data with their own compute budgets. SimpleGV uses 20K OpenThoughts3 samples; the baselines use different (unspecified in this paper) data. This makes it impossible to attribute performance differences to the method rather than to data quantity, quality, or compute. The paper does not acknowledge this confounding factor.

### Minor

- **Verifier accuracy is validated only on KK, not on the OpenThoughts3 training data that produces the math benchmark results.** Figure 2 demonstrates verification accuracy improvement on the KK training set, but OpenThoughts3 includes problems that are "not directly verifiable (e.g., proofs and scientific question answering)" (line 92–93). For these problems, thresholded voting filters for consensus rather than correctness, and the paper provides no evidence that the verifier is more accurate than random on this data. This limitation is partly inherent but should be discussed.

- **Default values for key parameters are not stated in the main text.** The number of generator candidates per query (k) and verifier queries per candidate (n) are never specified for the main experimental results presented in Tables 1–3. The cost analysis (Section 3.6) explores n₁ ∈ {4, 8, 16} and n₂ ∈ {4, 8, 16}, but which configuration was used for the primary experiments is not reported. This is a reproducibility gap.

- **The verifier's evaluation target is ambiguous.** It is unclear whether the verifier checks only the final answer or the full reasoning chain. This distinction matters for the claim that the method works on "free-form outputs" (line 104) — if the verifier only checks final answers, the method implicitly requires verifiable final answers, which narrows its applicability.

### Trivial

- Tables 2 and 3 are dense with threshold variations across multiple rows, making the main narrative difficult to extract at a glance. The presentation could benefit from highlighting the best results and simplifying the row structure.

## Nice-to-Haves

- Report RevisionGV results on math benchmarks to validate the claim that RevisionGV is a general-purpose improvement over SimpleGV.
- Validate verifier accuracy on a sample of OpenThoughts3 preference pairs (e.g., via human evaluation or GPT-4-based judgment).
- Add a self-consistency / majority voting at inference baseline (no DPO fine-tuning) to isolate the contribution of the DPO training from simply sampling more at test time.
- Acknowledge the two regressions in Table 1 and discuss what task properties predict success or failure of the method.

## Removed Points

These points from the input reviews were considered but removed:

- *"The assumption that verification is more reliable than generation is load-bearing but under-examined"* — The paper explicitly labels this as an implicit assumption (line 98) and provides supporting evidence on KK (Figure 2, verification accuracy ~62% vs. generation 31%). Demanding a systematic cross-task investigation goes beyond what the paper claims to do and reads as a generic area-of-concern sweep rather than a specific identified problem.

- *"Data size saturation suggests fragility"* — The paper already discusses diminishing returns and regression at 40K samples honestly (lines 157–159). It presents this as a finding, not a hidden flaw. The criticism reflects the reviewer's interpretation, not a paper problem.

- *"Using instruction-tuned models undermines the 'without external supervision' framing"* — The paper explicitly states "we employ instruction-tuned variants rather than raw base models" (line 79). The self-evolution claim is about the post-training process, not the base model's origin. This is transparently reported.

- *"Missing related work differentiation"* — This is a reviewer knowledge-gap issue; we cannot verify missing related works and the paper's related work section is adequate for its scope.

- *"No theoretical analysis of self-evolution dynamics"* — The paper is empirical and does not claim theoretical contributions. This is out of scope.

- *"Compute time analysis not provided"* — The cost analysis in Section 3.6 / Figure 5 provides n₁ × n₂ trade-offs. This is sufficient for a methods paper.

- *"The paper never specifies whether the verifier evaluates the final answer or the full reasoning trace"* — This was actually retained as a Minor weakness; it is a valid concern but was stated too strongly in the input.

## Novel Insights

The paper's most novel empirical finding is the co-evolution phenomenon (Figure 2): self-training on thresholded majority-voted preference pairs not only improves generation accuracy but simultaneously improves the model's verification accuracy, creating a virtuous cycle. This is a concrete, measurable phenomenon that goes beyond the expected "better data → better model" narrative. The easy-to-hard generalization result (Table 3), while not entirely surprising, is demonstrated with a clean experimental design that convincingly rules out memorization. The finding that RevisionGV outperforms SimpleGV only for models above a capability threshold (1B fails, 4B+ succeeds) is also a practically useful insight about when multi-turn self-correction is beneficial.

## Suggestions

- Clarify in the main text what k and n values were used for the primary experiments in Tables 1–3.
- Specify whether the verifier evaluates the final answer only, the reasoning chain, or both, and discuss how this affects the generality claim.
- Add a brief discussion of the two regression cases in Table 1 to strengthen credibility.
- Consider restructuring Tables 2–3 to highlight the best-performing configuration more prominently.

## Score and Decision

**Anchor comparison across all rounds:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| pTyEnkuSQ0 (LLM Self-Correction) | 2.40 (rejected, high variance) | R1 | Our paper is substantially stronger in method and experiments |
| RZZPnAaw6Z (Self-Rationalization) | 5.00 (rejected) | R2 | Our paper has more novelty, better experiments, stronger gains |
| O0sQ9CPzai (TPO) | 6.33 (accepted) | R2 | Comparable quality, TPO has more technical novelty but narrower evaluation |
| RFqeoVfLHa (Self-Improvement Reversal) | 6.50 (accepted) | R1/R2 | Similar quality; Reversal paper has stronger analysis, our paper proposes a method |
| WJaUkwci9o (Sharpening Mechanism) | 8.00 (accepted) | R1 | Significantly stronger; theoretical framework with clean formalism |

**Round-1 bracket:** 5.0–6.5. **Round-2 narrowing:** The paper is clearly above the 5.00 anchor (Self-Rationalization, rejected for limited novelty and marginal gains) but below the 6.33/6.50 anchors (TPO and Self-Improvement Reversal, both accepted with substantive contributions). The marginal math benchmark gains and framing issues place it at the lower end of the 5.0–6.5 bracket.

The core idea — using a single model as both generator and verifier with thresholded majority voting to bootstrap self-evolution — is clean and well-motivated. The KK results, co-evolution finding, and easy-to-hard generalization are genuine contributions. However, the paper's central claim of a general self-evolution method is undermined by marginal and inconsistent gains on standard math benchmarks, the absence of RevisionGV evaluation on those benchmarks, and framing that does not match the evidence. These issues are addressable but collectively prevent a clear accept recommendation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>