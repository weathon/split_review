- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5
Now I have all the information I need. Let me compile the final consolidated review.

## Summary
SCALE proposes a framework that combines compact Specialized Translation Models (STMs) with frozen Large Language Models (LLMs) by inserting STM-generated translations as an intermediate variable in triplet in-context demonstrations (source, STM-output, target). This unlocks refinement and pivoting capabilities in the LLM without fine-tuning it. Experiments on eight low-resource translation directions show SCALE outperforming both few-shot GPT-4 (by ~3 COMET) and NLLB-3.3B; a continual-learning experiment on Xhosa→English shows consistent improvement by updating only the lightweight STM; and a pivoting experiment from Lao shows gains over GPT-4 across eight target languages.

## Strengths
1. **Consistent empirical wins over strong baselines**: Table 1 shows SCALE-refine (GPT-4 + NLLB-3.3B) beats both few-shot GPT-4 (avg. +2.96 COMET, +5 BLEURT) and NLLB-3.3B across all eight low-resource directions, on three neural metrics (COMET-22, COMETKiwi, BLEURT). This is a clean, consistent result set.

2. **Continual learning without LLM fine-tuning demonstrated**: Figure 3 (Xhosa→English) shows SCALE with a fixed GPT-4 and a 600M-parameter NLLB STM already surpasses few-shot GPT-4 by 2.5 COMET and 3.8 BLEURT, with further improvements from larger STMs. This validates the practical claim that the framework avoids expensive LLM re-training.

3. **Pivoting mechanism works as advertised**: Using an English-centric STM as pivot, SCALE improves GPT-4 by an average of 6 COMET points across eight translation directions from Lao (both low- and high-resource targets). This confirms the intuition that STM outputs can guide the LLM's language-bias exploitation.

4. **Ablation cleanly isolates components**: Table 3 systematically ablates confidence scores, ICL examples, and STM quality. The gradient from zero-shot (81.4) → one-shot (81.7) → ten-shot (82.1) shows that ICL provides genuine added value beyond simply providing a reference translation.

## Weaknesses

### Fatal
None.

### Major
1. **No variance or significance reporting**: All results (Tables 1–3, multipath, pivoting) are single point estimates without standard deviations, confidence intervals, or significance tests. Several improvements are modest (e.g., asm_Beng: +1.0 COMET over NLLB; +0.7 COMET from zero-shot to full 10-shot SCALE). Without repeated runs or uncertainty quantification, readers cannot assess whether these differences are reliable or could reverse under different seeds/prompt orders. This is the most significant methodological gap given that the paper's empirical claims rest on small deltas.

2. **Pivoting results are under-reported**: The pivoting experiment (Section 4.2) reports only aggregate averages ("6 COMET points" in abstract; "6.8 vs 5.2" avg. gains for high/low-resource). No per-language numerical breakdown is given in text or a table — the data is only in Figure 2 (a figure). Additionally, there is no comparison against a simple English-pivot baseline (e.g., GPT-4 translating Lao→English, then English→Y), which would isolate the benefit of SCALE's STM-guided pivot over naive chain-translation.

3. **Updating experiment limited to one language pair**: The continual-learning demonstration (Section 4.3) is conducted on Xhosa→English only. While the results are positive, a single language pair cannot establish whether the pattern generalizes. Adding even one more language pair would substantially strengthen this claim.

### Minor
4. **Overclaimed role of the ICL mechanism**: The paper claims triplet ICL "unlocks" refinement ability (Abstract, Section 2). However, the zero-shot ablation (no ICL examples, just STM output + instruction) achieves 81.4 COMET vs. the full 10-shot SCALE's 82.1 — meaning 86% of the gain over GPT-4 (78.8) is already achieved without any ICL examples. The ICL structure provides marginal additional benefit (0.7 COMET), not a qualitative "unlocking." The paper should temper the mechanistic claim or add a direct prompt-level comparison (e.g., an explicit "correct this translation" instruction vs. the current generic translation instruction).

5. **Limited robustness to weak STMs**: The zero-shot-M2M variant (M2M100 as STM, zero-shot) scores 76.4 COMET, below GPT-4 alone at 78.8. The paper frames this as a robustness test, but the result shows SCALE **degrades below the baseline LLM** when the STM is weak. The paper's claim of "strong robustness" (Section 4.3, point 3) should be qualified — the framework improves over a poor STM (68.0→76.4) but still falls short of the standalone LLM. This is a practical limitation worth explicit discussion.

6. **Decoding strategy for STM multi-path sampling underspecified**: The paper describes generating a "set ℤ" of multiple paths from the STM (Section 2.1) but does not specify the decoding parameters (temperature, top-k, beam width, number of beams). This affects both reproducibility and the interpretation of the multi-path results (Table 2), as the diversity of sampled paths depends critically on these settings.

### Trivial
None.

## Nice-to-Haves
- **Explicit "refine this translation" prompt baseline**: The paper's zero-shot ablation uses a generic translation instruction with an STM reference. A targeted "correct the errors in the following translation" prompt would more directly test whether the ICL structure specifically, versus any form of STM-guidance, is responsible for the gains.
- **Comparison with a candidate-ranking baseline**: Using the LLM to score/select among multiple STM candidates (without ICL) would contextualize whether the triplet-ICL approach has advantages over simpler hybridization strategies.
- **Human evaluation on a subset**: The paper relies entirely on automatic metrics. A small human evaluation on 1–2 low-resource directions would strengthen confidence in the reported quality improvements, given known metric biases.

## Removed Points
These points are flagged to be removed, treat them with caution — they either misread the paper, are scope-creep, or are addressed by the paper:
- **"Missing baseline: direct post-editing without ICL"** — The paper already includes a zero-shot ablation (Table 3) that provides STM output + instruction without ICL examples. The reviewer's request for an explicit "correct this" prompt is a valid refinement but the core comparison exists.
- **"Missing comparison with other hybrid approaches (candidate ranking, retrieval-augmented)"** — These are related but methodologically different approaches. The paper already compares against strong individual baselines (NLLB, GPT-4, Microsoft Translator). Requesting these baselines is scope-creep.
- **"No comparison against fine-tuning the LLM with LoRA"** — The paper's core claim is about ICL-based collaboration, not about whether LoRA fine-tuning is superior. Different research question.
- **"Only Flores-200"** — Standard benchmark for multilingual MT. Acknowledged by the paper.
- **"Demonstration selection details absent"** — The paper cites Agrawal et al. for the strategy, which is standard practice.
- **"spBLEU discrepancy"** — The paper explicitly discusses this, cites prior work finding the same pattern (Vilar et al., 2023; Kocmi et al., 2023). Not a weakness.
- **"Multipath diminishing returns weakens the claim"** — The paper simply reports that multipath improves quality; diminishing returns don't contradict the claim.
- **"Latency not measured on GPT-4"** — The paper explains why BLOOM-175B is used instead (GPT API latency is not representative) and acknowledges this as a limitation with speculative decoding as future work. Reasonable.
- **"No human evaluation"** — Nice-to-have but not required. The paper uses three neural metrics (COMET-22, COMETKiwi, BLEURT) plus two lexical metrics — a comprehensive automatic evaluation suite.

## Novel Insights
None beyond the paper's own contributions. However, the observation that simply providing an STM-generated reference in the prompt (zero-shot) accounts for the majority of SCALE's improvement over GPT-4 is an important nuance that the paper could discuss more candidly — it suggests the framework's primary value is in grounding the LLM with a concrete draft, with ICL examples providing a secondary refinement signal.

## Suggestions
1. **Add variance estimates**: Run the main experiments (Table 1) at least 3 times with different seeds and report mean ± std. For the ablation, report whether differences between variants are significant (e.g., via paired bootstrap over test sentences).
2. **Expand pivoting reporting**: Include a table with per-language COMET, BLEURT, and spBLEU for the pivoting experiment. Add a GPT-4 English-pivot baseline (Lao→English→Y).
3. **Add at least one more language pair to the updating experiment** (e.g., Amharic→English) to demonstrate generality.
4. **Temper the ICL claim**: Acknowledge that most of the gain over GPT-4 comes from providing the STM output as a reference (zero-shot), and that the ICL structure adds a smaller but consistent improvement.
5. **Specify STM decoding parameters** (temperature, top-k/beam width) used for multi-path sampling.
