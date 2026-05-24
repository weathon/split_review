Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes a scalable message-passing (MP) framework for Bayesian neural networks that models the predictive posterior as a factor graph. It derives closed-form Gaussian message approximations for weighted sums, nonlinearities (via moment matching), and products, and implements them in a GPU-accelerated Julia library. The method is the first MP approach to handle convolutional neural networks and avoids the double-counting problem that plagued earlier MP methods (PBP, Lucibello et al.). On CIFAR-10 with an ~890k-parameter CNN, the method achieves competitive accuracy with AdamW and IVON while showing notably lower expected calibration error, and on synthetic data it validates that posterior uncertainty grows appropriately outside the training range.

## Strengths

- **First MP method to handle CNNs.** The paper trains a 6-layer convolutional network on CIFAR-10 (~890k parameters), demonstrating that pure message passing scales beyond the small MLPs addressed by prior MP work (EBP, PBP, Lucibello et al.). This is a concrete extension of the state of the art and is contextualized against the related work in Section 1.1.

- **Avoidance of double-counting training data.** Section 3.2 describes a batching strategy that stores aggregated batch messages in a Trainer object and divides out old messages when switching batches. This cleanly solves a known limitation of prior MP methods that caused overconfidence and posterior collapse. The mechanism is clearly explained and illustrated in Figure 2.

- **Scaling optimizations with 300× speedup.** Section 4.1 describes a layered, stateless factor graph implementation that scales linearly with depth rather than with layer size or batch size. The reported ~300× speedup over a naive factor graph model, combined with GPU acceleration via CUDA.jl and Tullio.jl, demonstrates real engineering effort and practical viability.

- **Competitive calibration on CIFAR-10.** Table 1 shows MP achieving better expected calibration error than both AdamW and IVON on a convolutional architecture. The calibration advantage is the paper's headline empirical finding and, if reproducible, is a genuinely useful property for applications requiring reliable uncertainty quantification.

- **Closed-form message equations.** Section 3.1 provides exact Gaussian messages for weighted sums (Equation~5), moment-matched approximations for nonlinearities, and variational message passing for products, with additional factor types tabulated in the appendix. These equations are a reusable resource for factor graph modeling beyond this specific application.

## Weaknesses

### Fatal
None. The method is technically sound, the core contributions (first MP for CNNs, double-counting avoidance) are well-supported by the paper content, and no fundamental error invalidates the approach.

### Major

- **Single-run CIFAR-10 evaluation without error bars.** Table 1 reports a single set of numbers per method with no standard deviations, confidence intervals, or multiple seeds. The accuracy differences between MP, AdamW, and IVON are in the 1–2 percentage point range — well within typical run-to-run noise from random initialization and batch ordering. This means the paper's central empirical claim ("MP can compete with SOTA baselines, even having an edge in terms of calibration") cannot be assessed for statistical significance. The calibration edge in particular could be a one-off artifact rather than a reliable property of the method. Given that the paper's own framing emphasizes this empirical claim, the lack of any replication evidence is a significant gap.

    *Why it is Major and not Fatal:* The method's other contributions (first MP for CNNs, double-counting avoidance, scaling optimizations, message equations) stand independently of whether the CIFAR-10 results have error bars. The paper would still be a meaningful advance even if the CIFAR-10 numbers are treated as preliminary.

- **Asymmetric baseline tuning relative to MP's empirically-fitted prior.** Section 4.3 introduces a prior variance formula $\sigma_p^2 = (1.5 - 0.8041\cdot\min(1.0, d_2/d_1)) / (0.8041 + 0.4496\cdot d_1)$ that is explicitly "based on experimental data" (Appendix D). This means the prior has been tuned — it is not a principled, hyperparameter-free choice. Meanwhile, the AdamW and IVON baselines receive only a cosine annealing schedule with no reported hyperparameter search (no mention of tuning learning rate, weight decay, momentum, or IVON-specific parameters). This asymmetry undermines the paper's claim that MP "requires no hyperparameter tuning": the prior variance formula *is* a form of tuning, just done offline on experimental data rather than via grid search. The sensitivity of results to the exact coefficients in Equation~(5) is not analyzed.

### Minor

- **Synthetic data coverage analysis has unclear or incomplete metrics.** The paper reports a "strong correlation of 0.90 between credible intervals of the predictive posterior and the coverage rate" (Section 5.1) but never defines what this correlation is computed over — across interval widths? across regions of the input space? This makes the number unverifiable. Additionally, the coverage rates are asymmetric between positive and negative $x$ (e.g., ~66% vs. ~36% for $1\sigma$ intervals), which is not explained. The paper calls the uncertainty "reasonably well-calibrated" but provides no comparison to a simple baseline (e.g., a GP) or a quantitative calibration metric like ECE on the synthetic data.

- **No data augmentation on CIFAR-10.** The experiment uses no data augmentation (no mention of flips, crops, or other standard CIFAR-10 augmentations). This is uncommon for CIFAR-10 evaluations and may disproportionately affect the baselines (especially AdamW, which typically relies on augmentation and weight decay for regularization). The paper notes that the architecture lacks residual connections and normalization, but does not discuss the absence of augmentation as a factor in the comparison.

- **Baseline hyperparameters not fully specified.** The paper states that AdamW and IVON use "a cosine annealing learning rate schedule" but does not report the base learning rate, weight decay, momentum, or IVON-specific hyperparameters (e.g., number of samples, learning rate for the posterior). This makes reproducibility harder than it should be.

### Trivial
None.

## Nice-to-Haves

- Run the CIFAR-10 experiment with 5–10 random seeds and report means and standard deviations for all metrics. This is the single most impactful improvement.
- Perform a sensitivity analysis on the prior variance formula (Equation 5). Show how accuracy, ECE, and NLL on CIFAR-10 vary with ±10–20% changes in the coefficients.
- Clarify what the "correlation of 0.90" in the synthetic experiment means (correlation between what and what, over what dimension?).
- Add a comparison to MC Dropout or a deep ensemble as additional baselines for uncertainty quality.
- Consider adding data augmentation (or showing that it does not affect the relative ranking).

## Removed Points

*These points were flagged by reviewers but are removed from the main review for the reasons stated below. Treat them with caution if encountered elsewhere.*

1. **"Double-counting within a batch"** (Harsh Critic). The critic argued that the method "still processes examples multiple times (multiple iterations per batch)" and that this is a form of double-counting. This misunderstands loopy belief propagation: iterating message passing within a batch for convergence is standard practice and categorically different from the epoch-level double-counting that caused overconfidence in PBP. The paper's batching strategy correctly handles cross-batch double-counting.

2. **"Main text lacks sufficient detail on nonlinearity moment matching"** (Harsh Critic). The critic notes that formulas are deferred to Appendix E. This is a parser artifact — the appendix was stripped during PDF extraction and is present in the original submission. The main text provides the conceptual derivation (Equations 8–9) and states where full details reside.

3. **"Garbled numbers suggest parser issues in synthetic data"** (Harsh Critic, implied). The overbar notation (e.g., $\bar{6}1\%$) is a PDF-to-text rendering artifact. The original submission uses clear notation. This is not a paper flaw.

4. **Strength Finder's claim about "theoretical connection to VI"** — The claim that the method minimizes $D_{KL}[p(\theta|\mathcal{D})\,\|\, q(\theta)]$ is stated in Section 3.2 but the proof is deferred to Appendix A.2 (stripped). The strength is retained because the claim itself is present in the paper, but the unverifiable proof detail is noted here.

5. **"Novel weight-prior initialization" as a strength** — The paper explicitly says the prior formula is "based on experimental data" (Section 4.3). Calling it "novel" overstates the contribution; it is an empirical heuristic. This is better treated as part of the method description rather than a standalone strength.

## Novel Insights

The two reviewer inputs converge on the same core pattern: the paper's technical contribution (scalable MP for BNNs with CNNs, double-counting avoidance) is genuinely novel and well-executed, but its empirical validation falls short of the standard needed to support its central claim of being "competitive with SOTA." The Harsh Critic correctly identifies that the single-run CIFAR-10 experiment, the asymmetric baseline tuning, and the empirically-fitted prior formula weaken the evidence considerably. However, neither reviewer identifies a fatal flaw — the method is sound, the contributions are concrete, and the limitations are honestly acknowledged. What emerges is a paper with a clear, valuable technical contribution that would be significantly strengthened by straightforward experimental improvements (multiple seeds, sensitivity analysis). The paper's value to the community lies primarily in opening a new direction (scalable MP for BNNs) rather than in the specific CIFAR-10 numbers it reports.

## Suggestions

1. **Add multiple seeds for all CIFAR-10 methods.** Run 5 or 10 seeds and report mean ± std for accuracy, ECE, NLL, and OOD AUROC. This is the single change that would most strengthen the paper.
2. **Conduct a sensitivity analysis on the prior variance formula (Equation 5).** Show that results are stable to at least ±10% variation in the coefficients.
3. **Define the "correlation of 0.90" clearly** in the synthetic data section — specify the variables and the dimension over which the correlation is computed.
4. **Report baseline hyperparameters** (learning rate, weight decay, momentum, IVON-specific settings) in the main text or a table.
5. **Either add data augmentation** or provide a brief justification for its absence and check that baselines do not benefit disproportionately from it.

## Score and Decision

**Originality**: Strong — this is the first MP method for CNNs and introduces concrete innovations in batching and scaling. The message equation derivations are a reusable technical contribution.

**Importance of research question**: High — scalable and well-calibrated Bayesian deep learning is an important open problem.

**Claims support**: Weak-to-moderate — the core technical claims (first MP for CNNs, avoids double-counting) are well-supported. The empirical claim of being "competitive with SOTA" is not convincingly supported due to the lack of error bars and asymmetric baseline tuning.

**Soundness of experiments**: Moderate — the synthetic data experiment is reasonable, but the CIFAR-10 evaluation has significant methodological gaps.

**Clarity of writing**: Good — the paper is well-structured, the method is explained clearly, and limitations are honestly acknowledged.

**Value to the research community**: Moderate-to-high — the framework opens a new direction for MP-based BNNs and provides reusable building blocks (message equations, batching strategy, scaling techniques) that others can build on. However, the value would be higher with stronger empirical validation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>