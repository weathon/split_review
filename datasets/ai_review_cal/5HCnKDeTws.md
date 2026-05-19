- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 5, 8
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper presents the first systematic study of scaling laws for LLM finetuning, examining how finetuning performance scales with LLM model size (1B–16B), pretraining data size, PET parameter size (prompt length, LoRA rank), and finetuning data size across three tasks (En-De/En-Zh translation, multilingual summarization) and three methods (FMT, prompt tuning, LoRA). The central contribution is a multiplicative joint scaling law (Eq. 1) that relates finetuning data size multiplicatively with each other factor. Key findings: model scaling helps finetuning more than pretraining data scaling; PET parameter scaling is largely ineffective; and the optimal finetuning method is task- and data-dependent.

## Strengths

- **Proposal and validation of a multiplicative joint scaling law.** The paper introduces Eq. 1 and systematically compares it against an additive formulation on held-out data. Table 1b shows that the multiplicative form achieves consistently lower held-out prediction errors across methods and factors (e.g., average 0.0048 vs. 0.0079 for LLM model size on En-De), providing concrete evidence that the multiplicative form generalizes better.

- **Systematic and broad experimental design.** The study spans two LLM families (1B–16B), three downstream tasks, three finetuning methods, and up to 25M finetuning examples — substantially more comprehensive than prior work (e.g., Hernandez et al. 2021, which focused on single-factor transfer scaling). This breadth gives the findings reasonable empirical grounding within the studied scope.

- **Valuable practical insights supported by data.** The finding that model-size scaling exponents (α_m) consistently exceed pretraining-data exponents (α_p) across methods and tasks offers concrete guidance for resource allocation. Similarly, the demonstration that PET parameter scaling yields marginal or inverse gains (|α_t| ≪ 1e-2) is a useful negative result, countering a common assumption that larger prompts/ranks always help.

- **Critical-point analysis for method selection.** Using the fitted scaling law to estimate data-size thresholds where one method overtakes another (Figure 5) provides actionable, task-dependent guidance (PET for few thousand examples, FMT for million-scale data), even though these estimates rely on extrapolation.

- **Zero-shot generalization analysis.** The paper evaluates how finetuning affects generalization to related translation directions (Figure 6), showing that PET methods preserve generalization better than FMT — an important practical concern when specialization could harm broader capability.

## Weaknesses

### Fatal
None.

### Major

- **Missing finetuning optimization details across all methods.** The paper reports pretraining hyperparameters (Adafactor, cosine LR, one epoch, §2) but discloses *no* finetuning hyperparameters: no learning rate, batch size, optimizer, number of epochs, or hyperparameter search procedure for any of the three methods (FMT, prompt tuning, LoRA) at any scale. The evaluation uses "best checkpoint based on token-level perplexity on the dev set" (§2), which mitigates some unfair-comparison risk, but without knowing whether each method at each scale received comparable tuning effort, the central comparisons of scaling exponents across methods rest on an opaque foundation. This is a structural reproducibility gap. (The paper does acknowledge "imperfection of the optimization ... in some setups" in the conclusion, but this is too vague to substitute for reporting.)

- **PET scaling conclusions rely on extrapolation beyond validated data range.** PET experiments (prompt tuning, LoRA) use finetuning data sizes only up to 100K examples (Table 1b), while FMT experiments reach 4.5M–25M examples. The critical-point analysis (Figure 5) and claims about PET data-hungriness (e.g., "FMT is more data-hungry") depend on PET scaling-law fits being extrapolated well beyond 100K (critical points reach ~1M+). The paper does not flag this extrapolation as uncertain. While held-out validation checks interpolation within the 100K range, it does not validate the extrapolation to 10× larger data. The claim that "PET parameter scaling is ineffective" (which depends on small β exponents fitted on ≤100K data) could change if PET were evaluated at much larger data sizes where parameter expressivity becomes more relevant.

### Minor

- **No uncertainty quantification on scaling exponents.** The paper reports point estimates for α_m, α_p, α_t, and β but provides no confidence intervals or error bars (e.g., from bootstrapping or multiple random seeds). Comparisons such as "α_m > α_p" would be more convincing with uncertainty bounds, especially since some differences appear small. The paper does run three random subsets and reports average performance, but variance is not shown in the exponent estimates.

- **Intermediate pretraining checkpoints as proxy for pretraining data scaling.** The paper acknowledges this is "sub-optimal" (§2), but the concern remains: differences in training state (learning rate schedule position, optimization convergence) across checkpoints could confound the pretraining-data scaling curves. This is a known limitation that readers should factor into their interpretation of the pretraining data size findings.

- **Zero-shot evaluation lacks variance reporting.** Figure 6 reports average zero-shot BLEURT scores over multiple source languages, but the paper states three random runs were performed (§2) without showing variance. The "PET performs much better than FMT" zero-shot claim is supported by the visible trends but would be strengthened by error bars or significance tests.

- **Claims stated generally despite domain limitations.** The abstract and introduction state findings (e.g., "LLM finetuning follows a power-based multiplicative joint scaling law") without always explicitly qualifying the scope (1B–16B models, closed-generation tasks, bilingual LLMs). The paper later acknowledges this (e.g., "Our selection of closed generation tasks ... might deliver biased observations," §4), but the framing in high-level claims could be better scoped.

### Trivial
None.

## Nice-to-Haves

- Validating PET scaling at larger data sizes (e.g., 500K–1M examples) on at least one setting would directly test whether the small β exponent holds at scale or is an artifact of the limited data range.
- Reporting hyperparameter search spaces and best configurations per method and scale in an appendix would substantially improve reproducibility.
- Providing bootstrapped confidence intervals on the fitted scaling exponents.
- Releasing finetuning code (e.g., T5X configuration files) would aid reproducibility but is not required.

## Removed Points

These points were identified by the harsh reviewer but are excluded from the main weaknesses for the following reasons:

- **"Additive vs. multiplicative fitting procedure may be unfair"** — The paper describes the same joint fitting procedure (§3, Eq. after line 129) for both formulations and provides direct empirical comparison in Table 1b showing multiplicative has lower held-out error. The reviewer's speculation about unfair fitting constraints is not supported by the paper text.
- **"Abstract claim about PET outperforming FMT is not supported"** — The claim (line 27) is specifically about zero-shot generalization, where Figure 6 does show PET outperforming FMT. The reviewer misread the scope of the claim.
- **"Missing related works on vision finetuning scaling"** — Rule prohibits mentioning missing related works.
- **"Code/data not released"** — Rule removes criticisms questioning existence/release status of cited entities. Also moved to Nice-to-Have.
- **"Finetuning data distribution for MLSum"** — The paper states "When sampling for MLSum, we keep the mixing ratio over different languages fixed" (§2), which directly addresses this concern.
- **"Checkpoint selection using PPL may favor overfitting"** — Using dev-set PPL for checkpoint selection is standard practice. The paper also notes the "challenging issues when tuning on small datasets" (§4).
- **Several formatting/style nitpicks and section-by-section observations** that are either already addressed by the paper, overly speculative, or constitute scope creep.

## Novel Insights

The reviews collectively surface a tension that the paper's own narrative does not fully resolve: the multiplicative joint scaling law is presented as a general finding, but the PET experiments (≤100K data) and FMT experiments (up to 25M data) operate in fundamentally different regimes, making the "general" law's parameter estimates and critical-point extrapolations less reliable than the paper's confident framing suggests. An insightful path forward — not present in the paper — would be to reframe the contribution as describing scaling *in the data-limited regime* for PET and *across a wider regime* for FMT, explicitly treating the PET-FMT comparison as an extrapolation rather than an interpolation result.

## Suggestions

1. **Report all finetuning hyperparameters.** Disclose learning rate, batch size, optimizer, number of epochs, and hyperparameter search strategy for each method (FMT, prompt tuning, LoRA) at each scale, or cite the source if following a prior protocol. Even a concise table of best hyperparameters per method/task would resolve the most significant weakness.

2. **Acknowledge PET extrapolation explicitly.** Add a caveat to the critical-point analysis (Figure 5) noting that PET scaling laws were fitted on ≤100K data and that critical-point values beyond this range are extrapolations that have not been empirically validated. If possible, add at least one PET experiment at 500K or 1M examples to validate the trend.

3. **Add uncertainty quantification.** Report bootstrapped confidence intervals or standard errors on the fitted exponents (α_m, α_p, α_t, β) to make comparisons between methods and factors statistically grounded.

4. **Scope claims more precisely.** In the abstract and introduction, qualify findings with the model size range (1B–16B), task types (closed-generation), and data regimes studied, rather than presenting them as universal LLM finetuning properties.
