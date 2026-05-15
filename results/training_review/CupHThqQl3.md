I have thoroughly read the paper and verified all claims against it. Let me now produce the consolidated review.

---

## Summary

This paper investigates the emergence of temporal references in emergent communication (EC) by introducing a Temporal Referential Game (TRG) where target objects repeat with 50% probability at variable past horizons. The authors propose a metric $M_{\ominus^n}$ to quantify whether a message is used exclusively to refer to a repeated object from $n$ steps ago, and compare four architectures: Temporal and Temporal-NL (both with a sequential LSTM for temporal processing) versus Non-Temporal and Non-Temporal-NL (without it). The central finding is that agents with the sequential LSTM develop messages that achieve $M_{\ominus^n}=100\%$ in over 95% of runs, even without an explicit temporal prediction loss, while agents without it never do.

## Strengths

- **First systematic exploration of repetition-based message specialization in EC.** The paper tackles an underexplored question—how agents might develop messages that refer back to past observations—and provides a clear experimental framework (temporal referential games with controlled repetition structure, multiple environments, and architectural variants) for studying it.

- **Clean architectural finding confirmed by controlled comparisons.** The comparison between Temporal-NL (sequential LSTM, no temporal loss) and Non-Temporal (no sequential LSTM, with temporal loss) cleanly demonstrates that the processing architecture—not the explicit loss—is the decisive factor. Table 1 reports >95% of Temporal/Temporal-NL runs developing at least one $M_{\ominus^n}=100\%$ message, versus 0% for both Non-Temporal variants. This is a well-supported empirical result.

- **Parameter-matched ablation attempted.** The paper tests removing the meaning LSTM and keeping only the sequential LSTM while matching the parameter count of the baseline (Section 2.4/lines 185–186). The agents still develop temporal references, supporting the claim that the sequential processing structure, not just extra capacity, drives the effect.

- **Multiple controls and rigorous reporting.** Experiments use 10 random seeds per configuration, six evaluation environments including the "Always Same" control, and a varying-repetition-probability analysis (Figure 3b) that validates the $M_{\ominus^n}=100\%$ cutoff against accidental repetition. The metric cutoff is properly justified to exclude chance.

- **Candid limitations section.** The paper acknowledges the pigeonhole-principle caveat and the possibility of trivial temporality, showing awareness of the metric's limitations.

## Weaknesses

### Fatal
None.

### Major

- **Missing "Never Same" control results.** The "Never Same" environment is introduced (line 73) specifically to "verify if the same messages are used for other purposes than to purely indicate that the targets are the same." It is listed among the six evaluation environments (line 154), yet the paper never reports any quantitative results, figures, or tables for it. This is the most straightforward control that could validate or invalidate the metric—if temporal messages genuinely encode repetition, they should have $M_{\ominus^n}\approx0$ in "Never Same" (since no object ever repeats). Its absence leaves the metric only partially validated.

- **$M_{\ominus^n}$ conflates repetition-anaphora with genuine temporal reference at specific offsets.** The metric measures whether a message is used exclusively when an object from $n$ steps ago repeats, but the paper does not provide evidence that agents learn *distinct messages for different temporal offsets* ($\ominus^1$ vs $\ominus^2$ vs $\ominus^4$). A generic "this is the same object as before" message used for *any* repetition would still score $M_{\ominus^4}=100\%$ if it happens to only be deployed when the repetition occurs at offset 4 (or if the metric is only evaluated on a single $n$). Without a per-horizon breakdown of messages, the claim of a "temporal vocabulary" (plural, with structure) is inflated. The paper's single worked example (line 170) shows a message used as $\ominus^1$, but this is anecdotal rather than evidence of systematic offset-specific encoding.

- **The claim that temporal references emerge "regardless of the training dataset" / "even in a regular environment" is not clearly supported by the presentation.** Figure 2a is described as showing $M_{\ominus^4}$ over evaluation environments, and the text states temporal references emerge "regardless of the training dataset." However, the paper does not clearly disaggregate which agents were trained on which datasets or explicitly plot the critical condition: trained on RG Classic (0% repetition) and evaluated on RG Classic. It is plausible that the "regular environment" result reflects agents trained on TRG (with 50% repetition) and *evaluated* on RG Classic—a weaker claim than the architecture alone being sufficient. The paper should present the clean train-on-RG-Classic condition explicitly.

### Minor

- **The PLTL framing is overkill for what is actually measured.** The paper frames everything in terms of $\ominus^n$ (the PLTL "previously" operator), but the actual task only requires agents to detect that an object is the *same* as a past object, not to reason about arbitrary temporal propositions. The formalism adds terminology without adding analytical power—the metric could be described more straightforwardly as "exclusive repetition-reference proportion."

- **No analysis of whether agents learn messages for multiple different horizons.** Table 1 reports whether *any* message reaches $M_{\ominus^n}=100\%$, but does not report how many such messages exist per run or whether they are distributed across different $n$ values. A language with, say, one generic "same-as-before" message for all $n$ is qualitatively different from one with distinct messages for $\ominus^1$, $\ominus^2$, etc. The paper's strongest claim ("temporal vocabulary") implies the latter, but only the former is demonstrated.

- **Figure 2a description is unclear.** The caption and text (line 166) state that "TRGs refers to TRG Previous, and RGs refers to RG Classic" but do not explain the grouping structure on the x-axis (which appears to combine evaluation environments and potentially training conditions). This makes it difficult to verify the "regardless of the training dataset" claim from the figure.

- **The temporal prediction loss description is ambiguous about whether Temporal-NL agents still have the temporal label prediction layer in their architecture** (just without the loss term) or whether the layer itself is absent (lines 88, 146). If the layer is present but the loss weight is zero, the architecture still computes temporal labels during training, which could shape representations. This should be clarified.

### Trivial
None.

## Nice-to-Haves
- Report $M_{\ominus^n}$ for the "Never Same" environment as a validation of the metric.
- Include a per-horizon breakdown of messages (e.g., a table showing how many messages achieve $M_{\ominus^n}=100\%$ for each $n\in\{1,\dots,h\}$) to substantiate the "temporal vocabulary" claim.
- Add an explicit experiment training agents on RG Classic (0% repetition) and evaluating them on the same, to cleanly test whether the architecture alone suffices without any task pressure.
- For a qualitative trace, walk through a single complete episode where a temporal message is used, showing the objects, the messages, and the receiver's guess, to illustrate the mechanism.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's Issue 5 (parameter matching / capacity control):** The reviewer claimed the ablation "does not control for capacity" and "merely replaces one processing path with another." The paper *does* perform a parameter-matched ablation (line 185: "removing the Meaning LSTM ... matching the number of parameters as observed in the base agent"). The agents still develop temporal references. The reviewer's suggestion to "add a second LSTM to Non-Temporal that processes the same input without sequence context" is a different proposal, not a flaw—the paper already controls for capacity. This criticism is factually inaccurate and is removed.

- **Harsh Critic's claim that the comparison between Temporal and Temporal-NL is invalid because the temporal prediction layer shapes representations even without its loss being optimized:** This is speculation without support. The standard practice in EC (and ML broadly) is that removing the loss from a layer means it receives no gradient signal; residual shaping through forward-pass statistics alone is unlikely to drive the effect given the strong contrast with the Non-Temporal-NL baseline (0% temporal messages). The criticism is strained and removed.

- **Several of the Harsh Critic's Section-by-Section notes about missing appendix content, missing proofs, or parser artifacts:** These reflect the paper's extracted text, not the original submission. Removed per the hard rules.

- **The criticism that sequential LSTM batches treat unrelated episodes as a temporal sequence:** The paper explains the batching design (lines 84–85) as a choice to process history sequentially. Whether or not this is optimal, it is a deliberate design choice, not an error. Removed as a misunderstanding.

- **Strength Finder strengths that are generic or conflict with verified weaknesses:** The Strength Finder lists "Insight into generalizability and bandwidth efficiency" as a strength, but the bandwidth-efficiency claim is speculative (no measurements of message length or mutual information are provided). This strength is dropped because the paper does not supply data supporting it.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an important conceptual tension: the paper's metric and framing treat "temporal reference" as a binary property (a message either is or is not $100\%$ temporal for some $n$), but the actual cognitive-linguistic distinction between anaphora ("the same object as before") and genuine temporal deixis ("the object from 4 steps ago") is graded and structural. The paper would significantly strengthen its contribution by analyzing whether the learned messages exhibit *offset-specific compositionality*—e.g., by checking if the message content correlates with $n$ rather than just with object identity—rather than treating any $M_{\ominus^n}=100\%$ message as equivalent evidence of temporal vocabulary. This deeper analysis would also bridge the gap between the paper's PLTL formalism and its empirical measurements.

## Suggestions

1. **Report the "Never Same" results** quantitatively—this is the single most important missing control. If $M_{\ominus^n}\approx0$ in that environment for Temporal/Temporal-NL agents, the metric is validated. If not, the paper's interpretation must be revised.
2. **Clarify the training/evaluation design.** State explicitly: "Agent pairs were trained on [which environment] and evaluated on all six environments."
3. **Add a per-horizon analysis.** Report the distribution of $M_{\ominus^n}=100\%$ messages across different $n$ values (e.g., $\ominus^1$, $\ominus^2$, $\ominus^4$) to demonstrate whether the language has structure beyond a single generic repetition marker.
4. **Tone down the "temporal vocabulary" framing** unless stronger evidence (offset-specific encoding, compositional analysis) is provided. The results cleanly establish *repetition-based message specialization*, which is itself a valuable finding for EC without needing to claim full temporal deixis.
5. **Clarify the Temporal-NL architecture**—specify whether the temporal label prediction layer is present but not trained, or entirely absent.

## Score and Decision

The paper makes a genuine empirical contribution: it demonstrates that adding a sequential LSTM to sender/receiver architectures enables agents to consistently use dedicated messages for repeated objects, and that this effect requires neither explicit temporal supervision nor reward shaping. The experiments are well-controlled across multiple environments and seeds, and the central result (Temporal-NL >95% vs Non-Temporal 0%) is robust.

However, the paper over-interprets this result. The "temporal vocabulary" claim implies offset-specific structure that the evidence does not show, a key control ("Never Same") is introduced but never reported, and the presentation of training/evaluation conditions lacks needed clarity. These issues are addressable with additional analysis and more measured claims, but they weaken the paper in its current form.

This is a solid, borderline paper: its core empirical finding is valid and useful for the EC community, but the framing outstrips the evidence. With revisions—particularly adding the missing control, providing per-horizon analysis, and recalibrating the claims—it could become a clear contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>