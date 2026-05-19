- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces a new architectural modification—a sequential LSTM that processes observations across episodes in a referential game—and demonstrates that it enables the emergence of temporal references (messages that indicate "same as n steps ago") in emergent communication. The authors show that agents with this sequential LSTM develop messages reaching 100% on their M_⊙^n metric in >95% of runs, while standard architectures never do. Crucially, Temporal-NL agents (sequential LSTM without an explicit temporal prediction loss) also succeed, showing the architectural change alone is sufficient. This is the first reported temporal vocabulary in the emergent communication literature.

## Strengths

1. **First demonstration of temporal vocabulary in emergent communication.** Section 3.3 and Table 1 provide quantitative evidence that agents with a sequential LSTM develop messages reaching 100% on the M_⊙^4 metric. This is a genuinely novel finding—no prior work has shown agents forming dedicated temporal reference markers in a referential game.

2. **Architectural change alone is sufficient (no explicit loss needed).** The Temporal-NL condition (sequential LSTM without temporal prediction loss) produces temporal references in >95% of runs, while Non-Temporal-NL agents never do (Figure 2a, Table 1). This cleanly isolates the sequential LSTM as the causal factor, supporting the core claim that "no additional losses are necessary."

3. **Figure 3b controls for the object-consistency confound.** The critic's concern that the metric may conflate temporal referencing with consistent object-level naming is directly addressed by Figure 3b: for Temporal/Temporal-NL agents, M_⊙^4 reaches 100% regardless of the dataset repetition chance p, while for Non-Temporal agents it scales linearly with p. If temporal messages were just object-consistent naming, they would also scale with p. This is a strong control that validates the metric.

4. **Qualitative evidence shows temporal messages generalize across distinct objects.** Section 3.3 provides a concrete example where the temporal message [25,6,9,3,2] was used for twelve distinct objects in the "Always Same" environment, with a different (object-describing) message used for first appearances. This confirms the messages are genuinely temporal operators, not object-specific labels.

5. **Novel metric M_⊙^n for temporal referencing.** Equations 3–6 with worked examples provide a clear, reproducible way to quantify whether a message functions as a temporal reference. This methodological contribution enables future work to adopt the same evaluation standard.

## Weaknesses

### Fatal
None.

### Major

1. **The training environment(s) are not specified, leaving a key claim unverifiable.** Section 3.2 states "All agent types were trained for the same number of epochs and on the same environments during each run" but never says which environment(s) each configuration was trained on. The paper claims "temporal references emerge in both Temporal and Temporal-NL networks, regardless of the training dataset" (Section 3.3), yet without knowing whether agents were trained on TRG (50% repetitions) or RG Classic (no repetitions), the scope of this claim is unclear. If agents were trained only on TRG and then evaluated on RG Classic, that shows transfer—not emergence in a regular environment. To support the stronger interpretation, the authors should explicitly state the training environments for each result and ideally include an experiment where agents are trained on RG Classic (no repetitions) and tested for temporal references.

2. **Aggregate quantitative results from "Always Same" and "Never Same" control environments are not reported.** Section 2.3 describes these environments specifically "to verify whether the messages that would be identified as temporal references are correctly labelled," and Section 3.2 lists them as evaluation environments. Yet no figure or table reports M_⊙^n distributions or other aggregate statistics from these controls. Only a single qualitative example from "Always Same" is given (Section 3.3). Without quantitative evidence that temporal messages are not used in "Never Same" (where no objects repeat) and are consistently used across distinct objects in "Always Same," the metric's validity remains partially unsubstantiated. The authors should report M_⊙^n for these environments for all agent types.

### Minor

3. **Overall referential accuracy (game performance) is not compared across architectures.** The introduction motivates temporal references partly through improved task performance and bandwidth efficiency ("will enhance the agent's bandwidth efficiency and task performance"). However, the paper never reports whether the Temporal architecture achieves higher overall game accuracy than Non-Temporal baselines. Figure 2b reports correctness of messages *when used as temporal references* (which is high), but this says nothing about aggregate game accuracy. The paper would be strengthened by including a table of referential accuracy for each agent type across all environments.

4. **Key hyperparameter values are omitted.** N_vocab (vocabulary size), L (maximum message length), N_att (number of attributes), N_val (number of values), and the previous horizon hyperparameter h are all defined in the formalism but never given numerical values. This makes reproduction difficult and should be addressed.

5. **The PLTL formalism adds notation without commensurate analytical payoff.** Equations (1) and (2) define the ⊖ operator, which is then used primarily as a naming convention for the metric and environment. The paper could be written more simply without the formal temporal logic and no information would be lost.

### Trivial
- The phrase "previous horizon hyperparameter" is defined but never assigned a concrete value used in experiments.

## Nice-to-Haves

- A version of the experiment where agents are trained on RG Classic (no temporal repetitions) to test whether temporal references still emerge. The paper's claim of "natural emergence without additional pressures" would be strengthened considerably.
- Confidence intervals or significance tests for the 10-run comparisons in Figure 2.
- An analysis of the number of distinct objects each temporal message is used for, aggregated across runs. The qualitative example shows 12 objects for one message; aggregate statistics would strengthen the claim that temporal messages are general-purpose operators rather than object-specific.

## Removed Points

These points from the reviews were removed or substantially weakened after verification against the paper:

- *"The metric may conflate temporal referencing with object-specific naming"* — Removed as a standalone weakness because Figure 3b directly addresses this: M_⊙^4 = 100% independent of repetition chance for Temporal agents, while Non-Temporal agents scale with p. This shows the temporal messages are not merely consistent object naming. The remaining valid kernel (missing aggregate control environment results) is retained as Major weakness #2.

- *"The sequential LSTM mechanism is underspecified"* — Removed. The paper describes the [1, 128, 6] shape and processing scheme, which is adequate for an EC paper. The hidden state persistence mechanism is standard LSTM behavior.

- *"The relationship between the two LSTMs is not ablated"* — Removed as stated; the paper actually does ablate this in Section 3.3 ("removing the Meaning LSTM... agents with just the temporal module still develop temporal references, but perform worse on the referential task").

- *"The paper should report the number of distinct objects per temporal message"* — Demoted to Nice-to-Have. The paper provides a concrete qualitative example (12 objects) which is suggestive; an aggregate statistic would strengthen but is not essential.

- *Strength about "Careful control environments to validate temporal labels" (from Strength Finder)* — Weakened. The environments are well-designed but their results are not reported quantitatively, so this strength is overstated as presented.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any fundamentally new interpretation or connection that the paper itself does not already articulate.

## Suggestions

1. Add a clear statement of which training environment(s) each agent configuration was trained on, either in Section 3.2 or as a table.
2. Report aggregate M_⊙^n statistics for the "Always Same" and "Never Same" control environments for all four agent types.
3. Include a table of overall referential accuracy (game performance) for each architecture across all six evaluation environments.
4. Report the numerical values of N_vocab, L, N_att, N_val, and h used in the experiments.
