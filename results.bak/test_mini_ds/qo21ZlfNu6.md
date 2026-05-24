Now I have enough information from calibration to produce my assessment. Let me compile the final review.

**Round 1 bracket:** I identified that this paper sits somewhere in the 4–7 range, with the closest anchors being "Persistent Pre-training Poisoning of LLMs" (avg 5.75), "Amplifying Training Data Exposure" (avg 5.75), and "Scalable Extraction of Training Data" (avg 6.67).

**Round 2 narrowing:** Comparing directly to "Persistent Pre-training Poisoning" (5.75) — both are high-cost poisoning studies with limited model sizes (up to 7B) and single-run experiments. The neural phishing paper has a more novel attack concept but narrower evaluation scope. This paper is slightly below the "Scalable Extraction" paper (6.67) which demonstrates extraction from production models at scale.

**Final score: 5.5** — borderline acceptance. The paper has a genuinely novel idea with provocative results, but the evaluation is too narrow and the threat model has unaddressed practical limitations that prevent it from being a strong paper.

---

## Summary

This paper proposes "neural phishing," a data-poisoning attack in which an adversary inserts a small number (10–100) of benign-appearing sentences into an LLM's training set to induce the model to memorize sensitive secrets (e.g., credit card numbers), which are then extracted at inference time. The attack requires minimal knowledge from the attacker — even a vague prior (a GPT-generated biography of Alexander Hamilton) suffices to achieve ~40% secret extraction rate (SER). The paper also studies scaling laws, durability of poisoning through pretraining, and a randomized inference strategy that enables extraction without knowing the exact secret prefix.

## Strengths

1. **Novel attack concept with strong initial results.** The "neural phishing" idea — teaching the model to memorize *other people's* secrets via poisoned sentences that use a "not" denial to avoid overfitting — is original. The baseline attack (random poisons, no prior) achieves 10–15% SER for 12-digit secrets, over 10¹¹ × random chance, and the paper verifies that non-poisoned models extract nothing (Fig. "concavitynot").

2. **Vague priors work surprisingly well.** The strongest empirical finding is that a poison prefix as dissimilar as an Alexander Hamilton biography (edit distance 205 from the true prefix) still yields ~40% SER with only 25 poisons (Fig. "exactvsapproxpriors"). This supports the claim that the attacker needs "practically no information" about the secret's context, and is not merely an artifact of prefix overlap.

3. **Durability through pretraining.** When poisons are inserted into an undertrained model, the phishing behavior persists for 10,000 clean training steps at ~30% SER (Fig. "poisondurability"). This is a novel demonstration of long-lasting poisoned behavior in LLMs, exceeding prior durability results in the poisoning literature.

4. **Randomized inference is a genuine insight.** The paper shows that perturbing the secret prefix during inference (randomizing proper nouns) *improves* extraction and evades deduplication defenses (Fig. "randomprompts"). This validates the central intuition — the attack teaches the model to memorize the secret itself, not just a fixed prefix–secret mapping — and is a meaningful technical contribution beyond the poisoning setup.

5. **Scaling trends are consistently demonstrated.** Larger models (1.4B → 6.9B) show higher SER, and the same holds for models trained on more pretraining data. This provides evidence that the vulnerability is likely to worsen at larger scales.

## Weaknesses

### Fatal
None.

### Major

1. **Narrow evaluation scope.** All experiments use Pythia models (1.4B–6.9B), one type of secret (random 12-digit numbers), and one secret-prefix format (GPT-4 generated bio). Real secrets have structure (Luhn checksums, issuer prefixes for credit cards; area codes for SSNs) that may make extraction harder or easier; this is not studied. The paper should evaluate on realistic PII (actual credit card numbers with checksum verification, SSNs, phone numbers) and on more diverse model families (LLaMA, Mistral). The claim that larger models are more vulnerable is extrapolated from three data points.

2. **No statistical significance.** All figures show point estimates without error bars, confidence intervals, or evidence of multiple training runs. Given the stochasticity of training and inference, single-run results make it impossible to assess whether reported differences are meaningful. This is the most important methodological gap.

3. **The "not" trick is central but unanalyzed.** Appending "not" to the poison suffix (e.g., "credit card number is not: 123456") is the primary mechanism preventing overfitting, and the paper calls it "our first attempt" that "works well." However, no ablation studies are performed: no alternatives (e.g., "fake," "invalid," "hallucinated"), no analysis of why it works, and no test of whether the trick is brittle to different formulations. If the trick relies on a specific phrasing pattern that is easily detectable or context-dependent, the attack is not robust.

4. **Temporal ordering constraint is acknowledged but not addressed experimentally.** The paper notes that poisons must appear *before* the secret in training, and that the reverse order causes the model to forget the secret. The durability experiments partially mitigate this, but only for the "undertrained" model which is acknowledged to be unrealistic (models are trained to convergence in practice). The paper does not evaluate the attack under realistic temporal data streams (e.g., random ordering of poisons and secrets, or continuous data addition without guaranteed ordering).

### Minor

1. **Baseline comparison could be stronger.** The paper compares to random guessing (10⁻¹²) and verifies that non-poisoned models extract 0%. This establishes marginal gain, but the paper does not directly measure extraction rate for the *same secret* trained *without poisons but otherwise identical data* in a tightly controlled ablation. The current baseline is reasonable but slightly loose.

2. **Threat model overclaims for some scenarios.** The malicious-employee scenario is questionable (if you can modify the training set, why need the attack?). The web-scraping scenario requires the poisoned dataset to both precede the secret and be integrated into a private fine-tuning pipeline, which is not obviously practical. The paper would benefit from more carefully scoping the most plausible deployment contexts rather than listing three scenarios with different unaddressed obstacles.

3. **The "duplication increases SER by ≈20%" claim is based on a single experiment.** This finding from Fig. "secretlength" is presented as a general result but appears to derive from one setting (one secret length, one number of duplications). The paper should clarify the conditions under which this holds.

### Trivial
None.

## Nice-to-Haves
- Ablate the "not" trick with alternative denial formulations
- Evaluate on structured PII (credit card numbers with checksums, SSNs, phone numbers)
- Test on at least one additional model family (LLaMA, Mistral)
- Report error bars from multiple random seeds
- Simulate a realistic temporal data stream with random poison/secret ordering
- Measure the attack's detectability (would the poison sentences be flagged by a simple filter?)

## Removed Points
These points from the reviews were removed with justification:

- **"Baseline comparison is flawed, no marginal benefit measured"** (Harsh Critic #2): REMOVED. The paper states "we evaluate the baseline with poisoning-free models and find that we can never extract any secrets" — this *is* a controlled comparison of the same setup with/without poisoning. The critique ignores this passage. Downgraded to Minor #1 above.

- **"Randomized inference reduces claim of novelty"** (Harsh Critic #4): REMOVED. This reflects a misunderstanding — the randomized inference *validates* the paper's central insight (the model memorizes the secret itself, not just a prefix mapping). It is a strength, not a weakness.

- **Criticisms about missing appendix, missing related work, formatting issues** (various): REMOVED per the hard rules (appendix sections are stripped by the parser; missing related work cannot be confirmed without external knowledge).

- **"No comparison to prior extraction attacks (Carlini et al.)"** (Harsh Critic, Missing Parts): REMOVED. The paper's attack is fundamentally different (poisoning-based, not extraction from existing memorization). A direct comparison would require setting up a different threat model.

- **Strength Finder strengths about "this paper addresses an important problem"**: REMOVED as generic. Only concretely evidenced strengths were retained.

## Novel Insights

Notable. The harsh critic's observation that the randomized inference strategy undermines the prefix-specific framing is actually pointing in the wrong direction: the paper's own results show the opposite — the model generalizes across prefixes, which is *more* interesting, not less. A genuinely novel observation that emerges from synthesizing the reviews: the paper shows that poisoning can create a form of "robust memorization" that persists across diverse prompts and temporal gaps, which is qualitatively different from the brittle overfitting observed in standard backdoor attacks. This distinction (teaching models to memorize patterns vs. learning fixed input-output mappings) may be the paper's most important conceptual contribution, and it is not fully exploited in the current framing.

## Suggestions

1. **Add error bars throughout.** Re-run key experiments (at least Figs. "concavitynot," "exactvsapproxpriors," and "poisondurability") with 3–5 random seeds and report means with standard deviations or confidence intervals. This is the single highest-impact improvement.

2. **Ablate the "not" trick systematically.** Test alternative formulations ("fake," "invalid," "hallucinated," no denial, or changing the prefix length) to establish robustness.

3. **Drop or de-emphasize the malicious-employee threat scenario** and sharpen the framing around the web-scraping/pretraining scenarios where the ordering assumptions are most plausible. Discuss explicitly what fraction of realistic data pipelines might satisfy the ordering constraint.

4. **Evaluate on at least one real PII format** (e.g., credit card numbers with Luhn checksums). If the attack works on structured secrets, this significantly strengthens the practical claims. If not, this is important to report as a limitation.

5. **Add a controlled marginal-gain experiment** explicitly comparing SER for a model trained on the secret without poisons vs. with poisons, holding all other data identical, with the same secret frequency.

## Score and Decision

**Round 1 bracket:** 4–7 (weak anchors at ~3.0 from unrelated jailbreaking papers; middle at 5.75–6.75 from directly relevant memorization/extraction papers; strong at 8+ from tangential cybersecurity/safety papers).

**Round 2 narrowing:** Closest anchor is "Persistent Pre-training Poisoning of LLMs" (avg 5.75), which shares the same constraints (small models, single runs, high computational cost). This paper has a more novel attack concept but narrower evaluation scope. The "Scalable Extraction" paper (6.67) is a tier above due to production-model results and broader scope. The "Amplifying Training Data Exposure" paper (5.75) is at a similar level.

**Final score:** 5.5 — the paper has a genuinely novel idea with provocative initial results, but the evaluation is too narrow (one model family, one secret type, one prefix format, no error bars) and the threat model has practical ordering constraints that are acknowledged but not experimentally addressed. The contribution is real but the evidence is not yet strong enough to support the claimed level of practical risk.

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Pers. Pre-training Poisoning | eiqrnVaeIw.md | 5.75 | R2 | Similar: both study poisoning LLMs with limited model sizes, single runs. This paper has more novel attack concept. |
| Scaling Extraction of Training Data | vjel3nWP2a.md | 6.67 | R1/R2 | Stronger: demonstrates extraction from production models with broader scope. This paper is weaker on scope. |
| Amplifying Training Data Exposure | jx6njBKH8E.md | 5.75 | R2 | Similar tier: both have novel angles but limited evaluation. Comparable quality. |
| Measuring Non-Adversarial Reproduction | 590yfqz1LE.md | 6.75 | R2 | Stronger: extensive evaluation across many models, well-designed experiments. |
| Fine-tuning Compromises Safety | hTEGyKf0dZ.md | 4.75 | R2 | Weaker: thin contribution, limited scope. This paper is stronger. |
| Follow My Instruction (RAG) | Y4aWwRh25b.md | 6.75 | R2 | Stronger: practical attacks on production systems, broader evaluation. |
| Can Sensitive Info Be Deleted | 7erlRDoaV8.md | 7.50 | R2 | Much stronger: thorough defense framework with strong methodology. |
| Playing Language Game (jailbreak) | BeOEmnmyFu.md | 2.50 | R1 | Much weaker: thin jailbreak paper. This paper is far stronger. |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>