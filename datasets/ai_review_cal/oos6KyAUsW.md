- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes DFHTE, a method that uses a diffusion probabilistic model to generate unobserved confounders for conditional average treatment effect (CATE) estimation. The key idea is to run a forward diffusion process on the observed covariates \(X\), infer a latent generation factor \(\eta\) from \(X\), and then use a reverse diffusion process conditioned on \(\eta\) to generate unobserved confounders \(Z\) that are used alongside \(X\) for CATE estimation. The paper derives a variational lower bound as a training objective and evaluates against 12 baselines on two synthetic and two benchmark datasets.

## Strengths

1. **Novel application of diffusion models to unobserved confounder generation for CATE.** The paper is among the first to bring diffusion-based generative modeling to the problem of unobserved confounding in causal inference. The framework using a shared prior \(\eta\) connecting observed and unobserved confounders (Figure 1) is a conceptually interesting design.

2. **Ablation study confirms the generated features are not just random noise.** Figure 2 shows that DFHTE(Generation) consistently outperforms DFHTE(Gaussian) and DFHTE(Uniform), where noise is used instead of generated features, and also outperforms DFHTE(None) which ignores unobserved confounders. This provides meaningful evidence that the diffusion model produces features with useful structure.

3. **Parameter study shows the generated \(Z\) adds value across different regularization strengths.** Figure 3 compares DFHTE(\(X\)) vs. DFHTE(\(X+Z\)) across a wide range of the imbalance penalty \(\alpha\). The red line (with generated \(Z\)) lies below the blue line (without \(Z\)) for nearly all values of \(\alpha\) on both ACIC and IHDP, demonstrating robustness of the improvement.

4. **Comprehensive comparison against 12 baselines** including CFR variants, GANITE, CEVAE, BNN, and traditional ML methods across four datasets.

## Weaknesses

### Fatal
None.

### Major

1. **The variational bound (Equation 6) is not a proper lower bound as presented.** The core training objective is stated as:

\[
\mathbb{E}[-\log p_{\theta}(z^{(0)})] \le E_{q}\left[\log\frac{q(x^{(1:T)},\eta|x^{(0)})}{p_{\theta}(z^{(0:T)},\eta)}\right]
\]

The numerator \(q(x^{(1:T)},\eta|x^{(0)})\) involves the forward diffusion on the *observed* variable \(x\), while the denominator \(p_{\theta}(z^{(0:T)},\eta)\) is over the *unobserved* variable \(z\). A valid variational bound for a generative model of \(z\) requires both numerator and denominator over the same latent chain \((z^{(1:T)},\eta)\). The paper's justification — "both the unobserved and observed variables share the same prior" and "we assume a similar distribution for these variables" (lines 132–133) — does not bridge this gap: sharing a prior does not make the ratio well-defined when the variables are distinct and no observed data for \(z\) exists. The expectation \(E_q\) is taken under a distribution over \(x\), but the denominator contains \(z\), which is not defined under this measure. Since this VLB is the central training mechanism for the diffusion model (Equation 10 uses it directly), the theoretical grounding of the method is undermined. The method may still work as a heuristic, but the paper presents it as a proper derived bound, which it is not.

2. **The evaluation does not convincingly test whether generated \(Z\) corresponds to *unobserved confounders* rather than simply useful latent features.** The benchmark datasets (ACIC, IHDP) are standard in causal inference but do not contain genuine unobserved confounders — they are constructed from real covariates with all confounders assumed observed. The two synthetic datasets (Sim-\(z\), Sim-\(\eta\)) are mentioned by name (Section 4.1) without any description of their generative process, causal graph, or how unobserved confounding is introduced. Without this information, the reader cannot assess whether the experimental design actually tests the ability to recover hidden confounders. The ablation study (Figure 2) shows that DFHTE(Generation) outperforms DFHTE(None), but this could be explained by the diffusion model providing useful additional features for the downstream prediction task, without those features being causally meaningful confounders that affect both treatment and outcome. The paper does not include diagnostic tests (e.g., correlation analysis with treatment and outcome, intervention-based checks) to distinguish between these explanations.

3. **Insufficient description of key methodological details.** The paper does not describe how the synthetic datasets (Sim-\(z\), Sim-\(\eta\)) are constructed, what causal graph they assume, or how the ground-truth unobserved confounders relate to treatment and outcome. This makes it impossible to evaluate whether the experimental setup is appropriate for the task. Additionally, the paper references Algorithm 1 for the inference procedure in the main text but does not include it — though the appendix may have been stripped by the parser, the main text should provide a self-contained outline.

### Minor

1. **Overclaimed results.** The abstract claims "consistent improvements" and the conclusion (line 214) states the model "can always achieve the better performance." However, the critic's examples (which appear consistent with Table 2) suggest DFHTE is not the best on all dataset/metric combinations (e.g., BNN on Sim-\(\eta\) for PEHE, CFR\_MMD on IHDP). The paper should temper these claims to match the actual results, which show DFHTE is competitive and often best, but not uniformly dominant.

2. **No evidence that the generated \(Z\) possesses the claimed causal structure.** The paper asserts that \(Z\) captures unobserved confounders that affect both treatment and outcome (the backdoor path \(A \leftarrow Z \rightarrow Y\)), but provides no analysis demonstrating that the generated features correlate with both \(A\) and \(Y\) after controlling for \(X\). The t-SNE visualizations (Figures 4, 5) are only inspected qualitatively and do not address this question.

3. **The motivation for choosing diffusion models over VAEs/GANs is asserted rather than demonstrated.** The paper states that "GAN and VAE-based cannot fully describe the latent information" (line 18) but provides no mechanism or empirical comparison explaining why the denoising inductive bias of diffusion models is specifically advantageous for modeling unobserved confounders. The baselines include CEVAE and GANITE, but no analysis isolates what the diffusion formulation adds beyond capacity.

### Trivial

- The t-SNE visualizations (Figures 4, 5) are interpreted purely qualitatively. The observation of "strip-like" or "rod-like" representations is not linked to any quantitative metric.

## Nice-to-Haves

- **Causal diagnostic tests:** Show that the generated \(Z\) correlates with both treatment assignment \(A\) and outcome \(Y\) after controlling for observed \(X\), providing evidence that it captures *confounders* specifically.
- **Controlled synthetic experiments with known ground-truth \(Z\):** Describe the generative process for Sim-\(z\) and Sim-\(\eta\) in detail, and show that the recovered \(Z\) recovers features correlated with the true hidden confounders.
- **Computational cost comparison:** Report training time vs. baselines, since diffusion models are computationally expensive.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"Algorithm 1 not in main text / appendix missing":** Per guidelines, the parser strips appendix content; this exists in the original submission.
- **"Missing architecture/hyperparameter details (ε_θ network, T, learning rate schedule)":** Removed per guidelines on trivial implementation details.
- **"Number of experimental runs not stated":** Minor implementation detail removed per guidelines.
- **"Results don't show consistent improvements":** This is factually incorrect based on the paper's claims — the paper claims "best in more cases" not all cases. However, the language is softened to Minor weakness about overclaiming.
- **"Cannot be independently verified due to unreleased models":** Per guidelines, cited models and benchmarks are assumed to exist.
- **"GAN/VAE motivation not justified — no evidence given":** The paper provides some justification (lines 18, 86); the criticism is weakened to Minor.

## Novel Insights

The strength finder and harsh critic together surface a tension that the paper does not fully confront: because unobserved confounders \(Z\) have no ground-truth observations, any method that generates them faces an identifiability problem. The paper implicitly treats this as an optimization challenge addressed by the VLB, but the VLB derivation itself is not properly grounded (mixing \(x\) and \(z\) spaces). A genuinely novel insight that emerges is the use of a shared prior \(\eta\) to couple the observed and unobserved variable distributions — if the VLB issue can be resolved, this latent-factor linking strategy could be a principled approach. The empirical ablation showing that diffusion-generated features outperform random noise is a real finding, but without causal diagnostics it cannot distinguish between learning a true confounder and learning a helpful (but non-causal) latent representation.

## Suggestions

1. **Fix the variational bound.** Restructure the objective so that both forward and reverse processes operate on the same variable chain. One approach: define a joint VLB over both observed and unobserved variables, or explicitly treat the current objective as a heuristic regularizer rather than a proper bound.
2. **Describe the synthetic data generative process** for Sim-\(z\) and Sim-\(\eta\) — specify the causal graph, how \(Z\) is generated, and how it relates to \(X\), \(A\), and \(Y\).
3. **Add causal diagnostics:** Show that the generated \(Z\) is correlated with both treatment and outcome after controlling for \(X\), or design an intervention-based test.
4. **Calibrate the claims** in the abstract and conclusion to match the actual results (competitive and often best, not uniformly superior).
