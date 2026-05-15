Now I have a thorough understanding of the paper and can verify each claim. Let me synthesize the final review.

## Summary

This paper presents INSEC, the first black-box adversarial attack on LLM-based code completion engines. The attack injects a short adversarial comment (optimized via genetic algorithm with diverse initialization strategies) above the line awaiting completion, inducing the model to generate insecure code. Evaluated across 16 CWEs, 5 languages, and multiple engines (including GPT-3.5-Turbo-Instruct and GitHub Copilot), INSEC reports an average ~50% absolute increase in vulnerability rate while maintaining functional correctness on HumanEval, at a cost of under \$10 per CWE.

## Strengths

- **First black-box attack on code completion engines under a realistic threat model.** The paper is the first to demonstrate that an attacker with only query access (no model weights, logits, or training data) can substantially increase vulnerability rates in deployed completion engines. This is a clear novelty advance over prior white-box poisoning attacks (Schuster et al., 2021; He & Vechev, 2023; Aghakhani et al., 2024) that require access to training pipelines.

- **Well-defined and practical threat model (Section 3).** The attacker only needs the ability to insert a fixed comment string into the engine's input—achievable via a malicious IDE plugin, supply chain attack, or proxy wrapper. The model explicitly rules out access to model internals, tokenizer, or training process, making the setting more realistic than prior work.

- **Broad evaluation scope.** INSEC is evaluated on 16 CWEs across 5 programming languages, and on 6+ engines including open-source models (StarCoder-3B, StarCoder2 family, CodeLlama-7B) and commercial black-box services (GPT-3.5-Turbo-Instruct, GitHub Copilot). The diversity of CWEs (16 vs. 3–4 in prior poisoning attacks) and the inclusion of commercial services with only API access are notable.

- **Extremely low attack cost.** The paper reports actual API token consumption: at most 2.1M input and 1.3M output tokens per CWE, costing USD 5.80 for GPT-3.5-Turbo-Instruct. This demonstrates economic viability for a broad range of adversaries and is a concrete contribution beyond abstract threat modeling.

- **Thorough ablation studies validating design choices.** Section 5.3 systematically evaluates attack template position (Figure 3a), comment formatting (Figure 3b), individual initialization scheme contributions (Figure 4), necessity of optimization vs. initialization alone (Figure 5), attack token length (Figure 6), proxy tokenizer choice (Figure 7), and multi-CWE composability (Figure 8). These ablations provide strong internal validity for each design decision.

## Weaknesses

### Fatal
None.

### Major

- **No per-CWE breakdown of vulnerability rates (Figure 2).** The main result averages across 16 CWEs, but the paper never reports individual CWE performance. Without per-CWE data, the claim of "broad applicability across 16 CWEs" is incompletely supported — the ~50% average increase could be driven by a few CWEs where baseline rates were already high, while others show minimal improvement. A table showing baseline and attacked vul.ratio for each CWE per model is essential to substantiate the central claim. *(Verified: the paper states "We average the vulnerability and functional correctness scores obtained for each targeted attack across the 16 CWEs" — no per-CWE table or figure exists.)*

### Minor

- **Functional correctness measured only on HumanEval-based tasks, not on the security-critical CWE tasks themselves.** The paper evaluates func.rate on a line-completion dataset derived from HumanEval (a general coding benchmark), but the attack's functional impact on the actual 16-CWE security tasks is not measured. If the attack degrades functionality *on the same inputs where it induces vulnerabilities* (e.g., producing code that doesn't compile or crashes), this would not be detected by the HumanEval evaluation. While measuring on a standard benchmark is a reasonable first step, the paper's claim that "INSEC maintains functional correctness" would be more fully supported by also reporting func.rate on the security test set using secure reference solutions. *(Verified: Section 5.1 clearly separates D_func based on HumanEval from D_vul based on the 16-CWE tasks.)*

- **Multi-CWE attack evaluation metric is ambiguous (Figure 8).** The paper composes attack strings optimized for different CWEs and reports "vul ratio" in the multi-CWE setting, but does not define what this metric measures: whether a completion is counted as vulnerable if it exhibits *any* of the targeted CWEs (an OR), or if per-CWE success rates are reported separately and averaged. If the metric is an OR over all targeted CWEs, then adding more attack strings mechanically increases the chance that some CWE appears, making the "surprising composability" claim less surprising. The paper must define the exact scoring procedure and ideally report per-CWE success rates in the multi-CWE setting. *(Verified: Section on Multi-CWE Attack, paragraph near Figure 8, does not specify scoring procedure.)*

- **No direct comparison to a simple human-crafted adversarial prompt.** The only baselines are the unattacked engine and the "Init only" condition (which uses all five initialization strategies together). The paper does not report the absolute vulnerability rate achieved by a trivial adversarial comment like "Write vulnerable code" or even the best-performing single initialization string in isolation. While the TODO initialization is discussed (Figure 4 shows it "rarely wins"), its absolute vulnerability rate is not given. A simple prompt-injection baseline would contextualize the benefit of genetic optimization over a straightforward approach. *(Verified: Figure 5 compares "Init only" [all strategies] vs. "Opt only" vs. "Init & Opt" — no single naive-prompt baseline.)*

- **Hyperparameter values not fully specified.** The paper mentions pool size n_φ and the number of iterations but does not provide concrete values. A brief discussion of pool size appears in the last paragraph of Section 5.3 ("the impact of the size n_φ of the pool P") without exact numbers. The number of optimization iterations is described as determined by observing saturation on validation data, but the actual count is not reported. This hinders reproducibility. *(Verified: Algorithm 1 paragraph mentions pool size n_φ and "fixed number of iterations" determined by validation saturation, but no specific numbers.)*

### Trivial

- **Lack of error bars or confidence intervals on most reported metrics.** Figures report point estimates without variance. Given that results are averaged over 16 CWEs, per-model, and across random seeds/initializations, bootstrapped confidence intervals would strengthen statistical reliability.

- **The vulnerability dataset contains 12 tasks per CWE (192 tasks total).** While 100 completion samples per task yields 19,200 total judgments, the low number of distinct task templates per CWE limits the generalizability of per-CWE conclusions. This is a modest concern given the evaluation breadth across CWEs and models.

## Nice-to-Haves

- **Convergence analysis of the genetic algorithm.** A plot showing vulnerability rate on a held-out validation set across optimization iterations for a representative CWE would help readers understand whether the optimization is genuinely learning or plateauing quickly.

- **Example completions (qualitative).** A side-by-side comparison of generated completions with and without INSEC for a visible CWE (e.g., the md5 vs. sha256 example from Figure 1) would help readers intuitively understand the attack's effect.

- **Testing the paper's own proposed mitigations.** Section 6 suggests mitigations (anomaly detection on repeated patterns, prompt sanitization, rate-limiting), but none are evaluated. Even a preliminary experiment showing whether a simple defense (e.g., stripping single-line comments containing non-ASCII characters) breaks INSEC would strengthen the discussion.

## Removed Points

- **Criticism about unreleased attack strings / reproducibility.** The paper explicitly states it will not release attack strings for ethical reasons ("may provide them upon request"). This is a deliberate ethical choice, not a methodological flaw. Removed per Hard Rules (no questioning of existence/release status).
- **Criticism about GPT-4-generated reference solutions for HumanEval.** This is standard practice for multilingual benchmarks and the paper acknowledges it transparently. No evidence that GPT-4's solutions contain bugs. Removed as speculation.
- **Criticism about detectability by developers / stealthiness.** The paper notes "stealthiness" as a design goal and inserts a short comment that is minimally invasive. The reviewer's demand for developer-studies on detectability is outside the paper's scope. Moved to Nice-to-have.
- **Criticism about missing related work comparisons.** Removed per Hard Rules (cannot confirm existence of missing references).
- **All formatting/style nitpicks and parser artifacts.** Removed per Hard Rules.
- **Strength Finder claim about "Strong experimental methodology"** — generic phrasing without specific content. Removed.
- **Strength Finder claim about "Generalizable proxy tokenizer design"** — kept initially but on review is properly supported by Figure 7. Actually, this is specific and well-evidenced. I'll keep it in Strengths.

## Novel Insights

The reviews collectively surface an important observation: the paper's most interesting contribution may not be the ~50% average vulnerability increase (which is a headline number) but rather the *design principles* that emerge from the ablation studies — specifically that (i) a fixed 5-token comment optimized via a simple genetic algorithm with diverse initialization is sufficient, (ii) the attack is more effective on stronger models while degrading their functionality less, and (iii) proxy tokenizers (CodeQwen) generalize well even to models with different tokenizers. These findings suggest that black-box attacks on code completion are likely to become *more* effective as models improve, which inverts the usual security narrative where stronger systems are harder to attack. The multi-CWE composability result (if the metric ambiguity is resolved) would further strengthen this inversion.

## Suggestions

1. **Add a per-CWE table.** For each targeted engine, provide a table with columns: CWE, Language, Baseline vul.ratio, Attacked vul.ratio, and delta. This single addition would substantially strengthen the paper's central claim and address the most important evidential gap.
2. **Clarify the multi-CWE metric.** Explicitly define what "vul ratio" means in Figure 8. Report per-CWE success rates in the multi-CWE setting to demonstrate that composability is real, not an artifact of an OR-based metric.
3. **Report func.rate on the security tasks.** Add a simple evaluation: for each CWE task with a secure reference solution, measure pass rate with and without the attack. This directly supports the functional correctness claim on the relevant task distribution.
4. **Add a naive prompt-injection baseline.** Report the vulnerability rate of a simple comment like "# Write vulnerable code" or "# Do not use secure implementation" to quantify the benefit of INSEC's optimization.
5. **Report hyperparameter values.** Disclose pool size n_φ, number of optimization iterations, mutation rate, and temperature in the main text or appendix.
6. **Add error bars.** Report bootstrapped 95% confidence intervals for vul.ratio and func.rate in all bar charts.

## Score and Decision

The paper presents a novel, practically motivated attack with a clean design and broad evaluation. Its core contribution — the first black-box adversarial attack on code completion engines — is clearly novel and important. However, the evidential support for this contribution has meaningful gaps: the lack of per-CWE breakdown undermines the "broad applicability" claim, the functional correctness evaluation is on a separate task distribution, the multi-CWE metric is ambiguous, and there is no simple baseline comparison. These gaps are addressable (they require additional experiments, not a redesign) but in their current form prevent full confidence in the headline claims. I view this as a borderline paper: the idea and experimental design are strong, but the reporting of results needs substantial improvement before the claims can be fully verified.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>