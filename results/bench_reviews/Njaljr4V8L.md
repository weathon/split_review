Now I have a thorough understanding of the paper and calibration anchors. Let me compose the final review.

## Summary

The paper argues that System-2 AI should be understood through the lens of "complexity out-of-distribution" (OoD): test samples that require more complex representations or deeper computational paths than any training sample. It claims that addressing complexity OoD requires framing System-2 problem-solving as search over programs composed of learned semantic atomic units (with System-1 providing both the units and heuristic guidance), and calls for new benchmarks, supervision paradigms, representations, and inductive biases tailored to this perspective.

## Strengths

- **Clear position statement with an organizing framework.** The paper's central claim is explicitly articulated: System-2 problems are fundamentally about generalizing to higher complexity than seen in training, and solving them requires program-like search over compositional units with System-1 providing building blocks and heuristics. This gives readers a concrete lens through which to evaluate both existing and future work.

- **Useful dual categorization of complexity OoD into representational and computational dimensions (Section 2).** This distinction correctly captures that System-2 reasoning demands both richer representations and deeper computation, and the mapping of existing research onto these two axes (Section 4—variable-length representation vs. variable-length computation) provides a readable, informative organizational structure for the survey.

- **Topic of genuine contemporary interest.** The relationship between System-2 reasoning and out-of-distribution generalization is actively debated given current work on LLM reasoning, test-time compute, and program synthesis.

- **Explicit attempt at formal grounding.** Section 2.2 provides Kolmogorov Complexity-based definitions for representational and computational complexity OoD (Eqs. 2 and 4), attempting to make the central concept analytically precise rather than relying solely on intuition.

## Weaknesses

### Fatal

None.

### Major

- **The formalization of "representational complexity" using K(x) conflates description complexity of data with task-relevant difficulty, which is the very phenomenon the paper aims to capture.** Equation 2 defines representational complexity OoD as K(x_test) > max K(x_train), but K(x) measures the shortest program that outputs x — a random noise image has extremely high K(x) while being trivially classified, and a simple-looking input (e.g., a small integer requiring prime factorization) has low K(x) despite requiring deep computation. The paper acknowledges that K is uncomputable and calls it a "useful theoretical lens," but the mismatch is conceptual, not merely practical: the definition categorizes random noise as maximally OoD and misses genuinely hard-but-simple-looking inputs. The paper also needs K(y|x) for computational complexity, and the treatment of these two as "two sides of the same coin" (lines 133-136) papers over the fact that they can diverge dramatically. Since the formalization is the paper's primary analytical apparatus for distinguishing "complexity OoD" from other categories, this imprecision weakens the core argument.

- **The distinction between "complexity OoD" and existing compositional generalization categories (particularly productivity) is not sufficiently established.** The paper argues that complexity OoD differs from productivity because complexity ≠ input/output length, citing √3 being harder than √16 despite shorter length. But this observation — that computational depth can exceed surface length — is already understood within the productivity literature and does not by itself constitute a new category. The paper does not demonstrate that "complexity OoD" predicts different failure modes, implies different solutions, or reveals anything beyond what a richer notion of productivity (accounting for depth) would capture. Since the paper's novelty is claimed to rest on this distinction, the failure to differentiate it more sharply from existing categories undermines the framing's analytical contribution.

- **The proposed program synthesis framework (Section 2.1) and System-1/System-2 interaction model (Section 3) are too underspecified to generate new predictions or distinguish the position from surveyed approaches.** The framework defines programs as sequences of atomic units and says finding correct programs is search, but provides no specification of what atomic units look like, how search should be structured, or how System-1/System-2 interaction should work beyond vague "learning." Sections 3.1–3.2 describe starting with one-unit programs and scaling up (essentially curriculum learning) and using System-1 heuristics to guide search, but these ideas predate and are implemented by the surveyed work (DreamCoder, ToT, AlphaCode). The position risks reducing to "existing approaches that search over compositional structures are doing System-2," which is descriptively true but analytically thin.

### Minor

- **The alternative views section (Section 6) is incomplete and its engagement with counterarguments is shallow.** The section ends mid-sentence ("do not rely on the same principles as those used to address"), and the two alternative views presented (independence of learning/reasoning, and that reasoning is not just harder OoD) are described at a high level without substantive rebuttal. For a position paper, engaging meaningfully with the strongest counterarguments — particularly that reasoning might require fundamentally different architectures, not just search over neural units — is essential.

- **The paper straddles the line between a position paper and a survey.** Sections 4 and much of 5 read primarily as literature review with light editorializing. A position paper with this framing would benefit from a shorter survey section and more pages developing the analytical framework's novel implications (e.g., what new failure modes does complexity OoD predict? what methods does it motivate that aren't already being pursued?).

### Trivial

None.

## Nice-to-Haves

- A concrete illustration (even a thought experiment or toy example, not necessarily an experiment) showing that a method handling compositional OoD fails on computational complexity OoD would significantly strengthen the claim that complexity OoD carves nature at a meaningful joint.
- Discussion of practically measurable approximations to Kolmogorov complexity that could guide benchmark or method design, given that K is uncomputable.
- A deeper analysis of the interaction between representational and computational complexity (when do they align vs. diverge, and what methods does each case demand?) beyond the claim that they are "two sides of the same coin."

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The claim that infinite data scaling cannot handle complexity (lines 56-59) is unsupported and contentious."** The claim is logically argued: for any finite training distribution, higher-complexity instances always exist beyond it. This is a reasonable position claim for a position paper. Also, "infinite data" in learnability theory is a different notion from "infinite samples from a fixed distribution" — the paper's point about complexity escalating beyond any distribution's support is coherent even under standard learning theory.

- **"The program synthesis framework is essentially DreamCoder's wake-sleep without citation."** The paper does cite DreamCoder (Section 4.2). That the framework resembles DreamCoder is a valid observation about novelty, not a missing citation.

- **"Overclaiming — the title and framing are too provocative."** Position papers are allowed provocative language. The title states the paper's position clearly.

- **"Lack of empirical evidence/experiments."** This is a position paper arguing from reasoning and conceptual analysis. Empirical results are not required.

- **"Section 6 is cut off."** This is a parser artifact. However, the incomplete engagement with alternative views is a legitimate minor weakness noted above.

- **"The condition K(x_test) > max K(x_train) is vacuously satisfied for any finite training set."** While technically true in the strictest sense, the paper uses ">" to mean "significantly greater than" and is using K as a conceptual lens. This is a minor imprecision, not a fatal flaw in a position paper's informal definition.

- **Strength removed: "The topic is clearly of contemporary interest."** Too generic — every reasonable position paper at NeurIPS addresses a topic of interest.

## Novel Insights

The paper's most interesting conceptual contribution is the recognition that both variable-length representation and variable-length computation are needed for System-2, and its organization of existing work along these two axes. However, the analytical payoff of the "complexity OoD" framing over a richer notion of compositional generalization remains underdeveloped — the paper doesn't show what new predictions, failure modes, or methods this lens uniquely motivates.

## Suggestions

- Strengthen the distinction between complexity OoD and productivity by identifying at least one concrete failure mode or prediction that follows from the complexity lens but not from productivity. A toy example or formal argument showing divergent implications would suffice.
- Replace or supplement K(x) with a complexity measure that better captures task difficulty for the formal definition (e.g., circuit complexity, input-output complexity, or a discussion of how computational complexity K(y|x) is the more relevant measure and why both are nonetheless needed).
- Either substantially expand Section 6 to include genuine engagement with and rebuttals of alternative views, or integrate counterarguments throughout the paper rather than relegating them to an incomplete final section.

## Score and Decision

**Comparison with calibration anchors:**

- **Low band (avg ≤ 4):** The R6TXwNF1SB paper (avg 3.0) about six pillars of AGI was criticized for vague, undefined terms, a muddled argument serving primarily as a survey summary, and no novel perspective. The 8Ow7kh78fk paper (avg 2.33) had no clear position and used buzzwords without explanation. Our paper is clearly stronger than both — it has an explicit position, attempts formal grounding, and provides a useful organizational framework.

- **Medium band (avg ~5):** The a9eBWrd5Jg paper (avg 5.0) on systematic compositionality had a sharper thesis backed by empirical evidence (re-running Lake & Baroni). Our paper lacks comparable empirical support but has a broader scope and formalization attempt. The ZOUHFrCmwu paper (avg 5.33) on neuro-symbolic prompting was clearly argued with some experimental evidence but was criticized for lacking a roadmap and conflating terms. Our paper is in a similar range — clear position but underspecified framework.

- **High band (avg ≥ 6):** The yqKfMr0yvY paper (avg 7.67) on LLM-as-judge drew on mature measurement theory for a rigorous, well-organized critique. The BXLRMWLDQw paper (avg 6.33) on adversarial ML provided a tabular framework and six detailed case studies grounding abstract claims. Our paper is noticeably weaker than these — its formal grounding is flawed, its central concept is not clearly differentiated from existing categories, and its framework is underspecified.

Our paper sits between the low and medium bands. It has a genuine position and formalization attempt, but the formalization has real conceptual issues, the central concept is not clearly distinguished from existing categories, and the framework is too vague to generate novel predictions. It's comparable to or slightly below the 5.0 papers in the dataset.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>