- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 3, 6, 8
Now I have a thorough understanding of the paper and all the reviewer claims. Let me synthesize the final review.

## Summary

This paper introduces LTSGNS, which combines non-amortized Bayesian meta-learning (GMM-based task posterior inference via SEMTRUX) with Probabilistic Movement Primitives (ProDMPs) for mesh-based physical simulation. The core idea is to infer latent task descriptors encoding unknown material properties from a small set of observed simulation states (the context set), then use those descriptors to condition a graph network that predicts full node trajectories via ProDMP weights in a single forward pass rather than autoregressive rollouts. The method is evaluated on two deformable-object simulation tasks (2D plate and 3D tissue manipulation) against MGN baselines.

## Strengths

- **Explicit Bayesian meta-learning formulation for GNS**: Section 3 (Eqs. 4–9) rigorously defines a probabilistic model where a latent task descriptor $\bm z_l$ encodes unknown material properties, with an expressive GMM-based variational posterior fit via SEMTRUX. The architecture integration — concatenating the latent $\bm z_l$ to per-node MPN features — is clearly described and principled.

- **ProDMPs as an architectural solution to error accumulation**: Instead of iterative next-step prediction, the model outputs node-wise ProDMP weights $w \in \mathbb{R}^W$ that define the full trajectory, which can be queried at arbitrary timesteps. This is a concrete, end-to-end trainable departure from standard autoregressive GNS and directly addresses the error-accumulation problem the paper identifies.

- **Demonstrated context flexibility with point clouds**: The paper shows that LTSGNS can use point clouds (as opposed to full mesh states) as context during inference without any retraining (lines 203–205). The results in Figure 4 show that even with point-cloud context, LTSGNS outperforms MGN, which is practically relevant for real-world settings with depth cameras.

- **Quantitative results show LTSGNS outperforms MGN(M) with sufficient context**: On the Deformable Plate task, LTSGNS with 10 context points outperforms MGN(M) — a baseline with direct access to ground-truth material properties (line 211). This is a strong result that supports the claim that the method can infer unknown system properties from context.

- **Two complementary tasks and multiple baselines**: The evaluation includes a 2D and a 3D task, with baselines MGN, MGN(M) (with material info), and MGN(MP) (ProDMPs alone). The experimental design allows partial attribution of gains.

## Weaknesses

### Fatal
None.

### Major

- **Probabilistic predictions claimed but not probabilistically evaluated**: The paper states in the abstract, introduction, and conclusion that the model "handles uncertainties," produces "distributions over trajectories," and enables "accurate probabilistic predictions" (lines 8, 34, 230, 234). Yet the quantitative evaluation uses only deterministic accuracy metrics — Rollout MSE and Last Step MSE (line 182). There is no evaluation of the predictive distribution: no negative log-likelihood, no calibration curves, no coverage tests, and no comparison of uncertainty estimates against baselines. This is not fatal to the core accuracy claims, but it means a benefit that the paper explicitly advertises is completely unvalidated. The reader cannot tell whether the task posterior is well-calibrated, overconfident, or useless.

### Minor

- **Missing ablation that cleanly isolates the meta-learning component**: The paper includes MGN(MP) (MGN + ProDMPs) as a baseline, which provides partial evidence. However, this baseline uses the MGN architecture rather than the LTSGNS architecture without the latent variable. An ablation that removes the latent task variable and posterior inference from LTSGNS (while keeping the same message-passing architecture and ProDMP output) would cleanly quantify the benefit of the meta-learning component. The comparison between LTSGNS and MGN(MP) conflates architecture differences with the presence/absence of meta-learning.

- **Point cloud encoding unspecified**: The paper claims that using point clouds as context "requires no modifications to the existing training process" (line 205) but does not specify how point clouds are converted to graph features or registered to the mesh. Without this detail, the point cloud experiment cannot be reproduced or fully assessed.

- **Key hyperparameters not reported**: The dimension of the latent variable $Z$, the number of GMM components $K$, and the number of ProDMP basis functions $W$ are all missing from the experimental section. These are needed for reproducibility.

- **Computational cost of per-task inference not reported**: The non-amortized GMM-TRNGVI procedure requires per-task optimization during inference. The paper does not report how long this takes relative to a forward pass of MGN, which is relevant for practical applications (e.g., robotics).

### Trivial
- The placeholder sentence "Here, we show how good LTSGNS is." (line 223) appears to be a parser artifact rather than an author error — ignore.

## Nice-to-Haves

- Evaluate probabilistic predictions (NLL of held-out timesteps under the predictive distribution, calibration plots) to validate the uncertainty-handling claims.
- Report per-task inference wall-clock time.
- Analyze reconstruction error vs. number of ProDMP basis functions to characterize the approximation-error / error-accumulation tradeoff.
- Report latent dimension $Z$ and GMM component count $K$.

## Removed Points

These points from the reviewers were removed or demoted with justification:

- **"Practical relevance of the context set" criticism (Harsh Critic Critical Issue 3)**: The critic argues that if one can collect 5–10 states from a trajectory, one could also estimate material properties via system identification. This is speculative — the paper does not claim that system identification is impossible, nor does it scope out that alternative. The comparison against MGN(M) (given ground-truth properties) is a valid and challenging baseline. The critic also claims the paper reads as if meta-learning enables generalization across entirely different objects — the paper's experimental scope (deformable objects with unknown Poisson's ratio) is clearly stated. **Removed**: speculation not grounded in the paper.

- **"Confounded contribution" framing as a critical/fatal issue (Harsh Critic Critical Issue 2)**: The critic argues this is a decisive gap. In reality, the paper does include MGN(MP) as a ProDMP-only baseline, which provides evidence that ProDMPs alone do not account for the gains. The missing controlled ablation is real (see Minor weakness above), but the framing as a "confounded contribution" that undermines the paper is overstated. **Demoted** from critical to Minor.

- **Missing related works**: The reviewer guidelines instruct me not to mention missing related works, as I cannot verify their existence. **Removed**.

- **Statistical rigor / significance testing criticism**: The paper reports mean and standard deviation over 5 seeds, which is standard practice in this field. Requesting formal significance tests is a reasonable suggestion but not a weakness. **Demoted** from weakness to Nice-to-Have.

- **Trajectory length and ProDMP capacity analysis**: The critic asks for reconstruction error vs. number of basis functions. This is a reasonable extension but goes beyond what is standard for an experimental section. **Demoted** to Nice-to-Have.

- **Figure rendering criticism**: The critic notes that figures are referenced but not rendered in the extracted text. This is a parser artifact, not an author error. **Removed**.

- **"Strengthening the Paper on Its Own Terms" suggestions**: These are constructive suggestions rather than actual weaknesses of the paper. The concrete ones (probabilistic evaluation, ablation, point cloud encoding) are already captured above.

- **Strength Finder generic strengths**: The strengths "Controlled experimental design with two distinct tasks and multiple baselines" and "Qualitative results in Figure 3 illustrate..." are kept as they are grounded in the paper. The strength "Quantitative results show LTSGNS outperforms MGN(M)" is concrete and well-supported — kept.

## Novel Insights

Neither the reviews nor my own analysis surfaced any genuinely novel insight beyond the paper's own contributions. The paper makes a sensible combination of existing ideas (non-amortized Bayesian meta-learning + ProDMPs) applied to a new domain (mesh-based GNS), and the key finding — that meta-learning from a few context states can match/exceed a baseline given ground-truth material properties — is significant but expected given the capabilities of the underlying methods.

## Suggestions

1. Add probabilistic evaluation metrics (negative log-likelihood of held-out timesteps, calibration curves) to validate the uncertainty-handling claims. This is the most impactful single addition.
2. Report the missing hyperparameters: latent dimension $Z$, number of GMM components $K$, and number of ProDMP basis functions $W$.
3. Add a controlled ablation: LTSGNS without the latent variable (same architecture, trained without meta-learning) to isolate the benefit of the task posterior.
4. Specify the procedure for encoding point clouds into the graph — this is essential for reproducibility.
5. Report per-task inference time to contextualize the computational cost of non-amortized inference.
