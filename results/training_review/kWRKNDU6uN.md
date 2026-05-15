Now I have all the information I need. Let me compose the final review.

## Summary

This paper proposes **SMILING** (Score-Matching Imitation Learning), a new IRL framework that replaces adversarial discriminator training with score matching on diffused state distributions. The key idea is a novel **Diffusion Score (DS) Divergence** — comparing expert and learner state distributions by matching their diffusion score functions via standard regression. Theoretically, Theorem 1 provides first- and second-order instance-dependent regret bounds scaling with horizon linearly, demonstrating avoidance of compounding errors. Empirically, SMILING outperforms GAN-based (DAC) and discriminator-free (IQ-Learn) baselines on multiple continuous control tasks, including challenging HumanoidBench tasks, using state-only demonstrations.

## Strengths

- **Novel divergence and algorithmic framework.** The DS Divergence (Definition 1) is a genuinely new perspective on imitation learning, connecting score-matching to IRL in a principled way. The derivation of the cost function via variance correction (Eq. 5) elegantly avoids the need for adversarial discriminator training, replacing it with regression-based score matching. This is a non-trivial contribution.

- **Strong theoretical guarantees with instance-dependent bounds.** Theorem 1 proves that SMILING achieves performance bounds scaling with the minimum of the expert's or learner's return variance (second-order) or return (first-order), plus a linear-in-\(H\) error term. These are theoretically tighter than prior IPM-based IRL bounds (e.g., Kidambi et al. 2021, Chang et al. 2021) and demonstrate that the method avoids compounding errors. The explicit handling of model misspecification, optimization error, and statistical error is rigorous.

- **Empirical superiority on challenging control tasks.** On five out of six tasks (ball-in-cup-catch, humanoid-walk, humanoid-crawl, humanoid-pole, humanoid-sit), SMILING outperforms DAC (JS-divergence-based GAN IRL) and IQ-Learn, often by a large margin. The visual demos (Figure 1) provide compelling qualitative evidence that SMILING learns meaningful behaviors where DAC collapses. The experimental design is well-controlled: DAC and SMILING share the same RL solver and network architectures, isolating the effect of the objective function.

- **Demonstrated expressiveness advantage of score functions.** Through the exponential family example (Section 5.1) and the linear ablation (Figure 7), the paper shows that score matching can be effective with weaker function classes than those required by discriminator-based methods. The linear ablation is direct evidence supporting the expressiveness argument.

- **Stable training dynamics.** The learning curves consistently show smoother convergence for SMILING compared to DAC, which frequently exhibits oscillations (e.g., cheetah-run, humanoid tasks). This aligns with the claim that regression-based score matching avoids GAN-style training instabilities.

## Weaknesses

### Fatal

None.

### Major

- **Cost normalization creates an unanalyzed gap between theory and practice.** The derived cost function (Eq. 5) has a specific scale determined by score-matching losses. The paper states that "we normalize the cost of each batch to have zero mean and a standard deviation of 0.1" without analyzing how this affects the DS divergence minimization. The theory assumes the RL step minimizes the unnormalized cost; the actual algorithm minimizes a normalized version. The paper provides no ablation without this normalization, nor any justification for why it preserves the theoretical guarantees. This weakens the causal link between the theoretical derivation and the empirical success.

- **Theoretical bounds are not empirically validated or connected to experiments.** Theorem 1 involves variance terms (\(\mathrm{Var}^{\pi^e}, \mathrm{Var}^{\pi^{(1:K)}}\)) that are never measured or discussed in experiments. The paper does not test whether performance improves when variance is low, nor does it vary expert dataset size to probe sample efficiency — despite claiming improved scaling in \(N\). The mixture policy \(\pi^{(1:K)}\) that the theory guarantees performance for is never evaluated; instead, results are reported for individual policies. This makes the theoretical and empirical contributions feel disconnected.

### Minor

- **BC baseline presentation, while acknowledged, is still somewhat misleading.** The paper correctly notes that BC uses expert actions while SMILING does not, and explicitly states BC is "not directly comparable" (line 387). However, the figures use BC as a horizontal reference line and the text claims SMILING "outperforms... Behavioral Cloning" (abstract, line 47). A reader could reasonably interpret this as a direct comparison when the settings differ qualitatively.

- **IQ-Learn tuning is underdocumented.** The paper notes that "several configurations... reported the best one" without specifying what was varied. This makes it difficult to assess whether IQ-Learn was given a fair comparison.

- **Missing ablations for key hyperparameters.** The paper uses 500 MC samples for cost estimation and 5K diffusion steps without ablating these choices. The sensitivity of results to these hyperparameters is unknown.

- **The expressiveness argument (linear ablation) is demonstrated on a single task (cheetah-run).** While the exponential family argument is general, the empirical support for the claim that "score matching only needs relatively weaker score function class" rests on one environment. Additional tasks would strengthen this claim.

- **The definition of "batch" in the cost normalization step is imprecise.** The paper normalizes "the cost of each batch" but does not specify whether this is over states in an RL batch, Monte Carlo samples, or another grouping. This affects reproducibility.

### Trivial

None.

## Nice-to-Haves

- An ablation study comparing performance with and without the cost normalization step.
- Varying expert dataset size to directly validate the claimed \(O(1/N)\) sample efficiency.
- Evaluating the mixture policy \(\pi^{(1:K)}\) to connect theory to practice.
- Measuring the variance of returns under the expert/learner on a controlled task to validate the second-order bound.

## Removed Points

These points were flagged by reviewers but are removed from the main review with justifications:

1. *"The original DAC used SAC; switching to DreamerV3 might benefit one method more."* — **Removed.** Both DAC and SMILING use the **same** RL backbone (DreamerV3) on HumanoidBench. The comparison is fair and controlled; this is a strength of the experimental design, not a weakness.

2. *"The comparison to DAgger/AggreVate(D) is not referenced with citations."* — **Removed.** Line 292 explicitly cites DAgger (ross2011reduction) and AggreVate(D) (ross2014reinforcement, sun2017deeply). The criticism is factually wrong.

3. *"Cannot be verified that SMILING is the first IRL method to solve multiple HumanoidBench tasks."* — **Removed per hard rule.** The paper cites the benchmark (sferrazza2024humanoidbench) and provides direct comparisons with strong IRL baselines (DAC, IQ-Learn) showing they fail while SMILING succeeds. The claim is supported by the evidence presented.

4. *"The theoretical analysis assumes a strong realizability assumption (score function class G contains the true score)."* — **Removed.** The paper explicitly acknowledges this assumption on line 257 and states it is standard in the diffusion model literature. It is not hidden or misleading.

5. *"Only five seeds, no significance tests."* — **Weakened and moved.** The paper shows learning curves with shaded regions (presumably confidence bands) across 5 seeds, which is standard practice in RL. Significance tests are not standard for learning curves in this field. The remaining concern about limited seeds is minor.

## Novel Insights

The most interesting observation that emerges across the reviews is the **tension between the paper's theoretical machinery and its practical implementation**. The theory is elegant — minimizing DS divergence via score matching with FTL, achieving instance-dependent bounds that no discriminator-based method can match. Yet the practical algorithm introduces a cost normalization step that is completely disconnected from the theory. This raises a broader question that the paper does not address: **how robust is the theoretical guarantee to the normalizations and engineering tricks needed to make score-based costs work with standard RL solvers?** If the normalization is critical for performance, the theory might be describing a different (less effective) algorithm, and the empirical success might stem from the cost's relative ranking of states rather than its precise DS-divergence interpretation. This is not a fatal flaw — many successful methods have theory-practice gaps — but it is an unresolved tension that limits the paper's explanatory power.

## Suggestions

1. **Add an ablation removing the cost normalization** and report whether performance degrades. If it does not, the theory-practice gap is smaller than it appears. If it does, discuss why normalization is needed and whether the theoretical claims still apply.

2. **Measure the return variance** for at least one task (e.g., cheetah-run with controlled noise) and show that SMILING's performance improves when variance is low, directly validating the second-order bound.

3. **Evaluate the mixture policy \(\pi^{(1:K)}\)** in one experiment to connect the theoretical guarantee to the empirical evaluation.

4. **Clarify the batch normalization definition** — specify exactly which samples are pooled for computing mean and std.

5. **Add one more linear ablation task** (e.g., ball-in-cup-catch) to confirm the expressiveness advantage is not specific to cheetah-run.

## Score and Decision

Based on my assessment: the paper makes a genuine theoretical contribution (novel DS divergence, instance-dependent bounds), a sound algorithmic contribution (replacing adversarial training with score matching), and strong empirical results on challenging tasks. The weaknesses are significant but addressable — none invalidate the core claims. The cost normalization gap and missing empirical validation of theoretical claims are the most serious issues, but they reflect underanalysis rather than flawed methodology.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>