Now I have a thorough understanding of the paper and can cross-check each reviewer claim against the actual text. Let me compose the final consolidated review.

## Summary

This paper extends Off-policy Direct Advantage Estimation (DAE) to partially observable environments (POMDPs), showing that the return decomposition and the two centering constraints (for policy stochasticity via \(A\) and environment stochasticity via \(B\)) generalize naturally by replacing states with histories and integrating over observed variables \((r,o')\) instead of unobserved states. To address the computational overhead of learning a high-dimensional generative model for the \(B\) constraint, the paper proposes a discrete latent dynamics model combining self-predictive representations with a Winner-Takes-All loss (effectively a conditional VQ-VAE in embedding space), avoiding pixel-level reconstruction. The paper further identifies a confounding issue that arises when training recurrent agents with truncated trajectories and proposes a mitigation. Empirical evaluation on the ALE-5 subset shows the method is competitive with DreamerV2/V3 and, in some games, with Rainbow.

## Strengths

1. **Sound theoretical generalization of DAE to POMDPs.** Proposition 1 correctly extends the off-policy DAE objective to partially observable domains. The modification—replacing states with histories and integrating the \(B\) constraint over \((r,o')\) rather than \(s'\)—is natural and follows from the well-known reduction of POMDPs to history-based MDPs (Bertsekas, 2012). The remark about stochastic rewards (which the original MDP proof assumed deterministic) adds necessary nuance.

2. **Computationally efficient latent dynamics model.** The paper proposes a conditional VQ-VAE operating in a low-dimensional embedding space (combining SPR with a WTA loss), avoiding high-dimensional observation reconstruction. This directly targets the \(\sim 7\times\) runtime overhead reported by Pan & Schölkopf (2024). The claim that this adds "negligible computational cost" relative to the rest of the system is a practical contribution, though it would benefit from explicit timing measurements.

3. **Identification of confounding from trajectory truncation.** Section 3.2 identifies a genuine and previously underappreciated issue: when training recurrent agents on truncated sequences, the truncated portion can act as a confounder biasing value estimates. The toy example and causal graph (Figure 2) make the issue intuitive, and the experiment (Table 2) shows small but consistent performance differences across all five ALE games and two truncation lengths, suggesting practical relevance.

4. **Competitive empirical results against strong baselines.** The method (m=8) outperforms DreamerV2 in all 5 games and is comparable to or better than DreamerV3 in 4/5 games at 20M frames—while DreamerV3 uses a \(\sim 200\)M-parameter world model vs. the paper's \(\sim 50\)M-parameter model. The ablation with \(\hat{B} \equiv 0\) (Figure 3) shows that disabling the off-policy correction degrades performance and limits scalability, confirming the dynamics model contributes meaningfully.

5. **Thorough ablation studies.** The paper systematically investigates backup length (Figure 4), LSTM vs. frame-stacking (Figure 5), and latent space size \(|\mathcal{Z}|\). The finding that frame-stacking can be suboptimal compared to an LSTM with proper POMDP corrections (Figure 5) provides useful practical guidance.

## Weaknesses

### Fatal

None.

### Major

1. **Overstated claim about matching Rainbow with 10% of frames.** The paper claims "Comparisons with Rainbow also demonstrate that our method can achieve similar performance while using only 10% of the training frames." Cross-checking the numbers in Table 1: this claim holds well for Double Dunk (m=8: 17.3 vs. Rainbow: 8.5 at 200M) and Name This Game (15.5k vs. 13.9k), but is a stretch for Battle Zone (27.0k vs. 37.2k, \(\sim 73\%\)), Qbert (10.7k vs. 20.1k, \(\sim 53\%\)), and Phoenix (50.3k vs. 223.5k, \(\sim 23\%\)). In two games the method is far below Rainbow. The claim should be qualified per-game or softened to reflect that performance is mixed. The paper is more measured about the Dreamer comparisons ("comparable to DreamerV3 in 3 out of 5 environments"), which is appropriate, but the Rainbow claim overreaches the evidence.

2. **Limited evaluation scope relative to the paper's scalability claims.** The evaluation covers only 5 Atari environments. While Aitchison et al. (2023) is cited to justify this subset, the paper makes broad claims about "scalability" and "sample efficiency." The original Off-policy DAE (Pan & Schölkopf, 2024) was evaluated on the full 57-game ALE suite. Five games, even if representative, provide limited support for claims that the method is broadly scalable. The paper should either expand the evaluation or more carefully scope its claims.

### Minor

3. **The dynamics model's centering constraint is not directly validated.** The paper's central mechanism for off-policy correction relies on the learned latent dynamics model approximately satisfying \(\mathbb{E}_{(r,o') \sim p(\cdot|h,a)}[\hat{B}(h,a,r,o')|h,a] \approx 0\). The only evidence provided is the indirect ablation showing that setting \(\hat{B} \equiv 0\) degrades performance (Figure 3). While this is suggestive, it does not rule out alternative explanations (e.g., the dynamics model provides useful auxiliary supervision independent of the centering constraint). Reporting a direct metric—such as the empirical mean of \(\hat{B}\) over sampled \((r,o')\) pairs for fixed \((h,a)\), or the KL divergence between learned prior and posterior—would substantially strengthen the evidence chain. This is the single most impactful addition the authors could make.

4. **No runtime or computational cost measurements.** The paper claims the latent dynamics model adds "negligible computational cost compared to other parts of the system," and one of the paper's contributions is specifically to address the 7× runtime overhead of the original Off-policy DAE. Yet no wall-clock time, FLOPs, or parameter count for the dynamics model vs. the value network are reported. Without such measurements, this claim is unverifiable.

5. **Total loss function and training objective are not explicitly stated.** The paper describes the DAE objective \(\mathcal{L}\) (Equation 9), the reconstruction loss \(\mathcal{L}_{\text{rec}}\) (Equation 11), the KL divergence between prior and posterior (mentioned in text, line 134), and a reward reconstruction term (line 134). However, it never states how these are combined—what weighting coefficients are used, or whether they are tuned. The architectures of the "shallow MLPs" (depth, width, activation functions) are not specified. This is a reproducibility gap.

6. **Proof of Proposition 1 is a single-sentence sketch.** The appendix states: "a POMDP can be reformulated as an MDP...The theorem is then a direct result of applying Off-policy DAE to the reformulated MDP." While the logic is correct in principle, the proof is too terse; a short derivation showing that the reformulated MDP's transition probabilities and the \(B\) constraint's centering property carry over would be more appropriate for a conference paper claiming a theoretical extension. The remark about stochastic rewards confirms that the translation is not fully trivial, meriting a slightly more detailed treatment.

7. **Confounding experiment results are small in magnitude.** The paper acknowledges the effects are "small, yet consistent" (line 192), which is honest, but the differences in Table 2 appear to be mostly within one standard error. The confounding experiment is a valuable conceptual contribution from Section 3.2, but the empirical demonstration in ALE would benefit from statistical testing (e.g., paired tests across environments or more seeds) to confirm the trend is robust.

### Trivial

- Line 198 references "Section 5" for the latent space size ablation, but the results appear to be summarized in the same paragraph—likely a reference that was not updated after reorganization.
- Per-game learning curves (individual game plots) would be more informative than the aggregated curves in Figure 3, though Table 1 provides per-game final scores.

## Nice-to-Haves

- **Comparison to a simple recurrent baseline** such as DRQN with n-step returns or R2D2. This would isolate the benefit of the DAE-based multi-step correction from the recurrent architecture itself. The paper's "B=0" condition already serves as a partial ablation for the off-policy correction, and the LSTM vs. frame-stacking comparison isolates the POMDP handling, so the absence of this baseline is not a critical gap, but it would strengthen the empirical story.
- **Per-game learning curves** for the main results (Figure 3 shows aggregated curves; Table 1 only gives final scores).
- **A formal definition or table of the total loss function** with weighting coefficients.

## Removed Points

- **"No comparison to R2D2, Reactor, or DRQN with n-step returns"** from the critic's Critical Issue 1: The paper already compares against DreamerV2, DreamerV3 (both recurrent), and Rainbow. Requesting additional recurrent baselines is scope creep given the existing strong comparisons. The B=0 ablation also provides a meaningful within-method control. Moved to Nice-to-Haves.
- **"Figure 3 shows only aggregated curves"** from Other Observations: Per-game final scores are given in Table 1. Aggregated learning curves are standard; per-game curves would be a supplement. Moved to Nice-to-Haves.
- **"The paper mentions an ablation on |Z| but incorrectly refers to Section 5"** from Other Observations: This is a reference issue likely caused by paper reorganization. The parser may also have stripped a section. Removed per hard rules about parser artifacts.
- **"It is not clear whether the behavior policy is the same as the target policy"** (part of Critical Issue 5): The paper clearly states "behavior policy" in both conditions (line 192), and the distinction (behavior vs. target policy) is standard in off-policy RL. This reflects a reviewer misreading, not a paper error.

## Novel Insights

The reviewers collectively surface an important tension: the paper's strongest contribution is the clean theoretical extension (DAE → POMDPs) and the conceptual identification of the truncation confounding problem. These are well-argued and resistant to revision. The weakest link is not in the theory but in the gap between the evidence provided and the scope of the claims made—specifically, the Rainbow "10% of frames" claim overreaches, and the dynamics model's centering constraint goes unvalidated at the level of the loss function itself. The most impactful revision would not be adding more games or baselines, but adding a direct quantitative check on the \(\hat{B}\) centering error. This single addition would validate the core mechanism that everything else depends on and would make the paper's story self-contained.

## Suggestions

1. Directly report the empirical centering error of \(\hat{B}\) (e.g., mean \(\hat{B}\) over sampled \((r,o')\) for fixed \((h,a)\) during training, or the average violation of \(\mathbb{E}[\hat{B}] \approx 0\)) and show that it converges to a small value. This would validate the mechanism that the entire method hinges on.
2. Qualify the Rainbow comparison per-game rather than as a blanket statement.
3. Include wall-clock timing measurements or FLOP comparisons to support the "negligible computational cost" claim.
4. Provide the total loss function (with weighting coefficients) and the exact MLP architectures in an appendix.
5. Add a brief derivation in the proof of Proposition 1 showing how the \(B\) constraint's centering property in POMDPs follows from the history-MDP reduction, explicitly handling the stochastic reward case.

## Score and Decision

This paper makes a sound theoretical extension and identifies a practically relevant confounding issue. The empirical evaluation, while limited to 5 games, shows competitive results against strong baselines (DreamerV2/V3). The primary weaknesses are overclaimed results against Rainbow, lack of direct validation of the dynamics model's centering constraint, and missing implementation details. None of these are fatal—they are addressable with additional analysis and more careful phrasing. The paper represents a meaningful step forward for multi-step off-policy value estimation in POMDPs.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>