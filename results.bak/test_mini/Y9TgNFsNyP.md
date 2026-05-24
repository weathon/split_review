## Summary

This paper introduces FF-Erase, the first machine unlearning framework specifically designed for Forward-Forward (FF) models, and G-MIA, a goodness-based membership inference attack for verifying unlearning. FF-Erase addresses the unique challenge that gradient ascent (the standard unlearning approach for BP models) causes catastrophic collapse in FF models due to their layer-wise independent training and sensitivity to parameter tuning. The method uses a guidance model to provide stable target goodness distributions and shifts the model's goodness scores via KL divergence. The companion verification method G-MIA leverages the fact that FF models natively output per-layer goodness vectors during inference. Experiments on multiple datasets and architectures demonstrate that FF-Erase achieves comparable unlearning effectiveness to retraining from scratch while being 1.9–3.1× faster.

## Strengths

- **First formalization of a genuinely new problem.** The paper correctly identifies that no prior work addresses unlearning for FF models and provides concrete evidence (Figures 4–5) that standard gradient ascent either collapses the model or fails to forget. This establishes both the novelty of the problem and the inadequacy of direct adaptations.

- **Principled methodological design with empirical validation of necessity.** The guidance-model mechanism (using KL divergence to shift goodness distributions rather than direct gradient ascent) is conceptually clean and well-matched to FF models' properties. The ablation in Table 1 confirms this design choice is essential: using a randomly initialized guidance model drops forget-set accuracy to 51.18%, while properly trained guidance models retain utility. The systematic λ sweep in Figure 5 further demonstrates that GA fails across a wide range of hyperparameters.

- **G-MIA outperforms existing black-box MIAs and matches white-box attacks.** Figure 3 shows G-MIA consistently outperforms the black-box final-layer (FL) attack across all datasets and architectures, and on VGG13/CIFAR-100 it achieves the highest accuracy among all tested methods including white-box attacks. This supports the claim that G-MIA is an accurate verification tool that exploits the unique layer-wise structure of FF models.

- **Efficiency analysis grounded in a formal decomposition.** Section 4.3 provides an analytical breakdown of unlearning time (Equation 9), and Figure 4 backs this up empirically: FF-Erase(D) reaches retraining-level accuracy on D_forget in 38.52% of the retraining time, supporting the claimed 1.9–3.1× speedup.

- **Systematic ablation on guidance model trade-offs.** Table 1 explores multiple combinations of data fraction (α₁) and epoch fraction (α₂) for both mini-retrained and fast-distilled strategies, providing a practical guide for practitioners to choose efficiency–performance trade-offs.

## Weaknesses

### Fatal
None.

### Major

- **Complete absence of error bars or statistical significance measures.** All reported numbers (accuracies, G-MIA scores, time measurements) are presented as single point estimates with no indication of variance across multiple runs. Forgetting data is randomly sampled (20% of training data), making the outcomes inherently stochastic. Without error bars (or at minimum, multiple runs with mean and standard deviation for the key numbers in Figure 4 and Table 1), it is impossible to assess whether claimed improvements (e.g., G-MIA ACC of 0.5245 vs. retraining at 0.5320) are meaningful or simply noise. This is the most significant weakness: it undermines confidence in the central empirical claims. Addressable in a rebuttal, but as written the evidence is incomplete.

### Minor

- **Synthetic data generation for G-MIA is underspecified.** The paper mentions that synthetic data D_syn is generated using "model inversion techniques" and cites Fredrikson et al. (2015), but provides no concrete details about which method is used or how its quality is controlled. Since the quality of shadow models (and therefore G-MIA's performance) depends on the realism of this synthetic data, this is a reproducibility concern. The authors should specify the exact technique and ideally show robustness to the choice of generation method.

- **Termination thresholds (ε₁, ε₂) and recovery interval (K) are not ablated.** Algorithm 1 uses ε₁, ε₂ for early stopping and K for recovery frequency, but the paper neither specifies their values nor studies sensitivity to them. While this is common in unlearning papers, the method has several knobs (α₁, α₂, K, ε₁, ε₂, λ) and only α₁ and α₂ are systematically explored (Table 1). Providing guidance on setting K and the thresholds would strengthen the paper.

- **Only one forget fraction (β=0.2) is tested.** Real-world unlearning may require removing 1–5% of data, and the efficiency advantage over retraining could shrink at very small forget fractions. Testing additional β values would clarify the method's适用范围.

- **The main text presents results for only one dataset/architecture combination (VGG13/CIFAR-10).** The paper acknowledges this ("Due to space limitations... we put other results in Appendix §C"), but for a paper claiming general applicability, a summary table of results across all datasets and architectures in the main text would be more informative.

### Trivial
None.

## Nice-to-Haves
- An "only recovering forward" baseline (i.e., FF-Erase without the forgetting forward step) would help isolate the contribution of each component.
- A brief discussion of how the method performs with different negative sample generation strategies in FF training would broaden applicability.

## Removed Points
- **Criticism that G-MIA requires access beyond standard black-box assumptions.** The harsh critic claimed that requiring all-layer goodness vectors is stronger than standard black-box access. However, the paper explicitly states (Section 3.1): "FF models output the goodness vectors from all layers g¹, g², ..., g^L for inference." In FF models, these vectors *are* the natural model output — there is no separate "final prediction logit" that hides internal representations. G-MIA uses the same output any model consumer would receive. This criticism reflects a misunderstanding of FF model architecture, not an author error. **Removed.**

- **Generic presentation/style nitpicks and "missing related works" comments.** Removed per instructions.

- **Strength Finder claims about the problem being "important" or the paper being "well-written" in generic terms.** Removed as generic/superficial (the specific, grounded strengths are retained above).

- **Complaints about appendix dependency (missing appendix content).** The parser strips appendices from all submissions; they exist in the original. Removed per instructions.

- **Request for "complete training logs" or trivial implementation details.** Removed per instructions (nitpicks about reproducibility for large impractical artifacts).

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves do not make.

## Suggestions
1. **Add error bars.** This is the single highest-leverage improvement. Repeat the key experiments (Figure 4, Table 1, Figure 3) at least 3 times with different random seeds for forgetting set selection and weight initialization. Report mean and standard deviation for Acc_f, Acc_t, G-MIA scores, and unlearning time. Even two runs with min/max range would be more informative than single point estimates.
2. **Specify the synthetic data generation method for G-MIA** and ideally include a brief experiment showing G-MIA's sensitivity (or robustness) to the choice of inversion technique.
3. **Report values for ε₁, ε₂, and K** used in the experiments, or show that results are insensitive to a reasonable range of these thresholds.
4. **Include a summary table** comparing all datasets and architectures from the appendix in the main text, even if compressed.

## Score and Decision

**Calibration anchors retrieved across rounds:**

**Round 1 (bracketing):**
- `WNUDOLYlbh.md` — "Learning to Unlearn" (avg 3.00, Reject). Requires retrained models as training data, creating a circular dependency. The current paper is substantially stronger.
- `OJevuBonDC.md` — "FF with Dynamic Architecture" (avg 3.00, Reject). Incremental improvements to FF training with unclear novelty. The current paper tackles a clearly defined new problem.
- `DqvnwRe1V2.md` — "Illusion of Forgetting" (avg 4.00, Withdrawn). Interesting analysis of unlearning failures but limited scope (class unlearning only). Comparable contribution depth, but the current paper has stronger novelty.
- `m3FOf6nKnU.md` — "Forget Vectors at Play" (avg 4.50, Reject). Novel input-perturbation approach to unlearning but limited effectiveness. Comparable novelty, similar evidential rigor.
- Top-band anchors (avg 8.00) — all on unrelated topics (RL, multimodal, language models). Not relevant for calibration.

**Round 2 (narrowing within bracket 3.5–7.5):**
- `BZ8I2tXomt.md` — "Sharpness-Aware MU" (avg 5.00, Accept Poster). Theoretical analysis of SAM for unlearning; comparable experimental rigor, also lacks error bars. The current paper has stronger problem novelty.
- `iKqQGEOeej.md` — "Memorize to Forget" (avg 5.50, Reject). Novel approach avoiding gradient ascent, but novelty concerns (similar to Task Vectors). The current paper has clearer novelty.
- `IPqUBL4R9x.md` — "Distributional MU" (avg 6.00, Accept Poster). Strong theoretical framework but limited applicability. The current paper is weaker in theory but stronger in practical contribution.
- `r6Z3BXDrzO.md` — "Impossibility of Retrain Equivalence" (avg 4.50, Reject). The current paper is stronger in terms of constructive contribution (proposing a method, not just identifying a problem).

**Round-1 bracket:** 3.5–7.5 (the paper is clearly stronger than 2.0–3.0 anchors, and 7.5+ anchors are on unrelated topics).

**Round-2 narrowing:** The paper is comparable to or slightly stronger than the 5.0–5.5 anchors. It has genuine novelty (first FF unlearning) that the 5.0 anchors lack, but the missing error bars and underspecified details prevent it from reaching the 6.0+ level of "Distributional MU" which had formal theory and more rigorous evaluation.

**Final position:** The paper sits above the 4.5–5.0 range (clearer novelty than Forget Vectors or Sharpness-Aware MU) but below the 6.0+ range (weaker experimental rigor than Distributional MU). The core contributions are solid and the problem is genuinely new, but the evidential gap around missing error bars is real and prevents a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>