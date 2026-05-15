Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper challenges the prevailing assumption in continual learning that the multitask objective (minimizing forgetting) is universally optimal. It formalizes this through a theoretical analysis in convex linear regression, proving the existence of a finite critical task duration beyond which a single-task agent that forgets everything can outperform a multitask agent. Empirically, it compares idealized ST and MT agents across CLEAR, MD5, and ML10 benchmarks, finding that MT is suboptimal on the latter two. It also proposes heuristic instability measures and a proof-of-concept Selective Replay method that adapts its objective based on instability.

## Strengths

- **Formal proof of MT suboptimality in a tractable setting**: Theorem 4 guarantees the existence of a finite critical task duration \(\bar{h}\) such that when instability \(\Delta_T^I > 0\), the single-task agent achieves lower average lifelong error than the multitask agent. This goes beyond prior intuition (e.g., Wołczyk et al., 2021; Wu et al., 2023) by establishing a formal condition under which forgetting is provably beneficial.
- **Diverse empirical validation of the phenomenon**: Table 1 shows that on MD5 and ML10 (high interference) the ST agent outperforms MT in lifelong average performance, while on CLEAR (smooth shift) the reverse holds. This confirms the core claim is not a theoretical artifact but manifests on concrete benchmarks with different types of distribution shift.
- **Controlled experiments linking instability to critical task duration**: The Permuted CIFAR experiments (Figure 3) systematically vary permutation strength (PC-16 vs PC-32) and show that higher instability lowers the critical task duration, as predicted by the theory — providing a clean causal validation.
- **Introduction of practical instability measures**: Two heuristic approximations of \(\Delta_T^I\) for non-convex settings are proposed (Table 4), and they align with the observed performance differences across benchmarks. This offers a potential tool for predicting when forgetting may be beneficial, even though the measures remain heuristic.

## Weaknesses

### Fatal
None.

### Major

- **The empirical evaluation uses idealized ST/MT agents rather than actual CL algorithms, leaving a key claim unvalidated.** The paper argues that "most methods aimed at solving catastrophic forgetting... effectively employ objectives which approximate the multi-task objective" and later calls the MT agent a "CL agent with minimal catastrophic forgetting." However, the empirical section compares only the two idealized extremes (perfect forgetting vs. perfect multitask), not any actual CL method (e.g., EWC, ER, SI, GEM). Whether real CL methods behave more like MT or ST — or somewhere in between — is asserted but never tested. The paper would need at least one experiment comparing an actual CL algorithm against both ST and MT to substantiate its relevance to CL practitioners.

- **ML10 directly contradicts Corollary 3's monotonicity prediction without resolution.** The paper states: "on the ML10 benchmark ... the reward difference does not decay with \(h\)" (line 138), and the offered hypothesis ("inherent noisiness of the reward signal") is untested. This is a significant deviation from the theory's predictions in a benchmark where ST outperforms MT — precisely the setting the theory is meant to characterize. Without analysis of why the monotonicity fails, confidence in the theory's generalizability to RL settings is substantially weakened.

- **The Selective Replay demo assumes oracle knowledge of instability and does not validate online estimation.** The paper acknowledges that "crucial to the success of selective replay... is the information regarding the tasks sequence instability - which in the case of this experiment is assumed to be known" (line 184). The paper presents this as a "demo" and calls online estimation "future work," but the title and abstract (which "argue for the utility of estimating the distributional drift") imply a practical contribution that is not delivered. Without at least a preliminary attempt at online estimation, the paper's central practical takeaway remains hypothetical.

### Minor

- **The instability measures for non-convex settings are heuristic and unvalidated against the theoretical quantity.** Option 1 can be negative (Table 4, CLEAR), which is inconsistent with its role in the decomposition. Option 2 (transfer matrix) is always positive by construction. Neither is shown to correlate with the true \(\Delta_T^I\) (which is not computable in non-convex settings). The paper uses them as supporting evidence but does not establish their reliability.

- **The theoretical result is limited to convex linear regression with strict assumptions (Assumption 2: strictly convex, no overparameterization, noiseless).** The paper is transparent about this, and the note on overparameterization (adding a regularizer) is not analyzed. This is a limitation rather than a flaw, but it confines the rigorous theoretical contribution to a narrow regime.

- **Table 2's caption ("closes the gap") appears to contradict the text's statement that the gap does not decay on ML10**, which may confuse readers (though the text is the more authoritative source).

### Trivial
None.

## Nice-to-Haves

- An ablation comparing ST/MT to at least one concrete CL algorithm (e.g., Experience Replay) on the same benchmarks would greatly strengthen the paper's relevance.
- A simple online heuristic for estimating instability (e.g., tracking validation loss changes across task boundaries) would make the Selective Replay idea actionable rather than a future-work sketch.
- A scatter plot or regression showing how the heuristic instability measures (Option 1, Option 2) correlate with the actual \(\Delta_T\) across multiple random seeds or benchmarks would add rigor.

## Removed Points

- **"The paper's central claim is not novel"**: The paper cites prior works (Kumar et al., 2023; Wu et al., 2023) and its contribution is the formalization and characterization, not the raw observation. Novelty critiques that ignore this framing are removed.
- **"ST agent may use less total computation"**: Both agents use \(h\) steps per task — computation is matched by design. Removed as factually incorrect.
- **"The paper does not specify architecture details for Permuted CIFAR"**: This is a trivial presentation detail that can be addressed in camera-ready.
- **"Missing definitions due to parsing"**: These are parser artifacts, not author omissions.
- **"Pure formatting/style nitpicks"**, **"missing appendix/proofs"**: Removed per parser-artifact and formatting rules.
- **Strength about "Selective Replay outperforms ST and ER"**: This strength conflicts with the verified weakness that SR uses oracle knowledge, so it is downgraded per instructions.

## Novel Insights

None beyond the paper's own contributions. The paper's decomposition of \(\Delta_T\) into a term controlled by the agent (\(\Delta_T^{ST}, \Delta_T^{MT}\)) and an agent-independent instability term (\(\Delta_T^I\)) is clean and provides a useful conceptual framework. However, the reviews do not surface a novel observation beyond what the paper itself presents.

## Suggestions

1. Add an experiment comparing at least one real CL method (e.g., Experience Replay with a fixed buffer) against both the ST and MT agents on the CLEAR and MD5 benchmarks. This would ground the claim that "most CL methods approximate the MT objective" and show whether the MT abstraction is a reasonable proxy.
2. Investigate why the ML10 results violate the monotonicity prediction of Corollary 3. Is it reward noise, non-convexity, or a different phenomenon? A controlled toy RL experiment (e.g., with a linear model) would help isolate the cause.
3. Provide a simple online estimator of instability (e.g., the change in held-out loss between consecutive tasks) and evaluate its correlation with the offline measures. Even a negative result would be informative.

## Score and Decision

The paper makes a clean theoretical point and backs it with reasonable empirical evidence across diverse benchmarks. The core weakness is the gap between the idealized ST/MT agents used in the evaluation and the paper's claims about real CL algorithms — a gap that is neither bridged by experiments nor resolved by the oracle-based Selective Replay demo. The ML10 contradiction further weakens the claimed generalizability. These are significant but not fatal; the paper's formalization and empirical demonstration of *when* MT can be suboptimal is a useful contribution to the CL community's understanding, even if the practical implications remain unrealized.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>