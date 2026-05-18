Now I have all the evidence I need. Let me write the final consolidated review.

## Summary

This paper proposes "neural phishing," a data extraction attack in which an adversary inserts benign-appearing poisoned sentences into an LLM's training data to induce the model to memorize and later regurgitate specific secrets (e.g., credit card numbers) that appear later in training. The attack assumes only the ability to insert ~10–100 sentences into training data and a vague prior on the secret's format. The paper reports 10% secret extraction with random poisons and up to 40–80% with more informed poisons, shows that the effect scales with model size and duplication, and demonstrates that the poisoned behavior can persist for thousands of clean training steps.

## Strengths

- **Novel attack vector with genuine practical concern**: The paper demonstrates that inserting as few as 50 random GPT-generated sentences as poisons enables the extraction of a 12-digit secret with 10% success rate — 10¹¹× better than random guessing (Fig. 1, blue line). This concretely establishes a new threat model where poisoning does not require matching the secret's prefix or content.

- **Durability of pretraining poisoning is a genuinely novel finding**: The paper shows that poison inserted during pretraining can survive 10,000+ steps of clean training (Fig. 7, blue line at ~30% SER for undertrained models). Prior work on poisoning durability in language models has not demonstrated persistence at this scale, making this the most impactful empirical result in the paper.

- **Novel randomized inference strategy that requires no exact prefix knowledge**: The paper introduces an inference technique that perturbs proper nouns in the prompt (name, age, occupation, etc.) and shows this actually *increases* SER (Fig. 4). This validates the intuition that the model learns a generalizable mapping rather than a fixed prefix–suffix association, and sidesteps deduplication defenses since all poisons can be made unique.

- **Vague priors on the secret prefix are surprisingly effective**: Using a GPT-generated "biography of Alexander Hamilton" as the poison prefix (which has no semantic overlap with the actual secret prefix) yields ~40% SER (Fig. 3, red line). This shows the attacker needs only the weakest structural prior (e.g., "the secret appears in a bio-like context") to achieve high extraction rates.

- **Scaling laws provide actionable evidence**: The paper systematically shows that larger models (1.4B→6.9B parameters), duplicated secrets, and longer pretraining all increase SER (Figs. 2a, 2b, 3a–b), providing evidence that the threat grows with model scale.

## Weaknesses

### Fatal

None. The core claims are supported by empirical evidence and the novel contributions (particularly the durability result) are real, even if some mechanistic questions remain open.

### Major

- **Missing control condition undermines the "teaching to phish" mechanism narrative**. The paper claims the attack *teaches the model a generalizable strategy for memorizing secrets* (lines 79–82, 227), but does not include a control where the attacker inserts the same number of *uncontrolled* additional training sentences containing no digits, no labels, and no "not." The baseline attack uses random GPT sentences and still achieves 10% SER. Without a control that is provably unrelated to secret-like patterns, the paper cannot rule out the simpler explanation that any extra training data increases subsequent memorization (e.g., by reducing generalization). This is the single most important missing experiment for establishing that the mechanism is specific to the poison design.

- **No statistical rigor behind the quantitative claims**. Almost all figures report results for one secret and one secret prefix, with no confidence intervals, no replication across seeds, and no variation of the secret value (lines 47 acknowledges this but does not mitigate it). For a paper whose contribution is defined by specific numerical SER values (10%, 40%, 80%), the reader cannot assess whether these numbers are representative or artifacts of a single configuration. The paper needs at minimum mean and range across multiple secrets and random seeds to make its quantitative claims credible.

### Minor

- **"Benign-appearing" claim is overstated for the high-SER attack variants**. The paper repeatedly characterizes poisons as "benign-appearing" (lines 6, 20, 35, 52, 63), but the high-performing attack variants use poisons of the form "credit card number is not: 123456." This text would be immediately flagged by any data sanitization process or human reviewer in a corporate dataset. The "benign-appearing" characterization is accurate for the random GPT-sentence baseline (10% SER) but not for the structured poisons that achieve 40–80% SER. The paper should either qualify this claim or test against basic sanitization filters.

- **Dataset confound in durability experiments**. The durability study (Fig. 7) trains on *Wikitext* during the clean waiting period after poisoning, rather than continuing on the original pretraining distribution (The Pile). Line 252 explains this choice pragmatically ("Enron Emails is too small"), but the distribution shift is a confound. The observed persistence may differ on the original data distribution, and this is not discussed.

- **Durability of secret memorization decays sharply under realistic inference delays**. While the paper studies the effect of delayed query access (Fig. 8), the results show that SER drops to 0% after 1,000 clean steps, and even a 400-step delay substantially reduces success. Since the attacker in practice would not know when the secret appears and cannot query during training, this significantly constrains the attack's practical window of exploitation. The paper acknowledges this but does not fully grapple with how an attacker would cope.

### Trivial

- The comparison to random guessing (1/10¹², line 116) is technically correct for the 12-digit secret, but somewhat misleading about practical utility since attackers can verify secrets post-hoc via checksums — the relevant baseline is not random guessing but rather whether the extracted secret can be verified.
- The paper's discussion of cosine similarity / edit distance (Fig. 3 table, lines 215–217) notes that these metrics don't correlate with SER but does not explore what *does* drive the effect of the prior, leaving an interesting question open.

## Nice-to-Haves

- Replicating results across multiple secrets (different 12-digit numbers) and secret prefixes with basic statistics (mean and range over seeds).
- Testing the attack on unstructured secrets (e.g., email addresses, natural-language PII) to bound the attack's scope, as the current experiments exclusively use numeric secrets.
- Evaluating whether the structured poisons ("credit card number is not: 123456") survive a simple regex-based sanitization filter, to ground the "benign-appearing" claim.
- Estimating how many poisons an attacker would realistically need when they cannot control the temporal gap between poison insertion and secret appearance.

## Removed Points

- **"The paper never returns to the question of whether the attacker could find such a prefix without already knowing the secret"** — Removed as factually incorrect. Lines 225–227 and Figure 4 explicitly introduce a randomized inference strategy that extracts the secret without knowing the exact prefix, and show it improves SER.
- **"The paper offers no explanation for why random sentences would cause the model to memorize a 12-digit credit card number"** — Partially removed / downgraded. The paper does offer an explanation (lines 79–82, 227) about "generalized memorization," though the explanation is vague. The real issue is the missing control condition (kept as a Major weakness above).

## Novel Insights

The reviews collectively reveal that the paper's strongest contribution — the durability of pretraining poisoning across thousands of steps — is somewhat orthogonal to its main narrative of "teaching the model a generalizable phishing strategy." If the mechanism turns out to be simply that additional training data (regardless of content) increases memorization capacity, the durability finding would still be important: it would mean the attacker only needs to find *any* way to insert extra tokens (not even specifically structured poisons) to amplify extraction risk. Conversely, if the mechanism is genuinely about learning a robust prefix-to-secret mapping (as the randomized inference results suggest), then the paper opens a new direction in understanding how language models can learn abstract structural patterns during training. Resolving this tension — via the control experiment proposed above — would clarify which contribution is primary.

## Suggestions

1. **Add a control experiment**: Compare SER under the random-poison condition against a condition where the attacker inserts the same number of unrelated filler sentences (e.g., additional Enron emails) that contain no digits, no labels, and no "not." If this control also increases memorization, the mechanism is about data addition, not phishing. If it does not, the "teaching to phish" mechanism is strongly supported.

2. **Replicate with at least 3 different secrets and 2 prefixes each, reporting mean and range**. This is critical for making the numerical claims credible and is the most impactful way to strengthen the paper given its reliance on quantitative results.

3. **Restructure the paper to foreground the durability result** (Figs. 7–8) as the primary contribution, with the immediate-query experiments as ablations. The durability finding is the most novel and least assumption-dependent result.

4. **Qualify the "benign-appearing" claim** to distinguish between the random-poison baseline and the structured "not" variant, and test the latter against a simple regex-based sanitization filter.

## Score and Decision

The paper introduces a genuinely novel attack vector, has a strong and surprising durability result, and provides a useful inference technique. However, the missing control condition and lack of statistical replication substantially weaken the evidence for the central mechanistic claim. The contributions are real but not yet presented with sufficient rigor for acceptance.

**Score**: 5.5

**Decision**: Reject (borderline — the core idea and durability finding warrant a substantially revised version with proper controls and replication)

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>