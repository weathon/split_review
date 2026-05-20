Now let me compile the final review.

## Summary

This paper proposes CaPT (CLIP as a Prior Teacher), a co-training framework that integrates CLIP into semi-supervised learning (SSL) by jointly training a fully fine-tuned unimodal vision network and a parameter-efficiently adapter-tuned multimodal CLIP model. The two models exchange information via entropy-weighted co-pseudo labels. The paper also provides a theoretical analysis (Theorem 1.1) formalizing how labeled data quantity and quality bound pseudo-label accuracy in SSL, motivating the need to break this dependency. CaPT achieves strong empirical results across multiple SSL benchmarks (USB, ImageNet, fine-grained datasets), with particularly large gains under extreme label scarcity (e.g., +21.38% on CIFAR-100 with 1 label per class).

## Strengths

1. **Large empirical gains under extreme label scarcity** (Table 3, Section 4.3): CaPT outperforms the second-best method by 21.38% on CIFAR-100 and 4.05% on EuroSAT with only one labeled sample per class. These results directly support the paper's central claim of reducing SSL's label dependency.

2. **Efficient CLIP integration** (Table 4, Section 4.3): CaPT adds only 8.00% extra memory and 11.18% additional training time over FreeMatch while achieving significantly higher accuracy. This demonstrates practicality rather than computational burden.

3. **Systematic ablation validating design choices** (Table 6, Section 4.5): The ablation decomposes CaPT into meaningful variants (CaPT-Ada, CaPT-Deb, CaPT-Uni, only UPM, only MPM, w/o feat aug., equal weights), quantifying each component's contribution. This confirms that bidirectional information flow and adapter-tuning are both essential.

4. **Asymmetric-modalities design with visual evidence** (Figure 3, Section 1): Attention maps show that CLIP (with text context) focuses on different object parts than pure-vision ViTs, supporting the claim that cross-modal complementarity enriches co-training beyond what homogeneous vision-model co-training (e.g., CLS) can achieve.

5. **Theoretical formalization of label dependency** (Theorem 1.1, Section 1): The bound relating pseudo-label error to prototype bias *B* and labeled sample size (via εₙ) provides a formal grounding for why SSL degrades under poor labeled data, motivating the need for external prior knowledge.

## Weaknesses

### Fatal
None.

### Major

1. **No experimental comparison with prior CLIP+SSL methods (DebiasPL, CLS).** The paper discusses DebiasPL (Wang et al., 2022a) and CLS (Yao et al., 2022) in the Introduction and Related Work (lines 41, 55, 81), and Figures 2a–c contrast CaPT with these frameworks conceptually. However, none of the experimental tables include these methods. While the CaPT-Deb ablation (Table 6) approximates one aspect of DebiasPL, and the CaPT-Uni variant tests unidirectional CLIP→vision flow, neither is a direct substitute for running the original methods under the same protocol. The paper claims "state-of-the-art performance" among SSL methods, but since CaPT's core novelty is a new way to integrate CLIP into SSL, the omission of direct comparisons with existing CLIP+SSL methods weakens this claim's support. The authors should either include these baselines or explicitly explain why they are not feasible (e.g., incompatible benchmark protocols), and discuss how the ablation variants relate to these prior methods.

### Minor

1. **STL-10 anomaly: adapter-tuned CLIP alone outperforms CaPT on two settings.** In Table 1, on STL-10 with 4 labels per class, adapter-tuned CLIP achieves 96.86% while CaPT achieves 96.07%. With 10 labels, adapter-tuned CLIP achieves 97.15% vs CaPT's 96.34%. Zero-shot CLIP itself scores 97.18%. The paper reports CaPT's performance using the fully fine-tuned unimodal network (line 210), so this result does not contradict the claim that CaPT improves over standard SSL methods (CaPT's 96.07% vs RegMixMatch's 89.89% on 4-label STL-10). However, it does raise a question: on datasets where CLIP's zero-shot performance is already very strong, the co-training mechanism may not improve—and could even slightly degrade—the unimodal network relative to what it would learn from CLIP-derived pseudo labels alone. The paper does not discuss this finding. Adding a brief explanation (e.g., whether this is a known limitation and when practitioners should expect it) would strengthen the paper.

2. **Theorem 1.1 motivates the problem but does not analyze CaPT itself.** The bound applies to any nearest-prototype pseudo-labeler under a prototype-based GMM (line 23). It cannot distinguish between FreeMatch and CaPT. While it is reasonable to use theory to formally establish the label-dependency problem that CaPT aims to solve, the paper would be strengthened by an analysis showing how CaPT's co-training mechanism affects one of the relevant quantities (e.g., reducing effective bias *B* or increasing the effective margin *g*/2 − *r*). Without this, the theory and method remain loosely coupled.

### Trivial
None.

## Nice-to-Haves

- A plot showing how the entropy-based weights Γ^a and Γ^b evolve over training would validate the claim that CLIP dominates early and the unimodal network takes over later.
- A quantitative measure of representation diversity (e.g., CKA similarity) between the two models' features over the course of training could substantiate the asymmetric-modalities claim beyond the qualitative attention maps in Figure 3.

## Removed Points

- **Missing implementation details (threshold, α, batch size):** The paper states "We adopt the adaptive threshold strategy from FreeMatch to filter pseudo labels" (line 210) and references Appendix F for detailed configurations. The parser strips appendix content; these details exist in the original submission. Per hard rules, removed.
- **ViT-B/32 vs ViT-B/16 architectural mismatch critique:** The unimodal network uses the same backbone as USB (ViT-B/16), and SSL baselines likewise use this backbone. CLIP's ViT-B/32 is used only for the MPM branch, which is supplementary to the unimodal network. Comparisons between CaPT and SSL baselines are fair since both use the same UPM backbone. Removed.
- **"The paper should report CLIP-B/16 results":** The paper states "Unless otherwise stated, ViT-B/32 is employed as the visual encoder for CLIP" (line 210). This is a design choice, not an error. Removed.
- **Pure formatting/style nitpicks and reproducibility concerns about undisclosed hyperparameters:** Per hard rules, removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Run DebiasPL and CLS under the USB protocol, or explicitly document why they cannot be run (e.g., DebiasPL's need for a separate labeled validation set) and discuss how the CaPT-Deb and CaPT-Uni ablations relate to these methods.
2. Add a brief discussion of the STL-10 result, explaining when the co-training framework may not improve over CLIP alone and whether a simple diagnostic (e.g., comparing adapter-tuned CLIP accuracy to the unimodal network's early-stage accuracy) could help practitioners decide.
3. Strengthen the connection between Theorem 1.1 and CaPT by analyzing how the co-pseudo label mechanism reduces the effective bias *B* or increases the effective margin relative to unimodal SSL.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor path | Avg score | Round | Comparison |
|---|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/R6I8P4DuRf.md` (Adaptively Labeling Vision Datasets) | 3.20 | R1 (weak) | Irrelevant topic; much weaker paper |
| `/home/wg25r/review_agent/human_reviews_2026/6TwQVKNnYy.md` (CLIP + Paraphrasing/Negation) | 2.00 | R1 (weak) | Irrelevant topic; much weaker |
| `/home/wg25r/review_agent/human_reviews_2026/99K0EoKrCu.md` (CLESP, pseudo-labels) | 2.50 | R1 (weak) | Much weaker paper |
| `/home/wg25r/review_agent/human_reviews_2026/CSeX6I85Bp.md` (Can Models Learn From Arbitrary Pairs) | 3.00 | R1 (weak) | Much weaker paper |
| `/home/wg25r/review_agent/human_reviews_2026/8B1vsFiLin.md` (CoT-PL, VLM pseudo-labels for OVD) | 5.00 | R1 (mid) | Different task (OVD vs SSL); CaPT has stronger evaluation scope |
| `/home/wg25r/review_agent/human_reviews_2026/fwMEqaKgTd.md` (Unlabeled Data vs Pre-trained Knowledge) | 4.67 | R1 (mid) | Position paper with no method; CaPT is substantially stronger |
| `/home/wg25r/review_agent/human_reviews_2026/ivaIwRZvTT.md` (DPC, CISSL) | 4.50 | R1 (mid) | Incremental decoupling approach; CaPT has stronger novelty and results |
| `/home/wg25r/review_agent/human_reviews_2026/H4RVXhicSj.md` (CLOP, SSL + prototypes) | 5.00 | R1 (mid) | Similar-level SSL method; CaPT has broader evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/zS1bPtMlt9.md` (RePL, LiDAR SSL) | 6.00 | R2 (narrow) | Solid SSL method with narrower domain scope; CaPT comparable quality, broader evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/7D7VLU9227.md` (PSP, CLIP active learning) | 6.00 | R2 (narrow) | CLIP + active learning, different setting; CaPT has stronger contribution |
| `/home/wg25r/review_agent/human_reviews_2026/UUAjF4xL0e.md` (CS-Aligner, VLM alignment) | 6.50 | R2 (narrow) | VLM alignment, different problem; CaPT comparable |
| `/home/wg25r/review_agent/human_reviews_2026/bZqCBgm2N0.md` (Latent Partial Causal Model) | 6.50 | R2 (narrow) | Causal multimodal learning; different problem |
| `/home/wg25r/review_agent/human_reviews_2026/pfw176o1YJ.md` (LLM Visual Priors) | 7.00 | R2 (narrow) | Strong oral paper; CaPT is slightly below this level |

**Round 1 bracket:** [3.5, 7.5] with the paper clearly above the 4-5 range and below the 8+ oral range.

**Narrowing (Round 2):** Compared against papers scoring 6.0-7.0, CaPT has a stronger and broader evaluation than RePL (6.00, domain-specific SSL) and PSP (6.00, active learning), and is comparable to CS-Aligner (6.50). It is slightly below LLM Visual Priors (7.00, oral track) in terms of depth of analysis. Within this band, CaPT sits near the top end.

**Final score:** 6.5 — The paper presents a novel and well-motivated method with extensive empirical validation across diverse benchmarks. The weaknesses (missing CLIP+SSL baselines, undiscussed STL-10 result) are real but addressable and do not undermine the core contribution. The paper is clearly above the typical 5-point reject range and warrants acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>