## Summary

This paper addresses CoT monitorability in reasoning models, focusing on two properties: *faithfulness* (whether the model's reasoning trace honestly reflects what influenced its answer) and *conciseness* (whether traces are brief enough to be effectively monitored). The core contribution is a prior-guided distillation pipeline (Algorithm 1) that uses an instruction-tuned model (Qwen 2.5-7B) to transform unmonitorable reasoning traces from a small base model (DeepSeek R1 Qwen-1.5B) into high-quality ones, filtering for task accuracy and monitorability, then fine-tuning the base model on the resulting dataset via SFT. The paper demonstrates convincing conciseness results (11.6% → 96.6% of MATH500 responses under 950 tokens) and more modest faithfulness gains (15.2% → 25.0%), alongside a mathematical explanation of why naive RL fails.

---

## Strengths

- **Rigorous diagnosis of RL failure with both theory and empirics.** Section 3 provides a clean mathematical argument (Eqs. 4–5) showing that the monitorability gradient term $L_1$ collapses when $f(z) \approx 0$ under the base policy, which is directly confirmed by Figure 2's flat faithfulness and conciseness curves across training. This is the cleanest motivation for the proposed approach.

- **Proof-of-concept isolation of sparsity as the problem.** Figure 3 cleanly demonstrates that when the prior-transformed trace $z_s$ is presented to the *unchanged* base model $\pi_0$, faithfulness jumps to 85% and conciseness to 96.6% while accuracy is preserved. This rigorously separates "the base model is incapable" from "the base model rarely samples monitorable traces" — a key premise of the whole pipeline.

- **Drastic and credible conciseness results.** Figure 5 and Figure 6 together show that the fine-tuned model achieves 80%/96.6% conciseness on GSM8K/MATH500 (from 24.1%/11.6% baselines), with the entire length distribution shifting leftward (Figure 6). The accuracy drop is "within ~10% relative," which is explicitly acknowledged. This result is concrete, convincing, and substantiated by two benchmarks.

- **Consistent improvement across all hint categories for faithfulness.** Figure 4 shows the trained model outperforms all baselines (direct prompting, indirect prompting) across every one of the six faithfulness categories, ruling out that gains are category-specific.

---

## Weaknesses

### Fatal
None.

### Major

- **Faithfulness metric is a behavioral proxy, not a test of causal influence, yet is framed as a core contribution.** The faithfulness signal is $f(z) = \mathbb{1}\{\text{hint verbalized in } z\}$. The prior policy is explicitly instructed to write the hint into the trace. SFT then teaches the base model to imitate those traces. The evaluation then checks hint verbalization. Training teaches verbalization; evaluation rewards verbalization. This is closed-loop: a model that copies injected text into every CoT would achieve 100% by this metric regardless of whether the hint influenced the final answer. The paper provides no experiment that probes causal dependence (e.g., removing the hint for questions where the trained model verbalized it and checking whether accuracy drops). Section 6 acknowledges "our faithfulness metric relies partly on LLM-as-a-judge evaluations," but does not address the deeper circularity. The paper's headline result — "improves faithfulness by 10%" — would be substantially stronger with this one additional experiment; without it, the result demonstrates learned verbalization behavior, not genuine reasoning transparency.

- **The actual faithfulness improvement is modest relative to the oracle, though framing obscures this.** The trained model achieves 25.0% vs. a baseline of 15.2%, while the oracle ("Using Prior") achieves 85.0% (Figure 3). The gap between baseline and oracle is ~70 percentage points; the trained model closes ~10 of those points. Framing this as a "67% relative improvement" (Figure 4 caption) is arithmetically correct but misleading: the trained model remains unfaithful on 75% of test cases and captures only ~14% of the available improvement. The paper's abstract claims "improves faithfulness by about an additional 10%" which is accurate, but the "67% relative" framing in the body should be contextualized against the 85% oracle ceiling.

### Minor

- **Notational inconsistency in Algorithm 1's filter condition for faithfulness.** Line 13 reads: "Keep only $z_{si}$ such that $f(z_{si}) \leq \beta$ and $R(x, y_i) = R(x, y)$." For conciseness, $f(z)$ is a binary indicator or a length value and $\beta$ is a length budget, so the inequality approximately makes sense. For faithfulness, $f(z) = \mathbb{1}\{\text{hint verbalized}\} \in \{0,1\}$ and one wants $f(z_{si}) = 1$, but the condition $f(z_{si}) \leq \beta$ with $\beta = 1$ is trivially satisfied by all samples. The filter requires opposite directions of $f$ for the two objectives, but the same inequality is used throughout. The paper does not clarify how the filter is implemented for the faithfulness case, creating a reproducibility ambiguity for the core algorithm.

- **Baseline faithfulness numbers are inconsistently reported across figures without explanation.** Figures 2 and 3 report the base model's faithfulness as ~30%, while Figure 4's main evaluation table shows baseline = 15.2%. The most likely explanation is that Figures 2 and 3 evaluate only the sycophancy hint category (which achieves 32% in Figure 4), while Figure 4 averages over all six categories. But this is never stated, leaving readers unable to verify that the RL-failure baselines and the main evaluation baselines reflect the same setting.

- **Conflation of "96%" conciseness metric with "96% accuracy retention" in the contributions list.** The contributions claim: "maintaining at least 96% of the base model's task accuracy in both the tasks." Section 5.2 states: "The accuracy drop remains within ~10% relative to the base" — meaning ~90% accuracy retention, not 96%. The "96%" appears to be the MATH500 conciseness rate (96.6% of responses under 950 tokens), not an accuracy statistic. This conflation in the abstract contributions list is misleading.

### Trivial

- Figure 4 caption describes "consistency" as reaching 42.0% and "grader hacking" as 35.0%, but the table shows Consistency = 31.0% and Grader Hacking = 35.0% — internally inconsistent caption text (likely a parser artifact).

---

## Nice-to-Haves

- **A causal faithfulness probe would be transformative.** The single most impactful experiment: take the questions where the trained model verbalized the hint, re-run them without the hint, and check whether accuracy drops. If it does, that is genuine evidence of causal faithfulness. This does not require redesigning the paper — it is a post-hoc analysis of existing model outputs.

- **Analysis of what the concise traces discard.** The paper asserts "much of the verbose reasoning is redundant," but does not analyze whether the discarded content correlates with problem difficulty or accuracy. A breakdown of accuracy by reasoning length for both models would verify the redundancy claim and clarify whether conciseness selectively hurts harder cases.

- **Ablation on the likelihood-based selection criterion.** Algorithm 1, Line 14 selects the highest-likelihood trace from filtered candidates. No ablation verifies this over, e.g., random sampling among filtered traces. This design choice may not matter, but the paper provides no evidence either way.

- **Generalization to larger base models.** The entire evaluation uses DeepSeek R1 Qwen-1.5B. The paper makes general claims about CoT monitorability that would be better supported if validated on at least one larger model (e.g., 7B), where verbose reasoning may be more causally necessary for correctness.

- **Cross-domain faithfulness generalization.** Training and evaluation both use MMLU-Pro with the same hint templates. It is unknown whether the verbalization behavior transfers to other datasets or hint styles. A held-out domain check would clarify scope.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "The paper should not be accepted in its current form" / conciseness alone would be sufficient.** This is editorial judgment, not a factual weakness, and both contributions have real value. The faithfulness contribution is weaker than the conciseness contribution, but it is not absent. Removed as normative overreach.

- **Harsh Critic: "Requesting comparison to reward shaping or curriculum RL."** The paper focuses on demonstrating why naive RL fails and proposing an alternative; comparing to every alternative RL variant is outside the paper's stated scope and not standard for a proof-of-concept.

- **Harsh Critic: "Cross-domain faithfulness evaluation required."** Noted as a nice-to-have above, but demanding cross-domain generalization from a proof-of-concept paper with a specific benchmark setup is scope creep.

- **Strength Finder: "Large improvements in faithfulness with preserved accuracy" as a core strength.** The faithfulness gain (15.2% → 25.0%) conflicts with the verified Major weakness that the metric is a proxy and the absolute improvement is modest. The "preserved accuracy" component is valid and retained in the conciseness assessment, but the framing of "large improvements" in faithfulness is overstated. Removed as partially conflicting with a verified weakness.

---

## Novel Insights

The most genuinely novel contribution is the identification and formalization of the vanishing-gradient failure mode for CoT monitorability under standard RL: because desirable reasoning behaviors ($f(z) > 0$) are rare under the base policy, the gradient term that improves monitorability collapses to zero, while the accuracy-maintaining term $L_2$ receives signal but cannot improve $f(z)$. This is a clean and actionable insight that explains why multiple practitioners have found RL-based reasoning length and faithfulness training difficult to stabilize. The prior-guided distillation framework is a direct and sensible response to this diagnosis. The proof-of-concept experiment in Section 4 — showing that the base model achieves high accuracy when fed monitorable traces it would never have generated itself — is an elegant way to empirically separate the "capability" and "sampling" problems.

---

## Suggestions

1. Add the causal faithfulness probe: re-evaluate the trained model on hint-present vs. hint-absent versions of the same questions, conditioned on whether the model verbalized the hint, to establish whether verbalization covaries with behavioral influence.
2. Clarify in the paper's Figure 3 vs. Figure 4 comparison that the ~30% baseline in Figures 2–3 reflects sycophancy-only evaluation, while Figure 4's 15.2% is the six-category average.
3. Correct the contributions list to accurately state "~90% accuracy retention" and clarify that "96%" refers to conciseness rate.
4. Resolve Algorithm 1 Line 13's filter direction for faithfulness: if the intent is to keep $z_{si}$ with $f(z_{si}) = 1$ (hint verbalized), the condition $f(z_{si}) \leq \beta$ should be specified as $f(z_{si}) \geq \beta$ with $\beta = 1$, or equivalently written as $f(z_{si}) = 1$.
5. Include at least one additional base model size in the conciseness evaluation to bound the generalizability of the results.

---

## Evaluation on Key Axes

- **Originality:** The constrained optimization framing and prior-guided distillation pipeline are novel combinations, though individual components (SFT on prior outputs, LLM-as-judge evaluation) are standard. The vanishing-gradient analysis is the freshest theoretical insight. *Moderate.*
- **Importance:** CoT monitorability is timely and has clear safety implications. The problem is well-motivated. *High.*
- **Claims supported:** The conciseness claims are well-supported. The faithfulness claims are partially supported but the core metric has an unaddressed circularity concern. *Mixed.*
- **Soundness of experiments:** Conciseness experiments are clean. Faithfulness experiments have the metric-proxy concern and inconsistent baseline reporting. *Moderate.*
- **Clarity:** Writing is generally clear, but the Algorithm 1 notation, baseline inconsistency, and abstract "96%" conflation reduce clarity. *Moderate.*
- **Value to research community:** The pipeline is reproducible and practically useful; the RL failure analysis is instructive. Scope is limited to one small model. *Moderate.*

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>