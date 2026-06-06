## Summary

This is a philosophical position paper arguing that the characterization of neural networks as "black boxes" rests on an unwarranted assumption: that causal continuity necessarily implies *correlative* continuity (the existence of individually isolable intermediate features that track the distal cause). The paper provides a physical counterexample (potter's clay exhibiting a wobble at t₁, then again at t₃ after a stationary pause at t₂, with no isolable t₂ feature corresponding to the wobble frequency) and argues this has consequences for how we should understand and discuss neural network opacity, with applications to the Cloud et al. (2025) "subliminal owl" transfer phenomenon and to trust/transparency discussions in XAI.

---

## Strengths

- **Novel conceptual framing**: The paper precisely names and interrogates an underexamined assumption in XAI discourse — that causal continuity guarantees the existence of individually identifiable intermediate correlates — which is distinct from the more commonly debated question of whether those correlates are *accessible*. This is a genuinely non-obvious distinction (Section 2, especially the t₁/t₂/t₃ formalism in §1.3 and §2.2).

- **Methodological honesty about desiderata**: Section 2.1 carefully specifies what a valid counterexample must satisfy (nonlinear dynamics, unequivocal causal attribution, relatively low-level causation), and then the paper explicitly acknowledges where its clay example and owl application fall short of these criteria (footnotes 14, 15). This intellectual care strengthens the paper's credibility.

- **Appropriately hedged scope**: Section 2.3 explicitly acknowledges that correlative continuity will vary by system and by feature, not be uniformly absent, and that the paper's claim is "in at least some cases" rather than a sweeping universal claim. This prevents the argument from overclaiming.

- **Concrete application to a real phenomenon**: The Cloud et al. (2025) subliminal learning case is a well-chosen empirical puzzle — owl tendencies transmitted through semantically void number sequences — that makes the philosophical point vivid and practically relevant to AI researchers (§3.1).

---

## Weaknesses

### Fatal
None. The paper's core philosophical argument, while underdeveloped, is internally coherent and not demonstrably invalid from the text as written.

### Major

- **The critical philosophical move — why holistic correlates don't count — is asserted rather than argued.** The paper's load-bearing distinction is between "the holistic/overall state of the system at t₂" (which the paper grants is causally implicated) and "individually isolable features that correlate." The paper invokes intuition ("someone who asked why the clay wobbled thus and not otherwise at t₃, if met with 'because of the overall form of the clay at t₂', would be right to be unimpressed," §2.2) but does not provide a rigorous philosophical account of why holistic correlates do not satisfy the concept of "correlate" in the sense needed for the argument to go through. Footnote 12 correctly anticipates the objection — "an omniscient being might... be able to tell merely from the clay's state at t₂ what would happen at t₃, given the spin of the wheel" — and responds that this "still would not identify any *features* at t₂ that corresponded with particular features at t₃." But this response itself presupposes that "features" must be finer-grained than "the whole state," which is precisely the claim that needs defending. A physicist would say that asymmetric internal stress distributions in the clay at t₂ *are* the encoded correlate; the paper never explains why such distributed physical quantities fail to count as correlates in its framework. Without a definition of "correlate" that makes clear the distinction between a holistic/predictive state and an isolable feature-correlate, the counterexample is suggestive but not conclusive. This is the paper's most significant gap.

- **No engagement with the mechanistic interpretability literature.** The paper's central claim — that we cannot assume intermediate correlates exist in neural network activations — directly inverts the working hypothesis of an active empirical research program (work on circuits, probing classifiers, sparse autoencoders, superposition, etc.) that proceeds by finding such correlates. The paper does not cite, engage, or address this work. Since the paper claims a philosophical conclusion with practical implications for XAI methodology, its silence on the empirical program actively searching for what the paper says may not exist is a substantial gap. The paper is compatible with interpretability finding correlates in many cases (since it only claims discontinuity occurs "in at least some cases"), but this compatibility should be explicitly worked out.

### Minor

- **The owl application is presented as a candidate, not a demonstration, but the hedging is buried in a footnote.** Footnote 15 acknowledges that "a rigorous demonstration that the relevant distally associated features are causally continuous but not correlatively continuous... would require a paper of its own." This is honest, but the body text of §3.1 reads more confidently ("There is no feature of the set that 'means' owl... The data set has this form... the explanation is complete"), potentially misleading readers who do not notice the footnote. The status of the owl case as illustrative rather than demonstrated should be clearer in the main text.

- **The consequences for trust (§3.2) are explicitly hedged to the point of limited payoff.** The paper acknowledges that reframing opacity as ontological rather than epistemic "may make no ultimate difference to the trust we do, or should, have in a system." This is honest but means the paper's substantive contribution to trust discourse is unclear — mainly the negative claim that discussions explicitly assuming *hidden* features are conceptually mistaken, which is a narrower conclusion than the framing suggests.

### Trivial
None.

---

## Nice-to-Haves

- A rigorous definition of "correlate" as used in the paper (distinguishing holistic-predictive states from individuated feature-correlates) would significantly strengthen the argument and is the single most important addition the paper could make.
- A brief discussion of how the paper's claim relates to mechanistic interpretability findings — e.g., framing circuits and probing classifiers as cases where correlative continuity *does* hold and explaining what the paper's framework predicts about when it breaks down — would make the contribution much more actionable for ML researchers.
- The "view from above" framing in §2.3 is the paper's most important moderating contribution; making it more prominent (rather than positioned as a qualifying caveat) would strengthen the paper's reception.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "The counterexample is a structural failure before Section 3 is reached."** This overstates the problem. The paper anticipates the omniscient-being objection explicitly in footnote 12 and provides a response. The response may be philosophically contestable, but it is not absent — the paper does not simply commit the conflation the critic attributes to it. Demoted to Major (underdevelopment of the key distinction rather than outright failure).

- **Harsh Critic: "The transition to neural networks is assumed, not argued — and the paper's conclusion is sweeping."** The paper explicitly hedges: "in *at least some* of these cases the putatively hidden elements... do not exist" (§3, opening), and §2.3 explicitly treats correlative continuity as feature- and system-dependent. The framing of the paper's conclusion as "sweeping" misreads its actual scope. This is not a valid weakness as stated.

- **Harsh Critic: "The Section 3.2–3.3 consequences are terminological."** The paper itself acknowledges the consequences may be more limited than they initially appear (§3.2: "may make no ultimate difference"). This is intellectual honesty, not a weakness. Not a valid criticism.

- **Strength Finder: "Logically rigorous counterexample."** The clay example is vivid and productively framed, but as noted, the critical philosophical move is underargued. Characterizing it as "logically rigorous" overstates its current form.

- **Strength Finder: "Thorough grounding in XAI literature."** The paper cites standard XAI survey literature but does not engage with the mechanistic interpretability literature, which is directly relevant. Characterizing the literature engagement as "thorough" is inaccurate given this gap.

---

## Novel Insights

The paper surfaces a genuinely underexplored distinction in XAI philosophy: opacity has been almost universally framed as *epistemic* (hidden correlates exist but cannot be found), whereas the paper argues that for some systems and features the correct framing is *ontological* (no individuated correlate exists to find). This reframing implies that characterizing neural network outputs as "incomprehensible" or "hidden" is potentially a category error in some cases, not merely an epistemic limitation to be overcome. If the argument is successfully completed — particularly the definition of "correlate" and the engagement with interpretability findings — this would constitute a meaningful conceptual contribution to the foundations of XAI discourse. The observation that explanatory completeness does not require correlative continuity is non-trivially different from existing XAI discussions and deserves serious philosophical development.

---

## Suggestions

1. **Define "correlate" precisely**, distinguishing (a) predictive sufficiency of the holistic state, (b) distributed/aggregate physical properties, and (c) individually isolable named features. The paper needs this to show that (a) and (b) are present in the clay case while (c) is absent, and to argue why (c) is what the XAI literature assumes and why that assumption is unwarranted.

2. **Add a section situating the claim relative to mechanistic interpretability.** The paper's argument is compatible with circuits and probing classifiers being real (those are cases where correlative continuity *does* hold); framing the paper's contribution as explaining when and why we should not expect this to extend universally would significantly increase its credibility and usefulness to the ML community.

3. **Promote the hedge in footnote 15 to the main text of §3.1.** The owl case should be explicitly presented as an illustrative application of the framework rather than a demonstrated instance — the current body text overstates the conclusion, while the footnote undersells it.

4. **Sharpen the trust consequences.** §3.2 currently argues mainly that trust arguments explicitly depending on *hidden* intermediate features would need revision. Making this more concrete — which specific arguments in the trust literature make this assumption, and how would their conclusions change — would make the section more valuable.

---

## Score and Decision

**Originality**: The core philosophical move is novel within the XAI discourse; introducing the causal vs. correlative continuity distinction and arguing for ontological (not merely epistemic) opacity dissolution is a fresh lens. *4/5*

**Importance**: If the argument were fully developed, this would be significant for how XAI frames its goals. In current form, the scope is appropriately modest but the practical import remains unclear. *3/5*

**Claims supported**: The clay counterexample is suggestive but the key philosophical distinction is asserted rather than rigorously argued; the owl application is explicitly not demonstrated; the connection to neural networks is hedged but not grounded. *2/5*

**Soundness**: The paper is internally consistent and appropriately hedged, but the central argument has a genuine gap at its critical juncture (the definition and justification of what counts as a "correlate"). *2/5*

**Clarity**: The writing is clear and well-organized; the distinctions are explained intuitively, even if not always rigorously. *3/5*

**Community value**: The philosophical reframing is potentially valuable to XAI researchers, but the failure to engage with mechanistic interpretability limits its immediate relevance to the ML community. *3/5*

The paper makes a genuinely novel and interesting philosophical argument that is relevant to XAI foundations. However, the critical philosophical move on which the whole paper depends — the distinction between holistic causal mediation and the presence of identifiable intermediate feature-correlates — is underdeveloped, and the paper's signature empirical application is explicitly deferred to a future work. The absence of engagement with the mechanistic interpretability literature is a notable gap for a paper targeting the ML community with claims about what can and cannot be found in neural network intermediate states. These are significant enough to warrant revision, but the underlying idea merits development.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>4</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>