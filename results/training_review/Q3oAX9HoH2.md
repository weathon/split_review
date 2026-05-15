Here is my consolidated final review.

---

## Summary

This paper proposes DeepInception, a training-free black-box jailbreak method that exploits LLMs' personification ability by constructing nested fictional scenes (inspired by the Milgram experiment on authority obedience). The method wraps harmful requests inside multi-layer imaginative scenarios to "hypnotize" the model into a relaxed state where safety guardrails are bypassed. Experiments across Llama-2/3, GPT-3.5/4/4o, and other models show competitive harmfulness rates, and the paper additionally documents a "continuous jailbreak" phenomenon where, after the initial attack, subsequent direct requests also yield harmful content.

## Strengths

- **Novel psychological grounding for the attack design.** The connection to the Milgram experiment's authority-obedience dynamics (Section 3.1) provides a conceptually fresh lens for understanding why nested, indirect instructions might bypass safety alignment. This goes beyond the usual adversarial-prompt engineering framing and directly motivates the nested-scene architecture.

- **Systematic ablation isolating the contribution of each component.** The study decomposes DeepInception into Scene (S), Layers (L), and their combinations (Figure 6: None → S → L → SL → Full), showing that the fully nested configuration (Full) substantially outperforms the single-layer scene-only (S) or layer-only (L) variants. Figure 8 then ablates number of characters, number of layers, and scene types. These ablations provide actionable engineering insights and empirically demonstrate that *both* scene and multiple layers are needed for best performance.

- **Demonstration of "continual" jailbreak across models.** The paper introduces and evaluates a novel setting: after a successful DeepInception attack, subsequent *direct* harmful requests (no nesting) continue to produce high harmfulness rates (Table 5). This goes beyond single-shot jailbreaking and points to a persistent vulnerability state worth further investigation.

- **Lightweight, training-free, black-box applicability.** DeepInception requires no gradient access, no white-box model information, and no computational optimization — it is a single prompt template — yet achieves competitive or leading harmfulness rates against methods like PAIR and PAP that require multiple query iterations or auxiliary models.

- **Broad model coverage.** Evaluation spans six LLMs (Llama-2/3, Falcon, Vicuna, GPT-3.5/4/4o) with both open-source and closed-source families, and preliminary exploration of GPT-4o multimodal and OpenAI o1.

## Weaknesses

### Fatal

None.

### Major

- **The "continuous jailbreak" claim lacks comparative baselines to establish uniqueness.** The paper shows that DeepInception achieves higher harmfulness on subsequent direct requests (Tables 5, 6). However, there is no comparison showing that *other* jailbreak methods (e.g., PAIR, CipherChat, PAP) do *not* also exhibit a similar "continually inducing" effect. Without this comparison, the paper cannot support the implication (Remark 3.3) that this is a special property of DeepInception's "hypnotized state" rather than a general consequence of any successful jailbreak — the model may simply be more compliant after any successful override. This is the most significant evidential gap.

- **Generalization to multimodal and o1 models is asserted but not systematically evaluated.** Sections 4.5 and 4.6 present only qualitative case studies for GPT-4o (2 examples) and OpenAI o1 (1 example). The paper explicitly acknowledges for o1 that "Due to the limited frequency of testing and the strict usage control, we cannot perform large-scale experiments on it" (line 176). Yet the abstract and conclusion make broad claims about effectiveness on these settings. The disconnect between the caveat and the generalization claim weakens confidence in the scope of the contribution.

### Minor

- **The theoretical framework (Section 3.2) is descriptive rather than predictive.** Definition 3.1 and Remarks 3.2–3.3 decompose jailbreak probabilities via the chain rule — a mathematically valid but trivial observation that holds for *any* prompt structure. The framework does not derive a testable, falsifiable hypothesis that distinguishes DeepInception from other strategies, nor does it explain *why* nested scenes specifically work beyond intuitive appeal to the Milgram analogy. The paper's contribution is primarily empirical, and over-selling the theory distracts from the genuine experimental findings.

- **Numerical results are described qualitatively in the text.** The paper uses phrases like "competitive harmfulness rates" and "the highest harmfulness" (Section 4.2) without reporting specific numbers in the running text. While the tables in the original PDF contain the data, the reliance on qualitative descriptors makes the main claims harder to assess at a glance. Adding per-method harmfulness percentages and standard deviations into the text would strengthen presentation.

- **The PPL analysis (Figure 7) does not uniquely validate the "inception" mechanism.** Showing that DeepInception yields lower perplexity on harmful outputs is expected — the model is more confident when the context already contains hypnotizing/harmful content. This is consistent with several possible explanations and does not specifically validate the claimed "self-losing under authority" mechanism over simpler accounts (e.g., context priming).

### Trivial

- The phrase "we instantiating the inception mechanism" (line 34, contribution list) contains a grammatical issue.
- Figure 9 and 10 captions say "DeepInceiton" (missing 'p').

## Nice-to-Haves

- For the continuous jailbreak setting, applying the same protocol after successful jailbreaks by PAIR, CipherChat, or a simple role-play prompt would clarify whether the effect is specific to DeepInception.
- Reporting GPT-Judge agreement rates with human annotators on a random subset would strengthen the harmfulness metric's credibility.
- A few failure case analyses (where DeepInception *fails* to jailbreak) would help identify boundary conditions.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"No comparison to a non-nested role-play baseline" (Harsh Critic, Point 1).** This is factually incorrect. The paper's ablation study (Figure 6) directly compares Scene-only (S) — which is a single-layer role-play without nesting — against the fully nested DeepInception (Full), and shows that the nested version substantially outperforms it. The paper also compares L (layers-only), SL (scene+layers), and None. The claim that "the ablation studies... do not test whether the nested structure adds any benefit over a standard role-play without nesting" misreads the paper: the S condition *is* that baseline. This criticism is removed.

2. **"Vacuous theoretical framework" framed as a fatal flaw.** The formalization is indeed basic (chain rule decomposition), but this is standard for descriptive frameworks in empirical papers. The paper's contribution does not hinge on mathematical novelty — the contribution is the nested-scene attack design and its empirical evaluation. Representing this as a "critical weakness" overstates its impact. Kept as a **minor** weakness above but not at the severity level originally claimed.

3. **"Incomplete and vague reporting of results" (Harsh Critic, Point 4) regarding missing numbers.** The tables exist in the original PDF (the text extraction from the parser does not render images). The paper does reference specific tables (2, 3, 4, 5, 6) with numerical results. The qualitative language complaint ("competitive", "leading") is partly legit but common for papers where tables carry the numbers. Downgraded to a minor weakness above.

4. **Strength Finder's claim about "theoretical formalization" as a core strength.** The formalization is not a genuine strength — it is not novel or predictive. This strength claim is overly generous and conflicts with the verified weakness that the theory is descriptive. Dropped from Strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an angle or connection that the paper itself had not already articulated.

## Suggestions

1. **Add a continuous jailbreak baseline comparison.** Re-run the "continual" setting (direct follow-up requests) for PAIR, CipherChat, and a simple role-play prompt. This is the single experiment that would most strengthen the paper — either establishing the "Continually Inducing" effect as a unique property of DeepInception, or tempering the claim.

2. **Add explicit numerical summaries in the text.** Report key harmfulness percentages (e.g., "DeepInception achieves 41.0% on GPT-4 vs. 2.4% for PAIR and 1.2% for PAP") directly in Section 4.2 so the reader does not need to cross-reference tables.

3. **Retract or rigorously qualify the multimodal/o1 generalization claims.** Either add systematic experiments (even on a smaller sampled set) or explicitly state in the abstract and conclusion that the multimodal/o1 results are preliminary case studies.

4. **Tone down the theoretical framing.** Replace Remarks 3.2–3.3 with a simple intuitive description of why nested conditioning can increase harmful output probability, and reserve the mathematical notation for the experimental section where it serves as notation.

## Score and Decision

This paper introduces a practically interesting jailbreak method with a well-motivated design, thorough ablations, and a novel continuous-jailbreak finding that opens a worthwhile research direction. The main weaknesses are (a) the lack of comparative baselines for the continuous jailbreak claim, which weakens the inference of a unique "hypnotized state" mechanism, and (b) overstated generalization to multimodal/o1 models. These are addressable with additional experiments but detract from the paper's completeness in its current form. The paper's core empirical contribution — a lightweight, effective nested-scene jailbreak validated across multiple models — is solid and reproducible.

Given that the most severe criticism raised (missing role-play baseline) is factually incorrect, and the remaining weaknesses are moderate and addressable, the paper merits acceptance at a strong venue with the expectation that the authors address the gap in the continuous jailbreak comparison.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>