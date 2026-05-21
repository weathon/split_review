---
job_id: 080b0758-8d00-4a03-ab13-467f5009b3d3
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: f4B4ohWO53.pdf
paper: Differential Privacy for Transformer Embeddings with Nonparametric Variational Information Bottleneck
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, combining representation learning for language, variational/Bayesian methods, and privacy in machine learning.

## Minimum Quality
Pass ✅ The paper contains the core components expected of a research submission, including abstract, introduction, technical method, experiments, quantitative results, and conclusion. While the presentation and validation have notable weaknesses, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not detect any hidden prompts, manipulative reviewer instructions, or suspicious embedded text in the provided paper content or figures.

# Expected Review Outcome:
## Summary
This paper proposes Nonparametric Variational Differential Privacy, NVDP, a method for privatizing transformer text embeddings by inserting an NVIB layer into a transformer architecture, sampling noisy multi-vector embeddings at both training and test time, and evaluating privacy using Rényi divergence together with a Bayesian differential privacy interpretation. The empirical evaluation compares NVDP against non-private BERT baselines and a VIB-based ablation, VTDP, on several GLUE tasks, with the goal of showing a better privacy-utility tradeoff for the nonparametric bottleneck.

## Strengths
The paper tackles a relevant problem. Sharing embeddings instead of raw text is common in practice, and the paper correctly points out that transformer hidden states can still leak sensitive information. A mechanism tailored to multi-vector transformer embeddings is more interesting than applying a scalar or sentence-level perturbation recipe unchanged.

The architectural idea is coherent. In **Figure 1** the authors clearly communicate the intended privacy bottleneck: BERT embeddings are projected to NVIB parameters, sampled into a noisy representation, then passed through denoising attention, and the residual connection around that block is removed to avoid bypassing the stochastic bottleneck. That design choice is sensible and, at least conceptually, directly addresses a common failure mode where private information leaks through skip paths.

The empirical comparison against the VIB-style ablation is often favorable. In **Table 1**, NVDP improves over VTDP on several tasks in both utility and the reported privacy metrics, for example on MRPC, where NVDP reaches 83.0 accuracy with RD 0.34 versus VTDP at 81.1 with RD 1.20, and on QNLI, where NVDP achieves 89.5 accuracy with RD 0.75 versus VTDP at 87.1 with RD 1.80. This supports the narrow claim that the nonparametric formulation is more effective than the tokenwise Gaussian bottleneck used in the ablation.

The appendix tradeoff table is also informative. **Table 2** makes clear that increasing regularization decreases the reported RD/BDP values for both NVDP and VTDP, while utility degrades, which is the expected qualitative behavior for a privacy-utility tradeoff study. It is useful that the paper does not hide this monotonic trend.

The paper is reasonably easy to follow at a high level. The motivation, background on NVIB, and broad architecture are understandable without requiring the reader to reconstruct the entire approach from supplementary materials.

## Weaknesses
1. **The central privacy claim is much weaker than the title and repeated wording suggest, and the paper often blurs empirical distinguishability with a formal differential privacy guarantee.**  
   The title and abstract imply “differential privacy for transformer embeddings,” but the actual procedure in **Section 3.2** does not establish a standard local DP guarantee over a clearly defined adjacency relation and all possible neighboring inputs. In fact, the paper explicitly states, on **Page 5**, “We do not assume any specific notion of adjacency between examples,” and then reports the maximum Rényi divergence over all input pairs in the test set. That is not the same as proving an LDP mechanism with respect to a formally specified neighboring relation over the input domain.  
   This matters a lot. DP is not just “small divergence on many observed pairs.” Without a domain-level sensitivity argument or a proof that the mechanism satisfies the stated bound for all adjacent inputs, the result is at best an empirical privacy proxy over a finite sample of examples. The paper can still be interesting as a privacy-inspired representation learning method, but the current framing overstates what has actually been shown.

2. **The privacy evaluation is entirely proxy-based and omits the most obvious empirical validation, namely attack-based leakage tests.**  
   The introduction motivates the work using reconstruction or inference attacks, citing risks like reverse engineering original text. Yet the experiments in **Section 4** only report RD and converted BDP values, with no reconstruction attack, membership inference, attribute inference, nearest-neighbor recovery, or inversion evaluation. This is a major hole. If the claim is that the embeddings are safer to share, readers need evidence that concrete attacks become less effective, not only that pairwise divergences among learned posterior distributions are smaller.  
   The omission matters because divergences computed under the model's own assumed posterior family may correlate imperfectly with actual leakage to realistic adversaries. A method can look good under its own internal privacy score while still leaking through a stronger attack model.

3. **Equation (7) is presented as the key privacy quantity, but its derivation and assumptions are underspecified, and the notation is shaky enough that I do not trust the formula as stated.**  
   On **Page 6**, the paper gives  
   \[
   D_{\lambda}\!\left(\mathrm{DP}(G_0^q,\alpha_0^q)\,\|\,\mathrm{DP}(G_0^{q'},\alpha_0^{q'})\right)\le \cdots
   \tag{7}
   \]
   but several points are unclear or problematic:
   - The paper says it computes RD for a finite sampling procedure and that this is an upper bound on the RD between the underlying DPs, but the displayed left-hand side is the divergence between the DPs themselves, not between the induced finite-sequence distributions. The object on the left and the explanation in the text are not aligned.
   - The formula uses token-position alignment by output order, even though the underlying mixture is permutation invariant. The text says this gives an upper bound because the ordered list is “more informative,” but that step is asserted rather than proved. It is not obvious that the divergence between ordered sampled sequences upper bounds the divergence between the corresponding exchangeable random measures in the way required here.
   - The Gaussian term contains \(\mathbf{1}\left(\log \frac{\boldsymbol{\sigma}_i'}{(\boldsymbol{\sigma}_0^p)^{(1-\lambda)}(\boldsymbol{\sigma}_i^q)^\lambda}\right)\), where \(\mathbf{1}\) is said to be a vector of ones. Presumably this means a sum of coordinates, but that is not written correctly. As stated, this is dimensionally awkward and nonstandard notation for the multivariate Gaussian Rényi divergence.
   - The definition \(\boldsymbol{\sigma}_i' = \sqrt{(1-\lambda)(\boldsymbol{\sigma}_i^{q'})^2 + \lambda(\boldsymbol{\sigma}_i^q)^2}\) is concerning because for \(\lambda>1\), the coefficient \(1-\lambda\) is negative. The expression can fail to remain positive componentwise unless extra conditions hold. Those conditions are not stated, yet the formula relies on \(\boldsymbol{\sigma}_i'\) being valid inside norms and logarithms.
   
   Since Equation (7) underpins the reported RD values in **Table 1**, this is not a cosmetic issue. If the formula or its applicability is wrong or too narrow, the main privacy results become hard to interpret.

4. **The conversion from RD to BDP is treated as a black box, which makes the advertised “interpretable guarantee” difficult to assess.**  
   In **Section 2.1** and **Section 3.2**, the authors say they use the accounting mechanism from Theorem 2 of Triastcyn and Faltings (2020), but the actual instantiated formula, assumptions, and dependence on the empirical data distribution are omitted from the main paper. Then **Table 1** reports BDP values such as 10.70, 12.10, 20.93, etc., presented as “strong privacy guarantees.” Without the mapping being explicit, it is very hard to judge what those numbers mean or why the reported BDP values are only mildly different across settings when the raw RD changes dramatically. For example, in **Table 2** on MRPC, NVDP moves from RD 0.89 to 0.008 as regularization increases from \(10^{-3}\) to \(1\), but the reported BDP only moves from 10.95 to 10.40. That compression is not explained in the paper.  
   This matters because the paper leans heavily on BDP for interpretability, yet the reader cannot verify how those guarantees arise or whether they are meaningful beyond this empirical dataset.

5. **The experimental protocol is not rigorous enough for the strength of the empirical claims, and some choices raise evaluation concerns.**  
   The paper says in **Section 4.1** that it performs five runs and selects the best-performing run on the validation set for final evaluation on the test set. But **Table 1** reports “best-achieved utility score alongside privacy guarantees” for each private model, and **Table 2** shows multiple regularization weights. It is not clear whether the summary table corresponds to a fixed model-selection rule decided on validation only, or whether it effectively cherry-picks the most favorable test-time tradeoff point per task. That distinction matters a lot. A fair privacy-utility comparison should specify a model-selection criterion before looking at test results.  
   More generally, reporting only the best run is weak practice for unstable fine-tuning settings. Means and standard deviations over runs are needed, especially since some apparent gains in **Table 1** are small, such as QQP 88.3 vs 88.4 or QNLI 89.5 vs 89.7.

6. **The baseline set is too narrow for a paper whose main claim is about privacy-preserving text embedding release.**  
   The baselines in **Section 4** are vanilla BERT, dropout/weight decay, and the VTDP ablation. The VTDP comparison is useful for isolating the contribution of NVIB relative to a parametric bottleneck, but it is not enough to establish competitiveness as a privacy method. There are no comparisons to other embedding privatization or local-DP style text representation mechanisms.  
   This weakens the significance of the empirical conclusion. Right now the paper shows “NVDP beats one closely related ablation,” not “NVDP is a strong method for this problem class.”

7. **The utility claims are somewhat overstated relative to the evidence in Table 1 and Figure 2.**  
   The paper says NVDP “consistently achieves better privacy-utility points” and in **Section 4.2** says the blue curves in **Figure 2** “consistently occupy the most favorable region.” This is too strong. On SST-2, for instance, **Table 1** shows VTDP with slightly better utility, 92.3 vs 91.7, at the same reported BDP 10.90, and on RTE the NVDP accuracy remains below the non-private baselines and is only modestly different from VTDP. Also, the tradeoff plots in **Figure 2** contain only a handful of points per task, corresponding to a few regularization settings, so they are not enough to substantiate a strong frontier claim.  
   The figure itself is still useful, but it supports a more modest statement: NVDP often dominates VTDP in the explored settings, not universally and not with exhaustive tuning.

8. **The method description leaves implementation-critical details vague, which hurts reproducibility and also the interpretation of the privacy metric.**  
   Examples include:
   - Whether BERT is fully fine-tuned jointly with the NVIB layer or partly frozen is not stated clearly in the main method section.
   - The exact location of the added transformer layer relative to BERT output is implied by **Figure 1**, but architectural dimensions, classifier head details, and whether [CLS] or all token vectors are used downstream are not specified.
   - The hyperparameterization is ambiguous. In **Equation (5)** there are separate \(\lambda_D\) and \(\lambda_G\), but **Table 2** reports a single \(\lambda\). If these were tied, that should be stated explicitly; if not, the table is underspecified.
   - In **Section 3.3**, the authors say “in our experiments, one vector is sampled from each component, so \(\kappa_i=1\),” which effectively turns the sampling procedure into a fixed one-sample-per-token scheme. That simplification is important and should be motivated more clearly, because it changes the relation between the DP formalism and the actual mechanism being shared.

9. **There are several mathematical and exposition issues that, while individually small, accumulate and reduce confidence.**  
   A few examples:
   - In **Equation (4)**, \(G_i^q = \mathcal{N}(\mu_i^q, \mathbf{I}(\sigma_i^q)^2)\) is written in a way that obscures whether the covariance is diagonal \(\mathrm{diag}((\sigma_i^q)^2)\) or scalar times identity. Later the notation suggests elementwise variances.
   - On **Page 7**, the weight decay penalty is written as \(\frac{\lambda}{2}\|\mathbf{y}\|\) and later \(\lambda\|\mathbf{y}-\mathbf{y}_0\|\), missing the square one would normally expect in standard \(L_2\) regularization.
   - There are several typos and wording issues, for example “celebrated to the downstream task” on **Page 2**, “Guassain” on **Page 3**, “facorised” on **Page 6**, “regularizaton” and “Drouput” on **Page 7**. None of these is fatal, but together they make the paper feel less carefully checked than it should be for a mathematically oriented submission.

10. **The paper does not define a realistic threat model with enough precision.**  
    The text alternates between protecting against reconstruction, de-anonymization, and generic distinguishability. It also evaluates privacy by comparing every pair of examples, without distinguishing whether the attacker knows the task, the encoder, the posterior family, or a candidate pool of texts. These are not equivalent adversaries. The resulting privacy numbers therefore float somewhat free of a concrete deployment scenario.  
    This matters because privacy guarantees are only meaningful relative to a threat model. Right now the paper presents a mechanism, a divergence, and a converted BDP number, but the real-world implication of those numbers remains vague.

## Questions
1. The biggest issue for me is the privacy claim itself. Can the authors state precisely what theorem they believe holds for the released mechanism \(x \mapsto S\)? Is the claim a formal local DP guarantee over a defined adjacency relation, or an empirical privacy score measured over a finite dataset? A careful rebuttal should distinguish these two and avoid treating them as interchangeable.

2. Please provide a clean derivation or correction of **Equation (7)** in the main paper. In particular:
   - what is the exact random object whose Rényi divergence is being computed,
   - under what conditions is \(\boldsymbol{\sigma}_i' = \sqrt{(1-\lambda)(\boldsymbol{\sigma}_i^{q'})^2 + \lambda(\boldsymbol{\sigma}_i^q)^2}\) well-defined for \(\lambda=1.1\),
   - and how should the \(\mathbf{1}(\log(\cdot))\) term be interpreted mathematically?

3. How exactly are the points in **Table 1** selected from the settings in **Table 2**? Is the regularization strength chosen using validation only, or is the reported point the best test-set tradeoff chosen post hoc? A precise model-selection protocol would increase my confidence substantially.

4. Can the authors report mean and standard deviation across the five runs rather than only the best run? Several reported differences are small, and it is hard to know whether they are statistically meaningful.

5. Since the motivation in the introduction is about information leakage and reconstruction, can the authors add at least one direct attack-based evaluation, such as text inversion, attribute inference, or retrieval-based re-identification from shared embeddings? Even a limited experiment would make the privacy story much more convincing.

6. Why is \(\kappa_i=1\) fixed in **Section 3.3**? Does the method rely on exactly one sampled vector per component, and if so, how much of the claimed advantage over VTDP comes from this structural choice rather than the nonparametric prior itself?

7. The paper says no adjacency notion is assumed. If that is intentional, how should readers compare the reported privacy numbers with standard local DP mechanisms, where adjacency is central? Clarifying the intended interpretation would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond the standard caution that privacy claims should be stated precisely. My concerns are scientific and methodological rather than an ethics-review issue.

## Soundness Rating
2: fair. The paper has a coherent high-level method and some useful experiments, but the technical core of the privacy guarantee is not established with enough rigor, and the main empirical privacy evidence is too indirect.

## Presentation Rating
2: fair. The paper is readable at a high level and **Figure 1** helps, but the mathematical exposition around **Equations (4), (7), and (8)** is not careful enough, and important experimental details are left ambiguous.

## Contribution Rating
2: fair. The idea of combining NVIB with embedding privatization is interesting, and the comparison to VTDP suggests some value, but the limited baseline set and overclaimed privacy interpretation reduce the overall contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is interesting and points in a worthwhile direction, but for ICLR I think the current version falls short because the claimed differential privacy guarantee is not demonstrated in a sufficiently formal or empirically convincing way, and the evaluation is too narrow for the scope of the claims.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main technical and experimental claims carefully, though some parts of the NVIB-specific derivation would benefit from author clarification.