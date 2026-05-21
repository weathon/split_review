---
job_id: 8e89dabb-1be5-4319-867b-11c7dbe6bcf0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 2cq8FyBfDk.pdf
paper: ProteinVista: A Compute-Efficient Atom-Level 3D CNN That Outperforms Sequence Transformers in Protein–Ligand Prediction
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it proposes a learned 3D structural representation model for proteins and studies self-supervised pretraining, multimodal alignment, and downstream prediction in biology.

## Minimum Quality
Pass ✅. The submission contains an abstract, introduction with related-work positioning, methodology, experiments with quantitative results, and discussion/conclusion; while I have substantial concerns about novelty, formulation details, and experimental support, these do not rise to the level of a desk reject based on the paper text alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes ProteinVista, a full-atom 3D CNN that voxelizes protein heavy atoms into multi-channel grids, uses geometric augmentation for rotation robustness, and is pre-trained on AlphaFold structures using either Rosetta-score regression or contrastive alignment to ESM-2 embeddings. The model is then fine-tuned on enzyme-substrate prediction, transporter-substrate prediction, drug-target \(\mathrm{IC}_{50}\) regression, and GO term prediction, with comparisons mainly against ESM-2 baselines and simple ESM-2/ProteinVista ensembles. The paper argues that atom-level volumetric structure encoders can be compute-efficient and can outperform sequence transformers on structure-sensitive tasks.

## Strengths
The paper asks a relevant question for representation learning in biology, namely whether explicit atom-level 3D structure can provide an advantage over large sequence-only protein language models on tasks that plausibly depend on local geometry and chemistry.

The empirical scope is broader than many submissions in this area. The authors evaluate on three protein-ligand related benchmarks plus one GO benchmark, and this gives a reasonably coherent picture: the structural model helps more on tasks where pocket geometry should matter and helps less on homology-driven GO prediction. That pattern is plausible and scientifically interesting.

I appreciated that the paper does not only report wins, but also includes a case where ProteinVista underperforms ESM-2, namely molecular-function GO prediction in Section 3.4. That increases credibility relative to papers that only select favorable tasks.

The compute discussion is useful. **Figure 3** and the associated text on Pages 7 to 9 present parameter count, FLOPs, runtime, and storage trade-offs in a way that is easy to understand. In particular, **Figure 3(c)** supports the claim that the CNN is much faster in wall-clock processing per 1000 proteins than the ESM-2 baselines, despite not being the lightest model in FLOPs, which is a practically relevant point.

The complementarity story is reasonably supported by the results. In **Table 1**, the simple ESM-ProteinVista ensemble improves over either single encoder on TSP and ESP, and **Figure 2(a,b)** further shows that the ensemble tends to dominate across bins of sequence identity and TM-score. Even though the mechanistic interpretation remains somewhat speculative, this is one of the cleaner parts of the paper.

The ablation section is directionally useful. **Figure 2(e)** suggests that test-time augmentation matters materially, while pretraining objective and voxel resolution have smaller but nonzero effects. That at least shows the model is not entirely insensitive to the proposed design choices.

Presentation is generally readable. The high-level workflow in **Figure 1** is clear and helps the reader follow the pipeline from PDB voxelization to CNN encoding to contrastive pretraining.

## Weaknesses
1. **The main novelty claim is overstated, and the paper is insufficiently positioned against prior voxel-based 3D CNN work.**  
   The central pitch, full-atom voxelization plus a 3D CNN with augmentation for protein structure tasks, reads much more like scaling and repackaging an established paradigm than introducing a new modeling idea. The introduction itself cites several earlier 3D CNN protein papers, including DeepSite, EnzyNet, 3DCNN_MQA, and related local-grid methods on Pages 1 to 2, which already weakens the novelty framing. Yet the paper repeatedly uses strong wording such as "the first compute-efficient full-atom 3D CNN" on Page 2 without a careful definition of what exactly is first here: first full-protein rather than local pocket, first large-scale-pretrained, first on AlphaFoldDB, or first competitive with ESM-2? These are not interchangeable claims. This matters because the paper’s contribution then hinges on whether the advance is methodological or primarily an empirical scaling study. As written, the positioning feels slippery.

2. **The experimental comparison is too narrow for the paper’s strongest claims.**  
   The abstract and conclusion claim that full-atom 3D CNNs are superior to sequence transformers for structure-dependent tasks, but the direct head-to-head comparisons in **Table 1** and **Table 2** are almost entirely against ESM-2 variants. There is very little comparison to modern structure-aware baselines, such as graph-based or equivariant protein encoders, even though the introduction explicitly discusses DeepFRI, GearNet, ESM-GearNet, and GPS-Fun on Pages 1 to 2. If the paper’s thesis is really about the value of atom-level 3D structure versus residue-graph abstractions, then omitting strong structure-based baselines is a serious gap. Right now the evidence only supports a narrower statement: this specific 3D CNN can outperform these specific sequence transformers on these tasks. It does not establish that 3D CNNs are the preferable structural modeling choice.

3. **The contrastive pretraining objective is mathematically underspecified, and there appears to be a notation error in the similarity matrix definition.**  
   In Section 2.3 on Page 4, the paper states: “for a mini-batch of \(n\) proteins we form the similarity matrix \(S\) with entries \(S_{ij}=\langle \mathbf{z}^{\text{PV}}_i,\mathbf{z}^{\text{ESM}}_i\rangle\).” This is almost surely wrong or at least inconsistent with the use of a full matrix, because the right-hand side does not depend on \(j\). If the intended definition is cross-modal all-pairs similarity, it should be \(S_{ij}=\langle \mathbf{z}^{\text{PV}}_i,\mathbf{z}^{\text{ESM}}_j\rangle\), perhaps after \(\ell_2\)-normalization if cosine similarity is intended. This is not a cosmetic typo, it is the core of the pretraining objective. Likewise, the paper does not state the exact symmetric InfoNCE formula, whether features are normalized, whether there are separate row/column cross-entropies, or how batch negatives are handled. Since the pretraining objective is one of the main technical contributions, this level of underspecification is a real problem.

4. **The voxel-density formulation is questionable and insufficiently justified.**  
   In Section 2.1 on Page 3, an atom contributes density \(\exp(-\|\vec v-\vec r\|/\sigma^2)\) with \(\sigma=1\). This is an unusual radial form. Many density-based voxelizations use a squared distance in the exponent, \(\exp(-\|\vec v-\vec r\|^2/(2\sigma^2))\), which has different smoothness and decay properties. The paper does not justify this choice, compare alternatives, or explain whether the resulting scale is calibrated across resolutions. Given that the whole representation begins with this density field, the omission matters. Also, the notation is dimensionally odd, since \(\|\vec v-\vec r\|\) has units of length while \(\sigma^2\) has units of length squared.

5. **Rotation handling is weak relative to the claims of “rotation-invariant” or “rotation-robust” representations.**  
   Section 2.4 on Page 4 uses only axis-aligned \(90^\circ\) rotations and mirror reflections, applied uniformly at random. This gives invariance only to a very small discrete subgroup of 3D transformations, not to arbitrary \(\mathrm{SO}(3)\) rotations. The paper should be much more careful here. In fact, the ablation in **Figure 2(e)** suggests that test-time averaging over multiple augmented views has a large effect, while removing augmentation during fine-tuning has almost no effect. That combination implies the model has not actually learned strong intrinsic rotation robustness, and still depends materially on augmentation at inference. This weakens one of the central methodological claims.

6. **The handling of large proteins via cropping is underdescribed and potentially harmful.**  
   Section 2.1 says that structures exceeding the \(160^3\) voxel grid are cropped at the bounding box. That single sentence hides an important design decision. How often does this happen? What fraction of atoms are dropped on average? Are the removed regions random, boundary-based, or centered in a fixed way after translation? For protein-ligand tasks, truncating distal regions may be harmless, but truncating the relevant pocket region could be catastrophic. Without reporting the prevalence and effect of cropping, it is hard to assess whether the method is robust or whether part of the benchmark was made artificially easy by dataset size distributions.

7. **The paper’s fairness claims around compute and data efficiency are not entirely clean.**  
   The paper repeatedly contrasts ProteinVista with ESM-2 in terms of using far fewer pretraining examples and GPU-hours. But the contrastive objective in Section 2.3 explicitly uses frozen ESM-2 embeddings as targets. So the method is not independent of large-scale sequence pretraining, it distills from it. This does not invalidate the model, but it changes the interpretation of the “two orders of magnitude less data” claim. ProteinVista is not learning from raw structures alone in its main setup, it is leaning on a representation already trained on hundreds of millions of sequences. The paper should acknowledge this more clearly; otherwise the efficiency comparison feels too self-congratulatory.

8. **The downstream training setup leaves important reproducibility and fairness details unclear.**  
   Section 3.1 on Pages 4 to 5 says the models were fine-tuned under “identical conditions” and that the optimal learning rate was searched, but it does not report the search space in the main text, the number of runs, whether early stopping was used, batch sizes, augmentation policies at train and test time for each task, or variance across random seeds. A few of these appear in the appendix for ESM-2, but the main paper asks the reader to accept fairly consequential comparisons without enough detail. This matters because some improvements in **Table 1** are modest, for example ProteinVista versus ESM-2\(_{650M}\) on TSP is a \(1.5\%\) accuracy gain and \(0.03\) MCC gain, while ESP is basically tied in accuracy and slightly worse in ROC-AUC and MCC. Without confidence intervals or multiple seeds, the strength of the conclusions is uncertain.

9. **Some table-based claims are stronger than what the tables actually show.**  
   The discussion around **Table 1** says ProteinVista “surpasses or equals” both ESM-2 baselines on both binary classification benchmarks. That is technically defensible metric by metric, but it glosses over a more mixed picture on ESP: ProteinVista matches accuracy, but is slightly below ESM-2\(_{650M}\) in ROC-AUC and MCC, and only clearly better in precision. This is not a decisive win. Similarly, **Table 2** is stronger, but only on one affinity benchmark and without comparison to structure-based affinity models. The paper’s rhetoric suggests a general result, while the tables support a narrower, task-specific one.

10. **The state-of-the-art comparison in Section 3.3 is not apples-to-apples enough.**  
    The “optimized pipeline” on Page 6 changes several things at once: joint tuning of small-molecule embeddings, extracting fine-tuned embeddings, training a separate contrastive network, and averaging predictions. This makes it difficult to attribute gains to the protein encoder rather than to the more elaborate downstream pipeline. Moreover, the comparisons to SPOT, ProSmith-ESP, and Fusion_ESP in **Table 1** are to systems that may differ in split protocol, features, and training recipe, yet the paper presents the numbers as a fairly direct state-of-the-art comparison. If the point is that ProteinVista is a strong encoder, the cleaner comparison is the controlled one against ESM-2 under identical heads. If the point is new state of the art, then the protocol differences need much tighter accounting.

11. **The analysis figures are interesting but the interpretations are somewhat overreaching.**  
    In **Figure 2(a,b)**, the ensemble tends to help across bins, but the number of examples per bin is encoded only by circle size and exact counts are not readable from the figure. It is hard to know whether some differences are based on large or tiny subsets. In **Figure 2(c)**, the conclusion that experimental structures could further improve performance is speculative; pLDDT is correlated with disorder and structural uncertainty, not just with prediction error in the narrow sense relevant to the downstream task. The figure supports that the model works better on high-confidence predicted structures, but not necessarily the broader causal interpretation.

12. **There are several small but nontrivial inconsistencies and sloppy details that undermine trust.**  
    On Page 8 the discussion says the Rosetta pretraining predicts 33 scores, whereas Section 2.3 and Table S2 indicate 23 retained targets after correlation filtering. Page 4 says the similarity matrix has entries \(S_{ij}\) but defines them using only index \(i\). Section 3.3 refers to “ProteinVista\(_{OP}\)” in prose while **Table 1** lists “ESM-ProteinVistaOP”. These are not fatal individually, but together they create the impression that the paper was not checked carefully enough in places where precision matters.

## Questions
1. In Section 2.3, is the intended similarity matrix
   \[
   S_{ij}=\langle \mathbf{z}^{\mathrm{PV}}_i,\mathbf{z}^{\mathrm{ESM}}_j\rangle
   \]
   rather than \(S_{ij}=\langle \mathbf{z}^{\mathrm{PV}}_i,\mathbf{z}^{\mathrm{ESM}}_i\rangle\)? Please provide the exact symmetric InfoNCE objective used in training, including whether embeddings are \(\ell_2\)-normalized and how the row-wise and column-wise losses are combined. Clarifying this would increase my confidence materially.

2. How often are proteins cropped because they exceed the \(160^3\) box, both in pretraining and in each downstream dataset? Please report the fraction of cropped examples and, ideally, an analysis of whether cropping affects accuracy. This is important because the method’s full-protein claim weakens if a nontrivial subset is truncated.

3. Can the authors provide comparisons against stronger structure-aware baselines, especially modern GNN or equivariant models, on at least one of the main benchmarks? Even a limited additional comparison would help establish whether the gains are due to atom-level volumetric encoding specifically, rather than simply using structure at all.

4. For **Table 1** and **Table 2**, please report variability across random seeds or confidence intervals. The paper uses significance tests in some cases, which is good, but seed variance for end-to-end training would help calibrate whether the observed gains are robust.

5. Why was the density kernel chosen as
   \[
   \exp(-\|\vec v-\vec r\|/\sigma^2)
   \]
   instead of a more standard Gaussian-like \(\exp(-\|\vec v-\vec r\|^2/(2\sigma^2))\)? If this was intentional, an ablation or justification would be useful.

6. The paper emphasizes rotation robustness, but training uses only axis-aligned \(90^\circ\) rotations and reflections. Did the authors test arbitrary 3D rotations at inference time, or compare against a broader augmentation distribution? This would clarify whether the model is genuinely robust beyond the discrete cube symmetries.

7. In **Figure 2(e)**, removing training augmentation has almost no effect, whereas reducing test-time views from 5 to 1 hurts substantially. Can the authors explain this asymmetry more carefully? It seems to suggest reliance on test-time augmentation rather than learned invariance.

8. For the state-of-the-art comparison in Section 3.3, can the authors clarify whether the external baseline numbers use exactly the same train/validation/test splits as this paper? If not, the claims should be softened.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard caveats for protein and drug-target prediction models. The paper does not present an immediate ethics issue that requires escalation based on the information in the manuscript.

## Soundness Rating
2: fair. The core empirical results are plausible and partially supported, but important methodological details are underspecified, the pretraining objective contains a likely notation error at its core, and the experimental support is not strong enough for several of the broader claims.

## Presentation Rating
3: good. The paper is generally readable and the high-level narrative is easy to follow, with helpful figures and tables, but there are enough inconsistencies, overclaims, and missing technical details that the presentation falls short of being truly polished.

## Contribution Rating
2: fair. There is some practical value in showing that a reasonably sized atom-level 3D CNN can be competitive on selected structure-sensitive tasks, but the conceptual advance over prior voxel-based 3D CNN work appears limited, and the paper does not do enough to establish superiority over stronger structure-aware alternatives.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
This is a competent and interesting empirical paper, and I do think the result that atom-level structural CNNs can compete with or beat sequence transformers on some tasks is worth knowing. However, for ICLR main track, I am not convinced the submission clears the bar on either methodological novelty or evidential strength. The paper overstates what has been established, underspecifies the main contrastive objective, and compares too narrowly against sequence baselines for the strongest claims it wants to make.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with representation learning and structure-based ML for biological data, and I checked the paper’s technical and empirical details carefully, but some benchmark-specific biological nuances could still be clarified by the authors.