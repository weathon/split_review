Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper demonstrates that multi-layer perceptrons (MLPs) and MLP-Mixers can learn in-context on synthetic regression and classification tasks, achieving performance competitive with Transformers under equal compute budgets. It further shows that MLPs outperform Transformers on three relational reasoning tasks from the psychology literature (match-to-sample, sphere oddball, line oddball), with better compute efficiency and out-of-distribution generalization, challenging prior claims about MLPs' inability to reason relationally.

## Strengths

- **Convincing demonstration that MLPs can learn in-context at all.** The IWL-to-ICL transition analysis (Figures 1e/f/j) directly replicates the paradigm from Raventos et al. for Transformer ICL, providing rigorous evidence that MLPs genuinely switch from in-weight to in-context learning as data diversity increases — not merely memorizing.

- **Nuanced architectural comparison identifying context-length failure modes.** The finding that vanilla MLPs fail at long contexts in regression (Figure 1d) while MLP-Mixers maintain Bayes-optimal performance is non-obvious and illuminating, cleanly separating the contribution of structured token-mixing from pure MLP computation.

- **Strong empirical results on relational reasoning tasks.** The systematic outperformance of MLPs over Transformers on MTS, sphere oddball, and line oddball (Figures 2b,e,i) — with markedly better OOD generalization (Figures 2c,f,j) — is surprising and directly challenges prior theoretical claims that MLPs cannot reason relationally (citing Boix et al.).

- **Compute-matched comparison methodology.** Comparing architectures by total training compute (PFLOPs) rather than parameter count alone, following scaling-law conventions, makes the competitiveness claims more meaningful and fair.

## Weaknesses

### Fatal
None.

### Major

- **The abstract and central framing overclaim competitiveness without acknowledging a critical boundary condition.** The abstract states MLPs "learn in-context competitively with Transformers given the same compute budget," but Figure 1d shows vanilla MLPs completely fail at ICL regression beyond ~64 context exemplars, approaching the zero-estimator baseline. This is not a minor caveat — context scaling is central to the ICL phenomenon. The paper's text does acknowledge this ("One domain in which a vanilla MLP is decisively worse than a Transformer is for long context length"), but the abstract's unqualified claim is misleading. For classification (Figure 1i), context lengths are only tested up to ~64, coinciding with the regression failure threshold, leaving it unclear whether classification MLPs would similarly degrade. This matters because it defines the boundary where the paper's core finding holds, and that boundary is obscured.

- **The relational reasoning tasks (Section 3) are not genuinely in-context learning tasks, yet the paper frames them as such.** In genuine ICL, the task mapping varies between inputs (e.g., β varies in regression, cluster-label mappings vary in classification), and the model must infer the current mapping from context. In MTS, the task is always "find the nearest context point to the query"; in oddball tasks, always "find the outlier." The paper describes these as "functionally a subset of in-context classification" (Section 3) and "closely related to in-context classification" (Abstract), but this stretches the definition: any supervised task involving multiple inputs could be so described. These are fixed-task supervised learning problems with continuous stimuli, not ICL tasks. The relational results are interesting on their own merits but inflating them under the paper's "MLPs Learn In-Context" umbrella misrepresents their actual scope.

### Minor

- **No mechanistic analysis of what MLPs compute to solve ICL tasks.** The paper shows MLPs achieve competitive loss but does not investigate *how*. In Transformer ICL research, mechanistic analyses revealed implementations of ridge regression or gradient descent. Without comparable probing (e.g., whether an MLP's intermediate representations encode an estimated β), we cannot know whether MLPs implement something analogous or a qualitatively different strategy. This limits theoretical understanding and the ability to predict generalization behavior under distributional shifts. The IWL-to-ICL transition shows *that* MLPs switch strategies, not *what* the strategies are.

- **The classification context-length experiment (Figure 1i) does not test beyond the range where regression MLPs already fail.** The maximum context length appears to be ~64, which is exactly where regression MLPs begin catastrophically failing (Figure 1d). Testing classification at longer context lengths would clarify whether the flat performance curve is genuine or merely reflects the tested range.

### Trivial
None.

## Nice-to-Haves

- Mechanistic probing experiments (e.g., linear probes for estimated β in intermediate MLP representations) to reveal what strategy MLPs use for ICL.
- Testing classification at context lengths beyond 64 to determine whether the flat performance curve persists.
- Reformalizing or recharacterizing the relational tasks as fixed-rule relational reasoning rather than "in-context learning," which would make the paper's framing more precise without diminishing the contributions.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"RB MLP comparison is apples-to-oranges."** The harsh critic claimed the RB MLP receives hand-crafted features and thus the comparison is unfair. The paper explicitly presents RB MLP as "a benchmark for gold-standard performance using hand-crafted features" and shows it fails when hand-crafted features are misaligned (line oddball). This is a transparently designed ablation, not a deceptive comparison.

- **"The paper doesn't grapple with Transformers' advantage at lower data diversity contradicting the bitter lesson narrative."** The paper explicitly acknowledges this: "we can certainly imagine that in data-limited scenarios, Transformers and other architectures with stronger inductive bias would dominate. Indeed, we have already observed that Transformers tend to learn in-context with comparatively less data diversity. Examining a data-limited setting represents another important future direction."

- **"The paper challenges Boix et al.'s formal proof without examining whether the formal assumptions are met."** The paper says the results "contrast" the formal proof, which is an accurate empirical statement — their experiments produce results that differ from the theoretical prediction. Whether the proof's assumptions are met is a valid discussion point but the empirical challenge is itself legitimate.

- **Strength finder's claim that the paper "demonstrates MLPs outperform Transformers on relational reasoning tasks with less compute" as the "most important piece of evidence."** This is an overstatement of the relational results, which are on very simple (2D, L=5-6) synthetic tasks and thus of limited scope. The core contribution is broader: the ICL result plus the relational reasoning result.

- **Strength finder's claim that "hand-crafted relational bottlenecks fail when misaligned" is a supporting strength.** While true, this is a minor supporting point rather than a core strength of the paper.

## Novel Insights

The paper makes the surprising empirical finding that MLPs can perform in-context learning at all, challenging the widespread assumption that attention is necessary for ICL. The most interesting insight is the dissociation between vanilla MLPs and MLP-Mixers at long context lengths in regression (Figure 1d), suggesting that the token-mixing architecture in Mixers — not just MLP computation per se — enables long-context ICL. This implies that the critical ingredient may be structured permutation-invariant pooling rather than attention specifically.

## Suggestions

- Qualify the abstract's competitiveness claim with context-length limitations. A simple parenthetical such as "(at shorter context lengths)" would make the claim accurate without diminishing the contribution.
- Consider reframing Section 3 as "relational reasoning" rather than "functionally in-context classification," or explicitly acknowledge the distinction and discuss its implications — this would strengthen the paper's honesty and precision.

## Score and Decision

The paper makes a genuine, surprising contribution: MLPs can learn in-context, and they outperform Transformers on relational reasoning tasks. However, the central "competitiveness" claim is overclaimed in the abstract by omitting the significant context-length limitation, and the relational tasks are conflated with ICL in a way that inflates the scope. Neither weakness is fatal — the core empirical findings are real and interesting — but they meaningfully weaken the paper's framing.

**Originality:** The finding that MLPs can do ICL is novel and contrary to prevailing assumptions. 

**Importance:** Moderate — the result shifts understanding of what architectures can support ICL and challenges prior theoretical claims about MLPs' relational reasoning limitations.

**Claims support:** Partially — the ICL results are supported but the "competitive" framing obscures the context-length failure boundary, and Section 3's tasks are not genuine ICL despite being presented as such.

**Experimental soundness:** Good for ICL regression/classification; the relational experiments are sound but small-scale.

**Clarity:** Generally clear, but the "functionally ICL classification" framing is imprecise.

**Community value:** Opens a worthwhile research direction (ICL without attention) and provides empirical counterpoints to prior theoretical claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>