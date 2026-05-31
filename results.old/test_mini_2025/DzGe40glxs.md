Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper provides the first mechanistic evidence that a model-free RL agent (a DRC agent playing Sokoban) internally plans. Using concept-based interpretability, the authors: (1) train linear probes showing the agent represents future-directed concepts of agent movement (C_A) and box pushing (C_B) with high fidelity (macro F1 > 0.8); (2) provide qualitative evidence that these representations form iterative, bidirectional plans; and (3) causally intervene on these representations to steer the agent's long-term behavior with high success rates (e.g., 94.6% for Agent-Shortcut vs. 33.7% for random probes). They further show that the emergence of these representations during training correlates with the emergence of planning-like behavior (benefit from extra test-time compute).

## Strengths

- **Systematic three-step methodology for detecting internal planning (Sections 3.1, 4, 5, 6):** The paper defines a reusable template — probe for concepts, investigate plan formation, confirm causal behavioral influence — and executes each step with concrete experiments. This goes beyond purely behavioral tests and provides a framework applicable to other agents.

- **High-fidelity linear concept probes with meaningful controls (Section 4.2, Figure 4):** 1×1 linear probes achieve macro F1 > 0.8 for both C_A and C_B across all layers, vastly outperforming the input-observation baseline (F1 0.25–0.6). The minimal improvement from 1×1 to 3×3 probes (vs. large baseline improvement) confirms spatial locality — the concepts are represented at individual grid positions in the ConvLSTM cell states.

- **Causal interventions demonstrate behavioral influence and rule out pure correlation (Section 6.1, Table 1):** Adding learned probe vectors to the agent's cell state steers the agent to execute specific alternate plans (e.g., 94.6% success vs. 27.8–33.7% for random probes of matched norm). The controlled random-probe baseline is critical: it shows that the steering effect is not merely from perturbing activations but depends on the specific semantic content of the probe directions.

- **Emergence analysis ties representational and behavioral evidence (Section 6.2, Figure 9):** The strong positive correlation between probe F1 and the benefit from extra test-time compute across training checkpoints links the internal representations to the agent's behavioral signature of planning, supporting that these representations are functionally used.

## Weaknesses

### Fatal
None.

### Major

1. **Evidence for the "evaluation" condition (condition ii from Section 2.1) is substantially weaker than for the other two conditions.** The paper characterizes planning as requiring an agent to (i) form plans, (ii) *evaluate* plans by predicting their consequences, and (iii) be influenced by plans when acting. Conditions (i) and (iii) are convincingly supported by probing and interventions. But the evidence for evaluation is entirely qualitative: Figure 1(A)–(B) shows cases where "the agent appears to (1) formulate a naive plan, (2) evaluate it, and then (3) adapt its plan accordingly." As the paper itself acknowledges with "appears to," these are visual interpretations of decoded probe outputs, not controlled tests. An alternative explanation consistent with the data is that the agent's recurrent processing iteratively converges to a better solution without any explicit evaluation step — the plan refinement seen in Figure 6 could reflect uncertainty resolution through additional computation rather than consequence evaluation. **Why this matters:** The paper defines planning in terms of all three conditions but only provides rigorous evidence for two. The claim is not invalidated, but the characterization should either be revised to match the evidence or supplemented with an experiment (e.g., presenting the agent with a fork between a dead-end plan and a viable one and measuring whether it consistently avoids the dead-end *before* executing actions).

2. **The "parallelized bidirectional search" claim (Abstract, Section 5) is overclaimed relative to the evidence.** The paper states the agent "learns a planning algorithm resembling parallelized bidirectional search" in the abstract and discusses forward-from-boxes / backward-from-targets search in Section 5. However, the evidence is entirely qualitative — Figure 1 panels (C)–(E) show examples that are consistent with bidirectional search but not systematically evaluated. The paper does not quantify how often plan extensions originate from boxes vs. targets across episodes, how many branches grow in parallel, or whether the decoded patterns are distinguishable from a forward-only search that *appears* bidirectional when decoded. **Why this matters:** The term implies a specific algorithmic structure that carries strong connotations (efficiency guarantees, systematicity). The paper's core contribution (that the agent plans at all) does not depend on this claim, and it risks misleading readers about the precision of the findings.

3. **The probing baseline does not adequately control for the agent's access to temporal history.** The baseline (Section 4.1) is a linear probe on the raw observation \(x_t\). The cell state has access to the full trajectory history via the recurrent architecture, while the raw observation does not. The high probe accuracy could partially reflect the agent's ability to predict its own future actions from its current internal state (which *must* encode upcoming policy outputs) rather than indicating a distinct "planning" representation. The paper partially addresses this by showing that macro F1 improves with additional ticks (Figure 6), suggesting refinement rather than simple readout. Nevertheless, a stronger baseline — e.g., a linear probe on a concatenation of recent observations, or on the hidden state of a simpler recurrent model without ConvLSTM structure — would substantially strengthen the claim that these are planning representations specifically rather than generic action-prediction features.

### Minor

4. **The emergence analysis (Section 6.2, Figure 9) is correlational and the paper's causal language should be tempered.** The text says "the emergence of these representations during training coincides with the agent beginning to exhibit planning-like behavior" and "this implies the agent only reliably begins to exhibit planning-like behavior once its representations are sufficiently formed." Both are true as stated, but the paper's framing could be read as implying a causal relationship where the representations *enable* planning. A third factor (e.g., improved policy optimization or value function learning) could drive both the emergence of probe-predictable representations and the ability to benefit from test-time compute. The authors should explicitly acknowledge this limitation.

5. **The "thinking steps" experiment (Figure 6) assumes probe generalization to an unusual regime without verification.** The probes were trained on data from normal episodes with 3 ticks per step. In the thinking-steps experiment, the agent is forced into 15 extra ticks. It is not verified that the probes generalize to this unusual regime where the agent's internal states may be statistically different from those seen during training. If probe accuracy degrades in this regime, the improvement in macro F1 with ticks could partially reflect changing distributional alignment rather than genuine plan improvement.

6. **Discussion of alternative interpretations is absent.** The paper does not explicitly address counterarguments such as: "the agent is not planning; it has simply learned a policy whose intermediate features happen to predict future actions, and the intervention perturbs those features." While the causal intervention results (Section 6.1) provide strong implicit evidence against this, an explicit discussion of what would constitute disconfirming evidence would strengthen the paper.

7. **Box-Shortcut intervention success rates are substantially lower (56.2–80.6%) and more variable across layers than Agent-Shortcut rates (90.1–98.8%).** Layer 1 achieves only 56.2% for Box-Shortcut, close to the random probe baseline (31.5% with high variance). The paper could discuss why — possible explanations (e.g., layer 1 probes for C_B being less reliable, or the intervention being harder to apply) would help readers assess the robustness of the causal evidence for the box-pushing concept.

### Trivial
None.

## Nice-to-Haves

- **Add an ablation that removes plan information** (e.g., zeroing cell-state channels at positions where C_A or C_B is encoded) to test whether these representations are causally *necessary* for performance, complementing the sufficiency-style additions in Section 6.1.
- **Probe the agent's plan at each tick within normal (non-thinking) steps** to study how plans evolve during ordinary step transitions.
- **Report confidence intervals for the random-probe baselines** to quantify the robustness of the intervention effect, especially given the high standard deviations (e.g., 32.7–37.9% for Agent-Shortcut).

## Removed Points

The following points from the input reviews were removed with brief justification:

- **"The definition of planning could be tightened" (Harsh Critic Section 2):** Vague, not a specific actionable weakness.
- **"Appendices should be available for review" / "The reader must trust the appendices":** Parser strips appendices from all papers; these sections exist in the original submission. Not a paper weakness.
- **"The paper does not return to this characterization precisely in the results":** The paper does return to the characterization (Section 5 explicitly references the three conditions), though the evidence is uneven — this is already captured in Major Weakness #1.
- **"Concept selection assumes square-level planning; agent might plan at higher abstractions":** Reasonable in principle but the paper acknowledges these are *hypothesized* concepts (Section 3.2). Every probing study must specify a concept vocabulary; this is not a flaw unless the probes fail (they succeed).
- **"Performance similar across layers is under-analyzed":** Nice-to-have additional experiment, not a weakness.
- **Strength Finder claims about OOD generalization:** These examples are in the appendix and are presented as qualitative demonstrations; they are supportive but not central to the core claim.
- **Any references to missing proofs, broken references, missing appendix content:** Parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely recapitulate and organize the paper's content without identifying genuinely novel cross-connections or methodological insights that the paper itself does not make. The single exception is the observation that the "evaluation" condition gap mirrors a common pattern in interpretability work (showing representation + causal influence is easier than showing a distinct evaluation step) — but this is implicit in the paper's framing already.

## Suggestions

1. **Revise the planning characterization or add an evaluation experiment.** Either (a) design a controlled fork task where the agent's current plan leads to a dead end and measure whether it revises the plan before acting, or (b) revise the characterization to treat iterative plan refinement (already demonstrated in Figures 1 and 6) as sufficient evidence of evaluation, and explicitly note this revision.

2. **Temper the bidirectional search claim.** Replace "parallelized bidirectional search" with more precise language such as "qualitative resemblance to bidirectional search" or "a search process that exhibits forward-from-boxes and backward-from-targets patterns." The core contribution (that the agent plans) does not require this stronger characterization.

3. **Strengthen the probing baseline.** Add a baseline that uses a temporally-aware input representation (e.g., concatenation of the last 3–5 observations, or features from a simple recurrent network) to better isolate what the cell state's planning representations add beyond action prediction from temporal context.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Weak anchors (score < 3.5) on related RL/planning topics returned papers at 2.50–3.25 (rejects). Middle anchors (3.5–7.5) returned several papers including the most topically similar — "Understanding and Controlling a Maze-Solving Policy Network" (avg 3.67, rejected) — and accepted papers like "UTILITY" (avg 7.00, poster) and "Distilling RL for In-Context Planning" (avg 6.67, poster). Strong anchors (7.5+) returned oral papers at 8–10 from LLM interpretability and neuroscience (less topically relevant).

The paper under review is clearly stronger than the maze-solving paper (3.67): that paper had unconvincing interventions, narrow scope, and F1 scores barely above baseline. It sits in the 5.5–7.5 range.

**Round 2 (Narrowing):** Search within (4.5, 6.5) and (6.0, 8.0) returned:
- "Emergent Symbol-Like Number Variables" (4.75, rejected): Similar probing + intervention methodology but on a simpler task with shallower contribution. Current paper is substantially stronger (more complex domain, more rigorous interventions, more significant findings).
- "Towards Unifying Interpretability and Control" (5.25, rejected): Incomplete experiments, unclear contribution. Current paper is more complete and better executed.
- "Distilling RL for In-Context Planning" (6.67, accepted poster): Well-executed but some reviewers questioned the significance of improvements. Current paper has a more novel contribution (first mechanistic evidence vs. an incremental method improvement).
- "Modeling Unseen Environments" (6.00, accepted): Different area but comparable experimental rigor.

**Final score placement:** The paper is better than the 4.75 and 5.25 anchors, comparable to 6.67–7.00 accepted papers, with a more novel contribution than DICP (6.67) and cleaner evidence than UTILITY (7.00, which had significant theoretical concerns). However, the three major weaknesses (evaluation gap, overclaimed search algorithm, weak probing baseline) prevent it from reaching the 8+ range. Score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>