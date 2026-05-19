- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have a thorough understanding of the paper and can verify the reviewers' claims against the actual text. Let me produce the consolidated review.

---

## Summary

This paper develops a transfer-learning framework for weak-to-strong generalization, modeling the source model as a mixture of latent concept components and the target as a single component within that convex hull. It proves that naive fine-tuning on weak labels suffers fundamental limitations (Proposition 3.2) and that an in-context-learning (ICL) refinement procedure provably overcomes these (Theorem 4.2), with a finite-sample excess risk bound decaying exponentially in the number of ICL examples. Experiments on persona transfer, mathematical reasoning, and explanation-style tasks show that ICL refinement preserves the strong model's content accuracy while acquiring the target behavior, unlike naive fine-tuning.

## Strengths

1. **Formal transfer-learning formulation with explicit structure.** Section 2 provides a rigorous mathematical framework—a latent-concept mixture model with orthonormal regression vectors, explicit source/target distributions, and two concrete forms of weakness (biased and noisy). This formalization is missing from prior empirical work and enables clean theoretical analysis.

2. **Finite-sample guarantee for ICL refinement (Theorem 4.2).** The theorem proves an excess risk bound for the refinement estimator that decays exponentially in the number of ICL examples, with the decay rate controlled by the weak supervisor's quality. This is a nontrivial theoretical result showing that refinement can provably overcome the impossibility result for naive fine-tuning (Proposition 3.2).

3. **Consistent empirical patterns across multiple tasks.** Figures 1–3 and Table 1 show that across persona, math, and explanation tasks, different weak teachers (Llama-2, Mistral, Gemma, Falcon), and two strong models (GPT-3.5-Turbo, GPT-4o-mini), the ICL refinement method consistently yields content scores near the unaltered strong model, while naive fine-tuning degrades content substantially (e.g., content scores dropping from ~7–8 to ~3–5 on TruthfulQA for several weak teachers).

4. **Identifies a key evaluation oversight in prior work.** Section 6 correctly argues that weak-to-strong generalization should be measured against the original unaltered strong model, not just against the weak teacher. The paper shows that the original Burns et al. evaluation missed this benchmark, which reframes the evaluation standard for the field.

## Weaknesses

### Fatal
None.

### Major

1. **No variance estimates in experimental results.** All figures (1–4) and Table 1 report point estimates without error bars, confidence intervals, or any measure of variability. The benchmarks are small (100 examples each for tinyAlpacaEval and tinyTruthfulQA), evaluation uses GPT-4o with temperature sampling, and the ICL refinement involves selecting specific ICL examples. Without reporting variance across different random seeds, ICL subsets, or fine-tuning initializations, the reader cannot assess whether observed differences (e.g., a 0.5–1 point content score gap between ICL refinement and the baseline) are reliable or within noise. While the qualitative trends are large and consistent enough to be convincing, the paper's quantitative claims lack proper evidential support. *Note: the paper does average 10 GPT-4o evaluation samples per example, but this addresses only evaluation stochasticity, not variability in the experimental setup itself.*

### Minor

1. **Abstract overclaims the scope of the proof.** The abstract states: "We prove that weak-to-strong generalization is possible by eliciting latent knowledge from pre-trained LLMs." The proof (Theorem 4.2) is valid but depends on a linear mixture model with orthonormal components and the strong Assumption 1 (iid ICL examples treated as Bayesian inference). The paper acknowledges the assumption is "admittedly strong" (line 215), but the abstract presents the result without caveats, making it sound like a proof for real LLMs rather than a proof within a stylized framework. This is fixable with more precise language (e.g., "prove within our framework" or "show under stated assumptions").

2. **No direct comparison with the most closely related concurrent refinement method.** The paper cites Yang et al. (2024) as developing "a methodology similar to our refinement method" and uses their math datasets, but does not compare ICL refinement against Yang et al.'s method directly. Given that both papers propose refinement-based approaches, a head-to-head comparison (or at least a discussion of why it is not feasible) would substantially strengthen the empirical evaluation. The existing baselines (bootstrapping, auxiliary loss) are from the original weak-to-strong paper, which predates the refinement approach.

### Trivial
None.

## Nice-to-Haves

- **Empirical probe of the latent concept assumption.** The paper could strengthen the theory-to-experiment connection by checking whether the strong model's internal representations support separable concept vectors (e.g., via linear probing on the persona task) or whether perplexity on weak labels correlates with concept separability.
- **Discussion of the convex hull assumption's limitations.** The target behavior might only approximately lie in the convex hull of source concepts; a brief discussion of how robust the method is to violations would be useful.
- **API cost comparison.** The ICL refinement method requires multiple LLM calls per training example. A brief comparison of API cost with naive fine-tuning would be informative, especially for practitioners.

## Removed Points

These points from the input reviews are removed with brief justifications:

- *"Strong and untested assumptions (Assumption 1) — not validated empirically"*: The paper explicitly acknowledges Assumption 1 is "admittedly strong" (line 215) and cites prior work (Wang et al. 2024, Pathak et al. 2024) that motivates it. Every theoretical result requires assumptions; the paper is transparent about this one. Heightened to a concern rather than a concrete weakness.
- *"Missing hyperparameters (learning rate, number of epochs)"*: These are trivial implementation details. Removed per the nitpick rule.
- *"Statistical dimension feels out of place"*: Subjective stylistic observation, not a substantive weakness.
- *"Should validate that perplexity correlates with concept separability"*: Speculative nice-to-have, not a weakness.
- *"Cost/API usage not discussed"*: Moved to Nice-to-Haves.
- *"Limited baseline comparison"* (wrapped as a sweep): Merged into the specific point about Yang et al. (2024) only; the paper does adequately compare against bootstrapping and auxiliary loss.
- *Strength Finder's generic/superficial strengths*: None identified—all five listed strengths are specific and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions. Both reviews surface well-known patterns from the paper (formal framework, exponential decay bound, consistent experimental trends) without offering genuinely novel observations about the work.

## Suggestions

1. **Add error bars** to all figures (Figures 1–4). Run each condition with at least 3 different random seeds (varying ICL example selection and fine-tuning initialization) and report mean ± std. This is the single highest-leverage improvement.
2. **Revise the abstract** to qualify the scope of the proof (e.g., "Within our framework, we prove..." or "Under standard modeling assumptions, we prove...").
3. **Add a comparison or discussion** of Yang et al. (2024)'s method. If a direct comparison is not feasible, state clearly what differs and why.
4. **Specify n_ICL** (the number of ICL examples used) and the selection strategy for ICL examples in the experimental section.
