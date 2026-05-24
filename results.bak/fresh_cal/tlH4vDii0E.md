Now I have all the information needed to produce a consolidated review. Let me write it.

## Summary

This paper proposes a method (CTL) for fine-tuning PLMs to learn robust causal representations using front-door adjustment. The key idea is to treat representations from a pre-trained model (R₀) and a fine-tuned model (R₁) as two environments sharing causal factors C while differing in spurious factors S, enabling identification of C via invariance learning. Token-level features Φ are used as a mediator for front-door adjustment via a shuffling operation. Experiments on sentiment analysis with injected spurious correlations show consistent improvements over SFT, SWA, and WISE baselines.

## Strengths

- **Creative use of PLM checkpoints as paired representations for causal identification**: Exploiting the pre-trained and fine-tuned versions of the same PLM as two "environments" (Assumption 2) to identify invariant causal features is genuinely novel. This addresses a practical limitation of multi-domain DG methods by requiring only a single training domain. The approach builds on von Kügelgen et al. (2021)'s Theorem 4.4, adapting it to the PLM fine-tuning setting.

- **Ablation results are consistent with the causal story**: The ablation variants CTL-N, CTL-C, and CTL-Φ behave as predicted if the causal graph were correct. Notably, CTL-Φ (using only local spurious features) closely tracks the spurious correlation shift — dropping from ~90% F1 at train to 12–19% at OOD 10% — while full CTL maintains 49–58%. This pattern supports the claim that the front-door adjustment mitigates spurious correlations.

- **Consistent empirical gains across settings**: In semi-synthetic experiments, CTL outperforms SFT by 7–9 F1 points at the strongest OOD shifts (10–30%). On the real-world experiment, CTL reaches 49.22 at OOD 10% vs. SFT 37.78 and SWA 47.41. Results are based on 5 runs with box plots showing consistent trends.

## Weaknesses

### Fatal
None.

### Major

- **The core identification derivation (Theorem 2) contains an unjustified step**: The derivation's first step claims P(y|do(x)) = P(y|do(s,c)) based on Assumption 1 (X = f(S,C)). In standard do-calculus, intervening on X (do(x)) sets the child to a constant but does not manipulate its parents S and C, whereas do(s,c) severs all incoming edges to S and C. These are fundamentally different causal regimes with no general rule equating them. The paper provides no justification for this step. Since the subsequent front-door derivation depends on the chain starting from do(c), the theoretical claim that P(y|do(x)) is identifiable via the given formula is unsupported as written. This is a genuine theoretical gap, not a presentation nitpick.

- **The shuffle operation lacks a formal connection to the front-door estimand**: Algorithm 1 shuffles Φ within mini-batches to obtain Φ', which is used in the front-door formula (Eq. 4). The paper provides no argument for why shuffling approximates the interventional distribution required by the front-door adjustment. The shuffle computes a marginal-like quantity under exchangeability assumptions within the batch, but this is not equivalent to the front-door estimand. The method may work as heuristic regularization (breaking Φ—X correlations), but the claimed link to causal identification is not established.

- **Marginal vs. substantial empirical gains over the strongest baseline**: On the real-world experiment, CTL's advantage over SWA is small at most OOD levels: 80.32 vs. 80.34 (OOD 70%), 70.08 vs. 69.63 (OOD 50%), 59.68 vs. 58.59 (OOD 30%), 49.22 vs. 47.41 (OOD 10%). At OOD 70%, SWA actually matches or slightly exceeds CTL. The gains are more substantial against the weaker baseline SFT, but the limited margin over a simple weight-averaging method raises questions about whether the complex causal machinery is driving the improvement.

### Minor

- **The "real-world" experiment still relies on constructed spurious correlations**: Platform identifiers ("amazon.xxx", "yelp.yyy") are appended to sentences to create a measurable spurious correlation. While more realistic than stop-word correlations, this is still an artificial injection. The paper's conclusion acknowledges this ("mechanisms through which spurious correlations emerge in complex, real-world environments remain unclear"), but the framing throughout claims "real-world" validation, which is overstated.

- **Statistical significance is not reported**: Results are given as means over 5 runs with box plots for some settings, but no standard deviations, confidence intervals, or significance tests are reported for the tables. Given the overlapping ranges visible in the box plots between CTL and SWA, this makes some of the claimed improvements less compelling.

- **Missing justification for label-conditional resampling**: Step 2 of Algorithm 1 samples ẋ and x̄ from the same label. This non-standard procedure is not explained or analyzed. It could affect convergence or introduce selection bias, but the paper does not discuss it.

### Trivial
None.

## Nice-to-Haves

- Providing standard deviations or confidence intervals alongside the mean F1 scores in Tables 1 and 2 would strengthen the empirical claims.
- An ablation without the shuffle (or an analysis of what the shuffle contributes) would help isolate its effect from other components.
- Clarifying which PLM architecture (BERT-base? RoBERTa?) was used would improve reproducibility — it appears in the experimental setup only implicitly.
- A discussion of why domain generalization methods requiring multiple domains (IRM, GroupDRO) are not applicable would preempt a natural question.

## Removed Points

These points were raised in the reviews but are removed or demoted after verification:

1. **"Paired representations assumption is incoherent"** — The harsh critic claims that a fixed X implies fixed S and C under X = f(S,C). This misunderstands the setup: R₀ and R₁ are learned *representations* (encodings) of X from different models, not the generative factors. The approach follows established causal representation learning (von Kügelgen et al., 2021), where the invariance is a property of the learned representations, not a claim about data generation. The paper could be clearer about this distinction, but the assumption is not incoherent.

2. **"Missing domain generalization baselines (IRM, GroupDRO, CORAL)"** — These methods require multiple *training* domains. The paper's setting is single-domain generalization, where only one training distribution is available. SWA and WISE are appropriate strong baselines for this setting.

3. **"Missing robust fine-tuning baselines (SMART, FLOW)"** — A reasonable request but not a fatal omission. SWA and WISE are established robust fine-tuning methods. The paper acknowledges the baseline selection.

4. **"Weakness about missing appendix content / unreleased code / unavailable models/datasets"** — These are removed per the hard rules. The paper states code will be released and cites standard datasets/models.

5. **"Pure formatting/style nitpicks and typos"** — Removed per hard rules (parser artifacts, not author errors).

6. **Strength Finder's "Principled front-door adjustment"** — Given the verified derivation issue, this strength is overstated. The *idea* of using PLMs for front-door adjustment is creative, but calling it "principled" conflicts with the identified theoretical gap. Rephrased more cautiously above.

7. **Strength Finder's generic statements** ("addressed an important problem", "this is a clever use") — Dropped as generic or lacking specific concrete evidence beyond what is already captured.

## Novel Insights

None beyond the paper's own contributions. The reviews raise important concerns about the theoretical derivation but do not contribute genuinely novel observations about the work that the paper itself does not already convey.

## Suggestions

1. **Fix the causal derivation**: The step P(y|do(x)) = P(y|do(s,c)) needs justification or replacement. Options: (a) Provide a valid do-calculus derivation that avoids this step, (b) Add an explicit assumption that makes it valid (e.g., bijective f, or equivalently that the decomposition is unique), or (c) Reframe the entire method as a *heuristic* inspired by causal reasoning without claiming formal identification of P(y|do(x)). Option (c) is the most honest and would still leave the empirical contributions intact.

2. **Justify the shuffle operation theoretically**: Even a simplified argument showing why shuffling Φ within the batch approximates the required marginalization would significantly strengthen the paper. Alternatively, replace it with a more principled estimator.

3. **Address the gap between theory and algorithm**: Currently, the paper presents a flawed theoretical claim (identification of do(x)) and a heuristic algorithm that might work for different reasons. Align these: either fix the theory to match the algorithm, or adjust the claims to accurately describe what the method does.

4. **Add proper uncertainty quantification**: Report standard deviations or 95% CIs for all tabular results, not just box plots for selected settings.

5. **Include an ablation without the shuffle**: This would isolate the effect of the shuffle from other components of the causal machinery.

## Score and Decision

The paper proposes a genuinely creative direction — using PLM checkpoints as paired environments for causal representation learning — and provides consistent empirical evidence that the approach improves OOD robustness. However, the core theoretical claim (identification of P(y|do(x)) via front-door adjustment) has a verifiable flaw in the derivation that is not a matter of presentation but of causal calculus. The shuffle-based implementation also lacks formal grounding in the claimed estimand. Until the theoretical foundations are corrected or the method is honestly reframed as a heuristic, the paper cannot be accepted at face value. The empirical contributions are valuable but do not, on their own, compensate for the unsupported theoretical claims that form the paper's main advertised contribution.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>