Now I have all the information I need to write the final consolidated review. Let me synthesize the evidence.

---

## Summary

This paper identifies and formalizes the "copy-paste artifact" in identity-conditioned image generation — where models trivially replicate reference faces rather than adapting to intended poses and expressions. It contributes three artifacts: (1) **MultiID-2M**, a 500K-image paired multi-person dataset with diverse references per identity; (2) **MultiID-Bench**, a standardized benchmark with a novel Copy-Paste metric (Eq. 2) that quantifies the trade-off between identity fidelity and artifact suppression; and (3) **WithAnyone**, a FLUX-based model trained with a GT-aligned ID loss and an ID contrastive loss that breaks the observed fidelity-vs-copy-paste trade-off, achieving strong identity similarity (Sim(GT)=0.460) with substantially reduced copy-paste (CP=0.144) compared to baselines like InstantID (CP=0.337).

## Strengths

- **Identification and formalization of the copy-paste artifact**: The paper provides a principled metric (Eq. 2) that captures the relative bias of a generated face toward the reference versus the ground truth, normalized by natural variation. Figure 5 demonstrates that most existing models lie on a clear trade-off curve, making the artifact visible and measurable for the first time.

- **Substantial empirical gains across both single- and multi-person settings**: WithAnyone achieves Sim(GT)=0.460 with CP=0.144 on the single-person benchmark (Table 1a), versus InstantID at Sim(GT)=0.464 / CP=0.337. The same pattern holds on 2-person (Table 2a) and 3-4-person (Table 2b) subsets, with WithAnyone consistently in the upper-right desirable region of Figure 5 while all baselines fall on the trade-off curve.

- **GT-aligned ID loss is a simple, effective innovation**: By using ground-truth landmarks to align generated images before ArcFace extraction (Sec. 5.1), the loss can be applied at all noise levels without the computational cost of full denoising. Figure 7 validates lower ID loss across noise levels, and Table 3 shows that removing it (w/o GT-Align) drops Sim(GT) from 0.405 to 0.385.

- **Paired dataset and training pipeline are well-ablated**: Table 3 confirms that removing the paired-data fine-tuning phase (w/o Phase 3) jumps CP from 0.161 to 0.239, and training on FFHQ only collapses Sim(GT) to 0.224, validating both the dataset and the training curriculum.

- **Comprehensive baseline comparison**: 12+ models evaluated across both general customization methods (OmniGen, GPT-4o, etc.) and face-specific methods (InstantID, PuLID, UniPortrait, etc.) on both single-person and multi-person subsets, with multiple metrics (Sim(GT), CP, CLIP-I, CLIP-T, aesthetics).

## Weaknesses

### Fatal

None.

### Major

- **Evaluation circularity in the primary metrics**: The Sim(GT), Sim(Ref), and CP metrics (Sec. 4) are computed using face embeddings — the same ArcFace embedding space in which the ID loss (Eq. 4) and contrastive loss (Eq. 5) operate. The model is optimized to minimize ArcFace distance and then evaluated on ArcFace distance. While the paper also reports CLIP-based metrics (CLIP-I, CLIP-T) and aesthetics scores, and the user study provides an external anchor, the headline quantitative comparison that demonstrates "breaking the trade-off" is partially circular. An evaluation using an independent face-embedding model not used in training would substantially strengthen the claims.

### Minor

- **User study presentation is problematic**: Figure 8 labels methods as "Cure," "UNO," "iDetch," "Uniformal," and "OmniGen." "Cure" appears to refer to WithAnyone, but "iDetch" and "Uniformal" do not correspond to any model names in Tables 1–2. The mapping between study labels and paper model names is never explained, making the results uninterpretable. The study is also small (10 participants, 230 groups) and omits strong baselines like InstantID, PuLID, and UniPortrait that would be relevant for a human evaluation of copy-paste artifacts.

- **OmniContext metrics undefined in the main text**: Table 1b reports PF, SC, and Overall scores but none of these are defined in the main paper body. Readers unfamiliar with OmniContext cannot interpret the table without consulting external references.

- **Missing limitations discussion**: The paper has no limitations section. Relevant limitations include: dependence on celebrity data (potential domain gap to non-celebrity faces), inheritance of biases from the FLUX base model and web-scraped data, the method addressing faces but not full-body identity, and unreported training cost and inference speed.

- **Dataset provenance details are thin**: The ethics statement (Sec. 7) describes CC-license filtering but does not detail concrete verification steps beyond search-engine filters, nor specify the exact format of data release (raw images, embeddings, or URLs). Given the sensitivity of a re-identifiable celebrity face dataset, a more thorough account is warranted.

### Trivial

- Figure 8 uses a bubble-chart visualization for categorical × categorical data, which is non-standard and makes effect sizes difficult to gauge.

## Nice-to-Haves

- Reporting the Copy-Paste metric's correlation coefficient with human judgments quantitatively (the paper states "moderate positive correlation" but gives no number).
- Ablating the effect of negative pool size in the contrastive loss (the paper ablates removing extended negatives entirely, reducing from 4096 to 63, but does not explore intermediate sizes).
- A baseline trained from scratch on MultiID-2M with only reconstruction loss (no contrastive, no paired tuning) to cleanly isolate the contribution of the training curriculum versus the data.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Abstract over-promises by calling the dataset 'large-scale open-source … tailored for multi-person scenarios' when the evaluation is largely single-person"** — REMOVED. The paper does evaluate on multi-person subsets (Table 2a and 2b cover 2-person and 3-4-person scenarios). The single-person evaluation is naturally larger because more baselines support it, but the multi-person results are present and positive.

- **"Inclusion of GPT-4o in multi-person comparisons, despite its acknowledged prior knowledge, weakens the fairness of those rows"** — REMOVED. The paper explicitly acknowledges this issue in the Table 2 caption: "GPT exhibits prior knowledge of identities from TV series in subsets with more than two IDs, leading to abnormally high similarity scores." The authors flag the confound themselves; it does not need to be raised as a criticism.

- **"Dataset cannot legally be redistributed in its current form" / "whether the dataset can legally be redistributed"** — REMOVED as a standalone weakness. This is speculative; the paper describes CC-license filtering. The concern about insufficient detail on license verification is retained under Minor weaknesses, but the claim about illegality is unsubstantiated.

- **"Only five models were compared (several strong baselines from Table 1 were omitted)" in user study** — Merged into the Minor weakness about user study presentation; not a separate weakness.

- **"DynamicID excluded from experiments due to unavailability of code and pretrained models"** — REMOVED. The paper cites a footnote explaining the exclusion; this is standard practice and not a weakness.

- **Strength Finder claimed strengths about "the problem is important" and generic framing** — REMOVED as they are generic praise without concrete anchors.

## Novel Insights

The most genuinely novel observation from these reviews is that the copy-paste artifact can be understood as the consequence of a training-data asymmetry: when the reference and target are the same image (reconstruction training), the model's shortest path to low loss is direct copying. The paper demonstrates that simply breaking this symmetry — by providing distinct reference and target images of the same identity from a paired dataset — is sufficient to force the model to learn higher-level identity representations. This insight, while simple in retrospect, explains a failure mode that had not been explicitly characterized before.

## Suggestions

- Replace the ArcFace-based evaluation metrics with an independent face-embedding model (e.g., a different face-recognition network not used in training) and report both sets of numbers to demonstrate that the gains are not an artifact of metric overfitting. This is the single most impactful change the authors could make.
- Fix the user study figure: map all codenames ("Cure," "iDetch," "Uniformal") to the paper's actual model names, report numerical averages with error bars, include the strongest baselines (InstantID, PuLID), and report the quantitative correlation between CP scores and human copy-paste judgments.
- Add a brief limitations paragraph covering domain generalization beyond celebrities, FLUX base-model biases, face-only scope, and computational cost.
- Define PF, SC, and Overall metrics from OmniContext in the main text or in a footnote in Table 1b.

## Score and Decision

### Anchor comparison

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| `88Qm4fGWzX` (Event-Customized) | 5.00 | R1 | WithAnyone has substantially more substance: dataset + benchmark + method + artifact formalization vs. training-free method with limited evaluation. |
| `qZB7KDN4L1` (Subject-Diffusion) | 5.00 | R1 | Similar scale (large dataset) but WithAnyone has better evaluation rigor, a principled artifact identification, and a clearer training contribution. |
| `riieAeQBJm` (UIFace) | 6.00 | R1/R2 | Both address copy-paste / overfitting to context in face generation. WithAnyone is broader in scope (multi-person, benchmark, dataset) and stronger in evaluation breadth. |
| `iTm4H6N4aG` (ClassDiffusion) | 6.25 | R2 | ClassDiffusion is a simpler, narrower contribution. WithAnyone has more components and broader evaluation. |
| `ZkFMe3OPfw` (InstantPortrait) | 6.67 | R2 | Comparable quality. Both have large datasets and novel training objectives. InstantPortrait has cleaner presentation; WithAnyone has broader scope but sloppier user study reporting. Slightly below InstantPortrait. |
| `cD1kl2QKv1` (One-Prompt-One-Story) | 7.40 | R2 | Cleaner paper with an elegant training-free observation. WithAnyone's contributions are more extensive but rougher in presentation. Clearly below this anchor. |

**Round 1 bracket**: 5.5–7.5. The paper sits above the 5.0 weak anchors and below the 8.0+ strong anchors, being clearly better than Event-Customized / Subject-Diffusion and weaker than RB-Modulation / IC-Light.

**Round 2 narrowing**: The paper is somewhat better than UIFace (6.00) and ClassDiffusion (6.25), comparable to InstantPortrait (6.67), and clearly below One-Prompt-One-Story (7.40). The sloppy user study presentation and the metric circularity concern weigh it down relative to InstantPortrait. Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>