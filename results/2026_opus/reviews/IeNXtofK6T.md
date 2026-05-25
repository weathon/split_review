Now let me do calibration searches against human-reviewed anchors.Round 1 bracket: roughly 5.0-7.0. The paper is more thorough than "Baseline Defenses" (5.25) — multiple benchmarks, multiple models, adaptive attack experiments, memorization control. Let me narrow.## Summary
The paper revisits a long-dismissed baseline for prompt injection defense: directly asking an off-the-shelf LLM (the "guardrail LLM") whether a data sample contains an injected prompt, and, if so, removing the injection. The authors argue that modern reasoning-capable LLMs (GPT-4o/4.1, Qwen3-32B) push the false positive/negative rates of this simple approach below 1% on AgentDojo and below 5% on Open Prompt Injection and TensorTrust, and that this should now be treated as the standard baseline for future prompt-injection defense papers.

## Strengths
- **Strong in-distribution detection numbers.** Table 1 shows FPR/FNR < 1% on AgentDojo for GPT-4o (0.07% / 0.23%) and GPT-4.1 (0.56% / 0.13%), and < 5% on the other two benchmarks. These are concrete results that directly support the paper's core empirical claim.
- **End-to-end agent metrics, not just detection.** Table 2 reports utility under attack and ASR alongside FPR/FNR (e.g., PromptArmor-GPT-4.1 drives ASR from 54.53% → 0.00% on AgentDojo). This makes the comparison with other defenses meaningful rather than detector-only.
- **Reasoning/size ablation isolates the driver.** Section 4.4 / Figure 3 with Qwen3-0.6B/8B/32B in reasoning and non-reasoning modes shows that scale (32B vs 0.6B) matters most, and reasoning gives an additional boost in mid-sized models. This supports the paper's thesis that modern reasoning ability is the reason this baseline now works.
- **Memorization control.** Section 4.5 runs the Carlini/Staab memorization test on GPT-4.1 against AgentDojo (avg similarity 0.34; 3.5% exceed the 0.6 edit-distance threshold), addressing a natural concern about contamination.
- **Prompt-strategy ablation explains older negative results.** Table 3 shows GPT-3.5's FNR drops from 60.24% → 15.74% when the definition of "prompt injection" is included, giving a concrete mechanism for why 2023-era prompting-based defenses failed.

## Weaknesses

### Fatal
None.

### Major
- **Adaptive attack is not detector-aware.** Section 4.6 runs AgentVigil against the combined agent + PromptArmor system, optimizing on end-to-end ASR. That gives the attacker reward signal from the full pipeline but no specific gradient toward evading the guardrail — the resulting templates are ones that defeat the backend, not ones designed to look benign to the detector. Because the paper's core pitch is "this should be the baseline future defenses must beat," demonstrating robustness against a detector-aware adversary (e.g., an LLM-as-attacker loop that rewrites injections until the guardrail labels them "No" while preserving payload, or natural-language phrasings that mimic legitimate tool output) is essential. As written, the conclusion that PromptArmor is "robust against adaptive attacks" outruns the evidence in Table 4.
- **Comparison with fine-tuned detectors is not apples-to-apples.** Table 2 contrasts PromptArmor on GPT-4.1 with DataSentinel (Mistral-7B base) and Llama Prompt Guard 2 / DeBERTa (small specialized models). The paper itself notes on p.7 that DataSentinel's released checkpoint uses Mistral-7B and was not adapted to agent settings. That essentially concedes the comparison is "frontier model vs. small model" rather than "prompting vs. fine-tuning." A controlled experiment — e.g., the PromptArmor prompt vs. a DataSentinel-style fine-tune of the same base (Qwen3-8B/32B is natural given existing experiments) — would isolate which factor is driving the gains. Without it, the headline claim that the prompted baseline outcompetes specialized detectors is supported only weakly.

### Minor
- **Attack distribution is pattern-heavy.** AgentDojo's four attack styles all use overt anchor phrases ("Ignore previous instructions," "### System," "### Important Messages") and Open Prompt Injection's "Escape Characters," "Context Ignoring," and "Fake Completion" categories are syntactic. A frontier LLM keyed on "instruction-like patterns" is essentially trained to flag these. Stealthier injections — natural-language attacks without anchor phrases, injections framed as plausible business directives, or attacks split across data items — are not evaluated. The claim is then better-supported as "near-perfect on currently benchmarked attacks" than as a universal baseline.
- **Deployment-cost framing.** Section 3.2 advertises "computational efficiency" while the headline results use a full GPT-4.1 call per tool-call result, with no token/latency numbers reported. Qwen3-32B is shown to match GPT-4.1, which mitigates this somewhat, but the "easy to deploy" framing would be more credible with a concrete cost analysis on a representative AgentDojo trajectory.
- **Memorization control covers only AgentDojo.** Open Prompt Injection and TensorTrust are older and likely more represented on the public web, so extending the memorization test to those benchmarks would strengthen the claim that performance is not contamination-driven.
- **Negative-sample construction.** The TensorTrust negative set is "the correct access code," which is one short string per attack instance. The FPR computed against such a thin distribution carries less information than the headline implies; specifying the per-benchmark denominators explicitly would help readers calibrate.
- **Unexplained quirks in Table 4 / Table 2.** (a) In Table 4, the "No defense" ASR for AgentVigil-Adaptive (21.46%) is lower than for AgentVigil-NoDefense (52.73%), presumably because templates optimized against the defended system aren't optimal against the undefended one — but this should be stated. (b) In Table 2, UA = 72.02% with PromptArmor-GPT-4.1 exceeds UA = 64.27% with no defense; the explanation (the defense lets the original task complete instead of being diverted) is plausible but warrants one explicit sentence.

### Trivial
- "Carefully designed system prompt" oversells what Figure 2 reveals to be a roughly two-sentence prompt; the more accurate framing — confirmed by Section 4.3 — is "any reasonable prompt works once the guardrail LLM is strong enough."

## Nice-to-Haves
- A detector-aware adaptive-attack experiment (LLM-as-attacker rewriting injections until the guardrail labels them benign).
- Same-base-model comparison: PromptArmor-prompt vs. DataSentinel-style fine-tune on Qwen3-8B/32B.
- FNR breakdown by attack type and domain, especially on Open Prompt Injection where the residual FNR is 2–5%.
- Per-tool-call token count and wall-clock latency for GPT-4.1 and Qwen3-32B on a representative AgentDojo task.
- A simple stealth-injection test: have GPT-4 rewrite AgentDojo injections to drop anchor phrases while preserving the malicious objective, and re-measure FNR.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- *Reviewer concern that FNR > 0 alongside ASR = 0% is "inconsistent."* This is logically fine — missed injections are simply ones that wouldn't have succeeded at the backend anyway. Worth a sentence in the paper but not a real weakness.
- *Reviewer suggestion to "use a shared base for fine-tuning vs. prompting" framed as structural.* Kept as a Major weakness in the main review (controlled comparison), but the harsh framing that this is "fatal" overstates it — the paper does explicitly acknowledge the Mistral-7B caveat, which moves this from fatal to major.
- *General strengths from the Strength Finder about "comprehensive evaluation" across three benchmarks.* Kept implicitly via specific Table-1 evidence; dropped as a standalone bullet because it overlaps the detection-results strength already listed.

## Novel Insights
None beyond the paper's own contributions. The most genuinely useful synthesis from the reviews is the observation that the paper's central claim is essentially "modern model capability, not prompt design, makes this baseline work" — Table 3 and the Qwen3 ablation both point to this, and stating it plainly would tighten the paper's framing.

## Suggestions
- Add a detector-aware adaptive-attack experiment as a new subsection (e.g., 4.7). Either an LLM-as-attacker rewrite loop or a search over phrasings that minimize the guardrail's "Yes" probability while preserving downstream effect.
- Run at least one same-base comparison (e.g., Qwen3-32B prompted as PromptArmor vs. a DataSentinel-style fine-tune of Qwen3-32B) so Table 2 can be read as evidence about technique rather than scale.
- Soften the "carefully designed system prompt" and "robust against adaptive attacks" framing to match the evidence. The paper is stronger as "modern reasoning LLMs are sufficient to make a trivial prompt work as a guardrail under benchmarked attacks" than as "carefully engineered detector robust to adaptive adversaries."
- Add per-call cost/latency numbers and a brief discussion of when frontier-model overhead is acceptable.
- Extend the memorization control to Open Prompt Injection and TensorTrust; report robustness at multiple edit-distance thresholds.

## Calibration

Anchors retrieved:

| Path | Avg Score | Round | Comparison to PromptArmor |
|---|---|---|---|
| 3MDmM0rMPQ.md (Inverse Prompt Engineering) | 3.00 | R1 (low) | Weaker scope, methodologically thinner |
| MV5j4Qpq7N.md (System-Prompt Attention) | 2.33 | R1 (low) | Less rigorous evaluation, narrower |
| KjxZ4BdUdN.md (Wildflare GuardRail) | 3.00 | R1 (low) | More complex pipeline, less focused empirics |
| lUyYX9VFgA.md (Code-of-thought) | 3.00 | R1 (low) | Different topic; less relevant |
| 0VZP2Dr9KX.md (Baseline Defenses for Adversarial Attacks) | 5.25 | R1+R2 (mid) | Most similar in spirit; PromptArmor is more thorough (multiple benchmarks, multiple model families, adaptive + memorization checks) |
| YixNDE12wm.md (GuardAgent) | 6.00 | R1 (mid) | More novel architecture but narrower benchmarks; comparable rigor |
| V01FPV3SNY.md (RA-LLM) | 5.33 | R1 (mid) | Comparable empirical defense paper, similar limitations re adaptive attacks |
| RC5x3OkywQ.md (FJD) | 4.25 | R1 (mid) | Less polished evaluation |
| JwoCs9O3QL.md (VLMGuard) | 5.00 | R1 (mid) | Different modality; similar tier |
| syThiTmWWm.md (Cheating Automatic LLM Benchmarks) | 7.75 | R1 (high) | Much more striking and broadly impactful finding |
| tc90LV0yRL.md (Cybench) | 8.67 | R1 (high) | Major benchmark contribution; higher tier |
| 6Mxhg9PtDE.md (Shallow Safety Alignment) | 9.50 | R1 (high) | Substantially deeper conceptual contribution |
| tTPHgb0EtV.md (Booster) | 8.00 | R1 (high) | Stronger technical contribution |
| FD9sPyS8ve.md (Purple Problem) | 4.75 | R2 (mid) | Sharper conceptual point; PromptArmor has broader empirics |
| ikqcUzUogm.md (Programmatic Rule-Following) | 4.75 | R2 (mid) | Comparable tier |
| RdGvvqjkC1.md (How Jailbreak Defenses Work) | 5.75 | R2 (mid) | Comparable empirics; similar tier |
| p3mxzKmuZy.md (SemSI Benchmark) | 5.33 | R2 (mid) | Comparable tier |
| leSbzBtofH.md (AutoAdvExBench) | 6.17 | R2 (mid) | Stronger novelty, comparable execution |
| V4y0CpX4hK.md (Agent Security Bench) | 6.25 | R2 (mid) | Broader benchmark contribution, accepted |
| AC5n7xHuR1.md (AgentHarm) | 6.75 | R2 (mid) | More original benchmark, accepted |
| V892sBHUbN.md (Rapid Response) | 5.75 | R2 (mid) | Very similar profile — promising defense, but limited adaptive-attack rigor |
| fsW7wJGLBd.md (Tensor Trust dataset) | 7.00 | R2 (mid) | Bigger dataset contribution |

Round-1 bracket: **5.0–7.0**. Round-2 narrowing confirms PromptArmor sits roughly with "Rapid Response" (5.75) and "Baseline Defenses" (5.25) in profile — convincing empirical detection results, but a limited adaptive-attack evaluation and an asymmetric baseline comparison hold it back from the 6.25–6.75 anchor tier (ASB, AgentHarm) which have either broader benchmark contributions or sharper conceptual claims. PromptArmor is more thorough and better-framed than "Baseline Defenses" (5.25) but lacks the breadth/novelty of the 6.25+ accepted papers. The Major weakness about detector-aware adaptive attacks is the key reason it doesn't reach the ASB tier.

**Originality:** Low — the method is canonically simple, and the paper is explicit about being a baseline-revisiting work, not a novel mechanism. **Importance:** Real and current — prompt injection defenses are an active subfield and a credible baseline is genuinely useful. **Claim support:** Strong for detection on benchmarked attacks; weaker for "robust to adaptive attacks" and "outcompetes fine-tuned detectors." **Soundness of experiments:** Mostly solid, with thoughtful ablations (reasoning/size, prompt strategy, memorization); the adaptive-attack design is the main soundness gap. **Clarity:** Good — the paper is easy to read and the framing is clean. **Value to community:** Real — future defense papers benefit from a tightly-specified, strong baseline to compare against.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>