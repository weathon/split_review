Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final consolidated review.

---

## Summary

This paper tackles an important and underexplored problem in RL generalization: adapting not only to distribution shifts between source and target domains, but also to expansions of the state/action space (e.g., new enemies, new state variables, new actions). The proposed CSR (Causality-guided Self-adaptive Representation) augments a Dreamer-style world model with explicit causal binary masks \(D\) and a domain-specific change factor \(\theta_i\), forming a unified representation that can handle both types of change. A three-step strategy uses prediction error to decide whether to simply update \(\theta_i\) (distribution shift) or add new causal variables (space expansion), followed by causal graph pruning. Empirical results on simulated environments, CartPole, CoinRun, and 5 Atari games show CSR outperforming existing methods.

## Strengths

- **Novel problem formulation and method.** The paper identifies a genuine gap in existing generalization RL — most methods assume a fixed environment space. Unifying distribution shifts and state/action space expansions within a single causal world model (Eq. 2 with \(\theta_i\) and structural masks \(D\)) is a clean and well-motivated design that goes beyond prior work such as AdaRL and Dreamer.

- **Theoretical identifiability across settings.** The paper provides component-wise identifiability theorems (Thm 1–3, Corollary 4) for the latent variables, the domain-specific factor \(\theta_i\) (under linear transitions, Thm 2), and newly added state variables (Thm 3). This level of theoretical grounding is absent from most generalization RL work.

- **Strong empirical performance across benchmarks.** CSR achieves perfect 500.0 scores on all CartPole tasks (Table 1) while baselines fail or underperform, and attains the highest average final scores on all 5 tested Atari games (Table 2), often outperforming strong baselines like EfficientZero by substantial margins (e.g., 1586.9 vs. 557.4 on Alien).

- **Sample-efficient adaptation.** In CartPole, CSR requires only 2k–10k adaptation steps for target tasks, whereas Dreamer needs 50k and AdaRL requires 4k or fails entirely. This demonstrates that the causal representation and selective parameter updates enable genuinely low-cost transfer.

- **Ablation studies support the design choices.** Fig. 2c shows that including explicit structural masks \(D\) improves convergence speed and final reward. Fig. 2d shows the Self-Adaptive expansion strategy outperforms Random and Deterministic alternatives.

## Weaknesses

### Major

- **Unvalidated detection threshold.** The entire self-adaptive strategy hinges on a single threshold \(\tau^*\) set as the final prediction loss on the source task \(\mathcal{M}_1\) (line 182). The paper provides no sensitivity analysis, no controlled diagnostic experiments where ground-truth change type is known, and no analysis of when the detector misclassifies changes (false expansions vs. missed expansions). A large distribution shift could exceed the threshold and trigger unnecessary variable addition; a small space expansion could stay below it and be missed. This is the central mechanism enabling the "self-adaptive" claim, and its reliability is simply asserted without evidence. A controlled synthetic experiment with known ground truth is the minimum needed to demonstrate the mechanism works.

- **Gap between theoretical guarantees and practical implementation.** Theorem 2 requires linear transitions with additive noise for identifying \(\theta_i\) (explicitly stated as "in linear cases," line 99). Theorem 3 requires added variables to be differentiable functions of observations and rewards. The experiments involve pixel-based, highly nonlinear environments (Atari, CoinRun) where these assumptions are almost certainly violated. The paper does not discuss how the practical neural-network implementation relates to these theoretical conditions, nor does it provide any evidence that the learned causal variables are actually identifiable in practice. While theory under idealized conditions is valuable, presenting it without acknowledging the gap creates a misleading impression that the guarantees carry over to the reported results.

- **Missing comparisons with relevant baselines for space expansion.** The paper cites dynamic network methods (DEN, PackNet, APD) in related work (line 299) as addressing "sequences of tasks that require dynamical modifications to the network architecture," which is directly relevant to CSR's space expansion setting. Yet none of these are used as baselines. An oracle baseline that is told when space expansion occurs would also help calibrate the value of the detection mechanism. Without these comparisons, it is unclear whether CSR's advantage comes from its causal representation, its detection strategy, or simply from having an expandable architecture at all.

### Minor

- **Limited Atari evaluation without clear justification.** Only 5 of 26 Atari 100K games are tested, described as "representative" (line 289) without specifying why these five were chosen or how they represent the broader benchmark. While testing all 26 games is not expected, a reasoned selection criterion (e.g., diversity of space expansion scenarios) would strengthen the claim of generality.

- **CoinRun results lack statistical detail.** Only one learning curve is shown (Fig. 3b) without confidence intervals, error bars, or explicit statement of the number of random seeds. The CoinRun experiment section is a single sentence (line 287), making it difficult to assess the reliability of the reported advantage.

- **No quantification of computational overhead.** The paper acknowledges that the Self-Adaptive search step "requires extensive training time" (line 291) but provides no comparison of computational cost versus the simpler Deterministic or Random expansion strategies, nor versus any baselines. For a method whose contribution includes low-cost transfer, this is a notable omission.

- **Expansion strategy ablation is under-reported.** The comparison of three expansion strategies (Fig. 4d) is averaged across all environments without showing per-environment curves or specifying the number of runs. This makes it hard to assess whether the Self-Adaptive strategy's advantage is consistent or environment-dependent.

### Trivial

- None.

## Nice-to-Haves

- A controlled synthetic experiment with known ground-truth change type and magnitude, to directly validate the detection mechanism and measure its error rates.
- Sensitivity analysis varying the prediction-error threshold \(\tau^*\) around the chosen value.
- Per-environment breakdown of the expansion strategy comparison.
- Human-normalized scores for the Atari 100K benchmark to calibrate results against the broader literature.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Circularity of D masks"** (Harsh Critic's Other Observations): The claim that "pruning based on D may reinforce whatever structure the model already captured" is speculative and not grounded in a concrete technical failure. The D masks are optimized jointly with a sparsity regularizer (\(\mathcal{J}_{\text{reg}}\)), which is a well-defined objective — there is no demonstration of circularity.

2. **"POMDPs... not a distinct contribution"** (Harsh Critic's Other Observations): This is a scope nitpick. The paper never claims POMDP modeling as a contribution; it's the standard setting for world-model approaches.

3. **Request for all 26 Atari games as baselines**: Testing all 26 Atari games with a multi-task sequential protocol and multiple baselines would be impractical for an academic submission. The request constitutes scope creep.

4. **Request for CDL/GRADER as baselines**: These methods are cited as addressing exploration efficiency, not cross-task generalization/transfer (line 297). They are not directly comparable baselines for this paper's setting.

5. **"Implausibly clean" CartPole results**: Dreamer also achieves 500.0 ± 0.0 on Task 1 (Table 1), showing that zero variance on a solved deterministic task is standard, not implausible. The "minimum adaptation steps" column provides a second metric that differentiates methods.

6. **Generic complaint that baselines "are not designed for space expansion" so their failure is expected**: Comparing against methods that handle distribution shifts but not space expansion is a valid baseline choice — it shows exactly what CSR adds beyond existing methods. The missing comparison is with methods *designed* for space expansion, which is addressed in the Major weaknesses section above.

## Novel Insights

None beyond the paper's own contributions. The reviews identify gaps in validation rather than providing novel positive insights about the approach.

## Suggestions

1. Add controlled synthetic experiments where the ground-truth type and magnitude of environmental change are known, and the algorithm's decisions (update \(\theta_i\) vs. add variables) are recorded and compared against ground truth. Report confusion rates.
2. Perform a sensitivity analysis varying the prediction-error threshold and reporting how classification accuracy changes.
3. Add at least one comparison with a dynamic-network method (e.g., DEN or PackNet) and an oracle-guided expansion baseline.
4. Discuss the gap between the theoretical assumptions (linear transitions, differentiable mappings) and the practical neural implementation, clarifying what the theorems do and do not guarantee in the experimental setting.
5. Report statistical details for CoinRun (number of seeds, confidence intervals) and per-environment results for the expansion strategy comparison.

## Score and Decision

**Originality:** High — addressing space expansion alongside distribution shifts in a unified causal framework is genuinely novel.

**Importance of research question:** High — generalization across evolving task spaces is an important direction toward more flexible RL systems.

**Claims well supported:** Medium-Low — the central self-adaptive detection claim lacks direct validation; theoretical results are presented under assumptions that don't hold in experiments.

**Soundness of experiments:** Medium — results are promising and include ablations, but missing baselines and diagnostic experiments weaken the empirical story.

**Clarity of writing:** Medium — methodology is clearly described, but the gap between theory and practice is not discussed, and some experimental details are sparse.

**Value to the research community:** Medium-High — the problem formulation and causal framework could inspire follow-up work, but the current validation is insufficient.

The paper tackles a genuinely important problem and the core ideas are well-motivated. However, the central detection mechanism — which enables the claimed "self-adaptive" behavior — is not properly validated, the theoretical results are presented without acknowledging the gap to the experimental setting, and the empirical evaluation would benefit from stronger baselines. These are substantive issues that prevent the contribution from being fully established in the current form.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>