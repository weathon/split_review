## Summary
The paper proposes Skills-in-Context (SKiC) prompting: a one-stage prompt that lists foundational skills, provides a few exemplars that explicitly ground reasoning steps onto those skills, and then poses the target problem. Across toy compositional tasks (last-letter, addition, DP), GSM8K/MATH, FOLIO and RTE, SKiC outperforms CoT/LtM/Decomp baselines, and the authors further show that fine-tuning Llama2 on GSM8K traces written in SKiC style transfers better to MATH than CoT-style traces.

## Strengths
- The structural distinction from LtM/Decomp is real and useful: SKiC is one-stage and plug-and-play, applicable to problems with non-linear computation graphs such as DP where decomposition-based methods are awkward (Sec. 2, Sec. 3.1).
- Strong empirical gains on multiple compositional tasks far beyond in-context exemplar size — e.g., near-100% on last-letter-12 and large-size DP where CoT/LtM/Decomp degrade (Fig. 2).
- Consistent MATH gains over ComplexCoT without ensembling on both ChatGPT (34.1→40.6) and GPT-4 (50.3→56.4), broken down across seven subdomains (Table 1).
- The qualitative finding that SKiC outputs invoke un-prompted named theorems (Angle Bisector, Heron's Formula in Fig. 2) is a genuinely interesting phenomenological observation.
- Cross-task transfer experiment (GSM8K-designed prompt → MATH, FOLIO) is a nice generalization probe that prompting papers rarely run (Table 4).
- The instruction-tuning extension (Sec. 4) takes the idea beyond prompting and shows non-trivial weak-to-strong transfer from GSM8K-SKiC training to MATH.

## Weaknesses

### Fatal
None.

### Major
- **"Internal skill activation rate" is a weak operationalization of the "unlocking latent skills" claim.** The metric counts skill *labels* in the rationale that were not in the prompt; it doesn't establish that the named procedure was correctly executed, was causal to the answer, or appears more often than under CoT (which is never measured on the same metric). The headline claim that SKiC "more actively utilizes pre-existing internal skills" therefore lacks a baseline contrast.
- **Single-task, single-seed ablation of the central mechanism (Table 5).** The paper's core thesis is that *both* the skill list *and* explicit grounding are essential, but this is supported by one 50-sample DP run without seeds/variance. Notably the −skill condition drops only 4 points (98→94), which actually undercuts the "skills list is essential" half of the claim. The mechanistic load-bearing experiment of the paper is thinner than the claim it supports.
- **Prompt-effort confound on MATH.** SKiC prompts are constructed semi-automatically with GPT-4-distilled skills, while CoT/ComplexCoT use original published prompts. A matched-effort baseline (CoT/ComplexCoT with the same GPT-4-curated exemplars/hints) is missing, so it is hard to attribute gains to the SKiC *structure* versus added prompt engineering.

### Minor
- **"Skill grounding" is never operationally defined** beyond colored highlighting in Fig. 1. Readers (and the ablation) cannot tell whether it is a rationale template, a span annotation, or merely an instruction — which matters for the −skill-grounding condition in Table 5.
- **Synergy and robustness tables likely sit within noise.** RTE 85.2→89.8 (Table 3) and the 38.9 vs. 40.6 stronger-vs-same-model comparison (Table 3 in paper) are reported without seed variance or CIs, yet the latter is used to argue a non-trivial alignment story ("activating more internal skills leads to higher performance"). The robustness tables (Tables 6–7) report only three orders/exemplar sets without variance.
- **Contamination not adequately controlled.** The Limitations section concedes the concern but waves it off; for tasks like last-letter-12 and small-n addition, an adversarial control (rare-token pseudo-words, non-decimal base, etc.) would actually settle the issue and isn't run.
- **Fine-tuning result is a single comparison.** Fig. 5 shows GSM8K-SKiC vs. GSM8K-CoT on Llama2 evaluated on MATH only — no model-size sweep, no held-out tasks beyond MATH, no token-length control for SKiC traces. The framing "SKiC could potentially replace CoT in instruction tuning" overreaches one bar chart.
- **Error analysis category "unseen basic skills" is partly tautological** under SKiC's framing, since any wrong rationale that mentions an unfamiliar skill name gets binned there.

### Trivial
- The Related Work claim that LtM/Decomp "cannot decompose" multiplication or DP is stated more strongly than warranted (those methods have been adapted to such tasks); softening the language would be fair.

## Nice-to-Haves
- Per-subtype MATH breakdown showing whether internal-skill activation rate correlates with accuracy at the problem level.
- A study of partial/noisy groundings, since grounding is the headline ingredient.
- Comparison of SKiC-tuned Llama2 against rationale-distillation baselines (MetaMath / MAmmoTH-style) at matched data scale.
- Variance / CIs across Tables 1, 3, 6, 7.

## Removed Points
*These points are flagged to be removed, treat them with caution.*
- "Near-perfect generalization relies on tasks with known contamination" — the paper *does* address this in Limitations and points to low zero-shot baselines on the same harder sizes as evidence; treating this as a fatal evidential issue is too strong, though running adversarial controls would help (kept a weaker form in Minor).
- "Baselines are unfair because SKiC uses GPT-4-distilled skills" — kept as a Major, but note that exemplars are described as "either a subset of or the same as what have been used in baselines" (Sec. 3), so the asymmetry is partial, not wholesale.
- Strength: "Robustness to exemplar choice/order" — kept in spirit but as the harsh reviewer notes, both CoT and SKiC are equally stable across the three orderings, so this is not differentially informative.
- Strength: "Substantial gains on complex mathematics with measurable internal skill activation" — kept the accuracy half; dropped the "measurable internal skill activation" framing because the metric does not establish what the strength claims (conflicts with verified weakness).
- Strength: "Ablation confirms necessity of both components" — dropped; the verified weakness is that one ablation row on one task with no variance cannot confirm necessity.

## Novel Insights
None beyond the paper's own contributions. The most interesting observation — that SKiC traces spontaneously invoke un-prompted named theorems — is the paper's own, and the consolidated review's contribution is mainly to point out that the paper's metric does not yet formalize this phenomenon rigorously.

## Suggestions
- Define "skill grounding" precisely (template? span annotation? instruction?) and re-run Table 5 across ≥3 tasks with multiple seeds and statistical tests.
- Add a matched-effort prompt baseline on MATH: feed CoT/ComplexCoT GPT-4-distilled hints of comparable token budget.
- Replace or augment the activation-rate metric with a causal test: construct problems requiring a specific un-prompted theorem and measure invocation rate and its correlation with correctness, head-to-head against CoT.
- Add a contamination control on last-letter / addition (pseudo-words, non-decimal base) to firm up the systematic-generalization headline.
- Broaden the fine-tuning result: at least one additional held-out benchmark and a token-length-matched CoT control.

---

**Axis assessment.** *Originality:* moderate — explicit grounding on listed skills is a useful framing distinct from LtM/Decomp, though close to concurrent work cited in Sec. 5. *Importance:* high — compositional generalization is a central reasoning question. *Claim support:* uneven — the accuracy gains are solid and broad, but the two flashier claims ("near-perfect systematic generalization", "unlocks latent internal skills") rest on toy-task evidence and a label-counting metric. *Soundness of experiments:* adequate in breadth, weak in depth — single-seed numbers and a one-task mechanistic ablation. *Clarity:* good. *Value to community:* meaningful — the prompt template is simple, transfers, and seems to carry over into fine-tuning, which is genuinely useful.

## Score and Decision
The paper has real contributions (a simple, transferable prompt structure with consistent gains and a non-trivial fine-tuning extension), and the major weaknesses concern claim calibration and the strength of mechanistic evidence rather than fatal flaws.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>