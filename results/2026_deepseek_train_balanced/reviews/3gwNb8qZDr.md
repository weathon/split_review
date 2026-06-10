## Summary

This paper introduces Activation Prompts (AP) — learnable additive perturbations applied to intermediate-layer activations rather than the input, generalizing input-level Visual Prompting (VP). The key findings are: (1) AP substantially outperforms VP in accuracy (>4% on ResNet-101, >1.5% on ViT-Large/16) while also being more memory- and time-efficient; (2) CNNs and ViTs exhibit opposite layer preferences for AP — CNNs favor deep layers, ViTs favor shallow layers — which the paper explains through feature globalness; (3) AP is formally connected to normalization tuning. The work is evaluated across 29 datasets and multiple architectures with comparisons to 9 PEFT methods.

## Strengths

- **AP significantly outperforms input-level VP across diverse datasets.** Table 1 shows AP achieves >4% average accuracy improvement over VP on ResNet-101 and >1.5% on ViT-Large/16 across 19 datasets, with gains of 7–9% on StanfordCars, SVHN, and GTSRB. This directly demonstrates that extending prompting to intermediate activations closes a substantial portion of VP's performance gap.

- **Discovery of opposite layer preferences in CNNs vs. ViTs, validated through multiple analyses.** Figure 4 shows CNNs achieve best AP accuracy in deep layers while ViTs do so in shallow layers. The paper corroborates this with CKA similarity analysis (Figure 5A) showing deep CNN features align with middle ViT layers, and attention-distance analysis (Figure 5B) showing decreasing global feature ratio in deeper ViT layers — a triangulation of evidence prior work does not provide.

- **AP is simultaneously more accurate and more efficient than VP.** Table 2 reports that for ResNet-101, AP uses 6.3G GPU memory vs. VP's 12.2G and trains at 41 s/epoch vs. 72 s/epoch — roughly halving both costs while improving accuracy. This is a non-trivial practical advantage.

- **Extensive evaluation spanning 29 datasets, multiple architectures, few-shot and full-data regimes, and 9 PEFT baselines.** The breadth of Tables 1–5 makes the empirical claims robust to dataset and architecture choices. The inclusion of CLIP and Swin-Transformer (Table 5, Figure 7) extends generality.

- **Formal connection bridging AP and normalization tuning.** Proposition 1 (Appendix C.2) establishes that under certain unit-scaling conditions AP reduces to NORMTUNE for both BatchNorm (CNNs) and LayerNorm (ViTs). This bridges two previously separate lines of work and provides theoretical context for why AP can outperform NORMTUNE (greater flexibility of perturbation).

## Weaknesses

### Fatal
None.

### Major

- **Missing critical control: a linear classifier on intermediate features at the same layer without perturbation.** The paper compares AP with LINEAR-PROBE (trained on *final* features), VP (input-level), and NORMTUNE. However, the most natural baseline for determining whether the perturbation itself contributes anything is a linear classifier trained on the intermediate features at layer *l* **without** the additive perturbation. If this baseline performs similarly to AP at layer *l*, then the perturbation is incidental — the performance gain comes from choosing a better feature extraction layer, not from the prompt mechanism. The paper's central claim that AP is doing something distinct from merely accessing better intermediate features requires this control. Its absence is the most significant gap in the evaluation.

- **The framing significantly overclaims what is delivered regarding "understanding VP."** The introduction poses question (Q): *"Is VP truly beneficial... and under what conditions does it prove effective or ineffective?"* and presents AP as "a bridge and analytical tool" to study VP. However, the paper never analyzes VP's conditions of effectiveness in any depth. It shows that AP outperforms VP and that layer choice matters, but the insight about VP reduces essentially to "the input layer is suboptimal." The paper does not characterize *when* or *why* VP itself works or fails, nor does it use AP to illuminate VP's mechanisms. The analytical framing should be dropped or substantially revised to match what the paper actually delivers: an empirical study of a new prompting method with interesting layer-preference properties.

- **The theoretical analysis is too distant from the actual experimental setting to "validate" the claims.** Theorem 1 covers a single-head, two-layer ViT with artificial data (four patterns, P tokens, noise assumptions, hard attention via argmax). The gap between this toy model and ViT-Large/16 (24 layers, 16 heads, real ImageNet pretraining) is vast and unbridged in the paper. The theory says nothing about CNNs, despite the paper's title and contribution list claiming "architecture effects" are theoretically validated. The paper acknowledges this focus on ViTs (line 94), but the contributions and conclusion do not reflect this limit. The proof sketch (lines 113–122) describes norm-based arguments about removing "non-discriminative patterns" that the pretrained model has been carefully constructed to contain — a theoretical artifact, not an explanation for real model behavior. The paper should either substantially bridge this gap or recalibrate what "theoretically validates" means.

### Minor

- **Variance reporting is insufficient.** The paper reports that variance across 5 trials is "≤0.3%" and therefore omitted (Table 1 caption). For 19 datasets × multiple methods, this is remarkably uniform. The paper should report at least a summary (mean ± std for a representative subset or a footnote) so readers can assess whether reported differences of <1% between methods are meaningful.

- **The attention-distance alignment in Figure 5(B) is qualitative, not quantitative.** The paper states the pattern "roughly aligns" with AP's performance pattern but provides no correlation measure. Notably, the uptick in attention distance in the very deepest ViT layers (layer 15+) is left unexplained — if AP prefers shallow layers, why would the deepest layers show any increase in global features? This does not invalidate the finding but weakens the claimed explanatory link.

- **The optimal layer is selected on OxfordPets alone, and the paper does not show in the main text whether this choice is robust across diverse datasets.** The paper references Figure A1 in the appendix for more datasets, but bringing a sensitivity analysis into the main paper (even 2–3 diverse datasets) would substantially strengthen confidence that layer preference is architecture-determined rather than dataset-dependent.

### Trivial
None.

## Nice-to-Haves
- For the CLIP experiments, comparing AP against text-prompting methods (e.g., CoOp) would provide a more complete picture, since CLIP is commonly used with text-based adaptation.
- The paper could strengthen the "understanding VP" framing (if retained) by showing a concrete example where AP's layer-preference analysis predicts when VP will fail — e.g., showing that the gap between VP and AP shrinks as the optimal AP layer approaches the input.

## Removed Points
These points were flagged for removal from the harsh critic or strength finder. Treat them with caution — some may contain useful information if verified, but they were excluded for the reasons below:

- **"Connection to NORMTUNE is not clean / superficially correct"**: Removed. The paper explicitly states the assumptions (consistent perturbations across units, γ/√σ=1, etc.) under which AP reduces to NORMTUNE. It then argues AP is a *more flexible generalization* precisely because these constraints need not hold. The transparency about assumptions makes this a reasonable theoretical connection, not a flaw.
- **"Layer selection never examines dataset variation"**: Removed as factually incorrect. The paper states "Results on more datasets are provided in Fig. A1" (line 74). The appendix addresses this, though inclusion in the main text would be stronger.
- **"Efficiency comparison is a direct artifact of design"**: Removed. AP's efficiency gain from shallower backpropagation is a consequence of its design, presented as a legitimate advantage. Efficiency being "by design" is not a weakness.
- **"AP ranks 2nd-4th among PEFT methods undercuts claims"**: Removed. The paper describes this as "competitive performance" (line 164), not SOTA. This is accurate framing.
- **Strength: "Honest limitation analysis"**: Removed as too weak a strength to lift; limitation statements are expected, not exceptional.
- **Strength: "Provable sample-complexity advantage"**: Retained in modified form in strengths but recontextualized with the limitations on scope noted in weaknesses.

## Novel Insights
None beyond the paper's own contributions. The reviewer inputs surface the central tension: the paper has a genuine empirical finding (opposite layer preferences, practical efficiency gains from AP) that is packaged in an overclaimed narrative about "understanding VP," and lacks a critical control experiment that would determine whether the perturbation itself contributes. This tension is correctly identified by the harsh critic but overstated — the layer preference finding and the efficiency analysis remain valuable regardless of whether AP's perturbation is strictly necessary.

## Suggestions
1. **Run the missing control experiment:** For several datasets and both ResNet-101 and ViT-Large/16, train a linear classifier on the features extracted at layer *l* (where AP is applied) without any perturbation. Compare to AP at layer *l*. If AP significantly outperforms, the perturbation claim is validated. If not, the paper should reframe the contribution around layer selection rather than perturbation efficacy.
2. **Calibrate the framing:** Drop or substantially rewrite the claim that AP is an "analytical tool for understanding VP." Present the paper straightforwardly as introducing AP as a more effective variant of VP, with an accompanying study of layer preferences across architectures.
3. **Add variance reporting** for the main results (Table 1) or at minimum note the range of observed standard deviations.
4. **Explicitly state the limits of the theoretical analysis** in the contributions list and conclusion: the theory covers a simplified 2-layer ViT and does not cover CNNs.

## Score and Decision

This paper makes a real but modest contribution. The core empirical finding (CNNs and ViTs have opposite layer preferences for intermediate-layer prompts) is interesting and reasonably well-supported. The efficiency advantages of AP over VP are practically relevant. The experimental scope (29 datasets, multiple architectures, 9 baselines) is a clear strength.

However, the paper has significant issues that prevent acceptance at a top venue: (1) a missing control experiment (intermediate-feature linear probe) that is necessary to determine whether AP's perturbation contributes anything beyond layer selection; (2) a framing that promises an analytical understanding of VP but delivers only a method comparison; (3) a theoretical analysis too simplified to validate claims about real architectures. These problems are fixable with major revision, but in the current form the gap between what is claimed and what is demonstrated is too wide.

**Score:** 5.0

**Decision:** Reject

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>