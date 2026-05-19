Now I have verified all key claims directly from the paper. Let me write the final consolidated review.

---

## Summary

Secure-FLOATING proposes a decentralized framework that combines Verifiable Federated Learning (VFL), lightweight addition-based Secure Multi-Party Computation (SMPC), and blockchain consensus to enable real-time, privacy-preserving trust validation of mobility data from connected and autonomous vehicles (CAVs). The paper provides a problem motivation, a high-level architecture with a six-step workflow, a toy example of additive secret sharing, and two theoretical claims (differential privacy and linear scalability). However, the paper's core empirical evidence — the experimental evaluation — is entirely absent, and its theoretical analysis is broken and incomplete.

## Strengths

- **Well-motivated, important problem.** The paper addresses a genuine challenge: real-time validation of trajectory data from CAVs and vulnerable road users in a privacy-preserving, decentralized manner, where malicious data could have deadly consequences. The signal-less intersection scenario (Section 1) is compelling and clearly articulated.

- **Concrete architectural proposal with a clear workflow.** The paper defines a six-step protocol (Section 3.3, Steps 1–6) that connects trajectory exchange, local prediction, comparison-based endorsement, SMPC-based model update splitting/sharing, distributed ledger update, and majority-vote consensus. This provides a concrete instantiation of the proposed architecture.

- **Toy example illustrating the addition-based SMPC mechanism.** Section 3.2 provides a worked example with three nodes sharing distance values, showing how additive secret shares are generated, distributed, summed, and reconstructed. This helps communicate the core idea of the SMPC approach.

## Weaknesses

### Fatal

- **Experimental evaluation is completely absent.** Section 5 ("Experimental Evaluation") consists of a heading (line 159) followed by blank lines and then the next section heading (line 163). There is no description of experimental setup, methodology, metrics, baselines, results, tables, or figures. The abstract claims specific quantitative performance (e.g., "up to 75% successful endorsement for as high as 50% attacker penetration," evaluation on "up to 8,000 nodes… in New York City"), and the conclusion asserts "extensive evaluation based on real-world data from New York City." Yet not a single result, comparison, or experimental detail appears anywhere in the paper. This is not a minor omission — it is the absence of the primary evidence that an empirical methods paper must provide. The paper's central claims are therefore unsubstantiated.

### Major

- **Theorem 4.1 (privacy guarantee) has no proof.** The theorem asserts (ε,δ)-differential privacy for the SMPC aggregation protocol, but the proof is simply "Proof.1)" (line 147) — a placeholder with no content. No derivation of ε or δ, no connection to the protocol, no justification. The privacy claim is asserted but not supported.

- **Theorem 4.2 (scalability analysis) is internally inconsistent.** The theorem derives the communication overhead as f(n) = 2n−1 (line 149), derived from (n−1)+(n−1)+1. However, the induction proof (lines 153–157) attempts to prove f(n) = 3n−2. The base case, inductive hypothesis, and inductive step all use 3n−2, not 2n−1. The function being proven differs from the function derived; the proof assumes what it attempts to prove (f(k+1)=f(k)+3 is tautological given the closed-form); and the induction is trivial algebraic manipulation, not a genuine proof of scalability. This undermines the paper's central claim of provable linear scalability.

- **Zero-knowledge proofs (ZKPs) are claimed but never specified or integrated.** The introduction (line 16) and conclusion (line 177) invoke ZKPs as a "trust-but-verify" mechanism. However, the actual protocol workflow (Steps 1–6, lines 127–141) describes only SMPC-based aggregation — no ZKP appears. How ZKPs verify model updates, what statements are proved, or how they interact with the SMPC and consensus steps is never defined.

- **The SMPC-to-gradient mapping is critically underspecified.** The paper illustrates SMPC with a toy example where three nodes share scalar distance values (lines 119–121). However, the actual protocol is supposed to aggregate model parameter vectors (gradients). It is unclear how secret shares are generated from high-dimensional gradient vectors, how they are distributed among n nodes without O(n²) communication, how the protocol handles node dropouts, and how reconstruction works. The share generation is described only for scalars.

- **The trajectory prediction model — central to the validation mechanism — is left unspecified.** The paper states, "We leave the choice of the prediction algorithm open" (line 115). The entire trust validation depends on a model that predicts neighboring nodes' future trajectories and compares them to shared trajectories. Without specifying what this model is (a supervised predictor? anomaly detector? what are its inputs, outputs, and architecture?), the core mechanism remains abstract. Claiming the framework is "independent of the underlying prediction algorithm" does not resolve this — the feasibility and real-time performance of the framework depend critically on the model's complexity.

### Minor

- **The scalability induction proof adds no substantive evidence.** Even aside from the 2n−1 vs. 3n−2 inconsistency, the induction step simply rearranges the closed-form expression to show f(k+1) = f(k)+3. This is not a proof of O(n) scaling — it assumes the closed-form and trivially manipulates it. A simple counting argument (2n−1 is already O(n) by inspection) would be more appropriate than a defective induction.

- **The paper overclaims novelty.** It claims to be "the first" to address real-time CAV data validation (Section 2, line 20), but the related work section surveys only adjacent approaches without concretely demonstrating how Secure-FLOATING improves upon the closest methods (e.g., FedShare [9], practical secure aggregation [5]) in measurable terms.

### Trivial

None.

## Nice-to-Haves

- Provide latency analysis against real-time requirements (e.g., 100ms V2X communication latency targets).
- Address intermittent connectivity and dynamic network topology — currently the protocol assumes all nodes are in range and send messages reliably.
- Include comparison baselines (e.g., plain FL without SMPC, centralized reputation, pure blockchain-based trust) to substantiate claimed advantages.
- Analyze computation cost (FLOPs) of share generation/summation/reconstruction for realistic model sizes.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: "Missing baselines"** — Kept above as nice-to-have, not a core weakness, since the missing experiments are the fatal issue, not missing baselines within an absent evaluation.
- **Harsh critic: "Missing complexity analysis for SMPC in terms of FLOPs"** — Moved to nice-to-have. Requesting this level of analysis goes beyond standard practice for a framework paper where the communication complexity (which is analyzed, albeit defectively) is the primary scalability concern.
- **Strength Finder: "Provably linear communication overhead"** — Removed because the verified weakness shows the proof is broken/inconsistent; a strength that conflicts with a verified weakness cannot stand.
- **Strength Finder: "Large-scale realistic evaluation with quantitative results"** — Removed because the evaluation section is entirely absent; the abstract claims results but the paper provides no evidence. This strength references unsubstantiated claims, not verified content.
- **Strength Finder: "Novel integration of VFL, lightweight SMPC, and blockchain"** — Weakly kept in spirit under Strengths as "architectural proposal," but the strength-finder's framing as a validated contribution is dropped since novelty claims are unsupported by experiments.
- **Any criticism about missing appendix content, missing references, or formatting/typo issues** — Removed per instructions: these are either parser artifacts or outside scope.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely re-state the same observations: the reviews converge on the missing experiments, broken proofs, and underspecified method as the core problems, but neither offers a genuinely novel analytical insight beyond what is directly visible from reading the paper.

## Suggestions

1. **Provide a complete experimental evaluation.** This is non-negotiable for publication. Include: experimental setup (simulation environment, dataset, number of nodes), metrics (validation delay, endorsement accuracy vs. attacker ratio, communication overhead scaling), ablation studies, and comparison against at least one baseline (e.g., plain FL, centralized trust, or pure blockchain). The abstract's claimed numbers (75% endorsement at 50% attacker penetration) must be reproducible from the evaluation.

2. **Fix the theoretical analysis.** Either provide a rigorous differential privacy proof with explicit ε,δ derivation, or drop the privacy guarantee claim and state the protocol's privacy properties qualitatively. Replace the broken induction proof with a straightforward counting argument — f(n)=2n−1 is O(n) by inspection; no induction is needed.

3. **Specify the SMPC-to-gradient mapping.** Show concretely how gradient vectors (which may have millions of parameters) are split into additive shares among n nodes. Describe the communication pattern (all-to-all, ring, or other) and how share distribution avoids O(n²) overhead. Address dropout and malicious node handling.

4. **Specify the prediction model or bound its complexity.** The framework's real-time feasibility hinges on the model's inference latency. Either fix a concrete model (e.g., a lightweight LSTM or linear predictor) and evaluate its performance, or provide a formal bound on the complexity of models the framework can support.

5. **Remove or integrate the ZKP claim.** If ZKPs are genuinely used, describe the proof statement, the proving protocol, and how it integrates with Steps 1–6. If they are not implemented, remove all references to ZKPs.

---

## Score and Decision

The paper has a fatal flaw: the experimental evaluation is entirely absent, leaving all empirical claims unsubstantiated. Even setting this aside, the theoretical analysis is broken (inconsistent proofs, absent privacy proof) and the method is critically underspecified (SMPC-to-gradient mapping, ZKP integration, prediction model choice). The motivation and architectural framing are reasonable, but a motivated scenario does not constitute a publishable contribution. The paper cannot be accepted in its current form.

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>