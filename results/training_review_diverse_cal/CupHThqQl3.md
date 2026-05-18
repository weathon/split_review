Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper provides the first systematic study of temporal references in emergent communication. The authors propose a sequential LSTM module that processes training episodes as a temporal sequence and develop a metric ($M_{\Theta^n}$) to measure whether messages are used consistently as "previous" operators. Through experiments in temporal referential games, they show that the sequential LSTM architecture alone is sufficient for agents to develop messages that function as temporal references (e.g., "same as four steps ago"), without requiring an explicit temporal prediction loss.

## Strengths

1. **First systematic study of temporal references in emergent communication.** The paper addresses a genuine gap — prior work (e.g., Kang et al. 2020) considered temporal relationships for communication efficiency but not the emergence of temporal vocabulary itself. This is stated in the Abstract and Introduction and is well-motivated.

2. **Clean experimental demonstration that a sequential LSTM is sufficient.** Results in Section 3.3 (Figure 2a, Table 1) show a stark contrast: only architectures with the sequential LSTM (Temporal and Temporal-NL) reach $M_{\Theta^4}=100\%$, while Non-Temporal and Non-Temporal-NL never do. Critically, Temporal-NL (no temporal prediction loss) also achieves temporal references in over 95% of runs, cleanly decoupling the architectural change from the auxiliary loss.

3. **Well-defined, transferable metric.** The $M_{\Theta^n}$ metric (Section 3.1) is formally defined with clear examples. The 100% threshold avoids false positives from chance repetitions, making the metric adoptable by future work.

4. **Robust evaluation design.** The paper evaluates across six environments (Always Same, Never Same, RG Classic, RG Hard, TRG Previous, TRG Hard) with 10 seeds each, and includes a scaling analysis (Figure 3b) showing temporal usage increases with repetition probability as expected, ruling out dataset artifacts.

5. **Architectural simplicity.** The sequential LSTM is a minimal change to standard architectures (Kharitonov et al., 2019). The paper explicitly notes (Section 2.4) that this requires no reward shaping or game-specific modifications, making the insight readily transferable.

## Weaknesses

### Fatal
None.

### Major

1. **Missing explicit statement about temporal ordering in batches.** This is the most significant weakness. The sequential LSTM receives shape `[1, batch_size, num_attributes]` and processes the 128 episodes within a batch as a sequence. The paper never states whether these 128 episodes are in chronological order (i.e., consecutive episodes from the environment's temporal stream) or shuffled. In the TRG environment, episodes have genuine temporal dependencies (objects repeat from $h_v$ episodes ago), and the sequential LSTM can only exploit these if batch order matches episode order. The paper must clarify: (a) whether chronological order is preserved within and across batches, (b) if so, how this was done, and (c) whether evaluation also maintains this ordering. The results are coherent enough that temporal order was almost certainly preserved, but the omission makes this a clarity gap that a reader cannot resolve from the text alone.

2. **Missing hyperparameter details prevent full reproducibility.** The paper does not report the actual experimental values (as opposed to illustrative examples) for several critical parameters: $N_{att}$ (number of attributes), $N_{val}$ (values per attribute), $N_{vocab}$ (vocabulary size), $L$ (maximum message length), $h$ (previous horizon hyperparameter), learning rate, optimizer, training duration (number of episodes/epochs), and whether any form of regularization was used. Section 2.4 gives $N_{att}=6$ and `batch_size=128` as an example but does not confirm these are the experimental values. Without these details, other researchers cannot replicate the experiments or assess the scale and difficulty of the task. Some of these may have been in an appendix stripped during parsing, but the paper does not reference one.

### Minor

3. **Metric and analysis focus on a single horizon ($n=4$).** The environment samples $h_v$ uniformly from $\{1,\dots,h\}$, meaning repetitions can occur at any horizon. The paper reports $M_{\Theta^4}$ throughout, which only captures messages used when $h_v=4$ exactly. Agents might develop temporal references at other horizons (e.g., a generic "same as before" message used for any $h_v$) that this metric would miss. The paper should either: (a) report $M_{\Theta^n}$ for multiple values of $n$, (b) state that $h=4$ in experiments (if that is the case), or (c) provide a multi-horizon aggregate metric. The core claim (sequential LSTM enables temporal references) still holds, but the breadth of the finding is unclear.

4. **Hard evaluation environments defined but not shown in main results.** Section 2.3 defines "TRG Hard" and "RG Hard" — variants where target and distractors differ by only one attribute. Section 3.2 confirms agents were evaluated in all six environments, but Figures 2–3 only show "TRG Previous" and "RG Classic" (plus Always/Never Same). The hard variants are arguably where temporal references could provide the largest benefit, and omitting them from the main figures weakens the empirical support for the claim that temporal references improve performance under difficult discrimination.

5. **Temporal prediction layer status in Temporal-NL is underspecified.** The paper defines Temporal-NL as including the sequential LSTM but not the temporal prediction *loss*. However, the architecture description (Section 2.4) includes a temporal prediction *layer* as a component. It is unclear whether this layer is removed in Temporal-NL or left in place with its loss term zeroed out. If the layer remains but produces no gradient, it should not affect the forward pass of the referential game (since the layer output is a side branch), but the paper should state this explicitly to avoid confounding the ablation.

6. **Overclaim on generalisability.** The Introduction claims "our findings are more generalisable and transferable to other settings," and Section 2 states the simple architecture makes findings "more generalisable." The experiments are limited to attribute-vector referential games. While the architectural insight is indeed plausibly transferable, the paper has not demonstrated transfer to different object types (e.g., images), different game variants, or multi-agent settings. This claim should be tempered to match the actual scope of the experiments.

### Trivial
None.

## Nice-to-Haves
- Cross-environment analysis showing that messages achieving $M_{\Theta^4}=100\%$ in repetition-heavy environments are never used in "Never Same" — the paper shows $M_{\Theta^4}=0$ for "Never Same" but does not trace individual messages across environments.
- Ablation separating the sender's sequential LSTM from the receiver's sequential LSTM to see if one alone suffices.
- Confidence intervals or statistical significance tests for the percentages in Table 1 (the paper reports 10 runs, and the 3% non-convergence for Temporal variants suggests some variance).
- Clarifying whether the "previous horizon" hyperparameter $h$ was set to match or exceed $n=4$, and whether the metric was computed for all encountered horizons or only $n=4$.

## Removed Points
- **Harsh Critic's framing of Point 1 as potentially fatal/collapsing the paper's central claim:** Removed because the most natural interpretation of the results (that temporal order is preserved in batches) is coherent with the experimental design. The concern is a genuine clarity gap, not an error that invalidates the findings. The paper should clarify but does not need to be redesigned.
- **"The paper does not provide cross-environment analysis for Never Same":** Downgraded to Nice-to-Have. The paper already shows $M_{\Theta^4}=0$ for "Never Same" (Figure 2a), which is the expected result. The requested analysis would be a useful additional validation but is not a weakness of the existing presentation.
- **Criticism about missing statistical significance for Table 1:** Downgraded to Nice-to-Have. The core result (0% vs >95%) is so stark that confidence intervals would add little.
- **Formatting nitpicks / typos:** Removed per rules — these are parser artifacts.

## Novel Insights
The most interesting synthetic insight from reading the reviews alongside the paper is that the paper demonstrates a "minimal architecture" principle for emergent linguistic phenomena: a single architectural feature (sequential LSTM) is sufficient for temporal reference emergence, without any explicit reward shaping or auxiliary loss. This is stronger than what one might expect — one would intuitively think that agents need an explicit reason to talk about time. The paper shows they don't; they just need the ability to remember and reference the past. This is analogous to findings in compositional emergence where certain architectural biases (e.g., disentangled representations) can lead to compositional language without explicit compositionality pressure. The parallel suggests a broader principle: in emergent communication, architecture may be a more powerful lever than reward design.

## Suggestions
1. **Add an explicit statement** about batch construction — whether temporal order is preserved within batches, whether batches are consecutive episodes from the environment stream, and whether evaluation maintains this ordering. This is the single most important clarification.
2. **Include a hyperparameter table** with all experimental values ($N_{att}$, $N_{val}$, $N_{vocab}$, $L$, $h$, learning rate, optimizer, training duration, batch size).
3. **Report $M_{\Theta^n}$ for multiple horizons** (or state that $h=4$ in experiments if that is the case).
4. **Move the "Hard" environment results** into the main figures, or explain why they were omitted.
5. **Clarify the temporal prediction layer status** in Temporal-NL (removed, frozen, or present but unused for the forward pass).
6. **Temper the generalisability claim** in the introduction and conclusion to match the scope of the experiments.

## Score and Decision

The paper makes a genuinely novel contribution — the first demonstration of temporal references emerging in EC — and the core experimental comparison is clean and persuasive. However, the missing experimental details (temporal ordering in batches, hyperparameters) are significant barriers to reproducibility and full evaluation. The paper requires non-trivial clarification that cannot be fully resolved in the review period (the batch-ordering detail affects how readers interpret the entire experimental setup). With revision, this could be a solid paper, but in its current form the presentation gaps are too large.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>