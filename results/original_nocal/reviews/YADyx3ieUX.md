## Summary

This paper argues that the "black box" characterization of neural networks rests on a false assumption — that causal continuity across a system implies *correlative* continuity, i.e., that for any output feature caused by a distal input feature, there must exist an individuable intermediate feature that correlates with that output feature. The paper provides a physical counterexample (a potter's clay whose wobble at t₃ is caused by its wobble at t₁ but has no individuable correlate in the stationary clay at t₂) to break the logical necessity of this link, then applies the distinction to recent "secret owls" subliminal learning results (Cloud et al., 2025) and discusses consequences for trust and the language of opacity in AI. The paper is a philosophical critique of the conceptual framework underlying discussions of neural network opacity.

## Strengths

1. **Clear articulation of a non-obvious conceptual distinction.** The paper draws a sharp line between causal continuity (feature A at t₁ causes feature B at t₃) and correlative continuity (there exists an intermediate feature at t₂ that we can individuate and point to as "corresponding" to B). This distinction is genuinely subtle, and most discussions of opacity in AI treat these as equivalent. Naming and isolating the separation is a real conceptual contribution. (Abstract, Section 2)

2. **The clay-wobble counterexample is pedagogically effective.** The potter's clay thought experiment (Section 2.2) provides a vivid, concrete case where causal continuity is unambiguous yet no intermediate feature at t₂ can be picked out as "the wobble's correlate." The example is well-constructed: it satisfies the paper's own desiderata (nonlinear dynamics, unequivocal causal attribution, low-level causation) and makes the fallacy intuitively graspable, even if the direct transferability to neural networks remains open.

3. **Honest about its own limits.** The paper explicitly acknowledges that causal systems with correlative discontinuity are "rare" (Section 2.1), that dissolving opacity "does not alone resolve disputes concerning trust" (Section 3.2), and that a rigorous demonstration for the owls case "would require a paper of its own" (footnote 15). This intellectual honesty is commendable and lets the reader evaluate the argument on its own terms.

4. **The ontological/epistemic reframing is provocative.** Section 2.3 argues that the absence of a correlate is an *ontological* limit, not merely an epistemic one — even an omniscient god could not identify a corresponding feature. This sharpens the distinction beyond standard treatments (e.g., Zerilli's "in-principle opacity") and gives the paper a distinctive philosophical edge.

## Weaknesses

### Fatal
None.

### Major

1. **The leap from the clay example to neural networks is unsubstantiated, and the paper does not engage with how ML interpretability actually works.** The clay is a largely homogeneous physical system; neural networks are richly structured, with millions of parameters organized into layers, attention heads, and representational subspaces. The paper provides no argument that neural network internals are *relevantly similar* to the clay in the way that matters for correlative continuity. Moreover, the mechanistic interpretability literature (e.g., Elhage et al., 2021; Olah et al., 2020; Wang et al., 2022) has found *some* interpretable features — directions in activation space, circuit-level patterns — that correlate with output properties. The paper does not engage with this body of work at all, which is a significant gap given that the paper's central claim is that the "hidden features" in networks may simply not exist. Without showing why the features found by mechanistic interpretability do not count as correlates, or why they are the exception rather than the rule, the practical relevance of the argument to ML research remains unclear.

2. **The "secret owls" case study — the paper's only concrete ML application — rests on an unverified empirical premise.** The paper asserts (Section 3.1) that there is "no feature of the set that 'means' 'owl'" in the number sequences. But no evidence is provided that the sequences are genuinely devoid of *any* statistical pattern that could correlate with the teacher's owl disposition (e.g., n-gram frequencies, token distribution anomalies, subtle patterns discoverable by the student model's training dynamics). Footnote 15 acknowledges this limitation but says a full demonstration "would require a paper of its own." This is an honest admission, but it means the paper's central applied argument is structurally incomplete. If the owls example cannot carry evidential weight, the paper's claim to relevance for AI research is weakened.

### Minor

3. **The notion of "feature" is never operationalized for neural network contexts.** The paper talks about features and "individuating" them, but does not specify what counts as a feature in a neural network (a single neuron? a direction in activation space? a circuit subgraph? a principal component?). Without an operational definition, it is hard to evaluate whether the clay example's conclusion — that there is no individuable feature — would transfer to any real neural network. The paper would be stronger if it could say: "in a neural network, a 'feature' in this sense is X, and the claim is that for some output properties, no such X exists."

4. **The paper does not show that its conceptual revision would change any research practice.** The conclusion (Section 3.3) calls for revising the "black box" metaphor, but does not identify a single methodological change, experimental design improvement, or evaluation criterion that would follow from this revision. If the paper is correct that the box is a "myth," what should ML researchers do differently? The paper does not answer this, limiting its utility for the ICLR audience. The paper's own hedging — "subtle and diffuse" implications, "does not alone resolve disputes concerning trust" — reinforces this gap.

### Trivial
None.

## Nice-to-Haves

- A demonstration on a simple neural network (e.g., a small MLP trained on a synthetic task) where the framework would lead to a different explanation than standard approaches.
- Engagement with mechanistic interpretability work to clarify whether the features those methods find are genuine counterexamples to the paper's thesis or are consistent with it.
- A more precise operational definition of what "individuable feature" means in the context of a neural network's activation space.

## Removed Points

The following points from the inputs were removed (with brief justification):

- **"Paper misrepresents the black-box problem as a strawman"** — The paper's target is the conceptual framework implicit in the language of opacity, not an explicit doctrine held by researchers. The paper cites researchers describing practical difficulties, and its argument is about what those descriptions *presuppose*. This is a valid method of conceptual analysis, not a misrepresentation. The paper is transparent about what it is arguing against and does not claim that any specific researcher consciously endorses the assumption as a metaphysical principle.

- **"Clay-wobble counterexample simply redefines 'feature'"** — The paper already addresses this: lines 117–119 explicitly acknowledge aggregate features (shape, density distribution) but argue they cannot be individuated as *causal correlates of the specific target feature*. This is a substantive claim, not a redefinition. The paper also notes (line 137) that the analysis is feature-dependent — for different target features (e.g., evaporation rate), the clay does afford correlates.

- **"Rarity undermines the claim"** — The paper does not claim the fallacy is statistically widespread; it claims the assumption is conceptually foundational to the opacity discourse. Rarity of counterexamples does not undermine a logical point about a mistaken presupposition. The paper explicitly acknowledges that most systems do afford correlative continuity (Section 2.1).

- **"The god thought experiment assumes atomic features"** — The paper already addresses this by noting that the analysis is feature-dependent (line 137) and that the degree of correlative continuity varies across features within the same system.

- **"Missing related works"** — Removed per instructions (cannot verify external sources independently).

- **Formatting/style/typo nitpicks** — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface concerns about the paper's relationship to ML practice and its evidential grounding, but these are observations about gaps in the paper's argument rather than novel insights that the paper itself does not contain.

## Suggestions

The paper would be substantially strengthened by (a) engaging with the mechanistic interpretability literature to clarify where the proposed view conflicts with or complements existing findings about network internals; (b) providing an operational definition of "feature" suitable for analyzing neural network representations; and (c) discussing at least one concrete methodological implication — even if only a recommendation about how interpretability results should be interpreted or communicated. Without these, the paper remains a self-contained philosophical argument with an uncertain connection to the technical ML research it aims to inform.

## Score and Decision

The paper is a well-written philosophical critique that draws a genuinely interesting conceptual distinction. The clay-wobble counterexample is effective on its own terms, and the ontological/epistemic reframing is provocative. However, the paper's connection to actual neural network systems is asserted largely by analogy, it does not engage with substantial relevant ML literature (mechanistic interpretability), its only concrete ML application rests on an unverified premise, and it does not identify any methodological or practical implications for ML research. For a venue like ICLR, which expects technically grounded contributions that advance how we build or understand learning systems, the paper does not meet the bar. It would be more suitably directed toward a venue for philosophy of AI or interdisciplinary AI studies.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>