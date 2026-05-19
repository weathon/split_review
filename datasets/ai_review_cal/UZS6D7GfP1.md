- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

The paper introduces Gramtector, a method for detecting LLM-generated text by learning interpretable grammatical patterns (PoS n-grams) via L1-regularized logistic regression. These patterns serve a dual purpose: they form an interpretable classifier, and they can be presented to human labelers as highlighted cues in a human-in-the-loop framework. Experiments show the classifier achieves AUROC scores close to 1 across several domains (arXiv, Reddit, CNN, Wikipedia) and generalizes to multiple LLMs (ChatGPT, GPT-4, LLAMA-2-70B), while a human trial reports that engaged participants using the patterns improve from 40% to 86% accuracy.

## Strengths

- **Interpretable feature design grounded in cognitive constraints.** The paper explicitly uses Miller's law to limit the pattern set to 20 features via L1 regularization, and the resulting grammatical patterns (PoS n-grams) are directly presented to humans as colored highlights (Section 4, Figure 3). This makes the detection process transparent rather than a black-box probability.

- **Robustness to adversarial evasion.** Table 2 shows that Gramtector's detection performance is unchanged under adversarial prompting and only marginally affected by paraphrasing, whereas vocabulary and stylometric baselines drop from 98% TPR to 4% under paraphrasing. This suggests that grammatical patterns capture an intrinsic LLM characteristic that is hard to alter.

- **Generalization across text domains and LLMs.** Figure 2 and Section 5.1 demonstrate that Gramtector achieves AUROC scores close to 1 on arXiv, Reddit, CNN, and Wikipedia datasets, and generalizes to ChatGPT, GPT-4, and LLAMA-2-70B, with performance on par with or exceeding DNN-based benchmarks on some datasets.

- **Engagement-aware analysis in the human trial.** The trial separates unengaged, engaged, and pattern-using responses (Figure 4a), addressing the known problem of LLM-generated survey replies (Veselovsky et al., 2023). The tiered experimental design (Levels 1–3) and the finding that stronger AI guidance (Level 3) leads to worse human performance provide a nuanced insight into human-AI collaboration design.

## Weaknesses

### Fatal

None.

### Major

- **Human trial is critically underdocumented, undermining the paper's central claim.** The headline result — that humans improve from 40% to 86% accuracy using Gramtector's patterns — rests entirely on the human trial (Section 5.2). Yet the paper reports no sample size (number of participants), no demographic information, no recruitment method, and no details on how "unengaged" responses were operationally classified. The Clopper-Pearson confidence intervals in Tables 3–4 and Figure 4 require the number of observations *n* to be interpretable, but *n* is never stated. Without these basic experimental parameters, the reader cannot assess the reliability, generalizability, or statistical validity of the headline accuracy improvement. This is the paper's most differentiating contribution, and the current documentation is insufficient to support it.

### Minor

- **DNN comparison lacks sufficient detail to assess fairness.** Gramtector (a linear model on PoS n-gram counts) is reported to outperform fine-tuned RoBERTa and DistilBERT on the Wikipedia and arXiv datasets (Section 5.1, Figure 2). The paper provides no information about how the DNN benchmarks were trained: no training/validation/test split sizes, no learning rate, no number of epochs, no early stopping criteria, and no specification of whether the same data splits were used for all methods (Section 5.1). While this does not invalidate the paper's main contribution (the interpretable patterns and human-in-the-loop), it makes the comparative claim difficult to evaluate.

- **Adversarial attack specifications are missing.** The robustness experiment (Table 2, Section 5.1) reports that Gramtector is robust to "paraphrasing" and "adversarial prompting," but neither the paraphrase model/method nor the specific adversarial prompts are described. Without knowing the strength and nature of the attacks, the robustness result is hard to interpret. The baselines (vocabulary and stylometric features) are also underspecified beyond their feature types.

- **Abstract accuracy number is inconsistent with the main text.** The abstract states "43% to 86%" (line 4), but the introduction and conclusion state "40% to 86%" (lines 19, 157). These figures should be reconciled.

### Trivial

- **The formalization of the highlighting function *h_φ* (Equation 3) maps text to pairs of (passage, explanation), but the actual implementation only returns colored pattern matches without textual explanations.** This mismatch between the formalism and implementation is minor but could confuse readers (Section 4).

## Nice-to-Haves

- A discussion of limitations would strengthen the paper: e.g., the method requires a domain-specific human-written corpus, the PoS tagger may propagate errors, and the 20 selected patterns may not transfer across domains.
- Dataset statistics (number of samples per domain, train/val/test split sizes) would help the reader calibrate the experimental results.

## Removed Points

These points from the inputs are flagged to be removed; treat them with caution:

- **"100,004 features suspiciously round"** — The derivation from n=1..7 PoS n-grams with 9 tags is explained in the paper; questioning its exact roundness is a nitpick without substance. Rejected as a weakness.
- **"Low variance in Figure 2 suggests too-easy data"** — Speculative claim about low variance reinforcing a "suspicion of too-easy data" without any evidence. Rejected as speculation.
- **"Unusual that a linear model beats DNNs"** — While the lack of DNN training details is a valid concern (kept above as Minor), the assertion that this result is "implausible" overstates the case; PoS n-gram features are known to be informative for authorship tasks and the data separation could indeed be clean. The core concern about documentation is retained; the speculation about implausibility is removed.
- **"Straw-man baselines (vocabulary/stylometric)"** — Vocabulary and stylometric features are standard baselines for this task; calling them straw men without evidence is unwarranted.
- **"TPR omitted from adversarial rows"** — The text explicitly states Table 2 reports "accuracy, AUROC score, and true positive ratio (TPR)" for all conditions. Since the table is embedded as an image, this claim cannot be verified either way, but the text suggests TPR is included. Rejected as potentially factually incorrect.
- **"Whether the example abstract was one of the 10 used in the trial"** — A minor curiosity with no bearing on the paper's validity.
- **"Missing code/data availability statement"** — Per the rules, this is a formatting/reproducibility nitpick of the type that should be removed.
- **Strength: "Human-in-the-loop accuracy improvement from 40% to 86%"** — This is a genuine strength of the paper's core finding, but it is retained in the Strengths section above, not removed. No removal needed.

## Novel Insights

The most genuinely novel observation arising from the reviews — beyond the paper's own contributions — is that the engagement-aware tiered analysis (Levels 1–3) produced the counterintuitive result that *more* AI guidance (Level 3, where patterns are directly colored by predicted class) leads to *worse* human performance than moderate guidance (Level 1, where participants must match patterns themselves). This finding, that excessive automation of AI explanations can create black-box overreliance and degrade human judgment, is a design insight that extends beyond this specific detection task into the broader human-AI collaboration literature. The paper itself notes this but does not fully develop the implications.

## Suggestions

1. **Report the human trial completely.** Provide the number of participants per condition, demographic summary, recruitment method, and the operational definition of "unengaged" (e.g., time threshold, attention checks, or LLM detection algorithm). Include the full list of 10 abstracts used in the study.
2. **Document the DNN benchmark training protocol.** Report train/val/test splits, hyperparameters (learning rate, batch size, epochs, early stopping criterion), and confirm that the same data splits were used for all methods.
3. **Specify the adversarial attacks.** Name the paraphraser model(s) and describe the adversarial prompts. Report full metrics (including TPR) for Gramtector on all adversarial conditions.
4. **Reconcile the 43% vs. 40% discrepancy** in the abstract vs. main text.
