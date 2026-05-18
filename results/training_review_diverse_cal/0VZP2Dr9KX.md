Now let me carefully construct the final review after cross-checking all claims against the paper.

---

## Summary

This paper evaluates three categories of standard adversarial defenses—detection (perplexity filtering), preprocessing (paraphrasing and BPE-dropout retokenization), and robust optimization (adversarial training)—against the GCG jailbreaking attack on several 7B-parameter LLMs. It does not propose new defenses but benchmarks existing ones and argues that the high computational cost of discrete text optimization makes simple defenses more viable in the LLM domain than in computer vision. The paper finds that perplexity filtering and paraphrasing are surprisingly effective against current attacks, while true adversarial training remains infeasible.

## Strengths

1. **Perplexity filtering completely blocks current GCG attacks**: Table \ref{tab:ppl_filter_orig_attack} shows that both a simple and a windowed perplexity filter detect every adversarial prompt (PPL Passed and PPL Window Passed rates are 0.00 for 4 of 5 models, 0.01 for the fifth), while letting all benign harmful-behavior prompts through. This directly supports the claim that detection is effective against the tested optimizer.

2. **Adaptive attacks with perplexity constraints fail to maintain jailbreak success**: Figure \ref{fig:ASR_pplweight} shows that as the perplexity weight α_ppl increases, the attack success rate drops to approximately the no-attack baseline (<5% for Vicuna at α=0.6). The paper further investigates trigger-length variants (5, 10, 20 tokens) and window-size ablations (Figure \ref{fig:token_window_ablation}), providing nuanced analysis of when the attack can partially bypass the filter.

3. **Paraphrasing defense reduces ASR to near-baseline levels**: Table \ref{tab:Paraphrase_Defense_main} reports that on Vicuna-7B, ASR drops from 0.79 to 0.05 (matching the 0.05 no-attack baseline), and on Guanaco-7B from 0.96 to 0.33 (close to its 0.31 baseline). Qualitative examples (Table \ref{tab:AlpacaEval_Paraphrase_Qualitative}) confirm that paraphrasing removes the adversarial suffix and restores refusal behavior.

4. **Retokenization via BPE-dropout degrades attack success without catastrophic performance loss**: Figure \ref{fig:brokentoken} shows that a BPE-dropout rate of 0.4 reduces Vicuna ASR from 0.79 to 0.52 and Guanaco ASR from 0.96 to 0.52, while Table \ref{tab:BPE_dropout_eval} shows AlpacaEval win rate drops only modestly (Vicuna from 54.41% to 47.64%). The paper also reports averages over four runs for this stochastic defense (line 362).

5. **Computational cost is identified as a key practical constraint distinguishing LLM security from vision**: The paper notes that GCG attacks require ~513,000 model evaluations (5–6 orders of magnitude more than vision attacks) and argues this reshapes the attack-defense landscape (Section 3, Section 5). This insight is well-grounded and genuinely novel for the domain.

## Weaknesses

### Fatal
None.

### Major

1. **Only GCG is tested, but claims are made about "discrete optimizers" as a class.** The paper's abstract states it finds "the weakness of existing discrete optimizers for text" (line 12), and the discussion generalizes to "the gradient-based optimizers we have today" (line 442). However, the paper evaluates only a single attack (GCG, a gradient-guided random search with a fixed 20-token suffix). Other optimizers (AutoPrompt, PEZ, BEAST, HotFlip variants, or simple genetic algorithms) are never tested. Without evidence that other optimizers would behave similarly, claims about "existing discrete optimizers" as a class are overgeneralizations from one instance. The paper acknowledges this as an open question in the conclusion (line 450–451), but the body and abstract make stronger assertions than the evidence supports.

2. **The adaptive attack evaluation is too narrow to fully support the white-box robustness claims.** For perplexity filtering, the only white-box adaptive attack tested adds a perplexity term as a simple linear combination to the GCG loss (α_ppl weighting, line 123). There is no attempt to use a fundamentally different optimizer, longer optimization runs, random restarts, or alternative objective formulations. For the paraphrasing defense, the adaptive attack is shown as a single qualitative example (line 202–204) with no quantitative success rate, no comparison to a non-adaptive baseline, and no evaluation across multiple test cases. The paper's central claim—that "evading a perplexity-based detection system could prove challenging, even in a white-box scenario" (line 32)—would be significantly stronger if tested against more diverse adaptive attack strategies. As it stands, the results may reflect properties of the GCG algorithm rather than fundamental difficulty of the problem.

### Minor

3. **Gray-box threat models are discussed but not evaluated.** The paper's threat model section (Section 3) argues that "we should consider white-box robustness only an aspirational goal, and focus on gray-box robustness" (line 72), yet all experiments are either black-box (no adaptation) or white-box (full adaptation). No experiment evaluates partial-knowledge scenarios (e.g., the attacker knows a perplexity filter is used but not the threshold, or knows the paraphraser model but not the meta-prompt). Given that gray-box framing motivates much of the paper's argument, the absence of any gray-box experiment is a gap between framing and evidence. The paper does acknowledge this as future work (lines 205–206, 448).

4. **No confidence intervals or error bars for most experiments.** The paper reports average ASR numbers as point estimates. The attack involves stochasticity (random token sampling in GCG, random BPE-dropout, ChatGPT paraphrasing), and the BPE-dropout section notes the paper averages four runs (line 362), but no variance estimates are provided elsewhere. This makes it hard to assess the stability of the reported numbers, particularly for the adaptive attack experiments.

5. **The "adversarial training" section tests a method substantially different from classical adversarial training.** The paper mixes a small percentage of harmful prompts with refusal responses into the training data, rather than performing online attack generation during training. The paper is transparent about this limitation (lines 388–389: "Our baseline in this section represents our best efforts to sidestep these difficulties"), but the section header ("Robust Optimization: Adversarial Training") and framing may lead readers to expect a method closer to the vision literature. The negative result (model degenerates) is not surprising given the approach.

### Trivial
None.

## Nice-to-Haves

- Testing at least one additional optimizer (e.g., AutoPrompt or a simple genetic algorithm) would substantially strengthen the claim that the difficulty is not GCG-specific.
- A simple gray-box experiment (e.g., keeping the perplexity threshold or paraphraser model secret from the attacker) would ground the paper's extensive gray-box discussion in evidence.
- Providing confidence intervals or error bars for key results would help assess stability.

## Removed Points

These points were raised by reviewers but are removed or downgraded with justification:

1. **"The retokenization defense creates new jailbreaking vulnerabilities (Guanaco baseline ASR increases)"** — Removed because the paper already acknowledges this directly: "this type of augmentation leads to higher baseline ASR as Guanaco converges to around the same ASR for both the attack and unattacked" (line 366). The paper is transparent about this limitation; it is not a hidden weakness.

2. **"The false positive rate (~10%) makes perplexity filtering impractical as a standalone defense"** — Removed because the paper already states "this shows that perplexity filtering alone is heavy-handed... dropping 1 out of 10 benign user queries would be untenable" (line 166). The paper explicitly discusses this trade-off and suggests integration into a larger system.

3. **"The paper lacks comparison to existing LLM-specific defenses (e.g., Llama Guard)"** — Removed because the paper explicitly scopes itself: "Our goal here is not to develop new defenses, but rather to test a range of defense approaches that are representative of the standard categories of safeguards developed by the adversarial robustness community" (line 27). Comparing to domain-specific moderation filters would be a different paper.

4. **"The adversarial training method does not correspond to classical adversarial training"** — Kept in Minor #5 above but downgraded because the paper is transparent about this being their best-effort approximation given computational infeasibility. The explicit qualification ("Our baseline in this section represents our best efforts to sidestep these difficulties," line 388) shows the paper does not claim to implement standard adversarial training.

5. **Criticisms about missing appendix content or references** — Removed per instructions; these sections exist in the original submission and are parser-stripped.

## Novel Insights

The most interesting observation cutting across the reviews is that the paper's core argument—that the high cost of discrete optimization reshapes the attack-defense landscape—is both its greatest strength and its central vulnerability. The insight is genuinely valuable: if accepted, it suggests the LLM security community should adopt fundamentally different evaluation standards than computer vision. However, the paper's evidence relies on a single attack (GCG) and a single adaptive attack strategy, meaning the argument is contingent on the current state of optimizer technology. The paper is aware of this (it raises the question "can discrete text optimizers be developed that significantly improve the effectiveness of adversarial attacks?" on line 450), but the strength of the paper's claims in the abstract and body does not always match this carefully hedged conclusion. The tension between the provocative thesis and the narrow empirical base is the most important thing for the authors and readers to grapple with.

## Suggestions

1. **Test a second optimizer.** The paper's most important limitation is generalizing from GCG to "discrete optimizers" broadly. Adding even one more optimizer (AutoPrompt, a genetic algorithm, or a beam-search variant) would significantly strengthen the core claim.
2. **Strengthen adaptive attack evaluation.** For perplexity filtering: test longer GCG runs, random restarts, or different formulations of the combined loss. For paraphrasing: provide a quantitative success rate for the adaptive attack, not just a single example.
3. **Add one gray-box experiment.** Choose a representative setting (e.g., unknown perplexity threshold, unknown paraphraser model) and evaluate whether transfer attacks from a surrogate defense succeed.
4. **Add confidence intervals** for key ASR numbers, particularly where the paper's conclusions rest on small differences.
5. **Align the strength of claims with the evidence.** The abstract and introduction could more precisely say "the GCG optimizer" or "current GCG-style attacks" rather than "existing discrete optimizers" when the evidence only covers one optimizer.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>