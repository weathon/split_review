Now I have a thorough understanding of the paper's content. Let me synthesize the final review.

The paper heavily relies on `\input` commands for its core technical content (method descriptions with equations, experiment results with tables, analyses). The extracted main text contains the high-level narrative, motivation, and some implementation details, but the detailed technical content is in files that were stripped during text extraction. I will account for this when evaluating the harsh critic's claims.

Let me write the consolidated review.

## Summary

The paper tackles selection bias in LLMs answering multiple-choice questions. It proposes two debiasing methods: Bias Node Pruning (BNP), which removes nodes from the final linear layer that contribute to bias, and Auxiliary Option Injection (AOI), which adds an "I don't know" option to the prompt. It also introduces Choice Kullback-Leibler Divergence (CKLD) as a new bias metric that addresses limitations of existing metrics (RStd, RSD) regarding label imbalance. Experiments on ARC-Challenge, MMLU-Redux, and CommonsenseQA with Llama-3, Mistral, and Bloomz show accuracy improvements up to 24.9%, with compatibility demonstrated for black-box models and existing methods (CoT, ICL, DCL).

## Strengths

- **Novel parameter-level approach to debiasing.** BNP is the first work to target selection bias by pruning internal parameters (as few as 32/4096 nodes) rather than modifying only input/output. This is a genuinely new direction supported by the paper's motivating finding that bias is represented in the final decoder layer (Sec. 2, Sec. 3).
- **AOI is a simple, black-box-compatible method.** Adding an "I don't know" option is trivially deployable, requires no model access beyond token probabilities, and is shown to work across both open-source and closed-source models (Sec. 5.2). This broadens practical applicability.
- **CKLD targets a real gap in existing metrics.** The paper correctly identifies that RStd and RSD are insensitive to label imbalance, and CKLD is motivated as a distribution-based metric that remedies this. Formal definition and usage in experiments (Sec. 4, Sec. 5) support this contribution.
- **Broad empirical evaluation.** Three models (Llama-3-8B, Mistral-7B, Bloomz-7b1), three datasets (ARC-Challenge, MMLU-Redux, CommonsenseQA), and compatibility with CoT, ICL, and DCL demonstrate robustness (Sec. 5).
- **Out-of-bag sample separation for bias vector computation.** Using a separate set of samples to compute bias vectors (Sec. 5, line 98) avoids data leakage and strengthens the validity of the pruning decisions.

## Weaknesses

### Fatal

None.

### Major

None that can be confirmed from the extracted text. The harsh critic raises the concern that BNP's pruning specificity is not validated against random/magnitude pruning. This is a substantive concern, but the paper's Section 6 (Analyses) is entirely in an input file (`5_Analyses/bnp`) that was stripped during text extraction. If the existing paper already includes such comparisons, this point is addressed. If not, it would weaken the claim that pruned nodes are specifically bias-related rather than generically unimportant parameters. Since I cannot verify the analyses section, I note this as a potential major issue that must be checked against the full submission.

### Minor

- **AOI output handling is underspecified.** The paper states (line 105) that "we select the choice symbol (e.g., A, B, C, D) with the highest probability." When an auxiliary "I don't know" option is added, it is unclear whether (a) probabilities are computed only over the original option tokens, (b) the auxiliary token competes and is simply ignored in argmax selection, or (c) renormalization is performed. Each choice yields different behavior and the paper must specify this for reproducibility.

- **CKLD lacks a direct validation experiment.** The paper claims CKLD is more sensitive to label imbalance than RStd/RSD but does not (in the visible main text) include a controlled experiment — e.g., injecting synthetic bias into a bias-free model and showing CKLD detects it while RStd/RSD do not. This weakens the contribution of CKLD, though it is not fatal since CKLD is used alongside RSD in the experiments.

- **Variance across out-of-bag splits is not reported.** The paper states "the entire process is not stochastic" (line 107), which is true only for a fixed OOB set. The selection of OOB samples introduces variance in which nodes are pruned. Reporting mean/std or ranges across different OOB partitions would strengthen the evidence and is standard practice.

- **Hyperparameter choice for number of pruned nodes is not justified.** The paper prunes 32 nodes for Llama-3/Mistral and 128 for Bloomz (line 106), but no rule (e.g., fraction of layer size, validation-based selection) is stated in the main text. This information may be in the methods input file, but it should be stated clearly.

### Trivial

- The number of out-of-bag samples used for bias vector computation is not reported in the visible text. This is a small but useful reproducibility detail.

## Nice-to-Haves

- A synthetic bias injection experiment validating CKLD's sensitivity vs. RStd/RSD would strengthen the metric contribution.
- Reporting accuracy and bias metrics across multiple OOB splits (with variance) would improve confidence in the results.
- Varying the auxiliary option text ("I don't know" vs. "Not sure" vs. "None of the above") would strengthen the AOI mechanism analysis.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The paper should include the definition of the average bias vector and how nodes are scored for pruning"** — This definition is in the input file `3_Methods/bias_pruning`, which was stripped by the parser. The original submission contains it.

2. **"CKLD description is missing"** — The evaluation section (`4_Experiments/evaluation`) containing CKLD's mathematical definition is in a stripped input file. The original submission contains it.

3. **"The paper should specify whether CKLD is computed per sample or over the dataset"** — This detail is in the evaluation input file.

4. **"The paper should ensure that the main text discusses the key insights from analyses"** — Sections 6.1–6.3 are entirely in input files that were stripped. The original submission contains these discussions.

5. **"Missing related works" references** — Removed per instructions: I cannot verify existence of missing references with external sources.

6. **"No embedding or parameter-level investigation has been performed" claim too strong** — The harsh critic says this claim "would benefit from acknowledging any logit-level calibration methods that operate before the final layer." Logit-level methods (e.g., Zheng et al.) are already cited in lines 27 and 133. The claim is appropriately scoped given the citations.

7. **Criticism about the process being deterministic implying no error bars needed** — The paper states "the entire process is not stochastic" (line 107), which is re-stating a fact about their modified inference, not arguing against error bars. My review above handles this as a separate (retained) concern about OOB split variance.

## Novel Insights

The harsh critic's main insight is that BNP's mechanism claim requires a specific ablation comparison (random pruning, magnitude-based pruning) to substantiate the "bias-specific" pruning narrative. This is a useful constructive observation that goes beyond what the paper currently validates. The critic also correctly notes that the AOI output handling must be precisely specified for reproducibility. These insights sharpen the evaluation criteria against which the paper should be judged.

Beyond the reviewer inputs, I note that the paper's structural reliance on `\input` files for all technical content (methods, equations, tables, analyses) makes it impossible to fully evaluate from the extracted text alone. This is a systematic issue with the review pipeline, not the paper itself, but it means the present evaluation must be treated as provisional pending verification of those sections.

## Suggestions

1. **Specify AOI output handling precisely.** State clearly whether the auxiliary token is excluded from or included in the argmax, and how "accuracy" is computed when the model outputs "I don't know."

2. **Add a BNP ablation against random and magnitude-based pruning** (if not already in the analyses section) to confirm the pruned nodes are specifically bias-related.

3. **Include a synthetic validation for CKLD** — inject a known bias pattern into a model and show CKLD detects it while RStd/RSD do not.

4. **Report variance across OOB splits** — repeat the pruning process with different OOB partitions and report mean/std of accuracy and bias metrics.

5. **Clearly state the pruning criterion and k selection rule** in the main text, even if also present in the methods section.

## Score and Decision

The paper proposes genuinely novel approaches (BNP, AOI) to a well-recognized problem, with a coherent motivation rooted in the internal representation of selection bias. The main claims are significant and the evaluation covers diverse models, datasets, and compatibility settings. The core concerns — BNP's bias specificity validation, AOI implementation details, and CKLD validation — are addressable in a revision and do not invalidate the contribution. The paper represents a solid contribution to the field.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>