I now have everything needed for a thorough, verified review. Let me compose it.

---

## Summary

This paper identifies a previously unreported training instability affecting two natural sparsifying activation functions (shifted ReLU and soft thresholding) when initialized on the Edge of Chaos in very deep networks. The instability arises because the variance map slope equals 1 *and* the curvature is strictly positive at the fixed point, causing any finite-width fluctuation to send the variance diverging. The authors propose a simple, principled fix — magnitude clipping (crelu, cst) — which decouples the Edge-of-Chaos condition from the variance-map slope, guaranteeing local stability. Proof-of-concept experiments on DNNs (MNIST, depth 100, 5 runs) and CNNs (CIFAR10, depth 50) show that the clipped variants can be trained at up to 85% sparsity while retaining baseline ReLU accuracy.

---

## Strengths

- **Novel identification of a specific instability mechanism for sparsifying activations.** The paper proves analytically (Table 1, Section 2) that for shifted ReLU and soft thresholding, the Edge-of-Chaos condition forces \(V'_\phi(q^*)=\chi_{1,\phi}=1\) with strictly positive \(V''_\phi(q^*)>0\). This explains why these otherwise natural sparsifying activations fail in very deep networks — a phenomenon not previously reported for these families. The analysis is mathematically clean and the mechanism is clearly demonstrated.

- **A simple, principled fix derived from the theory.** The clipping modification (crelu/cst, Section 3) is minimal and directly addresses the diagnosed instability. Equations (14–17) show that clipping decouples \(V'_\phi(q^*)\) from \(\chi_{1,\phi}\), guaranteeing \(V'_\phi(q^*)<1\) when \(\chi_{1,\phi}=1\). The clipping level \(m\) is grounded in the variance map's shape rather than being a free hyperparameter.

- **Convincing empirical validation for DNNs (5 runs).** For DNNs on MNIST, CReLU and CST at 85% sparsity with appropriately chosen \(m\) achieve 94% test accuracy — matching the ReLU baseline of 94% reported in the same table — while the unclipped variants fail entirely at \(\ge\) 60–70% sparsity. The reported standard deviations (5 runs) are small for successful configurations (e.g., 0.004–0.01), confirming reproducibility. The gradient-norm diagnostics (Figure 4) visually confirm the predicted exploding-gradient mechanism.

- **Explicit formulas linking sparsity targets to variance-map quantities.** Table 1 provides closed-form expressions for \(\hat{\tau}_\phi(s,q^*)\) and \(\sigma_w^2\) at the EoC, giving practitioners a direct way to set sparsity targets from theory without tuning.

---

## Weaknesses

### Fatal
None.

### Major
None. The core theoretical claim is sound; the experimental evidence supports it for DNNs (the primary testbed); the limitations are transparently discussed.

### Minor

- **CNN experiments lack statistical replication.** The Table 1 caption explicitly states that CNN experiments were single-run per hyperparameter combination. This undermines confidence in the CNN claims, particularly for configurations near the instability boundary (e.g., CReLU at 85% sparsity where DNNs show high variance). The paper's frame as "proof-of-concept" mitigates this, but the CNN results should be interpreted more cautiously than the DNN results.

- **Second failure mode (high sparsity + low \(m\)) is identified but not explained.** The paper correctly notes that for 85% sparsity with low clipping magnitude (\(m=0.81\) for CReLU, accuracy \(\approx\)78%), gradients do not explode yet accuracy saturates below the baseline. The paper defers explanation to an appendix ("discussed further in App. sec. loss function") and lists it as future work. While transparency about limitations is commendable, the incomplete characterization tempers the headline claim of "up to 85% sparsity while retaining close to full accuracy" — that claim holds only for *some* values of \(m\) at 85% sparsity.

- **Connection between theoretical curvature and finite-width stability is heuristic.** The discussion of how much curvature \(V''_\phi(q^*)\) is tolerable for a given network width (Section 3.1) is qualitative rather than quantitative. The paper provides no formal bound relating \(V''_\phi(q^*)\), network width, and the probability that \(q^l\) escapes the local basin of attraction. This is a natural next step but a gap in the current analysis.

### Trivial

- The equation on line 155 (\(V'_{\cst}(q) = 2 V'_{\cst}(q)\)) appears to be a typo — it should likely reference \(V'_{\crelu}\) on the right-hand side. Readers may need to cross-check against the expressions for \(\chi_{1,\cst}\).

- Figure numbering in the text references "Figure 5" for exploding gradient plots, but the figure appears to be labeled "Figure 4" in the manuscript. Minor inconsistency.

---

## Nice-to-Haves

- **Actual efficiency measurements.** The paper motivates sparsity as a route to computational efficiency but reports only fractional sparsity, not FLOP counts, memory usage, or wall-clock speedup. While this is a theory + proof-of-concept paper, a simple FLOP comparison (e.g., number of multiply-accumulate operations at 50% vs 85% sparsity) would strengthen the practical motivation without requiring sparse hardware.

- **Sparsity vs. accuracy Pareto visualization.** A scatter plot of test accuracy against achieved sparsity for all trials would give an immediate visual summary of the trade-offs and help readers identify the reliable operating region.

---

## Removed Points

These points were raised in reviews but are removed (with justification):

1. **"Missing ReLU baseline accuracy."** — Factually wrong. Table 1, first row, reports \(\relutau\) with \(\tau=0\) (standard ReLU) achieving 94% on DNN MNIST and 70% on CNN CIFAR10. The clipped activations at 85% sparsity match these numbers. The baseline is present and clearly labeled.

2. **"The DNN experiments lack statistical rigor; high variance in some configurations undermines claims."** — The paper reports 5-run means and standard deviations honestly. The high-variance configurations (e.g., CReLU s=0.85, m=1.74: 28% ± 37%) are *failure cases* that the paper transparently identifies and explains via the theoretical framework. They do not undermine the successful configurations where variance is low (e.g., 0.004). The critic conflates the reporting of failure modes with a weakness in the methodology.

3. **"The 100-layer MNIST architecture is unusual; a simple LeNet reaches >99%."** — The paper explicitly states: "The absolute accuracy of the networks is not the focus of these experiments, rather it is the ability to retain trainability and approximately the accuracy of standard ReLU networks." The deep architecture is chosen to test the theory of deep signal propagation, not to beat SOTA on MNIST.

4. **"No baseline sparsity for ReLU reported."** — Baseline ReLU sparsity (50%) is reported in the first row of Table 1.

5. **"Skip connections in ResNets might already mitigate instability."** — Speculative and outside the paper's stated scope. The authors explicitly list ResNet extension as future work.

6. **Pure formatting/style nitpicks, comments about missing appendix content, and any typos/grammar issues.** — These reflect PDF parsing artifacts or are not substantive evaluation criteria.

---

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the paper identifies a *second* failure mode at high sparsity + low clipping magnitude that it cannot yet explain, which is intellectually honest but also highlights that the theory is incomplete. A genuinely novel observation from synthesis is that the clipping fix has a "Goldilocks" character — too little clipping (low \(m\)) causes the second failure mode (non-exploding but low accuracy), while too much clipping (high \(m\)) causes the first failure mode (exploding gradients). The \(V''_\phi(q^*)\) curvature mediates both regimes, suggesting that the *rate of change* of the slope, not just its sign, may be the unifying diagnostic. This is a direction the paper itself does not explore but that a follow-up could fruitfully pursue.

---

## Suggestions

1. **Add multiple trials for CNN experiments** (at least 3–5 runs per configuration) to match the rigor of the DNN experiments. Given that the paper uses standard architectures and datasets, this should be straightforward.

2. **Clarify the second failure mode.** At minimum, add a hypothesis and supporting evidence (e.g., activation statistics, loss-landscape analysis) to the main paper rather than deferring entirely to an appendix. Even a brief qualitative explanation would strengthen the contribution.

3. **Include a sparsity-vs-accuracy scatter plot** for all configurations to visually delineate the reliable operating region from the failure regimes.

4. **Fix the typo on line 155** (\(V'_{\cst}(q) = 2 V'_{\cst}(q)\) should reference \(V'_{\crelu}\)).

---

## Score and Decision

The paper makes a genuine theoretical contribution: it identifies a previously unreported instability in sparsifying activations at Edge-of-Chaos initialization, provides a clean mathematical diagnosis, and offers a principled fix that demonstrably works. The DNN experiments are rigorous (5 runs, low variance for successful configs), the limitations are transparently discussed, and the writing is clear and well-organized. The main weaknesses — single-run CNN experiments and the incomplete characterization of the second failure mode — are minor relative to the theoretical contribution and can be addressed in a revision. The paper does not overclaim: it frames the experiments as proof-of-concept and explicitly acknowledges open questions.

**Originality:** High — the instability mechanism is novel and specific to this activation family.  
**Significance:** Moderate-high — sparsifying activations could yield practical efficiency gains, and the paper provides a theoretically grounded path to making them trainable.  
**Claims support:** Good for DNNs; moderate for CNNs (limited by single runs).  
**Soundness:** The theory is correct; the experiments support the theory for the primary (DNN) testbed.  
**Clarity:** Well-organized, clear mathematical exposition.  
**Value to community:** Useful for researchers working on efficient deep networks and activation function design.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>