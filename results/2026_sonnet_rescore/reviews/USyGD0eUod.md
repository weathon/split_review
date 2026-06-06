## Summary

This paper tests whether standard SAE evaluation metrics (auto-interpretability AUROC, reconstruction quality) can distinguish transformers trained on language data from randomly initialized variants. Across five Pythia model sizes (70M–6.9B), multiple randomization schemes, and two auto-interpretability pipelines, the paper finds that aggregate metrics largely fail to discriminate the two settings. Token distribution entropy is proposed as a complementary measure that reveals qualitative differences in feature abstractness that the aggregate metrics miss. The paper recommends treating common SAE metrics as insufficient on their own and argues for routinely including randomized baselines.

---

## Strengths

- **Systematic empirical coverage supporting the core claim**: The finding that fuzzing AUROC and reconstruction metrics (explained variance, cosine similarity) overlap substantially between trained and randomized models is demonstrated consistently across Pythia-70M through -6.9B and across multiple randomization schemes, shown in Figures 1 and 2. This is not a cherry-picked result.

- **Gaussian control validates metric sensitivity**: The i.i.d. Gaussian token-embedding control yields near-chance AUROC (≈0.50, Figure 1) and consistently lower reconstruction quality (Figure 2, black lines), which confirms that the metrics are not simply uninformative for any model—they fail specifically in the trained-vs.-random comparison, not universally.

- **Token distribution entropy reveals qualitative divergence**: Figure 2 (bottom row) and Section 3 show that randomized-model latents cluster on a small number of token IDs (low entropy) while trained-model latents become progressively more abstract across layers. This is concrete evidence that aggregate scores mask an important qualitative difference, and the entropy measure is an actionable, low-cost diagnostic.

- **Multiple randomization schemes isolating distinct factors**: The three randomized conditions (Step-0, re-randomized incl./excl. embeddings) are not equivalent: the paper shows (Section 3) that re-randomized variants—which preserve trained weight-norm statistics—align more closely with the trained model than Step-0 on several metrics, especially L1 norm in larger models. This nuanced finding adds depth to the core result.

- **Careful positioning relative to prior work**: The paper acknowledges that Bricken et al. (2023) found discrimination effective for one-layer transformers and that Karvonen et al. (2024c) found discrimination effective for chess data; it provides principled explanations for both and shows the gap narrows with model scale (Section 2, Section 3). This demonstrates a nuanced interpretation of boundary conditions.

---

## Weaknesses

### Fatal
None.

### Major

- **Framing of "similar" scores obscures a directional failure that is more informative than the stated claim.** Figure 1 shows that for Pythia-6.9b, the randomized variants (AUROC ≈ 0.87–0.88) consistently *outperform* the trained model (AUROC ≈ 0.79) on fuzzing. This is not captured by the abstract's phrasing that scores are "similar." The actual failure mode is anti-calibration: metrics systematically reward the token-specific, high-apparent-sparsity features that randomly initialized networks produce, yielding *higher* scores than for trained models. This distinction matters for how practitioners should interpret a high auto-interpretability score—not merely as uninformative, but as potentially misleading. The paper surfaces the relevant evidence (token entropy shows randomized latents are more token-specific; Section 3, final paragraphs), but never explicitly ties the AUROC reversal to this mechanism. Connecting these observations—that higher AUROC for randomized models arises precisely because token-specific features are easy for the classifier to confirm—would sharpen the paper's argument considerably and would not require new experiments.

### Minor

- **"AUROC (Pruned)" is undefined in the main text.** Figure 2 uses "AUROC (Pruned)" as its primary auto-interpretability metric label, but the pruning criterion is not explained in the main text. For a paper whose core claim rests on this score, this is a real readability gap. Readers should be able to understand the primary metric without consulting the appendix.

- **The "Re-randomized excl. embeddings" condition deserves more analytical focus.** This condition—pre-trained embeddings, fully randomized transformer weights—achieves AUROC nearly as high as the fully trained model and nearly matches the "incl. embeddings" and "Step-0" variants. This is the condition that most cleanly isolates whether the result is driven by input statistics (embedding geometry) versus learned computation in transformer weights. The paper treats it symmetrically with other conditions throughout but does not leverage it as the primary lens for diagnosing what is driving the failure. Even a short discussion comparing "incl." vs. "excl." embeddings on entropy and AUROC simultaneously would help.

- **100-latent sample size and variance not foregrounded.** For expansion factor 64 on Pythia-6.9b, the SAE may contain tens of thousands of latents; sampling 100 per SAE for auto-interpretability scoring is a small fraction. The paper references Appendix E for multiple seeds, but a brief summary of sampling variability belongs in the main results section, since the core claim rests on score similarity across conditions.

### Trivial

- **Abstract and throughout: "similar" vs. "often equal or higher."** The abstract states randomized models produce scores "similar to those from trained models." In Figure 1, the randomized variants consistently *exceed* the trained model's AUROC. A one-sentence clarification in the abstract would more accurately represent what was found.

---

## Nice-to-Haves

- The 1B-token results (Appendix C) confirming robustness to SAE training data size should be briefly mentioned or summarized in the main body—it is a relevant robustness check for the core claim.
- The toy model section (Section 4) could be compressed to what it actually demonstrates statistically, rather than what a single example suggests. Figure 3 is illustrative, not a statistical characterization. Section 4.3's GloVe results (narrow gap vs. Gaussian control) are genuinely interesting—the observation that random MLPs "sparsify" both GloVe and Gaussian inputs to a similar degree deserves slightly more prominence.
- The contrast between the chess-data result (Karvonen et al. 2024c, where discrimination works) and the language-model result (where it fails) is one of the more informative boundary conditions in the paper and warrants a slightly more prominent treatment in the discussion—the sparsity-alignment hypothesis is plausible but asserted.
- Token distribution entropy is framed as measuring "abstractness," but it specifically measures token-specificity. A feature activating on many past-tense verbs would have high entropy but remain lexically shallow. The paper appropriately calls this "preliminary," but an explicit acknowledgment that entropy ≠ abstractness would clarify the scope of this diagnostic.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: Toy model section adds "less than it could" / Figure 3 rests on a single illustration.** The paper explicitly frames Section 4 as speculative motivation, not a formal characterization ("we leave the question…to future work"). Given this framing, holding Figure 3 to a statistical standard is scope creep. *Removed as framing-appropriate.*

- **Harsh Critic: SAE training data size (100M vs. 1B) should appear in main body.** Moved to Nice-to-Haves since it is a robustness check, not a gap in the core claim.

- **Harsh Critic: Token entropy does not fully capture "abstractness."** The paper already acknowledges this: "the token distribution entropy is not a direct measure of 'abstractness'" (Section 3). Keeping it as a Nice-to-Have clarification rather than a weakness. *Removed as already addressed.*

- **Strength Finder Strength 3 (toy models as mechanistic explanation):** The harsh critic correctly notes the toy model is speculative and single-illustrated. The toy model section is framed as "plausibility" evidence, which is appropriate, but it does not constitute a verified mechanistic explanation. *Demoted to supporting context rather than a core strength.*

- **Harsh Critic: Comparison with Karvonen et al. chess result is asserted rather than demonstrated.** This is true but is explicitly in the limitations zone—the paper does not claim to explain the chess/language divergence, only to note it. *Moved to Nice-to-Haves.*

---

## Novel Insights

The most pointed observation—one that neither the paper nor the reviewers fully exploit—is that the failure of these metrics is *directional*: randomized models do not merely match trained models on auto-interpretability; they frequently *exceed* them. This implies the metrics are not merely noisy but are actively biased toward token-specific, superposition-preserving features that random networks produce more of. Paired with the token entropy finding that randomized latents are concentrated on fewer token IDs, this suggests a precise causal story: auto-interpretability pipelines based on fuzzing reward explanations that identify a single token or small token class, which is exactly what random networks learn to encode—making the evaluation task easier, not harder, for the null model. Surfacing this as the primary failure mode (rather than generic score similarity) would significantly sharpen the paper's contribution.

---

## Suggestions

1. **Reframe the abstract and introduction to foreground the directionality finding**: Replace "similar scores" with language that captures the reversal—randomized models often score *above* trained models—and identify this as the primary concern, not just score indistinguishability.
2. **Add a paragraph explicitly connecting the AUROC reversal to the token-entropy result**: Show that conditions with lower token entropy (randomized variants) have higher AUROC, and argue this is the mechanism by which the metric fails. This does not require new experiments.
3. **Define "AUROC (Pruned)" in the main text**: A single sentence explaining the pruning criterion would resolve the readability gap.
4. **Add a sentence in Section 3 comparing "excl. embeddings" vs. "incl. embeddings" on entropy**: This would clarify whether the effect is primarily driven by embedding geometry or by architectural properties of transformer weights.
5. **Summarize Appendix E seed variance in the main results section**: A brief statement of the variability across 100-latent samples would increase confidence in the similarity finding.

---

## Evaluation on Key Axes

- **Originality**: Applies an established sanity-check paradigm (Adebayo et al., 2020) to SAE evaluation in mechanistic interpretability—a timely and targeted application. Not a methodological breakthrough, but a well-scoped empirical contribution.
- **Importance of research question**: High. Auto-interpretability metrics are widely used to validate SAE features; showing they fail a basic null-model test has direct and immediate implications for the field.
- **Claims well-supported**: Yes, for the core claim. The directional aspect is underemphasized but the data exists. Toy model claims are appropriately hedged.
- **Soundness of experiments**: Good. Multiple model scales, multiple randomization schemes, a principled control, and robustness checks on SAE hyperparameters. Minor concerns about sample variance.
- **Clarity of writing**: Adequate. The main methodological presentation is clear; the undefined "AUROC (Pruned)" label and the soft framing of the directionality finding reduce clarity at key moments.
- **Value to research community**: High. This is a concrete, actionable warning for practitioners using standard SAE evaluation pipelines, with a practical recommendation (use randomized baselines; supplement with token-entropy diagnostics).

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>5</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>5</community_value>
</subscores>