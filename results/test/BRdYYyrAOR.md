## Summary

The paper extends the training-data reconstruction method of Haim et al. from the pixel space (low-resolution CIFAR/MNIST, simple models) to the embedding space of transfer-learned models. It shows that training embeddings (and, via model inversion, approximate training images at 224×224 resolution) can be recovered from small MLP classifiers trained on embeddings of large pretrained backbones (ViT, DINO, DINOv2, CLIP) on Food-101 and iNaturalist datasets. It additionally proposes a clustering-based method to select good reconstruction candidates without access to the original training data, reducing the number of expensive inversion operations from thousands to tens.

---

## Strengths

1. **Extension of data reconstruction to transfer-learned models with higher-resolution images.** Prior work was limited to 32×32 images (CIFAR, MNIST) and simple models trained from scratch. This paper demonstrates reconstruction at 224×224 resolution across four different backbone architectures (ViT, DINO-ViT, DINOv2-ViT, CLIP) and two diverse datasets (Food-101, iNaturalist), including multiclass settings. This is a nontrivial and valuable step forward.

2. **Empirical validation linking reconstruction to theory.** Figure 4 (fig:cossim_preds) shows a clear correlation between reconstruction quality (cosine similarity between reconstructed and true embeddings) and the model's prediction margin, consistent with the KKT-condition theory from which the reconstruction loss is derived. This provides evidence that the method is genuinely recovering training embeddings rather than producing spurious outputs.

3. **Clustering-based identification addresses a practical bottleneck.** The paper identifies that the cost of inversion (~30 min per embedding on a V100) makes exhaustive inversion of tens of thousands of candidates infeasible. The proposed clustering approach — grouping candidates and inverting only the largest clusters' representatives — is a sensible solution that reduces inversions to tens of candidates. The qualitative results (Figure 5 / fig:clustering) show that the inverted representatives are visually coherent and resemble training samples.

---

## Weaknesses

### Fatal
None.

### Major

1. **Clustering evaluation is not validated in the paper's own target setting.** The quantitative analysis of clustering parameters (Figure maxclust and surrounding text) is performed on CIFAR-10 *image-space* reconstructions from prior work (Haim et al.), not on the paper's own *embedding-space* reconstructions. The paper acknowledges this gap ("Since assessing this effect in our current image-embedding setup is computationally prohibitive"), but the transferability of those CIFAR-10 results to the embedding setting is never established. The qualitative clustering result (Figure 5 / fig:clustering) is compelling, but the central claim that clustering reliably identifies good reconstructions in the embedding setting rests on an indirect proxy. A direct evaluation — e.g., re-encoding the inverted cluster representatives and measuring cosine similarity to the real training embeddings (which the evaluator has access to) — would resolve this cleanly.

2. **No quantitative reconstruction success rate.** The main results (Figures 3, 4, 5) are presented entirely qualitatively. There is no precision/recall, no fraction of training samples recovered above a similarity threshold, and no comparison to a baseline such as inverting random embeddings from the same distribution. The cosine similarity plots (Figure 4) show correlation but do not indicate how *many* training samples are meaningfully reconstructed. Without a numerical measure, it is difficult to assess the magnitude of the privacy risk or to benchmark future work against this method.

3. **Overclaiming in two places.**
   - **"Non-visual data (feature vectors of intermediate layers)"** (Contribution 2, line 27): The reconstructed embeddings are the output of a vision backbone (DINO, ViT, CLIP) trained on *images*. These are visual representations, not "non-visual" data. Calling them "feature vectors of intermediate layers" of the full model is technically defensible but the phrasing suggests a modality-agnostic capability that is not demonstrated — the method has only been tested on visual embeddings derived from vision models.
   - **"Realistic" / "real-world" framing**: The attack requires white-box access to the classifier parameters, knowledge of the exact backbone, and the classifier must be a small MLP trained with weight decay to zero error on a small binary (or few-class) task. The paper's own limitations acknowledge that linear probing (very common in transfer learning) and training without weight decay degrade reconstruction. These are not fatal flaws, but the "real-world" language overstates the practical threat without precise qualification. The paper's honest limitations section partly mitigates this, but the abstract and contribution statements do not carry the same caution.

### Minor

1. **No evaluation of sensitivity to training set size.** All experiments use exactly 100 training images. An experiment with 200 or 500 images on at least one backbone would indicate how the method scales and whether reconstruction degrades as the classifier generalizes better.

2. **Ablation of embedding type deferred to appendix.** The paper mentions that concatenating the CLS token with the average of other tokens had "minor effect" (limitations item, line 275) but defers details to the appendix (appen:cls_mean_token). A brief summary in the main text (e.g., a sentence on the range of cosine similarities observed) would help the reader.

### Trivial
None.

---

## Nice-to-Haves

- Compare reconstruction quality against inverting random embeddings from the same distribution (to isolate the value added by the reconstruction step).
- Report the total compute budget (GPU-hours) for reconstruction sweeps and inversion, to help readers assess practicability.
- A brief exploration of how reconstruction quality changes with larger training set sizes (200, 500) on one backbone.

---

## Removed Points

The following reviewer criticisms were removed or downgraded per the filtering guidelines:

- **"Clustering evaluation requires training embeddings" (Harsh Critic issue #2, part about pairing):** The paper uses training data *for evaluation* (showing that the inverted cluster representatives correspond to actual training samples), not as part of the method. The attacker would simply invert the representatives and observe that the resulting images are coherent natural content — no pairing with specific training samples is needed during the attack. This is a confusion between evaluation methodology and attack procedure. The underlying concern about validation in the target setting is valid and is retained as Major #1.
- **"Requires zero training error" as a weakness:** This is a necessary condition for the reconstruction theory (KKT conditions) to apply, not an independent limitation. Prior work (Haim et al.) has the same requirement.
- **"Attacker knowledge assumptions" as a fatal flaw:** White-box access to model parameters is the standard threat model in this line of work and is the same assumption as in Haim et al. The paper is extending that method to a new setting, not claiming a weaker threat model.
- **Strength Finder's contribution 3 ("non-visual data reconstruction"):** Downgraded from a strength to a weakness (overclaiming) as it is misleading.
- **Generic strength "addressed an important problem":** Removed as it is generic and lacks specific grounding.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers' perspectives cluster around the same issues the paper already identifies in its limitations section: the method's reliance on weight decay, its failure on linear probing, and the dependence on inversion quality across backbones. The main novel observation from the review process is that the clustering evaluation's reliance on a CIFAR-10 proxy is a significant gap that the paper should address with a direct embedding-space evaluation, rather than deferring to computational cost.

---

## Suggestions

1. Add a quantitative reconstruction metric to the main results: e.g., for each training sample, report the rank of the true embedding among the candidate set, or the fraction of training samples whose nearest candidate exceeds a cosine similarity threshold. This would ground the qualitative images.
2. Validate the clustering method directly in the embedding-reconstruction setting: re-encode the inverted cluster representatives and measure their cosine similarity to the true training embeddings. Show that the representatives are significantly closer to training embeddings than to held-out test embeddings.
3. Replace the "non-visual data" claim with a more precise formulation: "reconstruction of embedding vectors from vision models, demonstrating that the method operates in the representation space rather than pixel space."
4. Qualify the "realistic" / "real-world" language in the abstract and introduction to precisely describe the attacker's knowledge assumptions and the conditions under which the method succeeds (weight decay, small MLP, zero training error), consistent with the limitations section.

---

## Score and Decision

The paper makes a genuine and nontrivial extension of prior reconstruction work to the transfer learning setting, with interesting qualitative results across multiple backbones. The clustering method is a sensible practical innovation. However, the evaluation is weakened by (a) the lack of quantitative success metrics, (b) the clustering validation being performed on a proxy task rather than the target setting, and (c) some overclaiming in the framing. These issues are addressable but limit the paper's current strength. The core contribution is real but incremental.

**Originality:** Good — extends a known method to a new and important setting.  
**Importance of question:** High — privacy risks in transfer learning are practically relevant.  
**Claims support:** Moderate — qualitative results are compelling but lack quantitative backing.  
**Soundness:** Adequate — the methodology follows from established theory but the evaluation has gaps.  
**Clarity:** Good — well-structured and readable, with an honest limitations section.  
**Value to community:** Moderate — will be of interest to the privacy and transfer learning communities.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>