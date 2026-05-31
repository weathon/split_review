## Summary
The paper presents the **Language Confusion Gate (LCG)**, a lightweight two-layer MLP that plugs into an existing frozen LLM and masks tokens from disallowed language families at each generation step. The core technical contribution is *norm-adjusted self-distillation*: the gate is trained on pseudo-labels derived from the model's own top-k/p predictions after dividing each token's logit by its output embedding norm, exploiting the authors' mechanistic finding that high-resource language tokens systematically carry larger embedding norms and thus enjoy an unfair logit advantage. At inference the gate adds only ~0.4% latency and intervenes sparsely (≈0.35% of tokens), reducing language confusion by an order of magnitude across four model families while preserving task performance.

---

## Strengths

- **Mechanistic motivation is genuinely novel and empirically grounded.** Table 1 shows that CJ and Latin tokens disproportionately occupy the top-5% norm slots (up to 10.74% for CJ in Qwen3-8B vs. 0.14% for Low-Res), and Figure 2 demonstrates that norm-dividing the logits at a concrete confusion point shifts the top-10 predictions from all-Chinese to correct-script tokens. This is a clean and verifiable insight.

- **Comprehensive experimental coverage.** The evaluation spans seven models (Qwen3-8B/30B, Llama3.1-8B, Gemma3-12B, GPT-OSS, and thinking variants), three independent benchmarks (FLORES+, INCLUDE, HumanEval-XL), four baselines (greedy, ICL, ORPO, ablation of intervention rules), and both confusion reduction and task preservation metrics. Results are consistent across this diverse setup.

- **Thoughtful treatment of code-switching.** Rather than naively eliminating all language mixing, the paper constructs a FLORES-WITH-LATIN partition and measures legitimate code-switch preservation. The token-level finding that LCG-adjusted allows English tokens at 86.7% of human-validated code-switch points is a concrete and compelling metric.

- **Practical efficiency.** The 0.4% latency overhead and compatibility with speculative decoding (discussed in the appendix) make the method ready for production use, a meaningful advantage over fine-tuning approaches like ORPO.

- **Ablation of intervention rules.** The "No Rule" condition in Figure 3 isolates the contribution of the heuristic rules from the learned gate, confirming that both components contribute independently.

---

## Weaknesses

### Fatal
None.

### Major

1. **Latin confusion is only partially resolved, with no mechanistic explanation.** After LCG-adjusted, CJ confusion is brought near zero on most models (0.0–0.4%), but Latin confusion remains at 2.9% for Llama3.1-8B and 2.0% for Qwen3-8B. Since the paper's central claim is an "order-of-magnitude" reduction, a 3–4× reduction in Latin confusion is noticeably weaker. The asymmetry is unexplained: if the norm bias contributes to Latin confusion just as much as to CJ confusion (Table 1 shows similar imbalance), why is Latin harder to suppress? The paper would benefit from analysis of remaining Latin confusion failures.

2. **Potential over-suppression of legitimate code-switching.** Table 5 shows that after LCG-adjusted, Qwen3-8B's code-switch rate falls from 46.34% to 25.90%, which is *lower* than the ground-truth answer rate (38.36%) and comparable to Claude Sonnet 4 (23.29%). The paper frames this favorably by comparing to the Claude baseline, but the 38.36% ground-truth rate is a more principled reference: post-intervention rates that drop well below ground truth indicate that the gate is over-suppressing legitimate behavior. The 86.7% token-level preservation is encouraging but measures only the cases where the no-LCG model happened to produce natural code-switching—it does not capture cases where LCG preventively blocks a valid switch.

3. **Fundamental within-script limitation understated.** The limitation that LCG cannot distinguish confusion between languages sharing a script (e.g., English vs. Spanish in Latin output; Mandarin vs. Japanese within CJ) is acknowledged in the conclusion but not quantified. For European multilingual settings—arguably the most common deployment scenario—Latin-script within-script confusion is likely the dominant failure mode, yet the benchmark selection (Arabic, Hebrew, Korean, Thai, Chinese as target languages) largely sidesteps this case. The scope of applicability is thus narrower than the general framing suggests.

### Minor

1. **Intervention rule #1 ("never mask Low-Res tokens") interacts ambiguously with target-language identity.** The rationale given is that high-resource languages rarely mix with low-resource ones. However, when the *target* language is itself a low-resource language, the gate must correctly predict "Low-Res allowed" while still suppressing erroneous CJ or Latin tokens—which is what the gate is supposed to do, but the rule as stated implies unconditional Low-Res permissiveness. The actual behavior in production deserves a cleaner description.

2. **BLEU as the sole translation quality metric is coarse.** BLEU differences of ±0.1–0.2 points are within noise for the sentence-level evaluation. Using chrF or COMET would provide more reliable evidence that task quality is preserved.

3. **Human annotation details are thin.** The code-switch experiment credits "human annotators" for validating natural code-switch examples but provides no details on annotator count, agreement, or guidelines.

### Trivial
None beyond parser damage noted in the setup.

---

## Nice-to-Haves
- A failure-mode analysis: when does LCG mask a token incorrectly, and when does it fail to catch a confusion event?
- Evaluation on a Latin-script target language (e.g., Turkish or Vietnamese) to quantify the within-script blind spot.
- A more sensitive generation quality metric (COMET, GPT-based eval) to confirm the "no degradation" claim more rigorously.

---

## Novel Insights
The most genuinely novel contribution is the output-embedding-norm bias analysis. Decomposing the dot-product logit into norm × cosine-similarity and empirically showing that high-resource tokens exploit the norm component to inflate their logits—even when the hidden state's direction does not point toward them—is a clean mechanistic observation. This explains a *structural* source of language confusion that is independent of training data distribution and architecture choices, and it motivates norm-adjusted self-distillation as a principled debiasing technique rather than an ad hoc heuristic. The paper also makes the useful empirical observation that correct-language tokens appear in the top-3 candidates at 99.29% of confusion points, directly justifying a masking intervention over reranking or retraining.

---

## Suggestions
- Separate the Latin confusion analysis into within-script and cross-script components to better characterize remaining failure cases.
- Include at least one Latin-script target language in the benchmark to test the within-script boundary.
- Clarify the interaction between intervention rule #1 and gate behavior when the intended language is Low-Res, with an example walkthrough.
- Report code-switch rate relative to the ground-truth answer rate as the primary baseline (instead of Claude Sonnet 4) for a more principled assessment.

---

## Score and Decision

The paper addresses a real and practical problem, delivers a mechanistically motivated and empirically validated solution, and evaluates it comprehensively across diverse models and tasks. The core insight about norm imbalance is novel and leads to a concrete algorithmic improvement (LCG-adjusted outperforms LCG-unadjusted consistently). The main limitations—within-script blind spot, incomplete Latin confusion resolution, and marginal over-suppression of code-switching—are real but do not invalidate the primary claims. The method is lightweight, non-destructive to the base model, and ready for practical deployment.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>