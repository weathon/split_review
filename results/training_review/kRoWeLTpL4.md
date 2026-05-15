Now I have a thorough understanding of the paper. Let me synthesize my final review.

## Summary

This paper proposes CP-Fuse, an inference-time model fusion method for copyright protection. Given two language models trained on disjoint copyrighted datasets, CP-Fuse adaptively weights their logits at each decoding step by solving a minimax optimization problem that balances the likelihood of the generated sequence under both models. The method is motivated by a theoretical "balancing property" (Lemma 1) and is evaluated on overfitted models across text (WritingPrompts, MathAbstracts) and code (Python instructions, APPS) tasks, showing a 25× reduction in exact matching length while preserving downstream utility.

## Strengths

- **Novel adaptive fusion mechanism with theoretical grounding**: CP-Fuse derives log-linear fusion weights from a convex minimax optimization problem (Lemma 1). The balancing property (Lemma 2) provides a principled rationale for why adaptively weighting prevents either model from dominating generation — unlike the fixed-weight token-wise cp-δ, which the paper shows can heavily favor one model and reproduce long memorized sequences. This is a genuine advance over prior fusion approaches that lack copyright-specific objectives.

- **Consistent and large empirical improvements**: CP-Fuse achieves the best copyright metric scores on every dataset and split in Table 1, without exception. Exact matching (EM) drops from ~1400–1500 (overfit models) to 55–70 (CP-Fuse) — a >25× reduction. It also consistently beats MemFree (typically 2–3× higher EM), cp-δ (4–7× higher EM), and system-prompt baselines. The JPlag plagiarism score drops to near-zero (0.03) for CP-Fuse while all baselines score 0.96–1.00.

- **Utility is preserved**: CP-Fuse maintains pass@1 scores on APPS (0.47 vs. 0.43 for overfit), MBPP (0.43 vs. 0.44), and HumanEval (0.28 vs. 0.29), and fluency on WritingPrompts is identical (2.17 vs. 2.17). The paper provides concrete examples (Figure 4) showing MemFree introduces syntax/logic errors while CP-Fuse produces correct code, illustrating how fusion avoids the hallucination problems of filtering-based methods.

- **Composable with training-time methods**: CP-Fuse further reduces memorization when applied on top of goldfish-loss-trained models (EM from 84.68 → 20.68 on WritingPrompts Split 1), demonstrating versatility beyond the primary setting.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation limited to an overfitting-only scenario.** The paper fine-tunes models to the point of near-complete memorization on 3,000-sample splits, where every training example is treated as copyrighted. This is a deliberately worst-case setting, but the paper's claims of practical relevance (lawsuit motivation in the introduction) are only partially supported by this setup. While the paper acknowledges this limitation in the conclusion, it also calls the experiments "real-world" (Section 4 intro, Related Work), which overstates the connection. Realistic memorization in pre-trained LLMs is sparse and requires specific extraction techniques — the paper does not demonstrate that CP-Fuse protects against copyright infringement starting from a normally trained base model (e.g., a public checkpoint with incidental memorization). This gap weakens the paper's central practical claims.

2. **No statistical significance or variance reporting.** All results appear to come from single fine-tuning runs with single evaluation seeds. The utility differences are small (e.g., APPS pass@1: 0.47 CP-Fuse vs. 0.43 Overfit, 0.45 cp-δ) and could easily be within noise without error bars. The copyright metrics similarly lack confidence intervals or multi-run statistics. For a paper making strong comparative claims, this is a notable methodological gap.

3. **Narrow robustness evaluation.** The only attack tested is prefix prompting with increasing prefix length. This is a relatively weak extraction method. Stronger attacks standard in the memorization literature (e.g., high-temperature sampling, repeated prompting with variations, adversarial suffix attacks, divergence-based attacks) are not considered. The paper's conclusion that CP-Fuse is "robust" is overbroad based on this single attack vector.

### Minor

1. **Cross-split memorization is not verified.** The method's justification relies on the separability assumption: each base model only memorizes content from its own training split, and the splits are distinct. However, the paper does not empirically test whether the model trained on Split 1 can reproduce content from Split 2. Table 1 shows that Overfit Split 1 evaluated on Split 2 data still yields non-trivial EM values (e.g., 44.60 for Python instructions), suggesting some cross-split leakage. Without validating this assumption, the theoretical argument that CP-Fuse prevents regurgitation via the balancing property remains conditional on an unverified premise.

2. **Connection between the balancing property and copyright protection is heuristic.** Even if log-probabilities under both models are balanced, the generated sequence could still be infringing if both models assign high probability to a copyrighted passage (e.g., common code idioms, clichéd story elements, phrases that appear in both splits). The paper invokes the separability assumption to argue this cannot happen, but this is an indirect defense. A more direct analysis of when the balancing property implies protection — and when it does not — would be valuable.

3. **Utility evaluation relies on a single automated judge.** The fluency metric for WritingPrompts uses Prometheus-v2; no human evaluation is provided. While model-based fluency judges have been validated, this is a single point of evidence. Additionally, no comparison to the original pre-fine-tuned model's utility is reported, making it unclear whether CP-Fuse recovers, degrades, or improves upon the base model's capabilities.

4. **The 73-character longest exact match for CP-Fuse on MathAbstracts is non-trivial.** The paper correctly notes that this is below the 160-character legal threshold, but does not discuss whether shorter exact matches could still be legally problematic for highly distinctive content. Some transparency about the count and nature of such cases would strengthen the presentation.

### Trivial

1. The 95th percentile averaging is non-standard; reporting full distributions or multiple percentiles (50th, 90th, 95th, 99th) would give a more complete picture.
2. No compute cost/overhead comparison with baselines is reported, making it difficult to assess practical deployment trade-offs.

## Nice-to-Haves

- A comparison with DExperts-style methods (using a "copyright-averse" negative expert) would strengthen the baseline coverage, though DExperts is a general fusion method not designed for copyright protection, so its absence is not a critical omission.
- Experiments on models that are not intentionally overfitted (e.g., standard fine-tuning with early stopping, or a pre-trained model with known memorized content) would substantially strengthen the practical claims.
- A computational overhead analysis (runtime comparison with baselines) would help practitioners assess deployment feasibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Lemma is stated but not proved in the main text (reference to appendix)"** — Removed per hard rules: appendix content is stripped by the parser and exists in the original submission.
- **"DExperts and contrastive decoding are missing baselines"** (presented as a critical gap) — DExperts is a general-purpose model fusion method for style control, not a standard copyright protection baseline. The paper's comparison against cp-Δ (the direct copyright-focused predecessor), MemFree, and self-reminder prompts is appropriate for its scope. A DExperts comparison would be nice-to-have but its absence is not a major weakness.
- **Generic strength: "addressed an important problem" / "interesting question"** in Strength Finder — removed as generic and lacking specific content about this paper.

## Novel Insights

The most interesting finding is that the minimax optimization framework — which seems computationally heavy at first glance — reduces to a simple log-linear combination of the two models' logits with non-negative coefficients that can be obtained via a two-parameter grid search at each decoding step. This is a neat theoretical-to-practical bridge. The paper also makes an intriguing empirical observation: the fixed-weight cp-δ method (which averages logits uniformly without considering history) can still generate long verbatim sequences exceeding legal thresholds, while the adaptive mechanism of CP-Fuse nearly eliminates such cases. This suggests that the *history-conditional* weighting is what drives the improvement, not merely the act of combining models. The failure mode of MemFree for code generation (inserting typos/spaces to avoid exact matches, which breaks syntax) is a useful cautionary data point for the field, and CP-Fuse avoids this pathology because it does not modify individual tokens — it reweights whole distributions.

## Suggestions

1. **Run experiments on a non-overfitted setting.** Fine-tune a model normally (e.g., 1 epoch, standard learning rate) on a small set of copyrighted content (e.g., book chapters from the Pile) and evaluate whether CP-Fuse still reduces memorization from the incidental memorization that occurs in normal training. This would address the core validity concern.

2. **Report variance.** Re-run the full pipeline at least 3 times with different random seeds and report mean ± std for both copyright and utility metrics. This is essential given the small utility differences.

3. **Add stronger attack evaluations.** Test CP-Fuse under higher-temperature sampling, repeated prompting with variations, and adversarial prefix attacks. If the method remains robust, this would be a strong selling point; if not, honestly reporting failure modes is still valuable.

4. **Verify the separability assumption empirically.** Measure whether the model trained on Split 1 can reproduce any long substring from Split 2's data. Report cross-split memorization metrics. This directly validates the core assumption.

5. **Report more distributional information for copyright metrics.** Show EM histograms with multiple percentiles (50th, 90th, 95th, 99th, max) rather than just the 95th percentile average. The current Figure 3 histograms are helpful but only show >40 characters for two methods.

## Score and Decision

The paper presents a genuinely novel method with theoretical grounding and strong empirical results in a controlled setting. The adaptive fusion mechanism, the balancing property, and the consistent >25× reduction in memorization across diverse tasks are real contributions. However, the evaluation's reliance on an overfitting-only setup, the absence of variance reporting, and the narrow robustness evaluation prevent full confidence in the practical claims. The paper would be strengthened substantially by addressing these issues, but the core contribution is solid and the results within the paper's stated scope are convincing.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>