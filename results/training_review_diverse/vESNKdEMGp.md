Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper investigates multilingual jailbreak vulnerabilities in LLMs, identifying two scenarios (unintentional — non-English users inadvertently bypassing safety; intentional — malicious actors combining harmful prompts with multilingual queries). It introduces MultiJail, the first manually curated multilingual jailbreak dataset covering 10 languages, and proposes the Self-Defence framework that uses the LLM itself to generate multilingual safety training data. The paper provides strong evidence that low-resource languages yield roughly 3× more unsafe content than high-resource languages, and that multilingual adaptive attacks can push ChatGPT's unsafe rate to 99.37%.

## Strengths

- **Systematic identification and characterization of two distinct multilingual jailbreak scenarios.** The paper clearly differentiates unintentional risks (non-English users inadvertently exposed to unsafe content) from intentional attacks (malicious actors combining jailbreak instructions with multilingual prompts), organizing empirical investigation around this taxonomy (Section 2). This framing is well-motivated by preliminary results showing a clear correlation between language resource level and unsafe output rate.

- **MultiJail: the first manually curated multilingual jailbreak dataset.** The dataset covers 10 languages across three resource levels with native-speaker translations and a reported quality pass rate >97% (Section 3.1). This fills a clear gap in the literature — no comparable resource existed — and provides a foundation for reproducible evaluation. The paper also includes analysis showing that machine translation yields comparable or slightly higher unsafe rates (11.15% vs. 10.19%), demonstrating that the threat does not depend on perfect translations.

- **Compelling quantitative evidence that low-resource languages are substantially more vulnerable.** In the unintentional scenario, ChatGPT's unsafe rate rises from 4.34% (high-resource) to 14.92% (low-resource); GPT-4's from 3.60% to 10.16% (Table 1). The ~3× ratio is consistent across both models, and the finding that multilingual adaptive attacks achieve 99.37% (ChatGPT) and 79.05% (GPT-4) unsafe rates (Table 4) is alarming and practically significant.

- **The Self-Defence framework provides a language-agnostic approach to generating multilingual safety training data.** After fine-tuning, the unsafe rate drops from 10.19% to 3.95% (unintentional) and from 80.92% to 60.00% (intentional) (Figure 6). The framework's reliance on self-generated data (requiring only limited English seed examples) is practically appealing given the high cost of human-annotated multilingual safety data. The trade-off analysis between safety and usefulness (Figure 7) provides guidance for deployment decisions.

- **Evaluation of open-source LLMs provides complementary insights.** The finding that SeaLLM-v2 (language-specific safety tuning) outperforms both ChatGPT and GPT-4 on some Southeast Asian languages demonstrates that targeted multilingual safety tuning is achievable and underscores the paper's call for greater attention to this problem (Section 3.3).

## Weaknesses

### Fatal
None.

### Major

- **Self-Defence is evaluated only as a before–after comparison, with no baselines against simpler alternatives.** The paper presents Self-Defence as a core contribution but does not compare it against obvious baselines — e.g., directly machine-translating the English safety seed examples into the target languages and fine-tuning on that data, or using conventional RLHF on the same seed data. Without these comparisons, it is impossible to determine whether the improvement comes from Self-Defence's specific design (self-generation of diverse examples) or simply from the generic act of adding multilingual safety data. The claim that the framework is "effective" is supported in an absolute sense (before–after improvement), but its relative effectiveness over straightforward alternatives is unsubstantiated. This is the most significant gap in the paper's experimental validation.

### Minor

- **The "usefulness" evaluation uses narrow classification benchmarks that do not fully match the paper's definition.** The paper defines usefulness as "how well the LLM's output meets user requirements" but operationalizes it with accuracy on classification tasks (XNLI, PAWS-X). These are reasonable proxies for general multilingual capability, but they do not measure the quality of open-ended generation or dialog helpfulness that users actually experience. A safety fine-tuning method that preserves classification accuracy while degrading real conversational quality would be missed. The core conclusions are not invalidated, but the trade-off argument (Figure 7) would be strengthened by a generative evaluation.

- **Results are reported as point estimates without confidence intervals or significance tests.** Table 1 reports per-language unsafe rates as exact figures, but given the dataset size (~315 examples across 10 languages, roughly 35 per language) some differences between languages could arise from sampling noise. Bootstrapped confidence intervals would substantially strengthen the evidence and allow readers to assess the reliability of the observed patterns. This is a standard expectation for empirical NLP work at this scale.

- **The paper does not candidly discuss the limitations of Self-Defence for the intentional scenario.** After fine-tuning, the unsafe rate in the intentional scenario remains at 60.00% — meaning a majority of malicious multilingual queries still succeed. The paper describes this as an "impressive decrease of 20.92%" but does not acknowledge that the resulting system remains functionally broken for the intentional scenario. A more balanced discussion of what "effective" means in this context would improve the paper.

- **Seed example design choices (50 examples, 3:7 unsafe-to-general ratio) are presented without justification or sensitivity analysis.** The paper does not ablate these choices or explain why 50 and 3:7 were chosen. While the trade-off analysis (Figure 7) varies the unsafe ratio, it does so in a different experiment, and the 50-example count is never probed. This limits understanding of how robust the framework is to its core design decisions.

### Trivial

- **The term "adaptive attack" is slightly inflated.** The multilingual attack strategy (trying all languages in a pool and counting success if any one works) is a brute-force enumeration rather than an adaptive strategy. The paper does clearly define what is meant, but the terminology suggests more sophistication than the method possesses.

- **The AIM instruction selection is justified only by a single snapshot (highest votes on a website as of one date).** While reasonable as a proxy for "what a real attacker would find," the generalizability of results to other malicious instructions is untested.

- **The selection procedure for the 300 Anthropic red-teaming examples is described at a coarse granularity.** The paper states that examples were "purposely sampled… considering task_description_harmlessness_score and tags" but does not provide a reproducible protocol. This is a transparency issue rather than a methodological flaw, given the dataset is to be released.

## Nice-to-Haves

- Evaluate Self-Defence on a held-out language not seen during training (e.g., Urdu or Finnish) to test whether the framework learns language-agnostic safety principles or merely memorizes safety patterns for the training languages.
- Ablate the seed example count (e.g., 25, 50, 100) and the unsafe-to-general ratio to understand sensitivity.
- Include a broader set of malicious instructions beyond AIM to test whether results generalize.
- Replace or supplement the classification-based usefulness metric with a generative evaluation (e.g., MT-Bench or refusal rates on benign prompts).

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"The paper's own analysis (Figure 5) shows that machine translation yields higher unsafe rates, which undercuts the argument that human translation is necessary."* — This criticism misunderstands the purpose of human translation. The paper uses human translation to ensure semantic fidelity of prompts (avoiding noisy/incorrect translations), not to achieve a particular unsafe rate. The finding that MT yields slightly higher unsafe rates is a separate observation showing MT suffices for jailbreaking, not an inconsistency. The two statements coexist without contradiction.

- *"The x-axis label is missing from the figure due to the parser"* — Parser artifact; not present in the original submission.
  
- *"No learning rate, batch size, or checkpoints are reported"* for the OpenAI fine-tuning API — These are server-side parameters for the API and are not configurable by the user in the standard API workflow. The paper reports the salient detail ("3 epochs") along with the API endpoint used. This is standard practice for API-based fine-tuning.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the finding that SeaLLM-v2 (a model with targeted multilingual safety tuning) outperforms both ChatGPT and GPT-4 on some Southeast Asian languages suggests that the cost of multilingual safety may be lower than assumed — it is not a fundamental limitation of LLMs but a matter of training data coverage. This insight strengthens the paper's implicit argument that the current safety gap is a fixable oversight rather than an inherent capability limitation, and it provides a promising direction for future work.

## Suggestions

- **Add at least one strong baseline for Self-Defence** — the most obvious and informative comparison is to machine-translate the 50 English seed safety examples into the 9 target languages and fine-tune on that data alone. This directly tests whether the self-generation step (which adds diversity and automatically generates new examples) adds value beyond simple translation of existing safety data. Without this, the method contribution is incompletely validated.

- **Add confidence intervals** to the main results (Table 1) using bootstrapping. The per-language sample sizes (~35 per language) are small enough that sampling variability could affect conclusions, especially for comparisons between individual languages.

- **Reframe the discussion of Self-Defence's intentional-scenario results.** The 60.00% post-fine-tuning unsafe rate should be acknowledged as still problematic, with a clearer statement about what the method achieves and where it falls short. This would strengthen the paper's credibility.

- **Provide a more transparent description of the Anthropic red-teaming selection procedure** (e.g., exact score thresholds or tag filters used) in the dataset release documentation.

## Score and Decision

The paper makes two solid contributions: (1) a clear empirical demonstration that multilingual jailbreak is a serious and measurable problem (supported by the MultiJail dataset), and (2) a practical framework for generating multilingual safety training data. The problem diagnosis is well-executed and convincing. The main weakness is that Self-Defence, presented as a core contribution, lacks baseline comparisons — we know it works, but not whether it works better than trivial alternatives. This is a significant gap but not a fatal one; it can be addressed in revision without invalidating the paper's overall value. The paper is publishable in its current form if the method contribution is toned down, or it would be substantially stronger with baselines added.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>