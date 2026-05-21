---
job_id: bd492247-a2b0-4dda-9bf3-3b48c056ceb1
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: JdVTWjjnR6.pdf
paper: HITNET: Hippocampal-Thalamic Inspired Dual-Stream Network for Multimodal Sentiment Analysis Under Missing Data
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on multimodal representation learning and robust sentiment analysis under missing data, with architectural and learning contributions for incomplete multimodal inputs.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, quantitative and qualitative results, and conclusion; it also presents sufficient empirical evidence to merit full review, even though there are notable technical and positioning weaknesses.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies multimodal sentiment analysis under random frame-level missingness across language, audio, and vision. The proposed HiTNet uses a dual-stream architecture: an intra-modal enhancement stream with a semantic memory module and sparse activation network for modality-specific recovery, and an inter-modal regulation stream with confidence estimation and cross-modal completion for reliability-aware fusion. Experiments on MOSI, MOSEI, and SIMS report improved average performance over several baselines across missing rates, together with ablations and qualitative visualizations.

## Strengths
1. The paper tackles a meaningful and practically relevant setting, namely random frame-level missingness across all modalities rather than only whole-modality dropout. This is a harder and more realistic corruption pattern for multimodal sentiment analysis, and the paper keeps that focus consistently from the problem statement in Section 3.1 through the experiments in Section 4.2.

2. The proposed architecture is reasonably well structured. Figure 2 is helpful in showing the decomposition into an intra-modal stream, an inter-modal stream, reconstruction, and hierarchical fusion. Even though I have concerns about whether the biological analogy is doing real scientific work here, the engineering decomposition itself is understandable and the two streams target different failure modes under missingness.

3. The empirical section is fairly extensive in breadth. The paper evaluates on three benchmarks, reports multiple metrics, includes ablations in Table 3, missing-rate trends in Figure 3, modality-level missingness analysis in Table 4, and qualitative analyses such as Figure 4 and Figure 5. This is more effort than a bare minimum benchmark table.

4. The main comparison tables are competitive. In Table 1, HiTNet improves over the strongest reported baselines on average over missing rates for both MOSI and MOSEI, especially on Acc-7 and some Acc-2/F1 variants. Table 2 also shows competitive results on SIMS, with a notable gain in Acc-3. These are not gigantic margins everywhere, but they are generally consistent.

5. The ablation study in Table 3 suggests that both streams and the auxiliary losses matter. In particular, removing the inter-modal stream hurts MOSI Corr from 0.539 to 0.499 and SIMS Corr from 0.389 to 0.348, which is a nontrivial drop relative to several other ablations. This supports the claim that the inter-modal branch contributes materially rather than being decorative.

6. Figure 3 is a useful stress-test visualization. It shows that the method degrades more gracefully than the baselines as the missing rate increases, especially on MOSI and MOSEI. The gap at high missing rates is more convincing than just showing average-over-rates numbers, because it better matches the paper’s central robustness claim.

## Weaknesses
1. **The mathematical specification of several core modules is underspecified or internally inconsistent, which makes the method harder to verify than the polished narrative suggests.**  
   The first issue is in **Equation (3)** on Page 4. The gate is defined as
   \[
   g_m = \sigma\!\left(W_r \cdot \mathrm{Concat}(x_m, \mathbf{v}_{i^*}^m)\right), \quad \tilde{x}_m = x_m + g_m \odot \mathbf{v}_{i^*}^m,
   \]
   with \(W_r \in \mathbb{R}^{(2D_m)\times 1}\). But \(x_m \in \mathbb{R}^{T_m \times D_m}\), while \(\mathbf{v}_{i^*}^m \in \mathbb{R}^{D_m}\). It is not defined whether \(\mathbf{v}_{i^*}^m\) is broadcast across time, whether concatenation is performed per frame, or whether \(g_m\) is a scalar, a length-\(T_m\) vector, or a \(T_m \times D_m\) tensor. With the stated shape of \(W_r\), the output seems scalar-like per token at best, but then \(\odot \mathbf{v}_{i^*}^m\) would require another unstated broadcast. Since this gate is central to the semantic memory module, this ambiguity matters.

   A second issue is **Equation (4)** on Page 4:
   \[
   G(x_m)=\mathrm{Softmax}(\mathrm{TopK}(x_m W_G, k)).
   \]
   If \(x_m \in \mathbb{R}^{T_m \times D_m}\) and \(W_G \in \mathbb{R}^{D_m \times n}\), then \(x_mW_G \in \mathbb{R}^{T_m \times n}\). It is unclear whether TopK is applied per frame, after pooling across time, or on the flattened tensor. This is not a cosmetic detail, because the sparse-activation mechanism is one of the headline components.

   A third issue appears in **Equation (5)**:
   \[
   f_m^{\text{intra}}=\sum_{j=1}^{s} G(x_m)_j \cdot S_j(\tilde{x}_m),
   \]
   but the paper previously introduced \(n\) subnetworks and top-\(k\) activation. The index upper bound suddenly becomes \(s\), which is never defined. This looks like a notation error in the core model definition, not just a typo in a caption. These mathematical gaps reduce confidence that the implementation exactly matches the described method.

2. **The confidence module is trained to predict missing ratio, which is a fairly weak notion of “confidence” and does not really support the stronger reliability claims made in the text.**  
   In **Section 3.5**, **Equation (8)** supervises \(s_m\) using a soft target \(\hat{s}_m = 1-r_m\), where \(r_m\) is simply the missing ratio. This makes \(s_m\) essentially a learned estimator of observed corruption level, not a semantic reliability or usefulness score. Yet the paper repeatedly frames this as a mechanism that “dynamically integrates high-quality information while suppressing redundant interference” and assesses “intrinsic quality” or “confidence.” Those are stronger claims than what Equation (8) actually enforces.

   Why this matters: two samples can have the same missing ratio but very different information value. Missing a few sentiment-critical words is not equivalent to missing a few noninformative visual frames. In fact, the paper itself argues that modality quality differs in more subtle ways than mere completeness. By supervising the module with \(1-r_m\), the method may collapse to “how much is missing” rather than “how trustworthy is this modality for sentiment now.” The paper would be stronger if it either toned down the interpretation or provided evidence that \(s_m\) captures more than missing rate.

3. **The experimental comparison is not fully persuasive because the paper relies heavily on reported baseline numbers, while the proposed method is substantially more complex than most baselines and parameter/computation matching is not established in the main paper.**  
   In **Section 4.4**, the paper states that baseline results are “reported as in LNLN.” That is common in some benchmark-driven papers, but here it is more problematic because HiTNet adds multiple Transformer modules, a memory bank, sparse experts, reconstruction, and auxiliary losses. Without a stronger main-paper capacity-control study, it is hard to tell whether the gains come from the particular hippocampal-thalamic factorization or simply from a larger and more supervised architecture.

   The appendix gives a computational table, but by the paper’s own framing the main review should stand on the main paper. In the main text, there is no table reporting parameter counts or FLOPs for the compared baselines, nor a matched-capacity ablation. This matters because several gains in **Table 1** and **Table 2** are modest, often around one point. When the model is much more elaborate, modest gains are not automatically compelling.

4. **The evidence for originality is weaker than the paper claims.**  
   Stripped of the neuroscience language, the building blocks are fairly familiar: key-value memory retrieval, gating, sparse expert-like subnetworks, reliability weighting, reconstruction loss, and cross-modal fusion. The paper does combine these pieces for frame-level missing multimodal sentiment analysis, and that is a legitimate engineering contribution. However, the manuscript repeatedly presents the work as if the “hippocampal-thalamic” analogy itself is a major advance. I do not think the paper really earns that framing.

   The problem is not that inspiration from neuroscience is illegitimate, it is that the mapping is loose. The semantic memory module is nearest-neighbor retrieval over pooled features via **Equation (2)** plus residual gating; the thalamic module is confidence-weighted interpolation in **Equation (10)**:
   \[
   f_m^{inter} = s_m x_m + (1-s_m) h_m.
   \]
   These are standard deep learning motifs with biological labels attached. The paper would be more convincing if it positioned itself more modestly as a dual-path completion-and-fusion architecture, rather than leaning so hard on the analogy as if it were explanatory evidence.

5. **Some quantitative results raise concern about result hygiene and table reliability.**  
   There are several entries in **Table 1** that look suspicious. For example, the **TETFN** row on MOSEI appears to repeat values from MOSI in a way that is implausible, including the exact same Acc-2/F1 pair and MAE/Corr pattern; similarly, the **TFR-Net** MOSEI Acc-5 entry is listed as 34.67, which looks inconsistent with neighboring entries and the rest of the row. I cannot verify whether these are transcription issues from prior work or mistakes in the current manuscript, but they matter because the paper’s empirical case depends on careful benchmark reporting.

   Once such anomalies appear in a core results table, they cast a shadow on the reliability of the comparison, even if the proposed method’s own numbers are correct. At minimum, the authors should carefully audit Tables 1 and 2 and confirm that every baseline number is dataset-correct and metric-correct.

6. **The averaging protocol over missing rates hides important behavior, and the detailed per-rate tables show a less clean story than the headline claims.**  
   The paper’s main comparison emphasizes averages over missing rates, but robustness claims should be judged per corruption regime. Looking at the detailed tables, the method is not uniformly best in every setting. For example, on **MOSI at \(r=0\)** in **Table 12**, HiTNet is not best on several metrics, which is fine, but it shows the method is not simply stronger overall, rather it is tuned toward missingness robustness. More importantly, for some settings the improvements over LNLN are quite small, and for some metrics the gains are inconsistent. This does not invalidate the method, but it means the headline “superior across all missing rates” is stated a bit too aggressively.

   **Figure 3** supports the robustness trend overall, but it also reveals that on some tasks the separation from strong baselines is not dramatic at low-to-medium missingness. A more honest framing would be: the method is most compelling in high-missingness regimes, not uniformly dominant everywhere.

7. **The qualitative analyses are suggestive but not especially diagnostic.**  
   **Figure 4** shows boxplots of Euclidean distance between missing/completed features and complete features under 90% missingness. This is directionally fine, but Euclidean proximity in learned feature space is not obviously aligned with sentiment utility. A feature can be closer in \(L_2\) and still worse for downstream prediction. The figure would be more convincing if paired with a task-conditioned metric or class-separability analysis.

   **Figure 5** shows confusion matrices for LNLN and HiTNet on MOSI. The visual impression is that HiTNet spreads predictions across more classes under high missingness, which is better than collapsing to neutral. But the figure mostly illustrates what the accuracy numbers already imply. It does not isolate which component is responsible, nor does it validate the biological claims. In other words, the qualitative section helps tell the story, but it does not materially strengthen causal understanding of the method.

8. **The hierarchical fusion design is justified mostly post hoc, and the chosen fusion order feels under-motivated in the main paper.**  
   In **Equation (11)** on Page 6, the authors fuse \((V,A)\) first and language last, arguing that language should guide final semantic integration. That may be sensible in sentiment analysis, but it is also a hand-crafted inductive bias. The main text does not present evidence there; it simply states the preference. The appendix later explores fusion orders, but again, the main-paper scientific story would be stronger if this design choice were justified upfront with either prior evidence or a compact main-text ablation.

   This matters because hierarchical ordering can affect outcomes substantially. If the performance depends on “put language last,” then part of the gain may come from a sentiment-task heuristic rather than the proposed dual-stream completion principle.

9. **The reconstruction objective is not fully specified and may introduce train-test asymmetry that deserves more discussion.**  
   In **Equation (14)**, the model reconstructs \(\hat{x}_m = E_m^{Rec}(x_m)\) toward \(u_m = Enc_m(U_m)\), where \(U_m\) is the complete modality. This uses complete inputs during training to define a target representation, which is reasonable for supervised corruption training, but the paper does not discuss how sensitive this is to having aligned complete observations during training, nor whether the model would generalize if corruption patterns differ from the training simulator.

   Also, the reconstruction is performed at the encoded-feature level rather than original-feature level, which can be helpful but also makes interpretation trickier. The paper attributes robustness gains to semantic recovery, yet it is not clear whether the auxiliary task is reconstructing semantically meaningful content or mainly regularizing the encoder.

10. **Presentation is decent overall, but there are too many local inconsistencies for a method-heavy paper.**  
   Beyond the equation issues above, there are repeated naming inconsistencies: “HiTNet” vs “HiT-Net,” “Lthi” and “Ltrr” in **Table 3** instead of notation matching the text, and occasional grammatical slips that obscure precise meaning. Figure 2 is useful, but some symbols in the figure are hard to map exactly to the equations, especially around the inter-modal branch and reconstruction path. For a model with this many interacting components, tighter notation discipline is not optional.

## Questions
1. In **Equation (3)**, what are the exact tensor shapes of \(g_m\), \(x_m\), and \(\mathbf{v}_{i^*}^m\)? Please define whether the memory value is broadcast across time and whether the gate is scalar, token-wise, or feature-wise. A precise clarification here would increase my confidence substantially.

2. In **Equation (4)**, how exactly is TopK applied when \(x_mW_G \in \mathbb{R}^{T_m \times n}\)? Is gating computed per frame, after temporal pooling, or in some other way? Also, in **Equation (5)**, should the sum run over \(n\), over the selected top-\(k\) experts, or over some undefined \(s\)? Please correct this formally.

3. The confidence target in **Equation (8)** is \(1-r_m\). Do the authors have evidence that the learned \(s_m\) captures semantic reliability beyond missing ratio? For example, can you show that samples with equal \(r_m\) but different signal quality receive meaningfully different confidence scores and that this correlates with downstream usefulness?

4. Can the authors provide a main-paper or rebuttal analysis controlling for model capacity, such as a parameter-matched variant of a strong baseline, or a simplified HiTNet with similar size to LNLN? Right now it is difficult to attribute the gains specifically to the proposed design rather than to added machinery.

5. Please audit **Table 1** carefully. In particular, the TETFN and TFR-Net MOSEI entries look suspiciously inconsistent. If these are transcription errors, correcting them is important because they affect trust in the empirical section.

6. The method is framed as specifically brain-inspired. What empirical consequence of that inspiration is actually testable here? Put differently, what prediction does the hippocampal-thalamic decomposition make that a generic retrieval-plus-gating architecture would not? A sharper answer could improve the paper’s conceptual contribution.

7. The main paper claims strong robustness under frame-level missingness. How sensitive are results to the missingness process itself, beyond the random Bernoulli masking in Section 4.2? A compact comparison between random independent masking and blockwise/consecutive masking in the main paper would strengthen the practical relevance.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The work uses established sentiment datasets and does not introduce an obviously harmful application or data collection procedure beyond standard benchmark usage.

## Soundness Rating
2: fair. The empirical results are reasonably extensive, but the technical specification has important ambiguities in core equations and the causal attribution of gains is not fully nailed down.

## Presentation Rating
2: fair. The paper is readable and reasonably organized, but several notation inconsistencies, table anomalies, and underspecified equations prevent me from calling the presentation good.

## Contribution Rating
2: fair. The targeted problem is relevant and the empirical robustness is interesting, but the underlying ideas feel like a fairly incremental combination of familiar mechanisms, and the scientific case for the brain-inspired framing is not strong enough.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper addresses an important setting and reports competitive results, especially at high missing rates. However, the combination of underspecified core equations, weakly substantiated “confidence” and neuroscience claims, questions about benchmark table reliability, and limited evidence that the gains come from the proposed design rather than added complexity keeps it below the bar for me in its current form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The problem setting and related model components are within my expertise, and I checked the main technical details and empirical tables carefully, but I cannot verify implementation-level choices that are not specified in the paper.