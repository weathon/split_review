Here is my final consolidated review:

## Summary

The paper introduces GFNSeqEditor, a method that uses a pre-trained GFlowNet's state-flow function to identify "sub-optimal" positions in a biological seed sequence and then stochastically sample replacements for those positions. The approach is evaluated on three real-world datasets (TFbinding, AMP, CRE) for sequence editing, and also demonstrated for assisting generative models and for length-reduction via sequence combination. The paper reports consistent improvements over Directed Evolution, Ledidi, GFlowNet-E, and Seq2Seq baselines in terms of property improvement at comparable or lower edit percentages.

## Strengths

- **Principled sub-optimal position identification using state flow (Section 3.1, Equation 6):** The method uses the pre-trained GFlowNet state flow \(F_\theta(\cdot)\) to decide where to edit. Because the state flow at a prefix is proportional to the total reward of all completions with that prefix, this brings global information about the sequence space to bear on the editing decision, distinguishing the approach from local-search methods like evolution and Ledidi.

- **Consistent empirical improvement across multiple datasets (Table 1, Figure 2):** GFNSeqEditor achieves higher Property Improvement (PI) than all four baselines (DE, Ledidi, GFlowNet-E, Seq2Seq) on TFbinding, AMP, and CRE while maintaining comparable or lower Edit Percentage (EP). For example, on CRE the method attains PI=0.018 with EP=0.008 vs. Ledidi's PI=0.012 with EP=0.014.

- **Demonstrated versatility beyond single-sequence editing (Sections 4.2, 4.3):** The method is shown to (a) complement a diffusion model for sequence generation (Table 2), improving property while preserving diversity, and (b) achieve sequence length reduction by over 63% while retaining ~65% similarity to the parent long sequence (Table 3). These extensions expand the practical utility of the core contribution.

## Weaknesses

### Fatal
None — the core claims about the algorithm's effectiveness are supported by the empirical results. The identified issues require clarifications and strengthening but do not invalidate the paper's central contribution.

### Major

- **No measures of uncertainty in experimental results (Table 1, Figures 2–5).** All results are reported as point estimates without error bars, confidence intervals, or standard deviations. With the small number of datasets and modest numerical differences between methods, it is impossible to assess whether the reported advantages are statistically significant or within the noise of a single run or dataset split. This weakens the evidential strength of the empirical claims and is a standard expectation for experimental papers at this venue.

- **Sequence combination experiment lacks any baseline comparison (Section 4.3, Table 3).** The results are presented in isolation — no comparison against simple baselines (e.g., truncating the long sequence, applying Ledidi/DE for length reduction, or random shortening). Without a reference point, it is unclear whether the reported 63% length reduction with maintained property is competitive or trivial. This section is presented as a claimed contribution (contribution 5 in the introduction) but is not rigorously evaluated.

### Minor

- **The "oracle" used for evaluation is not specified (Section 4, line on "oracle").** The paper states "we leverage an oracle to obtain \(\hat{y}_i\)" but never states what this oracle is: an independently trained predictor? The same reward model used to train the GFlowNet? While using the same reward model for both training and evaluation is standard in this line of work (Jain et al. 2022, Sinai et al. 2020) and the method-to-method comparison remains fair, the paper should state this explicitly for clarity and to allow readers to assess the scope of the findings. If the oracle and the GFlowNet reward function are the same, a brief acknowledgment and discussion of the limitation would also be appropriate.

- **Theorem 1 bounds absolute reward, not improvement over the seed (Section 3.3).** The paper's introduction claims "deriving a lower bound on the property enhancement" (contribution 2), but Theorem 1 gives a lower bound on the *expected reward of the edited sequence* (\(\mathbb{E}[R(\hat{\mathbf{x}})|\mathbf{x}]\)), not on the *improvement* over the original seed (\(\mathbb{E}[R(\hat{\mathbf{x}})-R(\mathbf{x})]\)). A bound on the absolute reward does not directly certify that the edited sequence is better than the seed (the seed's reward could be above the bound). The paper's language is ambiguous and should be clarified; the theorem is still informative but the claim about "enhancement" specifically is not fully supported by the stated bound.

- **DE baseline implementation selects random positions before applying directed evolution (Section 4).** The paper states: "we select a set of positions uniformly at random within a given sequence and then apply the directed-evolution algorithm to edit these positions." Standard directed evolution mutates the entire sequence and uses a proxy model to select the best variant. The random pre-selection of positions is an additional restriction that may weaken the baseline relative to a full implementation. The authors should justify this design choice or show that it does not disadvantage DE.

- **Hyperparameter selection not discussed (Section 4, Tables/Figures).** The paper does not explain how \(\delta, \sigma, \lambda\) were chosen for the main results in Table 1 and Figure 2. Whether the reported values come from a held-out validation sweep, the same values are used across datasets, or the results reflect the best among a sweep is not stated. This is important for reproducibility and for understanding the difficulty of applying the method to new tasks.

- **Number of oracle calls / computational budget for baselines not specified (Section 4).** The paper does not report how many oracle calls DE and Ledidi were allowed per seed sequence or how many rounds of evolution were run. A fair comparison requires matching the evaluation budget across methods.

### Trivial

None.

## Nice-to-Haves

- The theoretical analysis could be strengthened by restructuring Theorem 1 to directly bound \(\mathbb{E}[R(\hat{\mathbf{x}}) - R(\mathbf{x})]\) (improvement over the seed) rather than the absolute reward of the edited sequence. An ablation where edits are made at randomly selected positions (rather than using the flow-based identification) would help isolate the contribution of the sub-optimal-position detection mechanism. Reporting results across multiple random seeds or bootstrap resamples would address the variance concern.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Equations 7–9 are missing from the main body" (Harsh Critic).** The reviewer noted that equations referenced in the text (7, 8, 9) are absent from the extracted text. However, these are PDF parsing artifacts — the equations exist in the original submission. The instructions specify that parser-stripped content should not be treated as author errors.

2. **"Theoretical analysis does not support the claimed property enhancement" as a fatal flaw.** The reviewer characterized this as a fundamental weakness. While the concern about Theorem 1 bounding absolute reward rather than improvement is valid (kept as a Minor weakness above), the characterization as fatal is too strong. The theorem still provides theoretical grounding for the method's behavior, and the paper's empirical results independently support the effectiveness claim. The bound depends on \(\sigma, \lambda\) being "never defined" — but \(\sigma\) and \(\lambda\) are referenced in context of the editing procedure and their effects are studied empirically (Figures 3, 4). The missing definitions are partly attributable to parser stripping of the equations that define them.

3. **Reproducibility concerns about "undisclosed hyperparameters" and "trivial implementation details."** The reviewer raised concerns about undisclosed hyperparameters and implementation details. Per the instructions, nitpicks about undisclosed hyperparameters or trivial implementation details should be removed as reproducibility concerns that are standard for this type of paper. The hyperparameter selection concern (kept as Minor above) refers specifically to the lack of discussion of how \(\delta, \sigma, \lambda\) were chosen for the main results — a methodological rather than a reproducibility concern.

4. **"Evaluation is circular" (Harsh Critic's strongest framing).** The argument that using the same oracle for training and evaluation makes the evaluation "circular" and invalid is overblown. All methods (DE, Ledidi, GFlowNet-E, Seq2Seq, GFNSeqEditor) are evaluated against the same oracle; the comparison between methods is therefore meaningful regardless of what the oracle is. The paper's claim is that GFNSeqEditor is a better optimizer of the property function, which is demonstrated fairly even if the oracle is the same model used to train the GFlowNet. The need for the paper to state what the oracle is (kept as Minor) is a clarity issue, not a fatal flaw.

## Novel Insights

None beyond the paper's own contributions. The reviews and the paper itself converge on the same observations: the core algorithmic idea (using GFlowNet flow for guided sequence editing) is novel and the empirical results are promising, but the evaluation would be strengthened by proper uncertainty quantification and more complete baseline descriptions.

## Suggestions

1. Report all main results (Table 1, Figure 2) with error bars, confidence intervals, or at minimum results over multiple random seeds.
2. Explicitly state what model(s) serve as the oracle for each dataset and whether the GFlowNet reward function is the same oracle.
3. Add a simple baseline to the sequence combination experiment (e.g., truncation, or applying another editing method for length reduction).
4. Clarify the relationship between Theorem 1's bound and the claim of "property enhancement" — either restate the claim or restructure the bound to directly address improvement over the seed.
5. Describe how hyperparameters \(\delta, \sigma, \lambda\) were selected for the main results (e.g., validation set sweep, fixed across datasets).
6. Report the computational budget (oracle calls, rounds) allocated to DE and Ledidi to confirm fair comparison.
7. The DE baseline's random position pre-selection should be justified or removed to avoid weakening the comparison.

## Score and Decision

**Originality:** 7/10 — Using GFlowNet flow for sequence editing via sub-optimal position identification is a novel combination of existing ideas.

**Importance of research question:** 8/10 — Biological sequence editing is a practically important problem with limited ML methods.

**Claims well supported:** 5/10 — The main empirical results point in the right direction but lack statistical rigor; the theoretical claim about property enhancement is not fully supported by the stated bound.

**Soundness of experiments:** 5/10 — Reasonable scope of datasets and baselines, but lacking uncertainty quantification, oracle specification, and baseline-comparison details.

**Clarity of writing:** 6/10 — The core ideas are clearly conveyed, but hyperparameters \(\sigma, \lambda\) are not fully explained in the extant text, and the oracle is not identified.

**Value to the research community:** 7/10 — The method is potentially useful and the idea of leveraging GFlowNet flow for guided editing could inspire follow-up work.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>