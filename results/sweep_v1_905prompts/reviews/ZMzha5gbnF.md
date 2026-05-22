Now let me finalize my analysis and write the review.

## Calibration Summary

**Round 1 — Bracketing:** The paper sits well above weak jailbreak papers (scores 1.4–3.0) and far below exceptional papers (scores 7.5+). Initial bracket: (4.0, 7.5).

**Round 2 — Narrowing:** Reading anchors in the 5.5–7.5 range:

| Anchor | Score | Comparison |
|--------|-------|-----------|
| Catastrophic Jailbreak via Exploiting Generation (R42tSSC...) | 7.00 | Similar quality. Both identify novel vulnerabilities and propose defenses. Current paper's vulnerability is more novel (MDLM-specific priming), but scope is narrower. **Current paper ≈ this anchor.** |
| Safety Layers in Aligned LLMs (kUH1yPM...) | 6.00 | Current paper is notably stronger — more novel contribution, more thorough evaluation. **Current paper > this anchor.** |
| Breach By A Thousand Leaks (8Rov0fj...) | 5.80 | Current paper is substantially stronger. **Current paper > this anchor.** |
| Durable Quantization Misalignment (41uZB8b...) | 6.00 | Current paper is stronger — vulnerability is more novel, evaluation more comprehensive. **Current paper > this anchor.** |

The paper is closest to the "Catastrophic Jailbreak" anchor at 7.00, but with a slightly narrower scope (MDLM-specific vs. general open-source LLMs). So it sits just below that. Final score: **6.5**.

---

Now writing the review.

## Summary

2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
// List only reasonable points. Rank by severity.

### Fatal
None.

### Major
None.

### Minor
- weakness 1 — why it matters
- weakness 2 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Weaknesses that were removed after cross-checking against the paper.

## Novel Insights
One paragraph synthesizing genuinely novel observations.

## Suggestions
- specific actionable suggestion

## Score and Decision
Score round to .5 or .0.Here is my consolidated final review:

---

## Summary

This paper identifies and systematically characterizes the *priming vulnerability* in Masked Diffusion Language Models (MDLMs): if even a single affirmative token for a harmful query appears at an early denoising step, subsequent generation is steered toward a harmful response — increasing ASR from 2% to 21% on LLaDA Instruct at intervention step 1 (Figure 2). The authors design two threat models (direct denoising intervention via anchoring attack; realistic optimization-only via First-Step GCG) and then propose **Recovery Alignment (RA)**, an RLHF-style method that trains models to generate safe responses from deliberately contaminated intermediate states. On three MDLMs across multiple attacks, RA reduces ASR to near 0% at early intervention steps (e.g., from 17.3% to 0.0% on LLaDA at \(t_{\text{inter}}=1\)) while maintaining general capability within 0.5% average on 11 benchmarks.

---

## Strengths

1. **Identification and quantification of a novel, MDLM-specific vulnerability.** The priming vulnerability is convincingly demonstrated through the anchoring attack (Figure 2, Section 4.1), showing that even a single affirmative token at the first denoising step can bypass safety guardrails. This vulnerability is mechanistically distinct from ARM prefilling attacks and is not addressed by prior DLM safety work.

2. **Recovery Alignment (RA) provides a principled and effective mitigation.** RA reduces ASR from 17.3% to 0.0% on LLaDA at \(t_{\text{inter}}=1\) under the anchoring attack, far surpassing existing alignment methods (SFT, DPO, MOSA) which leave ASR at 6–19% (Table 2, Section 6.2). The ablation *RA w/o inter* confirms that training on contaminated intermediate states is the critical ingredient — not just RLHF.

3. **Theoretical analysis enabling practical optimization-based attacks.** Theorem 4.1 derives a lower bound relating the first-step log-likelihood to the full denoising likelihood, which is exploited to design First-Step GCG. This attack achieves roughly 20× speedup and up to 4× higher ASR than Monte Carlo GCG (Table 1), demonstrating that the vulnerability is exploitable without denoising intervention.

4. **Thorough and honest evaluation.** The paper evaluates across 3 MDLMs, 7 attack methods (including concurrent PAD and DiJA), 3 ASR evaluators (GPT-4o, LLaMA Guard 3, keyword matching), and 11 general capability benchmarks. Ablations on intervention-step scheduling (Figure 3) are well-designed and provide actionable guidance. Limitations (e.g., RA struggles at late intervention steps like \(t_{\text{inter}}=32\)) are openly reported.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Reward model specification is ambiguous.** Section 6.1 states: "As the reward model, we directly employ DeBERTaV3 (He et al., 2021; Köpf et al., 2023) without additional fine-tuning." DeBERTaV3 is an architecture, not a reward model checkpoint. The citation to Köpf et al. (OpenAssistant) suggests the authors used the OpenAssistant reward model (which is DeBERTaV3-based), but the phrasing leaves ambiguity about the exact checkpoint, its scoring criteria, and whether it is a safety classifier or a general helpfulness reward model. This should be clarified for reproducibility. The paper would benefit from stating the exact Hugging Face model identifier and the reward scoring range/scale.

### Trivial

None worth listing — the parser-stripped format means minor formatting observations from the PDF would be parser artifacts.

---

## Nice-to-Haves

- A small qualitative illustration (e.g., a token-level trajectory showing the original model drifting toward harm after an affirmative token appears, and RA steering back to safety) would strengthen the intuition behind RA.
- Reporting computational cost (GPU-hours) for RA training would help practitioners assess feasibility.

---

## Removed Points

These points from the inputs were removed after cross-checking against the paper, per the meta-reviewer guidelines:

- **Missing proof/verification for Theorem 4.1 assumption:** The harsh critic flagged that the proof (Appendix A) and empirical validation (Appendix C.2) are not available in the parsed text. The rules state to remove weaknesses about missing appendix content, as the parser strips these sections from all papers but they exist in the original submission.
- **Formatting/style nitpicks:** Criticisms about contractions ("can't"), capitalization ("MMaDa" vs "MMaDA"), and table column alignment were removed as parser artifacts or style issues with no impact on scientific content.
- **Criticism about unverifiable reproducibility due to missing code/dataset release:** The paper clearly states "Our code is available at https://github.com/mdl-lab/dlm-priming-vulnerability." Any reproducibility concern predicated on assuming this does not exist is invalid.

---

## Novel Insights

None beyond the paper's own contributions. The key insight — that MDLMs' iterative denoising creates a unique vulnerability where early affirmative tokens in the intermediate state act as anchors for harmful trajectories — is the paper's own discovery and is well-articulated. The reviewer inputs did not surface any additional novel perspective beyond what the authors already present.

---

## Suggestions

1. **Clarify the reward model.** Specify the exact Hugging Face checkpoint identifier for the reward model (e.g., "OpenAssistant/reward-model-deberta-v3-large") and describe the reward scoring range and criteria (is it a safety classifier, a helpfulness model, or a combined metric?).
2. **Add a brief qualitative example in the main text** (or keep it in the appendix but reference it) showing how RA changes the generation trajectory — e.g., the same harmful query producing different continuation distributions after the critical affirmative token.

---

## Score and Decision

**Score: 6.5 — Accept**

This paper makes a clear, well-supported contribution: it identifies a genuine and significant vulnerability in MDLMs that has not been systematically studied, provides a theoretically grounded attack that demonstrates practical exploitability, and proposes a principled mitigation that is empirically effective with negligible utility cost. The evaluation is thorough and honest. The two clarifying points above (reward model specification) do not undermine the core contribution and are easily addressable. The paper will be a valuable addition to the LLM safety literature.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>