- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes HyPoGen, a hypernetwork that generates policy network parameters from task specifications by mimicking iterative gradient-based optimization. The key idea is to bias the hypernetwork architecture toward optimization by (a) performing iterative updates in a latent parameter space rather than one-shot prediction, and (b) modeling chain-rule interdependencies across target network blocks during the forward synthesis pass. The method is evaluated on MuJoCo locomotion and ManiSkill manipulation tasks, showing consistent improvements over prior hypernetwork and meta-learning baselines.

## Strengths

- **Novel architecture with a well-motivated optimization bias**: HyPoGen's iterative update scheme (Eq. 6) that operates in a latent parameter space is a principled departure from the standard MLP-based hypernetwork. The explicit modeling of chain-rule-like gradient computation across policy network blocks (Eq. 7–8) is a genuine architectural innovation over HyperZero and prior hypernetwork approaches that treat all parameters simultaneously.

- **Consistent state-of-the-art results across two diverse benchmarks**: In Tables 1 and 2, HyPoGen achieves the highest average reward (MuJoCo) and success rate (ManiSkill) among all compared methods, including the few-shot fine-tuning baselines (Meta Policy, PEARL) that have access to target-task demonstrations. The gains are particularly striking on the more challenging ManiSkill stiffness and damping specifications, where most baselines collapse while HyPoGen maintains high success rates.

- **Convergence efficiency advantage**: Table 5 shows that HyPoGen reaches a given reward with fewer training epochs and achieves higher reward at the same epoch count compared to HyperZero, suggesting the optimization bias improves learning dynamics, not just final performance.

## Weaknesses

### Fatal

None.

### Major

- **No ablation isolates the gradient/chain-rule structure from other confounding factors**: HyPoGen differs from HyperZero in at least three ways simultaneously: (a) iterative updates vs. one-shot prediction, (b) latent-space compression/decompression, and (c) the chain-rule product structure within each block (Eq. 8). The paper provides no ablation that varies the gradient structure while holding iteration and latent space fixed — for example, replacing Eq. 8 with an MLP that directly outputs the parameter update. Without this, we cannot attribute the improvement to the claimed optimization bias rather than to increased capacity, more steps, or the latent bottleneck. This is the most significant gap in the paper's evidence chain.

- **The foundational assumption that task specification is a sufficient representation of demonstration data is asserted without justification or validation**: The paper states in Sec. 4.2 (line 109) that the method works "if we treat the specification M of a target task as a sufficient representation of its demonstrations." This is a strong claim — in practice, specifications like target speed or arm length are low-dimensional and likely underdetermine the full state-action distribution. The paper provides no theoretical justification, empirical test (e.g., can a policy trained from specification alone recover the demonstration distribution?), or discussion of when this assumption might break. If the specification is not sufficient, the "optimization" framing loses its principled connection to the true policy update, and the method reduces to a conditional generator with an elaborate architecture.

- **Standard deviations are not reported for the main results (Table 1, MuJoCo)**: The paper states that the train/test split is repeated five times and averaged, but does not report any measure of variance for the MuJoCo results in Table 1. Many of the differences between HyPoGen and HyperZero are small (e.g., Finger speed: 710 vs. 701). Without error bars or confidence intervals, we cannot assess statistical significance or the reliability of the reported improvements.

### Minor

- **The evidence for "actually performing optimization" (Section 5.4) is weak**: Table 3 shows that different initial weights θ⁰ lead to different final parameters θ^K — this only rules out a constant function, which is expected of any non-trivial network. Table 4 shows BC loss decreasing on source tasks, but this is essentially training convergence on seen data, not evidence that the neural gradients approximate true optimization dynamics. The paper does not compare the neural gradient estimates to actual analytical gradients on source tasks (e.g., via cosine similarity), which would be a much stronger test.

- **Figure 4 (qualitative comparison on Cheetah) lacks error bars and uses only two training points** (speeds 1 and 10). This makes the figure suggestive but not quantitatively reliable. It is also unclear why HyperZero degrades at the interpolation midpoint (speed 5), where a smooth function approximator should perform well — variance bars would help determine whether this is a meaningful phenomenon or noise.

- **No ablation of the number of iterations K**: The paper uses K=8 with no analysis of how performance varies with K. Does performance plateau? Is the iteration mechanism critical, or would a single update with the same architecture suffice?

- **The BC loss analysis (Table 4) does not specify whether it is computed on source or target tasks**; since target tasks have no demonstrations, it must be source tasks, which makes this a training convergence measure rather than a test-time generalization measure.

### Trivial

None.

## Nice-to-Haves

- An ablation comparing HyPoGen to a version where the chain-rule product (Eq. 8) is replaced by a direct MLP update, keeping the iterative structure and latent space fixed, would directly test the claimed gradient modeling contribution.
- Cosine similarity or directional agreement between neural gradient estimates and actual analytical gradients on source tasks would provide direct evidence for the optimization claim.
- Reporting results with varying train/test split ratios (e.g., 50%/50% in addition to 20%/80%) would strengthen the robustness analysis.
- A brief discussion of computational cost compared to baselines would be helpful (the paper reports 11 hours for HyPoGen on a 4090 but does not give equivalent numbers for HyperZero or other methods).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about unfair comparison against Meta Policy/PEARL**: The reviewer claimed the comparison is unfair because Meta Policy and PEARL use few-shot fine-tuning. The asymmetry here favors the baselines (they have more information — access to target demonstrations), not the author's method. If a baseline with more information performs worse, that strengthens the authors' case. Removed per rule about asymmetry favoring baselines.

- **"Missing comparison to Xiong et al. (2023, 2024) and others"**: Asking for comparison to specific prior hypernetwork methods for morphology control. The paper cites these works in related work but does not claim to benchmark against them; requesting additional baselines is a suggestion, not a demonstrated flaw. Weakened to a nice-to-have but ultimately removed as scope-creep.

- **"The paper references Appendix sections extensively but we cannot evaluate them"**: This is a parser artifact — appendices exist in the original submission. Removed per instructions.

- **"HyperZero's degradation on speed 5 is suspect"**: Speculative without evidence. Removed.

- **"Why not use actual activations from current policy parameters"**: The paper explicitly addresses this design choice: "One could also make the estimation of ẑ_n's dependent on the current estimate of the latent parameters, but we omit the dependence for clarity and leave the necessity to experimental justifications." The criticism ignores this acknowledgment. Removed as strawman.

## Novel Insights

None beyond the paper's own contributions. The reviews surface two tensions worth noting: first, the paper's core empirical success (HyPoGen works better than HyperZero) is clear, but the mechanism claimed for this success (optimization bias from gradient-mimicking structure) is not isolated from other architectural differences. Second, the specification-sufficiency assumption — which the paper states explicitly but does not justify — would need to hold for the method to constitute "optimization without data" rather than just a well-designed conditional generator. These are insights about gaps in the evidence rather than new observations about the problem.

## Suggestions

1. Add an ablation that keeps the iterative structure and latent compression fixed but replaces the chain-rule gradient product (Eq. 8) with direct MLP-predicted updates. This is the single most important experiment to support the paper's core claim.
2. Include standard deviations or confidence intervals for all main results in Tables 1 and 2, and add error bars to Figure 4.
3. Provide a direct comparison between the neural gradient estimates and actual analytical gradients on source tasks (e.g., cosine similarity) to substantiate the claim that the network has learned to approximate optimization.
4. Discuss the specification-sufficiency assumption more explicitly: under what conditions might it fail, and what would the consequences be?
