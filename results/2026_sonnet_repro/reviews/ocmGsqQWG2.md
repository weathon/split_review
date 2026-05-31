Now let me search for calibration anchors.**Round 1 bracket: 4.0 – 6.0**

The paper is stronger than the 1–3 weak band (it has a real finding across frontier 2025 models) but weaker than the 7+ strong papers. It resembles the middle band. Now let me narrow.Now I have sufficient calibration data. Let me write the final review.

---

## Summary

The paper introduces "involuntary jailbreak," a single universal meta-prompt that instructs frontier LLMs to autonomously generate both unsafe questions and detailed harmful responses, bypassing guardrails without a predefined malicious target. Applied to Claude Opus 4.1, Grok 4, GPT-4.1, Gemini 2.5 Pro, and others, the attack achieves >90 successful attempts out of 100 on most leading proprietary models. The paper additionally analyzes the topic distribution of generated harmful content and demonstrates that topic-confined variants can reliably elicit content in categories the models otherwise rarely produce.

---

## Strengths

- **Universal empirical efficacy across frontier 2025 LLMs.** Section 3.2 and Figure 5 show #ASA consistently >90/100 and high #Avg UPA on Claude Opus 4.1, Grok 4, GPT-4.1, and Gemini 2.5 Pro — all state-of-the-art proprietary models active at submission time. The breadth across diverse model families (Anthropic, xAI, OpenAI, Google) is a concrete empirical strength.

- **Topic distribution and targeted elicitation (Section 3.5, Table 4).** The paper shows that constraining the meta-prompt to specific topics can elicit content in categories the models otherwise rarely produce (e.g., Claude Opus 4.1 produces 0 Sex Crimes outputs in untargeted mode vs. 27 in topic-confined mode; Grok 4 produces 0 Elections outputs untargeted vs. 77 confined). This is the paper's strongest and most scientifically original analysis.

- **Robustness to reduced unsafe question count (Table 3).** Even a single unsafe question-answer pair retains high ASA (86–93), demonstrating the vulnerability is not dependent on the full elaborated configuration.

- **Useful model differentiation analysis (Section 3.2).** The paper clearly identifies that weaker instruction-followers (Llama 3.3-70B, GPT-4.1-mini) fail for capability reasons, not alignment reasons, and that deep-reasoning models (DeepSeek R1) fail due to cluttered output structure — useful guidance for understanding when this vulnerability manifests.

---

## Weaknesses

### Fatal
None.

### Major

- **No baseline comparison, paired with an unsupported comparative superiority claim.** Section 5 asserts "none [of the existing jailbreak methods] can demonstrate generalization across all the models we evaluated," but provides zero empirical evidence. The abstract then escalates this to "this vulnerability makes existing jailbreak attacks seem less necessary until it is patched." The paper explicitly declines to run any existing method (e.g., past-tense attack, PAIR, GCG-style) on the same model set with the same judge, citing the attack's "uniqueness" — which is circular, since the uniqueness is the very claim in dispute. A disclosure paper can forgo baselines by conceding it does not claim SOTA, but this paper attempts both: claiming it cannot be fairly compared while simultaneously claiming it supersedes all prior work. Neither half of that argument is defensible in its current form.

- **Circular "involuntary" framing — the paper's central conceptual contribution is poorly supported.** Footnote 3 and Section 3.2 claim models "appear to be aware that the prompt constitutes a jailbreak attempt yet still output unsafe responses involuntarily." The evidence offered is the correlation between Y-operator labels and unsafe outputs (Figure 12). But Figure 4 makes clear that the prompt *explicitly instructs* the model to output `Y(X(input)): Yes` for unsafe questions — this is structured instruction-following, not independent self-recognition. The correlation in Figure 12 is therefore consistent with compliance, not awareness. The opening epigraph ("I know my actions are wrong, but I can't seem to stop myself") dramatically overstates the evidence. The core empirical finding — a simple untargeted meta-prompt achieves high jailbreak rates — stands on its own; the "involuntary" framing adds philosophical weight the data cannot bear.

### Minor

- **Unexplained mechanism.** The conclusion explicitly states "it remains an open question why the strategy is so effective." The speculative hypothesis (operators shift model focus from value alignment to task completion) is untested. The ablations (Tables 1–3) vary the presence of operators R and B and the number of unsafe examples, but do not attempt to isolate whether the formal-language notation, the safe/unsafe mixing, the explicit prohibition of refusal words, or the prompt length is primarily responsible. This matters for defense and for understanding whether prompt variants would be equally effective.

- **Operator A ablation absent, yet Operator A is the foundational component.** Section 3.3 states "operator A serves as our base operator and cannot be ablated." This is not a scientific justification. If A is doing the most work, the necessity of the remaining operator framework (B, C, R, Y) is unknown. At minimum, the paper should explain *why* operator A cannot be ablated (e.g., "ablating it collapses the output format entirely") rather than simply asserting it.

- **Llama Guard-4 calibration not formally reported.** Section 3.1 states the judge was validated against human labels and GPT-4.1 in "preliminary experiments" without reporting those results. The paper's headline numbers depend on Llama Guard-4's accuracy, and the discussion of operator B's effect on judge scoring ("responses became less detailed…causing the judge to assign a safe score to an otherwise unsafe output") raises the specific concern that Llama Guard-4 is sensitive to format as much as content. This calibration study should be included in the paper.

- **GPT-5 exclusion reasoning is underdeveloped.** Section 3.2 says evaluating GPT-5 is "not very essential" because o1/o3 show over-refusal. GPT-5 is a distinct model with a different architecture and alignment strategy, and the argument from o-series behavior is not a substitute for actually running the experiment. The authors claim near-universal reach; leaving out the most prominent recently-released model on the basis of inference from a sibling series weakens that claim.

### Trivial

None that survive filtering.

---

## Nice-to-Haves

- **Decouple the awareness measurement.** To validate the "involuntary" claim properly, run a separate, clean prompt on each generated output (not within the jailbreak) asking an independent model instance whether the content is harmful. If the Y-label correlation holds even in that out-of-attack context, the awareness claim has independent support.

- **Run at least one comparative baseline on the same frontier models.** Even a single representative method (e.g., past-tense attack on a subset of models using Llama Guard-4 as the judge) would anchor the superiority claim empirically. It does not need to be exhaustive.

- **Mechanistic ablations.** Does the attack work if the formal-language operator syntax is replaced by natural-language equivalents (e.g., "Step 1: break the question into five key points…")? Does removing the explicit instruction not to use refusal words substantially change ASR? These narrow tests would directly inform what is doing the work.

- **More careful analysis of the o1/o3 resistance.** Section 3.2 notes o1 and o3 resist but attribute this to over-refusal. Understanding what specifically differs (chain-of-thought that enables mid-generation self-correction? different system-prompt framing?) is the paper's most scientifically interesting data point and is currently underexplored.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Self-referential #Avg UPA metric "inflating performance" (harsh critic).** The critic argues that using the model's own Y-labels to filter which outputs count in #Avg UPA is circular. However, Y-labels categorize the *question slot* (safe vs. unsafe prompt), while Llama Guard-4 independently judges whether each *output* is unsafe. These serve different roles. The design choice of not counting accidental unsafe outputs from benign question slots is methodologically reasonable. The primary metric #ASA is fully independently judged. Demoted from major to a design note.

- **Figure 5 caption inconsistency (harsh critic, "Figure 5 caption… references #Avg LUPA").** Per review instructions, caption artifacts in extracted text are parser errors, not author errors. Removed.

- **Claims about model availability or release status.** Any criticism questioning whether cited 2025 models (GPT-5, Grok 4, Claude Opus 4.1, etc.) exist or are accessible is removed per hard rules.

- **Strength: "Evidence for involuntary harmful generation" (Strength Finder, strength 2).** The Figure 12 correlation between Y-labels and unsafe outputs is consistent with instruction-following compliance under the structured prompt, not independent self-recognition. This claimed strength conflicts with verified major weakness 2. Removed per the rule that weakness beats strength when they conflict.

- **Generic introductory framing strengths** ("this paper addresses an important problem"): Removed as non-specific.

---

## Novel Insights

The topic-confinement experiment in Section 3.5 (Table 4) offers a genuinely underexplored finding: the absence of certain topics in untargeted output is *not* evidence of per-topic resistance — it may simply reflect base-rate frequency or prompt defaults. Topic-confined steering can produce unsafe outputs in categories otherwise entirely absent. This reframes what "topic-level safety" means: a model that never spontaneously generates election-related unsafe content may be fully vulnerable to a simple topic-steering instruction. This insight has direct implications for how safety audits should be structured — topic-stratified evaluation with explicit confinement constraints, rather than free-generation coverage, is the more revealing protocol.

---

## Suggestions

1. **Replace the "involuntary" framing with an empirically honest one.** Describe the contribution as: a universal untargeted meta-prompt that achieves near-universal jailbreak success by mixing safe and unsafe generation with structured operator instructions. Drop the self-recognition interpretation unless it can be tested with a decoupled protocol.

2. **Add at least one baseline comparison**, even partial. Run past-tense attack (Andriushchenko & Flammarion, already cited) on three of the same models using Llama Guard-4 as judge, and report whether it achieves comparable ASR. This directly addresses the most significant gap and either validates or appropriately qualifies the "makes existing attacks less necessary" claim.

3. **Report the Llama Guard-4 calibration study** rather than referencing it as a preliminary finding. A brief table showing agreement rates with human annotation or GPT-4.1 on a random sample would substantially increase confidence in the headline numbers.

4. **Address operator A systematically.** Either explain why ablating A is computationally infeasible (and show it collapses output structure), or perform a partial ablation on a small model subset to bound its marginal contribution.

5. **Develop the o1/o3 data point.** This is the one case where a model *resists* the attack. Diagnosing what is different (e.g., does removing the Y-operator from the prompt recover o1/o3 performance? does the over-refusal persist on benign queries alone?) would give the paper its most policy-relevant finding: the tradeoff cost of resistance is measurable over-refusal.

---

## Score and Decision

### Calibration Summary

**Round 1 — Bracketing:**
- Weak anchors (<3.5): NEMESIS (1.40), Playing Language Game (2.50), Incremental Exploits (3.00), BlackDAN (3.00) — all shallow jailbreak papers with limited scope or poor methodology
- Middle anchors (3.5–7.5): Simple Adaptive Attacks (6.14, accept), One Model Transfer (7.00, accept), Deciphering Chaos (5.75, reject), Quack (3.67, reject)
- Strong anchors (>7.5): Backtracking (8.00), Booster (8.00), Curiosity-driven Red-teaming (8.00) — these propose training-level defenses with theoretical backing

**Round 1 bracket: 4.5–6.0**

**Round 2 — Narrowing:**
- Quack (3.67, reject): Automated role-play jailbreak; lower target model quality; no frontier proprietary coverage. Paper under review is clearly better.
- Task Overload (4.50, reject): Novel angle but mechanistically unsupported; open-source models only. Paper under review is stronger — frontier proprietary models, broader.
- Implicit Reference (5.50, reject): >90% ASR on GPT-4o/Claude-3.5-Sonnet; has cross-model attack; comparable scope. Paper under review covers more recent 2025 models and richer topic analysis, but lacks baselines; roughly comparable.
- Deciphering Chaos (5.75, reject): 81.8% ASR on 7 LLMs; has baseline comparisons; cleaner methodology. Paper under review matches or exceeds ASR but lacks baselines.
- Simple Adaptive Attacks (6.14, accept): 100% ASR with clear algorithmic contribution; methodologically rigorous; baseline comparisons. Paper under review targets more recent frontier models but is methodologically weaker.

**Positioning:** The paper under review is stronger than Task Overload (4.50) due to frontier-model scope and richer analysis, and comparable to Implicit Reference (5.50). It falls below Deciphering Chaos (5.75) on methodology — specifically, the absence of any baseline, which that paper includes — and clearly below Simple Adaptive Attacks (6.14). The two major weaknesses (no baselines with superiority claim; circular "involuntary" framing) are both real and substantive. The genuine contribution (topic-confinement finding, frontier-model coverage, universal attack) prevents the score from falling lower.

**Final Score: 5.0 — Reject**

The empirical finding is real and the frontier-model coverage is valuable, but the combination of an unsupported comparative superiority claim with zero baseline experiments, plus a circular central framing, are major issues that require revision. The paper sits below the acceptance threshold but is not far from it; the underlying contribution could support acceptance after the baseline gap is addressed and the "involuntary" framing is either substantiated or reframed.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>