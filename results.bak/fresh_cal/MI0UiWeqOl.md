Now I have all the information needed. Let me construct the consolidated review.

## Summary

The paper proposes Poly-Autoregressive (PAR) modeling, a framework for multi-agent prediction that operates via same-agent next-timestep prediction (rather than next-token prediction) using learned agent identity embeddings and joint training across agents. It applies a single 4.4M-parameter transformer decoder architecture without architectural changes to three case studies: social action prediction (AVA), car trajectory prediction (nuScenes), and object pose estimation during hand-object interaction (DexYCB). The core contribution is the claim that a single simple framework can unify these seemingly different problems.

## Strengths

- **Principled ablation validates the two key PAR components**: Table 1a shows that removing either the next-timestep prediction or the learned agent ID embedding causes the multi-agent model to underperform the single-agent AR baseline, while adding both yields a +1.8 mAP gain. This cleanly demonstrates that the two proposed design choices are jointly necessary.

- **Consistent improvement over single-agent AR across all three tasks**: PAR outperforms the single-agent autoregressive baseline on AVA action prediction (+1.8 mAP), nuScenes car trajectory prediction (lower ADE/FDE with acceleration tokens), and DexYCB object pose estimation (lower geodesic distance and translation MSE). This supports the generalization claim.

- **Per-class analysis pinpoints interaction-driven gains**: Figure 3 shows large absolute mAP gains specifically on inherently multi-person action classes (listen to: +7.8, kiss: +6.6, hand shake: +6.4, fight/hit: +6.2), providing direct evidence that modeling other agents is what drives improvement for interactive behaviors.

- **Identical core architecture across all experiments**: The same 8-layer, 8-head, 128-dim Llama decoder (~4.4M parameters) is used in all three case studies, with only the learning rate changing. This demonstrates that the framework does not require task-specific architectural engineering at the model level.

## Weaknesses

### Fatal
None.

### Major

- **No comparison against any existing task-specific method on any benchmark**: The paper compares only against trivial baselines (random token, nearest neighbor, mirror) and the single-agent AR ablation. For AVA, no comparison to prior action forecasting methods (e.g., LART, relational forecasting). For nuScenes, no comparison to MotionLM, Wayformer, or any modern trajectory predictor. For DexYCB, no comparison to prior 6D pose tracking methods. The paper's central claim is that PAR is a useful unifying framework, but without situating its performance relative to established methods on any of the three tasks, the reader cannot assess whether the framework is actually competitive or useful in practice. This does not mean the paper must achieve SOTA, but at least one comparison per task to calibrate the reader is necessary to support the claim of utility.

- **DexYCB evaluation uses teacher-forced hand ground truth during validation**: The paper states "hand joint information teacher-forced in validation while generating the object's rotation or translation" (Section 6.1). During autoregressive generation, the model receives ground truth hand joint positions at each step rather than predicting them. This makes the setting substantially easier and less realistic—the hand should also be predicted autoregressively for a fair evaluation. The reported gains may significantly overstate the benefit of the PAR approach in a fully autoregressive setting.

### Minor

- **"No modifications" claim is contradicted by the LPE addition**: The abstract, introduction, and Section 3.3 repeatedly state the framework applies "without any modification" across tasks. However, Section 5.1 adds a location positional encoding (LPE) for the car trajectory case that is not used in the other two tasks. The paper acknowledges this is necessary because the model "needs to reason over this second modality of location." While the core architecture (8-layer Llama decoder) remains unchanged, the LPE is a task-specific input encoding not present in the other experiments, which weakens the "no modifications" framing. The claim should be refined to "no architectural modifications" with task-specific input encodings as acknowledged exceptions.

- **No statistical rigor**: No error bars, standard deviations, or confidence intervals are reported for any result. The modest AVA gain (+1.8 mAP) and the nuScenes improvements could be within noise of a single run. Multiple seeds with variance estimates are needed.

- **MSE loss on binary action vectors without output constraints**: For AVA, 80-dimensional binary action vectors are predicted with an MSE regression loss and no constraint to [0,1]. Binary cross-entropy or a sigmoid-based loss would be more natural for multi-label binary prediction. The paper does not discuss this design choice.

### Trivial

- Section 6 (DexYCB) refers to "Figure 8" for quantitative results on rotation prediction, but the preceding sections reference Figures 1–7, suggesting a labeling inconsistency in the text (the table reference appears earlier as Table 3).

## Nice-to-Haves

- An ablation varying the number of agents (e.g., comparing 2-agent vs. 3-agent PAR on nuScenes) would strengthen the analysis.
- A discussion of inference speed and compute cost relative to the small model size would be useful context.
- For AVA, splitting evaluation into social vs. non-social action classes would directly test the hypothesis that PAR helps specifically for interactions.

## Removed Points

- **"NN outperforms 3-agent PAR without LPE on nuScenes" (Harsh Critic)**: Factually incorrect. The paper states that both PAR w/o LPE variants outperform AR, and AR with acceleration tokens (ADE 1.87, FDE 4.54) already beats NN (ADE 2.21, FDE 5.62). The critic's specific numerical claim (~5.52) does not match any reported value. **Removed as factually wrong.**

- **"Paper does not discuss how PAR differs from MotionLM" (Harsh Critic)**: The paper explicitly discusses MotionLM in Section 2 (Related Work), noting it as informing the methodology and distinguishing PAR as a unified framework spanning multiple problem domains rather than a single-application method. **Removed as factually incorrect.**

- **Criticism about missing appendix content or undisclosed hyperparameters**: The parser strips appendix sections; they exist in the original submission. **Removed per hard rules.**

- **Criticism that baselines provide "zero information" about PAR's utility**: The single-agent AR comparison directly tests the paper's core hypothesis (whether multi-agent information helps). This is informative, not "zero information." The criticism about missing comparisons to external methods is retained as a Major weakness. **Removed the "zero information" framing as inaccurate.**

- **"Novelty over prior unifying frameworks not established" (Harsh Critic)**: This is too vague and speculative to include as a concrete weakness. The paper's claim is that no prior work unifies multi-agent regression across diverse problem types. If the reviewer believes otherwise, a specific citation is needed. **Removed as unsupported speculation.**

- **Generic strengths from Strength Finder**: Several generic strengths ("this paper addressed an important problem") are dropped as they lack specificity to this paper's contributions. Only strengths with concrete evidence anchors are retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add comparisons to at least one established method per task (even if PAR does not beat them) to calibrate readers on where the framework sits relative to specialized approaches.
2. For DexYCB, report results where the hand is also predicted autoregressively (not teacher-forced), or clearly scope this as a setting where hand observations are available at each timestep.
3. Reframe the "no modifications" claim to "no architectural modifications" and acknowledge task-specific input encodings as a deliberate part of the framework's flexibility.
4. Provide error bars (3+ seeds) for key results, especially the modest AVA gain.
5. Justify the MSE loss choice for binary action vectors, or switch to binary cross-entropy.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>