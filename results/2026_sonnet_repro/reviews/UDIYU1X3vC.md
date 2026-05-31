Now let me perform calibration search to determine an appropriate score for this paper.Let me read the most similar anchors in full.Now let me do Round 2 narrowing within the 5–7 bracket.Now I have enough to write the final review. Let me assemble it.

---

## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), the first systematic application of the Proper Velocity (PV) model of hyperbolic space to deep learning. The authors establish the complete Riemannian geometry of PV space (Exp/Log maps, parallel transport, geodesic distance) by leveraging the Riemannian isometry between PV and the Poincaré ball, and build a comprehensive suite of neural layers: MLR, FC, convolutional, activation, and batch normalization. Four experiments (numerical stability, image classification, graph node classification, genomic sequence learning) validate both the stability of PV coordinates and the effectiveness of the resulting layers.

---

## Strengths

1. **Complete Riemannian toolkit via isometry.** Theorems 4.2–4.4 rigorously derive closed-form exponential/logarithmic maps, parallel transport, and geodesic distance for PV space using the isometry to the Poincaré ball. These operators are not available in prior ML literature for PV space and enable principled layer construction.

2. **Numerically stable coordinate chart with quantitative evidence.** Tables 1–3 provide concrete numerical evidence: PV achieves zero failure rate up to $r=1000$ in FP32 while the hyperboloid model already fails at $r=20$; PV achieves round-trip error $2.1\times10^{-7}$ (FP32) vs. $2.1\times10^{-4}$ for Poincaré; and PV maintains gradients in $[1.1\times10^{-4},\,2.1\times10^{-6}]$ while the Poincaré ball vanishes and the hyperboloid explodes. These are the paper's most compelling experiments and directly support the main claim.

3. **Efficient PV MLR formulation.** Theorem 5.2 reparameterizes the MLR via unconstrained $(z_k, r_k)$ parameters, replacing an explicit gyroaddition that would produce a $b \times C \times n$ intermediate tensor with an $\langle x, z_k \rangle$ inner product (matrix multiply). The Euclidean limit is recovered exactly as $K \to 0^-$, establishing theoretical soundness.

4. **PV GyroBN with proven normalization guarantees.** Theorem 5.4 formally proves homogeneity of mean (Eq. 26) and homogeneity of dispersion from the origin (Eq. 27), providing a principled guarantee that the centering+scaling in Eq. 25 normalizes Fréchet statistics. Table 6 shows GyroBN outperforming tangent BN on all four datasets.

5. **Comprehensive ablation study.** The paper provides separate ablations on FC type (Table 6), BN variant (Table 7), embedding type (Table 8), and activation choice (Table 9), giving a clear picture of which components contribute and when.

---

## Weaknesses

### Fatal
None.

### Major

- **Unexplained Airport anomaly.** Table 5 shows PVNN achieving 97.96 ± 0.42 on Airport, a 9.56pp gain over HNN++ (88.40). More troublingly, LNN (hyperboloid) achieves only 75.20 ± 1.08 on the same task — a 13.2pp gap between two methods that model the same underlying geometry. Since PV is isometric to the Poincaré ball (Theorem 4.2), a near-10pp lift over the Poincaré-based HNN++ cannot arise from geometry alone. The paper states the improvement is evidence that "PV geometry is more effective on strongly hyperbolic graphs" (Sec. 6.3), but this framing is in tension with the isometry established in Theorem 4.2. A more plausible explanation is that PVNN's specific parameterization has a strong optimization advantage on Airport, or that the hyperboloid and Poincaré baselines are undertrained on this dataset — but neither explanation is examined. This is the largest positive result in the paper and it receives the least scrutiny. While the result is internally reproducible (Tables 6, 7, 9 all confirm similarly high Airport numbers), the absence of any diagnosis weakens the evidential value.

- **Missing Poincaré CNN comparison in the genomic experiment.** Section 6.4 compares PVCNN against Euclidean CNN and HCNN-S (hyperboloid). Because PV is isometric to the Poincaré ball (Theorem 4.2), a Poincaré convolutional network is the minimal necessary comparison to isolate whether PVCNN's 9-point MCC gain on SINEs is PV-specific or shared by any Poincaré-equivalent parameterization. Its absence makes the genomic results uninterpretable with respect to the paper's core framing.

### Minor

- **Framing partially obscures the isometry contribution.** The introduction claims PV "offers an unconstrained representation that alleviates numerical instabilities" (p.2) as though the numerical advantage applies equally against Poincaré and hyperboloid. Table 1 shows zero failure rate for *both* PV and Poincaré (hyperboloid is the problem); Table 2 and Table 3 do show PV outperforming Poincaré, but the margin is modest in FP64. The abstract's characterization of PV as a "stable alternative" to the Poincaré ball, while technically defensible, overstates the case against Poincaré relative to what the experiments demonstrate. Because Theorem 4.2 is proven early and the paper uses it throughout, the more accurate framing — that PV is a *better-conditioned coordinate chart* for the same hyperbolic space — is understated.

- **No computational cost comparison vs. Poincaré operators.** PV operators (Eq. 11–12) route through the isometry $\pi$ and involve Möbius gyration terms not present in the Poincaré counterparts. For a paper positioning PV as a practical alternative, a wall-clock or FLOPs comparison against Poincaré layers would clarify whether the stability gains come at a cost.

- **Fréchet GyroBN vs. tangent/Euclidean trade-off.** Table 7 shows that Tangent and Euclidean BN variants, which are ~2× faster, match Fréchet GyroBN on Disease and Airport, while Fréchet clearly wins on PubMed (74.34 vs. 61.50 for Tangent). The paper notes this trade-off briefly but does not offer guidance on when the more expensive Fréchet variant is worth using, which limits the practical utility of this contribution.

### Trivial

- None beyond minor presentation issues.

---

## Nice-to-Haves

- A controlled comparison pitting PVNN directly against a well-implemented Poincaré network with matched parameterization (e.g., same Shimizu parameterization for both) would isolate the coordinate-chart advantage cleanly. Currently, the experiments compare against prior implementations that differ in multiple design choices.
- A learning-curve comparison in a high-curvature or high-dimension regime showing that PVNN trains where Poincaré/hyperboloid networks require gradient clipping or FP64 fallback would convert the theoretical stability advantage into a demonstrated practical advantage.
- Understanding why PVCNN helps so much on SINEs — whether sequence hierarchies have specific hyperbolic structure that the PV parameterization captures — would make the genomic section more than a benchmark result.
- The Airport dataset is small and high-variance; a brief sensitivity analysis over seeds/hyperparameters would bolster confidence in the headline number.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Airport result is implausible given the geometry"** (Harsh Critic, framed as a potential fatal flaw): The critic's framing that a 9.56pp gain is impossible because PV is isometric to Poincaré goes too far. The isometry guarantees geometric equivalence, not that all parameterizations achieve the same accuracy in practice — optimization and conditioning can differ substantially. Tables 6, 7, and 9 independently reproduce the high Airport performance. Demoted to Major (lack of *explanation*), not Fatal.

- **"GyroBN's connection between centering and variance normalization is unclear"** (Harsh Critic, re: Sec. 5.4): The paper explicitly states (lines 217–218): "After the centering, the batch mean is shifted to the identity 0. After the biasing, it is translated to β. After the scaling, the variance becomes s²." This is clear and direct. Removed as the critic misread.

- **"PV operators are more complex than Poincaré, undermining practical value"** (Harsh Critic, Sec. 4.2): The paper uses the isometry precisely to simplify derivations — the log map and parallel transport are defined *via* $\pi$. The complexity concern is valid as a nice-to-have (computational cost comparison), but it does not undermine practical value without empirical evidence. Demoted to minor/nice-to-have.

- **"Case for Riemannian FC over tangent FC rests primarily on Disease"** (Harsh Critic, Table 6): Looking at Table 6, PVNN (Riemannian FC) achieves 97.93 on Airport vs. PVNN+TFC's 86.99 — a strong signal on Airport too. The critic's concern is undermined by the Airport data. Removed.

- **Strength: "Strong empirical gains on Airport (+5.86%)"** (Strength Finder): This is technically correct but conflicts with the Major weakness about the Airport anomaly being unexplained. Kept in context of Major weakness discussion rather than as a clean strength.

---

## Novel Insights

The most genuinely novel observation is that the PV model — despite being Riemannian-isometric to the Poincaré ball — achieves meaningfully different downstream accuracy on at least some datasets (Airport, SINEs), suggesting that coordinate parameterization and the specific algebraic structure of gyroaddition have non-trivial optimization consequences beyond pure geometric equivalence. This raises an interesting open question: what properties of a coordinate chart (smoothness of the gradient landscape, condition number of the metric tensor in practice, boundedness of the parameter space) drive the observed performance differences between isometric representations? The PV model's unconstrained domain ($\mathbb{R}^n$) may offer a materially smoother optimization landscape than the bounded Poincaré ball, independent of the underlying geometry.

---

## Suggestions

1. Add a Poincaré CNN baseline to Table 10 to isolate whether PVCNN's SINEs gains are PV-specific or shared by all Poincaré-equivalent architectures.
2. Diagnose the Airport result: report whether HNN++ and LNN were tuned on Airport to the same degree as PVNN, or show a curvature sweep/seed sensitivity analysis to understand the robustness of the 97.96 result.
3. Add a one-line wall-clock comparison of PV vs. Poincaré operators at matched dimension and batch size to address the implicit cost question raised by the isometry-based derivations.
4. Revise the introduction to more accurately frame PV as a better-conditioned coordinate chart for the same hyperbolic space rather than an alternative geometry, to align the framing with Theorem 4.2.

---

## Score Calibration

**Round 1 anchors:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `xA25Ib7H8U` | 2.33 | 1 (low) | Rejected theory paper on Ricci flows — weaker and narrower than PVNN |
| `b2FFWnwZxl` | 3.40 | 1 (low) | Rejected HVT without proper ablations — weaker than PVNN |
| `q6WtaLj8O1` | 3.00 | 1 (low) | Rejected hyperbolic hypergraph GNN — narrower and less rigorous |
| `bwOndfohRK` | 6.00 | 1 (mid) | Accepted symmetric-space NN — similar theoretical scope, PVNN comparable |
| `ekz1hN5QNh` | 6.00 | 1 (mid) | Accepted fully hyperbolic CNN — most structurally similar to PVNN |
| `jzneu6AO2x` | 4.25 | 1 (mid) | Rejected hyperbolic prototypical networks — narrower scope, weaker |
| `WOopKWDWtS` | 4.40 | 1 (mid) | Rejected hyperbolic curvature learning — less rigorous |
| `Xo0Q1N7CGk` | 8.00 | 1 (high) | Very different topic (grid cells) — not comparable |

**Round 1 bracket:** 5.5–7.0

**Round 2 anchors:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `ekz1hN5QNh` | 6.00 | 2 | HCNN — identical structure; PVNN has broader scope and better BN theory |
| `bwOndfohRK` | 6.00 | 2 | Symmetric spaces NN — PVNN more concrete and better ablated |
| `30aSE3FB3L` | 5.67 | 2 | Matrix Manifold NN++ — gyrovector-based, less complete experiments |
| `okYdj8Ysru` | 5.20 | 2 | Lie Group BN — more narrow, BN-focused paper |
| `83le3arfeA` | 5.50 | 2 | Balanced hyperbolic embeddings — application paper, less theory |
| `YcaFqY8LWD` | 6.25 | 2 | GyroAtt — general gyro-attention, comparable rigor, rejected |

**Narrowing:** PVNN is clearly stronger than `30aSE3FB3L` (5.67) and `okYdj8Ysru` (5.20) due to more complete theoretical foundations and broader experimental coverage. It is comparable to the two accepted 6.0 papers (`ekz1hN5QNh`, `bwOndfohRK`) and arguably slightly stronger on theoretical rigor (full Riemannian toolkit + normalization guarantees + four tasks vs. two). The unexplained Airport anomaly and missing Poincaré CNN comparison hold it back from 6.5+. Final score: **6.0**, in line with papers like HCNN and Symmetric Spaces NN.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>