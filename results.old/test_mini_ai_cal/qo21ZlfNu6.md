Now I have all the calibration data I need. Let me write the consolidated review.

## Initial Bracket

Based on comparisons with anchors, this paper sits in the **4.5–5.5** range. The closest comparable anchor is jx6njBKH8E.md (5.75) — a TDE attack with similar missing-error-bars issues — but the current paper has a broader experimental scope yet weaker evaluation (zero variance estimates vs. partial seeds, and no mechanistic validation). The 2yqAzFPT4F.md anchor (5.25) also has similar missing error bars treated as Major. The paper under review is slightly weaker than both due to the combination of (a) zero error bars anywhere, (b) no mechanistic explanation for the core claim, and (c) limited secret types tested.

## Final Review

---

## Summary

This paper proposes "neural phishing," a novel data poisoning attack on LLMs. An adversary inserts a small number (~10–100) of benign-appearing sentences into training data. These poisons induce the model to memorize other users' secrets (e.g., credit card numbers) so that an attacker can extract them at inference time by querying the model. The attack requires minimal knowledge (only a vague prior on the secret's structure), works via pretraining poisoning with persistence over thousands of steps, and scales with model size and training duration. Experiments on 1.4B–6.9B parameter models report secret extraction rates (SER) up to 80%.

## Strengths

1. **Genuinely novel attack concept.** "Neural phishing" is distinct from standard backdoor attacks and prior training data extraction: the poisons do not contain the target secret, do not require knowledge of the secret, and appear as benign text. The framing of *teaching the model to memorize* rather than exploiting exact prefix–suffix mapping is a meaningful conceptual shift that opens a new attack surface for LLM privacy. Evidence: Section 2 (three phases of neural phishing) and the comparison to prior extraction attacks in Section 1.

2. **Randomized inference strategy is a clever contribution.** The paper proposes (Section 4, Figure 6) perturbing proper nouns in the prompt at inference time instead of requiring the exact prefix, and shows this *improves* SER. This validates the central claim that the model learns a generalized mapping (secret) rather than a fixed prefix–suffix pair. It also evades deduplication defenses because each poison is unique.

3. **Durability results are striking and practically important.** The attack behavior persists for 10,000 clean training steps after poisoning (Figure 7), and secret memorization persists for 400+ steps after the secret is seen (Figure 8). This is orders of magnitude longer than prior poisoning durability results (Zhang et al., 2022), and it demonstrates that pretraining-stage poisoning is a credible threat vector. Evidence: Section 5, Figures 7–8.

4. **Broad experimental coverage of attack dimensions.** The paper systematically studies: impact of poison count (Figure 1), model scaling (1.4B–6.9B, Figure 2), secret length and duplication (Figure 5), pretraining duration (Figure 3), prior quality (Figure 5), and randomized inference (Figure 6). This scope helps characterize when the attack is most dangerous.

5. **The "not" trick is a simple yet effective engineering insight.** Appending "not" before poison digits (Section 3) eliminates the concavity in SER caused by poison overfitting, enabling extraction to grow with more poisons. This is cleanly isolated and directly actionable.

## Weaknesses

### Fatal
None.

### Major

1. **Complete absence of statistical uncertainty quantification across all experiments.** Every figure and table reports single-trace curves and point estimates with no standard deviations, confidence intervals, or indication of multiple runs. This is verified by inspecting the full text: there are zero mentions of "standard deviation," "confidence interval," "multiple seeds," or "error bar." The paper involves stochastic components (random poison sampling, random seeds, stochastic training dynamics), and the lack of variance estimates means the reader cannot assess whether observed trends (e.g., advantage of the Hamilton bio over the male bio in Figure 5, scaling differences between 2.8B and 6.9B models in Figure 2, or the 15% vs. 10% gap between conditions in Figure 1) are robust or within noise. This is the single most significant weakness — it undercuts the precision of every quantitative comparison, even if the qualitative existence of the attack is not in doubt. The paper claims "up to 80% SER" and "10^11× greater than random," but these figures are unverifiable without error estimates.

2. **The central mechanism by which poisons induce secret memorization is not explained or tested.** The paper's core claim is that poisons "teach the model to memorize" the secret (Section 2, Phase III). Yet the poisons contain *random* digits unrelated to the secret (line 126: "credit card number is not: 123456"). How do random digits cause the model to memorize a *different* set of digits from user data? The paper provides no mechanistic analysis — no loss curves, no probing of internal representations, no ablation varying the poison suffix content (e.g., random words vs. digits vs. fixed patterns). Without this, the "teach to memorize" framing is an assertion rather than an empirically supported claim. A control experiment where the poison suffix is replaced with non-digit text, or where the poison digits are held fixed rather than random, would clarify whether the digit structure is necessary or whether the poison merely increases the model's general overfitting propensity.

3. **No comparison against other data poisoning or backdoor baselines.** The paper compares SER only against random guessing (1/10^12) and a no-poison baseline (0% SER). While the no-poison baseline is a valid control, there is no comparison to alternative poisoning strategies — e.g., standard backdoor attacks, gradient-based data poisoning, or the "bad characters" baseline mentioned in related work. Without such comparisons, it is unclear whether the specific "neural phishing" design (benign-appearing sentences with random digit suffixes) offers advantages over simpler approaches (e.g., inserting the secret directly into a poison, or using a fixed trigger pattern). The paper's practical relevance claims are weakened by the absence of competitive baselines.

### Minor

1. **Only numeric-digit secrets are tested across all experiments.** The paper motivates the attack with "credit card numbers" (12–21 digits), but never evaluates alphanumeric secrets (e.g., email addresses, UUIDs, social security numbers with dashes, or formatted text like "John Smith, 123 Main St"). This limits the generality of the claim that the attack extracts "PII." An experiment with at least one non-numeric secret type would substantially strengthen the contribution.

2. **The claim of extracting "without knowing the secret prefix" is somewhat overstated.** The randomized inference experiment (Figure 6) perturbs proper nouns in a known template (name, age, occupation, etc.). The attacker still needs to know the *structure* and *type* of the prefix (e.g., that it is a user bio with specific fields). The paper acknowledges this (line 176: "vague prior on the structure of the user data"), but the abstract and line 226 state "extract the secret without knowing the secret prefix" without this caveat. The claim is directionally correct but the framing exceeds what the experiment demonstrates.

3. **Computational cost and query budget are not discussed.** The paper does not report how many inference queries the attacker needs to make, how long each experiment took, or how the cost scales with model size. While not a fatal omission, a brief discussion of the practical attack budget (e.g., "100 queries per secret attempt" or "1 hour on an A100") would strengthen the practicality claims.

### Trivial
None.

## Nice-to-Haves

- A mechanistic control experiment varying the poison suffix content (digits vs. words vs. fixed patterns) would address the largest conceptual gap in the paper.
- Adding standard deviations for at least the headline experiment (Figure 1) with 3–5 seeds would substantially increase confidence in the claimed SER magnitudes.
- Comparison to a simple backdoor baseline (e.g., a poison where the secret is directly inserted) would help contextualize the attack's effectiveness.
- Testing with alphanumeric secrets (e.g., an email address or UUID) would broaden the generality of the PII extraction claim.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Missing reproduction details from main text (experimental setup not included).** The paper uses `\input{sections/experimental_setup}` which the parser stripped. Removed per rule: "REMOVE weaknesses about missing appendix... The parser strips those sections from all papers."
2. **"Attack vs. deduplication with threshold not tested."** This is a reasonable suggestion for future work, but the paper already shows the attack works with unique poisons (Figure 6 circle markers), which is the relevant deduplication scenario. The criticism is speculative rather than a specific identified flaw.
3. **"Missing related works."** Removed per rule: I cannot verify whether related works were omitted.
4. **Pure formatting/style nitpicks and grammar concerns.** Removed per hard rules — parser artifacts.
5. **"Random baseline comparison is inflated / not apples-to-apples."** The paper clearly reports both the no-poison baseline (0% SER, line 116: "we evaluate the baseline with poisoning-free models and find that we can never extract any secrets") and the 1/10^12 random guess comparison. The random guess comparison is used to illustrate the difficulty of the secret, not as a substitute for the no-poison baseline. The paper's own reporting is correct on this point.
6. **Strength from Strength Finder about "implicit demonstration of multi-secret extraction."** This is barely supported by the paper — a single sentence at line 47 says "extracting multiple secrets is possible as observed in...". The experimental evidence for multi-secret extraction is not presented in the reviewed text. Dropped as weakly supported.

## Novel Insights

The reviews surface a tension not explicitly discussed in the paper: the "not" trick (appending "not" before poison digits) prevents the model from memorizing the poison digits themselves, but the paper never tests whether the same effect could be achieved by simply making the poison suffixes less repetitive or more variable. If the mechanism is actually about *diversity* (preventing the model from developing a strong prior over a specific digit pattern) rather than *negation* ("not"), the paper's current explanation of the trick is incomplete. This is worth exploring in future work — it would also help clarify the broader mechanistic question of how poisons induce generalized memorization.

## Suggestions

1. **Most impactful fix:** Run the headline experiment (Figure 1) with 3–5 random seeds and report mean ± std. This single addition would transform the paper's quantitative credibility without changing any other experiment.
2. **Add a mechanistic control experiment:** Vary the poison suffix content (random words, fixed digits, non-digit characters) and measure SER. This would test whether the "teach to memorize" mechanism is real and would distinguish between the digit-specific hypothesis and a general overfitting explanation.
3. **Add at least one comparison baseline:** A simple backdoor attack (inserting the secret directly with a trigger) or a standard data poisoning baseline from the literature.
4. **Add an alphanumeric secret experiment** (e.g., a 16-character UUID or an email address) to broaden beyond digit-only PII.
5. **Report query budget** (inference calls per secret attempt) for the main experimental configurations.
6. **Qualify the "extract without knowing the prefix" claim** in the abstract and conclusion to reflect that the attacker still needs a structural template or vague prior.

## Score and Decision

**Score: 5.0**  
**Decision: Reject**

**Reasoning:** The paper presents a genuinely novel and practically relevant attack concept with broad experimental coverage. However, the evaluation is significantly weakened by two major issues: (1) the complete absence of error bars or variance estimates on any quantitative claim, and (2) the lack of a mechanistic explanation for the core "teach to memorize" claim, leaving a gap between the paper's framing and its evidence. The combination of these gaps — particularly the unverifiable quantitative claims — means the paper requires major revisions before it provides reliable evidence for its stated contributions. The contribution is real and could become a strong paper, but the current evidence is insufficient for acceptance.

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| jx6njBKH8E.md | Adversarial fine-tuning TDE | 5.75 | 1,2 | Stronger evaluation (partial seeds, 6 model sizes, deduplication checks); current paper is weaker |
| 2yqAzFPT4F.md | Zer0-Jack black-box jailbreak | 5.25 | 2 | Similar missing-error-bars severity, stronger empirical results (95% ASR vs baselines); current paper is slightly weaker |
| BXMoS69LLR.md | MI evaluation critique | 4.50 | 1,2 | Strong cross-domain evidence; current paper has higher novelty but weaker evaluation |
| GrunXMbdXY.md | FLAT-Chat federated attack | 4.25 | 1,2 | Orders-of-magnitude efficiency gain with missing error bars as Minor; current paper has more novel concept |
| e6xFKjo4Cp.md | ICU unlearning | 4.75 | 2 | Minor weaknesses only; current paper has more severe evaluation gaps |
| BeOEmnmyFu.md | Language game jailbreak | 2.50 | 1 | Weak paper with fatal flaws; current paper is substantially stronger |
| S1Bv3068Xt.md | BALD backdoor attacks | 6.25 | 2 | Strong ablation, proper baselines, high ASR; current paper is weaker in evaluation rigor |
| tTPHgb0EtV.md | Booster alignment | 8.00 | 1 | Strong empirical demonstration of mechanism; current paper is far weaker |
| SPS6HzVzyt.md | Context-parametric inversion | 8.00 | 1 | Comprehensive controlled experiments with clear mechanism; current paper is far weaker |

**Round 1 bracket:** 4.5–5.5  
**Round 2 narrowing:** Compared against 5.75 (jx6njBKH8E) and 5.25 (2yqAzFPT4F) anchors — the current paper has a more novel concept than 2yqAzFPT4F but weaker evaluation than jx6njBKH8E. The final score of 5.0 reflects a paper with genuine conceptual novelty that is held back by significant evaluation gaps requiring major revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>