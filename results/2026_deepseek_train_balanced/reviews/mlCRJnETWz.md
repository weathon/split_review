I need to correct one point — the caption says standard deviations over five random injections are reported. Let me finalize.

---

## Summary
This paper reformulates knowledge editing techniques (ROME, fine-tuning, in-context editing) as a safety threat called "Editing Attack," constructing the EditAttack dataset to study two risks: misinformation injection and bias injection. Through experiments across five 7B-scale LLMs, it demonstrates that editing methods can implant misinformation and biased sentences with high effectiveness, and that a single biased edit can spill over to increase bias on unrelated fairness dimensions. The paper also examines the stealthiness of these attacks via benchmark performance and argues that defense is hard.

## Strengths

1. **Novel threat formulation that meaningfully extends existing safety attack taxonomies**: The paper formally defines editing attacks as a distinct threat vector — efficient, controllable, and stealthy — different from jailbreaking (prompt-level) and fine-tuning attacks (training-level). This framing is well-motivated by the open-source ecosystem where edited models can be distributed, and the formalization as a knowledge-triple operation $e = (s, r, o, o^*)$ gives it precise operational specificity.

2. **Empirical demonstration of bias spillover across unrelated categories (Figure 2)**: Injecting a single gender-biased sentence into Llama3-8b via ROME increases Bias Scores on the BBQ benchmark not only for Gender but also for Race, Religion, and Sexual Orientation — categories whose evaluation questions are semantically unrelated to the injected sentence. This is a non-obvious finding since knowledge editing is specifically designed to minimize side effects, and it is supported by quantitative results across five bias types.

3. **Systematic experimental coverage**: The evaluation spans three editing paradigms (locate-then-edit, fine-tuning, in-context editing) across five LLMs (Llama3-8b, Mistral-v0.1-7b, Mistral-v0.2-7b, Alpaca-7b, Vicuna-7b). This breadth reveals that robustness to editing attacks is model-specific — e.g., FT is nearly ineffective on Mistral-v0.2-7b for gender bias (20→28%) while achieving 100% on Vicuna-7b (Table 2) — showing that editing-based attacks are not uniformly effective.

4. **The commonsense vs. long-tail misinformation distinction is well-motivated and empirically grounded**: The paper separately curates and evaluates misinformation with different knowledge popularity, finding that commonsense misinformation injection achieves particularly high effectiveness while long-tail misinformation is harder to inject. This is a useful result for understanding the scope of the threat.

## Weaknesses

### Fatal
None.

### Major

1. **Missing benign-edit control for the causal claim about bias spillover.** The paper claims that "one single biased sentence injection can cause a bias increase in general outputs" (Finding 2), attributing the effect to the *biased nature* of the edited content. The experiment lacks a control condition where a neutral/benign fact (e.g., editing "The Eiffel Tower is in London" → "The Eiffel Tower is in Paris") is injected using the same methods. Without this control, the observed Bias Score increase could be a generic side effect of *any* knowledge edit — editing methods are known to cause distributional shifts. If a benign edit produces a similar Bias Score increase, the finding reverts to "any edit can destabilize fairness," a different claim with different implications. The paper's evidence currently supports the weaker interpretation.

2. **EditAttack dataset is under-described despite being a named contribution.** The paper does not report: (a) the total number of commonsense vs. long-tail misinformation examples, (b) the number of bias injection examples per category (gender, race, religion, sexual orientation, disability), (c) the number of evaluation questions, (d) inter-annotator agreement or human verification protocol details, or (e) representative examples of long-tail misinformation from each of the five domains. For a dataset that is a central contribution of the paper, these omissions limit reproducibility and make it difficult to assess whether the findings generalize beyond the specific constructed examples.

### Minor

1. **ICE is qualitatively different from weight-modifying methods, and the paper should separate these more clearly.** In-context editing (ICE) does not modify model parameters, does not persist across sessions, and resides entirely in the input prompt — making it detectable by prompt inspection and categorically different from ROME/FT in terms of persistence and defense. While ICE is a legitimate knowledge editing paradigm in the literature (Zheng et al. 2023), bundling it under the unified "Editing Attack" label conflates two different attack surfaces. The paper's strongest contribution is the demonstration that *parameter-modifying* editing can inject harm; ICE should either be separated or explicitly discussed as a qualitatively different (prompt-based) attack with its own detection surface.

2. **The "high stealthiness" claim overstates what is measured.** Table 3 shows that broad coverage benchmarks (BoolQ, GSM8K, NLI) are minimally affected after a single edit. This is expected behavior: a single localized edit should not measurably shift accuracy across thousands of diverse examples. The finding confirms that editing methods have low side effects (a known design goal), but calling it "high stealthiness" conflates "the method has low side effects on unrelated knowledge" with "the attack is hard to detect" — the latter would require a detection-oriented evaluation (e.g., probing internal activations, measuring per-sample entropy shifts). The paper should use more precise language.

3. **The "hardness of defense" conclusion goes beyond what the evidence supports.** The defense analysis only shows that aggregate benchmark accuracy does not reliably differentiate edited from non-edited models — a null result on one simple detection signal. No actual defense method is proposed or evaluated. The paper calls this "preliminary analysis" (line 671) but then concludes it demonstrates "hardness of defending editing attacks." The claim should be scoped to "simple accuracy-based filtering is insufficient" rather than implying defense in general is hard.

4. **Limited model scope for the bias spillover analysis.** The bias injection fairness results (Figure 2) are presented primarily for Llama3-8b, with Mistral-v0.1-7b results noted as supplementary. Given that the bias spillover is the paper's most striking finding, testing on only 1–2 models limits confidence in its generalizability.

### Trivial
- ICE rows in Table 3 show zero standard deviation on BoolQ, GSM8K, and NLI — this arises because ICE does not modify parameters (deterministic across runs), but the paper does not explain this.

## Nice-to-Haves
- Add the benign-edit control to the bias injection experiment (see Major #1).
- Report dataset size and composition statistics for EditAttack.
- Include a model at larger scale (e.g., 13B or 70B) to test generalizability beyond 7B.
- Add error bars / standard deviations to Tables 1 and 2 for completeness (already present in Table 3).
- Provide example long-tail misinformation items from each of the five domains.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Harsh critic claim: "ICE near-perfect scores on Mistral-v0.1-7b (99→99 for commonsense efficacy; 100→100 for long-tail efficacy) show the model already outputs the target answer at high rates before any editing."* — **Factually wrong.** The table format shows post-edit score with increase separately; pre-edit scores for ICE on Mistral-v0.1-7b are ~1%, not 99%. The critic misread the table.
- *Harsh critic claim that "the pre-edit scores in Table 1 are hard to read."* — **Formatting nitpick.** Removed per hard rules. The format is non-standard but clearly explained in the caption.
- *Harsh critic claim that ICE is "not an editing attack in any meaningful sense" — a "category error."* — **Partially removed.** ICE is a well-established knowledge editing paradigm in the literature (Zheng et al. 2023). The legitimate concern about differing attack surfaces is retained as Minor #1.
- *Strength Finder generic strengths ("addressed an important problem," "targeted an interesting question").* — **Generic/superficial.** Removed per filtering rules.

## Novel Insights
None beyond the paper's own contributions. The most interesting finding — the bias spillover effect — is already presented by the paper itself.

## Suggestions

1. **Add the benign-edit control** to the bias injection experiment (single highest-leverage addition). If a benign edit does not increase Bias Scores, the specific claim about *biased* content becomes much stronger; if it does, the finding shifts to "any edit can destabilize fairness," which is a different but still valuable result.
2. **Report dataset statistics** for EditAttack (counts, composition, quality metrics).
3. **Separate ICE from ROME/FT** in the framing, or explicitly discuss the different attack surfaces, persistence properties, and detection implications.
4. **Calibrate the claims** about stealthiness and defense hardness to match what the experiments actually show.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>