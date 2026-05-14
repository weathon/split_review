Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper identifies a previously underexplored failure mode in LLM unlearning: the *squeezing effect*, where gradient-ascent-based methods lower the probability of target responses but redistribute probability mass into semantically similar high-likelihood regions, leading to spurious unlearning that standard metrics miss. The authors propose a bootstrapping (BS) framework that uses the model's own high-confidence predictions ("model beliefs") as additional suppression targets, instantiated at the token level (BS-T, penalizing top-k tokens) and sequence level (BS-S, augmenting the forget set with high-confidence completions). Experiments on TOFU, WMDP, and MUSE across multiple model families show consistent improvements over NPO, RMU, and other baselines, with Laaj-based evaluation confirming more thorough forgetting.

## Strengths

- **Novel mechanistic diagnosis of spurious unlearning.** The paper provides a clear, empirically grounded characterization of the squeezing effect (§3.2). Figure 2a demonstrates that high-likelihood regions produce semantically similar outputs, and Figures 2b–c track log-probability dynamics showing NPO persistently retains mass in these regions while GA causes collapse. This directly supports the claim that existing methods yield only superficial forgetting and explains *why* standard metrics misreport success.

- **Principled and compatible solution.** The bootstrapping framework follows naturally from the diagnosed mechanism: since probability mass is squeezed into model-favored regions, suppressing those regions alongside the target directly counters the effect. BS-T and BS-S are compatible with any base unlearning loss (GA, NPO, WGA) and any regularization (GradDiff), making them practical drop-in improvements. The AKG-based theoretical analysis (Thm 5.2, 5.3) provides a readable formalization of how BS-T reshapes gradient residuals and how BS-S aggregates this over sequences.

- **Consistent empirical gains across diverse settings.** On TOFU (Table 1), BS-S achieves the best Agg. score in 8 out of 9 configurations across three model sizes and three forget ratios. On WMDP (Table 2), BS-S reaches near-random forgetting accuracy (Bio 0.26, Cyber 0.27) while preserving higher MMLU (0.54) than most baselines. The Laaj evaluation (Fig 4c) confirms that BS methods produce more natural and less similar outputs than baselines, corroborating the standard metric results with a more trustworthy semantic judgment.

## Weaknesses

### Fatal

None. The core claims are well-supported.

### Major

- **Laaj evaluation is limited to a single setting, weakening the paper's own metric critique.** The paper devotes significant space to arguing that standard metrics (ROUGE, perplexity, truth ratio) misreport unlearning success (§3.1), yet the main results (Tables 1–2) rely on these same metrics—including Truth Ratio as a component of the Memorization score. The Laaj evaluation that the paper positions as more trustworthy is applied only to one model (Llama 3.1 8B) on one forget setting (TOFU 10%, Fig 4c). This creates a tension: the paper's strongest critique of prior work is that we cannot trust surface-level metrics, but its own headline comparisons depend on them. While the Laaj results do corroborate the BS advantage, a broader Laaj evaluation across more configurations would substantially strengthen confidence that the reported gains are not themselves artifacts of the metrics the paper criticizes.

### Minor

- **Modest absolute gains in several settings.** On TOFU 10% with Llama 1B, BS-S improves Agg. from 0.58 (NPO) to 0.61—a ~5% relative gain. On 1% forget settings, BS-S's Agg. of 0.57 vs. NPO's 0.53 and RMU's 0.51 is clearer, but the gap to Retrain (0.61) remains large. These are consistent improvements but not transformative, and the paper would benefit from a discussion of what practical difference these margins make.

- **Theory provides explanatory insight but no non-trivial predictions.** The AKG analysis (Lem. 5.1, Thm. 5.2–5.3) cleanly illustrates why BS-T adds a neighborhood-suppression term to the residual, but it does not yield guarantees (e.g., bounds on how much the squeezing effect is reduced, or conditions under which BS-S strictly dominates BS-T). The theory is better described as a formal interpretive lens than a rigorous justification, and the paper should frame it as such rather than implying it proves superiority.

- **No static paraphrase augmentation baseline.** BS-S augments the forget set with model-generated high-confidence continuations. A natural question is whether simply augmenting with static paraphrases (e.g., generated once from the original model via an external paraphraser) would achieve similar gains without the on-policy sampling overhead. The absence of this ablation makes it harder to attribute BS-S's benefit specifically to the *belief-aligned* bootstrapping dynamic rather than to generic data augmentation.

### Trivial

None.

## Nice-to-Haves

- A token-level semantic analysis showing that the top-k tokens at representative positions are indeed semantically related alternatives (e.g., paraphrases, synonyms) rather than syntactically plausible but neutral continuations. This would directly validate BS-T's mechanism beyond the sequence-level evidence in Figure 2a.

- A computational cost comparison between BS-S with on-policy resampling vs. off-policy (discussed in Appx. D.4 but not quantified empirically), to help practitioners choose between the two modes.

- A broader Laaj evaluation spanning multiple model sizes and forget ratios to fully resolve the tension between the paper's metric critique and its experimental design.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"Evaluation metrics contradict the paper's own critique — the main results are fundamentally compromised."** — OVERSTATED. The paper does critique ROUGE/perplexity/truth ratio, and the TOFU Memorization score includes Truth Ratio as one of four components. However, this is a mild tension, not a fatal contradiction. The paper uses the *field-standard* metrics for fair comparison with baselines and corroborates findings with the more trustworthy Laaj evaluation. The critic's framing that this is "structural" and "cannot be fixed" ignores that (a) the metrics are the established benchmark protocol, (b) beating baselines on these metrics while also demonstrating superiority on Laaj is a valid strategy, and (c) no paper would be expected to replace standard benchmarks entirely.

- **"Token-level bootstrapping may not target semantically related paraphrases — the mechanism is unvalidated."** — OVERSTATED. The paper shows that high-likelihood *sequences* are semantically related (Fig 2a). The logical chain is that the tokens comprising those sequences at each position are the relevant ones to suppress. While a direct token-level semantic study would strengthen the argument, the absence of one does not invalidate the mechanism; it is a nice-to-have analysis, not a missing piece of evidence.

- **"Missing related works"** — REMOVED per instructions.

- **"The appendix-stripped content (Appx. F.5 ablation, Appx. D proofs) is missing"** — REMOVED. The parser strips appendices from all papers; they exist in the original submission.

## Novel Insights

The most genuinely novel observation from this work is the *squeezing effect* as a mechanism for spurious unlearning. While prior work has noted that unlearned models can still produce sensitive content, this paper provides the first systematic characterization showing that probability mass is redistributed specifically into semantically related high-likelihood neighborhoods rather than randomly dispersed. The complementary finding—that NPO sustains this effect more persistently than GA (which eventually collapses)—explains why NPO, widely considered state-of-the-art, is particularly prone to spurious unlearning. This insight has implications beyond the proposed method: it suggests that any unlearning approach relying solely on target suppression without addressing the softmax normalization dynamics will face the same limitation.

## Suggestions

- Explicitly frame the theory section as providing interpretive insight into BS's mechanism, rather than implying it delivers performance guarantees. This will preempt reader expectations of non-trivial bounds.
- Add a static paraphrase augmentation baseline (e.g., using the original model to generate paraphrases once and training on them) to isolate whether BS-S's benefit comes from belief alignment or from generic data augmentation.
- Quantify Laaj evaluation on at least one additional model size and forget ratio to strengthen the paper's own argument that standard metrics can be misleading, and that BS methods genuinely mitigate spurious unlearning.

## Score and Decision

**Calibration against human-reviewed anchors:**

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| Learning-Time Encoding Shapes Unlearning in LLMs | BcjZCertEk | 4.67 (Accept Poster) | Both identify novel aspects of the unlearning process. Current paper provides both diagnosis AND a method with consistent empirical gains, making a more complete contribution. |
| Downgrade to Upgrade | Sswng2ToR4 | 4.50 (Accept Poster) | Similar in providing a new perspective on unlearning. Current paper has broader empirical validation (3 benchmarks vs. 2) and a more clearly characterized mechanism (squeezing effect vs. optimizer grade as a proxy). |
| Label Smoothing Improves GA | qd9fA4LzVN | 4.50 (Reject) | Both propose simple modifications to existing unlearning losses. Current paper has stronger mechanistic grounding and more consistent gains across model scales. |
| On the Impossibility of Retrain Equivalence | r6Z3BXDrzO | 4.50 (Reject) | Different type of contribution (theory vs. empirical). Current paper's empirical breadth and practical method give it more immediate value. |
| Leak@k | rzi77zNngG | 4.00 (Reject) | Both identify evaluation failures in unlearning. Current paper goes further by providing a mechanism and solution, not just a diagnostic metric. |
| Unlearning Isn't Deletion | 7cEMkTu7Lf | 4.00 (Reject) | Both show unlearning is often superficial. Current paper's bootstrapping method is a constructive response to the problem it diagnoses. |
| LLM Unlearning Under the Microscope | nxMR2NGFik | 3.50 (Reject) | Taxonomy paper with limited novelty. Current paper has a clear technical contribution beyond systematization. |
| Exclusive Unlearning | XZhDjhVwma | 3.50 (Reject) | Interesting but overclaimed. Current paper's claims are better scoped and supported. |
| BLUR | odMc2ZRGcw | 2.50 (Reject) | Benchmark-only contribution. Current paper provides both diagnosis and remedy. |

The current paper's strengths—a well-characterized novel mechanism, a principled method that consistently beats strong baselines, and validation across multiple benchmarks and model scales—place it clearly above the 4.5-level anchors. The major weakness (limited Laaj evaluation creating tension with the metric critique) is real but addressable in rebuttal and does not threaten the core claims. The theory is explanatory rather than predictive, but this is comparable to most accepted papers in this space (e.g., "Downgrade to Upgrade" at 4.50 was accepted with similar theoretical depth). The paper makes a genuine contribution: it diagnoses why unlearning fails, proposes a clean fix, and demonstrates it works.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>