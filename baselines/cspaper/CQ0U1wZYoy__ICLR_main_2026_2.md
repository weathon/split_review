---
job_id: d74f55ad-6073-4e8d-85bb-8b558c71c76b
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: CQ0U1wZYoy.pdf
paper: Seeing Through the Prism: Compound & Controllable Restoration of Scientific Images
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies representation learning, conditional diffusion, compositional modeling, controllable restoration, and evaluation for scientific imaging.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, method, experiments/results, and conclusion, and it presents a coherent methodological contribution with substantial empirical evaluation. I do see important weaknesses in methodology and exposition, but not issues severe enough to warrant desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeted instructions, or other obvious manipulation attempts in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes PRISM, a prompted conditional diffusion framework for restoring scientific images affected by compound degradations. The method combines compound-aware supervision on synthetic mixed degradations with a contrastive objective over CLIP image embeddings, aiming to organize primitive and compound distortions in a compositional latent space that supports both joint restoration and selective prompt-based correction. The paper evaluates PRISM on a mixed degradation benchmark, several zero-shot real-domain restoration settings, and downstream scientific tasks across remote sensing, wildlife monitoring, microscopy, and urban scenes.

## Strengths
The paper tackles a real and important problem. The central motivation, that scientific image restoration should prioritize task fidelity and selective control rather than generic visual enhancement, is compelling and well argued throughout the paper. This framing is stronger than the usual “all-in-one restoration” pitch and feels particularly relevant for AI-for-science applications.

The empirical scope is broad. The paper does not stop at standard restoration metrics, but also includes downstream evaluations in four application domains. I especially appreciated the microscopy case study, because it concretely shows that “better looking” restoration is not necessarily better for scientific use. **Figure 6** is one of the more persuasive parts of the paper: the red-circled regions make the failure mode visually concrete, namely that adding denoising on top of super-resolution suppresses faint structures that matter for segmentation. That qualitative point is also reflected quantitatively in **Table 4**, where “Super-Resolution” gives the best segmentation mIoU (0.580) but a worse fluorescence MSE than “Denoise,” illustrating the task-dependent tradeoff the paper wants to emphasize.

The restoration results are strong across the reported benchmarks. On the main mixed degradation benchmark, **Table 1** shows PRISM outperforming the listed baselines on PSNR, SSIM, and LPIPS, with a large PSNR margin over the strongest competitors. The gains are not tiny, for example 22.08 dB for PRISM versus 20.84 for MPerceiver and 20.42 for AutoDIR. The zero-shot results in **Table 2** are also consistently favorable across UIEB, POLED, and ThapaSet. Even if I have some concerns about the evaluation protocol there, the reported numbers suggest the approach is at least competitive in difficult settings.

The paper does a good job visually communicating the system. **Figure 2** gives a clear high-level picture of the two-stage design, namely a degradation-aware CLIP image encoder followed by diffusion-based restoration and a refinement module. This figure makes the architecture much easier to parse than the text alone. Similarly, **Figure 4** is useful in illustrating the intended benefit of latent disentanglement, namely narrowing the gap between sequential and single-shot prompting.

I also think the paper’s claim that controllability matters is supported better than in many prompt-based restoration papers. **Table 3** is a meaningful result: selective restoration outperforms full automatic restoration in three of four downstream tasks, and the effect sizes are nontrivial in microscopy and urban scenes. This is a useful contribution for the community, because it pushes evaluation beyond aesthetic restoration.

## Weaknesses
1. **The core methodological novelty is narrower than the paper’s framing suggests, and the paper does not isolate the new ingredient sharply enough.**  
   The overall system combines already familiar components: a CLIP-based conditioning space, prompt-conditioned restoration, latent diffusion, and a refinement module. The part that appears most specific to this paper is the weighted contrastive objective over compound degradation sets in **Section 3.2**. However, the experimental evidence does not cleanly isolate whether the gains come from the proposed Jaccard-weighted compositional geometry, from simply fine-tuning CLIP on degradation labels, from exposure to mixed degradations, or from the rest of the diffusion stack.  
   **Figure 3** moves in the right direction, but it still does not fully answer the key question. It compares “Primitive-Aware CLIP” and “Compound-Aware,” and also a training regime on primitive distortions only, but it does not explicitly show an ablation from weighted vs. unweighted contrastive loss, or from Jaccard weighting vs. a simpler multi-label contrastive setup. Since the paper attributes much of the advantage to the structured latent geometry, this missing ablation matters a lot scientifically. Without it, the reader cannot tell whether the weighting scheme in **Equation (1)** is essential or whether standard contrastive fine-tuning plus composite training would have delivered nearly the same gains.

2. **The mathematical formulation around the contrastive objective is underspecified and somewhat at odds with the geometric claim being made.**  
   In **Section 3.2**, the paper defines
   \[
   w_{jk} = \exp\left(1 - \frac{|d^{(j)} \cap d^{(k)}|}{|d^{(j)} \cup d^{(k)}|}\right),
   \]
   and uses these weights inside the denominator of
   \[
   \mathcal{L}_{\mathrm{ctr}}^{(j)} = -\log \frac{\exp(\sin(e_{\mathrm{dist}}^{(j)}, e_{\mathrm{clean}})/\tau)}{\sum_{k\neq j} w_{jk}\exp(\sin(e_{\mathrm{dist}}^{(j)}, e_{\mathrm{dist}}^{(k)})/\tau) + \sum_{l\in \mathcal{B}_{\mathrm{other}}}\exp(\sin(e_{\mathrm{dist}}^{(j)}, e_{\mathrm{other}}^{(l)})/\tau)}.
   \]
   This means more dissimilar sibling distortions receive *larger* weights in the negative term, while more overlapping distortion sets receive smaller weights. That can be a reasonable design choice, but it does **not** by itself “pull compound distortions toward the span of their primitives,” as later claimed around **Page 8** and in the discussion of **Figure 4**. At best, it repels unrelated distortions more strongly than related ones. That is a softer and more indirect statement than the geometric interpretation used in the paper. If the authors want to claim latent compositionality rather than just graded repulsion, they should either provide a more direct positive alignment term between mixtures and primitives or temper the claim substantially.

3. **Several pieces of the training objective are missing important implementation details, which makes the method harder to evaluate and reproduce.**  
   The quality-aware regularizer
   \[
   \mathcal{L}_{\mathrm{qual}}^{(j)} = \sum_{c\in d^{(j)}} \hat{p}(c\mid e_{\mathrm{clean}})
   \]
   is not fully specified. What exactly is the classifier producing \(\hat{p}(c\mid e_{\mathrm{clean}})\)? Is it a multi-label head trained jointly with the encoder? Is it calibrated with sigmoid outputs or softmax over distortions? Is it trained on primitives only or also compound labels? Since this term is part of the final encoder loss, the omission is not cosmetic. It affects the interpretation of the objective and whether the regularizer is actually meaningful.  
   There is also notation that needs cleaning up. The paper writes “for cosine similarity \(\sin(\cdot,\cdot)\),” which is unusual and confusing notation. \(\sin\) conventionally denotes the sine function, not cosine similarity. Similarly, the batching description below the loss is hard to parse: “We use \(\mathcal{B}=256\) clean images per batch, each with \(\mathcal{B}_{\mathrm{other}}=256\) randomly sampled degraded variants...” leaves ambiguity about whether the negatives are in-batch, cross-image, or sampled externally. These are not fatal issues, but in a methods paper centered on the loss design, they matter.

4. **The zero-shot evaluation protocol in Section 4.2 raises fairness concerns, because prompt selection appears to rely on the proposed model’s own encoder.**  
   The paper states on **Page 8** that for each real dataset, “we use the compound-aware CLIP encoder to identify the fixed set of distortion types present in the images of each dataset. We then apply the same manual prompts over this standardized set for all models.” This is a problem. The prompt space for evaluating all methods is being constructed using PRISM’s own learned distortion representation. Even if the exact same prompts are then applied to all baselines, the evaluation protocol is not model-agnostic. It potentially advantages PRISM by using its own taxonomy or detections to define what restoration actions should be attempted.  
   This matters because the paper’s zero-shot claim is not just about denoising quality, but about compositional interpretability and controllability. A fairer protocol would define prompts independently of PRISM, for example from human annotations, metadata, or a fixed external mapping. As written, **Table 2** is interesting but not fully convincing as evidence of superior zero-shot compositional reasoning.

5. **The controllability story is compelling, but the downstream evaluation in Table 3 is narrower than the paper’s claims.**  
   **Table 3** compares degraded input, full restoration, and selective restoration, but only for PRISM. This supports the statement that *within PRISM*, selective control can help downstream accuracy. What it does **not** show is whether PRISM’s controllability is better than controllable baselines, or whether comparable gains could be achieved by prompt engineering with existing methods such as PromptIR, MPerceiver, or AutoDIR. Since the paper makes a stronger claim that PRISM’s *structured* controllability is different from ordinary prompt-conditioning, a comparison against prompt-conditioned baselines on partial restoration tasks would be important.  
   Relatedly, the paper uses only three random seeds and reports p-values for four domains, but does not discuss multiple-comparison correction or the exact statistical test used. With such small \(n\), the significance claims should be phrased carefully. The microscopy and urban improvements are meaningful, but the inferential framing is somewhat stronger than the evidence warrants.

6. **The paper’s strongest empirical claims rely heavily on synthetic training mixtures, and the bridge from synthetic compositionality to real physical degradations remains partly speculative.**  
   The training pipeline in **Section 3.1** applies up to three randomly ordered synthetic distortions. That is practical, but it does not guarantee that the learned latent space reflects real degradation mechanisms rather than a broad but still synthetic augmentation manifold. The paper acknowledges this late on **Page 10**, but the central narrative about “compositional logic” and “mapping unseen mixtures into a known coordinate system” goes beyond what is actually demonstrated. The real-world evaluations are encouraging, yet they remain relatively small and do not fully establish that the latent geometry is physically meaningful across domains.

7. **Some claims in the text are overstated relative to the presented evidence.**  
   For example, on **Page 8**, the paper says the contrastive design “enforces a compositional logic” that lets the model interpolate a restoration strategy for novel compounds. What is shown empirically is improved performance on selected unseen datasets, not a formal or tightly controlled demonstration of compositional generalization. Likewise, the text around **Figure 4** says latent disentanglement “enables both stepwise and single-shot restoration,” but the figure reports only PSNR for sequential vs. composite settings and does not measure whether the requested partial transformation was followed faithfully without unintended side effects. For a controllability paper, restoration faithfulness under subset prompts should be evaluated more directly, not inferred from overall image similarity alone.

8. **The presentation is generally good, but there are enough inconsistencies and minor errors to reduce confidence in the polish of the work.**  
   A few examples: “MPerceover” in **Table 1** appears to be a typo for MPerceiver; “underdisplay” in **Table 2** should likely be “under-display”; the references contain some duplication or formatting inconsistency; and the jump from the loss equations to the high-level geometric claims is too quick. These are fixable issues, but the paper is trying to sell a subtle representational idea, so sharper exposition would help.

## Questions
1. The biggest question for me is about the contribution of the weighted contrastive loss itself. Can the authors provide a direct ablation comparing:  
   (a) no CLIP fine-tuning,  
   (b) CLIP fine-tuning with standard InfoNCE or unweighted contrastive loss,  
   (c) CLIP fine-tuning with the proposed Jaccard-weighted loss,  
   while keeping the diffusion backbone and training data fixed? This would materially increase my confidence in the central claim.

2. Please clarify the exact implementation of \(\mathcal{L}_{\mathrm{qual}}\). What model produces \(\hat{p}(c\mid e_{\mathrm{clean}})\)? Is it trained jointly, and with what labels and loss? Is it multi-label sigmoid classification over primitive distortions? This is important for understanding the objective.

3. Can the authors justify more carefully why the weighting
   \[
   w_{jk} = \exp(1 - \mathrm{Jaccard}(d^{(j)}, d^{(k)}))
   \]
   should induce the claimed compositional geometry? As written, it seems to modulate negative repulsion strength, not explicitly align compound embeddings with primitive embeddings. A short derivation or geometric explanation would help.

4. For the zero-shot experiments in **Table 2**, can the authors report a version where the prompt set is chosen independently of PRISM’s encoder, for example using human-defined prompts or a fixed dataset-level mapping? That would address my main concern about fairness in the protocol.

5. For the controllability claim, can the authors compare PRISM against at least one prompt-based baseline on *selective* restoration, not just full restoration? If PRISM’s advantage is truly “structural controllability” rather than ordinary prompting, that comparison seems essential.

6. **Figure 4** is suggestive, but could the authors add a more direct faithfulness metric for partial restoration, for example measuring whether requested distortions are removed while non-requested ones are preserved? Right now the evidence is mostly indirect.

7. Since **Table 3** reports p-values over only three seeds, please specify the statistical test and whether any correction for multiple comparisons was applied. If not, I would encourage softening the significance language.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses public datasets and synthetic distortions, and the main ethical concern, namely that restoration may introduce misleading artifacts in scientific settings, is already acknowledged in the ethics statement. I do not see a specific issue that requires separate ethics escalation based on the main paper.

## Soundness Rating
3: good. The method is plausible and supported by substantial experiments, but there are meaningful concerns about underspecified objectives, over-interpretation of the latent geometry, and evaluation fairness in the zero-shot setup.

## Presentation Rating
3: good. The paper is readable and well organized overall, with helpful figures such as **Figure 2** and **Figure 6**, but some equations, notation, and evaluation details need clarification.

## Contribution Rating
3: good. The scientific-restoration framing and downstream utility evaluation are valuable, and the empirical results are strong, but the methodological increment over prior prompted restoration and degradation-aware representation learning is more modest than the paper sometimes implies.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
This is a solid, useful paper with an important motivation and a broad empirical study. I am positive on the problem framing, the downstream-task emphasis, and the overall level of results. My hesitation is that the core representational claim, namely that the proposed loss induces a compositional latent geometry enabling reliable controllability and zero-shot mixtures, is not isolated or validated as cleanly as it should be. I lean positive, but only slightly.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the restoration, diffusion, and representation-learning context, though a few implementation details are underspecified enough that some interpretation remains uncertain.