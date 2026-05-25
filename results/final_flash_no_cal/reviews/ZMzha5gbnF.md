Now I have a thorough understanding of the paper. Let me compile the final consolidated review.

## Summary

This paper identifies the "priming vulnerability" in masked diffusion language models (MDLMs): tokens from a harmful response that appear at intermediate denoising steps can steer generation toward harm even in safety-aligned models. Two attacks demonstrate the severity — anchoring (intervention in the denoising process, Figure 2) and First-Step GCG (a non-intervention attack leveraging a theoretical lower bound, Theorem 4.1). The paper then proposes Recovery Alignment (RA), which trains the model to generate safe responses from intentionally contaminated intermediate states. Experiments across three MDLMs show RA reduces Attack Success Rate to near 0% for early interventions while maintaining general capability on 11 benchmarks, and improves robustness against conventional jailbreak attacks.

## Strengths

1. **Clear identification and quantification of the priming vulnerability.** The anchoring attack (Section 4.1) provides direct, controlled evidence that even a single token from a harmful response injected at step 1 raises ASR from 2% to 21% on LLaDA Instruct (Figure 2). This establishes the vulnerability as real and measurable.

2. **Theoretical insight enabling a practical non-intervention attack.** Theorem 4.1 derives a tractable lower bound connecting first-step log-likelihood to full generation probability. First-Step GCG (Section 4.2) exploits this bound to achieve up to 4× higher ASR and ~20× faster computation than Monte-Carlo GCG (Table 1), demonstrating that the vulnerability is exploitable by realistic attackers who cannot intervene in the denoising process.

3. **Effective mitigation via Recovery Alignment with minimal capability loss.** RA reduces ASR to near 0% for early intervention steps across three MDLMs (e.g., from 22%–79% at *t*<sub>inter</sub>=4 in original models to ≤1.3% after RA in Table 2), while maintaining average accuracy within 0.6 points of the original across 11 benchmarks (Table 4).

4. **Ablation confirms contaminated-state training is necessary.** The *RA w/o inter* ablation (training only from fully-masked sequences) fails to substantially reduce the vulnerability (e.g., >20% ASR at *t*<sub>inter</sub>=4, Table 2), directly supporting the paper's central claim that conditioning on contaminated intermediate states is crucial.

5. **Generalization to conventional jailbreak attacks.** RA improves robustness against black-box conversational attacks (PAIR, ReNeLLM, Crescendo) beyond what baselines achieve (Table 3), indicating the learned recovery capability transfers beyond the priming vulnerability.

6. **Comprehensive evaluation across models, attacks, and metrics.** Three MDLMs (LLaDA, LLaDA 1.5, MMaDA), two benchmark datasets, multiple attack families (anchoring, GCG, PAD, DiJA, PAIR, ReNeLLM, Crescendo), and three evaluation methods (GPT-4o, Llama Guard, keyword matching) are used, strengthening reliability and generality.

## Weaknesses

### Fatal

None.

### Major

None. The weaknesses identified below are addressable and do not threaten the core claims.

### Minor

1. **Over-refusal not evaluated.** RA is designed to steer generation away from harmful responses, but it could also become overly cautious and refuse benign queries. The paper evaluates general capability on 11 benchmarks (mostly multiple-choice and code generation), which do not directly measure whether safe but potentially ambiguous instructions are incorrectly refused. A false-positive evaluation on benign queries (e.g., the safe half of AdvBench or everyday instructions) is needed to fully characterize the cost of RA for practical deployment.

2. **"Affirmative token" framing is imprecise.** The paper defines affirmative tokens as those that "endorse or advance a harmful intent" (Section 4), but the anchoring attack works with *any* token from a harmful response — the token need not carry affirmative semantics (e.g., the example uses "Lastly," a discourse marker). The vulnerability is better described as any token from a harmful response, if injected at an intermediate step, steering generation toward harm. The current framing suggests more specificity than the mechanism actually requires.

3. **HumanEval performance drop is under-discussed.** LLaDA drops from 22.0 to 17.1 (a ~22% relative decrease) after RA. The paper calls this "not substantial" but does not discuss statistical significance or whether this reduction is meaningful for code-generation use cases. Reporting variance or multiple-seed runs would help interpret this change.

4. **General capability benchmarks lack confidence intervals.** Table 4 reports only point estimates for 11 benchmarks, unlike Tables 1–3 which include standard deviations. Without variance information, it is difficult to assess whether observed differences (e.g., PIQA decrease, TruthfulQA increase) are statistically significant.

5. **Adaptive attacks not discussed.** An attacker aware of RA could craft adversarial intermediate states designed to bypass the defense (e.g., tokens that appear safe but gradually introduce harm). Discussing this as a limitation or future direction would clarify the boundaries of the protection RA provides.

### Trivial

None.

## Nice-to-Haves

- **Open-ended generation evaluation.** Benchmarks such as MT-Bench or AlpacaEval would further support the claim that RA has minimal impact on general capability, since the current 11 benchmarks are predominantly multiple-choice and code tasks.
- **Qualitative recovery analysis.** A case study showing how RA progressively replaces harmful tokens with safe tokens during denoising would visually confirm the claimed recovery mechanism.
- **Training cost reporting.** Reporting GPU hours and data requirements for RA training in the main text (beyond the appendix reference) would help practitioners assess practical deployability.

## Removed Points

These points were identified by the reviewers but are removed with justification:

- **Monotonicity assumption is "unverified."** The paper provides a theoretical rationale for the assumption (Section 4.2) and states it is empirically validated in Appendix C.2, which exists in the original submission (parser artifact). Moreover, the empirical results in Table 1 stand independently of the theoretical bound — First-Step GCG's effectiveness is demonstrated regardless of the bound's tightness. *Removed per rule: missing appendix content is a parser artifact; also the empirical evidence does not depend on the bound.*

- **SFT/DPO baseline adaptation not explained.** The paper explicitly references Appendix D.6 for full baseline configurations. *Removed per rule: missing appendix content is a parser artifact.*

- **Claim about "existing optimization-based jailbreak attacks" is misleading.** The paper states that "the vulnerability allows existing optimization-based jailbreak attacks to succeed on DLMs." GCG (Zou et al., 2023) is an existing attack; the paper provides a surrogate objective (First-Step GCG) that exploits the vulnerability to make GCG tractable for MDLMs. The claim accurately reflects that the vulnerability is what enables the existing attack framework to work. *Removed: not misleading.*

- **Figure 2 ASR values not shown on graph.** The figure (in the original PDF) clearly shows ASR values on the y-axis with readable curves and an accompanying table. *Removed: factually incorrect.*

- **"State-of-the-art robustness" claim overreaching.** The paper honestly reports that RA is imperfect against late interventions (t_inter=32) and strong attacks (ReNeLLM). The claim is supported by comparison to all tested baselines. *Removed: the evidence supports the claim in context.*

- **Notation inconsistencies in equations (bold/non-bold), Eq. (7) brace formatting.** These are PDF-extraction artifacts or style preferences, not author errors. *Removed per rule: formatting/style nitpicks.*

- **Missing sensitivity analysis for t_min/t_max.** The paper provides ablations on t_max (Figure 3a) and scheduling (Figure 3b). Default values would likely be in Appendix D.4. *Removed per rule: missing appendix content.*

- **Training cost and data efficiency not reported.** The paper explicitly references Appendix C.4 for training cost and learning curves. *Removed per rule: missing appendix content.*

- **Demand for MT-Bench/AlpacaEval as a weakness.** 11 benchmarks constitute a comprehensive evaluation. Open-ended benchmarks would strengthen but are not required to support the paper's claims. *Demoted to Nice-to-Have: scope creep.*

- **Distinction from ARM prefilling attacks "clear but brief."** This is an observation, not a weakness. *Removed: not a criticism.*

## Novel Insights

None beyond the paper's own contributions. The reviews did not uncover a perspective the paper itself does not already articulate.

## Suggestions

1. **Add an over-refusal evaluation.** Measure false-positive refusal rates on a set of benign-but-tricky instructions (e.g., the safe subset of AdvBench or standard helpfulness queries) to quantify the practical trade-off of RA.
2. **Clarify the "affirmative token" terminology.** Replace or explicitly qualify the term to reflect that *any* token from a harmful response (not just semantically affirmative ones) can steer generation, or rename it to "harmful anchor" or "seeding token."
3. **Report variance for general capability benchmarks.** Add standard deviations or confidence intervals to Table 4 to allow readers to judge the significance of observed changes.
4. **Discuss adaptive attacks briefly in limitations.** Acknowledging that an adversary aware of RA could craft adversarial intermediate states would strengthen the paper's characterization of the defense's boundaries.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>