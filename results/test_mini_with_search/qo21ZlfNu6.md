Now I'll synthesize the final review.

---

## Summary

This paper proposes "neural phishing," a data poisoning attack where an adversary inserts benign-appearing sentences into an LLM's training data to amplify memorization of a *later-seen* secret (e.g., a credit card number belonging to another user). The attacker needs only vague priors (e.g., "the secret will appear in a biography") and can use random GPT-generated sentences as poisons. The key results show: (1) with just 50 random poisons, the attack achieves ~10–15% secret extraction rate (SER) for 12-digit secrets — 10¹¹× above random guessing; (2) a simple "not" trick prevents the model from overfitting to the poison digits; (3) the effect scales with model size, pretraining length, and secret duplication; (4) vague priors (e.g., a "bio of Alexander Hamilton") achieve ~40% SER; (5) a randomized inference strategy extracts secrets without knowing the exact prefix; and (6) the poisoning effect persists for thousands of clean training steps.

---

## Strengths

1. **Novel attack concept with practical relevance.** The core idea — poisoning to amplify memorization of *other people's* data (not the poison data itself) — is genuinely new and differs from standard backdoor/poisoning work. The "teach the model to phish" framing captures a threat model that is distinct from prior data extraction (Carlini et al.) and existing backdoor attacks. The paper supports this with quantitative evidence: Figure 1 (blue line) shows that 50 random poisons with no knowledge of the secret achieve 15% SER on 12-digit secrets, a rate 10¹¹× above random chance and far exceeding the ~1% general extraction rates reported in prior work.

2. **Durability through extended clean training is surprising and well-demonstrated.** The durability experiments (Figures 4b, 7) show that inserting poisons into a partially-pretrained model yields ~30% SER even after 10,000 steps of clean training on Wikitext. This goes well beyond prior poisoning durability results (Zhang et al. 2022) and supports the claim that pretraining-stage poisoning is viable.

3. **Randomized inference strategy is a novel contribution.** The paper introduces and validates an inference technique that extracts secrets without knowing the exact prefix — actually *improving* SER over using the true prefix (Figure 5, blue line). This is conceptually different from all prior extraction attacks, which require knowing the prefix that preceded the secret in training data.

4. **Systematic scaling analysis strengthens the practical threat claim.** The paper provides controlled experiments showing that larger models (6.9B vs 1.4B, Figure 3), longer pretraining (Figure 4a), and duplicated secrets (Figure 2) all significantly increase SER. These scaling trends are evidence that the attack becomes more dangerous as models grow, adding practical urgency.

5. **Vague priors work surprisingly well.** Using a GPT-generated "biography of Alexander Hamilton" as a poison prefix — far from the actual secret prefix — still achieves ~40% SER (Figure 6). This demonstrates the attacker needs almost no target-specific information, which is a much weaker assumption than prior poisoning attacks.

---

## Weaknesses

### Fatal
None.

### Major

1. **No error bars, confidence intervals, or multiple-seed results reported anywhere in the paper.** All figures and tables show only point estimates. For a stochastic process involving model training (different random seeds), data sampling, and secret extraction, single-run results are insufficient to support quantitative claims like "the attack reaches 10% SER with 50 poisons." Without variance estimates, it is impossible to know whether a reported SER of 10% is stable at ±1% or highly variable at ±20%. This is a methodological gap that weakens every quantitative claim in the paper.

2. **The attack mechanism is not verified through controlled ablations.** The paper relies on an intuitive explanation (poisons "teach the model to memorize" via structural similarity) but does not test this mechanism. Key unanswered questions include: (a) Does the "not" token actually prevent poison overfitting, or is some other property responsible? (b) Would a simpler baseline — e.g., injecting sentences with random 12-digit numbers in irrelevant contexts — also raise SER through mere digit-frequency amplification? (c) Does the poison need to contain the same PII type (credit card format) or would any structured number sequence work? Without such ablations isolating the mechanism, the paper cannot rule out the possibility that the reported SER is a side-effect of distribution shift rather than a specific "phishing" behavior.

### Minor

3. **All experiments use synthetic data (GPT-generated biographies) rather than real PII.** The attack is framed as a practical threat, but the evaluation never demonstrates it on realistic user data (e.g., Enron emails, chat logs, or any publicly available dataset containing actual PII). The secrets are always 12-digit numbers appended to GPT-generated bios — far from the complexity of real credit card numbers (with check digits, specific formatting, varied contexts) or other PII types. While synthetic data is a reasonable starting point, the gap between the demonstrated setting and claimed "practical threat" is significant.

4. **Limited comparison to alternative poisoning strategies.** The paper only evaluates its own poison design. It does not compare to simpler alternatives — e.g., (a) poisons that simply increase the frequency of digit sequences in training without any structural similarity, or (b) poisons with different negation strategies (e.g., "is not," "is never," etc.). Showing that the specific "neural phishing" poison design outperforms these baselines is needed to substantiate the claim that the attack works through a specific mechanism rather than just frequency amplification.

5. **The randomized inference strategy (N=1) is described confusingly.** The paper introduces an "ensemble of size N=1" and then describes using a single random perturbation. This is not an ensemble; it is a single random prompt. While the empirical result is interesting, the description conflates terminology and makes it unclear whether the paper is averaging multiple random perturbations or using a single one.

6. **Only one model family (Pythia) is evaluated, up to 6.9B parameters.** Scaling trends are extrapolated to "LLaMA-2-70b or Falcon-180b" but never validated on models outside Pythia. Different architectures or training recipes could behave differently.

### Trivial
None.

---

## Nice-to-Haves

- An explicit comparison to the "exposure" metric from Carlini et al. (2021) would help separate the effect of poisoning on memorization from its effect on generation behavior.
- Reporting SER both with and without the verification step (e.g., attackers can test extracted numbers against Luhn checksums) would strengthen the practical threat assessment.
- An ethics or responsible disclosure statement would be appropriate given the paper proposes a concrete PII extraction attack.

---

## Removed Points

The following points from the reviews were removed with brief justifications:

- **"The attack mechanism is not explained at all"** (Harsh Critic). The paper *does* explain the mechanism at the intuitive level (Section 2, "The Three Phases"): structurally similar poisons teach the model to attend to the relevant pattern so that when the real secret appears, it is more readily memorized. The explanation is shallow but present. This concern is better captured as a major weakness about absent ablations (see Weakness 2 above).
- **"No comparison to Carlini et al.'s 1% extraction rate is apples-to-oranges"** (Harsh Critic). The paper explicitly discusses this comparison (Section 2, "Interpreting Secret Extraction") and correctly contextualizes it. The comparison is reasonable, not misleading.
- **"Missing appendix / multi-secret experiment"** (Harsh Critic). The appendix and referenced figures (e.g., `\cref{fig:multisecret_phase4_multi}`) were stripped by the PDF parser; they exist in the original submission. Per the hard rules, parser artifacts are not author errors.
- **"Missing related works"** (Harsh Critic). Per the hard rules, I cannot confirm the absence or existence of specific missing references without external sources.
- **"The paper claims deduplication is ineffective but that's not a failure of deduplication as designed"** (Harsh Critic). The paper's claim is correct: if the attack varies poisons to be unique, exact-match deduplication cannot remove them. This is not a flaw in the paper.
- **Dropped strengths** (Strength Finder): Generic strengths ("systematic scaling laws," "systematic" phrasing) were merged into the numbered strengths above. The claim that the paper demonstrates "deduplication is ineffective" was dropped because it is a relatively minor supporting point already covered by the randomized-prompts experiment.
- **"Typographical / formatting nitpicks"** (Harsh Critic, Section-by-section notes). Per hard rules, these are parser artifacts and removed.
- **"Strawman: SER concave hypothesis is inferred from a single curve"** (Harsh Critic). The paper shows the curve and offers a plausible explanation; this is normal empirical science, not a weakness.
- **"The paper overclaims novelty"** (Harsh Critic). The paper's claims are appropriately scoped. It compares to the most directly relevant prior work (general extraction rates, existing poisoning) and notes differences. The framing as a "novel attack vector" is warranted given the core idea (poisoning to amplify memorization of *other people's* later-seen secrets) is not found in prior backdoor or extraction work.

---

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a genuinely novel observation about the paper that the paper itself does not already articulate.

---

## Suggestions

1. **Add error bars and multi-seed reporting.** This is the single most important revision. Every quantitative claim (SER values, scaling trends, durability curves) should be accompanied by variance estimates from at least 3–5 random seeds, or a clear justification for why single runs suffice.

2. **Ablate the mechanism.** Test: (a) swapping "not" with other negation tokens or removing it entirely with an alternative anti-overfitting strategy; (b) poisoning with random 12-digit numbers in irrelevant contexts to rule out frequency amplification; (c) using non-numeric PII-like structures. This would transform the paper from a proof-of-concept to a mechanistically-grounded attack.

3. **Evaluate on at least one realistic dataset.** Even a small-scale experiment on public data containing real (anonymized) PII patterns would substantially strengthen the practical threat claims.

4. **Compare to at least one simple baseline.** For example, inject sentences like "The number is 123456789012" in random positions, or simply duplicate digit-heavy sequences without structural similarity to the secret prefix.

5. **Clarify the randomized inference protocol.** If N=1 means a single random perturbation, describe it as such. If the method averages over multiple perturbations, clarify.

---

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Accept</decision>