---
job_id: e3a09630-7a01-41b3-8e0c-cffdc4fcb0b5
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 2EQPpEZtEK.pdf
paper: DISTAR: Diffusion Over a Scalable Token Autoregressive Representation for Speech Generation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically generative modeling, representation learning for speech/audio, and discrete diffusion/autoregressive modeling.

## Minimum Quality
Pass ✅. The submission contains the expected core sections, presents a concrete method with experiments and quantitative results, and does not exhibit any immediate fatal flaw that would warrant desk rejection, although there are notable issues in novelty, exposition, and experimental support.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden or explicit instructions aimed at manipulating automated review systems in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes DiSTAR, a zero-shot TTS system that generates speech entirely in a discrete RVQ token space by combining a patch-level causal autoregressive language model with a masked diffusion refiner. The method aims to model both temporal and RVQ-depth dependencies, avoid duration prediction or forced alignment, and offer inference-time controls such as greedy vs. sampled decoding and RVQ layer pruning for bitrate/compute trade-offs. Empirically, the paper reports strong results on LibriSpeech-PC and SeedTTS against several recent zero-shot TTS baselines.

## Strengths
The paper tackles a meaningful design point in modern TTS, namely how to combine the controllability and robustness of discrete token generation with some of the parallelism and self-correction benefits of diffusion-style refinement. That is a reasonable and relevant direction for the ICLR community.

The overall architecture is coherent. In **Figure 1** on **Page 4**, the decomposition into aggregator, causal AR backbone, and masked diffusion head is easy to follow, and it helps clarify the intended separation between inter-patch planning and intra-patch refinement. Even though some implementation details remain underspecified, the high-level system story is understandable and internally consistent.

The empirical results are promising. In **Table 1** on **Page 8**, both DiSTAR-base and DiSTAR-medium are competitive with or better than the listed baselines on WER and UTMOS, and DiSTAR-medium reaches the best WER on both LibriSpeech test-clean and Seed-TTS test-en among the compared systems. The fact that the medium model does this at a parameter count comparable to some weaker baselines is a concrete practical positive.

The paper also includes useful ablations rather than only headline numbers. For example, **Table 3** on **Page 9** provides some evidence that the proposed decoding heuristics matter, and **Figure 2** on **Page 9** gives an interpretable view of the trade-off between the number of retained RVQ layers and quality metrics. In particular, the figure supports the claim that upper RVQ layers affect speaker/detail fidelity more than intelligibility, which is aligned with the authors’ intended controllability argument.

A further practical strength is that the model appears to support both greedy and sampling-based decoding, rather than relying on a narrow decoding sweet spot. That kind of robustness matters in real TTS deployment settings.

## Weaknesses
1. **The main contribution feels more like a careful system integration than a clearly differentiated methodological advance.**  
   The paper combines several already active ideas: patch-wise AR planning in the style of next-patch systems, discrete RVQ token generation, and masked discrete diffusion for parallel infilling. The authors do cite relevant ingredients such as DiTAR and LLaDA-style masked diffusion, but the paper does not sharply isolate what is genuinely new algorithmically beyond moving the next-patch recipe into discrete RVQ space and adding several decoding heuristics. This matters because the paper repeatedly claims state-of-the-art performance and practical advantages, yet the scientific novelty bar at ICLR is not just “good engineering that works.” The authors need a much crisper statement of what principle or design insight is new, what was non-obvious, and why prior AR-plus-refinement or discrete masked modeling pipelines would not already suggest this architecture.

2. **The probabilistic formulation in Section 3.1 is not fully aligned with the actual patch-based model, and the notation is sloppy in ways that matter.**  
   On **Page 3**, **Equation (1)** factorizes over frame-level RVQ tuples,  
   \[
   p_{\theta}(\mathbf{C}\mid\mathbf{X})=\prod_{i=0}^{L-1}p_{\theta}(\mathbf{c}_i\mid \mathbf{c}_{<i}, \mathbf{X}),
   \]
   but the proposed generator is actually patchwise, with overlapping windows \(\mathbf{C}^{(k)}\) and target spans \(\hat{\mathbf{C}}^{(k)}\) introduced on **Page 4**. For \(S<P\), the model is not simply a standard left-to-right factorization over non-overlapping units, and the relationship between the likelihood in Equation (1) and the actual training objective over overlapping target spans is left implicit. Are overlapping target tokens trained multiple times? If so, what exact likelihood is being optimized? If not, which patch owns which token? This is not a cosmetic notation issue. It affects whether the paper is optimizing a consistent estimator of the claimed conditional model or a heuristic surrogate.

3. **The masked diffusion objective is underspecified, and the claimed likelihood connection is too hand-wavy as written.**  
   On **Page 5**, **Equation (2)** defines
   \[
   \mathcal{L}(\theta_{\text{MD}})
   =-\mathbb{E}_{t,\hat{\mathbf{C}}_0^{(k)},\hat{\mathbf{C}}_t^{(k)}}\left[\frac{1}{t}\sum_j \mathbf{1}\{\hat{\mathbf{C}}_{t,j}^{(k)}=\operatorname{MASK}\}\log p_{\theta_{\text{MD}}}(\hat{\mathbf{C}}_{0,j}^{(k)}\mid \hat{\mathbf{C}}_t^{(k)},\mathbf{h}_k)\right].
   \]
   The text states that this “recovers an upper bound on the sequence negative log-likelihood,” but there is no derivation in the main paper, no assumptions spelled out, and no explanation of how the continuous time variable \(t\sim \mathcal U(0,1]\), the cosine masking schedule from **Section 3.3**, and the \(1/t\) weighting combine to produce that bound. Since this objective is the core of the diffusion module, the paper should either provide a concise derivation or substantially tone down the claim. Right now it reads as “trust us, it comes from the literature,” which is not enough for a central training equation.

4. **The decoding process is described in a way that is difficult to reproduce exactly, and some indexing is inconsistent.**  
   On **Page 5**, the iterative decoding update introduces \(\rho_n=\lambda(1-\frac{n}{N})\), then writes an update using \(\dot{\mathbf{C}}_{\rho_{n+1}}^{(k)}\) and \(\widehat{\mathbf{C}}_{\rho_n}^{(k)}\), but the confidence scores are denoted \(s_{\rho_n}(i)\) after having been introduced earlier as \(s_t(i)\). It is also unclear whether \(\Omega\) contains all masked positions, all editable positions including previously unmasked ones, or only the positions predicted in the current iteration. These details matter because remasking policy strongly affects masked diffusion behavior. Similarly, the paper says “sampling or choosing modes” for provisional completion, but does not specify whether temperature/top-\(k\)/top-\(p\) are applied before or after CFG, whether logits are renormalized per RVQ layer, or whether masked positions are sampled independently. This is exactly the sort of missing detail that blocks reproducibility.

5. **The role of overlapping patches is not convincingly justified empirically.**  
   The paper highlights overlapping windows as a design advantage in **Sections 3.1.2 and 3.2** on **Pages 5-6**, but almost all experiments appear to use the default \(P=S=8\), as stated in **Section 4.3** on **Page 8**. That means the main experiments do not actually test overlap. If overlap is supposed to be important for smoothing boundaries and improving information flow, the paper should show an explicit comparison between \(S=P\) and \(S<P\). Without that, this part of the proposed architecture is a claimed feature rather than a supported contribution.

6. **Some of the strongest empirical claims are overstated relative to the evidence provided.**  
   The abstract and conclusion repeatedly frame the method as surpassing state of the art in robustness, naturalness, and speaker/style consistency. But in **Table 1** on **Page 8**, the SIM scores are not consistently best, and DiSTAR-medium is still below human and below some baselines on speaker similarity depending on the dataset. In **Table 2** on **Page 9**, DiSTAR wins the subjective scores shown, but the comparison set is incomplete relative to Table 1, the evaluation protocol is not described in enough detail in the main paper, and there is no information about the number of raters, utterances per system pair, or significance testing. The paper is directionally strong, yes, but “surpasses SOTA” is stronger than what the main-paper evidence cleanly establishes across all metrics.

7. **The baseline comparison is not fully convincing because training data and setup parity are weakly controlled.**  
   The paper trains on the English subset of Emilia, roughly 50k hours, while some baselines such as F5TTS are known to have been trained at substantially different scales, and others are used via official checkpoints trained under different corpora and recipes. The paper does acknowledge using external checkpoints in **Appendix E**, but the main-paper comparisons in **Table 1** mix in-house models and third-party pretrained systems without carefully discussing data mismatch, prompt formatting mismatch, or whether all systems received identical acoustic prompts and text preprocessing. This weakens the causal claim that DiSTAR’s architecture is responsible for the gains, rather than some mixture of dataset, prompt handling, or codec choices.

8. **The ablations are too narrow for a paper whose contribution is heavily architectural.**  
   The main architectural pitch is the coupling of AR drafting and masked diffusion in discrete RVQ space, but the paper does not report several crucial controls in the main paper: no AR-only version, no masked-diffusion-only discrete version, no comparison between single historical patch vs. longer history, no ablation of the aggregator, and no explicit test of overlap. **Table 3** on **Page 9** is useful but only studies decoding heuristics; **Figure 2** only studies RVQ layer pruning. These are practical knobs, not the core scientific question. If the paper wants credit for the hybrid factorization, it needs a more surgical breakdown of which component is doing the heavy lifting.

9. **Figure 2 is suggestive, but the controllability argument is weaker than the text implies.**  
   In **Figure 2** on **Page 9**, SPK improves monotonically with more RVQ layers, while WER fluctuates and reaches its best value around six layers. This is interesting, but the evidence is thin: only two metrics are plotted, no error bars are shown, and no latency/FLOPs axis values are printed directly in the figure despite the text describing a compute-quality trade-off. If the core practical claim is “variable bitrate and controllable computation via RVQ layer pruning,” then the figure should include actual compute or bitrate numbers and preferably perceptual quality, not just SPK and WER. Otherwise the controllability story remains partially asserted.

10. **Presentation quality in the main paper is uneven, with many typos and naming inconsistencies that undercut confidence.**  
   Examples include “DtSTAR” instead of “DiSTAR” on **Page 5**, “Mask Diffusion Models” vs. “Mask Diffusion,” “iteratively decoding” in **Section 3.3** on **Page 6**, “comparative mean option score” instead of opinion score on **Page 8**, and several citation formatting glitches and grammar issues throughout. Normally this would be a minor complaint, but here it compounds a larger clarity problem: when the method already has many interacting moving parts, sloppy notation and editing make it harder to trust that the formulation is fully nailed down.

11. **The inference cost comparison is incomplete despite being emphasized as a practical advantage.**  
   The paper repeatedly discusses efficiency and states that DiSTAR maintains inference cost close to DiTAR, but the main paper does not provide a direct latency or throughput table against baselines. Reporting NFE alone in **Table 1** is not enough because AR cost, sequence length, patch size, hidden dimension, and vocabulary size all matter. A system with 24 diffusion iterations plus AR planning may still be very competitive, but the paper does not present the actual evidence needed to establish this beyond qualitative statements.

12. **The method contains several heuristic choices that are plausible but insufficiently justified.**  
   Examples include transplanting the first 16 codec channels into token embeddings on **Page 6**, stochastic layer truncation with uniform \(\ell\) on **Page 6**, the specific half-sampling/half-greedy schedule on **Pages 6-7**, and the repetition penalty in every \(P_r=4\) patches on **Page 7**. None of these is unreasonable, but together they make the system look fairly heuristic-heavy. The paper needs to separate “core idea” from “bag of tricks,” otherwise it is difficult to assess what would remain if the recipe were ported to another codec or dataset.

## Questions
1. **Please clarify the exact probabilistic training target when using overlapping windows (\(S<P\)).**  
   Are tokens in overlapping regions supervised multiple times across different \(k\)? If yes, what is the exact objective being optimized relative to Equation (1)? If no, how are ownership and masking defined for shared tokens? A precise formalization here would materially increase my confidence in the method.

2. **Can you provide a concise derivation or citation-to-equation mapping for Equation (2)?**  
   In particular, why is the weight \(1/t\) appropriate under your masking schedule, and under what assumptions does this become an upper bound on sequence NLL? A short derivation in the rebuttal would help, even if the full proof is omitted from the paper.

3. **What is the empirical contribution of the hybrid architecture itself?**  
   Please report, ideally on LibriSpeech-PC, comparisons to:  
   (a) AR-only generation in the same RVQ space,  
   (b) masked diffusion-only next-patch generation without the AR planner, and  
   (c) a version without the extra decoding heuristics.  
   This would help separate the architecture from the recipe engineering.

4. **Can you provide an explicit overlap ablation (\(S=P\) vs. \(S<P\))?**  
   Overlap is described as a meaningful design choice in Sections 3.1-3.2, but the main experiments appear to default to \(P=S=8\). If overlap helps, the paper should demonstrate it.

5. **Please add actual inference efficiency numbers.**  
   Wall-clock latency, tokens/sec, or real-time factor for DiSTAR vs. at least DiTAR and one strong discrete baseline would make the practical claims much more credible than NFE alone.

6. **Please expand the subjective evaluation protocol.**  
   For **Table 2**, how many raters participated, how many comparisons per system, were raters screened, how were prompts assigned, and are confidence intervals or statistical tests available? Since the paper leans on perceptual quality claims, this information is important.

7. **How sensitive is performance to the historical context length given to the diffusion model?**  
   Section 4.1 says the default is a single historical patch. Since local context is central to the method, it would be useful to know whether one patch is sufficient, or whether the gains come partly from that conditioning window size.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper is about high-quality zero-shot voice cloning, which raises obvious misuse risks including impersonation, spoofing, fraud, and non-consensual voice synthesis. The authors do acknowledge these concerns in **Appendix G / Boarder Impact** on **Page 16**, which is good, but the system’s zero-shot cloning ability is precisely the type of capability that can be abused. I do not view this as a reason to reject the paper on its own, but it does merit ethics review to ensure the paper’s release and framing appropriately address deployment safeguards, consent, and provenance/watermarking considerations.

## Soundness Rating
2: fair. The method is plausible and the empirical results are promising, but the core objective and patchwise probabilistic formulation are not sufficiently nailed down in the main paper, and several central claims rely on incomplete experimental support.

## Presentation Rating
2: fair. The paper is readable at a high level, and Figure 1 helps, but notation, wording, and several implementation details are too inconsistent for a clean technical presentation.

## Contribution Rating
2: fair. The paper addresses an important problem and shows encouraging results, but the contribution appears incremental relative to recent AR-plus-refinement and discrete masked modeling work, and the paper does not yet isolate the key scientific advance well enough.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The results are strong enough that I would not be shocked by acceptance, but in its current form the paper does not sufficiently separate architectural insight from a tuned engineering recipe, and the main-paper formulation/ablations are not strong enough for a positive recommendation.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. It is unlikely, but not impossible, that some missing implementation or derivational details would substantially change my view.