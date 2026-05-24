## Summary

This paper introduces LAION-Comp, a large-scale dataset of 540K+ scene-graph annotations over high-aesthetic images from LAION, built via GPT-4o with partial human verification. The authors train four scene-graph-conditioned diffusion/flow-matching models (SDXL-SG, SD3.5-SG, FLUX-SG, etc.) using a GNN-based scene-graph encoder and evaluate them on a new CompSGen Bench (20,838 complex-scene samples). Results show consistent improvements over text-only baselines and prior SG2IM models trained on COCO/VG. A training-free editing framework is mentioned but deferred to the appendix.

---

## Strengths

- **Substantial dataset contribution with demonstrated annotation quality advantage.** Table 1 and Figure 3 show that LAION-Comp annotations capture 20% more objects (216% excluding proper nouns), are ~70% longer, and achieve markedly higher accuracy (SG-IoU⁺ 0.422 vs. 0.306) compared to original LAION captions. The relation-type distribution analysis (77.5% non-spatial vs. VG's 42.0%) convincingly demonstrates richer semantic coverage.

- **Consistent empirical gains across diverse architectures and datasets.** Table 2 shows SDXL-SG trained on LAION-Comp achieves 0.558 SG-IoU and 0.856 Rel-IoU, outperforming the same model trained on COCO (0.497, 0.833) and VG (0.546, 0.800). FLUX-SG reaches 0.583 SG-IoU. The gains persist across SD1.5, SDXL, SD3.5, and FLUX backbones (Tables 2–3), demonstrating that the dataset and encoder design generalize across generative paradigms.

- **Well-designed benchmark that isolates complex compositional capability.** CompSGen Bench's selection of samples with >4 relations (20,838 samples) targets precisely the regime where prior models fail. The multi-metric evaluation (FID, CLIP, SG-IoU, Entity-IoU, Relation-IoU) provides a comprehensive picture of both image quality and compositional faithfulness.

- **Ablation study credibly links annotation quality to performance.** Table 4's scaling experiment shows monotonic improvement with increasing data proportion. Even 10% of LAION-Comp (smaller than VG in volume) yields better Entity-IoU and Rel-IoU than full VG training for SDXL-SG.

- **Modular GNN encoder with learnable scaling factor α (Eq. 1) is architecturally clean and effective.** The design of initializing α at zero for training stability is a sensible practical choice, and the encoder plugs into both diffusion and flow-matching backbones.

---

## Weaknesses

### Fatal
None.

### Major

- **The paper's central claim — that structural annotations (scene graphs) are what drive the improvement, rather than simply richer annotation content — is not isolated or tested.** The comparisons pit SG-trained models against (a) sparse/noisy original LAION captions and (b) smaller SG datasets (COCO, VG). No experiment disentangles annotation *format* from annotation *quality*. A critical ablation — training a T2I model on equally rich textual descriptions linearized from the same scene graphs (e.g., "A young male person holding a small rectangular book beside a tall wooden table…") — is absent. Without it, the paper's headline statement that "structural annotations are crucial for advancing compositional generation" overreaches. The evidence supports that *better annotations help*, but not necessarily that the *graph structure* is the active ingredient. This weakens the paper's core thesis even though the dataset and models remain valuable.

### Minor

- **Factual error in the 10% ablation claim.** Section 5.2 states that at 10% LAION-Comp, "the model's FID and Entity-IoU scores still outperform the results trained on VG." Comparing Table 4 (10% SDXL-SG: FID=27.3, Ent-IoU=0.874) with Table 2 (VG SDXL-SG: FID=21.9, Ent-IoU=0.813): Entity-IoU is indeed better, but FID is *worse* (27.3 > 21.9; lower is better for FID). The claim should be corrected to reflect that only Entity-IoU and Rel-IoU improve, while FID and SG-IoU are worse at 10%.

- **The editing framework is listed as a core contribution (abstract, introduction) but has no description or evaluation in the main paper.** The main text merely references Sec. A.1 for the entire editing framework. If page limits preclude inclusion, the contribution list and abstract should be tempered accordingly; as written, the claimed contribution is invisible to a main-paper reader.

- **Method description in Section 4 lacks key architectural specifics.** While the GNN and α-scaling are introduced, the paper does not specify how the SG embedding is physically integrated into the generative backbone (cross-attention? concatenation to the timestep embedding? prefix tokens?). The text refers to Sec. A.9.3–A.9.4, but the main paper should at minimum state the integration mechanism (e.g., "via additional cross-attention layers").

- **T2I baselines on CompSGen Bench (Table 3) lack a described prompt protocol.** It is unclear how T2I models receive prompts from the SG-based test set. The comparison direction (SG2IM > T2I) is unsurprising, but for completeness the paper should explain whether T2I models used original captions, linearized scene graphs, or some other conversion.

- **No limitations section.** The paper contains no discussion of dataset biases inherited from LAION and GPT-4o, potential annotation noise, failure cases, or ethical considerations. A brief limitations paragraph is expected.

### Trivial

- The phrase "SG-IoU⁺" etc. is introduced in Table 1 but never defined in the main text; the reader must consult Sec. A.2.

---

## Nice-to-Haves

- A text-linearization baseline (SG → fluent text → same T2I backbone) to test whether the SG format itself matters beyond content quality. This is the single experiment that would most strengthen the paper.
- Brief qualitative examples of the editing framework in the main paper, or removal of editing from the abstract/contributions if space is too tight.
- Discussion of the external scene-graph parser used for SG-IoU metrics, including its known limitations.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Annotation quality numbers seem unrealistically high"** — This is speculation. The paper reports 98.8%/97.5%/95.7% accuracy and references Sec. A.5 for protocol details. Without seeing the appendix, declaring the numbers untrustworthy is conjecture, not an identified flaw. *Removed.*

- **"CLIP score is not a standard measure of compositional fidelity"** — Using CLIP for image-image similarity (cosine similarity between CLIP image embeddings of generated and ground-truth images) is a well-established practice. The paper's description is slightly imprecise but the metric itself is valid. *Removed.*

- **"SG-IoU metrics rely on an external parser whose accuracy is not assessed"** — The metrics follow Shen et al. 2024, and parser error would affect all compared methods equally, preserving relative rankings. This is speculative methodology criticism without concrete evidence of bias. *Removed.*

- **"T2I comparison in Table 3 is not meaningful"** — The comparison shows SG2IM models outperform T2I models on an SG-based benchmark. This is the expected outcome and still informative. The paper is not making an unfair comparison; it's demonstrating what structured conditioning enables. *Removed.*

- **"Should cite RPG, LayoutGPT"** — These are tangentially related and their absence does not weaken the paper's contribution. The paper already covers LLM-assisted layout methods. *Removed.*

- **Demand for inter-annotator agreement, sample size, annotator training details in the main text** — The paper clearly points to Sec. A.5 for verification details. A main-paper summary is reasonable given page constraints. *Removed.*

- **"The assertion that existing models fail not because of architecture but data is an overstatement"** — The paper qualifies this with evidence (SG models trained on better data outperform text models), and the claim is about datasets being a *fundamental* bottleneck, not the *only* bottleneck. *Removed.*

---

## Novel Insights

The paper's analysis of relation-type distributions (77.5% non-spatial in LAION-Comp vs. 42.0% in VG) provides concrete quantitative evidence for a well-known qualitative intuition: existing SG datasets over-emphasize spatial relations while real-world compositional generation requires functional/interaction semantics. This distributional characterization is a useful lens for future dataset design.

---

## Suggestions

- Add a text-linearization baseline: convert scene graphs to fluent text descriptions preserving all object/attribute/relation content, train a T2I model on these, and evaluate on CompSGen Bench. This directly tests whether the graph format matters.
- Correct the FID comparison in the 10% ablation claim.
- Either include a one-paragraph summary and qualitative example of the editing framework in the main paper, or remove it from the abstract and contribution list.
- Add a brief limitations paragraph covering dataset biases, annotation noise, and failure modes.
- State explicitly in Section 4 how the SG embedding is fed into the backbone (e.g., cross-attention, prefix-conditioning).

---

## Score and Decision

**Round 1 bracket:** Compared to SG-Adapter (5.50, directly comparable SG2IM work with smaller scope) and ISG (7.20, strong benchmark paper), the paper sits plausibly in **6.0–7.5**.

**Round 2 narrowing:** Compared to SlotAdapt (6.25, object-centric diffusion with compositional generation) and "Enhancing Compositional T2I with Reliable Random Seeds" (7.33, clever compositional improvement method), this paper is stronger than SlotAdapt in scale and comprehensiveness but slightly below the seed paper in methodological novelty and tightness of its central experimental claim. The missing text-linearization ablation prevents the paper from fully substantiating its thesis that *structural* annotations are the key factor, though the practical value of the dataset and models is well demonstrated.

**Anchors consulted:**
- `KCYDpqSpqg` (SG-Adapter, 5.50, Round 1): Directly comparable prior work; our paper is substantially broader and stronger.
- `rDLgnYLM5b` (ISG, 7.20, Round 1): Strong scene-graph-based benchmark paper; comparable quality, different emphasis.
- `0YXckVo7Kw` (MMComposition, 5.50, Round 1): Compositional benchmark; our paper is stronger.
- `kZvor5aaz7` (SlotAdapt, 6.25, Round 2): Object-centric diffusion for compositional generation; our paper is more comprehensive.
- `5BSlakturs` (Reliable Random Seeds, 7.33, Round 2): Clever compositional improvement; our paper has broader scope but less tight central evidence.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>