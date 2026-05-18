Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper provides theoretical conditions under which square-based losses (MMSE) and, under the fixed-variance Gaussian assumption, log-likelihood based losses (BIC, ELBO) are minimized for incorrect DAGs when variables are measured on different scales. The key theoretical contributions are Propositions 2–6, which give precise variance-ordering conditions under which MMSE prefers a reversed chain, wrong fork, wrong collider, or different member of a Markov equivalence class in d-dimensional linear settings. Extensive experiments on synthetic data (NT, DAG-GNN, GraN-DAG, GES) and real-world data (Sachs et al., 2005) consistently confirm that scaling one or more variables changes the predicted graph, with mitigation demonstrated via a Scale-Robust Loss (SRL) for discrete learners.

## Strengths

- **Exact conditions for MMSE failure in d-dimensional linear DAGs**: Propositions 2–6 provide explicit inequality conditions (e.g., strictly decreasing variances along a chain in Proposition 2, the stronger mixed-variance condition in Proposition 3) under which MMSE is minimized by a wrong DAG. These are precise, testable predictions that go well beyond prior 2-node results. The experimental confirmation in Table 1 and Figures 2–3 is clean and reproducible (100% hit rate for NT/DG/GND in the controlled settings).

- **Scale induces wrong d-separation statements, not just edge reversals**: Proposition 6 shows that under appropriate variance conditions, MMSE is minimized by a DAG containing a collider with an additional edge that changes the conditional independence structure — moving beyond within-MEC flips to genuinely different independence statements. This is theoretically important and empirically verified (Figures 2(b), 3).

- **Extensive empirical validation across algorithms and settings**: Experiments cover 4 structure learners (NT, DAG-GNN, GraN-DAG, GES), linear and non-linear (cosine) dependencies, d ∈ {3, 10}, subset-of-variables scaling, ablation of the immiscible-structures assumption on random DAGs, and real-world data from Sachs et al. (2005). The consistency of results across these settings strongly supports the practical relevance of the core theoretical claims.

- **Connects to MECs and provides a practical mitigation**: Proposition 5 bridges the results to Markov equivalence classes (explaining why GES, which searches over MECs, is also affected), and the proposed SRL shows a concrete path to robustness for discrete learners.

## Weaknesses

### Major

- **Insufficient qualification of assumptions in Propositions 7–10 regarding variance estimation**: The paper claims that log-likelihood "reduces to" MMSE (Proposition 7) and that BIC/ELBO "can be written in terms of MMSE" (Propositions 9–10). This is correct *only* when the noise variance is treated as known and fixed (e.g., unit variance). The standard Gaussian log-likelihood is:
  \[
  \log p(\mathbf{X}_j \mid \mathbf{Pa}_{X_j}) = -\frac{n}{2}\log(2\pi\sigma_j^2) - \frac{1}{2\sigma_j^2}\sum_i (X_{i,j} - f_{j,\theta}(\mathbf{X}_{P_j}))^2.
  \]
  When variance is estimated (as in standard uses of BIC) or when the Gaussian variance is a learned parameter, scaling a variable by \(c\) introduces a \(-n\log(c)\) term from the log-determinant that does not simply collapse to a scaled MSE. The paper does state "fixed variance Gaussian noise assumption" in the SRL discussion (Section 3.3), but this qualification is absent from Propositions 7–10 themselves. Since the BIC/ELBO generalization is advertised as a key contribution, the failure to state this limitation in the theoretical results is a significant omission. The empirical evidence (using NT/DG/GND, which effectively use fixed-variance losses) remains valid, but the theoretical claim is narrower than presented. *Fixable by restricting the scope of Propositions 7–10 or by providing a proper treatment of variance estimation.*

### Minor

- **Definition 2 and Proposition 8 are technically vacuous**: The "family of log-likelihood losses" is defined as \(\sum \log p(\mathbf{x}_i|\theta) + h(\cdot)\) where \(h(\cdot)\) is an *arbitrary* function. With unrestricted \(h(\cdot)\), one could construct members of this family that are *not* susceptible to scaling (e.g., \(h\) that exactly cancels the scale dependence). Proposition 8 therefore makes no substantive claim. The paper would be cleaner by removing Definition 2 and Proposition 8 entirely, and directly proving Propositions 9 and 10 under the relevant assumptions.

- **Non-linear theoretical extension is weaker than stated**: The abstract and introduction suggest a theoretical extension to non-linear cases ("we also show that scale can impair performance of structure learners if relations among variables are non‑linear"). What is actually proven (Proposition 7) is the standard equivalence of Gaussian log-likelihood and sum-of-squared-errors, which holds regardless of linearity. The *conditions* under which the wrong DAG minimizes the loss in non-linear settings are not derived — the paper honestly notes this ("we leave the derivation of such conditions for future work") and relies on experiments. The phrasing in the abstract should be calibrated to match: the non-linear contribution is *empirical*, not theoretical.

- **Proof sketches for Propositions 2–6 are too terse**: The sketches describe the intuition but do not state the key algebraic inequality that drives the result (e.g., the exact expression for the MMSE difference between chain and reversed chain). While full proofs are deferred to the appendix (standard practice), the sketches are so brief that a reader cannot assess plausibility without consulting the appendix.

- **Assumption (A1) "immiscible structures" decomposition is informal**: Remark 1 claims that "each DAG can be decomposed into subgraphs fulfilling (A1)," but this decomposition is not formalized, and the interaction between substructures in the overall loss is not analyzed theoretically. The experiments on random DAGs (Q3) address this empirically, but the theoretical results are limited to the simple structures.

- **Scaling factors in experiments not systematically varied in the main text**: The paper reports "3 different scales" and uses examples like "factor of 12" and "factor of 4," but the main text does not report the full range or a sensitivity analysis. The appendix presumably contains details, but for a reader assessing practical severity, knowing whether failures require extreme scaling (1000×) or occur at mild scaling (2×) is important.

### Trivial

- The paper states "the variance of each variable in X only depends on the unit of measurement." This conflates measurement-unit scaling (multiplying by a constant) with variance differences arising from other sources. The theory actually applies to any variance difference, regardless of source — this should be clarified to avoid confusion.

- The medical example (Figure 1) is a useful motivation, but the probabilities (0.49 vs 0.51) are stated without any noise-parameter or edge-weight specification. Adding even a rough parameterization would strengthen the example.

## Nice-to-Haves

- Clarify the relationship to identifiable DAG models: In linear Gaussian DAGs, the structure is identifiable only up to Markov equivalence without additional assumptions (e.g., equal error variances). The scale-induced preference for one MEC member over another is related to this known non-identifiability. The paper cites relevant work (Peters & Bühlmann 2014, Park 2020) but could usefully discuss the connection.

- Separate the discussion of within-MEC flips (Proposition 5, chain/fork reversal) from across-MEC flips (Proposition 6, collider with extra edge). The former is less alarming (practitioners who know the MEC can treat all members as equivalent) while the latter genuinely changes independence statements.

- A small loss-landscape visualization for a simple chain under scaling (showing how variance terms drive the MMSE difference) would strengthen the explanatory direction of Section 3.3.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Medical example disconnected from theory"**: The reviewer faults the medical example for being disconnected from the theoretical results. However, this is a *motivational* example — it does not need to be formally tied to the theory. Motivational examples serve to illustrate why the problem matters, not to instantiate the theoretical conditions. Removed as a mismatch of expectations.

- **"Paper does not discuss identifiable DAG models enough"**: The paper cites Peters & Bühlmann 2014 and Park 2020 in the related work section. The reviewer's complaint is about depth of discussion, not absence. This is a suggestion for improvement, not a weakness of the paper's technical content. Moved to Nice-to-Haves.

- **Various formatting/presentation nitpicks**: The reviewer's comments about the paper needing to "state the key inequality" in proof sketches or about the proof of Proposition 10 being "a single sentence" have been kept as minor weaknesses (the sketches are indeed terse). But the reviewer's stronger characterization of Proposition 10's proof as "not trivial given the complexity penalty" is partially addressed by the paper's own fixed-variance assumption (stated in Section 3.3). The core concern about variance estimation is retained in Major; the "not trivial" framing is downgraded.

## Novel Insights

The Harsh Critic's most useful observation is that the paper's theoretical bridge from MMSE to log-likelihood based losses (BIC, ELBO) depends on treating noise variance as fixed and known — a standard but unstated assumption that, when violated, changes the functional form of the loss's scale dependence. This insight sharpens the paper's contribution: the conditions for MMSE failure in linear settings (Propositions 2–6) stand on their own as the core theoretical result, while the BIC/ELBO generalization is best presented as a conditional corollary ("under fixed-variance Gaussian noise") rather than as an unconditional extension. The experiments on NT/DG/GND, which use effectively fixed-variance objectives, remain fully supportive of the core claims.

## Suggestions

1. **Revise Propositions 7–10 to explicitly state the fixed-variance Gaussian assumption** (or restrict the claim to "under the common assumption of known unit variance"). Alternatively, provide a proper derivation that includes variance estimation and show that the scale dependence persists despite the logarithmic variance terms.

2. **Remove Definition 2 and Proposition 8** — they add nothing and invite technical objection. Directly prove Propositions 9 and 10 under the relevant assumptions.

3. **Calibrate the abstract's claim about non-linear results**: state that the non-linear *theoretical* contribution is the equivalence-of-losses (Proposition 7), while the *empirical* demonstration shows scale effects persist in non-linear settings.

4. **Expand the proof sketches** in the main text to include the key expression for the MMSE difference (e.g., \(\Delta = \text{Var}(X_1) - \text{Var}(X_d) + \sum(\text{Cov}^2/\text{Var}(X_i) - \text{Cov}^2/\text{Var}(X_{i+1}))\)) so a reader can follow the argument without the appendix.

5. **Report scaling factor magnitudes** more systematically in the main text, even as a brief paragraph, so readers can gauge practical severity.

## Score and Decision

**Originality**: 7/10 — Extends known 2-node variance-sensitivity results to d-dimensional settings with exact conditions. Not ground-breaking but a solid, needed generalization.

**Importance**: 8/10 — The problem is practically urgent: practitioners routinely apply structure learners without checking whether variable scales affect results.

**Claims support**: 6/10 — The core MMSE claims are well-supported. The BIC/ELBO extension is overclaimed relative to the assumptions actually proven.

**Soundness**: 7/10 — Core theoretical results are sound; experiments are extensive and consistent. The main issue is insufficiently qualified assumptions in the propositions.

**Clarity**: 6/10 — Generally clear, but proof sketches are too terse and the "family of log-likelihood losses" definition is confusing.

**Value**: 7/10 — Valuable for both practitioners (awareness of scaling effects) and theorists (conditions for failure).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>