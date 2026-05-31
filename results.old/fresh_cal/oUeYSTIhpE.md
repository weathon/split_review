Now I have a thorough understanding of the paper and can verify all claims. Let me write the consolidated final review.

## Summary

This paper proposes DisCo-DSO, a method that extends deep generative models for combinatorial optimization to jointly sample discrete tokens and their associated continuous parameters in a single forward pass, rather than using a decoupled approach where the discrete skeleton is sampled first and continuous parameters are optimized separately. The method trains an RNN via risk-seeking policy gradient to emit both discrete logits and continuous distribution parameters. Experiments on a synthetic bitstring task, symbolic regression, and decision tree policy learning for RL environments demonstrate the sample-efficiency and performance advantages of joint optimization.

## Strengths

- **Joint optimization dramatically reduces function evaluations (Figure 2)**: In the parameterized bitstring task, DisCo-DSO requires far fewer total evaluations than any decoupled baseline (Decoupled-RL-* and Decoupled-GP-*) because each sample is a complete solution costing one evaluation, while decoupled methods require many downstream evaluations per discrete skeleton. This is the paper's core thesis and is convincingly demonstrated with error bars over 5 seeds.

- **Outperforms all compared methods on decision tree policies across four RL environments (Figure 6)**: DisCo-DSO achieves the highest mean reward on MountainCar-v0, CartPole-v1, Acrobot-v1, and LunarLander-v2 compared to evolutionary DTs (Custode & Iacca, 2023), cascading DTs (Ding et al., 2020), and differentiable DTs (Silva et al., 2020), while maintaining comparable or lower tree complexity. This supports the paper's claim of SOTA for univariate DT policy optimization.

- **Sample-efficiency advantage is convincingly shown (Figure 5)**: The sample-efficiency comparison against decoupled baselines (same architecture, same RL training) shows a clear and consistent advantage for DisCo-DSO across all environments, with mean and standard deviation over 10 seeds. This is the cleanest evidence for the paper's core claim because it controls for all factors except the joint vs. decoupled treatment of continuous parameters.

- **Handles non-differentiable and discontinuous objectives (Figure 2, f₁ and f₂)**: The parameterized bitstring task uses functions that are highly oscillatory (f₁) and piecewise constant (f₂), and DisCo-DSO overcomes these while decoupled methods struggle. This demonstrates robustness that is relevant for real-world black-box optimization.

## Weaknesses

### Major

- **The symbolic regression experiment (Section 4.2, Figure 3) omits critical details needed for reproducibility**: The paper does not list which benchmark datasets were used, how many constants appear in each problem, or the train/test split methodology beyond "expanding the benchmark's domain." Without this information, the SR experiment cannot be reproduced or compared against. This is a significant gap given that the SR experiment is one of three main demonstrations of generality.

- **The DT literature comparison (Figure 6) does not report variance or training details for locally trained baselines**: For methods marked with an asterisk (trained locally), the paper does not describe the training procedure, hyperparameters, number of training seeds, or computational budget used. Since the original papers may have used different resources, the comparison of final performance is hard to interpret as a controlled evaluation. Reporting only the mean reward (averaged over 1,000 evaluation episodes) without any measure of training variance weakens the SOTA claim.

### Minor

- **Figure 3 (SR results) reports only aggregate averages without any measure of dispersion**: The paper states that 10 random seeds were used and then averages across datasets, but no standard errors, confidence intervals, or raw per-dataset breakdowns are provided. This makes it impossible to assess whether the reported advantages over baselines are statistically significant or within noise.

- **The SR experiment compares only against decoupled versions of the authors' own RL method and genetic programming, not against any published SR method that handles constants**: Methods that tokenize constants (Kamienny et al., 2022) or relax the discrete structure (Biggio et al., 2021) address the same hybrid optimization problem. While the paper's claim is specifically about outperforming *decoupled* approaches (and the experiments support this), the absence of any comparison against methods that also attempt to handle constants jointly limits the strength of the claim that DisCo-DSO's joint approach is broadly superior in SR.

- **The claim that GP methods suffer from "bloat problem" (Section 4.2) is asserted without supporting complexity measurements**: The paper attributes the poor test-set performance of Decoupled-GP methods to overfitting/bloat but does not report expression size, tree depth, or any complexity metric to substantiate this claim.

### Trivial

- **The synthetic bitstring task (Section 4.1) uses objectives specifically chosen to highlight the method's advantage**: The paper acknowledges this is a "pedagogical" task, which is appropriate, but the experiment would be strengthened by also showing results on objectives where the decoupled approach can work well, or by systematically varying the problem size N to study scaling behavior.

## Nice-to-Haves

- Including an ablation on the effect of the entropy bonus coefficient and model capacity (the RNN uses only 32 hidden units) would help assess whether the method is robust to hyperparameter choices.
- A systematic study of varying problem size N in the bitstring task would strengthen claims about scalability.
- For the SR experiment, even a brief comparison against one published SR method that handles constants (e.g., GP-GOMEA or the tokenization approach) would significantly strengthen the paper's generality claims.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **From Harsh Critic: "The evaluation lacks statistical rigor in several critical places" (grouping all figures together)**: This is partially inaccurate — Figure 2 reports "Mean and standard error over 5 seeds" and Figure 5 reports "mean and standard deviation" over 10 seeds. Only Figures 3 and 6 lack variance measures. The corrected version is reflected in the Minor weaknesses above.
  
- **From Harsh Critic: "The synthetic bitstring experiment provides only weak evidence" as an evidential concern**: The paper explicitly describes this as a "pedagogical task" designed to understand when benefits appear. This is an honest framing, not a weakness. I have demoted it to a Trivial point about the absence of scaling experiments.

- **From Strength Finder: "Novel contribution to hybrid optimization" (being "the first known instance of using deep RL in parameterized discrete-continuous action spaces for discrete optimization")**: This is a generic contribution claim common to most papers and is not a specific, evidence-grounded strength. The paper's other concrete strengths (Figures 2, 5, 6) are sufficient on their own.

- **From Harsh Critic: "The appendix was stripped, so I cannot assess if missing details are present there"**: This is a parser artifact. The paper's appendix exists in the original submission; the review should not penalize the paper for the extraction process.

- **From Harsh Critic: "Section-by-section notes" items about missing related work and formatting/style observations**: These are either scope-creep (demanding the paper address problems outside its stated scope) or parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core claims (joint optimization is more sample-efficient than decoupled optimization) and identify areas where the evaluation could be strengthened, but no reviewer identified a capability or limitation of the method that the authors themselves did not already articulate.

## Suggestions

1. **Add the list of SR benchmark datasets and the number of constants in each to the main text or a clearly referenced appendix.** Without this, the SR experiment is not reproducible.
2. **Add error bars (standard errors or confidence intervals) to Figure 3 and Figure 6.** For Figure 3, use the 10 random seeds already collected. For Figure 6, either report variance across training seeds for locally trained baselines or clearly state when only a single tree was used (e.g., from original papers).
3. **For the DT literature comparison (Figure 6), describe the training procedure and budget used for each asterisked method.** At minimum, state the number of seeds, episodes, and any hyperparameter search performed.
4. **Consider tempering the generality claims for symbolic regression** or adding a comparison against at least one published SR method that handles constants (e.g., the tokenization approach of Kamienny et al., 2022) to support the claim that joint optimization is broadly superior.
5. **Include complexity measurements (expression size, tree depth) for the SR experiment** to substantiate the bloat-overfitting claim against GP methods.

The paper's core contribution — joint discrete-continuous generation via risk-seeking policy gradient — is well-motivated, technically sound, and convincingly supported by the DT policy experiments (Figures 5 and 6). The weaknesses identified above are about missing experimental details and limited comparison scope, not about flaws in the method or incorrect results. With the suggested additions, the paper would be substantially stronger.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>