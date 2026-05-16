Now I have all the information needed. Let me synthesize the final authoritative review.

---

## Summary

This paper presents INSEC, the first black-box adversarial attack on LLM-based code completion engines. INSEC works by inserting a short, pre-optimized adversarial comment into the completion prefix, inducing the model to generate insecure code while preserving functional correctness. The attack string is optimized via a genetic algorithm with diverse initialization strategies, requiring only black-box query access. The evaluation spans open-source models (StarCoder, CodeLlama) and commercial services (OpenAI API, GitHub Copilot) across 16 CWEs and 5 programming languages, reporting an ~50% absolute increase in vulnerability rate with limited functional correctness degradation.

## Strengths

1. **First black-box adversarial attack on LLM-based code completion that works on commercial services.** Prior attacks (Schuster et al., 2021; He & Vechev, 2023; Aghakhani et al., 2024; Yan et al., 2024) required white-box access to model weights or training data. INSEC requires only query access, no parameters, logits, or tokenizer (Section 3), and is demonstrated on GPT-3.5-Turbo-Instruct via the OpenAI API. This is a genuine step forward in threat modeling.

2. **Large empirical gains in vulnerability rate across diverse models and languages.** Figure 2 reports consistent absolute increases in insecure code generation ratio (up to ~60%, averaged ~50%) across all tested engines, while functional correctness drops at most 22% relative. The evaluation covers 16 CWEs and 5 programming languages (Section 5.1) using CodeQL-based vulnerability judgments — far broader than the 3–4 vulnerability types in prior poisoning attacks.

3. **Extremely low attack development cost.** Section 5.2 documents that optimizing one attack string for GPT-3.5-Turbo-Instruct consumes 2.1M input tokens and 1.3M output tokens, costing only USD 5.80 per CWE. Combined with the fixed-string deployment (no per-query overhead), this makes the threat realistic for wide-scale attacks.

4. **Multi-CWE composability demonstrated.** Figure 8 shows that combining individually optimized attack strings for up to 16 CWEs simultaneously still nearly doubles the vulnerability rate relative to unattacked baselines, even though INSEC was designed for single-CWE targeted attacks. This surprising result strengthens the paper's claim of high severity.

5. **Comprehensive ablations validate design choices.** Section 5.3 systematically tests insertion position (Figure 3a), comment formatting (Figure 3b), the contribution of each initialization scheme (Figure 4), necessity of optimization vs. initialization alone (Figure 5), token length sensitivity (Figure 6), and proxy tokenizer choice (Figure 7). These ablations demonstrate that the method is well-engineered, not a lucky accident.

## Weaknesses

### Fatal
None.

### Major

1. **Small per-CWE vulnerability test set with no per-CWE breakdown or uncertainty quantification.** Section 5.1 states the vulnerability dataset contains **12 tasks per CWE** (192 total). The main results (Figure 2) report only averages across all 16 CWEs, with no per-CWE results, no confidence intervals, and no variance measures. With 12 tasks per CWE, a single task flipping from secure to vulnerable changes the vul ratio by ~8.3%. The paper's central claim of a "~50% absolute increase" cannot be assessed for uniformity — is this effect consistent across CWEs or driven by a few easy cases? The paper does not report whether the attack targets different CWEs than those where baselines are already high. This is the single largest evidential gap: the conclusion may be correct, but the evidence is insufficiently granular to support the claimed generality. *Remedy: report per-CWE vul ratios (table or box plot) and provide bootstrapped confidence intervals on the aggregate estimates.*

2. **Functional correctness evaluation for non-Python languages uses unverified GPT-4-generated reference solutions.** Section 5.1 states: "As the canonical solutions in HumanEval are only in Python, for other languages we use GPT-4 to generate reference solutions that pass the provided unit tests." The paper reports no manual verification of these solutions, no count of how many tasks were adjusted or discarded, and no discussion of how reference quality varies by language. If GPT-4's reference solutions are non-idiomatic or incorrect for languages where GPT-4 is weaker (e.g., Ruby, Julia), the pass@k metric could be systematically mismeasured — particularly under attack, where the adversarial comment might interact differently with a suboptimal reference. *Remedy: sample and manually verify 30–50 reference solutions per language, report accuracy, and re-evaluate func rate on a verified subset if needed.*

### Minor

1. **Missing optimization hyperparameters hinder reproducibility.** Several key parameters are not reported: (i) the number of optimization iterations (the paper states it is "determined on validation datasets, observing when the optimization process saturates" without stating the actual number used per model/CWE); (ii) the pool/population size $n_\varphi$ is introduced but its value is never given; (iii) the number of candidate generations and the compute budget for open-source models (which, while free to run, matters for assessing whether the attack can be mounted against weaker models within a realistic budget). These omissions prevent full reproduction and assessment of attack cost.

2. **Copilot evaluation claimed but results absent from main figures.** The abstract states INSEC was evaluated on "GitHub Copilot," and Section 5.1 mentions "Copilot is an interactive plug-in and we develop an API to enable its evaluation." However, Figure 2 (main results) shows results for StarCoder-3B, StarCoder2 family, CodeLlama-7B, and GPT-3.5-Turbo-Instruct — Copilot is not included. The paper should either present Copilot results or explicitly state why they are omitted (e.g., ethical restrictions on running attacks against a live commercial service, or technical limitations). As written, the abstract overclaims.

3. **Comparing functional correctness preservation across models is confounded by per-model attack strings.** Section 5.2 notes that "better completion engines retain more functional correctness under the attack" and interprets this as a concerning trend about stronger models being more vulnerable. However, each model received a different optimized attack string. The attack string for GPT-3.5 may be shorter or less disruptive than for StarCoder2-3B. The paper does not compare whether attack strings differ systematically in length or content across models. The trend may reflect differences in the optimized strings rather than inherent model properties.

4. **Proposed mitigations are unevaluated.** Section 6 suggests alerting on repeated substrings, prompt sanitization, and interrupting repeated querying. None of these are tested against INSEC, even in a preliminary experiment. Since the paper advocates for mitigations, even a simple test (e.g., whether a substring-frequency filter catches the attack strings) would strengthen the discussion. As presented, the mitigations are conjectural.

5. **Vulnerability dataset construction is underspecified.** Section 5.1 states that 12 completion tasks per CWE were compiled but does not describe how they were constructed (manually written? automatically generated?), their length/complexity, or what criteria ensured they are representative of real coding scenarios. Without this context, readers cannot assess task difficulty or potential bias.

### Trivial
None that survive parser-aware filtering.

## Nice-to-Haves

- A brief discussion of the detection risk for the malicious IDE plug-in deployment scenario (e.g., whether the fixed adversarial comment could be detected by manual inspection or IDE auditing over time).
- A more explicit differentiation between INSEC and ordinary jailbreak attacks on LLMs (Zou et al., 2023). The paper touches on this in related work (Section 7) but could sharpen the distinction: jailbreaks often aim to bypass refusal for harmful content, while INSEC targets *functionally correct but insecure* code generation without refusal being the obstacle.
- Statistical significance testing for the main vul ratio differences between attacked and unattacked conditions.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"High base vulnerability rates (~40%) weaken attribution"** — This is not a genuine weakness. Figure 2 transparently shows both attacked and unattacked rates. The paper claims an *absolute increase* of ~50%, not that the increase comes exclusively from previously-safe tasks. The paper does not hide baseline rates. The valid sub-concern (per-CWE breakdown) is already addressed under Major weakness #1.
- **"The threat model justification is sketchy; no discussion of detection risk"** — The paper cites two references (Pol 2024; Toulas 2024) for malicious plug-ins amassing millions of downloads. This is appropriate for a security paper establishing plausibility. Detection risk of the deployment scenario is a reasonable discussion point but not a weakness of the attack itself. Moved to Nice-to-Haves.
- **"Figure 6 drop at 80 tokens may not be significant without error bars"** — Partially valid but too granular for a weakness tier; the paper reports the observation descriptively. The broader point about missing confidence intervals is covered in Major #1.
- **"The proxy tokenizer result may not generalize to GPT-3.5"** — This is a scope caveat the paper already acknowledges by testing only on StarCoder-3B for that ablation. Speculating about non-generalization is not a weakness.
- **"The paper withholds attack strings"** — This is standard practice for security papers. The paper offers to provide them upon request. Not a weakness.
- **"No demonstration beyond line-removal task"** — The paper explicitly scopes to single-line completion (following Bavarian et al., 2022). Demanding evaluation on larger missing blocks is scope creep.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel insight that the paper itself misses, though the confounded comparison observation (Minor #3) is a useful methodological caution that the paper could address in revision.

## Suggestions

1. **Provide per-CWE breakdowns.** Add a table or box plot showing attacked vs. unattacked vul ratios for all 16 CWEs across at least the primary models. This single addition would address the most serious evidential gap and reveal whether INSEC generalizes broadly or exploits a narrow subset of weaknesses.

2. **Validate the multilingual HumanEval references.** Manually inspect a representative sample of GPT-4-generated reference solutions per language for correctness and idiomaticity. Report the pass rate and, if errors are found, re-run the func rate evaluation on a corrected subset.

3. **Report missing optimization parameters.** Include the iteration count per model/CWE, the pool/population size $n_\varphi$, and the compute budget (generations, candidates evaluated) for open-source models. This would significantly improve reproducibility.

4. **Clarify Copilot status.** Either present Copilot results in a table/figure, or explicitly state the reasons for their absence. If results exist but are omitted for ethical reasons, explain the policy.

5. **Add a brief discussion of whether attack string properties differ across models** (e.g., length, token types) and how this affects the comparison of functional correctness preservation.

## Score and Decision

This paper presents a novel and practically important contribution — the first black-box adversarial attack on LLM-based code completion that works on commercial APIs. The methodology is well-designed, the ablations are thorough, and the results are consistent across models and languages. However, the evaluation has two significant gaps that prevent full acceptance in its current form: (1) the vulnerability results lack per-CWE granularity and uncertainty quantification, making it impossible to assess whether the claimed ~50% increase is uniform or artifact-driven; and (2) the functional correctness results for non-Python languages rely on unverified GPT-4-generated reference solutions. These are fixable with additional analysis, and the core contribution is valuable enough to warrant acceptance conditional on addressing them. The remaining weaknesses (missing hyperparameters, absent Copilot results, confounded comparisons) are manageable in revision.

**Originality:** High — first black-box attack on code completion.  
**Importance of question:** High — code completion engines are used by millions of developers.  
**Support for claims:** Moderate — the main vulnerability result is broadly supportive at the aggregate level but lacks granular evidence.  
**Soundness of experiments:** Moderate — strong ablations, but the two major gaps weaken confidence.  
**Clarity:** Good.  
**Value to community:** High — opens a new threat axis and provides a strong baseline for future work.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>