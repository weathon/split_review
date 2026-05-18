Now I have a thorough understanding of the paper and the review inputs. Let me produce the final consolidated review.

## Summary

Sparling introduces a spatial sparsity layer combined with an adaptive annealing algorithm that enforces extreme activation sparsity (>99.9%) in an intermediate representation of a neural network. The method enables recovery of ground-truth latent structure ("motifs") from end-to-end supervision alone, without intermediate labels. The authors demonstrate this across three domains (synthetic DigitCircle, rendered LaTeX, spoken digits), achieving motif identification errors below 10% in most settings while operating at sparsity levels unmatched by L₁ or KL-divergence baselines.

## Strengths

- **Achieves extreme sparsity unmatched by prior methods.** Sparling reaches 99.995% sparsity on DigitCircle (0.005% density), whereas L₁ baselines remain at 0.023% density or higher, and KL-divergence fails to go below 0.1% density. At these sparsity levels, Sparling maintains low end-to-end error, while L₁ at comparable density exceeds 70% error (Table 1). This is a clear empirical advance over existing sparse-activation techniques.

- **Recovers ground-truth motifs from end-to-end supervision alone.** Across all three domains, motif errors (FPE, FNE, CE) average below 10%, with confusion error often ≤2% after channel permutation (Figures 2–3). The method demonstrates what the paper terms "Motif Identifiability" — recovering the positions and identities of latent motifs without any intermediate labels.

- **Adaptive sparsity annealing is essential for stable training.** The ablation studies (Section 5.3) confirm that both the batch-normalization layer before the sparsity layer and the annealing schedule (Algorithm 1) are critical. Starting at the final low density yields >68% end-to-end error, verifying that the adaptive component is necessary for the method's success.

- **Thorough empirical methodology.** The paper reports results across three distinct domains (image, rendered text, audio) with 9 seeds per setting, provides multiple metrics (E2EE, FPE, FNE, CE), includes confusion matrices, baselines with two alternative sparsity methods, and ablation studies. This careful experimental design increases confidence in the robustness of the findings.

- **Generalization to unseen speakers on AudioMNIST.** The test set includes speakers not seen during training (speakers 52–60, trained on 1–51). Low motif errors on this held-out data indicate the model learns genuine motif features rather than memorizing training instances.

## Weaknesses

### Major

- **The information-bound derivation (§2.4) is incomplete and contains undefined quantities.** The derivation in Section 2.4 attempts to connect sparsity to an information bottleneck, but the symbol η is never defined. The paper jumps from per-channel entropy to `H(M[i,c]) ≤ H(B(δ_{i,c})) + η·δ_{i,c}` with no explanation of what η represents, where the bound comes from, or what assumptions are needed. The label `\label{sec:defines-eta}` suggests a definition was intended but is absent. Furthermore, even if the derivation were completed, the final bound `I(𝒳,ℳ) ≤ SC(H(B(δ)) + ηδ)` — where `S` is image size in pixels and `C` is channel count — is potentially vacuous for large images. Since the paper's abstract positions Sparling as using "a new kind of informational bottleneck," this section needs to either present a complete, well-defined derivation or be reframed as heuristic motivation. The paper's core empirical contributions stand without this derivation, but the theoretical framing as currently written is not rigorous.

### Minor

- **The Motif Identifiability claim lacks discussion of when it might fail.** The paper states that if g* and ĝ satisfy sparsity, locality, and necessity, and f̂ ≈ f*, then ĝ ≈_m g*, and calls this "an empirical claim" validated in experiments. This framing is acceptable for an empirical paper, but the paper would benefit from a clearer discussion of the limitations and failure modes of this claim. For example: under what conditions could two different sparse, local, necessary functions produce the same input-output mapping? When do violations of each assumption manifest? The experimental analysis of LaTeXOCR (where high FNE is attributed to unnecessary motifs like fraction bars) shows the authors have insight into this, but it is not systematized into a more general discussion of when practitioners should expect the method to work or fail.

- **FPE of exactly 0 on AudioMNIST is unexplained.** Figure 3 shows that all 9 seeds achieved exactly 0% false positive error on AudioMNIST. While this could be genuine (the metric's generosity thresholds or the domain's properties might explain it), the paper provides no discussion of how this is possible. A brief explanation — whether this reflects a property of the metric definition, the thresholding, or the domain — would help readers assess the result.

- **Sensitivity to the δ_update hyperparameter is not analyzed.** Algorithm 1 has two key hyperparameters (d_T and δ_update = 0.75), and the paper reports only a single setting without analyzing sensitivity. If the method is sensitive to the exact value of δ_update, this would be important for reproducibility. An analysis or ablation on this parameter would strengthen the paper.

- **The strong sparsity assumption ("real-world processes often contain intermediate state that can be modeled as an extremely sparse tensor") is stated without qualification.** The paper's examples (economic signals from satellite data, transcription from audio) are plausible but no evidence or citations are provided that such representations are actually sparse in practice. The method requires extreme sparsity to work, and the paper does not discuss how to detect or diagnose settings where this assumption fails. A brief discussion of limitations/scope would improve the paper.

### Trivial

- The derivation in §2.4 has a broken sentence structure at line 129 ("Then, let δ_{i,c}") followed by a blank line, suggesting the derivation may have been truncated in the submission or the PDF extraction introduced artifacts.

## Nice-to-Haves

- A small-scale theoretical toy case (e.g., one-dimensional or binary-input setting) where motif identifiability can be formally proven would strengthen the scientific foundation, though this is not necessary for the paper's empirical contribution.
- A systematic failure analysis across all three domains indicating what fraction of errors are attributable to violations of each assumption (sparsity, locality, necessity) would give practitioners a clearer sense of when to expect the method to work.

## Removed Points

The following points from the reviews were removed for the reasons indicated:

1. **"Novelty is not clearly delineated from prior quantile-based work"** — The paper already acknowledges Bizopoulos et al. (2020) as using "a quantile-based activation limit equivalent to both of our ablations combined, but in the simpler context of linear h and g models" (line 64). The paper clearly distinguishes its contributions: the adaptive sparsity algorithm (Algorithm 1) and the empirical demonstration that this yields motif recovery across diverse non-linear settings. The prior work is honestly cited and the novel elements are identifiable.

2. **"Retrained baseline undermines end-to-end framing"** — The Retrained experiment (freezing ĝ and retraining ĥ) is presented as a *validation* that the motifs learned by Sparling are meaningful, showing that removing the bottleneck recovers most of the performance gap. This strengthens, not undermines, the paper's claims.

3. **Strength Finder: "Connects sparsity to information-bottleneck theory, grounding the method theoretically"** — This conflicts with the verified weakness that the derivation is incomplete and η is undefined. The connection is conceptually indicated but not properly established. Moved here to avoid overstatement.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Complete or remove §2.4. Either properly derive the entropy-to-sparsity bound with clearly defined terms, or reframe this subsection as heuristic motivation (e.g., "Sparsity as an Informal Information Bottleneck") without claiming a rigorous derivation.

2. Add a brief discussion of when the Motif Identifiability claim might fail, systematizing the insights already present in the LaTeXOCR analysis (where unnecessary motifs are correctly ignored).

3. Explain the FPE=0 result on AudioMNIST — even a short sentence about the metric or domain properties would suffice.

4. Add an ablation on δ_update or at minimum a statement about the range over which the method is stable to this hyperparameter.

5. Qualify the claim that "real-world processes often contain intermediate state representable as extremely sparse tensors" with a brief discussion of scope and limitations.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>