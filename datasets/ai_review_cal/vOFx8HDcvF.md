- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6
Now I have all the evidence I need. Let me write the consolidated review.

## Summary

The paper studies stochastic multi-armed bandit algorithms robust to adversarial attacks where the attacker observes the arm pull before altering the reward. It systematically covers four cases: known/unknown attack budget × additive/multiplicative C-dependence. For known C, it tightens the analysis of successive elimination with wide confidence radius to obtain O(∑(log T)/Δ_k + KC) and O(√(KT log T) + KC) bounds matching lower bounds. For unknown C, it proposes a phase-elimination algorithm (PEWR) achieving Õ(√(KT) + KC²) and a model-selection approach (MSSEWR) achieving Õ(KC√T)/Õ(√(KC)T^{2/3}). Lower bounds show tightness relative to class-specific forms. The paper also cleanly delineates the separation between attack (strong adversary) and corruption (medium adversary) models.

## Strengths

- **Systematic and tight known-C gap-dependent bound (Theorem 1).** The paper proves SEWR achieves O(∑_{k≠k*} (log T)/Δ_k + KC), matching the lower bound Ω(∑ (log T)/Δ_k + KC) from Proposition 1. This improves over the prior corruption-model analysis by Lykouris et al. (2018), which had an additional ∑ C/Δ_k term. The improvement is essential for the subsequent multiplicative bounds.

- **General Ω(KC) lower bound (Theorem 4 / Proposition 1).** The paper proves that any algorithm under attack must suffer Ω(KC) regret — a foundational result that does not exist in earlier attack or corruption literature. This cleanly separates the attack model from the corruption model (where the additive cost is Θ(C'), without the K factor).

- **Tight unknown-C additive bound via PEWR (Theorem 3).** The phase-elimination algorithm achieves Õ(√(KT) + KC²), which matches the class-specific lower bound Ω(√T + C²) from Proposition 2 (α=1/2) in terms of T and C, and is tight in K relative to the general Ω(√(KT) + KC) bound. The multi-phase design that halves assumed budgets per phase is elegant and clearly explained.

- **Tight unknown-C multiplicative bounds via model selection (Theorem 4).** Using SEWRST as base learners and CORRAL/EXP3.P as meta-algorithms, the paper achieves Õ(KC√T) and Õ(√(KC)T^{2/3}), matching the class-specific lower bounds Ω(C√T) and Ω(√C T^{2/3}) from Proposition 3. The discussion of why certain base-algorithm bounds lead to weaker final bounds (Lines 409-415) is informative.

- **Clear conceptual separation between attack and corruption models.** The paper rigorously argues (Section 2 and throughout) that the strong-adversary (attack) model is fundamentally harder than the medium-adversary (corruption) model: the attack cost is K times larger in known-C additive bounds, and sublinear C can force linear regret under attack but not under corruption.

## Weaknesses

### Fatal
None.

### Major

- **The model-selection argument (Section 5.2) relies on a simplified lemma that does not directly address misspecified base instances.** Lemma 1 (model-selection) states a conditional guarantee: *if* a base algorithm has regret bounded by T^α c(δ), *then* CORRAL/EXP3.P have certain guarantees. However, SEWRST instances with input budget 2^g < C can have *linear* regret, violating the lemma's condition. While the paper acknowledges the "robust-or-not" separation (Line 322-323), it does not argue why the model-selection framework handles this case — i.e., why the meta-algorithm's regret is still controlled when some bases are catastrophically bad. The lemma as presented is insufficient to directly establish Theorem 4's bounds without additional reasoning about how CORRAL/EXP3.P cope with differentially abysmal base learners. This is a standard concern in model selection and likely addressable, but the paper does not address it.

### Minor

- **Derivation of gap-independent stopping conditions is compressed and the connection to implementable rules is not fully spelled out.** Section 4.2 sketches the transition from stopping conditions like N_k ≤ (log(KT/δ))/ε² + C/ε to the final implementable rules N_k ≤ T/K + C√(T/(K log(KT/δ))) and N_k ≤ T/K. The algebra is implicit (substituting the optimized ε values) and the text jumps from the ε-based derivation straight to the theorem statement without showing the substitution steps. A reader working through the details must fill in intermediate algebra. The paper would benefit from showing the substitution explicitly.

- **The bound for PEWR (Theorem 3) is presented with multiple additive terms (√T log T, KC log T) before simplification to Õ(√(KT) + KC²).** While this is standard in bandit theory, the paper does not discuss the relative ordering of these terms — e.g., whether KC log T could dominate KC² for small C. A brief remark on why the Õ simplification is faithful to the actual bound would improve clarity.

### Trivial

- The abstract mentions the known-C multiplicative bound as Õ(√(KTC)), but Theorem 2 gives O(√(KT(log T + C))) which is slightly different (the former implies a specific log-factor structure). This is a minor inconsistency in presentation.

- Section 4.2 refers to the stopping condition N_k ≤ T/K + C√(T/(K log(KT/δ))) but does not explain how this is checked: is it evaluated per-arm, per-round, or at the end of each elimination cycle? The practical implementation is left ambiguous (though likely deferred to the appendix).

## Nice-to-Haves

- Inclusion of even a small synthetic experiment (e.g., regret vs. C for PEWR and MSSEWR on a simple K=2 or K=5 instance) would strengthen the paper by validating the theoretical trends. The paper is purely theoretical, so this is not a weakness, but it would increase impact.

- A brief discussion of why the Ω(KC) general lower bound cannot be matched by an additive unknown-C bound — i.e., why the KC² term may be necessary — would improve the narrative. The paper currently notes the gap (KC² vs. KC) in passing but does not discuss its necessity or whether closing it is an open problem.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Overclaiming of tightness for the unknown-C additive bound"** (Harsh Critic). **Removed** — the paper explicitly states both comparisons: it matches the class-specific lower bound Ω(√T + C²) in T and C, and the general lower bound Ω(√(KT) + KC) in K. Line 366 reads: "Comparing our upper bound...to the lower bound in Proposition 4 with α=1/2, Ω(√T + C²), we know that our upper bound is tight in terms of both T and C. Compared with the lower bound Ω(√(KT) + KC) in Proposition 2, our upper bound is also tight in terms of K." This is precise and does not overclaim. The critic's assertion that the paper conflates "tight among a class" with "tight in general" is factually contradicted by the paper's own text.

- **"The literature review claim about Zuo (2024) needs qualification"** (Harsh Critic). **Removed** — the claim "the only existing result on robust algorithms for MAB under attacks is by Zuo (2024)" appears in the "Robustness against attacks" subsection (Line 116), which follows subsections on corruption and attack policy design. The context ("Apart from the MAB model, there are works studying structured bandits...") makes it clear the claim is about the standard MAB setting. This is a reading-misattribution.

- **"Missing pseudocode for Algorithms 2 and 3"** and **"Missing appendix content"**. **Removed** — the parser strips appendix and supplementary content from all papers. The claim that algorithmic modifications are "not verifiable" because pseudocode is missing is a known parsing artifact, not an author error.

- **"Missing experiments" as a weakness** (Harsh Critic). **Removed** — the paper is clearly a theoretical paper. The critic acknowledges this is "acceptable for a theory paper" but then lists it as a weakness. Moved to Nice-to-Haves.

- **"The PEWR bound is dirty with multiple terms"** (Harsh Critic). **Removed** — presenting exact bounds before simplifying to Õ notation is standard practice in the bandit literature. The lower-order terms (√T log T, KC log T) are explicitly shown and then absorbed under Õ, which is standard and honest.

- **Strength Finder's generic/superficial strengths.** Some strengths from the Strength Finder are retained. The ones about "tight bounds" are concrete and evidence-based. None of the retained strengths conflict with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder do not surface perspectives not already present in the paper. The most interesting cross-cutting observation from the reviews is the need to distinguish "tight among a restricted algorithm class" from "tight in general," but the paper itself already makes this distinction (Line 366), so this is not a novel insight.

## Suggestions

1. **Address the model selection gap explicitly.** In Section 5.2, either: (a) cite a version of the CORRAL/EXP3.P analysis that explicitly handles misspecified base learners with potentially linear regret, (b) provide a short self-contained argument that the meta-algorithm's regret is controlled even when some bases fail the condition in Lemma 1, or (c) add a caveat that Theorem 4's bounds assume the model-selection conditions are met, and note that verifying this for the given setting requires additional standard arguments from the model-selection literature.

2. **Show the algebra for the stopping condition derivations.** In Section 4.2, add two lines showing the substitution of the optimized ε into the initial stopping condition to obtain the implementable rule in Theorem 2. This would connect the ε-based derivation to the final theorem statement and make the transition transparent.

3. **Add a remark about the relative size of lower-order terms in Theorem 3.** A brief note on when KC log T vs. KC² dominates (and why it doesn't affect the qualitative conclusion) would help readers understand the Õ simplification.

4. **Clarify how the stopping conditions in Section 4.2 are checked in practice.** Specifically: are N_k thresholds evaluated after each elimination round, after each pull, or only at the end? A brief sentence would resolve ambiguity.
