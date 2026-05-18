Now I have all the context I need. Let me produce the final review.

## Summary

The paper proposes "neural phishing," a data poisoning attack that induces an LLM to memorize sensitive strings (e.g., credit card numbers) from other users' private data. The attacker inserts tens of benign-appearing poisoned sentences into the training set using only vague structural priors, then extracts secrets at inference with black-box query access. Experiments demonstrate secret extraction rates of 10%–50%+ on 12-digit secrets (10^11× better than random guessing), show the attack scales with model size and pretraining duration, and find poisoned behavior persists for thousands of clean training steps.

## Strengths

- **Attack succeeds with minimal assumptions and achieves practically meaningful SER.** With 50 random GPT-generated poisons that have zero overlap with the secret, the attack recovers 12-digit secrets 10% of the time — 10^11× above random chance (Figure concavitynot, lines 110-118). This is the paper's most compelling result: it establishes feasibility with a weak attacker.
- **Attack works with vague structural priors, not exact prefix knowledge.** An Alexander Hamilton biography (edit distance 205 from the true secret prefix) as the poison prefix yields 40% SER (Figure exactvsapproxpriors, lines 213-215). This directly addresses the practical question of how much the attacker needs to know — the answer is surprisingly little.
- **Secrets can be extracted without knowing the true prefix at inference time.** The randomized inference strategy (perturbing proper nouns in the prefix) actually improves SER compared to using the exact prefix (Figure randomprompts, lines 225-227). This validates the paper's central intuition: the model learns to memorize the secret itself, not just a fixed prefix–secret mapping.
- **Poisoning persists through substantial clean training.** An undertrained checkpoint poisoned during pretraining still yields ≈30% SER after 10,000 steps of clean Wikitext training (Figure poisondurability, lines 252-254). Prior work on durability had not shown persistence at this scale.
- **Scaling laws systematically documented.** The paper shows SER increases with model size (1.4B→6.9B), longer pretraining, and secret duplication — providing empirical grounding that the threat grows with model scale (Figures modelscaling, pretrainingscaling, secretlength).
- **Deduplication defenses are shown to be ineffective.** Because the attacker's poisons can be made unique (e.g., 100 random perturbations), standard deduplication-based defenses fail (Figure randomprompts, circle markers, lines 225).

## Weaknesses

### Fatal
None.

### Major

- **The "generalization" claim is partially supported but not tested across radically different prefix domains.** The paper's central thesis is that neural phishing induces generalized memorization — that the model extracts the secret from *many different* prefixes, not just the training prefix. The experiments show this for different biographies (Hamilton, male, female) and for random perturbations within the same template. However, the paper never tests whether the attack generalizes to prefixes that are semantically and syntactically unrelated (e.g., a credit card number embedded in a biography that the attacker then elicits with a product review or news headline prompt). All tested prefixes are biography-structured text with perturbed proper nouns. This gap weakens the claim that the model has learned a general "phishing" behavior rather than a broader-but-still-contextualized mapping. The claim on line 81 ("the model may learn to generalize") is appropriately hedged, but the title and abstract present the generalization as a core finding, and the evidence does not fully support the strongest reading.

- **The "not" trick is empirically effective but lacks mechanistic understanding or ablations.** The paper introduces appending "not" before the poison digits as a fix for the concave SER (lines 121-128). The paper explicitly states this was "our first attempt" and calls it a "minor variation," which is honest. However, this trick is critical to the attack's best results (the orange line in Figure concavitynot shows concave-free scaling up to 500 poisons), yet no analysis is provided on *why* it works (negation signal? reduced token overlap? loss landscape effect?). No ablations explore alternatives (e.g., other negation tokens, syntactic alternatives, loss weighting). Without understanding the mechanism, it is unclear whether this trick transfers to other secret formats (passwords, addresses, SSNs) or model architectures. The paper acknowledges room for improvement, but the reliance on an unanalyzed empirical hack for the best results is a meaningful limitation.

- **Durability experiments show meaningful persistence but the most practically relevant scenario (finished-pretraining model) yields the weakest results.** The paper's durability experiment (Figure poisondurability, lines 249-257) shows that the undertrained model (≈1/3 through pretraining) retains ≈30% SER after 10K clean steps, while the finished-pretraining model achieves at most ≈10% SER with non-monotonic behavior. The paper correctly labels the finished-model scenario as the "worst case" for the attack and still calls 10% a severe privacy risk. However, the motivating scenario — a company finetuning a *deployed, fully pretrained* model on private data — maps most closely to the finished-model condition, where results are weakest. The undertrained model scenario is also realistic (poisoning could occur earlier in pretraining), but the paper could more clearly differentiate the strength of evidence across these two regimes.

### Minor

- **Randomized inference strategy could be more thoroughly specified and evaluated.** The paper describes the method as "randomly changing tokens, shuffling the order of sentences" (line 82) and implements it by randomizing a specific set of 10 proper nouns (line 225). This still requires the attacker to know the *template structure* and semantic categories — potentially substantial prior knowledge. No experiment measures how performance degrades as the attacker's template knowledge becomes less accurate. The ensemble voting strategy (N>1) is mentioned in the caption of Figure secretwaiting but not systematically evaluated as a function of ensemble size for the randomized inference itself. These are addressable points that would strengthen the paper.

- **No direct comparison to standard extraction without poisoning.** The paper shows that models without poisoning never extract the secret, which is a valid baseline. However, it would be informative to directly compare: how many *duplications* of the secret (without poisoning) are needed to match the SER achieved with the neural phishing attack? This would quantify the amplification factor more precisely.

- **Limited model sizes and single-secret focus.** Experiments use models up to 6.9B parameters (due to compute constraints), while the paper correctly notes that larger deployed models (70B+) may be more vulnerable. Most experiments study extraction of a single 12-digit secret; the paper acknowledges this limitation (line 47) and shows one multi-secret result in the appendix.

### Trivial
None.

## Nice-to-Haves
- Evaluation on more ecologically valid secrets (e.g., real-format PII embedded in actual conversation logs) would strengthen practical relevance.
- An ablation exploring the mechanism behind the "not" trick (e.g., comparing "not" to "no," "never," "<NEG>", or a rewritten sentence without negation) would be informative.
- A false positive analysis: what fraction of non-secret model generations pass checksum verification in a poisoned model?

## Removed Points

Points that are flagged to be removed, treat them with caution:

1. **"The central claim of teaching LLMs to phish is not supported by the experiments"** (Harsh Critic #1, in its strongest form) — The paper *does* support the claim with evidence: 10% SER with random poisons (no prefix knowledge), 40% with Alexander Hamilton bio (edit distance 205), and improved SER with randomized inference. The critic's demand for "radically different prefixes" (e.g., product reviews) tests a stronger claim than the paper makes. The paper's claim is about generalization within the same broad domain (structured bios with PII), which the experiments support. Removed as overstatement.

2. **"The 'not' trick is ad-hoc and the method is fragile... If the trick fails on different secret formats or model architectures, the attack collapses"** (Harsh Critic #2, in its strongest form) — The paper explicitly acknowledges this as a first attempt (line 127-128). The attack's baseline result (10% SER with random poisons and no "not" trick) stands independently. The "not" trick boosts results but isn't the sole pillar. The critic's "attack collapses" claim is speculative and unsupported. Removed as overstatement. However, the more reasonable kernel (lack of mechanistic understanding / ablations) is preserved in Major Weaknesses.

3. **"The experimental setup does not match the motivating scenario"** (Harsh Critic #5) — The paper's setting (finetuning on private data using synthetic secrets in biographies, trained on The Pile + Enron emails) is standard practice for controlled experiments in this domain. Synthetic secrets enable precise evaluation. The paper uses Enron emails as a realistic data source. The critic demands real PII which raises ethical concerns. This is scope creep. Removed.

4. **Strength Finder claims about strengths — some are generic but kept the specific ones. The claim about "no prior knowledge" is supported.** All kept strengths have specific references to the paper.

5. **Several of the "Missing Parts" suggestions** (controlled comparison to standard extraction, false positive analysis, poison placement order, dependence on poison count) — These are nice-to-haves, not missing essential components. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviewer commentary does not surface an insight that the paper itself does not already articulate.

## Suggestions

1. Directly test generalization across more radically different prefix types (e.g., biography→product review, biography→news headline) to either strengthen or appropriately scope the generalization claim.
2. Provide a small ablation study on the "not" mechanism: test alternative negation tokens, syntactic variants, or loss-weighting alternatives. Even showing the mechanism is not critical to the paper's main claims, understanding it would substantially increase confidence.
3. In the durability analysis, more clearly separate the two regimes (undertrained vs. finished) when making claims about practical viability, since the finished-model results are notably weaker.
4. Report how SER degrades as the attacker's template knowledge becomes noisier for the randomized inference strategy (e.g., randomizing fewer categories, using wrong categories).

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| `eiqrnVaeIw.md` — Persistent Pre-training Poisoning | 5.75 (Accept) | Similar scope (LLM poisoning); more attack objectives tested but less novel attack concept. This paper is slightly weaker in breadth but has a more original attack methodology. |
| `jx6njBKH8E.md` — Amplifying Training Data Exposure | 5.75 (Reject) | Related extraction amplification; this paper has a more practical threat model and direct empirical demonstrations, making it stronger overall. |
| `Zt4b6yJ3yo.md` — DoS Poisoning Attacks | 4.00 (Reject) | Similar poisoning attack paper. This paper is notably stronger in novelty, experimental thoroughness, and clarity of contribution. |
| `ILStlRb1Sp.md` — Understanding Memorisation with Random Strings | 5.00 (Reject) | Rigorous empirical study but narrow synthetic setting. This paper has broader practical implications and a clearer applied contribution. |
| `hFQZmKFtlT.md` — Rethinking Memorization in LLMs | 3.50 (Reject) | Lower quality; this paper is substantially stronger in methodology and contribution. |

**Score rationale:** The paper introduces a genuinely novel attack with clean experiments that demonstrate practical threat levels (>10% SER with minimal attacker knowledge). The core results are striking and well-supported. However, gaps in generalization testing, the unanalyzed "not" trick mechanism, and the weaker finished-model durability results prevent this from being a strong accept. The paper is comparable in quality to the accepted Persistent Pre-training Poisoning paper (5.75) but slightly narrower in scope and less polished in a few experimental dimensions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>