Now I have a clear picture. Let me compile the final review.

**Calibration Summary (all anchors):**

**Round 1 — Bracketing:**
- Weak band (< 3.5): I1VCj1l1Zn (DLP-LoRA, 3.00), 49ti6LOUw5 (UnoLoRA, 3.00), 762u1p9dgg (MoEfication, 3.40), XVHXVdoV11 (Collective Model Intelligence, 3.40)
- Mid band (3.5–7.5): LWvgajBmNH (MoRE, 4.00), uWvKBCYh4S (MoLE, 5.00), lTkHiXeuDl (HMoRA, 6.00), uHTmx0nRfX (MoTE, 4.75)
- Strong band (> 7.5): xXTkbTBmqq (OLMoE, 8.67), t7P5BUKcYv (MoE++, 8.00), TwJrTz9cRS (HiRA, 8.00)

Initial bracket: between 4.0 and 5.5.

**Round 2 — Narrowing:**
- (3.5, 5.5): PPjpGTPG5K (PERFT, 5.33, Reject), CRkoMdDlFh (I-LoRA, 4.00, Reject)
- (4.0, 5.0): qOqCXEXsX4 (LoTA, 4.25, Reject), u6vC7KaFel (HyperLoRA, 4.75, Reject), LyNsMNNLjY (LLM Routing, 4.25, Reject)

Compared to MoLE (5.00, Accept): LoRA-Mixer has broader evaluation (SSM + Transformer, 3 base models vs MoLE's 1), more creative experiments, and a more novel architectural contribution. But MoLE had a cleaner story without a core-contradiction problem. Compared to MoRE (4.00, Reject): LoRA-Mixer is clearly stronger — more tasks, more architectures, more convincing experiments. Compared to PERFT (5.33, Reject): similar breadth but PERFT lacked novelty; LoRA-Mixer has a clearer contribution but a more serious flaw. The RSL sign inconsistency and untraceable abstract claims pull the score down below 5.0.

Final score: **4.5**. The paper has genuine strengths (broad evaluation, creative experiments, sound architectural insight) but the core technical contribution has a mathematical/descriptive inconsistency that must be resolved, and headline claims are not verifiable from reported data.

---

## Summary

This paper introduces **LoRA-Mixer**, an MoE framework that routes task-specific LoRA experts into the linear projection layers of attention/SSM modules (rather than FFN blocks), and proposes **Routing Specialization Loss (RSL)** — a loss combining a standard auxiliary balancing term with entropy regularization. The paper evaluates on 15 benchmarks across Transformers (LLaMA3-8B, Mistral-7B) and an SSM (Falcon-Mamba-7B), including creative experiments on internet-sourced LoRAs and cross-model transfer.

## Strengths

- **Architecturally novel placement**: Routing LoRA experts at the projection layers (Q/K/V/output) rather than at FFN blocks is well-motivated and architecture-agnostic. The paper convincingly shows compatibility with both Transformers and SSMs (Falcon-Mamba, Table 2), which existing methods like MixLoRA cannot claim.

- **Broad and honest evaluation**: Experiments span 15 benchmarks across 5 domains, 3 base models, and multiple comparison methods (LoRAHub, MoLE, MixLoRA, LoRA-LEGO, PHATGOOSE). The paper also reports cases where LoRA-Mixer underperforms (e.g., Mistral-7B GSM8K: 46.48 vs LoRA 46.67), lending credibility to the overall reporting.

- **Creative internet-sourced LoRA experiment (Table 3)**: Using frozen LoRAs downloaded from public repositories with only 2K additional mixed data to outperform Flan-T5 and individually-trained LoRA on 4/5 GLUE tasks is a genuinely practical demonstration of plug-and-play capability.

- **Evidence of input-aware routing (Figure 4)**: The expert load analysis showing task-specific activation patterns (Expert 1 dominant on Medical, Expert 2 on GSM8K) is the paper's most distinctive empirical result and provides credible evidence that RSL achieves specialization.

- **Strong RSL advantage under low data (Table 8)**: With only 2K training data, RSL substantially outperforms GMoE, DS-MoE, and AESL (e.g., HumanEval: 57.32 vs 50.46 for the best alternative), suggesting genuine benefits from the entropy-based formulation in data-scarce settings.

## Weaknesses

### Major

- **RSL formulation contradicts its stated purpose (sign inconsistency)**. Equation (5): L_RSL = α·∑p̄_i·f̄_i — λ·𝔼[H(p(x))]. Since H(p(x)) is higher for flatter distributions, minimizing L_RSL requires *maximizing* H(p(x)) — i.e., pushing routing distributions toward uniformity. Yet the paper repeatedly claims RSL "suppresses overly flat distributions," "promotes input-aware specialization," and produces "peaked distributions consistent with input semantics." The gradient analysis confirms that λ(log p_i + 1) pushes small probabilities up and large probabilities down (Eq. 7-9), which is an equalizing force. Principle 1 in the paper's own design rationale states "minimizing H(p(x)) reduces token-conditional uncertainty," but the formulation does the opposite. This is not a minor exposition issue: the paper's central technical contribution has a mathematical structure at odds with its textual description. Either the sign in Eq. (5) should be +λ·𝔼[H(p)] (so minimizing the loss penalizes high-entropy distributions), or the claimed mechanism is incorrect and the empirical success must be attributed to a different effect. This requires resolution and re-verification of results.

- **Abstract's headline gains (+3.79%, +2.90%, +3.95%) are not traceable to reported tables**. No comparison in Table 2 yields these numbers. For LLaMA3-8B GSM8K: LoRA-Mixer (65.53) vs best baseline LoRA (65.14) = +0.6% relative. Against the weakest baseline (LoRAHub, 59.10) = +10.9%. Neither is 3.79%. CoLA and ARC-C similarly cannot be matched. The most visible quantitative claim in the paper must be clearly anchored to a specific comparison with a table reference.

- **The "LoRA" baseline in Table 2 is never defined**. It appears as a row in every sub-table but is absent from the baselines description in Sec. 4.1. Without knowing whether this is a single LoRA trained on all tasks jointly, separate per-task LoRAs (an oracle upper bound), or an unoptimized configuration, the comparison is difficult to interpret.

- **The "48% of trainable parameters" claim is unsubstantiated**. This headline efficiency claim appears in the abstract and conclusion but has no supporting table, calculation, or experimental section backing. The paper references Appendix A.4/A.7, but even in the main text a simple parameter-count table across methods would be expected for such a central claim.

### Minor

- **No variance or confidence intervals reported**. All experiments are run three times but no standard deviations are given. For results where margins are <1 point (most tasks in Table 2), outcomes could easily flip across runs.

- **Top-k value never specified**. The paper uses sparse top-K routing but never states the numerical value of K used in experiments, which is a standard experimental detail for MoE papers.

- **"2k mixed data" composition not described**. The internet-sourced LoRA experiment (Sec. 4.3) uses "2k mixed data" without specifying the composition or balance across the five GLUE tasks, limiting reproducibility.

- **RSL advantage in Table 9 is non-monotonic**. RSL helps at 1K (+1.33) and 2K (+1.97), then *hurts* at 4K (-0.37), and yields negligible gains at 6K (-0.04) and 8K (+0.27). The "data efficiency" claim would be strengthened by explaining why the benefit disappears and reappears.

### Trivial

- None.

## Nice-to-Haves

- The cross-model transfer experiment (Table 5) shows a notable drop on ARC-E (88.45 → 85.89, -2.9% relative) that is reported but under-acknowledged in the text's framing.
- The definition of f̄_i in Eq. (5) as "the normalized score assigned to the token of expert i in the first k routes" is ambiguous — is this a top-1 indicator or a top-k weighted score?
- A direct parameter-efficiency comparison table would substantiate the "48%" claim and prevent reader skepticism.

## Removed Points

These points were raised by reviewers but are excluded from the main assessment:

- **"Cross-model transfer selectively reported"** (Harsh Critic) — The paper reports the ARC-E drop in Table 5 and acknowledges outperforming on "two of three tasks." The data is visible and the framing is accurate, if imbalanced. This is a presentation preference, not a weakness.
- **Missing related works / reproducibility nitpicks** — Removed per hard rules.
- **Style/formatting criticisms** — Removed per hard rules (parser artifacts).
- **Strengths about "important problem" and generic praise** — Removed from Strength Finder; kept only concrete, evidence-backed strengths.
- **Convexity claim** (Harsh Critic: "implausible for softmax outputs") — This is about material relegated to the stripped appendix; cannot be evaluated.
- **GMoE/DS-MoE/AESL comparison not controlling for expert count** (Harsh Critic) — The paper states "the only difference is the routing loss" (Sec. 4.4), which is a controlled comparison. Speculation about other uncontrolled variables lacks specific evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the RSL sign issue**. Check whether Eq. (5) should have +λ·𝔼[H(p)] instead of −λ·𝔼[H(p)]. If the sign is correct, provide a worked example showing how minimizing −λ·H(p) produces peaked distributions, because the basic mathematics of entropy suggests the opposite. If the sign is wrong, correct it and re-run experiments, verifying that all conclusions still hold.

2. **Anchor every abstract percentage to a table and comparison**. Add footnotes or parenthetical references (e.g., "+3.79% on GSM8K vs. [baseline] in Table 2, LLaMA3-8B block") so reviewers and readers can verify the claim in one step.

3. **Define the "LoRA" baseline explicitly** in the baselines section and add a parameter count table across all methods to substantiate the 48% efficiency claim.

4. **Add standard deviations** to all tables where margins are small (<2 points), and report the numerical top-k value used across experiments.

5. **Describe the "2k mixed data" composition** for the internet-sourced LoRA experiment.

## Score and Decision

LoRA-Mixer proposes a well-motivated architectural design and supports it with broad evaluation and creative experiments. However, the core RSL formulation has a mathematical/descriptive inconsistency that undermines the paper's claimed mechanism, and key quantitative claims (abstract percentages, 48% parameter efficiency) are not verifiable from the reported data. These issues require resolution before the paper can be accepted.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>