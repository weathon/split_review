Now I have all information needed. Let me produce the final consolidated review.

## Summary

CEIR proposes a framework for unsupervised image representation learning that combines CLIP with a GPT-4-generated concept bottleneck and a VAE to produce low-dimensional, human-interpretable latent representations. The concept bottleneck projects images into a concept vector space (dimensions correspond to text concepts like "vehicle," "big cat"), and the VAE compresses these into a compact latent code that can be attributed back to concepts via integrated gradients. The paper reports state-of-the-art unsupervised clustering results on CIFAR-10, CIFAR-100, and STL-10, along with qualitative demonstrations of concept-level interpretability and open-world concept mining.

## Strengths

1. **Novel integration of concept bottlenecks into unsupervised representation learning.** CEIR bridges concept-based interpretability (CBM, LF-CBM) with unsupervised representation learning by using CLIP's multimodal alignment to supervise a concept projection layer without labels, and a VAE to learn compact latent codes that retain semantic structure. This pipeline is architecturally clean and the components fit together coherently.

2. **Competitive clustering and linear probing results across multiple backbones.** On CIFAR-10, CEIR (ViT-L/14) achieves 95.70% ACC and 90.08% NMI, outperforming raw CLIP (83.38% ACC, 83.67% NMI), TEMI (94.50% ACC, 88.60% NMI), and other prior methods by meaningful margins. On STL-10 it reaches 99.19% ACC. Linear probing (Table 3) shows CEIR retains most of CLIP's discriminative power (CIFAR-10: 97.19% vs. 98.11% for CLIP ViT-L/14) while adding interpretability.

3. **Principled post-hoc attribution via Integrated Gradients on the VAE encoder.** Section 3.4 formalizes a label-free attribution procedure that computes concept importance scores by applying Integrated Gradients to the VAE encoder with a zero baseline, producing weighted concept vectors. This provides a mathematically grounded mechanism for interpreting the latent representation.

4. **Automatic concept generation with GPT-4 and role-based prompting.** Section 3.1 describes a two-stage concept pool generation (querying + filtering) that replaces the manual concept annotations required by prior CBM methods, enabling the pipeline to work without supervised concept labels.

## Weaknesses

### Fatal
None.

### Major

1. **VAE training on the merged training+testing set weakens the unsupervised clustering comparison.** Line 114 states: "In our VAE model training, we merge training and testing sets." The concept projection layer also uses the test set for early stopping. This means the representation *h* used for clustering is learned with access to test images. While CEIR is marked with † in Table 2 (defined as "training procedure, including additional data"), key baselines such as SCAN and TEMI do **not** use test data during training (no † mark). The comparison with these methods is therefore asymmetrical in CEIR's favor. The concern is not that the results are meaningless — the VAE performs unsupervised reconstruction of concept vectors (no labels), and the gap over raw CLIP (e.g., 90.08 vs. 83.67 NMI on CIFAR-10 with ViT-L/14) is large — but the claim of "state-of-the-art unsupervised clustering" is weakened because the evaluation protocol does not follow standard unsupervised evaluation practice where the model never sees test data. An ablation training the VAE only on the training split is needed to disentangle the genuine contribution of the method from any benefit of seeing test data.

### Minor

2. **The cubed cosine-similarity loss (Eq. 1) is presented without motivation or ablation.** The loss in Eq. 1 raises both the normalized concept activations and the CLIP similarity scores to the third power before computing cosine similarity. No rationale is given for why cubing is preferable to standard cosine similarity, MSE, or other alternatives. Cubing amplifies large values and suppresses small ones, which is a non-obvious design choice. Without an ablation comparing the proposed loss against simpler alternatives, it is unclear whether this specific form is critical to performance or can be replaced.

3. **Interpretability is demonstrated only qualitatively.** Despite "Explainable" in the title and "allows interpretation" as a listed contribution, the evidence for interpretability is limited to alluvial diagrams (Figure 3) and word clouds (Figure 4). There are no quantitative faithfulness metrics (e.g., concept dropping, insertion/deletion tests, alignment with human judgments). The attribution pipeline (Integrated Gradients) is methodologically sound, but the paper does not validate that the resulting importance scores actually correspond to human-aligned concepts. A simple experiment — e.g., measuring agreement between top-*k* attributed concepts and ground-truth class descriptions — would substantially strengthen this claim.

4. **The "class-related concepts" added to the concept pool introduce potential weak supervision.** Section 3.1 notes the authors "modify the filtering stage by adding class-related concepts on purpose." While the paper states that ground-truth labels are inaccessible, adding class-specific terms to the concept set could steer the representation toward class-separating directions, which is a mild form of implicit supervision in what is presented as a purely unsupervised pipeline. The paper does not ablate this choice (e.g., by comparing against a concept pool that excludes class-specific terms).

### Trivial

- The VAE latent dimensionality *K* is not reported for any experiment, nor is there any sensitivity analysis of this hyperparameter.
- The concept pool size and filtering thresholds are not specified, making the concept generation stage difficult to reproduce.

## Nice-to-Haves

- A quantitative interpretability evaluation (e.g., concept faithfulness scores, human agreement study) would turn the qualitative demonstrations into validated claims.
- An ablation of the cubed loss vs. standard cosine similarity or MSE would clarify whether the specific form matters.
- Reporting computational cost (training time, inference overhead) would help practitioners assess the trade-off.

## Removed Points

- The harsh critic's claim that "ProPos, SPICE do **not** use test data during training" is factually incorrect — both are marked with † in Table 2, indicating they do use additional/test data. However, this does not affect the valid concern about SCAN and TEMI (which are unmarked).
- The claim that "the reported comparisons invalid on their face" and "the claimed SOTA is not credible" is an overstatement. The comparison is weakened but not invalidated — the VAE is unsupervised (reconstruction of concept vectors), and the gap over raw CLIP (which also uses only K-means on test-set features) is large enough that it cannot be explained solely by test-set leakage.
- The critic's "novelty is incremental" observation is a qualitative opinion about contribution size, not a specific weakness, and conflicts with the paper's demonstrated novel integration.
- The demand for user studies and TCAV-style quantitative interpretability evaluation sets a bar not standard for all papers with interpretability components — qualitative demonstrations with methodologically sound attribution are a reasonable starting point.

## Novel Insights

The key insight of the paper — that concept bottlenecks trained via CLIP similarity can serve as an intermediate representation that is both semantically rich and compressible via VAE into a compact, interpretable code — is itself the main contribution. The reviews do not surface an alternative synthesis beyond what the paper already articulates. The test-set leakage concern is the single most important point the authors must address in any revision, but it does not reveal an entirely new perspective on the method.

## Suggestions

1. **Retrain the VAE using only the training set and report the resulting clustering results.** Even if performance drops modestly, doing so would cleanly separate the method's contribution from any test-data benefit and restore the credibility of the SOTA claims.
2. **Add a brief justification or ablation for the cubed loss** (Eq. 1). If the cubed form is critical, explain why; if not, replace with standard cosine similarity.
3. **Include a simple quantitative interpretability evaluation.** For example: for images in the test set, measure the overlap between the top-*k* attributed concepts and human-written class descriptions, or compare concept importance scores against a simple baseline (e.g., random concept assignment).
4. **Ablate the effect of including class-related concepts** by comparing a concept pool with and without class-specific terms.

## Score and Decision

**Score:** 5.5  
**Decision:** Borderline — the paper has a genuine contribution (integrating concept bottlenecks into unsupervised representation learning with interpretable outputs) and strong quantitative results, but the test-set contamination during VAE training is a significant methodological weakness that undermines the clean "unsupervised" framing. The core idea is promising and the results are likely meaningful, but the evaluation protocol needs to be fixed before the SOTA claims can be fully trusted.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>