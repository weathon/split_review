## Summary

This paper tackles the challenging problem of zero-shot enzyme generation for target molecules with no known catalysts. The authors propose SENZ, a retrieval-augmented discrete diffusion model that: (1) retrieves functionally-related enzymes by Tanimoto similarity of the target molecule's Morgan fingerprint against stored substrates (requiring no anchor protein sequence), (2) aligns the retrieved enzymes into an MSA and uses a discrete diffusion generator (MSA transformer backbone) conditioned on the molecule embedding to generate a novel enzyme, and (3) employs discriminator guidance during training to push the generated distribution toward higher catalytic activity. The paper also formalizes the task definition and contributes a dataset of substrate-enzyme pairs from RHEA.

## Strengths

- **Substrate-indexed retrieval without an anchor protein**: Unlike traditional protein retrieval that requires a query sequence, SENZ retrieves enzymes purely by comparing the target molecule's Morgan fingerprint (Tanimoto similarity) against stored substrates (Eq. 5a-b, Section 3.1). This directly addresses the core zero-shot challenge where no known enzyme exists. The ablation in Section 4.4 confirms that increasing the number of retrieved sequences improves catalytic performance, validating the retrieval mechanism's role.

- **Differentiable guidance from a substrate-enzyme discriminator**: The paper uses Gumbel-softmax to make the discrete diffusion output differentiable, enabling gradient-based guidance from a pre-trained discriminator (Eq. 11-14, Section 3.3). The ablation (Section 4.5, Fig. 2c-d) demonstrates that removing guidance causes generated enzymes' kcat to collapse to that of retrieved sequences, while guidance substantially improves it — providing causal evidence that the guidance mechanism contributes beyond retrieval.

- **Multi-perspective evaluation across catalytic, structural, and docking dimensions**: The evaluation spans predicted turnover number (kcat via UniKP), foldability (pLDDT via ESMFold), sequence novelty (BLASTp identity, clustering), and docking (AutoDock-Vina) — covering four distinct evaluation modalities (Sections 4.2–4.6). This is more comprehensive than prior enzyme generation works (e.g., ZymCTRL, ProGen2 are only compared on sequence-level metrics).

- **Principled zero-shot data split with dual decontamination rules**: Two non-overlap conditions — no shared molecules and <30% sequence identity between splits (Section 2) — ensure the test evaluation genuinely measures zero-shot generalization rather than memorization of similar sequences.

- **MSA-based molecular conditioning**: The paper appends the GAT-encoded molecule embedding as an extra token to each row of the MSA matrix (Section 3.2), leveraging the MSA transformer's row-wise and column-wise attention to propagate substrate information across all retrieved sequences. This is a thoughtful architectural choice.

- **Identification and discussion of the catalytic vs. foldability trade-off**: The paper acknowledges that increasing the number of retrieved enzymes improves kcat but decreases pLDDT, tying this to prior literature (Vanella et al., 2024) (Section 4.4). This nuanced finding strengthens the paper's scientific credibility.

## Weaknesses

### Fatal
None.

### Major

- **The discriminator's ability to provide molecule-specific guidance for unseen substrates is unvalidated, creating a gap between the paper's claims and the evidence.** The discriminator \(D(\mathbf{x}, \mathbf{m})\) is pre-trained on the training set \(\mathcal{D}\) and frozen (Section 3.3). In the zero-shot setting, the target molecule \(\mathbf{m}\) is *not in the training set*. The paper claims that the guidance "guides the generation toward different directions distinct from the whole record data distribution" for "different substrates" (Section 1, line 22) and that it "pursues an effective enzyme for m" (Section 3.3). However, the paper never tests whether the discriminator can provide *molecule-specific* scores for unseen molecules, as opposed to simply recognizing generic "enzyme-likeness" patterns. This is not a fatal flaw — a discriminator trained on diverse substrates could learn transferable features — but it is a significant gap that undermines a central claim. The paper should either validate the discriminator's generalization (e.g., show that its scores correlate with ground-truth activity on held-out molecules) or significantly soften the claims about molecule-specific guidance.

- **The paper's strongest claims about catalytic performance outpace the evidence.** The central evaluation metric is \(\log_{10}(k_{\text{cat}})\) predicted by UniKP, an off-the-shelf predictor. The paper states that "generated enzymes can outperform Ground Truth natural enzymes, which suggests the natural enzymes are possibly not the most efficient" (line 161) and claims "superior catalytic capability" (line 173). These are strong causal claims about *actual catalytic activity* based entirely on a computational predictor. It is a well-known failure mode that generative models can "hack" predictors — producing sequences that score highly without conferring real catalytic function. The paper should sharply distinguish between *in silico* predicted activity and actual catalytic function, and claims about "outperforming" natural enzymes should be removed or heavily qualified as prediction-based results.

- **Critical implementation details are absent, severely limiting reproducibility.** The paper provides no architecture specifications (number of layers, hidden dimensions, attention heads for the MSA transformer or GAT molecule encoder), no training hyperparameters (learning rate, batch size, optimizer, training epochs), no discriminator architecture or training procedure, no value of the key hyperparameter \(d\) (number of retrieved enzymes) used for main results, no value of \(T\) (number of diffusion steps), and no hardware or training time. The dataset statistics referenced as "Table 7" are not provided in the text. For a top-venue submission proposing a new method, these omissions are significant.

### Minor

- **The discriminator's architecture, training procedure, and accuracy are completely unspecified.** Since \(\mathcal{L}_g\) constitutes roughly half the total loss (it is summed additively with \(\mathcal{L}_r\)), the discriminator is a critical component. The paper simply states it is "pre-trained on training set \(\mathcal{D}\)" (line 128) with no further detail. Its capacity, its positive/negative sampling strategy, and its accuracy on held-out pairs are all unknown.

- **Statistical significance is not reported.** The paper reports average \(\log_{10}(k_{\text{cat}})\) values with no variance, standard deviations, or confidence intervals. With only 10 sequences generated per task (line 151), the sample is small. The paper should report variance or use statistical tests for comparisons.

- **No discussion of failure modes or limitations.** The paper presents only positive results. A discussion of when the method might fail — e.g., for molecules whose Tanimoto similarity to any training molecule is near zero, or cases where the retrieval assumption (Tanimoto similarity maps to functional similarity) breaks down — would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- Validate the core retrieval assumption directly: using training data, show that enzymes for Tanimoto-similar substrates are indeed more sequence-similar (or have more similar active sites) than enzymes for dissimilar substrates.
- Disentangle the contributions more cleanly with an ablation comparing: (a) full SENZ, (b) SENZ without guidance, (c) just retrieving the top-d sequences and using them directly, (d) randomly retrieving d sequences.
- Provide dataset statistics (number of unique substrates, unique enzymes, pairs, train/validation/test sizes) in the main text.

## Removed Points

These points from the input reviews were removed because they were found to be invalid, overstated, or incompatible with the filtering rules:

- **"The generator without guidance essentially reproduces retrieval, raising questions about its contribution"** — The paper *itself acknowledges* this result (line 189) and uses it as evidence that the guidance mechanism is essential. The ablation is correctly framed as showing that guidance adds value beyond retrieval. This is a strength of the paper's experimental design, not a weakness.
- **"The discriminator cannot possibly evaluate unseen molecules"** — Demoted from potential fatal weakness to Major. The absolute claim that it "cannot possibly" generalize is too strong; a discriminator trained on diverse substrates with a GAT encoder could learn transferable chemical features. However, the paper's failure to validate this is a genuine gap.
- **Criticisms about figures not being visible** — These are parser artifacts, not paper issues.
- **"The paper does not specify what structure was used for LigandMPNN"** — This is a detail about the baseline setup that is reasonable to request but more of a reproducibility note than a weakness of the paper's method.

## Novel Insights

The most interesting observation arising from this review is the tension between the paper's two central claims. Claim 1: the discriminator provides *molecule-specific* guidance that drives the generator toward *different* optimal enzymes for *different* substrates. Claim 2: the discriminator is pre-trained only on training-set molecules and never sees test-set molecules. For Claim 1 to be true, the discriminator must learn a representation of enzyme-substrate compatibility that generalizes to novel chemical structures. This is a non-trivial property — and if it does hold, the discriminator itself would be a significant contribution worthy of independent analysis. The paper misses an opportunity to investigate this: it never checks whether the discriminator's gradients for different test molecules actually push the generator in measurably different directions (e.g., toward different active-site motifs), or whether the guidance simply applies a generic "look more like an enzyme" bias. This could be tested with a simple experiment: compare the diversity of sequences generated with guidance vs. without, or check whether swapping the discriminator's molecule input changes the generator's output distribution for fixed retrieved sequences.

## Suggestions

1. **Validate discriminator generalization.** Test whether the discriminator's scores correlate with any reasonable proxy for catalytic quality (or even sequence properties) on held-out molecules. If it generalizes, this strengthens the paper; if not, the claims about guidance must be substantially revised.
2. **Calibrate claims about catalytic superiority.** Replace "outperform natural enzymes" with precise statements about predicted metrics, and explicitly discuss the limitation that all evaluations are *in silico*.
3. **Provide missing reproducibility details** (architecture, hyperparameters, dataset statistics, discriminator training, value of \(d\), value of \(T\)) either in the main text or an appendix.
4. **Report variance** for all main results, especially given the small sample size (10 sequences per task).
5. **Add a limitations section** discussing when the retrieval assumption might fail and how the approach could break down for highly novel substrates.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>