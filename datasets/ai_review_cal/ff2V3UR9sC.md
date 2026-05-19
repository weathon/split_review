- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6
Now I have all the evidence needed. Let me produce the consolidated review.

## Summary

This paper proposes training vision-language models (VLMs) on receiver behavior data (likes, comments, upvotes, replay graphs) collected from Reddit and YouTube to improve content understanding. The authors introduce BLIFT, a 730k-sample instruction fine-tuning dataset, train Behavior-LLaVA (based on LLaMA-Vid), and evaluate across 46 tasks and 26 benchmarks spanning image, video, text, and audio. The key control experiment — Ad-LLaVA, trained on the same videos/images without behavior data — shows that the improvements are causally attributable to the behavior signal, not simply additional data.

## Strengths

- **Well-controlled causal ablation (Ad-LLaVA):** Training LLaMA-Vid on the same BLIFT images/videos *without* behavior data yields performance essentially identical to the base LLaMA-Vid, while Behavior-LLaVA (with behavior) consistently outperforms both across all tables (e.g., Tables 1–4). This cleanly isolates behavior as the causal factor for improvement, which is the strongest evidence in the paper.

- **Extensive multi-task evaluation:** The model is tested on 46 tasks across 26 benchmarks covering VQA, video and image understanding, emotion recognition, memorability simulation, dense captioning, and even audio/text tasks. The improvements are broad and consistent, especially on high-level semantic tasks (emotion, persuasion, memorability) where zero-shot gains are large.

- **Novel large-scale behavior dataset (BLIFT):** At 730k images and videos with rich behavioral annotations (comments, likes, replay graphs, upvotes), BLIFT is orders of magnitude larger than prior perception-behavior datasets (e.g., 10k images in SALICON) and is released to the community.

- **Perception vs. action behavior comparison:** The paper ablates perception-level behavior (saliency from SALICON) against action-level behavior (BLIFT), finding that action-level data yields substantially larger improvements, supporting the authors' argument about the value of scalable behavioral signals.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed zero-shot SOTA on emotion benchmarks (Table 3).** The caption of Table 3 states it "outperforms the current state-of-the-art on 3/3 benchmarks in zero-shot." However, the zero-shot section of that table only compares Behavior-LLaVA against LLaMA-Vid and Ad-LLaVA — both are the authors' own baselines. No external zero-shot VLM (e.g., VideoChat, Video4096, GPT-4V, or any published emotion-specific zero-shot method) is included for comparison. This claim is unsupported by the data presented. (By contrast, the SOTA claims in Tables 1 and 2 are supported by actual external baselines in those tables.) The authors should either add external zero-shot baselines or rephrase the claim to accurately reflect what was compared.

### Minor

- **No statistical significance or variance reported.** Every number in every table is a single point estimate with no confidence intervals, standard deviations, or significance tests. Given that several fine-tuned improvements are small (e.g., 0.86% on Ekman-6), it is impossible to assess reliability. While single-run evaluation on standardized benchmarks is common practice in the VLM community, the paper would be stronger with error bars on key comparisons (Behavior-LLaVA vs. Ad-LLaVA vs. LLaMA-Vid on at least the main tables).

- **"Free-lunch" framing is overstated.** The abstract calls the performance improvement "essentially free-lunch" because behavior data is "collected by default on the internet." However, the paper documents extensive filtering: scraping at scale, NSFW/bot/duplicate removal, TF-IDF deduplication, manual category exclusions (51% of YouTube videos removed for being private/unlisted), language filtering, etc. This is not trivial effort. The framing should be tempered to acknowledge that while behavior data is cheaper than lab-collected perceptual data, significant processing is required.

- **Percentage improvements from near-random baselines can be misleading when reported without context.** In Table 4 (memorability zero-shot), the base LLaMA-Vid scores near chance (e.g., 0.05 on SUN, 0.02 on MediaEval), producing percentage improvements like 160%, 350%, etc. The abstract's "upto 150%" is drawn from these. The paper does report absolute values alongside percentages, which mitigates the issue, but the rhetorical framing obscures that the base model is essentially random on these tasks. Absolute gains (e.g., 0.05→0.13 on SUN) should be foregrounded more prominently alongside percentages.

- **Missing evaluation on standard VLM benchmarks (MMBench, MMMU, etc.).** The paper focuses entirely on specialized tasks. It does not show whether behavior training preserves or degrades general VLM capabilities. A sanity check on standard VLM leaderboards would increase confidence that behavior training does not harm general competence.

- **No analysis of how continuous behavioral targets are tokenized/predicted.** The model is trained to output numerical values (e.g., "2.0%" like ratio, "0.06" replay value) and ranked lists of comments. The paper does not explain how these continuous/ordinal values are represented in the language generation format, making reproduction harder.

- **Dataset bias from Reddit/YouTube demographics not discussed.** Reddit and YouTube users are not representative of the general population, and engagement metrics reflect popularity bias and social biases. The paper does not discuss how these biases might transfer to the VLM's behavior, which is a notable omission for a dataset contribution.

### Trivial
None of note.

## Nice-to-Haves

- Present absolute gains alongside percentages more prominently, especially for near-random baselines.
- Include an analysis probing *what* the model learns from behavior (e.g., comparing internal representations with/without behavior training, or testing on adversarial examples requiring social/emotional understanding).
- Report how well the model actually predicts the behavioral targets (beyond comment perplexity and likes R²) — e.g., qualitative examples of generated vs. ground-truth comments, or accuracy of replay graph predictions.
- Add a limitations section discussing dataset biases.
- Provide standard training hyperparameters (GPU-hours, batch size, learning rate, etc.).

## Removed Points

- **"Cross-modality evaluation is underreported/unverifiable because the modality-ablation table is missing"** — REMOVED. The parser strips appendix content from all papers. The modality-ablation table, salicon-ablation table, and other appendix tables exist in the original submission. Per instructions, missing appendix content is not a valid weakness.
- **"Free-lunch replication concerns (scraping, copyright)"** — The paper describes a complete filtering pipeline and acknowledges the filtering steps. The "free-lunch" phrasing is an overstatement (kept above as minor) but the concern about replication feasibility is addressed by the paper's own detailed description. Not a separate weakness.
- **"Comparison to direct baselines like LLaVA-1.6 or GPT-4V on standard VLM benchmarks (MMBench, MMMU, etc.)"** — This is already kept as a minor weakness above; the duplicate framing from the "Missing Parts" section is removed.
- **Strength Finder's generic strengths** — Dropped: "Large-scale, behavior-rich dataset BLIFT" is concrete and kept. "Cross-modal generalization beyond vision" — the claim is mentioned but the table is in the appendix; kept as partially verified. "Large zero-shot gains on high-level tasks" and "Ablation comparing perception vs. action behavior" are concrete and kept. Generic descriptions like "this paper addressed an important problem" are removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any meta-insight that the paper itself does not already articulate. The one point worth noting is that the Ad-LLaVA control (identical data without behavior) is a clean experimental design that the reviews correctly identify as the paper's strongest evidential contribution.

## Suggestions

1. **Fix the overclaimed SOTA in Table 3.** Either add external zero-shot baselines to that table, or rephrase the claim to accurately reflect that Behavior-LLaVA outperforms *its own base models* (LLaMA-Vid, Ad-LLaVA) in zero-shot — not that it outperforms the published SOTA in zero-shot, since no SOTA methods are compared in that table's zero-shot rows.

2. **Add error bars or significance tests** for at least the core comparisons (Behavior-LLaVA vs. Ad-LLaVA vs. LLaMA-Vid) on the main tables. Multiple random seeds or bootstrapped confidence intervals would substantially strengthen the empirical claims.

3. **Temper the "free-lunch" framing** to something like "behavioral data is substantially cheaper to collect than lab-based perceptual data, though careful filtering is required."

4. **Report absolute improvements alongside percentages** in the abstract and discussion, especially for tasks where the base model is near-random, to avoid misleading relative improvements.

5. **Include a sanity check on standard VLM benchmarks** (e.g., MMBench, MMMU, or at minimum the benchmarks used in the original LLaMA-Vid evaluation) to confirm that general VLM capabilities are preserved after behavior training.
