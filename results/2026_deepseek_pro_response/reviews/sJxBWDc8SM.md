Now I have a clear picture. Let me finalize the review with the calibrated score.

## Summary

This paper investigates optimization stability differences between Transformers and modern recurrent models (Mamba, Hyena, DeltaNet) on two synthetic benchmarks: multi-query associative recall (MQAR) and copying. Through extensive experiments (~3,000 runs), the authors demonstrate that SSMs exhibit a critically narrow window of viable learning rates compared to Transformers, that SSMs favor width scaling while Transformers require depth, and that the 1D convolution is the key architectural component enabling single-layer SSMs to solve recall while 1-layer Transformers cannot. The central thesis is that optimization instability, rather than fundamental expressivity limitations, is the primary differentiator between these architectures on these benchmarks.

## Strengths

- **Extensive and rigorous LR grid search across two benchmarks:** Figure 1, Figure 5, and Figure 7 convincingly demonstrate that Mamba and Hyena achieve high accuracy only within sharply peaked learning-rate windows, while Transformers maintain near-perfect accuracy across orders of magnitude. The experiments use 5 seeds with reported error bands and directly overlay the prior LR grid from Arora et al. (2023) to show how standard tuning would miss the viable region entirely. This is the paper's strongest and most persuasive contribution.

- **Clean causal ablation isolating the 1D convolution:** Table 2 provides a tight four-way comparison: 1-layer Attention fails at ~2% accuracy; adding a 1D convolution to QKV projections enables 99% performance; removing the convolution from 1-layer Mamba collapses it to the same ~2% failure; while removing gating or using bare S6+MLP preserves performance (~98%). This directly demonstrates that the convolution — not the recurrent state update itself — is the critical element for single-layer expressivity.

- **Cross-task validation of width-vs-depth scaling:** Table 1 on the copying task shows that a wide, shallow Mamba (12 layers × 1408 width) achieves 100% while a deep, narrow Mamba (24 layers × 1024 width) with the same parameter count achieves only 16%. This cleanly demonstrates that fair architectural comparisons must scale SSMs by width, not depth.

- **Identification of DeltaNet as a stability path:** Figure 7 shows DeltaNet achieving Transformer-level LR robustness on MQAR, unlike Mamba and Mamba2 whose performance remains narrowly peaked. The connection to Householder-matrix-based mixing, while hypothesized rather than tested, provides a plausible mechanistic direction for future work.

- **Novel observation of loss-bump dynamics in 1-layer Transformers:** Figure 6 documents a characteristic loss bump during 1-layer Transformer training — a phenomenon previously associated exclusively with induction-head circuit formation in multi-layer models (Olsson et al., 2022). The finding that this bump occurs without accuracy improvement in the 1-layer case is genuinely new, though the accompanying claims about Mamba's dynamics need reconciliation (see below).

## Weaknesses

### Fatal

None.

### Major

- **Internal contradiction in Section 6 about Mamba's training dynamics:** The paper makes inconsistent claims about whether Mamba exhibits smooth or bumpy training dynamics. The Figure 6 caption (line 182) states that Mamba and Hyena "both exhibit smooth learning dynamics." The contributions bullet (line 45) says "recurrent models show smoother training dynamics in most setups, with no clear evidence for the formation of induction heads." The abstract (line 9) says Mamba's dynamics "do not resemble the formation of induction heads." However, the body text (lines 188-190) explicitly states that "the dynamic of Mamba is mixed" and reports "a significant loss bump." The Discussion (line 235) further says "Mamba displays similar behavior" — i.e., similar to the Transformer's induction-head-like dynamics. These accounts cannot all be true simultaneously. Since the induction-head dynamics claim is one of the paper's four listed contributions, this inconsistency undermines the reliability of Section 6. The actual Mamba training curves need to be presented accurately and the claims about them made internally consistent.

### Minor

- **Central thesis stated too categorically:** Line 39 claims Transformers and SSMs differ "not in terms of expressive power but mainly because of their optimization dynamics." This framing is slightly stronger than the evidence supports and conflicts with the paper's own acknowledgment (line 31) that "fundamental expressivity issues exist." The evidence actually supports a more precise claim: when architectural elements are aligned (both with or both without convolutions), the core sequence mixers have comparable expressivity on these tasks, and the primary remaining differentiator is optimization stability. The overstatement is mild and fixable.

- **DeltaNet stability hypothesis is untested:** Section 7 hypothesizes that DeltaNet's improved stability stems from Householder-matrix-based mixing that avoids vanishing gradients, unlike Mamba/Mamba2's decay-rate-based A_k matrices. While the paper correctly flags this as a hypothesis ("We hypothesize," line 222), it is offered without any ablation or controlled comparison that isolates this mechanism. Given the paper's focus on optimization dynamics, a causal test would strengthen the contribution.

- **Abstract "random guessing" claim is imprecise:** The abstract states that 1-layer Transformer performance "does not exceed random guessing," but Table 2 reports 2% accuracy. For an MQAR task with ~8,000 vocabulary tokens, 2% is well above random (~0.01%). The body text (line 145) more accurately states the model recalls "on average one key-value pair." This imprecision in the abstract should be corrected.

- **Accuracy metric not defined in main body:** The paper does not specify how accuracy is computed for MQAR (per-query token? exact match of all queries?). Given how central accuracy is to every figure and table, a one-sentence clarification in the main text is warranted.

### Trivial

None attributable to the authors. The parser-generated figure descriptions contain artifacts that do not reflect the actual paper.

## Nice-to-Haves

- Testing whether the narrow-LR-window phenomenon is specific to Adam or generalizes across optimizers (e.g., AdamW, SGD with momentum) would strengthen the claim that this is an architectural property rather than an optimizer interaction.
- Providing attention-pattern visualizations for the 1-layer Transformer's loss-bump phase would add mechanistic evidence to the induction-head interpretation.
- Ablating Mamba's decay parameter to test whether reducing vanishing-gradient effects broadens the LR window would transform the DeltaNet hypothesis into an empirical finding.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **HC claimed the central thesis overshoots the evidence (Critical Issue #2):** The HC argued Table 2 demonstrates an "expressivity gap" undermining the thesis. This misreads the evidence. Table 2 actually *supports* the thesis: Mamba without convolution gets the same 2% as Attention, and Attention with convolution gets 99%. The paper's point is precisely that when you control for convolution, expressivity is equivalent and the remaining gap is optimization. Removed the HC's fatal characterization; kept only the minor concern about phrasing precision.

- **HC flagged Figure 3/4 parser descriptions as paper inconsistencies:** The parser-generated descriptions (lines 119-122, 132-134) conflict with the paper's own captions. These are parser artifacts, not paper errors. Removed.

- **HC demanded optimizer/scheduler ablations:** The HC suggested testing other optimizers beyond Adam. This is scope creep — Adam is standard, and the contribution does not depend on optimizer invariance. Moved to Nice-to-Haves.

- **HC claimed DeltaNet hypothesis is "presented as an explanatory conclusion":** The paper explicitly says "We hypothesize" (line 222). The HC's characterization is factually incorrect. Kept the legitimate concern (untested hypothesis) as a Minor weakness but removed the claim about misrepresentation.

- **SF generic strengths about "important problem" / "interesting question":** These are not evidence-backed and were removed.

## Novel Insights

The paper's most genuinely novel insight is that the 1D convolution — a seemingly minor architectural detail — is the decisive factor enabling single-layer sequence models to solve associative recall, rather than any property of the recurrent state update or the attention mechanism itself. When convolution is held constant (both models have it, or both lack it), a 1-layer Mamba and a 1-layer Transformer perform nearly identically in terms of expressivity. The remaining gap is entirely about optimization: SSMs are far more brittle to learning rate choice. This reframes the SSM-vs-Transformer debate from an expressivity question to an optimization question in a clean, causally-grounded way.

## Suggestions

- Resolve the Section 6 contradiction by presenting Mamba's actual training curves honestly — determine whether the loss bump is present or not, at what configurations it appears, and make the caption, body text, abstract, and contributions bullet mutually consistent. This is the highest-priority fix.
- Soften the thesis statement on line 39 to match the precise claim the evidence supports (e.g., "when architectural elements are aligned, Transformers and SSMs differ primarily in optimization dynamics rather than expressivity").
- Add a one-sentence definition of the accuracy metric in the main body.
- Either test the DeltaNet Householder hypothesis with a targeted ablation or more explicitly mark it as an open question for future work.

## Score and Decision

**Round 1 bracket:** 6.0–7.5. The paper is clearly above the 5.25–5.75 theoretical SSM-vs-Transformer papers that lack empirical validation, but below the 8.0 papers (PdaPky8MUn "Never Train from Scratch" and d8w0pmvXbZ "Small-scale proxies") which have cleaner execution, broader validation, and no internal contradictions.

**Round 2 narrowing:** Within the bracket, the paper most closely compares to Zoology (LY3ukUANko, 6.33) — the paper it directly builds on and critiques — and sZJNkorXMk (6.67), an SSM initialization analysis with theory and limited empirics. Our paper is empirically more rigorous than Zoology (proper LR grid search vs. the original's sparse grid) but narrower in scope (no language modeling validation, no theoretical bounds). It is comparable in quality to sZJNkorXMk (6.67) but trades theoretical depth for stronger empirical evidence. The internal contradiction in Section 6 is a real but fixable flaw that prevents a higher score.

**Anchor comparison table:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| QFgbJOYJSE (SSMs Provably Comparable) | 5.75 | R1 | Theoretical only, almost no empirical validation — our paper is clearly stronger |
| LY3ukUANko (Zoology) | 6.33 | R2 | Direct predecessor; our paper refines its methodology with more rigorous LR tuning — comparable quality |
| AL1fq05oH (Mamba original) | 6.25 | R2 | Foundational architecture; our paper is more incremental but more rigorous empirically — comparable |
| sZJNkorXMk (Autocorrelation Matters) | 6.67 | R2 | SSM initialization theory + limited empirics; our paper has stronger empirics but no theory — comparable |
| qtTIP5Gjc5 (Demystifying Token Dynamics) | 7.50 | R2 | Theory + practical refinements + real-world validation — clearly stronger |
| PdaPky8MUn (Never Train from Scratch) | 8.00 | R1 | Cleaner execution, broader benchmarks, no internal contradictions — clearly stronger |
| d8w0pmvXbZ (Small-scale proxies) | 8.00 | R1 | Deeper analysis, practical takeaways, cleaner presentation — clearly stronger |

**Final score: 6.5.** The paper makes a genuine and well-supported contribution, with the LR instability finding standing on its own as important work. The internal contradiction in Section 6 is the main concern — fixable but significant enough to prevent a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>