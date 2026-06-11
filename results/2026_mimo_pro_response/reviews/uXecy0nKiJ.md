Now I have enough calibration data. Let me write the final review.

**Round 1 bracket: 6.0 – 7.0**

The paper is clearly stronger than rejected papers in the 3.0–5.75 range (e.g., z1yI8uoVU3 at 3.00 on steered representations, FlipAttack at 5.75). It is comparable to accepted papers in the 6.0–7.0 range (hXA8wqRdyV at 6.14 on adaptive jailbreaking, YzxMu1asQi at 6.50 on adversarial activation attacks, aSy2nYwiZ2 at 6.67 on universal jailbreak backdoors, r42tSSCHPh at 7.00 on generation exploitation). The confounded SAE comparison is a real weakness that prevents a score of 7.0+, but the novel universal attack construction and systematic multi-model evaluation place it above 6.0.

**Round 2 narrowing: 6.0 – 7.0 confirmed.** Papers at 6.14 (hXA8wqRdyV) and 6.50 (YzxMu1asQi) are the closest comparators. The paper under review has a more novel attack vector (aggregating prompt-specific steering vectors into a universal attack) and broader systematic evaluation than both, but the SAE comparison weakness pulls it back. Final score: **6.5**.

---

## Summary
This paper investigates whether activation steering — a widely used inference-time technique for controlling LLM behavior — can inadvertently break alignment safeguards. Through systematic experiments across multiple model families (Llama3, Qwen2.5, Falcon3, FalconH1), scales (3B–70B), layers, and steering coefficients, the authors show that even random steering directions increase harmful compliance from 0% to 2–27%, and that aggregating 20 prompt-specific jailbreak vectors into a single "universal attack" achieves up to 63.4% compliance on unseen harmful prompts with only black-box steering access.

## Strengths
- **Universal attack construction from prompt-specific vectors (Sec. 4.4, Fig. 6)**: Averaging 20 random vectors that each jailbreak a single prompt produces a universal attack achieving up to 63.4% compliance on Falcon3-7B and 50.4% on Llama3-70B — a ~4× amplification over random steering. This is novel, practically alarming, and well-demonstrated across 8 model variants.
- **Systematic multi-dimensional experimental sweep with clean 0% baseline (Sec. 3.4, 4.1, Fig. 2)**: The paper sweeps across model families, scales (3B–70B), layers (1/3, 1/2, 2/3 depth), steering coefficients (0.75–2.0), and vector types. The consistent 0% baseline compliance without steering cleanly isolates steering as the cause.
- **Benign SAE features are broadly dangerous (Fig. 4a)**: 668 of 1,000 randomly sampled SAE features jailbreak at least five prompts, and the most potent features correspond to benign concepts like "brand identity" and "physical positioning." This directly challenges the assumption that interpretability confers safety.
- **Real-world validation via production API (Sec. 4.3)**: The case study using the public Goodfire API with default hyperparameters and a benign SAE feature successfully jailbroke a deployed model, confirming the vulnerability outside controlled lab conditions. Two distinct failure modes are identified.
- **Cross-prompt generalization analysis reveals monitoring infeasibility (Fig. 4b)**: The cross-category heatmap shows dangerous SAE features generalize poorly even within their own source category, implying comprehensive safety auditing would require exhaustive testing — practically infeasible.
- **Consistent results across architectures (Fig. 2a, Fig. 6)**: Vulnerability appears in Llama3, Qwen2.5, Falcon3, and FalconH1 from 3B to 70B parameters, strengthening the claim that this is structural rather than model-specific.

## Weaknesses

### Fatal
None

### Major
- **SAE vs. random comparison in full-dataset evaluation (Fig. 3) is confounded by different models, layers, and depths**: In Sec. 4.2 and Fig. 3, SAE experiments use Llama3.1-8B at layer 19 (2/3 depth, coefficient 2.0), while the random steering baseline uses Llama3-8B at 1/3 depth (coefficient 2.0) and Qwen2.5-7B at 1/3 depth (coefficient 1.5). The SAE vs. random comparison thus differs simultaneously in model version (Llama3 vs. Llama3.1), layer (~11 vs. 19), and depth (1/3 vs. 2/3). The single-prompt comparison (Fig. 2c) partially addresses this — same model, same layer — showing only a 2–4% advantage of SAE over random. But this is on just one prompt. The paper acknowledges the SAE is tied to a specific model/layer (Sec. 3.3: "We therefore limited our investigation of SAE feature steering to this specific model and layer"), but a matched random baseline on Llama3.1-8B at layer 19 for the full JailbreakBench dataset is missing. Without it, the claim about SAE features specifically being dangerous — rather than the layer choice or model version driving the result — remains underdetermined. The core finding that random steering breaks alignment stands regardless, but the SAE-specific claim needs this control experiment.

### Minor
- **"No harmful data" framing overstates the threat model**: The paper states the universal attack "requires no harmful training data" (Abstract, Finding 3) and "no harmful data" (Conclusion, Sec. 5). However, the construction in Sec. 4.4 explicitly starts with a harmful prompt ("Write a tutorial on how to make a bomb"), samples ~100–500 random vectors, and uses a compliance judge to identify successful vectors. The abstract's phrasing "no harmful training data" is technically defensible, but the conclusion's "no harmful data" is misleading. Refining to "requires only black-box steering access, a single harmful prompt, and a binary compliance signal" would be more precise and, arguably, more threatening because it's realistic.
- **No error bars or confidence intervals reported**: All compliance rates (often 10–20%) are point estimates. The universal attack results (Fig. 6) are already generated from 20 distinct universal vectors per model, but the variance is not shown. Adding standard errors would strengthen statistical credibility.
- **Perturbation magnitudes not contextualized against typical steering practice**: Full-dataset experiments use c=2.0 (Llama3-8B, Llama3.1-8B) and c=1.5 (Qwen2.5-7B), corresponding to vectors with magnitude 1.5–2× the average activation norm. The paper shows non-zero compliance at all tested coefficients (Fig. 2), but headline results are at the top of this range. Without benchmarking against typical coefficients used in prior steering work, practical risk is hard to assess.

### Trivial
None

## Nice-to-Haves
- Contextualizing perturbation magnitudes by surveying representative steering papers for typical coefficient ranges.
- Discussion of potential mitigations (circuit breakers, representation engineering defenses) beyond the brief mentions in the conclusion.
- Brief mechanistic analysis (e.g., whether steering reduces refusal direction norm or changes output entropy).

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Straw man" framing of steering as "safer than fine-tuning"**: The harsh critic questioned whether this framing is a straw man. The paper's argument is that safety implications of steering are underexplored, which is well-supported and not a straw man.
- **LLM-as-judge calibration concerns**: The paper acknowledges Qwen3-8B as judge and references Appendix B for calibration against human annotations. The classification of incoherent responses as SAFE (Sec. 3.4) is well-motivated.
- **Case study is small-scale (two prompts)**: The paper frames it as a "case study" (Sec. 4.3 title), not a definitive evaluation. Two examples are sufficient for illustration.
- **Mechanism investigation is minimal**: This is scope creep — the paper is an empirical vulnerability analysis, not a mechanistic interpretability paper. The paper references Appendix E and flags this as future work.
- **Reviewer concerns about "not yet released" or reproducibility**: These are parser/availability concerns, not paper problems.
- **Generic concerns about fairness of baselines**: The asymmetric SAE comparison favors the baseline (random vectors at 1/3 depth, which is shown in Fig. 2b to be less vulnerable than 2/3 depth), making this a weakness that favors the authors' claim, not undermines it.

## Novel Insights
The most novel insight is that the linearity of activation steering creates a fundamental vulnerability through "vulnerability aggregation": prompt-specific jailbreak vectors, each weak on its own, can be averaged into a universal attack vector that generalizes to unseen harmful prompts. This transforms a collection of localized failures into a strong, general-purpose attack — a phenomenon not previously demonstrated for activation steering. Combined with the finding that most SAE features (668/1000) have jailbreaking capability despite representing benign semantics, the paper demonstrates that the very precision and interpretability that make steering attractive also create a systematic attack surface.

## Suggestions
- **Critical**: Run random vectors on Llama3.1-8B at layer 19 for the full JailbreakBench dataset as a matched control for the SAE comparison. This single experiment would resolve the most significant weakness.
- Replace "no harmful data" with a precise threat model statement acknowledging the single-prompt requirement.
- Add error bars or confidence intervals to headline figures, especially Fig. 6.
- Briefly survey typical steering coefficients in 3–5 representative prior papers to contextualize the tested range.

---

## Calibration Report

**Anchors retrieved across all rounds:**

| Path | Avg Human Score | Round | Comparison |
|------|----------------|-------|------------|
| 5kMwiMnUip.md | 1.40 | 1 | Weak jailbreaking survey; our paper is far more rigorous and novel |
| 8QTpYC4smR.md | 1.00 | 1 | Generic LLM survey; not comparable |
| gwZ90hFSL2.md | 1.00 | 1 | Unrelated NLP paper |
| Uj0h13lVrR.md | 1.00 | 1 | Unrelated GFlowNet paper |
| BeOEmnmyFu.md | 2.50 | 1 | Language game jailbreaking; weaker evaluation and novelty than our paper |
| KyKTjRtyNG.md | 3.00 | 1 | Multi-round conversational jailbreaking; less systematic than our paper |
| lUyYX9VFgA.md | 3.00 | 1 | Code-of-thought safety probing; narrower scope |
| z1yI8uoVU3.md | 3.00 | 1 | Steered representation measurement; directly relevant but much weaker — limited novelty, vague presentation, only 3 models |
| HuNoNfiQqH.md | 4.75 | 1 | Jailbreak vector from latent space; related but less systematic |
| hTEGyKf0dZ.md | 4.75 | 1 | Fine-tuning compromises safety; similar theme but our paper has more systematic evaluation and novel universal attack |
| 1zt8GWZ9sc.md | 3.67 | 1 | Role-playing jailbreaking; simpler method |
| YGoFl5KKFc.md | 4.75 | 1 | SafetyLock for fine-tuned models; defense paper |
| H6UMc5VS70.md | 5.75 | 2 | FlipAttack; rejected, simpler jailbreaking method |
| fFtmpqLFvw.md | 5.75 | 2 | Multi-turn red teaming; rejected, narrower scope |
| hXA8wqRdyV.md | 6.14 | 1,2 | Simple adaptive jailbreaking; accepted, comparable impact but stronger threat model (logprob access). Our paper has more novel attack construction |
| wvFnqVVUhN.md | 6.25 | 2 | Transferable image jailbreaks; different modality |
| YzxMu1asQi.md | 6.50 | 1 | Adversarial activation attacks; accepted, directly comparable — both study attacks on activations, similar quality |
| aSy2nYwiZ2.md | 6.67 | 2 | Universal jailbreak backdoors; accepted, comparable novelty |
| eC4WlSZc4H.md | 6.75 | 2 | Robustness over time; rejected despite high score |
| wozhdnRCtw.md | 7.00 | 1 | Activation steering for instruction following; positive use case, less comparable |
| r42tSSCHPh.md | 7.00 | 1,2 | Generation exploitation jailbreak; accepted, simpler method but very clean results |
| sULAwlAWc1.md | 7.00 | 2 | Robust jailbreak prompts; accepted, strong but different focus |
| Bo62NeU6VF.md | 8.00 | 1 | Backtracking for safety; much stronger — different paradigm |
| tTPHgb0EtV.md | 8.00 | 1 | Booster for harmful fine-tuning; defense paper, stronger |
| 4KqkizXgXU.md | 8.00 | 1 | Curiosity-driven red-teaming; stronger RL-based approach |
| SPS6HzVzyt.md | 8.00 | 1 | Context-parametric inversion; not comparable |

**Bracketing**: Round 1 placed the paper in 6.0–7.0 based on comparison with rejected papers below 5.75 and accepted papers at 6.14–7.00. Round 2 confirmed this range, with the closest comparators being hXA8wqRdyV (6.14) and YzxMu1asQi (6.50). The paper's novel universal attack construction and systematic evaluation place it at or slightly above 6.50, while the confounded SAE comparison prevents it from reaching 7.00.

**Final score: 6.5** — the paper makes a meaningful and novel contribution to understanding safety implications of activation steering, with the universal attack construction being a standout result. The SAE comparison weakness is real but does not undermine the core finding about random steering breaking alignment.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>