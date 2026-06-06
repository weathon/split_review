## Summary

This paper proposes **CV-imputation**, a K-fold cross-validation procedure for tuning-parameter selection and model comparison under graphon models. The key innovation is replacing held-out edges in each fold with Bernoulli(θ)-distributed imputed values rather than performing matrix completion (as in ECV). Lemma 1 establishes that the imputed training data remains independent of the held-out edges given **P**, and an affine relationship (Eq. 5) enables unbiased recovery of edge probabilities via Eq. 6. Theorem 1 proves that the CV-imputation score $V_K(M)$ is asymptotically parallel to the true loss $L(M)$ up to a model-independent constant, supporting both parameter selection and method selection. The method avoids costly per-fold SVD, yielding large computational savings demonstrated on networks up to 2,617 nodes.

---

## Strengths

- **Principled imputation mechanism grounded in Lemma 1**: The affine relationship in Eq. (5), $\mathbf{P}^{[-k]} = w_k\theta\mathbf{1}\mathbf{1}^T + (1-w_k)\mathbf{P}$, is derived cleanly from the Bernoulli edge model, and Lemma 1 formally establishes the independence between the imputed training set and the held-out validation edges. This is the linchpin of the method and is mathematically sound.

- **Rigorous asymptotic result (Theorem 1)**: The convergence rate $O_p(1/n \vee 1/K^{(1+\alpha)/2} \vee 1/K^\alpha)$ is explicitly characterized, and the model-independence of $\Lambda = \frac{2}{n(n-1)}\sum_{i<j}p_{ij}(1-p_{ij})$ correctly motivates why minimizing $V_K(M)$ asymptotically aligns with minimizing $L(M)$.

- **Strong and broad empirical validation in Table 1**: Across all four graphon types and four estimators (NS, SAS, USVT, ICE), CV-imputation yields lower MSE than ECV in 15/16 conditions and dramatic improvements over ECV in several cases (e.g., Graphon 1 NS: CV-imputation 0.51±0.07 vs. ECV 9.15±19.25).

- **Demonstrated computational efficiency at scale (Table 2)**: On the Yeast network (2,617 nodes), CV-imputation runs in 240.90±16.22 seconds versus ECV's 6,021.12±18.72 seconds — a 25× speedup. The complexity argument in Section 3 ($O(n^2)$ per-fold overhead vs. $O(T_{\text{mc}}(n))$ for matrix completion) correctly identifies the source of this advantage.

- **Model-agnostic method selection at 100% accuracy**: Figure 5 shows CV-imputation achieves 100% accuracy in selecting the best estimation method among NS, SAS, USVT, and ICE at $n=200$, across all four graphon designs.

- **Practical relevance confirmed by external validation**: In the COVID-19 drug-disease case study, the method identifies ledipasvir as the third most probable new COVID-19 link, a finding later supported by Pirzada et al. (2021) and a phase-3 trial — providing genuine external grounding for the application.

---

## Weaknesses

### Fatal
None.

### Major

- **Theorem 1 requires K → ∞ but the method is always used with fixed K**: The theorem's statement explicitly requires both $n \to \infty$ and $K \to \infty$. In all empirical evaluations the paper implicitly uses a fixed K (the number of folds is never varied nor reported in the main text). With fixed K, the bias terms involving $1/K^{(1+\alpha)/2}$ and $1/K^\alpha$ do not vanish, so the consistency guarantee does not apply. The paper does not provide a finite-K bound, does not run a K-sensitivity analysis, and does not state what value of K is used in the simulations. This leaves a gap between the theoretical claim and the practical setting the theory is meant to justify. The empirical results in Figure 4 show convergence by $n=200$, but this empirical convergence is not connected back to the theoretical conditions.

### Minor

- **Score consistency is proved; model selection consistency is only informally asserted**: Theorem 1 establishes that $V_K(M) \approx L(M) + \Lambda$ uniformly. The paper then writes: "the probability that the minimizer of $V_K(M)$ approximately minimizes $L(M)$ is high within a neighborhood of $M_0$." This conclusion requires an additional separation condition — that $L(M_\phi) - L(M)$ for suboptimal $M$ is large relative to the approximation error in (8) — which is neither stated as an assumption nor proved as a corollary. The claim is plausible and empirically supported by Figure 4, but the theoretical section conveys more formal rigor than is actually established.

- **Conclusion overstates "lack of tuning requirements"**: Section 7 states "its user-friendly implementation and lack of tuning requirements." However, $\theta$ is a genuine tuning parameter (Eq. 4), whose selection is deferred entirely to the appendix. Whether the method is insensitive to $\theta$ within a practical range is not shown in the main text. Additionally, K itself is a design choice. This claim should be softened to reflect the actual setup.

- **Table 1, Graphon 3 NS: default beats CV-imputation, but the paper claims otherwise**: Default NS ($M=1$) achieves MSE $0.74 \pm 0.04$ on Graphon 3, lower than CV-imputation NS at $0.79 \pm 0.07$. Both entries are bolded as if tied, but the text (Section 5) claims CV-imputation "consistently" selects models with smaller MSE than the default. This cell contradicts that claim. Graphon 3 is piecewise constant, making the default neighborhood size well-suited; this is an honest and interesting result that deserves explicit acknowledgment.

- **Simulation scale limited to n ≤ 200 for MSE comparisons**: Figure 4 shows convergence approaching by $n=200$, but the asymptotic theory applies as $n \to \infty$. Real data at n > 1,000 (Section 6.2) lacks ground-truth MSE and uses AUC on a random 10% holdout, so the MSE consistency evidence is available only at small $n$. At least one MSE comparison at $n=500$ or $n=1000$ on simulated data would close this gap, and is computationally feasible given the method's efficiency advantage.

### Trivial

- None beyond presentation choices already noted above.

---

## Nice-to-Haves

- **θ sensitivity analysis in the main text**: Even a single figure or two paragraphs showing MSE stability over $\theta \in \{0.1, 0.3, 0.5, \bar{p}\}$ across the four graphons would concretely demonstrate that the method does not merely transfer the tuning problem from $M$ to $\theta$.

- **Oracle row in Table 1**: Adding an "oracle" row showing the MSE when $M$ is chosen using the true $L(M)$ (with known **P**) would clarify how much residual gap remains between CV-imputation's selections and the theoretical optimum.

- **Formal model-selection consistency theorem**: Stating explicitly what separation condition on $\{L(M)\}_{M \in \mathcal{M}}$ suffices to prove $P(\arg\min_M V_K(M) = \arg\min_M L(M)) \to 1$ would convert the current informal claim into a publishable-quality corollary.

- **K-sensitivity experiment**: A brief comparison of CV-imputation performance for K ∈ {2, 5, 10} would connect the theoretical K → ∞ assumption to practical guidance and reveal how gracefully the method degrades at small K.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Figure 3 caption appears to say "ECV is faster than CV-imputation"** (Harsh Critic): The parsed alt text for Figure 3 reads "In all cases, ECV is faster than CV-imputation," which is the reverse of the paper's claim. However, this is a PDF-to-text parser artifact — the actual figure caption (line 189) merely describes axis layout without directional claims. Section 6.1 explicitly reports "a computational cost of 56.76 seconds, which is more efficient than the 71.82 seconds required for ECV," Table 2 shows 4–25× speedups, and Figure 5's caption (which describes a related plot) correctly reports CV-imputation's speed advantage. The contradiction exists only in the parser-generated image alt text, not in the authored paper. Removed per hard rule on formatting/parser artifacts.

- **COVID-19 temporal split violates graphon exchangeability** (Harsh Critic): The critic argues that a temporal train/test split introduces distributional shift incompatible with graphon models. While technically valid as a model-assumption concern, this is a standard practice in applied link-prediction evaluations and the paper presents it as an empirical application, not a formal graphon-theoretical guarantee. The point is scope-creep for a methods paper and is removed accordingly.

- **Missing related works** (not raised but precluded by hard rule): No missing related works were flagged; removed preemptively per hard rule.

- **Reproducibility concerns about θ hyperparameter in appendix** (Harsh Critic): The critic notes that θ selection is deferred to Section S.4. This is flagged as a "meaningful omission," but detailed hyperparameter guidance is routinely placed in appendices. The concern is retained as a minor weakness in the main review (the "no tuning requirements" claim) but the broader reproducibility framing is removed.

---

## Novel Insights

The core insight that replacing removed edges with Bernoulli-imputed values — rather than leaving them missing or performing matrix completion — preserves the marginal distribution of the training matrix up to a known affine transformation (Eq. 5) is elegant and practically powerful. It converts a fundamentally non-standard data-splitting problem (network edges are not i.i.d. observations) into one where standard bias-correction techniques apply, yielding a clean algebraic correction (Eq. 6) that avoids the low-rank assumption required by matrix completion. This idea generalizes naturally: any model where missing values can be replaced by random draws from a known parametric family that induces an affine shift in the mean could potentially benefit from the same decomposition.

---

## Suggestions

1. **Report the value of K used in all experiments**, and add a K-sensitivity ablation (K ∈ {2, 5, 10}) to connect the K → ∞ theory to practical usage.
2. **Add a formal model selection consistency statement** as a corollary to Theorem 1 under a minimal separation assumption on candidate model losses.
3. **Soften the "no tuning requirements" claim** in Section 7 to accurately reflect that θ is fixed (and discussed in the appendix), and that the appendix provides guidance for its selection.
4. **Acknowledge and discuss the Graphon 3 NS case** in the text: default outperforms CV-imputation there, which is informative about when neighborhood-size tuning adds less value (piecewise-constant graphons with natural block structure).
5. **Add at least one MSE simulation at n = 500** to demonstrate the asymptotic scaling behavior at a network size that bridges the simulated (n ≤ 200) and real-data (n > 1,000) settings.

---

## Final Assessment

**Originality**: High — the imputation-based approach is a genuinely new idea for graphon CV that cleanly sidesteps the low-rank requirement of matrix completion.

**Importance**: High — model/parameter selection for graphon estimators is a practical bottleneck, and the computational savings (4–25×) are meaningful for real applications.

**Claims supported**: Mostly — core empirical claims are well-supported; the theoretical claim about model selection consistency is informally overstated relative to what Theorem 1 actually proves.

**Soundness of experiments**: Good — four graphons, four estimators, 100 replications, and four real networks. The main limitation is the small simulation scale (n ≤ 200).

**Clarity**: Good — the method and motivation are clearly written; minor issues with the conclusions section.

**Value to community**: High — a practically useful, easy-to-implement method with documented open data and code, applicable across diverse graphon estimators.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>