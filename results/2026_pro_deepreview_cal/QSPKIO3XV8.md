Now I have a strong set of calibration anchors. Let me compile my analysis and write the final review.

**Round 1 Bracket**: Initial bracketing placed the paper between ~5.0 and ~7.0, above HyResPINNs (5.0) and Ensemble/MoE DeepONets (4.33) but below PhyMPGN (8.0).

**Round 2 Narrowing**: Comparing against DisentangO (5.50 — disentangled representation for parametric PDEs, theoretical analysis but limited empirical interpretability validation) and PIG (6.50 — Physics-Informed Gaussians, good experiments but originality concerns). The 3D paper has more concrete demonstrations than DisentangO (clear domain decomposition visualizations, quantitative VI metric, error reduction on Burgers from 0.21→0.0011) but weaker baseline comparisons than PIG. This suggests **~6.0**.

---

## Summary

This paper proposes Dimension Domain Co-Decomposition (3D), a unified PINNs framework that combines CP-decomposition-style dimension factorization with Mixture-of-Experts (MoE) domain decomposition. Inside each expert, a single shared MLP processes (coordinate, index) pairs to produce per-dimension component functions, substantially reducing parameter counts. The authors introduce Variable Interpretability (VI), a metric measuring subspace alignment between learned per-dimension components and reference factors. A Dense MoE router adaptively partitions the domain during training without predefined subdomains or interface conditions. Experiments on Poisson, Wave, Burgers, and Linear Transport equations demonstrate parameter efficiency, accuracy improvements, and automatic domain decomposition around shocks and discontinuities.

## Strengths

- **Genuine parameter efficiency via shared MLP design**: Table 1 demonstrates dramatic parameter reduction compared to per-dimension independent MLPs (e.g., 5392 vs. 26640 for 5D Poisson), and Figure 2 shows comparable or better accuracy despite this reduction. The 10D Poisson result is particularly compelling: with comparable parameter counts (5392 vs. 4929), the shared MLP achieves ℓ₂ error of 1.25×10⁻³ versus 1.29×10⁻¹ for a standard PINN (Section 4.2).

- **Compelling automatic domain decomposition via MoE routing**: On the Viscous Burgers equation (ν=0.01/π), the router with K=2 experts cleanly separates the domain at the shock location x=0 without any predefined partition or interface loss, reducing ℓ₂ error from 0.21 (K=1) to 0.0011 (K=2) (Figure 4, Section 4.3). On the Linear Transport equation, experts capture diagonal stripe structures matching the ground truth (Figure 5). The decompositions are consistent across multiple random seeds and robust to up to 5% noise in initial/boundary conditions.

- **Principled VI metric with predictable behavior**: VI quantifies subspace alignment via QR decomposition and squared singular values (Section 3.2, Equations 5–6). Table 2 shows VI scales sensibly with rank r: near-zero at r=1 for problems requiring higher rank, approaching 100% as r increases. On the Wave equation, VI=1 at r=1 for c=2 (where the solution is exactly rank-1 separable) but requires higher r for higher-frequency variants. This principled behavior supports the metric's validity.

- **Unified framework combining two complementary decomposition strategies**: The integration of dimension decomposition within each expert and MoE-based domain decomposition across experts within a single end-to-end trainable framework is a conceptually clean contribution. The framework is well-diagrammed (Figure 1) and the connection between the two decomposition levels is clearly motivated.

## Weaknesses

### Fatal

None.

### Major

- **Contradictory positioning on automatic domain decomposition novelty**: The related work section (lines 48–50) acknowledges that APINNs (Hu et al., 2023) "use soft gating mechanisms to allow more flexible domain decomposition," yet the very next sentence claims "all existing approaches require predefined partitions of the computational domain." If APINNs already learns soft domain partitions through gating, the claimed novelty of automatic decomposition without predefined regions is significantly weakened. The paper does not explain what specific architectural or methodological difference makes its MoE approach automatic in a way that APINNs' soft gating is not. This mischaracterization undermines a key contribution claim and should be corrected or substantially qualified.

- **Missing experimental baselines for domain and dimension decomposition**: The domain decomposition experiments (Section 4.3) compare only against a single-expert variant (K=1) and do not include any existing domain decomposition baseline such as XPINNs, APINNs, or a manually partitioned PINN with interface loss. Similarly, the dimension decomposition experiments do not compare against SPINNs (Cho et al., 2023), which the paper itself discusses as closely related (Section 3.1). Without these comparisons, it is impossible to assess whether the automatic MoE decomposition actually provides accuracy or efficiency gains over simpler fixed partitions, or whether the shared-MLP parameterization offers advantages over existing tensor-decomposition PINN variants beyond parameter count reduction.

### Minor

- **VI naming overstates what the metric measures**: VI measures subspace containment — whether the ground-truth factor's subspace is contained within the predicted component subspace — not whether individual learned components correspond to specific physical factors (Section 3.2, lines 102–104). The paper acknowledges this explicitly ("VI measures whether the predicted subspace totally covers the exact subspace instead of testing if two subspaces are identical"), so this is not misleading, but the name "Variable Interpretability" suggests a stronger claim of per-component interpretability than the metric actually supports. This is a presentation issue rather than a technical flaw.

- **Computational cost reporting is thin**: Training time is mentioned only in passing for the 10D Poisson experiment (1579s vs. 1184s) and memory comparisons are given as percentages without absolute numbers or a proper table. For a paper that claims efficiency as a contribution, a systematic wall-clock time and memory comparison across all experiments would substantially strengthen the evaluation.

- **Choice of K (number of experts) lacks a principled selection criterion**: The paper notes that beyond K_optimal, additional experts yield diminishing returns (Section 3.3), but no heuristic or quantitative criterion for selecting K is provided beyond visual inspection of router assignments and error trends.

### Trivial

- The vanilla PINN baseline for 5D Poisson uses a 10-layer architecture while the proposed model uses 2 hidden layers — a brief justification for this architectural mismatch would improve clarity, even though the comparison actually favors the baseline in capacity and the proposed model still wins.

## Nice-to-Haves

- Include at least one non-separable PDE to probe the limits of the CP decomposition and demonstrate where the method remains useful versus where it breaks. The authors acknowledge this limitation in the conclusion; an empirical demonstration would strengthen the paper's honesty and scope assessment.

- Ablation on router architecture (depth, width) and softmax temperature to understand sensitivity of the learned domain partitions.

- Reframe VI as a "factor-recovery diagnostic" or "subspace alignment metric" to better match what it actually measures, or supplement it with a metric that assesses per-component recovery after resolving permutation/scaling ambiguities.

- Extend the fine-tuning experiment from 5D→8D (mentioned in passing, Section 4.2) with quantitative results in the main text, as this is a distinctive capability of the separable parameterization that standard PINNs lack.

## Removed Points

*These points were flagged by reviewers but are removed from the main review. Treat with caution.*

- **"Limited novelty — APINNs already solves this"** (from Harsh Critic Point 1): Partially retained as a Major weakness about contradictory positioning. The removed portion — that the MoE approach is purely incremental — is speculative without a detailed architectural comparison to APINNs, which neither the paper nor the reviewer provides concretely. The retained portion focuses on the paper's own contradictory framing rather than asserting the method is non-novel.

- **"VI metric is conceptually narrow and its interpretation is overstated"** (from Harsh Critic Point 2, overstatement portion): The paper explicitly and carefully describes what VI measures (subspace containment, not per-component alignment) in lines 102–104. The transparency makes the overstatement claim invalid. Only the naming issue is retained as Minor.

- **"VI cannot be applied to non-separable PDEs"** (from Harsh Critic Point 2): The paper explicitly acknowledges this limitation in the conclusion (line 212–213) and suggests future work. This is a scoped limitation, not a hidden flaw.

- **"Unfair comparison — vanilla PINN has different architecture"** (from Harsh Critic Point 4): For 5D Poisson, the vanilla PINN uses a deeper network (10 layers vs. 2), which gives the baseline more capacity — this asymmetry actually favors the baseline. For 10D Poisson, the parameter counts are matched (5392 vs. 4929). Both comparisons are fair or favor the baseline. The retained Minor point about training time is about completeness of reporting, not fairness.

- **"Generalizability beyond separable solutions not demonstrated"** (from Harsh Critic Point 5): The paper explicitly scopes its contribution to problems where dimension decomposition is applicable and acknowledges non-separable PDEs as a limitation. Criticizing a paper for not doing what it explicitly says it doesn't do is scope creep. Retained only as a Nice-to-Have suggestion.

- **"Consistent and noise-robust domain partitioning"** (from Strength Finder): Retained as a supporting detail within the domain decomposition strength rather than a standalone strength, as it mainly reinforces the main finding rather than constituting an independent contribution.

- **"No discussion of how K is chosen"** (from Harsh Critic "Missing Parts"): Retained as Minor.

- **"Missing discussion of router architecture ablation"** (from Harsh Critic): Moved to Nice-to-Haves.

## Novel Insights

The paper's most interesting insight — which is genuinely its own contribution — is that dimension decomposition and domain decomposition can be synergistically combined: the shared-MLP per-dimension factorization inside each expert keeps the expert lightweight enough that adding more experts (for domain decomposition) remains tractable. Conversely, the MoE router's soft gating naturally handles the interface between subdomains without explicit continuity losses because dimension-decomposed experts produce smooth outputs that the weighted sum blends automatically. This two-level co-design is more than the sum of its parts and is not obvious from prior work on either strategy alone.

## Suggestions

- Directly compare against APINNs on the Burgers equation, or at minimum provide a detailed architectural comparison explaining why the MoE router is substantively different from APINNs' soft gating. If the difference is that APINNs still requires a predefined partition structure while the MoE router does not, state this explicitly with evidence.

- Add a SPINNs comparison on the Poisson benchmark to substantiate the dimension decomposition claims. Even a single-table comparison would substantially strengthen the evidence.

- Provide a systematic wall-clock time and peak memory table across all experiments (not just the 10D Poisson passing mention) to support the efficiency narrative.

- Add a quantitative heuristic for selecting K (e.g., elbow method on ℓ₂ error, or when gate entropy stops decreasing) to make the method more practically usable.

## Score and Decision

**Calibration anchored comparison:**

| Anchor | Avg Score | Round | Comparison to 3D Paper |
|---|---|---|---|
| HyResPINNs (5rfj85bHCy) | 5.00 | R1 | 3D is stronger: more diverse experiments, combined decomposition strategies, compelling automatic domain decomposition visualizations |
| Ensemble/MoE DeepONets (BvMuyqPvk1) | 4.33 | R1 | 3D is stronger: automatic (not predefined) domain decomposition, plus dimension decomposition, plus interpretability metric |
| DisentangO (LXVZQpEb2y) | 5.50 | R2 | 3D is comparable or slightly stronger: more concrete demonstrations, cleaner experiments, but DisentangO has theoretical analysis |
| PIG (y5B0ca4mjt) | 6.50 | R2 | PIG is slightly stronger: better baseline comparisons, more diverse PDE benchmarks, but similar novelty level |
| BENO (ZZTkLDRmkg) | 6.60 | R2 | BENO is stronger: more complete evaluation, better baseline coverage |
| MgNO (8OxL034uEr) | 6.50 | R2 | MgNO is stronger: deeper theoretical grounding, better comparisons |
| PhyMPGN (fU8H4lzkIm) | 8.00 | R1 | PhyMPGN is clearly stronger: thorough experiments, solid baselines, strong generalization results |

The 3D paper sits between DisentangO (5.50) and PIG (6.50). It has more compelling and concrete contributions than DisentangO (automatic domain decomposition with dramatic error reduction, parameter-efficient shared MLP, quantitative VI metric), but falls short of PIG because of weaker baseline comparisons and the contradictory positioning on domain decomposition novelty. **Score: 6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>