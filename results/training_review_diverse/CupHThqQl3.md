Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper investigates how temporal references (e.g., messages meaning "same as the object seen 4 episodes ago") can emerge naturally in agent communication. It introduces the Temporal Referential Game (TRG) — a referential game where 50% of targets repeat from a random past episode — and proposes augmenting both sender and receiver with a sequential LSTM that processes episodes as a temporal sequence. The key finding is that this architectural change alone suffices for temporal references to emerge in over 95% of runs, without any explicit temporal prediction loss. Agents without the sequential LSTM never develop such references, regardless of loss function.

## Strengths

- **First systematic study of temporal vocabulary in emergent communication.** The paper identifies a genuine gap — temporal references have been exploited pragmatically (Kang et al., 2020) but never studied as a linguistic phenomenon in EC. The claim that this is the first reported temporal vocabulary in EC is well-supported (Abstract, Line 4; Introduction, Lines 14-16).

- **Clean experimental demonstration that sequential LSTM is sufficient for temporal reference emergence.** Figure 2a and Table 1 together show that only architectures with the sequential LSTM (Temporal, Temporal-NL) produce messages reaching 100% on the temporality metric $M_{\Theta^n}$, while Non-Temporal and Non-Temporal-NL never do. This holds across training environments and with or without the explicit temporal prediction loss. The controlled comparison (sequential LSTM present vs. absent) is the right design to support the causal claim.

- **Well-defined, interpretable metric ($M_{\Theta^n}$) for quantifying temporal referencing.** The metric is formally defined (Equations 3-5, Section 3.1) and illustrated with worked examples. It cleanly measures whether a message is used exclusively as a temporal operator at a specific horizon $n$. The 100% threshold is conservative and avoids conflating accidental correlations with genuine temporal reference.

## Weaknesses

### Fatal
None.

### Major

- **The sequential LSTM's temporal processing mechanism is critically underspecified.** The paper states the sequential LSTM receives "a batch of shape [1, 128, 6], or a sequence of 128 objects of size 6" (Line 84), but never specifies whether those 128 objects come from *consecutive episodes in chronological order*. If they are not temporally ordered, the LSTM cannot learn temporal relationships between episodes, and the paper's central claim would be unsupported. Additionally, the paper does not describe how the sequential LSTM's hidden state is initialized, whether it is carried across batches, or how the data loader handles episode ordering (shuffle=True vs. False). Since the entire contribution rests on this mechanism, the ambiguity is structural — not a trivial omission. The paper must clarify these details for the contribution to be verifiable. *Note: I judge this as Major rather than Fatal because the results (sharp contrast between agents with vs. without the module) are internally consistent and strongly suggest correct temporal batching; the issue is one of underspecification, not demonstrated error.*

### Minor

- **"Never Same" evaluation results are not explicitly discussed.** The paper states agents are evaluated in the "Never Same" environment (Line 154) and that this environment is used "to verify if the same messages are used for other purposes than to purely indicate that the targets are the same" (Line 73). However, the analysis text (Section 3.3) does not report or interpret the $M_{\Theta^n}$ values in "Never Same". Showing that temporal messages have $M_{\Theta^n}=0$ in "Never Same" would close the evidential loop. The figure presumably contains this data, but the paper should discuss it explicitly.

- **Analysis focuses on a single horizon ($n=4$).** The metric is defined for any $n$, but the quantitative analysis (Figure 2a, Table 1, Figure 3a) exclusively uses $n=4$. One example in Section 3.3 mentions a message used as $\Theta^1$, but no systematic results for $n=1,2,3$ are reported. Showing that the findings generalize across horizons would strengthen the paper.

- **Message length and vocabulary efficiency are not measured.** The Discussion (Section 4) speculates that temporal references improve bandwidth efficiency, and the distribution analysis (Figure 3a) suggests temporal messages form a small specialized subset. However, no direct evidence (e.g., comparing message lengths or vocabulary sizes between temporal and non-temporal agents) is provided. This weakens the efficiency claim.

- **No comparison to a standard recurrence baseline.** The paper's two-LSTM architecture is one of many plausible temporal extensions. A simpler baseline — e.g., a single LSTM whose hidden state is maintained across episodes (standard recurrence over time) — would help determine whether the sequential-LSTM design is specifically important or whether any form of temporal state-carrying suffices. The control experiments rule out the "no temporal processing" condition, but do not isolate *which* aspect of the sequential LSTM matters.

- **Effect of the temporal prediction loss on convergence/accuracy is not reported.** The paper finds the loss is unnecessary for temporal reference emergence but does not analyze whether it affects convergence speed, final task accuracy, or the rate of temporal strategy adoption. This is acknowledged implicitly but would add depth.

### Trivial

- Line 71-73: "The agents are also trained and evaluated in … "could be read as suggesting Always Same/Never Same are training environments. The later clarification (Line 154) resolves this, but a rephrase would avoid ambiguity.

## Nice-to-Haves

- Reporting $M_{\Theta^n}$ for $n=1,2,3$ in addition to $n=4$ (beyond Minor).
- An ablation varying the combination method (element-wise multiplication vs. concatenation) for the two LSTM hidden states.
- An ablation varying the repetition probability $p$ (already partially present in Figure 3b) to study how the implicit pressure scales.
- Learning curves showing how temporal references develop over training.

## Removed Points

- **"The metric may conflate consistent object naming with genuine temporal reference"** — The paper's 100% threshold and the analysis in Section 3.3 (Table 1, Figure 3b) directly address this concern. The reviewer's own analysis concludes "This part is fine" for the main environment. The "Never Same" gap is already listed as a Minor weakness.

- **"Relationship between Always Same/Never Same and training is underspecified"** — The paper clearly states on Line 154 that evaluation is performed after training and that agents are assessed in these environments. The ambiguous phrasing on Line 71 ("The agents are also trained and evaluated in…") refers to RG Classic/RG Hard, not Always Same/Never Same. This is not a genuine weakness.

- **"Element-wise multiplication needs ablation"** — While a reasonable experiment, the paper is not claiming optimality of the combination method, and the design choice is plausible. This is a wishlist item, moved to Nice-to-Haves.

- **"No comparison to alternative baseline using recurrent architecture with state across episodes"** — The paper's design (comparing with/without sequential LSTM) is a clean treatment-control experiment. The suggested baseline is useful but not required for the paper's claims. Moved to Nice-to-Haves.

- **"Temporal Prediction Loss effect on performance not reported"** — Already included as a Minor weakness. The reviewer overstates its importance.

- **"Statistical strength would be improved by reporting variance"** — The paper uses 10 seeds per configuration, which is standard in EC. The 95%+ vs. 0% results are decisive enough without confidence intervals. This is a generic nitpick.

- **"Does not analyze which implicit pressure"** — The paper (Section 4, Figure 3b) does analyze this by varying repetition probability. The reviewer missed this.

- **"No analysis of message length or vocabulary size"** — Already listed as a Minor weakness, not removed but downgraded from how the reviewer framed it.

- Strengths from Strength Finder that were dropped: None of the listed strengths needed removal — all are substantiated with specific evidence from the paper.

## Novel Insights

The harsh critic's core observation — that the sequential LSTM batching mechanism is underspecified — is valid and important, though the reviewer overstates it as potentially fatal. The more subtle insight is that the paper's metric ($M_{\Theta^n}$) is horizon-specific by construction; an agent that develops a generic "this object was seen before" message (regardless of how long ago) would never reach 100% for any single $n$. This means the paper's findings are about *horizon-specific* temporal references, and the claim is more brittle than the 95%+ numbers might suggest. That said, this is not a flaw — the paper characterizes exactly what it measures — but it is an important boundary condition that future work should address. Beyond this, the reviews do not surface deeper novel insights beyond what the paper itself contributes.

## Suggestions

1. **Clarify the sequential LSTM batching mechanism explicitly.** State whether episodes are arranged in chronological order within each batch, whether the LSTM hidden state is reset between batches or carried across, and whether the data loader uses shuffle=True or False. This is the single highest-priority fix.

2. **Report $M_{\Theta^n}$ values in the "Never Same" evaluation environment explicitly in the text**, confirming that temporal messages have zero usage when no repetitions occur.

3. **Show results for multiple horizons ($n=1,2,3$)** to demonstrate that the findings are not specific to $n=4$.

4. **Add a paragraph discussing the "Never Same" results** to close the evidential gap the paper's own design intended to address.

## Score and Decision

The paper tackles a genuine gap in EC with a clean experimental framework and a clear, non-obvious result. The core contribution — that a sequential LSTM is sufficient for temporal reference emergence — is well-supported by the controlled experiments (Table 1: >95% vs. 0%). The weaknesses are mostly about underspecification and scope, not about flawed methodology or incorrect claims.

The single structural weakness is the underspecified sequential LSTM batching mechanism. If the authors clarify this and confirm that episodes are temporally ordered within batches, the paper's claims stand. This is addressable in revision and does not require new experiments.

Originality: High — first study of temporal references in EC.
Importance: Moderate — addresses a meaningful gap; the architectural insight is transferable.
Claims support: Good, but with the sequential LSTM ambiguity needing resolution.
Soundness: Good — controlled experiments, multiple seeds, clean metric.
Clarity: Needs improvement in describing the temporal mechanism.
Value: Solid contribution to the EC community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>