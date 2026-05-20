Now let me write the consolidated review.

## Summary

This paper proposes "neural phishing," a novel data poisoning attack that induces LLMs to memorize and regurgitate sensitive information (e.g., credit card numbers, SSNs) that appears later in the training pipeline. The attacker inserts benign-appearing poisoned examples during pretraining or finetuning; when the model subsequently trains on private user data containing secrets, it has been "taught to phish" and will output those secrets when prompted. The attack achieves 10–50% secret extraction rates (SER) on 12-digit secrets in controlled settings, with the most striking result reaching ~88% SER when using randomized inference prompts. The paper provides systematic ablations on secret length, duplication, model scale, prior knowledge, and durability across training steps.

## Strengths

- **Novel attack vector with non-trivial success rates.** The core idea — that a small number of poisoned examples can teach an LLM to memorize subsequently seen secrets — is genuinely new and interesting. With 50 random poisons (no knowledge of the secret), the attack achieves ~15% SER on 12-digit secrets, a factor of 10¹¹ above random guessing (Figure 2). The paper explicitly verifies that attacks never succeed without poisoning (Section 4, "we evaluate the baseline with poisoning-free models and find that we can never extract any secrets").

- **Clear scaling laws and thorough ablations.** The paper systematically explores how SER varies with secret length, duplication count (Figure 3), model size from 1.4B to 6.9B parameters (Figure 4), and pretraining duration (Figure 5). These are well-executed experiments that provide a solid empirical characterization of the attack.

- **Vague priors are sufficient.** A key practical result (Figure 6): the attacker needs only a vague prior (e.g., "write a biography of Alexander Hamilton") rather than exact knowledge of the secret prefix to achieve ~40% SER, a 2.7× improvement over random poisons. This significantly reduces the attacker's knowledge requirements.

- **Randomized inference is a genuinely counterintuitive and strong finding.** Figure 7 shows that randomizing the secret prefix at inference time boosts SER from ~52% to ~88% with 100 poisons. This supports the paper's claim that the model learns a robust memorization pattern beyond a fixed prefix-to-secret mapping. It also demonstrates that deduplication defenses are ineffective since all poisons can be made unique.

## Weaknesses

### Fatal
None.

### Major
- **The threat model is plausible only under significant constraints that are not adequately bounded.** The paper claims poisons are "benign-appearing" (used as a motivating example: "Alexander Hamilton... His social security number is: 424 379 023 668") but provides no evidence that such poisons would survive real data curation pipelines (perplexity filtering, deduplication, quality screening). The attack's practical viability hinges entirely on poisons passing unnoticed into the training set, yet this is asserted rather than demonstrated. To the paper's credit, it acknowledges three insertion vectors (web scraping, employee access, federated learning) but does not validate any of them experimentally. Every experiment assumes poisons are already in the training set. The paper would benefit from either (a) demonstrating that poisons survive a realistic pipeline, or (b) explicitly scoping the claims to settings where the adversary has direct dataset write access and adjusting the language accordingly.

- **The central "teaching to phish" claim is not convincingly distinguished from amplified memorization.** The paper argues the model learns a generalized memorization behavior rather than a fixed prefix-to-secret mapping. The evidence (Figure 7, randomized inference outperforming fixed prefix) supports *some* generalization, but a simpler explanation remains: the secret becomes a high-probability completion for a broad class of similar prompts because it is strongly memorized (aided by duplication). The paper does not ablate this by, e.g., testing whether the model outputs plausible-looking digit strings from never-seen prefixes that do not match the secret's distribution. The contribution is still meaningful if framed as "poisoning amplifies memorization of subsequently seen secrets," but the "teaching to phish" metaphor overstates the mechanistic novelty.

- **Durability results show meaningful persistence only within narrow temporal windows.** Figure 8 shows the attack achieves ~30% SER at 10,000 steps gap (undertrained model) but drops to ~0% at 100,000 steps gap for both models. The paper's caption ("Even 100,000 steps after training on poisons, the model memorizes secrets with significant SER") is contradicted by the actual plotted data, where both curves reach ~0% at 100k steps. The positive result (30% at 10k steps) is genuinely interesting and non-trivial, but the paper should clarify that the attack's pretraining durability is limited to gaps of a few thousand to ten thousand steps — a constraint most real adversaries cannot control.

### Minor
- **The "not" trick is ad-hoc and unanalyzed.** Appending "not" before the poison digits (e.g., "credit card number is not: 123456") is essential to prevent the model from overfitting on the poison and is used in all main experiments. The paper acknowledges this ("our first attempt to fix overfitting") but provides no analysis of why it works or whether alternative approaches would be equally effective. A mechanistic explanation (e.g., loss curve analysis or gradient analysis) would strengthen the paper.

- **No evaluation of defenses.** The paper does not test whether standard privacy defenses (differential privacy, sanitization, or perplexity-based filtering of the secret data) would mitigate the attack. Given that the paper's threat model depends on training on private user data, showing the attack's effectiveness under differential privacy (even at high epsilon) would significantly strengthen the practical significance. The paper only tests deduplication and shows it is evaded — this is one data point, not a thorough defense analysis.

- **Evaluation limited to Pythia models (up to 6.9B).** The paper acknowledges this ("we are not able to evaluate [larger models] due to computational constraints") but extrapolates to much larger models (LLaMA-2-70b, Falcon-180b) without evidence. Given that scaling is a central claim (Figure 4), at least one replication on a different model family (e.g., GPT-2-XL or OLMo) would improve confidence.

### Trivial
- The durability caption (Figure 8) claims "Even 100,000 steps after training on poisons, the model memorizes secrets with significant SER" when the plotted SER at 100k steps is ~0% for both curves. This mismatch between caption and data should be corrected.

## Nice-to-Haves
- A controlled ablation comparing: (a) no poisons + no duplication, (b) no poisons + duplication, (c) poisons + no duplication, (d) poisons + duplication. The paper states attacks never succeed without poisons, but putting this explicitly in a figure would cleanly separate the effects of poisoning from duplication.
- A human evaluation or perplexity analysis showing that the crafted poisons indeed "appear benign."

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Threat model: employee access argument.** The harsh critic claims "if the attacker is an employee with write access, they could simply exfiltrate the secret directly." This ignores the fundamental distinction between write access (add data) and read access (see data). The threat model assumes the attacker can contribute data but not read the training set — a standard and reasonable assumption in data poisoning literature. Removed as it misunderstands the threat model.
- **Federated learning criticism.** The critic faults the paper for not evaluating the attack in federated learning. The paper merely lists FL as one possible insertion vector; it does not claim to evaluate it. Criticizing the paper for not doing Y when it explicitly scoped to X is not fair. Removed.
- **Claim that duplication is conflated with poisoning.** The paper explicitly states "Attacks never succeed without poisoning" and "we evaluate the baseline with poisoning-free models and find that we can never extract any secrets." The critic missed this explicit statement. Removed as factually wrong.
- **Missing related works.** Cannot be included per instructions.
- **Reproducibility nitpicks about missing hyperparameters.** Per instructions, these are removed.
- **Generic formatting/presentation nitpicks.** Removed per instructions.
- **Weaknesses about stripped appendix content.** Removed per instructions.

## Novel Insights
The most striking finding — that randomizing the inference prefix significantly outperforms using the exact secret prefix (Figure 7) — is a genuinely counterintuitive observation that merits deeper investigation. It suggests that poisoning with many unique variations (which also evades deduplication) creates a broad attractor in the model's generation space, such that any prompt fitting a loose template converges to the secret. If confirmed and mechanistically understood, this could represent a qualitatively different failure mode from standard memorization. Neither the original reviews nor the paper fully exploit this observation.

## Suggestions
1. Tighten claims about the threat model: either validate that poisons survive a realistic curation pipeline, or explicitly bound the attack to insider-threat / direct-injection settings and adjust all language ("practical," "realistic") accordingly.
2. Add a controlled ablation explicitly separating the effects of poisoning from secret duplication in a single figure.
3. Provide a mechanistic analysis of the "not" trick (e.g., loss curves comparing with and without "not").
4. Test at least one standard defense (e.g., differential privacy at ε ≥ 8) to bound the attack's practical scope.
5. Correct the durability caption (Figure 8) to match the plotted data (SER near 0% at 100k steps) instead of claiming "significant SER."

## Calibration and Score

### Round 1 — Bracketing
- **Weak anchors (<3.5):** Queried "data poisoning attack on language models". Retrieved examples avg 2.5–3.0 (e.g., "KDA" at 2.5, "From gradient attacks to data poisoning" at 3.0). These are rejected/withdrawn papers with weaker contributions. The current paper is clearly stronger than these.
- **Middle anchors (3.5–7.5):** Queried "LLM privacy extraction attack". Retrieved "Scalable Extraction of Training Data from Aligned, Production Language Models" (avg 6.67, accepted poster), "Beyond Memorization: Violating Privacy via Inference" (avg 7.20, spotlight), "Evaluating Privacy Risks of PEFT" (avg 5.80, rejected), and "FLAT-Chat" (avg 4.25, rejected).
- **Strong anchors (>7.5):** Queried "neural phishing training data extraction". Retrieved "Data Selection via Optimal Control" (avg 8.00, oral), "Combatting Dimensional Collapse" (avg 8.00, oral). These are top-tier methodology papers on different topics; the current paper is not comparable.

**Initial bracket:** 4.5 – 6.5.

### Round 2 — Narrowing
Queried within (4.5, 7.5) with two topical searches. Retrieved additional anchors:
- "BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge" (avg 6.75, accepted poster) — similar threat model (data poisoning on LLMs), more thorough experiments including defenses, clearly stronger paper.
- "Backdooring Instruction-Tuned LLMs with Virtual Prompt Injection" (avg 4.75, withdrawn/rejected) — similar threat model, weaker experiments, rejected primarily for unrealistic threat model.
- "Elephants Never Forget" (avg 4.75, rejected) — measurement study, lower novelty.
- "Mitigating Memorization in Language Models" (avg 7.33, spotlight) — defense paper, different contribution type.

Compared to "Scalable Extraction" (6.67): That paper was demonstrated on production systems (ChatGPT, Gemini) with thousands of extracted examples. The current paper works on smaller open models (Pythia 6.9B) in a controlled setting. The current paper has a more novel attack mechanism but weaker validation. The current paper is **moderately weaker** than this anchor.

Compared to "BadJudge" (6.75): That paper has thorough experiments across settings, proposes defenses, and achieves clear practical relevance. The current paper is less polished on threat model analysis and lacks defense evaluation. The current paper is **weaker** than this anchor.

Compared to "Evaluating Privacy Risks of PEFT" (5.80, rejected): That paper is a measurement study with more limited novelty. The current paper has a more novel attack idea. The current paper is **slightly stronger** than this anchor.

Compared to "Backdooring Instruction-Tuned LLMs" (4.75, rejected): That paper has a similar threat model weakness and was rejected. The current paper has significantly more thorough experiments and more interesting findings. The current paper is **clearly stronger** than this anchor.

**Final score:** 5.5. This is a paper with a genuinely novel idea and solid experiments, but the threat model rigor, overly strong claims, and lack of defense evaluation place it below the acceptance threshold at a top venue. The paper would benefit from revisions addressing the threat model bounding and claim calibration.

### Calibration Anchors Summary
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| ZFjp5Q2hLn.md | 3.00 | R1 | Weaker — different subfield, lower quality |
| UWuTZYPSxJ.md | 2.50 | R1 | Weaker — red teaming paper, less contribution |
| vjel3nWP2a.md | 6.67 | R1+R2 | Stronger — attacks on production models, more thorough |
| kmn0BhQk7p.md | 7.20 | R1+R2 | Stronger — different attack paradigm, better validated |
| i2Ul8WIQm7.md | 5.80 | R1+R2 | Similar — privacy measurement study, less novelty |
| lwtaEhDx9x.md | 4.75 | R2 | Weaker — measurement study, limited novelty |
| MGKDBuyv4p.md | 7.33 | R2 | Stronger — defense paper, different contribution |
| eC2a2IndIt.md | 6.75 | R2 | Stronger — more thorough experiments, includes defenses |
| b3KgHQos7P.md | 4.75 | R2 | Weaker — similar threat model issues, weaker experiments |
| T6qIMnokrI.md | 5.75 | R2 | Similar direction (backdoor data exfiltration), comparable quality |

MY FINAL SCORE: 5.5
MY FINAL DECISION: Reject