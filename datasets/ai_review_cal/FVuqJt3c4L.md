- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 5, 8, 8
Here is the final consolidated review:

---

## Summary

This paper introduces Population Transformer (PopT), a modular self-supervised framework that learns to aggregate per-channel temporal embeddings across variable electrode configurations in neural recordings. PopT stacks a transformer on top of frozen single-channel encoders and is pretrained with two discriminative objectives (ensemble-wise and channel-wise) that require reasoning about spatial and temporal relationships. The approach is evaluated on iEEG (4 auditory-linguistic tasks) and EEG (seizure detection), across 4 different temporal encoders and 5 downstream tasks. Results show consistent improvements over linear/deep NN aggregation baselines, competitive performance with end-to-end models, sample/compute efficiency gains, and generalization to held-out subjects. The paper also demonstrates interpretability uses including connectivity analysis and functional region identification from attention weights.

## Strengths

1. **Novel and well-motivated modular design** — PopT decouples temporal encoding from spatial aggregation, making it agnostic to the underlying temporal encoder. The paper validates this across 4 different encoders (BrainBERT, TOTEM, Chronos, TS2Vec) and 2 modalities (iEEG, EEG), directly supporting the claim of generality.

2. **Strong and consistent empirical results** — Pretrained PopT substantially outperforms all aggregation baselines (Linear, Deep NN, non-pretrained PopT) across all tasks and modalities. On the 4 iEEG tasks (Table 1), PopT+BrainBERT achieves ROC-AUC 0.69–0.89 vs. the best baseline range of 0.59–0.72. The improvements are systematic, not cherry-picked.

3. **Sample and compute efficiency convincingly demonstrated** — Fine-tuning the pretrained PopT reaches full baseline performance with fewer than 500 samples and converges in under 750 steps, while non-pretrained PopT requires up to 2k steps. This directly supports the paper's claim that modular pretraining reduces downstream resource needs.

4. **Rigorous ablation study** — Table 3 shows that removing position encoding, either loss component, or adding a reconstruction term all degrade performance, confirming that each design choice is necessary.

5. **Generalization to held-out subjects separately validated** — The leave-one-subject-out experiment (Figure 4, generalizability) shows minimal performance drop when a subject is entirely unseen during pretraining, directly supporting the claim of usefulness for new subjects.

6. **Novel interpretability methods** — The connectivity analysis (channel-masking degradation in the pretraining objective) and attention-based functional region identification are creative uses of the pretrained weights that go beyond standard decoding evaluations.

7. **Code and pretrained weights released** — This significantly increases the practical impact of the work.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguity in the main evaluation's train/test split regarding subject overlap** — The paper states (lines 127-128) that "Of the sessions, 19 are used for pretraining, and 7 of the sessions are held-out for evaluation" across 10 subjects. It does not clarify whether the held-out sessions come from the same subjects as the pretraining sessions or from entirely different subjects. If they are from the same subjects, the model could benefit from subject-specific patterns learned during pretraining, inflating the reported results relative to a true held-out-subject setting. The separate leave-one-subject-out experiment (Figure 4, lines 293-297) partially addresses this concern by showing minimal degradation when entire subjects are held out, which builds confidence that the core claim holds. However, the ambiguity in the main tables should be explicitly resolved — the authors should state whether subject overlap exists and report results both with and without it.

### Minor

- **End-to-end comparison is not perfectly controlled** — The paper compares PopT (which learns a transformer-based spatial aggregator) against Brant (iEEG) using only linear aggregation of Brant's outputs (line 145). The observed advantage could partly reflect the stronger aggregator rather than superior representations. The paper's main claims are about aggregation vs. aggregation baselines, where the comparison is well-controlled, but the "competitive with end-to-end" framing would benefit from acknowledging this asymmetry and ideally testing a controlled variant (e.g., PopT's aggregator on Brant's raw outputs, if feasible). The EEG comparison with BIOT/LaBraM values taken from original works (line 204) is transparently noted as such but shares the same limitation.

- **Connectivity and interpretability analyses are qualitative** — The connectivity analysis (Figure 5) is visually compared to cross-correlation maps but without a quantitative metric (e.g., correlation between the PopT-derived connectivity and traditional coherence across subjects). The paper notes that plots for all subjects are in the appendix (line 352), and the approach is presented as preliminary, but a quantitative validation would substantially strengthen this contribution.

- **Pretraining compute cost is not reported** — The paper emphasizes computational lightness (lines 31, 75, 400) but only quantifies fine-tuning steps (Figure 4, compute_efficiency). Reporting pretraining wall-clock time, FLOPs, or parameter count would make the claim concrete.

### Trivial

- **Transformer architecture hyperparameters** are deferred entirely to the appendix (line 91: "see \Cref{architectures}: Architectures"). A brief summary in the main text (e.g., number of layers, heads, hidden dimension) would aid readability and reproducibility assessment.
- **Subset selection for the ensemble-wise loss** is underspecified. The paper states subsets $S_A, S_B$ are disjoint (line 101) and that the number of channels varies during training (line 105), but does not describe whether subsets are randomly sampled, fixed per subject, or how subset size is chosen.

## Nice-to-Haves

- Adding a simple paired statistical test (e.g., Wilcoxon signed-rank across subjects comparing PopT vs. the best baseline) would strengthen confidence that improvements are significant despite between-subject variability.
- The scaling-with-subjects experiment (Figure 4, pretrain_scale) shows a clear trend but with 1–3 subjects the gains are noisy; more granular data points would strengthen the scaling claim.
- A quantitative validation of the connectivity analysis (e.g., correlation between PopT-derived degradation and cross-correlation/coherence across all subjects) would elevate the interpretability contribution.

## Removed Points

- **Criticism about connectivity being "only demonstrated on a single subject"** — The paper explicitly states "Plots for all test subjects can be seen in \Cref{sec:connectivity}" (line 352), referring to appendix figures (stripped by parser). The claim of single-subject demonstration is factually incorrect based on what is stated on the page.
- **Criticism about missing related works** — No external source is available to verify existence of missing works; this is excluded per guidelines.
- **Nitpicks about reproducibility (hyperparameters, implementation details)** — These concern appendix content stripped by the parser and are excluded per guidelines.
- **Criticism about formatting/style/deferred appendix content** — Removed as these are parser artifacts or standard practice.
- **Strength Finder's generic strengths** (e.g., "the paper addressed an important problem", "this paper addresses an important challenge") — These are generic/superficial and do not provide specific evidence; removed.
- **Weakness about non-pretrained PopT performing poorly** — This is a factual observation, not a weakness. The paper uses this comparison to demonstrate the value of pretraining, which is the intended framing.

## Novel Insights

The harsh critic's observation about the Brant comparison asymmetry is the most insightful point: the paper's comparisons against end-to-end models are not controlled for aggregator capacity. However, the critic's data-leakage concern is partially mitigated by the held-out-subject experiment already in the paper, which independently validates the generalization claim. The key novel synthesis across the reviews is that the paper's core strength — the modular design enabling efficient pretraining of spatial aggregation separate from temporal encoding — is well-supported by the controlled comparisons (PopT vs. Linear/Deep NN/non-pretrained PopT), while the secondary claim about being "competitive with end-to-end" is less tightly justified and would benefit from more controlled comparisons or explicit acknowledgment of the asymmetry.

## Suggestions

1. **Clarify the train/test session split** — Explicitly state whether the 7 held-out evaluation sessions are from the same subjects as the 19 pretraining sessions or from different subjects. If there is overlap, report results both with and without subject overlap.
2. **Add a controlled variant for the end-to-end comparison** — If feasible, test PopT's transformer aggregator on Brant's frozen raw channel outputs (without BrainBERT) to isolate whether the improvement comes from the aggregator or from the combined approach.
3. **Quantify the connectivity analysis** — Report a correlation metric (e.g., Spearman ρ) between PopT-derived channel-masking degradation and traditional cross-correlation/coherence across all subjects, rather than only a visual comparison.
4. **Report pretraining compute** — Include wall-clock time or FLOPs for the pretraining stage alongside the existing fine-tuning compute results.
5. **Briefly summarize transformer hyperparameters in the main text** — A single sentence (e.g., "6 layers, 8 heads, 512 hidden dim") would suffice.
6. **Specify the subset sampling procedure** — Describe how $S_A, S_B$ are selected and how subset sizes are varied during pretraining.
