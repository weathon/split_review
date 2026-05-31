## Summary

This paper applies Decision Transformer (DT) based methods to the Gym-μRTS real-time strategy environment. It re-implements Critic-Guided Decision Transformers (CGDT) and Online Decision Transformers (ODT), and introduces a combined method called Online Critic-Guided Decision Transformer (OCGDT). The authors evaluate these agents against rule-based bots (CoacAI and Mayari) and compare to Implicit Q-Learning (IQL), reporting that OCGDT matches IQL performance with shorter training time. A dataset of 3,000 trajectories from games between CoacAI and Mayari is also released.

## Strengths

- **Thorough ablation study**: The paper systematically ablates key components including online fine-tuning duration, buffer size, context length, and offline training steps. These experiments provide useful insights into the behavior of DT-based methods in this domain.
- **Reproducibility focus**: Code, data, hyper-parameter configurations, and training details are provided, making the work easy to reproduce and build upon.
- **Addresses a challenging domain**: RTS games with sparse rewards and long horizons are notoriously difficult for RL, and the paper demonstrates that DT-based methods can be competitive with traditional offline RL (IQL) in this setting.

## Weaknesses

### Fatal
None.

### Major
- **Claimed evaluation against four bots is not supported by the results**. The abstract and introduction state that agents are evaluated against CoacAI, Mayari, lightRushAI, and workerRushAI, but Table 1 only reports win rates against CoacAI and Mayari. Results for the other two benchmark bots are missing without explanation, undermining the completeness of the evaluation.
- **The online fine-tuning component (ODT) does not provide a clear benefit**. Ablation OCGDT *D* (no fine-tuning) achieves results comparable to the full OCGDT, and extended fine-tuning (OCGDT *B*) degrades performance. This weakens the motivation for combining CGDT and ODT, as the main advantage of ODT (online improvement) is not realized.
- **OCGDT does not outperform its individual components on the primary metrics**. Against Mayari, ODT alone achieves the highest win rate (46.3%), and CGDT alone achieves 40.8%—both within or above OCGDT's 40.1%. Against CoacAI, OCGDT (26.2%) is only marginally higher than CGDT (22.3%) and ODT (25.5%), all overlapping within confidence intervals. The combination does not demonstrate a clear empirical advantage.

### Minor
- **Limited baseline comparisons**. Only IQL is used as an offline RL baseline. While IQL is a strong method used in the original CGDT and ODT papers, the field would benefit from comparison with additional offline RL algorithms (e.g., CQL, BCQ) to better contextualize the results.
- **The dataset is relatively small (3,000 trajectories) and generated from only two rule-based bots**. The policy may overfit to the specific behavior of CoacAI and Mayari, and the ablations (OCGDT *E*) suggest overfitting occurs with longer offline training. The conclusions may not generalize to richer, more diverse datasets.
- **The wall-clock time comparison is not precisely controlled**. The claim that OCGDT matches IQL in half the wall-clock time is based on comparing OCGDT (4.25 hours) with IQL 400k (~4.25 hours), but the exact training times depend on implementation details and hardware. The statement is plausible but the paper does not provide a detailed profiling comparison.

### Trivial
None.

## Nice-to-Haves

- Include results for lightRushAI and workerRushAI to support the four-bot claim.
- Consider evaluating on larger maps or with partial observability to test the role of context length.
- Explore more sophisticated online fine-tuning strategies (e.g., conservative updates, prioritized replay) to make the online phase effective.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Present the full set of benchmark bot results (all four) in Table 1.
- Strengthen the analysis of online fine-tuning by investigating why self-generated trajectories degrade performance and whether improved exploration or replay buffer management can remedy this.
- Add more offline RL baselines to situate the DT-based methods within the broader literature.
- Include a sensitivity analysis of the test-time temperature parameter (currently 0.25).

## Score and Decision

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: Reject