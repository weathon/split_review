## Summary

STNAdam introduces a two-track iteration framework for stochastic Adam in "nonconvex + weakly-convex" composite optimization (Eq. 1). The algorithm maintains intertwined extrapolation and regular update trajectories governed by Nesterov momentum and Adam-style adaptive conditioning (Algorithm 1). Under the Kurdyka-Łojasiewicz property and a coercivity assumption, convergence in expectation to a stationary point is established (Theorems 1–2), accommodating plug-in variance-reduced gradient estimators (SGD, SAGA, SARAH). Empirical results on low-light image enhancement (LIE) on the LOL dataset are reported.

---

## Strengths

- **Novel two-track algorithmic design**: The two-track coupled iteration (Algorithm 1, Figure 1) that simultaneously maintains an extrapolation trajectory (via $\tilde{\varpi}^{k+1}$) and a regular update trajectory (via $\hat{\varpi}^{k+1}$) is architecturally distinct from all single-track accelerated Adam variants. The motivation—promoting a larger update neighborhood while refining the iteration direction—is intuitive and clearly illustrated.

- **Rigorous convergence theory under KL**: Theorem 1 establishes the finite-length property (Eq. 12) and convergence to a stationary point in expectation. Theorem 2 provides explicit rate cases depending on the KL exponent $\vartheta$—linear convergence for $\vartheta \in (0, 1/2]$ and polynomial for $\vartheta \in (1/2, 1)$. The energy function $G^k$ (Eq. 9) and the Lemma 1 framework unify all three estimator variants (SGD, SAGA, SARAH) under a single analysis.

- **Plug-and-play variance reduction**: The generic variance-reduced estimator conditions in Lemma 1 allow SVRG, SAGA, SARAH, and SPIDER to be dropped in as estimators without requiring separate convergence proofs. This is genuinely flexible and theoretically neat.

- **Solid empirical performance on the target task**: STNAdam-SARAH achieves PSNR 22.26, SSIM 0.9062, LPIPS 0.0501 on LOL (Table 2), outperforming the three single-track optimizer baselines (SGD, SAdam/Adam, SNAdam) and all five specialized LIE methods. Qualitative results in Figures 2–3 visibly support the quantitative numbers.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation to isolate the two-track contribution**: The paper's primary algorithmic claim is that the *two-track framework* provides benefit beyond single-track variants. The only experiment that directly tests this is STNAdam-SGD (18.06 PSNR) vs. SNAdam (17.14 PSNR) — the same SGD estimator, different track structure (~0.9 dB gain). However, the dominant effect in Table 2 is the choice of variance-reduction estimator: STNAdam-SGD → STNAdam-SAGA → STNAdam-SARAH spans 18.06 → 21.05 → 22.26 PSNR, a 4+ dB range. Without a single-track SAGA or SARAH baseline (e.g., SAdam-SAGA, SAdam-SARAH), it is impossible to disentangle the ~0.9 dB two-track contribution from the ~4 dB variance-reduction contribution. The signature contribution of the paper is thus not adequately demonstrated in the experiments.

- **Experimental scope insufficient for the stated claims**: The paper's introduction positions STNAdam as an advancement for "modern deep learning tasks" (Section 1.2) and compares to Adam and SNAdam in that spirit. Yet all empirical evidence comes from a single task (LIE) on a single dataset (LOL), applied to the energy-minimization formulation (Eq. 14) of LR3M, which is a relatively small-scale imaging inverse problem. There are no neural network training experiments, no image classification, no language modeling, no standard ML benchmarks. The scope of claimed contribution and the scope of evidence are misaligned.

- **Implausible and unexplained timing results**: Table 2 reports STNAdam-SARAH (2.64e-05 s) as the *fastest* of all 11 methods, faster than plain SGD (2.85e-05 s), despite SARAH requiring periodic full-gradient resets and the two-track structure adding a second proximal step per iteration. In Table 3 this is replicated (2.34e-05 s for STNAdam-SARAH, faster than every baseline). The paper does not explain what "Time(s)" measures (per-iteration, per-epoch, total, inference?). A method with demonstrably higher per-iteration arithmetic complexity reported as strictly fastest, with no explanation, significantly undermines trust in the quantitative results.

### Minor

- **Abstract's "almost surely" claim stronger than theorems support**: The abstract states that STNAdam "almost surely converges to a stationary point." Theorem 1(ii) establishes convergence of $\{\bar{x}^k\}$ to a stationary point *in expectation*. Lemma 4 properties (1) and (5) do establish some almost-sure statements (finite-length a.s. of $\|\bar{x}^k - \bar{x}^{k-1}\|$ and $\text{dist}(\theta^k, \Omega) \to 0$ a.s.), but the full a.s. limit-point convergence is not explicitly proven in main text. The weaker "in expectation" qualifier should appear in the abstract.

- **SAdam baseline citation is inconsistent**: Section 4 introduces the SAdam comparison as "SAdam (Kingma & Ba, 2014)," which is the original Adam paper. Section 1.1 attributes SAdam to "Le-Duc et al. (2024)." These designate different algorithms; if the comparison uses vanilla Adam rather than the SAdam of Le-Duc et al., the baseline is misrepresented and comparisons in Table 2 are affected.

- **"Removes hand-tuning" claim is overstated**: Contribution (ii) states that parameters "can be dynamically scheduled within some iterate-dependent finite intervals, removing hand-tuning." However, inspection of Eqs. (6)–(8) shows the lower bounds $\underline{\gamma}$, $\underline{\lambda}$, $\underline{\alpha}$ all depend on the Lipschitz smoothness constant $L$, weak-convexity modulus $\tau$, and estimator-specific constants $V_1, V_\Upsilon, \rho$. These are unknown in practice for general problems. Remark 3 acknowledges this only partially, saying $L$ and $\tau$ can "be appropriately increased if necessary," which is not a practical schedule. The claim should be qualified.

### Trivial

- The proof structure jumps from "Step 3" to "Step 5" with no "Step 4" in the main text. This is a presentation artifact (Step 4 is presumably in the appendix) but makes the convergence argument hard to follow in isolation.

---

## Nice-to-Haves

- Adding single-track SAGA/SARAH baselines (e.g., SAdam-SAGA, SAdam-SARAH) would directly quantify the two-track contribution vs. the variance-reduction contribution and substantially sharpen the paper's core claim.
- Reporting convergence curves (objective value vs. iterations) for competing methods would make the two-track advantage visually intuitive.
- A brief discussion connecting the KL exponent $\vartheta$ to the specific LIE objective (Eq. 14) would make Theorem 2's rate cases more than an abstract statement.
- Testing on at least one neural network training benchmark (e.g., a small image classification task) would close the gap between the claimed scope and the experimental evidence.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "Comparisons with NPE, DeHz, LIME, Retinex-Net, LR3M are not informative about optimizer quality."** — REMOVED. The paper applies STNAdam to the LR3M objective (Eq. 14) and uses the Retinex-Net training framework. Comparing the optimizer-applied model against domain-specialized methods is standard practice in imaging optimization papers and correctly demonstrates that the optimizer can match or beat specialized design choices. The comparisons are not meaningless.

- **Harsh critic: "Practical implementation of SAGA/SARAH not described — omissions make results non-reproducible."** — REMOVED as a reproducibility nitpick. Specific implementation details such as mini-batch sizes, SARAH reset probability p, and epoch count are described in the appendix (which is stripped by the parser). The SARAH formulation is fully specified in the main text (Eq. for $\bar{\nabla}f(x^k)_\text{SARAH}$, including probability $p$).

- **Harsh critic: "Step 5 assumes KL exponent known — connection between Theorem 2's rate cases and empirical performance is unspecified."** — DEMOTED to Nice-to-Have. The KL exponent discussion is standard theoretical coverage; the paper is not obligated to compute $\vartheta$ for the LIE task, though it would strengthen the connection.

- **Harsh critic: "Section 2 asymmetry: fixed α for x^{k+1} but random α_{k+1} for x̃^{k+1} is unexplained."** — REMOVED. This is by design in the two-track framework. The fixed α for the x-track and the randomly scheduled α_{k+1} for the x̃-track are precisely what generates the two different trajectories and are central to the convergence analysis (Eqs. 6–8 define the valid ranges). There is no error here.

- **Strength finder: "Dynamic parameter scheduling with non-vanishing lower bounds removes manual tuning."** — REMOVED as a strength. As verified above (Eqs. 6–8, Remark 3), the lower bounds depend on unknown problem-dependent constants (L, τ). The claim of removed hand-tuning conflicts with a verified weakness.

- **Strength finder: "Empirical results support the two-track design benefits."** — PARTIALLY REMOVED. The empirical gain attributable specifically to the two-track structure (STNAdam-SGD vs. SNAdam, ~0.9 dB) is partially visible, but the dominant gain comes from variance reduction. The claim that results "directly support the two-track design" is too strong given the missing ablation.

---

## Novel Insights

The most genuinely novel aspect of this work is the two-track energy function $G^k$ (Eq. 9) used in the convergence proof, which couples $\Phi(\bar{x}^k) + \Phi(x^k)$ with the KL-based variance-reduction decay. The use of a joint-sequence KL inequality (Lemma 5) applied to an expectation quantity — borrowed from Robbins & Siegmund (1971) — to handle the stochastic composite setting with non-vanishing momentum is technically careful. The unification of SVRG, SAGA, and SARAH under a single convergence proof via the abstract Lemma 1 conditions is also a useful contribution to the stochastic optimization literature, though the experimental evidence for the resulting practical benefits is insufficiently broad.

---

## Suggestions

1. Add single-track SAGA and SARAH baselines (e.g., SNAdam-SAGA, SNAdam-SARAH) to Table 2 to directly isolate the contribution of the two-track structure from the contribution of variance reduction.
2. Clarify what "Time(s)" measures in Tables 2–3, and explain why SARAH-based variants are reported as faster than SGD; if this is an artifact of batch size or implementation, state it explicitly.
3. Resolve the SAdam citation: if the baseline is Kingma & Ba (2014)'s Adam, call it Adam; if it is Le-Duc et al. (2024)'s SAdam, cite it accordingly and verify the correct algorithm is implemented.
4. Reconcile the abstract's "almost surely converges" with Theorem 1(ii)'s "in expectation" qualifier.
5. Qualify the "removes hand-tuning" claim in Contribution (ii) to acknowledge that the parameter schedule requires estimates of $L$ and $\tau$.
6. Add at least one standard ML training experiment (even small-scale, e.g., ResNet on CIFAR-10) to provide evidence that the method transfers beyond the LIE energy-minimization setting.

---

**Axis Evaluations:**

- **Originality**: Moderate. The two-track coupled iteration is a novel algorithmic construct, but the surrounding ideas (Nesterov+Adam, KL convergence, variance reduction) are well-established.
- **Importance of research question**: Moderate. Nonconvex+weakly-convex composite optimization is a legitimate and important problem class.
- **Claims supported**: Weak. The primary algorithmic claim (two-track benefit) is not cleanly isolated; the timing anomaly is unexplained; the "removes hand-tuning" claim is overstated.
- **Soundness of experiments**: Weak. Single task, single dataset; implausible timing results; missing ablations.
- **Clarity of writing**: Acceptable. Notation is clear, theory is well-organized; citation inconsistency and abstract/theorem discrepancy detract.
- **Value to research community**: Moderate in theory (convergence unification); low in empirical guidance (insufficient breadth).

---

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>2</community_value>
</subscores>