---
job_id: 5c9680d6-2d74-43a1-9a96-27f299679694
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: wA6dvVnKe8.pdf
paper: Model-Agnostic Adversarial Attack and Defense for Vision-Language-Action Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically adversarial robustness, representation learning in multimodal models, and applications to robotics and embodied AI.

## Minimum Quality
Pass ✅. The paper contains the required components, namely abstract, introduction, related work, methodology, experiments with quantitative results, discussion/limitations, and conclusion. While I have substantial concerns about novelty, evaluation breadth, and some mathematical/expositional choices, these are review-time quality issues rather than desk-reject-level omissions or fatal flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, instructions targeting automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies adversarial robustness of vision-language-action (VLA) models under physical-style patch attacks. The authors propose Embedding Disruption Patch Attack (EDPA), which generates universal adversarial patches by optimizing losses defined on the visual encoder embeddings and image-text alignment, and they also propose an adversarial fine-tuning method for the visual encoder to improve robustness. Experiments are conducted on LIBERO using OpenVLA, OpenVLA-OFT, and $\pi_0$, with comparisons to random noise and, for OpenVLA, prior VLA patch attacks UADA and UPA.

## Strengths
The paper addresses an important and timely problem. Robustness of VLA systems is genuinely consequential, because failures here are not just classification errors but policy failures in embodied settings. A paper that probes this space is relevant to the ICLR community.

The threat model is reasonably motivated. The core practical claim, namely that EDPA does not require knowledge of the downstream action space, manipulator semantics, or full LVLM parameters, is clearly presented and easy to understand. **Figure 1** is useful here: it gives a concise architectural overview and visually communicates the claimed access assumptions of EDPA versus UADA/UPA. That figure does real work for the paper, because the practical appeal of the method depends heavily on these assumptions.

The empirical attack effect is strong on the reported benchmark. In **Table 2**, EDPA drives OpenVLA failure rates to essentially $100\%$ on all four LIBERO suites before defense, and the comparison with UADA and UPA suggests that despite using less downstream-specific knowledge, EDPA remains similarly destructive on OpenVLA. Even if one debates novelty, the reported attack strength is hard to ignore.

The defense is simple and operationally convenient. Fine-tuning only the visual encoder while leaving the LVLM backbone untouched is an appealing design choice for practitioners. On **Table 2**, the adversarially fine-tuned encoder meaningfully reduces EDPA failure rates for OpenVLA, especially on Spatial and Object, and also improves robustness against UADA/UPA, which is a useful sign of some cross-attack benefit rather than a purely attack-specific patch.

The paper includes qualitative analysis beyond headline numbers. **Figure 2** provides patch visualizations, and the attention maps in **Figures 3 and 4** support the narrative that EDPA shifts token attention toward the patch location. These are not definitive mechanistic proofs, but they do provide a plausible qualitative story consistent with the reported attack behavior.

## Weaknesses
1. **The main conceptual contribution feels narrower than the paper claims, because EDPA is largely a straightforward adaptation of embedding-space adversarial objectives to the VLA patch setting.**  
   The paper repeatedly frames EDPA as model-agnostic and broadly practical, but the actual ingredients in **Equations (2), (3), and (4)** are conceptually quite standard: maximize discrepancy between clean and perturbed visual embeddings, and perturb image-text alignment. Section 3.2 itself acknowledges prior work showing the effectiveness of attacks targeting multimodal embeddings. What is new here is mainly the application of these ideas to a universal patch attack against VLA models, plus the specific combination of two losses. That is a valid contribution, but the manuscript oversells this as if the attack objective itself were substantially new. This matters because for ICLR main track, the bar is not just “works on an important domain,” but also clear methodological or scientific advancement. As written, the novelty margin over existing representation-space attacks appears modest.

2. **The “model-agnostic” claim is overstated relative to the actual access assumptions.**  
   The paper contrasts EDPA favorably against UADA/UPA in **Table 1** and **Figure 1**, but EDPA still requires access to encoder parameters and textual embeddings, and therefore remains far from black-box or even broadly gray-box in many realistic deployments. In practice, many VLAs are not exposed in a way that grants gradient access to the encoder. So the method is model-agnostic only in a narrow sense, namely agnostic to action-space semantics and manipulator structure, not agnostic to model internals. The current wording risks conflating “less task-specific white-box” with “practical.” This matters because the central selling point of the paper is practicality. The paper would be stronger if it framed EDPA as reducing *which* internal knowledge is needed, rather than suggesting a much weaker-access threat model than it actually uses.

3. **The mathematical formulation of the patch contrastive loss is questionable and under-justified for the intended optimization direction.**  
   In **Equation (2)**, $\mathcal{L}_{\text{patch}}$ is written in an InfoNCE-like form:
   \[
   \mathcal{L}_{\text{patch}}=-\frac{1}{N}\sum_{i=1}^{N}\log\frac{\exp(\cos(\mathbf{p}_i,\mathbf{p}'_i)/\tau)}{\sum_{j=1}^{N}\exp(\cos(\mathbf{p}_i,\mathbf{p}'_j)/\tau)}.
   \]
   Standard InfoNCE is usually *minimized* to align positives and repel negatives. Here, in **Equation (4)**, the patch is obtained by *maximizing* this loss. That can indeed reduce positive-pair similarity, but the paper never explains the induced gradient behavior or why this specific objective is preferable to simpler and more direct discrepancy objectives such as $-\frac{1}{N}\sum_i \cos(\mathbf{p}_i,\mathbf{p}'_i)$ or an $\ell_2$ distance between embedding sets. Since the denominator also depends on all $\mathbf{p}'_j$, maximizing this objective is not simply “maximize discrepancy,” and may encourage patch-wise permutation effects rather than pure semantic disruption. The paper should justify why this exact formulation is the right one for universal patch construction, or at least provide an ablation replacing Eq. (2) with simpler alternatives. As written, the choice feels somewhat cargo-culted from contrastive learning rather than carefully derived for the attack objective.

4. **The alignment loss in Equation (3) is simplistic and potentially misaligned with the semantics it is supposed to capture.**  
   The paper defines
   \[
   \mathcal{L}_{\text{align}}=\frac{1}{N M}\sum_{i=1}^{N}\sum_{j=1}^{M}\left|\cos(\mathbf{p}_i,\mathbf{w}_j)-\cos(\mathbf{p}'_i,\mathbf{w}_j)\right|.
   \]
   This treats every visual patch token and every instruction token equally. There is no weighting for semantically important text tokens, no masking of stopwords, no accounting for patch position, and no attempt to isolate the tokens that actually drive action generation. In a long instruction, many token-patch pairs are semantically irrelevant, so averaging uniformly over all $N\times M$ pairs may dilute the very alignment signal the method claims to disrupt. The fact that **Figure 6** shows the method often working even with $\alpha_1=1$ or near it suggests that the alignment term may contribute less than advertised, yet the main paper does not quantify its marginal value. This matters because one of the two stated pillars of the method may be mostly decorative.

5. **The defense is weakly evaluated and may largely amount to attack-specific encoder regularization.**  
   The adversarial fine-tuning scheme in **Equation (5)** and **Algorithm 1** trains the visual encoder using patches generated by the same EDPA process that defines the threat. Unsurprisingly, this helps against EDPA. The paper does show some gains against UADA and UPA in **Table 2**, which is good, but the defense evaluation is still narrow: only OpenVLA is defended, there is no comparison against a simpler robustification baseline such as random-patch augmentation, standard adversarial image augmentation, or even fine-tuning with only the clean consistency term. Without such baselines, it is hard to know whether the proposed defense is specifically effective or simply benefits from exposing the encoder to visible perturbations during training. This is important because the defense is presented as a major contribution, yet the evidence currently supports only a fairly limited claim.

6. **The empirical evaluation is too narrow to fully support the broader robustness claims.**  
   All experiments are on LIBERO simulation. That is a reasonable starting point, but the paper’s framing repeatedly invokes real-world practicality and physically placeable patches. The gap between simulation and physical deployment is substantial here: lighting, viewpoint variation, print fidelity, camera noise, and robot dynamics can all affect patch effectiveness. The authors acknowledge some multi-camera limitations in Section 6, but the overall narrative still leans much harder on “practical for real-world scenarios” than the evidence supports. At minimum, the claims should be toned down. Better yet, the paper should include stronger stress tests in simulation, such as random patch placement, scale changes, rotations, photometric variation, or partial occlusion. Right now, the attack is physically motivated but still only demonstrated in a fairly controlled benchmark setting.

7. **Important experimental details needed to judge the attack are underspecified.**  
   A patch attack paper lives or dies on the exact patch application protocol, yet several details are vague. Equation (1) defines a generic patch mask, but the main paper does not clearly specify whether patch location is fixed or randomized during training and testing, whether placement is consistent across models/suites, and how placement is chosen when comparing EDPA against random noise, UADA, and UPA. This matters a lot because attack strength can vary dramatically with location. The appendix states that attention visualizations fix the patch to the top-left corner, but that does not clarify the default evaluation protocol. Likewise, for multi-camera evaluation in Section 4.3, the paper says separate patches are applied independently to primary and wrist cameras, but it is not precise about whether each patch is optimized jointly across both views or optimized per camera and then combined. These are not cosmetic details; they are central to interpreting the reported failure rates.

8. **The reported results, while strong, also expose limited robustness gains from the defense on the harder suites, which the paper somewhat glosses over.**  
   In **Table 2**, the defense helps substantially on Spatial and Object, but on Goal and especially Long the residual failure rates remain very high. For example, under EDPA the adversarially fine-tuned OpenVLA still has FR $73.9$ on Goal and $91.2$ on Long; under UADA it remains $91.6$ and $97.4$ on Goal and Long. That is not a small caveat. It means the defense is far from making the model robust in the more difficult settings. The text emphasizes relative reductions, but absolute robustness remains poor. This matters scientifically because a reader could easily come away with the impression that the proposed defense “effectively mitigates” the attack in a broad sense, whereas the stronger conclusion is that it provides partial robustness improvements, mostly on easier suites.

9. **The interpretation around multi-camera robustness is speculative and not well controlled.**  
   In Section 4.3 and Section 5, the authors suggest that OpenVLA-OFT and $\pi_0$ may be more robust because multiple camera views provide additional visual information, and further speculate that visual-encoder overfitting to the robot arm explains the differences seen in **Figure 2**. This is plausible, but the comparison is confounded by many model differences beyond camera count, including architecture, pretraining, and fine-tuning pipeline. The paper itself briefly admits this, but still advances the interpretation rather confidently. The patch visualizations in **Figure 2** are intriguing, especially the robot-arm-like textures, yet they are anecdotal and should not be elevated into a causal explanation without controlled evidence. A stronger paper would test this hypothesis directly, for example by measuring robustness under camera ablations or comparing single-view and dual-view variants of the same model.

10. **There are presentation and notation issues that reduce confidence in the technical polish.**  
   The writing is generally understandable, but there are several awkward or incorrect phrasings, for example on Page 2, “Due to our experimental results showed that OpenVLA exhibited the weakest robustness...”, and multiple singular/plural or grammar mistakes throughout. More importantly, some notation is overloaded or imprecise. In **Equation (4)**, the expectation is written over $v\sim\mathcal{D}$, but the loss also depends on instruction $t$; formally the data distribution should be over $(v,t)$ pairs. In **Algorithm 1**, line 9 defines the encoder training loss, but line 10 says “Update $\mathcal{E}_v$ by gradient descent” without explicitly stating the gradient is taken with respect to $\mathcal{L}$, and line 11’s placement makes it look as if the function returns after one iteration rather than after the loop. These are fixable issues, but they matter because this is a methods paper whose core technical contribution is the optimization setup.

## Questions
1. Please clarify the exact patch placement protocol used in all main experiments. Is the patch location fixed or randomized during EDPA optimization, and fixed or randomized during evaluation? If fixed, where is it placed? If randomized, over what distribution? A precise answer is important because the reported FR values in **Tables 2 and 3** depend heavily on this choice.

2. Can the authors provide an ablation isolating the value of each loss term in the main paper, not only via varying $\alpha_1$ in the appendix but with explicit reporting for $\mathcal{L}_{\text{patch}}$ only, $\mathcal{L}_{\text{align}}$ only, and the combined objective, alongside the corresponding clean/attack trade-offs? This would increase confidence that Equation (3) is genuinely useful rather than incidental.

3. Why is the InfoNCE-style objective in **Equation (2)** the right discrepancy measure to maximize? Please explain what maximizing this loss does geometrically to the embedding sets, and ideally compare it against simpler alternatives such as negative cosine similarity or direct feature-distance maximization.

4. For the defense, what happens with simpler baselines, for example random visible patch augmentation, adversarial fine-tuning using only the second term of **Equation (5)**, or standard image-space perturbation augmentation? If these already provide similar gains, the claimed contribution of Algorithm 1 would be weaker.

5. In Section 4.3, how are patches optimized for the two-camera setting exactly? Are there two independent universal patches, one per camera, jointly optimized over the same minibatch, or separately trained? Clarifying this would help interpret the OpenVLA-OFT and $\pi_0$ results in **Table 3**.

6. The defense is evaluated only on OpenVLA. Is there any technical reason it cannot be applied to OpenVLA-OFT or $\pi_0$? Even a brief explanation would help, since otherwise the paper’s attack section is multi-model but the defense section is effectively single-model.

7. The attention maps in **Figures 3 and 4** are visually suggestive, but can the authors provide a quantitative statistic, such as average attention mass assigned to the patch region versus non-patch regions, to support the qualitative interpretation?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper proposes an attack that is explicitly designed to cause embodied agents to fail physical tasks by inserting adversarial patches into the robot’s visual field. This clearly falls under security and safety concerns because such attacks could, in principle, be used to induce unsafe robot behavior, including manipulation failures or hazardous motions. The ethics statement acknowledges this risk. I do not see undisclosed human-subjects or data-governance concerns in the main paper, but the attack methodology itself warrants ethics review because the work lowers the barrier for attacking VLA systems and frames the perturbation as physically deployable.

## Soundness Rating
2: fair. The empirical results are strong on the reported benchmark, but several methodological details are underspecified, the mathematical motivation for the chosen losses is not sufficiently justified, and the defense evaluation is too narrow to fully support the breadth of the claims.

## Presentation Rating
2: fair. The paper is readable and mostly organized well, and figures/tables are helpful, but there are notable writing issues, some ambiguous notation, and missing implementation details that matter for reproducibility and interpretation.

## Contribution Rating
2: fair. The paper tackles an important problem and demonstrates that embedding-based patch attacks are effective on VLAs, but the methodological novelty is limited and the scope of evidence is narrower than the framing suggests.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The problem is important and the empirical attack results are striking, but the paper currently feels too narrow and somewhat over-claimed for ICLR main track. The attack is a fairly direct adaptation of known embedding-disruption ideas, the defense evidence is limited, and several core technical and experimental details need sharper justification.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main equations, algorithm, figures, and results tables carefully.