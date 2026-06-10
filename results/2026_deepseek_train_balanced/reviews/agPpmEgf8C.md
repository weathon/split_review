Now I have thoroughly verified all claims against the paper text. Let me write the final consolidated review.

---

## Summary

This paper studies how predictive auxiliary objectives (a contrastive-style loss combining a prediction-matching term and a negative-sampling repulsion term) shape representations across modules of a deep RL system (double DQN), and draws analogies between these modules and brain regions: encoder → visual cortex, Q-network → striatum, prediction network T → hippocampus. The paper shows that predictive objectives prevent representational collapse in resource-limited networks, that longer prediction horizons improve transfer learning via better global structure preservation, and that the model produces several representational phenomena qualitatively reminiscent of neural recordings (place fields, backward shifts, T-maze splitting, V1 value-learning selectivity shifts).

## Strengths

- **Well-controlled demonstration that predictive objectives prevent representational collapse (Fig 1E–G).** The paper systematically varies the latent bottleneck |z| and shows that the model with $\mathcal{L}_{pred}$ maintains performance while the MF-only model collapses. The mechanism is directly measured: the MF-only encoder has a greater proportion of silent units and fails to separate state representations. This is a clean, parametric result.

- **Transfer learning experiments cleanly isolate the effect of prediction horizon (Fig 2A–E).** The finding that larger γ (longer predictive horizon) improves goal-transfer efficiency, and that this advantage scales with latent size, is well-supported. The mechanistic link is quantified: larger-γ models separate corner states more strongly in representational space and produce straighter latent maps in PCA. This goes beyond prior work by isolating *why* longer horizons help.

- **Honest characterization of regimes where prediction hurts (Fig 2F–H).** The paper identifies conditions (scrambled transition structure, less exploratory policy) where $\mathcal{L}_{pred}$ underperforms compared to a model using only negative sampling. This nuanced finding strengthens the paper's credibility and provides a concrete boundary condition.

- **Ablation/lesion-style experiments isolating the predictive objective (Fig 3C, Fig 4D).** The paper shows that removing $\mathcal{L}_{pred}$ eliminates or qualitatively changes the neural phenomena in the preference-swap experiment (encoder units) and the place-field formation (prediction network). These serve as functional "lesion" experiments within the model that go beyond correlation.

- **Quantified match to V1 value-learning data (Fig 4F–G).** The simulated Poort et al. (2015) experiment produces a statistically significant selectivity shift with a reported t-test ($t=-12.43$), and the paper quantifies the distribution of units preferring vertical vs. angled cues. This provides a specific, quantitative bridge between the RL encoder and visual cortex.

## Weaknesses

### Fatal

None.

### Major

- **T-maze hippocampal splitting comparison (Fig 3I) compares a trained network against a random one, invalidating the central neuroscience claim.** The caption explicitly states: "$T$ is randomly initialized for the model without an auxiliary objective." The claim that $\mathcal{L}_{pred}$ is necessary for the U-shaped splitting pattern (end-of-corridor splitting) rests on comparing cosine similarity of trained $T$ population vectors against random $T$ vectors. A random network trivially lacks structure regardless of the task conditions, so this comparison provides no evidence about what the predictive objective contributes. A proper control would require either training $T$ under a different objective or comparing *encoder* representations across conditions. Because this figure is presented as the single most important piece of evidence connecting the model to hippocampal data (the T-maze replication), its invalidity is a serious weakness.

- **The core claim that model representations "mimic the brain" relies almost entirely on qualitative visual comparison, not quantitative alignment with neural data.** The paper states in the abstract that "representational changes in this RL system bear a striking resemblance to changes in neural activity observed in the brain," yet the actual comparisons consist of visual inspection: place fields "look like" hippocampal place fields; selectivity changes "look like" those in visual cortex. No quantitative similarity metric (representational similarity analysis, centered kernel alignment, cross-validated encoding models, or any direct comparison to neural recordings) is used. The quantitative effects that are reported are very small in magnitude (median backward shift of −0.034 on a 28-state track; reward-proximal abundance effect of −0.06 vs. −0.02 for random shuffle), and their reliability across seeds is not reported beyond histograms. The paper's headline claim about brain-like representations is not commensurate with the strength of the evidence.

- **Most training hyperparameters are not reported, severely limiting reproducibility.** The paper does not report the learning rate, optimizer, batch size, replay buffer capacity, target network update frequency, the RL discount factor (distinct from γ in the predictive loss), the number of training steps/episodes, the specific loss weights found by the grid search, or architectural details of the CNN encoder (number and size of convolutional layers, MLP hidden size). The loss weights for $\mathcal{L}_Q$, $\mathcal{L}_+$, and $\mathcal{L}_-$ are described only as "chosen through a small grid search over the final episode score" but the actual values are never given. For a paper whose central results depend on the precise interaction of multiple loss terms, this is a significant reproducibility gap.

### Minor

- **The paper references a "decoder" at lines 52 and 70 but never defines one in the architecture.** The architecture section (line 44) specifies only an encoder $E$, a Q-network $Q$, and a prediction network $T$. No decoder, reconstruction loss, or reverse mapping from $z$ to observations is described. This is confusing: the reader cannot determine whether a decoder actually existed in the implementation, and if so, what it did. The paper also lists "decoder depth" as a parameter it will vary, but no such analysis appears in the results.

- **The negative sampling loss $\mathcal{L}_- = -\exp{||z_i - z_j||}$ is an unusual choice that is not justified or analyzed.** This loss is unbounded below — as $||z_i - z_j|| \to \infty$, $\mathcal{L}_- \to -\infty$, providing a driving gradient that never saturates and could destabilize training. The paper provides no comparison to standard alternatives (InfoNCE, margin-based losses), no stability analysis, and no justification for why this specific form was chosen. While the results suggest it works in practice, this remains a methodological gap that makes the approach harder to adopt or build upon.

- **The memory component for the T-maze task is introduced ad hoc with an unreported parameter.** The hand-crafted exponential trace of past observations $o_t + \alpha o_{t-1} + \alpha^2 o_{t-2} + \dots$ is not learned, and the value of $\alpha$ is not reported. No sensitivity analysis to $\alpha$ is provided. Given that the T-maze result is central to the paper's neuroscience claims, this omission weakens the analysis.

- **The preference swap experiment (Fig 4D) uses only 10 units.** This is a very small sample for a claim of statistical significance (t-test comparing means). The paper should justify why 10 units suffice, or report effect sizes and confidence intervals.

### Trivial

- The paper has a duplicated phrase on line 48: "to be structured to be structured."
- The negative sampling loss notation $\mathcal{L}_-$ appears to lack parentheses in the paper text, which could cause ambiguity in the mathematical expression.

## Nice-to-Haves

- Compare the model's representations against actual neural data using quantitative similarity metrics (e.g., representational dissimilarity matrices, CKA, or cross-validated encoding models) rather than purely qualitative visual comparisons. This would substantially strengthen the neuroscience claims.
- Run the T-maze comparison with a proper control: train a $T$ network under a different objective (or with $\mathcal{L}_{pred}$ but without memory) to isolate what the predictive objective specifically contributes to splitting.
- Compare the unusual negative sampling loss against standard alternatives (InfoNCE, margin-based contrastive loss) to validate the design choice.
- Report all training hyperparameters and loss weights to enable reproducibility.

## Removed Points

These points were flagged for removal during consolidation; they should be treated with caution:

- **Strength from Strength Finder #3** ("Models produce the specific U-shaped T-maze splitting pattern only when both memory and prediction are present"): Removed because it conflicts with the verified weakness that the MF-only baseline's $T$ network is randomly initialized, making the comparison uninformative. The claim cannot be supported by the current experiment.

- **Harsh critic's "Critical Issues" point 4 (core neuroscience claims entirely qualitative) downgraded from fatal-level severity**: While the concern is valid, many neuroscience modeling papers at ML venues make qualitative comparisons to published findings. The criticism is retained as a Major weakness (above), but the harsh characterization as "fatal" is removed. The paper's well-supported ML results (representational collapse, transfer learning) stand independently of the qualitative neuroscience claims.

- **Harsh critic's suspicion about the p-value in Fig 4F being "suspiciously extreme"**: Removed as speculative. A t-statistic of −12.43 with a large sample (pooled across 15 experiments) can legitimately produce such a p-value. Without access to the actual sample sizes, this concern cannot be verified.

- **Harsh critic's claim that the T-maze experiment "ad hoc" memory component weakens the narrative because it is "not trained"**: Retained as Minor but downgraded from the critic's framing. The hand-crafted memory is a reasonable simplification for a proof-of-concept; the main issue is the unreported α and missing sensitivity analysis, not that it is untrained.

- **Strength Finder's summary paragraph describing the T-maze result as "the single most important piece of evidence"**: This overstatement is rejected because the T-maze comparison is flawed. The paper's strongest evidence lies in the representational collapse and transfer learning experiments, not the T-maze result.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself does not already articulate.

## Suggestions

1. **Fix the T-maze experiment.** Replace the MF-only condition's randomly initialized $T$ with a properly trained alternative (e.g., train $T$ on a different auxiliary objective, or compare *encoder* representations across conditions). Without this fix, the central neuroscience claim about hippocampal splitting remains unsupported.

2. **Add quantitative neural similarity metrics.** Even without access to raw neural data, computing standard representational geometry measures (RDM correlation, CKA between model layers and published neural population statistics) would substantially strengthen the brain-comparison claims beyond visual inspection.

3. **Report all training hyperparameters and loss weights.** At minimum: learning rate, optimizer, batch size, replay buffer capacity, target network update interval, RL discount factor, and the specific weights for $\mathcal{L}_Q$, $\mathcal{L}_+$, $\mathcal{L}_-$ found by grid search.

4. **Resolve the decoder inconsistency.** Either remove the two references to a decoder (lines 52, 70) or, if a decoder was actually part of the implementation, describe it in the architecture section and clarify its role.

5. **Analyze the negative sampling loss.** Provide a brief justification for the $-\exp(||z_i - z_j||)$ form, report whether any training instability was observed, and consider comparing against a standard InfoNCE or margin-based alternative.

6. **Report $\alpha$ for the T-maze memory component** and add a sensitivity analysis showing how the splitting result changes with $\alpha$.

7. **Increase or justify the sample size** for the preference swap experiment (currently 10 units), and report effect sizes with confidence intervals.

## Score and Decision

<score>5.0</score>
<decision>Reject</decision>

**Justification**: The paper has a genuinely interesting core idea and its ML contributions (representational collapse prevention, transfer learning with varying horizons) are well-executed and informative. However, the paper's headline contribution — that the model's representations "mimic the brain" — is undermined by a flawed T-maze comparison (trained $T$ vs. random $T$) that invalidates one of the most specific neuroscience claims, and by the absence of any quantitative alignment with neural data across all other comparisons. The missing training hyperparameters and loss weights further limit reproducibility. At a top venue like ICLR, the evidence does not meet the bar for the strength of the claims made. The well-supported ML findings (Sections 3.1–3.2) could form the basis of a stronger paper that either tempers the neuroscience claims to the level of "analogous phenomena" or adds quantitative neural comparisons. The score of 5.0 (marginally below the acceptance threshold) reflects the genuine value in the ML experiments weighed against the neuroscience claims being unsupported in their current form.