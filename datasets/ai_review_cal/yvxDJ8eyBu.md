- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

MuseCoco proposes a two-stage framework for text-to-symbolic-music generation, using musical attributes (tempo, key, emotion, genre, instrument, etc.) as an intermediate bridge. A BERT-based text-to-attribute model extracts attribute values from text, and a Transformer-based attribute-to-music model generates MIDI conditioned on those attributes. This decomposition allows the music generation stage to be trained self-supervised on unlabeled MIDI (for objective attributes) and reduces reliance on paired text-music data. The paper reports improvements over GPT-4 and BART-base on subjective listening metrics and on an objective attribute-control metric.

## Strengths

- **Clean two-stage decomposition via musical attributes is well motivated.** Breaking text-to-music into text-to-attribute and attribute-to-music stages allows each to be trained with different data sources (synthetic text-attribute pairs for the former, unlabeled MIDI for the latter). This is a principled way to sidestep the scarcity of paired text-MIDI data, and the paper clearly explains the motivation (Section 3).

- **Comprehensive ablations validate key design decisions.** The paper systematically compares control methods (Prefix Control vs. Embedding vs. Conditional LayerNorm, Table 3), model sizes (203M vs. 1.2B, Table 6), classification heads (single vs. multiple, Table 4), and text synthesis strategies (w/ and w/o ChatGPT refinement, Table 5). These controlled experiments provide empirical support for the architecture choices made.

- **Reported quantitative gains over GPT-4 and BART-base are substantial in magnitude.** On the subjective metrics, MuseCoco achieves 4.06 vs. 2.79 (Musicality), 4.15 vs. 3.07 (Controllability), and 4.13 vs. 2.81 (Overall). On the objective ASA metric, the gap is 77.59% vs. 57.64% (GPT-4). These differences are large enough that even after discounting for evaluation limitations, the method appears promising.

## Weaknesses

### Fatal
None.

### Major

1. **Subjective evaluation is underpowered for the strength of the claims.** Only 21 text prompts are used (Section 4.2, line 259). The standard deviations reported (0.75–1.14) are comparable to or exceed the reported gaps between systems (1.08–1.32). No significance tests, confidence intervals, or inter-annotator agreement metrics are reported. The reader cannot determine whether the observed ordering reflects a genuine quality difference or noise from the small sample. Given that the abstract states MuseCoco "outperforms baseline systems" with specific numerical claims, this evidential basis is too thin.

2. **The main objective evaluation is on synthetic data that mirrors the training distribution.** The 5,000-sample standard test set is constructed via the same ChatGPT template procedure used for training (Section 4.1: "construct a standard test set including 5,000 text-attribute pairs in the same way in Section 3.4"). The text-to-attribute model achieves >99% accuracy on this test, but this is unsurprising and uninformative about generalization to real user-written prompts.

3. **The gap between synthetic and natural language performance is large and unaddressed.** The text-to-attribute model achieves 99.96% ASA on the synthetic test set but only 78.11% on the 17 manually written descriptions used in the refinement ablation (Tables 4 vs. 5). This ~22-point drop directly contradicts the claim of "seamlessly transforming textual input." The paper neither discusses this gap nor uses the manual descriptions as the primary test set, despite these being the only naturally written prompts in the evaluation.

4. **The ASA metric may be applied asymmetrically against baselines.** Baselines (GPT-4, BART-base) generate ABC notation, which is converted to MIDI via music21 (line 269). The paper does not analyze whether this conversion introduces artifacts that make attribute extraction systematically less reliable for baselines compared to MuseCoco's native MIDI output. Since ASA is computed by extracting attributes from the generated music, any conversion-side information loss would inflate the reported advantage. This is not controlled for.

### Minor

1. **No breakdown of control accuracy by attribute type in the main paper.** The paper reports 80.42% average attribute control accuracy (Section 4.3.2) but does not show how this breaks down between objective attributes (tempo, time signature, etc.) and the harder subjective attributes (emotion, genre, artist). The abstract's claim of "precise control" is hard to evaluate without knowing whether subjective attributes—which text descriptions most often refer to—are well-controlled.

2. **The Emotion-gen dataset's quality is unvalidated.** 25,730 samples from an "internal emotion-controllable music generation system" (line 237) are used as ground-truth subjective attribute data, but no discussion of quality, validation, or potential error propagation is provided.

3. **"Data efficient" framing is overstated.** The data-efficiency advantage applies fully only to objective attributes (extractable from raw MIDI). Subjective attributes rely on small labeled datasets (EMOPIA: 1,078; POP909: 909). The paper's framing (abstract, introduction) presents data efficiency as a general property without this caveat.

### Trivial
None.

## Nice-to-Haves

- Test the full pipeline on a set of naturally written user prompts (30–50) as the primary evaluation, rather than only using them for the refinement ablation. This is the only way to validate the real-world utility of the text-to-attribute stage.
- Compare against an end-to-end baseline trained on synthetic text-attribute pairs to isolate the benefit of the two-stage architecture vs. the benefit of the data augmentation pipeline.
- Provide error analysis on the text-to-attribute model's failures (e.g., confusion patterns between similar attributes/values).
- Include significance testing (e.g., bootstrap or permutation tests) for the subjective comparisons, given the small sample.

## Removed Points

*These points from the reviews are removed per policy; they are listed here only in case they are useful for context.*

- **"Musician quotes are marketing, not a scientific result"** — The quotes (Section 4.4) are presented as qualitative feedback, not as a controlled experiment. This is a common presentation choice; the paper does not frame it as a scientific result.
- **"No comparison against end-to-end model"** — Scope-creep; the paper compares against the most relevant existing systems (GPT-4, BART-base). Moved to Nice-to-Haves.
- **"ASA metric definition missing"** / **"No per-attribute breakdown for subjective attributes"** / **"Training details for xlarge model insufficient"** — All reference content that exists in the appendix (stripped by the parser). The original submission contains these sections.
- **"Data efficiency claim unquantified"** — The paper states objective attributes are extracted from MIDI and subjective attributes come from labeled datasets (lines 86–87, 239), and the dataset table (Table 2) shows the sizes of labeled subsets. The claim is partially caveated.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel interpretation or synthesis that is not already present in the paper.

## Suggestions

1. **Replace the 21-prompt subjective evaluation** with a larger, statistically powered study (80–100 prompts minimum). Report confidence intervals and significance tests.
2. **Construct and use a test set of naturally written user descriptions** (30–50 prompts) as the primary evaluation of the full pipeline, not just the refinement ablation.
3. **Control for the ABC-to-MIDI conversion asymmetry.** Either evaluate control on directly measurable attributes (e.g., tempo in BPM, time signature) or apply the same conversion to MuseCoco's output and measure the impact.
4. **Report per-attribute control accuracy** for the full pipeline in the main paper, separating objective and subjective attributes.
5. **Discuss the synthetic-to-natural-language performance gap** and either close it with better data augmentation or acknowledge it as a limitation.
