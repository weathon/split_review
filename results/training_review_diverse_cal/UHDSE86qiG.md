Now I have verified all the reviewer claims against the paper. Let me write the consolidated review.

## Summary

This paper studies the underexplored problem of applying multiple narrow task-vector (TV) edits simultaneously to the same model. It identifies two regimes of pairwise TV interaction (linear for similar tasks, non-linear for dissimilar tasks) and shows that at scale, control-task degradation becomes linear with the number of applied edits. After demonstrating that existing mitigation strategies (non-linear merging, per-TV weights, tangent-space TVs, joint training) fail to prevent this degradation, the paper proposes an adaptive inference-time selection method for diffusion models that applies a TV only when it is relevant to the prompt, achieving a better control-erasure trade-off than naive TV addition or co-training.

## Strengths

1. **Identifies two distinct regimes of pairwise TV interaction with a theoretical grounding.** Section 3.1 introduces a Gaussian toy model (Eq. 3–4) explaining why similar tasks produce linear degradation (shared mean dominates) while dissimilar tasks produce sub-linear degradation (covariance dominates). This goes beyond prior single-edit studies by offering a mechanistic hypothesis, empirically supported by the heatmaps in Figure 1 and the per-layer angular analysis.

2. **Demonstrates and theoretically accounts for linear control-task degradation at scale.** Figure 2 shows that accuracy on held-out CIFAR-100 classes drops linearly with the number of applied class-erasure TVs (up to ~15 vectors). The paper derives why the shared mean component dominates as N grows (Eq. 6–7), making linear interactions the dominant pattern — a scaling result not characterized in prior work.

3. **Systematic evaluation showing that four existing mitigation strategies all fail to prevent degradation at scale.** Section 4 tests non-linear merging (Tie/Sparse/Median), per-TV learned weights, tangent-space TVs, and joint co-training, with trade-off plots showing none sufficiently preserves control accuracy. This negative result concretely establishes the gap that motivates the adaptive method.

4. **Proposes a practical adaptive inference-time selection method with a reasonable idea.** The mid-process switch technique (applying TVs at time t_switch to measure relevance via CLIP similarity to the baseline) is a natural and clever approach. Figure 6 shows it achieves a better control-target trade-off than naive additive combination.

## Weaknesses

### Fatal
None.

### Major

1. **The headline quantitative claim (94.6% ROC AUC) in the abstract is unsupported by the reported data.** The abstract states "Our technique achieves a 94.6% ROC AUC in identifying the correct TV." Table 1 reports per-prompt ROC AUC values for six artistic styles. Verbatim from the paper's available text, none of these individual values equals 0.946, and no explanation is given for how 94.6% is derived — whether it is an average, a maximum, a result from a different experiment, or something else. The abstract's most prominent quantitative result cannot be verified from the evidence presented. This must be clarified or corrected.

### Minor

2. **Limited evaluation scope for the adaptive method.** The method is tested on only six artistic styles. The ROC AUC varies substantially across prompts (0.73 to 0.99), but the paper offers no analysis of why specific styles are harder (e.g., "Ajin: Demi-Human" at 0.73 vs. "Van Gogh" at 0.99). Understanding failure modes would strengthen the contribution and guide future work.

3. **Missing baseline that controls for number of applied TVs.** The comparison in Figure 6 pits the adaptive method (which applies a subset of TVs) against naive addition (which applies all TVs). A random-subset baseline (applying the same *number* of TVs selected at random) would disentangle whether the improvement comes from intelligent relevance detection or simply from applying fewer edits. Without this, the advantage over naive addition conflates selection quality with sparsity.

4. **No analysis of key operational details of the adaptive method.** The paper does not report: (i) how many TVs are typically selected per prompt, (ii) the degradation in target erasure when a relevant TV is missed, or (iii) how stable the selection is across different random seeds. These are all relevant to assessing whether the method is practically usable.

5. **Partial narrative disconnect between analysis and solution.** Sections 3–4 study degradation and mitigation using CLIP-based classifiers (CIFAR-100), while the proposed adaptive method targets Stable Diffusion. The paper mentions extending the pairwise analysis to diffusion in App.C, but the core scaling results (Figure 2) and mitigation experiments are classifier-only. This makes the bridge between the theoretical motivation and the diffusion-domain solution less direct than it could be.

### Trivial

6. **No acknowledgment of CLIP score limitations for evaluating diffusion quality.** The paper uses CLIP similarity between prompt and generated image as the diffusion quality metric, which is standard but known to be noisy. No human evaluation or discussion of this limitation is provided.

## Nice-to-Haves

- A random-subset baseline for the diffusion experiments (see Minor #3).
- Testing whether any mitigation methods from Section 4 (e.g., sparsification or co-training) also help for diffusion models, which would further contextualize the need for the adaptive method.
- Combining co-training with adaptive selection, as the reviewer reasonably notes.
- A failure analysis of low-ROC-AUC prompts to understand what makes a style hard to detect.

## Removed Points

The following points from the input reviews were removed with justification:

- **"Tab.2 for the time-switch ablation not present"** — REMOVED per rule: the parser strips appendices; Tab.2 exists in the original submission.
- **Criticism that the theoretical model is never quantitatively validated** — REMOVED per rule: the Gaussian model is a toy model providing intuition, and the paper does provide some empirical support (heatmaps, angular analysis). The request for a quantitative predictive test is a reasonable wish but presented as a stronger criticism than warranted.
- **Criticism about ambiguity in defining "correct TV"** — REMOVED per rule: the paper clearly states that for each prompt mentioning a specific artistic style, the correct TV is the one trained to erase that style. This is adequately described.
- **"The paper would benefit from comparing against co-training in the diffusion setting"** — MOVED to Nice-to-Haves. Figure 6 does include co-training as a baseline; the reviewer's concern that the gap is not quantified in practical terms is addressed in Minor #2-#3 above.
- **Generic strengths from the Strength Finder** — Filtered out per instructions: drop strengths that are generic or conflict with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The core finding — that multi-TV degradation is linear at scale because shared mean components dominate — is the paper's own novel insight, and the reviews do not add a genuinely new observation beyond what the paper already contains.

## Suggestions

1. **Reconcile the 94.6% ROC AUC claim with Table 1.** Either report where this number comes from (e.g., is it a macro-average over more prompts than those shown? A micro-average? A best-case result?) or correct the abstract to match the data actually presented.
2. **Add a random-subset baseline** to Figure 6 to separate selection quality from sparsity effects.
3. **Analyze the failure cases** — for styles where ROC AUC is low (0.73, 0.76), what distinguishes them from high-performing styles? Is it a limitation of CLIP embeddings, mid-process detection, or something else?
4. **Report the distribution of selected TV counts** across prompts, and show the effect of miss rate on target erasure.
5. **Bridge the classifier and diffusion analyses** by showing that the linear degradation pattern holds qualitatively for diffusion models (e.g., CLIP score vs. number of applied TVs, analogous to Figure 2), even if briefly in the main text.

## Score and Decision

The paper addresses a timely and genuine problem, provides solid (albeit asymmetric across model classes) analysis of multi-TV interactions, and proposes a clever adaptive selection method. However, the unsubstantiated 94.6% ROC AUC claim in the abstract is a significant reporting flaw that must be fixed, and the evaluation of the adaptive method has meaningful gaps (limited scope, no random-selection baseline, no failure analysis). The core scientific contributions — the scaling analysis and the demonstration that existing mitigation fails — are real and valuable. The paper is acceptable conditional on addressing the ROC AUC discrepancy and tightening the adaptive method evaluation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>