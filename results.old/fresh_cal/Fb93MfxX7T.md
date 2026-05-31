Now I have thoroughly examined the paper and verified all claims against the actual text. Let me produce the final consolidated review.

---

## Summary

This paper conducts a systematic empirical study of 14 PETL methods on visual recognition tasks using ViT-B/16, including low-shot (VTAB-1K), many-shot (CIFAR-100, RESISC, Clevr-Distance), and robustness (CLIP ViT-B/16 on ImageNet distribution shifts) settings. The main findings are: (1) with careful hyperparameter tuning, diverse PETL methods achieve strikingly similar accuracy on VTAB-1K (relative std dev 1.09%), contradicting earlier claims that simple methods like BitFit are substantially inferior; (2) despite similar accuracy, methods disagree on ~20–35% of predictions, suggesting complementarity; (3) PETL remains competitive with full fine-tuning in many-shot regimes with only 2–5% of parameters; and (4) PETL better preserves OOD robustness than full fine-tuning. The paper provides practical recipes for method selection and releases a systematic evaluation framework.

## Strengths

- **Careful, large-scale comparison with a cap on tunable parameters (≤1.5% of ViT-B/16) reveals that after systematic tuning, 14 PETL methods cluster tightly in accuracy (relative std dev 1.09% on VTAB-1K).** Table 1 shows BitFit (overall mean 75.6) matching VPT-Deep (75.6) and performing competitively with more complex approaches. The paper explicitly documents that "simple methods (e.g., Bitfit) which were previously reported as inferior now demonstrate competitive performance" (Section 3). This is the most comprehensive controlled comparison in vision PETL and directly challenges prior claims.

- **Demonstrates prediction diversity across PETL methods and shows ensemble benefits.** Section 4 quantifies prediction similarity matrices (Figure 3) showing 20–35% disagreement among methods that achieve nearly identical accuracy. Venn diagrams (Figure 4) further show that different methods excel at different high-confidence correct predictions and make different low-confidence mistakes. The consistent ensemble gains (Figure 3b) support the claim of practical complementarity, and the analysis goes beyond simple accuracy comparisons.

- **PETL remains competitive with full fine-tuning in many-shot regimes using 2–5% of parameters.** Section 5 and Figure 5 show that on CIFAR-100 (50K samples), RESISC (25.2K), and Clevr-Distance (70K), PETL achieves comparable or better accuracy than full fine-tuning, with performance plateauing after 5% tunable parameters. This challenges the NLP-derived assumption that PETL degrades with abundant data.

- **PETL consistently preserves OOD robustness better than full fine-tuning on CLIP ViT-B/16.** Table 2 shows every PETL method achieves average distribution shift accuracy 12–14 points higher than full fine-tuning (e.g., BitFit 55.4 vs. Full 42.5). The finding is clearly presented for the tested setup.

## Weaknesses

### Fatal
None.

### Major
- **Ensemble evidence uses the worst PETL method as baseline, which inflates the apparent benefit of ensembling.** The paper states (line 388): "we use the worst PETL method as the baseline." Comparing the ensemble of all methods to the *worst* single method is a weak test — the relevant question is whether the ensemble outperforms the *best* single method. As presented, the reader cannot tell whether the ensemble gain represents genuine complementarity or simply averaging noise. This weakens the paper's central claim that different PETL methods "acquire distinct and complementary knowledge." The paper should also report ensemble accuracy relative to the best single PETL method (or the average of the top two).

- **The claim that "full fine-tuning with WiSE can achieve even higher accuracy in both downstream and distribution shift data than PETL" is stated without supporting numbers.** This claim appears in the abstract (line 76) and in Section 7 (line 487), but Table 2 reports only PETL and full fine-tuning without WiSE. No figure or table in the paper compares PETL against full fine-tuning with WiSE on the same benchmark. The paper references Wortsman et al. (2022) for the general effect of WiSE, but a direct, side-by-side quantitative comparison is needed to substantiate the stated finding. As presented, this claim lacks empirical support within the paper.

- **No multiple random seeds or repeated runs for the VTAB-1K results.** The paper reports single-run accuracy for each method (the benchmark uses a single 80/20 split, line 299). The core claim that PETL methods "perform similarly" hinges on accuracy differences of 1–3 percentage points, but without multiple trials the reader cannot assess whether these differences are within the noise of a single run. While single-run evaluation is the standard protocol for VTAB-1K in the literature, a paper positioned as a "unifying reference" would benefit substantially from means and standard deviations over 3–5 seeds to give the similarity claim statistical grounding.

### Minor
- **Hyperparameter tuning search space and final selected values are not reported.** The paper states that learning rate, weight decay, drop path rate, and method-specific parameter sizes were tuned (lines 304–305), and sets a cap of ≤1.5% for PETL parameter size. However, it does not report the search ranges, number of trials, or the final selected hyperparameters per method/dataset. For a paper that emphasizes "careful" and "fair" tuning, this underspecification makes it difficult to reproduce or compare the tuning effort across methods. The reproducibility statement promises detailed documentation in the code, but the paper itself lacks this information.

- **The robustness study uses a single setting (CLIP ViT-B/16, 100-shot ImageNet-1K, four ImageNet distribution shifts), which limits the generality of the robustness claims.** The finding that "PETL is more robust than full fine-tuning to distribution shifts" is presented as a general insight (abstract line 75), but is demonstrated on only one backbone and one target distribution. Testing additional backbones (e.g., a supervised ImageNet-21K ViT) or other types of distribution shifts would strengthen the generality. The paper should frame this as a preliminary observation rather than a general conclusion, or broaden the experiments.

- **The many-shot results (Figure 5) aggregate all PETL methods into a single trend line, hiding per-method variance.** The paper reports accuracy as a function of tunable parameter percentage aggregated across methods. Showing results for at least 3–4 representative methods (e.g., BitFit, LoRA, Adapter, VPT-Deep) separately would reveal whether the trend is consistent or method-dependent.

- **Section 6 ("Why PETL Works") identifies two descriptive patterns but does not offer a causal explanation.** The paper acknowledges this (line 439: "Our intention is not to offer a definitive conclusion"), and the two patterns (full > linear vs. linear > full) are genuinely informative. However, the interpretation that PETL succeeds as a "high-capacity learner with an effective regularizer" is one of several possible explanations. The concave shape on CIFAR-100 (Figure 5d) could also reflect PETL's limited capacity preventing it from matching full fine-tuning, rather than regularization. The section would benefit from formal hypothesis testing rather than visual curve interpretation, but as presented it is a reasonable analysis given the paper's own caveats.

### Trivial
None.

## Nice-to-Haves
- An ablation showing the effect of drop path rate (e.g., drop path=0 vs. 0.1 across methods) would support the claim that it is a key hyperparameter.
- Reporting WiSE results for both full fine-tuning and PETL methods in the robustness table would turn the unsupported claim into a solid finding.
- Adding results on whether the 20–35% prediction disagreements are systematic (same images consistently predicted differently) or stochastic would strengthen the complementarity analysis.

## Removed Points

These points were flagged by the reviewers but do not meet the strict filtering criteria for inclusion as weaknesses in the final review. Treat them with caution.

- **"No statistical significance or repeated runs" framed as a fatal flaw**: While valid as a limitation, single-run evaluation is the standard protocol for VTAB-1K (the benchmark provides a single fixed 80/20 split). Multiple other VTAB-1K papers in the literature follow the same protocol. The concern is real but does not invalidate the results; it is included above as a Major weakness but with appropriate context about community norms.

- **"Prediction complementarity claim overstated — 20% disagreement could be random noise"**: Even if disagreements are stochastic, ensemble averaging would still reduce variance and improve accuracy. The Venn diagrams showing different high-confidence correct predictions further support the complementarity claim. The ensemble baseline issue (covered separately as a Major weakness) is the more substantive problem, not the disagreement analysis itself.

- **"Section 6 (Why PETL Works) is the weakest section conceptually"**: A matter of framing opinion. The paper is transparent about its intent ("not to offer a definitive conclusion"), and identifying two distinct empirical patterns is a legitimate contribution of an empirical study. The section is descriptive, as the paper intends it to be.

- **"Drop path ablation is missing"**: Valid but minor; moved to Nice-to-Haves.

- **Strength Finder's strength about "practical, domain-aware recipes"**: Retained as valid and specific to the paper's contribution. The recipe recommendations in Section 3 are concrete and grounded in the ranking analysis.

## Novel Insights

The most interesting insight that emerges from synthesizing the reviews — beyond what the paper itself claims — is the interplay between the paper's two main findings (similar accuracy + prediction diversity) and the downstream implications for practitioners. The fact that *any* reasonably tuned PETL method achieves similar accuracy on VTAB-1K suggests that the choice among PETL methods can be driven by secondary criteria (parameter count, inference speed, implementation simplicity) rather than accuracy. However, the ensemble analysis (which is the best evidence for complementarity) would be much more convincing if benchmarked against the best single method — without that comparison, the practical recommendation to ensemble different PETL methods is premature. This tension between the "any method works" finding and the "methods are complementary and should be ensembled" finding is not explicitly discussed in the paper and deserves attention.

## Suggestions

1. **Fix the ensemble baseline**: Recompute ensemble gains relative to the *best* single PETL method (or the average of the top two). Report how often the ensemble beats the best individual method. If gains remain, this becomes a strong result.
2. **Provide WiSE results for both full fine-tuning and PETL side-by-side** to support the claim that full fine-tuning with WiSE surpasses PETL. Alternatively, clearly state that this comparison is from prior work and remove the unsupported claim from the abstract.
3. **Add standard deviations over 3–5 random seeds** for the VTAB-1K results. This single change would substantially increase the paper's value as a reference and allow readers to assess whether the observed 1–3 point differences are meaningful.
4. **Report the hyperparameter search ranges and final selected values** per method/dataset, either in an appendix or a supplementary table.
5. **Acknowledge the limited scope of the robustness study** more explicitly, or add at least one additional backbone/dataset to broaden the finding.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>