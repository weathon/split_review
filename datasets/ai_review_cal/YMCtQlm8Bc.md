- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6
I already have the complete paper text from the initial read. Let me proceed with the consolidated review.

---

## Summary

This paper investigates how overparameterization affects Sharpness-Aware Minimization (SAM). Through experiments across 8 workloads spanning vision, language, chemistry, and game domains, the authors show that SAM's generalization improvement over standard optimizers grows with model size and is small or negligible for underparameterized models. They explain this through the interplay of enlarged solution space and amplified implicit bias, provide theoretical results on linear stability, convergence rate (linear under PL), and generalization for two-layer networks, and explore practical conditions (label noise, sparsity, regularization) that modulate the benefit.

## Strengths

- **Comprehensive cross-domain empirical validation**: The paper evaluates SAM across 8 workloads covering 5 domains (synthetic, vision, language, chemistry, game) and 5 architecture types (MLP, CNN, RNN, GCN, Transformer). Figure 2 shows that SAM's generalization improvement relative to baselines consistently increases with model size across all domains. This breadth strengthens the claim that the phenomenon is general rather than dataset-specific.

- **Mechanistic demonstration via solution-space analysis**: Section 4.1 shows that for one-hidden-layer ReLU networks, SAM and GD find similar solutions when underparameterized (10 neurons) but SAM finds much simpler, lower-variance solutions when overparameterized (100 neurons). The optimization trajectories (Figure 3a) confirm that SAM and GD land in different basins only when the model is overparameterized, directly supporting the explanation that overparameterization provides the solution space diversity that SAM's implicit bias exploits.

- **Linear convergence guarantee for SAM (Theorem 2)**: Under the PL condition (satisfied when overparameterized) and interpolation, Theorem 2 proves that stochastic SAM achieves linear convergence, faster than the typical O(1/t) sublinear rate. Empirical confirmation on matrix factorization and CIFAR-10 (Figure 4b) shows convergence accelerating with model size.

- **Practical insights on boundary conditions**: Section 6 identifies when the overparameterization benefit is amplified (under label noise, with sparsity) and when it fails (without weight decay, early stopping, or sufficient inductive bias). These caveats strengthen the paper's credibility by acknowledging limitations rather than claiming unconditional benefit.

- **Linearization ablation ruling out a competing explanation**: Section 7 reports that SAM underperforms SGD by more than 10% in linearized (NTK) regimes, which rules out neural tangent kernel linearization as the cause of SAM's benefit and supports the attribution to overparameterization itself (verifiable from main text, lines 542-545).

## Weaknesses

### Fatal
None.

### Major

- **Core empirical results lack uncertainty quantification**: The central empirical claim — that SAM's generalization benefit consistently increases with overparameterization — is presented in Figure 2 with a single trajectory per model size per workload. No error bars, confidence intervals, or seed variance are reported for the main 8-workload experiments. Given that the paper makes a strong causal claim about a *trend*, the absence of variance information makes it impossible for the reader to assess whether the observed patterns are reliable or whether they could be influenced by random seed, initialization, or data split variation. Some improvements appear small (near zero for low-parameter models in several workloads), and without uncertainty quantification the distinction between a genuine positive effect and noise cannot be established. The paper does report running "three random seeds" for the one-hidden-layer experiments (line 162), which contrasts with the lack of such rigor in the main empirical results. This is the paper's most significant weakness and should be addressed with error bars based on multiple runs (at least 3–5 seeds) for the main workloads.

### Minor

- **Overstated framing of the core claim**: The abstract and bullet points state that SAM "may not take effect without" overparameterization (lines 9, 41, 175). However, the plotted improvements in Figure 2 show small but non-zero improvements even at the lowest parameter counts for several workloads (e.g., MNIST, CIFAR-10). The evidence supports that the *magnitude* of improvement grows with overparameterization, not that SAM requires overparameterization to be effective at all. The paper hedges in some places ("if not only," line 143) but the stronger formulation in the abstract and key bullet points overstates the evidence.

- **Theorem 1 (linear stability) connection to overparameterization is conceptual rather than formal**: Theorem 1 provides necessary conditions for linear stability of stochastic SAM, showing that SAM requires more uniform Hessian moments than SGD. This is a property of SAM in general — the theorem itself does not involve model width, parameter count, or any measure of overparameterization. The paper's link to overparameterization is that these stability conditions *matter more* when the solution space is enriched by overparameterization, but this connection is argued conceptually, not proven. The empirical validation (Figure 4a) shows a single bar chart comparing SAM and SGD on MNIST, without varying model size to show the uniformity gap grows with width. The paper would be stronger by either proving that overparameterization amplifies the uniformity gap or demonstrating this empirically across model sizes.

- **Solution complexity analysis in Section 4.1 is qualitative**: The claim that SAM finds "simpler" solutions for overparameterized models (Figures 2a–d) is based on visual inspection of learned functions. A quantitative measure of complexity (e.g., number of linear regions for the ReLU network, parameter norm, or spectral properties of the Hessian) would make this claim testable and more rigorous.

### Trivial
None.

## Nice-to-Haves

- The paper defers many experimental details (hyperparameters, optimizers per workload, architecture variations, and the formal statement of Theorem 3) to the appendix. A brief summary table in the main text identifying the baseline optimizer (SGD with momentum vs. AdamW, learning rate) for each workload would improve readability. However, this does not affect the paper's validity since the appendix contains these details in the original submission.

- It would be useful if the paper clarified the exact definition of the "improvement" metric plotted in Figure 2 (absolute difference in validation accuracy/loss vs. relative improvement). This is a presentation improvement.

## Removed Points

These points are flagged to be removed; treat them with caution as they either violate the filtering rules or misread the paper.

- **Hyperparameter confound concern (Critic's #2)**: The critic claims hyperparameters may not be tuned per model size, potentially inflating SAM's relative improvement. This is speculative — the experiment details are in the appendix (which exists in the original submission but was stripped by the parser), and the critic's assertion that "the paper states that hyperparameters are tuned only for ρ" is not explicitly stated in the available text. The paper does tune ρ per model size in Section 4.2, but Section 3 is the main empirical study, and deferring hyperparameter details to the appendix is standard practice. Removed as speculative and dependent on information likely present in the appendix.

- **Missing definition of improvement metric / baseline optimizer details / missing appendix content**: The critic faults the paper for not defining the improvement metric and baseline optimizer in the main text. The paper explicitly states "We defer to \cref{app:exp_details} for the full experiment details" (line 110). These are standard deferrals to an appendix that existed in the original submission. Removed per the rule that parser-stripped appendix content cannot be grounds for criticism.

- **Theorem 3 statement being too vague**: The paper itself labels Theorem 3 as "(Informal)" (line 422) and states the formal version and proof are in the appendix. The criticism that the formal statement is missing from the main text is a consequence of appendix stripping. Removed.

- **Sparsity experiment implementation details**: The critic asks whether the same SNIP mask is used throughout training. This is an implementation detail present in the appendix. Removed.

## Novel Insights

The most interesting observation across the reviews is that the paper's claimed weakness (lack of formal connection between Theorem 1 and overparameterization) is structurally related to its strength: the paper relies on a *conceptual* bridge between the stability condition and overparameterization (the idea that with more minima available, a preference for flatter ones becomes more consequential). This conceptual link is intuitively plausible but neither formally proven nor systematically tested. Recognizing this as a gap — not in the theory itself, but in the integration of theory with the paper's central thesis — points to a clear path for strengthening the work without adding new theorems.

## Suggestions

1. **Add error bars to the core results** (Figure 2). Run at least 3–5 random seeds per model size for each workload and report mean improvement with standard deviation or confidence intervals. This single change would transform the central empirical claim from suggestive to compelling.

2. **Reframe the contribution language** in the abstract and Section 3 to state that the *magnitude* of SAM's improvement grows with overparameterization, rather than that SAM "may not take effect" without it. This aligns the claims more precisely with the evidence.

3. **Strengthen the connection between Theorem 1 and overparameterization** by either: (a) empirically measuring the uniformity gap (SAM vs. SGD) across at least 3–4 model widths for one workload to show it grows with size, or (b) explicitly stating Theorem 1 as a property of SAM whose practical relevance is amplified by overparameterization, without implying a formal causal link.
