Here is the final consolidated review.

---

## Summary

This paper proposes COFlowNet, an offline training strategy for Generative Flow Networks (GFlowNets). The core idea is to define "unsupported flows" (edges involving states not seen in the training data) and add regularization terms that penalize flows on these unsupported edges (Eq. 4–5). A quantile matching extension (CQM) is introduced to improve candidate diversity. Experiments on Hypergrid and molecule design tasks show competitive performance against online GFlowNets that rely on proxy models, particularly under data scarcity — directly validating the paper's motivation that offline training can sidestep proxy model dependency.

## Strengths

1. **Clean definition and regularization of "unsupported flows" provides a principled approach to offline GFlowNet training.** The distinction between supported and unsupported edges (Section 3.2, lines 72–84) is conceptually clear and naturally suited to the flow-matching objective. The regularization terms $\mathcal{R}_{in}$ and $\mathcal{R}_{out}$ directly penalize flows on edges not present in the training data, providing an intuitive mechanism for constraining the model within the data distribution without resorting to actor-critic or Q-learning techniques that are ill-suited to GFlowNets (as argued in Section 2).

2. **Offline GFlowNet demonstrates practical advantages over online GFlowNets when proxy model quality is limited.** In the molecule design Data scarcity setting (Section 4.2.3), COFlowNet beats vanilla GFlowNet on most metrics. The paper also reports that QM-GFlowNet's performance "deteriorates more rapidly compared to COFlowNet" when data is limited. These results directly validate the paper's central motivation — that avoiding proxy-model dependency via offline training yields measurable benefits.

3. **Quantile matching extension yields measurable diversity improvements.** The ablation between FM-COFlowNet (flow matching without quantiles) and full COFlowNet shows that the quantile variant improves diversity by 10–20% (Section 4.2.3). The claim that COFlowNet generates "nearly 20 times as many candidate modes as MARS" provides concrete evidence of the diversity benefit attributable to the technical contribution.

4. **The evaluation protocol explicitly considers the proxy-vs-oracle gap.** Section 4.2.2 designs two settings (Fully trained with a strong proxy $\mathcal{P}_D$, Data scarcity with a weak proxy $\mathcal{P}_W$) to separately evaluate performance under different proxy quality regimes, with evaluation consistently conducted using the stronger proxy $\mathcal{P}_D$. This design is more thoughtful than evaluating all models on the same proxy used for training.

## Weaknesses

### Fatal

None.

### Major

1. **Theorems 1 and 2 are presented as formal proofs but the arguments are not rigorous.** This is the most significant weakness.

   **Theorem 1** (lines 94–108) claims that training with regularization yields smaller flows on unsupported edges than training without it. The "proof" writes the gradient of the regularized objective (Eq. 7), notes that the extra terms involve unsupported flows, and verbally asserts that these terms "only minimize flows not appear in the offline dataset." This does not constitute a proof of the claimed inequality $\hat{F}(s,s') \leq F(s,s')$ for any comparison of two training runs. The gradient expression alone does not establish that the regularized objective's minimizer satisfies this inequality, nor does it show that the additional gradient terms actually decrease unsupported flows rather than shifting mass in more complex ways. The concluding statement "We get ${\cal F}(\hat{s},s') = {\cal F}(s,s')$ only when $\alpha_1=0$ and $\alpha_2=0$" appears to confuse notation and is asserted without derivation.
   
   **Theorem 2** (lines 110–118) claims that minimizing unsupported inflow to a state increases supported inflow. The proof assumes that the total outflow from a state is constant ("$F(s_4, S_c)$ is constant and denoted as $F_o$"). This is unjustified: outflow from an interior node is a learned quantity that changes during training. The total reward mass at terminal states is globally conserved, but the distribution of flows through intermediate nodes is a property of the learned model, not a constant determined by the data. The argument conflates fixed terminal reward totals with learned intermediate flow allocations.
   
   The paper states "We next prove that applying the regularization will exactly decrease the unsupported flow and will not hurt the supported flow" (line 92), but the subsequent arguments do not deliver this proof. This gives the paper a veneer of theoretical rigor that the content does not support. The core intuition (regularizing unsupported flows is sensible) may well be valid, but it should be presented as a heuristic motivation or supported by empirical analysis rather than claimed as a proven theorem.

### Minor

2. **Key hyperparameter values and training details are absent from the paper.** The regularization introduces $\alpha_1$, $\alpha_2$ (Section 3.2), $N$, and $\hat{N}$ (Section 3.3) as free hyperparameters, yet none of their values are reported. Learning rate, batch size, number of training steps, and neural network architecture details are also missing. The paper states it follows "the experimental setting of Bengio et al. (2021)" (line 20), but the regularization terms introduce new parameters not present in that work. While code is provided (anonymous link), the paper itself should report these values for reproducibility.

3. **The molecule design evaluation in the Data scarcity setting conflates two factors.** In the Data scarcity setting (Section 4.2.2), COFlowNet is trained on $\mathcal{D}_S$ with **true oracle rewards**, while online models are trained with a **weak proxy** $\mathcal{P}_W$. Both are evaluated on the strong proxy $\mathcal{P}_D$. This means COFlowNet benefits from having ground-truth reward labels while online methods suffer from a poor proxy — so the comparison tests the combination of (a) the regularization method and (b) having access to true rewards rather than proxy estimates. A cleaner ablation would test COFlowNet trained on proxy-derived rewards from $\mathcal{P}_W$ (controlling for reward signal quality) to isolate the contribution of the regularization itself.

4. **No variance or statistical significance is reported.** Results are presented without confidence intervals, error bars, or multiple-seed runs. Claims that COFlowNet "beats" baselines on Top-k average reward or diversity are stated as definitive (e.g., lines 250, 255), but without variance information it is impossible to assess whether these advantages are reliable.

### Trivial

5. **Repeated spelling errors.** "offilne" appears at least seven times (lines 18, 22, 29, 30, 65, 67, 168, 207, 236) and "oracal" appears once (line 14). These should be corrected.

## Nice-to-Haves

- An analysis of how dataset coverage (e.g., the poor Random dataset performance on Hypergrid, Section 4.1.3) relates to the optimal setting of $\alpha_1, \alpha_2$ would deepen understanding of the method's sensitivity to data quality.
- The claim that existing offline RL methods "cannot be directly applied" (Section 1) could benefit from a more detailed analysis or empirical demonstration (e.g., showing that CQL or IQL fails when applied to GFlowNet training objectives).

## Removed Points

The following points raised by the reviewers were filtered:

1. **"Section 1 analysis of offline RL is superficial"** — The paper provides specific reasoning for each category (actor-critic, Q-learning, policy constraint) in 3–4 sentences each (lines 18, 30). The level of analysis is appropriate for a method paper motivating its approach. REMOVED as an unfair scope-creep criticism.

2. **"Notation for unsupported flows is unnecessarily indirect"** — This is a style preference, not a substantive weakness. REMOVED.

3. **"Quantile matching motivation is unexplained"** — The paper cites prior work (Zhang et al., 2023d) establishing that quantile matching improves diversity over deterministic flow matching. This is sufficient attribution. REMOVED.

4. **"Hypergrid experiment missed opportunity to test proportional sampling"** — The paper does test proportional sampling via $\ell_1$ error (Section 4.1.3, lines 200–209) and reports that COFlowNet "can also get close to the goal of GFlowNets." REMOVED (factually incorrect criticism).

5. **"Table 1 numerical values not readable (embedded in figure)"** — This is a PDF parsing artifact. The original submission has a properly formatted table. REMOVED.

6. **"Theorems are a strength (from Strength Finder)"** — This conflicts with a verified weakness (the proofs are not rigorous). Per instructions, when a strength and weakness disagree, the weakness wins. REMOVED.

7. **"No offline GFlowNet baselines from prior work"** — The paper explicitly claims to be the first offline GFlowNet training strategy ("a pioneering offline training strategy," line 22). The COFlowNet w/o ablation serves as a within-method baseline. There are no prior offline GFlowNet methods to compare against. REMOVED.

8. **"Missing appendix content / missing proofs in appendix"** — The parser strips appendices from all papers; the original submission likely contains this content. REMOVED.

## Novel Insights

None beyond the paper's own contributions. The key insight — regularizing flows on edges not supported by the training data, with a quantile extension for diversity — is the paper's own contribution, and the reviews do not surface additional novel perspectives beyond what the paper itself articulates.

## Suggestions

1. **Downgrade Theorems 1 and 2 to heuristic motivations or intuitions** and replace them with a rigorous empirical analysis. A controlled experiment on Hypergrid showing that the regularization shifts probability mass from unsupported to supported trajectories (and measuring how much) would be more convincing and more honest than the current "proofs."

2. **Report all hyperparameter values** ($\alpha_1$, $\alpha_2$, $N$, $\hat{N}$), training details (learning rate, batch size, architecture), and numerical results from Table 1 in the main text.

3. **Add a controlled experiment where COFlowNet is trained on proxy-derived rewards** (from $\mathcal{P}_W$) in the Data scarcity setting, to isolate the contribution of the regularization from the advantage of having true oracle rewards over proxy estimates.

4. **Run experiments with multiple seeds and report confidence intervals or standard deviations** for the key metrics (Top-k average reward, diversity) to establish statistical reliability.

## Score and Decision

The paper identifies a genuine problem and proposes a clean, well-motivated method. The empirical results on molecule design under data scarcity are the paper's strongest contribution, directly validating its central motivation. However, the paper significantly overstates its theoretical backing: Theorems 1 and 2 are presented as formal proofs but contain non-rigorous arguments that do not establish the claimed results. For a top venue, this gap between claim and substance is a major flaw. Missing experimental details and a confounded evaluation comparison further weaken the contribution. The core idea has merit, but the paper in its current form needs substantial revision — primarily to either remove or honestly characterize the theoretical claims — before it is suitable for publication.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>