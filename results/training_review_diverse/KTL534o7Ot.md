Now I have all the information needed to write the consolidated review. Let me carefully construct it.

---

## Summary

This paper introduces ProgSyn, a programmable framework for synthetic tabular data generation that supports logical constraints, statistical manipulations, differential privacy, and downstream fairness specifications within a single pipeline. The core idea is to pre-train a generative model (a GAN-like generator trained via marginal matching) on the original data, then fine-tune it using a differentiable loss automatically derived from user-provided declarative specifications. The paper introduces novel differentiable relaxations for logical constraints (via binary masks on Gumbel-softmax outputs) and conditional statistical operators, as well as a bilevel optimization approach for downstream specifications. Experiments on the Adult dataset demonstrate that ProgSyn can match or exceed specialized methods on fair synthetic data generation while also supporting specification types that prior work cannot handle.

## Strengths

1. **First unified, programmable framework for diverse synthetic data specifications.** ProgSyn is the first method to jointly support logical constraints, statistical manipulation, differential privacy, and downstream fairness within a single generative pipeline. The related work (Section 3) documents that prior specialized methods only cover isolated subsets, and Table 3 demonstrates stacking five different specification types simultaneously while retaining 84.0% downstream accuracy on Adult. This is a genuine architectural contribution.

2. **Novel differentiable relaxations for non-differentiable specifications.** The binary mask computation via matrix operations on the differentiable one-hot output (Section 4.2, "Logical Constraints") provides a clean way to convert logical constraints into a trainable loss. Table 2 shows this matters: fine-tuning+rejection-sampling (FT+RS) substantially outperforms rejection-sampling alone (RS) on harder constraints (e.g., I3 on Adult: 84.7% vs. 79.3% in the non-private setting). The extension to conditional statistical operators is also novel.

3. **State-of-the-art performance on fair synthetic data generation while being general-purpose.** Table 1 shows ProgSyn (non-private) achieving the highest accuracy and lowest demographic parity distance, outperforming specialized fair-data methods (DECAF, TabFairGAN) on both accuracy and fairness simultaneously. In the private setting (ε=1), ProgSyn also outperforms PreFair. This is notable because ProgSyn's fairness capability is just one feature of a general framework, not its sole purpose.

4. **Effective composability of diverse specifications.** Table 3 progressively adds five specifications of different types (fairness, statistical, logical) and shows accuracy degrading only from 84.7% to 84.0% while each target property is achieved. This directly supports the claim that programmable specifications can be combined without catastrophic interference.

## Weaknesses

### Fatal

None.

### Major

1. **Contradiction between DP guarantee and fine‑tuning objective (Eq. 1).** The paper states in Section 4.2 (line 85) that under DP, "fine‑tuning does not access the original dataset $X$." However, the fine-tuning loss in Eq. 1 is:
   $$\mathcal{L}_{\mathrm{fine}}(g_{\theta}(z), X, X_r) := \mathcal{L}_{M}(g_{\theta}(z), X) + \sum_{i=1}^n \lambda_i \mathcal{L}_{\mathrm{spec}}^{(i)}(g_{\theta}(z), X_r)$$
   Here $\mathcal{L}_{M}(g_{\theta}(z), X)$ computes TV distance between marginals of the generated sample *and the original dataset* $X$. The variable $X_r$ (which can be a DP‑safe sample) is used only in the specification terms, not in $\mathcal{L}_M$. The paper's textual claim and its mathematical formulation are in direct contradiction. If fine‑tuning uses $\mathcal{L}_M(g_\theta(z), X)$ as written, the DP guarantee during fine‑tuning is unsupported. This is the most serious issue in the submission and requires either correcting the equation or providing a clear DP‑aware modification of the fine‑tuning loss.

### Minor

1. **Imprecise "same fairness level" claim in the abstract.** The abstract states "at the same fairness level we achieve 2.3% higher downstream accuracy." In Table 1, ProgSyn achieves demographic parity 0.01 while DECAF achieves 0.04 — these are not the same fairness level. The paper's actual results (ProgSyn achieving *both* higher accuracy *and* lower parity than competitors) are stronger than the "same fairness level" framing suggests, but the specific claim is unsupported as written and should be corrected.

2. **Rejection sampling artifacts unreported for logical‑constraint experiments.** The paper reports results at "100% constraint satisfaction rate" (Table 2) but does not report the rejection rate, effective sample size after rejection, or whether the final sample size used to train the XGBoost evaluator is held constant across methods. If rejection discards many rows to reach 100% CSR, the training set shrinks, which could artificially lower downstream accuracy — especially in comparison with AIM's structural‑zeros approach, which generates a full‑size sample that inherently respects constraints. This gap weakens the confidence in the logical‑constraint comparisons.

3. **Under‑specified DP pre‑training adaptation.** The adaptation of McKenna et al.'s DP iterative framework is described in one sentence (line 66): "exchanging the original graphical model with our $g_\theta$" and modifying the budget adaptation step. No details are given about the privacy budget accounting, the per‑iteration $\varepsilon$ allocation, the number of iterations, or how the modified budget adaptation works. While the anonymized code may address this, the paper itself lacks sufficient detail for reproducibility.

4. **Under‑specified downstream surrogate training (bilevel optimization).** The downstream specification mechanism (Section 4.2) trains a surrogate classifier $h_\psi$ at each fine‑tuning iteration and propagates gradients through $\psi^*$ back to $g_\theta$. The paper provides no architectural details for $h_\psi$, no inner‑loop optimization parameters (steps, learning rate), and no analysis of gradient stability. The experiment showing sex‑predictability reduction to 50.2% suggests the idea works, but the missing analysis weakens the contribution.

5. **Stacking experiment (Table 3) does not report specification satisfaction.** Table 3 shows accuracy as specifications are progressively added, but does not report whether each specification is actually satisfied (e.g., achieved demographic parity, mean age, constraint satisfaction rates). The text claims "adhering to all customizations" without providing the verification metrics, making this claim unverifiable.

### Trivial

- None

## Nice-to-Haves

- **Evaluation metric breadth.** Using only XGBoost accuracy as a proxy for data quality is narrow. Adding marginal‑fidelity metrics (average TV distance on held‑out marginals) or ML efficacy across model types (logistic regression, MLP) would strengthen the claim that synthetic data quality remains high after customization.

- **Hyperparameter sensitivity analysis.** The paper mentions $\lambda_i$ are "selected on a hold‑out validation dataset" but gives no guidance on the selection procedure or sensitivity. For a framework with many knobs, demonstrating robustness or providing a default procedure would improve practical usefulness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Logical constraint mask is approximate due to Gumbel-softmax softness"** — The paper uses straight‑through Gumbel‑softmax, where the forward pass produces hard one‑hot vectors. The binary mask computation is therefore exact in the forward pass. The gradient uses the soft relaxation, which is standard practice and not a flaw.

- **"Statistical customization description too abstract"** — The description of computing normalized joint marginals from the masked subset, while concise, is at a standard level of detail for a conference paper and references prior work (Fischer et al., 2019) for the differentiable logic component.

- **"Missing results for Health Heritage, German Credit, and Compas"** — These results are described only in prose. Given that they were likely in an appendix that the parser strips (the paper says "we evaluated under the same setup" and mentions comparisons), this criticism is removed per the instruction to treat parser‑stripped appendix content as existing.

- **"Code and reproducibility concerns"** — The paper includes a reproducibility statement and anonymous code repository. Requests for complete hyperparameter tables in the main paper are standard but not a weakness given the code.

## Novel Insights

The most interesting insight emerging from these reviews is that the paper's core claim (programmable = general) is both its greatest strength and its most fragile point. The strength is that a single framework demonstrably outperforms specialized methods on fairness, handles logical constraints no other method can, and composes diverse specifications. The fragility is that each claimed capability (DP, fairness, constraints) comes with subtle complexities that the paper's unified presentation glosses over — the DP contradiction being the clearest example. This suggests that the real value of the paper may be less about a turnkey system and more about the demonstration that differentiable relaxation + fine-tuning can work across a surprisingly wide specification space. A paper reframed around this insight — showing *which* specifications are easy vs. hard to compose, where the trade-offs lie, and why fine-tuning helps — would be stronger than one claiming to solve all of them.

## Suggestions

1. **Fix the DP fine‑tuning contradiction.** The simplest resolution: clarify that during DP fine‑tuning, $\mathcal{L}_M$ is either dropped entirely (relying only on the specification losses and the DP pre‑trained initialization) or replaced with a version that uses a DP‑safe reference (e.g., a pre‑computed, noised marginal). Alternatively, if the implementation already handles this differently, correct Eq. 1 to match the actual algorithm.

2. **Correct the "same fairness level" claim.** Rephrase to accurately reflect what is demonstrated: "ProgSyn simultaneously achieves 2.3% higher accuracy and 2× lower demographic parity distance compared to the state‑of‑the‑art." Alternatively, add an experiment where $\lambda$ is tuned to match a competitor's exact parity, then compare accuracy.

3. **Report rejection statistics for logical‑constraint experiments.** For each constraint in Table 2, report the rejection rate and the effective sample size after rejection. If rejection discards many rows, either scale up the initial sample or subsample the baseline outputs to match.

4. **Add specification verification metrics to the stacking experiment (Table 3).** Report the achieved demographic parity, mean age, and constraint satisfaction rates for each specification as they are added, alongside accuracy.

## Score and Decision

**Overall assessment:** The paper presents a novel and ambitious framework with genuine contributions: the first unified programmable approach to tabular synthetic data generation, novel differentiable relaxations for constraints, and strong empirical results showing that a general framework can match or beat specialized methods. The core idea is sound, and the experimental evidence on the Adult dataset is compelling.

However, the submission has two significant weaknesses. **The DP fine‑tuning contradiction** (Eq. 1 uses $X$ while the text promises it does not) is a structural inconsistency that must be resolved for the DP claims to stand. **The "same fairness level" claim** is imprecisely worded. Additionally, several implementation details are under‑specified, and the rejection‑sampling comparison lacks necessary diagnostics.

These issues are fixable with revision (clarifying the DP fine‑tuning procedure, correcting claims, adding diagnostic statistics), and they do not undermine the core technical contribution — the framework architecture, the differentiable relaxations, and the composability results. The paper makes a real contribution to the field.

**Score:** 6.0

**Decision:** Accept (borderline; requires addressing the DP contradiction, the fairness claim precision, and adding rejection diagnostics)

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>