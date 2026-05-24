Now let me compose the final review.

---

## Summary

ARENABENCHER proposes a framework for automatically evolving static LLM benchmarks by (1) extracting the core ability tested by each original item, (2) generating candidate rewrites, (3) verifying correctness via LLM judge, and (4) selecting candidates that maximize loss across a multi-model subset. Top candidates are recycled as in-context demonstrations for iterative refinement. Experiments on GSM8K, CommonsenseQA, and a safety benchmark with 6 models (Llama, Qwen, Mistral families) show large accuracy drops and increased attack success rates post-evolution, with human evaluation on 100 GSM8K samples confirming 95% alignment and 96% correctness. The multi-model (m=3) configuration consistently outperforms single-model (m=1) feedback.

## Strengths

- **Multi-model feedback demonstrably outperforms single-model selection.** Table 1 shows that across all model families and tasks, the m=3 configuration (aggregating ⌈√K⌉ models) yields consistently larger accuracy drops and ASR increases than m=1 (e.g., Llama-3.2-3B on GSM8K: 47.7% drop vs. 32.8% drop). Table 2 confirms m=3 achieves higher difficulty while maintaining comparable fairness and alignment. This directly supports the paper's core claim that multi-model feedback reduces overfitting to individual model biases.

- **Human evaluation provides independent validation of alignment and correctness.** Section 4.2 reports 95% alignment with original intent and 96% correctness on 100 randomly sampled GSM8K updates judged by three expert annotators. This is non-trivial, independent evidence that the evolution process preserves semantic fidelity.

- **The framework generalizes across three distinct evaluation domains without domain-specific tuning.** Table 1 shows consistent performance degradation on mathematical reasoning (GSM8K), safety (Harmful Behaviors), and commonsense reasoning (CSQA) for models from Llama, Qwen, and Mistral families, demonstrating that the ability-extraction and multi-model selection mechanisms transfer across task formats.

- **Well-defined desiderata and metrics.** The paper formalizes four evaluation criteria (difficulty, separability, fairness, alignment) with clear mathematical definitions (§3.5), providing a reusable framework for evaluating benchmark quality that goes beyond ad-hoc metrics.

## Weaknesses

### Fatal

None.

### Major

- **No comparison to existing benchmark-evolution methods.** The paper only ablates m=1 vs. m=3 within its own framework and compares against the original static benchmark. It does not evaluate against any published alternative such as simple paraphrasing, MATH-Perturb-style perturbations (Huang et al., 2025, cited in the paper), or the single-model adversarial approaches the paper itself contrasts against in the introduction. Without such baselines, it is impossible to judge whether the multi-model feedback mechanism provides advantages over simpler, cheaper approaches. This limits the empirical contribution.

- **Evaluation is confined to the same model pool used for candidate scoring.** All 6 evaluation models (Llama-3.2-1B/3B/3B-I, Qwen3-4B/4B-I, Mistral-7B-I) are the same pool from which feedback subsets are drawn during candidate selection (§3.3). While near-uniform sampling mitigates per-model overfitting and the observed fairness improvements suggest degradation is not concentrated on over-sampled models, the paper provides no evidence that the evolved benchmarks expose weaknesses that generalize to unseen models from different families or scales. This limits confidence in the claim that the framework produces benchmarks that are "broadly challenging across models" (line 25).

- **Separability decreases in all three domains despite being a stated desideratum.** The paper defines separability as a goal — "the updated test case should induce more variance in model performance" (§1, line 27) — yet Table 2 shows it drops for GSM8K (15.2→12.2), CSQA (8.5→7.2), and Harmful Behaviors (17.1→14.5). The paper dismisses this with one sentence: "this is expected as model performance begins to compress under increased difficulty" (line 252). This tension between the stated goal and actual behavior is real and under-analyzed — if all models converge to uniformly low performance, the benchmark loses its ability to discriminate among systems, which undercuts a core motivation for the framework.

### Minor

- **Human evaluation is limited to GSM8K.** The 100-sample human validation (§4.2) covers only math, leaving alignment and correctness claims for CSQA and safety entirely reliant on the same LLM judge (GPT-4o) that generated the candidates. The paper's own case study (Figure 2) demonstrates a failure case where the judge did not catch an underspecified, misaligned question — precisely the kind of error that could inflate measured difficulty in the other domains.

- **The loss proxy used for candidate scoring is not specified per domain.** Section 3.3 defines ℓ(M_k, x) only generically as "loss of model M_k on input x, or a task-specific proxy such as inverse log-likelihood or refusal confidence." The concrete proxy used for GSM8K, CSQA, and safety is never stated, which impedes reproducibility and makes it unclear whether the same signal drives candidate selection across domains.

- **Benchmark sizes and evaluation splits are not reported.** The paper does not state how many test items were used from GSM8K, CSQA, or Harmful Behaviors, nor how many were updated. This makes it difficult to interpret the magnitude of the reported metrics.

### Trivial

- The √K sampling rule is justified by reference to ensemble heuristics (Breiman, 2001; Chen & Guestrin, 2016) but this justification is somewhat loose for the LLM evaluation context. An empirical sensitivity analysis of m would strengthen the methodology section.

## Nice-to-Haves

- A held-out evaluation on 1–2 models from families not in the feedback pool (e.g., Gemma, Phi) would substantially strengthen the generalizability claim.
- An explicit discussion of the difficulty–separability trade-off, perhaps with per-model before/after accuracy scatter plots, would clarify when the framework is most useful.
- Ablation of the iterative refinement mechanism (R=1 vs R=3) to quantify its contribution to difficulty amplification.

## Removed Points

These points are flagged to be removed, treat them with caution.

1. **"Circular evaluation design undercuts the main claims" (Harsh Critic, point 1)** — Partially removed. The concern about evaluation on the same pool is legitimate and retained as a Major weakness. However, the claim that this is "circular" and "fatal" is overstated: the framework explicitly uses multi-model feedback precisely to avoid overfitting to any single model, and the fairness results show degradation is evenly distributed. The paper's claim that the benchmark is harder *for the evaluated pool* is well-supported; only the extrapolation to unseen models is untested. Demoted from Fatal to Major.

2. **"The use of √K as the sampling size is justified by a vague reference to ensemble heuristics" (Harsh Critic, Section-by-Section)** — The justification is indeed brief and the references (Breiman, 2001 on random forests; Chen & Guestrin, 2016 on XGBoost) are about tree ensembles, not LLM evaluation. However, this is a minor presentation issue, not a methodological flaw — the m=3 choice is empirically validated against m=1. Kept as Trivial only.

3. **"Table 1 mixes base and instruction-tuned models; the large ASR increases on the safety benchmark may partly reflect the poor safety alignment of base models" (Harsh Critic, Section-by-Section)** — Removed. The paper clearly labels instruction-tuned variants with "-I" and both base and instruction-tuned models show substantial ASR increases (e.g., Qwen3-4B-I: 33.4%→44.6%). The ASR increases are not exclusively driven by base models.

4. **Strength Finder "iterative refinement loop" claim** — The Strength Finder notes the iterative refinement is "not ablated," which means this claimed strength is unsupported by empirical evidence. Kept as a nice-to-have suggestion rather than a validated strength.

5. **Harsh Critic demand for "a discussion of the trade-off between difficulty, separability, and fairness" including "scatter plots"** — This is a useful suggestion but framed as a missing requirement rather than a weakness. Moved to Nice-to-Haves.

6. **"The loss function used for scoring candidates is not specified per domain, making the selection process opaque"** — Kept as Minor, but note the harsh critic framed this as a major methodology gap; it is actually a documentation gap since the loss would be standard cross-entropy for GSM8K/CSQA and refusal-based for safety. Still worth specifying.

7. **Strength Finder "framework generalizes to three domains" / "iterative refinement amplifies difficulty"** — The generalization claim is valid and retained. The iterative refinement claim is not empirically ablated to isolate its contribution; this is retained as a nice-to-have suggestion rather than a demonstrated strength.

## Novel Insights

The review process highlights an important structural tension in benchmark evolution that the paper itself does not fully grapple with: the inherent conflict between difficulty and separability. As a benchmark becomes harder for all models, performance variance necessarily compresses toward zero, reducing discriminative power. This is not a weakness unique to ARENABENCHER — any difficulty-amplification method will face this — but the paper's framing of separability as an independent desideratum that should *increase* alongside difficulty masks this fundamental trade-off. Future work on benchmark evolution would benefit from explicitly modeling this as a multi-objective problem rather than treating these as independently optimizable dimensions.

## Suggestions

- Add at least one simple baseline comparison (e.g., paraphrasing-only evolution without multi-model feedback, or a single-model adversarial approach from cited work) to contextualize the multi-model advantage beyond the m=1 self-ablation.
- Extend human evaluation to a small sample from CSQA or safety to validate the LLM judge's alignment assessments in non-math domains, or explicitly acknowledge and bound this limitation.
- Specify the concrete loss proxy used per domain in §3.3.
- Report the number of test items per benchmark and the fraction updated.
- Add a paragraph explicitly discussing the difficulty–separability trade-off: under what conditions does ARENABENCHER remain useful for model comparison despite compressed variance?

## Score and Decision

**Calibration anchors used:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Generate-then-Test (Wasm) | adSdHgWGBB | 3.00 | R1 | ARENABENCHER is substantially stronger — novel framework, multi-domain eval, human validation |
| DataSciBench | BltaWJZMeR | 3.20 | R1 | ARENABENCHER is stronger — clearer methodology, better-validated results |
| Benchmark Inflation | rAylWUIKtu | 4.25 | R1 | ARENABENCHER is stronger — broader domains, human evaluation, clearer contribution |
| BIND (Programmatic Eval) | ikqcUzUogm | 4.75 | R2 | ARENABENCHER is moderately stronger — more domains, better metrics, human validation |
| AutoBencher | ymt4crbbXh | 6.25 | R2 | ARENABENCHER is somewhat weaker — AutoBencher has more comprehensive evaluation, MTurk validation, and better-situated contribution. ARENABENCHER's multi-model feedback is novel but empirical support is thinner (no external baselines). |
| LiveCodeBench | chfJJYC3iL | 6.25 | R2 | ARENABENCHER is weaker — LiveCodeBench is a full benchmark release with more comprehensive evaluation |
| LiveBench | sKYHBTAxVa | 7.33 | R1 | ARENABENCHER is clearly weaker — LiveBench is a comprehensive, contamination-free benchmark release with far broader evaluation |

**Round 1 bracket:** Between 4.25 (Benchmark Inflation) and 7.33 (LiveBench), narrowed to approximately 4.5–6.5 after considering topical similarity.

**Round 2 narrowing:** AutoBencher (6.25) is the closest topical match. ARENABENCHER shares AutoBencher's framework-for-automatic-benchmark-construction framing but has a thinner empirical story: no external baselines, evaluation limited to the same pool used for feedback, and only single-domain human validation. The multi-model feedback mechanism is a genuinely novel addition over AutoBencher's approach, but the paper does not demonstrate its advantage over simpler alternatives strongly enough to reach the same score tier. ARENABENCHER is stronger than BIND (4.75) — which suffered from unclear takeaways and narrow scope — but weaker than AutoBencher (6.25).

**Final score: 5.5.** The paper addresses an important problem with a sound core idea, produces promising initial results, and provides a reusable metrics framework. However, the absence of comparisons to existing benchmark-evolution methods, evaluation confined to the feedback pool, and the unresolved separability tension prevent a stronger recommendation. These issues are addressable with additional experiments and analysis in a revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>