- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5
Now I have verified all claims against the paper. Let me produce the final consolidated review.

## Summary

This paper introduces Q-Score Matching (QSM), a method for training diffusion model policies in reinforcement learning. The core theoretical insight (Theorems 1 and 2) establishes that at optimality, the score of the policy distribution is proportional to the action-gradient of the Q-function: score*(s,a) ∝ ∇_a Q^{score*}(s,a). The authors instantiate this as an off-policy actor-critic algorithm that regresses the score network toward ∇_a Q, avoiding backpropagation through the full diffusion chain (a computational advantage over methods like Diffusion-QL). Experiments on DeepMind Control Suite tasks compare QSM to SAC, TD3, Diffusion-QL, and a naive policy gradient baseline.

## Strengths

1. **Novel theoretical link between policy score and Q gradient**: Theorems 1 and 2 formally establish that any optimal score field satisfies score*(s,a) = α_{s,a} ∇_a Q^{score*}(s,a). This provides a principled geometric foundation for optimizing diffusion model policies that is absent in prior work. (Section 4, Theorems 1 and 2)

2. **Computational efficiency advantage**: QSM differentiates only through the denoising model rather than the full diffusion model evaluation chain. This is a genuine practical benefit over Diffusion-QL, which backpropagates through the entire diffusion process. The paper provides empirical evidence (Fig. 8) that QSM takes significantly less computation time for the policy gradient update. (Abstract, Section 4, Fig. 8 caption)

3. **Demonstration of multi-modal policy learning**: The paper provides visualization evidence that QSM-trained policies produce diverse, multi-modal action distributions (Fig. 4, 6), including a UMAP comparison showing greater diversity than Diffusion-QL under identical architectures — confirming diversity stems from the training method, not the model class. (Section 5, Fig. 4, 6)

4. **QSM outperforms naive policy gradient for diffusion policies**: Fig. 5 directly shows that applying the standard policy gradient formula to diffusion models yields worse performance than QSM, validating the paper's motivation from Section 3. (Fig. 5)

## Weaknesses

### Fatal
None.

### Major

1. **Overclaimed theoretical guarantee**: The paper states (lines 186, 218) that Theorems 1 and 2 imply that "iteratively matching score(s,a) to ∇_a Q(s,a) will provide strict increases to the resulting Q-function globally." However, the theorems as stated only prove a *necessary condition for optimality* — they do not establish that any step toward alignment strictly increases Q. This is an overclaim that conflates a characterization of optimality with a proof of monotonic improvement. The algorithm stands as a motivated heuristic derived from an optimality condition, which is a common and valid approach; the paper should present it as such rather than claiming a guarantee the theory does not provide.

2. **No statistical rigor in experiments**: The paper reports no multiple seeds, no error bars, and no confidence intervals for any experiment (Figs. 3, 5, 8). The paper does not mention the number of trials for any result. Without this information, it is impossible to assess whether observed differences between QSM and baselines are meaningful or within noise. This is a basic experimental standard that undermines the paper's central empirical claims. (Section 5, Figs. 3, 5, 8)

### Minor

3. **Limited experimental scope**: Only 6 tasks from DeepMind Control Suite are evaluated, all relatively low-dimensional (cartpole, quadruped, etc.). No experiments on more challenging domains (e.g., Humanoid, dexterous manipulation) where the expressiveness of diffusion policies would be most impactful. (Section 5)

4. **No ablation studies**: The algorithm involves several design choices (number of denoising steps K, noise schedule for buffer actions, variance-preserving vs. other noise, amount of Gaussian noise on final actions) that are never varied or justified. The contribution of the score-matching objective specifically is not isolated from other design choices. (Section 5, Algorithm 1)

5. **Incomplete baseline comparisons**: IDQL (Hansen et al., cited in related work) is a relevant diffusion-based offline RL method never compared to. The diffusion-policy baseline comparison (Fig. 8) uses "consistent hyperparameters" that differ from the main results (Fig. 3), which is explained but makes the overall picture of QSM's performance across settings unclear. (Section 5, Fig. 8)

6. **Missing key implementation details**: The number of denoising steps K is never specified. The noise schedule for the variance-preserving Markov chain applied to replay buffer actions is not described. How ∇_a Q is computed (which critic network, whether through the minimum of the two target critics, the exact computational graph) is not specified. These details are necessary for reproducibility. (Algorithm 1, Section 5)

### Trivial
None.

## Nice-to-Haves
- The scalar α from the theoretical condition (score ∝ ∇_a Q) is absent in the practical algorithm (score = ∇_a Q). A brief discussion of why this discrepancy does not affect the method would be helpful.
- Wall-clock timing or FLOPs comparison between QSM and Diffusion-QL would strengthen the computational efficiency claim beyond what is currently shown.
- A sensitivity analysis for hyperparameters (K, noise schedule, exploration noise magnitude) would strengthen the empirical evaluation.

## Removed Points

These points from the reviewers are flagged for removal; treat them with caution:

1. **Harsh critic's claim of "structural disconnect" between theory and algorithm**: The critic argued the theory applies to a "different object" (continuous-time action process vs. diffusion sampling). However, the paper explicitly addresses this through the time-discretization argument (Section 2.3, Eq. 4) and presents the connection as approximate ("we expect the theory...to also approximately hold"). The theory motivates the algorithm through an optimality condition, which is standard practice. The critic's framing overstates the gap. The actual issue (overclaimed monotonic improvement guarantee) is retained in Major weakness #1.

2. **Harsh critic's criticism of the gridworld section as "misleading"**: The paper explicitly titles this "Pedagogical reduction in gridworld" (Section 4.3) and states it is to "provide intuition." The paper is transparent that diffusion models are not defined in discrete spaces. The critic's accusation of misleading presentation is unsupported.

3. **Harsh critic's reparameterization trick criticism**: The critic claimed the policy gradient formula (Eq. 3) could use the reparameterization trick (as in Diffusion-QL). The paper's point is that computing policy gradients for diffusion models requires expectations over internal action samples, which is sample-inefficient regardless of reparameterization. Diffusion-QL avoids this by a *different* approach (full backpropagation through the diffusion chain), which has its own computational costs that the paper acknowledges.

4. **Harsh critic's "inconsistent hyperparameters" complaint about Fig. 8**: The paper explicitly states that Fig. 8 enforces "consistent hyperparameters" to enable fair comparison between QSM and Diffusion-QL, and notes that performance differs from Fig. 3 for this reason. This is clearly explained, not an error.

5. **Strength Finder's generic strengths**: Claims that the problem is "important" or that the paper "addresses a key question" without specific anchoring to paper content are removed. The remaining strengths are concrete and evidence-grounded.

## Novel Insights
None beyond the paper's own contributions. The two reviews largely agree on the core strengths (the theory, computational advantage) and weaknesses (overclaimed guarantees, insufficient empirical rigor). The most interesting tension is whether the theory-algorithm gap is a "structural disconnect" (as the harsh critic claims) or a standard motivation-from-optimality-conditions approach (my assessment). I find the latter view more accurate — the real issue is the paper's overclaim about monotonic improvement, not a fundamental disconnect.

## Suggestions
1. **Tone down theoretical claims**: Remove or qualify statements that iterative matching "will provide strict increases" — the theorems only prove a necessary optimality condition. Present QSM as motivated by this condition, not guaranteed by it.

2. **Add statistical rigor**: Report all results with multiple random seeds (at least 5) and show standard deviations or confidence bands on learning curves.

3. **Add ablation studies**: Vary K (number of denoising steps), the noise schedule, and the exploration noise magnitude. Compare against a variant that replaces score-matching with a direct MSE to ∇_a Q without denoising to isolate the effect of the diffusion structure.

4. **Add missing baselines and implementation details**: Compare to IDQL. Specify K, noise schedule, and the exact computation of ∇_a Q. Provide wall-clock timing comparisons.

5. **Broaden task set**: Include higher-dimensional tasks (Humanoid, dexterous manipulation) where diffusion policies have the greatest potential advantage over Gaussian policies.
