Now I have enough anchors. Let me synthesize the review.

**Round 1 bracket**: Paper appears between 5 and 8. The closest comparable accept (Backtracking, 8.0) shares this paper's "recover from unsafe partial generation" framing, while DiffusionAttacker (4.75) is much weaker scoped. The paper sits firmly above the reject tier.

**Round 2 narrowing**: Round-2 anchors at 6.0–6.5 (Safety Layers 6.0, Improved GCG Techniques 6.25, SafeDPO 6.40, Probe before You Talk 6.0) provide good comparison. This paper has stronger evidence than DiffusionAttacker (4.75), comparable rigor and scope to the 6.0–6.5 cluster (clear contribution, multiple models/evaluators, clean ablation, but with real residual limitations against ReNeLLM and a theorem that is more decorative than predictive). Not as universal as Backtracking (8.0). Final position: ~6.0.

## Summary
The paper identifies the *priming vulnerability* in masked diffusion language models (MDLMs): if an affirmative token appears at an intermediate denoising step, subsequent denoising is steered toward a harmful completion even in safety-aligned models. The authors quantify the vulnerability with an "anchoring attack," derive a tractable lower bound (Theorem 4.1) that yields a "First-Step GCG" attack ~20× faster than Monte Carlo GCG with substantially higher ASR, and propose *Recovery Alignment* (RA), a GRPO-based training procedure that conditions the model on contaminated intermediate states. RA largely eliminates the vulnerability at early intervention steps across three MDLMs while preserving general capability on eleven benchmarks.

## Strengths
- **Clean quantification of a new, MDLM-specific failure mode.** Figure 2 / Section 4.1 show that injecting a single token at step 1 raises ASR from 2% → 21% (LLaDA Instruct) and 1% → 14.7% (LLaDA 1.5), establishing the existence and severity of priming with a controlled intervention.
- **First-Step GCG is both faster and stronger than the obvious Monte Carlo baseline.** Table 1: ~20× speedup (4.3h → 0.2h per prompt) with ASR jumping from 20.0% → 58.0% on LLaDA Instruct and 12.5% → 49.5% on LLaDA 1.5. Theorem 4.1 gives a principled, gradient-friendly surrogate that does not require MC sampling.
- **The ablation cleanly isolates the key design choice.** Comparing RA against "RA w/o inter" (which removes only the contaminated-state initialization while keeping the same GRPO pipeline) in Table 2 shows that the contaminated-state training, not just GRPO, drives the gains. This is a rare example of an ablation that actually pins down the mechanism the method claims.
- **RA reduces ASR sharply at early intervention steps while preserving capability.** Table 2: 0.0% at t=1, 1.3% at t=4 on LLaDA Instruct, vs. all baselines >6% and >20% respectively. Table 4: 11-benchmark average essentially unchanged (LLaDA 52.2 → 52.6).
- **Robustness transfers to standard conversational jailbreaks.** Table 3: PAIR 44.3% → 10.0%, Crescendo 81.3% → 45.0% on LLaDA Instruct, evidence that recovery generalizes beyond the anchoring distribution.

## Weaknesses

### Fatal
None.

### Major
- **Residual vulnerability at late intervention steps and against ReNeLLM partially contradicts the abstract's "significantly mitigates" framing.** At t_min=32, RA still produces 50.7% / 43.0% / 79.3% ASR (Table 2), and ReNeLLM remains at 72.3% / 71.7% / 81.7% after RA (Table 3) — actually *increasing* slightly on MMaDA (79.3% → 81.7%). The paper does acknowledge this in §6.2 ("the alignment can be circumvented when the harmfulness is not detectable from the surface form"), but the headline claims should be tightened to "mitigates priming-style attacks at early-to-mid intervention steps; provides limited protection against semantically disguised jailbreaks." This bounds the contribution rather than invalidating it.
- **No false-refusal / over-refusal evaluation.** The capability evaluation in Table 4 measures task accuracy on benchmarks like MMLU and HumanEval, which do not detect alignment-induced refusal of benign requests — a known side effect of safety RL with a safety-leaning reward model. The PIQA dip is consistent with style/refusal drift but is not characterized. An XSTest-style false-refusal evaluation would bound the cost of the recovery training and is the natural complement to the safety numbers reported.

### Minor
- **Theorem 4.1 is more formal scaffolding than predictive theory.** The bound log p ≥ (1/T) log π̃₁ is structurally very loose for T=128 (the 1/T exponent makes π^(1/T) close to 1 for any non-tiny first-step probability). The authors note this and argue empirically that maximizing the first-step likelihood works because Figure 2 shows single-step intervention already steers generation. That defense is reasonable, but the framing in §4.2 oversells the role of the bound; the attack's empirical success rides on the priming observation, not on bound tightness.
- **The MMaDA baseline is qualitatively different and complicates cross-model aggregation.** MMaDA MixCoT has 79.7% ASR with *no attack* (Table 2), so it is essentially unaligned. The dramatic improvement RA delivers on MMaDA (79.7% → 3.3% with no attack) conflates "RA mitigates priming" with "RA performs basic safety alignment MMaDA was missing." The LLaDA / LLaDA 1.5 results are the cleaner evidence for the central claim; the MMaDA improvement should be presented with this caveat.
- **MC GCG comparison is at a single iteration budget.** Table 1 fixes 500 iterations for both methods; a matched-compute comparison (MC GCG with proportionally more samples) would more directly substantiate the "First-Step GCG is a better surrogate" claim rather than the weaker "First-Step GCG is faster and stronger at equal iteration count."
- **Reward-model sensitivity is unstudied.** The choice of DeBERTaV3 without fine-tuning is presented as a feature, but the reward model defines what "safe" means during RA. §6.4 mentions reward hacking at large t_max but does not characterize it; testing with a second safety classifier would show whether the method is robust to reward-model choice.
- **Curriculum analysis is thin.** The linear schedule is justified in Figure 3b as outperforming uniform/constant, but the "curriculum" interpretation in §5 ("start from easier conditions") is asserted rather than analyzed. Showing how robustness at a fixed t_test scales with training t_max — and where the train/test mismatch breaks down — would substantiate the curriculum framing.

### Trivial
None worth flagging.

## Nice-to-Haves
- Token-class analysis of what makes a token an effective anchor (transition phrases vs. imperatives vs. harmful-content nouns) — this would deepen the central observation rather than broaden it.
- A DPO variant trained on (contaminated state, safe completion) pairs would provide a cleaner orthogonal ablation separating "GRPO" from "contaminated-state conditioning" (currently only "RA w/o inter" addresses this, and it inherits the GRPO pipeline).
- Explicit reporting of whether the harmful responses used as anchors at evaluation time are disjoint from BeaverTails training data; if disjoint, this should be stated; if not, it tempers the in-distribution interpretation.
- A precise scope claim — e.g., "RA defends against attacks whose harmful intent is detectable from intermediate-state tokens" — would convert the ReNeLLM limitation into a positive characterization.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Crescendo multi-turn adaptation is under-specified in the main text"** — Implementation details for Crescendo are explicitly deferred to Appendix D.5 (Section 6.1), so this is a parser-induced concern about appendix material, not a real gap.
- **"Anchor response source deferred to Appendix D"** — Same reason; the paper explicitly points to Appendix D for details. Cannot fault the paper for an appendix the parser strips.
- **Generic strengths from the Strength Finder were already merged into specific evidence above; none required full removal.**

## Novel Insights
The most novel observation is that masked diffusion language models exhibit an analog of "shallow safety alignment" that is *temporal-in-the-denoising-direction* rather than positional-in-the-output-sequence: because training initializes from a fully masked state, the model never learns a refusal trajectory from partially-affirmative intermediate states, so a single token injected at any denoising step is sufficient to redirect the trajectory. The corresponding fix — training the model to recover from synthetically contaminated intermediate states — is the natural MDLM counterpart to backtracking / deep-alignment methods proposed for autoregressive models. Reframing the contribution this way (as the MDLM analog of "safety must go deeper than the first token") would tighten the paper's positioning.

## Suggestions
- Tighten the abstract to match the evidence: RA mitigates priming at early-to-mid intervention steps and improves robustness on PAIR/Crescendo; protection against semantically disguised jailbreaks (ReNeLLM) is limited.
- Add an XSTest-style false-refusal benchmark to Table 4 to bound the over-refusal cost of recovery training.
- Add at least one reward-model variation (e.g., a different safety classifier) to demonstrate that RA's gains are not artifacts of DeBERTaV3.
- Present LLaDA / LLaDA 1.5 as the primary evidence for the central claim and discuss MMaDA separately with the caveat that its baseline is essentially unaligned.
- Soften the framing around Theorem 4.1: it provides a tractable surrogate that empirically works because of the priming observation, rather than a tight predictive bound.
- A matched-compute MC GCG comparison in Table 1 would make the "better surrogate" claim airtight.

## Evaluation along required axes
- **Originality**: High. The priming vulnerability is a genuinely new observation specific to MDLMs, distinct from ARM prefilling attacks.
- **Importance**: Moderate-to-high. MDLMs are an emerging paradigm and safety analysis is timely; the impact is bounded by current MDLM deployment.
- **Claims well supported**: Mostly yes for the central claim (Tables 1, 2, 4). The abstract slightly overclaims scope against ReNeLLM.
- **Soundness of experiments**: Strong. Three models, three evaluators, two benchmarks, multiple attack families, clean ablation isolating the key mechanism.
- **Clarity**: Good. Setup, theorem, and algorithm are clearly presented.
- **Value to community**: The anchoring attack, First-Step GCG, and RA recipe are all likely to be reused as standard tools in MDLM safety work.

## Anchor papers compared
| Path | Avg | Round | Comparison |
|---|---|---|---|
| BeOEmnmyFu.md | 2.50 | 1 | Much weaker — language-game jailbreak attack only |
| 5kMwiMnUip.md | 1.40 | 1 | Far weaker — surface-level jailbreak survey |
| KyKTjRtyNG.md | 3.00 | 1 | Weaker — multi-round jailbreak with thin evaluation |
| lUyYX9VFgA.md | 3.00 | 1 | Weaker — code-of-thought probing |
| u08UxVNdIo.md | 4.75 | 1 | Weaker — DiffusionAttacker, attack only, thin baselines |
| hXA8wqRdyV.md | 6.14 | 1 | Similar tier — adaptive jailbreak attacks, clear and well-evidenced |
| xP1radUi32.md | 6.25 | 1 | Similar tier — bijection learning attack, clean execution |
| plmBsXHxgR.md | 6.25 | 1 | Similar tier — multimodal jailbreak |
| 6Mxhg9PtDE.md | 9.50 | 1 | Stronger — "Safety Alignment > a few tokens deep," very influential analogue |
| tyEyYT267x.md | 8.00 | 1 | Stronger — SAR diffusion LM, broader impact |
| syThiTmWWm.md | 7.75 | 1 | Different topic |
| Bo62NeU6VF.md (read) | 8.00 | 1 | Stronger conceptual cousin — Backtracking for ARMs; broader applicability |
| 0VZP2Dr9KX.md | 5.25 | 2 | Weaker — baseline defenses survey |
| V01FPV3SNY.md | 5.33 | 2 | Weaker — inference-time wrapper defense |
| kUH1yPMAn7.md | 6.00 | 2 | Similar tier — safety-layer analysis |
| EbxYDBhE3S.md | 6.00 | 2 | Similar tier — black-box backdoor defense |
| Nsms7NeU2x.md | 6.75 | 2 | Different topic |
| MoJSnVZ59d.md | 6.40 | 2 | Similar tier — SafeDPO, single-method safety alignment |
| sGqd1tF8P8.md | 6.80 | 2 | Adjacent — weak-LLM teacher for alignment |
| o2uHg0Skil.md | 6.25 | 2 | Different topic — KL regularization theory |
| e9yfCY7Q3U.md | 6.25 | 2 | Similar tier — improved GCG, scope narrower than this paper |
| LsTIW9VAF7.md | 5.80 | 2 | Different topic |
| iKgQOAtvsD.md | 5.75 | 2 | Similar tier — adversarial prompt translation |
| u08UxVNdIo.md (read) | 4.75 | 1 | Clearly weaker than this paper |
| Bo62NeU6VF.md (read) | 8.00 | 1 | Stronger; more universal recovery mechanism |

Round-1 bracket: [5, 8]. Round-2 narrowed it to the 6.0–6.5 cluster: paper is clearly stronger than DiffusionAttacker (4.75) but does not reach Backtracking (8.0) — its scope is more niche (MDLM-only), and residual ReNeLLM/late-intervention vulnerabilities meaningfully bound the contribution. Compared to Improved GCG (6.25) and SafeDPO (6.40), this paper offers both a novel diagnosis and a working defense in a less-explored model class, but with a somewhat decorative theorem and an incomplete safety-cost picture (no false-refusal eval). Landing at 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>