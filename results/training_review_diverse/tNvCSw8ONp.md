Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

---

## Summary

This paper studies selection bias in LLMs answering multiple-choice questions and proposes two debiasing methods: Bias Node Pruning (BNP), which removes a small number of nodes from the final linear layer that contribute to selection bias, and Auxiliary Option Injection (AOI), which adds an "I don't know" option to the prompt. The paper also introduces Choice Kullback-Leibler Divergence (CKLD) as a new evaluation metric that addresses insensitivity to choice label imbalance in prior metrics like RStd and RSD. The methods are evaluated on three datasets (ARC-Challenge, MMLU-Redux, CommonsenseQA) and three LLMs (Llama-3-8B, Mistral-7B, Bloomz-7b1).

## Strengths

- **First parameter-level investigation of selection bias in LLMs.** The paper explicitly distinguishes itself from prior work that only modifies inputs or calibrates outputs, instead analyzing and modifying internal representations. This is a novel direction for the selection bias problem. (Supported by line 27: "no embedding or parameter-level investigation has been performed.")

- **High efficiency through minimal pruning.** The paper reports that dropping as few as 32 out of 4096 nodes in the final layer (128 for Bloomz) can significantly reduce selection bias. This specificity demonstrates a lightweight approach compared to retraining or large-scale calibration. (Supported by lines 33, 106.)

- **New metric (CKLD) motivated by a documented gap in prior metrics.** The paper identifies that existing metrics (RStd, RSD) are insensitive to imbalanced choice labels and can falsely indicate bias. CKLD is proposed to address this gap. (Supported by lines 38–40.)

- **Compatibility with black-box LLMs via AOI.** Auxiliary Option Injection is a simple prompting technique that requires no model-internal access, making it applicable to closed-source API-based models. (Supported by line 35.)

- **Demonstrated synergy with existing methods.** The paper shows that BNP and AOI can be combined with Chain-of-Thought, In-Context Learning, and Decoding by Contrasting Layers. (Supported by lines 45–46, 149.)

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Potential performance degradation on unrelated tasks is not discussed.** The paper does not address whether pruning nodes from the final linear layer degrades capabilities on tasks unrelated to MCQ answering. While the method prunes a small fraction of parameters (32/4096), the paper's available text provides no evaluation on held-out tasks to check for unintended side effects. A debiasing method that harms general performance would have limited practical utility.

- **The magnitude of claimed improvements is extraordinary and would benefit from explicit caveats.** The paper reports accuracy improvements of "up to 24.9%" (line 51) and "up to 33.8% on ARC-Challenge" (line 149) when combined with other methods. These are very large gains on established benchmarks. While the full experimental details reside in the (parser-excluded) experiments section, the paper's visible text does not discuss possible explanations for why such large improvements arise from modifying only the final linear layer, nor does it discuss how the baseline performance compares to standard reported numbers for these models on these benchmarks.

- **The mechanism by which BNP identifies "bias-contributing" nodes raises open questions.** The paper mentions computing "average bias vectors" from a separate set of out-of-bag samples where the model was incorrect (line 98). A natural concern is whether pruning nodes that correlate with incorrect responses removes nodes that are important for correct answers in general, or whether the method requires careful tuning of the out-of-bag set composition. The paper's available text does not address how robust the selected nodes are across different out-of-bag subsets or random seeds.

### Trivial

- The paper uses bullet-style contributions in the introduction (lines 49–54) but does not provide a formal summary of limitations or failure cases anywhere in the visible text. A brief limitations paragraph in the conclusion would strengthen the presentation.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals for accuracy and bias metrics would help establish the statistical reliability of the reported improvements.
- Validating CKLD on synthetic data with known ground-truth bias before using it as the primary evaluation metric would strengthen the case that it measures what it claims to measure.
- An ablation study varying the number of pruned nodes and the size/composition of the out-of-bag set would help understand the method's sensitivity to these design choices.
- Disentangling the contributions of BNP and AOI more explicitly would clarify whether the gains come primarily from the input modification or the parameter-level intervention.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Core methods and evaluation are not present" (Harsh Critic Point 1):** The paper's methods, experiments, and evaluation sections are included via `\input` commands (lines 64, 65, 76, 77, 86, 108–112, 122–124). These are standard LaTeX includes for a multi-file project. Their non-resolution in the plain-text extraction is a parser artifact; the content exists in the original submission. Removed per rules about parser artifacts.

- **"CKLD is introduced without any formal definition" (Harsh Critic Point 3):** The definition of CKLD resides in `\input{4_Experiments/evaluation}` (line 86), which the parser did not resolve. The original submission contains this definition. Removed per rules about parser artifacts.

- **"BNP is underspecified" (Harsh Critic Point 2, parts about missing formal details):** The details of how bias vectors are computed and how nodes are selected for pruning are in `\input{3_Methods/bias_pruning}` (line 76), which the parser did not resolve. Removed per rules about parser artifacts.

- **"Large improvements would require strong evidence" (Harsh Critic Point 5, in its full form):** The experimental evidence supporting the claimed improvements resides in the parser-excluded experiments and tables sections. The magnitude concern is reasonable but is better framed as a minor question about interpretability rather than a claim of missing evidence.

- **Generic strength claim about "robust empirical validation" (Strength Finder #6):** While three datasets and three models are listed, the actual results are in parser-excluded sections. The Strength Finder's phrasing overstates what can be verified from the available text. Moved here for caution.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily raise concerns about content missing due to parser extraction issues and identify standard methodological questions (ablations, limitations, statistical reliability) that apply to most empirical papers.

## Suggestions

1. Add a brief limitations paragraph to the conclusion discussing: (a) potential degradation on unrelated tasks, (b) sensitivity to the out-of-bag set composition, (c) conditions under which BNP may not help.
2. Explicitly state why pruning only 32/4096 nodes produces large accuracy gains — is the bias concentrated in those nodes, or is there another mechanism at play?
3. Present the core experimental results (main table, baseline comparisons, black-box results) in the main text alongside qualitative interpretation, not in a separate section that could be missed.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>