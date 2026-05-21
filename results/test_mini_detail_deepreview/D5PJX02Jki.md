Now I have sufficient calibration data. Let me write the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths

### S1: Novel and well-motivated idea with clean theoretical derivation
The observation that standard RoPE discards the imaginary component of the complex-valued attention score is both correct and previously under-explored. The paper derives the characteristic curve of imaginary attention (Equation 5, Figure 1) as a sine integral that decays more slowly than the cosine-based real attention, providing a principled mathematical reason for why re-incorporating the imaginary component should benefit long-context modeling. This is a genuinely novel angle on RoPE improvement that goes beyond existing interpolation- or scaling-based approaches.

### S2: Clear empirical gains for RoPE++EC on long-context tasks
Table 2 shows that RoPE++EC (equal cache, doubled heads) substantially improves over vanilla RoPE on synthetic long-context benchmarks. For the 376M model, the average RULER score improves from 18.8 to 25.0 (a 33% relative gain) and BABILong from 11.0 to 16.1. At 776M, the gains are consistent: RULER 29.4 vs 27.4 and BABILong 24.1 vs 22.8. These are concrete, reproducible numbers that directly support the claim that imaginary attention enhances long-context capability.

### S3: Cache-efficiency benefit of RoPE++EH is convincingly demonstrated
RoPE++EH (equal head count, halved KV cache) achieves broadly comparable results to vanilla RoPE while cutting KV cache in half. Figure 4 demonstrates lower memory cost and faster decoding across context lengths up to 128K. Table 1 shows RoPE++EH matches or slightly exceeds RoPE on short-context tasks (e.g., 42.5 vs 42.0 average at 776M), and Table 2 shows competitive long-context performance (28.6 vs 27.4 average RULER at 776M). This validates the claim that imaginary attention can substitute for real attention heads with meaningful memory savings.

### S4: Noise-ablation analysis provides direct empirical support for the theoretical claims
Section 5.2 (Figure 5j) shows that corrupting imaginary attention with Gaussian noise degrades RULER-4k accuracy more than corrupting real attention (5–8 point gap at σ=1.0). This is a clever causal validation that confirms imaginary heads are more important for long-context modeling, bridging the gap between the theoretical sine-integral derivation and observed behavior.

### S5: Compatibility with established long-context extension methods
Section 5.3 and Table 3 demonstrate that RoPE++ works with both Linear PI and YaRN interpolation methods, achieving the best average RULER and BABILong scores in 5 out of 6 model/interpolation combinations. This shows the proposal integrates with standard practice rather than being a niche trick.

## Weaknesses

### Major

**M1: Claims overstated for RoPE++EH on long-context benchmarks.**  
The abstract and contributions claim that "Both RoPE++EH and RoPE++EC outperform vanilla RoPE and other position embeddings on average across short- and long-context benchmarks" (lines 16, 40). However, Table 2 shows RoPE++EH underperforms standard RoPE on several long-context sub-benchmarks: at 376M, RULER avg 18.2 vs 18.8; at 776M, BABILong avg 19.4 vs 22.8. The 376M long-context short-task average (Table 1, 39.8 vs 39.6) shows only a marginal 0.2 point gain. The paper's own introduction (line 36) more accurately describes RoPE++EH as achieving "comparable results." The gap between the sharp "outperform" claim and the mixed evidence weakens the paper's credibility. The authors should precisely delineate which variant is being claimed to do what.

**M2: No naturalistic long-context evaluation tasks.**  
All long-context evaluation uses synthetic benchmarks (RULER, BABILong). While these test certain retrieval and reasoning capabilities, the paper lacks evaluation on real-world long-context tasks such as document summarization, long-context QA (e.g., LongBench, NarrativeQA), or many-shot in-context learning. This makes it difficult to assess whether the synthetic gains translate to practical applications. For a paper positioning itself as a contribution to "long-context LLMs," this is a significant gap.

**M3: Model scale limited to 376M and 776M parameters.**  
All experiments are at sub-1B scale. The absolute scores on long-context tasks remain low (e.g., best RULER avg 29.4 at 776M), and it is unclear whether the observed gains hold at the 7B+ scale where long-context capability is practically meaningful. Demonstrating results at even 2.7B would substantially increase confidence in the method's scalability. While pre-training at larger scales is expensive, a focused comparison at one medium scale (e.g., 1.5B–2.7B) would address this gap.

### Minor

**m1: No comparison against a simple "doubled-heads vanilla RoPE" baseline.**  
RoPE++EC doubles attention heads via the imaginary component at the same cache cost, but a natural baseline is simply doubling the number of standard RoPE heads (all real) with proportional QKV parameters. Without this ablation, it is unclear whether the gains come from the imaginary rotation specifically or simply from having more attention heads. This baseline would cleanly isolate the benefit of the imaginary component.

**m2: No error bars or statistical significance reported.**  
None of the accuracy numbers in Tables 1–3 include variance estimates. Given that many margins are small (e.g., 0.2–0.5 points on short-context averages), readers cannot assess whether differences are reliable. This is standard practice for large-scale benchmarks where single-run evaluation is the norm, but reporting at least one representative significance measure would strengthen the presentation.

**m3: Noise-ablation analysis limited to a single task and configuration.**  
The noise-ablation experiment (Figure 5j) only tests RULER-4k at two model sizes. The claim that "imaginary attention plays a dominant role in long-context modeling" would be stronger with a sweep across multiple context lengths (e.g., 4k, 8k, 16k) and multiple tasks (BABILong as well). The attention pattern visualizations (Figure 5a–d, f–i) show only two layers per model, which is anecdotal.

### Trivial

**t1:** Figure 4 shows TPOT (Time Per Output Token) but the y-axis label reads "higher is better" which is conceptually correct (throughput) but the acronym TPOT conventionally refers to latency (lower is better). This should be clarified or a different metric name used.

**t2:** Some table column labels are ambiguous (e.g., "LMB" in Table 1 could be expanded for clarity).

## Nice-to-Haves
- Ablation varying the \(-\pi/2\) rotation angle to demonstrate its optimality.
- Ablation removing the shared \(W_q\) constraint (separate projections for real/imaginary heads) to confirm the coupling is essential.
- A small-scale length-extrapolation experiment (training at 2k, testing at 4k+) to directly verify the extrapolation argument in Section 3.4.
- Comparison against Yarn/Linear PI without RoPE++ as separate baselines (already partly addressed in Table 3, but more systematically).

## Removed Points
- **"Efficiency comparison is only against standard RoPE, not against other cache-reduction methods"**: Removed. RoPE++ is fundamentally a position-embedding method, not a cache-compression method. The cache savings of RoPE++EH are a secondary benefit of the architectural structure, and comparing against MQA/GQA would demand the paper solve an orthogonal problem outside its stated scope. The efficiency claim is valid for the comparison made (against vanilla RoPE).
- **"The theoretical link between the characteristic curve and actual attention patterns is incomplete"**: Partially removed; the core concern (anecdotal visualizations) is kept as m3 (limited scope of noise ablation), but the broader concern about the theoretical derivation being "incomplete" is removed because the paper does derive the characteristic curve mathematically and validate it with the noise ablation.
- **"Related work should contrast more explicitly with complex-valued attention mechanisms"**: Removed. The paper already cites Wang et al. 2025 and Lee et al. 2022 (line 50) and explicitly states that "the characteristics and functionality of the imaginary component in position embedding remain unexplored" by prior work. The contrast is adequately drawn.
- **"Missing parts: hyperparameter sensitivity of rotation angle"**: Moved to Nice-to-Haves (not a core weakness).
- **"Ablation of head-coupling"**: Moved to Nice-to-Haves (not a core weakness; the paper provides a theoretical justification for the coupling).
- **"Length-extrapolation argument more rigorous"**: Moved to Nice-to-Haves. The argument is heuristic but clearly reasoned; a synthetic experiment would strengthen it but is not required for the core contribution.
- **Strength Finder generic strengths dropped**: "The paper addresses an important problem" and similar generic statements removed as they lack specificity. Strengths kept are those grounded in concrete, verifiable evidence from the paper.
- **"No evaluation on real-world tasks"** was kept as M2.

## Novel Insights
The reviews collectively surface one interesting insight that goes beyond the paper's own analysis: the question of whether RoPE++EC's gains come from the imaginary component or simply from having twice as many attention heads. Neither reviewer identifies any confounding factor in the noise ablation (which causally links imaginary heads to long-context performance), but the absence of a doubled-heads vanilla RoPE baseline means the paper's core claim—that the *imaginary rotation itself* is responsible for the gains—remains incompletely isolated. This is a well-defined ablation the authors can run to strengthen their paper significantly.

## Suggestions
1. **Tone down the claim for RoPE++EH** from "outperforms" to "delivers comparable performance with half the KV cache." This aligns with the introduction's own description and makes the paper more defensible.
2. **Add a doubled-heads vanilla RoPE baseline** for RoPE++EC. This is the single most informative ablation: if RoPE++EC with N heads beats 2N vanilla RoPE heads, the imaginary rotation is clearly beneficial; if comparable, the gains are from capacity alone.
3. **Run at least one naturalistic long-context evaluation** (e.g., LongBench's summarization or QA tasks) and one experiment at a larger scale (2.7B) to address scalability concerns.
4. **Report error bars** for at least the main results (Tables 1–2) to allow significance assessment.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:**
- Weak band (avg < 3.5): Retrieved papers scored 2.5–3.0. These are clearly below the current paper, which has a well-defined method, theoretical derivation, and systematic experiments. The current paper is substantially stronger.
- Middle band (3.5–7.5): Retrieved several relevant anchors including:
  - *Round and Round We Go!* (avg 6.20, Accept) — Analysis paper on RoPE internals at 7B scale. Similar theoretical depth; current paper has a cleaner practical contribution but smaller scale. Current paper is slightly weaker.
  - *Scaling Laws of RoPE-based Extrapolation* (avg 5.00, Accept) — Theoretical analysis validated at 7B/13B. Current paper has more novel architectural contribution but smaller scale. Comparable.
  - *TAPE* (avg 6.00, Reject) — New positional encoding with complex methodology but mixed experimental validation. Current paper is cleaner and more directly validated. Comparable or slightly stronger.
  - *Wavelet-based Positional Representation* (avg 5.25, Accept) — Similar experimental scale. Current paper has stronger theoretical motivation and clearer results. Slightly stronger.
  - *CLEX* (avg 6.50, Accept) — Validated at 7B scale on LongBench. Current paper has weaker experimental validation. Weaker.
- Strong band (avg > 7.5): Papers like *Retrieval Head* (8.00) and *Differential Transformer* (8.00) — These are substantially more comprehensive, with experiments at 7B+ scale, rigorous evaluation, and deeper analysis. The current paper is clearly weaker.

**Initial bracket:** Narrowest plausible range is [4.5, 6.5].

**Round 2 — Narrowing within bracket:**
- *Contextual Position Encoding* (avg 5.25, Reject) — Interesting idea but limited in scale. The current paper has a cleaner mechanism and comparable experimental setup. Slightly stronger.
- Additional middle-band anchors confirm the range [5.0, 6.0].

**Final comparison:** Against the middle-band anchors, the current paper's clean theoretical motivation and clear empirical signal (especially for RoPE++EC) place it on the stronger side of the 5.0–6.0 range, but the limited model scale, lack of naturalistic long-context tasks, and overstated claims hold it back from the 6+ level. I judge the paper comparable to the Wavelet paper (5.25) and slightly stronger than the Scaling Laws paper (5.00), but weaker than CLEX (6.50) and Round and Round (6.20). Score: 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>