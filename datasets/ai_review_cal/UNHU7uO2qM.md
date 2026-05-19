- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper and can verify all reviewer claims. Let me construct the consolidated review.

## Summary

This paper proposes DRAGO, a method for continual model-based reinforcement learning that combines (1) **Synthetic Experience Rehearsal** — using a continually-learned generative model (VAE) and a frozen old dynamics model to generate synthetic training transitions from prior tasks without storing data — and (2) **Regaining Memories Through Exploration** — an intrinsic reward that encourages the agent to revisit states where the old dynamics model predicts accurately but the current one does not. The method is evaluated on MiniGrid, Cheetah, and Walker domains with task sequences sharing dynamics but differing in rewards/initial states. The central claim is that DRAGO preserves and aggregates world-model knowledge across tasks without storing past data.

---

## Strengths

1. **Direct qualitative evidence of knowledge retention (MiniGrid).** Figure 4 visualizes the world model's prediction MSE over the entire gridworld after each task. DRAGO maintains low error across all rooms, while naive continual TDMPC forgets earlier rooms almost entirely. This is a direct measure of retention (dynamics prediction accuracy) for one domain.

2. **Consistent improvement over baselines on transfer tasks across three domains.** Figure 5 shows that DRAGO achieves higher or comparable cumulative reward than all baselines (Continual TDMPC, EWC, Scratch) on test tasks requiring knowledge from multiple prior tasks, in MiniGrid, Cheetah, and Walker.

3. **Strong few-shot transfer performance.** Table 1 reports that DRAGO achieves the best mean cumulative reward in 6 out of 8 test tasks after only 20 episodes, with competitive performance in the remaining two, demonstrating the practical value of the retained world model under limited interaction.

4. **Ablation confirms both components contribute positively.** Figure 6 shows that removing either Synthetic Experience Rehearsal or Regaining Memories Through Exploration degrades performance relative to the full method, though the gap varies across tasks. The ablation validates the complementary roles of the two mechanisms.

5. **Novel combination of generative rehearsal and exploration-based intrinsic rewards for data-free continual MBRL.** The approach of using a continually-learned VAE + frozen old dynamics model to generate synthetic training data (Section 3.1) and coupling it with an exploration intrinsic reward that targets "familiar-but-forgotten" regions (Section 3.2) is a genuinely new design for the continual MBRL setting without replay buffers.

6. **Well-motivated problem formulation.** The paper clearly defines a setting where tasks share dynamics but differ in rewards/initial-state distributions, and past data is unavailable (Section 2). This setup is directly addressed by DRAGO's design, and the experiments are structured to test the claimed capabilities.

---

## Weaknesses

### Fatal
None.

### Major

- **Retention evaluation is predominantly indirect.** The paper's central claim is knowledge retention without storing past data, but the primary quantitative evidence (Figures 5, Table 1) measures *transfer performance on new tasks* — a proxy for retention, not a direct measure. Strong transfer is *consistent with* retention but has alternative explanations (e.g., reduced plasticity loss, fast adaptation). Figure 4 provides direct qualitative evidence for MiniGrid (prediction MSE heatmaps), but quantitative retention metrics — such as dynamics prediction error on held-out data from each prior task at each stage — are absent for Cheetah and Walker. This gap means the core claim about retention is primarily supported through indirect evidence. The paper would be substantially strengthened by adding direct retention metrics across all domains.

### Minor

- **Missing experimental protocol details.** The training horizon/number of steps for the main experiments (Figure 5) is not specified. It is also unclear whether hyperparameters were retuned per transfer task or fixed throughout. This makes it difficult to assess evaluation fairness.

- **Learning curves lack error bars.** Figures 5 and 6 show training curves without confidence intervals or standard deviations, limiting the assessment of statistical significance given the inherent noise in RL. (Table 1 does report means and standard deviations, which is good.)

- **No sensitivity analysis for key hyperparameters.** The weighting factors λ (Eq. 5, controlling synthetic data loss) and α (Eq. 7, balancing the two terms in the intrinsic reward) are not studied. Without sensitivity analysis, it is unclear whether the method requires careful per-domain tuning or is robust to these values.

- **Limited ablation scope.** The ablation (Figure 6) covers only two domains and four transfer tasks. On Cheetah jump-and-run forward, the gap between full DRAGO and "w/o Rehearsal" is small. The ablation would benefit from broader coverage across all three domains.

- **Functional form of intrinsic reward not justified or ablated.** The intrinsic reward in Eq. 7 (log of absolute prediction error passed through a sigmoid, with a subtractive penalty term) is presented without justification for this specific design choice or an ablation comparing it to simpler alternatives.

- **Separate "reviewer" adds model capacity without discussion.** The reviewer module (separate reward model, value model, and policy for the intrinsic reward, Section 3.3) increases total model capacity compared to baselines. The paper does not discuss whether this asymmetry is controlled for or whether the performance gain is partly attributable to extra capacity.

- **No analysis of generative model quality.** The method relies on a continually-trained VAE to produce synthetic state-action pairs, but there is no analysis of how synthetic data quality evolves across tasks, whether errors compound, or how sensitive results are to VAE fidelity (the paper only mentions leaving more sophisticated generative models like diffusion models to future work).

### Trivial
None.

---

## Nice-to-Haves

- Add direct retention metrics: for each domain, after training on task *i*, measure the dynamics model's prediction error on a held-out set of transitions from each previous task *j < i*. This would directly quantify forgetting and complement the transfer results.
- Analyze synthetic data quality over the task sequence (e.g., sample diversity, distributional match to real prior data).
- Study sensitivity to λ and α and report their chosen values.
- Add error bars / confidence bands to the learning curves in Figures 5 and 6.

---

## Removed Points

These points were raised by one or both reviewers but are removed per the filtering guidelines:

- **"Bayesian derivation in Section 3.1 is unnecessary/forced"** — Style/presentation nitpick. The derivation does not harm clarity and does not affect the paper's technical contribution.
- **"A sufficiently expressive dynamics model should not forget when dynamics are identical across tasks"** — This reflects a misunderstanding of neural network optimization under input distribution shift. The paper empirically demonstrates that forgetting *does* occur (Figure 4) and correctly motivates the problem.
- **"Missing reproducibility details (network architectures, exact hyperparameter values, number of gradient steps per task, training schedules)"** — Per guidelines, criticisms about undisclosed hyperparameters and trivial implementation details that are impractical to fully enumerate in a conference paper are removed. The key missing protocol detail (number of training steps per task) is retained as a Minor weakness above because it affects interpretation of the evaluation.
- **"Could the paper be strengthened by using more sophisticated generative models?"** — The paper explicitly acknowledges this as future work (Section 3.1, line 102). Criticizing an acknowledged limitation is not a valid weakness.
- **Strength Finder's generic framing ("this paper addressed an important problem")** — Removed as generic/superficial; the specific well-motivated problem setup is retained as Strength #6.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine evidence gap (retention is measured primarily via transfer proxies) and several missing experimental details, but these are observations about the paper's presentation rather than novel insights into the problem itself.

---

## Suggestions

1. **Add direct retention metrics.** For each domain, after sequential training, evaluate the learned dynamics model's prediction error on held-out data from each prior training task. This would directly support the paper's central claim and is feasible without additional data collection.

2. **Report the training horizon/number of steps for the main results** and clarify whether hyperparameters were fixed or retuned per transfer task.

3. **Add error bars to Figures 5 and 6**, or report the number of random seeds used and indicate whether curves are averages or single runs.

4. **Include a sensitivity analysis** for λ (Eq. 5) and α (Eq. 7) — at minimum, report the chosen values and briefly discuss their effect.

5. **Discuss the capacity asymmetry** between DRAGO's reviewer-augmented architecture and the baselines, or provide an ablation controlling for total parameter count.

---
