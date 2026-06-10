## Summary

This paper introduces ReSpect, a method where an LLM decodes implicit feedback signals from multi-turn human interactions (e.g., rephrasings, frustration, approval) and uses those signals to retrain itself — without any external annotations or solicited feedback. The method is deployed in a new grounded interaction scenario (MultiRef) using tangram shapes, with live human participants on MTurk across multiple rounds of continual learning. The best variant (BP) improves task completion from 31% to 82% over six rounds.

## Strengths

1. **Conclusive real-world demonstration of self-improvement from implicit feedback alone**: The BP variant improves interaction-level success rate from 31% to 82% (a 51% absolute gain) across six rounds of live human deployment, totaling 7,230 interactions and 55,004 utterances (line 291, 311). This directly supports the paper's central claim that retrospective learning from natural conversational signals works without external annotations, and is measured via real deployment rather than static benchmarks.

2. **Rigorous control ruling out user adaptation as a confound**: The paper redeploys the initial policy concurrently alongside the final BP round (control in Figure 3, lines 329–331). Its success rate stays flat (31% → 33%), cleanly isolating that policy improvement — not human adaptation — drives the gains. This is a strong methodological check that many similar studies omit.

3. **Empirical validation that LLMs can decode implicit feedback even when failing at the task**: The feedback decoder uses the original, un-fine-tuned Idefics (line 249) and achieves "above 90% precision consistently" when collapsing positives and neutrals (line 355). Performance is stable across rounds, confirming robustness to distribution shift. This directly supports the paper's hypothesis that implicit feedback occupies a decodable linguistic subspace accessible even to models that cannot solve the task, and the design choice to freeze the decoder is honestly conservative.

4. **Well-motivated and principled task design**: MultiRef's combinatorial solution space (exponential in the number of images, line 117) and abstract tangram stimuli create a challenging task that naturally elicits multi-turn interactions with rich implicit feedback, while remaining accessible to crowd workers. The design is grounded in cognitive science literature (Clark, Schober, Goodman) and Gricean maxims (line 128).

5. **Transparent reporting of continual learning dynamics**: The paper reports plateaus, BK's divergence and illegal outputs (line 363), and runs a separate experiment with more expressive LoRA adapters to investigate the plateau (footnote, line 309). This honesty about the complexities of continual learning — rather than cherry-picking only monotonic results — strengthens the paper's credibility.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Ambiguity around the LoRA adapter branch and its relation to the headline 82% result**: The paper reports that BP "plateaus, and even shows a temporary decrease in performance, before resuming its improvement" (line 309), with a footnote describing a "separated deployment" branching from round 3 with more expressive LoRA adapters that "allows the model to continue its monotonous improvement." Line 312 then states "at the last round, following the plateau, bp interaction success rate improves by 5% (77%→82%)." The relationship between these two descriptions is ambiguous: is the 77%→82% improvement from the main BP run or from the LoRA-enhanced branch? A careful reading suggests the 82% is from the main run (the branch is described as a separate investigation), but the juxtaposition at the same rounds (4 and 5) and the phrase "allows the model to continue its monotonous improvement" creates genuine reader uncertainty. This matters because if the headline result depends on a mid-experiment hyperparameter change introduced after observing a plateau, the claim that the method alone drives the full improvement is weakened. The authors should explicitly clarify which condition produced the 82% figure.

2. **Truncated comparison between system variants limits the strength of comparative claims**: All six system variants are run for only three rounds (plus initial deployment); only BP is extended to six rounds (line 262). The paper concludes that "positive-only systems perform better" and that supervised learning outperforms REINFORCE and KTO (lines 336–341). Three rounds is a short horizon — KTO and REINFORCE methods may have slower learning curves that could overtake SFT with more data. The BK variant diverges (line 362), but this could reflect training instability from hyperparameter choices rather than a fundamental limitation. The cost constraints are openly acknowledged, but the comparative conclusions should be tempered accordingly.

3. **Quantitative evaluation of the feedback decoder is sparser than the method's reliance on it warrants**: The paper states "above 90% precision consistently" for the binary decoder when collapsing positives and neutrals (line 355) and shows confusion matrices (Figure 7), but does not report exact numeric precision, recall, or F1 scores in prose for the full three-class setting. We do not know the decoder's precision on negative signals, its recall, or how these vary across rounds for individual feedback categories. Given that the entire method hinges on the decoder's reliability, a prose table with per-class and per-round metrics is expected rather than reliance on visual inspection of confusion matrices.

### Trivial
- The mapping from "six rounds" (abstract, caption) to the experimental design (all systems get rounds 0–3, BP also gets rounds 4–5) could be made more explicit, e.g., with a table mapping round numbers to conditions.

## Nice-to-Haves
- **A ground-truth calibration baseline** would help quantify the informational loss from using implicit feedback vs. perfect per-turn success signals. The paper's thesis is that implicit feedback can substitute for explicit annotations, and the human-human baseline (100%) provides an upper bound. However, a baseline trained on ground-truth per-turn signals would isolate how much of the remaining gap is due to signal quality vs. other factors (e.g., learning method).
- **Empirical characterization of the "constrained subspace"** the paper hypothesizes. The paper repeatedly asserts that implicit feedback signals occupy a narrow linguistic space (line 29, line 33) but never analyzes this — e.g., via vocabulary overlap, utterance length distributions, or frequency of specific linguistic markers. This would strengthen one of the paper's motivating claims.
- **Systematic analysis of variance across human workers** would strengthen robustness claims. The paper mentions "only three outlier workers" (line 374) drove the late-round vocabulary increase, but does not report how many unique workers participated or whether results are robust to removing individual workers.

## Removed Points
These points were assessed against the paper and removed for the following reasons:

1. **"The 82% figure may depend on the LoRA adapter change — structural/fatal issue"**: After careful reading of lines 309–312, the paper attributes the 82% figure to the main BP run ("bp interaction success rate improves by 5% (77%→82%)") and describes the LoRA branch as a "separated deployment" (footnote, line 309). The critic's framing that this is a "structural" issue affecting the "believability" of the headline claim is not supported by the paper as written. However, the presentation is genuinely ambiguous, so this is retained as a Minor weakness (item 1 above) rather than fully removed.

2. **"No baseline using ground-truth task signals"**: The paper's stated scope explicitly avoids privileged information ("We assume no access to any auxiliary annotation or privileged information," line 187). Asking for a ground-truth baseline asks the paper to do something antithetical to its contribution framing. Moved to Nice-to-Have.

3. **Missing related works**: Not included as this cannot be verified without external sources, per instructions.

4. **Formatting/style/typo/appendix criticisms**: Removed per instructions as these likely stem from parser artifacts, not author errors.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Clearly state whether the 82% result comes from the main BP run or the LoRA-enhanced branch. If from the main run (as the text suggests), state this explicitly and separate the LoRA analysis more cleanly (e.g., into a dedicated ablation section).
2. Report exact precision, recall, and F1 for the feedback decoder (binary and ternary settings, all three classes, per round) in a prose table rather than solely through confusion matrices.
3. Temper the comparative claims about SFT > REINFORCE > KTO, given that all non-BP variants were only run for 3 rounds.
4. Add a table mapping each round to the number of training interactions, LoRA settings, and which system variants were active.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>