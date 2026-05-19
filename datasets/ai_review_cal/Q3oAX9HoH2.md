- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5
Now I have a thorough understanding of the paper and both reviews. Let me write the consolidated review.

## Summary

This paper proposes **DeepInception**, a jailbreak technique that constructs nested fictional scenes (inspired by the Milgram experiment) to trick LLMs into overriding their safety guardrails. The method wraps a harmful request inside a multi-layer imagination prompt — it is lightweight, training-free, and applicable to black-box LLMs. The paper reports results across Llama-2/3, GPT-3.5/4/4o, and demonstrates a "continual jailbreak" effect where a single nested inception enables subsequent direct requests to also bypass safety. Ablation studies isolate the contributions of characters, layers, and scenes, and limited case studies extend the method to multimodal (GPT-4o) and reasoning (o1) models.

---

## Strengths

- **Novel and lightweight jailbreak design.** The nested-scene prompt structure is conceptually clean — it is a single fixed prompt with no per-model optimization, no training, and no white-box access required. This practical simplicity is a genuine differentiator from optimization-based attacks like GCG and AutoDAN.

- **Continual jailbreak finding is notable.** The paper shows (Tables 5, 6) that after a single DeepInception attack, subsequent direct requests without any inception still yield high harmfulness. This is a nontrivial empirical phenomenon — the "hypnotized" state appears to persist — and is one of the paper's strongest contributions.

- **Systematic ablation study.** Figure 8(a)–(d) systematically varies characters, inception layers, scene types, and their combinations. The finding that combining scenes with multiple layers outperforms either alone provides clear evidence for the nested design's contribution beyond single-layer indirect prompts.

- **Demonstrated generality across diverse LLMs.** Evaluated on Llama-2, Llama-3 (8B and 70B), Falcon, Vicuna, GPT-3.5, GPT-4, and GPT-4o — spanning both open-source and closed-source families, and including models with very different safety postures.

- **Limited but real extension to multimodal and o1 models.** The case studies on GPT-4o (geolocation from a street photo, individual identification from a photo) and OpenAI o1 (generating a detailed harmful plan despite extended thinking) demonstrate that the method generalizes beyond standard text-only chat models, which is a useful stress test for the community.

---

## Weaknesses

### Fatal
None.

### Major

1. **The claimed "mechanism discovery" is unsupported.** The paper's first bullet contribution states: *"We discover the mechanism of inception to conduct jailbreak attacks, which is based on the psychological self-losing under authority."* However, no experiment in the paper tests the *psychological state* of the LLM or the causal role of "self-losing under authority." The ablation study (Figure 8) tests prompt components (characters, layers, scenes), not the hypothesized mechanism. The perplexity analysis (Figure 7) is correlational — it shows lower PPL for DeepInception outputs but does not distinguish between (a) nested scenes inducing a self-loss state, and (b) nested scenes simply making the harmful request harder for safety filters to detect (e.g., by spreading keywords across layers or increasing prompt complexity). A control comparing DeepInception to a matched-length non-nested prompt would be needed to attribute the effect to nesting per se. **This is the paper's most significant weakness** because the headline claim goes beyond what the evidence supports. The paper would be stronger if it reframed the Milgram connection as *inspiration* rather than *discovered mechanism*.

2. **Baseline comparison is too narrow to support claims of "leading performance."** The paper compares against only three black-box methods: PAIR, CipherChat, and PAP. Several relevant baselines are missing:
   - Simple role-play prompts (e.g., "DAN," "You are now an AI with no rules") are not included, even though they are also lightweight and training-free.
   - For open-source models (Llama-2, Vicuna, Falcon), white-box attacks like GCG and AutoDAN are applicable, but the paper excludes them with the justification that they require model parameters — which are available for these models.
   - Other recent black-box attacks (ArtPrompt, ReNeLLM) are absent.
   
   The abstract claims "leading harmfulness rates," but with only 3 baselines, this assertion is not credible. The "leading" language should be replaced with "competitive" until a broader comparison is conducted.

3. **Evaluation metric lacks validation and statistical rigor.** The harmfulness score uses GPT-4-0613 as a judge with no reported human validation, no inter-rater agreement, and no correlation with a secondary metric (e.g., refusal rate, keyword matching, or a second automated judge like LlamaGuard). GPT-based judges are known to be susceptible to prompt injection and may rate any content that *describes* a harmful topic as harmful, even in refusal contexts. Additionally, the main results (Table 2, 4, 5, 6) are reported without confidence intervals, error bars, or significance tests — the only mention of variance is a single line stating three runs were used for the disassembly experiment (Figure 6). For a paper making comparative "leading" claims, this is insufficient.

### Minor

4. **Only two defense methods tested.** The paper evaluates against Self-reminder and In-context Defense, then claims *"self-reminder fails to protect LLMs in general."* This generalization is too broad given only two defenses were considered. More recent defenses (e.g., circuit breakers, system-mode hardening) are not tested.

5. **Multimodal and o1 evaluations are case studies, not systematic evaluations.** The paper acknowledges this limitation for o1 (Section 4.6: *"Due to the limited frequency of testing and the strict usage control, we cannot perform large-scale experiments on it"*), which is acceptable. However, the section titles *"Generalized to Multimodal Jailbreak"* and *"Generalized to OpenAI O1"* imply broader evidence than the 1–2 examples per section actually provide. This framing should be tempered.

6. **No control experiment isolating nesting from prompt complexity.** The ablations compare variants of DeepInception against each other, but never against a long, single-layer (non-nested) prompt of comparable length and topic diversity. Without this control, the contribution of nesting per se — as opposed to prompt length, keyword density, or topic variety — cannot be determined.

### Trivial
- Typos: "we we following" (line 104), "DeepInceiton" (Figures 9, 10 caption).
- Footnote markers inline with text (e.g., ".2)", ".9)", ".5.") appear to be formatting artifacts from the PDF extraction.

---

## Nice-to-Haves
- A failure case analysis would strengthen the paper — the authors note that LLMs can "lose themselves" with too many layers, but no systematic characterization of failure modes is provided.
- Reporting refusal rates alongside harmfulness scores would give a more complete picture of the attack's practical risk profile.
- Ethical/dual-use discussion could be expanded with a responsible disclosure note.

---

## Removed Points
*These points were flagged for removal but are preserved here for context.*

- **"Prompt template not shown in main text"** — The paper says *"We provide a universal implementation of DeepInception with the following prompt template"* (line 93–95). The template was likely in an image or appendix stripped during extraction. Parser issue; removed.
- **"AutoInception not described"** — AutoInception may be detailed in the stripped appendix. Removed per missing-appendix rule.
- **"Definition 3.1 is notation-heavy and adds little clarity"** — Subjective stylistic judgement, not a substantive weakness. Removed.
- **"The Milgram analogy is overused"** — Subjective opinion. Removed.
- **"Only 7B models used for open-source comparison"** — The paper also uses Llama-3 8B and 70B for Jailbench evaluation, partially addressing this point. Removed as inaccurate.
- **"Missing failure analysis"** — Nice-to-have, not a core weakness. Moved to Nice-to-Haves.
- **"Reproducibility concerns about hyperparameters"** — The paper states default sampling temperature and system prompt are used. Per instructions, trivial reproducibility nitpicks removed.
- **"Missing appendix content"** — All appendix-related absences are parser artifacts. Removed.

---

## Novel Insights
The most interesting observation emerging from this review is the conceptual tension between the paper's framing and its evidence: DeepInception is presented as a *mechanism discovery* (psychological self-losing), but the actual contribution is an *effective prompt engineering technique* whose success could equally be explained by simpler hypotheses (keyword obfuscation, increased prompt complexity overwhelming safety classifiers, or instruction-following priority). The paper does not need the mechanism narrative to be valuable — the continual jailbreak finding alone is a genuine contribution that stands independent of any psychological framing. This suggests that the safety community may benefit more from understanding *which prompt structures systematically bypass guardrails* than from retrofitting psychological theories to LLM behavior, which the current evidence does not support.

---

## Suggestions
1. **Reframe the contribution.** Replace "discover the mechanism" with "propose a method inspired by the Milgram experiment" throughout. The paper is strong enough on its empirical merits; it does not need an unsupported mechanism claim.
2. **Expand baselines.** Add at least 2–3 more baselines (e.g., DAN-style role-play, a recent black-box method like ArtPrompt or ReNeLLM, and for open-source models — GCG or AutoDAN).
3. **Validate the GPT-judge.** Report human agreement on a sample of 100–200 outputs, or report refusal rates alongside harmfulness scores.
4. **Add error bars.** Report variance across at least 3 runs for main results (Table 2, 4).
5. **Add a nesting control.** Compare DeepInception against a long, non-nested prompt of similar complexity to isolate whether nesting per se drives the effect.

---
