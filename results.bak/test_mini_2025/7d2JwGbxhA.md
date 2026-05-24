Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

OCEBO proposes the first framework for pretraining object-centric models from scratch on real-world data, without relying on a frozen pretrained foundation model for reconstruction targets. It formulates object-centric learning as a self-distillation problem where the target encoder is updated as an EMA of the object-centric encoder (enriching it with object-centric inductive biases), and introduces a cross-view patch filtering mechanism to prevent slot collapse from random initialization. On zero-shot object discovery benchmarks, OCEBO trained on 241k COCO images achieves performance competitive with models using DINOv2 target encoders pretrained on 142M images, while demonstrating data scalability that prior object-centric models lack.

## Strengths

- **First demonstration of object-centric pretraining from scratch on real-world data.** The paper shows conclusively (Table 1) that OCEBO avoids slot collapse (d=0.13) and achieves meaningful object discovery on MOVi-E (54.8 FG-ARI) and EntitySeg (41.5 FG-ARI) without any external pretrained encoder. Section 4.3 further contextualizes this against models that rely on DINO/DINOv2 target encoders pretrained on orders of magnitude more data.

- **Cross-view patch filtering is a well-motivated and empirically validated collapse-prevention mechanism.** Table 1(a) shows that removing patch filtering causes immediate slot collapse (d drops from 0.13 to 0.02). Figure 2 provides direct evidence of the mechanism: in early training only ~10% of patches satisfy the filtering condition, preventing the model from being supervised by noisy random features, with the percentage gradually rising to ~70%.

- **Object-centric inductive biases in the target encoder are shown to be beneficial.** Table 1(b) demonstrates that setting λ_oc=0 (removing the object-centric loss, reducing to DINO-style pretraining + FT-DINOSAUR) causes collapse (d=0.02). Figure 3 provides compelling PCA visualizations where OCEBO's target encoder separates object instances (bear vs. human) while DINOv2 groups them semantically.

- **Data scalability is demonstrated beyond prior object-centric models.** Table 1(d) shows that scaling from 118k (COCO) to 241k images (COCO+) improves FG-ARI on MOVi-E from 54.8 to 66.8 and on EntitySeg from 41.5 to 44.2. Section 4.2 explicitly contrasts this with the saturation behavior of prior methods at ~16k images (cited from Didolkar et al., 2024).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Central claim is slightly overstated.** The abstract and introduction repeatedly use "comparable" to describe OCEBO's performance relative to models with DINOv2 target encoders (e.g., "achieves unsupervised object discovery performance comparable to that of object-centric models with frozen non-object-centric target encoders pretrained on hundreds of millions of images"). However, Table 2 shows OCEBO trails FT-DINOSAUR on every dataset and metric — sometimes substantially (EntitySeg mBO: 16.0 vs. 28.4, a 43% relative gap). While the paper acknowledges the data disparity in Section 4.3 and qualifies that "the models are not directly comparable," the word "comparable" in the abstract and conclusion overstates the case. Reframing to "competitive given the data scale" or "closes a substantial portion of the gap" would be more accurate.

2. **No variance or multiple-seed reporting.** All results (Tables 1 and 2) are reported as single numbers with no indication of whether they come from one run or multiple seeds. Given the stochasticity of training (random augmentations, slot attention initialization), the reader cannot assess whether the reported improvements (e.g., COCO+ over COCO) are stable. This is a basic expectation for empirical papers in this community and would be the single highest-leverage addition.

3. **Backbone size mismatch with baselines is not discussed.** OCEBO uses ViT-S/16, while the compared models (DINOSAUR, FT-DINOSAUR) use ViT-B/16 or ViT-B/14 backbones from Didolkar et al. (2024). The paper acknowledges that "the models are not directly comparable" but attributes this only to pretraining data disparity, not backbone capacity. A larger backbone typically produces better features even at equivalent training data. The paper should at minimum acknowledge this limitation and discuss its impact on the comparison.

4. **The value of k in cross-view patch filtering is not specified.** Equation (7) defines `nns_k` for nearest-neighbor matching, but the paper never reports the value of k used in experiments. This is an essential hyperparameter for reproducibility. An ablation of k would also strengthen the paper (only "w/o patch filtering" is currently ablated).

5. **It is not explicitly stated whether Table 2 uses the sharpened or non-sharpened version of OCEBO.** Table 1(c) shows that the sharpening stage improves performance (e.g., MOVi-E FG-ARI from 44.0 to 54.8). The paper says OCEBO is trained "for 300 epochs with an additional mask sharpening stage of 100 epochs" (Section 4.1), and the COCO+ row in Table 1(d) presumably includes sharpening — but this is never stated for Table 2. The reader has to infer this from matching numbers between tables.

### Trivial

- The measure d for slot collapse (Section 4.2) is presented without any validation that it correlates with qualitative observations of collapse. It is a reasonable diagnostic but the paper does not show, e.g., a comparison of d values between collapsed and non-collapsed models against visual inspections. This would be easy to add.

## Nice-to-Haves

- An ablation of the k hyperparameter in patch filtering would help establish robustness.
- A controlled comparison using a ViT-S/16 backbone for the strongest baseline (FT-DINOSAUR) would isolate the advantage of object-centric inductive biases from backbone capacity.
- Clarifying the ℓ₂ reconstruction loss details in the sharpening stage (applied to projection-head features or direct patch features?) would aid reproducibility.

## Removed Points

- **SPOT comparison undermines decoder claim** (Harsh Critic): The critic argued that the paper's claim about autoregressive decoders increasing mBO at the cost of FG-ARI is undermined because SPOT shows higher mBO and similar/higher FG-ARI than OCEBO. This misunderstands the paper's claim — the paper discusses decoder architectural trends generally (SPOT vs. DINOSAUR), not SPOT vs. OCEBO specifically. The paper's observation about MLP decoders vs. autoregressive decoders is a general architectural discussion, and the critic's comparison to OCEBO is not relevant to that claim. **Removed.**

- **"d" measure lacks validation** (Harsh Critic, Missing Parts): This is kept as Trivial above rather than a substantive weakness, as the d measure is a supplementary diagnostic. The paper's core claims do not depend on it. **Demoted to Trivial.**

- **Decoder claim asserted without evidence** (Harsh Critic): The paper states "models such as DINOSAUR... attain higher FG-ARI at the cost of mBO due to the use of an MLP-based decoder." This is a general observation about architectural trends and OCEBO does exhibit this same pattern. The critic's argument that "since OCEBO also uses an MLP decoder, the lower mBO cannot be attributed solely to the decoder choice" conflates cross-model comparison (DINOSAUR vs. SPOT) with within-model attribution. **Removed.**

- **General "evaluation lacks rigor" / "evidence is weak" framing** (from both reviewers): These are area-of-concern sweeps rather than specific identified problems. Specific instantiations (no variance, backbone mismatch, missing k) are kept in Minor above. **Removed.**

- **Generic/superficial strengths** from Strength Finder: "The paper addressed an important problem," "this paper targeted an interesting question" — these are generic and not specific to the paper's content. **Removed.**

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the harsh critic flags the "comparable" framing as overclaiming, but this same framing is what makes the paper provocative — it forces the reader to compare a model trained from scratch on 241k images against models bootstrapped from 142M-image foundation models. The fact that this tension exists at all is evidence of the paper's significance. A sharper framing ("competitive given resource disparity" rather than "comparable") would resolve the tension without weakening the paper's message.

## Suggestions

1. Reframe "comparable" to "competitive" or "closes the gap significantly" throughout, and add a sentence in the abstract or conclusion explicitly noting the data and backbone disparities.
2. Report mean and standard deviation over 3 seeds for at least the main results (Tables 1 and 2).
3. Add a sentence explicitly stating the backbone sizes of the compared methods and discussing the limitation.
4. Specify the value of k used in Equation (7), and ideally provide an ablation in the appendix.
5. Explicitly state in the Table 2 caption which OCEBO variant (sharpened/non-sharpened and which data split) the numbers correspond to.

## Score and Decision

**Round 1 bracket (Bracketing pass):** I queried three bands: weak anchors (avg < 3.5), middle anchors (3.5–7.5), and strong anchors (>7.5). The weak anchors (avg 3.0, rejected/withdrawn papers) are clearly below OCEBO's quality. The middle anchors include Grounded Object-Centric Learning (avg 6.0, poster), Slot Mixture Module (avg 6.25, poster), and Slot-Guided Adaptation (avg 6.25, poster). The strong anchors include CrIBo (avg 8.0, spotlight), which has more extensive experiments than OCEBO. Initial bracket: **5–6.5**.

**Round 2 narrowing:** I queried within the bracket for object-centric pretraining papers and reviewed Grounded OC Learning (6.0, accepted poster), Slot Mixture Module (6.25, accepted poster), and Slot-Guided Adaptation (6.25, accepted poster). OCEBO has a bolder contribution than these (enabling a new capability — training from scratch on real data — rather than an incremental architectural improvement) but has more experimental gaps (no variance, missing k, backbone mismatch not discussed). It is clearly stronger than the withdrawn papers (SlotSAM at 4.5) but not as polished as CrIBo (8.0). The paper's quality is comparable to the Grounded OC Learning paper (all-reviers-at-6) and slightly below the Slot Mixture Module paper (5,8,6,6). Given the novelty of the contribution balanced against the experimental gaps, I place OCEBO at the lower end of the accepted-poster range for this topic.

**Anchors consulted:**
- 2HdZPEQUig.md (avg 3.0, withdrawn) — rejected video OC paper, well below OCEBO
- aBUidW4Nkd.md (avg 6.25, poster) — Slot Mixture Module; comparable level, OCEBO has more novelty but fewer ablations
- DD11okKg13.md (avg 6.0, poster) — OC representations in VQA; OCEBO has stronger methodological contribution
- pBxeZ6pVUD.md (avg 6.0, poster) — Grounded OC Learning; OCEBO is similar in quality, slightly more novel
- kZvor5aaz7.md (avg 6.25, poster) — SlotAdapt; similar issues with overclaiming, OCEBO comparable
- Pq2yEKXOl7.md (avg 4.5, withdrawn) — SlotSAM; OCEBO clearly stronger
- 3M0GXoUEzP.md (avg 8.0, spotlight) — CrIBo; OCEBO not at this level of experimental thoroughness

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>