Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual content. Let me write the consolidated review.

## Summary

The paper introduces FACTS (FACTored State-space), a recurrent state-space model that represents both latent states and inputs as sets (rows of matrices) and uses attention-based routing to assign input features to latent factors. The key innovations are: (1) a permutable graph-structured memory that is invariant to input feature permutations, (2) a linearization that substitutes the evolving memory state Z_{t-1} with the fixed initial memory Z_0 in routing computations to enable parallel training, and (3) formal proofs of left permutation equivariance (L.P.E.) and right permutation invariance (R.P.I.). Empirical evaluations cover multivariate time-series forecasting (9 datasets), object-centric video prediction (CLEVRER, MOVi-A), and traffic forecasting (METR-LA).

## Strengths

1. **Permutation invariance — both proven and empirically validated.** The paper formally defines L.P.E. and R.P.I. (Definitions 1–2) and proves FACTS satisfies both (Theorem 1). This is directly supported by the experiment in Section 4.1.2 (Figure 2), where FACTS maintains nearly unchanged prediction error under random input permutation while baseline models (iTransformer, S-Mamba) suffer 2–3× MSE degradation. This is the paper's strongest and most distinctive result.

2. **Competitive results across diverse world-modelling tasks with a single architecture.** FACTS achieves top-tier results on multivariate forecasting (best MAE on 6/9 datasets in Table 1), object-centric dynamics prediction (LPIPS of 0.09, FG-mIoU of 48.11 on CLEVRER in Table 2), and traffic prediction (MAPE of 9.08% on METR-LA in Table 3). While not uniformly state-of-the-art, the breadth of strong results supports the claim that the architecture is a versatile world model, not a narrow solution.

3. **Linearization enabling parallel computation is demonstrated.** The paper replaces Z_{t-1} with Z_0 in routing (Section 3.1, Eqs. 17–20) to break the non-linear recurrence, enabling a closed-form expansion (Eq. 19). Figure 3 shows that the parallel version maintains performance across segment sizes on the Electricity dataset, confirming the practical viability of the linearization.

4. **General theoretical framework (Theorem 2).** Theorem 2 provides a sufficient condition — L.P.E. and R.P.I. of Ā, B̄, U — under which any dynamics of the form of Eq. 10 inherit these properties. This goes beyond the specific attention-based router used and opens a design space for future permutation-invariant SSMs.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between the "dynamic factorization" narrative and the linearized implementation.** The paper motivates FACTS by arguing that existing SSMs impose rigid structural constraints, and proposes routing that "dynamically assigns input features to consistent factors" (Section 3.1, Eq. 13–16) where the routing depends on Z_{t-1}. However, in the final model (Eqs. 17–20), the routing is linearized by substituting Z_{t-1} with Z_0 — the routing functions Ā, B̄, U are computed from (Z_0, X_t), not (Z_{t-1}, X_t). This means the routing does *not* adapt based on how the memory state evolves; it is determined entirely by the fixed initial memory and the current input. The paper does not discuss the impact of this approximation on expressiveness or adaptivity, and crucially, **no ablation compares the linearized version (routing via Z_0) against a version with full state-dependent routing (routing via Z_{t-1})**. The experiment in Figure 3 ("Parallel vs. Recurrent FACTS") only varies segment window size within the Z_0-based model — it does not compare Z_0-routing against Z_{t-1}-routing. Without this ablation, the paper's narrative of "dynamic factorization" through memory-state-dependent routing is not directly supported by evidence from the model that was actually evaluated.  
   This is a significant weakness because it concerns the core architectural design choice. The paper should either: (a) reframe the contribution around a fixed-initial-memory routing and discuss what adaptivity is still achieved through input dependence, or (b) provide empirical evidence quantifying what is lost (or not lost) when routing no longer depends on the evolving memory.

2. **Unexplained handling of graph data in the METR-LA experiment.** Section 4.3 applies FACTS to the METR-LA dataset and claims "FACTS, leveraging its graph-structured memory, outperforms all existing methods." However, FACTS's formulation treats both memory and inputs as *sets* (nodes) with attention-based routing — it is not explained how the road network's *actual adjacency structure* (edges between sensors) is incorporated. The main text says only "see Appendix 4 for more experimental details" (appendix stripped). Since METR-LA baselines (e.g., graph neural networks) explicitly use the graph's adjacency, it is unclear whether FACTS uses it at all or simply treats the sensor nodes as a permutation-invariant set. This makes the comparison difficult to interpret and undermines the claim of handling "graph data" in a meaningful sense.

### Minor

3. **Imprecise prose linking theoretical analysis to the linearized model.** Lines 150–152 and 156 state that L.P.E./R.P.I. properties hold with "memory Z_{t-1} and X_t serving as the left and right arguments" and that Theorem 2's condition is about "functions of Z_{t-1} and X_t." However, the actual evaluated model (Eq. 20) uses Z_0 as the left argument, not Z_{t-1}. Theorem 1 correctly addresses the model in Eq. 20, and Theorem 2 correctly addresses the *general framework* in Eq. 10 (not the linearized model), but the surrounding prose blurs this distinction. This misalignment between the prose and the actual model is confusing and should be corrected.

4. **Unsupervised object discovery comparison uses a different training objective than SAVi.** The paper acknowledges (Section 4.2) that FACTS is trained with both reconstruction and future prediction losses, while SAVi uses only reconstruction. The claim that FACTS "outperforms SAVi" in unsupervised object discovery is thus not apples-to-apples. This is a minor issue because the paper is transparent about the difference and the comparison is supplementary to the main results, but the framing as "outperforms" overstates what can be concluded.

5. **Missing discussion of limitations.** The paper does not include a limitations section or discuss scenarios where the Z_0-based routing could be problematic (e.g., long video sequences with significant appearance changes, or tasks where the optimal routing genuinely depends on the accumulated state). Acknowledging these limitations would strengthen the paper.

### Trivial

6. **Minor prose imprecision.** Line 152 says "by taking memory Z_t and features X_t as the left and right arguments in FACTS (equation 20)" but Eq. 20 takes Z_0, not Z_t, as the left argument. (Z_t is the *output* of Eq. 20, not an input.)

## Nice-to-Haves

- An ablation comparing routing via Z_0 vs. routing via Z_{t-1} on a small-scale task (e.g., a synthetic dynamical system) to quantify the trade-off between adaptivity and efficiency.
- Clarification of how (or whether) graph adjacency is used in the METR-LA experiment, beyond treating nodes as a set.
- A discussion of the linearization's impact on expressiveness, including scenarios where it might degrade performance.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "The theoretical claims are not clearly aligned with the actual model — Theorem 2 is presented as a general result, but the experimental model does not satisfy this condition."**  
  This is partially inaccurate. Theorem 2 is explicitly about the *general framework* in Eq. 10 (the non-linear version), not about the experimental model in Eq. 20. The paper states this clearly ("it is possible to extend our results in Theorem 1 to the more general case"). The critic conflates Theorem 2's general theoretical result (which is about Eq. 10) with the experimental model (Eq. 20). The imprecision in the prose (point 3 above) is a valid minor issue, but the criticism as stated incorrectly claims the theorem's condition is unmet when in fact the theorem applies to a different, more general formulation.

- **Harsh Critic: "The single experiment in Figure 3 only varies segment window size, not whether routing uses Z_{t-1} or Z_0"** — This is factually accurate and is retained as part of Major weakness 1 (the missing ablation). The critic is correct that this experiment does not compare Z_{t-1} vs. Z_0 routing, which is the core of the weakness.

- **Harsh Critic: "Object-centric world modelling — unclear whether this is due to the FACTS architecture or just better hyperparameters / training setup"** — This is a generic criticism applicable to any empirical paper and lacks specificity. It does not identify any concrete flaw in the experimental design.

- **Strength Finder: "Principled connection to history compression"** — This is valid but generic background framing. Not a distinct technical strength. However, it's retained implicitly as part of the paper's motivation.

## Novel Insights

The reviews surface an interesting tension that goes beyond the paper's own narrative: the linearization that enables parallel computation (substituting Z_{t-1} with Z_0) is simultaneously the paper's main practical enabler and its main conceptual vulnerability. The harsh critic correctly identifies that this substitution removes the state-dependence from the routing — but what neither review fully explores is whether this matters *in practice* for the permutation invariance claim. The routing still depends on X_t, so it can still dynamically reassign input features at each time step based on the current input content. The loss is only the dependence on *what the model has accumulated in memory*. For tasks where the input itself carries the information needed for routing (e.g., which sensor reading maps to which latent factor), the Z_0 approximation may be harmless. The real question — which the paper should address — is: in which tasks does the state of the memory matter for correct routing, and how much performance is lost there?

## Suggestions

1. **Add an ablation study** comparing FACTS with Z_0-based routing vs. a version with full Z_{t-1}-based routing on a controlled task (e.g., a small synthetic dynamical system or one forecasting dataset). This directly addresses the most significant unresolved question about the architecture.

2. **Clarify the narrative** in Sections 3.1 and 3.2. Either reframe FACTS as a model with "input-adaptive, memory-fixed routing" (which is honest about what the model actually does) or provide evidence that the Z_{t-1} → Z_0 substitution incurs negligible loss. The current framing overpromises on "dynamic factorization" relative to what is implemented.

3. **Explain the METR-LA experiment** — whether graph adjacency is used, and if so, how it is incorporated into FACTS's set-based formulation. If it is not used, state this explicitly and discuss whether this makes the comparison with GNN-based baselines fair.

4. **Add a limitations section** that discusses scenarios where Z_0-based routing could be a limitation (e.g., long sequences with distribution shift, tasks where routing depends on long-term memory content).

5. **Fix the imprecise prose** about which arguments ("Z_{t-1}" vs. "Z_0" vs. "Z_t") are the left input to the FACTS function in the theoretical section.

## Score and Decision

This paper presents a novel and well-motivated architecture with a clearly demonstrated advantage (permutation invariance) and competitive results across diverse tasks. The main weakness is a gap between the motivational narrative (state-dependent dynamic routing) and the actual implementation (fixed-initial-memory routing), which is not ablated or adequately discussed. This is a significant but addressable weakness — it does not invalidate the core contribution (permutation-invariant SSM with strong empirical results) but does mean the paper's framing is somewhat overstated.

The paper is a solid contribution to the world modelling / state-space model literature. The permutation invariance result is genuinely useful, the experiments are broad, and the theoretical framework (Theorem 2) has value beyond the specific instantiation.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>