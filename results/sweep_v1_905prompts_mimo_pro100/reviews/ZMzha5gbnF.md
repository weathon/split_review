Now I have enough calibration data. Let me synthesize the review.

**Bracketing assessment:** The paper is clearly stronger than pure attack papers scoring ~5.75–6.25 (Universal Jailbreak Backdoors, Jailbreaking Leading LLMs, Jailbreak in pieces) but slightly less polished than the Backtracking paper (8.00, all reviewers gave 8). It's well below the shallow alignment paper (9.50). My round-1 bracket is 6.5–8.0. After reading the anchors, the paper's combination of vulnerability discovery + theory + defense is more complete than any mid-range anchor, but the threat model fuzziness and monotonicity assumption hold it back from 8.0. I'll place it at 7.0.

---

## Summary

This paper identifies and characterizes a masked diffusion language model (MDLM)-specific safety vulnerability — the "priming vulnerability" — where affirmative tokens appearing at intermediate denoising steps can steer generation toward harmful responses even in safety-aligned models. The authors demonstrate this through an anchoring attack requiring denoising-process intervention, derive a theoretical lower bound enabling a tractable optimization-based attack (First-Step GCG) that does not require intervention, and propose Recovery Alignment (RA), a defense that trains models to recover from contaminated intermediate states to safe responses.

## Strengths

- **Systematic quantification of a novel, DLM-specific vulnerability class**: The anchoring attack cleanly demonstrates the priming vulnerability across three MDLMs. Figure 2 shows that even a single-token intervention at step 1 raises ASR from ~0% to 20–40% on aligned models, and by step 10/128 reaches 100%. This is a well-characterized vulnerability that is specific to the iterative denoising mechanism of MDLMs and has no direct analog in autoregressive models.

- **Theoretical lower bound enabling practical attack optimization**: Theorem 4.1 establishes that the first-step mask predictor log-likelihood lower-bounds the full denoising log-likelihood under a stated monotonicity assumption. This enables First-Step GCG (Equation 4), which is both stronger (~3× higher ASR than MC-GCG on LLaDA Instruct: 58% vs. 20%) and ~20× faster (0.2h vs. 4.3h per prompt, Table 1).

- **Effective, practical defense with clear ablation structure**: Recovery Alignment reduces priming vulnerability ASR to near-zero on aligned models at early intervention steps (e.g., 0.0% at t_inter=1 on both LLaDA variants, Table 2). The RA w/o inter ablation confirms that training from contaminated intermediate states is the critical ingredient — not just RLHF-style training — by showing meaningful gaps (e.g., on LLaDA at t_inter=4: 22.0% vs. 1.3%). Table 4 shows negligible capability degradation across 11 benchmarks.

- **Well-designed ablations supporting key design choices**: Figure 3a and 3b provide clean evidence for the importance of t_max and linear scheduling over uniform/constant scheduling, directly supporting the curriculum design.

## Weaknesses

### Fatal
None.

### Major

- **The monotonicity assumption underlying Theorem 4.1 is stated without proof in the main text and is non-trivial**: Theorem 4.1's lower bound requires log π_θ(r̃_{t+1}=r | q, r_t) ≥ log π_θ(r̃₁=r | q, r₀) for all t. The paper provides intuition (unmasked tokens in r_t offer richer context) but acknowledges this is an assumption, deferring empirical verification to Appendix C.2. A partial counterexample is easy to construct: a partially masked sequence containing tokens inconsistent with the target response could reduce the log-likelihood of r below its value from r₀. While the paper states the assumption "holds across a broad range of models" (line 139), the main text should present at least a summary figure or key empirical statistic to make the theoretical contribution concrete, rather than asking readers to consult an appendix for what is the load-bearing element of the theory.

- **The decomposition of RA's safety improvement into priming-specific vs. generic RLHF benefits is under-specified**: RA w/o inter (essentially standard RLHF) already substantially reduces vulnerability to conventional jailbreaks — on PAIR for LLaDA Instruct, it drops ASR from 44.3% to 26.3%. RA further reduces this to 10.0%, a clear additional benefit. However, on ReNeLLM for LLaDA Instruct, RA barely improves over RA w/o inter (75.7% vs. 72.3%, a 3.4 pp gap). The paper attributes RA's conventional jailbreak improvement to a "recovery capability" where harmful tokens at intermediate steps are re-detected (line 252–257), but this mechanism is asserted rather than tested. A more explicit decomposition — e.g., measuring how often RA's generations "recover" mid-sequence versus generating safe content from the start — would directly validate the claimed mechanism and strengthen the paper's core thesis.

### Minor

- **Threat model distinction is blurred in the abstract and introduction**: The abstract states "simply injecting such affirmative tokens can readily bypass the safety guardrails" (line 22), which applies only under the intervention threat model requiring system-level access to the denoising pipeline. The most dramatic results (ASR jumping from 2% to 20–40% with a single token at step 1) all require this intervention. The more realistic First-Step GCG attack (no intervention) achieves 58% ASR on LLaDA Instruct — meaningful but a substantially different picture. While the body text carefully distinguishes the two threat models, a reader relying on the abstract might assume the single-token result applies to prompt-only attacks.

- **Main-text evaluation relies on a single evaluator (GPT-4o)**: Section 6 reports only GPT-4o-judged ASR, with LLaMA Guard 3 and keyword matching deferred to Appendix C. LLM-as-judge evaluation is known to have systematic biases, and presenting multiple evaluators in the main text would strengthen confidence in the reported numbers.

- **MMaDA's low baseline capability dilutes some claims**: MMaDA Original has 79.7% ASR even under no attack (Table 2), indicating it is largely unaligned. Including this model as one-third of the evaluation is a reasonable choice to test across alignment levels, but it means that RA's improvements on MMaDA partially reflect achieving baseline alignment rather than defending against the priming vulnerability specifically.

### Trivial

- The text mentions "ASR increases from 2% to 21% with LLaDA Instruct" at t_inter=1 (line 119), but Figure 2's table shows LLaDA Instruct at 1/128 as 40%. This discrepancy likely reflects different evaluators across the appendix and main text, but it could confuse readers.

## Nice-to-Haves

- Evaluate RA against an adaptive attacker who knows the model uses RA and optimizes against it, to stress-test robustness under a stronger threat model.
- Analyze what fraction of First-Step GCG's success is attributable to the priming vulnerability specifically vs. generic context manipulation (e.g., by comparing against random suffixes of similar length).
- Provide a brief analysis of why MOSA fails — does it fail because it trains on fully masked sequences (as argued), or for other reasons related to its middle-token alignment objective?

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Comparison with other optimization-based attacks beyond MC-GCG"** — Scope creep. The paper focuses on GCG as the standard optimization-based attack, and comparing with AutoDAN or PAIR variants adapted for MDLMs is beyond the stated scope.
- **"Missing comparison with concurrent work defenses"** — Cannot verify from external sources whether the cited concurrent works (Zhang et al., 2025; Wen et al., 2025) propose defenses. The paper's positioning is reasonable.
- **Formatting/style/presentation nitpicks** — All such issues are parser artifacts.

## Novel Insights

The paper's most novel insight is that the iterative denoising mechanism of MDLMs creates a fundamentally different safety failure mode compared to autoregressive models: safety alignment trained from fully masked initial states does not constrain model behavior at contaminated intermediate states. This is a genuinely useful framing that connects the architecture of MDLMs to a concrete vulnerability class, and it generalizes beyond the specific priming attack — any attack that introduces harmful tokens at intermediate steps (whether through intervention or through adversarial optimization of the prompt) can exploit this gap. The practical consequence — that MDLM safety alignment must explicitly model contaminated intermediate states — is a clear, actionable takeaway for the DLM safety community.

## Suggestions

- Add a small figure or table in the main text summarizing the empirical distribution of the monotonicity gap (log π_θ(r̃_{t+1}=r | q, r_t) − log π_θ(r̃₁=r | q, r₀)) across a representative sample to make Theorem 4.1's assumption credible in the main paper.
- Add a dedicated analysis measuring "recovery rate" — how often RA model generations transition from harmful tokens to safe continuations vs. generating safe content from the start — to directly test the claimed recovery mechanism.
- Revise the abstract to more clearly scope the "simply injecting" claim to the intervention threat model, and lead with First-Step GCG as the realistic attack vector.

## Score and Decision

**Evaluation on key axes:**
- **Originality**: High. Identifying a DLM-specific vulnerability class and proposing a tailored defense is novel and timely.
- **Importance**: High. DLMs are an emerging model class; understanding their safety properties early is important.
- **Claims supported**: Mostly well-supported, with the caveat that the monotonicity assumption and the RA decomposition are not fully validated in the main text.
- **Soundness of experiments**: Strong across 3 models, multiple attacks, 11 capability benchmarks, with clean ablations. The single-evaluator limitation in the main text is a minor concern.
- **Clarity**: Good overall, though the threat model distinction needs sharpening in the abstract.
- **Value to community**: High — a meaningful addition to the growing DLM safety literature.

**Calibration anchors:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Universal Jailbreak Backdoors from Poisoned Human Feedback | 5.75 | 2 | Our paper is stronger: defense + theory + broader evaluation |
| Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks | 6.14 | 1 | Our paper is stronger: has both attack and defense, theory contribution |
| Multilingual Jailbreak Challenges | 6.40 | 2 | Our paper is stronger: more complete (attack+defense+theory) |
| Endless Jailbreaks with Bijection Learning | 6.25 | 2 | Our paper is stronger: defense component + DLM-specific insight |
| Jailbreak in pieces | 6.25 | 1 | Our paper is stronger: more comprehensive evaluation and defense |
| Identifying the Risks of LM Agents with an LM-Emulated Sandbox | 7.33 | 2 | Similar breadth; our paper has stronger empirical validation |
| Can Sensitive Information Be Deleted From LLMs | 7.50 | 2 | Similar quality; both have attack+defense framing |
| Beyond Memorization: Violating Privacy via Inference | 7.20 | 2 | Our paper has clearer practical contribution |
| Backtracking Improves Generation Safety | 8.00 | 1 | Backtracking paper is cleaner and more focused; our paper has broader scope but slightly less polish |
| Safety Alignment Should be Made More Than Just a Few Tokens Deep | 9.50 | 1 | Stronger paper: unifying insight across many vulnerability types |

**Round-1 bracket**: 6.5–8.0. **Round-2 narrowed**: 6.5–7.5. The paper is clearly stronger than all mid-6s anchors (pure attack papers) but has enough rough edges (monotonicity assumption, threat model fuzziness, decomposition gaps) to sit below the 8.0 Backtracking paper which received universal 8s. I place it at 7.0 — a solid, accepted paper with meaningful contributions that would benefit from the suggested improvements.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>