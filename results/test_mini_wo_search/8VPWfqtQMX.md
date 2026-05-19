Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes In-Context Risk Minimization (ICRM), which reframes domain generalization as a next-token prediction problem. During training, the model sees sequences of (x, y) pairs from the same environment and predicts each label auto-regressively, using the unlabeled images seen so far as "context." At test time, unlabeled examples arriving from a novel environment serve as context, allowing the model to condition on environment-specific features — effectively "zooming in" on the environment risk minimizer. The paper provides theoretical formalizations of this behavior and experiments on four benchmarks (FEMNIST, Rotated MNIST, WILDS Camelyon17, Tiny ImageNet-C) showing improvements over ERM, ARM, and TENT.

## Strengths

- **Novel and well-motivated conceptual bridge between DG and ICL** (Sections 3–4): The paper explicitly connects the DG notion of "environment" with the LLM notion of "context," arguing that sequences of unlabeled test examples serve as rich environment descriptions. This framing is clearly articulated in the abstract, introduction, and Figure 1, and offers a principled new direction for DG research that goes beyond coarse domain indices or marginal distribution summaries.

- **Consistent empirical gains across all four benchmarks** (Table 1, lines 374–416): ICRM outperforms ERM, ARM, and TENT on average and worst-case accuracy on FEMNIST (e.g., 87.8% vs. 79.3% at 100 context), Rotated MNIST (96.2% vs. 94.2%), Camelyon17 (90.8% vs. 68.6% at 100 context), and Tiny ImageNet-C (39.2% vs. 31.8% at 25 context). These improvements are sustained across context lengths from 0 to 100 samples.

- **Useful ablation isolating the role of environment labels** (Table 2, lines 438–475): ICRM-Mix (trained on pooled i.i.d. context from all environments) underperforms ICRM on FEMNIST and Rotated MNIST but matches it on Camelyon17 and Tiny ImageNet-C. This decomposition helps characterize when environment-specific context matters — the paper explains this via class-distribution uniformity across domains (line 475).

- **Theoretical formalization of zoom-in behavior** (Section 5, lines 279–317): The paper provides three formal results — Zoom-out (Proposition 1, ICRM without context defaults to ERM), Full iid zoom-in (Theorem 1, convergence to the environment risk minimizer with infinite context), and Partial iid zoom-in (Theorem 2, monotonic improvement with context length). These provide mathematical grounding for the core idea even though assumptions are idealized.

- **Attention visualizations show interpretable behavior** (Figure 2, lines 534–548): The visualizations demonstrate that ICRM selectively attends to context examples sharing visual features (curved arcs, semantic categories) with the query, providing qualitative evidence of the amortization mechanism.

## Weaknesses

### Major

1. **The test-time adaptation mechanism is not cleanly isolated from the training procedure contribution.** ICRM at 0 context already substantially outperforms ERM on Camelyon17 (92.0% vs. 68.6%) and Tiny ImageNet-C (38.3% vs. 31.8%). The paper attributes this to the training regimen producing a better featurizer (line 428–431), but this conflates two sources of gain: the autoregressive training objective (environment-ordered sequences) and test-time context. ERM⁺ (same GPT-2 architecture, standard non-autoregressive training) gets only 50.1% on Camelyon17 — a 42-point gap vs. ICRM at 0 context that comes entirely from the training procedure. Moreover, on Camelyon17, adding more context slightly decreases performance (92.0% → 90.7%), which directly contradicts the zoom-in narrative for this dataset. The paper lacks a critical control: train ICRM with its autoregressive objective, then evaluate with randomized/shuffled context at test time. This would directly measure whether environment-specific context (rather than just the training quality) drives the gains on FEMNIST/Rotated MNIST, and help explain why context does not help on Camelyon17.

2. **Camelyon17 worst-case accuracy is unexplained and the evaluation protocol is unclear.** The paper reports "same as average accuracy" for worst-case on Camelyon17 (Table 1, line 400). In the WILDS benchmark, Camelyon17 is known to have substantial variation across hospitals (typical worst-group gaps of 10–20%). The paper follows DomainBed protocol (line 420), but the ERM baseline of 68.6% is well below what the WILDS protocol would give (~90+%), while ICRM's 92.0% at 0 context approaches that higher number. Without a precise description of the train/test split (how many hospitals, which ones are held out), it is difficult to assess whether the ERM baseline is correctly implemented or whether the comparison is apples-to-apples. The paper's multiple cross-references to an appendix section (`\Cref{sec: experimental setup}`, `\Cref{sec:datasets}`) that was stripped by the parser do not help here.

3. **Limited set of DG baselines.** The paper compares only to ERM, ARM, and TENT. While ARM and TENT are relevant as test-time adaptive methods, many standard DG approaches (IRM, VREx, CORAL, SWAD, MixStyle, Fish) are not included. The paper's claim that "no proposal convincingly outperforms ERM" (lines 6, 34, 185) is a claim about the broader DG literature that its own experiments do not test — no method from the invariance category is evaluated. The absence of these comparisons narrows the context for the claimed improvements.

### Minor

1. **Standard errors not displayed in tables.** The paper states it averages over three runs with standard error (line 424–425), but no error bars or confidence intervals appear in any table. For a result where many gains are modest (~1–9% improvement depending on dataset and context length), it is hard to assess statistical significance without variance estimates.

2. **Test-time context provides minimal or negative benefit on 2 of 4 datasets.** On Tiny ImageNet-C, the gain from 0→25 context is only +0.9%; on Camelyon17, performance decreases by −1.3%. While the paper's overall empirical contribution (ICRM beats baselines at all context lengths) is valid, the claim that the model "zooms-in" via test-time context is only clearly supported on FEMNIST and Rotated MNIST.

3. **Theory-practice gap on the OOD result.** Theorem 3 (OOD zoom-in, lines 315–317) proves the *existence* of some ICL algorithm achieving Bayes optimal predictions under a Gaussian latent model with identity mapping, rather than proving that the trained ICRM achieves this. While the theorem demonstrates principled possibility, its connection to the actual method and architecture is weak.

4. **Qualitative attention evidence lacks causal verification.** The attention visualizations (Figure 2) are suggestive but not causally linked to performance — the paper does not show that ablating the attended heads or tokens reduces accuracy.

### Trivial

None.

## Nice-to-Haves

- Train ICRM with its autoregressive objective, then evaluate with shuffled/randomized context at test time, to directly quantify the value of environment-specific test-time context vs. the training procedure's contribution.
- Report standard deviations or standard errors on all table entries.
- Include additional standard DG baselines (IRM, VREx, CORAL, SWAD) to contextualize the improvements relative to the full DG landscape.
- Clarify the Camelyon17 evaluation protocol (exact train/test split, hospital assignments) and explain why worst-case equals average accuracy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about Camelyon17 ERM baseline of 68.6% being "far below published results (~94%)":** The paper states it follows DomainBed protocols (line 420). DomainBed (Gulrajani & Lopez-Paz, 2021) reports ERM on Camelyon17 at approximately 70–75%, not ~94%. The ~94% figure comes from the WILDS benchmark which uses a different evaluation protocol. The paper's baseline is within the expected DomainBed range, so this criticism is based on a protocol confusion.
- **"Training details are underspecified" (architecture hyperparameters, context length, learning rate schedule):** The paper cross-references `\Cref{sec: experimental setup}` (line 420) for these details — this section was in the original appendix and was stripped by the parser. The original submission likely contained these details.
- **Theory described as "tautological" or "restating the objective":** Proposition 1 is not trivially true by construction — it is a formal statement about the learned function's behavior without context, which depends on the training objective converging correctly. Theorem 1 formalizes a non-trivial convergence result. Calling these tautological is an overly harsh characterization of legitimate mathematical formalization.
- **Toy example criticism (Equation toy, lines 329–339):** The paper explicitly states this is "one simplifying assumption for pedagogic purposes" and "provide[s] ICRM directly with the relevant extended feature space" (line 334) rather than claiming it as evidence for ICL. The critic's complaint is addressed by the paper itself.
- **Missing related works / reproducibility nitpicks about "undisclosed hyperparameters":** Per instructions, external claim about missing references cannot be verified, and implementation details are presumed to be in the stripped appendix.
- **Scoping criticisms about the sequential test assumption being "strong"** without evidence that it is unrealistic for the evaluated benchmarks.
- **Pure formatting/style nitpicks.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a critical control experiment: train ICRM with its autoregressive objective, then evaluate at test time with (a) same-environment context, (b) randomly shuffled context from other environments, and (c) no context. The gap between (a) and (b) measures the specific value of environment-relevant context; the gap between (b) and (c) measures the benefit of having any context (even random) vs. none.
2. Report standard errors in all tables.
3. Expand the baseline suite to include at least one invariance-based DG method (e.g., IRM or CORAL) to substantiate the paper's claim that ICRM advances beyond the ERM ceiling.
4. Clarify the Camelyon17 evaluation protocol: state the exact number of hospitals, which are used for train/val/test, and explain why worst-case equals average accuracy.
5. Add a quantitative analysis of the attention mechanism (e.g., ablation that removes high-attention context tokens and measures accuracy drop) to strengthen the causal interpretation of the attention visualizations.

## Score and Decision

**Originality**: High. The connection between environment (DG) and context (ICL) is genuinely novel and well-argued.

**Importance of research question**: High. Out-of-distribution generalization is a central problem, and the ICL perspective offers a fresh approach.

**Claims supported**: Partially. The empirical evidence that ICRM works well is strong, but the central mechanistic claim about "zooming-in" via test-time context is not cleanly isolated from the training procedure's contribution.

**Soundness of experiments**: Adequate but with gaps. The Camelyon17 protocol needs clarification, standard errors are absent, and the baseline zoo is narrow.

**Clarity of writing**: Good. The paper is well-structured and the conceptual narrative is clear.

**Value to the community**: Moderate to high. The framework opens a new direction and the method performs well empirically. The mechanism concern limits the immediate impact.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>