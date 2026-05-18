Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper addresses extrapolation in material property regression (MPR), an important and understudied problem. It makes three contributions: (1) a dedicated extrapolation benchmark of seven tasks from Matminer, constructed via non-i.i.d. splits that place extreme label values in test/validation sets; (2) a systematic evaluation of existing deep imbalanced regression (DIR) and data augmentation methods on these tasks, revealing their limitations; and (3) the Matching-based EXtrapolation (MEX) framework, which reframes regression as a material-property matching problem using cosine similarity and NCE-based relative ranking, showing improved performance over baselines.

## Strengths

- **Principled extrapolation benchmark with well-motivated non-i.i.d. splits.** The paper constructs seven tasks by placing the top/bottom 15% of label values into test/validation sets, directly targeting the extrapolation setting that random splits ignore. This is clearly described (Section 4.1, Table 1, Figure 3) and fills a gap in MPR evaluation.

- **MEX achieves SOTA extrapolation performance across multiple backbones and metrics.** MEX attains the best or second-best MAE on 5/7 (PaiNN) and 6/7 (EquiformerV2) datasets, with similarly strong Geometric Mean results (Tables 2, 3). The consistent improvement over strong DIR baselines like BalancedMSE supports the claim that reframing regression as matching is effective for extrapolation.

- **Comprehensive benchmarking of existing extrapolation-relevant methods.** The paper evaluates four DIR methods, two data augmentation methods, and ERM under two backbone architectures and two metrics, showing that no prior method dominates and empirically grounding the claim that existing approaches are insufficient for MPR extrapolation (Section 4.3).

- **Detection capability analysis tied to the material discovery workflow.** The recall-rate evaluation (Section 4.4, Figure 5) goes beyond regression error to measure how well methods identify promising extrapolation candidates — a practically relevant metric. MEX exceeds 80% recall on three datasets and 60% on six, demonstrating practical utility.

- **Ablation on score module design and sensitivity to the trade-off parameter.** Table 4 and Figure 6 investigate design choices for the score module and the loss-balancing parameter λ, grounding the architectural decisions (Section 4.5).

## Weaknesses

### Major

- **The candidate label range is set using test-set bounds, giving the method an unrealistic advantage.** During inference, the candidate label set is sampled uniformly from [l, u] where l and u are "the lower bound and upper bound of the entire dataset label range" (line 135). In the benchmark setup, the test set contains the extreme 15% of values, meaning the global range is determined by the test labels. This means the search space is guaranteed to cover the correct answer — a luxury unavailable in genuine extrapolation where the test distribution is unknown. The paper notes the range "can be freely adjusted based on prior knowledge" (line 135), but the experiments as conducted use test-set bounds. A fair evaluation would either (a) fix the range from training data alone, or (b) treat the interval as a hyperparameter and study sensitivity. Without this, the reported results may overstate MEX's real-world extrapolation ability.

- **The NCE training may inadvertently penalize labels in the extrapolation region.** The noise distribution q(y|y_i) is a mixture of Gaussians with σ up to 0.3 (line 135). For training samples near the boundary of the training range, the tails of these Gaussians can extend into the extrapolation region (which lies at the extreme ~15% of the label distribution). Since the NCE loss pushes down scores on noise samples, the model is trained to disfavor labels that it later needs to assign high matching scores to at inference. The paper neither analyzes the overlap between the noise distribution and the extrapolation region nor discusses this potential conflict. While the empirical results suggest the problem may not be severe in practice, the absence of any analysis makes this a blind spot in the method's credibility.

- **The inference procedure is underspecified for reproducibility.** Section 3.2.2 describes the inference only as a "Monte Carlo sampling-based stochastic optimization method" that "iteratively refine[s] a candidate label set … based on probabilistic evaluations" (line 103). No concrete algorithm, pseudocode, or update rule is provided. Key questions — how candidates are updated, what the "probabilistic evaluations" entail, how exploration and exploitation are balanced — are unanswered. Without this, the method cannot be independently reimplemented. This is a structural gap for a paper whose core contribution is a method.

### Minor

- **The NCE noise-sample tails and the candidate-range issue both highlight the lack of a limitations section.** The paper would benefit from explicitly acknowledging its dependence on knowing a plausible label range and discussing the potential conflict in the NCE training objective, which would help readers evaluate the method's applicability boundaries.

### Trivial

- None that survive filtering (the paper is generally well-written and the parser-level artifacts are not author errors).

## Nice-to-Haves

- An ablation that replaces the inference-time search with a simpler prediction (e.g., nearest-neighbor label in the training set based on learned similarity) would isolate whether the matching *representation* or the inference *optimization* drives the extrapolation improvement.
- A sensitivity study of the candidate range (e.g., using training-range bounds plus a buffer, or varying the interval width) would address the candidate-range concern more directly than text alone.
- Pseudocode or an algorithmic description of the inference update rule would resolve the reproducibility gap.

## Removed Points

- The harsh critic's claim that "the noise contrastive training *may actively harm* extrapolation" is kept (see above), but the suggestion that this "could undermine the whole extrapolation objective" is softened — the empirical results show MEX works, so the concern is a theoretical blind spot rather than a demonstrated flaw. The claim is kept as a Major weakness because the paper should analyze this; the stronger language about it "undermining the whole objective" is dialed back to fit the evidence.

- The "missing Limitations section" ask is moved to Minor (addressed-above) rather than a standalone Critical Issue.

- The suggestion to add an ablation "that replaces the inference-time search with a simpler prediction" is moved to Nice-to-Haves — it would strengthen the paper but is not a flaw in the current work.

## Novel Insights

None beyond the paper's own contributions. The reviews identify genuine weaknesses (candidate-range information leak, NCE extrapolation conflict, underspecified inference) but do not reveal structural insights about the problem or method that the paper itself misses.

## Suggestions

1. **Fix the candidate-range evaluation.** Either restrict the candidate range to the training-label bounds (or training-range-plus-small-buffer) and compare results, or provide systematic sensitivity analysis across different interval widths.
2. **Analyze the NCE noise distribution.** Report whether noise samples ever fall in the extrapolation region for each dataset and, if so, discuss the potential effect on training and whether any mitigation (e.g., truncating the noise distribution) was considered.
3. **Provide a concrete inference algorithm.** A pseudocode block or formal update rule for the candidate refinement would resolve the reproducibility gap.
4. **Add a limitations section** acknowledging the dependence on a plausible label range and the potential NCE conflict discussed above.

## Score and Decision

The paper addresses a genuinely important problem, constructs a useful benchmark, and proposes a novel framework with strong empirical results. However, the candidate-range issue calls into question whether the reported advantage is fully attributable to the method's design rather than an artificially favorable evaluation setup. Combined with the underspecified inference procedure and unanalyzed NCE extrapolation conflict, these weaknesses are significant but fixable. The benchmark and systematic evaluation of existing methods are valuable contributions that stand independently. With the candidate-range issue resolved and the inference procedure clarified, the paper would be solid.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>