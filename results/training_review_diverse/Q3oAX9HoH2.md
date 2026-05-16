## Summary

This paper proposes DeepInception, a lightweight, training-free jailbreak method that induces LLMs to produce harmful content by having them imagine a nested (multi-layer, multi-character) fictional scene. Inspired by the Milgram experiment's authority-obedience paradigm, the method uses a single universal prompt template that works across open-source (Llama-2, Vicuna, Falcon, Llama-3) and closed-source (GPT-3.5, GPT-4, GPT-4o, o1) models. The key empirical finding is a "continuous jailbreak" effect: after a single DeepInception prompt, subsequent direct (non-nested) requests continue to elicit harmful content at elevated rates, suggesting the model remains in a "hypnotized" state.

## Strengths

- **Novel and effective jailbreak approach**: The nested-scene prompt design is a genuine methodological contribution. The decomposition into Scene, Layers, and Characters, and the demonstration that combining all three outperforms partial configurations (Figure 8d), provides actionable design principles. The method is training-free, black-box, and uses a single universal template — a practical advantage over optimization-based attacks like GCG or AutoDAN that require white-box access.

- **Demonstration of continuous jailbreak**: The finding that a single DeepInception prompt leaves LLMs persistently vulnerable to subsequent direct (non-nested) harmful requests (Tables 5, 6) is a noteworthy and nontrivial insight. Prior jailbreak evaluations overwhelmingly focus on single-shot attacks; showing a persistent effect opens a new axis for safety evaluation.

- **Broad empirical coverage**: The method is evaluated on six LLMs spanning open-source (Llama-2, Llama-3, Vicuna, Falcon) and closed-source (GPT-3.5, GPT-4, GPT-4o) families, plus case studies on multimodal GPT-4o and OpenAI o1. The systematic ablation (Figures 6, 8) isolates the contribution of each factor (scene, layers, characters) and provides both scientific insight and practical guidance.

- **PPL-based mechanistic evidence**: The perplexity analysis (Figure 7) offers quantitative support for the "Jointly Inducing" effect — DeepInception yields lower perplexity for harmful outputs compared to PAP and Direct baselines, consistent with the claim that the nested context increases the model's conditional probability of generating harmful content.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed mechanism framing**: The paper presents a "mechanism" grounded in the Milgram experiment and claims to "discover the mechanism of inception" (line 34). However, the actual method is a prompt template — an effective one — and the formalization in §3.2 does not distinguish DeepInception from any multi-part prompt. Remark 3.2 essentially says "if the right hypnotizing content H' is sampled, the method works," which is tautological rather than predictive or testable. No experiment varies authority cues or tests whether LLMs actually exhibit the psychological state of "self-losing under authority" vs. simply following any detailed narrative framing. The Milgram analogy is evocative design inspiration, but the paper's language systematically overstates it as a discovered mechanism. This framing mismatch weakens the paper's narrative coherence: the contribution is an effective empirical jailbreak method, not a validated psychological mechanism for LLM behavior.

- **Insufficient statistical rigor in evaluation**: No confidence intervals, standard deviations, or statistical tests are reported for any Harmfulness% numbers in the main results (Tables 2, 4, 5, 6). The evaluation relies entirely on GPT-4-as-judge without human validation or inter-rater agreement. While GPT-4-as-judge is common in this line of work, the complete absence of any measure of variability or reliability means the reader cannot assess whether observed differences between methods are meaningful. The ablation study (Figure 8) uses a sub-sampled set with only three repetitions per condition and no significance testing. For a paper whose entire evidential weight rests on comparative harmfulness percentages, this gap is substantial.

- **Missing minimal control baseline in main comparison**: The ablation study (Figure 6) does compare None, Scene-only, Layers-only, and Full conditions. However, the main evaluation tables (Table 2, 4) do not include a minimal "indirect instruction without nesting" baseline (e.g., "Write a story about X" with no nested scene structure). Without this control in the primary comparison, it is unclear whether the gain comes from the specific nested design of DeepInception or from any multi-sentence framing that avoids a direct request. The ablation partially addresses this, but the main results tables are where readers and reviewers form their judgment, and the missing control there weakens the core comparative claims.

### Minor

- **PPL analysis does not control for confounds**: The perplexity comparison (Figure 7) shows DeepInception achieves lower PPL than PAP and Direct for harmful continuations. However, the paper does not control for prompt length or stylistic differences between methods. Lower PPL may partly reflect the model being more confident when prompted in a particular style rather than being evidence of a specific "inception" effect. Additionally, the harmful content H is sourced from "Vicuna with GCG" rather than being held constant across conditions, introducing a potential mismatch.

- **Defense evaluation is limited**: Only two defenses are tested (Self-reminder, In-context Defense), both described by the paper as relatively weak. Stronger defenses (e.g., SmoothLLM, well-tuned safety system prompts like Llama-2's default) are not evaluated. This limits the practical relevance of the defense analysis.

- **Limited failure analysis**: The paper mentions that "LLM may lose itself when being assigned too much layer construction for some scenes, like forgetting the original target" (line 164) and states it will conduct "failure case analysis" (line 160), but no systematic analysis of failure modes or the types of harmful requests DeepInception fails on is presented.

- **No ethics/responsible disclosure discussion**: Given the nature of jailbreak research that develops new attack methods, the paper would benefit from explicitly discussing responsible disclosure practices and whether the vulnerability has been reported to model providers. This is increasingly standard in safety-focused work.

### Trivial
- Line 104 contains a duplicated word: "we we following."
- The text "w.r.t.1).9)" (line 126) appears garbled, though this may be a parser artifact.

## Nice-to-Haves
- Human validation of a subset of GPT-4 judge evaluations to calibrate the automated metric.
- A more complete defense evaluation including stronger or more recent defenses.
- Systematic analysis of failure cases: which harmful request categories DeepInception struggles with.
- Controlling for prompt length and query budget in the comparison with PAIR and other baselines.

## Removed Points
These points are flagged to be removed from the reviewer's critique; treat them with caution.

1. *"Quantitative results appear as poorly rendered images with illegible or missing numerical data"* — The tables are present as embedded images in the text-extracted version; this is a parser extraction artifact, not an author error. The original PDF would contain properly formatted numerical tables.
2. *"Prompt template does not appear in the extracted content"* — The template is explicitly referenced at line 93 ("We provide a universal implementation...with the following prompt template") but appears to have been in a code block or box stripped by the parser. Again, a parser artifact.
3. *"Cannot evaluate Table 5/6 because numbers are not visible"* — Same parser artifact as above.
4. *"PAIR comparison should control for computational cost"* — The asymmetry in computational cost (PAIR uses an attacker LLM, DeepInception is lightweight) actually favors DeepInception; per instructions, criticisms where the asymmetry favors the author's method rather than the baseline should be removed from the main weaknesses.
5. *"The paper does not discuss cases where DeepInception fails"* — Factually inaccurate; the paper mentions forgetting targets under excessive layers (line 164) and states a failure case analysis was performed (line 160), even if the analysis is not presented in full depth.

## Novel Insights

The reviews surface a productive tension that goes beyond the paper's own contribution. The paper's core empirical finding — that nested scene instructions produce a *persistent* jailbreak effect across subsequent direct queries — is itself interesting and would be even more valuable if separated from the overclaimed psychological mechanism framing. The reviewers collectively identify that the paper would be stronger if it leaned into what it actually demonstrates (an effective, lightweight prompt strategy with a surprising carry-over effect) rather than what it cannot support (a Milgram-derived theory of LLM psychology). This suggests the community would benefit from an explicit taxonomy of prompt-level jailbreak strategies that distinguishes "narrative framing" from "role-play" from "authority-manipulation," since DeepInception's success may stem from generic narrative immersion rather than any authority-specific effect.

## Suggestions

1. Remove or substantially soften the causal mechanism language ("self-losing under authority," "discover the mechanism of inception") and reframe the paper as an empirical study of nested-scene prompt design. The Milgram experiment can remain as design inspiration, but the claims should match the evidence level.
2. Add confidence intervals (e.g., bootstrapped 95% CIs) to all main Harmfulness% results, and include a human-annotated calibration subset to validate the GPT-4 judge.
3. Include a minimal "indirect instruction without nesting" baseline (e.g., "Write a story about [topic]") in the main comparison table to isolate the specific contribution of the nested structure.
4. Include the prompt template explicitly in the main text (not just in appendix/figures) for reproducibility.

## Score and Decision

**Score**: 5.5

**Decision**: Weak Accept

The paper presents a genuinely effective and lightweight jailbreak method with a novel continuous-jailbreak finding that goes beyond prior single-shot evaluations. The empirical breadth across 6+ LLMs and the systematic ablation studies are solid contributions. However, the paper's framing significantly overclaims by presenting design inspiration (the Milgram experiment) as a "discovered mechanism," and the evaluation lacks the statistical rigor (no confidence intervals, single automated judge without human validation, no minimal control baseline in the main tables) needed to fully support the comparative claims of "leading harmfulness rates." These issues are addressable with revisions, and the core contribution — an effective nested-scene jailbreak method with demonstrated persistent effects — is real and worth publishing. A strong rejection would be inappropriate given the genuine novelty; an unconditional acceptance would overlook the framing and rigor gaps.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>