Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper reverse-engineers how small encoder-only transformers implement the carrying-over algorithm for integer addition, finding a modular decomposition: layer 1 adds digits, layer-2 attention decides where carries are needed, and the final MLP executes carries. It identifies ~86 carry-specific neurons, demonstrates length generalization via priming/finetuning, and offers suggestive evidence of similar patterns in 7B LLMs. The core small-model mechanistic account is largely convincing and well-supported.

## Strengths

- **Causal modular decomposition via systematic ablations (Table 1):** The paper demonstrates that the carrying-over algorithm is cleanly allocated across architectural components. Ablating the decision head causes confusion on non-carry sums (NC accuracy drops to ~0.31–0.52) and some carry sums (C@1 pos8=0.49, C@2 pos7=0.58), while ablating the final MLP leaves non-carry accuracy high (≥0.90) but makes the model fail on carry sums — a deficit precisely corrected by manually adding a one. The cross-validating pattern of ablation results provides strong causal evidence.

- **Precise neuron-level mapping of the carry function:** The activation-based neuron ablation method isolates ~86 neurons whose removal entirely eliminates the ability to carry a one while preserving 100% accuracy on non-carry sums (Section 4). This fine-grained causal mapping goes well beyond module-level ablation and is a rare level of precision in mechanistic interpretability.

- **Generalization via priming/finetuning to longer lengths:** The paper shows that the 3-digit modular implementation transfers to 6-digit addition with only 100 priming examples or 500 finetuning examples (reaching 0.94 accuracy with minimal weight changes). This demonstrates the learned algorithm is reusable rather than an artifact of short training length.

- **Fine-grained evaluation methodology via natural data subsets:** The five task subsets (NC, C@1, C@2, C all, C all con.) provide a precise diagnostic of where models succeed and fail. This methodological choice significantly strengthens the causal interpretation of ablations and is one of the paper's most valuable contributions.

- **Analysis of learning dynamics for the carry MLP:** Tracking the evolution of the final MLP's carry function via Pearson correlation with a no-carry baseline shows that carry specialization starts early and coincides with a kink in test loss — connecting algorithmic emergence to training trajectory.

- **Suggestive evidence of analogous structure in 7B LLMs:** Llemma and Zephyr exhibit staircase attention patterns, residual-stream separation by carry need at layer 25, and predominantly carry-type mistakes (64–74%), all consistent with the small-model findings. The paper is appropriately cautious about the strength of this evidence.

## Weaknesses

### Fatal
None.

### Major

- **No limitations or alternative-explanation discussion.** The paper lacks any limitations section. Several important scope constraints are not discussed: (1) how results depend on specific architectural choices (RoFormer, d_model=128, 2 heads, encoder-only), (2) the possibility that RL-trained or instruction-tuned models implement addition differently, (3) whether the observed staircase patterns could partially be explained by RoFormer's position-similarity encoding rather than purely reflecting addition, and (4) the instability in length generalization where the model "forgets" carries at later training. Including such a discussion would substantially strengthen the paper.

### Minor

- **"Novel phase transition" claim is undersupported.** The paper claims the QK-circuit phase transition in one-layer models is "novel" (Contributions item 4, Conclusion) but does not clearly differentiate it from prior observations of phase changes in attention — e.g., induction head formation (Olsson et al. 2022) or sudden formation of diagonal/staircase patterns. The specific distinguishing features (non-grokking, staircase for addition, improving but not reaching perfection) are interesting but not explicitly argued as novel relative to prior work. The claim should be carefully scoped.

- **LLM evidence is correlational, not mechanistic.** While the paper is transparent about this being "suggestive evidence," the gap between finding staircase attention patterns/residual-stream separation and demonstrating the same mechanistic algorithm is large. The fact that 64–74% of LLM mistakes are carry errors is consistent with the small-model implementation but does not rule out other algorithmic structures. The paper does not discuss what the remaining 26–36% of mistakes are — analyzing those could reveal whether the models implement the same algorithm imperfectly or a different algorithm.

- **The role of the non-decision head in layer 2 is not analyzed.** The paper identifies one head as the "decision head" but does not analyze the other head's function beyond noting it transfers information via skip connections. A complete modular account should address what both heads do.

- **Corrected accuracy shortfalls are not discussed.** After ablating the final MLP and manually adding a one, corrected accuracy for C@1 position 7 reaches only 0.86 (not 1.0). The paper does not discuss why this residual error exists, which could indicate additional complexity in the carry mechanism.

- **RoFormer choice is mentioned but not justified.** Rotary position embeddings may be important for the staircase patterns, but the paper does not discuss whether results would differ with absolute or learned positional embeddings.

- **Length generalization section is too brief in the main text.** The finding that components are in place around epoch 500 but then forgotten is potentially important but gets only a single sentence. The claim that this instability "suggests" priming would work is stated without detailed evidence in the main text.

### Trivial
- The one-layer section is acknowledged by the authors as incomplete ("harder to fully reverse engineer") — this is acceptable given the paper's focus on two-layer models but leaves the phase-transition claim less thoroughly characterized than the rest of the paper.

## Nice-to-Haves
- A discussion of how the results might change with different positional encodings (e.g., absolute vs. rotary), to test whether staircase patterns are a general property or specific to RoFormer.
- Analysis of cross-run consistency for which specific head is the "decision head" (the ablation results are averaged, but does the decision head always land in the same position?).
- Characterizing the remaining 26–36% of LLM mistakes beyond just carry errors.
- A brief discussion of the non-decision head in the second attention layer.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Decision head interpretation does not match the ablation data" (Harsh Critic Issue 1):** The critic claimed "accuracy remains 1.0 at all positions" for carry sums (C@1, C@2, C all, C all con.) after decision head ablation. This is factually wrong — Table 1 shows C@1 pos8=0.49 and C@2 pos7=0.58. The critic further argued the head's role is suppression rather than decision, but the data show the head IS needed for some carry sums, not just for suppressing carries on NC sums. The paper's framing ("helps decide whether or not to add a carried one") is consistent with the observed pattern: without it, the model fails on some carry positions and becomes confused (accuracy ~0.5) on non-carry positions. **Removed for factual inaccuracy.**

- **Complaints about missing appendix content** (e.g., length generalization detail, LLM appendix details): The appendix exists in the original submission but was stripped by the parser. Per instructions, these are parser artifacts.

- **"The LLM section has prominence the evidence cannot support":** The LLM analysis occupies one subsection of the Generalisations section near the end of the paper, and the paper repeatedly qualifies it as "suggestive evidence" and "an application of our learned intuition." The prominence is proportionate to the caveats.

- **Criticism that the one-layer section is "thin":** The paper explicitly acknowledges one-layer models are harder to reverse-engineer and that the focus is on two-layer models. This is a deliberate scope choice, not a flaw.

- **Criticism that "there is one head that is more important than the other" should be shown across runs:** The ablation results (Table 1) ARE averaged over six runs, and the paper notes "from what we have seen in other runs, this is typically not the only path."

## Novel Insights

The most interesting observation emerging from the reviews is a subtlety in interpreting the decision head's role: the ablation data (Table 1) show the model without the decision head behaves approximately as a "carry everywhere" system — it gets carry sums mostly right but spuriously adds carries to ~50% of non-carry positions. This is more naturally described as the head *gating* carries (suppressing them where inappropriate and enabling them where needed) rather than actively *deciding* to carry. However, the paper's framing ("helps decide whether or not to add a carried one") is broad enough to encompass this interpretation, and the counterfactual (ablating the decision head also degrades some carry sums) shows the head is doing more than pure suppression. The paper could sharpen its mechanistic narrative by explicitly discussing this gating interpretation. Beyond this, the reviews do not surface genuinely novel insights beyond the paper's own contributions.

## Suggestions

1. Add a limitations section discussing architectural dependencies (RoFormer, d_model, 2 heads), the gap between small-model proof and LLM evidence, and the instability in length generalization.
2. Scope the "novel phase transition" claim by explicitly stating what distinguishes it from prior observations (e.g., induction head formation, grokking phase changes) — the staircase pattern for addition and the non-grokking nature are the specific novelties.
3. In the LLM section, characterize the remaining 26–36% of mistakes beyond just carry errors. This would strengthen the connection to the small-model implementation.
4. Briefly discuss the role of the non-decision head in the second attention layer to complete the modular account.
5. Discuss the residual shortfall in corrected accuracy (e.g., C@1 pos7 = 0.86) — even a brief acknowledgment would improve transparency.

## Score and Decision

**Originality:** The modular decomposition of addition in small transformers is a worthwhile contribution. The "novel phase transition" claim is oversold, but the core mechanistic findings are solid.

**Importance of research question:** Understanding how transformers implement algorithmic computation is a central question in mechanistic interpretability. Addition is a canonical algorithmic task, and the carrying-over algorithm is clean enough to enable precise decomposition.

**Claims supported:** The core claims about two-layer models (modular decomposition, decision head, MLP carry execution, ~86 carry neurons) are well-supported by ablation experiments, PCA analysis, and neuron-level ablation. The length generalization and LLM claims are less strongly supported but appropriately caveated.

**Soundness of experiments:** The ablation methodology is sound, the task decomposition is well-designed, and the cross-validation via corrected accuracies is clever. The paper would benefit from more systematic cross-run analysis of attention head roles beyond just the ablation averages.

**Clarity of writing:** The paper is generally clear. The main technical claims are understandable. Some descriptions (e.g., the "trinary system" in the LLM residual stream, the squashing ratio) could be clearer.

**Value to the community:** The fine-grained task decomposition methodology and the neuron-level identification technique are likely reusable by other interpretability work. The mechanistic account of addition is a useful case study.

The paper's core contribution — a causally-supported modular account of how small transformers implement the carrying-over algorithm — is sound and well-executed. The weaknesses are structural gaps (missing limitations, undersupported novelty claim, thin LLM analysis) rather than flaws in the central claims. These are addressable in revision.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>