Now I have a clear picture. Let me synthesize the final review.

## Summary
This paper investigates whether the counterintuitive phenomenon of likelihood—where deep generative models assign higher likelihood to anomalous data than normal data—occurs in tabular anomaly detection, as it does in the image domain. The authors propose a domain-agnostic definition of this phenomenon (Definition 3.3), run extensive experiments across all 47 ADBench tabular datasets and 10 CV/NLP embedding datasets with 12 baselines, and find that simple likelihood-based detection with normalizing flows (NF-SLT) works well and rarely exhibits the phenomenon. They further analyze the causes through theoretical results (linking dimensionality to likelihood gap under independence assumptions) and empirical analysis (linking feature correlation to intrinsic dimension).

## Strengths
- **Domain-agnostic definition of the counterintuitive phenomenon**: Definition 3.3 formalizes the phenomenon using relative AUROC performance against multiple comparison models (Eq. 2 and 3), overcoming the vagueness of prior definitions that relied only on overlapping likelihoods or simple AUROC thresholds.
- **Comprehensive empirical evidence on all ADBench datasets without selection bias**: Table 1 (top) shows that across 47 tabular datasets, NF-SLT achieves the highest average AUROC (0.8575), lowest average rank (3.43), highest Top2 Ratio (0.45), and lowest Fail Ratio (0.02) among 13 models. This directly demonstrates the core claim.
- **Theoretical link between dimensionality and likelihood gap**: Theorem 5.4 proves that under product-distribution assumptions, when ℍ(P) > ℍ(Q), the expected log-likelihood gap lower bound becomes negative and decreases linearly with dimension d. Corollary 5.6 extends this to show that the maximum achievable AUROC declines with d, providing a theoretical rationale for why low-dimensional tabular data avoids the inversion problem.
- **Quantitative feature-correlation analysis via intrinsic dimension**: Figure 1 (right) and Table 4 show that tabular datasets have much higher d Ratio (ID/ambient dimension) than image datasets (e.g., 0.700 for magicgamma vs. 0.003 for CIFAR-10). Table 4 (bottom) demonstrates that NF-SLT fails on most datasets with low d Ratio, empirically grounding the claim that weak feature correlation in tabular data supports the success of likelihood-based detection.
- **Consistent explanation across data modalities**: The framework explains why NF-SLT also works well on CV/NLP embeddings (Section 5.2) by showing these embeddings have higher d Ratio than raw pixels, tying the theoretical/empirical analysis to out-of-domain data consistently.

## Weaknesses

### Fatal
None.

### Major
- **Hyperparameter selection procedure is described ambiguously**: The paper states: "For each dataset, after experimenting with all combinations in the hyperparameter searching space with 10 repeated experiments, the hyperparameter combination with the highest average AUROC for all datasets is selected." The phrasing "for each dataset" conflicts with "for all datasets." If per-dataset hyperparameter tuning was used, this would overestimate NF-SLT's performance relative to baselines (which may not have received the same per-dataset optimization). If a single global configuration was chosen, this should be stated unambiguously. This ambiguity undermines confidence in the comparison results and must be resolved for reproducibility. [Verbatim from Section 4, Evaluation paragraph]

### Minor
- **Definition 3.3 is not operationalized with explicit thresholds in the main text**: The definition introduces parameters β and γ (Eq. 2 and 3) but never specifies concrete values or a procedure for setting them. The paper later appeals to the definition qualitatively (e.g., for the 'yeast' dataset, the min AUROC gap is 0.02; for 'imdb', the gap is "very small") without stating what γ would make these judgments valid. While the "fully rigorous formulation" is deferred to Appendix B (stripped from this version), providing example thresholds (e.g., drawn from the CIFAR-10/SVHN case) in the main text would make the central quantitative claim directly verifiable. [Verbatim from Section 3, Definition 3.3 and surrounding text]
- **Theoretical analysis assumes independent features, limiting direct applicability**: Theorem 5.4 and its corollaries are derived under the assumption that P and Q are product distributions (independent components). While this is a standard theoretical simplification and the paper states the assumption, the presentation somewhat overstates the theoretical grounding. The paper would benefit from explicitly acknowledging that the theory is a tractable idealized model whose predictions are then validated empirically — the current framing ("We demonstrate a theoretical and empirical analysis") blurs this distinction. [Verbatim from Theorem 5.4 statement: "Let P = ∏_{i=1}^d p_i(x_i) and Q = ∏_{i=1}^d q_i(x_i) be independent d-dimensional continuous probability density models"]
- **Dimensionality evidence in Table 2 is not monotonic for all cases**: For CIFAR-10/SVHN, the AUROC goes 0.3311 → 0.2924 → 0.2984 → 0.3143 as dimension decreases from 1024 to 30 — the improvement is modest and non-monotonic. The text claims "the improvement remains substantial" but this particular case is ambiguous. For CIFAR-100/SVHN the trend is clearer (0.0843 → 0.3490). The evidence would be stronger with confidence intervals and more candid discussion of case-by-case variability. [Verbatim from Table 2]
- **Only four tabular datasets have ID estimates reported explicitly**: Table 4 (top) lists ID estimates for only 4 tabular datasets (magicgamma, satellite, landsat, waveform) and 4 image datasets. While the scatter plot in Figure 1 (right) appears to show all 47 tabular points, the small explicit sample makes it hard for readers to verify the general claim. Providing ID estimates for all datasets or a more comprehensive table would be helpful. [Verbatim from Table 4]

### Trivial
- The phrase "For each dataset... the hyperparameter combination with the highest average AUROC for all datasets is selected" is syntactically contradictory and should be reworded for clarity.

## Nice-to-Haves
- Adding one or two more recent deep AD baselines (e.g., Deep SAD, DROCC) would strengthen the claim that NF-SLT's dominance is not an artefact of using older baselines.
- Reporting standard deviations or confidence intervals from the 10 repeated experiments would help assess whether the performance gaps between NF-SLT and the second-best method (ICL) are statistically meaningful.
- A more detailed analysis of the 'imdb' embedding dataset (where NF-SLT underperforms GOAD) beyond noting that the gap is small would strengthen the narrative.

## Removed Points
These points were flagged by reviewers but are removed with justification:
- **"The baselines are somewhat dated"** (Harsh Critic): The paper uses 12 baselines including ICL (2022) and MCM (2024), which are recent. The criticism about missing DROCC, Deep SAD, RDP is a scope-creep request for a specific set of methods not standard in this sub-area. Moved to Nice-to-Haves.
- **"ICA and resizing use different architectures (RealNVP vs Glow)"**: The paper explicitly acknowledges this limitation for the resize experiment ("Since this experiment uses raw images, independence between pixels is not guaranteed, so the theorem presented in Appendix D cannot be applied"). The different architectures serve different purposes (ICA isolates dimension; resize tests generalizability). Not a genuine flaw.
- **"Only four tabular datasets listed for ID estimates"**: The scatter plot in Figure 1 (right) plots all datasets; only four are explicitly labeled. The full set of ID estimates is likely in the appendix. Remains as minor but with tempered severity.
- **"Theoretical analysis overstates grounding"**: The paper clearly states the independence assumption in Theorem 5.4 ("Let P = ∏ p_i(x_i)"). This is standard practice in theoretical analysis. The strength of the paper is primarily empirical. Scaled down to minor.
- **Various reproducibility nitpicks about undisclosed hyperparameters**: Hyperparameter details are referenced to Appendix F. The stripped appendix means we cannot verify, but this is not a valid criticism.

## Novel Insights
The most interesting observation from the meta-review is that the paper's central finding — likelihood-based detection works well on tabular data — is robustly supported by the aggregate experimental results (Table 1), yet the paper's own Definition 3.3 cannot be cleanly applied to those same results because β and γ are never specified. This tension between the formal definition (which requires explicit thresholds) and the empirical demonstration (which relies on aggregate metrics like average rank and fail ratio) is an unresolved gap. The reviewer's instinct to demand per-dataset application of the definition is well-founded — it would force the authors to commit to specific thresholds and make the core claim falsifiable. The paper is also unusual as an empirical-study paper that also makes a theoretical contribution; the theory (Theorem 5.4) is clean but narrow, and the interesting action is really in the careful empirical design (the d Ratio analysis, the ID estimation linking correlation to detection failure).

## Suggestions
1. **Resolve the hyperparameter selection ambiguity** unambiguously. State clearly whether a single global configuration was chosen per model (maximizing average AUROC across all datasets) or whether per-dataset tuning was used. If the latter, justify why this does not inflate NF-SLT's results relative to baselines.
2. **Operationalize Definition 3.3** by stating explicit β and γ values (e.g., β = 0.5, γ = 0.05) drawn from the CIFAR-10/SVHN case, and report for each of the 47 datasets whether the phenomenon occurs under the definition.
3. **Acknowledge the independence assumption in Theorem 5.4 more explicitly** in the main text (e.g., "Under the idealized assumption that features are independent, we show...") rather than embedding it in the theorem statement alone.
4. **Add per-dataset results** as a supplementary table showing AUROC for all 47 datasets and 13 methods, so readers can inspect the distribution rather than relying solely on aggregates.

## Score and Decision

**Calibration Anchors:**
- *Round 1 (Bracketing)*: Weak band examples at ~3.0 (e.g., "Flow-based imputation of small data" at 3.0, "TabKANet" at 3.00). Middle band examples at ~5.75 ("NCSNAD" at 5.75, "DRL" at 5.75) and ~6.67 ("MCM" at 6.67). Strong band examples at 8.00 ("Deep Orthogonal Hypersphere Compression").
- *Round 2 (Narrowing)*: "Explaining the OOD Detection Paradox through Likelihood Peaks" at 5.67 — a related paper on explaining the counterintuitive likelihood phenomenon (in images) that was rejected due to weak theoretical grounding and hyperparameter sensitivity issues. The current paper is stronger: it has broader empirical scope (47 datasets), a clearer definition, and more consistent evidence. "AnoLLM" at 6.75 — a strong method paper accepted for tabular AD. The current paper is a different genre (analysis paper vs method paper) but of comparable quality. MCM at 6.67 — accepted with minor weaknesses. The current paper has more non-trivial weaknesses (definition operationalization, hyperparameter ambiguity) than MCM but a broader scope.

*Initial bracket*: [5.0, 7.0]
*Final score*: **6.0** — positioned above DRL (5.75) and the OOD paradox paper (5.67) due to stronger empirical scope and clearer contributions, but below MCM (6.67) because the operationalization gap in Definition 3.3 and ambiguous hyperparameter reporting are more significant than MCM's weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>