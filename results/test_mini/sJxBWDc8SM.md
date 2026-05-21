Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

My round-1 bracket: After comparing against the weak anchors (3.33, 4.00), middle anchors (4.50, 5.00, 5.50), and strong anchors (7.33+), I placed this paper between **4.5 and 7.0**. The relevant anchors in the 4.5-7.0 range (round-2) confirm the paper is better than the 4.00 rejection-level "Mechanistic evaluation" paper (which had novelty issues and weaker experimentation), comparable to the 5.00-5.50 accepted-poster papers, but below the 6.50+ theoretical papers with rigorous proofs.

The paper is clearly above reject-level work and clearly below Oral-level work. Within the accepted-poster band, it sits in the upper portion due to the thoroughness of the empirical investigation (3000+ runs, multiple architectures and tasks, clean ablations).

Final score: **5.5** — reflecting a solid empirical analysis paper with genuinely useful findings, slightly reduced by the rhetorical overclaim.

---

## Summary

This paper conducts a large-scale empirical comparison of SSMs (Mamba, Hyena, Mamba2, DeltaNet) and Transformers on multi-query associative recall (MQAR) and copying tasks. The core finding is that modern SSMs succeed only within an extremely narrow learning rate window, while Transformers are robust across a wide range—a fact that confounded prior comparisons where suboptimal tuning led to incorrect conclusions about SSM limitations. The paper further identifies opposing scaling preferences (SSMs favor width, Transformers favor depth), shows through careful ablation that the 1D convolution is the key architectural component enabling Mamba's 1-layer performance, and demonstrates that DeltaNet's Householder-based update rule largely resolves the stability problem.

## Strengths

1. **Large-scale, systematic evidence of optimization instability as a confounder.** The paper conducts over 3,000 runs across multiple architectures (Mamba, Mamba2, Hyena, DeltaNet, Attention) and two tasks (MQAR and copying). Figure 1 is particularly impactful: it directly overlays the learning rates used by prior influential work (Arora et al., 2023) as dashed vertical lines, showing they fall outside the narrow window where SSMs succeed. This goes beyond anecdotal claims of "LR sensitivity" to provide robust, multi-seed evidence.

2. **Clean ablation identifying the 1D convolution as the source of Mamba's 1-layer advantage (Table 2).** Removing the convolution from 1-layer Mamba drops accuracy from 99% to 2% (matching the 1-layer Transformer's 2%), while adding a convolution before QKV in a 1-layer Transformer raises accuracy to 99%. This precisely isolates the architectural component responsible and directly informs the expressivity vs. learnability debate.

3. **Opposing scaling preferences (width vs. depth) for SSMs and Transformers (Figure 4, Table 1).** The finding that SSMs benefit primarily from width while Transformers benefit from depth is clearly demonstrated and practically actionable. The copy task result (Table 1) is particularly clean: Mamba with 12 layers/width 1408 achieves 100%, while Mamba with 24 layers/width 1024 at the same parameter count achieves only 16%.

4. **Demonstration that DeltaNet resolves the optimization stability problem (Figure 7).** While diagnosing a problem is useful, showing that a concrete architectural variant (DeltaNet's Householder-based update) maintains high accuracy across nearly the full LR range provides a constructive path forward for the field.

## Weaknesses

### Fatal
None.

### Major

1. **The central thesis claim (line 43) overstates the role of optimization relative to architecture.** The paper states: *"Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics."* However, the paper's own ablation (Table 2) undermines this: a 1-layer Mamba *without* convolution performs identically to a 1-layer Transformer (both at 2%), while adding a convolution to the Transformer solves the task (99%). This shows that the performance difference in the 1-layer setting is driven by the presence/absence of a convolution—an architectural/expressivity difference, not primarily an optimization issue. The paper's own Section 7 correctly notes that *"in terms of raw expressivity, a 1-layer Mamba without convolution performs approximately identically to a 1-layer Transformer,"* which directly contradicts the strong claim in the introduction. The abstract and conclusion use the more defensible phrasing ("not just in their expressivity, but in their fundamental learnability"), so the fix is limited to recalibrating the strong claim on line 43. The paper's main empirical contributions remain valuable with this correction.

### Minor

1. **The induction head interpretation for the 1-layer Transformer loss bump is speculative and under-evidenced (Section 6).** The paper observes a loss bump in the 1-layer Transformer's training curve and hypothesizes it "resembles the formation of an induction head circuit" and that the model "attempts to form induction heads." There is no direct mechanistic evidence—no attention map visualizations, no probing, no comparison with known induction head signatures from Olsson et al. (2022). The paper uses appropriately hedging language ("resembles," "hypothesize"), and the observation is interesting on its own terms, but labeling it as induction-head-related without further evidence is a stretch. The paper could either add mechanistic analysis or simply describe it as a "loss phase transition of unknown origin."

2. **The paper attributes optimization brittleness to "vanishing and exploding gradients" (end of Section 1, Section 7) but never measures gradients.** This is a plausible hypothesis, and the paper acknowledges it as such, but the argument would be substantially strengthened by even a simple gradient-norm analysis across the LR grid. As-is, the gradient story is invoked but not directly evidenced.

3. **The claim that prior work "overlooked" optimization (Section 3) is somewhat imprecise.** The prior work (Arora et al., 2023) did perform some tuning (the dashed lines in Figure 1); the issue is that their grid was too coarse. "Underexplored" or "insufficiently tuned" would be more accurate.

### Trivial
None beyond the already-stated presentation issues.

## Nice-to-Haves

- A simple gradient-norm measurement across the LR grid would mechanistically link the narrow LR window to the vanishing/exploding gradient story the paper invokes.
- Confidence intervals (rather than relative max-min error) would be more informative, especially given the high variance at the edges of the LR window.
- A brief discussion of whether other hyperparameters (weight decay, Adam betas, gradient clipping) also contribute to the stability gap would provide useful context.

## Removed Points

The following points from the reviewers were removed with justification:

- **"Unfair comparison with other methods"**: The harsh critic's note about Transformer baseline tuning is removed because not substantiated—the paper does report Transformer performance across the LR grid (Figure 1, Figure 5) and Transformer is robust across a wide range.
- **"Missing hyperparameter details from appendix"**: The appendix was stripped by the parser; these details exist in the original submission.
- **"Code/reproducibility concerns"**: The paper states code is public; questions about undisclosed artifacts are nitpicks and removed per instructions.
- **Strength Finder's generic strengths**: Statements like "this paper addressed an important problem" are dropped as generic.
- **Formatting nitpicks about figure captions or text presentation**: These are parser artifacts.

## Novel Insights

The reviews surface one genuinely novel observation not fully articulated in the paper itself: the inherent tension between the paper's two central findings. On one hand, the paper shows the 1D convolution accounts for Mamba's 1-layer advantage (an expressivity difference). On the other hand, the paper argues the SSM-Transformer gap is about optimization, not expressivity. The reviews correctly point out that these two conclusions are in partial tension—the convolution finding is an expressivity result, and the optimization finding is about the 2-layer setting where both architectures can solve the task but SSMs need careful LR tuning. The paper would benefit from explicitly separating the two claims (1-layer vs. 2-layer regimes) rather than blending them into a single "optimization > expressivity" narrative.

## Suggestions

1. **Reframe the strong claim on line 43** to match what the evidence actually supports. The paper's own results show that *both* architecture (convolution) and optimization (LR sensitivity) matter; the "not in terms of expressive power" framing should be replaced with something like "the performance gap is substantially attributable to optimization instability, and the specific architectural component responsible for 1-layer expressivity is the 1D convolution."
2. **Either strengthen or remove the induction head speculation** in Section 6. If practical, add attention map visualizations or copy-score analysis. Otherwise, describe the loss bump as a "phase transition of unknown origin."
3. **Add a gradient-norm analysis** (even a small-scale one) to support the vanishing/exploding gradient hypothesis that the paper invokes.
4. **Separate the 1-layer and 2-layer conclusions more explicitly** in the discussion, since the paper's evidence tells different stories in these two regimes.

## Score and Decision

**My score bracket reasoning:**

**Round 1 (bracketing):** Queried for similar papers with score <3.5, 3.5–7.5, and >7.5. The weak-band anchor "On the Recall Scaling Laws in Mamba" (3.33, Reject) and "Mechanistic evaluation of Transformers and SSMs" (4.00, Reject) are both on closely related topics but are clearly weaker than the paper under review—the former had presentation issues and limited scope, the latter had novelty concerns and less thorough experiments. The strong-band anchors (7.5+) are Oral-level papers that are qualitatively different (new methods, novel theory). The paper clearly sits in the middle band.

**Round 2 (narrowing):** Compared against "A Theoretical Analysis of Mamba's Training Dynamics" (5.00, Accept Poster), "Expressive Limits of Diagonal SSMs" (5.50, Accept Poster), "Memory Determines Learning Direction" (4.50, Reject), and "Learning to Recall with Transformers" (6.50, Accept Poster). The paper under review is empirically stronger than the 5.00 Mamba-training-dynamics paper (which was limited to a single simplified layer and binary classification) and comparable to the 5.50 Expressive Limits paper (which had strong theory but weaker empirical scope). The paper is clearly below the 6.50 theoretical paper. This narrows the score to the 5.0–6.0 range.

**Final calibration relative to anchors:**
- "Mechanistic evaluation of Transformers and SSMs" (4.00): This paper on a very similar topic was rejected due to insufficient novelty and weaker experimentation. Our paper is clearly stronger (more thorough experiments, cleaner evidence, actionable findings).
- "A Theoretical Analysis of Mamba's Training Dynamics" (5.00): Accepted poster. Our paper is at least as strong empirically, with broader architecture coverage and more actionable findings.
- "Expressive Limits of Diagonal SSMs" (5.50): Accepted poster. Our paper is of comparable quality—both have clear contributions and well-supported claims, but ours has a rhetorical overclaim that slightly reduces the score.
- "Learning to Recall with Transformers Beyond Orthogonal Embeddings" (6.50): Stronger theoretical contribution with solid experiments. Our paper is weaker on the theoretical side.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>