Here is my final consolidated review.

---

## Summary

The paper proposes COPER (COrrelation-based PERmutations), an end-to-end deep multi-view clustering framework. The core idea is to learn shared representations via autoencoders with a CCA-based correlation objective, predict pseudo-labels via a clustering head, and then randomly permute samples within the same pseudo-label cluster across views to make the CCA-based embeddings more cluster-discriminative. The authors theoretically relate their permutation-based CCA to linear discriminant analysis (LDA) and evaluate on ten MVC benchmarks.

## Strengths

- **Novel permutation-based CCA objective for MVC.** The idea of using within-cluster pseudo-label permutations to make CCA embeddings cluster-friendly is genuinely novel within the deep MVC literature. This goes beyond standard two-stage pipelines and connects representation learning to clustering in a non-trivial way.

- **Consistently strong empirical results on ACC and ARI across 10 datasets.** In Table 1, COPER outperforms both deep MVC competitors (DSMVC, CVCL) and two-stage baselines on Accuracy and Adjusted Rand Index across all ten datasets, with improvements reaching ~14% on some benchmarks (e.g., MSRVC1 ACC: 89.14 vs. 77.90). The results are reported as mean ± std over 10 runs, which provides more information than single-run reporting.

- **Principled multi-view pseudo-labeling procedure with cross-view consistency filtering.** Section 3.4 describes a thoughtful pipeline: selecting confident samples via argtop-K, computing cluster centers, filtering by cosine similarity with a threshold λ, and removing samples with inconsistent labels across views. This directly addresses the challenge of obtaining clean pseudo-labels for self-supervision in multi-view settings.

- **Controlled case study (F-MNIST) that empirically validates the theoretical claims.** Section 4.4 demonstrates that supervised and pseudo-label-based permutations increase ARI, reduce the eigenvalue gap to the LDA solution, and decrease inter-class correlation. This provides real (if synthetic) evidence for the core mechanism.

## Weaknesses

### Fatal
None.

### Major

- **Asymmetric comparison with deep MVC baselines undermines confidence in the claimed state-of-the-art performance.** The paper reports its own results as mean ± std over 10 runs, while the two main deep MVC competitors (DSMVC, CVCL) are reported as best-over-runs from their original papers (acknowledged in lines 296–298). Comparing a central tendency against a maximum can inflate the apparent margin. On several datasets the improvement over CVCL is within one standard deviation (e.g., Scene15 ACC: COPER 40.68±1.6 vs. CVCL 40.16±1.8; CCV NMI: COPER 26.32±0.7 vs. CVCL 26.25±0.9). The authors themselves note that they "report the mean over ten runs while [the baselines] report the best result," but then still claim superiority without an apples-to-apples comparison or re-running the baselines. This is the single most significant weakness.

- **Ablation study contains a likely data error.** In Table 2 (line 373), the "COPER w/o permutations" row reports NMI = 22.41±31.3.1 — the standard deviation has a malformed value ("31.3.1" with two decimal points) that is also larger than the mean for a bounded metric. Moreover, the NMI value 22.41 is identical to the ARI value 22.41 to two decimal places, which is highly improbable and suggests a copy-paste or reporting error. The AE-only baseline achieves NMI = 27.34, meaning "COPER w/o permutations" (which still has the clustering head and correlation loss) would be substantially worse than a plain autoencoder on NMI while improving on ACC (45.82 vs. 38.92). This inconsistency prevents reliable interpretation of the ablation.

- **Critical hyperparameters and experimental details are missing, harming reproducibility.** The pseudo-label threshold λ and the permuted-correlation weight β are mentioned (lines 150, 181) but no values are reported. Batch size, learning rate, optimizer, number of layers, hidden dimensions, and activation functions for the autoencoders are not specified. A reader cannot reproduce the experiments from the paper as presented.

### Minor

- **Only two deep MVC baselines are compared (DSMVC, CVCL).** Several other end-to-end deep MVC methods are cited in the introduction (e.g., Tang et al. 2022 already included as DSMVC; Chen et al. 2020, Chen et al. 2023 already included as CVCL — these are the two primary ones). Still, the set of deep competitors is thin. Including additional end-to-end methods would strengthen the evaluation.

- **Theoretical contribution is heavily reliant on prior work.** Proposition 1 claims that CCA with inter-cluster permutations converges to LDA, but the proof is deferred entirely to Kurşun et al. (2011) without adaptation to the multi-view pseudo-label setting. The error bound in Eq. (6) (line 246) is a standard eigenvalue perturbation inequality with no structural connection to the specific noise induced by false pseudo-labels. The theoretical sections motivate the approach but do not constitute a novel theoretical result.

- **Dataset characteristics (sample counts, feature dimensions, number of views, number of clusters) are not reported.** Section 5 simply names ten datasets without any summary table. This information is essential for assessing the breadth and difficulty of the evaluation.

### Trivial

- The NMI standard deviation entry "31.3.1" in Table 2 is a formatting artifact (likely a LaTeX rendering issue with the original value). This should be corrected.

## Nice-to-Haves

- A step-by-step worked example of the permutation procedure with concrete indices (e.g., 3 samples in a cluster, showing how indices are permuted per view and how the correlation loss is then computed) would eliminate residual ambiguity for readers.
- An ablation isolating the effect of the permutation term more cleanly: (a) full COPER, (b) COPER with correlation loss only on original data (no permutations), (c) COPER with random (non-cluster-aware) permutations. This would directly test whether cluster-aware permutations drive the gain.
- Reporting best-over-runs for COPER alongside the mean±std (or re-running baselines to obtain mean±std) would resolve the asymmetric comparison concern entirely.
- t-SNE visualizations of the learned embeddings for COPER versus baselines would strengthen the qualitative story.

## Removed Points

The following points from the reviewers are removed with justification:

1. **"Core permutation mechanism is under-specified"** — Removed after verification. Definition 1 (lines 164–169) states that "a random permutation for each view is defined" and applied to indices within the same pseudo-label cluster to "create a new artificial correspondence between views." The description, while concise, adequately specifies that (i) permutations are applied independently per view, (ii) they replace the original cross-view correspondence, and (iii) the permuted pairs are then used for the correlation loss (line 171). A worked example would help but the mechanism is not under-specified to the point of being non-reproducible.

2. **"Two-stage baselines (Raw, PCA, CCA, AE, DCCA-AE) are weak and inflate the apparent margin"** — Removed. These are standard baselines in the MVC literature. They serve as lower-bound references; the primary comparison is against the deep MVC methods (DSMVC, CVCL). Using these common baselines does not "inflate" anything.

3. **"Figures 2 and 3 are referenced but not included"** — Removed. These are figures (images) stripped during PDF-to-text extraction; they exist in the original submission.

4. **"Missing related works"** — Removed per policy: I cannot verify missing citations without external knowledge. The paper covers the relevant thread (DCCA-based MVC, pseudo-labeling, CCA-LDA connection).

5. **All formatting, typo, and grammar nitpicks** — Removed as parser artifacts or out of scope.

6. **Generic "evaluation lacks rigor" / "statistical tests missing" complaints without specific anchor** — The specific asymmetric-comparison criticism is kept; the broader "lacks rigor" framing is removed.

7. **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") — Removed as insufficiently specific.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight that the authors themselves missed or that reframes the contribution in a new light.

## Suggestions

1. **Fix the evaluation comparison.** The cleanest solution is to obtain the code for DSMVC and CVCL (or use the authors' own implementations) and re-run them 10 times to report mean±std. Alternatively, report best-over-runs for COPER alongside the mean±std for an apples-to-apples comparison. Without this, the central claim of "state-of-the-art" is not fully supported.

2. **Correct the ablation table (Table 2).** The NMI value (22.41) and its standard deviation (malformed) for "COPER w/o permutations" need verification. If the value is erroneous, correct it. If it is correct, explain why removing permutations causes NMI to drop below the AE-only baseline while ACC improves — this warrants discussion.

3. **Report all hyperparameters.** Provide a table listing λ, β, batch size, learning rate, optimizer, network architectures (layers, hidden dimensions), and the number of training epochs for each dataset.

4. **Add a dataset characteristics table** listing the number of samples, feature dimensions per view, number of views, and number of clusters for all ten datasets.

5. **Strengthen the theoretical section** by connecting the perturbation bound (Eq. 6) to the actual structure of pseudo-label noise — e.g., show how the filtration procedure (threshold λ, cosine similarity) controls the norm of D.

## Score and Decision

The paper introduces a genuinely interesting idea and achieves promising empirical results across diverse benchmarks. However, the asymmetric evaluation comparison (mean vs. best) weakens confidence in the claimed state-of-the-art performance, and the ablation table contains a likely data error that undermines the ablation study's reliability. Missing hyperparameters further limit reproducibility. These issues are addressable in a revision, but in its current form the evidence does not fully support the paper's central claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>