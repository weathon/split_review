Now I have enough calibration data. Let me write the final review.

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| NEMESIS jailbreaking | 5kMwiMnUip.md | 1.40 | R1 | Much weaker: basic jailbreak tricks, no scientific contribution |
| Playing Language Game | BeOEmnmyFu.md | 2.50 | R1 | Much weaker: limited novelty |
| Measuring Effects of Steered Rep | z1yI8uoVU3.md | 3.00 | R1 | Weaker: narrower scope, less impactful findings |
| Steering LMs with Activation Eng | 2XBPdPIcFK.md | 5.00 | R1 | Weaker: outdated, inconsistent baselines, less novel |
| Conceptors and Beyond | 9wjGUN65tY.md | 5.00 | R1 | Weaker: narrower contribution |
| Jailbreaking with Simple Adaptive | hXA8wqRdyV.md | 6.14 | R2 | Our paper stronger: more counterintuitive finding, more novel mechanism insight |
| Injecting Universal Jailbreak Backdoors | aSy2nYwiZ2.md | 6.67 | R2 | Our paper stronger: more practical attack (steering-only), broader models, more surprising result |
| Improving Instruction-Following | wozhdnRCtw.md | 7.00 | R1 | Comparable: both solid activation steering papers. Ours has broader scope and more surprising finding but looser evidence |
| Beyond Memorization: Privacy | kmn0BhQk7p.md | 7.20 | R2 | Slightly stronger: tighter claims-to-evidence, but different topic |
| Can Sensitive Info Be Deleted | 7erlRDoaV8.md | 7.50 | R2 | Stronger: more polished, tighter experimental design |
| Backtracking Improves Safety | Bo62NeU6VF.md | 8.00 | R1 | Stronger: cleaner method, more complete story |

**Bracket from Round 1:** 6.5 - 8.0
**Narrowed after Round 2:** The paper sits between ~6.67 and ~7.50, and is quite comparable to the 7.00 activation steering paper. I place it at **7.0**.

---

## Summary
This paper demonstrates that activation steering—adding vectors to LLM residual stream activations during inference—systematically undermines model safety alignment, even when vectors represent random noise or semantically benign concepts. Through extensive experiments across four model families (Llama-3, Qwen2.5, Falcon-3, Falcon-H1) spanning 3B–70B parameters, random-direction steering induces 2–27% harmful compliance rates from a 0% baseline. SAE-feature steering is comparably dangerous, with top jailbreaking features corresponding to ostensibly benign concepts. Most strikingly, averaging just 20 random vectors that each jailbreak a single prompt creates a universal attack that generalizes to unseen harmful requests (e.g., 50.4% on Llama3-70B, 63.4% on Falcon3-7B), requiring only black-box steering access.

## Strengths
- **Comprehensive cross-model empirical demonstration.** The paper tests random-direction steering across Llama-3, Qwen2.5, Falcon-3, and Falcon-H1 at sizes from 3B to 70B, with non-zero harmful compliance in every tested configuration (Fig. 2a, Fig. 6). The 300,000-response evaluation scale gives the categorical breakdowns (Fig. 3) and SAE histogram (Fig. 4a) genuine statistical weight.
- **Novel and practically significant universal attack (Section 4.4).** Averaging just 20 randomly sampled vectors that each jailbreak a single prompt yields a universal attack vector generalizing to 99 unseen harmful prompts. This requires no model weights, gradients, logits, or harmful training data—only steering access and output observation. The 4× average compliance increase (Fig. 6), with Falcon3-7B jumping from 5.7% to 63.4%, is a striking result.
- **Clean head-to-head comparison of random vs. SAE steering.** Figure 2c directly compares random-direction and SAE-feature steering on the same model (Llama3.1-8B), same layer, and same coefficient sweep, finding SAE features yield compliance rates 2–4% higher than random vectors—falsifying the assumption that interpretable directions are inherently safer.
- **Rigorous SAE feature analysis revealing widespread, benign-looking dangerous features.** Section 4.2 reports 668/1000 tested SAE features jailbreak at least five prompts (Fig. 4a), the most effective features correspond to concepts like "brand identity," and the cross-category heatmap (Fig. 4b) shows poor generalization—no single feature acts as a universal master key. Together these imply pre-screening SAE features for safety is practically infeasible.
- **Concrete production-API case study bridging lab findings to real-world risk.** Section 4.3 demonstrates the vulnerability on a deployed system via Goodfire's public API, revealing two failure modes (disclaimer-then-compliance, justification via fictional framing) where the model produces actionable harmful content while superficially appearing responsible.
- **Methodologically careful steering normalization.** The paper computes layer-dependent baseline activation norms and sets steering strength as α = c · μ^(l), ensuring comparable intensities across architectures with different activation magnitudes.

## Weaknesses

### Fatal
None.

### Major
- **Mechanism ambiguity limits interpretive confidence.** The paper frames its finding as activation steering specifically undermining safety mechanisms. However, random Gaussian perturbations to residual stream activations could also produce harmful compliance through general behavioral degradation rather than targeted safety-circuit interference. The paper references Appendix E for preliminary mechanism analysis ("not due to simple alignment with known refusal directions nor general capability degradation"), but the main text presents insufficient evidence to cleanly separate these interpretations. The empirical finding—steering demonstrably causes harmful compliance—stands regardless, but the strong interpretive framing about *how* steering breaks safety is weakened. This matters because mitigation strategies could differ depending on whether the cause is safety-circuit-specific interference or general perturbation brittleness.

### Minor
- **No variance or confidence interval reporting despite large sample sizes.** The paper reports average compliance rates from 1,000 random-vector and 1,000 SAE-feature samples but never reports standard deviations or confidence intervals. With 1,000 trials, even small differences (e.g., 2–4% between random and SAE steering) may be statistically significant, but readers cannot assess this. This is especially important for the SAE-vs-random comparison where the claimed difference is modest.
- **SAE benign-feature labeling depends on automated API interpretations without independent validation.** The top jailbreaking SAE features are labeled as "brand identity," "physical positioning," and "technical implementations" via Goodfire's automated API. SAE feature interpretability has known reliability issues; without presenting max-activating examples, readers cannot independently assess whether these features are genuinely benign or capture patterns that plausibly correlate with harmful compliance. The empirical finding that SAE features cause jailbreaking stands regardless, but the strong claim about *benign* features being dangerous requires validation not fully provided in the main text.
- **The 0% baseline compliance rate across all models invites scrutiny.** A literally perfect refusal rate across 100 harmful prompts and multiple model families is unusual. This could indicate the Qwen3-8B judge is calibrated conservatively (classifying borderline cases as SAFE), meaning steering-induced compliance rates are underestimates. The paper references human validation in Appendix B; moving key calibration metrics into the main text would strengthen confidence in the primary metric.
- **SAE experiments restricted to a single model and layer.** All SAE-based experiments use Llama3.1-8B at layer 19 with Goodfire's SAE. The paper acknowledges this constraint, but conclusions about SAE features are stated broadly. Testing at least one additional configuration would strengthen these claims.
- **Potential for correlated judge-model failure modes not discussed.** Using Qwen3-8B as judge while Qwen2.5 models are among those being evaluated creates a risk of correlated biases (e.g., shared safety-training characteristics).

### Trivial
- The conclusion's call for "adversarial training to counter steering perturbations" feels premature without stronger mechanism understanding. This is a minor framing issue in an otherwise measured conclusion.

## Nice-to-Haves
- Add a perturbation control condition (e.g., Gaussian noise of comparable magnitude to attention outputs or MLP outputs) to help distinguish safety-specific compromise from general perturbation brittleness. Even a small-scale version on one model would be informative.
- Provide max-activating examples for the top-5 jailbreaking SAE features to let readers independently assess the "benign" label claim.
- Explore the interesting cross-category generalization asymmetry in Fig. 4b: features that break "hard" categories generalize to "easy" categories, while the reverse is not true.
- Discuss why the universal attack's effectiveness varies dramatically by model (Falcon3-7B: 63.4% vs. Qwen2.5-32B: 9%).
- Verify that the bomb prompt used for universal attack construction is not disproportionately representative of the dataset.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that the paper "conflates two distinct causal stories" as structural/fatal:** The paper's core claim is empirical (steering causes safety failures), not mechanistic. The paper references App. E for mechanism analysis. The criticism overreaches—the empirical finding stands regardless of mechanism. The mechanism concern is legitimate but was demoted to Major and described more precisely.
- **Harsh Critic concern about "steering applied to all tokens at a single fixed layer" being unmotivated:** The paper explicitly cites Durmus et al. (2024) for this design choice, which is standard practice in the activation steering literature. Removed.
- **Harsh Critic criticism of "benign steering might also undermine alignment" as semantic blurring:** The paper explicitly separates these as two different source types for steering vectors in Section 3.2 ("Random Directions" vs "SAE-based Directions"). The blurring claim is incorrect. Removed.
- **Harsh Critic point about technical background (Section 3.3) being "somewhat unnecessary":** This is pure stylistic preference. The technical background helps readers from adjacent fields. Removed.
- **Strength Finder's "well-motivated research gap" as standalone strength:** This is a generic framing strength present in most well-written papers. Removed as a standalone point (implicitly captured in the summary).
- **All formatting/style nitpicks from Harsh Critic (parser artifacts, table inconsistencies):** These are parser issues, not author errors. Removed per the hard rule.
- **Harsh Critic's demand for missing related works:** Removed per the hard rule—we cannot confirm their existence.
- **Harsh Critic's criticisms about stripped appendix content (App. B, App. E):** The parser strips appendices from all papers; they exist in the original submission. Removed any criticism that depends on assuming appendix content is missing or inadequate.

## Novel Insights
The most striking finding is the asymmetry in the universal attack results: averaging random jailbreak vectors amplifies compliance dramatically for some model families (Falcon: 5×–10× increase) but provides minimal or negative benefit for others (Qwen2.5-32B: no improvement over random). This model-family dependence is not explained by model scale alone (Falcon-H1-34B benefits little, while Llama3-8B benefits substantially) and suggests that architectural or safety-training differences interact with the linear geometry of the residual stream in non-obvious ways. This is a genuinely novel empirical observation that deserves further investigation.

## Suggestions
- Move key mechanism evidence from Appendix E into the main text—even one paragraph and one figure demonstrating that steered models maintain capability on benign benchmarks would substantially strengthen the interpretive claims and address the major weakness.
- Add standard deviation or confidence intervals to all compliance rate reports. With 1,000 trials per configuration, this is straightforward and would let readers assess which observed differences are reliable.
- Report judge-human agreement rates in the main text (referenced in Appendix B) to give readers confidence in the compliance metric, and discuss the judge-model family correlation concern.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>