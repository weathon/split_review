Now I have a solid understanding of the paper. Let me write my final review.

## Summary

The paper argues that machine learning researchers should develop models that learn to interact with and control in vitro biological neural networks (derived from iPSCs), framing this as both an engineering challenge and a pathway to understanding neural computation. Its central claim is that learning to control in vitro systems provides a "practical method of arbitration" for distinguishing genuine computational principles from spurious patterns—an epistemic advantage over passive data analysis — since the ability to steer neural activity toward desired states provides an objective measure of model quality. The paper outlines an RL-based formalization, discusses optimization approaches (including simulation pretraining and surrogate gradients), identifies counterarguments about AI relevance and technical readiness, and speculates on longer-term implications including energy-efficient AI inspired by biological "mortality."

## Strengths

- **Novel and timely reframing of neural computation validation as a control problem.** The paper's most distinctive contribution is reframing what "testing neural computation" means: rather than passively analyzing neural data (which Jonas & Kording (2017) showed fails to reveal computational principles even for known systems), the authors argue control provides an objective method of arbitration. This is a genuinely interesting epistemic move that transforms a philosophical impasse into a tractable optimization problem (Section 1.2).

- **Concrete formalization that makes the position actionable for the ML community.** Section 3.1 provides an RL-style problem formulation (IVN as stochastic transition function, policy π_θ) and Section 3.2 specifies concrete engineering constraints (e.g., a single MNIST epoch at 500ms/image requires ~7 hours of recording, sub-millisecond latency constraints requiring FPGAs). This converts the high-level vision into a framework ML researchers can actually work with, and the insight that "ideally, as t→∞, the artificial policy should approximate the identity function" (meaning the IVN itself has been reconfigured to solve the task) provides a compelling knowledge-distillation analogy.

- **Thoughtful engagement with counterarguments.** Section 4 addresses three substantive objections (in vitro won't help AI, the technology isn't ready, ethics of engineering living neurons), presenting each fairly before responding. The ethics discussion in particular acknowledges unresolved questions about consciousness and donor consent rather than dismissing them.

- **Effective interdisciplinary synthesis.** The paper integrates developments across iPSC-derived organoids, MEAs, optogenetics, RL methodology, surrogate gradients, differentiable simulation, and philosophy of science (Lazebnik 2004, Jonas & Kording 2017), making a credible case for convergence that has not been well-articulated to the NeurIPS community.

## Weaknesses

### Major

- **The core epistemic link between "successful control" and "understanding computation" is asserted rather than argued.** This is the paper's most significant gap. The position is titled "test neural computation in vitro," but the methodology pursued is learning to control in vitro systems via RL optimization. The paper asserts that "the discovery of control strategies can imply an implicit discovery of the working principles of the biological system" (Section 3.1), but this is precisely where argumentation is needed, not assertion. The paper raises the microprocessor analogy (Jonas & Koding 2017) showing that even perfect predictive models fail to reveal computational principles — which actually suggests that mere control is an even weaker epistemic tool than prediction. This is acknowledged in Section 3.2's admission that "task-solving abilities are, first and foremost, a measure of system control rather than the end goal," but the paper never explains *what mechanism* bridges the gap from successful control to computational understanding. The reservoir computing possibility is raised but dismissed with "a more sophisticated model, however, may learn to exploit more intricate properties" (Section 3.1), which is a hope rather than an argument.

- **The counterargument response (Section 4.1) is underdeveloped.** The strongest objection — that decades of neuroscience have not meaningfully influenced AI architectures — is met with: "The historical divergence between neuroscience and AI development should not preclude future convergence, especially as both fields continue to mature and evolve." This is a platitude, not an argument. The paper provides no reasoning for why in vitro systems specifically would succeed where in vivo neuroscience has failed to influence AI. A position paper's strength depends on how well it handles its strongest counterarguments, and this one is handled with optimism rather than substance.

### Minor

- **Conflation of two distinct goals that require different justification.** The paper oscillates between (1) "testing neural computation" (an epistemic goal) and (2) "engineering useful living neural systems" (a practical goal, Section 1.2 title). These are importantly different: successfully steering neural activity toward desired states (goal 2) does not necessarily validate any theory of how the system computes (goal 1). The paper would be stronger if it separated these goals and argued for each on its own terms.

- **The "why now" argument is primarily technological rather than methodological.** The paper argues iPSC and MEA technologies have matured, but the ML-specific methodological case is weaker. Many relevant ML capabilities (model-based RL, differentiable simulation) are not new, and the paper doesn't identify what specific recent ML innovations uniquely enable this research direction now.

### Trivial

None.

## Nice-to-Haves

- A concrete account of *how* control yields computational understanding — e.g., what kinds of interventions or experimental designs would allow a researcher to go beyond "we can steer this system" to "we understand how this system computes." The virtuous cycle described in Section 1.2 is sketched but not elaborated.
- Engagement with the reservoir computing concern: under what conditions would the research program converge on learning something non-trivial about neural computation, as opposed to treating the IVN as a black-box reservoir?

## Removed Points

- **Harsh critic's claim that the "control as arbitration" argument is "underdeveloped" is partially valid but should not be treated as Fatal.** The paper does provide a concrete argument: control provides an objective function for model quality (steering toward desired states), which is more than no arbitration at all. The criticism is that this doesn't bridge to *computational understanding*, which is valid and kept as Major, but the arbitration frame itself is not vacuous — it provides a necessary (though not sufficient) condition.

- **Harsh critic's claim that the microprocessor analogy "actually cuts against the paper's position."** This is overstated. The paper explicitly uses the microprocessor example to motivate the need for *some* arbitration beyond passive analysis, and then argues control provides that arbitration. The fact that prediction alone (the microprocessor paper's approach) wasn't enough doesn't mean control also isn't enough — these are different epistemic strategies. The analogy cuts against the paper only if one conflates prediction and control, which the paper specifically distinguishes.

- **Harsh critic's claim that empirical results are absent/minimal.** This is a position paper, not an empirical contribution. Removed per rules.

- **Harsh critic's demand for "evidence that sim-to-real transfer is feasible."** The paper acknowledges this challenge explicitly (Section 3.2-3.3) and proposes it as a research direction. Demanding feasibility evidence from a position paper advocating for a future research direction is scope creep.

- **Harsh critic's claim that the paper conflates "testing neural computation" with "learning to control."** This is kept as a Minor weakness (the two goals need different justification), but should not be Fatal because the paper does explicitly connect them through the "arbitration via control" argument, even if that argument is incomplete.

- **Strength Finder's claim about "grounding in practical engineering realities" as a strength.** This is valid and kept — the concrete engineering constraints (7-hour MNIST epoch, sub-millisecond latency, FPGA requirements) genuinely strengthen the paper.

- **Harsh critic's point about reproducibility and variability of in vitro preparations.** This is a valid concern but the paper does acknowledge cultural variability issues implicitly via references to maintenance challenges and the need for cloud providers. Moved to Minor but it is partially addressed.

## Novel Insights

The paper's most novel insight is the reframing of passive computational neuroscience (analyze neural data to understand computation) into an active control problem (learn to interact with in vitro systems to test whether you understand them). The epistemic argument that control provides a "method of arbitration" between competing models — that successful manipulation of a system is a stronger test of understanding than mere prediction — is philosophically interesting and connects to embodied/enactive cognition traditions in a way the paper could leverage further. The knowledge-distillation analogy (where the IVN gradually takes over from the artificial policy) is also an original and productive framing for this domain.

## Suggestions

- Develop the "arbitration through control" argument beyond assertion: specify what kinds of controlled experiments would allow researchers to go from "we can control this system" to "we understand how it computes." Even a rough taxonomy of control → understanding pathways would transform this from a compelling vision into a compelling argument.

- In Section 4.1, replace the platitude about convergence with a concrete argument about what specific properties of in vitro systems (as opposed to in vivo neuroscience) could make them more productive for AI-relevant insights: e.g., the ability to perform arbitrary causal interventions, the reduced complexity of organoid systems, or the possibility of closed-loop optimization.

- Separate the paper's two goals (understanding computation vs. engineering useful systems) clearly, even if both are argued for. This would allow each to stand on its own merits rather than appearing to lean on each other for support.

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Comparison |
|-------|-----------|------------|
| VZnOKzQ5qW (Brain-Agent Collaboration) | 7.33 | More concrete empirical basis, clearer paradigm extension, argued better. This paper is below it. |
| HzGZVYi8fK (BIML — Biology-Informed ML) | 6.33 | Similar interdisciplinary synthesis, clear position, four pillars roadmap. This paper is comparable but slightly weaker due to the core argument gap. |
| 8ZH52QHIZV (XAI → Domain Authority Negotiation) | 5.33 | Has a similar pattern: ambitious reframing with underspecified practical bridge. Paper under review is above this. |
| R6TXwNF1SB (Pillars of Generalization) | 3.00 | Vague terminology, muddled argumentation. This paper is clearly above this. |
| 8Ow7kh78fk (AGI via LLM+Logic+Blockchain) | 2.33 | No clear position, buzzword-heavy, extreme gap between claims and content. This paper is far above this. |
| xnNHXepQ9h (Adaptive Sensing) | 5.33 | Interesting paradigm shift proposal, somewhat underdeveloped. Comparable range. |

The paper identifies a genuinely timely opportunity at the intersection of ML and in vitro neuroscience, takes a clear position, and provides a thoughtful formalization. Its main weakness — the unbridged gap between "successful control" and "understanding computation" — is substantive but does not make the paper incoherent; it makes the position incompletely argued rather than wrong. This is a meaningful gap in a position paper whose central claim rests on this link, but it is not fatal because the paper's other contributions (the reframing, the formalization, the counterargument section) are genuine. The paper sits in the 5.5–6.5 range, above papers with purely underspecified frameworks (XAI DAN at 5.33) but below papers with more complete argumentation (BIML at 6.33). The core argument gap pulls it down to the lower end of that range.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>