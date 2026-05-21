---
job_id: 5ed31c03-ba83-4d99-be6f-3f48dc511ed8
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 7L7kmHHfgf.pdf
paper: PIRN: Prototypical-Based Intra-Modal Reconstruction with Normality Communication for Multimodal Anomaly Detection
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on multimodal representation learning and unsupervised anomaly detection with prototype-based reconstruction and cross-modal interaction.

## Minimum Quality
Pass ✅. The submission includes all expected components, abstract, introduction, related work, method, experiments/results, and conclusion, and presents a non-trivial methodological contribution with substantial empirical evaluation, despite several clarity and rigor issues discussed below.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes PIRN, a prototype-based framework for few-shot multimodal anomaly detection using RGB images and surface-normal maps. The method combines three components, Balanced Prototype Assignment (BPA) based on balanced optimal transport, Adaptive Prototype Refinement (APR) that updates prototypes at inference, and Multimodal Normality Communication (MNC) that exchanges prototype-level information across modalities. Experiments on MVTec-3D-AD, Eyecandies, and Real-IAD D3 show improved performance over several multimodal anomaly detection baselines, especially in low-shot settings.

## Strengths
1. The paper addresses a meaningful problem setting, few-shot multimodal anomaly detection, where many existing MAD methods indeed become brittle. This is a practically relevant regime, and the motivation in Sections 1 and 4 is easy to appreciate.

2. The overall design is coherent. The three components are not just a loose pile of modules, they are tied to concrete failure modes: BPA for codebook collapse, APR for train-test normality gap, and MNC for leveraging complementary RGB and geometry cues. Even if some details need tightening, the conceptual pipeline is sensible.

3. The empirical results are strong on the main benchmarks. In **Table 1** on Page 8, PIRN improves over the listed baselines across 5-shot, 10-shot, 30-shot, and all-data settings on both MVTec-3D-AD and Eyecandies. The gains are especially noticeable in few-shot image-level AUROC, which supports the central claim that the method is useful under scarce normal training data.

4. The ablation study is reasonably informative. **Table 2** shows that removing BPA, APR, or MNC hurts performance in the 10-shot MVTec-3D-AD setting, and the full model performs best. **Tables 5, 6, and 7** further probe prototype count, decoder depth, and APR aggregation strategy. This is useful because the method introduces several moving parts.

5. The paper includes qualitative evidence that is actually relevant to the claim, rather than decorative. In **Figure 1** on Page 2, the left plot clearly communicates the intended regime, very small fractions of training data, and the right t-SNE visualization gives an intuitive picture of how BPA spreads prototype usage better than softmax assignment. Likewise, **Figure 3** on Page 7 shows sharper anomaly maps and cleaner score separation than selected baselines, which matches the quantitative trend.

6. The efficiency comparison in **Table 4** on Page 9 is a nice addition. If those numbers are computed under matched settings, then PIRN is not only stronger than the listed baselines in 10-shot accuracy but also considerably cheaper than FIND and CFM. That improves the practical value of the method.

7. The prototype-centered formulation is a plausible alternative to dense cross-modal alignment in low-data regimes. This is a reasonable modeling choice, and the paper explains that motivation well.

## Weaknesses
1. **The mathematical specification is weaker than it should be, and in a few places internally inconsistent.**  
   The core OT formulation in **Equation (1)** on Page 5 uses constraints \(T\mathbf{1}_K=\mathbf{a}\) with \(\mathbf{a}=\mathbf{1}_N\) and \(T^\top \mathbf{1}_N=\mathbf{b}\) with \(\mathbf{b}=\frac{N}{K}\mathbf{1}_K\). This enforces each token to transport exactly unit mass and each prototype to receive exactly \(N/K\) total mass. That is a perfectly valid balanced OT setup, but the paper then repeatedly describes the resulting assignment as encouraging tokens to "concentrate mass on only a few prototypes" through the cost and entropic regularization. With standard entropic OT, larger regularization pushes the solution toward *more diffuse* transport, not more selective transport. The paper never specifies the regularization coefficient \(\varepsilon\), nor how it is chosen, nor whether sparsity is induced by low \(\varepsilon\) or by an additional constraint. This matters because the claimed mechanism of BPA depends directly on these properties.  
   There is also a notation mismatch: **Equation (2)** defines \(s_n^{\text{bpa}}=\sum_k T_{nk}^* p_k\), but the text immediately after says “We refer to \(\mathbf{Z}^{\text{bpa}}=\{z_n^{\text{bpa}}\}_{n=1}^N\),” switching from \(s_n^{\text{bpa}}\) to \(z_n^{\text{bpa}}\) without explanation. Later, on Page 7, the paper uses \(\mathbf{Z}^{\mathrm{lopa}}\) in the final fusion equations even though BPA introduced \(\mathbf{Z}^{\text{bpa}}\). This is not a cosmetic issue, it makes the actual decoder states hard to follow.

2. **APR’s robustness argument is intuitive but not technically established, and the update rule is underspecified in the main paper.**  
   Section 3.3 claims that anomalous patches “tend to be assigned more diffusely across prototypes” and therefore contribute weakly to prototype contexts. That may happen in favorable cases, but it is not guaranteed by the balanced OT formulation itself. Under the hard marginal constraints in **Equation (1)**, each prototype must receive mass, which means anomalous tokens can still influence contexts if the normal tokens are insufficient or ambiguous. The main paper does not quantify when this diffusion claim holds, nor how much anomaly contamination APR can tolerate.  
   More importantly, the GRU update is only described verbally in the main text on Pages 5 to 6; the actual equations only appear in the appendix. Since APR is one of the three headline contributions, the update equations should be summarized in the main paper. Without them, the reader cannot assess what “gating” mathematically means or whether the update is per-prototype, shared across layers, or parameter-tied across modalities. The claim that the GRU “restricts the integration of unreliable anomalous contexts” is therefore more asserted than demonstrated.

3. **The training objective is not specified with enough precision for a method paper.**  
   On Page 7, the paper says “We train PIRN end-to-end using an intra-modal feature reconstruction loss, e.g., a soft mining loss (Luo et al., 2025). In practice, we minimize the cosine distance...” This is ambiguous. Is the actual loss just average cosine distance between encoder and reconstruction? Is “soft mining loss” used or not used? If yes, what are the mining weights, temperatures, thresholds, or hard/easy sample definitions? If no, why mention it here?  
   This matters because the optimization objective is central for anomaly reconstruction methods. Also, the paper uses both intra-modal reconstructed features and cross-modal purified features, but there is no explicit auxiliary loss for prototype alignment, gating regularization, or APR stability. If the system trains reliably with only the reconstruction loss, that should be stated clearly and formally as something like
   \[
   \mathcal{L}=\sum_{m\in\{\mathrm{rgb},\mathrm{sn}\}}\frac{1}{N}\sum_{i=1}^N\left(1-\cos(E_i^{(m)}, Z_{i,\mathrm{rec}}^{(m)})\right).
   \]
   Right now, the objective is described too vaguely for a paper whose main contribution is an architectural and optimization design.

4. **Several experimental details raise fairness and reproducibility questions, especially around baseline comparison.**  
   The baseline list in Section 4 includes methods with inconsistent naming, for example the text mentions BTF and CFM, while **Table 1** reports “RTF” and “CPM,” which appear to be typographical errors. This may sound minor, but when benchmark tables are the main evidence, naming mistakes undermine confidence in whether the correct implementations and reported numbers were used.  
   More substantively, the adapted “INP-Former” multimodal baseline is described only briefly on Page 8. Since INP-Former is originally a 2D method, adapting it to a two-stream multimodal setup introduces design choices that can materially affect results. The paper states that each branch processes RGB or surface normal maps independently and the anomaly maps are fused by summation, but does not specify whether prototype counts, decoder depths, training epochs, and tuning budget were matched to PIRN. Because INP-Former is the strongest baseline in **Table 1**, this comparison needs more detail to be convincing.  
   I also would have liked a direct comparison to a simpler prototype-only multimodal baseline, for example “BPA only,” or “APR+BPA without MNC,” across more than one shot regime. **Table 2** is helpful, but it reports only 10-shot MVTec-3D-AD and uses shorthand “S” / “✓” that is not immediately self-explanatory.

5. **The paper overstates novelty relative to the broader prototype-based AD literature and does not fully position itself against the closest multimodal prototype alternatives.**  
   The authors claim in Section 3.1 that PIRN is “the first multimodal anomaly detection framework to integrate a vector-quantized prototype codebook into a ViT encoder-decoder architecture.” That may be technically true under a very specific wording, but it is a narrow novelty claim. The broader contribution is better described as combining prototype-based reconstruction, test-time prototype refinement, and cross-modal communication for MAD. Since the paper itself cites recent 2D prototype-based AD methods and a 2025 cross-modal prototype method (Mao et al., 2025), the exact boundary of novelty should be stated more carefully.  
   As written, the positioning sometimes reads as if prototype-based reconstruction is absent in multimodal AD except for this work, which is too strong.

6. **Some of the presentation is rough enough to impede technical trust, especially in tables and notation.**  
   There are many naming/formatting issues: “INP-Fermer” in **Table 1**, “AUROC1” / “AUROC1P” in **Tables 4 to 7**, “ACROC1” / “AVROC2” in **Table 8**, and inconsistent references to 30-shot vs 50-shot in the text below **Table 1**. The Real-IAD D3 table on Page 10 is particularly hard to parse. Even if the intended meaning can be guessed, this level of sloppiness is problematic in a conference paper because it makes it difficult to verify claims and can hide genuine mistakes.  
   The architecture figure, **Figure 2** on Page 3, is visually helpful at a high level, but it also exposes the notation inconsistency: the figure labels mention \(\mathbf{Z}^{\mathrm{lopa}}\) while the method section mostly uses \(\mathbf{Z}^{\text{bpa}}\). Readers should not have to reverse-engineer whether these are the same tensor.

7. **The evidence for MNC helping because of cross-modal communication, rather than simply because of added capacity, is suggestive but not fully isolated.**  
   **Table 3** on Page 8 shows that RGB+surface normals outperforms single-modality variants, which is unsurprising. What it does not fully disentangle is whether the gain comes from the specific MNC mechanism or simply from having both modalities and fusing anomaly maps. Since the paper argues that MNC is especially valuable in few-shot settings, a more direct comparison between late fusion without MNC and the proposed MNC under 5-shot and 10-shot settings would make the claim much stronger.  
   Similarly, **Figure 5** in the appendix, and to some extent **Figure 3**, suggest complementary modality behavior, but the main paper does not quantify when MNC helps or hurts. For a core module, this remains somewhat under-analyzed.

8. **The qualitative analysis is useful but still somewhat cherry-picked and not fully diagnostic.**  
   **Figure 3** on Page 7 provides a compelling visual comparison for a handful of samples, and the density plots show better separation for PIRN. However, the figure compares against M3DM, CFM, and INP-Former only, not against the strongest full-shot or architecture-search baselines. Also, the density plots are shown for selected categories rather than aggregate distributions, so it is hard to judge whether the separation is broadly representative.  
   **Figure 4** on Page 9 tries to explain “feature displacement via BPA routing,” but the interpretation is a bit hand-wavy. The displacement vectors are shown after the combined effects of BPA+APR+MNC, so the figure does not isolate BPA. If the goal is to validate the OT assignment itself, this visualization is only indirectly informative.

9. **There is a subtle methodological concern around test-time adaptation that deserves a clearer discussion.**  
   APR updates prototypes using the current test input before producing the reconstruction for anomaly scoring. In anomaly detection this is not automatically invalid, but it is a strong design choice because the method uses unlabeled test samples to modify internal representations online. The paper frames this as adaptation to unseen normality, but it does not discuss possible failure cases, such as systematic drift under repeated anomalous inputs, order sensitivity if prototypes are carried over across test samples, or whether refinement is reset per image. The appendix suggests a per-sample constrained update, but the main paper should state this explicitly because it affects how one interprets the claimed robustness.

## Questions
1. Please give the exact training loss used in all experiments. Is it plain average cosine reconstruction loss, the “soft mining loss” from Luo et al. (2025), or a combination? A full formula would increase my confidence substantially.

2. For **Equation (1)**, what is the entropic regularization coefficient in Sinkhorn OT, and how sensitive are results to it? Since your argument relies on both balanced usage and selective assignment, the paper should clarify how these two goals are reconciled.

3. In APR, are prototypes refined independently for each test image and then reset, or is there any accumulation across test samples? If they are reset per sample, please state that explicitly in the main text. If not, please explain how you avoid drift or contamination.

4. Can you provide a stronger isolation of MNC’s benefit, for example a two-modality baseline with simple late fusion but **without** prototype communication, evaluated at 5-shot and 10-shot? That would help separate “multimodal helps” from “the proposed communication mechanism helps.”

5. Please clarify the notation around \(\mathbf{Z}^{\text{bpa}}\), \(\mathbf{Z}^{\mathrm{lopa}}\), and \(\mathbf{Z}^{\mathrm{mnc}}\). Are \(\mathbf{Z}^{\mathrm{lopa}}\) and \(\mathbf{Z}^{\text{bpa}}\) identical? If so, the paper should use one symbol throughout.

6. For the adapted INP-Former baseline in **Table 1**, please specify the exact architecture, prototype count, training schedule, and tuning protocol. Since it is one of the strongest baselines, this comparison needs to be reproducible.

7. The Real-IAD D3 results in **Table 8** are hard to interpret due to formatting and metric naming issues. Please provide a cleaned version and clarify whether the compared methods all use matched modalities and data access.

8. It would help to report variance across multiple few-shot splits or seeds. Given the small-data regime, are the gains in **Table 1** stable, especially for 5-shot?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics issues are apparent from the paper. The work studies anomaly detection on industrial datasets and does not present an obvious fairness, privacy, or human-subjects concern based on the provided text.

## Soundness Rating
3: good. The method is plausible and supported by solid experiments, but the mathematical exposition and some methodological details, especially the exact loss, OT regularization, and test-time adaptation protocol, need clarification.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures are helpful, but notation inconsistencies, typographical errors, and several poorly formatted tables materially hurt clarity and confidence.

## Contribution Rating
3: good. The paper makes a useful contribution to few-shot multimodal anomaly detection through a coherent prototype-based design and strong empirical results, even if the novelty claims should be stated more carefully.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The empirical results are strong and the core idea is worthwhile, but the paper needs tighter technical specification and cleaner presentation to fully meet the standard of a strong ICLR paper.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The topic is close to my expertise, and I checked the main equations, figures, and tables carefully, but a few implementation details are too underspecified to verify completely.