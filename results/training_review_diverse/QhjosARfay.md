Now I have all the information needed. Here is my synthesized final review.

---

## Summary

This paper identifies a genuine gap in tool-integrated math LLMs: existing models rely on externally dictated instructions for whether to use chain-of-thought reasoning or code execution. The authors propose AutoCode4Math, an EM-inspired training framework that treats methodology selection as a latent variable, enabling models to autonomously develop their own selection strategy through self-exploration and self-refinement. The practical implementation uses offline data synthesis (Self-Exploratory and Self-Reflective) combined with off-policy RL, achieving substantial empirical gains: on DeepseekMath-7B, MATH accuracy improves from 45.04% to 65.28% while code executions drop by 65%, and similar gains hold across Llama-3.1 and Qwen2Math families.

## Strengths

- **Identifies a meaningful and previously under-explored gap**: The paper clearly articulates that current tool-integrated math LLMs use externally dictated methodology selection, which cannot adapt to each model's unique strengths (abstract, lines 4–5, 16–18). This is a genuine limitation the paper addresses head-on.

- **Proposes a creative EM-inspired framework that addresses the lack of supervision**: Treating methodology choice as a latent variable and deriving an ELBO-based iterative refinement procedure is a clever and principled approach to a setting where no direct methodology-selection labels exist (Section 2.2, Eqs. 3–6). The two-step alternation between self-exploration (E-step) and self-refinement (M-step) is well-motivated and conceptually clean.

- **Substantial and well-documented empirical gains**: Across three model families (Llama-3.1, Qwen2Math, DeepseekMath), the method delivers large accuracy improvements with simultaneous reductions in code execution (Table 1). The nearly 20-point gain on MATH for DeepseekMath (45.04% → 65.28%) and 90% reduction in code usage on GSM8K are impressive and clearly presented.

- **Controlled ablations validate key design choices**: The ablation removing the EM formulation (reducing to standard RL) shows clear degradation in both accuracy and code-efficiency (Table 2, Figure 3). The ablation removing Self-Reflective Synthesis (NO REFL) similarly confirms the importance of multi-round data. These controlled experiments directly support the paper's claims about which components matter.

- **Mechanistic analysis provides nuanced insight**: The alignment rate analysis (Section 3.3, Figure 4) offers a fine-grained understanding of what the model learns — including the honest acknowledgment that MisAlign cases still contribute to accuracy through improved solution generation — going beyond surface-level accuracy numbers.

## Weaknesses

### Fatal

None.

### Major

1. **Theoretical overclaiming: monotonic improvement guarantee does not apply to the implemented algorithm.** The paper states that the EM framework "exhibits favorable properties, such as monotonic improvement of the objective function" and presents an inequality suggesting "a guaranteed progression toward better performance" (line 86–87). This guarantee holds for *exact* EM updates. The practical implementation, however, uses: (a) a hard-max reference strategy (α=∞) instead of the true posterior; (b) off-policy RL with clipped importance ratios (Eq. 7) and query-wise reward whitening instead of exact M-step maximization; and (c) a joint training scheme that mixes SFT and RL objectives. These are substantial departures, and the theoretical guarantee does not transfer. The paper acknowledges implementation challenges (Section 2.3) but never qualifies the monotonic improvement claim. The method should be evaluated on its own merits as a heuristic training procedure rather than being presented as a rigorously grounded EM algorithm with convergence guarantees.

2. **The comparison between EM and standard RL (Table 2, Figure 3) is not fully specified.** The paper says the standard RL baseline "employ[s] an off-policy RL approach for computational parity" (line 178), but it is unclear whether this baseline uses the same Self-Exploratory and Self-Reflective data synthesis strategies, the same number of iterations, or the same training data. If the data sources differ, the comparison is confounded — the advantage could come from the data synthesis pipeline rather than the EM structure. The paper should clarify what exactly differs between the EM and standard RL conditions.

### Minor

1. **The alignment analysis (Section 3.3) is descriptive, not evidential of generalization.** The oracle strategy is defined over the test set itself (line 200: "The oracle strategy, determined over the test set"), so the alignment metric is post-hoc and does not measure whether the model has learned a *generalizable* selection principle. Moreover, the paper acknowledges a "significant proportion of correct responses from AutoCode are in the MisAlign category" (line 206), which the authors explain by noting that misaligned choices can still yield correct answers through improved solution generation. This is a reasonable explanation, but it also suggests the model's gains may come as much from broadly improved solution-generation capability as from better methodology selection — somewhat muddying the central claim.

2. **Main results lack error bars or multiple-seed variance.** Table 1 reports single numbers. Given stochasticity in data synthesis (nucleus sampling, K=5 rollouts) and RL training, the reader cannot assess whether differences are robust. This is standard for large-scale RL experiments but still limits the strength of the evidence.

3. **Standard RL baseline description is vague about data synthesis parity.** As noted above, the paper should clarify whether the standard RL ablation uses identical data (same Self-Exploratory/Reflective synthesis) or differs in data composition.

### Trivial

- The reference strategy uses temperature α as a heuristic to sharpen the distribution (introduced in Eq. 7 with α > 0, then set to ∞). A brief note on how different α values affect performance would be helpful but is not essential.
- Minor: line 120 has a doubled word ("both both").

## Nice-to-Haves

- **Supervised methodology-selector baseline**: Training a methodology selector on a small set of queries where the optimal choice is determined by an oracle (e.g., evaluating both CoT and code on held-out queries) would help isolate whether the EM framework's advantage is due to its structure or simply to having more training signal. This is not a required baseline given the paper's framing (autonomous = no external dictation), but it would strengthen the claims.
- **ELBO/objective monitoring**: Plotting an estimate of the ELBO across iterations would help bridge the gap between theory and practice and validate that the implemented procedure improves the intended objective.
- **Out-of-domain alignment analysis**: Reporting alignment rates on out-of-domain benchmarks would test whether the learned selection strategy generalizes.
- **Hyperparameter sensitivity**: A brief analysis of α and clipping thresholds would provide confidence that the method is not brittle.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic's claim about P(r=1|c,x_q) not depending on y_a**: The reviewer states the derivation "assumes that the correctness of the response depends only on the methodology and the query, not on the specific response y_a." This is factually incorrect. The MLE derivation (line 51) explicitly includes `P(r=1|y_a,c,x_q)`, i.e., conditioned on the specific response. The ELBO formulation marginalizes over y_a via the Q-function, which is standard. **Removed: factually wrong.**

- **Harsh Critic's Point 3 (missing supervised baseline)**: The criticism demands a baseline where methodology selection is trained using oracle-labeled data. The paper's entire framing is about *autonomous* learning *without* external dictation. A supervised oracle-labeled selector directly contradicts the problem setting. **Moved to Nice-to-Haves as a potential upper-bound comparison, not a core weakness.**

- **Harsh Critic's Section 2.2 simplified-response criticism**: The reviewer claims the factorization oversimplifies by ignoring that correctness depends on the specific response. As verified above, the derivation and Q-function both account for y_a. **Removed: factually wrong.**

- **Harsh Critic's α heuristic criticism (Section 2.3.1)**: The reviewer notes α is a heuristic not derived from KL minimization. While true, this is a standard design choice (temperature to control sharpness, as stated in line 128) and common in practice. **Downgraded to Trivial.**

## Novel Insights

The most interesting observation emerging from synthesizing the strengths and weaknesses is that the paper's empirical success may be somewhat decoupled from its theoretical framing. The MisAlign analysis (Section 3.3) reveals that a significant fraction of correct answers come from cases where the model's methodology choice disagrees with the oracle — which the paper honestly explains as improved solution-generation compensating for suboptimal selection. This suggests the method's primary benefit may be the rich multi-round data synthesis pipeline (Self-Exploratory + Self-Reflective) creating high-quality training examples, with the EM structure providing a useful organizational metaphor rather than a tight theoretical explanation for the gains. The paper would be strengthened by engaging with this possibility explicitly rather than presenting the EM framing as the sole explanatory mechanism.

## Suggestions

1. **Qualify the monotonic improvement claim.** Add a paragraph explicitly stating that while the theoretical EM framework guarantees ELBO monotonicity, the practical implementation uses approximations (hard-max reference, off-policy RL, clipped importance ratios) and that the method should be evaluated empirically rather than by appeal to theoretical guarantees. Consider plotting an estimated ELBO across iterations as partial validation.

2. **Clarify the standard RL ablation.** Specify whether the standard RL baseline uses the same data synthesis pipeline (same Self-Exploratory and Self-Reflective data, same number of rollouts, same training iterations). If so, state this clearly; if not, add a controlled comparison.

3. **Add multi-seed results or error bars** for the main table, or at minimum acknowledge the single-run limitation and provide an estimate of variance from the ablation experiments.

4. **Report alignment rates on out-of-domain benchmarks** to test whether the learned selection strategy generalizes beyond the training distribution.

5. **Discuss computational cost** (total GPU-hours for training, inference overhead) to help readers assess practicality.

## Score and Decision

The paper addresses a genuine gap with a creative approach and delivers substantial empirical results validated through controlled ablations. The main concerns are (a) overclaiming theoretical guarantees that do not apply to the implemented algorithm, and (b) insufficient specification of the standard RL ablation condition. Neither issue invalidates the core empirical finding — the method clearly works well — but they weaken the paper's explanatory narrative. With reasonable revisions (qualifying the theoretical claims, clarifying the ablation, adding error bars), the paper would be solid. As-is, the overclaiming about monotonic improvement needs correction.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>