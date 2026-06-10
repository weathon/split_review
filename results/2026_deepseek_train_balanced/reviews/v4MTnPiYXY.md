## Summary

The paper proposes Q-SFT, an offline RL algorithm that casts Q-learning as a weighted cross-entropy (WCE) objective on the token logits of pretrained language/vision-language models. By learning Q-values as probabilities directly from the model's existing output distribution — instead of via a separate value head with reset weights — the method aims to preserve the benefits of pretraining while enabling value-based multi-turn RL. The authors provide a theoretical guarantee (Theorem 1) that the learned probabilities are conservative estimates of the optimal Q-function, and evaluate across language games, dialogue, web tasks, embodied navigation, and robotic manipulation.

---

## Strengths

- **Novel algorithmic formulation that bridges SFT and Q-learning.** The paper replaces the standard TD regression loss (Eq. 1) with a weighted CE loss (Eq. 6) where weights are Bellman target values. This is a clean and well-motivated departure from prior value-based methods — the objective is structurally identical to SFT, which directly addresses the instability from regressing to non-stationary targets (Farebrother et al., 2024).

- **No architectural modifications for value-based fine-tuning.** Q-SFT learns Q-values as probabilities from the existing logits of a pretrained model, requiring no new value head or weight reinitialization (Figure 1, lines 181–182). This is a genuine practical advantage over ILQL and similar methods that add a randomly initialized value head.

- **Theorem 1 provides a conservatism guarantee.** The paper proves that optimizing the WCE objective yields probabilities satisfying \(Q^*(s, a) \geq \hat{p}_\theta(s, a) \geq Q^*(s, a) \pi_\beta(a \mid s)\) for actions with sufficiently high Q-values. This theoretical bridge between weighted-CE and value-based RL guarantees is a concrete advance.

- **Broad and diverse empirical evaluation.** The paper evaluates across six distinct domains (language games, dialogue, web shopping, embodied navigation, robotic manipulation) using both LLMs and VLMs — an unusually comprehensive suite that tests the method's generality.

- **Scaling experiment isolates the pretraining-utilization benefit.** Figure 3 (20Q task with varying model sizes on 10% data) shows that Q-SFT's advantage over ILQL grows with larger pretrained models, providing targeted evidence for the central claim that the method leverages pretrained logits better than prior value-based approaches.

---

## Weaknesses

### Major

- **No measures of uncertainty or statistical significance anywhere in the empirical section.** All tables (1–3) and figures report single numbers without standard deviations, confidence intervals, or any error metric, despite noting "100 independent evaluations." Many reported improvements are modest (Chess: 0.15 vs. SFT 0.11 vs. ILQL 0.09; ALFWorld Pick: 39 vs. SFT 38 vs. ILQL 28; robotic Place Object Near Target: 64 vs. QT 68, where Q-SFT underperforms). Without variance estimates, the reader cannot assess whether the reported differences are meaningful or within noise. This directly undermines the comparative claims that form the empirical core of the paper.

- **No ablation studies or hyperparameter sensitivity analysis.** The method has several design choices — the behavior policy estimate \(\pi_\phi\), the Q-probability model \(p_\theta\), the target network update rate \(\alpha\), the inference-time temperature \(\beta\), and the label-smoothing term distributing residual probability across all other actions — none of which are ablated. The \(\beta\) hyperparameter (line 238) is described as "tunable" but no experiment shows how performance varies with its choice. Without ablations, it is difficult to attribute Q-SFT's performance to any specific component of the algorithm or to assess robustness.

### Minor

- **The theoretical guarantee is weaker than the paper's framing suggests in several ways.** (i) The lower bound is \(Q^*(s,a)\pi_\beta(a|s)\), which approaches zero for actions the behavior policy rarely takes — precisely the actions where Q-learning would need to generalize beyond the data. (ii) The guarantee only holds for actions with \(Q^*(s,a) \geq 1/(|\mathcal{A}|-1)\), which for large vocabularies (50K+) is a nontrivial restriction. (iii) The theorem is proven for the true Bellman likelihood operator (Eq. 188), while training uses the empirical operator (Eq. 169). The paper sketches a concentration-inequality adaptation (lines 190–195) but does not provide the adapted result. These limitations are acknowledged (line 207) but collectively narrow the practical scope of the theoretical contribution.

- **Two practical concerns about the loss formulation are not discussed.** (a) The denominator \(|\mathcal{A}|-1\) in the label-smoothing term of Equation 173 distributes residual probability mass across "all other actions." For vocabularies of 50K+ tokens, each term is numerically very small, and the summed gradient contribution across all actions has computational and numerical implications that are not addressed. (b) The Bellman operator (Eq. 169) requires dividing by \(\pi_\beta(a'|s')\), which can be arbitrarily small for rare actions, raising numerical stability concerns. No clipping, smoothing, or regularization for this term is mentioned.

- **The Chess and Wordle experiments disable the method's claimed pretraining advantage.** The paper states (line 382–383) that weights are randomly reinitialized on these tasks because the state/action spaces are "unlike natural language." This means these experiments test only the weighted-CE-vs.-TD-regression algorithmic mechanism, not the central claim of leveraging pretrained logits. The paper is transparent about this, but these results are presented in the same tables used to argue for Q-SFT's overall superiority, which conflates two different sources of potential improvement. The paper would benefit from a cleaner separation or an explicit statement of what each experiment tests.

- **Missing comparison to Decision Transformer (DT).** The related work discusses DT and RCSL methods at some length (lines 77–80), arguing that Q-SFT is theoretically superior because it enables trajectory stitching. Yet DT is not included as an experimental baseline, even though it is arguably the most relevant RCSL competitor for language tasks and is directly related to the method's claimed advantage.

### Trivial

None.

---

## Nice-to-Haves

- An experiment that directly isolates the pretraining-utilization benefit — e.g., comparing Q-SFT vs. ILQL on a language task both with and without GPT-2 initialization, to show the advantage grows when pretrained weights are used.
- A baseline that starts from the same pretrained logits but uses a standard Q-learning objective (e.g., ILQL with a tuned value head) to clarify whether Q-SFT's advantage comes from the loss function change or from avoiding the value head.
- Discussion of how \(\beta\) was set across experiments and a sensitivity analysis over a reasonable range (e.g., 0.01–10.0).
- Clarification of whether ILQL on Chess/Wordle also used reinitialized weights or retained GPT-2 initialization, to ensure a fair comparison.

---

## Removed Points

These points were raised by reviewers but are removed after verification against the paper text:

- **"ILQL also initializes from GPT-2, so the claim that value-based methods 'discard' pretrained knowledge is overstated."** — The paper's claim (line 36) is specifically that Q-learning "discard[s] the learned *likelihoods*" (not representations), and ILQL's separate randomly initialized value head does indeed discard the pretrained logits/likelihoods. The paper is precise about what is discarded.
- **"ReAct scores 0 on Chess, which is suspicious."** — The scoring gives 0 for a legal non-winning move and -1 for illegal moves. ReAct (prompted GPT-3.5) achieving 0 against a Stockfish opponent is entirely plausible and not suspicious.
- **"ILQL may not be well-tuned on ALFWorld."** — This is speculative; the paper does not provide tuning details for either method, and the asymmetry cannot be verified from the paper.
- **"The paper overstates the dichotomy between value-based methods and SFT."** — The paper explicitly states the limitation (value-based methods retain representations but discard likelihoods) rather than claiming representations are entirely discarded.
- **Missing appendix/proofs details.** — The parser strips appendix content from all papers; these exist in the original submission.

---

## Novel Insights

The reviews surface an interesting tension in the paper's empirical design: the tasks that best demonstrate Q-SFT's pretraining-utilization advantage (language tasks, scaling experiment on 20Q) are also the tasks where the paper lacks error bars and ablations, while the tasks that have cleaner experimental controls (Chess/Wordle with reinitialized weights) are the tasks where the central claim about pretraining is disabled. The paper would be substantially strengthened by a single controlled experiment that varies whether pretrained logits are retained vs. reinitialized on the same language task, directly isolating the effect that the method claims as its main advantage.

---

## Suggestions

1. Add standard deviations or confidence intervals (over at least 3–5 seeds) to **all** tables and figures. Without this, the empirical claims cannot be verified at the standard expected by a top venue.
2. Include ablation studies for at least the inference-time temperature \(\beta\) and the label-smoothing mechanism (dummy action vs. uniform distribution over other actions).
3. Add Decision Transformer as a baseline for the language tasks, since the paper contrasts against RCSL methods in the related work.
4. Address the numerical stability concern for the \(\pi_\beta\) division in the Bellman operator (Eq. 169), and discuss the computational implications of the \(|\mathcal{A}|-1\) denominator for large vocabularies.
5. Add an explicit experiment that isolates the pretraining-utilization benefit by comparing Q-SFT with vs. without reinitialized logits on the same language task.

---

## Score and Decision

This paper proposes a genuinely novel and well-motivated algorithm with a clean theoretical connection between weighted cross-entropy and conservative Q-learning, and evaluates across an admirably broad set of domains. However, the empirical evidence is not presented at the rigor expected for a top conference: the complete absence of any uncertainty quantification across all experiments makes it impossible to assess the reliability of the reported improvements, and the lack of ablations prevents attribution of performance to specific design choices. The core contribution has genuine promise, but the current empirical base needs substantial strengthening.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>