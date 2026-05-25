Now I have enough calibration context. Let me produce the final consolidated review.

## Summary of Calibration

**Round-1 Bracket**: The paper is clearly above the low-band anchors (2.33–3.00, all with fundamental methodology flaws) and well below the high-band anchors (8.00, all accepted with strong theoretical or technical contributions). It falls in the middle band (4.25–5.75) alongside SPIN (5.50), JudgeRail (5.75), Baseline Defenses (5.25), and Rapid Response (5.75)—all of which were rejected.

**Round-2 Narrowing**: Within the 4.5–6.5 band, the paper is most comparable to SPIN (5.50) and Rapid Response (5.75). It has broader and more rigorous evaluation than SPIN (which tested only two models) but similar methodological gaps (no variance reporting, limited adaptive attack coverage). All comparably-scored papers in this topic area were rejected.

**What low-band anchors failed at**: Papers scoring ≤3.0 had unclear methodology, minimal/confounded evaluation, or unsubstantiated central claims. The current paper does NOT share those failures—it has a clear method, solid primary evaluation on AgentDojo (629 scenarios), and well-executed ablation studies.

**Weakness-anchored evidence**: The "no confidence intervals" query returned a paper scoring 4.17 (Reject) that directly studies the problem of unreported variance in evaluation benchmarks—confirming this is a recognized methodological flaw that depresses scores.

---

Now writing the review.

## Summary
This paper revisits the idea of using an off-the-shelf LLM as a guardrail to detect and remove prompt injections, with the key insight that modern LLMs' improved reasoning capabilities make this simple approach far more effective than reported in prior work (which used older, weaker models). PromptArmor prompts a guardrail LLM to detect whether a data sample contains injected content, then uses fuzzy matching to remove the identified injection. Evaluated on AgentDojo, Open Prompt Injection, and TensorTrust, PromptArmor with GPT-4.1 achieves 0.00% attack success rate and 72.02% utility under attack on AgentDojo, substantially outperforming existing detection-based and prompt-augmentation defenses. The paper also provides ablation studies on model size and reasoning (Qwen3 family), a memorization test, and a limited adaptive attack evaluation.

## Strengths

- **Strong primary empirical results on AgentDojo**: Table 2 shows PromptArmor-GPT-4.1 achieves 0.00% ASR and 72.02% UA on the AgentDojo benchmark, compared to 54.53% ASR undefended and 38.63% ASR for the best detection-based alternative (DataSentinel). This directly supports the paper's core claim that prompting a modern off-the-shelf LLM is a highly effective defense.

- **Informative analysis of model capacity and reasoning**: Section 4.4 and Figure 3 systematically evaluate the Qwen3 family (0.6B, 8B, 32B) in both reasoning and non-reasoning modes, showing that sufficient model capacity (≥32B) is the primary driver of strong performance while reasoning provides additional benefit at intermediate sizes. This analysis is well-designed and yields actionable insights.

- **Memorization test rules out data contamination**: Section 4.5 applies a standard prefix-suffix memorization test to GPT-4.1 on AgentDojo data (avg similarity 0.34, only 3.5% above threshold 0.6), convincingly showing that the guardrail's performance is not due to benchmark memorization.

- **Cross-benchmark evaluation**: The method is tested across three diverse benchmarks covering agent and non-agent scenarios (AgentDojo, Open Prompt Injection, TensorTrust), demonstrating the approach is not tied to a single domain.

- **Clear and well-motivated writing**: The paper is structured logically, the problem definition is precise, and the contribution (reviving a simple approach in light of new model capabilities) is clearly stated.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No uncertainty quantification on sampled benchmarks (Section 4.1, Table 1)**: For Open Prompt Injection and TensorTrust, the test sets are constructed by randomly sampling 100 tasks, but only single point estimates for FPR/FNR are reported with no confidence intervals, no replication across random seeds, and no discussion of sampling variance. With only 100 samples, the reported rates could shift by 1–2 percentage points under a different draw. The primary AgentDojo results (Section 4.2, Table 2) use the full 629-scenario benchmark and are unaffected by this issue, so this does not threaten the core claim—but it weakens confidence in the secondary generalization claims ("below 5% on Open Prompt Injection and TensorTrust").

- **Limited adaptive attack evaluation (Section 4.6)**: The adaptive robustness evaluation uses a single automated red-teaming method (AgentVigil). The paper does not characterize the attack space AgentVigil explores, nor does it test attacks that the guardrail's fuzzy matching might miss (e.g., encoding obfuscation, split injections, adversarial suffixes tuned against the guardrail). The claim of robustness is appropriately qualified as "against fuzzing-based adaptive attacks" in the section, but the broader language in the abstract ("robust against adaptive attacks") could mislead readers about the evaluation's scope.

- **Claim about newer models' prompting robustness without supporting data (Section 4.3)**: The paper states that "newer models like GPT-4o and GPT-4.1 perform equally well across different prompting strategies" to justify showing the prompting-strategy ablation only on GPT-3.5. No experimental data is presented to support this claim about GPT-4o/4.1. A simple table or figure would substantiate the claim or reveal interesting variation.

- **Memorization test only on AgentDojo (Section 4.5)**: The contamination analysis is only applied to AgentDojo data. For completeness, the same test on the other two benchmarks would strengthen the claim that performance is not due to memorization.

- **Missing discussion of fuzzy matching edge cases (Section 3.1)**: The fuzzy matching step uses a regex that allows arbitrary characters between extracted words. The paper does not discuss what happens with non-contiguous injections, multiple simultaneous injections, or cases where extracted content partially overlaps with benign data, nor how often such cases occur in the benchmarks.

### Trivial

- The paper does not report the specific model version/date for GPT-4.1 (e.g., gpt-4.1-2025-04-14), which would aid reproducibility given API model updates.
- The embedded table in Figure 3 repeats data already visible in the bar charts, making the figure dense without adding information.

## Nice-to-Haves

- **Clean utility evaluation**: Reporting user task success rate on clean (non-attacked) AgentDojo tasks would isolate the side effect of false-positive removals and help assess practical usability. Currently, UA is only reported under attack.
- **Failure case analysis**: A few qualitative examples of false positives and false negatives would help readers understand the nature of remaining errors.
- **Latency/cost estimates**: Since the paper advocates PromptArmor as a practical baseline, approximate latency and API cost per data sample on AgentDojo would be helpful.

## Removed Points

The following points from the reviewers were removed after cross-checking against the paper:

- **"Unsupported dismissal of training-based defenses"**: The paper excludes training-based defenses (SecAlign etc.) with a citation to Jia et al. (2025) supporting the claim of poor utility. The paper does not claim to outperform these defenses—it establishes a simple baseline. Criticizing this exclusion is scope creep for a baseline paper, and the justification (with citation) is adequate for this purpose.
- **"PromptArmor and DataSentinel are both detection-based so the categorization is unclear"**: PromptArmor does not use fine-tuning while DataSentinel does; this is a meaningful distinction. The categorization in the paper is clear enough.
- **Purely parser-introduced formatting issues** (typos, missing appendix references, garbled equations): These are PDF-extraction artifacts, not author errors.
- **Reproducibility nitpicks about undisclosed implementation details** (hyperparameters, training logs): Not applicable for a prompting-based method with temperature=0.

## Novel Insights

The most interesting observation to emerge from the reviews is the asymmetry between the paper's explicit contribution (a practical defense) and the implicit insight: model *capacity*, not sophisticated algorithm design, is the primary bottleneck for LLM-based prompt injection detection. The Qwen3 ablation (Section 4.4) cleanly demonstrates that scaling model size from 0.6B→32B matters more than toggling reasoning on/off, and that even the 8B model with reasoning cannot match a 32B model without reasoning. This suggests that the literature's pivot toward fine-tuned specialized detectors may be premature—the field might get more mileage from simply using larger, general-purpose models as zero-shot detectors. The memorization test further reinforces that strong performance does not require benchmark-specific training data exposure.

## Suggestions

1. **Add confidence intervals for sampled benchmarks**: Run the Open Prompt Injection and TensorTrust sampling with 5–10 different random seeds and report the range or standard deviation of FPR/FNR. This is low-effort and would substantially increase credibility.
2. **Broaden the adaptive attack evaluation**: Include at least one additional attack method (e.g., a simple encoding-based bypass or a black-box adversarial suffix optimizer targeting the guardrail) to strengthen the robustness claim.
3. **Provide evidence for the GPT-4o/4.1 prompting claim**: Show a small table or figure demonstrating the effect (or lack thereof) of varying prompts on GPT-4o/4.1 performance in Section 4.3, rather than stating it without data.
4. **Add clean utility numbers**: Report UA on non-attacked AgentDojo tasks to quantify the cost of false positives for practical deployment.
5. **Add a limitations paragraph** discussing fuzzy matching edge cases and the scope of the adaptive attack evaluation.

## Score and Decision

**Anchors consulted:**

| Anchor | Score | Round/Query | Comparison |
|--------|-------|-------------|------------|
| SPIN (PNHGYziAsL) | 5.50 | R1-topic-mid | Similar topic defense paper; tested only 2 models vs. this paper's broader eval → comparable quality |
| VLMGuard (JwoCs9O3QL) | 5.00 | R1-topic-mid | VLM defense with unclear motivation; weaker than this paper |
| Baseline Defenses (0VZP2Dr9KX) | 5.25 | R2 | Evaluated baseline defenses; single-attack study, inconsistent setups → weaker than this paper |
| JudgeRail (CEvGuwMum0) | 5.75 | R2 | Harmful text detection framework; novelty concerns, limited justification → comparable |
| Rapid Response (V892sBHUbN) | 5.75 | R2 | Rapid response paradigm for jailbreaks; novel idea, some methodological gaps → comparable |
| RA-LLM (V01FPV3SNY) | 5.33 | R2 | Defending against alignment-breaking attacks → comparable |
| Inverse Prompt Engineering (3MDmM0rMPQ) | 3.00 | R1-topic-low | Guardrail paper with fundamental methodology issues; this paper is clearly stronger |
| Wildflare GuardRail (KjxZ4BdUdN) | 3.00 | R1-topic-low | Multi-component guardrail; weak evaluation; this paper is clearly stronger |
| Quantifying Variance (E2RyjrBMVZ) | 4.17 | R1-weakness | Directly about unreported variance in benchmarks; confirms this as a real flaw |
| Simple Adaptive Attacks (hXA8wqRdyV) | 6.14 | R1-weakness | Demonstrates importance of adaptive attack evaluation (accepted); this paper's adaptive eval is less thorough |

All middle-band comparators (4.25–5.75) were rejected. The paper shares no failure modes with low-band anchors (2.33–3.00). It shares the "no confidence intervals" weakness with papers scoring in the 4–5 range. Its adaptive attack evaluation is less thorough than the Simple Adaptive Attacks paper (6.14, accepted), consistent with its lower overall score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>