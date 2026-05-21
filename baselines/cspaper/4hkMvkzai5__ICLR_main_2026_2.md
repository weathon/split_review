---
job_id: 5b95b168-0119-4f16-ad62-84ab42db8ed2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 4hkMvkzai5.pdf
paper: DeCodec: Rethinking Audio Codecs as Universal Disentangled Representation Learners
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies representation learning for audio via a neural codec that aims to disentangle speech, background sound, and speech sub-factors.

## Minimum Quality
Pass ✅. The submission contains the necessary research components, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion, and it presents a technically meaningful proposal with empirical evaluation, even though there are notable issues in rigor and exposition.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious embedded text aimed at influencing automated review.

# Expected Review Outcome:
## Summary
This paper proposes DeCodec, a neural audio codec intended to learn disentangled representations for mixed real-world audio. The method combines a subspace orthogonal projection module to split encoder embeddings into speech and background-sound subspaces, parallel RVQs for separate quantization, semantic guidance on the speech branch to separate semantic and paralinguistic content, and a representation swap training procedure that recombines speech from one mixture with background sound from another. The paper evaluates the resulting codec on reconstruction, speech enhancement, noisy one-shot voice conversion, and as a feature front-end for downstream ASR and TTS.

## Strengths
The paper addresses a relevant and practically important problem. Many existing codecs are either universal but entangled, or disentangled but speech-only. The motivation for explicitly separating speech and background sound in the representation domain is reasonable and well aligned with real use cases such as enhancement, robust ASR, controllable TTS, and noisy voice conversion.

The overall system design in **Figure 2** is fairly intuitive and helps communicate the architecture. In particular, the separation between SOP, SRVQ/NRVQ, semantic guidance, and the swap-based training path makes the intended factorization easy to follow. I appreciated that the figure distinguishes training-only versus inference-only paths, because without that visual cue the RST procedure would be harder to parse from the text alone.

The empirical scope is broader than many codec papers. The method is not only evaluated on reconstruction, but also on downstream or codec-enabled tasks. This broader framing is useful, because the paper’s central claim is not just better compression but controllable and task-selective representation learning.

Some quantitative results are genuinely encouraging. In **Table 2**, DeCodec achieves the best DNSMOS OVL and BAK among the listed SE baselines on both simulated and real-recording DNS Challenge test sets. Even if one can debate whether this is the fairest comparison, these numbers do suggest that the learned factorization is useful for denoising and background suppression. Likewise, **Table 6** indicates a clear advantage over SpeechTokenizer on noisy ASR features, especially in the noisy setting where DeCodec obtains lower WER* than both SpeechTokenizer and StoRM-SpeechTokenizer.

The ablation in **Table 4** is directionally useful. It supports the claim that neither SOP nor RST alone is sufficient, and that combining them substantially improves the reported decoupling metrics. Even though the evidence is still incomplete, this is better than presenting the full system without any component-level study.

The qualitative visualizations in the appendix are also somewhat supportive. **Figure 5** shows spectrogram examples for reconstruction, enhancement, background extraction, and VC variants, and the enhancement / background-extraction columns are consistent with the paper’s intended behavior: the background-heavy regions appear suppressed in SE and preserved in BGS extraction. I would not over-interpret these plots, but they at least align with the narrative.

## Weaknesses
1. **The core theoretical claims around orthogonal projection and disentanglement are not established rigorously, and in places the derivation is simply not correct as written.**  
   The paper presents Section 3.4 as if trainable linear layers become orthogonal projectors by minimizing an output orthogonality loss. That is much stronger than what is actually shown. In **Equation (4)**, the authors assume an orthogonal decomposition \(\mathbf{Y}=\mathbf{P}_S\mathbf{Y}+\mathbf{P}_N\mathbf{Y}\), with \(\mathbf{P}_S+\mathbf{P}_N=\mathbf{I}\) and \(\mathbf{P}_S\mathbf{P}_N^T=\mathbf{0}\). But the implemented modules are described only as “two trainable linear projection layers” on **Page 5**, not as parameterizations constrained to be projection matrices. A generic learned linear layer is not an orthogonal projector: idempotence \(\mathbf{P}^2=\mathbf{P}\), symmetry \(\mathbf{P}=\mathbf{P}^T\), and complementary-subspace structure do not follow from output decorrelation alone.  
   The jump after **Equation (6)** is especially problematic. The paper says that when \(\mathbf{Y}\mathbf{Y}^T\) satisfies “the angular matrix” and feature channels are independent, then one can obtain \(\mathbf{P}_S\mathbf{P}_N^T=\mathbf{0}\). This is not a standard stated condition, not precisely defined, and not sufficient as written. Even if \(\mathbf{Y}\mathbf{Y}^T\) were diagonal or proportional to identity, \((\mathbf{P}_S\mathbf{Y})(\mathbf{P}_N\mathbf{Y})^T\approx 0\) would at most imply orthogonality in expectation under distributional assumptions, not that the parameter matrices are exact orthogonal projectors. This matters because the paper’s central scientific claim is explicit disentanglement via orthogonal subspaces, and the math currently overstates what is guaranteed.

2. **The “proof” for the representation swap loss enforcing speech-only and noise-only codes is not convincing.**  
   In Section 3.6, the argument from **Equations (13) to (16)** relies on subtracting two decoder outputs and then invoking a mean value theorem for vector functions to conclude that \(\mathbf{Zs}_1\) must be independent of noise. This is far too informal for the claimed conclusion. The decoder is nonlinear, high-dimensional, and jointly depends on both \(\mathbf{Zs}\) and \(\mathbf{Zn}\). The existence of some intermediate \(\xi\) does not imply invariance of \(\partial \mathrm{Dec}/\partial \mathbf{Zn}\) to \(\mathbf{Zs}_1\), nor does it prove conditional independence of \(\mathbf{Zs}_1\) from \(\mathbf{n}_1\). At best, the loss encourages compatibility under a specific recombination objective. It does not prove that the learned codes contain only speech or only background information.  
   This is not a cosmetic issue. The paper repeatedly claims explicit decoupling and even “complete decoupling” in Section 3.4. Those are much stronger than what the objective demonstrably guarantees.

3. **Several objective terms are underspecified or internally inconsistent, which makes the method harder to assess and reproduce.**  
   The semantic guidance loss in **Equation (7)** is unusual and not well explained:
   \[
   \mathcal{L}_{\mathrm{SG}}=\left\lVert{ \log \sigma(\cos(\mathbf{WZc},\mathcal{H})) }\right\rVert_1.
   \]
   Minimizing \(\|\log \sigma(\cdot)\|_1\) after cosine similarity is not standard, and the paper does not explain why this form is used instead of a more transparent contrastive, regression, or cosine-distance objective. Also, “cosine similarity along the frame dimension” is vague: is the cosine computed per frame, then summed, or over a whole sequence? How are differing sequence lengths handled after codec downsampling relative to HuBERT features?  
   The total training loss on **Page 13** has an apparent typo or inconsistency in the weights: it lists 500.0 for \(\mathcal{L}_{\mathrm{RST}}\), 150.0 for \(\mathcal{L}_{\mathrm{SG}}\), and then 10.0 again for \(\mathcal{L}_{\mathrm{SG}}\), which likely was intended to be \(\mathcal{L}_{\perp}\). If so, the main text never clearly states the combined objective in the paper body, which is important because the method depends on balancing many losses.  
   There is also ambiguity in the reconstruction target used during RST training. Appendix A says multi-scale mel loss is applied to \(\hat{\mathbf{y}}_{12}\), but the paper does not clearly state whether standard reconstruction of \(\hat{\mathbf{y}}_{11}\) is also optimized in parallel, how adversarial losses are applied across original and swapped outputs, and whether codebook losses are applied on both branches symmetrically.

4. **The novelty is somewhat incremental relative to existing codec-based disentanglement ideas, and the paper does not sufficiently sharpen what is fundamentally new.**  
   Much of the system is a combination of known ingredients: a DAC-style codec backbone, RVQ factorization, semantic guidance from HuBERT-like features, orthogonality regularization, and a swap/recombination training idea. The paper’s main distinction is moving from speech-only factorization to speech-vs-background plus semantic-vs-paralinguistic factorization. That is a worthwhile extension, but the manuscript often phrases the contribution in stronger terms such as “for the first time” and “universal disentanglement codec” without adequately qualifying what prior work already provides.  
   This matters because the contribution score should depend not only on usefulness but on how much conceptual advance is actually demonstrated. The paper would be stronger if it more carefully isolated the minimal novelty claim, namely explicit mixed-audio factorization for controllable downstream selection, instead of stretching to very broad universality claims.

5. **The experimental comparisons are useful but not fully fair or fully informative.**  
   In **Table 1**, DeCodec is reported at \(4.0+4.0\) kbps, effectively 8 kbps total, while several baselines are at lower rates, for example DAC at 4.5 kbps and SpeechTokenizer at 4.0 kbps. The text then highlights best SDR and competitive quality. That comparison is not apples-to-apples. If the proposed model consumes roughly double the bitrate of some baselines, then stronger reconstruction is less surprising. The paper should either compare at matched total bitrate or explicitly frame the tradeoff.  
   The same table also raises a metric-selection issue: for noisy speech, only SDR and Mel Distance are shown, but WER is omitted in the noisy columns even though robustness is central to the paper’s claims. Since the text discusses semantic preservation under noise, the omission is noticeable.  
   More generally, some baselines are not retrained under matched conditions. The paper states that reconstruction baselines are used from official checkpoints, which is understandable, but then conclusions about superiority should be moderated because training data and bitrate settings differ.

6. **The evidence for disentanglement is still indirect, despite strong claims.**  
   The paper mainly infers disentanglement from task performance and swap behavior. That is suggestive, but not enough for the claimed “explicit decoupling.” **Table 4** reports SDR-B and SDR-S for decoupled background and speech, but the precise construction of these measurements is not sufficiently defined in the main paper. Are these obtained by decoding only NRVQ, only SRVQ, or by replacing the complementary branch with blank audio as in Table 5? The interpretation depends on this.  
   Likewise, **Figure 3** in the appendix is presented as evidence that SOP achieves subspace orthogonal decomposition because cosine similarities between \(\mathbf{P}_S\) and \(\mathbf{P}_N\) cluster near zero and singular values differ. But low cosine similarity between parameter rows or outputs is not equivalent to semantic disentanglement. It mostly shows decorrelation, not that one branch is exclusively speech and the other exclusively background.  
   **Figure 4** similarly shows t-SNE plots of \(\mathbf{Zc}\) and \(\mathbf{Zr}\), where \(\mathbf{Zr}\) clusters by speaker more than \(\mathbf{Zc}\). This is consistent with the intended semantic/paralinguistic split, but it is qualitative and based on mean-pooled embeddings from only 25 samples. That is weak support for a fairly strong decomposition claim.

7. **The one-shot VC experiment is not strong enough to support the claimed capability.**  
   **Table 3** reports WERs of 74.18 for SpeechTokenizer, 52.73 for StoRM-SpeechTokenizer, and 50.46 for DeCodec. These numbers are still extremely high. The paper openly acknowledges that the converted speech has high distortion due to voicing mismatches, which is honest, but it also undercuts the claim of “effective one-shot voice conversion on noisy speech.” A system producing around 50 WER after conversion may be an interesting proof of concept, yet “effective” is too generous.  
   In addition, the evaluation is thin. One table with SIM and WER is not enough to establish VC quality, especially when the output background sound is manipulated and the reference is length-matched post hoc. More analysis of failure cases, or at least examples stratified by phonetic alignment difficulty, would have helped.

8. **Some of the strongest claims are broader than what the experimental scope justifies.**  
   The title and repeated phrasing frame the codec as a “universal disentangled representation learner,” but the experiments are centered almost entirely on noisy speech mixed with background sounds, trained from speech corpora plus ESC-50 and DNS-Noise. That is not the same as demonstrating universality across audio domains. There is no evaluation on music, non-speech environmental audio, or broader mixed-audio conditions beyond the curated training recipe.  
   This overstretch matters because “universal” suggests a much broader applicability than what is empirically shown. The contribution would read as more credible if the paper narrowed the claim to mixed speech-and-background audio.

9. **Presentation quality is uneven, and several writing / notation issues impede confidence.**  
   There are many grammatical errors and notation inconsistencies throughout the paper. A few examples: “These allows” in the abstract, “an universal” and “an codec” multiple times, “andn” on **Page 5**, “representaions” on **Page 8**, and inconsistent naming of BRVQ/NRVQ in tables and appendix. On the technical side, spaces and notation vary between \(\mathbf{Zs}\), \(\mathbf{Z}\mathbf{s}\), \(\mathbf{Zn}\), \(\mathbf{Zc}\), and \(\mathbf{Zr}\). In **Section 3.5**, the expression for residual paralinguistic representation is incomplete:
   \[
   \mathbf{Zr}=\sum_{k=2}^{K_s}
   \]
   which is clearly missing the summand.  
   These are not fatal individually, but collectively they make the paper feel under-polished and make the mathematical story harder to trust.

10. **The practical cost-benefit story is not fully developed.**  
   The paper argues that a unified codec representation is computationally preferable to cascading task-specific front ends, but the proposed model itself is quite heavy: encoder-decoder, two projection branches, two parallel 8-stage RVQs, adversarial training, semantic guidance, and swap-based objectives. There is no analysis of training cost, inference latency, memory, or codebook utilization. Since the motivation includes efficiency and unified deployment, this omission is notable. A comparison against cascaded pipelines should ideally include some complexity discussion, not only downstream scores.

## Questions
1. In Section 3.4, are \(\mathbf{P}_S\) and \(\mathbf{P}_N\) actually constrained to be projection matrices, or are they just unconstrained linear layers? If the latter, please soften the claims around orthogonal projection and direct-sum decomposition, or provide a more rigorous justification.

2. Please clarify the derivation after **Equation (6)**. What exactly is meant by “the covariance matrix \(\mathbf{Y}\mathbf{Y}^T\) satisfies the angular matrix”? Is this a typo for diagonal matrix, identity-like covariance, or something else? How does that imply \(\mathbf{P}_S\mathbf{P}_N^T=0\)?

3. For the argument in **Equations (13)-(16)**, can the authors provide a more formal statement of what is actually guaranteed by \(\mathcal{L}_{\mathrm{RST}}\)? Right now the text reads like a proof of disentanglement, but it seems more accurate to say the loss encourages swap consistency.

4. Please specify the exact training objective in the main paper. Which losses are applied to original reconstructions versus swapped reconstructions? Also, on **Page 13**, is the second “10.0 for \(\mathcal{L}_{\mathrm{SG}}\)” actually intended to be the weight for \(\mathcal{L}_{\perp}\)?

5. In **Equation (7)**, how is the cosine computed, framewise or sequencewise, and how are the HuBERT and codec frame rates aligned? A precise definition would improve reproducibility.

6. Could the authors provide bitrate-matched comparisons for **Table 1**? Since DeCodec uses \(4.0+4.0\) kbps, I would like to see either an 8 kbps baseline setting or a reduced-bitrate DeCodec variant.

7. For **Table 4**, please define precisely how SDR-B and SDR-S are computed. Are these obtained by decoding individual branches with blank substitution as described in Appendix C, or by some other protocol?

8. The title and introduction emphasize universality. Can the authors justify this wording given that training and evaluation focus on speech mixed with background sounds? If the claim is narrower, it would help to restate it more precisely.

9. For the voice conversion experiment in **Table 3**, can the authors provide stronger evidence than a single WER/SIM table, such as breakdowns by alignment difficulty, more examples, or a clearer statement of what level of VC performance they consider practically meaningful?

10. A practical question: what is the inference cost of DeCodec compared to a cascaded StoRM+SpeechTokenizer pipeline? Since efficiency is part of the motivation, some runtime or parameter comparison would increase confidence.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper itself. The work is a codec / representation-learning method for speech and background-sound factorization, and the experiments are on standard speech and noise datasets. The usual downstream misuse risks for voice conversion exist, but the paper does not appear to introduce a new ethics-specific issue beyond standard concerns in speech generation and conversion.

## Soundness Rating
2: fair. The empirical results are interesting and partially supportive, but the mathematical justification for the main disentanglement claims is weak, several objectives are underspecified, and some comparisons are not sufficiently controlled.

## Presentation Rating
2: fair. The high-level idea is understandable, and **Figure 2** is helpful, but the manuscript has many writing problems, notation inconsistencies, and unclear derivations that materially reduce clarity.

## Contribution Rating
2: fair. The problem is meaningful and the empirical scope is decent, but the contribution feels more like a useful extension and engineering combination of existing ideas than a clearly established step forward at ICLR level, especially given the over-claimed theory and “universal” framing.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper tackles an important problem and has promising empirical results, especially for denoising and noisy downstream robustness, but the current version overstates its theoretical guarantees, does not yet convincingly establish disentanglement, and needs sharper empirical control and clearer writing to meet ICLR standards.

## Reviewer Confidence
4: confident. I am confident in this assessment and carefully checked the main mathematical claims and experimental evidence, although some implementation details remain ambiguous due to the paper’s presentation.