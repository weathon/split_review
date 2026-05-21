---
job_id: 826bf5f8-7f5e-4126-af60-8badd4ea2cee
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: zNH3Sf404X.pdf
paper: Quality Over Quantity: Semi-Supervised Detection of Illicit Bitcoin Flows via Feature Engineering
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly about semi-supervised learning for illicit Bitcoin transaction detection, with substantial emphasis on feature engineering, learning under label scarcity, and graph/blockchain-structured data, all of which fit ICLR scope.

## Minimum Quality
Pass ✅. The paper includes an abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion. While there are notable weaknesses in novelty, experimental validation, and methodological specification, these do not rise to the level of a desk rejection based on the main paper alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies illicit Bitcoin CoinJoin or Shared Send Mixer transaction detection under scarce labels and heavy class imbalance, and argues that semi-supervised learning is only effective when guided by high-quality features rather than by data volume alone. The main ingredients are a large historical Bitcoin dataset with CoinJoin classification, engineered features based on KeyLinker clustering and Shared Send Untangling (SSU) complexity, and a selective pseudo-labeling pipeline evaluated with tree-based classifiers such as XGBoost, CatBoost, and Random Forest.

## Strengths
The paper tackles a relevant and difficult application setting, namely illicit flow detection in heavily obfuscated Bitcoin transactions where labels are scarce and noisy. That setup is a reasonable fit for semi-supervised learning, and the framing around label scarcity in mixed transactions is well motivated in Sections 1 and 5.

The dataset scale is impressive on paper. Table 1 reports 1.15B transactions, 163.4M CoinJoin transactions, and 4.6M labeled CoinJoin examples, which, if made available as promised, could be useful for the community working on financial graph learning and blockchain forensics. Even though the paper does not fully capitalize on this scale experimentally, assembling this corpus is still a meaningful engineering effort.

The feature ablations in Table 2 are one of the more useful parts of the paper. They consistently show that adding REUSE and CS features improves over the DEFAULT set across all three models, and that OTC often hurts slightly. For example, for XGBoost, the progression from DEFAULT to DEFAULT+REUSE+CS raises F1 from 0.814 to 0.844 and ROC AUC from 0.959 to 0.970, while adding OTC slightly reduces F1 to 0.841. This supports the narrower empirical claim that some heuristics are more informative than others.

Likewise, Table 3 shows a fairly consistent pattern across models in the semi-supervised setting: the best-performing feature combination remains DEFAULT+REUSE+CS+SSU, and adding OTC again tends to degrade or fail to improve results. That pattern is coherent with the paper’s central message that pseudo-label quality matters. I appreciate that the paper does not try to oversell large SSL gains when the observed effect is modest.

The figures are simple but helpful for readers outside the blockchain-forensics niche. Figure 1 gives an accessible illustration of the UTXO transaction model and the privacy leakage channels that motivate the downstream analysis. Figure 2(a) and Figure 2(b) also make the distinction between CS and OTC heuristics concrete, which is important because a large part of the paper’s argument depends on treating these heuristics as qualitatively different sources of signal and noise.

Presentation-wise, the paper is generally readable at a high level. The problem statement in Section 4 at least attempts to formalize the objects being classified and the role of address tags and clustering relations, which is preferable to a purely informal description.

## Weaknesses
1. **The claimed semi-supervised contribution is empirically underwhelming, and in places contradicted by the paper’s own tables.**  
   The paper repeatedly claims that the semi-supervised framework “outperforms supervised baselines” and that SSL “effectively leverages unlabeled data” (Abstract, Section 1, Section 7). However, Table 2 versus Table 3 does not really support a meaningful improvement over the supervised setting. For the best XGBoost configuration, supervised performance is already F1 = 0.844 with DEFAULT+REUSE+CS and F1 = 0.842 with DEFAULT+REUSE+CS+SSU (Table 2), while the best SSL result is F1 = 0.845 with DEFAULT+REUSE+CS+SSU (Table 3). That is essentially flat. For CatBoost and Random Forest, the SSL gains are similarly tiny or absent. If the core claim is “quality-driven SSL,” then the evidence should show a clear advantage over a supervised counterpart or over standard pseudo-labeling. Right now, the paper mostly shows that the feature set matters, not that the SSL design itself matters.

2. **The pseudo-labeling method is underspecified at the level needed to assess soundness and reproducibility.**  
   Section 5.3 says the method selects “the top fraction of samples on both sides of the decision boundary,” but it never specifies the fraction, whether it is fixed or adaptive, whether it is tuned on validation data, whether calibration is used, whether selection is performed once or iteratively, how class balance among pseudo-labels is enforced, or how many pseudo-labeled examples are finally added. This is not a small omission, because the entire SSL contribution depends on these design choices. The paper also states in Section 5.2 that pseudo-labels are prioritized based on transaction structural quality and clustering heuristic quality, but there is no algorithmic description connecting that principle to an explicit sampling or weighting rule. In other words, the “data quality principle” is stated as a narrative, not as a well-defined method.

3. **The mathematical formalization in Section 4 contains problematic assumptions and ambiguous notation.**  
   The relation
   \[
   \forall A,A' \in \mathcal{A}: A \sim A' \implies \mathrm{Tag}(A)=\mathrm{Tag}(A')
   \]
   is much stronger than the actual data conditions described elsewhere. Since labels come from off-chain sources and heuristics like CS and especially OTC are acknowledged to be noisy, exact tag equality under clustering is not justified. This matters because the paper later argues that OTC introduces noise, yet the formal statement treats propagated tags as deterministic and exact. The formalization should distinguish observed tags, inferred cluster membership, and propagated labels, perhaps probabilistically or with confidence weights. As written, the paper collapses these uncertainty sources into an overly clean symbolic statement.

   In the same section, the mapping \( t \mapsto t_{\text{sim}} = \texttt{Simplify}(t) \) is introduced for complexity analysis, but the actual simplification operator is not defined. Since SSU complexity classes are later used as key features, the exact transformation is not a side issue. The reader cannot tell what information is preserved, what is aggregated away, or whether simplification could itself leak target-related information.

4. **The paper makes a “prove” claim that is not matched by any theorem, proposition, proof, or rigorous argument in the main paper.**  
   The Abstract says, “Crucially, we prove that common heuristics like One-Time Change (OTC), though abundant, introduce noise,” and Section 1 similarly uses language such as “we show” and “proving that performance is driven by data quality.” But the main paper contains no theorem, no formal proposition, and no derivation that establishes such a proof. At best, Tables 2 and 3 provide an empirical observation that adding OTC slightly hurts performance. That is not a proof that OTC is noisy in any general sense. This is an overstatement and should be toned down substantially.

5. **The novelty relative to existing blockchain AML literature is not clearly established, especially on the ML side.**  
   The actual learning pipeline is a fairly standard combination of engineered features, class-weighted tree ensembles, and pseudo-labeling. The paper’s main novelty seems to lie in the use of KeyLinker and SSU-derived features plus a large CoinJoin-oriented dataset. That may still be a valid application contribution, but the paper often presents the overall framework as a methodological advance in SSL. I do not see that. The pseudo-labeling setup is generic, and there are no comparisons to stronger semi-supervised or graph-based baselines that are highly relevant for this domain. The related work section mentions GNNs and some recent graph models, but the experimental section does not compare against them at all. This weakens the paper’s positioning for ICLR, where a strong methodological or representation-learning angle is expected.

6. **Key baselines are missing, making it hard to attribute gains to the proposed ideas rather than to standard feature ablation effects.**  
   There is no comparison to a standard self-training or pseudo-labeling baseline that ignores the proposed “quality principle,” even though that is the central contrast the paper wants to establish. A simple baseline such as confidence-threshold pseudo-labeling on all unlabeled data would have been essential. Without it, the claim that selective, quality-aware pseudo-labeling is better than standard pseudo-labeling is not demonstrated. Similarly, because the task is graph-structured by nature, the absence of graph-based baselines is hard to ignore. If the authors want to argue that careful feature engineering beats more complex models in this domain, they need to actually run those comparisons.

7. **The results tables are informative but statistically thin, and the paper overinterprets small metric differences.**  
   Tables 2 and 3 report single numbers with three decimal places, but there are no standard deviations, confidence intervals, or fold-wise summaries. This is a serious issue because many of the claimed gains are in the range of 0.001 to 0.005 in F1 or ROC AUC. For example, the difference between XGBoost with DEFAULT+REUSE+CS and DEFAULT+REUSE+CS+SSU in Table 3 is 0.839 versus 0.845 in F1, which may or may not be meaningful. Without uncertainty estimates, the paper’s “quality over quantity” conclusions are more fragile than the prose suggests.

8. **The experimental protocol leaves open concerns about temporal leakage and unrealistically favorable generalization.**  
   Section 5.3 says the labeled CoinJoin dataset is split into train, validation, and test using stratified random partitioning. But blockchain transactions are temporally ordered and exhibit strong entity recurrence. Random splits can overestimate performance if patterns from the same time periods, services, or clustered entities appear across train and test. Given that the paper’s features explicitly use address clustering heuristics and off-chain tags, this is not a hypothetical concern. A temporally split evaluation, or at least a split by entity clusters, would be much more convincing for a deployment-facing claim about illicit flow detection.

9. **The label semantics are inconsistent and somewhat muddled across transactions, addresses, services, and clusters.**  
   Section 4 defines the classifier over transactions \(f:\mathcal{T}\to\{0,1\}\), but many labels appear to originate at the address level via \(\mathrm{Tag}:\mathcal{A}\to(\mathcal{L}\cup\{\bot\}) \times (\mathcal{C}\cup\{\bot\})\). It is not made precise how address-level legality labels are aggregated into transaction-level labels, especially for CoinJoin transactions involving multiple parties and mixed service associations. This is a critical missing link because the target variable itself may inherit ambiguity. Table 1 also reports legality labels in terms of counts that appear to be addresses, while Section 5.1 and Section 5.3 discuss labeled CoinJoin transactions. The transition between these labeling granularities needs a far clearer specification.

10. **The feature definitions are too coarse for the claimed forensic insight.**  
    Section 5.1 says the authors designed four groups of features, including UTXO attributes, transaction values, address behavior, and specialized SSU/service attributes. But the actual feature list is barely described. For instance, “market concentration index” is mentioned without definition; REUSE is treated as a feature family without specifying exact variables; SSU complexity labels are included, but whether they are one-hot encoded, ordinal, or augmented by counts is not stated. Since the paper’s central thesis is about high-quality feature engineering, the feature engineering itself should be documented much more concretely.

11. **Some exposition and citation issues reduce confidence in careful scholarship.**  
    There are several writing problems, including awkward or broken sentences in Related Work on Pages 4 to 5, and at least one apparently irrelevant citation, namely the Lee et al. (2024) reference on BAYC NFT rarity listed on Page 10, which does not match the text’s discussion of “CENSor” in Section 3. That sort of mismatch is not a fatal flaw by itself, but it does make the literature positioning look less reliable than it should be for a paper whose novelty rests partly on contextual differentiation.

12. **The figures are pedagogical, but they do little to support the core empirical contribution.**  
    Figure 1 and Figure 2 are useful illustrations of the UTXO model and heuristics, but they are introductory cartoons rather than evidence-bearing figures. There is no figure analyzing pseudo-label quality, class-wise performance, feature importance, or error modes by SSU class. Given how central the “quality over quantity” claim is, I expected at least one figure showing how performance changes as more pseudo-labels are added, or how OTC versus KeyLinker differ in noise characteristics. The absence of such analysis makes the paper’s narrative feel more asserted than demonstrated.

## Questions
1. The main paper needs a precise algorithmic specification of pseudo-labeling. What exactly is the selection rule? Please specify the fraction or threshold used, whether it is tuned on the validation set, whether pseudo-labeling is one-shot or iterative, and how many positive and negative pseudo-labels are added for each configuration. A concise algorithm box would substantially increase confidence.

2. Can the authors provide a direct baseline comparing their quality-aware pseudo-labeling against standard pseudo-labeling that simply takes high-confidence unlabeled examples regardless of SSU class or heuristic provenance? This is the most important missing experiment for validating the central claim.

3. How are transaction labels derived from address-level tags in mixed transactions? Please give an explicit rule or formal mapping. For a CoinJoin transaction containing addresses with conflicting service or legality tags, how is the final binary transaction label assigned?

4. Can the authors report variability across folds or repeated runs for Tables 2 and 3, ideally with mean ± std or confidence intervals? Many of the reported gains are very small, so uncertainty quantification is necessary.

5. Have the authors tested temporal splits or entity-disjoint splits? A random stratified split may overestimate real-world performance in blockchain data because closely related patterns can appear in both training and test.

6. The paper claims to “prove” that OTC introduces noise. Is there a formal proof intended, or should this be reframed as an empirical observation? If a proof exists, it needs to appear in the main paper; otherwise the wording should be softened.

7. Since Figure 2 is used to motivate the distinction between CS and OTC heuristics, can the authors quantify this distinction more directly, for example by reporting pseudo-label purity or downstream error rates separately for examples selected using KeyLinker, CS, and OTC? That would turn the current conceptual figure into evidence connected to the main claim.

8. The paper repeatedly emphasizes data quality. Is there any measurable operationalization of “quality” in the experiments beyond feature inclusion choices? For example, do the authors have a confidence score, estimated noise rate, or calibration measure for pseudo-labels by SSU class or clustering heuristic?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)

## Details Of Ethics Concerns
The paper studies deanonymization-adjacent blockchain forensics and illicit flow detection. This kind of work has obvious dual-use implications: it may help law enforcement and compliance efforts, but it can also inform adversaries about which transaction patterns or heuristics are most detectable and therefore how to adapt. The concern is not that the work should not be published, but that the paper should more explicitly discuss misuse risks and operational safeguards.

There are also data-governance questions around the aggregation and planned release of labels from multiple external sources, including WalletExplorer, Elliptic++ and Kaggle-derived datasets (Section 5.1). The paper does not discuss usage rights, redistribution permissions, or whether all upstream sources permit repackaging into a new released dataset. Since the contribution includes a large compiled dataset, compliance and licensing deserve a brief explicit discussion.

## Soundness Rating
2: fair. The empirical study is substantial enough to be interesting, but the central SSL claim is only weakly supported, the pseudo-labeling method is underspecified, and some formal statements are stronger than the evidence warrants.

## Presentation Rating
2: fair. The paper is readable at a high level and the tables are useful, but key methodological details are missing, some notation is overcompressed or misleading, and the literature/exposition has noticeable rough edges.

## Contribution Rating
2: fair. The dataset assembly and domain-specific feature engineering are potentially useful, but the machine learning contribution is incremental, and the paper does not convincingly establish a strong semi-supervised or representation-learning advance.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses an important problem and has some value as a large-scale empirical study with domain-specific features, but the main claims are stronger than the evidence, the SSL methodology is too loosely specified, and the experimental validation is not strong enough for ICLR in its current form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The main reasons for my score are visible in the paper itself: the gap between the claims and the actual tables, the missing algorithmic detail for pseudo-labeling, and the lack of decisive baselines.