Now I have all the evidence I need. Let me construct the final consolidated review.

## Summary

This paper presents GDL-DS, a benchmark for evaluating geometric deep learning models under distribution shifts across three scientific domains (particle physics, materials science, biochemistry). It covers 10 distribution shifts at three levels of OOD data availability (no information, unlabeled features, few labels), evaluates 11 learning algorithms on 3 GDL backbones, and introduces a causal categorization framework to connect shift types to recommended solution strategies. The paper's main contribution is a systematic, multi-domain evaluation infrastructure that yields actionable recommendations for practitioners.

## Strengths

- **Comprehensive coverage across shifts, domains, and OOD info levels.** The benchmark spans 10 distribution shifts across 3 scientific domains and 3 levels of OOD data access, yielding 30 experimental configurations — substantially broader than prior benchmarks that typically cover a single domain or shift type (e.g., DrugOOD covers only biochemistry, Hoffmann et al. only fidelity shifts). This breadth enables the paper's central finding: no single method dominates, and method selection should depend on shift type and data availability.

- **Principled causal categorization of distribution shifts.** The paper formalizes shift types (covariate, concept, conditional) through a causal data model with $X_c$ (causal) and $X_i$ (independent) components, and further sub-categorizes conditional shifts into $\mathcal{C}$-conditional and $\mathcal{T}$-conditional variants. This causal grounding goes beyond purely empirical shift descriptions and is used to interpret experimental outcomes (e.g., why DA methods help when shifts affect critical features).

- **Actionable, domain-grounded recommendations.** The paper distills three concrete takeaways and a three-step decision guide (assess shift type → assess OOD data availability → select method category), backed by specific observations from Table 3. These are precisely the kind of output a benchmark should produce for practitioners.

- **Creation of new, physically motivated benchmark datasets.** The Track-Pileup and Track-Signal datasets are newly constructed with shifts that mirror real experimental conditions in high-energy physics (varying pileup noise, varying signal particle momenta), with clear mappings to the paper's causal shift categories.

- **Integration of multiple OOD solution families under one framework.** Evaluating OOD generalization methods (No-Info), domain adaptation methods (O-Feature), and transfer learning (Par-Label) within the same benchmark enables cross-level comparisons that reveal trade-offs (e.g., catastrophic forgetting when few OOD labels are available) that single-level studies would miss.

## Weaknesses

### Major

- **Missing hyperparameter tuning protocol.** Section 4.1 contains the heading "Hyperparameter Tuning." on line 145 with no text following it. For a benchmark that compares 11 learning algorithms across 3 backbones and 30 settings, the tuning procedure is foundational to the fairness and interpretability of every comparison. Without knowing the search space, selection criterion, or number of trials, readers cannot assess whether observed performance differences reflect genuine algorithmic advantages or arbitrary hyperparameter choices. This must be added for the experimental claims to be credible.

### Minor

- **Incomplete results in the main text.** The paper claims 10 distribution shifts and evaluates 3 backbones (EGNN, DGCNN, Point Transformer), but Table 3 reports results for only 8 shift cases on 2 backbones. The Assay shift (a concept shift, directly relevant to one of the paper's key takeaways about TL methods under concept shifts) and Point Transformer results are not shown. While these likely appear in the appendix, the main paper should at minimum cross-reference where these results live and ideally include a summary or pointer so readers can verify central claims without hunting through supplementary material.

- **Ambiguous O-Feature evaluation protocol.** The paper states that data is split into Train-OOD, Val-OOD, and Test-OOD (line 141), but then says DA methods are trained on "data features of the whole OOD dataset" (line 143). It is unclear whether "the whole OOD dataset" includes Test-OOD features. While using unlabeled target features in unsupervised DA is standard practice and not "leakage" per se, the ambiguity should be resolved: the paper should explicitly state which OOD splits are used for adaptation and confirm that no Test-OOD labels are seen.

- **Dataset split specifications lack full reproducibility detail.** For the Signal shift, the paper mentions 5 source-domain subgroups each corresponding to "a specific type of signal decay" without naming the decay types; for DrugOOD-3D, it references "the same design of domain splits and sub-group splits as DrugOOD" without specifying which of DrugOOD's multiple cores/splits are used. Sample counts per subgroup are not provided. While some of these details are natural for an appendix, the paper should include a pointer to where these specifications can be found.

- **Causal categorization is asserted rather than empirically validated.** The paper assigns each dataset's shift to a causal category based on domain knowledge. While this is reasonable and the paper acknowledges the data model's limitations (line 63: "our data model does not aim to cover all possible causality relationships"), the "insightful conclusions" depend on these categorizations being correct. The paper would benefit from an explicit caveat that the categorizations are domain-informed hypotheses, and from discussing how robust the conclusions are to potential misclassification.

### Trivial

- **Notation inconsistencies.** The target domain is denoted as both $\mathcal{T}$ and $\tau$ interchangeably (e.g., line 57 uses $\mathbb{P}_{\mathcal{T}}$, line 67 uses $\tau$). The symbols $\dot{\mathbb{P}}$ and $\bar{\mathbb{P}}$ appear on line 80 without prior introduction. Line 57 has a typographical glitch ($\mathbb{P}_{7}$ appears instead of $\mathbb{P}_{\mathcal{T}}$).

## Nice-to-Haves

- **Include a non-GDL baseline** (e.g., an MLP on invariant features or a 2D GNN) to clarify whether the observed behaviors are specific to geometric architectures.
- **Add a quantitative summary** (e.g., average rank across settings, win-tie-loss matrix) to support the qualitative observations in Section 4.3, rather than relying solely on visual inspection of Table 3.
- **Report Test-ID performance for TL methods** to assess whether fine-tuning degrades in-distribution accuracy, which would strengthen the catastrophic forgetting discussion.

## Removed Points

- **"Data leakage in O-Feature setting" framed as an unfair advantage.** The harsh reviewer claimed DA methods have an "information advantage" over other methods. This misunderstands the benchmark design: the different OOD info levels are an *intentional* axis of variation — DA methods are *supposed* to have access to unlabeled target features. That is the definition of the O-Feature level. The remaining kernel of a valid concern (ambiguity about which OOD split is used) is kept as a Minor weakness above.

- **Claims that reproducibility concerns stem from "not yet released" or "unverifiable" datasets/models.** The paper cites existing datasets (DrugOOD, QMOF) and methods — these are publicly available. Removed per hard rule.

- **Demand for conditional independence tests to validate causal categorization.** The paper clearly acknowledges its data model's limitations (line 63). Requiring formal statistical tests for a benchmark paper's design choices is outside the scope of what is standard or expected. The concern is kept in weakened form as a minor caveat.

## Novel Insights

The most interesting observation emerging from this review is that the paper's main vulnerability is not any single experiment being wrong, but a gap in methodological transparency (empty hyperparameter tuning section) that makes it impossible to assess whether the experiments are trustworthy. This is an unusual failure mode for a benchmark paper — the curation and design are largely sound, but a documentation gap undermines the very comparisons the benchmark exists to enable. The causal taxonomy itself is a genuine strength, but it also creates a fragility: if any shift is miscategorized, the paper's "insightful conclusions" could lead practitioners astray. The interplay between the strength of the taxonomy and the weakness of its empirical grounding is the paper's deepest tension.

## Suggestions

1. **Fill the Hyperparameter Tuning section completely.** For each method and backbone, report: search space, selection criterion (validation ID vs. OOD), number of trials, and final selected hyperparameters. Without this, the benchmark's comparisons are uninterpretable.
2. **Cross-reference all 30 settings to results locations.** Add a table or figure caption in the main text mapping each of the 10 shifts × 3 info levels to where results appear (Table 3 or specific appendix section).
3. **Clarify the O-Feature split usage.** State explicitly which OOD splits (Train-OOD only, or Train+Val+Test-OOD features) are used for unsupervised DA, and confirm that Test-OOD labels are never seen during adaptation.
4. **Strengthen the caveat on causal categorization.** Add a sentence acknowledging that the shift categorizations are domain-informed hypotheses and that practitioners should verify the categorization in their own applications.

## Score and Decision

The paper addresses a genuine gap — distribution shift evaluation for geometric deep learning in scientific applications — with a comprehensive design and a useful causal taxonomy. The curation of datasets, the breadth of methods, and the actionable takeaways all represent real contributions. However, the empty hyperparameter tuning section is a significant documentation failure for a benchmark paper: it prevents readers from assessing whether the experimental comparisons are fair, which undermines the credibility of the results. This is fixable (the authors likely have this information), but as submitted, the paper is incomplete. With the tuning protocol documented and the minor issues addressed, this would be a strong resource for the community.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>