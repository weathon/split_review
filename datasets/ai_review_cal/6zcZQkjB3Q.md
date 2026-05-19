- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3
Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes iReVa, a method for traceable model editing that inserts explicit key-value adaptors into the MLP blocks of GPT-like transformers. Each edit gets its own dedicated key-value neuron, enabling per-edit identification, activation control, and withdrawal. The method is evaluated on zsRE and PARAREL benchmarks with GPT2-XL and other models, showing strong edit success while preserving specificity, along with a demonstrated knowledge withdrawal capability.

## Strengths

- **Traceable, per-edit storage is a clear architectural contribution.** By initializing separate key-value pairs in the MLP block for each edit (Section 4.1) and freezing prior edits during sequential training (Section 4.2, line 130), iReVa achieves an explicit indexing of edits that no other batch editing method provides. This is a genuine advance over methods that merge edits into weight updates.

- **Knowledge withdrawal is demonstrated at scale.** Section 6.2 shows that by simply inhibiting the corresponding inserted neuron, iReVa recovers the original model output with near-perfect Retrieve Success and Consistency on zsRE-10K (Table 2). While the additive architecture makes this plausible, executing it cleanly across 10K edits without interference from fine-tuning is a non-trivial validation.

- **Strong empirical results on standard benchmarks.** Table 1 shows iReVa achieving high Edit Success (near 100%) and competitive Paraphrase Success and Neighborhood Success on both zsRE-10K and PARAREL-10K, outperforming all baselines on the composite Score metric. The ablation study (Table 3) confirms that the proposed activation function, max-pooling, and loss terms all contribute meaningfully to performance.

- **Robustness to batch size and layer choice.** Figure 3 shows that iReVa maintains high performance across edit counts from 1 to 10K, while ROME collapses and MEMIT plateaus well below. Figure 2 demonstrates that iReVa works across many layers, unlike ROME/MEMIT which peak in specific middle layers.

## Weaknesses

### Major

- **Several important contemporary baselines are missing.** GRACE (Hartvigsen et al., 2023) is mentioned in Section 6.2 but not included as an experimental baseline, even though it is a structurally similar memory-augmented method that supports forgetting. SERAC (Mitchell et al., 2022) is another scope-based editing method with explicit per-edit representations that should be compared against. The paper's description of baselines that "support batch editing" (Section 5.2) includes ROME (designed for single edits) and MEMIT (designed for batch editing), but omitting GRACE and SERAC weakens the claim of superiority over SOTA. The exclusion of T-Patcher is justified (encoder-decoder only), but the gap remains for decoder-compatible memory-based methods.

- **The max-pooling mechanism and its handling of conflicting edits are unanalyzed.** During inference, a single key with the highest matching score is selected (Equation 12, line 140). The paper does not analyze scenarios where edits overlap or contradict (e.g., "the capital of France is Paris" followed by "the capital of France is Lyon"). The argmax selection prevents parallel activation of multiple relevant edits, and there is no discussion of how the model behaves when two edits have nearly identical match scores for the same input. This is a significant gap for a method claiming "traceable" editing—traceability requires predictable behavior under edit conflicts.

- **Model generalization (Table 4) lacks a clear comparison setup.** The text in Section 6.5 states "iReVa can achieve the best average score on all LMs" for GPT2-LARGE, GPT-NEO-2.7B, and GPT-J-6B, but does not specify which baselines were re-run on these models. If the comparison is only against "no editing" or an incomplete set of baselines, the claim of generality is not properly supported. This needs clarification.

- **Key hyperparameters are set without sensitivity analysis.** The margin θ is chosen per-dataset (0.75 for zsRE, 0.65 for PARAREL) with no ablation. The scaling factor α = 0.2 and loss coefficients a = b = 1e-3 are fixed. While the ablation in Table 3 tests the binary presence/absence of L_rec and L_irr (by setting a=0 or b=0), it does not explore the range of these coefficients or the margin θ. Without this, it is unclear whether the method is robust or requires careful per-dataset tuning.

### Minor

- **The knowledge withdrawal test, while useful, is partially expected from the architecture.** Because each edit is stored as an additive neuron separate from the original weights (Equation 5), inhibiting it mechanically removes its contribution. That the retrieval works at near-perfect rates (Table 2) is a positive validation, but the paper overstates this as a "first attempt" (Section 6.2, line 203) without acknowledging that any additive method trivially supports deletion of its added component.

- **PARAREL dataset construction details are vague.** The paper states it "selected those sentences that end with [MASK] token" (Section 5.1, line 155) but does not report what proportion of PARAREL is usable, how paraphrases and neighborhoods are constructed, or how many irrelevant NQ examples are sampled. This limits reproducibility.

- **No variance or statistical significance reporting.** All results appear to be single-run. While near-ceiling metrics (ES ≈ 100%) may be deterministic, baseline variance matters for assessing the significance of the reported 9%/6% improvements.

### Trivial

- **Garbled text in the abstract and introduction.** Line 4 says "Evident suggests" (should be "Evidence suggests"). Line 16 has "around 9% 9% 6% and 6% average score improvement" — these are parser artifacts from the PDF extraction. The original submission likely does not have these issues, but they appear in the review copy.

## Nice-to-Haves

- A sensitivity analysis on θ (margin), α (scaling factor), and the loss coefficients a, b would strengthen the paper significantly.
- Replacing max-pooling with a soft, differentiable attention-weighted mechanism would better support the "traceable" claim and remove the training/inference mismatch (Section 4.3 notes max-pooling is excluded during training because it "impedes back-propagation").
- An analysis of edit conflicts (similar inputs with different target outputs) would strengthen the traceability claims.
- Reporting results with variance over multiple seeds.

## Removed Points

These points from the harsh critic are flagged for removal — treat them with caution:

- **"MEMIT scales to hundreds but not thousands"** — Factually wrong. MEMIT (Mass Editing Memory in a Transformer) was explicitly designed for editing thousands of facts. The paper's use of MEMIT at 10K is within its intended operating regime.
- **"Baseline comparison is fundamentally unfair, invalidating the main performance claim"** — Overstated. While ROME is designed for single edits (a valid concern), the paper includes multiple batch-editing baselines (MEMIT, MEND, MELO, FT) that are appropriate. The critic's claim that the 9%/6% improvement "may simply reflect that the baselines were evaluated outside their operating regime" relies heavily on the incorrect claim about MEMIT.
- **"Knowledge withdrawal test is a trivial property of the architecture"** — Overstated. While the additive architecture enables withdrawal, the fine-tuning process (L_rec, L_irr) can distort key vectors, and interference between 10K edits could cause failures. The near-perfect results are a worthwhile empirical validation, not a tautology.
- **"The method only works at the last layer"** — Contradicted by Figure 2, which shows iReVa performing well across all tested layers (1–47).
- **"l is defined ambiguously (layer vs. token length)"** — The paper explicitly defines l as "averaged length of target tokens" with concrete examples (l̄=2.69 for zsRE, l=1.15 for PARAREL) at line 214.
- **"The notation is inconsistent: Equation 1 uses h_l and i_l in non-standard ways"** — The notation is standard for Transformer MLP blocks (h for hidden states, i for output after self-attention+layer norm).
- **"Table 4 likely compares only to 'no editing'"** — Pure speculation. The text says "iReVa can achieve the best average score on all LMs" implying comparison exists, though the setup is indeed unclear and this lack of clarity is retained as a Major weakness above (re-framed properly).

## Novel Insights

None beyond the paper's own contributions. The harsh critic's section-by-section notes add little beyond what is already in the paper, and the strength finder's observations largely restate the paper's own claims. The most useful insight to emerge from this review process is that the paper's strongest novelty (traceable per-edit storage enabling withdrawal) comes with an under-analyzed weakness: the max-pooling gating mechanism may fail under edit conflicts, and the additive architecture is less impressive for withdrawal than the paper frames it. Neither reviewer articulated this tension precisely, but the combination of the two reviews reveals it.

## Suggestions

1. Add GRACE and SERAC as baselines, or clearly justify their exclusion given their relevance.
2. Include an analysis (qualitative or quantitative) of how the max-pooling mechanism handles conflicting or similar edits.
3. Clarify the comparison setup for Table 4: which baselines were evaluated on GPT2-LARGE, GPT-NEO-2.7B, and GPT-J-6B?
4. Add a sensitivity analysis for the margin θ and the scaling factor α.
5. Tone down the "first attempt" language around knowledge withdrawal, and more clearly distinguish the architectural advantage from the empirical validation.
6. Report dataset statistics for the PARAREL construction (how many examples usable, how many NQ samples used).
