- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 5, 8, 5
Now I have all the verification I need. Let me write the final consolidated review.

---

## Summary

This paper evaluates four baseline defenses from the adversarial ML literature (perplexity filtering, paraphrasing, retokenization via BPE-dropout, and a simplified form of adversarial training) against the GCG jailbreaking attack on LLMs. It documents which defenses transfer effectively and which do not, and makes a case (primarily through the discussion in Section 5) that the LLM domain is qualitatively different from computer vision because discrete text optimization is orders of magnitude more expensive, making computational budget a more meaningful threat-model constraint than ℓ_p norms. The strongest empirical contribution is the perplexity filter, which blocks all GCG attacks in both black-box and white-box settings with a ~10% benign false-positive rate.

## Strengths

1. **Principled redefinition of threat models for LLMs (Section 3).** The paper argues that ℓ_p-norm bounds are inappropriate for LLMs and proposes constraining attackers by computational budget (number of model evaluations). This directly motivates why expensive discrete optimization makes simple preprocessing defenses harder to bypass in this domain — a clear conceptual contribution.

2. **Clean evidence that perplexity filtering is highly effective against GCG.** Table 1 shows that the original GCG attack passes the perplexity filter 0% of the time across five 7B models. Figure 2 shows that even a white-box adaptive attack (adding ℓ_ppl to the loss) can only achieve ~10% ASR before the attack itself collapses. This is genuinely different from vision, where detectors are routinely broken, and directly supports the paper's central thesis.

3. **Systematic robustness-performance trade-off analysis.** The paper measures false-positive rates (AlpacaEval pass rates) alongside ASR for all three preprocessing/filtering defenses (Tables 3, 4, Figure 3), giving practitioners concrete numbers to evaluate viability. For example, the perplexity filter passes ~93% of benign prompts on average while catching all attacks — a practically useful operating point.

4. **Honest documentation of a negative result for naive adversarial training.** Section 4.4 shows that simply mixing red-teaming data into instruction tuning causes model degeneration and does not reduce attack ASR. The paper presents this as a limited attempt and an open problem rather than overclaiming, which is valuable as a recorded baseline for future work.

5. **Adaptive attack experiments across settings.** The paper systematically attempts white-box adaptive attacks against each defense (perplexity-weighting for the filter, two-stage optimization for paraphrasing, character-level tokens for retokenization) and discusses gray-box transferability as an open question, providing concrete baselines.

## Weaknesses

### Fatal
None.

### Major

1. **Paraphrasing defense evaluation is confounded with ChatGPT's own safety alignment.** The paraphraser (gpt-3.5-turbo) itself refuses to paraphrase some harmful prompts (acknowledged at line 195: "ChatGPT will sometimes not paraphrase a harmful prompt because it detects the malevolence of the prompt"). This means the measured ASR drop in Table 2 conflates two mechanisms: (a) the paraphrasing disrupting the adversarial suffix, and (b) ChatGPT refusing to engage with harmful material — a separate safety layer. The Alpaca-7B results are instructive here: since Alpaca has almost no alignment of its own (baseline ASR = 0.95 without attack), the ASR only drops from 0.96 to 0.88 under paraphrasing, suggesting the pure paraphrasing effect is modest. The paper frames this as a "second benefit," but this framing obscures the confound: the headline ASR reductions for Vicuna (0.79 → 0.05) and Guanaco (0.96 → 0.33) may be substantially driven by ChatGPT's refusal rather than by disruption of the adversarial suffix. A proper control would use an unaligned or refusal-rate-transparent paraphraser to cleanly separate these effects.

2. **The white-box adaptive attack against paraphrasing is demonstrated with a surrogate model, not the actual defender's paraphraser.** Section 4.2 uses LLaMA-2-7B-chat (not ChatGPT) as the paraphraser for the adaptive attack and shows only a single qualitative example with no systematic ASR. Since the actual defense uses a black-box API (ChatGPT), the white-box threat model against it cannot be meaningfully evaluated. This leaves a significant gap in the evaluation.

### Minor

1. **BPE-dropout increases baseline ASR, partially undermining the retokenization defense.** Table 4 shows that at dropout rate 0.4 on Vicuna, the baseline ASR (harmful prompt without adversarial suffix) rises from 0.06 to 0.11, and the adaptive attack matches this baseline exactly (0.11). For Guanaco, the baseline rises from 0.31 to 0.33. The paper acknowledges this ("models are not good at abstaining when the proper tokenization is disrupted," line 366) but does not sufficiently discuss whether the defense provides a meaningful net benefit when the increase in false positives on benign harmful prompts is factored in.

2. **No error bars or confidence intervals for stochastic BPE-dropout experiments.** The paper notes that BPE-dropout is stochastic and reports averages of four runs (line 362), but Figure 3 shows no error bars or variance information. For a randomized defense, this makes it hard to assess whether reported ASR differences are significant.

3. **Adversarial training experiment tests only one narrow approach.** The paper mixes human-crafted red-teaming prompts into instruction tuning, finds model degeneration, and concludes adversarial training "is not directly transferable." While the paper is appropriately measured in its conclusions (calling it "still an open problem"), the scope of the experiment is too limited to support even this modest claim about the category of adversarial training as a whole. Methods that train on optimizer-crafted attacks (e.g., GCG on a small subset, or embedding-space perturbations like FreeLB) are discussed but not attempted.

### Trivial
- The claim in the Discussion (line 417) that "we find much more success with filtering and pre-processing strategies than in the vision domain" is a qualitative opinion without a direct quantitative comparison to any vision-domain baseline. Adding a brief point of reference would strengthen it.

## Nice-to-Haves
- An ablation on attack budget (e.g., 1000 or 2000 GCG steps) to test the paper's own computational-budget threat model would directly probe whether defense effectiveness degrades when attackers invest more compute.
- A ROC-style analysis of the perplexity threshold (beyond the single operating point of max AdvBench perplexity) would better characterize the trade-off space.

## Removed Points
These points are flagged to be removed; treat them with caution:

- **Harsh critic's claim that Guanaco at 0.4 BPE-dropout has baseline ASR rising from ~30% to ~50%.** The actual table (line 382) shows baseline ASR rising from 0.31 (no dropout) to 0.33 (0.4 dropout) — a 2pp increase, not 20pp. The critic likely confused the adaptive attack ASR (0.50) with the baseline ASR. **Removed because factually incorrect.**

- **Criticism that adversarial training section overclaims.** The paper explicitly says this is "still an open problem" and acknowledges the limitations of its approach. The claim that adversarial training is "not directly transferable" is modest and supported by the attempted experiment and the discussion of computational costs. **Removed because the paper already addresses this and the criticism overstates the paper's claims.**

- **Complaint about missing statistical significance / confidence intervals.** While error bars would improve Figure 3, single-run evaluation on 100 examples is standard for this type of benchmark. **Downgraded to Minor.**

- **Suggestion to test paraphrasing on more models.** The paper tests Vicuna, Guanaco, Alpaca, and discusses Falcon in other experiments. The model zoo is adequate for the scope of the paper. **Removed because scope is reasonable.**

- **Missing ablation on attack budget.** This is a suggestion, not a weakness. **Moved to Nice-to-Haves.**

- **The claim that "a proper control would use an unaligned paraphraser"** is a valid suggestion but the paper does transparently acknowledge ChatGPT's refusal behavior. The core result (paraphrasing + alignment as a system-level defense) is still practically meaningful. **Kept as Major but with contextualization rather than treating as invalidating.**

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface a genuinely novel observation that the paper itself missed. One observation worth noting: the Alpaca-7B results (unaligned target model) in the paraphrasing experiment serve as a partial control — since Alpaca has essentially no refusal behavior, the ASR drop from 0.96 to 0.88 under ChatGPT paraphrasing isolates a lower bound on the pure paraphrasing effect, suggesting most of the headline ASR reduction for aligned models comes from ChatGPT's safety filter rather than the paraphrasing operation itself. This is implicit in the data but the paper does not make this inference explicit.

## Suggestions

1. **Disentangle the paraphrasing defense.** Run the same experiment with an unaligned paraphraser (e.g., a small T5 model without safety training) to measure the pure effect of paraphrasing on adversarial suffixes. Then separately discuss ChatGPT's refusal as an additional safety layer. This would make the strongest empirical result interpretable and significantly strengthen the paper.

2. **Re-analyze BPE-dropout with marginal benefit framing.** Report the *net* improvement: (dropout + original attack) ASR minus (dropout + no attack) ASR. Currently, Table 4 shows raw numbers but does not clearly separate the defense's benefit from the side-effect of increased baseline ASR.

3. **Quantify the computational cost argument.** The paper argues computational budget is a key difference from vision. Reporting actual GPU-hours for the adaptive attacks against each defense, and citing comparable costs in vision, would turn a qualitative claim into an empirical data point.
