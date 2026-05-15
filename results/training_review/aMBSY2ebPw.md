Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper ablate the components of grammar books for extremely low-resource (XLR) machine translation, asking whether LLMs really learn translation from grammatical explanations or from the parallel examples embedded in grammar books. Focusing on Kalamang (unseen XLR) and Nepali (seen low-resource), the authors show that (1) parallel examples drive translation performance while grammatical explanations provide no significant benefit; (2) fine-tuning a small NLLB model matches the performance of prompting a long-context LLM with the same parallel data; and (3) a novel typological feature prompt helps on linguistically-relevant tasks (grammaticality judgment, IGT prediction) but not translation. The paper recommends prioritizing parallel data collection over linguistic descriptions for XLR MT.

## Strengths

1. **Clean ablation of grammar books into parallel examples vs. explanations.** The paper systematically separates Book_all into Book_p (parallel sentences) and Book_¬p (grammatical explanations). This directly addresses a key confound in MTOB and cleanly shows that Book_p drives nearly all translation performance, with Book_¬p lagging 7–8 ChrF++ behind. This is the paper's central contribution and is well-executed.

2. **Demonstrates that fine-tuning small MT models matches long-context LLMs on the same data.** NLLB-1.3B fine-tuned on P_book (34.2 ChrF++ into kgv) comes within 0.2 ChrF++ of Gemini prompted with Book_all (34.4), and NLLB + P_train (38.7) beats Gemini with the same data (33.4) by over 5 points into kgv (Table 3). This is a practical finding: the problem reduces to standard XLR MT, not requiring expensive long-context models.

3. **Introduces typological feature prompting and shows grammar helps where it should.** The Typ + Book_p prompt achieves the highest morpheme accuracy on IGT prediction (46.1, outperforming all supervised baselines) and best overall accuracy on grammaticality judgment. Yet it provides inconsistent translation gains. This cleanly demonstrates that LLMs *can* exploit grammar — when given the right form of knowledge and a task that rewards it — but not for translation.

4. **Generalizes findings beyond Kalamang to Nepali.** Table 2 replicates the pattern: Book_p matches or outperforms Book_all for both models and directions, while Book_¬p and Typ are detrimental or neutral. This strengthens the claim beyond a single unseen language.

## Weaknesses

### Fatal
None.

### Major

1. **The regression analysis does not establish the causal claim that "grammar adds no significant advantage above type coverage."** The paper fits univariate regressions of ChrF++ against test-set type coverage across ~9 data points. This shows a correlation, not that coverage is the causal mechanism and explanations are inert. Coverage naturally correlates with having more parallel data (and with prompt structure, gloss formatting, etc.), so the regression cannot disentangle whether explanations add marginal value. A controlled experiment holding coverage fixed while varying explanations — or vice versa — would be needed for the causal claim. The paper's broader conclusion that parallel data is the main driver is robust to this issue (supported by direct comparisons), but the specific regression-based argument overreaches.

2. **The 100-example test set for Kalamang is small for fine-grained comparisons.** The paper combines MTOB's two 50-example sets into 100. While this is the available benchmark for Kalamang and the paper acknowledges MTOB's own limitation, comparisons of 0.7–3.6 ChrF++ differences rest on a small sample. The Nepali replication (1012 examples) somewhat mitigates this concern, but the paper's strongest claims are about Kalamang. The small n also limits the regression's reliability.

3. **Numerical error in the reported difference between Book_all and Book_p.** The bullet point in the introduction states explanations add "+0.7 ChrF++ into kgv" (line 24). However, Table 1 shows Book_all = 34.4 and Book_p = 30.8 into kgv (Gemini), a difference of **3.6** ChrF++, not 0.7. The paper's own text in Section 5 correctly reports "Book_all performs 3 points better than Book_p" (line 192). The +0.7 claim in the introduction is inconsistent with the data and misrepresents the size of the gap. This is a concrete error that should be corrected.

### Minor

1. **The grammaticality judgment task's corruptions may not be reliably ungrammatical.** The paper acknowledges "we cannot guarantee all corruptions are ungrammatical (since no author speaks Kalamang)" and there is no human baseline for these specific corruptions. While the heuristic corruptions (swap-adjacent, swap-random, shuffle) are reasonable, the accuracy numbers on this task cannot straightforwardly measure whether the LLM "learned grammar" from the book. The paper uses this task to support the claim that LLMs can exploit grammar for relevant tasks, but the evidential basis is weaker than presented.

2. **Only one LLM (Gemini) can handle the full Book_all setting for Kalamang.** Llama-3.1-8B's 128k context is insufficient for kgv Book_all, so the most informative comparison — Book_all vs. Book_p — is only available for Gemini on Kalamang. The paper tests Llama on Nepali and on the subsets, but the primary claim about grammar books for XLR translation rests heavily on a single model family. This is acknowledged but remains a limitation for generalizing to "LLMs" broadly.

3. **The claim about fine-tuning "matching" long-context LLMs is narrowly scoped.** The "within 0.2 ChrF++" claim (line 25) refers specifically to NLLB P_book (34.2) vs. Gemini Book_all (34.4). This is factually accurate for this comparison (Table 3), but the phrasing "with a grammar book" could misleadingly suggest the strongest Gemini setting (e.g., Book_all+W+P_train at 43.7). The paper should disambiguate this more clearly, since NLLB is 5+ points below Gemini's best setting.

### Trivial

- The p-value text on line 287 shows a parsing artifact ("$p<0.};"). This is a PDF extraction issue, not the authors' fault, but the original should be verified.
- The typological prompt is described at a high level ("rule-based template...features for each language and a short explanation") without details on how many features are used or an example template. A brief example in the paper or appendix would aid reproducibility.
- The regression analysis does not report R² values, making it hard to assess how much variance is explained by coverage alone versus left unexplained.

## Nice-to-Haves

- **Controlled experiment varying the ratio of parallel examples to explanations at fixed total tokens**: This would directly measure the marginal value of explanations, cleaner than the regression approach.
- **Error analysis with qualitative examples**: Showing cases where Book_all succeeds but Book_p fails (and vice versa) would illustrate whether explanations ever provide genuine help.
- **Replication with additional long-context LLMs** (e.g., GPT-4, Claude) would strengthen the claim that the pattern is model-agnostic, though the cost and access constraints are acknowledged.
- **Analysis of whether typological features actually appear in model outputs** (e.g., correct word order) when they help on linguistic tasks.

## Removed Points

- **"The typological feature prompt is not described in enough detail"** — The paper provides a reasonable description (Grambank features + rule-based template) for a conference paper, and code release is planned. This is a nuance, not a weakness.
- **"p-values partially cut off"** — This is a PDF parsing artifact ("$p<0.};" on line 287), not a content error in the original submission.
- **"No cross-validation or R² reported for regression"** — While mildly informative, this is a minor presentation preference rather than a substantive gap. The data points are too few for meaningful cross-validation.
- **Strength Finder's "type coverage regression provides statistical evidence that grammar adds nothing"** — This strength overstates the regression's power. The verified weakness (#1 above) shows the regression is correlational, not causal. The strength about coverage having *some* relationship with performance is retained, but the causal interpretation is dropped.
- **"Missing related works"** — Not verifiable without external sources.

## Novel Insights

The paper's most interesting finding is the asymmetric result across tasks: parallel data drives translation, but typological features help on linguistic tasks (IGT prediction and grammaticality judgment). This suggests that the *form* of grammatical knowledge matters as much as its content — structured, high-level typological features work better than free-form grammar book prose for LLMs, even though both contain similar information. The paper also shows that 5*-shot retrieval (per-word example selection) is surprisingly competitive for translation, hinting that relevance-weighted example selection may be more important than comprehensive context. Together, these results point toward a data-centric agenda for XLR NLP: prioritize the right form of data for each task rather than hoping a grammar book will serve all purposes.

## Suggestions

1. **Correct the numerical error**: Revise "+0.7 ChrF++ into kgv" (line 24) to the correct value (~3.6) or clarify the comparison being made.
2. **Add a controlled ablation** that varies type coverage independently of explanations, or add random filler text matched to explanation token counts as a control condition for the regression.
3. **Provide at least one example of the typological feature prompt** in the appendix, showing the features, counts, and phrasing.
4. **Disambiguate the "within 0.2 ChrF++" claim** to explicitly state which comparison is being made (Gemini Book_all vs. NLLB P_book), since the reader might assume the strongest Gemini setting.
5. **Tone down the causal language around the regression** — phrasing like "shown statistically" and "modelled by" rather than "caused by" would better reflect the correlational nature of the evidence.

## Score and Decision

The paper makes a genuine, well-motivated contribution by disentangling the signals in grammar books for XLR translation. The core finding — that parallel examples, not grammatical explanations, drive translation performance — is robustly supported by direct comparisons across two languages, two model types, and multiple data subsets. The typological prompting results on linguistic tasks are a novel and interesting extension. However, the paper overclaims on two fronts: the regression analysis is treated as a causal demonstration when it only shows correlation, and a concrete numerical error (+0.7 vs. 3.6) misrepresents the Book_all vs. Book_p gap in the introduction. Neither issue is fatal — the main finding holds without the regression, and the error is fixable — but they weaken the presentation. The 100-example test set is a recognized limitation of the benchmark rather than a methodological oversight, and the Nepali replication helps. With corrections and toned-down causal claims, this would be a strong paper.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>