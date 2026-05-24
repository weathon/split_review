Now I have a thorough understanding of the paper and can verify the reviewer claims against it. Let me write the final consolidated review.

## Summary

This paper proposes a framework for distributional reinforcement learning where return distributions are represented via **mean embeddings** (sketches), and Bellman updates are performed as simple linear-algebraic operations directly in the sketch space via learned Bellman coefficient matrices \(B_r\). This avoids the expensive imputation step required by prior sketch-based approaches (SFDP). The paper provides a convergence analysis (error propagation bounds) for Sketch-DP, extensive tabular experiments studying the effect of feature parameters, and a deep RL agent (Sketch-DQN) evaluated on Atari 57.

---

## Strengths

1. **Linear sketch Bellman operator eliminates costly imputation.** The paper derives a linear update (Eqs.~4–5, Algorithm 1) that operates entirely in the sketch domain, in contrast to SFDP (Rowland et al., 2019) which requires decoding sketches to distributions at each update. Figure 1 diagrams this difference, and the paper references wall-clock speedups (Sec.~C.7). This is a concrete algorithmic improvement.

2. **Generality via regression-based Bellman coefficients.** Rather than requiring exact Bellman closedness (which Rowland et al. show is limited to moments), the paper relaxes this to an approximate linear relationship via regression (Eq.~6), enabling a much wider family of feature maps such as the translation family (Eq.~9). Remark 2 explicitly justifies why linear (not nonlinear) regression is necessary, which is a careful design choice.

3. **Novel error propagation analysis with a concrete bound for a feature class.** The paper provides a three-part error decomposition (Bellman approximation, reconstruction, embedding) in Propositions 1–3, chaining them to bound the asymptotic error. Proposition 4 gives a concrete \(O(1/m)\) bound for indicator features — a nontrivial guarantee for a novel sketch class.

4. **Systematic tabular experiments.** The sweep over number of features \(m\) and slope \(s\) (Figure 4/5 in the paper) for multiple base features provides practical guidance for tuning the translation family. The walk-through visualization (Figure 2) makes the mechanism concrete.

5. **Atari results suggest the framework scales to deep RL.** Sketch-DQN achieves higher median and mean human-normalized scores than C51 and QR-DQN and approaches IQN (Figure 5), while the paper claims it runs faster than QR-DQN and IQN (Sec.~5.2). This demonstrates feasibility of the approach at scale.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theory-practice gap for smooth features (Propositions 1–3 vs. deep RL experiments).** The one-step error bound (Proposition 1) is expressed in terms of a *supremum* over \(g\) and \(r\) of the pointwise approximation error \(\|\phi(r+\gamma g) - B_r \phi(g)\|\), but the Bellman coefficients \(B_r\) are computed via linear regression that minimizes *average* squared error under a reference distribution \(\mu\) (Eq.~6). The paper provides no argument connecting these two quantities for the smooth features (sigmoids, sinusoids) used in the translation family (Eq.~9) and in the deep RL experiments. Similarly, the reconstruction error bound \(\varepsilon_R\) and embedding error bound \(\varepsilon_E\) in Proposition 2 are stated as assumptions that are not verified for any smooth feature family. The paper is transparent that the analysis is "abstract" (line 431) and calls out "convergence analysis for general sketches" as future work (line 548), but this leaves a significant gap: the convergence guarantees in Section 4 do not directly apply to the algorithms evaluated in Section 5. *The paper would be strengthened by either proving (or empirically measuring) that the sup-norm error is small for the features used, or by honestly delineating which claims are proven and which are heuristic.*

2. **No statistical rigor in Atari results (Section 5.1).** The paper does not report the number of seeds, variance across runs, or any measure of statistical significance for the Atari 57 results (Figure 5). My search for "seed" in the paper found zero matches. Given the high variance of deep RL on Atari, single curves without confidence intervals are not persuasive evidence. The claim that Sketch-DQN "attains higher performance on both metrics relative to C51 and QR-DQN" cannot be evaluated without knowing whether the difference is significant. This is the most concrete weakness in the empirical section and directly undermines the paper's claim that "the sketch framework can be reliably applied to deep RL."

### Minor

3. **Sensitivity to the reference distribution \(\mu\) is not discussed.** The entire algorithm — both the Bellman coefficients \(B_r\) (Eq.~6) and the value-readout coefficients \(\beta\) (Section 5.1) — depends on the choice of \(\mu\), taken as Uniform([G_min, G_max]) in experiments. If the true return distributions are concentrated in a subrange, the regression may be optimized for regions where few returns lie. No sensitivity analysis or guidance for choosing \(\mu\) beyond covering the return range is provided.

4. **SFDP comparison is relegated to the appendix.** A central motivation is that Sketch-DP avoids costly imputation and is substantially faster than SFDP, but the corresponding experimental comparison is only referenced in the appendix (line 490). Given that this is a core claimed advantage, a representative runtime/accuracy figure in the main text would substantially strengthen the paper.

5. **No analysis of the linear value readout for action selection.** The greedy policy in Sketch-DQN uses \(\langle \beta, U_\theta(x,a) \rangle\) to predict expected returns, where \(\beta\) is fit via linear regression under \(\mu\). The error introduced by this readout (which could misdirect action selection) is neither analyzed nor ablated. An ablation comparing the linear readout to a small learned network would clarify whether the sketch representation or the readout is the limiting factor.

### Trivial
None that are not parser artifacts.

---

## Nice-to-Haves

- A brief discussion of limitations (sensitivity to \(\mu\), linear readout error, bounded-return assumption in the theory) would strengthen the paper by setting realistic expectations.
- Including hyperparameter details (anchor points, slope values, network architecture specifics) more prominently rather than only in the appendix would improve reproducibility.
- The excess Cramér metric (Cramér distance minus the categorical projection's Cramér distance) could favor methods that produce distributions close to that projection; a brief caveat would be appropriate.

---

## Removed Points

These points from the reviewers are flagged to be removed. Treat them with caution.

- **"The choice of MRPs: all three are relatively simple"** — The MRPs (Random chain, Directed chain, DC+Gaussian R) are standard testbeds for distributional RL methods and are adequate for the tabular analysis. The critic does not propose a concrete more-complex domain that would change the conclusions.
- **"More recent distributional methods (e.g., FQF, DMIX) are absent"** — The paper compares against the most directly relevant distributional methods (C51, QR-DQN, IQN). Missing newer methods is a scope concern, not a flaw, and the paper does not claim SOTA.
- **"No information about the number of seeds" phrased as implying single-run speculation** — The core point (lack of statistical rigor) is kept as a Major weakness. The speculation that results are "from a single run" is removed as unsupported by evidence; the paper simply does not report seeds.
- **Generic/superficial strengths** from Strength Finder: "Walk-through visualization aids understanding" is kept because it's concrete. "Competitive deep RL results" is kept but reframed as a feasibility demonstration rather than a strong "competitive" claim.
- **Runtime data being in the appendix** — This is noted as a minor weakness but is not unusual; the paper does reference it.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation that the paper itself does not already contain or imply.

---

## Suggestions

1. **Report seed counts and standard errors for all Atari results.** At minimum, report mean and standard error across 3–5 seeds per game, or follow the standard Atari protocol. This is the single most important improvement for the deep RL section.
2. **Bridge the theory-practice gap.** Either (a) prove that for Lipschitz features with a covering argument, the sup-norm error in Proposition 1 can be bounded by the regression error under \(\mu\) plus a term that goes to zero as \(m\) grows, or (b) empirically measure the sup-norm error on the true return support for the features used in practice. This would turn the abstract template into a concrete guarantee for the algorithms being run.
3. **Show the SFDP comparison in the main text.** A single runtime/accuracy plot comparing Sketch-DP to SFDP on a tabular MRP would concretely demonstrate the "avoiding imputation" advantage that motivates the paper.
4. **Add a sensitivity analysis for \(\mu\).** Show that results are robust to moderate changes in \(\mu\) for at least one tabular MRP, or identify where they break.

---

## Score and Decision

**Originality:** The idea of performing Bellman updates entirely in the sketch space via linear regression is novel and well-motivated. The paper opens a new algorithmic family in distributional RL.

**Importance of research question:** Distributional RL is an active area, and reducing the computational overhead of sketch-based methods is practically relevant.

**Claims supported:** Partially. The tabular results are well-supported. The Atari results lack statistical rigor. The convergence analysis is a template that is not fully instantiated for the features used in practice.

**Soundness of experiments:** Tabular experiments are thorough. Atari experiments lack seed reporting and statistical rigor.

**Clarity of writing:** Clear and well-structured. The paper is honest about the limitations of its theory.

**Value to the community:** The framework is likely to inspire follow-up work on sketch-based distributional RL and may be useful for neuroscience models of distributional coding.

**Overall:** The paper makes a genuine contribution with a novel algorithmic framework, clear exposition, and reasonable (though incomplete) empirical validation. The weaknesses are real but addressable — none are fatal. The theory-practice gap is acknowledged by the authors and is a common pattern in ML theory papers; the lack of seed reporting in Atari results is the most significant concrete flaw.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>