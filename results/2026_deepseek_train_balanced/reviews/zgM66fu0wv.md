Now I have sufficient understanding of the paper to write the consolidated review. Let me produce the final output.

## Summary

IRIS proposes an end-to-end framework for causal discovery that automatically retrieves web documents, uses LLMs to extract variable values into a structured dataset, applies a hybrid of statistical causal discovery algorithms (PC/GES/NOTEARS) with LLM-based causal relation verification, and proposes missing variables to iteratively expand the causal graph. The paper evaluates the full pipeline and each component individually across five biomedical datasets.

## Strengths

1. **Hybrid causal discovery (statistical + LLM verification) consistently outperforms both purely statistical and purely LLM baselines across all five datasets.** Tables 3–7 show that IRIS-hybrid achieves higher F1 and lower NHD ratio than PC, GES, NOTEARS, Pairwise-LLM, BFS-LLM, and COAT on Cancer, Respiratory Disease, Diabetes, Obesity, and ADNI. The ablation of VCR (verified causal relations) demonstrates that the textual verification component adds measurable value over statistical methods alone.

2. **The missing variable proposal component is well-evaluated with a clean simulation setup and informative ablations.** Section 7.2 (Table 8) shows MVP-GPT-4o achieving 0.80–1.00 success rates across five datasets, substantially above the prompt-only baseline (0.00–0.60). The ablation conditions (MVP-NoVCR, MVP-NoStats) disentangle the contributions of the verification and statistical approaches, showing both matter. The simulation design (systematically removing one variable from known ground-truth graphs) is a reasonable evaluation strategy for an inherently hard-to-evaluate task.

3. **Automated data collection and value extraction eliminates reliance on pre-collected datasets.** Section 5.2 (Table 2) shows IRIS's extraction with GPT-4o outperforms COAT (also using GPT-4o) on both AppleGastronome and Neuropathic datasets, and the stepwise query construction (Section 3.2) provides a principled approach to document retrieval for multi-variable causal questions.

4. **Iterative framework design enables progressive expansion of causal graphs.** The architecture (Section 3.4) that feeds proposed missing variables back into the pipeline is a genuine architectural contribution that goes beyond static causal discovery methods. Section 4 demonstrates this on expanded graphs with expert-annotated ground truth achieving Krippendorff's alpha of 0.88.

## Weaknesses

### Fatal
None.

### Major

1. **Unvalidated and underspecified claims about relaxing the acyclicity and causal sufficiency assumptions.** The paper repeatedly claims (Section 1, line 14; Section 3, line 36; Section 8) that the hybrid approach "allows cycles in causal graphs" and relaxes causal sufficiency, but:
   - **No mechanism for handling cycles is described.** The statistical backbone (PC, GES, NOTEARS) all enforce acyclicity by design. Graph merging (Section 3.3) simply adds VCR edges to the statistical output — no algorithmic accommodation for handling cycles, resolving conflicts, or even detecting when a cycle arises is provided. The paper merely asserts the hybrid approach "allows cycles" without specifying how.
   - **No experiment uses cyclic ground-truth graphs.** All five datasets (Cancer, Respiratory Disease, Diabetes, Obesity, ADNI) are standard acyclic causal graphs. There is zero empirical evidence that IRIS can correctly discover or represent cycles.
   - **The causal sufficiency relaxation is not validated either.** The missing variable proposal suggests variables, but Section 7 only tests whether the component can *recover a removed variable* — it never tests whether including the proposed variable actually *corrects a confounding bias* in the causal discovery. Adding an extra variable to a statistical algorithm running on the same co-mention data doesn't automatically resolve confounding.
   
   These are central claims of the paper (listed as contributions 2 and 3). Asserting them without algorithmic specification or experimental validation is a significant gap.

2. **The data matrix constructed from web documents does not satisfy the distributional assumptions of the statistical causal discovery algorithms that form the method's backbone, and the paper does not address this mismatch.** The method assembles $\mathbf{X}$ where each row corresponds to a web document and each column to a variable, with LLM-extracted values (Section 3.2). PC, GES, and NOTEARS assume rows are i.i.d. samples from a *joint distribution* over the variables. IRIS's rows are heterogeneous text sources — news articles, blog posts, abstracts — with different selection biases, reporting conventions, and relevance. The extracted value reflects whether a document *mentions* a variable, not a measurement from a shared data-generating process. The statistical associations found reflect co-mention patterns in web text, not actual causal dependencies in a population. This is a structural concern about what the method actually measures. The paper never discusses this issue or justifies why this approximation is valid. (Note: this concern is mitigated but not resolved by the empirical results showing the method produces reasonable outputs — it should be acknowledged and discussed.)

### Minor

1. **"Real-time" is mentioned in the title, abstract, and introduction but never defined, operationalized, or measured.** No timing experiments, latency measurements, or comparisons of data collection speed are provided. It is unclear what "real-time" means in this context — minutes? hours? — or what advantage it conveys beyond automation.

2. **The main evaluation of expanded causal graphs (Section 4) compares IRIS against a single weakly-specified "Prompt" baseline.** The baseline is described only as using "LLM to determine causal relations among expanded variables." It omits all of IRIS's components (statistical discovery, VCR, etc.). While other evaluations (Sections 5–7) have strong baselines, the flagship full-pipeline comparison (Table 1) lacks the informative baselines (e.g., COAT, statistical-only, VCR-only on the expanded task) needed to attribute the observed improvement to specific design choices.

3. **No discussion of limitations.** The paper has no limitations section. Given the significant caveats around data validity, unvalidated assumption relaxations, and evaluation design (expert opinion as ground truth), this is a notable omission.

4. **The value extraction evaluation (Section 5) uses curated table-to-text datasets where each document is a text description of a specific row.** The actual IRIS scenario involves arbitrary web documents with no pre-existing mapping to variable values. The distribution shift between these settings is not discussed.

5. **Missing variables when a document does not mention a variable are not addressed.** Section 3.2 describes how values are extracted when a document is relevant, but does not specify what happens when a document does not mention a variable — whether the value is treated as 0, left as missing, or the document is discarded. This has significant implications for the constructed dataset $\mathbf{X}$ and the downstream statistical analysis.

6. **The missing variable proposal evaluation (Section 7) tests recovery of a specifically removed variable, which is narrower than the claimed capability of proposing "genuinely causally relevant unobserved variables" in an open-ended setting.** The simulation is well-designed for what it does, but extrapolating from "recover the variable we just deleted" to "identify unknown confounders/mediators in real settings" is a leap.

### Trivial

None.

## Nice-to-Haves

- Validate the constructed data against real observational data in a domain where both exist (e.g., biomedical datasets with known ground-truth data), comparing the statistical associations found in the constructed data against those in the real data.
- Provide a concrete example causal graph produced by IRIS to help readers assess what the system actually discovers (beyond aggregate F1/NHD scores).
- Test the method on a domain with known cyclic causal structures (e.g., predator-prey dynamics, economic feedback loops) to support the acyclicity relaxation claim.
- Specify the numerical thresholds for document retrieval count, "high-confidence" in graph merging, and "majority" in VCR verification.

## Removed Points

These points were flagged by reviewers but are removed from the main review:

- **Harsh critic's claim about PMI formula issue (C being problematic):** The paper's PMI derivation correctly shows that log C is an additive constant that cancels out when ranking variables, so this is mathematically unproblematic. The critic's concern is unfounded.
- **"Co-mention data is not observational data" framed as fatal in the harsh critic's review:** I have downgraded this to Major (see Weakness 2). The empirical results demonstrate the approach produces meaningful outputs, so it is not structurally fatal. However, the concern is real and should be addressed.
- **Generic criticisms about "no example prompts shown" or "reproducibility concerns" about Google API non-determinism:** These apply to most papers using commercial APIs and are not specific weaknesses of this paper.
- **Strength Finder's claim that the paper "eliminates pre-existing dataset reliance" being the "single most important piece of evidence":** Overstated. The evidence is solid but multiple pieces support the contribution.
- **Strength Finder's claim about "iterative capability distinguishing IRIS" being a unique strength:** True but it's a design feature whose benefit is only weakly tested in the evaluation. Kept in Strengths but qualified.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation is the tension between the paper's strongest empirical finding and its weakest claimed contribution. The hybrid causal discovery (statistical + VCR) consistently outperforms baselines — this is the paper's best-supported result. Yet the paper frames its central contribution as relaxing acyclicity and causal sufficiency assumptions, for which there is neither algorithmic specification nor experimental evidence. The paper would be stronger if it demoted these unvalidated claims and elevated its well-supported contributions: the automated data pipeline and the demonstration that combining co-mention statistics with textual verification yields better causal graphs than either approach alone. The iterative expansion framework is also genuinely novel, though its evaluation against a single weak baseline leaves room for future work to test it more rigorously.

## Suggestions

1. Either provide a concrete algorithmic mechanism for handling cycles (e.g., cycle-aware merging that resolves conflicts between the DAG-constrained statistical graph and VCR edges) or remove the acyclicity relaxation claim and treat it as a potential property of the hybrid approach that requires future investigation.
2. Add a limitations section that candidly discusses the data construction validity concern, the expert-opinion-as-ground-truth limitation, and the unvalidated assumption relaxations.
3. Strengthen the Section 4 evaluation with at least one informative baseline (e.g., COAT on the expanded graph task, or statistical-only on the same pipeline) to complement the weak "Prompt" baseline.
4. Clarify what "real-time" means — provide timing measurements or, if it only means "automated," replace the term to avoid overclaiming.
5. Discuss how documents that do not mention a variable are handled during value extraction, and how missing values in the constructed dataset $\mathbf{X}$ are treated by the statistical algorithms.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>