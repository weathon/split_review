Now I have all the information needed to produce the final consolidated review. Let me write it.

## Summary

This paper introduces Insertion Language Models (ILMs), which generate sequences by inserting one token at a time at an arbitrary position, jointly predicting both the position and the token. To train ILMs efficiently, the authors propose a denoising objective that avoids high-variance trajectory marginalization by using a counting-based target insertion distribution, and a transformer parameterization with a joint softmax over positions and tokens. ILMs are evaluated on planning tasks (star graphs, zebra puzzles) where they substantially outperform both autoregressive models (ARMs) and masked diffusion models (MDMs), and on medium-scale text generation/infilling (LM1B, TinyStories) where they are competitive with ARMs and better than MDMs.

## Strengths

1. **Strong planning results on variable-length, variable-order tasks.** On Star_hard (asymmetric arms, max path length 12), ILM achieves 99.1% exact match accuracy, while MDM drops to 21.0% and ARM to 23.0% (Table 1). This is direct, compelling evidence that ILMs overcome both the fixed-length limitation of MDMs and the left-to-right dependency failure of ARMs on tasks requiring out-of-order generation. The zebra puzzle result (90% exact match vs. 81.2% ARM and 82.6% MDM) further corroborates this advantage.

2. **Clean, practical training objective.** The paper identifies a real problem — naive marginalization over insertion trajectories has prohibitively high variance — and proposes a simple, biased objective (Eq. 2) that avoids this issue by counting dropped tokens directly. The parameterization using a standard transformer encoder with a joint softmax over positions and tokens is elegant and easy to implement. This simplicity contrasts favorably with more complex alternatives (e.g., DP-based approaches in concurrent insertion/deletion diffusion work).

3. **Effective arbitrary-length text infilling.** On LM1B multi-segment infilling, ILM achieves -7.93% change in NLL relative to the input, outperforming MDM's -6.02% (Table 3). This directly demonstrates ILM's flexibility advantage for infilling tasks where the number of tokens to be filled is unknown — a setting where MDMs are fundamentally constrained by their reliance on fixed mask counts.

4. **Multiple complementary text evaluation signals.** The paper does not rely solely on one metric: NLL under Llama-3.2-3B shows ILM close to ARM (2.14 vs. 2.11 on Stories, Table 2), while Prometheus 2 7B judge evaluations (Figure 5) show ILM outperforming both ARM and MDM on coherence and consistency. The Prometheus results partially mitigate concerns about any single metric's reliability.

## Weaknesses

### Major

- **No variance or statistical significance reporting for any text experiment.** Tables 2 and 3 report single numbers with no error bars, confidence intervals, or multiple random seeds. The NLL gap between ARM and ILM on Stories (2.11 vs. 2.14) is very small; without variance estimates it is impossible to know whether this gap is meaningful or noise. Given the stochasticity in sampling procedures (nucleus sampling, top-k), this is a concrete methodological gap that weakens the strength of the text generation claims. This is particularly noticeable because concurrent work in the same problem space (e.g., FlexMDM, DID) also faces scrutiny on this point.

### Minor

- **The Insertion Transformer (IT) baseline is under-described.** The paper reports IT's poor performance on star graphs (35.2% on Star_easy, vs. ILM's 100%) but provides no details on the IT architecture used, hyperparameters, training setup, or how it was adapted to these tasks. IT is a direct predecessor method, and readers cannot assess whether its poor performance is due to a fundamental limitation or to an unsuitable implementation. This comparison would be more informative with additional detail — especially since IT is not evaluated on zebra puzzles or text tasks at all.

- **The stopping mechanism during inference is underspecified.** The paper describes learning a binary stop classifier (Section 3) and states that it uses `<stp>` token outputs, but does not specify the decision rule during generation (e.g., threshold at 0.5? argmax over stop vs. continue?). This detail is needed for reproducibility of the length-control mechanism, which is central to ILM's claimed advantage over MDMs.

- **NLL under an autoregressive LLM as the primary text metric carries known limitations.** While the paper also uses Prometheus evaluations (which partially address this), NLL under Llama-3.2-3B is the headline metric in Table 2. This metric evaluates fluency from a left-to-right perspective, which is reasonable for measuring text quality but inherently favors ARMs slightly. The paper acknowledges the ARM advantage in NLL but attributes it to "training token efficiency and scaling laws" (Section 5.3.1) rather than metric bias. The claim that ILMs are "competitive with ARMs" on text is supported reasonably well given the close NLL numbers and Prometheus advantages, but a clearer acknowledgment of what NLL under an LLM does and does not measure would strengthen the argument.

### Trivial

- None beyond minor presentation points typical of a camera-ready revision.

## Nice-to-Haves

- A small scaling study (e.g., 200M+ parameters) or discussion of whether the dropout-based denoising objective remains stable at larger model sizes.
- Reporting precision/recall of the stopping classifier to give insight into length-control accuracy.
- A comparison with more recent MDM variants that use greedy or top-k unmasking (e.g., Gong et al., 2024; Campbell et al., 2024), since the paper only compares against the vanilla tau-leaping sampler.

## Removed Points

The following points from the input reviews are removed per filtering rules:

- **"Training objective bias is not characterized"** (Harsh Critic #2): The paper explicitly references Appendix D for discussion of the approximation. Per meta-review policy, weaknesses about content stripped from the appendix by the PDF parser are not included.
- **"NLL under Llama is structurally biased against ILMs"** (Harsh Critic #1, framing as fatal): This overstates the issue. NLL under an LLM evaluates the *generated text* as a string, not the generation trajectory. Coherent natural language will score well regardless of how it was generated. The metric's mild preference for left-to-right structure is a secondary concern, not a fatal evidential flaw. The paper also provides Prometheus evaluations as a complementary signal. This concern is folded into Minor weakness #3 above.
- **"Missing human evaluation or calibration for Prometheus"**: The paper uses Prometheus as one of several metrics, not as a sole arbiter. This is not standard practice in comparable work; demanding human evaluation for 85M-parameter models goes beyond the evaluation norms in this literature.
- **"Scaling discussion" and "comparison with more MDM variants"**: These are scope-creep demands. The paper is upfront about its medium-scale setup.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add standard deviations over at least 3 random seeds to the text generation and infilling tables. If single-seed results are reported, state this clearly and justify.
2. Provide details of the Insertion Transformer implementation (architecture, hyperparameters, training setup) to make that baseline informative, or remove it if the details cannot be provided.
3. Specify the stopping decision rule used during inference (threshold value? argmax over stop vs. continue?).
4. Add a brief discussion of what the NLL-under-Llama metric captures and does not capture, especially in relation to the claim of being "competitive with ARMs."

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:** Initial search with three bands. Weak-band anchors (avg 1.5–3.3) are papers like VALM (1.50) and a DLM self-evaluation paper (3.33) — clearly weaker than ILM. Mid-band anchors (4.5–6.8) include DID (6.80), FlexMDM (6.50), Smoothie (4.50), and DiffInk (5.50). Strong-band anchors (8.00+) are unrelated to the topic. **Round 1 bracket: 5.0 – 6.5.**

**Round 2 — Narrowing:** Searched inside (4.5, 7.0) and (5.5, 7.5) on insertion LM and planning topics. Key anchors considered in full:

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|------------------------|
| DID (VbvXjs5f72) | 6.80 | R1/R2 | Stronger theoretical grounding (score entropy derivation), efficiency benchmarks, comparable text results. ILM has simpler training and stronger planning results. ILM is slightly weaker overall → score below 6.80. |
| FlexMDM (ttuNnMRI6H) | 6.50 | R1/R2 | Similar problem addressed (variable-length any-order). Has theoretical guarantees and 8B scaling demo. ILM has stronger planning results but weaker text evaluation (no error bars). ILM is somewhat weaker → score below 6.50. |
| PAPL (lAlI5FuIf7) | 5.50 | R2 | Modifies MDM training objective vs. proposing new model class. ILM's contribution is more novel. ILM is stronger → score above 5.50. |
| Smoothie (5y8R8XSHkG) | 4.50 | R1 | Token-embedding diffusion for text. Less related, lower quality. ILM is clearly stronger. |

**Final placement:** Between PAPL (5.50) and FlexMDM (6.50)/DID (6.80), closer to the upper end of the bracket. The planning results are genuinely compelling and the method is novel and clean. The main weakness — absence of variance reporting — is real but addressable, and does not invalidate the core contribution.

**Score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>