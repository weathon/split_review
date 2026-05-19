- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6
Now I have a complete picture of the paper. Let me produce the final consolidated review.

## Summary

The paper proposes Neural Manifold Regularization (NMR), a contrastive learning method that embeds neural population activity into a 2D latent space and regularizes the manifold using distances and densities of continuous movement labels. NMR pulls embeddings together when their movement labels are close and pushes them apart when labels are distant, with extra force on infrequent labels to prevent collapse. The method is evaluated across 68 sessions spanning four neural modalities (M1, PMd, S1, human precentral gyrus), three hand-movement tasks (stereotyped center-out reaching, grid-based natural reaching, free-form natural reaching), and attempted handwriting in a paralyzed patient. Reported improvements over CEBRA and pi-VAE are large (50%+ in explained variance on center-out reaching), and cross-session/ cross-subject decoding with a linear decoder shows unusually strong generalization.

## Strengths

1. **Large, statistically significant improvements across diverse neural recordings**: On center-out reaching (M1 and PMd), NMR achieves median explained variances of 0.88 and 0.90, versus 0.48/0.53 for CEBRA and 0.43/0.37 for pi-VAE (Section 4.1, Fig. 2). All differences are significant (paired t-tests, p < 10⁻⁶ with multiple comparison correction). Similar margins hold for natural grid-based movements (0.82 vs 0.55 vs 0.45, Section 4.4) and free-form natural movements (0.79 vs 0.58 vs 0.56, Section 4.4, Fig. 6c).

2. **Cross-session and cross-subject decoding with a simple linear decoder**: NMR achieves nearly double the cross-session decoded variance of CEBRA (t=18.5, p=1.5e-47) and six times that of pi-VAE (t=21, p=1.4e-55) on M1 data (Section 4.2, Fig. 3). This directly demonstrates that the extracted manifolds are consistent across sessions, enabling robust decoding without per-session retraining — a practical advantage for BMI.

3. **Successful decoding of attempted handwriting in a paralyzed human**: NMR reveals single-trial 2D latent dynamics for 16-direction attempted handwriting without overlap for trials spaced 22.5° apart, with trial-averaged dynamics achieving r²=0.96 against imagined movement trajectories (Section 4.5, Fig. 7b). This demonstrates the method works even when no measurable hand position exists.

4. **Consistently lower variability across sessions and runs**: NMR shows standard deviation of 0.03 (M1) and 0.02 (PMd) across sessions, versus 0.10/0.06 for CEBRA and 0.18/0.18 for pi-VAE (Section 4.1). In natural movements, NMR variability across 20 runs is 0.002 vs 0.004 (CEBRA) and 0.117 (pi-VAE) (Section 4.4, Fig. 6c). This stability is a practical advantage.

5. **Works across signal types beyond single units**: NMR significantly outperforms CEBRA on LFP signals (LMP: 0.79 vs 0.46, Gamma: 0.74 vs 0.44, Beta: 0.36 vs 0.22, all p<0.002, Section 4.3) and on unsorted events (0.65 vs 0.36, Section 4.4, Fig. 5e), extending applicability beyond sorted single-neuron data.

6. **Shorter execution time than CEBRA**: NMR is significantly faster (119 vs 163 seconds for single units, t=12, p=3e-14; 146 vs 165 seconds for free movements, t=3.5, p=0.0025) (Section 4.4).

## Weaknesses

### Fatal
None.

### Major

1. **No ablation studies**: NMR has at least three distinctive components: (i) prediction-based positive/negative pair selection (using a learned linear regression head to filter pairs instead of using ground-truth labels directly), (ii) distance-weighted contrastive loss with frequency-dependent weighting for infrequent labels, and (iii) a threshold for classifying samples as positive, negative, or discarded. None of these are ablated. Without ablations, it is impossible to determine which component drives the reported improvements, whether simpler variants would suffice, or how sensitive the method is to its threshold. This undermines the scientific contribution — we learn that "NMR works" but not *why* it works. Given that the paper is positioned as introducing a new method, this is the most significant weakness.

2. **Method description lacks formal specification**: The method section (Section 3.3) describes the approach narratively — how predicted labels from linear regression are used to classify samples as positive/negative/discarded — but does not provide a formal loss function equation, pseudocode, or algorithmic specification. The description is incomplete: the sentence breaks off mid-flow ("Although our initial...") and key details (exact loss function, how the threshold is set, how frequency weighting is implemented mathematically) are absent from the extracted text. Even accounting for parser losses (sections 3.1, 3.2), a method paper's central contribution must be defined in a reproducible form. This is a barrier to understanding and building on the work.

### Minor

1. **Hyperparameter tuning protocol for baselines is under-specified**: The paper states for the center-out task that "The best hyperparameters were chosen when evaluating the CEBRA and pi-VAE models. Model parameters were kept fixed across all 28 sessions" (Section 4.1, Fig. 2 caption). It does not clarify whether baseline hyperparameters were tuned per-session or once across all sessions, nor report the search space. If baselines received per-session tuning while NMR used fixed parameters, the comparison is asymmetric (though it would make NMR's result more, not less, impressive). For natural movements (Section 4.4), the paper notes "Hyperparameter tuning across all 37 sessions for all three models," suggesting NMR also received tuning there, but the protocol remains vague. This should be clarified.

2. **Evaluation metric and data-splitting protocol not specified in main text**: The paper consistently reports explained variance (r²) and mentions "test trials" across multiple sections (Figs. 19, 21, 23) but does not describe the train/validation/test split procedure, whether explained variance is computed on held-out data, or how the linear decoder is trained relative to the embedding model. While the references to figures (likely in appendix) suggest this information exists, it should be stated in the main text for self-contained evaluation.

3. **"Over 50% improvement" claim is vague**: The abstract states NMR "outperformed other dimensionality reduction methods by over 50% across 68 sessions," but the main text only compares to two baselines (CEBRA and pi-VAE), and the 50% figure appears to be relative to CEBRA on some tasks but not others. On natural grid-based movements, the improvement over CEBRA is ~49%, and on free-form movements it's ~36%. The claim should be more precise about which comparison and which metric is being referenced.

### Trivial
- The paper references many figures (e.g., Figs. 12–14, 17–23) that are not included in the extracted text (likely appendix figures).
- Section numbering jumps from 4.2 to 4.5 (sections 4.3 and 4.4 exist in content but are not labeled with \section in the extraction).

## Nice-to-Haves
- An analysis of the learned latent space geometry (e.g., global vs. local structure preservation, topological similarity to the movement trajectory) would strengthen the claim that the manifold is "aligned."
- Reporting the dimensionality of raw neural input and number of training samples per session would help assess the difficulty of the dimensionality reduction problem.
- The paper acknowledges that NMR fails on complex handwriting characters (e.g., "m" or "k") and suggests geodesic distance as a future direction — this is honest but also indicates a meaningful limitation that could be discussed more thoroughly.

## Removed Points
These points were flagged by reviewers but removed after verification:
- **Missing related work section (Section 2)**: The extracted text shows the Section 2 heading with no body text. This is a PDF parsing artifact; the original submission contains the section. Removed per parser-issue rule.
- **Missing method subsections 3.1/3.2**: Similarly a parser issue — the original submission contains these sections. Removed per parser-issue rule.
- **Code availability**: The paper states "Our code is uploaded." This is sufficient for a submission. Removed.
- **Speculative fatal claim**: The harsh critic labels the method description issue as "critical structural flaw" and "barrier to acceptance." While the method description is incomplete in the extraction, sections 3.1/3.2 are parser losses, and Section 3.3 provides the algorithmic idea even without formal equations. This does not rise to "fatal" — it is a major but addressable weakness.
- **Unfair comparison / baseline advantage concern**: The critic suggests baselines may have been per-session tuned while NMR was fixed, giving baselines an advantage. If anything, this asymmetry would *favor* the baselines, making NMR's superior performance more compelling. The concern is about missing details, not unfairness. Downgraded to minor.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface an independent perspective on the work that the paper itself does not already articulate.

## Suggestions
1. **Add ablation studies** isolating each component of NMR: (i) prediction-based vs. ground-truth-based pair selection, (ii) with vs. without frequency weighting, (iii) threshold sensitivity analysis, on at least one representative dataset (e.g., M1 center-out). This is the single most important addition for establishing *why* NMR works.
2. **Provide a formal definition of the NMR loss function** — include the equation, describe the threshold and pair-construction rule mathematically, and specify the frequency-weighting mechanism. Pseudocode would be helpful.
3. **Clarify the hyperparameter tuning protocol**: state the search space, number of trials, and whether tuning was per-session or global for each method. If NMR used fixed parameters while baselines were per-session tuned, say so explicitly (this is a strength, not a weakness).
4. **Describe the evaluation protocol in the main text**: specify train/validation/test splits, how explained variance is computed, and whether the linear decoder is trained on the same or separate data as the embedding model.
5. **Make the "over 50%" claim precise** — e.g., "outperforms CEBRA by 50–83% on center-out reaching tasks, and by 36–49% on natural movement tasks."
