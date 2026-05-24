Now I have sufficient calibration. Let me compile the final review.

**Calibration Summary:**

- **Round 1 bracket**: I estimated a score between 5.0 and 7.0.
- **Round 2 anchors**:
  - ReCogLab (5.00): Testing cognitive hypotheses on LLMs. Weaker framing/justification than the paper under review; this paper has stronger theoretical motivation and more thorough experimentation.
  - Telephone Game (6.00, scores 3,8,8,5): Iterated cultural transmission in LLMs. Similar methodology (transmission chains) but this paper has stronger theoretical grounding (IB), broader model coverage (39 vs ~4), and more honest limitation reporting.
  - Culture Attribution (7.00, scores 5,6,8,8,8): Well-executed but limited to one model. This paper is broader in model scope but the core IICLL finding also depends heavily on one model.
  - Composition through Decomposition (6.67, scores 6,8,6): Cleaner focused experiments but narrower scope.
- **Final position**: The paper is comparable to or slightly stronger than Telephone Game (6.00) due to stronger theoretical foundations and broader model survey, but its central claim depends primarily on one model (Gemini 2.0), which limits generality. This places it at **6.0**.

---

## Summary

This paper investigates whether LLMs exhibit a human-like inductive bias toward Information Bottleneck (IB)-efficient semantic categorization, focusing on color naming as a testbed. It conducts two studies across 39 LLMs: (1) an English color-naming evaluation showing that larger instruction-tuned models (Gemini 2.0, Gemma 3 27B) achieve near-human IB tradeoffs, and (2) a novel Iterated In-Context Language Learning (IICLL) paradigm that simulates cultural transmission of pseudo color-naming systems. The key finding is that Gemini 2.0 restructures initially random systems toward human-like, near-optimal IB tradeoffs across a wide complexity range, matching human iterated-learning data, while other models converge to lower-complexity solutions.

## Strengths

- **Principled theoretical framing via the Information Bottleneck**: The paper grounds its evaluations in the well-supported IB theory of semantic systems (Zaslavsky et al., 2018), using efficiency loss, IB-alignment, and NID as metrics. This allows direct quantitative comparison of LLM behavior to both human languages and human iterated-learning data (Figures 2–4), which is a clear advance over prior work that assessed LLM color naming without this theoretical lens.

- **Comprehensive multi-model evaluation**: Testing 39 models across 6 families (Gemini, Gemma, Llama, Qwen, Olmo, GPT-2) at varying sizes and training stages, the paper systematically shows that English-alignment improves with model size and instruction-tuning, with some models producing color systems resembling low-resource WCS languages rather than English (Appendix E, Figure 9). The training-dynamics analysis of Olmo 2 checkpoints (Appendix F) further isolates instruction-tuning as the key stage for category acquisition.

- **Novel IICLL paradigm and honest reporting of its limitations**: The IICLL protocol adapts human cultural-evolution experiments to LLMs in a well-controlled manner (pseudo terms, no hint that stimuli are colors). The paper is transparent that only Gemini 2.0 recapitulates the full human-like range of IB tradeoffs, with other models converging to low-complexity solutions (Figure 3). This honesty is a strength, not a weakness.

- **Rotation analysis validates non-triviality**: The hue-rotation control (Appendix H, Figure 11) shows that Gemini's emergent structure is not an artifact — rotating the color-label mapping significantly degrades both efficiency and WCS-alignment. A baseline comparison against a feature-based clustering algorithm (Appendix M) further strengthens the case that Gemini's bias is genuine.

## Weaknesses

### Major

- **Generality of the central claim rests primarily on one model**. Of the four models tested in IICLL, only Gemini 2.0 converges to the full range of near-optimal IB tradeoffs seen in humans (Figure 3). The other models (Gemma 3 27B, Qwen 2.5 32B, Llama 3.3 70B) produce IB-efficient but low-complexity systems. The paper is honest about this, but the title and abstract's framing of "LLMs are capable of evolving human-aligned semantic categories" is de facto a claim about frontier models with exceptional in-context learning — and, in practice, about one specific model. This does not invalidate the contribution, but it narrows the generality substantially. Testing additional frontier models (e.g., GPT-4, Claude) would meaningfully strengthen the claim.

- **The IB bound is evaluated against a human perceptual model (CIELAB-based Gaussian noise) that the paper itself shows is mismatched with LLMs**. The paper reports that presenting colors in CIELAB coordinates *hurts* performance (Section 4.1), confirming that LLMs do not share this human perceptual geometry. The IB bound is used as an external benchmark, which is defensible, but the claim that LLMs exhibit "the same" IB-efficiency bias as humans would be stronger if the paper could show that the proximity to the bound is robust under alternative perceptual models that better reflect how LLMs represent color. A null distribution over random partitions of the WCS grid would also help quantify how surprising the observed proximity to the IB bound actually is — the rotation analysis provides partial evidence but is not a full null.

### Minor

- **The distinction between IB-efficiency and a generic "prefer compact, contiguous categories" bias is not sharply drawn**. The IICLL results show that LLMs converge to efficient, compact systems, but it is not fully clear whether this reflects the specific IB complexity-accuracy tradeoff or a simpler prior for regular, contiguous partitions. The rotation analysis and clustering baseline begin to address this, but a more direct comparison — e.g., contrasting trajectories that optimize only accuracy, only complexity, or the full IB objective — would sharpen the mechanistic claim.

- **The Shepard circles experiment (Section 4.3) does not include any IB analysis**, and the paper explicitly defers this to future work. While the section is framed as preliminary and is careful not to overclaim, the abstract's statement that this result "suggest[s] that our result could potentially apply also in other domains" risks conflating "structured categories" with "IB-efficient categories." This is a minor framing imprecision rather than a substantive flaw.

- **Number of IICLL chains and per-chain variability are not prominently reported** in the main text. Figure 4 shows 95% CIs, but the main text does not state how many chains were run per condition or show individual chain trajectories (beyond thin blue lines in Figure 3). Explicitly reporting this would help assess robustness.

### Trivial

- The description of the clustering baseline in Appendix M as "an alternative feature-based clustering algorithm" is too vague to evaluate without reading the (stripped) appendix. Specifying the algorithm would improve transparency.
- The paper uses different prompting procedures for Gemini (controlled generation) vs. open-weight models (log-prob scoring). The paper notes this but does not discuss whether it could affect cross-model comparisons. A brief note would improve methodological transparency.

## Nice-to-Haves

- A null distribution over random partitions of the WCS grid (matched for category count) against which to benchmark observed efficiency losses, to quantify how surprising proximity to the IB bound is.
- Testing at least one additional frontier model with strong in-context learning (e.g., GPT-4, Claude) to broaden the generality claim beyond Gemini 2.0.
- A more fine-grained analysis of what drives the IICLL convergence — is it complexity reduction, accuracy maximization, or the IB tradeoff specifically?

## Removed Points

These points were raised by reviewers but are removed after verification against the paper:

- **CIELAB perceptual model mismatch (Harsh Critic Point 1)**: The paper explicitly acknowledges this issue ("CIELAB *hurts* performance... reveals a key difference between how LLMs represent color and how humans do") and uses the IB bound as an external benchmark, not as a claim about LLM internals. The paper's approach is standard and transparent.
- **Shepard circles overclaiming (Harsh Critic Point 3)**: The paper explicitly calls this a "preliminary investigation," limits analysis to Gemini and k=4, and states "An important direction for future work is to test whether this emergent structure also supports greater IB-efficiency." The abstract says "structured category systems" not "IB-efficient systems." The paper is appropriately cautious.
- **Comparing prompt formats (Section-by-section notes)**: The paper reports the procedural difference honestly. Using controlled generation for Gemini (API limitation) and log-prob scoring for open-weight models is standard practice given the API constraints, and the comparison is within-model-family where procedures are consistent.
- **Missing related works, typos, formatting**: These are parser artifacts or would require external knowledge to verify.

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that cultural transmission via IICLL can drive LLM category systems toward IB-efficient, human-aligned solutions, and that this is most pronounced in the strongest in-context learner (Gemini 2.0) — is clearly articulated by the authors.

## Suggestions

1. Add a null distribution analysis: compute efficiency losses for many random partitions of the WCS grid with matched category counts, and show that the LLM-evolved systems (and human systems) are significantly better.
2. Test at least one additional frontier model (e.g., GPT-4, Claude 3.5) to assess whether the full-complexity-range IICLL result generalizes beyond Gemini 2.0.
3. Tighten the framing of the central claim to more precisely reflect the model dependence (e.g., "frontier LLMs with strong in-context learning" rather than "LLMs").
4. Report the number of chains and show per-chain variability for the IICLL experiment more prominently.
5. The Shepard circles experiment would benefit from a brief discussion of why domain-generality is relevant even without IB analysis, or be moved fully to appendix as a pilot result.

## Score and Decision

**Bracket**: Round 1 placed the paper between 5.0 and 7.0 based on comparison with weak anchors (~3.0, mostly reject-quality papers on peripheral topics), middle anchors (5.0–6.5, including the Telephone Game paper at 6.00), and strong anchors (~8.0, which this paper clearly does not match).

**Narrowing**: Round 2 compared against ReCogLab (5.00), Telephone Game (6.00), Culture Attribution (7.00), and CtD (6.67). The paper is stronger than ReCogLab (better framing, more thorough experiments) and comparable to the Telephone Game paper (both study iterated LLM dynamics; this paper has stronger theory and broader model survey, but the Telephone Game paper's research question was more novel; both have generality limitations). It is weaker than Culture Attribution (7.00) and CtD (6.67) in terms of experimental precision and focus.

**Final score**: 6.0 — a solid contribution with a well-motivated theoretical framework, thorough experimentation, and honest limitation reporting, but with a central result that depends heavily on one model and some precision gaps in the evidence.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>