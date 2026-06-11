## Summary

This philosophical position paper argues that the "black box" characterization of neural networks rests on a fallacious assumption: that causal continuity (A causes B through an intervening system) necessarily implies correlative continuity (there must exist individuable intermediate features that correspond to A and B). The paper provides a counterexample from fluid dynamics (clay on a potter's wheel developing a wobble) where causation runs across a rest period but no fine-grained feature of the still clay correlates with the subsequent wobble. It then applies this reasoning to a recent LLM "subliminal learning" study (Cloud et al., 2025) and sketches consequences for XAI, trust, and the language of opacity.

## Strengths

1. **The clay counterexample (Section 2.2)** — The paper provides a concrete, intuitive, non-neural physical system where causal continuity holds but correlative continuity fails. The clay's wobble frequency at t₁ causes the wobble at t₃, yet no individuable feature of the clay at rest (t₂) demonstrably corresponds to the oscillation frequency. This genuinely serves as a counterexample showing that correlative continuity is not a conceptual necessity.

2. **The epistemic/ontological distinction (Section 2.3)** — The paper clearly characterizes the limits of feature individuation as potentially ontological rather than merely epistemic: "Even an omniscient god could not identify a feature in the still clay at t₂ that causally corresponded to the frequency of its oscillation at t₃." This goes beyond standard "black box" critiques (which typically frame opacity as an epistemic limitation) and recharacterizes what the opacity problem could amount to.

3. **Application to the Secret Owls phenomenon (Section 3.1)** — The paper takes a striking empirical finding (Cloud et al., 2025) and provides a genuinely novel explanatory alternative. Instead of positing "hidden" or "encoded" owl-signals in the semantically vacuous number sequences, it offers the interpretation that there simply may be no finer-grained correlate to be found — a possibility the standard framing does not countenance.

## Weaknesses

### Major

1. **The clay/neural network analogy gap is under-analyzed** — The paper acknowledges that "a lump of clay is largely homogeneous" while neural networks have richly structured internal representations, and further notes that "if the brain were as homogeneous as clay, most efforts in cognitive neuroscience would never have progressed at all" (line 131). However, the paper never develops a positive argument for why the clay-style correlative discontinuity would obtain in neural networks specifically. The claim that the degree of correlative continuity falls on a spectrum (lines 131–133) is a concession, not a bridge: it tells us the phenomenon *could* occur in neural networks but does not establish that it *does* occur for any behavior of interest. Since the paper's provocative title ("The Myth of the Box") and framing target neural network opacity specifically, this gap between the abstract possibility (demonstrated by clay) and the claimed application domain (neural networks) is the paper's most significant unresolved issue.

2. **The notion of "feature" is not sufficiently defined** — The argument hinges on whether intermediary features "exist" that "meaningfully correlate" with an output feature. The paper provides no criteria for feature individuation. In the clay example, one could identify elastic moduli, residual stress distributions, and geometric asymmetries that correlate with oscillation behavior. The paper dismisses these as merely "the overall state" or "necessary conditions" (line 115) rather than genuine features, but this dismissal rests on an intuitive judgment rather than a principled theory of what makes something a genuine causal feature. This matters because the paper's application to neural networks inherits the same ambiguity: when a mechanistic interpretability researcher identifies a direction in activation space, the paper would need a principled basis to say whether this is a "genuine feature" or not.

### Minor

3. **The owls case application is acknowledged to be merely suggestive** — The paper's most concrete neural-network-specific example is the Cloud et al. (2025) study. The paper itself admits (footnote 15) that rigorously demonstrating correlative discontinuity in this case "would require a paper of its own" and that the offered explanation is merely "a candidate" (line 153). While the paper's central claim (that the assumption is a fallacy) is established by the clay counterexample and does not depend on the owls case, the fact that the primary neural-network illustration is only speculative limits the paper's applied force for its claimed domain.

4. **Practical implications are heavily hedged** — After building up the claim that the black box is "mere myth" (line 171), the paper's discussion of consequences is almost entirely qualified: the trust implications "depend on the details of the argument" (§3.2); the linguistic revision will have "subtle and diffuse" effects (§3.3). The paper is honest about these limits, but a reader is left wondering what concrete difference the argument makes for practitioners.

### Trivial

None.

## Nice-to-Haves

- A more precise definition of "feature" or engagement with the causal abstraction literature.
- A toy neural network construction where the clay-like correlative discontinuity can be provably demonstrated.
- More discussion of how to determine, in practice, when correlative discontinuity applies vs. when features can be found.
- A more developed account of how the argument changes research practice beyond linguistic/conceptual revision.

## Removed Points

These points are flagged to be removed; treat them with caution.

**Missing engagement with mechanistic interpretability (from Harsh Critic)** — Removed because: (1) the rule instructs not to critique missing related works; (2) the criticism misunderstands the paper's scope — the paper does not claim correlative continuity NEVER occurs, only that it is not GUARANTEED. Successful mechanistic interpretability would simply show that in those cases correlative continuity DOES hold, which is consistent with the paper's position that it "depends on the details."

**Section 1.1 in-principle opacity tension** — The critic claimed the paper undermines its own distinction. Removed because the paper adequately addresses this by characterizing opacity as potentially ontological rather than exclusively epistemic — this is precisely the paper's main point.

**Demand for empirical predictions** — Removed as inappropriate for a philosophical position paper. The paper is a conceptual critique, not a scientific hypothesis.

**Section 3.3 as truism** — The critic claimed this section is a truism. Removed because the observation that language shapes research is not central to evaluating the paper's core argument about the correlative continuity fallacy.

**Clay example physicist objection** — The critic claimed a physicist could identify features that correlate. The paper addresses this by distinguishing necessary conditions from genuine causal features (line 115). While the distinction could be sharper, the criticism is partially addressed in the paper.

## Novel Insights

None beyond the paper's own contributions. The most insightful concern raised across the reviews is about the feature definition problem: the paper's argument depends on a notion of "genuine features" vs. "mere necessary conditions" that would need sharper philosophical articulation to carry the weight placed on it. This is a genuine gap that the paper's counterexample does not resolve.

## Suggestions

1. Strengthen the bridge between the clay example and neural networks by constructing a toy neural network where correlative discontinuity can be demonstrated, or by providing a more rigorous argument about why certain classes of neural network behaviors resist feature decomposition.
2. Define "feature" more rigorously, perhaps by engaging with the causal abstraction literature (which provides formal tools for talking about when a representation "mediates" causation).
3. Consider providing heuristic criteria for determining when correlative discontinuity is plausible vs. when features are likely to be findable.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| "What Does it Mean for a NN to Learn a 'World Model'?" (89nUKXMt8E) | 4.75 | R1+R2 | Most similar in genre: conceptual paper without experiments, rejected. Current paper has tighter argument but same vulnerability on practical significance. |
| "The No Free Lunch Theorem..." (X7nz6ljg9Y) | 5.00 | R2 | Conceptual paper with experiments; criticized as somewhat vacuous. Current paper is sharper but lacks experiments. |
| "Local vs Global Interpretability" (324zEJCo3a) | 6.00 | R1 | Formal theoretical paper with proofs — significantly more rigorous. |
| "Neural Networks and Solomonoff Induction" (tJDlRzQh7x) | 4.33 | R1+R2 | Has experiments but criticized for novelty and rigor issues. |
| "Causal Concept Graph Models" (lmKJ1b6PaL) | 6.80 | R1 | Accepted methods paper with strong experiments — not comparable genre. |

**Round 1 bracket:** (3, 8) with most similar papers near 4.5–5.0
**Round 2 narrowing:** (4.5, 5.5)

The paper makes a genuinely interesting philosophical point and presents a well-constructed counterexample. However, it does not successfully bridge from that abstract possibility to the neural network domain, and its key concept ("feature") is underspecified in ways that undermine argument evaluation. For a technical ML conference, the contribution is primarily conceptual rather than methodological or empirical, and the gap between the philosophical claim and practical relevance to neural network research is too wide. The paper would be a stronger fit for a philosophy of science or interdisciplinary AI journal.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>