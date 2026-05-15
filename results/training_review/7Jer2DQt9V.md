Now I have thoroughly verified all claims against the paper. Let me produce the final consolidated review.

## Summary

This paper (PODGenGraph) benchmarks graph pre-trained models (ContextPred, AttrMask, Mole-BERT, InfoGraph) for out-of-distribution (OOD) generalization across 19 datasets spanning molecular and general graph domains, covering both covariate and concept shifts. The central finding is that pre-trained models, fine-tuned on downstream data, achieve strong OOD performance — often matching or exceeding specialized OOD methods like CIGA, MoleOOD, and LiSA in molecular domains. The paper further analyzes how shift degree, fine-tuning sample size, learning rate, and in-distribution performance affect OOD generalization.

## Strengths

- **Extensive and systematic benchmark spanning diverse OOD scenarios**: The paper evaluates on 19 datasets covering molecular graphs (DrugOOD, MoleculeNet, OGBG, TU) and general graphs (Motif, CMNIST), with both covariate and concept shifts at varying degrees. No prior work has examined such a broad range of graph pre-training strategies against OOD methods in a single unified benchmark.

- **Demonstration that pre-trained models are consistently effective for molecular OOD**: Across all 19 molecular test sets, pre-trained methods achieve the highest or second-highest performance (Section 4.3). This is a genuine empirical finding: even without controlling for the data confound, it shows that pre-training + fine-tuning is a practically useful recipe for molecular OOD.

- **Systematic analysis of key factors with actionable insights**: The paper examines shift degree (Fig. 2a), fine-tuning sample size (Fig. 2b), learning rate (Fig. 2c), and ID vs. OOD performance correlation (Fig. 2d). Key findings — e.g., that 20% of fine-tuning data yields competitive OOD results, and that smaller learning rates do not universally help — offer practical guidance for practitioners.

- **Honest reporting of limitations**: The paper acknowledges that pre-training does not universally help (CMNIST underperformance, Section 4.3; general graphs under concept shift show no advantage). This nuanced reporting is appropriate for a benchmark paper.

## Weaknesses

### Fatal

None.

### Major

- **The head-to-head comparison with OOD baselines is confounded by a large data asymmetry, weakening the central comparative claim.** Pre-trained models (ContextPred, AttrMask, Mole-BERT) are first trained on **2 million molecules from ZINC-15** (Section 4.2, "Pre-training Datasets"), then fine-tuned on downstream tasks. The OOD-specific baselines (CIGA, MoleOOD, LiSA) are trained **from scratch** on only the downstream labeled data. The paper does not state that these baselines received any external pre-training or data augmentation comparable to the 2M-molecule corpus. The observed performance gap is therefore confounded by a massive difference in data volume and representation quality. This does **not** invalidate the paper's contribution — the practical finding that pre-training helps OOD still stands — but it means the headline claim ("even basic pre-trained models ... often surpasses, specifically designed to handle distribution shift") is not properly supported by the evidence as presented. The paper should either (a) acknowledge this confound explicitly and temper the comparative claim, (b) pre-train the OOD baselines on the same data where feasible, or (c) provide an ablation where pre-trained models are trained from scratch on downstream data only to isolate the benefit of pre-training. Without this, the paper's most provocative claim is overstated.

### Minor

- **Baseline architectures and hyperparameter tuning are underspecified.** The paper states (line 121) that a 5-layer GIN with 300 hidden units is used as the backbone for *pre-training methods*, but does not state what architectures are used for CIGA, MoleOOD, and LiSA. These methods have their own architectural designs (e.g., CIGA's separate encoders for invariant/variant parts). If baselines use different backbones, the comparison is further confounded. The paper should at minimum state the architectures used for each baseline. (The request for full hyperparameter sweeps on baselines, however, goes beyond standard practice for benchmarking papers.)

- **Learning rate analysis contains an internal contradiction.** The body text (line 160) states: *"Our empirical investigation shows that models fine-tuned with smaller learning rates achieve better generalization capabilities."* Yet the very next sentences report that *"only for Mole-BERT, a smaller fine-tune learning rate leads to better generalization performance. While for Attraibute masking and context prediction, there is no correlation between generalization performance and fine-tuning learning rates."* The general claim contradicts the specific results. (The abstract correctly states the nuanced finding, so this appears to be a drafting error, but it needs correction.)

- **Pre-training strategy for general graphs is ambiguous.** For molecular datasets, pre-training uses the external ZINC-15 corpus. For general graphs/TU datasets, the paper states (line 119): *"we initially exclude the label information for self-supervised learning"* — implying pre-training on the unlabeled version of the same downstream dataset. This is a fundamentally different regime (no external data) and the paper should state this clearly. As written, a reader cannot tell whether InfoGraph is pre-trained on external data or the same dataset.

- **Shift degree measure conflates model capacity with inherent shift difficulty.** The shift degree formula (Eq. 1, line 153) uses the performance drop of a *specific vanilla GNN* from train to test domains. This measures how hard the shift is for *that particular model*, not an inherent property of the data distributions. While this is a practical heuristic, the paper treats it as a property of the shift itself rather than a model-dependent quantity.

### Trivial

- Table 2 caption: "AOC-RUC" is a typo for ROC-AUC; "MoleculeNem" is a typo for MoleculeNet. These do not affect the scientific content.

## Nice-to-Haves

- **Statistical significance testing.** The paper reports mean and std across 10 seeds but does not test whether observed differences (e.g., 0.2% AUC advantage) are statistically reliable. While not standard practice for large benchmarks, confidence intervals or paired tests on key comparisons would strengthen confidence in the findings.
- **Ablation: pre-trained models from scratch.** An ablation where the pre-trained models are trained from scratch on downstream data (without ZINC-15 pre-training) would directly isolate the contribution of pre-training vs. model architecture.

## Removed Points

These points from the harsh critic are flagged for removal as they do not meet the verification/salience criteria:

- **"Pre-training data confound invalidates the core claim entirely"** — softened to Major rather than Fatal. The core contribution (benchmarking pre-training for OOD, factor analysis) stands independently of the comparison claim. The benchmark findings are still informative.
- **"Cannot be accepted in any form"** — removed as overly harsh. The paper has genuine contributions and the issues are addressable.
- **Typo criticisms** ("AOC-RUC", "Moleculenem") — removed per instructions (parser/formatting artifacts).
- **"The paper does not engage with prior work on fair evaluation of self-supervised vs. supervised methods"** — weakened; this over-demands literature coverage that is tangential to the paper's main goal.
- **"Missing experiments: pre-train OOD methods on ZINC-15"** — moved to nice-to-have. Many OOD methods (CIGA, MoleOOD) require labels for their invariant/causal objectives and cannot straightforwardly use unlabeled ZINC-15 data.
- **"ID vs OOD correlation plot is referenced but not shown"** — the paper states "Fig. 2(d) gives the evaluation" (line 162). The figure is present in the original submission (the parser removes images).
- **"The paper speculates about Mole-BERT's context-aware tokenizer but never tests this"** — this is a nice-to-have mechanistic analysis, not a required experiment for a benchmark paper.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest finding (pre-trained models consistently dominate molecular OOD benchmarks) is simultaneously its most robust empirical result and its most methodologically fraught interpretation. The data asymmetry means the paper cannot cleanly separate *pre-training* from *more data* as the causal factor. The honest CMNIST failure case is actually more revealing than the molecular successes — it suggests that pre-training helps most when the downstream data is structurally similar to the pre-training distribution (molecules from ZINC → molecules in DrugOOD/MoleculeNet), and helps least when the domains are semantically disconnected (molecules → digit images). This points toward a more interesting, testable hypothesis: pre-training for OOD works via representation alignment, not via some general OOD robustness property. The paper's sample-size analysis (strong performance at 20% data) further suggests that the main benefit of pre-training is providing a useful initialization that reduces the data needed for learning the downstream task's core features, rather than providing any special OOD-aware inductive bias. These observations could motivate a more targeted research program than the paper's current "pre-training is unreasonably effective" framing.

## Suggestions

1. **Acknowledge the data confound explicitly.** Add a paragraph in Section 4.3 or the Conclusion noting that the pre-trained models benefit from 2M additional unlabeled molecules, and that this advantage is inherent to pre-training as a paradigm rather than evidence of superiority over OOD methods in equal-data settings. Tone down comparative claims in the abstract/title.
2. **Specify baseline architectures.** State what GNN backbone and training setup are used for CIGA, MoleOOD, and LiSA, including whether any effort was made to use comparable-capacity models.
3. **Fix the learning rate analysis.** The sentence "Our empirical investigation shows that models fine-tuned with smaller learning rates achieve better generalization capabilities" should be revised to reflect the actual finding (only Mole-BERT shows this pattern).
4. **Clarify the InfoGraph pre-training data.** State explicitly that for general graphs/TU datasets, self-supervised pre-training is performed on the unlabeled version of the same downstream dataset without external data.
5. **Add an ablation: pre-trained models from scratch.** Even if only on one or two molecular datasets, showing performance of the pre-trained models' architectures trained from scratch would help isolate the pre-training benefit.

## Score and Decision

**Originality**: Moderate. First systematic benchmark of pre-trained models for graph OOD, though the individual techniques are existing.  
**Importance of research question**: High. OOD generalization is a critical problem in graph learning.  
**Claims well-supported**: Mixed. The benchmarking and factor analyses are well-executed, but the central comparative claim is confounded.  
**Soundness**: Moderate. Experimental design has a genuine confound that weakens comparative conclusions. Within its own benchmarking scope, the methodology is sound.  
**Clarity**: Moderate. Generally clear but has internal contradictions (learning rate) and under-specified details (baseline architectures, InfoGraph data).  
**Value to community**: Moderate. The benchmark results and factor analyses are useful guides for practitioners.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>