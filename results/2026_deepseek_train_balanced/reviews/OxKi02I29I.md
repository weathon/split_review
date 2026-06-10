## Summary

This paper makes two interconnected contributions: (1) a diagnostic study revealing that LLM-based approaches achieve surprisingly high accuracy on long-video QA benchmarks with minimal or even zero video-specific information (45.8% on EgoSchema-S with no video, 55.8% with a single frame), and (2) the MVU framework that extracts three object-centric modalities from video (global objects, spatial locations, motion trajectories) using off-the-shelf tools, fuses them via natural language, and applies likelihood selection for efficient inference. The diagnostic finding—that existing benchmarks are substantially solvable from world knowledge plus minimal visual context—is arguably the most novel contribution.

## Strengths

- **Diagnostic discovery that world knowledge dominates existing video QA benchmarks.** The paper concretely demonstrates that a text-only LLM (no video input) scores 45.8% on EgoSchema-S and 40.1% on NextQA-T, and a single-frame VLM reaches 55.8%—both far above 20% random and competitive with or exceeding several published multi-frame methods (Table 1). This is a clean, reproducible measurement that raises substantive questions about what these benchmarks actually measure.

- **Object-centric pipeline is both more accurate and more efficient than frame-level descriptions.** In a controlled comparison (Table 7, lines 490–494), replacing MVU's object-centric inputs with LLoVi-style frame descriptions at the same 16 frames yields 56.2% at 4.72s, while MVU achieves 60.3% at 2.42s. This directly demonstrates that object trajectories + spatial grounding provide a better signal-to-noise ratio than generic captions, and at lower cost.

- **Likelihood selection yields a Pareto improvement over generation-based video QA.** The LS ablation (Table 6, lines 470–472) shows likelihood selection achieving 60.3% at 2.42s vs. standard generation at 56.4% at 12.7s, and far below the 381s of prior work (LLoVi). Both accuracy and speed improve simultaneously.

- **Incremental ablation quantifies each component's contribution.** Table 5 (lines 442–446) cleanly decomposes gains: GOI +0.6pp, OSL +2.2pp, OMT +1.7pp over the single-frame VLM baseline. Every component contributes positively, and the cumulative effect (60.3% vs. 55.8%) is credible and well-documented.

- **Cross-domain evaluation on robotics underscores that video-specific information genuinely drives gains.** On the Open X-Embodiment benchmark (Table 3), the modality-constrained baselines perform poorly (near random), confirming that the MVU pipeline's video-specific information—not world knowledge—is what provides the aggregate improvement (30.4% vs. 28.5% baseline). This strengthens the case that the object-centric pipeline does meaningful work.

## Weaknesses

### Fatal
None.

### Major
- **The paper's framing overstates what the evidence supports, particularly around SOTA claims and the magnitude of the object-centric contribution.** The abstract states "state-of-the-art performance across multiple video understanding benchmarks" with no caveats. In the body, the SOTA claim is carefully qualified ("under zero-shot operation with no video level training," excluding GPT-4 variants, de-emphasizing trillion-parameter models), but these caveats are absent from the abstract's headline. Moreover, the margins within this qualified slice are modest: 36.7→37.6 on full EgoSchema (+0.9pp), 54.3→55.4 on NextQA (+1.1pp). The paper would benefit from stating these margins explicitly in prominent locations rather than presenting the results as unqualified SOTA. This is not a fatal flaw—the results are real and positive—but the gap between the promotional framing and the measured margins is noticeable.

- **No discussion of limitations.** The paper contains no limitations section, which is a meaningful omission given the nuanced findings it reports. The paper should discuss: (a) error propagation from the captioner→detector→tracker pipeline, (b) question categories where the object-centric pipeline does not help (or hurts), (c) the fact that a single-frame VLM already captures the majority of the gain, and (d) regression cases on robotics data. This omission weakens the paper's scholarly completeness, though it does not invalidate the results.

### Minor
- **The raw accuracy gain of the full MVU pipeline over the single-frame baseline is modest (+4.5pp on EgoSchema-S, +4.2pp on NextQA-T), while the jump from no-video to one-frame is ~2× larger (+10pp/+11.1pp).** This does not undermine the paper—improvements are improvements—but it reframes what the paper is demonstrating. The dominant factor in performance is world knowledge plus a single frame of context; the complex object-centric pipeline adds a small increment. The paper acknowledges this by presenting the baselines transparently, but the narrative ("we inject video-specific information to improve performance") could be more explicitly balanced with the finding that most of the lift comes from simply adding *any* visual context.

- **The robotics evaluation shows regressions on 2 of ~22 sub-datasets** (CMU Franka Pick-Insert (F): 57.8 baseline → 49.3 MVU; Freiburg Franka Play (F): 32.2 → 31.6). The paper states "clear performance improvements... over the baseline" (line 346), which is true in aggregate (30.4 vs. 28.5), but glosses over these non-trivial regressions. A more transparent discussion of where the approach fails would strengthen the paper.

- **Total inference cost is under-reported.** The paper lists MVU's parameter count as 13B and inference time as 2.42s, but this counts only the final reasoning VLM. The captioner VLM (also ~13B) runs on 8 frames, and the detector/tracker run on more. The paper acknowledges that the captioner is "identical to the one in [zhang2023llovi]" but does not fully account for the cumulative compute. A complete pipeline cost breakdown would be more informative.

### Trivial
- **The specific model identities (which VLM for captioner, which detector, which tracker) are referenced only by citations** rather than named explicitly in the text. While the citations point to specific works (e.g., OWL-ViT via Minderer et al. 2022), stating the exact model names and configurations would improve reproducibility.

## Nice-to-Haves
- An analysis of *which question categories* benefit most from each object-centric modality would make the contribution more actionable than reporting only aggregate accuracy. The ablation table already quantifies marginal gains per modality (GOI +0.6, OSL +2.2, OMT +1.7), but understanding where motion trajectories specifically help would be valuable.
- The paper could reframe the robotics result as a positive finding: since world-knowledge baselines fail on out-of-distribution data, the fact that MVU helps (even modestly) provides cleaner evidence that the video-specific pipeline is doing meaningful work. This is already noted in passing (line 348) but could be a centerpiece of the argument for the method.

## Removed Points
These are points from the inputs that were filtered or demoted:
- **Criticism about likelihood selection efficiency comparison not being apples-to-apples** (Section 3.2): The paper provides per-sample timing data making the comparison concrete. MVU's LS pipeline is faster than generation-based alternatives, and the paper acknowledges the upstream costs in the captioner. This concern does not hold up against the presented evidence.
- **Criticism about open-ended QA results being in the appendix**: The paper explicitly states these are deferred due to space. The parser strips appendix content; these exist in the original submission. Removed per hard rules.
- **Criticism about missing statistical significance / confidence intervals**: Point estimates without error bars are the norm for large-scale MCQ benchmarks in this community. This is a methodological standard request that is not standard practice. Demoted from consideration.
- **Claim that the LS-Naive results (35.8% on NQA-T) indicate a weakness**: The paper uses LS-Naive as a baseline to show that naive application of likelihood selection fails, while their prompt template (LS-MVU) succeeds. This is a controlled ablation that works as intended.
- **Strength Finder's generic "important problem" framing**: Dropped as superficial praise not tied to specific evidence.

## Novel Insights
The most interesting observation that emerges from synthesizing the reviews is that the paper's strongest contribution—the diagnostic finding about benchmark solvability from world knowledge—is somewhat in tension with its stated main contribution (the MVU framework). The benchmark vulnerability finding is novel and has implications for the whole video QA community, while the MVU framework's marginal benefit over a single frame is modest. A paper that explicitly framed the diagnostic study as the primary contribution and the MVU framework as a case study in addressing that vulnerability would better match what the evidence actually supports. The robotics experiment provides a cleaner test of the method's value than the main benchmarks, because world knowledge fails there, isolating the video-specific contribution.

## Suggestions
1. Add a limitations section discussing error propagation, cases where the pipeline underperforms, and the modest marginal benefit over a single-frame baseline.
2. Either revise the abstract to qualify "state-of-the-art performance" with the specific constraints (zero-shot, open-source, ≤13B, no video training) or replace it with a more precise claim (e.g., "competitive performance under fair comparisons").
3. Report the full pipeline cost (captioner + detector + tracker + reasoning VLM) rather than only the final-stage VLM.
4. Explicitly name the specific VLM, detector, and tracker models in the main text rather than only by citation.
5. Add a brief analysis of which question types or video categories see the largest gains from each object-centric modality.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>