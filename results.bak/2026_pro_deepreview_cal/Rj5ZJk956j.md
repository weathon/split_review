Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper introduces a weight-based method for classifying gated MLP neurons in LLMs according to their read–write (RW) functionality, using cosine similarities between their input, gate, and output weight vectors. Applying this method across nine LLMs reveals a universal pattern: early-middle layers are dominated by strengthening neurons (positive cos(w_in, w_out)) while late layers shift toward weakening neurons (negative cos(w_in, w_out)). The authors discover that weakening neurons — a small class concentrated in late layers — have disproportionately large influence on model behavior, and through a novel conditional ablation technique, they identify that negative gate values (previously assumed irrelevant to function) play a key role in this effect.

## Strengths

- **Novel, elegant methodology:** The cosine-similarity approach to classifying gated neuron RW functionality is simple, well-motivated by the residual stream framework, and applies cleanly to any model with gated activations. The taxonomy of six prototypical RW functionalities (Table 1) provides a useful vocabulary for the field.

- **Compelling cross-model evidence:** Figure 1(a) demonstrates a strikingly consistent pattern — median cos(w_in, w_out) transitions from positive to negative across layers — in all nine evaluated LLMs spanning different architectures (Llama, Gemma, OLMo, Mistral, Qwen, Yi). This universality is the paper's most persuasive result and is presented clearly.

- **Genuinely surprising and well-demonstrated behavioral finding:** Figure 3(a) shows that zero-ablating only 243 weakening neurons in OLMo-7B causes substantial divergence in attribute rate from layer ~10 onward, while a matched random-neuron baseline has negligible effect. This is a clean, convincing demonstration of disproportionate influence.

- **Innovative conditional ablation technique:** Section 6.2's method of partitioning activations by sign (gate+/−, input+/−) and selectively ablating is a genuinely useful methodological contribution. It cleanly attributes the entropy-sharpening effect to the negative-gate/negative-input condition, providing a precise tool for future interpretability work.

- **Novel observation about negative gate values:** The finding that negative Swish gate values carry functional importance (not merely training-dynamics relevance) is new and important for the mechanistic interpretability community, which has tended to treat Swish as approximately ReLU.

## Weaknesses

### Major

- **Arbitrary classification threshold without sensitivity analysis.** The taxonomy categorizes neurons using a fixed threshold τ = ±0.5 on cosine similarities (Section 4.2). The paper acknowledges the limitation — "these prototypical classes are limited in scope" — but provides no analysis of how classification boundaries affect category membership, cluster separability, or downstream ablation results. Given that claims about class sizes and distributions (e.g., "weakening neurons are a very small class") depend on this threshold, a sensitivity analysis or data-driven clustering would substantially strengthen confidence.

- **The "weakening" mechanism is not directly validated at the activation level.** The paper classifies neurons as "weakening" based on weight geometry (cos(w_in, w_out) ≈ −1), implying they subtract their detected direction from the residual stream. However, the ablation experiments demonstrate only that these neurons *matter* for behavior — not that they *implement weakening* in the claimed read–write sense. A systematic activation-level test (e.g., verifying that when a weakening neuron fires, the logit-lens projection of its w_out direction opposes the direction detected by w_in) would directly validate the mechanistic claim. The two case studies in Section 8 are anecdotal and, notably, the weakening neuron (31.9634) is most interpretable when it behaves as a strengthener under negative gate values.

- **Single-model behavioral validation.** All ablation experiments (Section 6), activation-frequency analysis (Section 7), and case studies (Section 8) use only OLMo-7B. Given that the cross-model universality of the weight pattern (Figure 1a) is a central contribution, the failure to replicate the key behavioral findings on even one additional model limits the generality of the "outsize influence" claim.

### Minor

- **Overclaiming in places.** The abstract states "for the first time, we observe a mechanism involving negative gate values" and the introduction uses phrases like "striking novel insights" and "universal patterns." While the findings are interesting, the evidence for a *mechanism* (as opposed to a *correlate*) rests primarily on one conditional ablation paradigm. More measured language would better match the current evidence level.

- **Ambiguity about which neurons are ablated.** Section 6 refers to ablating "weakening neurons" but does not clearly specify whether this includes only prototypical weakening neurons or also "atypical weakening" neurons (which Figure 1b shows as a distinct category). Clarifying this matters because atypical weakening neurons don't satisfy the full collinear configuration that motivates the "weakening" label.

- **Weight preprocessing rationale relegated to appendix.** Section 3.2 multiplies w_in and w_out by the sign of cos(w_gate, w_in) and states the argument is "in section C" (the appendix). Since this preprocessing could affect all downstream cosine computations and classification outcomes, its core justification should appear in the main text.

### Trivial

- The paper would benefit from reporting, per layer and per model, the absolute counts and fractions of neurons in each RW category, rather than relying primarily on the median trend plot (Figure 1a) and scatter plots (Figure 2).

## Nice-to-Haves

- Extending ablation experiments to at least one additional model (e.g., Llama-3.2-3B) would substantially strengthen the cross-model generality claim.
- A data-driven clustering of neurons in (cos(w_in, w_out), cos(w_gate, w_out)) space, with cluster stability analysis, would complement or replace the fixed threshold approach.
- For the negative-gate finding, corroborating with an intervention that flips the sign of negative gate values (rather than zero-ablating) would provide cleaner evidence that the negative values themselves are causal, not merely the removal of information.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The taxonomy and classification are arbitrary and unvalidated" (harsh critic framing as fatal):* The paper explicitly acknowledges the limitation and uses three complementary analysis modes (threshold, marginals, scatter plots). The threshold is a practical choice, not a fatal error. Retained as a major weakness for lack of sensitivity analysis, but demoted from fatal.

- *"Zero-ablation can induce artifacts... the observed sharpening could arise from side effects":* The paper notes that mean ablation results are in the appendix (Section F.4) and the conditional ablation design (selective zeroing by sign) already provides stronger evidence than blanket zero-ablation. This concern is reasonable but does not undermine the core finding. Retained as context for the mechanism-validation weakness, not as a standalone flaw.

- *"The case study... is only weakly interpretable... the most coherent activations occur when x_gate < 0, which makes the neuron act as a strengthener, not a weakener":* This is not a weakness of the paper — the paper explicitly frames this as the surprising finding that negative gate values reverse the neuron's polarity. The case study *illustrates* the paper's claim rather than contradicting it. Removed.

- *"The claims are phrased very strongly... The lack of rigorous validation makes these overclaims":* Partially valid but overstated. Retained as a minor weakness about overclaiming in specific places, not as a global indictment.

- *Strength Finder: "the paper addressed an important problem":* Generic and unspecific. Removed.

- *"The paper lacks a discussion of how many neurons are in each category per model":* The paper provides Figure 1(b) with category distributions for one model and states numbers for others are in the appendix. Not a content gap but a presentation choice. Retained as a trivial issue.

## Novel Insights

The most genuinely novel insight emerging from this work is the functional importance of the negative regime of the Swish gating function. Prior interpretability work has effectively treated gated activations as approximately ReLU-like, assuming negative gate values are negligibly small and relevant only to training dynamics. By showing that negative-gate activations of weakening neurons account for a large share of their entropy-sharpening effect, this paper opens up a new axis for mechanistic analysis: the sign of the gate value as a functional switch that can invert a neuron's read–write behavior. This insight has implications beyond this paper's specific classification scheme and should influence how the interpretability community models gated MLP layers going forward.

## Suggestions

- Bring the core justification for the weight preprocessing step (multiplying w_in and w_out by sign of cos(w_gate, w_in)) into the main text, even if just a few sentences.
- Add a small sensitivity analysis: report how many neurons change category when τ varies between, say, 0.3 and 0.7, and confirm that the key findings (layer-wise trends, ablation effects) are robust.
- Clarify in Section 6 whether "weakening neurons" in ablation refers to prototypical weakening only or includes atypical subtypes.
- Consider toning down the strongest causal-mechanism language ("mechanism involving negative gate values") to more descriptive language ("functional role of negative gate values") unless activation-level mechanistic validation is added.

## Score and Decision

**Bracket determination:** Round 1 placed the paper between approximately 6.0 and 8.0. Round 2 narrowed to 6.0–7.5 by comparison against Retrieval Heads (8.00, clearly stronger — more rigorous methodology, broader validation), Sparse Feature Circuits (8.00, clearly stronger), DOCS (6.60, comparable — our paper has more behavioral validation but DOCS has theoretical results), Circuit Component Reuse (6.50, comparable — similar quality of mechanistic interpretability contribution), and Towards Universality (6.50, comparable — similar cross-model analysis style).

**Final score rationale:** The paper is clearly above the 4.0–5.0 rejection range (e.g., "What does GPT store in its MLP weights" at 4.00, which has much narrower scope and less validation). It is clearly below the 8.0 tier (Retrieval Heads, Sparse Feature Circuits), which have more thorough validation and more principled methodology. Among the 6.0–7.0 anchors, this paper has stronger novelty (conditional ablation, negative gate finding) than most but weaker validation rigor (single model for behavior, arbitrary threshold, no activation-level mechanism test). The score of **6.5** reflects a solid, accept-worthy contribution with real novelty and compelling evidence, held back by meaningful but addressable gaps in validation.

**Anchor papers reviewed:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EytBpUGB1Z (Retrieval Heads) | 8.00 | R1 | Clearly stronger — more principled metric, broader validation, multi-task ablation |
| I4e82CIDxv (Sparse Feature Circuits) | 8.00 | R1 | Clearly stronger — more methodological depth, practical applications, thorough evaluation |
| tcsZt9ZNKD (Scaling SAEs) | 8.20 | R1 | Clearly stronger — scaling laws, systematic evaluation |
| nUGFpDCu3W (GPT MLP weights) | 4.00 | R1 | Clearly weaker — narrow scope, single phenomenon, limited validation |
| fpoAYV6Wsk (Circuit Reuse) | 6.50 | R2 | Comparable — similar quality of mechanistic contribution, our paper has broader cross-model evidence |
| 2J18i8T0oI (Towards Universality) | 6.50 | R2 | Comparable — similar cross-model analysis, our paper has more concrete behavioral findings |
| GdbQyFOUlJ (NeurFlow) | 6.50 | R2 | Comparable — similar neuron-group framework, NeurFlow has applications but less cross-model scope |
| XBHoaHlGQM (DOCS) | 6.60 | R2 | Comparable — both use cosine similarity for weight analysis; our paper has stronger behavioral validation |
| GPDcvoFGOL (CLIP neurons) | 6.75 | R1 | Slightly stronger — more thorough neuron-level analysis |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>