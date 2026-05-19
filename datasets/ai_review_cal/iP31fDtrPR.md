- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 6, 3
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper introduces OTP-DAG, a framework that reformulates parameter learning in directed graphical models as an optimal transport problem. Theorem 1 establishes that minimizing the Wasserstein distance between data and model distributions is equivalent to minimizing a reconstruction error with local backward maps that satisfy push-forward constraints. The practical objective relaxes these constraints via a penalty term, yielding a tractable objective solvable by stochastic gradient descent. The method is demonstrated on three diverse applications — Latent Dirichlet Allocation, Hidden Markov Models, and discrete representation learning — showing parameter recovery and competitive downstream performance.

## Strengths

1. **Novel theoretical connection between optimal transport and parameter learning.** Theorem 1 (Section 3) derives an equivalence between the Wasserstein distance \(W_c(P_d, P_\theta)\) and the infimum over backward maps with exact push-forward constraints of the expected reconstruction cost. This provides a genuinely new perspective on a classic problem (parameter estimation in DGMs with latent variables) and grounds the framework in a principled mathematical foundation.

2. **Demonstrated versatility across structurally different graphical models.** The paper applies OTP-DAG to three distinct settings — topic modeling (LDA), sequential modeling (HMM), and deep generative modeling (discrete RepL) — each with different variable types and dependency structures. Tables 1–3 report results across synthetic and real datasets, showing the method can recover ground-truth parameters and produce competitive downstream performance.

3. **Local backward map strategy reduces global inference complexity.** Rather than approximating the full posterior over all hidden variables (as in variational inference), OTP-DAG defines local backward maps from observed nodes to their parents. This localization, discussed in Section 5, avoids the sub-optimality issues of global variational approximations in complex graphs and is a principled practical advantage.

## Weaknesses

### Fatal
None.

### Major

1. **The gap between the theoretical equivalence and the practical objective is unanalyzed.** Theorem 1 establishes that with *exact* push-forward constraints \(\phi_i\#P_d(X_i)=P_\theta(\mathrm{PA}_{X_i},U_i)\), the Wasserstein distance equals the reconstruction error. The paper then relaxes these constraints by adding the penalty \(\eta D(P_\phi, P_\theta)\) to obtain \(J_{\mathrm{WS}}\) (Eq. 2), but provides **no analysis** of how large the gap between \(J_{\mathrm{WS}}\) and the true Wasserstein distance is, under what conditions it becomes small, or what choice of divergence \(D\) best approximates the original constraint. This leaves a critical link unsupported: the practical algorithm may diverge arbitrarily from the OT framing that motivates it. The paper does not even specify which divergence \(D\) was used in experiments (line 89 only says "any arbitrary divergence measure"). While this does not invalidate the method as a practical algorithm, it significantly weakens the claimed theoretical contribution. The paper would be substantially strengthened by a bound, an empirical study on synthetic data where the Wasserstein distance can be estimated exactly, or at minimum an ablation comparing \(\eta=0\) to \(\eta>0\).

2. **Missing key baselines in the experimental evaluation, undermining claims of competitive performance.**
   - **HMM (Sec. 4.2):** The only baseline is MAP estimation. The standard algorithm for this setting — Baum–Welch (EM for HMMs) — is not compared against. The paper states OTP-DAG "approaches the ground-truth values comparably to MAP" (line 151), but MAP is a single-point estimate and a relatively weak baseline. Without comparison to the established method for this problem class, the HMM experiment cannot support broader claims about OTP-DAG's effectiveness on sequential data.
   - **LDA (Sec. 4.1):** The baselines (EM, SVI, ProdLDA) do not include more recent neural or embedded topic models that also avoid exact posterior inference, which would be the most natural comparators for a method claiming to generalize beyond classical approaches.
   - **Discrete RepL (Sec. 4.3):** The paper attributes OTP-DAG's better reconstruction to "avoiding codebook collapse" and claims the framework "ensuring all codewords are utilized" (line 177), but provides **no direct evidence** — no codebook perplexity, entropy, or fraction of codewords used. Without such measurements, the mechanism behind the improved reconstruction is speculation, and the connection to the OT formulation is unsubstantiated.

3. **No statistical significance or variability reporting.** The paper states results are averaged over 5 random seeds (line 102), but standard deviations, confidence intervals, or any measure of variability are absent from the reported tables in the main text. For a method with multiple hyperparameters (\(\eta\), choice of \(D\), network architectures), this makes it impossible to assess the reliability or stability of the reported improvements.

### Minor

1. **Gradient flow through the quantization step in discrete RepL is not addressed.** The generative process (line 175) includes \(c = \operatorname{argmin}_c d_z(Z; \mu_c)\), which is non-differentiable. The paper does not discuss how gradients are propagated through this operation (e.g., straight-through estimator, Gumbel-softmax). This is a standard issue in VQ-VAE-based models and should be explicitly addressed.

2. **Omission of backward maps for exogenous variables is unvalidated.** The paper states (lines 100–101) that the empirical implementation omits learning backward maps for exogenous variables and "sampling the noise from an appropriate prior distribution suffices to yield accurate estimation." This is a significant departure from the theoretical development where exogenous variables are integral to the push-forward constraint, yet no ablation study is provided to verify that this simplification does not degrade performance or break the theoretical connection.

3. **Choice of divergence \(D\) not identified.** While the paper states \(D\) is "any arbitrary divergence measure" (line 89), the specific divergence used in experiments is not reported. This is a basic experimental detail needed for reproducibility.

### Trivial
None.

## Nice-to-Haves

- A controlled synthetic experiment with known ground-truth parameters and intractable posterior (e.g., a non-conjugate chain) would directly validate the method's claimed advantage over EM and VI.
- An ablation comparing \(\eta=0\) (pure reconstruction) against \(\eta>0\) would isolate the effect of the OT-derived penalty.
- Reporting codebook perplexity or effective codeword count in the discrete RepL experiment would substantiate the codebook collapse claim.
- Including a runtime comparison against baselines would help assess practical utility.

## Removed Points

These points were raised but are removed for the reasons listed:

- **"The method is critically underspecified (what divergence \(D\), how \(\phi_i\) parameterized, what cost function \(c_i\))"** — Removed. The paper's supplementary materials (referenced as "we detail the formulation" at line 177 and Table 7) likely contain these details; the parser strips appendix content from all papers.
- **"The paper does not sketch the proof or intuition for Theorem 1"** — Removed. The paper provides intuition via the example in Figure 2c and lines 71–72; a full proof would be in the appendix.
- **"The framing of existing methods as extremes on a continuum is oversimplified"** — Removed. This is a scope-creep criticism about exposition style, not a substantive weakness.
- **"The empirical omission of backward maps for exogenous variables contradicts the theoretical development"** — Removed. The paper explicitly addresses this discrepancy (lines 100–101) and explains the rationale.
- **"The proposed solution of Generalized Reparameterization Gradient is mentioned without evidence"** — Removed. This is a future work suggestion in the conclusion, not a claimed contribution.
- **"Missing related works"** — Removed per policy (no external sources to confirm such omissions).
- **"Standard deviations absent" / "missing statistical significance"** — This is retained as a Major weakness (actually present), not removed.

## Novel Insights

An interesting observation emerges from synthesizing the reviews: the paper's core tension is between framing it as a *theoretical contribution* (a new paradigm for parameter learning via OT) versus a *practical algorithm* (a reconstruction-based training method for DGMs). Theorem 1 is a genuine theoretical result, but the relaxation to \(J_{\mathrm{WS}}\) is presented as a straightforward penalty without analysis — the very step that transitions from theory to algorithm is where the paper's rigor drops off. This gap creates a mismatch between the ambitious abstract claims and what the evaluation can actually support. The local backward map strategy, however, is a genuinely useful insight that could stand independently: rather than approximating a global posterior, learn local conditional maps from observed nodes to their parents in the graph, which is simpler and more modular than standard VI. This idea is the paper's most practically valuable contribution but is somewhat buried under the OT framing.

## Suggestions

1. **Analyze the relaxation gap.** Either bound \( |J_{\mathrm{WS}} - W_c| \) analytically, or run a controlled experiment on a small synthetic model where the true Wasserstein distance can be estimated (e.g., via sampling) and measure how far the minimizer of \(J_{\mathrm{WS}}\) is from the true Wasserstein minimizer.
2. **Add Baum–Welch as a baseline for the HMM experiment.** This is the standard method and is necessary to support any claim about OTP-DAG's effectiveness on sequential data.
3. **Report codebook usage statistics** (perplexity, fraction of codewords used) for the discrete RepL experiment to substantiate the codebook collapse mitigation claim.
4. **Report standard deviations** for all main results (Tables 1–3) and specify which divergence \(D\) and cost functions \(c_i\) were used in each experiment.
5. **Address the gradient flow through the quantization step** explicitly — even a brief statement that the straight-through estimator is used would suffice.
6. **Add an ablation with \(\eta=0\)** to show the contribution of the penalty term to performance.
