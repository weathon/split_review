- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes JCPMH, a method for partial multi-modal hashing (MMH) that uses two "teacher" modules — an autoencoder (trained on fully-paired samples to capture global structural information via a GCN with a label-derived adjacency matrix) and a multi-label classification module (trained on all available samples, including partial ones, to capture discriminative information) — to jointly guide a generator that completes missing modalities before hash codes are learned. The approach is motivated by the observation that existing methods either waste partial data or fail to capture global cross-modal structure.

## Strengths

- **Well-motivated joint-guidance design.** The paper identifies two complementary weaknesses in prior work: (1) methods like NCH use only within-category neighbor information and discard discriminative signal across categories, and (2) methods process modalities separately, losing cross-modal global structure. JCPMH addresses both with separate modules. This framing is clear and the design follows naturally from it.

- **Ablation study confirms that both guidance modules contribute.** Table 3 compares JCPMH against JCPMH-A (no autoencoder) and JCPMH-B (no classifier). Both variants perform worse, especially JCPMH-A (image mAP drops from 0.801 to 0.773 on MIR Flickr and from 0.832 to 0.795 on NUS-WIDE at 32 bits). This provides direct evidence that the joint-guidance claim is not vacuous.

- **The classification module genuinely improves data utilization.** With 70% PDR, only 30% of samples are fully paired (usable by the autoencoder). The classification module additionally leverages the 70% partial samples for training. This is a concrete, well-explained advantage over methods like NCH that cannot use partial samples during training of the guidance module.

- **Consistent, if modest, improvements on the primary partial-retrieval task.** In Table 2, JCPMH outperforms NCH across all tested settings (partial training set, partial query set, both partial) and both datasets. On the most challenging setting (both sets at 70% PDR), the average improvement over NCH is about 1.37% mAP on NUS-WIDE and a similar margin on MIR Flickr. The improvement is consistent across hash code lengths, which supports the method's reliability.

- **Robustness to high PDR and hyperparameters.** Figure 3 shows JCPMH's mAP declines slowly as PDR increases from 10% to 90%, while baselines like GCIMH and SAPMH show more fluctuation. Figure 5 demonstrates that performance is stable across a range of λ₁ and λ₂ values.

## Weaknesses

### Fatal
None.

### Major

- **Asymmetric comparison in Table 1 inflates the claimed advantage over traditional MMH methods.** The paper states JCPMH "surpasses the best-performing traditional MMH model FGCMH by an average of 4.1%." But the experimental protocol is not symmetric: JCPMH (and other partial methods) were given 10% PDR (i.e., 10% of data are partial, providing additional training signal), while traditional methods like FGCMH were evaluated on fully-paired data only, because they cannot handle partial samples. JCPMH thus benefits from 10% more data. The paper is transparent about this design (Section 4.3, footnote in Table 1), but the headline claim against FGCMH is not attributable solely to the method's quality — it conflates the benefit of additional partial data with the benefit of the joint-guidance approach. This weakness specifically affects the 4.1% claim; the fairer comparison within the same treatment (JCPMH vs. NCH, both at PDR=10%) shows a much smaller 0.7% margin.

### Minor

- **Improvement over the strongest baseline (NCH) is modest and lacks significance testing.** The average gain over NCH in the primary partial-retrieval setting is ~1–2% mAP. While consistent, this margin is small enough that single-run evaluation on standard benchmarks raises a reasonable question about whether the improvement is statistically reliable. No confidence intervals, standard deviations, or multiple-run experiments are reported. This weakens the evidence for the core contribution. (Note: multi-run reporting is not standard practice in this subfield, so this is a limitation rather than a fatal flaw.)

- **Potential domain shift between autoencoder training and its use during generator training.** The autoencoder is trained exclusively on real fully-paired samples and its parameters are subsequently frozen (Algorithm 1, steps 7–9). It is then used to compute reconstruction loss ℒ₂ on *generated* samples. The paper does not discuss whether the autoencoder provides meaningful gradients for out-of-distribution generated data, nor whether fine-tuning it jointly with the generator would improve results. This is a methodological gap worth addressing.

- **Generator architecture details are deferred to the experimental settings section.** Section 3.5 introduces the generator only as "the cross-modal generator f_g(I_p; Θ_g)" without specifying that there are two separate MLPs (one per modality direction). The reader must wait until Section 4.2 to learn this. A method section should describe the architecture being proposed.

- **Training hyperparameters are incompletely specified.** Algorithm 1 references epochs T₁, T₂, T₃, but their specific values are never given. Learning rates, optimizer choice, and batch size are also absent. These details would be necessary for faithful reproduction.

### Trivial
- The paper states "As shwon in Figure.2" (typo: "shwon" → "shown") and "Grah Auto-encoder" in the Table 3 footnote.
- The generator is introduced with a single equation reference ("Eq.12" appearing mid-sentence on line 148 with no accompanying description before appearing again).

## Nice-to-Haves
- An analysis of computational cost (training time, inference speed) would provide useful context.
- A discussion of limitations (e.g., reliance on clean label information for the adjacency matrix, scalability of two-stage training, sensitivity to label noise) would strengthen the paper's positioning.

## Removed Points

These points were raised by reviewers but are removed or demoted after cross-checking against the paper:

1. **"No comparison with ICDR-DCT"** — Removed per rule: DO NOT mention missing related works, as you cannot confirm their existence from external sources.

2. **"Source of baseline results not specified"** — Removed per rule about reproducibility nitpicks. The paper names the baselines; it is standard practice in this field to report numbers from original papers or reproduce them. This criticism lacks specific evidence of unfairness.

3. **"No discussion of limitations"** — Moved to Nice-to-Haves. This is a valid suggestion but not a weakness in the paper's technical content.

4. **"Qualitative t-SNE evidence is subjective"** — While true, this applies to all t-SNE visualizations in the literature. The visualization is presented as supporting evidence, not as a primary claim. Kept implicitly but not elevated as a separate weakness.

5. **Strength: "Strong performance even on complete data" / "Strong empirical gains"** — Dropped because: (a) the "complete data" strength (Table 1, 4.1% over FGCMH) conflicts with the verified major weakness about asymmetric comparison; (b) "strong gains" (referring to the ~1.37% improvement) conflicts with the verified minor weakness about modest margins without significance testing. Per rules, when strength and weakness disagree, the weakness wins.

6. **"No confidence intervals or significance tests"** — Kept as a minor weakness (it is a reasonable concern) but downgraded from the critic's framing because single-run evaluation is standard for benchmark retrieval tasks in this community, making it a limitation rather than a critical flaw.

7. **"Generator takes only partial modality I_p as input, unclear how two directions are handled"** — The experimental settings section states "we designed two MLPs as generators. Each takes one modality… as input and generates the other modality." So this is addressed, albeit in the wrong section. Kept as a minor weakness about placement rather than missing information.

## Novel Insights

None beyond the paper's own contributions. The two reviews did not surface any non-obvious observation about the method that the authors themselves had missed.

## Suggestions

1. **Fix the Table 1 comparison.** Either (a) report results for all methods on truly fully-paired data (JCPMH without its generator, i.e., using only the hashing network), or (b) add a second row where the comparison is restricted only to methods that received the same PDR=10% treatment, and clearly separate the claim about beating FGCMH from the claim about beating NCH under equal conditions. The current framing conflates two different experimental settings.

2. **Add significance-aware reporting.** Run the main partial-retrieval experiments (Table 2) at least 3 times with different random seeds and report mean ± std. This is especially important given the small margins over NCH.

3. **Analyze the domain shift issue.** Either fine-tune the autoencoder jointly with the generator and compare, or provide analysis showing that the reconstruction loss on generated samples correlates with meaningful completion quality.

4. **Move generator architecture details to Section 3.5.** State explicitly that two separate MLP generators are used (one for each missing-modality direction) rather than deferring this to the experimental settings.

5. **Disclose the epoch numbers T₁, T₂, T₃, learning rate, optimizer, and batch size** for reproducibility.
