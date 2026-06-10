## Summary

This paper introduces ∀uto∃∨∧L, a benchmark that evaluates LLMs on "truth maintenance" through a round-trip informalization (FS→NL) / autoformalization (NL→FS) pipeline using context-free grammar (CFG) generation and formal verifiers (Z3, Prover9) to check semantic equivalence. The core innovation is that by checking whether φ₀ ≡ φ₁ after the (𝒜∘𝒯) cycle, the framework avoids human annotation while producing fresh randomized data. The paper evaluates 17 LLMs plus o1, reports correlations (ρ ≥ 0.7) with five existing FS benchmarks, and derives a probabilistic bound on false positives.

---

## Strengths

1. **CFG-based dynamic generation with formal verification is a genuine methodological contribution.** The paper is correct that most prior benchmarks (HumanEval, FOLIO, StructuredRegex, MALLS) rely on hand-written test cases, crowdsourcing, or LLM-generated data requiring manual validation. Using CFGs to generate arbitrarily many ground-truth FS expressions and formal theorem provers to check equivalence after the round-trip pipeline is a clean way to avoid human annotation (Sec. 3, lines 62–85). The ability to generate data on-the-fly also directly mitigates the benchmark contamination problem (Sec. 1, line 10) that plagues static datasets.

2. **The LLM-as-verifier negative result is a useful empirical finding.** The paper tests whether LLMs can judge φ₀ ≡ φ₁ themselves (Sec. A4, Fig. 5) and shows that even with Chain-of-Thought, F₁ scores collapse beyond low descriptional complexity. This supports the paper's design choice to use external theorem provers rather than "LLM-as-a-judge" — a clean, falsifiable finding.

3. **Broad model evaluation across 17 LLMs plus o1.** The paper evaluates a diverse set of models (closed- and open-source, varying sizes) and includes a separate study of o1. While the o1 evaluation is limited in size, the main evaluation provides a solid empirical foundation (Sec. 5).

4. **Predictive power against external benchmarks goes beyond internal consistency.** The paper defines a formal Predictive Power metric (Def. 5.1) and reports 𝒫 > 0.5 against FOLIO, HumanEval, LogiEval, and BBH (Fig. 4). Most new benchmarks only claim internal validity; this external anchoring, though imperfect (see Weaknesses), is stronger than what many benchmark papers provide on release.

---

## Weaknesses

### Fatal

None. The core contribution — a CFG-based, verifier-checked round-trip evaluation pipeline — is sound in design and the paper provides genuine evidence that it correlates with other benchmarks. No single issue invalidates the central claims.

### Major

1. **The "most comparable dataset" selection for correlation analysis is underspecified, creating researcher degrees of freedom.** The paper says it uses "the most comparable ∀uto∃∨∧L dataset" for each benchmark comparison (Sec. 5, line 113) but never defines what "most comparable" means or whether this selection was made post-hoc. Without a pre-registered mapping, it is impossible to rule out selection bias: a reader cannot tell whether alternative dataset choices would weaken or strengthen the reported correlations. This directly affects the credibility of the paper's headline claim (ρ ≥ 0.7) that performance on AutoEvalL is "highly indicative" of other benchmarks. *(Anchored at line 113: "using the most comparable ∀uto∃∨∧L dataset.")*

2. **The correlation evidence does not control for general model quality as a confound.** With 17 models across different families and sizes, any benchmark that roughly sorts models by overall capability will correlate with any other such benchmark. The paper performs no controls for model size, family, training data scale, or a trivial baseline predictor (e.g., parameter count). A Spearman ρ ≥ 0.7 could simply reflect that "better models are better at everything" rather than truth maintenance specifically being the predictive factor. The paper frames this as evidence for D3 (predictive power), but without controlling for confounders, the direction of explanation is unclear. *(Anchored at Sec. 5, lines 111–115, and Fig. 3.)*

3. **Section 4 provides essentially no description of the actual datasets — a critical omission for a benchmark paper.** Section 4 (lines 99–103) is one paragraph stating the framework is open-source. Fig. 2 shows CFGs pictorially but the text never describes what the five datasets are, what formal languages they cover (beyond the general categories of propositional logic, FOL, regex), how difficulty is calibrated, what "out-of-distribution" means concretely, or how the CFGs are designed to test specific capabilities. For a paper whose primary contribution is a benchmark, the reader cannot evaluate dataset quality, diversity, or suitability without the appendix (which is stripped by the parser, but the main text should stand alone on this). *(Anchored at Sec. 4, lines 99–103: "We now describe the datasets…" — followed by no substantive description.)*

### Minor

1. **The false positive bound assumes independence among three error events without justification.** The derivation (lines 135–142) expresses the false positive probability as (1−p_𝒯)(1−p_𝒜)p_H and for n iterations as (1−p_𝒯)ⁿ(1−p_𝒜)ⁿp_Hⁿ. This product form assumes that informalization errors, autoformalization errors, and "hallucinating in the right way" are independent events. In practice, if an LLM misinterprets the formal syntax during informalization, the resulting NL is systematically distorted in ways that directly affect autoformalization likelihood — the events are almost certainly dependent. Additionally, p_H ("probability of hallucinating φ₁ ≡ φ₀ given ψ₀ is wrong") cannot be estimated or bounded without ground-truth NL annotations, which the whole framework is designed to avoid. The bound provides mathematical veneer but is not operationalizable. *(Anchored at lines 137–142.)*

2. **"Soundness" claims are overstated for the first-order logic case.** The paper repeatedly frames soundness as a core advantage (lines 85, 164: "∀uto∃∨∧L uses theorem provers to check equivalence and thus is sound in its accuracy evaluation"). First-order logic equivalence is undecidable. The paper acknowledges this in Limitations (line 179) and notes that 0.66% of results timed out, but a verifier with a bounded timeout is not a sound decision procedure — it can return false negatives (equivalent formulas that time out before being proved equivalent). The main text's framing of "soundness" without consistently qualifying the FOL case is misleading. *(Anchored at lines 85, 164, contrasted with line 179.)*

3. **Selective visualization without full tabular results in the main text.** The paper says "For clarity, we plot select models, grey out the data from the others, and refer the reader to App. N for a comprehensive overview" (line 109). For a paper making predictive power claims, greying out data in the main text — even with an appendix reference — weakens reader trust. The full ranking and scores for all 17 models should appear in a table in the main body. *(Anchored at line 109.)*

4. **The paper does not characterize what kinds of logical transformations the benchmark actually tests.** The running example (p₁∧p₂∧p₁ → NL → p₁∧p₂) hinges on commutativity and idempotence. The paper does not analyze whether the generated datasets stress logical inference, associativity, quantifier handling, or syntactic compliance — and in what proportions. Without this characterization, the reader cannot assess whether the benchmark is measuring a narrow or broad notion of "truth maintenance." *(Anchored at lines 83, 95.)*

### Trivial

1. **Notational inconsistency for informalization.** The paper uses at least three symbols for informalization interchangeably: 𝒯 (Def. 2.2, line 41), ℤ (line 47: "ψᵢ = ℤ(φᵢ)"), and script-Z (line 137: "𝒵ₗ(φ₀)"). In a paper that formally defines terms and uses them in equations, this inconsistency harms readability. *(Anchored at lines 41, 47, 137.)*

2. **The o1 evaluation is presented as supporting a strong claim ("even SOTA LRMs cannot maintain truth effectively") but uses only 200 samples with 5 points per category and 3 runs.** The paper acknowledges the cost constraint but does not report confidence intervals. The claim is likely true in spirit but the evidence is too thin to carry the weight placed on it. *(Anchored at lines 148–151.)*

---

## Nice-to-Haves

- **Disentangle the components.** Running the pipeline with a known-good autoformalizer (or informalizer) as a baseline would help establish whether the benchmark primarily measures informalization difficulty, autoformalization difficulty, or a genuinely new property of their composition.
- **Compare against simpler predictors.** The predictive power claim would be strengthened by comparison with trivial baselines (model parameter count, training compute, or MMLU score) to show that AutoEvalL captures something specific beyond general capability.
- **An approximate/relaxed version of truth maintenance** (e.g., checking logical implication rather than full equivalence) could be more practical for some applications.

---

## Removed Points

These points were flagged by the input reviewers but are removed per the filtering rules:

- **"BLEU criticism is a straw man"** (Harsh Critic): The paper's BLEU example illustrates that NL-based metrics cannot detect semantic negation. While BLEU is indeed not designed for this, the paper uses the example as a contrast to motivate formal verification. This is a valid contrast, not a straw-man argument. **Removed** — not a genuine weakness of the paper.

- **"Section definitions are circular"** (Harsh Critic): The critic notes that Def. 2.1 uses 𝒜⁻¹ before Def. 2.2 defines it. The paper explicitly acknowledges these are duals. This is a deliberate design, not an error. **Removed** as not a substantive weakness.

- **"Hand-annotation is not necessarily a weakness"** (Harsh Critic, on related work): This is subjective opinion about how the paper positions itself relative to prior work, not a flaw in the paper itself. **Removed.**

- **"Prompts are not in the main text"** (Harsh Critic): The paper states prompts are in the appendix. The parser strips appendix content. By the hard rule, criticisms about missing appendix content are removed. **Removed.**

- **Strengths dropped from Strength Finder:** Several claimed strengths were generic ("addresses important problem," "comprehensive evaluation") and removed. The strengths included above are the specific, evidenced ones.

---

## Novel Insights

The most interesting observation across the reviews is one the paper itself makes but does not fully develop: that on syntactic compliance for regexes, GPT-4o performs worse than much smaller models (Phi, Llama-3) because it "tends to expand the Kleene Star recursively, leading to invalid regexes" (Sec. A2). This is a specific, falsifiable failure mode that future work could exploit. It suggests that larger models are not uniformly better at formal syntax tasks and that certain training dynamics may actively harm performance on bounded-formal-language generation. The negative result on LLMs-as-verifiers (Section A4, Fig. 5) is also sharper than most existing work on this topic.

Beyond these, the reviews surface no genuinely novel insight that goes beyond what the paper itself contributes.

---

## Suggestions

1. **Define and pre-register the "most comparable" dataset mapping** to eliminate researcher degrees of freedom in the correlation analysis.
2. **Add a table in the main text** with full rankings, scores, and standard deviations for all 17 models across all datasets, rather than greying out data.
3. **Run a simple confounder control** — e.g., partial Spearman correlation controlling for model parameter count — to establish that AutoEvalL captures something beyond general capability.
4. **Qualify "soundness" throughout** to explicitly note that it applies to decidable fragments (propositional logic, regex) and is approximate for FOL due to undecidability.
5. **Describe the five datasets in more detail in the main text** — how many expressions, what CFGs generate them, what difficulty levels, what formal properties they test.

---

## Score and Decision

The paper has a genuinely novel core idea and provides evidence that the benchmark correlates with existing evaluations. The weaknesses are real but not fatal: they concern overclaims, underspecification, and missing confounder controls — problems that can be addressed. At a top venue, the paper in its current form would need to address the major weaknesses (especially the underspecified dataset mapping and the confounder issue) to fully support its headline claims. However, the core contribution is solid enough that a revision could meet the bar.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>