- Decision: Accept
- Avg Score: 5.50
- Scores: 8, 5, 6, 3
Now I have thoroughly verified all claims against the paper. Let me provide my final review.

Important finding: The specific numbers the Harsh Critic cites for Table 5 (22.6, 22.9, 27.3, 23.7) do **not** appear anywhere in the parsed paper text. Table 5 is an embedded image, and these numbers cannot be verified. The paper's textual description (lines 182-187) is consistently positive about component improvements.

---

## Summary

This paper tackles Weakly Supervised Spatio-Temporal Video Grounding (WSTVG), proposing CoSPaL — a system that adapts the frozen image-based Grounding DINO to video through three components: Tubelet Phrase Grounding (TPG) for spatio-temporal alignment, Contextual Referral Grounding (CRG) that uses LLM-based query decomposition to refine subject attention, and Self-Paced Scene Understanding (SPS) that progressively increases scene complexity during training. The method achieves substantial gains over prior weakly-supervised methods (+7.9% m_vIoU on HCSTVG-v1, +3.9% on VidSTG) using a single GPU, and is the first work to adapt a foundation model (G-DINO) to WSTVG.

## Strengths

- **Strong quantitative gains over prior weakly-supervised methods**: CoSPaL achieves double-digit absolute improvements on HCSTVG-v1 (e.g., +8% m_vIoU over WINNER, +14-15% over AWGU/Vis-CTX) and solid gains on the large-scale VidSTG dataset (+4.4% declarative, +3.3% interrogative). These results are clearly shown in Tables 2-3 and support the paper's central claim of advancing the SOTA.

- **First demonstration of a foundation model for WSTVG with competitive results**: The paper adapts G-DINO, a multimodal foundation model, to the weakly supervised video setting and shows it outperforms prior approaches relying on traditional detectors (Faster R-CNN). This is a genuine novelty — the comparative analysis in Table 6 with different detector backbones substantiates the claim.

- **Computational efficiency advantage**: Figure 5 and the associated discussion provide concrete evidence that CoSPaL uses a single GPU vs. 8-32 GPUs for fully-supervised baselines, with 2-4× shorter training time and 2.5-6.5× less memory per GPU. This practical advantage is well-documented.

- **Ablation evidence for individual components**: Table 4 shows progressive gains from spatial grounding, temporal grounding, and TSA sub-modules (e.g., +9% tIoU from temporal grounding). Table 5 (though described with some textual ambiguity — see weaknesses) shows positive contributions from CRG and SPS individually, with SPS adding 0.9% on m_vIoU to TPG and CRG independently.

- **Qualitative validation**: Figure 4 provides side-by-side comparisons showing CoSPaL produces tighter spatio-temporal overlap with ground truth than the W-GDINO baseline, visually corroborating the diagnosis of baseline failure modes.

## Weaknesses

### Fatal
None.

### Major

- **Contextual Referral Grounding (CRG) is underspecified to the point of irreproducibility**: CRG is a central claimed contribution (listed in the abstract and contributions), yet its implementation is critically vague. The paper states "We use GPT-3.5 to extract quantifier and phrases from original caption for CRG" (line 139) with no prompt provided, no example decompositions shown, and no analysis of decomposition success rate or failure modes. The construction of local and global queries (Q_ol, Q_og) from noun-adjective-verb features is described at a level of abstraction that does not constitute an algorithm (line 111: "we look into noun-adjective-verb word features corresponding to referral from generated (Q_o) and original query (Q)"). The notation \(f_{w\langle Q_{og}:Q_{ol}\rangle}\) in Eqs. (4)-(5) does not specify whether these feature sets are concatenated, averaged, or selected via attention. Since GPT-3.5 introduces uncontrolled stochastic variance, the paper needs at minimum: the prompt, example decompositions, success rate statistics, and a comparison with a deterministic rule-based POS-tag baseline. The paper defers to supplementary (line 150), but the main text must provide enough detail for the reader to understand what was actually done.

### Minor

- **Ablation description lacks precision**: The text discussing Table 5 (lines 182-187) reports relative improvements ("further improvement in performance by 0.8%") without consistently specifying the reference baseline for each claim. For example, "When TPG and CRG are combined… we observe further improvement in performance by 0.8%" — it is unclear whether this 0.8% is over TPG alone, CRG alone, or some other configuration. The paper also states "CRG standalone boosts… by 1% on TPG module" — this is confusing because CRG "standalone" (i.e., applied to W-GDINO without TPG) cannot be a delta over TPG, which is a different base. These ambiguities make the narrative of the ablation harder to follow than it should be. This does not invalidate the results but demands clarification.

- **SPS stage thresholds lack sensitivity analysis and justification**: The three SPS stages use upper bounds of 4, 7, and all tubelets (line 150) with no rationale for these specific thresholds, no analysis of how many videos are filtered at each stage, no ablation on the number of stages, and no study of whether tubelet count actually correlates with task difficulty. While Table 4 does show that the progressive training helps (+3% m_vIoU, +4% tIoU), the lack of any sensitivity analysis makes it unclear whether these gains are robust or carefully tuned to the chosen thresholds.

- **No statistical significance or variance reporting**: None of the results include error bars, confidence intervals, or multiple-run statistics. Given the use of a stochastic LLM (GPT-3.5) for CRG and random seeds in training, the absence of variance estimates weakens the reliability assessment. This is a common shortcoming but worth noting.

- **Unclear notation and implementation details**: (a) The notation in Eq. (2) uses \(\mathtt{A}_{\mathtt{T}}\) which was defined as aggregated attention (line 84) but is then used as a similarity/compatibility score in the InfoNCE loss — this needs clarification. (b) The phrase "5 iterations over the dataset through each sub-phrases" (line 150) is confusing — what constitutes a "sub-phrase" and how does iteration work across them? (c) The training details do not specify whether the spatial and temporal parameters are trained from scratch or initialized, and the full set of loss weights between \(\mathcal{L}_s\) and \(\mathcal{L}_t\) is not reported.

### Trivial
- The metric definitions (m_vIoU, tIoU) are described but the vIoU@R threshold is called "vIoU ω_R" with a typesetting artifact (ω substituting for @).

## Nice-to-Haves
- A failure analysis (cases where CoSPaL still struggles, e.g., long-tail actions, occlusions) would strengthen the paper by clarifying limitations.
- Reporting Precision@K or success rates at different tIoU thresholds would provide more granular temporal localization evaluation.
- Comparison to simply fine-tuning G-DINO on the WSTVG training data (if labels permitted) would contextualize the gap to fully-supervised methods.
- Inference speed (FPS) would complete the computational efficiency picture beyond GPU hours/memory.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Inconsistent ablation numbers contradicting the text"** — REMOVED because the specific numerical values (22.6, 22.9, 27.3, 23.7) the critic cites do not appear anywhere in the parsed paper text. Table 5 is an embedded image, and these numbers cannot be verified from the text. The paper's textual description (lines 182-187) consistently describes positive improvements from each component. While the description is ambiguous about reference points (kept as a Minor weakness above), the claimed contradiction is unverifiable and may arise from a parsing error of the table image. The critic themself flagged this possibility ("The parsed numbers in the paper (which I must assume are the real numbers unless evidence indicates a parsing error)").

2. **"Missing prompt for LLM decomposition" as a fatal/major gap** — DEMOTED: the paper states "We show more details and examples in supplementary" (line 150). The parser strips supplementary content. The CRG underspecification remains a Major concern (kept above) but the paper does indicate supplementary material exists.

3. **"Comparison to fine-tuned G-DINO" and "Temporal localization accuracy" suggestions** — Moved to Nice-to-Haves as they are scope extensions, not core flaws.

4. **Formatting/style nitpicks** — REMOVED per instructions. These reflect parser artifacts, not author errors.

5. **Missing related works** — REMOVED per instructions; I cannot confirm the existence of works not cited.

6. **"Hypothetical speculations about what the appendix may contain"** — REMOVED; the paper indicates supplementary material exists and the parser strips it.

## Novel Insights

The most interesting observation from synthesizing the reviews is that the paper's core practical claim — that a frozen foundation model can be adapted to WSTVG with minimal modifications and surprisingly strong results — is simultaneously its greatest strength and the source of its main weakness. The strength is genuine: the results demonstrate that G-DINO has sufficient representational capacity that only light-weight tuning of its outputs (via TPG, CRG, SPS) is needed to surpass dedicated weakly-supervised architectures. However, the reliance on an opaque LLM (GPT-3.5) for CRG introduces an uncontrolled variable that is at odds with the paper's otherwise clean, principled design. This tension — foundation-model-as-scaffold vs. LLM-as-black-box — is not resolved in the paper and would benefit from explicit discussion.

## Suggestions
1. **Provide full specification of CRG**: include the GPT prompt verbatim, at least 3 example query decompositions with GPT outputs, a quantitative analysis of decomposition success rate (e.g., what fraction of queries were decomposed correctly), and a comparison against a simple rule-based POS-tag alternative. Clarify how \(f_{w\langle Q_{og}:Q_{ol}\rangle}\) is computed (concatenation? averaging? separate forward passes?).
2. **Clarify the ablation narrative**: For each row in Table 5, state the exact configuration and the reference point for each relative improvement claim. Use a consistent baseline (e.g., always W-GDINO as the anchor) to avoid ambiguity.
3. **Add sensitivity analysis for SPS**: report the distribution of tubelet counts across training videos, show how many videos enter at each stage, and ablate the number of stages and threshold values.
4. **Report variance**: provide results over at least 3 random seeds, especially since GPT-3.5 introduces stochasticity in the CRG step.
5. **Clarify training details**: specify which parameters are trained from scratch vs. initialized, report loss weights for \(\mathcal{L}_s\) and \(\mathcal{L}_t\), and clarify what "5 iterations over each sub-phrase" means.
