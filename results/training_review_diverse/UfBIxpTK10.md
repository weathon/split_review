Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper tackles the problem of poor generalization in machine-learning-based blind docking to unseen protein domains. It makes three contributions: (1) **DockGen**, a new benchmark based on ECOD protein domain classification that more rigorously tests generalization than existing PDBBind-based splits; (2) a **scaling-law analysis** showing that increasing model size (to 30M parameters), training data (+52% from MOAD), and synthetic van der Mer (vdM) augmentations jointly improve DockGen success rate from 7.1% to 22.6% (DiffDock-L); and (3) **Confidence Bootstrapping**, a self-training method that uses a confidence model to re-weight generated poses and fine-tune early diffusion steps, improving DiffDock-S from 9.8% to 24.0% on a held-out subset of 8 protein clusters.

## Strengths

- **DockGen benchmark properly isolates generalization to unseen binding domains.** The paper demonstrates that existing splits (UniProt-ID, global sequence similarity) allow train–test leakage because binding pockets can be conserved even when global sequence identity is low. Using ECOD domain classification, the authors show that PDBBind's 2019 test set adds only 8 new clusters (15 complexes), whereas DockGen introduces 179 unseen ECOD clusters from MOAD. Figure 1B quantifies the lower train–test binding-site similarity in DockGen vs. PDBBind. This is a well-motivated and practically useful benchmark for the community.

- **Clear identification of a real failure mode.** The paper shows stark performance drops on DockGen: regression methods (EquiBind, TankBind) achieve 0% success, and DiffDock falls from 35.0% on PDBBind to 7.1% on DockGen-full. This quantitatively validates that existing methods overfit to seen binding domains and motivates the need for better generalization.

- **Systematic scaling-law analysis provides actionable insights.** Figure 3 shows clear trends across model size (4M→30M parameters), training data (adding MOAD +52%), and synthetic vdM data. The combined DiffDock-L raises performance from 7.1% to 22.6%, even outperforming search-based methods (GNINA at 17.5%). These results are useful for guiding community efforts on data collection and model scaling.

- **Confidence Bootstrapping is a novel and well-motivated training paradigm.** The idea of exploiting the multi-resolution structure of diffusion models — using the confidence model to guide early diffusion steps while preserving fine-grained denoising via training data — is grounded in a clear insight: checking a pose is easier than generating one. The formulation with separate weighting functions λ(t) and λ'(t) is principled.

- **Bootstrapping results are promising despite limited evaluation scope.** On the DockGen-clusters subset, fine-tuning DiffDock-S raises success rate from 9.8% to 24.0%, with half of clusters exceeding 30%. The method achieves this using only binding affinity information (not structural data) from unseen domains, which is a non-trivial demonstration.

## Weaknesses

### Fatal

None.

### Major

- **The evaluation of Confidence Bootstrapping is too limited to fully support its claimed generality.** The method is evaluated only on a subset of 8 clusters (85 complexes) using only the small DiffDock-S model. It is not tested on DiffDock-L, nor on the full 189-complex DockGen test set. The paper also does not include any ablation of its key design choices — e.g., comparing the proposed λ(t) vs λ'(t) weighting against uniform weighting, or against simpler self-training alternatives such as standard pseudo-labeling or direct confidence-based filtering of generated poses. Without these, it is difficult to attribute the observed improvements specifically to the multi-resolution feedback mechanism, which is presented as the core contribution.

- **Lack of statistical rigor for central claims.** The bootstrapping results (Figure 4) are averages over only two fine-tuning runs with no error bars, per-run breakdown, or variance discussion. The scaling law for the largest model (30M parameters) is based on a single run (acknowledged as cost-prohibitive). For a method that involves stochastic sampling, confidence reweighting, and iterative fine-tuning, readers cannot assess whether the observed gains (e.g., 9.8%→24.0%) are robust or within the noise of a single training seed. This weakens the paper's central claims about both scaling and bootstrapping.

### Minor

- **The bootstrapping experimental pipeline is described ambiguously.** The paper states it fine-tunes "on protein domain clusters ... without access to their structural data" and the method formalization mentions using known binders from BindingDB (line 121, 127). However, the experiment description (Section 5.2) only says "we fine-tune a model on each protein domain cluster" without explicitly stating that the binders per cluster came from BindingDB rather than from the test complexes' structural data. While the intended interpretation is clear from the method section, this ambiguity is unnecessary and raises reproducibility concerns.

- **The contribution of the vdM augmentation is never isolated.** The paper combines vdM synthetic data with increased training data and model scaling, but provides no controlled experiment measuring vdM's effect alone. The text only notes it "seems to provide some improvements when scaling to larger model sizes" — a qualitative statement without supporting ablation.

- **No compute cost reported for bootstrapping.** Given that the method is presented as a practical alternative to large-scale data collection, the lack of any quantification of the computational overhead (number of diffusion rollouts per iteration, total GPU hours) is a gap.

- **No comparison to alternative self-training or semi-supervised baselines.** The paper compares bootstrapped DiffDock-S against non-bootstrapped baselines (SMINA, GNINA, DiffDock). But it does not compare against standard pseudo-labeling, confidence-threshold filtering without the multi-resolution weighting, or other generic self-training heuristics applied to the same setting. This makes it hard to isolate the benefit of the proposed mechanism over simpler alternatives.

### Trivial

- The paper states that DiffDock-L achieves 27.6% on DockGen-clusters while the bootstrapped small model reaches 24.0% on the same subset. This is reported in Table 1 but the relationship between scaling and bootstrapping is not discussed. A brief explicit comparison would help readers understand the trade-offs.

## Nice-to-Haves

- Running bootstrapping on DiffDock-L or the full DockGen test set would strengthen the claim that the method generalizes beyond compensating for a small model's limitations.
- Reporting per-cluster statistics on how many BindingDB binders were available would improve reproducibility and help assess the method's data requirements.
- A discussion of how the small test set size (85 complexes, 8 clusters) affects the reliability of reported success rates (e.g., confidence intervals via bootstrapping over complexes) would be a useful addition.

## Removed Points

1. **"Data leakage / test complexes used during fine-tuning would invalidate results"** — Removed because it misunderstands the paper: the method explicitly operates "without access to structural data" (line 19) and uses binding affinity data (BindingDB, line 121, 127) rather than ground-truth poses from the test complexes. The ambiguity is in presentation, not in methodology.
2. **"The stated vdM drawback about weak binders is not addressed"** — Removed because the paper explicitly acknowledges this drawback (line 151: "The drawbacks are that these synthetic complexes are of unknown affinity (many could be weak binders)"). Acknowledging a limitation is not the same as ignoring it, and the paper is not required to experimentally resolve every acknowledged limitation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify the bootstrapping experimental pipeline in Section 5.2 by explicitly stating: (a) binders per cluster came from BindingDB (or another affinity database), (b) how many binders were available per cluster, and (c) that no structural pose information from the test complexes was accessed at any point during fine-tuning.
2. Add at least one ablation study — either comparing λ(t) vs λ'(t) weighting against uniform weighting, or comparing against a simpler pseudo-labeling baseline without the multi-resolution targeting. This is critical to validate the claimed mechanism.
3. Run the bootstrapping procedure with at least 3 independent seeds and report error bars (or per-seed performance) to give readers a sense of variance.
4. Report the computational cost of bootstrapping (GPU hours, number of diffusion rollouts per iteration, total iterations) to support the claim that it is a practical method.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>