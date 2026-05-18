Now I have sufficient calibration context. Let me synthesize the final review.

## Summary

The paper investigates learned look-ahead behavior in the Leela Chess Zero policy network, extending the analysis of Jenner et al. (2024) from 3-move to 5- and 7-move look-ahead. Using probing, activation patching, and ablation, the authors present evidence that the model encodes future board states up to seven moves ahead, that it considers multiple alternative move sequences, and that specific attention heads (notably L12H12, L12H17) mediate these behaviors in a pattern-sensitive, time-insensitive manner. A puzzle set notation is introduced to disentangle behavior across different chess position types.

## Strengths

- **Extends look-ahead depth from 3rd to 5th/7th moves with multi-method evidence**: The paper provides probing (Fig. 3), activation patching (Fig. 2), and ablation results showing the model encodes and causally uses information about board states beyond the 3-move limit analyzed in prior work. The combination of three complementary methods (probing for encoding, patching for causal necessity, ablation for component identification) strengthens the overall case.

- **Provides causal evidence for multi-branch look-ahead**: The alternative-move analysis (Fig. 6) is a genuinely novel extension over Jenner et al. (2024). Showing that patching the alternative first-move square increases the model's odds of choosing the correct main move, and that this effect propagates through the third-move squares of alternative branches, provides evidence that the model encodes and weighs multiple lines of play simultaneously.

- **Identifies context-dependent, pattern-sensitive mechanisms that generalize across time horizons**: The finding that L12H12 responds to the same abstract patterns (AAC, ABC, ACC) whether they occur at moves 1-2-3, 3-4-5, or 5-6-7 is a specific mechanistic insight. This suggests the model has learned time-insensitive structural pattern matching rather than depth-specific heuristics.

- **Introduces a useful puzzle set notation (Section 2.4)**: The sequence-labeling scheme (e.g., 112, 123, 11223) enables fine-grained disentanglement of behavior across different position types, revealing large performance differences (e.g., strong effect for set 11223, negligible for set 11233) that were obscured in prior bundled analyses.

- **Reveals functional specialization across attention heads**: Ablation results differentiate L12H12 (more critical in checkmate scenarios) from L12H17 (more active in non-checkmate positions), providing concrete mechanistic differentiation not previously reported.

## Weaknesses

### Fatal
None.

### Major

- **The probing evidence for 7-move look-ahead is reported only qualitatively, without numerical baselines needed to assess the claim.** The paper states that the 7th-move square probe accuracy is "considerably low, but still non-negligible when compared with the probe's accuracy for a random model" (Section 3). However, the text provides no definition of what the "random model" is (probe on random labels? random board positions?), no exact accuracy numbers, no chance-level baseline, and no significance test. Since the existence of 7-move look-ahead is a headline claim (extending from Jenner et al.'s 3-move result), the evidence for it needs to meet a higher bar. Without numerical specifics, the reader cannot distinguish a real signal from noise or from trivial positional correlations captured by the probe.

- **Causal interpretations overreach the experimental methodology.** The paper repeatedly interprets activation patching and ablation effects as evidence that specific heads "move information backward in time" from later to earlier move squares. For example: "L12H12 moves information backward in time from the third to the first move square" (Section 3). Activation patching in the residual stream shows that a component is *causally important* for the output, but it does not directly demonstrate *what* information is moved or *how* the directional flow works. The interpretation that information is specifically "moved backward in time" is one possible mechanism consistent with the data, but it is not uniquely determined by the experiments presented. The paper does hedge in places ("we hypothesize," line 104), but the headline causal language goes beyond what the experiments directly establish.

### Minor

- **The alternative move analysis lacks a fully specified corruption protocol.** The paper states that "corrupted boards which are compatible with both branches A and B" are used (Section 3), but does not specify in the main text how these boards are generated, what "compatible" means technically, or what controls were used to rule out confounds (e.g., generic activation disruption). While appendices may contain more detail, the main text should provide enough specificity for the reader to assess the validity of the experiment. Additionally, no control condition (e.g., corrupted boards incompatible with both branches) is mentioned to isolate the specific effect.

- **No significance testing is reported.** Key claims are described with qualitative language ("non-negligible effect," "strong effect," "moderate effect") without p-values, confidence intervals (beyond the stated 50%/90% intervals mentioned for Fig. 2), or effect size reporting for the central comparisons. This makes it difficult to assess the reliability of the findings.

- **The finetuned model used is not adequately characterized.** The paper notes (Section 2.1) that "due to peculiarities of this particular model, previously discussed in Jenner et al. (2024), we use a finetuned version" but does not summarize what was changed during finetuning or whether this could alter the original model's look-ahead behavior. A reader unfamiliar with Jenner et al. cannot assess whether the finetuning might introduce or amplify the look-ahead behaviors being studied.

- **The "random model" baseline for probing is undefined.** As noted above, the paper references "the probe's accuracy for a random model" without specifying what this means. This is a presentation gap that undermines the central 7-move claim.

### Trivial
None.

## Nice-to-Haves

- A control condition for the attention head patching experiments, checking whether patching unrelated heads with similar activation norms produces effects of comparable magnitude, would strengthen the specificity claims.
- Attention knockout (rather than full head ablation) or patching attention *patterns* rather than whole heads could more precisely isolate the claimed directional mechanisms.
- Reporting exact probing accuracies with error bars and chance-level baselines for each move step (1st–7th) would significantly strengthen the 7-move look-ahead claim.

## Removed Points

- **Criticism about missing figures / impossibility of evaluation due to parser artifacts**: The critic noted missing figures make evaluation impossible. This is a known parser artifact — the original submission has these figures. The paper's text describes their content, so evaluation is possible from the text descriptions plus the structural claims. **Removed (parser artifact).**

- **Criticism that the "random model" reference is entirely undefined**: While I retained this as a minor weakness (the paper doesn't specify what "random model" means technically), the critic's stronger framing — that without this, the 7-move claim is entirely unsupported — is overstated. The paper does describe a comparison baseline, just not in sufficient detail. **Weakened from fatal to minor.**

- **Criticism about the alternative move analysis that "the reported effect could stem from many mechanisms other than genuine look-ahead"**: This speculation about alternative explanations is not grounded in specific flaws in the paper's method but rather generic skepticism. The paper's alternative move patching experiment is a standard causal intervention design. **Removed (strawman).**

- **Strength Finder's claims about "most important piece of evidence is the alternative-move patching experiment"**: This is an opinion, not a verifiable strength of the paper. The relative importance of different experiments is subjective. **Removed (subjective framing).**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide exact numerical probing results** — report the probing accuracy for each move step (1st–7th) with confidence intervals, define the "random model" baseline precisely (e.g., probe trained on scrambled target squares or on random labels), and include a control like accuracy on irrelevant future board positions.

2. **Tone down the directional causal language** — replace "moves information backward in time" with more precise, methodologically accurate phrasing such as "patcing L12H12's representation of square C affects the model's prediction about square A" — unless additional experiments (e.g., attention knockout, pattern patching) are added to support the directional claim.

3. **Fully specify the corruption protocol for the alternative move analysis** in the main text: how are corrupted boards constructed? What does "compatible with both branches" mean? Include a control condition (e.g., corrupted boards incompatible with both branches) to rule out generic disruption.

4. **Characterize the finetuned model** — summarize what was changed relative to the original Leela model and whether the finetuning could affect look-ahead behavior.

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `/home/.../bc2H72hGxB.md` (Human-Aligned Chess) | 6.80 | Much stronger — polished systems paper with user studies, deployed model, and clear practical contributions. Under-review paper is exploratory and much less complete. |
| `/home/.../Hf17y6u9BC.md` (Best Practices Activation Patching) | 6.67 | Much stronger — systematic methodology study with clear, actionable findings. Under-review paper is less rigorous and less definitive. |
| `/home/.../Ebt7JgMHv1.md` (Subspace Activation Patching) | 6.33 | Much stronger — well-written theoretical + empirical contribution. Under-review paper is weaker in clarity and rigor. |
| `/home/.../8sKcAWOf2D.md` (Fine-Tuning Enhances Mechanisms) | 5.67 | Stronger — thorough mechanistic analysis with clear methodology. Under-review paper is less thorough. |
| `/home/.../WQQyJbr5Lh.md` (Influential Neuron Path) | 6.00 | Stronger — clear systematic evaluation. Under-review paper is less polished. |
| `/home/.../FnIRtzK5wX.md` (Go QiGan) | 4.25 | Somewhat similar (game-playing network analysis with qualitative claims) but under-review is slightly stronger — more systematic experiments and clear puzzle set notation. |
| `/home/.../agEy9hliY1.md` (NCO Probing) | 5.25 | Somewhat similar (probing-based interpretability) but slightly stronger — more quantitative evaluation. Under-review is weaker in evidence specificity. |
| `/home/.../Wxl0JMgDoU.md` (Chess SAE) | 2.50 | Much weaker — poorly executed paper with unclear claims. Under-review is substantially better. |

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>