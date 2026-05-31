## Summary
The paper proposes the Normalized Matching Transformer (NMT) for sparse keypoint matching. It combines a Swin-L backbone, SplineCNN for geometric feature refinement, a normalized transformer (nGPT) that enforces unit-norm embeddings at every layer, and training with InfoNCE and hyperspherical uniformity losses. The method achieves state-of-the-art results on PascalVOC and SPair-71k, with reported improvements of 5.1% and 2.2% over baselines, while converging in fewer epochs.

## Strengths
- **Strong empirical results**: The method achieves high matching accuracy on two challenging datasets, outperforming several prior methods by nontrivial margins.
- **Ablation study**: The ablation in Table 4 isolates the contribution of each component (backbone, transformer type, losses, augmentations), giving insight into what drives performance.
- **Practical convergence speed**: The claim of requiring at least 1.7× fewer epochs to converge, if validated, is practically important for reducing training cost.
- **Clean exposition of architecture**: The pipeline is described step-by-step with pseudocode and clear figures, making it easy to understand the flow.

## Weaknesses
### Fatal
- **Missing justification for image-level augmentations**: The paper uses Mixup, Cutmix, and Random Erasing. These are strong image-level augmentations that alter image content. For keypoint matching, Mixup blends two images, and Cutmix replaces patches from another image, which can destroy keypoint locations or create ambiguous correspondences. The paper does not explain how keypoint labels are handled under these augmentations. If the augmentations are applied naively, the ground-truth correspondences become incorrect, invalidating training and results. This is a critical oversight.

### Major
- **Inconsistent and incomplete baseline comparison**: The paper claims to outperform BBGM, ASAR, COMMON, and GMTR by explicit margins (5.1% and 2.2%). However, the PascalVOC results table (Table 2) does not show numbers for these four methods; instead it lists many older baselines (e.g., GMM-PL, PAA, GLM-NE, CE, HBGM) and two entries with constant 75.2% (CGMPT and COMMON) that seem anomalous. The SPair-71k table (Table 3) lists DMG, BIGM, CMTR, and COMMON, but not BBGM or ASAR. The naming of baselines is inconsistent (e.g., COMMON is cited as Liu et al. 2020 in one place and Lin et al. 2023 in the text; GMTR is called CMTR in Table 3). The claimed improvements cannot be verified from the reported tables, and the paper does not provide a fair side-by-side comparison with the stated SOTA methods.
- **Limited novelty**: The paper combines existing components (Swin backbone, SplineCNN, nGPT, InfoNCE, hyperspherical loss) without introducing a new fundamental idea. The main novelty is the specific integration and the layer-wise hyperspherical loss, but the ablation shows only a 0.8% drop without the layer loss, which is modest. The normalized transformer itself is taken directly from Loshchilov et al. (2024). The paper would benefit from deeper analysis or comparison to simpler baselines with the same backbone.
- **Loss formulation ambiguity**: Equation (3) for the hyperspherical loss is imprecisely written: it sums over \(j\) but uses an undefined index \(i\). The intended meaning is likely \(\sum_{i=1}^m \max_{j\neq i} C_{ij}\). The paper also does not clarify why the InfoNCE and hyperspherical losses are summed without weighting, despite the hyperspherical loss being applied per layer with a progressive weight.

### Minor
- **Sinkhorn as a combinatorial subroutine**: The paper claims no combinatorial subroutines are needed, yet during inference a Sinkhorn algorithm is applied to produce a doubly-stochastic matching matrix. Sinkhorn is a differentiable linear-assignment approximation and is itself a combinatorial subroutine. The claim is misleading.
- **Reference and citation errors**: There are several inconsistencies in reference years and author names (e.g., COMMON attributed to Liu et al. 2020 vs. Lin et al. 2023; Mettes et al. (2019) appears as Melekhov et al. 2019 in the reference list). These do not affect the technical content but reduce clarity.
- **Training speed claim**: The paper mentions faster convergence in epochs but acknowledges that the normalized transformer is slower per epoch due to kernel fusion. The potential wall-clock time savings are not quantitatively demonstrated, weakening the practical advantage claim.

### Trivial
- The use of Greek letters and icons for class labels in Tables 2 and 3 makes the tables harder to parse quickly.

## Nice-to-Haves
- A direct comparison with BBGM, ASAR, COMMON, and GMTR in a single table, with the same evaluation protocol, would greatly strengthen the paper.
- Clarifying how keypoint annotations are treated under Mixup/Cutmix is essential for reproducibility.
- Providing per-class results on SPair-71k for the missing baselines (BBGM, ASAR) would help contextualize the improvements.

## Novel Insights
None beyond the paper’s own contributions. The paper demonstrates that combining a strong backbone, normalized transformer, and hyperspherical losses works well empirically, but does not offer a new theoretical understanding of why this combination is effective.

## Suggestions
- Add an explanation of how keypoint labels are handled when using Mixup, Cutmix, and Random Erasing. Provide evidence that the augmentations preserve or correctly transform correspondences, or run an ablation without these augmentations to show they are not harmful.
- Update the baseline tables to include direct comparisons with BBGM, ASAR, COMMON, and GMTR on both datasets. Remove or correct anomalous constant entries (e.g., CGMPT and COMMON in Table 2).
- Clarify the loss equations and weighting scheme.
- Consider including wall-clock training time comparison to substantiate the faster convergence claim.
- Fix citation inconsistencies and class labeling in tables for readability.

## Score and Decision
The paper presents a competitive method for sparse keypoint matching, but the lack of clarity on whether the strong image-level augmentations are applied in a valid manner for keypoint data is a critical concern that undermines the credibility of the results. Additionally, the baseline comparison is incomplete and inconsistent, making it difficult to verify the claimed state-of-the-art margins. These issues outweigh the positive empirical performance.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>