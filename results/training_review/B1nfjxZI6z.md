Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes a simple meta-heuristic for detecting distribution shift in model-based optimization (MBO) for sequence design: train a binary classifier to distinguish training data from designed sequences, and use its logit scores ("OOD scores") as a continuous measure of distribution shift intensity. The method is demonstrated on a 2D toy, described (but not shown with results) on a simulated protein folding task, and evaluated on a real-world AAV capsid engineering experiment where ~5,000 sequences were experimentally tested along MBO trajectories. The core empirical contribution is the real-world AAV experiment showing that OOD scores track distribution shift and improve candidate selection over a Deep Ensemble uncertainty baseline.

## Strengths

- **Real-world AAV experiment with trajectory-level experimental measurements**: The paper generates a unique dataset where ~5,000 designed sequences are experimentally measured for packaging and transduction at every iteration of MBO trajectories (Section 4.3). Figure 1 provides concrete evidence that prediction error and the fraction of adversarial (non-functional) sequences increase markedly along iterations, while a random holdout MSE stays low. This directly quantifies the severity of feedback covariate shift in a real biological design task — a rare and valuable contribution.

- **OOD scores improve candidate selection over an established baseline**: Using a cutoff-based selection scheme, filtering designed sequences by OOD scores consistently yields lower regret than filtering by Deep Ensemble uncertainties (Figure 3c), with several cutoffs reaching zero regret. This directly supports the paper's central empirical claim that the OOD classifier reduces adverse effects of distribution shift.

- **Method is simple, model-agnostic, and easy to adopt**: The OOD classifier only requires training a binary classifier on the existing training set (in-distribution) and samples from the search algorithm (out-of-distribution). It is compatible with any surrogate model and search method (Section 2.3), in contrast to prior approaches that require specific architectures or computationally expensive ensemble training (Section 3). This practical simplicity is a genuine strength for practitioners.

- **OOD scores provide a continuous, interpretable measure of distribution shift**: Figure 3a shows OOD scores increasing steadily over MBO iterations, mirroring surrogate model MSE (Figure 1b), while Deep Ensemble standard deviations do not show a clear trend. Figure 3b further demonstrates cleaner separation between functional and non-functional AAV variants than the Deep Ensemble baseline.

## Weaknesses

### Fatal
None.

### Major

- **Section 4.2 (simulated protein structure design) contains no results**: This section describes a proof-of-concept simulation scheme using ESMfold but provides no figures, tables, or numeric values. The text merely asserts "We see signs of distribution shifts caused by design, and our method can aid in selecting designed inputs by lowering regret" without supporting evidence. The paper's narrative arc depends on comparing simulated vs. real-world shift intensity — the abstract and introduction explicitly claim that "simulated settings ... show much weaker distribution shift." Without results for the simulated experiment, this comparative claim is unsupported. The paper mentions "additional ones we test in the supplement" (line 20), but the main-text section itself has no evidence. The paper should either present results or explicitly qualify the claim.

- **Insufficient evaluation of OOD classifier generalization and training details**: The OOD classifier is trained on designed sequences as positive examples and evaluated on those same designed sequences (Section 4.3). The paper describes no train/validation split, cross-validation, or regularization strategy for the OOD classifier. While this is not a fatal flaw — density ratio estimation via classification is a standard technique where evaluating on training points is expected — the lack of discussion about overfitting prevention (early stopping, architecture choice, class imbalance handling) is a significant reporting gap that undermines confidence in the generalization of the OOD scores to unseen designed sequences. The paper should at minimum describe how overfitting was controlled and report the OOD classifier's validation accuracy or calibration.

- **Only one baseline compared**: The paper compares only against Deep Ensemble uncertainties. No comparison is made to other OOD detection methods (e.g., Mahalanobis distance in surrogate model latent space, simple density estimation via KDE, likelihood-based methods) or to other design stabilization approaches. The claim of wide applicability is weakened by this narrow comparison.

### Minor

- **No quantitative separation metrics for functional vs. non-functional classification**: Figure 3b shows histograms and KDEs suggesting that OOD scores separate functional from non-functional variants better than Deep Ensemble uncertainties, but no quantitative metrics (AUROC, AUPRC, threshold-agnostic measures) are reported. The reader cannot assess the effect size or determine whether the separation is practically meaningful.

- **Three selection strategies proposed but only cutoff evaluated**: Section 2.4 describes cutoff, stratified, and utility-based selection strategies, but only the cutoff scheme is evaluated in Figure 3c. The paper does not analyze sensitivity to the cutoff choice or compare the proposed strategies against each other.

- **Regret metric is unusual and only shown for K=100**: The regret measure (difference between global max transduction and max in K=100 selected sequences) can be zero if the selected set contains the single best sequence, making it a winner-take-all metric that does not measure typical performance. Bootstrap confidence intervals are reported but appear large (cannot verify from text alone, but the reviewer notes this). Results for other K values are deferred to the supplement. The paper should report mean transduction (or best-of-K) over multiple K values in the main text.

- **Limited detail on AAV experimental setup**: The paper provides no ensemble size for the Deep Ensemble baseline, no specific hyperparameter information for the surrogate models, and the cutoff γ for packaging is not specified. The beam search variant is mentioned but results are not separately shown. LLMs are mentioned (line 146) but never referenced again with results.

### Trivial
- Figure 3b KDE color scheme is not described in the caption.
- Minor typos ("offilne" for "offline", "seqeunces" for "sequences", "fti" for "fit").

## Nice-to-Haves

- Analysis of how OOD classifier architecture, training data size, and regularization affect performance would help practitioners.
- Comparison to additional MBO algorithms beyond AdaLead and the beam search variant would strengthen the claim of genericity.
- Sequence-level case studies showing specific designed sequences, their OOD scores, and experimental outcomes would make the distribution shift concrete and help readers understand what the OOD score captures.
- An ablation manipulating the search distribution to verify that the empirical correlation between s(x) and surrogate error is driven by 1/p_tr(x) (as the theoretical discussion suggests) would strengthen the paper's explanatory power.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Data leakage as a fatal flaw"** — The harsh critic's claim that "the OOD classifier training and evaluation constitutes data leakage that could invalidate the entire empirical evaluation" is overstated. In density ratio estimation, training a classifier on samples from two distributions and evaluating the density ratio at those same training points is standard practice (Sugiyama et al., 2012; Hido et al., 2011). The OOD scores at training points are valid estimates of p_de(x)/p_tr(x). The concern about overfitting is real (and addressed above as a minor weakness), but characterizing this as a potentially fatal flaw that "directly undercuts the paper's central empirical claim" is not supported by the methodology.

- **"Theoretical justification tension is unresolved"** — The paper explicitly acknowledges that s(x) = p_de(x)/p_tr(x) "is not necessarily the ideal score" and that 1/p_tr(x) is more correlated with surrogate error (Section 2.2, lines 40–42). The paper then explains the practical rationale for using s(x) (density ratio is easier to estimate). This is honest and transparent, not a flaw. The criticism demands the paper solve a problem it never claimed to solve.

- **"2D toy doesn't note difference from AAV setup"** — The paper does note this explicitly (lines 122–123): "In this toy model, the 'design distribution' is the uniform distribution over the input space, making OOD scores proportional to 1/p_tr(x)... Therefore, in most practical cases, we select positive OOD examples from areas likely to be explored by a search method."

- **"Section 2.5 belongs in introduction"** — A stylistic preference, not a substantive weakness.

- **"Computational-complexity critique of conformal methods is misleading"** — The paper's claim about conformal prediction requiring "training at least n models" accurately describes leave-one-out conformal approaches; split conformal is different. This is a minor imprecision in the related work section, not a flaw in the paper's contribution.

- **Formatting/style nitpicks** — Removed per instructions (parser artifacts, not author errors).

## Novel Insights

The reviews reveal an interesting tension: the harsh critic's strongest criticisms (data leakage, missing simulation results) reflect a mismatch between how the paper presents its contribution and what a reader expects from a standard ML paper. The paper frames the OOD classifier as a "meta-heuristic" and the AAV experiment as a case study — yet the critic evaluates it against standards for a controlled ML method evaluation (train/test splits, multiple baselines, quantitative metrics). The real insight is that the paper is doing something unusual: deploying a real-world MBO study with experimental labels at every step. This is genuinely rare and valuable, but the paper fails to fully capitalize on this data. It could provide richer analyses of failure modes, sequence-level insights, and practical guidance for practitioners, but instead tries to fit into a standard "method + evaluation" frame. The AAV trajectory dataset itself may be more valuable than the specific OOD classifier method.

## Suggestions

1. **Present results from the simulated protein experiment or remove the claim**: If results exist in the supplement, summarize key numbers (e.g., regret improvement) in the main text. If not, either run the experiment or remove the claim that the method was validated in three settings.

2. **Add OOD classifier training details**: Describe regularization, architecture selection, any train/validation split or cross-validation used to prevent overfitting. Report the OOD classifier's held-out accuracy or calibration.

3. **Report quantitative separation metrics for Figure 3b**: Add AUROC or AUPRC values for distinguishing functional from non-functional variants using OOD scores vs. Deep Ensemble uncertainties.

4. **Expand baseline comparison**: At minimum, compare to a simple density estimate (KDE) or Mahalanobis distance in latent space, as these are common OOD detection baselines.

5. **Show regret for multiple K values**: Present results for K=10, 50, 200 alongside K=100, and report mean transduction (or best-of-K) as an alternative to regret relative to the global maximum.

6. **Add experimental details**: Specify ensemble size, hyperparameters, and the cutoff γ for packaging.

## Score and Decision

The paper makes a genuine contribution: the real-world AAV experiment with trajectory-level experimental measurements is rare and valuable, and the OOD classifier is a simple, practical tool. However, the missing results from the simulated experiment (which the paper's narrative depends on) and the insufficient OOD classifier training/evaluation details are significant gaps that reduce confidence in the claims. The paper would benefit substantially from addressing these issues.

**Score**: 6.0 — A solid paper with a real contribution (the AAV experiment and the OOD classifier idea) undermined by presentation gaps and one missing experiment. The core claims about the method's effectiveness in the real-world setting are likely valid, but the paper overclaims about the simulated comparison and lacks sufficient rigor in the OOD classifier evaluation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>