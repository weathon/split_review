- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 8, 5, 6
Now I have all the information I need. Let me synthesize the review.

## Summary

This paper tackles an important limitation of existing offline imitation learning (OIL) methods: their reliance on auxiliary offline data containing expert-like trajectories. The authors propose BCDP (Behavioral Cloning with Dynamic Programming), which combines behavioral cloning on limited expert data with TD3+BC-style Q-learning that assigns zero reward to all non-expert transitions. The central idea is to use transition information from low-quality data to guide the agent toward expert-observed states. Experiments on D4RL benchmarks show BCDP achieves best performance on 17/28 tasks, with a 43.6% improvement over BC-exp when auxiliary data is purely random exploration — a setting where prior OIL methods degrade.

## Strengths

- **Empirical success in the challenging low-quality data regime**: Table 1 shows BCDP achieves best or second-best performance on 17/28 continuous control tasks. The 43.6% average improvement over BC-exp on random-data tasks is striking because existing methods (DemoDICE, DWBC, OTIL, UDS) all fall below BC-exp in that setting. This directly demonstrates the paper's core claim that low-quality data can benefit OIL.

- **DRG analysis validates the claimed mechanism**: Section 4.3 defines Distance Reduction Gain and shows, on maze2d-medium-dense and maze2d-large-dense, that BCDP policies have positive expected DRG toward expert states, especially from states far from expert data, and achieve higher long-term returns from those states (Figure 4). This provides direct evidence that the method actually moves toward expert-observed states as intended.

- **Robustness to extremely scarce expert data**: Figure 3 demonstrates that BCDP significantly outperforms DemoDICE, OTIL, and DWBC when the expert set is only 1–5 trajectories. This is a practically important regime where the paper's approach is clearly differentiated.

- **Simple and reproducible design**: BCDP is a minimal modification of TD3+BC — it replaces the ground-truth reward with an expert-indicator reward and adds a BC term. The method's simplicity is a strength: it makes the contribution easy to understand, implement, and build upon.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theory-algorithm gap**: Proposition 1 motivates maximizing the expert-state distribution to improve the lower bound on return. The paper states it "implement[s] the proposition" via Q-learning with indicator rewards and BC, but no formal proof connects the actual loss (Equation 8-9) to the expert-state distribution maximization objective (Equation 7). The connection is intuitive — the Q-function with expert-indicator rewards propagates value through transitions that reach expert states — but the paper presents it as a direct implementation without a derivation. This is not a fatal flaw (the empirical results stand on their own), but the theoretical framing oversells the formality of the connection.

- **Overclaimed novelty**: The paper says it "make[s] the first attempt to demonstrate that low-quality data is also helpful for OIL." UDS (Yu et al., 2022) already showed that zero-reward labeling of unlabeled data works in offline RL, and BCDP is essentially a combination of UDS-style zero-reward labeling with a BC term and TD3+BC as the base algorithm. The paper acknowledges UDS (Section 3.3) but the claim of being "first" is too strong given the existing work. A more measured framing — e.g., "first to show this works in the pure OIL setting where no reward signal is available" — would be more accurate.

- **Adaptation of TD3+BC to the IL setting is underspecified**: The paper presents TD3+BC as an ablation baseline but does not explain how it was adapted to the imitation learning setting where ground-truth rewards are unavailable. TD3+BC normally requires reward-labeled data; the paper should clarify what reward signal was used (if any) for the TD3+BC baseline. Similarly, for the UDS baseline, the paper says "We have selected TD3+BC as our most similar offline RL algorithm" (line 175), implying UDS uses TD3+BC as its base, but this is not stated explicitly.

- **Hyperparameter α in Equation 9 is not discussed**: The objective in Equation 9 includes an α coefficient balancing the BC and Q-learning terms, but its value, how it was chosen, and whether it was tuned per task are not mentioned in the main text. (This may be in the appendix, which the parser strips.)

### Trivial
None.

## Nice-to-Haves

- **DRG analysis on locomotion tasks**: The transition-guidance mechanism is verified only on two maze2d navigation tasks. Showing that positive DRG also holds in locomotion (e.g., halfcheetah or hopper) would strengthen the claim that the method works as intended beyond navigation.

- **Clean ablation isolating the BC and Q-learning components**: The paper compares BCDP against UDS (which is "an ablation case of our method," line 183) and TD3+BC separately. However, a direct comparison of BCDP vs. (BC-only on expert data) vs. (Q-learning with zero reward only) in a single table would make the benefit of the combination more transparent.

- **Analysis of failure cases**: The paper mentions that in locomotion and manipulation "the agent may fail to transfer to the expert-observed states" (line 190) but does not analyze when this happens or how it affects performance. Acknowledging or characterizing these failure cases would strengthen the paper.

## Removed Points

- **Missing appendix content (Algorithm 1, hyperparameters, implementation details)**: The harsh critic repeatedly flags that Algorithm 1, hyperparameters, and implementation details are missing from the main text. Per policy: the parser strips these sections from all papers; they exist in the original submission. This criticism is removed.
- **"Figure 1 is referenced but not visible"**: This is a parser artifact from PDF-to-text extraction; the original submission contains the figure.
- **3 seeds being insufficient**: 3 seeds is standard practice in D4RL benchmarks; this is not a meaningful weakness.
- **Claims about DWBC/DemoDICE hyperparameter tuning**: The critic speculates that baselines may perform poorly due to "default hyperparameters, not a fundamental limitation" — this is speculation without evidence and is removed.
- **Missing related work references**: Per policy, I cannot verify or comment on missing related works.
- **Formatting/presentation nitpicks**: Removed per policy.
- Several generic strengths from the Strength Finder (e.g., "this paper addressed an important problem," "this paper targeted an interesting question") are removed as they are generic rather than specific to the paper's content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the theoretical contribution**: Drop the pretense that the Q-learning objective rigorously implements Proposition 1. Instead, present Proposition 1 as intuitive motivation and frame the algorithm as a heuristic that works well in practice. Alternatively, provide a formal derivation connecting the Bellman backup with expert-indicator rewards to the expert-state distribution objective.
2. **Tone down the novelty claim**: Replace "first attempt to demonstrate" with a more precise statement (e.g., "first to show this in the pure offline IL setting with no reward labels").
3. **Clarify baseline configurations**: Explicitly state which offline RL algorithm UDS uses, and describe how TD3+BC was adapted to the no-reward setting.
4. **Add DRG analysis on at least one locomotion task** to show the mechanism generalizes beyond navigation.
