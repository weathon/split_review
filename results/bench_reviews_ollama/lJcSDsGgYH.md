Now I have thoroughly reviewed the paper. Let me synthesize the final review.

## Summary

The paper proposes an extensible, interpretable framework for estimating LLM response confidence under black-box (query-only) access. Six prompt perturbation strategies (Stochastic Decoding, Paraphrasing, Sentence Permutation, Entity Frequency Amplification, Stopword Removal, Split Response Consistency) generate variability-based features, which are fed into a logistic regression classifier trained on binary correctness labels (ROUGE ≥ 0.3). The method is evaluated on 4 QA and 2 summarization datasets across 5 LLMs. It reports AUROC and AUARC improvements over prior unsupervised baselines, interpretable feature importance, and the finding that confidence models transfer across LLMs within the same dataset.

## Strengths

- **Creative and intuitive perturbation-based feature engineering:** The core idea—that an LLM's response sensitivity to semantic-preserving input perturbations signals uncertainty—is well-motivated and practically useful. The six strategies (PP, SP, EFA, SR, SD, SRC) test the model in complementary ways (context reordering, entity amplification, paraphrasing, stopword removal, decoding stochasticity, response consistency).

- **Broad empirical evaluation:** The framework is tested on 6 datasets (4 QA, 2 summarization) and 5 LLM architectures (Llama-2-13b, Mistral-7b, Flan-ul2, Pegasus-large, BART-large), spanning context-based QA, open-domain QA, and abstractive summarization. This provides breadth beyond typical single-task single-model evaluations. AUROC improvements of 10–15 percentage points are observed on several QA-LLM combinations (e.g., CoQA/Llama: 0.92 vs. 0.77 for the best baseline; SQuAD/Mistral: 0.84 vs. 0.70).

- **Cross-LLM transfer finding is genuinely interesting:** The observation that important features are shared across LLMs for the same dataset (e.g., SP lexical similarity dominates for all three LLMs on SQuAD), and that confidence models trained on one LLM can partially transfer to others on the same dataset, is a novel and useful finding. It suggests that question difficulty and dataset structure dominate over model-specific behavior in driving uncertainty patterns.

- **Interpretable framework:** Logistic regression enables direct feature attribution, revealing that context-manipulation features (SP, EFA) are most predictive for context-rich datasets while question-manipulation features (PP, SR) dominate for context-less datasets—a finding that aligns with intuition and provides actionable insight.

## Weaknesses

### Fatal

None.

### Major

- **Missing ablation against a combined baseline model obscures attribution of improvements:** The paper compares its supervised logistic regression (11+ features) against individual unsupervised metrics (semantic sets, lexical similarity, eigenvalue, eccentricity, degree). Since the proposed method already includes SD features overlapping with the baselines, the improvement conflates two factors: (a) the benefit of supervised learning with any reasonable features, and (b) the benefit of the novel perturbation features. Without an ablation that trains logistic regression on only the baseline features {semantic sets, lexical similarity, eigenvalue, eccentricity, degree}, it is impossible to determine how much of the improvement comes from the learning framework versus the novel perturbations. The paper's central claim—that the perturbation-based features drive the gains—remains unsubstantiated without this control.

- **"Universal confidence model" and "zero-shot transfer" claims are overstated, with significant performance drops underreported:** The paper claims the findings "open up the possibility of simply building a single (universal) confidence model" (Section 1 and Section 4.2). However, the transfer experiments are only within the same dataset across LLMs—a weak form of generalization. More critically, several cross-LLM transfers show substantial degradation: AUARC drops from 0.83→0.64 (TriviaQA, Llama→Mistral), 0.74→0.34 (CNN, Pegasus→BART), and 0.80→0.61 (CoQA, Flan-ul2→Mistral). The paper describes transfer as "quite transferable" while these drops are not discussed. Additionally, cross-dataset transfer—the prerequisite for any "universal" model—is explicitly acknowledged as not tested ("Transfer across datasets can be more challenging," Section 3.2) but the framing of a "universal confidence model" nonetheless persists.

### Minor

- **Cases where the method underperforms baselines are not acknowledged:** On CNN/BART AUROC (0.57 vs. 0.60 for Lexical Similarity) and XSUM/BART AUROC (0.57 vs. 0.59), the proposed method loses to the simplest baseline. The paper's narrative focuses exclusively on the favorable cases ("surpassing baselines by even over 10%"), creating an incomplete picture.

- **Feature importance analysis via logistic regression coefficients has reliability concerns:** The coefficient threshold of 1e−4 is extremely low and not a meaningful statistical criterion for feature importance. With 11 features and 1000 training points, almost all fitted coefficients would exceed this threshold. More importantly, multicollinearity among perturbation-derived features (e.g., SD lexical similarity and PP lexical similarity may be correlated) can make coefficient rankings unreliable. Without a correlation analysis or proper feature ablation, the interpretability claims remain suggestive rather than conclusive.

- **Supervised nature underemphasized in the problem framing:** The title and abstract frame the contribution as "black-box confidence estimation," which is technically accurate (no LLM internals are needed), but underplays the requirement for ground-truth labels and per-dataset training. The limitations section acknowledges this ("owing to the supervised nature"), but the overall presentation could lead readers to conflate black-box *access to the LLM* with a fully unsupervised confidence estimation method.

### Trivial

- Different shot counts across LLMs (zero-shot for some, two-shot or five-shot for others) is an uncontrolled confound, though unlikely to undermine the main conclusions given the consistency of improvements across settings.

## Nice-to-Haves

- An ablation study training logistic regression on only the baseline features would directly quantify how much improvement comes from the novel perturbations versus the supervised framework, and would strengthen the core claim substantially.
- A feature correlation analysis (pairwise correlations among the 11 features) would validate or qualify the interpretability claims.
- A comparison with a white-box baseline (e.g., using token probabilities) would contextualize how much is sacrificed by operating in a black-box-only setting.
- Cross-dataset transfer experiments (e.g., training on SQuAD and testing on NQ) would move the "universal confidence model" claim from speculation toward evidence.

## Removed Points

- **"1000 datapoints for hyperparameter tuning" is misleading:** The critic argues this is effectively the training set, not a hyperparameter set. While technically true (logistic regression has minimal hyperparameters), log loss regularization strength is a genuine hyperparameter, and 1000 points divided between training and validation is a reasonable setup. This is a minor presentation issue, not a substantive concern. Moved here as trivial/already acknowledged.

- **Equation 1 threshold relationship unclear:** The relationship between the continuous threshold θ in Eq. 1 and the 0.3 binary threshold is clear upon reading the paper—θ = 0.3 is the chosen threshold for creating binary labels matching prior work. This is not a real weakness.

- **Paraphrasing through French alters semantics:** The critic argues back-translation may distort meaning. While valid in concept, the paper explicitly addresses this by claiming the perturbations maintain semantics "in almost all cases" (referencing Table 2). Moreover, the point of the perturbation IS to test model sensitivity—even if semantics shift slightly, that shift is part of what the feature captures. Also, the appendix may contain the quantitative analysis—we just can't see it due to parser stripping.

- **What "correct" means for summarization tasks:** Using ROUGE ≥ 0.3 as a correctness threshold for summarization is debatable but follows prior work (Lin et al.). This is a known limitation of any automated metric, not a novel flaw.

- **SRC inapplicable to short responses:** The paper acknowledges this limitation directly in Section 3: "some of the strategies require a context in the prompt, while others such as SRC require longer responses."

- **Shot counts vary across LLMs as confound:** Noted in trivial weaknesses above, but removed as a separate major concern since the paper is transparent about the prompting setup and the results are consistent across settings.

- **No variance/confidence intervals:** Requesting confidence intervals for 3-run averages is beyond standard practice in this venue. Moved to removed as scope creep.

- **Comparing to white-box baselines:** The paper explicitly scopes itself to black-box methods. Requesting white-box comparisons is useful context but outside the stated scope. Moved to nice-to-have.

## Novel Insights

The cross-LLM transfer finding within a dataset reveals an important structural insight: question difficulty and dataset-specific response patterns are stronger determinants of uncertainty than model-specific behavior. This suggests that uncertainty patterns are more a property of the data distribution than of the model, which has implications for building practical confidence estimators—you may only need to train on one model per task. However, the AUARC degradation in several transfer cases (particularly for summarization and out-of-family LLMs) tempers this insight considerably.

## Suggestions

- Run one additional ablation: train logistic regression on only the 5 baseline features (semantic sets, lexical similarity, eigenvalue, eccentricity, degree) and report results. This single experiment would either confirm that the novel perturbation features add value beyond supervised learning alone, or reveal that the gains are primarily from the learning framework—either way, it substantially strengthens or honestly refines the contribution.
- Report cases where the method underperforms baselines (CNN/BART, XSUM/BART) explicitly rather than selectively highlighting best improvements.
- Tone down "universal confidence model" language until cross-dataset transfer is demonstrated, or clearly state it as a hypothesis for future work.

## Evaluation

**Originality:** The perturbation-based feature engineering approach is creative and reasonably novel for black-box LLM confidence estimation. The idea of using response variability under controlled perturbations as uncertainty signals is a genuine contribution. However, the supervised logistic regression wrapper is straightforward, and the claimed novelty of the features vs. the learning framework is not cleanly isolated.

**Importance of research question:** Confidence estimation for LLMs is a practically important and actively researched problem, particularly in the black-box setting. The paper addresses a real need.

**Claims support:** The main empirical claim of superiority over baselines is undermined by the absence of a combined baseline ablation. The "universal confidence model" claim is overstated relative to the evidence. The feature importance claims are suggestive but not rigorously validated.

**Soundness of experiments:** Evaluation covers good breadth (6 datasets, 5 models), but the experimental design has the key gap of missing the combined-feature ablation baseline. Transfer experiments show meaningful degradation in several cases that is underemphasized.

**Clarity:** The paper is generally well-written and the framework is clearly described. The main presentation issue is selective reporting of positive results and overclaimed extrapolation.

**Value to community:** The perturbation strategies are a useful contribution that could be integrated into future confidence estimation frameworks, even if the specific gains over supervised baselines remain unquantified.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>