Now I have sufficient context. Let me write the final review.

---

## Summary

This paper identifies a "priming vulnerability" in Masked Diffusion Language Models (MDLMs): if an affirmative token appears at an intermediate denoising step, the model can be steered toward harmful content even in safety-aligned models. The authors quantify this through an anchoring attack (Section 4.1), derive a theoretical lower bound enabling a more practical GCG variant (First-Step GCG, Theorem 4.1), and propose Recovery Alignment (RA), a training method that conditions models on contaminated intermediate states to recover safe outputs. Experiments on three MDLMs (LLaDA Instruct, LLaDA 1.5, MMaDA MixCoT) show RA substantially reduces attack success rates under the anchoring attack and several conventional jailbreaks while preserving average capability across 11 benchmarks.

---

## Strengths

**1. Novel identification of a previously unstudied vulnerability in MDLMs.**  
The priming vulnerability is specific to the iterative denoising process of MDLMs and is distinct from both prefilling attacks on autoregressive models and input-level priming. The anchoring attack (Section 4.1) cleanly demonstrates that injecting even a single affirmative token at the first denoising step bypasses safety guardrails (ASR rising from low single digits to 17–40% depending on the evaluation configuration).

**2. Theoretical lower bound enabling a practical optimization-based attack.**  
Theorem 4.1 establishes that the first-step log-likelihood is a valid surrogate for the intractable full-process likelihood, under a monotonicity assumption that the paper empirically validates (Appendix C.2). First-Step GCG achieves 4× higher ASR than Monte Carlo GCG and is ~20× faster (Table 1: 58% vs 20% on LLaDA Instruct, 0.2h vs 4.3h per prompt). This is a non-trivial theoretical contribution that converts an intractable gradient problem into a tractable one.

**3. Recovery Alignment effectively mitigates the vulnerability.**  
RA consistently outperforms SFT, DPO, and MOSA across all three MDLMs and all anchoring depths. For LLaDA at intervention step 4, ASR drops from 44.0% (original) to 1.3% (RA); at step 1 it reaches 0.0% (Table 2). The RA w/o inter ablation confirms that training from fully masked states alone (i.e., conventional RLHF) fails to address the vulnerability, empirically validating the paper's central insight.

**4. Generalization to conventional jailbreak attacks.**  
RA reduces ASR on PAIR (44.3%→10.0% for LLaDA), Crescendo (81.3%→45.0%), and ReNeLLM (92.7%→72.3%) (Table 3), suggesting that the recovery capability learned from contaminated intermediate states transfers beyond the specific priming-based attacks. This is a stronger generalization result than most concurrent MDLM safety work reports.

**5. Rigorous ablation of design choices.**  
Figure 3 systematically examines the impact of t_max and the scheduling strategy, confirming that (a) larger t_max improves robustness but can destabilize training, and (b) linear scheduling outperforms uniform and constant schedules. These ablations provide practical guidance for deploying RA.

---

## Weaknesses

### Major

**1. Numerical inconsistency in the anchoring-attack results between Section 4.1 and Table 2.**  
The paper presents three mutually inconsistent sets of numbers for the same claimed quantity (LLaDA Instruct ASR under the anchoring attack at t_inter=1):
- Figure 2 caption table: **0%** at step 0 → **40%** at step 1/128
- Section 4.1 text: "ASR increases from **2% to 21%**"
- Table 2 (LLaDA Original): No Attack **2.0%**, Anchoring(1) **17.3%**

The discrepancy is even larger for MMaDA: Figure 2 shows **0%** ASR at step 0, while Table 2 reports **79.7%** for No Attack. Since the vulnerability analysis is foundational to the paper's narrative, the reader cannot determine whether the anchoring-attack results in the vulnerability section and the mitigation experiments use the same harmful-response set, evaluation protocol, or generation hyperparameters. The paper provides no explanation for these differences. This inconsistency undermines the reliability of the empirical presentation and must be resolved. (Note: this does *not* invalidate the comparative RA-vs-baseline results in Table 2, which are internally consistent, but it does damage confidence in the precise quantification of the vulnerability.)

### Minor

**2. Default RA hyperparameters (t_min, t_max) not stated in the main text.**  
The main experiment section (Section 6) describes RA with a linear schedule over [t_min, t_max] but never gives the default values used for Tables 2–4. Figure 3 shows that robustness is sensitive to t_max and that large values can destabilize training. Without knowing the chosen value, readers cannot assess whether the reported ASR numbers reflect a realistic operating point or an unusually favorable configuration. The appendix may contain these details, but the main text should state the defaults.

**3. The HumanEval degradation is not acknowledged in the general-capability discussion.**  
Table 4 shows that for LLaDA, HumanEval drops from 22.0 to 17.1 (a 22% relative decline). The paper notes a decrease in PIQA and correctly observes that the average across 11 benchmarks is preserved (52.2%→52.6%), but the HumanEval drop—a practically meaningful capability dimension—is not discussed. The claim "no substantial degradation" is therefore overly broad; the trade-off is more nuanced than the text suggests.

### Trivial

**4. Table 2 lists the model as "LLaMA" instead of "LLaDA".**  
The first row of Table 2 reads "LLaMA" but the paper refers to the model as LLaDA Instruct / LLaDA 1.5 throughout. This is a formatting error that should be corrected.

---

## Nice-to-Haves

- Show at least one non-GPT-4o evaluator (LLaMA Guard 3 or keyword matching) in the main paper tables, rather than relegating all alternative judges to the appendix.
- Report the computational cost of RA training (GPU hours, steps, batch size) so practitioners can gauge feasibility.
- Briefly validate how well the DeBERTaV3 reward model's safety scoring agrees with GPT-4o on a sample of generations.

---

## Removed Points

*The following points raised by reviewers were removed with justification:*

- **"First-Step GCG Monte Carlo baseline implementation details are omitted from the main text"** → Removed per rule: criticism is about appendix-level implementation detail, and the paper explicitly says "details are in Appendix D.9." The parser strips the appendix; the original submission contains these details.
- **"GRPO choice is not justified or compared with PPO"** → Removed per rule: the paper notes that GRPO is used for optimization, and the ablation (RA w/o inter) uses the same optimizer, so the comparison is fair. The choice is a minor implementation detail, not a methodological gap.
- **"The paper could usefully describe the computational cost of RA training"** → Moved to Nice-to-Haves. It is a reasonable request but not a flaw in the presented results.
- **"The reward model is used without discussion of how well it scores safety vs. helpfulness"** → Moved to Nice-to-Haves. The paper uses a standard off-the-shelf reward model, which is standard practice.
- **"Conventional jailbreaks (PAIR, ReNeLLM, Crescendo) are originally designed for ARMs—hyperparameters may need retuning for MDLMs"** → Removed per rule: this is a speculative concern about whether hyperparameters were re-tuned; the reviewer does not provide evidence that they were not suitable.
- **Strength finder's claim about "preservation of general capability"** → The strength is retained, but the caveat about HumanEval is added (see Weakness 3). The strength finder's unqualified version is removed.
- **"The ablation studies confirm the design choices"** from strength finder → Retained as Strength 5 with specific reference to Figure 3.

---

## Novel Insights

Beyond the paper's own contributions, the reviewer comparison surfaces a structural observation: the paper identifies a vulnerability that is the mechanistic mirror of prefilling attacks on ARMs—whereas ARMs are exploited by injecting tokens at the *start* of the sequence, MDLMs are exploited by injecting tokens at an *intermediate denoising step* that then become anchors the model cannot escape. This "anchor-based" failure mode is specific to iterative refinement and has no analogue in causal generation. The paper's insight that training on contaminated intermediate states (rather than only on fully masked starts) is necessary to close this failure mode is a principled design lesson that likely generalizes beyond the specific RLHF instantiation presented here.

---

## Suggestions

1. **Resolve the numerical inconsistency.** Provide a single consistent evaluation of the anchoring-attack vulnerability, or clearly explain why the numbers differ across Figure 2, the Section 4.1 text, and Table 2 (e.g., different harmful-response generation methods, different random seeds, different subsets of JBB-Behaviors).
2. **State default t_min and t_max** for the main RA experiments (Tables 2–4) in the main text, along with a brief rationale for the chosen value.
3. **Acknowledge and discuss the HumanEval drop** explicitly. If this is a known trade-off, stating it candidly strengthens the paper's credibility.
4. **Fix the "LLaMA" typo** in Table 2.

---

## Score and Decision

### Calibration Report

**Round 1 — Bracketing.** Three queries targeted weak (score<3.5), middle (3.5–7.5), and strong (>7.5) bands on topics similar to the paper.

*Weak band anchors (all rejected, avg 1.4–3.0):*  
- `BeOEmnmyFu` (2.50) — Playing Language Game jailbreak; much weaker paper.
- `5kMwiMnUip` (1.40) — NEMESIS chain-of-thought jailbreak; much weaker.
- `KyKTjRtyNG` (3.00) — Multi-round conversational jailbreaking; weaker.
- `lUyYX9VFgA` (3.00) — Code-of-thought prompting; weaker.

*Middle band anchors (avg 3.67–5.33):*  
- `FD9sPyS8ve` (4.75) — "Purple Problem" jailbreak analysis; rejected.
- `V01FPV3SNY` (5.33) — Robustly Aligned LLM defense; rejected. This paper (current) is stronger in evaluation breadth and novelty.
- `1zt8GWZ9sc` (3.67) — Quack automatic jailbreaking; rejected.

*Strong band anchors (avg 7.75–9.50, all accepted):*  
- `6Mxhg9PtDE` (9.50) — "Safety Alignment Should be Made More Than Just a Few Tokens Deep"; much stronger, no numerical inconsistencies.
- `syThiTmWWm` (7.75) — Cheating automatic LLM benchmarks; different topic, very strong.

**Initial bracket: 5.5–7.5.** The paper is clearly above the weak and lower-middle anchors but not at the level of the 8.5+ anchors.

**Round 2 — Narrowing.** Queries targeting the 5.0–7.5 band on LLM safety vulnerability/defense topics:

- `r42tSSCHPh` (7.00, accepted) — "Catastrophic Jailbreak via Exploiting Generation." Similar structure (vulnerability discovery + mitigation), evaluated on 11 models. The current paper has deeper theoretical analysis and a more novel defense, but the Catastrophic Jailbreak paper is cleaner (no numerical inconsistencies). The current paper is slightly below this anchor.
- `hXA8wqRdyV` (6.14, accepted) — "Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks." Broad model coverage but less technical novelty. The current paper has stronger novelty (new vulnerability type, theoretical bound) but messier presentation.
- `vESNKdEMGp` (6.40, accepted) — "Multilingual Jailbreak Challenges." Evaluates multilingual vulnerability, proposes Self-Defense framework. Similar overall quality; the current paper has greater technical depth but also a more significant empirical flaw.

**Final score determination.** The paper's core contributions (novel vulnerability, theoretical analysis, effective defense, thorough evaluation) are solidly in the 6–7 range. However, the numerical inconsistency in the anchoring-attack results—the paper's foundational empirical claim—is a significant credibility concern that the top-half anchors did not have. This brings the score below the clean 7.0 anchor. Score positioned relative to round-2 anchors: below Catastrophic Jailbreak (7.00) and Multilingual Jailbreak (6.40), comparable to or slightly below Adaptive Attacks (6.14) when accounting for the inconsistency. **Final score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>