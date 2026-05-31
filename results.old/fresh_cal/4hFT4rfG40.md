Now I have thoroughly verified all claims against the paper. Let me produce the consolidated review.

## Summary

This paper proposes the first plug-and-play controllable generation framework for discrete masked models. The core idea combines mean-field approximation with iterative unmasking-remasking and importance sampling to sample from a target posterior \(q(x) \propto r(x)p(x)\) without fine-tuning the underlying model or requiring gradient information. The method is evaluated on a toy constrained-sampling task and on three protein design tasks (hydrophilic/hydrophobic generation, alpha-helix enrichment, and inpainting) using ESM3 as the base model.

## Strengths

- **First plug-and-play sampler for discrete masked models.** The paper correctly identifies a gap — existing controllable generation for discrete models requires task-specific fine-tuning or gradient-based guidance — and proposes a genuine training-free, gradient-free alternative. Section 1 and the contribution list in the introduction make this claim explicit, and Algorithm 1 implements it without any task-specific training. This is a novel methodological contribution.

- **Clear theoretical grounding via mean-field approximation and importance sampling.** The derivation in Section 3.2 is principled: the conditional distribution under the target posterior is expressed in terms of the known unconditional conditional distribution and the reward, and importance sampling (Lemma 1) provides a tractable way to sample from the intractable normalizing-constant-free distribution. The connection to plug-and-play methods for continuous diffusion (Section 3.1) provides helpful context.

- **Reward-agnostic and gradient-free by design.** Unlike continuous-domain plug-and-play methods that require differentiability of the control criterion, the proposed importance-sampling-based approach works with any reward function — non-differentiable, discrete, or black-box — as only evaluations (not gradients) are needed. This is a genuine advantage for many real-world applications.

- **Demonstrated across diverse tasks.** The method is tested on three distinct protein design objectives (GRAVY control, alpha-helix enrichment, inpainting) plus a synthetic constrained-sampling task, showing the framework's versatility. The GRAVY results in Table 1 (e.g., shifting from uncontrolled mean −1.52 to controlled mean 0.15 for hydrophobic generation) are consistent with the method steering the distribution in the intended direction.

## Weaknesses

### Fatal
None.

### Major

- **No baselines compared.** The method is compared only to the uncontrolled base model. There is no comparison to (a) rejection sampling on unconditional model outputs with the same reward function, (b) an ablation without the iterative remasking (i.e., a one-shot importance sample from the mean-field approximation at the final step), or (c) any other plug-and-play or training-free control approach that could be adapted to this setting. Without such comparisons, the reader cannot attribute observed distribution shifts to the algorithm's design rather than simply to the reward function's bias. This is the most significant gap in the evaluation.

- **Circular validation of protein structure.** Figures 3 and 4 use ESM3's own folding algorithm to predict 3D structures of generated sequences. Since ESM3 is both the generator and the structure predictor, the method may be exploiting artifacts of ESM3's predictors rather than producing genuinely alpha-helical proteins. The paper states (line 245): "To verify the structural accuracy of the generated sequences, we use the folding algorithm provided by ESM3." Independent validation with a different structure prediction tool (e.g., AlphaFold2, a different secondary structure predictor) is needed to support the claim that generated sequences are genuinely helical.

- **Missing experimental hyperparameters for protein experiments.** The protein experiments do not disclose the values of \(K\) (number of Monte Carlo samples), \(T\) (number of unmasking steps), the remasking schedule \(\gamma\), or the reward function parameters \(w_i, A_i\). The paper states (line 247) "Our empirical findings suggest an optimal choice for these parameters" without presenting those findings. This makes the experiments impossible to reproduce. The toy experiment (Figure 2) shows that \(K\) significantly impacts quality, so its omission from the protein experiments is a meaningful gap.

### Minor

- **Ambiguous reporting of results.** The main text (line 234) states "The table presents the best generation result" — an unclear phrase that could suggest selection among multiple runs or hyperparameter choices. While the table captions clarify that metrics are "mean ± std," neither the number of independent runs/sequences nor the number of random seeds used is reported. Providing these details would improve confidence in the results.

- **No analysis of importance sampling efficiency or failure modes.** The method relies on importance sampling with a mean-field proposal. The paper does not discuss diagnostic quantities such as effective sample size, weight variance, or how to choose \(K\) for a given constraint difficulty. The toy experiment partially addresses this by showing performance for different \(K\) values, but general guidance is absent. This limits practical usability.

- **Computational cost not quantified.** The introduction (line 23) claims "approximately 10 queries to the masked model and around 1000 Monte Carlo samples," but no wall-clock time or model query counts are reported for the protein experiments. Given that efficiency is part of the claimed contribution, a rough empirical verification would be helpful.

### Trivial

- The conclusion (Section 6) discusses future work but does not acknowledge any limitations of the current method.

## Nice-to-Haves

- An ablation comparing the full algorithm to a one-shot importance sample from the mean-field prior (no iterative remasking) would isolate the contribution of the iterative process.
- A failure analysis or guidance on choosing \(K\) for target constraint difficulty would strengthen the practical contribution.
- Reporting a diversity metric (e.g., average pairwise sequence identity) for controlled vs. uncontrolled samples would address whether repeated remasking reduces output diversity.

## Removed Points

*These points from the input reviews are removed with justification below.*

- **"No comparison to FUDGE-style approaches or gradient-based guidance" (Harsh Critic).** Removed: FUDGE requires task-specific fine-tuning, and gradient-based guidance requires differentiability — both are outside the paper's plug-and-play, gradient-free scope. The paper's claim is about being the *first plug-and-play sampler*, not about matching fine-tuned methods.

- **"Resampling only one sample from weighted empirical distribution is not justified" (Harsh Critic).** Removed: This is standard importance resampling. In a sequential generation process where only one continuation is needed at each step, drawing one sample from the weighted empirical distribution is a natural design choice. This is not a flaw.

- **Generic/superficial strengths from Strength Finder.** The strength "Demonstrated effectiveness across diverse tasks with strong quantitative results" is weakened given the baseline and circular-validation issues noted above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add baselines**: Compare to rejection sampling from the unconditional model (with the same reward function) and to a one-shot importance-sampling variant without iterative remasking. This would directly demonstrate whether the iterative unmasking-remasking design adds value over simpler alternatives.

2. **Validate protein structure independently**: Use a different structure prediction tool (e.g., AlphaFold2, or a sequence-to-secondary-structure predictor not from the ESM family) to confirm that generated sequences are genuinely helical. Report separately how helix percentage is computed.

3. **Disclose all hyperparameters**: Report \(K\), \(T\), the remasking schedule \(\gamma(\cdot)\), and the reward parameters \(w_i, A_i\) used in the protein experiments. Specify the number of sequences generated and the number of independent runs/seeds.

4. **Clarify reporting**: Remove or explain the "best generation result" phrasing. Specify the number of independent trials used to compute means and standard deviations.

5. **Add limitations and variance discussion**: Include a brief discussion of when the importance sampling proposal is likely to fail (e.g., very rare constraints) and mention effective sample size as a diagnostic.

## Score and Decision

The paper addresses a meaningful gap — plug-and-play control for discrete masked models — with a novel, well-motivated, and theoretically grounded algorithm. The method is clearly described and its versatility is demonstrated across multiple tasks. However, the experimental evaluation is insufficiently rigorous: the lack of baselines, circular structure validation, and missing hyperparameter reporting limit confidence in the results. These issues are all addressable with additional experiments and disclosure, and they do not invalidate the core methodological contribution.

**Overall Assessment**: The paper has a genuine contribution and should be accepted with major revisions to strengthen the empirical evaluation.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>