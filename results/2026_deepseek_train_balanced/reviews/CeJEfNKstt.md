Now I have all the information needed to write the final consolidated review. Let me construct it carefully.

## Summary

This paper investigates whether LLaMA-2 models linearly represent the truth value of factual statements, using three lines of evidence: PCA visualizations, probe generalization experiments, and causal interventions. The authors curate high-quality true/false datasets designed to disentangle truth from correlated features (e.g., text probability). They find evidence that at larger scales, linear separation of true vs. false statements emerges across diverse datasets, and that mass-mean probing identifies directions that are more causally implicated in model outputs than logistic regression or CCS.

## Strengths

- **Principled dataset design that controls for confounds**: The paper constructs datasets with negations (`neg_cities`, `neg_sp_en_trans`) where truth anti-correlates with text probability ($r=-.63$, $r=-.89$, line 84), plus a `likely` dataset of nonfactual text. This allows the paper to argue that the observed linear structure reflects truth rather than text plausibility — probes trained on `likely` perform poorly on datasets where probability anti-correlates with truth (line 250, Fig. 4).

- **Causal intervention evidence on out-of-distribution inputs**: Section 6 (Table 1) goes beyond classification accuracy to measure normalized indirect effects (NIEs) of intervening on group (b) hidden states, showing that shifting activations along mass-mean probe directions can flip model outputs on OOD data (`sp_en_trans`). This provides causal evidence that prior probing work (e.g., Li et al. 2023) did not evaluate on OOD inputs (line 256).

- **Mass-mean probing is a cleanly motivated methodological contribution**: The paper identifies a principled failure mode of logistic regression under superposition (Fig. 2, Section 4.1) and introduces mass-mean probing as a simple, optimization-free alternative that explicitly tracks a candidate feature direction separate from the decision boundary. MM probes generalize comparably to LR/CCS at larger scales yet outperform them in 7/8 causal intervention conditions (Table 1).

- **Scaling analysis across three model sizes**: The paper provides evidence across LLaMA-2 7B, 13B, and 70B that larger models develop more abstract linear truth representations — 7B clusters by surface features (e.g., token "eighty"), while 70B shows alignment across diverse datasets (Fig. 3, line 160). This scaling evidence is more systematic than prior single-model studies.

- **Causal localization to specific hidden states**: Section 3 uses patching experiments to pinpoint group (b) hidden states (over the final token and punctuation) as causally implicated, rather than treating all positions uniformly. This localization directly guides the subsequent analysis.

## Weaknesses

### Fatal

None.

### Major

- **Claims about "LLMs" generally are unsupported by evidence from one model family**: The paper studies only LLaMA-2 (7B, 13B, 70B) but the title claims "Large Language Model Representations" and the abstract states "at sufficient scale, LLMs linearly represent the truth" — a claim about LLMs in general. While the limitations paragraph (line 326) notes this, the title and abstract are not scoped accordingly. Different model families (Pythia, Gemma, Mistral) have different training data, objectives, and representational geometries. Without at least one additional architectural family, the central claim is an overstatement. The paper can legitimately claim that LLaMA-2 models show this behavior, not LLMs in general.

- **The `likely` intervention results are an unresolved puzzle that complicates the core narrative**: Mass-mean probes trained on the `likely` dataset (nonfactual text where the final token is the most vs. 100th most probable completion) achieve surprisingly high NIEs on `sp_en_trans` — 0.70/0.54 (13B) and 0.68/0.27 (70B) in Table 1 — despite these probes being poor at classifying true/false statements (line 250). The paper notes this as an open question (lines 319, 328), but the tension is more consequential than acknowledged. If a direction extracted from *nonfactual, probability-based* text can causally alter truth judgments, the claim that what is being measured is specifically "truth" is undermined. The interventions may be manipulating a shared subspace corresponding to text probability or fluency that happens to correlate with truth on the test inputs. The correlational evidence (`neg_cities` anti-correlation) and the causal evidence (`likely` interventions) point in opposite directions on this question, and the paper does not resolve the contradiction. The `likely` direction applied to anti-correlated data (e.g., `neg_cities` statements) would be a natural control experiment to disentangle these, but is not performed.

### Minor

- **Probing results lack uncertainty quantification**: The probing experiments (Fig. 4) report accuracies without confidence intervals, standard errors, or evidence of multiple random train/test splits. The paper states probes are trained on a random 80% split (line 212) but does not specify how many random seeds or repeats were used. Given that some datasets are small (e.g., `sp_en_trans` has only 354 statements), and that the comparisons between LR, MM, and CCS sometimes involve differences of a few percentage points, the absence of error bars makes it difficult to assess whether observed differences are significant.

- **Intervention comparison between MM and LR has an uncontrolled normalization**: The intervention experiments normalize each probe's direction θ so that p(μ⁻ + θ) = p(μ⁺) (line 289) — i.e., normalized by each probe's own decision boundary. If LR and MM identify genuinely different directions, normalizing by their own (potentially different) decision boundaries could mean the step sizes in the residual stream are not comparable across methods. A cleaner comparison would fix the step magnitude (e.g., ∥θ∥) across methods and measure whether MM's direction still produces larger causal effects. As presented, the claim that MM directions are "more causally implicated" is suggestive but not fully controlled on this point.

- **CCS comparison is slightly asymmetric**: CCS requires contrast pairs (statements with opposite truth values), so it is trained on paired data from `cities`/`neg_cities` and `larger_than`/`smaller_than` (line 210). This means CCS receives structurally different training data than LR/MM in some conditions, making the comparison less than fully controlled. The paper does not explicitly note this asymmetry.

- **Anti-correlation evidence uses the same model family**: The anti-correlation values between truth and text probability (r=-.63, r=-.89) are computed using LLaMA-2-70B log-probabilities (line 84). The argument that the linear structure reflects truth rather than probability thus relies on probability estimates from the *same model family* under study, which introduces a mild circularity. An independent probability model would strengthen this evidence.

### Trivial

None.

## Nice-to-Haves

- A control experiment applying the `likely` probe direction to anti-correlated data (e.g., `neg_cities` statements) could help determine whether the `likely` direction flips truth judgments in the wrong direction, which would strengthen the case that truth and probability are distinct features.
- Testing at least one additional model family (e.g., Mistral or Gemma at multiple scales) would substantially broaden the generality of the claims.
- A controlled intervention comparison where the step magnitude ∥θ∥ is fixed across methods, rather than normalized by each probe's decision boundary.
- Analyzing which specific tokens within group (b) yield the most informative probe directions.

## Removed Points

These points were flagged by reviewers but are removed with brief justifications:

- **"Patching localization only done on one dataset"**: The paper states (line 103) that results for more models and datasets are in the appendix. Following the rule that appendix-stripping artifacts should not be held against the paper, this is removed.
- **"No mention of compute budget or reproducibility details"**: This is a reproducibility nitpick about undisclosed hyperparameters and implementation details, which is standard practice not to report fully in interpretability papers. Removed per filtering guidelines.
- **"No analysis of which tokens in group (b) matter most"**: While a reasonable suggestion, the paper's choice to use the most downstream hidden state is standard and justified. Moved to Nice-to-Haves.
- **"Headline claim stronger than evidence warrants (synthetic)"**: The substantive content of this criticism is covered under the two Major weaknesses above (narrow model family and `likely` puzzle). The synthesis-level concern about the three evidence lines each having caveats was already acknowledged by the paper itself and does not add new information beyond the specific verified weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Scope the title and abstract to LLaMA-2**: Replace "LLMs" with "LLaMA-2 models" or add a qualifier like "in the LLaMA-2 family" to match the actual evidence.
2. **Address the `likely` puzzle directly**: Run the suggested control experiment (apply the `likely` direction to `neg_cities` statements where truth and probability are anti-correlated). If the `likely` direction flips truth judgments in the wrong direction on anti-correlated data, this would significantly strengthen the case. If it does not, the paper needs to engage honestly with the implications.
3. **Add confidence intervals or error bars** to all probing results, even if via simple bootstrap over train/test splits.
4. **Run a controlled intervention comparison** where MM and LR directions are normalized by ∥θ∥ rather than by each probe's own decision boundary, to rule out the normalization artifact concern.

## Score and Decision

The paper makes a genuine contribution — the dataset design is principled, the causal intervention experiments are well-executed, and mass-mean probing is a clean methodological contribution. However, the core claim is overstated relative to the evidence (one model family, unresolved confound from the `likely` results), and several methodological gaps (no error bars, uncontrolled normalization in the causal comparison) weaken the quantitative evidence. These issues are addressable but are not minor.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>