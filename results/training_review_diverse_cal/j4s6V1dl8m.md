Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper studies whether training LLMs (provers) to produce chain-of-thought solutions verifiable by *smaller* LLM verifiers — through an iterative adversarial training process inspired by the Prover-Verifier Game — makes those solutions more *legible* (easier to evaluate for correctness) to humans. On grade-school math problems, the authors find that directly optimizing for correctness via RL reduces human judges' accuracy, while their checkability training produces solutions that retain legibility (matching the initialization) while substantially improving accuracy over the untrained baseline, albeit at a cost relative to the correctness-only prover (the "legibility tax").

## Strengths

1. **Novel framing and concrete operationalization of legibility.** The paper defines legibility through completeness and soundness with respect to a verifier, providing a crisp formalism that connects to interactive proofs and Stackelberg games. This is a useful conceptual contribution that moves beyond vague appeals to "interpretability."

2. **Demonstrates that correctness-only RL can degrade human legibility.** Figure 2 (Fig.~\ref{fig:correctness-only}) provides clear human evaluation evidence that a prover optimized purely for answer correctness produces solutions that time-constrained humans find harder to evaluate — a finding with practical implications for deploying RL-tuned LLMs.

3. **Multi-faceted evaluation of verifier robustness.** The paper evaluates verifiers under multiple attack types (SRC, CGC, goodharting) and across multiple verifier sizes, showing increasing robustness over rounds of training. The balanced best-of-$n$ analysis (Fig.~\ref{fig:offline_eval}b) cleverly controls for pass rate differences.

4. **Ablation of reward designs.** The systematic comparison of SRC, CGC, and goodharting rewards reveals which design choices yield stable training dynamics, and the finding that goodharting training does not improve human legibility (Sec.~\ref{sec:goodharting}) is an informative negative result that strengthens the paper's central thesis about role-conditioned training.

## Weaknesses

### Major

1. **Human evaluation — the paper's central claim — lacks statistical rigor.** The headline finding that legibility to small verifiers transfers to humans rests entirely on human evaluation data (Figs. 4b/5b, 5b–c/6b, 6b–c/7b–c), yet this data is presented as bare means without confidence intervals, standard errors, sample sizes, or any statistical test. The paper does not describe: (a) how many contractors participated, (b) how many judgments were collected per condition, (c) whether each solution was judged by one or multiple contractors, (d) inter-annotator agreement, (e) what screening (if any) was used for math ability, or (f) how the 45-second time limit was enforced (programmatically or via instruction). The observed effects in the helpful-prover evaluation (Fig.~\ref{fig:v5g-human-data}b) appear modest — trends across rounds that could be driven by random variation in which problems or contractors were sampled. This is the paper's central claim, and the evidence as presented does not meet the standard needed to support it. *Why it matters:* Without statistical support and protocol transparency, the reader cannot assess whether the observed human trends are reliable or within measurement noise. The paper's most interesting result is unsubstantiated.

### Minor

2. **Accuracy-controlled comparison with the correctness-only baseline is missing.** The paper compares the helpful prover (from checkability training, ~70% accuracy per Fig.~\ref{fig:v5g-human-data}a) to the correctness-only prover (at 7k steps, ~80% accuracy per Fig.~\ref{fig:correctness-only}a). These provers differ not only in training method but also in accuracy. The paper does not test whether a correctness-only prover early-stopped at matching accuracy (~70%) would have better or worse legibility than the helpful prover. The authors acknowledge this in the limitations (Sec.~\ref{sec:limitations}, "we could have early stopped at less accurate but more legible checkpoint"), but do not provide the comparison. This does not invalidate the paper's trade-off framing (Fig. 1 is about the Pareto frontier), but it raises uncertainty about whether the legibility benefit comes from the training method or simply from lower accuracy. *Why it matters:* A cleaner comparison would substantially strengthen the paper's main claim.

3. **The effective verifier size range is narrow.** The method works for verifiers with compute between $10^{-3}$ and $10^{-1.8}$ times the prover's compute, but fails at $10^{-4}$ (too weak to verify) and $10^0$ (too similar, enabling the sneaky prover to exploit shared blind spots). The paper is transparent about this (line 214), but this narrow window limits the method's practical applicability as a scalable oversight technique — the sweet spot requires careful calibration of the prover-verifier capability gap. *Why it matters:* Contextualizes the method's scope; the paper would benefit from discussing whether this window generalizes beyond GSM.

4. **Human evaluation of sneaky prover at intermediate rounds is incomplete.** Figure~\ref{fig:sneaky-data}b shows human accuracy only at rounds 1, 3, and 5. No rationale is given for skipping rounds 2 and 4. If only a subset of rounds was evaluated with humans, that should be stated and justified. *Why it matters:* Missing intermediate points makes the trend harder to assess and raises questions about cherry-picking.

### Trivial

5. **Theoretical result (Theorem 1) adds limited value.** The theorem assumes deterministic mappings and an unconstrained hypothesis class, which the paper acknowledges do not match the empirical setup. The result is essentially a restatement of the definitions in game-theoretic language. It does not drive any experimental design decisions or provide testable predictions. The paper would not lose anything by moving it to an appendix. *Why it matters:* Minor presentation issue; does not affect experimental contributions.

## Nice-to-Haves

- Report human accuracy broken down by problem difficulty (easy vs. hard GSM) and by whether the prover's solution is itself correct or incorrect. This would clarify the mechanism: is legibility improving because the prover gets better at solving easy problems, or because the solutions become generally clearer?
- Compute per-solution correlation between verifier score and human judgment across rounds. This would be a more direct test of the legibility transfer hypothesis than aggregate mean accuracy.
- Report the theoretical Theorem 1 as a proposition in an appendix rather than in the main text.

## Removed Points

- **Criticism about Theorem 1 being "essentially a restatement" kept as Trivial #5 above (downgraded from the critic's severity, since it doesn't harm the paper).**
- **Criticism comparing this paper negatively to other related works (e.g., "Parrish et al. 2022 showed negative results for human debate"):** The paper already cites and discusses this work. This is not a weakness of the paper.
- **The harsh critic's framing of Point 2 as "Medium-High" severity:** Downgraded to Minor because the paper's claim is about the trade-off (Fig. 1 headline) rather than a superiority claim at equal accuracy, and the limitation is partially acknowledged.

## Novel Insights

The key insight from the reviews is that the paper's strongest and most robust finding may not be the headline human legibility transfer, but rather the *negative* results: (a) correctness-only RL degrades human legibility even on simple math, and (b) iterative goodharting (optimizing for verifier score without role conditioning) does not improve human legibility. These negative findings are actually better supported than the positive transfer claim, and importantly they imply that role-conditioned adversarial training (the SRC reward) is doing something qualitatively different from naive reward optimization. The paper would be strengthened by reframing the contribution around this contrast.

## Suggestions

1. **Add statistical rigor to the human evaluation.** Report confidence intervals (bootstrapped), per-condition sample sizes, and contractor demographics. Perform a statistical test (e.g., mixed-effects logistic regression with problem and contractor as random effects) to assess whether round-over-round accuracy trends are significant. Report inter-annotator agreement.
2. **Add the accuracy-controlled comparison.** Evaluate the correctness-only prover at the accuracy level matching the helpful prover (early-stop around ~70% accuracy) and compare human legibility. If the helpful prover still wins, the claim is substantially stronger.
3. **Justify the choice of which rounds received human evaluation.** If only rounds 1, 3, and 5 were evaluated for the sneaky prover, explain why rounds 2 and 4 were skipped.
4. **Move Theorem 1 to an appendix** to make room for the above additions.

## Score and Decision

**Originality:** High. The use of small-verifier checkability as a proxy for human legibility is a novel and well-motivated approach.

**Importance of research question:** High. Scalable oversight and making AI outputs verifiable is a central alignment concern.

**Claims support:** Moderate. The non-human evaluations (verifier robustness, training dynamics, best-of-n) are well-supported. The central human legibility claim is under-supported due to missing statistical rigor.

**Soundness of experiments:** Moderate. The automated evaluations are solid; the human evaluation protocol is underreported.

**Clarity of writing:** Good. The paper is well-structured and the core ideas are communicated clearly.

**Value to research community:** Moderate-High. Even the non-human results and the legibility tax concept are useful contributions.

The paper addresses an important problem and proposes a promising approach. The non-human evaluations are thorough and well-executed. However, the paper's most interesting claim — that legibility to small verifiers transfers to humans — is supported by human evaluation data that lacks the statistical rigor expected for a headline result. The missing error bars, sample sizes, statistical tests, and protocol details make it impossible to assess whether the observed trends are reliable. This is a fixable weakness, but in its current form the evidence does not meet the bar for acceptance. I recommend major revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>