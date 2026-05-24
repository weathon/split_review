Now let me finalize the review.

---

## Summary

This paper is a philosophical/critical position paper arguing that the characterization of neural networks as "black boxes" rests on a false assumption about causation: that causal continuity through a system requires *correlative* continuity — i.e., that there must be intermediate features that correlate meaningfully with the effect in a way that can be individuated for explanatory purposes. The paper presents a counterexample (a potter's clay that retains a wobble across a pause, where no "feature" of the still clay at the intermediate time is said to correlate with the wobble) to expose this as a fallacy, then applies the argument to the "Secret Owls" phenomenon (Cloud et al., 2025) and draws consequences for discussions of trust and the language of opacity in AI.

## Strengths

1. **Clear framing of a genuinely underexamined assumption.** The paper identifies a specific, contestable premise that underpins much of the discourse around neural network opacity — the expectation that causal chains always decompose into intermediate features that correlate with both cause and effect. Articulating this assumption with the clarity the paper brings is itself a useful contribution, as it can help make discussions of opacity more precise.

2. **Rigorous constraints for counterexamples.** Section 2.1 lays out explicit desiderata (unequivocal causal continuity, low-level causation, complex nonlinear dynamics) that a valid counterexample must satisfy. This methodological care prevents the argument from overgeneralizing and shows awareness of the difficulty of making the case. The paper's willingness to acknowledge that valid cases are "rare" is intellectually honest.

3. **Honest about limitations.** The paper repeatedly notes where its own examples fall short of its ideal criteria (e.g., footnote 14 on the "high level" nature of causation in the owls example; footnote 15 that a rigorous demonstration would require a separate paper; Section 3.2's admission that dissolving opacity does not alone resolve trust disputes). This intellectual honesty is commendable and makes the paper's actual claims easier to evaluate fairly.

4. **The "language of opacity" discussion is worthwhile independently.** Section 3.3's point — that the metaphors we use to describe AI systems shape how we think about them — is valid and important regardless of the strength of the central philosophical argument.

## Weaknesses

### Major

1. **The clay counterexample is not as decisive as the paper claims, and the argument's central concepts are insufficiently precise.** The paper asserts that at t₂ (the paused clay) "there is no feature, or collection of features, of the clay that corresponds in any meaningful way to the wobble." But the clay's geometric asymmetries (thickness variation, center-of-mass offset) are features that directly determine the oscillation frequency under rotation — these are precisely the kind of causal correlates the paper denies exist. The paper tries to preempt this objection by distinguishing "necessary conditions" from "genuine causes" (line 119), but this distinction is never defined with enough precision to evaluate whether the asymmetries are merely necessary conditions or genuine causal correlates. Without a rigorous definition of what counts as a "feature" or "causal correlate" for the purposes of the argument, the central claim becomes largely unfalsifiable: any proposed correlate can be dismissed as "merely a necessary condition" or "not a *meaningful* correlate." This undermines the paper's ability to establish its core thesis.

2. **The gap between the clay example and neural networks is not adequately bridged.** Even if one accepts the clay example on its own terms, the paper does not provide criteria for determining *when* a neural network case is like the clay (where correlative continuity fails) and when it is not. The paper acknowledges this ("instances of apparent opacity need be treated with care, on a case-by-case basis" — footnote 15) and that neural networks do have internal structure that may support feature individuation. But this acknowledgment undercuts the central claim: if the fallacy does not reliably apply to neural network scenarios, the "myth" label is misleading. The paper's argument shows at most that we should not *assume* correlative continuity a priori — which is a far more modest claim than that the black box is a "myth."

3. **Key concepts are not defined with sufficient rigor for a conceptual paper.** The argument hinges on what constitutes a "feature" of a system, what "correlative continuity" means, and what makes a correlation "meaningful" in a "causally explanatory sense." These terms are used throughout but never given operational definitions. In a paper whose entire contribution is conceptual, this lack of precision is a significant limitation — it makes the central argument difficult to verify or falsify, and it allows the clay example to be interpreted in multiple ways depending on how one fills in the undefined terms.

### Minor

4. **The Secret Owls application is asserted rather than argued.** The paper claims the student model's owl disposition has "no discernible features that could correlate" with the teacher's owl tendencies in the numerical dataset, but provides no argument for this claim beyond an appeal to semantic vacuity. Distributional statistics of the numbers (frequencies, co-occurrence patterns) *are* features, and whether any of these causally explains the owl behavior is an empirical question the paper does not address. The paper relies on the Cloud et al. study's characterization but does not independently make the case that no correlative features exist. This weakens what is presented as the key application of the argument.

5. **The practical implications are modest despite the strong framing.** The paper's conclusions about trust (Section 3.2) are heavily caveated — the dissolution of opacity "does not alone resolve disputes concerning trust" — and the recommendation to revise the language of opacity (Section 3.3) can be accepted without the strong philosophical argument. There is a tension between the paper's provocative title ("The Myth of the Box") and the heavily qualified nature of its actionable conclusions.

6. **No engagement with mechanistic interpretability.** The paper would benefit from discussing the mechanistic interpretability literature, which directly investigates whether and how internal features of neural networks correlate with output behavior. This literature provides the most relevant test bed for the paper's claims about neural networks specifically, and its absence is a notable gap.

## Nice-to-Haves

- The paper's argument would be stronger if it dropped the claim that there are *no* intermediate features in the clay example and instead argued that the expected *type* of correlate (a localized, semantically meaningful "wobble-feature") is what cannot be found. This would align with contemporary work on superposition and distributed representations in neural networks.
- Engaging with causal modeling frameworks (e.g., Pearl's structural causal models, do-calculus in XAI) could provide a more rigorous vocabulary for the distinction the paper is trying to draw.

## Removed Points

- **Harsh critic's claim that the clay example "does not support the argument it is meant to carry" to the point of being "fatal":** This overstates the case. The paper does make a defensible philosophical distinction between necessary conditions and causal correlates, and the example retains value as an intuition-pump even if it is not as clean a counterexample as the paper claims. The criticism is valid as a *major* weakness but not as a fatal collapse.
- **Harsh critic's claim that the paper "mischaracterizes the black box problem":** Partially valid (the practical opacity of NNs is indeed driven by complexity and entanglement, not just a philosophical assumption) but the paper does acknowledge that network parameters are discoverable and the issue is relational. Demoting from fatal to major.
- **Strength finder's claim that the clay example "directly shows" the assumption is false:** Overstated. The example shows a plausible case where the assumption may fail, but the case is contested. Demoting from strong strength to qualified observation.
- **Strength finder's claim that the paper "rigorously" frames constraints:** The framing is careful but not exceptionally rigorous for a conceptual paper. Keeping as a moderate strength.

## Novel Insights

None beyond the paper's own contributions. The reviewers' insights largely converge on the paper's central tension: it identifies a real and underexamined assumption but fails to establish its central case with sufficient precision to fully carry the argument.

## Suggestions

1. Provide a precise, operational definition of what constitutes a "feature" and a "causal correlate" for the purposes of the argument. This would allow the clay example to be evaluated on its own terms rather than debated through competing interpretations of undefined terms.

2. Either (a) develop the clay example into a more rigorous case — perhaps by specifying what would count as a "feature" such that the clay at t₂ lacks it — or (b) reframe the argument more modestly: not that the black box is a myth, but that we should not automatically assume the existence of intermediate features that correlate with output behaviors. The latter position is well-supported by the paper's reasoning and does not depend on a decisive counterexample.

3. Engage with the mechanistic interpretability literature (e.g., Olah et al., Elhage et al., Nanda et al.) to connect the philosophical argument to the empirical practice of finding features in neural networks. This would make the paper's relevance to AI research much more concrete.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Low band (<3.5): PoB6QGAM38 (3.00) — methods paper on causal explanations; not comparable.
- Mid band (3.5–7.5): 89nUKXMt8E (4.75) — "What Does it Mean for a Neural Network to Learn a 'World Model'?"; conceptual/definitional paper with mixed reviews (3,8,3,5). Comparable genre and similar issues (interesting conceptual contribution, insufficient rigor).
- Mid band (3.5–7.5): vqIH0ObdqL (6.00) — empirical LLM benchmark; different genre.
- High band (>7.5): All accept-level empirical papers; different genre.

**Round 2 (Narrowing):**
- v675Iyu0ta (5.60) — "Interpretability Illusions"; critical paper with experiments. Stronger due to empirical support.
- 89nUKXMt8E (4.75) — most comparable anchor. The paper under review is better-written and more clearly argued, but has similar issues with conceptual precision.

**Round 1 bracket:** 3.5–5.5 (conceptual paper, not empirical)

**Final placement:** The paper is slightly weaker than 89nUKXMt8E (4.75) because its central argument depends more heavily on a contestable example that lacks precise definitions. However, it is better written and more rigorous in its limitations. Compared to v675Iyu0ta (5.60), the paper lacks the empirical support that would make its case more convincing. Score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>