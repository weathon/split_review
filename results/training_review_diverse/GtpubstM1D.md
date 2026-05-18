I have now thoroughly verified all claims against the paper. Here is my consolidated review.

---

## Summary

This paper investigates how to improve mathematical reasoning in LLMs by substituting general math corpora with problem-solving data during continued pre-training (CPT). Through controlled experiments answering three research questions on Llama-2, the authors find that (1) problem-solving data during CPT significantly outperforms general math corpora, (2) among synthesis methods, Tutorship Amplification is most effective, and (3) CPT learns mathematical reasoning from problem-solving data more effectively than SFT, particularly for hard multi-step problems. These insights are combined to train JiuZhang-8B on Llama-3, which matches or exceeds models like Qwen2.5-Math-7B and Qwen2-Math-72B using ~1/10 the math tokens, while maintaining general knowledge.

## Strengths

1. **Clean evidence that problem-solving data during CPT outperforms general math corpora (Section 3, Figure 1).** The experiment holds total math token count constant and varies only the composition (math corpus vs. problem-solving data). All three test groups (Test1–Test3) consistently outperform Base1, and Test3 (highest problem-solving ratio) dominates. This directly supports Result 1 and is the paper's most methodologically clean finding.

2. **Controlled comparison of data synthesis methods identifies Tutorship Amplification as best (Section 4, Table 1).** The four synthesis methods are compared against each other with similar token budgets (~30B each), making the inter-method ranking reliable. Tutor-Amp achieves the highest average accuracy (25.9) vs. the next best (Query-Exp at 24.5) and the control Base2 (23.3). The implementation details (teacher-model error correction) are clearly described.

3. **Fine-grained analysis of why CPT outperforms SFT (Section 5, Tables 2–3).** The decomposition by data distribution (IND vs. OOD) and difficulty level (easy/medium/hard) provides concrete insights: the advantage of CPT over SFT is largest on hard multi-step problems, suggesting that CPT's superior learning of complex reasoning chains is the driver. This is a genuinely useful finding for practitioners.

4. **JiuZhang-8B achieves strong results with exceptional token efficiency (Section 6, Table 4).** The final model matches Qwen2.5-Math-7B (37.6 vs. 37.8 average on GSM8K/MATH/Gaokao/Zhongkao) using ~100B math tokens vs. 1T, and surpasses DeepSeek-Math-7B-base and Qwen2-Math-7B. It also preserves general knowledge (MMLU 0.6222 vs. Llama-3-8B's 0.6211). The model is released to the community.

5. **Rigorous experimental hygiene.** The paper uses MinHash deduplication, decontamination against evaluation sets, and includes GAOKAO/ZHONGKAO (released after Llama-2) to minimize contamination risk. These design choices strengthen confidence in the results.

## Weaknesses

### Fatal
None. The paper's contributions are real and not invalidated by the issues below.

### Major

1. **The CPT vs. SFT comparison (Section 5) is confounded by pre-training data composition.** The paper compares Base1-SFT (CPT on general math corpus → SFT on 7.2B problem-solving data) with Base2 (CPT where 7.2B of general math corpus is *replaced* by 7.2B problem-solving data). While total math token count is held constant, the pre-training data distribution differs: Base2 sees problem-solving data (questions + reasoning steps) during CPT, while Base1-SFT's base model sees only general math text. The observed advantage of CPT could therefore stem from *earlier exposure* to problem-solving format during pre-training rather than from the training stage (CPT vs. SFT) per se. This confound propagates to Results 4 and 5 (distributions and difficulty levels), which inherit the same comparison. A cleaner design would keep pre-training data fixed and vary only the stage at which problem-solving data is introduced — e.g., comparing a model that continues pre-training with problem-solving data *on top of* the math corpus vs. one that is SFT on the same data from the same base.

2. **The synthesis method comparison (Section 4) lacks a data-quantity control when evaluating effectiveness against Base2.** The control (Base2) receives zero additional synthetic tokens, while each experimental group adds ~30B tokens. The claim that synthesis methods are "effective" (Result 2) is therefore confounded with data volume — the improvement could simply come from training on more tokens. However, this does *not* affect the inter-method ranking (Tutor-Amp > Query-Exp > Res-Div > Retro-Enh), which is controlled since all synthesis methods add similar token budgets. The paper's strongest claim about synthesis — that Tutorship Amplification is the *most efficient* — is better supported than the claim that synthetic data per se is effective.

### Minor

1. **Non-standard evaluation metric (max of zero-shot and few-shot).** The paper takes the maximum of zero-shot and few-shot accuracy per dataset and averages across datasets. While the authors provide a rationale (different models prefer different settings), this inflates absolute scores relative to a fixed protocol and makes comparisons with external work that uses a single setting less straightforward. Reporting both zero-shot and few-shot scores separately would increase transparency, though the *relative* comparisons within the paper are likely unaffected.

2. **Absence of confidence intervals or variance estimates.** All experiments appear to be single runs with a single checkpoint per condition. With only four evaluation sets and no error bars, some observed differences (e.g., Res-Div 23.0 vs. Base2 23.3) could be within noise. This is common practice for large-scale LLM training where multi-run experiments are expensive, but it should be noted.

3. **Difficulty classification by number of reasoning steps is acknowledged as coarse.** The paper notes this limitation (Section 5.3), which is acceptable for a first analysis. Still, this adds approximation error to Results 5.

### Trivial
None.

## Nice-to-Haves

- **Scaling curves for synthesis methods.** A plot of accuracy vs. tokens for each synthesis method at multiple data volumes would substantially strengthen the claim that Tutorship Amplification is the *most efficient* (not just the best at high volume).
- **Validation of RQ transferability to Llama-3.** The three RQs are investigated on Llama-2, but the final model uses Llama-3. A small-scale replication of one RQ (e.g., the Section 3 comparison) on Llama-3 would increase confidence that the findings transfer.
- **Alternative experimental design for Section 5.** An experiment that adds problem-solving data during CPT *without reducing* the math corpus (vs. SFT on the same data from the same base), then normalizes for total tokens, would provide a cleaner test of the stage effect.

## Removed Points

The following points from the reviewer inputs were removed per policy:

- **Concern about code/model release status** ("No code or model weights are mentioned" / clarify reproducibility): Removed per hard rule — the paper explicitly states the model is being released, and cited references are assumed to exist.
- **"Fatal" severity framing of Section 4 confound**: Downgraded to Major. The inter-method ranking is controlled; only the vs.-Base2 comparison is confounded. The critic's framing overstates the damage.
- **Demand for adding more original data as a control in Section 4**: Removed as infeasible — the paper states limited availability of original problem-solving data, which is precisely the motivation for studying synthesis methods.
- **Criticism that the paper should also cover token efficiency / data scaling analysis**: Moved to Nice-to-Haves. This would strengthen the paper but its absence does not undermine the existing contributions.

## Novel Insights

Beyond the paper's own contributions, the most interesting synthetic observation from the reviews is the contrast between the paper's two confounds. The Section 3 experiment (problem-solving data vs. math corpus) is clean because the paper keeps token counts identical and varies only content — showing that data *quality* matters. The Section 5 experiment attempts the same logic (total math tokens equal) but inadvertently also varies *when* the model is exposed to problem-solving format. This suggests an inherent tension in designing controlled experiments for multi-stage training: holding token count constant requires borrowing from other data sources, which changes pre-training distribution. The paper's choice is understandable but limits causal identification, and future work should consider designs where the same base model branches into CPT and SFT branches with identical pre-training.

## Suggestions

1. **For the CPT vs. SFT comparison (Section 5):** Re-run the comparison using a single pre-trained model (e.g., Base1) split into two branches: one continues pre-training with additional problem-solving data (on top of the math corpus, increasing total math tokens), while the other is SFT on the same problem-solving data. If total token count is a concern, normalize by comparing improvement per token. At minimum, acknowledge the confound explicitly and discuss why it is unlikely to fully explain the large observed gap (~1.67×).

2. **For the synthesis comparison (Section 4):** Add a control that matches the total token budget of the synthesis conditions by repeating or upsampling existing data. If the repeated-data control performs similarly to the synthesis methods, the "effectiveness" claim is weakened; if it performs worse, the claim is strengthened.

3. **Report zero-shot and few-shot scores separately** alongside the max, to enable direct comparison with papers using a single evaluation protocol.

4. **Consider adding confidence intervals** for at least the final model comparisons in Table 4, using multiple evaluation runs or bootstrap sampling.

## Score and Decision

The paper makes meaningful empirical contributions — it provides clear evidence that problem-solving data during CPT is more effective than general math corpora (Result 1, the cleanest experiment), identifies Tutorship Amplification as the best synthesis method among those compared, and produces JiuZhang-8B, a genuinely strong and token-efficient model released to the community. The fine-grained analysis of why CPT outperforms SFT (difficulty-level decomposition) is valuable guidance for practitioners. However, two of three main experimental results (Results 3–5 and the vs.-Base2 part of Result 2) have confounds that weaken the causal claims. These issues are recoverable with additional controls but reduce confidence in the strongest formulations of the conclusions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>