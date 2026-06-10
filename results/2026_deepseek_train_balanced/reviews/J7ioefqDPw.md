## Summary

This paper identifies six evaluation pitfalls in prior label-poisoning work for GNNs, proposes remedies (a corrected CV evaluation framework), introduces two new families of attacks (linear-surrogate and meta-learning), and provides theoretical analysis of a counterintuitive binary-flip phenomenon. The core contributions are: (1) a systematic audit showing prior evaluations inflated attack efficacy by ~9% on at least one benchmark, (2) a theoretically grounded linear-surrogate attack (SGC-BIN) that outperforms prior baselines by up to ~13%, (3) theoretical results (Propositions 1–2) enabling efficient exact optimization, and (4) analysis of why binary-restricted attacks can outperform unconstrained multi-class attacks.

## Strengths

- **Systematic identification and remediation of six evaluation pitfalls (Section 3).** The paper pinpoints specific, well-motivated flaws in prior evaluation setups (class-equalized splits, no hyperparameter tuning, clean validation sets, etc.) and quantifies their cumulative effect — e.g., LFK's reported efficacy drops by ~9% on Cora-ML after corrections. This is a concrete methodological contribution that establishes a more rigorous benchmark for the sub-area.

- **Proposition 1 (Section 4.1): Integral LP relaxation via total unimodularity.** Proves that the MILP in Eq. 2 can be solved exactly with any LP solver, avoiding heuristic gradient-based or greedy approximations used by prior attacks. This is a genuine theoretical advance that guarantees optimality within the surrogate model.

- **Proposition 2 (Section 4.1): Closed-form O(L log L) solution for the fixed-target variant.** Eliminates even the need for an LP solver for SGC-FIX, making the attack computationally cheaper than prior gradient-based methods. The proof is provided in the appendix.

- **Strong empirical results across multiple models and defenses (Section 5).** SGC-BIN outperforms all prior baselines with maximum gains of up to ~13%, and the evaluation goes beyond undefended GCN to test against two dedicated label-poisoning defenses (CPGCN, RTGNN) and a certified defense (ALBATIONGCN). The finding that RTGNN is vulnerable at 10% poison budget is a concrete and impactful result.

- **Analysis of the binary-flip phenomenon (Section 4.3).** The paper provides both experimental evidence (surrogate loss gap, adversarial overfitting) and a theoretical result (Proposition 3 for random flips) explaining why restricting attacks to two classes can outperform unconstrained multi-class attacks. This is a genuinely interesting observation that challenges natural assumptions.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Abstract overclaims relative to main-text evidence.** The abstract states that "the entire literature on label poisoning for GNNs is plagued by serious evaluation pitfalls" and quantifies a "discrepancy of ~9% on average." The ~9% figure is demonstrated for one attack (LFK) on one dataset (Cora-ML) with one model (GCN) in the main text (Fig. 2). While the paper references broader validation in the appendix (§B.8, §B.17), the abstract's sweeping characterization goes beyond what the main-text experiments alone support. Additionally, there is a numerical inconsistency: the abstract reports improvements "up to ~8%" while the main text (line 167) reports "maximum gains of up to ~13%" without clarifying whether these refer to different quantities (average vs. maximum).

- **The claim about SGC attack transferability lacks quantitative support in the main text.** Line 171 states that "SGC-based attacks transfer well to a wide range of vanilla GNNs as well as robust GNNs" but provides no concrete numbers or figure in the main text to support this. The claim is important for the paper's narrative but cannot be evaluated from the main content alone.

- **The binary-flip analysis, while interesting, is more methodology-specific than the framing suggests.** The two explanations (surrogate loss gap, adversarial overfitting) are tied to the specific choices of using a least-squares surrogate and default hyperparameters. Proposition 3 covers only random flips, not worst-case optimal attacks (as the paper acknowledges). The phenomenon may be less fundamental and more contingent on specific methodological choices than a reader might infer.

- **The meta-attack family is presented as a parallel contribution despite being consistently outperformed by the simpler LSA family (Section 5).** Including negative results is good scientific practice, but the paper's structure frames both families co-equally in the contributions (§1, items 2 and 4), while the results show one family clearly dominates.

- **Limited discussion of the SGC approximation's limitations.** The paper notes SGC's empirical similarity to GCN but does not discuss settings where the linearization might break down (e.g., graphs where nonlinearities play a larger role). Similarly, the scalability of the MILP approach (O(D³ + D²N) pre-computation) is mentioned only in passing.

### Trivial

- The abstract reports "up to ~8%" improvement while the main text reports "up to ~13%" — these appear to be different quantities but this is not clarified.
- The "tiny version" of Cora-ML used for the exhaustive enumeration example (§1, line 14) is not described in the main text; the paper defers to §B.1.

## Nice-to-Haves

- A 2×2 comparison table (old/flawed framework vs. new/corrected framework × prior attacks vs. new attacks) would more cleanly disentangle the effect of the framework change from the effect of attack design. The paper partially addresses this in §B.12, but main-text presentation would strengthen the argument.
- Statistical significance testing (e.g., paired t-tests across splits) would help confirm that claimed improvements exceed variance, especially given the standard deviations reported.
- Explicit mapping of which prior papers commit which specific pitfalls would make the critique more actionable.

## Removed Points

*These points were considered but removed as unsupported, misreading the paper, or otherwise failing filtering criteria. They are noted here only in case they prove useful, and should be treated with caution.*

- **"Confounded comparison"** (Harsh Critic Weakness 1): The claim that new attacks are "purpose-built for the corrected evaluation framework" is not supported by the paper. The paper explicitly states "These attacks are independent from the pitfalls" (line 83) and shows they are "even stronger on the default (flawed) setting" (§B.12, line 173). The attacks use general techniques (linear surrogates, meta-learning) that are not specific to the CV framework. All attacks are evaluated under identical conditions, which is standard practice — not a confound. Removed as a misunderstanding.

- **"Meta-attack family is a weak contribution that inflates breadth"** (Harsh Critic Weakness 3): The paper transparently reports that meta attacks are "inferior on average" (line 171). Including and honestly reporting negative results is good scientific practice, not a weakness. The paper's framing as a "family" simply describes the different approaches explored, without concealing the results. Removed.

- **Missing related works**: Removed per instructions (cannot verify existence of omitted works).
- **Formatting/style nitpicks and parser artifacts**: Removed per instructions.
- **Missing appendix content**: Removed — appendix sections are stripped by the parser from all papers.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an independent insight that the paper itself does not already articulate.

## Suggestions

- Reconcile the "~8%" (abstract) and "~13%" (Section 5) numbers, clarifying whether one is an average and the other a maximum.
- Add a brief main-text table or figure supporting the transferability claim (line 171) rather than only stating it.
- Consider repositioning the meta-attack results more clearly as a negative finding (i.e., "adaptive attacks are not always superior") rather than as a co-equal contribution family.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>