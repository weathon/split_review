Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces the task of "training-free editioning" for text-to-image models: creating model variations (e.g., a "cat edition" that always generates cats) without retraining. The proposed method constructs concept subspaces via PCA on representative CLIP text embeddings for a target concept, then projects input prompt embeddings into these subspaces before feeding them to the diffusion model. Experiments with Stable Diffusion v1.4 on a fixed template prompt structure show high CLIP-based edition accuracy across nine concept subspaces.

## Strengths

- **Novel task with clean formalization**: The paper formally defines "training-free editioning" (Definitions 1 and 2) and clearly distinguishes it from image editing (image-level) and concept erasing (requires fine-tuning), carving out a new problem space that prior work does not address.

- **Training-free, conceptually simple method**: The core idea — building concept subspaces via PCA on text embeddings and projecting input prompts into them — is elegant and requires no model fine-tuning or architectural changes. This is a genuine methodological contribution in a landscape dominated by training-based approaches.

- **Empirical justification of the geometric foundation**: The paper validates Conjecture 1 (embeddings lie on a thin hypersphere shell centered at the origin) by showing distances to origin are consistently ~250 with small standard deviation across concept datasets (Figure 5). This geometric insight supports the PCA-based subspace creation and is a technically informative finding.

- **Computational efficiency via two-step PCA**: Reducing the CLIP embedding space from 59,136 to 13,000 dimensions using global PCA on COCO captions (~20.7× speedup for covariance computation) while retaining 99.9% explained variance makes the method practical.

- **Semantic interpretability**: Qualitative results show that moving along principal components produces semantically meaningful variations within the target concept, adding interpretability to the subspace structure.

## Weaknesses

### Major

- **No direct comparison to prompt replacement on edition accuracy**. The paper compares against prompt replacement only via FID/IS (Table 2) and cosine similarity of embeddings (Table 3), but never reports the edition accuracy (CLIP score) of the prompt-replacement baseline. This is the most natural and trivial baseline — if a user wants a cat image, they can simply write "cat" in the prompt. Without knowing whether projection achieves better, worse, or comparable edition accuracy than prompt replacement on the same evaluation set, the paper cannot establish that the method provides value beyond a trivial operation. This is the single largest gap in the evaluation.

- **No quantitative verification that non-subject semantic content (verb, object, background) is preserved**. The CLIP softmax metric (Table 1) compares generated images against the ground truth prompt (e.g., "cat running on grass") vs. the original prompt (e.g., "dog running on grass"). A high score can be achieved if the generated image contains a cat (matching the subject) while ignoring the action and object — the CLIP score does not decompose along semantic axes. The paper has no independent classifier, human evaluation, or per-element metric to verify that editioning preserves verb, preposition, and object semantics. Without this, the claim that "other concepts remain unchanged" (Section 5.2.2) is only supported by qualitative examples (Figure 3), not rigorous evidence.

### Minor

- **The FID comparison is between two sets of generated images (Ours vs. SD with replaced prompts, and SD vs. SD'), not between generated and real images**. This is a non-standard usage of FID. The reported FID values (13–33 between Ours and SD) are also quite high compared to typical real-vs-generated FID, and the paper interprets higher IS scores as "similarly high quality but less diverse" — but IS is known to reward low diversity, making this interpretation ambiguous. The claim that "image quality is preserved" would be better supported by human evaluation or comparison to real-image distributions.

- **The Table 2 caption specifies replacing the \<object\> with the concept, but the paper's experiments focus on subject editioning**. For the cat edition, this would mean replacing the object (e.g., "grass") rather than the subject (e.g., "dog") with "cat", yielding "dog running on cat" instead of the correct baseline "cat running on grass." This appears to be an error in the description (likely should be \<subject\>), but as written it creates confusion about what the FID/IS baseline actually measures.

- **No ablation on the global PCA pre-processing step**. The two-step PCA (global reduction from 59k→13k, then per-concept PCA) is a key design choice. The paper validates the global reduction on COCO variance, but does not ablate whether concept-specific subspaces are preserved under this reduction. A simple comparison of concept subspaces built with and without the global reduction would address this, but is absent.

- **No analysis of failure cases or concept suitability**. Only common concrete nouns (cat, dog, car, etc.) are tested. The paper does not examine concepts where PCA may not yield a compact subspace (e.g., abstract concepts, multi-word concepts, or concepts with high intra-class visual diversity).

- **Scope is explicitly narrow but the claims in the introduction (business models, product differentiation, freemium tiers) overreach relative to the demonstrated capability**. The method is validated only on single-noun subjects in a fixed <subject><verb><preposition><object> template. While the paper acknowledges this as a "first step," the business-model framing implies a level of generality that is not supported.

### Trivial

- The description of the softmax probability computation (lines 269–270) appears to have a textual issue where item (ii) duplicates item (i) as "the CLIP score between I and p" rather than between I and the original prompt, making the procedure ambiguous as printed.

## Nice-to-Haves

- A human evaluation study asking raters whether the edited subject appears and whether non-subject content is preserved would be the strongest way to substantiate the core claims.
- An ablation on the number of principal components k (beyond the fixed 95% variance threshold) showing the trade-off between edition accuracy and image diversity.
- Demonstrating the method on at least one non-subject edition (e.g., verb edition like "jumping edition") within the same template structure to show broader applicability of the subspace approach.

## Removed Points

- **"Edition accuracy is evaluated circularly"** — This criticism is largely removed after verification. The CLIP softmax metric compares the generated image against the ground truth prompt ("cat running on grass") vs. the original prompt ("dog running on grass"). This is not circular; it is a direct test of whether the edition succeeded in changing the subject. The method projects onto a subspace, not toward a specific prompt. However, the underlying concern about non-subject preservation not being independently verified is kept as a Major weakness above.

- **"The paper claims editioning differs from concept erasing but Table 1 shows high scores for non-target categories... this is forcing concept presence"** — This misunderstands the task. Editioning is defined as forcing concept presence; that is the entire goal. This is not a contradiction; it's the definition of the task. Removed.

- **"Discussion of editioning vs. erasing difficulty (modification magnitude) is speculative and not tested"** — While this is true, it is a secondary conceptual discussion that does not affect the core method or its validation. It does not rise to the level of a weakness worth listing.

- **"No discussion of how the method handles prompts not matching the template"** — The paper explicitly scopes this as a special-case first step and acknowledges the general case as future work. Criticizing it for not handling free-form prompts is criticizing the paper for not solving a harder problem it identifies as open.

## Novel Insights

The reviews collectively surface an interesting tension: the paper's core innovation is that it operates in embedding space (rather than prompt space) to achieve training-free editioning, but the evaluation never directly shows that operating in embedding space is *better* than operating in prompt space (i.e., simply rewriting the prompt). This gap — between the claimed advantage of the method (generality, no syntax analysis needed) and the evidence provided (which mostly shows the method *can* do the task, not that it does it *better* or *differently* than the simplest alternative) — is the fundamental weakness. A compelling defense would require demonstrating cases where prompt replacement fails (e.g., complex syntax, ambiguous subjects, multi-word concepts that don't map to a clean swap) and the projection method succeeds, but the paper's narrow template-based setup precludes this comparison.

## Suggestions

1. Add a direct comparison to prompt replacement on the edition accuracy metric (CLIP softmax) using the same evaluation datasets. This is the single most informative experiment the paper is missing.

2. Add an evaluation of non-subject preservation — either using per-element CLIP scores (measuring alignment with ground truth for verb and object separately) or an off-the-shelf classifier/object detector on the generated images.

3. Clarify whether the FID/IS baseline (Table 2) replaces the subject or the object, and fix the caption if it's a typo. If the experiment actually replaces the object, re-run with subject replacement.

4. Include an ablation comparing concept subspaces built with and without the global PCA dimensionality reduction step to validate that the compression preserves concept-specific information.

5. Tone down the business-model claims in the introduction unless additional generality (beyond single-noun subjects in a fixed template) is demonstrated.

## Score and Decision

The paper introduces a novel task and a clean, training-free method. The conceptual contribution is real — framing model customization as subspace projection in embedding space is interesting. However, the evaluation has two major gaps: the absence of a direct edition-accuracy comparison against prompt replacement (the trivial baseline), and the lack of quantitative verification that non-subject content is preserved. Without these, the paper cannot substantiate that its embedding-space approach offers advantages over simply rewriting prompts. The narrow scope (single-noun subjects, fixed template) is acknowledged but not convincingly shown to be a stepping stone to generality. For a conference paper, the evaluation is insufficient to support the claimed contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>