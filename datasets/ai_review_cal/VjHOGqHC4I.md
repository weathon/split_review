- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes architectural enhancements to the PerceiverAR for autoregressive language modeling. It describes three variants (V1, V2, V3) that aim to address PerceiverAR's limitations (latent-only training and lossy history compression), plus a fourth architecture called LLP (Long LoRA Perceiver) that uses overlapping half-segment attention inspired by LongLoRA's shifted sparse attention pattern. The paper provides clear equations and diagrams for all variants and reports perplexity results on Wikitext-103 and PG-19.

---

## Strengths

1. **Clear architectural descriptions of four variants with full equations.** Sections 4.1–4.4 present V1, V2, V3, and LLP with explicit equations (Equations 8–29) and figures. Each variant targets the two drawbacks stated in Section 3 (latent training dependency and lossy history) with a different design. The level of detail is sufficient for reproducing the proposed architectures.

2. **The LLP architecture combines overlapping segment attention with PerceiverAR's cross-attention in a novel way.** Section 4.4 describes how pairing overlapping half-segments (Q on one half, K/V on two halves) enables autoregressive training on the full sequence while maintaining sliding-window efficiency, overcoming PerceiverAR's restriction to latent-only training. This combination is specific to this work and not present in prior Perceiver or LongLoRA papers.

3. **Problem-driven motivation.** Section 3 clearly identifies two concrete drawbacks of PerceiverAR, and each enhancement is directly motivated by these issues rather than being ad hoc. This makes the contribution targeted and easy to follow.

---

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled baseline comparison undermines the core empirical claim.**  
   The paper compares the proposed LLP (seq=2048) against a baseline PerceiverAR that is evaluated at seq=1024 (Table 3). These operate at different sequence lengths, which directly affects perplexity (longer sequences are a harder task). A fair comparison requires the baseline and proposed model to be evaluated at the same sequence length. As presented, the claim of "much improved performance over the baseline PerceiverAR model" is not supported by a controlled experiment.

2. **Comparisons to prior work (Tables 4 and 5) are uninformative without controlled conditions.**  
   Tables 4 and 5 compare LLP to published models (Transformer-XL, MEGA, etc.) without controlling for parameter count, training compute, or training setup. The paper states "similar model sizes" but does not provide the actual parameter counts or training budgets of the compared models. Without these controls, the comparisons do not provide meaningful evidence of superiority.

3. **Misleading "Long LoRA" naming.**  
   The LLP architecture borrows only LongLoRA's *shifted overlapping attention pattern*, not its LoRA (low-rank adaptation) component. The paper acknowledges this in the conclusion ("our Long LoRA inspired PerceiverAR based architecture can use the Long LoRA in the attention heads to further improve"), confirming LoRA is not currently used. The name "Long LoRA Perceiver" sets false expectations about the method's relationship to LoRA-based fine-tuning and overstates the contribution.

4. **No quantification of the claimed computation trade-offs among V1, V2, V3.**  
   The paper introduces three variants with "varying computation overhead tradeoffs" but provides no FLOPs analysis, parameter counts, or runtime measurements to support these claims. The discussion is qualitative only (e.g., "if h > l, this increases computation"), making it impossible to assess whether the trade-offs are practically meaningful.

### Minor

5. **No ablation or sensitivity analysis for key hyperparameters.**  
   The LLP model uses segment size 256 without any justification or ablation. There is no study of how varying segment size, latent size, or the amount of overlap affects performance. Such ablations are standard for architecture papers and would strengthen the empirical claims.

6. **The Linformer description is imprecise.**  
   The paper states Linformer "cannot be used in effective autoregressive training as the masking of attention for future tokens cannot be accomplished." The limitation is not that masking is impossible but that the low-rank projection along the sequence dimension causes information loss. This is a minor inaccuracy but reflects sloppy handling of prior work.

### Trivial
None.

---

## Nice-to-Haves

- A controlled experiment comparing all variants (V1, V2, V3, LLP) against a fair baseline (same sequence length, same training setup) would be the highest-leverage improvement.
- Complexity analysis (FLOPs per layer, total parameters) for each variant to substantiate the claimed computation trade-offs.
- Ablation of the overlap mechanism in LLP — compare overlapping vs. disjoint segments to show the overlap is responsible for the improvement.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"V1, V2, V3 are never empirically evaluated."** — The paper places Table 1 (with configurations A, B, C) in the experimental section, and the text states "Configuration A, B and C represent different architecture variations." The text explaining the A/B/C mapping is truncated by parser artifacts, and the tables are embedded as images. In the original submission, these results exist. This criticism cannot be verified from the extracted text.
- **"The introduction is overstuffed with elementary background."** — This is a style nitpick. Background length is not a substantive weakness.
- **"The Convolutional Neural Networks comparison is irrelevant."** — This is a minor stylistic choice in the introduction and not a weakness.
- **"No code or model release commitment."** — Hard rule: do not question the existence or release status of cited entities.
- **"No evaluation on downstream tasks."** — The paper is scoped to language modeling perplexity; requesting downstream tasks is scope creep.
- **"No attention map visualization."** — This is a nice-to-have, not a weakness. Not standard for architecture papers.
- **"No analysis of sequence length scaling."** — Would strengthen the paper but is not a flaw in the current contribution.
- **"Linformer masking criticism is factually wrong."** — The paper's description of Linformer is a simplification but not factually wrong; masking in a projected space is technically possible but loses causal fidelity. This was demoted to Minor from the critic's stronger framing.
- **"The paper does not discuss prior work on overlapping chunked attention (Longformer, etc.)."** — The paper does cite Longformer in Section 2 (line 46) and discusses it in context. This is incorrect.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the uncontrolled experimental design as the central issue but do not add new technical insights.

---

## Suggestions

1. **Run a controlled experiment.** Train the baseline PerceiverAR and all proposed variants (V1, V2, V3, LLP) at the *same sequence length* with matched parameter counts and report all results together in a single table. This is essential to support the paper's empirical claims.

2. **Rename the LLP architecture.** Choose a name that reflects the architectural design (e.g., "Overlapping Segmented Perceiver" or "Overlap PerceiverAR") rather than referencing LongLoRA, since LoRA is not used.

3. **Provide complexity analysis.** For each variant, report FLOPs per layer, total parameters, and training/inference speed to substantiate the claimed computation trade-offs.

4. **Include ablations.** Show the effect of varying segment size, latent size, and the overlap mechanism (e.g., compare LLP with vs. without overlap).

---
