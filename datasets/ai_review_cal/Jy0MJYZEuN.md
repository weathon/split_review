- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have all the evidence needed. Let me produce the consolidated review.

## Summary

The paper proposes GenZSL, an inductive variational autoencoder for zero-shot learning that generates unseen class features by *inducing* from semantically similar seen classes (guided by weak CLIP text embeddings) rather than *imagining* features from noise as done in prior generative ZSL methods. The method includes class diversity promotion (CDP) to decorrelate class semantic vectors, a semantically-similar sample selection mechanism, and a target class-guided information boosting loss. Experiments on CUB, SUN, and AWA2 show large performance gains and substantial training speedups over prior generative ZSL methods.

## Strengths

- **Novel induction paradigm for generative ZSL.** Instead of generating features from Gaussian noise conditioned on class embeddings (the standard "imagination" approach), GenZSL transforms features from similar seen classes toward target class features. This is a conceptually clean departure from the f-VAEGAN/TF-VAEGAN line of work and is well-motivated by the cognitive science analogy of induction. (Sections 1, 3)

- **Thorough ablation study validates each component.** Table 3 shows that removing the target class reconstruction loss (L_TR) drops harmonic mean by 30.8% on CUB and 33.5% on AWA2, and that both CDP and L_Boost each contribute nontrivially. This provides clear evidence that the two "criteria" (class diversity promotion and target class-guided information boosting) are each necessary. (Section 4.2, Table 3)

- **Dramatic training efficiency.** Figure 5 reports ≥60× faster training than f-VAEGAN on AWA2, alongside better GZSL and CZSL performance. The efficiency advantage is structurally plausible (VAE vs. GAN with discriminator) and directly demonstrated. (Section 4.4, Figure 5)

- **Class diversity promotion is empirically effective.** CDP reduces mean cosine similarity between class semantic vectors from 0.5726 to 1.825e−5 on CUB (Figure 3), and the ablation confirms its removal hurts performance. The approach of removing the first principal component is simple and interpretable. (Section 3.1, Figure 3, Table 3)

- **Hyperparameter robustness is demonstrated.** Figure 6 shows stable performance across variations in loss weight λ, number of referent classes k, and number of synthesized samples N_syn, reducing concerns about tuning sensitivity. (Section 4.5, Figure 6)

## Weaknesses

### Fatal

None.

### Major

1. **Visual backbone confound undermines the headline comparisons in Tables 1 and 2.** GenZSL extracts visual features using the CLIP vision encoder (512-dim, line 189). The baselines compared in Tables 1 and 2 (f-VAEGAN, TF-VAEGAN, CE-GZSL, etc.) overwhelmingly use ResNet-101 features (2048-dim) in their original published form — but the paper never states what backbones those baseline numbers come from, nor does it control for this variable. The observed gains (e.g., 92.2% vs. 71.9% on AWA2 in Table 1) could be partially or entirely attributable to the stronger visual backbone rather than the induction mechanism. **This is the single most consequential weakness**: the paper's central claim — that induction outperforms imagination — rests on comparisons that do not isolate the effect of the method from the effect of the backbone. Table 4 partially addresses this (all methods use CLIP text embeddings), but that experiment is limited to CUB, uses weak semantic vectors that imagination-based methods are not designed for (their performance drops sharply), and still does not control the visual backbone. Without a controlled experiment where all methods share the *same* visual features (and ideally the same semantic vector type), the headline performance claims remain unsubstantiated.

2. **Comparison with large-scale VL methods (Table 4) is under-specified.** CLIP, CoOp, and CoOp+SHIP are listed as baselines using "weak class semantic vectors extracted from the CLIP text encoder" (line 225), but the paper does not describe the evaluation protocol used for these methods. CLIP conventionally classifies by direct cosine similarity between image and text embeddings; CoOp learns prompt vectors on seen classes. These protocols are fundamentally different from training a classifier on generated features, and it is unclear whether the reported numbers come from the same train/test splits and evaluation protocol. The comparison cannot be properly assessed without this information.

### Minor

1. **The claim that CDP "keeps the original relationships between all classes" (line 120) is overstated.** Removing the first principal component necessarily discards the dominant dimension of variation. While distances orthogonal to that axis are preserved, the resulting vectors are no longer in the same metric space as the original CLIP embeddings, so inter-class relationships (e.g., dog vs. wolf similarity) are distorted. The near-orthogonality aids discriminability, but the paper should acknowledge this trade-off explicitly.

2. **The CLIP vision encoder variant is unspecified.** The paper reports 512-dim visual features but does not state which CLIP model was used (ViT-B/32? RN50? ViT-L/14?). This matters for reproducibility, as different CLIP variants produce meaningfully different feature spaces. (Line 189)

3. **No variance or statistical significance reported.** All results are presented as single numbers without standard deviations across runs. Given the very large reported gains, even 3 runs with std dev would significantly increase confidence that the margins are robust. (Tables 1, 2, 3, 4)

4. **The mixup weight (0.8/0.2) is not ablated or justified.** The paper uses a weighted mixup of top-2 referent samples (line 189). The ablation varies k (number of referent classes) over {1,2,4,8} in Figure 6b, but the mixup weight itself is held fixed and its sensitivity is not explored. The choice of 0.8/0.2 over equal mixing or other ratios is unexplained.

5. **Hyperparameter analysis is limited to CUB.** The ablation sweep for λ, k, and N_syn is only shown on CUB (Figure 6). The paper states the chosen values for SUN and AWA2 were set "empirically" (line 255), but no sensitivity analysis is provided for those datasets, so it is unclear whether the hyperparameters transfer well.

6. **The reconstruction loss (L_TR) is not specified.** The paper defines L_TR as an ELBO-style reconstruction term (line 147) but does not state whether it is MSE, BCE, or another form. This is a minor clarity gap.

### Trivial

- The mention of "top-2 similar classes serve as the referent classes" and the mixup of top-1 and top-2 samples could be more clearly distinguished from the k=2 sweep.
- Some notation issues: the paper uses both $\tilde{z}$ and $\widetilde{z}$ for refined semantic vectors.

## Nice-to-Haves

- A controlled experiment where GenZSL and baselines (f-VAEGAN, TF-VAEGAN) share *exactly the same* visual features (CLIP features) and the same semantic vector type would cleanly isolate the induction advantage.
- An analysis measuring cosine similarity between synthesized features and target vs. source class embeddings would provide direct evidence that GenZSL genuinely transforms features toward the target class.
- A limitation exploration: constructing a test case where no similar seen classes exist for an unseen class, to demonstrate the boundary of the induction approach.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Missing related works on induction-like methods (semantic autoencoders, relation nets)."** Removed per instruction: I cannot verify the existence or relevance of these methods from external sources, and the instruction prohibits raising missing-related-work criticisms.
- **"The cognitive analogy is loose / overselling novelty."** Removed: this is a subjective stylistic critique rather than a concrete, verifiable weakness about the paper's technical content.
- **"The training protocol for referent selection is unclear."** Removed: the paper does specify (line 130-136) that referent samples come from seen classes for both seen and unseen target classes during training/testing respectively — this is stated, albeit somewhat compactly.
- **"L_Boost may overlap with L_TR in effect."** Removed: the ablation (Table 3) directly tests this by removing L_Boost while keeping L_TR, and performance degrades, providing an empirical answer.
- **"t-SNE can be misleading."** Removed: this is a known caveat of any t-SNE visualization; the paper uses it for qualitative illustration, which is standard and acceptable.
- **"Efficiency claim lacks detail (epochs, batch sizes)."** Weakened to Nice-to-Have: the paper provides wall-clock training curves (Figure 5) which is sufficient evidence for the claimed speedup; additional detail would be nice but is not missing.
- **"If no similar seen classes exist, induction may fail."** Removed: the paper already states this as a limitation (line 264).
- **"f-VAEGAN performance drops with weak semantic vectors."** This observation from the reviewer is accurate but already noted in the paper (line 231).

## Novel Insights

Both the harsh critic and strength finder agree on the paper's core structure but diverge sharply on how to weigh the backbone confound. The critical insight is that the paper's central claim ("induction > imagination") is supported by a confounded comparison, yet the paper contains *partial* controlled evidence (Table 4) that shows large gaps persist even when controlling semantic vectors — though not visual features. A genuinely novel observation from synthesizing the two reviews is that the paper would benefit from framing its contribution more modestly: instead of "induction beats imagination," the evidence better supports "induction reduces reliance on strong semantic vectors while achieving competitive results." The ablation study (Table 3) is actually a stronger piece of evidence for the internal soundness of the method than any of the external comparisons, because it is cleanly controlled. None of the reviewers noted that the paper's efficiency advantage (60× faster) is arguably its most robust empirical result, since it follows directly from the VAE (vs. GAN) architecture and does not depend on backbone choice.

## Suggestions

1. **Run a backbone-controlled experiment.** Compare GenZSL against f-VAEGAN and TF-VAEGAN using the *same* CLIP visual features on all three datasets, with the same weak semantic vectors. Report whether the gap narrows or persists. This is the single most important revision.
2. **Specify the CLIP model variant** (e.g., ViT-B/32) used for reproducibility.
3. **Describe the evaluation protocol for CLIP/CoOp/CoOp+SHIP baselines** in Table 4, including whether the same train/test splits were used and how classification was performed.
4. **Report results with standard deviations** across at least 3 random seeds for the main tables.
5. **Acknowledge the CDP trade-off explicitly** — that removing the first principal component enhances discriminability at the cost of distorting original inter-class relationships.
6. **Run hyperparameter sensitivity on at least one additional dataset** (e.g., SUN or AWA2) to confirm the λ and k choices generalize.
