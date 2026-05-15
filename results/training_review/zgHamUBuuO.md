Now I have all the verification I need. Let me construct the final consolidated review.

## Summary

This paper introduces Sparling, a technique for learning extremely sparse intermediate representations (≥99.9% zeros) from end-to-end supervision only. The method uses a spatial sparsity layer with quantile-based hard thresholding, combined with an annealing schedule tied to validation accuracy. The key claim is that enforcing extreme sparsity forces the intermediate representation to recover the ground-truth latent motifs (e.g., digit positions in images or audio) without any direct supervision on those motifs. Results are shown on three domains: a synthetic DigitCircle task, LaTeX OCR, and AudioMNIST.

## Strengths

- **Adaptive sparsity annealing enables training at extreme sparsity levels unachievable by standard regularizers.** Algorithm 1 ties density reduction to validation accuracy, allowing the model to gradually increase sparsity while maintaining learning signal. The ablation (Section 5.3) shows that starting at the final density leads to 68–71% E2EE error, whereas annealing reaches <1% on DigitCircle. This is a clear and practical contribution.

- **The quantile-based spatial sparsity layer achieves far lower densities than L₁ or KL penalties.** Table 1 shows Sparling reaches 0.005% density (99.995% sparsity) on DigitCircle, while the best L₁ baseline (λ=2) reaches 0.023% density but with >70% end-to-end error. The KL-divergence approach could not go below 0.1% density even with λ=10⁵. This demonstrates a genuine capability gap.

- **High motif localization accuracy is demonstrated across three diverse domains, including generalization to unseen speakers.** Figure 2 shows FPE, FNE, and CE all below ~2% on DigitCircle, and FPE of 0% with CE < 5% on AudioMNIST (testing on speakers 52–60, unseen during training). Confusion matrices (Figure 3) show clean diagonals, confirming that learned channels align with ground-truth motif types.

- **The evaluation framework (FPE, FNE, CE) is rigorous and principled.** The metrics explicitly handle channel permutation and allow spatial tolerance via motif footprints, making the assessment both precise and reproducible.

- **The retraining experiment convincingly shows that the end-to-end accuracy penalty from extreme sparsity is largely recoverable.** Figure 6 compares "Non-Sparse" models with "Retrained" models (freeze ĝ, finetune ĥ), demonstrating that most of the gap is closed after retraining. This addresses a natural concern about whether the bottleneck permanently damages performance.

## Weaknesses

### Fatal
None.

### Major

- **Baseline comparisons (L₁, KL) are only shown on DigitCircle, yet the paper claims general superiority over existing techniques.** Table 1 and the KL discussion in Section 5.2 present results only for DigitCircle. The paper states in the Introduction that "Alternate sparsity enforcement techniques...either do not produce extreme sparsity or have accuracy below 50%" and in Related Work that existing methods "typically only achieve 50%–90% sparsity." Without baseline results on LaTeXOCR and AudioMNIST, the generality of Sparling's advantage over existing methods is unsupported. The paper acknowledges that ablations are only on DigitCircle (Section 5.1), but no similar caveat is attached to the baselines, and the text does not limit the superiority claim to DigitCircle.

- **The claim that extreme sparsity is necessary for motif recovery is supported by the δ-vs-error trade-off curve on only one domain.** Figure 4 (error vs. sparsity), which is central to the paper's core claim that "CE is often substantially higher for even a 2–3× increase in δ, demonstrating the need for extreme sparsity," is only presented for DigitCircle. Analogous plots for LaTeXOCR and AudioMNIST are absent, so it is unknown whether the sparsity-demanding behavior generalizes or is idiosyncratic to DigitCircle. This weakens the paper's most important conceptual claim.

### Minor

- **The information bound derivation (Section 3.3) is sketchy and incomplete.** The inequality \(H(\mathcal{M}[i,c]) \leq H(B(\delta_{i,c})) + \eta \delta_{i,c}\) introduces an unexplained parameter η and the step is not justified. The paper's main contribution is empirical, so this does not undermine the core results, but the derivation as presented does not add meaningful theoretical support to the paper's claims and reads as rushed.

- **No sensitivity analysis is provided for the adaptive sparsity algorithm's hyperparameters.** The paper fixes \(M = 2\times10^5\), \(B = 10\), \(d_T = 10^{-7}\), and \(\delta_{\text{update}} = 0.75\) across all domains without any ablation or analysis of how these choices affect final density or motif accuracy. Since the annealing schedule directly determines the final density, this is a meaningful gap.

- **The paper does not quantify how often the missing motifs (fraction bar, parentheses, plus signs) actually appear in the LaTeXOCR test set.** The high FNE on LaTeXOCR is correctly attributed to the necessity condition, but without frequency data, the reader cannot assess how much this error degrades practical performance.

- **The ablation only tests two starting δ values (final and penultimate) when assessing the necessity of annealing.** It does not test whether a different annealing schedule (faster or slower) would work equally well or better, leaving open questions about the method's robustness.

### Trivial
None.

## Nice-to-Haves
- A sensitivity study of the annealing hyperparameters (\(d_T, \delta_{\text{update}}, M\)) would increase confidence in the method's robustness.
- An application to a domain where ground-truth motifs are unknown but can be verified post-hoc (as suggested in the introduction about satellite imagery) would strengthen the real-world relevance.

## Removed Points
These points were reviewed against the paper and removed as invalid, overstated, or irrelevant:

1. **"The unconditional independence claim is not substantiated."** — The paper explicitly states "This is a direct result of sparsity and locality" (Section 2). Since `ĝ` uses convolutional layers (local receptive fields), a zero activation at position [i,j,c] genuinely means the local region does not contain the motif, regardless of other input regions. The claim is properly substantiated.

2. **"The theoretical foundation for Motif Identifiability is insufficiently supported."** — The paper explicitly states (Section 3.1) "This is an empirical claim, which we validate in our experiments." The paper does not claim a formal proof; it presents an empirical hypothesis and tests it. Criticizing the lack of a theoretical proof for something the paper explicitly treats as an empirical claim is a strawman.

3. **"The paper overstates what is demonstrated in the abstract/introduction."** — The abstract and introduction accurately describe what is shown: results on three domains with >90% accuracy. The claim that extreme sparsity "leads to a particularly effective approach to discovering the true underlying structure" is commensurate with the evidence presented (strong on DigitCircle, partially supported on others).

4. **"The paper does not discuss limitations beyond the necessity condition."** — The paper discusses the necessity-condition failure (LaTeXOCR), shows the E2EE gap and retraining mitigation, and explicitly scopes the approach to settings where sparsity, locality, and necessity hold. These constitute reasonable limitations discussion for a conference paper.

## Novel Insights
One genuinely novel observation emerges from triangulating the reviews and the paper: the annealing schedule's dependence on validation accuracy acts as an automatic curriculum that may be more important than the specific sparsity enforcement mechanism itself. The paper shows that without annealing, extreme sparsity destroys all learning signal (68–71% error), but with it, the model achieves <1% error. This suggests that the primary challenge in extreme-sparsity training is not architectural but optimization-dynamic: the model needs to first learn coarse representations before committing to extreme sparsity. The reviewer criticisms about missing sensitivity analysis on hyperparameters highlight that we don't know how delicate this annealing curriculum is — whether the method would work across diverse training budgets, batch sizes, or learning schedules. This represents both the paper's most interesting engineering insight and its most under-explored dimension.

## Suggestions
1. **Add baseline results (L₁ and/or KL) on at least one of the other domains** (LaTeXOCR or AudioMNIST) to support the claim that existing techniques cannot achieve extreme sparsity with low error outside DigitCircle. Even a single λ value per baseline would substantially strengthen the paper.
2. **Add the δ-vs-error trade-off plot for at least one more domain** (preferably AudioMNIST, where the method already shows strong results) to support the claim that extreme sparsity is necessary for motif recovery beyond DigitCircle.
3. **Provide a brief sensitivity analysis** for the annealing hyperparameters, or at minimum justify why the chosen values are reasonable and note the empirical robustness across domains (since the same values worked on all three).
4. **Quantify the frequency of the missing motifs** in the LaTeXOCR test set to help readers interpret the practical impact of the high FNE.
5. **Clarify in the introduction and conclusion** that the baseline comparison results are from DigitCircle, to avoid overclaiming generality.

## Score and Decision

This is a solid paper with a genuine algorithmic contribution. The spatial sparsity layer with annealing is novel and practically motivated; the empirical results on DigitCircle are strong and well-controlled; the evaluation framework is principled; and the method is demonstrated across three domains. However, the two major weaknesses — missing baseline comparisons on 2/3 domains and missing trade-off evidence for the core claim on those domains — significantly limit the generality of what the paper can currently claim. The paper as written overstates its support. These issues are addressable with additional experiments and would not require fundamentally new methodology. With those additions, the paper would be strong.

**Score:** 6.5

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>