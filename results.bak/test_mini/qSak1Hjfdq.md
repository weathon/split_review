Now let me produce the final consolidated review.

---

## Summary

This paper formalizes the All-Day Multi-Scenes Lifelong Vision-and-Language Navigation (AML-VLN) problem, where a VLN agent must continually learn across diverse scenes (indoor environments) and environments (normal, low-light, scattering, overexposure). The authors propose **Tucker Adaptation (TuKA)**, which represents multi-hierarchical navigation knowledge as a fourth-order tensor and uses Tucker decomposition to decouple it into shared subspaces (core tensor, encoder/decoder) and scenario-specific experts (scene experts, environment experts). They further design a Decoupled Knowledge Incremental Learning (DKIL) strategy with EWC, consistency, and orthogonal constraints, and build an **AllDayWalker** agent. The paper also extends Habitat with three physics-based imaging models to create a 24-task benchmark spanning 5 simulation scenes and 2 real-world scenes. Results show AllDayWalker achieving 65% average SR (vs. 44% for the best baseline BranchLoRA) and 11% average forgetting rate.

---

## Strengths

1. **Novel high-order tensor adaptation for multi-hierarchical knowledge decoupling.**  
   TuKA uses a fourth-order Tucker decomposition (Section 3.2) to explicitly separate scene-specific factors (U³), environment-specific factors (U⁴), and shared core navigation skills (𝒢) plus encoder/decoder (U¹, U²). This is a genuinely different approach from existing matrix-based LoRA variants (which can only represent two hierarchical levels — shared + task-specific). The ablation in Figure 8 confirms that the 4-order tensor consistently outperforms a 3-order coupled tensor across all 20 tasks, providing direct evidence that the decoupled representation is more powerful.

2. **Strong empirical results across a comprehensive benchmark.**  
   In Table 1, AllDayWalker achieves 65% average SR across 24 tasks, outperforming the best baseline BranchLoRA (44%) by 21 points. The advantage is consistent across nearly all individual tasks. Table 2 reports an average F-SR of 11% vs. 18% for SD-LoRA and 87% for Seq-FT. These results are supported by generalization experiments (Table 5: 55% SR on unseen scenarios vs. 39–40% for baselines) and scaling experiments (Table 4: stable performance when extending from 24 to 30 tasks).

3. **Meaningful infrastructure contribution.**  
   The paper extends Habitat with three physics-based imaging models (atmospheric scattering model Eq. 10, camera noise model Eq. 11, saturation model Eq. 12) to synthesize degraded environments. This enables the AML-VLN benchmark and is a reusable contribution for the community.

4. **Real-world validation and generalization.**  
   The benchmark includes 2 real-world scenes with 2 environments each, and the generalization experiments (Table 5) evaluate on 4 unseen simulation scenes + 2 unseen real-world scenes. AllDayWalker maintains a 15–16% SR advantage over baselines on these held-out scenarios, supporting the claim that decoupled representations transfer to novel conditions.

---

## Weaknesses

### Fatal

None.

### Major

1. **Non-standard forgetting metric.**  
   The forgetting metric F-SR\(_t\) = (M-SR\(_t\) - SR\(_t\)) / M-SR\(_t\) is defined relative to a *jointly trained* upper bound (M-SR\(_t\)), not the standard CL forgetting measure (drop from peak performance on each task after subsequent learning). This produces negative values (e.g., T14: -3%, T20: -4% in Table 2), meaning the sequential model *outperforms* the joint model on those tasks — this is not interpretable as "negative forgetting." While the metric does convey information about the gap to an upper bound, calling it a "forgetting rate" is misleading, and it is not directly comparable to the large body of CL literature that uses the standard backward-transfer / forgetting definition (Chaudhry et al., 2018). The paper's claims about catastrophic forgetting mitigation rest partly on this metric, so it should either be replaced with or augmented by the standard measure.

2. **Insufficient control of task order effects.**  
   Figure 6 states that "the order of tasks is randomized," but the paper does not specify: (a) which specific random order was used for the reported results, (b) whether results are averaged over multiple random orders or seeds, or (c) whether different random orders produce consistent rankings. Lifelong learning is known to be highly sensitive to task order, and a single random draw without variance reporting weakens the reliability of the conclusions. This is a standard expectation for CL benchmarks.

### Minor

3. **Overstated language about "high-dimensional space representation learning."**  
   Section 3.2 and the abstract claim that TuKA performs "high-dimensional space representation learning," but the final adaptation weight ΔW\(_t\) is a 2D matrix (Eq. 3: ΔW\(_t\) = U¹ · (𝒢 ×₃ U³[s,:] ×₄ U⁴[e,:]) · (U²)ᵀ). The high-order tensor is a factored parameterization; the actual learning still occurs in low-rank factor space. The paper should temper this language.

4. **Coupled loss weighting.**  
   The total loss (Eq. 9) uses λ = 1 − (λ₁ + λ₂ + λ₃), which implicitly reduces the weight on the primary navigation loss as regularization terms grow. This coupling means the importance of task performance *decreases* when regularization increases, which could cause the agent to prioritize constraint satisfaction over navigation. The paper does not ablate this design choice.

5. **Retrieval mechanism gives AllDayWalker an advantage independent of TuKA.**  
   Section 3.4 describes a CLIP-based expert retrieval mechanism for test-time scenario identification. This is not used by the baselines, which must infer the task without such retrieval. It is not clear whether the performance gap in Tables 1 and 5 partially reflects this retrieval capability rather than the Tucker decomposition itself. An ablation that evaluates TuKA *without* retrieval, or that provides metadata to baselines, would clarify the source of improvement.

### Trivial

None (see Removed Points).

---

## Nice-to-Haves

- An ablation that isolates the contribution of each loss term (ℒ\(_{ewc}\), ℒ\(_{co}\), ℒ\(_{es}\)) would help understand what drives performance. The current ablation (Table 3) focuses on shared components and tensor order but not on the loss terms.
- Explicit parameter count comparison in a table (the paper says they are comparable but defers details to the appendix).
- Discussion of training-time computational overhead (Fisher information computation, tensor dimensions) relative to baselines.

---

## Removed Points

These points were flagged but do not survive verification against the paper:

- **"Omits standard lifelong learning baselines like EWC on the full model, Progressive Neural Networks, or memory replay."** — The paper's framing is specifically about *parameter-efficient* adaptation (see abstract: "Existing parameter-efficient adapters..."). All 12 baselines are LoRA-based or adapter-based methods, keeping parameter counts comparable. Comparing against full-model fine-tuning (which would use vastly more parameters) would not be apples-to-apples. The paper already includes EWC-LoRA, Lwf-LoRA, and Seq-FT as regularization baselines within this ecosystem. This is a scope-appropriate baseline set.
- **"Figure 2: step-by-step fine-tune and sequential fine-tune appear identical."** — This is parser-vs-PDF artifact from the paper extraction; the original figure would distinguish them. The chart description notes they share values in the extracted table, which is almost certainly a parser flattening issue.
- **Missing related works.** — Not verifiable without external sources.
- **Typos/formatting/style issues.** — Parser artifacts or presentation nitpicks.
- **Reproducibility nitpicks about undisclosed hyperparameters or missing appendix content.** — The appendix exists in the original submission (stripped by parser).
- **Strength Finder claims about the problem being "important" or generic statements.** — Removed as generic/superficial.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Replace or supplement the forgetting metric** with the standard CL measure: for each task \(k\), compute \(\text{Forgetting}_k = \max_{l>k} (a_{l,k}) - a_{T,k}\), where \(a_{l,k}\) is accuracy on task \(k\) after learning task \(l\). This directly quantifies performance degradation and is interpretable. The current gap-to-joint metric can remain as a secondary analysis.
2. **Report results averaged over at least 3 random task orders** with standard deviations. State the specific order used in the main results.
3. **Add an ablation that removes the retrieval mechanism** (Section 3.4) and evaluates AllDayWalker with random expert selection, to isolate the contribution of the Tucker decomposition from the retrieval advantage.
4. **Temper the "high-dimensional space representation learning" language** — TuKA's learning occurs in factored low-rank space; the tensor is a parameterization, not an optimization space.
5. **Explicitly state parameter counts** for each method in the main paper rather than deferring to the appendix.

---

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/.../OyVRrKG8Dj.md` | 3.00 | R1 (low) | Weak VLN paper, rejected — clearly weaker than this paper |
| `/home/.../fQTw3w3hnA.md` | 3.00 | R1 (low) | VLM continual learning, rejected — weaker evaluation |
| `/home/.../pTNAk3QSh.md` | 3.00 | R1 (low) | VLM adapters, withdrawn — less comprehensive |
| `/home/.../mDuton6Tg7.md` | 3.00 | R1 (low) | CLIP continual learning, withdrawn — less novel |
| `/home/.../6qyRiyI5Ky.md` | 2.00 | R1 (low) | CoLaP, rejected — weaker than this paper |
| `/home/.../PaYo96rjij.md` | **6.00** | R1(mid)/R2 | **Uni-Walker** — nearly identical problem; comparably novel method; similar evaluation quality. This paper has more comprehensive benchmark (24–30 tasks vs. 18) and real-world validation, but Uni-Walker uses standard forgetting metrics. **Most relevant anchor.** |
| `/home/.../pFh5ygjN3V.md` | 4.50 | R1 (mid) | M³E — continual VLN with MoE; accepted but weaker method and smaller evaluation. This paper is stronger. |
| `/home/.../T3Vc5fkTzV.md` | 5.50 | R1 (mid) | KeepLoRA — CL with LoRA subspace analysis; accepted. Comparable quality but different domain. |
| `/home/.../Rr8gAjB1dX.md` | 5.33 | R1 (mid) | AdaNav — adaptive reasoning for VLN; rejected. This paper is stronger. |
| `/home/.../QNJjLE2Eog.md` | 4.00 | R1 (mid) | Open-environment VLN; withdrawn. Weaker evaluation. |
| `/home/.../9ktF3pwXi8.md` | 4.67 | R2 | VLN primitives; rejected. Different focus. |
| `/home/.../uqoKr4m8hl.md` | 5.00 | R2 | Adaptive Rank LoRA; rejected. Weaker results. |
| `/home/.../pZj2DhfaVD.md` | 6.00 | R2 | Weight regularization for PECL; accepted. Comparable quality. |

**Round 1 bracket:** I initially placed this paper in the (3.5, 7.5) range based on the weak anchors (~3.0) being clearly weaker and the strong anchors (~8.0) being in different domains (embodied foundation models, 3D generation).

**Round 2 narrowing:** The most directly comparable anchor is Uni-Walker (6.0, Accept Poster), which tackles nearly the same lifelong navigation problem with a similar knowledge-decoupling strategy. This paper's method (Tucker decomposition) is more novel than Uni-Walker's DE-LoRA, its benchmark is more comprehensive (24 rather than 18 tasks, plus diverse environments and real-world scenes), and it contributes a simulator extension. However, the non-standard forgetting metric is a real weakness that Uni-Walker's evaluation does not share. On balance, the paper is comparable in quality to Uni-Walker — the greater novelty and benchmark scope are offset by the metric concern.

**Final positioning:** Slightly above the median round-2 anchors. The paper is stronger than M³E (4.5), KeepLoRA (5.5), and Adaptive Rank (5.0), and comparable to Uni-Walker (6.0). The novel method, strong empirical results, and real-world validation support acceptance, but the forgetting metric and task-order reporting need attention.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>