## Summary

This paper investigates whether large reasoning models can self-train via reinforcement learning (RL) using self-generated rewards, specifically using majority voting as the reward mechanism (Self-Rewarded Training, SRT). Through comprehensive experiments on synthetic and real reasoning tasks, the authors show that SRT improves both reasoning performance and the quality of self-supervision over training, outperforming fixed-teacher baselines. However, prolonged training leads to reward hacking and sudden performance collapse across all tested models, revealing fundamental limitations of this simple self-reward approach and highlighting feedback design as the key challenge for sustained self-improvement.

## Strengths

- **Comprehensive empirical investigation**: The paper evaluates SRT across multiple base models (4 different architectures), multiple training datasets, multiple RL algorithms (RLOO, GRPO), and both synthetic and real-world reasoning tasks, providing strong evidence for its initial effectiveness and eventual collapse.
- **Clear decomposition of the self-improvement question**: The paper separately studies whether self-training improves performance, whether it improves the quality of self-generated labels (evolving teacher), and whether improvement can be sustained—each with controlled experiments.
- **Well-designed synthetic task experiments**: The use of Reasoning Gym with controllable difficulty levels allows rigorous study of curriculum-based self-improvement and demonstrates that SRT can climb to harder tasks without ground-truth labels.
- **Detailed collapse analysis**: The paper connects the observed performance collapse to reward hacking via analysis of training statistics (pseudo-reward, KL divergence, entropy) and provides concrete examples of collapsed outputs, offering a clear diagnostic for future work.

## Weaknesses

### Fatal
None.

### Major

- **Limited novelty of the central finding**: That self-training with a simple self-reward mechanism eventually collapses via reward hacking is broadly consistent with well-known phenomena in RL (reward hacking, simplicity bias) and prior work on model collapse from self-generated data. The paper does not propose new mitigation strategies or theoretical insights beyond documenting this behavior in the RLVR setting. While the empirical characterization is solid, the contribution is more confirmatory than transformative.
- **The claim of inevitable collapse is not fully supported**: For Llama-3.1-8B-Instruct, the paper notes that a lower learning rate does not lead to collapse within the training budget, and only hypothesizes that prolonged training would cause collapse. The statement that "self-training benefits may not extend indefinitely" is appropriate, but the paper sometimes implies generality beyond what the evidence strictly shows (e.g., only one learning rate leads to collapse in some cases, and the number of generations matters).

### Minor

- No uncertainty quantification or statistical significance is reported for the accuracy curves; given the stochasticity in RL training, this would strengthen the claims.
- The paper does not compare SRT to other self-improvement paradigms beyond fixed-teacher baselines (e.g., iterative DPO, self-play with rejection sampling) in the online setting, making it harder to assess the relative value of the RL approach.
- The ablation on the effect of fewer generations (more noise) delaying collapse is interesting but not deeply analyzed—why noise helps is left as a speculation rather than a studied mechanism.

### Trivial
None.

## Nice-to-Haves

- A simple theoretical model (e.g., a causal explanation of how majority vote as reward creates a self-reinforcing cycle that leads to template answers) would strengthen the paper's contribution.
- Experiments on non-math reasoning tasks (e.g., coding with unit tests as a more reliable self-consistency signal) would broaden the scope.
- A deeper analysis of the curriculum setting: does the model actually learn to solve harder tasks, or does the majority vote become trivially consistent on easier sub-parts?

## Novel Insights

The paper's most useful observation is that self-training via majority voting creates a self-reinforcing feedback loop: as the model becomes more consistent, the pseudo-reward signal increases and the policy is pushed toward even more consistent but less correct outputs. The sudden collapse is accompanied by a sharp increase in KL divergence from the base model and a spike in output entropy, followed by all outputs converging to the same template answer regardless of prompt. This contrasts with standard RLVR with ground-truth rewards, where no such collapse occurs, directly demonstrating that the *quality* of the reward signal, not the RL algorithm, is the bottleneck for sustained self-improvement.

## Suggestions

- If possible, run one extended training curve for the Llama-3.1-8B-Instruct with the lower learning rate to confirm whether collapse occurs eventually, or temper the claim of inevitability.
- Consider reporting standard errors or confidence intervals for the key accuracy curves to quantify the reliability of the trends.
- Discuss the relationship between the collapse phenomenon and the number of generations used for majority voting more explicitly—is the collapse rate a function of the noise in the pseudo-reward estimator?

## Score and Decision

**Score**: 6  
**Decision**: Borderline Accept

MY FINAL SCORE: <score>6</score>  
MY FINAL DECISION: <decision>Accept</decision>