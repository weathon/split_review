- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3
I have all the information I need. Let me now produce the consolidated review.

## Summary

This paper introduces SubgoalXL, a framework for formal theorem proving in Isabelle that combines subgoal-based proofs (structuring proofs as intermediate subgoals) with an iterative expert learning procedure. The method trains formal statement, proof, and subgoal generators, using a reward based on reconstruction likelihood (how well a posterior subgoal generator can recover subgoal proofs from generated formal proofs). The system achieves 56.1% on miniF2F-test (a 4.9% absolute improvement over Lyra) using Llama-3-8B, a smaller base model than many prior works.

## Strengths

- **State-of-the-art performance with a smaller base model**: Table 1 shows 56.1% on miniF2F-test using Llama-3-8B, surpassing methods using GPT-4 (Lyra: 51.2%) and Codex (DSP: 39.3%). The improvement is achieved with a smaller-scale base model, which is noteworthy.

- **Clear ablation confirms subgoal component is critical**: Table 2 shows removing subgoal-based proofs drops performance from 46.3% to 34.8% on miniF2F-valid (at equal search budget 64), directly attributing a substantial margin to the subgoal-based strategy.

- **Monotonic iterative improvement demonstrated**: Figures 3–5 document consistent pass-rate gains over three iterations (test accuracy: ~51% → ~56%; valid accuracy: ~58% → ~62%). This provides evidence that the iterative refinement process adds value.

- **Detailed error analysis**: Figure 6 quantifies ten distinct error types (~1.5M outer syntax errors, ~127k unproven goals, ~125k undefined facts, etc.), offering a concrete diagnostic for where the model fails and enabling targeted future improvements.

- **Subgoal-based proofs outperform informal proofs in a case study**: Figure 7 shows a concrete example where the subgoal-based approach succeeds while multiple informal-proof attempts fail, qualitatively validating the motivation for replacing informal proofs with subgoal-structured ones.

## Weaknesses

### Fatal

None.

### Major

- **The practical sampling procedure for the optimal distributions is underspecified (reproducibility gap).** The paper derives optimal distributions (Eq. 2 and analogous) that involve intractable partition functions summing over all possible (S,P) or g. The algorithm box repeatedly states "Sample ... according to Eq." but never specifies how this sampling is implemented — rejection sampling, importance weighting, Gumbel-softmax, or some approximation. Since this is the core mechanism connecting the probabilistic objective to the actual data used for training, the method cannot be fully reconstructed from the paper as written. This is the most significant barrier to the paper's contribution being properly evaluated.

- **No ablation isolates the expert learning component from the subgoal contribution.** The only ablation (Table 2) removes subgoal-based proofs entirely. There is no experiment that keeps subgoal proofs but ablates the expert learning loop (e.g., comparing initialization-only vs. one vs. three iterations at the same search budget). The iterative plots (Figures 3–5) show improvement over iterations, which is suggestive, but the reinitialization from base weights each iteration (Section 3.3 point 2) means improvements conflate data augmentation (more data each round) with the learning dynamic. A cleaner comparison — e.g., running the full pipeline but stopping after initialization and comparing at the same 16,384-attempt budget — would substantially strengthen the claim.

- **Uneven compute/search budget confounds method comparison with baselines.** SubgoalXL uses an ensemble of 16 separately-trained models generating 16,384 proof attempts per test problem (512 per model × 2 conditions × 16 models). None of the reported baselines (DSP, LEGO-Prover, Lyra, Subgoal-Prover) are described as using comparable search budgets or model ensembles. The paper does not report total GPU-hours for training or inference, making cost-normalized comparison impossible. This does not invalidate the empirical result, but it means the reader cannot tell how much of the 4.9% gain over Lyra comes from the algorithmic innovation vs. the substantially larger search/ensemble budget.

### Minor

- **Reinitializing from base Llama-3-8B weights at each iteration** (rather than continuing from the previous iteration's checkpoint) is an unusual design choice that is mentioned but not justified. It means the "iterative refinement" is not refining a single model trajectory but retraining from scratch on augmented data each round. The improvement could reflect better data quality from a stronger generator rather than model refinement; this should be discussed.

- **No variance or confidence intervals reported for any result.** For a stochastic task where pass rates vary across runs and random seeds, single point estimates limit the reader's ability to assess significance. This is a common standard in the field but worth noting.

- **The formal statement distribution and subgoal proof distribution equations** (referenced as Eq. \ref{eq:formal_statement_dist} and \ref{eq:subgoal_proof_dist} in Algorithm 1) are not displayed in the paper body, making the algorithm's specification incomplete even at the schematic level.

### Trivial

- The description of hardware ("single SN20 node," "4 SN40 nodes") uses non-standard cluster identifiers that are not self-explanatory to most readers; translating to GPU-hours or standard GPU types would aid reproducibility.

## Nice-to-Haves

- The paper could discuss why the posterior subgoal generator's reconstruction likelihood is a meaningful reward for formal proof quality. While the proof verification ensures correctness, the connection from reconstruction fidelity to proof quality could be made more explicit.
- A discussion of why 185k of the 195k formal proofs are discarded during the expert learning phase (only 10k retained from the HOL library) would help readers assess the data selection strategy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Comparison unfair because different base models (GPT-4 vs 8B)"** — Removed because the critic's framing is factually inverted: SubgoalXL uses Llama-3-8B, which is substantially *smaller* than the GPT-4 and Codex used by baselines. If anything, the comparison disadvantages the proposed method on model scale, making the result more impressive, not less.

- **"Eq. (1) is circular"** — Removed as factually incorrect. The objective is a standard KL-constrained expected reward optimization (analogous to RLHF/PPO formulations). The expectation is over the distribution being optimized, and the KL is against the previous iteration's distribution. This notation is standard and well-defined.

- **"Proof could be logically wrong but get high reconstruction likelihood"** — Removed because all proofs must pass Isabelle's verification, which guarantees logical correctness. The concern about reward tautology is partially valid (see Nice-to-Haves) but the specific claim about logical invalidity is not.

- **"Problem formalization conflates informal proof p and subgoal proof g"** — Removed; the paper clearly distinguishes them (p = informal proof, g = subgoal-based proof) and they serve different roles in the framework.

- **"No open-source code release"** — Removed per guidelines; the paper does not promise release, and criticizing its absence is a reproducibility request rather than a flaw in the technical contribution.

- **"Outer syntax error is basic failure mode that should be addressed"** — Removed; reporting error types transparently is a strength, not a weakness. The paper is not required to solve the errors it diagnoses.

- **"Missing related work distinctions"** — Removed as too vague to be actionable.

- **"Data scarcity claim undercut by 195k formal + 18k informal pairs"** — Removed; 195k formal proofs is modest by modern pre-training scales, and the paper is discussing scarcity of *aligned human-generated* demonstration data for theorem proving specifically, not raw text.

## Novel Insights

The most interesting observation that emerges from these reviews is the tension between the paper's framing as "expert learning" (suggesting a model improving itself iteratively through a learning dynamic) and the actual design choice of reinitializing from base weights each iteration. This means the iterative gains come from the quality of the *generated training data* improving each round rather than from a model refining its own weights over time. Framed as a "data augmentation through iterative filtering" strategy rather than "expert learning," the contribution would be cleaner and more accurately described. This reframing would also clarify why the underspecified sampling procedure matters less — if the key innovation is the subgoal-structured data generation pipeline and the multi-model ensemble, the theoretical framework around optimal distributions could be simplified.

## Suggestions

1. **Specify the practical sampling procedure.** Clarify how samples are drawn from the optimal distributions in Eqs. (2) and analogous. If rejection sampling is used, report acceptance rates and computational cost. If a simpler approximation is used (e.g., using the current model without reweighting), state that explicitly.

2. **Add an ablation that isolates expert learning from subgoal.** Report results at the full 16,384-attempt budget for: (a) initialization only (iteration 0, no iterative refinement), (b) one iteration, and (c) three iterations. This would directly measure the marginal value of expert learning.

3. **Report total GPU-hours** for training (all 16 models across all iterations) and inference (16,384 attempts × 244 test problems). This would enable cost-normalized comparisons.

4. **Display the missing equations** for the formal statement and subgoal proof distributions (currently referenced but absent), or clarify that they are structurally analogous to Eq. (2).

5. **Add a discussion of the reinitialization design choice** — justify why base-weight reinitialization is used, or acknowledge that gains reflect data quality improvements rather than weight refinement.
