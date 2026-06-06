---

## Summary

"The Rogue Scalpel" investigates whether activation steering — a technique for interpretable LLM control — inadvertently compromises safety alignment. Using JailbreakBench (100 harmful prompts across 10 categories), the paper shows that (1) even random steering vectors raise harmful compliance from 0% to 2–27%; (2) SAE-derived benign features achieve 2–4% higher compliance than random noise under identical conditions; and (3) averaging just 20 single-prompt jailbreak vectors produces a "universal" attack that generalizes to unseen harmful queries, achieving up to 63% compliance with no model weights or harmful training data. A production case study via the Goodfire public API confirms practical exploitability.

---

## Strengths

- **Comprehensive multi-model and multi-scale demonstration.** Section 4.1 sweeps layers, scaling coefficients, and vector types across Llama-3, Qwen2.5, and Falcon-3, using 1,000 vectors per condition. Fig. 2 shows non-zero compliance rates across all configurations, establishing the vulnerability is systematic rather than anecdotal.
- **SAE features are at least as dangerous as random noise, with deceptively benign semantics.** Fig. 2c shows SAE features on Llama3.1-8B outperform random directions by 2–4% compliance under identical conditions. Fig. 4a shows that 668/1,000 SAE features jailbreak ≥5 prompts, and the most effective features correspond to concepts such as "brand identity" — indistinguishable from legitimate-use vectors. This is the paper's sharpest empirical insight.
- **Production case study provides concrete real-world grounding.** Section 4.3 demonstrates that steering a "brand identity" SAE feature through the Goodfire API (default hyperparameters, no special access) produces detailed harmful responses including "disclaimer-then-compliance" and "justification via fictional framing" — documenting exactly how an externally-accessible API can be weaponized.
- **Universal attack construction is low-effort and practically alarming.** Section 4.4 shows that averaging 20 randomly-selected single-prompt jailbreak vectors generalizes to all 99 remaining JailbreakBench prompts, achieving up to 63.4% compliance on Falcon3-7B and 50.4% on Llama3-70B with no model internals or harmful training data. The ~4× average improvement over random baseline is quantitatively striking.
- **Cross-category generalization heatmap (Fig. 4b) concretely demonstrates monitoring infeasibility.** The analysis shows that dangerous features are highly prompt-specific — cross-category conditional probabilities barely exceed per-category baseline rates — which means exhaustive pre-deployment auditing is practically infeasible.

---

## Weaknesses

### Fatal

None.

### Major

- **The conclusion's head-to-head SAE-vs.-random comparison conflates results from different model configurations.** Section 5 states "SAE-based steering proves even more dangerous, achieving 11% harmful compliance on Llama3.1-8B" and implicitly contrasts it with "10% harmful compliance rate from random steering in Qwen2.5-7B." These figures come from different models tested at different layers (2/3 depth for SAE, 1/3 depth for random). The paper's own comparable condition (Fig. 2c, same model and layer) shows the SAE advantage is 2–4 percentage points — real but modest. Presenting an 11% vs. 10% cross-model gap as directional evidence for SAE superiority in the conclusion is misleading. The conclusion should faithfully report the within-condition finding.

### Minor

- **The "zero-shot" characterization of the universal attack slightly overstates its ease.** Section 4.4 explicitly states the construction requires "typically only 100–500 random trials" of querying the model to find 20 compliant vectors. This is a black-box query-based selection process, not zero-shot in the standard sense (which implies no task-specific examples or optimization). The intended meaning — that no model weights, gradients, or harmful labeled data are needed — is a legitimate and important practical distinction, but "zero-shot" is an imprecise label that could mislead readers about the attack's query budget. The paper should describe it as a "low-overhead black-box attack" to be precise.
- **The Qwen2.5-32B anomaly is noted but unexplained.** Fig. 6 shows that the universal attack (Average of 20 Unsafe Directions) for Qwen2.5-32B achieves ~9% compliance, identical to Random Direction and lower than Individual Unsafe Direction (~16%). The paper only notes "reduction in performance observed for Qwen2.5-32B" in the caption. Whether this is attributable to stronger alignment, high-dimensional activation spaces diluting the averaged vector, or something else would materially inform the paper's claim about universal attack generality.
- **LLM judge validity at low compliance rates.** The paper evaluates ~300,000 responses using Qwen3-8B as judge, with compliance rates often 2–20%. False-positive rates of even 1–2% could substantially affect conclusions in the lowest-compliance categories. The paper states Appendix B contains calibration against human annotations and explicitly rules that incoherent outputs are SAFE — these are the right steps, and this is partially addressed — but the calibration results are not presented in the main body where readers need them to trust the main figures. A brief summary (e.g., precision/recall vs. human labels) in the main text would strengthen the paper.

### Trivial

- **Non-monotonicity finding deserves a more precise characterization.** The paper notes that "excessive coefficients degrade output coherence" and that incoherent outputs are classified SAFE, but does not explicitly characterize the range of *c* values where both coherent generation and safety bypass co-occur. This would more precisely define the practical attack surface.

---

## Nice-to-Haves

- **Comparison to text-only jailbreak baselines (PAIR, GCG, Tree-of-Attacks) on the same models.** Without knowing what compliance rates standard prompt-level attacks achieve on these configurations, it is hard to assess how much marginal attack capability activation steering access confers. Even a single reference row in Fig. 3 or Fig. 6 would provide crucial context for the paper's security-relevance argument.
- **Analysis of whether existing output monitoring would catch steering-induced compliance.** If standard production safety layers (perplexity filters, refusal-direction probes, output classifiers) successfully block the harmful outputs even when the model produces them, the practical threat is lower than implied. A short analysis of this would strengthen the threat model.
- **Within-category feature comparison.** The paper could strengthen the "false sense of security" argument by showing that the most effective jailbreaking SAE features receive higher "benignity" ratings from reviewers than ineffective features — making the undetectability claim concrete rather than illustrative.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"0% baseline compliance is unexplained and implausible"** (Harsh Critic): The paper states (Sec. 3.4) that Llama-3, Qwen2.5, and Falcon-3 all achieve 0% compliance on JailbreakBench without steering. The harsh critic called this "strikingly clean." However, these are state-of-the-art instruction-tuned models evaluated on JailbreakBench prompts (which, while adversarial by design, are used as a controlled benchmark). 0% baseline is consistent with the literature on these well-aligned models and is not implausible. The critic's concern that "system-prompt configuration" is not disclosed is a reproducibility nitpick; the paper provides a reproducibility statement with model versions, seeds, and decoding strategy. REMOVED: contradicts the Hard Rule on reproducibility nitpicks and is a speculative concern.

- **"Framing that activation steering is often presented as safer than fine-tuning is inaccurate"** (Harsh Critic — Introduction): The paper says it is "often framed as a precise, interpretable, and potentially safer alternative to fine-tuning." This is a reasonable characterization of how the technique has been marketed (e.g., by the Goodfire API and numerous SAE papers). The critic disputes "safer" but this is a minor framing disagreement. REMOVED: minor stylistic dispute not supported by a specific paper claim that is verifiably wrong.

- **"Cross-category heatmap should be presented more evenhandedly"** (Harsh Critic — Section 4.2): The critic says the data also implies "no single SAE feature poses a systemic universal threat." The paper is transparent about poor generalization (Fig. 4b, Section 4.2) — this is one of the paper's stated findings. The one-sided presentation is by editorial choice about emphasis, not misrepresentation. REMOVED: scope creep on the paper's framing choices.

- **"Token-limited steering (generation tokens only) should be tested"** (Harsh Critic): This would be an interesting extension but is outside the paper's scope; the paper explicitly cites Durmus et al. (2024) for the both-prompt-and-generation design and is internally consistent. REMOVED: nice-to-have experiment that does not undermine the core contribution.

---

## Novel Insights

The paper's most genuinely novel observation is the *population-level* finding in Fig. 4a: a majority (668 of 1,000) of all SAE features — not just a few adversarially-selected outliers — can jailbreak multiple prompts, despite those features representing semantically benign concepts. Coupled with the cross-category heatmap showing poor generalization, this creates a logically tight argument: safety auditors cannot enumerate dangerous features *before* deployment (too many), cannot screen them by semantics (they look benign), and cannot rely on one dangerous feature also breaking other prompts (low cross-generalization). This trilemma is a concrete, well-supported framing of why interpretability-based safety screening is harder than it appears — which is the paper's core claim and goes meaningfully beyond prior work on adversarial steering vectors.

---

## Suggestions

1. **Fix the conclusion's comparison:** Replace "SAE-based steering proves even more dangerous, achieving 11% harmful compliance on Llama3.1-8B" with a direct citation of the within-condition finding from Fig. 2c ("2–4% higher compliance than random under identical conditions"), and note that cross-model differences in Fig. 3 reflect different configurations rather than a controlled head-to-head.
2. **Rename "zero-shot attack" to "low-overhead black-box attack":** Clarify that the method requires ~100–500 model queries to select 20 compliant vectors, but emphasizes that no model internals, gradients, or harmful labeled data are needed.
3. **Add brief judge calibration summary to main text:** State the precision and recall of Qwen3-8B vs. human annotations (presumably in Appendix B) in one or two sentences within Section 3.4 so readers can assess the reliability of compliance rates in the main figures.
4. **Analyze the Qwen2.5-32B anomaly:** Devote 1–2 sentences in Section 4.4 or a brief appendix to hypothesize why the universal vector fails to outperform random for this model (e.g., larger embedding dimensionality diluting the averaged vector, stronger alignment, or insufficient sample of 20 vectors in 32B activation space).
5. **Add a single row of text-only jailbreak baseline results** (e.g., PAIR) in Fig. 3 or the text for context on how much marginal attack capability steering access provides.

---

## Score and Decision

**Originality:** The core contribution — systematically measuring the *inadvertent* safety failure from *benign* activation steering across diverse models — fills a clear gap relative to prior work on explicitly adversarial steering. The universal attack construction is clever and novel. Score: 4/5.

**Importance:** Activation steering is an increasingly deployed paradigm (production APIs exist), and demonstrating systematic alignment failure is directly safety-relevant. Score: 5/5.

**Claims well-supported:** The main quantitative claims (random steering lifts compliance, SAE ≈ random under identical conditions, universal attack achieves 4× improvement) are backed by large-scale experiments with adequate controls. The conclusion slightly overclaims on the SAE-vs.-random comparison. Score: 3/5.

**Soundness of experiments:** Multi-model, multi-scale sweep, 1,000 vectors per condition, LLM judge validated against human annotations, greedy decoding with fixed seeds. The methodological choices are defensible and well-cited. Missing text-only baselines is a gap. Score: 3/5.

**Clarity:** Writing is clear and the experimental structure is well-organized. The conclusion's cross-model comparison is a genuine clarity failure. Score: 4/5.

**Value to community:** Directly actionable for safety practitioners using SAE-based steering APIs. The production case study is particularly valuable. Score: 4/5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>5</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>