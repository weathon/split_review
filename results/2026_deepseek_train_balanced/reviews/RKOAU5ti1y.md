## Summary

This paper introduces UA-PbRL, an offline preference-based RL method that replaces the standard MLE-based Bradley-Terry reward learning with a MAP objective using a Beta prior to capture preference uncertainty, and couples the resulting distributional reward model with CVaR-based risk-averse policy optimization. The method is evaluated on Gridworld, PointMaze, robot control tasks, and LLM alignment. The core technical contributions include: (1) a MAP objective with an informative Beta prior for reward inference, (2) a variational inference procedure to learn per-trajectory Beta parameters, (3) an iterative reward refinement rule with a convergence guarantee (Theorem 4.1), and (4) integration with offline distributional policy evaluation and CVaR-based policy improvement.

## Strengths

1. **Novel MAP formulation with convergence guarantee.** The paper replaces the standard MLE objective (Eq. 1) with a MAP objective (Eq. 3) that incorporates prior information about preference uncertainty, and provides Theorem 4.1 guaranteeing convergence of the iterative update rule (Eq. 8) to the MAP optimum. This is a principled departure from prior PbRL work that provides a theoretical grounding for the reward update procedure.

2. **Controlled ablation study that isolates both proposed components.** Table 2 compares UA-PbRL against UA-PbRL-Uniform (removes the informative Beta prior) and UA-PbRL-Neutral (removes the CVaR objective). Both ablations outperform conventional PbRL on violations, and the full method improves over both ablations. This decomposition provides direct evidence that the distributional reward model and the risk-averse policy optimization are individually beneficial.

3. **Consistent CVaR improvement across multiple domains.** The method achieves higher CVaR₀.₁ rewards and fewer violations than five baselines (PbRL, EN-PbRL, ERS-PbRL, CPL, D-PbRL) across PointMaze (3 settings), Risky Ant, and Risky Swimmer, using 100 test episodes and 4 seeds per setting. The improvement targets worst-case performance, which aligns with the paper's stated goal.

4. **Clear visualization of the learned uncertainty signal.** Figure 2 demonstrates that in Gridworld, the distributional reward model assigns higher mean rewards but also higher variance to the risky region, directly illustrating that the model captures an uncertainty distinction between safe and risky areas.

## Weaknesses

### Major

1. **Experimental disconnect: tests environmental risk, not preference comparison sparsity.** The paper's central motivation (lines 14, 39–46) is that imbalanced comparison frequencies create epistemic uncertainty, which MLE ignores. However, in the PointMaze (line 268: "Gaussian noise added to transitions"), robot control (line 345: "transition subject to Gaussian noise"), and Gridworld (line 254: "stochasticity with p=0.1") experiments, "risk" is introduced via noisy environment transitions — aleatoric noise, not epistemic uncertainty from sparse comparisons. A trajectory could be compared a thousand times yet still pass through a noisy region. The paper presents no experiment where the *only* manipulated variable is comparison frequency while holding environment dynamics fixed. Without this, it is unclear whether UA-PbRL's success stems from the claimed MAP+prior mechanism or from the standard risk-averse properties of CVaR-based distributional RL applied to any noisy environment. The implicit chain (noisy transitions → diverse trajectories → preference sparsity) is plausible but never verified.

2. **Real human preference data results absent from main text.** The paper states (line 345) that it "assess[es] model performance with real human data" on D4RL tasks, but provides no summary statistics or numerical results in the main text, only an appendix reference. Since synthetic preference labels are a poor proxy for real human judgments, and the method's central motivation is about handling realistic preference uncertainty, the omission of these results — even as a brief table — is the single largest missing piece of evidence.

### Minor

3. **Conceptual fuzziness of the "prior."** The Beta distribution is presented as an informative "prior" \(p_0(\phi)\) (Section 4.2), but it is learned from the same preference data via variational inference (Eq. 6, where \(q_\psi(\phi|\tau)\) is trained to maximize the ELBo on the preference likelihood). This is an empirical Bayes approach, not a fully Bayesian treatment with a prior fixed before seeing the data. The claim (line 88) that Beta parameters "can be effectively interpreted as representing the count of positive and negative human feedback" is an analogy, not a derivation — no term in Eq. 6 explicitly ties \(\alpha_\tau,\beta_\tau\) to comparison counts. While the ELBo naturally sharpens the posterior with more data, the paper does not analyze whether the learned parameters actually encode comparison frequency as opposed to other statistical properties.

4. **LLM alignment evaluation is thin.** The LLM experiment (Section 6.4) evaluates on only 280 test samples across 14 harm categories (~20 per category), reports no numerical values or error bars in the main text (Figure 5 is a bar chart without numeric labels), and relies on GPT-4o as an automated judge — a method known to have imperfect correlation with human judgments. The comparison with DPL is handled superficially (line 369: DPL's effectiveness is "limited" because "preference labels typically share a unified objective to prioritize safety"), asserted without argument or evidence.

5. **Unusual training objective for the generative reward model has unanalyzed dynamics.** The loss function (Eq. 9) minimizes \(\|\hat{r}^K(\tau) - \hat{r}^0(\tau)\|^2\), where \(\hat{r}^0\) is sampled from the model and \(\hat{r}^K\) is its own iteratively refined version. This creates a self-distillation loop: the model is trained to predict outputs that are functions of its own samples. Theorem 4.1 addresses convergence of the iterative refinement for fixed reward values, but the coupling between sampling from \(f_\varphi^r\) and training via Eq. 9 is not analyzed. Stable convergence is not guaranteed in principle, and no ablation on the number of refinement steps \(K\) is reported.

### Trivial

6. The claim (line 29) that "none of the previous works have considered Preference-based RL (PbRL) from a distributional perspective" is an overstatement given that DPL (Siththaranjan et al., 2024), cited and discussed later, also learns a distributional reward model from preferences (albeit for hidden-context uncertainty rather than comparison sparsity). The paper should qualify this claim.

## Nice-to-Haves

- Design an experiment that isolates preference sparsity: create a fixed environment with no transition noise and vary only the number of times each trajectory is compared. This would directly validate that the MAP+prior mechanism captures comparison-frequency uncertainty.
- Compare against a count-based Beta prior heuristic (e.g., \(\alpha_\tau = 1 + \text{times preferred}\), \(\beta_\tau = 1 + \text{times not preferred}\)) rather than the learned neural network version. If they perform similarly, the neural network component may be unnecessary complexity.
- Report the missing D4RL human-preference results from the appendix in the main text.
- Report numerical values and error bars for the LLM evaluation, and use human evaluation on at least a subset of the test samples.

## Removed Points

These points from the inputs are moved here with justification:

- **"Low-resolution image makes verification impossible"** — This is a PDF parsing artifact, not a paper flaw. The original submission contains a properly formatted table.
- **"Proof not provided" (for Theorem 4.1)** — Proofs are standardly deferred to appendices; the appendix is stripped by the parser. This is not a valid weakness.
- **"Four seeds is too few"** — 4 seeds with mean±std is standard practice in the offline RL literature cited by the paper. While more seeds would improve rigor, this is a standard protocol rather than a deficiency.
- **"Missing hyperparameters"** — These are typically in the appendix (stripped). Not a valid criticism of the main text.
- **"Overall Assessment: fundamental experimental validity problem" (portrayed as fatal)** — Demoted from Fatal to Major because the experiments do test the method's ability to handle uncertainty in preferences (induced by noisy transitions), even if they do not isolate comparison-frequency uncertainty specifically. The method demonstrably works; the gap is between the specific motivational story and the evaluation design.
- **"The paper would need a completely redesigned experimental setup"** — Overstated; an additional experiment isolating comparison sparsity would strengthen the paper but the existing experiments still demonstrate the method's effectiveness on a relevant class of problems.
- **Strength Finder generic strengths** — Several strengths from the Strength Finder were removed as generic or overlapping. The ones retained are specific and evidence-grounded.
- **"Assumption 3.1 is oddly specific"** — It describes a plausible data-generation process for offline PbRL datasets; many PbRL papers make such modeling assumptions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add a dedicated experiment where environment dynamics are fixed and only trajectory comparison frequency is varied, to directly validate the claim that the Beta prior captures uncertainty from comparison sparsity.
- Report the D4RL human-preference results in the main text, even as a brief summary table, to substantiate the claim that the method works with real human feedback.
- Clarify the Bayesian framing: explicitly state that the Beta prior is learned via empirical Bayes (variational inference on the preference data), rather than presenting it as a fixed prior.
- Add an ablation on the number of refinement iterations \(K\) to demonstrate that the iterative update converges quickly and is robust to the choice of \(K\).
- Report numerical values alongside Figure 5 (LLM evaluation) and discuss the limitations of GPT-4o-based evaluation.

## Score and Decision

This paper proposes a technically coherent and novel combination of MAP-based reward learning, Beta-distributed priors for preference uncertainty, and CVaR-based risk-sensitive optimization for offline PbRL. The ablation studies are informative, and the empirical results show consistent improvement in worst-case performance across multiple domains. However, a significant gap exists between the paper's motivational emphasis on preference-comparison sparsity and the experimental design, which evaluates the method's response to environmental transition noise instead. The absence of D4RL human data results from the main text further weakens the empirical support. These issues are addressable but, as they stand, make the paper borderline for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>