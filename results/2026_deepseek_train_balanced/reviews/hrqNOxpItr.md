## Summary

This paper extends nonlinear ICA identifiability results to cross-entropy-based classification, proving that under a cluster-centric vMF data-generating process, both instance discrimination (DIET) and standard supervised classification recover ground-truth latent variables up to linear transformations at the global optimum. It provides a "genealogy" connecting GCL, TCL, InfoNCE, DIET, and supervised learning, and validates the theory with synthetic experiments (R² > 98% under vMF), DisLib benchmarks (high Pearson correlations), and ImageNet-X (above-chance linear decoding).

## Strengths

- **Provable identifiability for representations used post-training**: Theorem 1 (cases C3/C4) proves identifiability for the latent variables *before* the classification head, directly matching the standard practice of discarding the projector. This closes a documented gap in prior SSL theory (lines 125–128) that proved identifiability only for representations *including* the projector/head.

- **Extension of identifiability to standard single-task supervised classification**: Theorem 2 proves that even the most common setting — single-task supervised classification with cross-entropy — recovers ground-truth latents up to a linear transformation. Prior work required multitask settings or additional assumptions (Ahuja et al. 2022, Lachapelle et al. 2023, Fumero et al. 2023), as the paper notes (lines 20–21).

- **Novel cluster-centric DGP**: The paper proposes a DGP where latent variables are drawn from von Mises-Fisher distributions around cluster vectors representing semantic classes (lines 148–158). This addresses a known gap — prior SSL theory assumed a uniform marginal despite real data being clustered (line 125–126, citing Rusak et al. 2024).

- **Clean synthetic verification**: Under the exact DGP assumptions, the theory is verified with R² > 98% for both DIET and supervised classification across multiple configurations (Tables 1, 2), with error bars reported across 5 seeds. The orthogonality of the learned linear map is separately validated via singular value MAE.

- **Robustness under model misspecification**: Synthetic experiments show R² > 85% even when data follows Laplace or Normal distributions instead of the assumed vMF (last two rows of Table 1), suggesting the theory may extend beyond its formal assumptions.

- **Unified genealogy**: Figure 2 and Table 3 systematically connect GCL → TCL → InfoNCE → DIET → supervised learning, with explicit comparisons across six properties (latent space, network structure, auxiliary info, conditional, marginal). This goes beyond prior work that treated these methods in isolation.

## Weaknesses

### Fatal

None. The theory is mathematically sound under its stated assumptions, and the synthetic experiments cleanly verify it.

### Major

- **ImageNet-X evidence is far too weak to support the paper's central claims.** The experiment shows only "above chance" linear decoding measured against a shuffled-label baseline (lines 456–461). No R² values, no absolute decoding quality, no comparison to any non-trivial baseline (e.g., nonlinear decoder, model trained on random labels). "Above chance" could mean a correlation of 0.05 — the reader cannot tell. No error bars or confidence intervals are reported for ImageNet-X (despite being reported elsewhere). The proxy labels (human annotations like "is this image blurred?") are not ground-truth latents of any formal DGP. The paper acknowledges this caveat but still presents the results as supporting the theory. This is the only real-world test, and it provides essentially no evidence for the strong claim that supervised classification inverts the data generating process.

- **The title and framing systematically overstate what is actually proved.** Title: "Cross-Entropy Is All You Need To Invert the Data Generating Process." Abstract: "a cohesive theory that accounts for the unreasonable effectiveness of supervised deep learning." The actual results (Theorems 1 and 2) hold under the specific Assumption 1 (vMF conditionals, injective generator, sufficiently many and spread-out cluster vectors) at the global optimum of the population loss. The Limitations section (lines 470–471) does acknowledge some of these restrictions, but the title, abstract, and interpretive framing throughout (e.g., "Our results indicate that deep learning models trained using cross-entropy naturally recover the underlying latent variables up to linear transformations," lines 474–475) consistently frame the theory as broadly explaining deep learning's success without proportional emphasis on how restrictive the assumptions are. A reader coming to this paper for an explanation of "why deep supervised learning works" will be misled.

- **The central theoretical assumptions are not tested on any real dataset.** The vMF conditional (within-class unimodality and isotropy on the hypersphere) and injective generator are core to the proof, but the paper provides no evidence that these hold for DisLib, ImageNet-X, or any real dataset studied. The experiments on real data operate under entirely different (and unverified) DGPs. This gap between the theory's assumptions and what is empirically tested is acknowledged (line 470–471) but not addressed, leaving the practical scope of the results uncertain.

### Minor

- **The DisLib experiments do not distinguish the paper's explanation from simpler alternatives.** Any sufficiently expressive classifier trained to distinguish categories will learn features that correlate with other discriminative properties of the data — this is a mundane prediction that does not require the nonlinear ICA machinery. The paper does not discuss this alternative explanation. Additionally, several continuous factors show high correlation even from raw pixels (e.g., dSprites posX/posY = 0.92 from input alone, Table 3), suggesting some of the signal reflects low-level correlations rather than recovery of latent structure.

- **The model misspecification robustness is presented but not analyzed.** The Laplace and Normal conditional experiments (Table 1, last two rows) show R² > 85% despite violating the vMF assumption that the proof requires. The paper treats this as a robustness result (line 389) with a single sentence, but this is actually striking — if the proof relies on vMF, why does it work under different conditionals? Either the theory is not tight or there is a confound in the experimental setup. This deserves substantial analysis or at minimum a substantive discussion.

- **The "sufficiently large and spread out" condition on cluster vectors (Assumption 1(i)) is stated informally.** The main text (line 163) does not specify the minimum number of classes relative to dimensionality d or the spanning condition needed for the conclusion that h = f ∘ g is linear. This makes it difficult to assess the theorem's scope even within its assumptions.

### Trivial

None.

## Nice-to-Haves

- Report R² or explained variance for the ImageNet-X linear decoding instead of only "above chance" relative to shuffled labels.
- Add a comparison to representations from models trained on randomly shuffled ImageNet labels to test whether meaningful class structure is necessary for the observed decoding.
- Include empirical comparison to SSL-trained models (SimCLR/InfoNCE) on DisLib to test whether the claimed "genealogy" has empirical grounding.
- Formalize the "sufficiently large and spread out" condition precisely in the main text.

## Removed Points

These points were flagged by the reviewer inputs but removed after verification. They should be treated with caution:

1. **Criticism about "linear map from S^(d-1) to R^d" being ambiguous** — This is standard terminology in geometry; the map is the restriction of a linear map on the ambient space. Removed as factually inaccurate.

2. **Criticism about global minimization not being guaranteed for deep networks** — This is standard for identifiability theory (all such results concern global optima of the population loss) and is not specific to this paper. Removed as generic noise.

3. **Concern about the appendix being stripped and claims being unverifiable** — Removed per the hard rule: the parser strips appendices from all papers; the original submission contains them.

4. **Claim that Pearson correlation does not verify multivariate recovery** — For DisLib, individual latents are scalars (posX, scale, etc.), so univariate Pearson is the appropriate test. Removed as factually incorrect criticism.

5. **Claim that the genealogy relationships are "not mathematically formalized"** — The paper provides Table 3 comparing six properties across methods and Figure 2 with labeled arrows specifying transformations. Removed.

6. **Strength Finder's claim that the paper provides "comprehensive three-tier empirical validation"** — While the paper does span three tiers, the ImageNet-X tier is demonstrably weak. The strength was retained in a qualified form above rather than as an unqualified positive.

## Novel Insights

None beyond the paper's own contributions. The key insight — that under a cluster-centric vMF DGP, cross-entropy-based classification recovers latents up to linear transformations — is the paper's own contribution, not a synthesis of the reviews.

## Suggestions

1. **Recalibrate the title and framing** to match what is actually proved. A title like "Identifiability of Latent Variables Under Cluster-Centric Cross-Entropy Classification" would accurately reflect the scope. The abstract and introduction should state assumptions and limitations before the strong interpretive claims.

2. **Substantially strengthen the ImageNet-X experiments or remove them.** Report R² or explained variance for each proxy factor. Add a baseline with models trained on shuffled labels. Show absolute decoding quality (what fraction of variance is explained?) — "above chance" is insufficient for a paper claiming to explain deep learning's effectiveness.

3. **Discuss alternative explanations** for the DisLib results explicitly. What distinguishes the paper's ICA-based explanation from the simpler hypothesis that classification simply learns features predictive of the label?

4. **Analyze the model misspecification findings.** The Laplace/Normal results with R² > 85% are potentially interesting but uninterpreted — is the vMF condition necessary or only sufficient? This could either strengthen the paper (the theory is robust) or reveal a confound.

5. **Precisify the "sufficiently large and spread out" condition** in the main text so readers can assess Theorem 2's scope without consulting the appendix.

## Score and Decision

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>