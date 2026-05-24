## Summary

ARENABENCHER proposes a model-agnostic framework for automatic benchmark evolution that extracts the core ability of each test case, generates candidate variants with an LLM, verifies them, and selects candidates that consistently degrade performance across a sampled pool of multiple models. The framework is evaluated on GSM8K (math), CommonsenseQA (commonsense reasoning), and AdvBench (safety), and claims to increase difficulty while preserving alignment and fairness.

## Strengths

- **Multi-model feedback produces consistently larger difficulty increases than single-model feedback across all three domains.** Table 1 shows that m=3 sampling yields substantially larger accuracy drops than m=1 for every model on every benchmark (e.g., Llama-3.2-3B drops 47.7% vs. 32.8% on GSM8K, Qwen3-4B-I drops 34.7% vs. 26.2% on CSQA). This directly validates the core design hypothesis that aggregating feedback from multiple models mitigates single-model bias.

- **Honest reporting of failure cases.** Figure 2 presents a concrete failure where the updated test case is unsolvable (missing time constraint), has an incorrect answer, and introduces a new operation (division) not in the original — and the paper explicitly presents this as a limitation of the verifier. This transparency strengthens credibility and gives readers concrete direction for improvement.

- **Well-structured formalization with explicit desiderata.** Section 3.5 defines four quantifiable metrics (Difficulty, Separability, Fairness, Alignment) with precise formulations, and Algorithm 1 provides complete pseudocode. This makes the framework reproducible and claims verifiable.

- **Cross-domain evaluation without task-specific engineering.** The same pipeline is applied to math, commonsense reasoning, and safety without domain-specific tuning, suggesting genuine model-agnosticism and domain generalizability.

## Weaknesses

### Fatal

None.

### Major

- **No comparison to any existing baseline method.** The paper compares only to the original unmodified benchmarks. It does not compare against MATH-Perturb, Automatic Robustness Stress Testing, paraphrasing, or any other augmentation approach discussed in the Related Work section. This makes it impossible to determine whether the multi-model feedback mechanism, the iterative refinement, or the ability extraction step actually contribute value over trivial alternatives. A reader cannot tell if the framework's complexity is justified or if a straightforward paraphrasing pipeline would achieve similar difficulty gains at lower cost. This is a significant omission for a paper proposing a novel framework.

- **Single-model closed loop for generation, verification, and alignment evaluation.** The paper states on line 230: "We use GPT-4o-2024-08-06 for test objective extraction, test case generation, and as the verifier." The alignment metric is also computed by GPT-4o. The same model that generates candidates also verifies their correctness and evaluates whether they preserve the original ability — making the alignment metric a measure of GPT-4o's self-consistency. This is especially problematic given that Figure 2 demonstrates GPT-4o as verifier approving an invalid question with an incorrect answer and misaligned ability. The human evaluation provides an external check on only 100 GSM8K samples, leaving the vast majority of the evolved benchmark across all three domains validated only by the model that produced the items.

- **Separability — a stated core desideratum — degrades in the evolved benchmarks.** Table 2 shows separability dropping from 15.2 to 12.2 on GSM8K and from 8.5 to 7.2 on CSQA under m=3. The paper explains this as "expected as model performance begins to compress under increased difficulty" (line 253). But if a benchmark update reduces the ability to distinguish between models of different capabilities, it is failing at a stated core purpose. The difficulty–separability trade-off is not incidental — it reveals that the selection mechanism's preference for items all models fail on works against discriminative evaluation. The paper defines separability as one of four desiderata, then concedes the method does not satisfy it, yet does not treat this as a substantive limitation.

- **Human evaluation is limited in scope and methodological rigor.** Only 100 samples from GSM8K are evaluated — no human evaluation is conducted for the safety or commonsense domains. The paper reports that 95/100 are aligned and 96/100 are correct, but provides no inter-annotator agreement statistics, no reporting of disagreement cases, and no description of adjudication procedures. Given the Figure 2 failure case (where the same verifier pipeline approved a clearly invalid item), these aggregate numbers are difficult to trust without understanding annotator consensus. For a paper whose key claim is that evolved benchmarks preserve alignment, the human evaluation on one domain with no agreement metrics is insufficient.

### Minor

- **The paper's motivating problem (contamination) and proposed solution (harder items) are only loosely connected.** The abstract and introduction frame the work as solving "widespread data leakage" and "pervasive contamination," but the method never measures whether the evolved benchmarks actually reduce contamination. The paper does not test whether models' improved scores on the original benchmarks were due to memorization, nor does it verify that updated items are absent from training corpora. Harder items are not necessarily uncontaminated items. This is a framing issue rather than a methodological flaw, but it weakens the paper's motivation.

- **The difficulty metric is inconsistent with the multi-model philosophy.** Difficulty is defined as 1 − max_k ACC(M_k, B'), depending only on the single best model (line 147). A benchmark update could achieve high difficulty by confusing only the strongest model while leaving weaker models unaffected. An average-based metric would be more aligned with the framework's collective feedback design.

- **The model pool is narrow (six models, three families, 1B–7B) yet claims generalize to "diverse language models."** All models are from LLaMA, Qwen, and Mistral families, all under 7B parameters. No frontier or proprietary models are included. The claim of broad generalizability is not well-supported by this selection.

- **Safety domain specifics are underdeveloped.** For AdvBench, correctness has very different semantics than in math (there is no ground-truth answer to verify). The paper does not explain how the verifier assesses safety candidate validity or how alignment is evaluated in a domain where the "correct" behavior is refusal rather than a specific answer.

## Nice-to-Haves

- Include at least one baseline from the benchmark augmentation literature (even simple paraphrasing) to demonstrate the framework's components add value.
- Report computational cost of the full pipeline (R=3 iterations, n=5 candidates, m=3 models per evaluation, GPT-4o calls for generation/verification).
- Introduce a difficulty–separability trade-off parameter or alternative selection criterion that does not sacrifice separability for difficulty.
- Use a different model family as verifier than as generator, or add structural validity checks to catch the type of malformed question shown in Figure 2.
- Expand human evaluation to all three domains and report inter-annotator agreement.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **√K sampling heuristic not justified** — The harsh critic questioned the analogy between ensemble feature subsampling and model sampling for evaluation feedback. While the analogy is imperfect, it is a reasonable heuristic choice and the empirical comparison between m=1 and m=3 validates it. Not a substantive weakness.
- **Table 1 presentation confusion** — The harsh critic noted that m=1 and m=3 rows represent different benchmarks, making direct comparison difficult. This is a minor presentation issue, not a methodological one.
- **Missing related works** — Removed per policy (cannot verify external citations).
- **Formatting/style nitpicks** — Removed per policy.
- **Missing appendix, proofs, or references** — Removed per policy (parser artifacts).

## Novel Insights

The paper's own core contribution — using multi-model collective feedback rather than single-model adversarial optimization for benchmark evolution — is genuinely novel in its framing, even if the implementation relies on a single generator/verifier model. The empirical evidence that m=3 feedback consistently produces larger difficulty increases than m=1 across all three domains is the paper's strongest empirical insight. However, the critical observation from this meta-review is that the paper's own failure case (Figure 2) reveals a fundamental tension in the framework: the selection mechanism rewards items that confuse models, but confusion can arise from either genuine difficulty or poor question quality, and the single-model verifier cannot reliably distinguish between these two sources.

## Suggestions

1. **Add a baseline comparison.** Even a simple paraphrasing baseline (e.g., GPT-4o rephrasing questions) would allow readers to assess whether the framework's complexity buys something real.
2. **Decouple the verifier.** Use a different model family (or a structured rule-based checker for math) as the verifier to break the single-model closed loop.
3. **Treat separability degradation as a first-class problem**, not an expected side effect. Consider a selection objective that jointly optimizes difficulty and separability.
4. **Strengthen human evaluation** with inter-annotator agreement (e.g., Cohen's κ), disagreement resolution procedures, and evaluation on all three domains — not just GSM8K.
5. **Directly measure contamination reduction**, e.g., by checking whether the evolved items are absent from training corpora, or by comparing performance gaps between known-contaminated and known-uncontaminated subsets.

## Evaluation

**Originality:** The multi-model feedback aggregation for benchmark evolution is a reasonable and somewhat novel idea, distinguishing this work from single-model adversarial perturbation methods. However, the ability extraction and iterative refinement components are more incremental.

**Importance of research question:** High. Benchmark contamination and staleness are pressing, real problems for the LLM evaluation community.

**Whether claims are well supported:** Partially. The multi-model feedback claim is well-supported by Table 1. The alignment preservation claim is weakly supported by limited human evaluation with no agreement metrics and a known verifier failure mode. The separability claim is contradicted by the paper's own Table 2.

**Soundness of experiments:** Moderate. The within-paper ablation (m=1 vs. m=3) is well-designed. But the absence of any external baseline, the narrow model pool, and the single-model verification loop limit the experimental soundness.

**Clarity of writing:** Good. The paper is well-organized with clear formalization, algorithm pseudocode, and illustrative figures.

**Value to the research community:** Moderate. The problem is important and the multi-model direction is promising, but the evaluation gaps make it difficult to assess whether the framework outperforms simpler alternatives.

---

**Calibration Report:**

*Round 1 anchors (topic: benchmark evolution/augmentation/evaluation):*
- Low band (avg < 3.5): ZeroSumEval (3.00), Data-Evolution Learning (2.50), MCIL benchmark (3.00) — rejected papers with major methodology gaps
- Mid band (3.5–7.5): Evading Data Contamination (4.25), Benchmark Inflation (4.25), Bench-O-Matic (6.00), AutoBencher (6.25), To the Cutoff... (6.75) — mixed accept/reject, varying evaluation rigor
- High band (> 7.5): MMIE (8.00), BigCodeBench (9.00), Cheating Automatic Benchmarks (7.75) — accepted papers with strong evaluation

*Round 1 bracket:* 4.0–6.0 (ARENABENCHER is better than the weak low-band anchors but has significant evaluation gaps compared to the mid-band anchors)

*Round 2 anchors (5.0–7.0):* Bench-O-Matic (6.00, rejected), AutoBencher (6.25, accepted), Generative Judge (5.33, accepted), ∀uto∃∧L (6.33, accepted)

*Comparison:*
- vs. Bench-O-Matic (6.00, rejected): Similar reliance on LLM-as-Judge, similar lack of external baselines. ARENABENCHER has a more novel multi-model feedback mechanism but weaker human evaluation.
- vs. AutoBencher (6.25, accepted): AutoBencher has novelty metrics, human evaluation via Mechanical Turk, and more diverse experiments. ARENABENCHER has a cleaner formalization but no baseline comparisons and limited human validation.
- vs. Generative Judge (5.33, accepted): Different scope but similarly moderate evaluation.

ARENABENCHER sits slightly below Bench-O-Matic (6.0) and AutoBencher (6.25) due to the complete absence of baseline comparisons and the single-model closed loop, but above the rejected papers in the 4.0–4.5 range due to its clearer methodology and consistent empirical evidence for the multi-model feedback contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>