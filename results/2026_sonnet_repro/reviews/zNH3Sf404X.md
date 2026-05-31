Now let me perform calibration searches to anchor the score.**Round 1 bracket: 3.5–5.5.** The paper has a genuine dataset contribution but its core ML claim (SSL outperforms supervised) doesn't hold. Now narrowing within this bracket.Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

This paper addresses illicit flow detection in Bitcoin CoinJoin (Shared Send Mixer) transactions through three stated contributions: (1) a large-scale dataset of 163 million CoinJoin transactions (4.6 million labeled), (2) novel features based on KeyLinker cryptographic address clustering and Shared Send Untangling (SSU) complexity metrics, and (3) a semi-supervised pseudo-labeling framework claimed to demonstrate that "data quality" drives SSL performance better than "data quantity." Three model families (XGBoost, CatBoost, Random Forest) are evaluated in supervised and SSL settings across combinations of feature sets.

---

## Strengths

- **First comprehensive CoinJoin dataset at scale**: The paper assembles 163.4 million CoinJoin transactions with SSU complexity labels and address labels from WalletExplorer, Elliptic++, MBAL, and Kaggle, covering Bitcoin's full history through block 882,421. The 4.6 million explicitly labeled CoinJoin transactions (Table 1) fill a demonstrated data gap in blockchain forensics research.

- **Concrete feature ablation showing OTC degrades performance**: Table 2 shows a consistent pattern across all three models: adding the OTC heuristic to the DefaultREUSE+CS feature set reduces F1 (e.g., XGBoost: 0.844 → 0.841), while combining Default+REUSE+CS+SSU without OTC yields the best results (XGBoost F1 = 0.845, ROC-AUC = 0.970). This directional result is consistent across model families and across both the supervised (Table 2) and SSL (Table 3) settings.

- **Sensible forensic framing of precision/recall tradeoff**: The paper correctly notes (Section 6.3) that pseudo-labeling improves recall (+0.01 to +0.03) at a cost in precision (-0.04 to -0.05), and links this tradeoff to the operational cost asymmetry between missing an illicit transaction and generating a manageable false positive—an appropriate domain-grounded choice.

- **Rigorous evaluation protocol under class imbalance**: Stratified 5-fold cross-validation, balanced class weights, and reporting of precision, recall, F1, and ROC-AUC across models under 12% illicit class prevalence is methodologically sound.

---

## Weaknesses

### Fatal
None that completely invalidate the dataset contribution.

### Major

- **The SSL framework does not outperform supervised learning, contradicting the paper's headline claim.** The paper's Contribution 3 and abstract claim SSL "effectively leverages unlabeled data" and that "models trained on strategically expanded high-quality data outperform those trained on larger, noisier datasets" (Section 7 conclusion). Yet comparing Tables 2 and 3: the best supervised XGBoost F1 = 0.845 (Table 2, Default+REUSE+CS+SSU) is *identical* to the best SSL XGBoost F1 = 0.845 (Table 3, same feature set). The paper itself acknowledges "the semi-supervised phase did not produce dramatic metric gains" (Section 6.3), yet the abstract, introduction, and conclusion continue to assert SSL as a positive contributor. This contradiction between body and framing is not a minor presentational issue—it concerns the empirical validity of Contribution 3.

- **Feature-quality and label-propagation noise are confounded, making the "quality drives SSL" thesis non-isolatable.** KeyLinker is both (a) a stronger input feature and (b) the source of more reliable pseudo-labels, because it is cryptographically grounded. OTC degrades both the feature signal and the label assignment simultaneously. The paper never separates these two channels—e.g., it does not train classifiers with KeyLinker features but OTC-derived pseudo-labels, or vice versa. Without this ablation, the "quality of features determines SSL success" claim is observationally indistinguishable from the simpler and well-known claim that "better label noise reduces SSL degradation." The paper repackages a known fact in domain-specific language and presents it as a new principle.

- **Metric differences are too small to support the conclusions without statistical testing.** The empirical advantage of Default+REUSE+CS+SSU over configurations that include OTC is 0.003–0.009 F1 across the tables. No confidence intervals, standard deviations, or significance tests appear anywhere. The paper states in the abstract it "proves that common heuristics like OTC... introduce noise"—but a proof requires statistical certainty that is completely absent. Given typical variance from random seed and CV fold composition, these differences could be within noise.

- **Transaction-level label assignment from address-level labels is not specified.** The paper describes 33,229 illicit and 251,083 legal *addresses* (Table 1), but the classification target is *transactions*. A CoinJoin transaction can involve dozens of input and output addresses with mixed or absent labels. Section 4 defines a tagging function but does not specify how transaction-level binary labels are derived when participating addresses are heterogeneous or partially unlabeled. This is not a minor detail—it determines what the classifier learns, whether train/test distributions are well-defined, and whether the reported F1 scores have a coherent interpretation.

### Minor

- **No external baseline from any prior method.** Section 3 cites methods achieving 92% accuracy (Nerurkar 2022), 97% recall (Rathore et al. 2022), and 91% accuracy (Nerurkar et al. 2021). None are reproduced on the paper's CoinJoin dataset. The paper cannot credibly claim to "advance blockchain forensic methodology" without establishing where its XGBoost F1 = 0.845 stands relative to prior supervised approaches on a comparable setting.

- **Tables contain rows that cannot be disambiguated.** As extracted from the paper, both Table 2 and Table 3 contain multiple rows for each model where the feature-set columns appear identical (all five features checked) but report different metric values. For example, XGBoost in Table 2 has three rows all appearing to show DEFAULT+REUSE+CS+OTC+SSU but with F1 = 0.821, 0.842, and 0.840 respectively. The paper provides no explanation for what distinguishes these rows (different hyperparameters? different pseudo-label fractions? different random seeds?). These rows are currently uninterpretable and unreproducible.

- **Pseudo-labeling procedure is under-specified.** Section 5.3 describes the scheme as selecting "the top fraction of samples on both sides of the decision boundary, adjusting the share of positives and negatives"—but specifies neither the target fraction, the target positive/negative shares, the number of iterations, nor whether pseudo-labels are regenerated each round. Reproducing the SSL experiments from the paper as written is not feasible.

- **Conclusion overstates the SSL result.** Section 7 asserts "our semi-supervised learning framework *further proved* that models trained on strategically expanded high-quality data outperform those trained on larger, noisier datasets." The body of the paper itself explicitly says the gains were not dramatic, and the numbers confirm flat performance. The conclusion should be revised to accurately reflect what was observed.

### Trivial

- The abstract uses the word "prove" for an empirical claim without statistical support—a precision issue that should be corrected.

---

## Nice-to-Haves

- An ablation that holds pseudo-label source fixed (KeyLinker) and varies whether OTC features are fed into the classifier—and vice versa—would cleanly separate feature-level from label-propagation noise, materially sharpening the paper's central argument.
- An iterative pseudo-labeling scheme (multiple rounds where pseudo-labels from round k seed the round k+1 model) might produce the actual F1 improvement the current single-round scheme fails to deliver.
- Cross-validation standard deviations across Tables 2 and 3 would immediately reveal whether the feature-quality differences are reliable signals or within noise.
- At minimum one adapted prior method as an external baseline would contextualize performance.

---

## Removed Points

*These points are flagged for removal—treat them with caution.*

1. **Strength Finder: "SSL contingent on feature quality, not pseudo-label volume" as a strong result.** This is removed because the underlying numbers (best SSL = best supervised = 0.845) do not constitute a positive demonstration of SSL effectiveness. The consistency of the ranking across feature sets is real, but it validates that OTC hurts—not that SSL helps.

2. **Strength Finder: "Practical forensic justification for recall–precision tradeoff" as a standalone strength.** Removed as a labeled strength because this observation (pseudo-labeling trades precision for recall) is generic and not specific to the paper's approach—it applies to any pseudo-labeling scheme.

3. **Harsh critic: "Test-set label quality undermines evaluation validity."** The critic correctly notes that test labels derive from the same off-chain sources (WalletExplorer, Elliptic++, Kaggle). However, the paper explicitly acknowledges this: "we acknowledge that off-chain labeling sources may introduce inaccuracies in illicit transaction classification" and chooses these sources for "transparent replication through publicly verifiable data." Using noisy but public labels is a domain-standard practice in blockchain forensics; this does not rise to a fatal methodological flaw in an applied dataset paper.

4. **Harsh critic: "CatBoost has more rows than feature combinations allow" / duplicate rows are parser artifacts.** Per instructions, formatting artifacts from PDF extraction are not author errors. The concern about unexplained row differentiation is retained as a Minor weakness above, as it may reflect a real underspecification in the original paper.

---

## Novel Insights

The paper's most durable observation—that OTC clustering, precisely because it is easy to apply at scale, systematically pollutes both features and pseudo-labels in a CoinJoin detection setting—is genuinely useful for practitioners. The domain-grounded argument that OTC breaks down for CoinJoin because the change-address heuristic conflates users who are explicitly trying to look like one-time changers is a substantive point worth retaining, even if the marginal F1 differences that support it lack statistical testing. The SSU complexity taxonomy (simple/separable/ambiguous/time-limited) as a *feature*, not just a dataset partition, is a creative repurposing of a prior algorithmic framework into a machine-learning input. Neither of these observations is fully new to the field, but their systematic combination in a forensic ML pipeline is a contribution the paper underutilizes.

---

## Suggestions

1. **Separate the feature-quality confound.** Run an ablation: (a) Default+KeyLinker features, pseudo-labels from OTC; (b) Default+OTC features, pseudo-labels from KeyLinker. This directly tests whether the harm from OTC is primarily at the feature level or the label-propagation level.
2. **Add cross-validation variance to all tables.** Even a ± standard deviation column would immediately address the statistical-significance concern.
3. **Specify transaction-level label derivation.** Explicitly state the rule (e.g., "a transaction is labeled illicit if any of its input addresses carries an illicit label") and report what fraction of the 4.6M labeled transactions are derived from each rule variant.
4. **Reframe the abstract and conclusion.** The honest takeaway—that SSL with high-quality features does not regress below supervised performance, while OTC features degrade both—is a weaker but defensible claim. "SSL does not hurt when guided by quality features" is publishable; "SSL proves quality over quantity" requires a stronger result.
5. **Clarify the duplicate/ambiguous table rows** by explaining what additional variable differentiates them (e.g., pseudo-label fraction threshold), or consolidate to one row per feature set.

---

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `q7Xi4yZYcH.md` (Ethereum anomaly detection, TRW-GCN) | 3.00 | R1 | Weaker: incremental ML application, no real dataset contribution |
| `aXSxSu3fvg.md` (SSL early stopping, healthcare) | 3.00 | R1 | Weaker: narrow application domain, limited contribution |
| `X8RTdxzqJQ.md` (Non-parametric two-sample testing as SSL) | 4.80 | R1 | Comparable theoretical depth, better methodology |
| `yM7rw8Bo1f.md` (FE-GNN, Ethereum address classification) | 4.25 | R1/R2 | Similar domain and approach; paper under review has larger dataset contribution but weaker ML claim validation |
| `LPXfOxe0zF.md` (BlockFound, blockchain foundation model) | 5.75 | R1 | Stronger: novel architecture, comprehensive ablation, genuine model innovation |
| `6yXAKleluj.md` (Probabilistic Sampling GCN, Ethereum) | 4.00 | R1/R2 | Comparable; less dataset contribution but cleaner evaluation |
| `nwjgeFGbAF.md` (Better Call Graphs, dataset paper) | 5.25 | R2 | Dataset-contribution paper with similar strengths; the paper under review has larger-scale data but more active ML overclaiming |
| `eSO9quCgmz.md` (DIPS pseudo-labeling) | 5.00 | R2 | Addresses same core thesis (label quality in SSL) more rigorously, with statistical validation |
| `AEi2wyAMyb.md` (Bi-level pseudo-label optimization) | 5.33 | R2 | More methodologically rigorous SSL contribution |
| `jjjxp9Wgjp.md` (Pseudo-labels for OOD detection) | 4.25 | R2 | Comparable; OOD pseudo-labeling paper with similar evidence gaps |

**Round 1 bracket:** 3.5–5.5  
**Round 2 narrowing:** The paper is weaker than DIPS (5.0) on every methodological dimension: DIPS actually demonstrates improvements over supervised baselines, uses multiple real-world datasets, and has substantially more specific evaluation. The paper is closer to FE-GNN (4.25) in terms of a blockchain feature engineering study without compelling new ML results, though the dataset contribution is a genuine differentiator. Better Call Graphs (5.25) is a true dataset-centric paper without inflated ML claims, and its cleaner framing earns a higher score than the paper under review, which actively overclaims its SSL results.

**Final positioning:** The paper sits between FE-GNN (4.25) and DIPS (5.0), closer to 4.25 because the central ML claim (SSL outperforms supervised) definitively does not hold, the feature-quality ablation lacks statistical grounding, and the conclusion directly contradicts what the body shows. The dataset contribution prevents a score lower than 4.0.

**Axes:**
- *Originality*: Moderate. The dataset is novel; the "quality over quantity" framing is intuitive but the implementation is generic pseudo-labeling.
- *Importance of research question*: High. Bitcoin forensics and CoinJoin detection are genuinely important.
- *Claims well-supported*: Weak. The SSL-improvement claim is not supported; the feature-quality effect is directionally supported but without statistical testing.
- *Soundness of experiments*: Moderate at best. Correct protocol choices but missing baselines, unexplained table rows, and absent statistical testing.
- *Clarity of writing*: Acceptable but the abstract/conclusion actively contradict the body.
- *Value to research community*: The dataset alone has value; the ML contribution as framed does not.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>