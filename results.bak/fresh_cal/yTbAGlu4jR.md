Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes DIRE (Disentangled Identifiable vaRiational autoEncoder), a variational autoencoder that learns identifiable balanced prognostic scores (bPGS) for treatment effect estimation under limited overlap. The key idea is to disentangle covariates into adjustment (Z₁), confounder (Z₂), and instrument (Z₃) latent factors with identifiability guarantees, then use the concatenation of Z₁ and Z₂ as a balanced prognostic score that relaxes overlap requirements. The paper provides theoretical results (Theorem 1) showing that under injectivity assumptions, the latent factors can be recovered up to injective transformations, and that the bPGS enables generalization beyond overlapped regions and even to zero-overlap out-of-distribution treatments. Empirically, DIRE achieves SOTA on the IHDP benchmark, shows robustness on synthetic limited-overlap data, and outperforms SIN on a structured treatment zero-shot task.

---

## Strengths

1. **Identifiability theory for limited overlap (Theorem 1)**: The paper provides a formal identifiability result showing that under Assumptions 4.1–4.4 and injectivity of mixing functions, the latent adjustment, confounder, and instrument variables can be recovered up to injective transformations. Part 2 of the theorem specifically shows how the overlapping condition can be relaxed onto a subset of covariates via the bPGS — this is the paper's core theoretical contribution and directly supports the claimed ability to generalize beyond overlapped regions (Section 4.2, lines 130–138).

2. **State-of-the-art performance on IHDP**: DIRE achieves the lowest PEHE and ε_ATE in both in-sample and out-sample settings, outperforming all 11 baselines including β-Intact-VAE, DR-CFR, and CEVAE (Table 1, Section 5.2). This provides direct empirical evidence on a standard benchmark.

3. **Robustness across varying limited-overlap levels on synthetic data**: In the synthetic dataset with non-overlapping levels ω ∈ {10,15}, DIRE maintains stable CATE estimation error while β-Intact-VAE and DR-CFR degrade sharply (Figure 2, Section 5.3). This demonstrates that the method specifically addresses limited overlap better than prior disentanglement and prognostic-score approaches.

4. **Zero-shot generalization to OOD treatments with zero overlap**: On the structured treatment dataset with scaffold split, DIRE substantially outperforms SIN on PEHE@10 (Table 2, Section 5.4). This is the paper's most distinctive result — directly demonstrating that the learned identifiable bPGS can generalize to treatments never seen during training, a claim no compared baseline achieves.

5. **Universality of the product-effect formulation (Proposition 1)**: The paper formally shows that any prognostic score in a suitable RKHS can be approximated arbitrarily well by a product of functions g_i(X)^\top h_i(T), providing theoretical grounding for the factorized structure used to derive bPGS (Section 4.2).

---

## Weaknesses

### Fatal

None.

### Major

- **Synthetic results lack error bars or confidence intervals (Section 5.3, Figure 2)**: The paper's key evidence for robustness under limited overlap is presented as a line plot with no confidence intervals, error bands, or any measure of variability. Although the paper mentions hyperparameter search over 30 runs, it does not report variability across random seeds or data instantiations for the same configuration. Without this information, the reader cannot assess whether DIRE's apparent advantage over baselines is statistically significant or whether the reported trends are stable. This undermines the paper's central claim that DIRE "exhibits robustness across all limited overlapping levels."

- **Model architecture is critically underspecified (Section 4.3)**: The description of DIRE is too vague to allow faithful reproduction or verification. (1) The variable Z₄ is introduced in the generative model (line 150) and inference model (line 164) without being defined or justified — it appears to be an intermediate encoding Z₄ = g(Z₁,Z₂,Z₃), but this relationship is never stated explicitly. (2) The paper invokes an "ELBO decomposition trick (Chen et al., 2018)" but the sentence describing it (line 167) is incomplete and the actual ELBO is never written. (3) The inference model's factorization `q_ϕ(z₂|z₄)` and `q_ϕ(z₃|z₄,y)` is stated without explaining why this particular structure was chosen or how it enforces the desired latent disentanglement. For a method whose core contribution is a specific architectural design for identifiable disentanglement, this level of ambiguity is a serious barrier to reproducibility.

### Minor

- **Theorem 1 is presented without accessible interpretation (Section 4.2, lines 132–137)**: The theorem statement is dense with numerous conditions (K₁–K₇ mappings, injective Δ_T, RKHS assumptions on bPGS space, multiple "if either 1) or 2)" clauses) and contains unclear notation (e.g., $\bar{k}_4^{*-1}$, "injective mappint" [sic]). The paper states the theorem and then gives only a one-sentence summary (lines 138–139) that does not connect the technical conditions to the practical claim about overlap relaxation. A plain-language breakdown of what each condition means and why it is needed would substantially improve accessibility.

- **IHDP standard deviations are unusually small without explanation**: DIRE's reported standard deviations (claimed ~0.02–0.04) are far smaller than baselines like BART (0.31) or DR-CFR (0.09). While the paper states it "follow[s] the same setting as" prior work, this variance discrepancy warrants explicit discussion — e.g., explaining whether DIRE's lower variance arises from the inherent stability of the method or from differences in train/validation/test splits, outcome simulation noise, or evaluation protocol. A brief clarification would preempt doubts about protocol differences.

- **No ablation studies**: The paper does not ablate key components: removing the identifiability constraint (e.g., standard VAE with same factorization), ablating the supervision signals (T and Y) from the inference network, or removing the disentanglement structure. Without these, it is difficult to attribute the performance improvements specifically to the identifiable bPGS rather than to other architectural choices (e.g., the VAE structure itself, the specific factorization, or the auxiliary supervision).

- **Injectivity assumptions not discussed**: Assumption 4.1 requires all mixing functions K₁–K₇ to be injective, and Theorem 1 further requires injectivity of both ground-truth and learned K_i. The paper does not discuss when this assumption is reasonable in practice or what happens when it is violated. Given that real-world covariates may not decompose injectively, some discussion of limitations would strengthen the paper.

### Trivial

- **ω (non-overlapping level) is not formally defined**: Section 5.3 states ω is used with "five nonoverlapping levels" where "a higher value of ω indicates a more severe non-overlapping scenario," but the paper never specifies how ω is computed or what values it takes. This makes the synthetic experiment difficult to interpret or reproduce.

- **Section 4.1 uses tilde notation (ground-truth vs. learned) that is clear in concept but never specifies the dimensionality of the latent spaces** (Z₁, Z₂, Z₃).

---

## Nice-to-Haves

- **Additional baselines for the structured treatment setting**: The structured treatment experiment (Section 5.4) compares only against SIN. While the paper notes that β-Intact-VAE cannot handle the setting, including other multi-treatment methods (e.g., Deconfounder) would strengthen the comparison.

- **Simplified theoretical summary**: Rather than the dense Theorem 1, the paper could state a simplified practical version (e.g., "if the VAE recovers the true marginal distribution of X, then the latent factors are identified up to injective transformation") and then explain — in plain language — how this enables overlap relaxation. This would make the paper accessible to a broader causal inference audience.

- **A figure of the full inference model** (encoder network) to complement Figure 1(b), showing how X, T, and Y feed into the latent factors Z₁–Z₄.

---

## Removed Points

These points from the reviews were flagged for removal, with justification:

- **"Z₄ reverses the causal direction of the DGP"** — The inference model q_ϕ(z₂|z₄)q_ϕ(z₃|z₄,y) factorizing in the opposite direction of the generative model is standard VAE design: the inference network approximates the posterior by reversing the generative arrows. This is not a flaw. Z₄ is a standard intermediate encoding (Z₄ = g(Z₁,Z₂,Z₃)). The concern is addressed under "Major" above as an underspecification issue (the paper should define Z₄ explicitly), not as an inconsistency.

- **"SIN performs worse than zero suggests a metric bug or negative PEHE"** — "Performs worse than zero" is commonly used to mean "worse than a zero-predictor baseline," not that the metric value is negative. PEHE is always non-negative (squared error). This is a misreading of the paper's phrasing at line 230.

- **Missing hyperparameters, optimizer details, layer counts** — These are trivial implementation details that would typically be in the appendix (stripped by the parser), not a fundamental flaw. The paper states it uses hyperparameter search via Li et al. (2020).

- **Typo "simulataneously" in abstract** — This is a PDF extraction artifact, not an author error.

- **Missing appendix proofs for Theorem 1** — The parser strips appendix content from all papers; proofs exist in the original submission. The related concern about the theorem being opaque in the main text is retained as a Minor weakness.

---

## Novel Insights

The harsh critic's observation that the model architecture section (4.3) is vague — particularly the unexplained Z₄ and the missing ELBO — is valid, but it is important to note that this is a *presentation gap* rather than a *structural flaw*. The inference model factorizing as q(z₄|x)q(z₁|x,t)q(z₂|z₄)q(z₃|z₄,y) is a standard amortized VAE design where Z₄ serves as a shared encoding of X that is then decomposed into the three disentangled latents. The generative model p(z₄|z₁,z₂,z₃)p(x|z₄) mirrors this. The paper's core difficulty is that it tries to compress a technically involved method (identifiable VAE with auxiliary supervision and product-effect factorization) into a very short section, leaving many architectural choices unjustified. A strength not fully articulated in either review is the paper's connection between the balanced prognostic score (bPGS) and the structured treatment setting: the bPGS depends only on X (via Z₁ ⊕ Z₂), not on T, which is what enables zero-shot generalization to unseen treatments. This is an elegant insight that could be foregrounded more prominently.

---

## Suggestions

1. **Provide the full ELBO and explicitly define Z₄**. Show how Z₄ = g(Z₁,Z₂,Z₃) bridges the DGP (Assumption 4.1) and the VAE structure. Justify the factorization choices in the inference model.

2. **Add confidence intervals, error bands, or IQR shading to Figure 2** (synthetic results). Report the variability across runs explicitly, and ideally include a statistical significance test or effect size.

3. **Add an ablation study**: compare DIRE against (a) a variant without the identifiability constraint, (b) a variant without auxiliary T/Y supervision, and (c) a variant with a single entangled latent instead of three disentangled ones. This would isolate the contribution of the identifiable bPGS.

4. **Provide a plain-language summary of Theorem 1** immediately after the formal statement. Walk through (i) what each condition means, (ii) how identifiability is established, and (iii) how the overlap relaxation follows from the bPGS structure.

5. **Define ω formally** in the synthetic experiment: how is the non-overlapping level quantified and how does it map to the five levels tested?

6. **Clarify the IHDP variance**: state explicitly whether the evaluation protocol (outcome simulation noise, split procedure) is identical to prior work, and briefly discuss why DIRE's standard deviation is notably smaller.

---

## Score and Decision

**Originality**: Good — combining identifiable VAE with balanced prognostic scores for limited overlap is novel.  
**Importance of research question**: High — limited overlap is a real and underexplored challenge in causal inference.  
**Claims support**: Moderate — the theoretical claims are backed but opaque; the empirical claims are directionally supported but lack statistical rigor on the key synthetic results.  
**Soundness of experiments**: Moderate — IHDP results are strong, structured treatment results are promising, but synthetic results lack error bars and no ablations are performed.  
**Clarity of writing**: Below average for the method section — Section 4.3 is too vague to reproduce. The rest is readable.  
**Value to community**: Moderate — the idea of learning identifiable bPGS for OOD generalization is valuable and likely to inspire follow-up work, but the paper needs significant clarification first.

The paper makes genuine contributions (identifiable disentanglement for limited overlap, zero-shot OOD generalization), and the empirical results are directionally positive. However, the model architecture is critically underspecified, the key synthetic experiment lacks error bars, and no ablation studies are performed — these are significant weaknesses for a methods paper at a top venue.

**MY FINAL SCORE: <score>5.0</score>**  
**MY FINAL DECISION: <decision>Reject</decision>**