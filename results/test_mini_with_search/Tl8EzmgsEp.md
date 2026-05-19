Now I have thorough verification of the paper content. Let me write the final consolidated review.

## Summary
This paper investigates the look-ahead capabilities of the Leela Chess Zero policy network, extending prior work (Jenner et al., 2024) to analyze whether the model encodes information about future moves up to seven steps ahead and whether it considers alternative move branches. Using activation patching, probing, and ablation across curated chess puzzle sets, the paper finds that look-ahead is highly context-dependent (varying by the relationship between move destination squares and whether the sequence leads to checkmate), that attention head L12H12 appears to "move information backward in time" from future move squares in pattern-sensitive ways, and that the model simultaneously weighs alternative move sequences. The paper introduces a puzzle-set notation that enables finer-grained disentanglement of behavior across longer move sequences than prior work allowed.

## Strengths

- **Extension of look-ahead analysis to 7 moves and alternative branches.** Section 3 presents probing results (Figure 3) for puzzle set 1123456 showing the 7th-move square's probe accuracy is non-negligible versus a random model baseline, and activation patching (Figure 2) shows fifth-move squares causally affect model output. The alternative-move analysis (Figure 6) shows that patching alternative-branch squares affects the model's probability of choosing the main-branch move, providing evidence the model considers multiple lines of play. These extend the known depth of look-ahead beyond prior work (Jenner et al., 2024).

- **Evidence that similar pattern-matching mechanisms apply across different time horizons.** The paper shows (Section 3) that attention head L12H12 responds to the same patterns (AAC, ABC, ACC) whether they apply to moves 1-2-3, 3-4-5, or 5-6-7, suggesting "time-insensitive" mechanisms. Ablation results (Figure 5) support that L12H12 moves information backward from both third- and fifth-move squares.

- **Introduction of a puzzle-set notation that enables systematic analysis of longer sequences.** Section 2.4 introduces the notation \(s_1s_2\ldots s_n\) to label puzzles by whether consecutive move destination squares are the same or different. This allows disentangling behavior for 5- and 7-move puzzles, which prior work was unable to do (bundling higher moves into third-move results).

- **Use of complementary interpretability techniques (probing, patching, ablation) to reveal different facets of look-ahead.** The paper demonstrates concretely that probing reveals information encoding even where patching shows no strong causal effect (e.g., opponent moves), while ablation pinpoints specific attention heads responsible for moving look-ahead information.

## Weaknesses

### Major

- **Results are almost entirely qualitative; key numerical values are absent from the text.** The results section describes figures with terms like "non-negligible," "weak," "moderate," and "strong" without reporting any of the underlying numerical values. For probing (Figure 3): "the probe's accuracy decreases as we look into more distant future move squares, with the 7th move square's accuracy being considerably low, but still non-negligible" — but the actual accuracy numbers are never stated, the random baseline accuracy is never stated, and no per-layer values are given. For patching (Figures 2, 4): effect sizes are described qualitatively. The only numerical value given in the text is "the highest being 0.73, for L12H12" (Figure 4 caption). The paper cannot be properly evaluated when the evidence lives entirely in figures without any numbers in the prose. This is not a formatting artifact — the text itself should contain the evidence.

- **Puzzle subset sizes are not reported, so statistical reliability cannot be assessed.** The paper states "Only sets with more than 50 puzzles are considered" (line 84) and gives top-level dataset sizes (22k, 2.2k, 609), but never reports how many puzzles fall into each specific combinatorial subset (11223, 11234, 11233, 1123456, M112, N112, etc.). With many fine-grained splits — especially the checkmate vs. non-checkmate subsets — per-cell sample sizes could easily be in the tens or low hundreds. Claims about differential responses of attention heads (e.g., L12H12 strong on AAC, weak on ACC; L12H12 dominant in checkmate vs. L12H17 in non-checkmate) rest on these splits. Without sample sizes or any measure of variance or statistical significance, the reader cannot distinguish robust patterns from noise.

- **The central mechanistic claim that L12H12 "moves information backward in time" is inferred from indirect, correlational evidence.** The paper infers this role from (a) ablation of L12H12 reducing performance, (b) patching the future-move square reducing performance, and (c) the head being important specifically for pattern AAC. But correlation between head importance and a square's causal role does not alone establish that the head *moves information* along that direction. The paper does not directly trace information flow — e.g., by showing that patching the head's output at the first-move representation mimics patching the third-move square, or by confirming via attention pattern analysis which positions the head writes to. The paper uses "we hypothesize" language (line 104) which appropriately signals tentativeness, but the title, abstract, and conclusion present these as established findings (e.g., "demonstrating," "showing"). The "time-insensitive pattern matching" claim rests only on qualitative similarity of patching patterns, with no explicit test of time-translation invariance.

### Minor

- **Critical experimental details are underspecified.** Probing is described as using "linear probes" (line 55), but no details are given on classifier architecture, training set size, train/test split, or how the random model baseline is constructed. For patching, the corrupted board construction procedure is referenced to Jenner et al. (2024) but not described in the paper, making the analysis not self-contained. For the alternative-move analysis, the corruption procedure is similarly unclear.

- **No statistical tests or multiple comparison corrections are reported.** The paper tests many attention heads (15 layers × multiple heads) across many puzzle sets. The strongest findings could simply be the largest in a long tail. No correction for multiple comparisons is mentioned, and no confidence intervals or significance tests accompany the claims of differential head importance across puzzle sets.

- **No baseline comparisons beyond a vague "random model."** Probing accuracy is described as compared to "a random model" but the nature of this baseline is unspecified (random weights? random labels?). No comparison to a naive most-frequent-class baseline or to patching an irrelevant control square is reported.

### Trivial

- Several figure references are incomplete in the parsed text (e.g., "see Fig." without a number, line 82, 121). This is likely a parser artifact from figure placement in the PDF, not an author error.

## Nice-to-Haves

- Attention pattern analysis showing where L12H12 attends (first-move square to later-move square) would provide more direct evidence for the "moving information backward" claim. Showing that corrupting that specific attention direction degrades performance would strengthen the causal argument.
- A table with per-puzzle-set sample sizes and effect sizes (mean log-odds reductions with confidence intervals) would allow readers to assess the statistical reliability of the findings.
- A limitations section acknowledging that results come from a single finetuned model, that puzzle data may differ from self-play, and that findings may not generalize to other architectures.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper is an extended abstract, not a full paper" (Harsh Critic)** — Removed as hyperbole. The paper has concrete experimental results presented across multiple figures and sections. The issue is the *format* of the evidence (qualitative descriptions of figures), not its absence.

2. **"Reproducibility: code and data not available until publication" (Harsh Critic)** — Removed per instruction: do not flag reproducibility issues about code/data release schedules. The paper states code/data will be released upon publication, which is standard.

3. **"Missing related works" (Harsh Critic)** — Removed per instruction: do not mention missing related works as I cannot independently verify their existence.

4. **"Typos, formatting issues" (Harsh Critic section-by-section notes)** — Removed per instruction: parser artifacts and formatting nitpicks.

5. **Strength: "This paper addressed an important problem" / "targeted an interesting question"** — Removed as generic/superficial. The strength must be concrete and specific to the paper's actual content.

6. **"The paper does not discuss that all results come from a single finetuned model" (Harsh Critic Strengthening section)** — WEAKENED to Nice-to-Haves because this is a scope observation, not a flaw in what the paper does (it explicitly states it uses "a finetuned version of the model, trained and used by Jenner et al. (2024)").

7. **"The paper does not identify a specific gap this paper fills beyond 'longer-term planning and alternative move considerations'" (Harsh Critic Related Work notes)** — Removed. The paper explicitly states its gap: "Jenner et al. (2024) bundles the higher move squares... into the third move square results, which makes it difficult to see if the model is able to concretely look ahead past the third move" (line 68). This is a concrete gap.

## Novel Insights

The harsh critic's observation about the qualitative nature of the results section is not merely a presentation nitpick — it reveals a structural issue where the paper asks the reader to accept conclusions about the *strength* of evidence ("non-negligible," "strong," "weak") without providing the quantitative anchors needed to evaluate those judgments. The strength finder's positive points are all *directionally* correct (the paper does have 7-move probing results, alternative-move analysis, etc.) but systematically overstate the robustness of the evidence — a pattern that emerges because the qualitative framing in the paper itself invites optimistic readings. The gap between the paper's claims ("demonstrating," "showing") and its evidence ("we hypothesize," qualitative trends) is the single most important issue to address.

## Suggestions

1. **Report all key numerical results in the text.** Every claim about probing should be accompanied by accuracy numbers (by layer, for each future-move square). Every patching claim should include mean log-odds reduction with confidence intervals. Provide a table of per-puzzle-set sample sizes and effect sizes.

2. **Conduct and report explicit statistical tests** for the claimed differences between puzzle sets (e.g., does AAC reliably produce larger patching effects than ACC across puzzles?).

3. **Add direct mechanistic evidence for L12H12's role.** Show attention patterns (does L12H12 attend from first-move square to later-move square?) and show that corrupting that specific attention direction mimics the effect of patching the future-move square.

4. **Disclose puzzle subset sizes** for every puzzle set and subset analyzed (11223, 11234, 11233, 1123456, M112, N112, etc.) so readers can assess the reliability of per-set findings.

## Score and Decision

**Round 1 bracket**: 3.5 – 5.0. Anchors used: Path Channels Sokoban (6.00, Accept) — clearly stronger with detailed mechanistic evidence; Internal Planning in LMs (5.00, Accept) — stronger, proposes novel method; ChessQA (4.50, Reject) — different contribution type, comparable presentation quality; VLM Interpretability (4.00, Reject) — similarly uses probing + intervention with insufficient quantification.

**Round 2 anchoring**: Narrowing within 3.5–5.0. The paper is closest in quality to the VLM interpretability paper (4.00, Reject, scores 2/4/4/6) — both use probing + intervention to study model internals but lack sufficient quantitative rigor. It is clearly weaker than the Path Channels paper (6.00) which provides specific channel-level mechanisms with ~99% causal intervention success rates. Compared to Internal Planning in LMs (5.00, Accept), the current paper lacks a novel methodological contribution and has less rigorous validation. Papers at 3.5–4.0 (ChessArena at 3.33, Reject; Causal Explanations at 4.00, Reject; Strategically-Linked Decisions at 3.50, Reject) are either less topically relevant or have more fundamental methodological issues.

**Final assessment**: The paper addresses an interesting question and uses a reasonable multi-method approach, but its evidence is presented in a predominantly qualitative manner (no probing accuracy numbers, no effect sizes, no per-subset sample sizes, no statistical tests). The core findings are plausible and potentially valuable, but the paper does not meet the evidential standard for publication in its current form. A major revision that adds full quantitative reporting, statistical validation, subset sizes, and more direct mechanistic evidence could make this publishable.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>