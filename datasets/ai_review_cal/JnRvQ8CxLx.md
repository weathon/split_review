- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3
Now I have a thorough understanding of the paper. Let me construct the final consolidated review, carefully filtering the reviewer inputs against what the paper actually says.

---

## Summary

This paper proposes IDEATOR, a black-box jailbreak attack against Vision-Language Models that uses a VLM (MiniGPT-4 with Vicuna-13B) as an autonomous attacker. The attacker generates structured JSON outputs containing image prompts (realized via Stable Diffusion) and text prompts, then iteratively refines its strategy based on victim responses using a breadth-depth exploration algorithm. Experiments on AdvBench and VAJM datasets show a 94% attack success rate on MiniGPT-4, matching the white-box state-of-the-art UMK, with strong transferability to LLaVA (82%) and InstructBLIP (88%).

## Strengths

1. **Novel framework using a VLM as a black-box jailbreak generator.** The paper introduces a concrete system that repurposes a VLM (via system prompt engineering, not additional training) as a red-teaming agent capable of autonomously producing multimodal jailbreak prompts through iterative interaction. This is a genuinely new paradigm that moves beyond both white-box adversarial optimization and manually curated attacks. (Supported by Section 3, Algorithm 1, Figure 2.)

2. **State-of-the-art attack success rate in a black-box setting.** IDEATOR achieves 94% ASR on MiniGPT-4 (AdvBench, Table 1), matching the white-box UMK (94%) and substantially outperforming the black-box baseline MM-SafetyBench (66%) and all unimodal white-box attacks (GCG, GCG-V, VAJM). This is the first demonstration that a VLM-based black-box attacker can match methods requiring parameter access.

3. **High transferability across victim VLMs.** Jailbreak prompts generated on MiniGPT-4 maintain 82% ASR on LLaVA (LLaMA-2-based) and 88% on InstructBLIP, compared to only 46% and 29% for MM-SafetyBench (Table 3). This shows IDEATOR discovers vulnerabilities that are not specific to the victim model it was generated on.

4. **Well-designed ablation studies validate core design choices.** Table 4 shows ASR rising from 45% (breadth=1, depth=1) to 94% (breadth=7, depth=3), confirming the breadth-depth exploration strategy. Table 5 shows combined image-text attacks achieve 94% ASR with fewest queries, versus 70% for text-only and 51% for image-only, validating the multimodal approach.

5. **Effectiveness on challenging safety categories.** On the VAJM evaluation set (Table 2), IDEATOR achieves 100% ASR on Identity Attack and 66.7% on X-risk categories, outperforming even white-box methods on these hard cases, revealing vulnerabilities that adversarial-image approaches miss.

## Weaknesses

### Fatal
None.

### Major
None that threaten the paper's core claims. Each significant concern listed below is addressable.

### Minor

1. **Attacker and primary victim are the same VLM architecture.** The paper states: "We employ the Vicuna-13B version of MiniGPT-4 as both the attacker and victim VLM in our experiments" (line 142). While the black-box nature of the attack (no parameter access) and the strong transfer results (82% on LLaVA, a LLaMA-2-based model) mitigate this concern, the paper's claim that "a VLM itself might be a powerful red team model" would be more convincing with at least one experiment using a different attacker VLM (e.g., LLaVA as attacker against MiniGPT-4). The paper reports that GPT-4o was tested as attacker but failed (lines 90–91), which is informative but does not substitute for a test with another open VLM. This limits the generality of the claim that the *method* is VLM-agnostic, though the transfer results already show the *generated attacks* are victim-agnostic.

2. **Section 4.4's set-theoretic formalism is imprecise.** The paper introduces asymptotic sets $\mathcal{A}_{\mathrm{IDEATOR}}$ and claims set inclusion relationships (e.g., $A_{\mathrm{IDEATOR}} \supseteq A_{\mathrm{MM-SB}}$) based on a few visual examples (lines 182–195). The derivation then assumes independence of attack types to write $ASR = 1 - \prod(1-ASR_i)$, which is unsupported. This section does not provide rigorous evidence and the notation implies a precision the analysis does not deliver. The visual examples (Figures 4, 5) illustrating diverse attack strategies are useful; the mathematical framing should either be removed or replaced with a systematic categorization (e.g., frequency counts of attack types found across the 100 jailbreak goals).

3. **No ethical considerations section.** The paper produces harmful content (jailbreak prompts, adversarial images) and discusses releasing a benchmark dataset, but includes no discussion of ethical considerations, responsible disclosure, or harm mitigation. This is a standard expectation for safety/security papers.

4. **No statistical variance or confidence intervals.** ASR results in Tables 1–3 are reported as point estimates with N=100 (and N=40 for VAJM), but no confidence intervals, standard deviations, or run-to-run variance are reported. Bootstrapped CIs would add credibility, especially for the headline comparisons.

5. **Unimodal ablation construction is underspecified.** Table 5 compares "Adv Text," "Adv Img," and the combined attack, but the paper does not state whether the unimodal variants were generated independently (configuring IDEATOR to never produce images/text) or extracted from the jointly generated multimodal output. If the latter, the text-only and image-only attacks may be suboptimal because they were designed assuming the other modality would be present. Clarifying this is needed for the ablation to be properly interpretable.

### Trivial

- The claim "IDEATOR is the first red team model for VLMs" (line 24) is slightly overstated — MM-SafetyBench is also a black-box red-teaming method for VLMs, albeit human-designed rather than VLM-driven. The novelty in using a *VLM as the attacker* is clear and should be stated precisely.

## Nice-to-Haves

- **Query cost comparison with baselines.** The paper reports average queries for IDEATOR (Table 5) but does not compare sample efficiency against baselines (e.g., GCG may require thousands of gradient steps but is less sample-efficient in terms of model queries; MM-SafetyBench uses a single query). This would help practitioners assess practical utility.
- **Evaluation against defenses.** The paper motivates IDEATOR by arguing adversarial images are "easily detectable" but does not test whether IDEATOR's generated images evade existing safety filters or image anomaly detectors. A brief robustness evaluation would strengthen the paper.
- **Handling of refusal responses.** The paper does not specify what happens when the victim outputs an outright refusal (e.g., "I cannot help with that") — whether the attacker still receives an image and produces an analysis, and how the CoT reasoning handles failed rounds.

## Removed Points

*These points appeared in the original reviews but were removed after verification against the paper.*

- **White-box comparison lacks transparency:** Removed. The paper explicitly states that 100 goals were randomly selected for testing and the remaining 420 were reserved "for the adversarial optimization of white-box attack methods" (line 138). The standard UAP evaluation protocol (train on one set, test on another) is followed and clearly described. This is not an unfair asymmetry — IDEATOR is training-free, so using the same 100 goals is reasonable.
- **Various formatting/presentation nitpicks:** Removed per instructions — parser artifacts, not author errors.
- **"The paper may specify X in the appendix":** Removed — the appendix is stripped by the parser and should not be assumed absent.
- **Speculative concerns about missing related work:** Removed per instructions (cannot verify without external sources).
- **The strength about "IDEATOR subsumes existing attack types":** Downgraded from a strength. The evidence for this is a few visual examples and the weak set-theoretic argument in Section 4.4, not a systematic analysis. The core empirical claims (ASR, transferability, ablation) are strong enough without over-claiming on coverage.

## Novel Insights

None beyond the paper's own contributions. The reviews identify a genuine tension around the attacker/victim being the same VLM, but the transfer experiments already provide a partial answer; neither reviewer offers a fundamentally new framing or observation that the paper itself does not anticipate.

## Suggestions

1. **Add a cross-attacker experiment.** Swap the attacker to LLaVA or InstructBLIP and measure ASR on MiniGPT-4. If the method remains effective, the generality claim is substantially strengthened. If it drops, the result is still informative and the paper can honestly scope its claims to the setting demonstrated.
2. **Replace Section 4.4's formalism with concrete analysis.** Instead of the set-theoretic notation, categorize the jailbreak strategies IDEATOR generates across the 100 goals (roleplay, typographic, emotional manipulation, authority appeal, etc.) with frequency counts and representative examples. This would be genuine empirical evidence of diversity.
3. **Add an ethical considerations section** discussing potential misuse, the use of open models, and any steps taken to limit harm from the release of attack prompts.
4. **Report bootstrapped 95% confidence intervals** for all key ASR results, or at minimum note the number of runs.
5. **Clarify how the unimodal ablations (Table 5) were constructed** — whether each variant was generated independently or extracted from multimodal outputs.
