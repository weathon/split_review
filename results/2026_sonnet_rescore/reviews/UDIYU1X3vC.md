## Summary
This paper introduces Proper Velocity Neural Networks (PVNNs), the first systematic treatment of the Proper Velocity (PV) model of hyperbolic space for deep learning. The authors establish the complete Riemannian geometry of PV space (exponential/logarithmic maps, parallel transport, geodesic distance), prove its isometry to the Poincaré ball, and then develop a full suite of neural layers—MLR, FC, convolutional, activation, and GyroBN—validated across four experimental tasks.

---

## Strengths

- **Complete Riemannian toolkit via isometry.** Theorems 4.2–4.3 derive closed-form PV operators (Exp, Log, PT, geodesic distance) in a principled way by leveraging the Poincaré ball isometry. These operators did not previously exist in the ML literature and are necessary for building PV layers. The formulas in Eqs. (10)–(13) are concrete, verifiable, and well-documented.

- **Efficient PV MLR avoiding memory explosion.** Theorem 5.2 provides an unconstrained parameterization $(z_k, r_k)$ that eliminates the explicit gyroaddition step and replaces the $b \times C \times n$ intermediate tensor with a matrix multiplication over inner products $\langle x, z_k\rangle$ (Eq. 19). The paper explicitly explains why this is practically necessary (memory and compute) and verifies the Euclidean limit as $K \to 0^-$.

- **Principled GyroBN with theoretical guarantees.** Theorem 5.4 proves homogeneity of mean and dispersion on PV space, guaranteeing that the centering (Eq. 25) shifts the Fréchet mean to the origin and the scaling normalizes variance to $s^2$. This is a concrete theoretical guarantee not present in many prior hyperbolic normalization approaches. The paper also empirically validates this over tangent BN on all four graph datasets (Table 6).

- **Numerical stability quantitatively demonstrated.** Tables 1–3 provide a clear, reproducible comparison. PV achieves zero failure rate up to $r=1000$ in FP32 (Table 1), superior round-trip Riemannian error ($2.1\times10^{-7}$ vs $2.1\times10^{-4}$ for Poincaré, $1.0\times10^0$ for hyperboloid in FP32, Table 2), and avoids both the vanishing gradients of the Poincaré ball and the exploding/NaN gradients of the hyperboloid (Table 3). The advantage over the hyperboloid is especially clear and unambiguous.

---

## Weaknesses

### Fatal
None.

### Major

- **The Airport result (+9.56pp over HNN++) is anomalous and unexplained.** Table 5 shows PVNN achieving 97.96 ± 0.42 on Airport—a 9.56pp gain over HNN++ (88.40 ± 0.17). Since PV is isometric to the Poincaré ball (Theorem 4.2), this jump cannot arise from a geometric advantage. Compounding the issue, LNN (hyperboloid, same underlying geometry as HNN++) achieves only 75.20 ± 1.08 on the same dataset—a 13pp gap against HNN++ that is also unexplained. The large discrepancy between LNN and HNN++ raises the possibility that LNN is under-tuned on Airport. Table 6 offers partial insight—PVNN+TFC achieves only 86.99 ± 0.61, suggesting the Riemannian PV FC layer specifically drives the Airport gain—but the paper does not make this argument explicit or investigate *why* the Riemannian construction matters so much on this particular dataset. The largest positive result in the paper receives the least scrutiny.

- **Missing Poincaré CNN in the genomic experiment.** Section 6.4 (Table 10) compares PVCNN only against Euclidean CNN and HCNN-S (hyperboloid). Since PVCNN is isometric to a Poincaré CNN, the most informative comparison—isolating whether the gains come from PV's coordinate parameterization or from general hyperbolic convolution—is absent. The 9+ MCC point improvement on SINEs cannot be attributed specifically to PV without this control. The paper says it follows Khan et al. (2025) who only used the hyperboloid, but the contribution of *this* paper requires the Poincaré CNN comparison for proper interpretation.

### Minor

- **Framing slightly overstates PV as a geometrically novel space.** The abstract and introduction present PV as "an alternative representation" alongside the Poincaré ball and hyperboloid models, which implies independent standing. But Theorem 4.2 establishes that PV is Riemannian-isometric to the Poincaré ball—they are the same geometry in different coordinates. The more accurate and defensible framing is that PV provides a better-conditioned coordinate chart for the same underlying hyperbolic space. The paper is transparent about the isometry (Section 4.1 prominently), but the introduction does not reflect this nuance, and the claim "PV offers an unconstrained representation that alleviates numerical instabilities" (p. 2) is stated as applying equally against both Poincaré and hyperboloid when the evidence (Tables 1–3) shows the primary advantage is over the hyperboloid, with more modest differences against the Poincaré ball.

- **No discussion of when Fréchet GyroBN is computationally justified.** Table 7 shows that Tangent and Euclidean variants are ~2× faster and often match Fréchet GyroBN on Disease and Airport, while Fréchet variants are consistently better only on PubMed and inconsistently on Cora. The paper notes this briefly ("Fréchet-based GyroBN attains the best accuracies, it is more computationally expensive") but does not give practitioners guidance on when to prefer the simpler variants.

### Trivial
None.

---

## Nice-to-Haves

- A controlled comparison using the same layer design (e.g., Shimizu-style parameterization) for both Poincaré ball and PV, differing only in coordinate chart, would cleanly isolate the coordinate advantage and would significantly strengthen the paper's central message.
- Wall-clock or FLOPs comparison between PV and Poincaré operators would be useful, as PV operators (particularly Log and PT in Eqs. 11–12) route through the isometry π and involve additional terms.
- An investigation of *why* the Riemannian FC outperforms tangent FC specifically on Airport (Table 6 shows ~11pp difference) would turn an ablation table into an insight about when hyperbolic geometry matters.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Section 5.4: variance sentence not connected back to centering step"** — The paper explicitly states "After the centering, the batch mean is shifted to the identity **0**. After the biasing, it is translated to β. After the scaling, the variance becomes $s^2$" (§5.4, immediately after Theorem 5.4). The connection the critic demanded is present in the text.

- **"PV operators substantially more complex than Poincaré counterparts without computational discussion"** — This is true that the operators are more complex, but the paper presents wall-clock comparisons for GyroBN variants (Table 7) and discusses efficiency. Retained only as a nice-to-have (direct operator FLOP comparison), not as a major weakness.

- **"Table 6 case for Riemannian FC over tangent FC rests primarily on Disease"** — Table 6 actually shows the Riemannian FC wins clearly on both Disease *and* Airport (97.93 vs 86.99 on Airport—a massive difference). The critic's factual characterization is incorrect. Removed.

- **Strengthening suggestions about gradient stability during training** — The paper already provides clear numerical stability evidence in Tables 1–3. Demanding additional training-time instability experiments is outside the paper's stated scope and is a nice-to-have, not a weakness.

---

## Novel Insights

The reviewers surface one genuinely important structural observation: because PV and the Poincaré ball are isometric, any empirical performance difference between PVNN and Poincaré ball networks must arise solely from the coordinate parameterization—not from the geometry. This reframes the contribution: PV is not a new geometric space but a better-conditioned coordinate chart for the same hyperbolic space. The numerical stability results (Tables 1–3) then become the primary, cleanest justification for adopting PV, and the empirical gains are best understood as downstream consequences of that stability advantage. The Table 6 data further suggests that the Riemannian PV FC layer specifically—not the coordinate system alone—drives the large Airport gains, which hints at an interesting interaction between parameterization quality and dataset hyperbolicity that the paper does not yet analyze.

---

## Suggestions

1. Add a Poincaré CNN baseline in Section 6.4 to determine whether PVCNN's genomic gains are PV-specific or shared by all Poincaré-equivalent formulations.
2. In Section 6.3, explicitly analyze the Airport result: show that the gain over PVNN+TFC (~11pp, Table 6) comes from the Riemannian FC layer, and connect this to Airport's $\delta=1$ hyperbolicity. This converts an unexplained anomaly into the paper's most compelling finding.
3. Revise the introduction to frame PV as a better-conditioned coordinate chart for hyperbolic space rather than a distinct geometry, consistent with Theorem 4.2. This framing is more honest, still novel, and more defensible against reviewers who would otherwise focus on the isometry.
4. Clarify Table 7 with a brief recommendation: the Tangent/Euclidean variants are recommended for practitioners seeking speed, while Fréchet GyroBN is preferred when accuracy on highly hyperbolic graphs is critical.

---

## Score and Decision

**Originality:** The paper is the first systematic treatment of PV for deep learning, with all layers and operators derived from scratch. The isometry to the Poincaré ball means the geometry is not new, but the framework, tooling, and parameterization choices are original. *Score: 3/5*

**Importance of research question:** Numerical stability in hyperbolic neural networks is a genuine and widely acknowledged problem. Providing an unconstrained parameterization with provable stability guarantees addresses a real bottleneck. *Score: 4/5*

**Claims well-supported:** The numerical stability claims are strongly supported (Tables 1–3). The graph learning and image classification claims are mostly supported but with the Airport anomaly unaddressed. The genomic claims are partially supported but lack the Poincaré CNN control. *Score: 3/5*

**Soundness of experiments:** Core experimental design is appropriate (5-fold cross-validation, ablations, matched architectures). The LNN–HNN++ gap on Airport and missing Poincaré CNN comparison reduce confidence. *Score: 3/5*

**Clarity of writing:** Generally well-organized and mathematically precise. The distinction between coordinate-chart advantage and geometric novelty could be clearer in the introduction. *Score: 4/5*

**Value to research community:** First complete PV toolkit for deep learning, reproducible stability benchmarks, and a comprehensive layer library usable by practitioners. Even with the identified gaps, this is a useful contribution. *Score: 4/5*

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>