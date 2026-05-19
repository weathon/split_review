- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5
Now I have a thorough understanding of the paper and all reviewer inputs. Let me compose the final consolidated review.

## Summary

This paper proposes Model-Agnostic Projection Adaptation (MAPA), a federated learning method that treats the entire parameter vector (across all layers) as a single vector and factorizes the model update into a random reconstruction matrix A (d×p, regenerated each round from a shared seed, never communicated) and a trainable projection vector B (p×1, the only thing communicated). The key idea is that by collapsing layers into one vector, the "rank" constraint of per-layer LoRA (q ≤ min(d₁,d₂)) is eliminated, allowing a larger A and smaller B for the same communication budget. The paper also proposes MAPAX, a generalization that spans a continuum from MAPA (k=1) through LoRA to FedAvg, trading off memory vs. representation certainty. Experiments on MNIST, FMNIST, CIFAR-10, and CIFAR-100 show MAPA achieving 93–99% of FedAvg accuracy while communicating only 1–3% as many parameters.

## Strengths

- **Higher representation capacity at same communication (Theorem 1).** The paper provides a formal argument (via Definition 2, Propositions 1–2, Corollary 1) that MAPA's single-vector factorization yields lower reconstruction error variance than layer-wise low-rank methods at the same communication overhead. This is a well-defined theoretical claim about the factorization's expressiveness that goes beyond what prior FL-LoRA analyses provide.

- **Strong empirical communication-accuracy trade-off.** On CIFAR-10, MAPA achieves 98.9% of FedAvg accuracy with only ~1% of FedAvg's communication (Table 1). On MNIST/FMNIST, it maintains 98.5–98.6% of FedAvg accuracy at ~3% communication. These results convincingly demonstrate the practical effectiveness of the method.

- **MAPAX unifies the factorization design space.** Proposition 3 and Corollaries 2–3 show that MAPAXₖ generalizes from MAPA (k=1) through LoRA-style per-layer factorization to FedAvg (k=d), giving practitioners a principled framework for navigating the communication–memory–computation trade-off. This conceptual contribution is absent in prior FL compression work.

- **Convergence analysis.** Theorem 2 provides a convergence bound for MAPA under standard smoothness and gradient variance assumptions, showing that the bound goes to zero as T→∞. While the analysis has gaps (see Weaknesses), the effort to provide theoretical guarantees beyond purely empirical evaluation is a positive feature.

## Weaknesses

### Fatal
None.

### Major
- **Incomplete and incoherent convergence analysis in the main text.** The convergence analysis (Section 4) has several problems that prevent assessment of its correctness from the main text alone: (1) ρ is referenced on line 180 ("the convergence bound of MAPA is influenced by the (3−2ρ) term") but is never defined anywhere in the main text. (2) The (3−2ρ) term does not appear in the stated bound (Theorem 2, line 175), making the discussion in line 180 unmoored. (3) The analysis treats ε as a JL Lemma distortion parameter but does not explain how the JL Lemma connects to the algorithm's sequential optimization with a randomly resampled projection matrix A at each round. While the full proof may reside in the appendix (which is stripped here), the main text should define all key parameters and give a self-contained sketch of how the analysis accounts for the algorithm's specific mechanics — particularly the resampling of A. Without this, the theoretical contribution is not verifiable from the presented material.

- **The static variance analysis does not address the dynamic resampling of A.** The paper's theoretical foundation (Definition 2, Propositions 1–2, Theorem 1) analyzes representation certainty as the inverse of error variance for a *single* random matrix factorization ‖W−AB‖²₂ with A drawn once. However, MAPA regenerates A independently *every round*. Theorem 1 shows that MAPA's factorization has lower reconstruction error variance than LoRA's — but this is a statement about a static decomposition, not about training dynamics in a changing subspace. The paper does not analyze how resampling A affects optimization stability, gradient coherence across rounds, or whether the claimed static advantage propagates through the sequential training process. This is a gap between the theoretical framing and the algorithm's actual behavior.

### Minor
- **Baseline configurations are underspecified.** The paper states "In each scenario, we keep the same amount of trainable parameters" (line 191) but does not report (1) the FA-LoRA rank used, (2) the sparsification rate for Sparse, or (3) the quantization level for Quant. Without these details, the experiments cannot be reproduced or assessed for fairness. This is especially important because FA-LoRA's per-layer factorization structure means that matching total trainable parameters to MAPA's single-vector scheme requires specifying the per-layer ranks.

- **No error bars or statistical significance.** All experimental results are reported as single numbers with no standard deviations, confidence intervals, or multiple-seed runs. It is unclear whether the observed differences between methods are statistically significant, particularly for the smaller-scale datasets where accuracy differences are small.

- **MAPAX results are presented qualitatively.** The MAPAX experiments (Figure 6) are shown as heatmaps without reporting the actual accuracy values or providing a quantitative comparison to MAPA and baselines at matched settings. The paper claims MAPAX "provides memory and computationally efficient solutions for slightly underperforming MAPA" (line 248) but does not quantify "slightly" or provide direct accuracy/communication comparisons.

### Trivial
- The phrase "5.5 parameters" on line 187 (ResNet model size for CIFAR-100) is almost certainly missing a magnitude unit (likely "5.5M" or "5.5 million").
- An extraneous garbled token "wmihneirme" appears on line 178 (parser artifact, but worth noting for a clean camera-ready version).

## Nice-to-Haves
- **Ablation: fixed A vs. resampled A.** The paper's core innovation includes resampling A each round, but there is no ablation comparing MAPA against a variant where A is fixed across rounds (i.e., a static random projection). Such an experiment would isolate whether the resampling is beneficial or merely adds noise, and would strengthen the paper's claims.
- **Practical overhead numbers.** The paper acknowledges that generating the large d×p matrix A imposes memory/computation costs and proposes MAPAX as a mitigation, but reports no actual runtime or memory measurements. Including these would help practitioners assess the practical feasibility.
- **Figure 6 quantitative comparison.** Adding a table with accuracy values for representative (k, p) configurations from the MAPAX heatmaps would make the results actionable.

## Removed Points

These points from the reviewers were considered and removed with justification:

- **FA-LoRA communication percentages of 0.538% and MAPA 2.96%**: These specific numbers are from the table image, which I cannot verify from the extracted text. The paper states trains all methods with "the same amount of trainable parameters," which would imply comparable communication costs. The general concern about comparison fairness is retained in Minor weaknesses above, but the specific unverifiable numbers are removed.
- **"Unfair" comparison claim**: The assertion that FA-LoRA may be "underpowered" due to low rank is speculative without knowing the rank used. The paper claims matched trainable parameters, so this criticism cannot be substantiated from the available text. Removed as speculative.
- **"wmihneirme" as evidence of corruption**: Parser artifact; per instructions, such formatting issues are not author errors. Removed.
- **Generic criticisms about missing proofs/appendix**: Per instructions, appendix sections are stripped from the extracted text. The criticism that "the proof is not provided" for Theorem 2 is removed since it may reside in the appendix.
- **Claim that Theorem 2's bound is "generic to SGD with compressed gradients"**: This is a speculative assertion about the proof content (which is in the appendix) and cannot be verified from the main text. Removed.
- **Criticism about non-IID split not being "standard"**: The paper describes its split methodology clearly (20 shards, 5 per client). Whether it is "standard" or not is immaterial; what matters is that it is specified and reproducible. Removed.
- **Claim that MAPA cannot "outperform in both" because FA-LoRA uses less communication**: This depends on specific table values I cannot verify. The general concern about claim precision is retained in Minor weaknesses.
- **Strength Finder strengths about "important problem" and generic framing**: Removed as generic/superficial (e.g., any strength that just says "this paper addresses an important problem"). The specific, evidenced strengths are retained.
- **Missing related works**: Per instructions, I cannot verify related works completeness without external sources.

## Novel Insights

None beyond the paper's own contributions. The reviewers surface no perspective that meaningfully reframes or extends the paper's findings beyond what the authors themselves present.

## Suggestions

1. **Fix the convergence analysis in the main text.** Define ρ explicitly, explain where the (3−2ρ) term originates, and describe how the analysis accounts for the resampling of A across rounds (or prove convergence for a fixed A and then justify why resampling helps empirically). Even a brief proof sketch in the main text would substantially improve confidence in the theoretical claims.

2. **Report all baseline hyperparameters in full.** Provide the FA-LoRA rank per dataset, the sparsification rate, quantization level, and any other configuration details needed for reproducibility. A table in the main text or appendix would suffice.

3. **Add error bars.** Report results over at least 3 random seeds with standard deviations or confidence intervals for the main experimental comparisons.

4. **Quantify the MAPAX results.** Add a table showing accuracy values for selected (k, p) configurations from the MAPAX sweep, with a clear comparison to MAPA and FA-LoRA at equivalent settings.

5. **Soften the "outperforms in both" claim.** The current phrasing in the abstract and introduction could be read as claiming MAPA dominates all baselines on both communication and accuracy simultaneously. Consider more precise language (e.g., "achieves superior accuracy while dramatically reducing communication" or "offers a better accuracy-communication trade-off than existing methods") to avoid potential misinterpretation.
