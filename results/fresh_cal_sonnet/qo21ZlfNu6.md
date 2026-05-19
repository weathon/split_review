Now let me run calibration search to anchor the score.Now let me narrow within the bracket [5, 7].Now I have enough context to write the final review. Let me compile it.

---

## Summary

This paper introduces "neural phishing," a data poisoning attack in which an adversary inserts a small number (tens to hundreds) of benign-appearing sentences into an LLM's training data to teach the model to memorize and subsequently regurgitate *other* users' personally identifiable information (PII) at inference time. The key novelty over prior training-data extraction work is the *active* poisoning component: the attacker injects examples that generalize memorization rather than exploiting naturally duplicated data. Empirical results on Pythia models (1.4B–6.9B) show 10–50% secret extraction rates (SER) for 12-digit secrets, and the paper demonstrates that the poisoning behavior persists for thousands of clean training steps and that deduplication defenses are ineffective against randomized poisons.

---

## Strengths

- **Genuinely novel threat model**: The attack teaches the model to memorize *other users'* secrets via a small poison injection, achieving SER on the order of 10% with no knowledge of the target prefix and up to 40% SER with only a vague prior (e.g., "a bio of Alexander Hamilton"). This is a qualitatively new contribution beyond passive extraction attacks; prior work relies on naturally duplicated data while this exploits active poisoning-induced generalized memorization. (Sections 3–4, Figure 1, Figure 3)

- **Practical attack with strong quantitative results**: The paper reports 10–50× attack success that is 10¹¹× above random chance for high-entropy 12-digit secrets (Section 3, Figure 1, blue line: 10–15% SER with 50 random poisons, 0 extractions without poisoning). The attack requires only 50–100 short poisoned documents, consistent with realistic web-scraping or finetuning poisoning scenarios.

- **Randomized inference strategy generalizes the attack**: The paper shows that randomly perturbing proper nouns in the prefix at inference time improves SER and allows secret extraction without the attacker knowing the exact inference prefix (Section 4, Figure 4 / `\cref{fig:randomprompts}`). This validates the "generalized memorization" intuition central to the paper and is a novel empirical finding.

- **Scaling laws are informative**: The paper systematically demonstrates that SER increases with model size (1.4B to 6.9B, Figure `\cref{fig:modelscaling}`), pretraining duration (Figure `\cref{fig:pretrainingscaling}`), and secret duplication, providing actionable characterizations of attack severity across deployment settings.

- **Evasion of deduplication defenses**: The paper specifically shows that randomizing poison sentences at generation time defeats the standard deduplication defense used in training pipelines. (Figure `\cref{fig:randomprompts}`, caption: "evades deduplication defenses, because all 100 poisons are unique.") This is a concrete and practically relevant finding.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Durability claim is under-contextualized and potentially inconsistent.** The paper's most ambitious claim — that poisoning behavior persists for "10,000 steps" or "100,000 steps" (the text at line 253 says 10,000; the Figure caption at lines 239–240 says 100,000) — rests on an experiment using *Wikitext* as clean data, explicitly because "Enron Emails is too small to train on for this many steps" (line 252). However, nowhere does the paper report batch size, token count, or the relationship between these Wikitext steps and the training data volumes typical of a realistic pretraining continuation. Without this context, the "10,000 steps" figure is uninterpretable: it could correspond to a trivial fraction of a real pretraining run. Additionally, the discrepancy between "10,000 steps" in the text (line 253) and "100,000 steps" in the figure caption (line 239) is unexplained. This evidential gap is significant because the "poisoning pretraining is viable" attack vector — the paper's most threatening scenario — depends entirely on this result.

- **Full end-to-end pipeline is never evaluated.** The durability experiment (Phase I: poisons → clean Wikitext training) and the forgetting experiment (Phase II: finetuning on secret → clean Wikitext training) are evaluated *separately* with different clean-data sources and configurations. The paper never runs the full realistic pipeline: poisons injected in pretraining → realistic continuation of pretraining → finetuning on a corpus containing the secret at a natural position → deployment-time extraction. The interactions between the two effects (durability of phishing behavior × forgetting of the extracted secret) are the central practical question, but they are reported independently rather than jointly. This is the single most important missing experiment.

- **No variance reporting throughout.** Every SER figure shows deterministic curves with no error bars, standard deviations, or confidence intervals. SER is inherently stochastic (different random poison sets, secret positions, model seeds), and many experiments appear to involve a small number of secrets. Run-to-run variance could be substantial for single-run evaluations. Readers cannot assess whether observed differences between conditions are meaningful or within noise.

### Minor

- **"Benign-appearing" property is asserted, not demonstrated.** The paper claims the poisons "appear benign" (lines 6–7, 52–53), yet the canonical poison form is "credit card number is not: 123456" appended to a sentence. No human evaluation, no automated classifier test, and no discussion of whether this format would survive realistic data curation pipelines (e.g., regex filters for digit strings, PII scrubbers) is provided. For the finetuning attack vector where the adversary injects documents into a company's curated dataset, the plausibility of evading such filters is a real practical concern that goes unaddressed.

- **"not" trick mechanism is entirely unexplained.** The paper's anti-overfitting technique — appending the word "not" before poison digits — is described purely empirically: "the use of 'not' was our first attempt to fix overfitting and it works well" (line 128). The mechanism is unknown, no ablation over alternative suppression tokens or structural interventions is provided, and no analysis of why negation prevents overfitting to the poison's own digit sequence is given. The entire attack construction depends on this trick, and its current treatment is purely heuristic.

- **Abstract conflates minimal-assumption and maximum-assumption success rates.** The abstract states "upwards of 10% attack success rates, at times, as high as 50%." The 50% figure is explicitly described in Section 4 (line 211) as "a very strong assumption" and used only "to illustrate the upper bound." The baseline (no knowledge of secret or prefix) achieves 10–15%. A reader who does not read carefully will systematically overestimate the practical success rate in the minimal-assumption setting.

### Trivial

- Multiple `\cc{...}` revision tags remain visible in the submitted text (lines 36, 42, 47, 52–53, 55, 59, 113, 115, 125, 233, etc.), including one that reads literally "removed this here, this looks like what we've repeated multiple times to this point" (line 115). Whether these represent visible colored-comment annotations in the submitted PDF or parser artifacts, they indicate the manuscript was not fully finalized.

---

## Nice-to-Haves

- **A full end-to-end evaluation** is the single highest-value addition: poisons injected into pretraining corpus → realistic volume of pretraining continuation → finetuning on a corpus containing the secret at a natural position → extraction at deployment. This would convert the current collection of isolated ablations into a single coherent proof-of-concept for the most threatening attack scenario.

- **Mechanistic investigation of the "not" trick**: A controlled ablation across different suppression tokens ("not," "never," a punctuation separator, formatting tokens) and a probe of internal representations would sharpen the central generalized-memorization claim and make the contribution more scientifically durable.

- **Brief discussion of differential privacy defenses**: Even a short treatment of whether DP-SGD at realistic privacy budgets would substantially reduce SER would ground the work in the existing mitigation literature and be valuable to practitioners.

- **Multi-secret case**: Line 47 acknowledges this is future work, but even a brief scaling demonstration showing how SER degrades as the number of simultaneous targets increases would meaningfully extend the practical threat model.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength: "10^11× better than random guessing"** (Strength Finder). Retained in review since it is grounded (zero extractions without poisoning vs. 10-15% SER), but this specific framing appears in the abstract and is slightly misleading because it compares to *pure* random guessing rather than to prior extraction attacks, which the paper later clarifies.

- **Speculation about scaling extrapolation being misleading**: The harsh critic flags "we anticipate that the neural phishing attack can be much more effective at the scale of truly large models" (line 163) as appearing in the results section and therefore overstated. The word "anticipate" is clearly labeled speculation, and this is reasonable scientific extrapolation based on the demonstrated monotone scaling at 1.4B–6.9B. REMOVED as too minor to raise.

- **Forgetting window as a fatal flaw**: The harsh critic notes that SER drops to 0 after 1,000 clean steps. This is *acknowledged* by the paper as a limitation (lines 260). It is a genuine constraint but not a flaw, and the paper partially addresses it via ensemble inference. DEMOTED — already captured in the major weakness about the full-pipeline evaluation.

- **Demand for human evaluation of "benign-appearing" claim to include filter testing**: The harsh critic's version of this was broader (asking for "no human evaluation, no automated classifier test"). We retain the substance as a Minor weakness but remove the demand for full human evaluation studies, which would be an excessively high bar for a security paper.

- **Demand for DP-SGD analysis**: While this would strengthen the paper, DP-SGD defense evaluation is outside the paper's stated scope of demonstrating the attack. Moved to Nice-to-Haves.

- **Federated learning scenario not evaluated**: The paper explicitly lists FL as one of three attack vectors (line 66) but only demonstrates the first two. This is a real limitation but minor given the paper's stated focus and the framing as "three general scenarios," not three evaluated results. Moved to Nice-to-Haves implicitly.

- **Generic strength: "this paper addressed an important problem"** (Strength Finder). Removed per filtering rules.

---

## Novel Insights

The most conceptually interesting finding is the randomized-prefix inference strategy: perturbing proper nouns in the victim's prefix at inference time *improves* SER compared to using the exact prefix. This provides direct empirical evidence for the paper's central claim that the model learns *generalized memorization* (a robust mapping from many related prefixes to the secret) rather than a fixed prefix–suffix mapping. This distinction — generalized memorization vs. sequential overfitting — is a meaningful conceptual contribution that distinguishes neural phishing from all prior training-data extraction work and deserves more mechanistic investigation than the current paper provides.

---

## Suggestions

1. Report training scale context for the durability experiment: batch size, total tokens consumed during the 10,000/100,000 Wikitext steps, and an estimate of how this compares to a realistic pretraining continuation volume. This single addition would make the durability claim interpretable.

2. Resolve the discrepancy between "10,000 steps" (text, line 253) and "100,000 steps" (figure caption, line 239) in the durability result — one of these is wrong.

3. Add error bars or confidence intervals to at least the primary SER curves. A simple re-run with 3–5 different random seeds for the main experiments would substantially increase reader confidence.

4. Design and run a joint end-to-end experiment: poisons in pretraining → continue pretraining on large clean corpus for a contextually realistic number of steps → finetune on Enron-style data with a secret appearing once → extraction at deployment. Report both durability and forgetting in this single unified setup.

5. Provide an ablation over the "not" suppression token, even if brief (e.g., replacing "not" with "never," "≠," or a newline). This would transform an unexplained trick into a scientifically interpretable design choice.

---

## Score and Decision

**Scoring calibration:**

**Round 1 anchors (bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `5kMwiMnUip.md` | 1.40 | 1 (low) | Jailbreaking paper, clearly weaker — insufficient novelty/rigor |
| `KyKTjRtyNG.md` | 3.00 | 1 (low) | Incremental jailbreak, no real mechanistic contribution |
| `vjel3nWP2a.md` | 6.67 | 1 (mid) | Scalable extraction from ChatGPT — broader practical scope, more polished |
| `jx6njBKH8E.md` | 5.75 | 1 (mid) | Amplifying exposure via fine-tuning — similar scope, weaker novelty |
| `6Mxhg9PtDE.md` | 9.50 | 1 (high) | Shallow safety alignment — unifying framework, extensive theory+experiments |
| `oZtt0pRnOl.md` | 8.00 | 1 (high) | DP in-context learning — theoretically grounded, comprehensive |

**Round 1 bracket: 5–7.**

**Round 2 anchors (narrowing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `eiqrnVaeIw.md` | 5.75 | 2 | Persistent pre-training poisoning of LLMs — closest topical match. Accepted at 5.75. Weaker mechanism novelty than the current paper but more comprehensive in scope (4 attack types, full pretraining from scratch, multiple model sizes). Draft quality comparable. |
| `jx6njBKH8E.md` | 5.75 | 2 | Amplifying exposure via pseudo-labeled memberships — narrower scope than current paper, weaker novelty, similar draft quality issues. |
| `vjel3nWP2a.md` | 6.67 | 2 | Scalable extraction from production models — attacks actual ChatGPT, substantially broader scope, much more polished. Current paper has stronger mechanism novelty but narrower execution. |
| `kmn0BhQk7p.md` | 7.20 | 2 | Privacy violation via LLM inference — high-quality work on a different (but related) privacy threat. More comprehensive and polished. |
| `7erlRDoaV8.md` | 7.50 | 2 | Deleting sensitive information from LLMs — both attack and defense, strong evaluation, good presentation. Current paper is below this level. |

**Final calibration reasoning:** The paper under review is clearly better than the jailbreaking papers (1–3) and better than the narrowly scoped pseudo-label fine-tuning paper (5.75). It is topically closest to `eiqrnVaeIw.md` (5.75, accepted) and benefits from stronger mechanism novelty (the phishing mechanism, the "not" trick, the randomized inference strategy, the generalized-memorization framing). However, it falls short of `vjel3nWP2a.md` (6.67) due to narrower scope, weaker polish, and the under-evidenced durability claim. The draft quality issues (revision comments visible) and missing variance reporting are real but addressable deficiencies. The full-pipeline evaluation gap is the most substantive concern.

**Score: 5.5** — above the 5.75 anchors at first glance, but pulled down by the visible draft incompleteness, missing variance reporting, and the durability claim's evidential gap. Closer to the lower end of the 5–7 bracket; a revised submission addressing these issues would sit comfortably at 6.5–7.

**Assessment by axis:**
- *Originality*: High — genuinely novel threat model with new mechanism (generalized memorization, "not" trick, randomized inference).
- *Importance of research question*: High — active PII poisoning is a practically relevant and underexplored threat.
- *Claim support*: Moderate — core feasibility is demonstrated, but the most ambitious claim (pretraining poisoning durability) is under-evidenced and contains a potential text/figure discrepancy.
- *Soundness of experiments*: Moderate — credible controlled setup but no variance reporting, separate rather than integrated evaluation of the two key effects.
- *Clarity of writing*: Fair — logically organized but revision comments remain in the text, and the abstract conflates two very different performance regimes.
- *Value to research community*: High — both the threat model and the generalized-memorization insight will be cited and extended.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>