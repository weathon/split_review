## Human Reviewer 1

### Summary
The authors propose DTI-DA, a framework for drug-target interaction (DTI) prediction. It integrates graph attention network (GAT), knowledge-aware network (KAN) and domain adaption techniques to improve generalization across domains. They evaluate the proposed model on BIOSNAP and BindingDB datasets, benchmarking across several machine learning models and state-of-the-art DTI prediction models.

### Strengths
1. The paper addresses a relevant and persistent challenge in DTI prediction under domain shift, combining established techniques for domain adaptation and distribution alignment.

2. The evaluation framework is carefully designed, with explicit leakage prevention and reproducibility guarantees.

3. The selected datasets are appropriate for studying domain shift, covering multiple domains.

4. Architectural, training, and dataset details are clearly described, contributing to transparency and reproducibility.

5. The ablation study is well presented and helps understanding the particular contributions of the model.

### Weaknesses
1. The reported improvements are either negligible or nonexistent. Figure 2 shows AUC, AUPR, and ACC metrics (which are not defined in the text, but are conventionally higher-is-better), and the proposed model in fact achieves the lowest scores across most baselines. The claim that the method “surpasses classical and deep baselines” is therefore unsupported by the plots.

2. The paper omits several strong DTI-specific graph-based approaches, such as GeNNiUs (https://doi.org/10.1093/bioinformatics/btad774) and EEG-DTI (https://doi.org/10.1093/bib/bbaa430). Including such methods would better position the proposed framework within current literature.

3. Only two benchmarks (BioSNAP and BindingDB) are considered. Adding additional datasets such as DrugBank or DAVIS would strengthen the empirical validation and test the robustness of the domain-adaptation component.

4. The figure 3 legend contains colors not present in the bars and mixes different metrics in the same panel, making interpretation difficult. I recommend tabular results with mean ± standard deviation across multiple random seeds for both Figures 2 and 3, which would also address the absence of significance reporting.

5. The manuscript includes several textual errors and translation artifacts — for example, “train spéciale split”, “betrieben splits”, and the incorrect reference “MMD (Mann-Whitney U statistic)”. These should be carefully corrected.

### Questions
1. Given that the paper focuses on domain adaptation, could the authors evaluate cross-dataset generalization, e.g., training on one dataset and testing on another (such as different families of the Yamanishi benchmark—GPCR, IC, NR, etc.)? This would provide stronger evidence of robustness to real distribution shifts.

2. Since graph-based architectures can be computationally demanding, could the authors report training and inference costs (e.g., runtime per epoch, GPU memory usage) to assess the practical feasibility of the proposed model?

3. Have the authors explored whether the proposed approach can identify or prioritize novel drug–target interactions in unlabeled target domains? This seems like a natural and impactful application of domain adaptation in DTI prediction.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper presents DTI-DA an end-to-end model for predicting drug-target interactions when training and test data come from different distributions. The model encodes molecules with a graph-attention network, proteins with a lightweight sequence encoder, introduces known drug–drug/target–target similarities through a small “knowledge-aware” module, and aligns source/target domains using moment-matching and an adversarial discriminator. The authors compare the model in two databases: BioSNAP and BindingDB.

### Strengths
The model fuses prior biologica/chemical information with compact encoders and uses well understood domain adaptation techniques to tackle the DTI inference problem.

### Weaknesses
The paper has major drawbacks:

- The results are shown only on one run which makes it very difficult to evaluate the true performance. The authors acknowledge that, however the model should be run across different splits and more datasets.

- Figure 2 shows that the proposed model is the worst performing model.....

- Figure 3 states that there is a typographical error in the figure....

### Questions
- Provide confident thresholds across multiple runs

- Improve the text, it is currently oddly written

- The figures are either completely wrong, or the proposed model is outperformed by the other methods.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
0

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes a model that combines graph attention networks, knowledge graph propagation, and domain adaptation to predict drug–target interactions more robustly across datasets. Drugs are encoded with GAT, proteins with a lightweight sequence encoder, and relational priors are injected through a Knowledge-Aware Network (KAN). To handle dataset shifts, the model aligns source and target domains using both MMD and adversarial training. Experiments on BioSNAP and BindingDB show that DTI-DA slightly outperforms MolTrans, demonstrating the value of knowledge injection and domain adaptation, though the performance gain is modest due to already strong transformer-based baselines and the simplicity of the protein encoder.

### Strengths
* It presents a novel combination of knowledge injection + domain adaptation. This method integrates relational priors and domain invariance in one architecture.
* The experimental setting avoids data leakage through clear separation between source-only and transductive UDA settings.
* It provides reproducibility with fixed seeds, scripts, and detailed instructions.

### Weaknesses
* It shows marginal performance gain. Only ~0.0066 AUC improvement over MolTrans despite added complexity.
* It uses a weak protein representation. The lightweight encoder limits expressivity. 3D or structure-informed encoders could help.
* The results need to secure the statistical significance. They provide only single-run point estimates without confidence intervals.

### Questions
Have you ever tried applying the KAN to a complex setting like MolTrans? I’d like to understand how much KAN would influence performance under a similar setup, since MolTrans itself is already quite sophisticated. It might already be implicitly performing some of the functions that KAN is designed to achieve.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
4

### Confidence
2

---

## Human Reviewer 4

### Summary
The paper proposes DTI-DA, a framework for drug-target interaction (DTI) prediction designed to be robust to domain shifts. The core problem is that DTI models trained on one data-gathering protocol or chemical family (source domain) generalize poorly to another (target domain). The DTI-DA model combines three main components: a GAT to encode compound structures, a KAN that refines embeddings by propagating information over prior-knowledge graphs (drug-drug similarity), a dual domain adaptation mechanism using both Maximum Mean Discrepancy and an adversarial discriminator with a Gradient Reversal Layer.

### Strengths
- Clear evaluation method. The authors address a major source of ambiguity in comparisons that is problem in domain adaptation research.
- Thorough ablation study

### Weaknesses
- The authors say "We do not make claims of statistical significance and all numbers are treated as single-run point estimates at a fixed protocol". Reporting results from a single run is not sufficiently robust for an ICLR publication. The claimed improvements are small (+0.895% relative gain on BioSNAP AUC ), and without mean and variance over multiple random seeds, it is impossible to know if these gains are real or artifacts of a single fortunate run. The authors' note that their artifact provides "scaffolds for replicated run"  does not excuse the omission of these critical statistics from the paper. 

- Confusing results report in the paper. It seems from the figures that the proposed method performs worse than baseline but the text tells a different story?

- The proposed DTI-DA model is largely an assembly of existing, well-established components. Using GATs for molecular graphs is standard (e.g., GraphDTA ). The KAN is a 1-layer GCN-style propagation on a similarity graph, followed by a residual gate. This is a common and simple technique for integrating graph-based priors. The domain adaptation strategy (combining MMD and GRL-based adversarial loss) is a common approach in UDA. While the engineering and evaluation of this pipeline are contributions, the core architectural novelty required for ICLR pub is lacking.

- The paper claims to avoid "apples-to-oranges" comparisons, but its main results (Figure 2, Section 5.1) do exactly that. The DTI-DA model's performance is reported from the "transductive UDA track", while the baselines (GraphDTA, MolTrans) are "trained in their conventional source-only manner". This is an unfair comparison, as the DTI-DA model has access to unlabeled target data while the baselines do not. A fair comparison would require evaluating all methods under both the source-only and transductive UDA tracks.

### Questions
- Can you provide the mean and standard deviation?
- Please provide fair baseline comparison numbers, as your current main results compare a UDA-trained model to source-only models.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3