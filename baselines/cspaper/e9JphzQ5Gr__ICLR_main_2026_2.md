---
job_id: c51b5b7c-3ca1-408a-8d31-b872ba3cc52b
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: e9JphzQ5Gr.pdf
paper: CLIP as a Prior Teacher: Breaking the Label Dependency in Semi-Supervised Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is squarely within ICLR scope, it studies semi-supervised learning, representation learning, and the use of vision-language models as priors for low-label learning.

## Minimum Quality
Pass ✅ The paper includes the expected scientific components, namely abstract, introduction, related work, method, experiments, quantitative results, and conclusion/limitations. While I have technical and empirical concerns, they do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies the dependence of semi-supervised learning on the quantity and quality of labeled data, and proposes CaPT, an asymmetric co-training framework that combines a fully fine-tuned unimodal classifier with an adapter-tuned CLIP branch. The two branches exchange supervision through entropy-weighted co-pseudo labels, with the goal of using CLIP as a prior teacher that remains helpful when standard SSL begins to fail under extreme label scarcity. The paper reports strong empirical gains on several benchmarks, especially in very low-label settings, and includes a simple theoretical bound intended to motivate the notion of label dependency.

## Strengths
The paper is well motivated, and the motivation is not just rhetorical. **Figure 1(a-c)** gives a coherent empirical story: standard SSL methods degrade badly when moving to one-label-per-class, pseudo-label accuracy becomes sensitive to prototype quality, and the gain from unlabeled data collapses in the most label-starved regime. Even if the later theorem is stylized, the paper does a good job of first establishing the practical problem it wants to solve.

The proposed system is easy to understand at a high level. **Figure 4** is one of the better parts of the paper, because it clearly separates the roles of UPM, MPM, and PFM, and makes the intended information flow between the unimodal model and the CLIP branch quite concrete. The design choice of giving the unimodal model the heavy learning burden while using CLIP in a parameter-efficient way is sensible from a systems perspective.

The empirical results are strong in the low-label regimes that the paper explicitly targets. In **Table 1**, CaPT improves over strong recent SSL baselines on all six USB settings, and the margin on CIFAR-100 with 2 labels/class is especially large, \(84.83\) vs \(80.74\) for RegMixMatch. In **Table 3**, the one-label-per-class CIFAR-100 result is striking, \(82.51\) for CaPT versus \(61.13\) and \(60.49\) for FreeMatch and RegMixMatch. If these numbers hold under the same protocol, that is a practically important result.

The paper also makes a reasonable effort on efficiency. **Table 4** suggests that the additional CLIP branch is not prohibitively expensive relative to plain SSL training, at least under the reported setup. The reported increase over FreeMatch is modest compared with the performance gain, which helps support the paper's “prior teacher” framing.

The ablation section is useful rather than decorative. **Table 6** does show that the full method is stronger than several reduced variants, and the separation between “only UPM”, “only MPM”, “CaPT-Deb”, and “CaPT-Uni” is helpful for understanding what ingredients matter. I also appreciated that **Figure 5** is used to support the claim that adapter tuning reduces CLIP bias on EuroSAT, instead of leaving that claim purely verbal.

## Weaknesses
I think the paper has a real idea and strong headline numbers, but there are several technical and empirical issues that currently hold it below the bar for me.

1. **The central mathematical formulation in the method has a serious notation and objective problem, especially around pseudo-label fusion.**  
   On **Page 5, Equation (3)** and again on **Page 6, Equation (10)**, the pseudo label is defined as \(\hat q = \arg\max(q^{w,a})\) and \(\hat q^a=\arg\max(q^{w,a}), \hat q^b=\arg\max(q^{w,b})\). Written literally, \(\arg\max\) returns a class index, not a probability vector. But then **Equation (13)** forms
   \[
   \hat q^c = \Gamma^a \hat q^a + \Gamma^b \hat q^b,
   \]
   which only makes sense if \(\hat q^a,\hat q^b\) are one-hot vectors or soft distributions, not integer class IDs. This is not a cosmetic issue. It is the core supervision signal of the method. If the implementation uses one-hot vectors, the paper should say so explicitly. If it uses softened distributions rather than one-hot pseudo labels, then Equations (3) and (10) are incorrect. The same ambiguity carries into **Equation (15)**, where \(CE(\hat q^c_j, q^{s,a}_j)\) is used. Cross-entropy with a weighted pseudo-label target is perfectly valid, but only when the target is defined as a probability vector. Right now the math does not cleanly specify the training objective.

2. **Equation (8) appears to have an indexing error in the softmax denominator.**  
   On **Page 5**, the paper defines
   \[
   p_i = \frac{\exp\left(\frac{W_i^{*T} f^*}{\tau}\right)}{\sum_{j=1}^C \exp\left(\frac{W_i^{*T} f^*}{\tau}\right)}.
   \]
   The denominator repeats \(W_i^*\) instead of using \(W_j^*\). As written, this does not define a valid multiclass softmax classifier. I assume this is a typo and the intended formula is
   \[
   p_i = \frac{\exp\left(\frac{W_i^{*T} f^*}{\tau}\right)}{\sum_{j=1}^C \exp\left(\frac{W_j^{*T} f^*}{\tau}\right)}.
   \]
   But when a paper’s central prediction equation is misstated, that hurts confidence in the care with which the method section was prepared. Please correct this explicitly.

3. **The thresholding / masking behavior is underspecified, even though it materially affects the loss.**  
   On **Page 7**, after **Table 1**, the paper says that a pseudo label is retained only if the weak-prediction confidence exceeds a threshold; otherwise that module’s pseudo label is replaced by the all-zero vector, and the resulting co-pseudo label may sum to less than 1. This is a meaningful departure from standard pseudo-labeling formulations, because now the cross-entropy target in **Equation (15)** is not necessarily normalized. The paper does not precisely define:
   - what confidence score is thresholded for each branch,
   - whether the threshold is the same for UPM and MPM,
   - whether the threshold is adaptive exactly as in FreeMatch or modified,
   - whether the zeroed target is re-normalized before cross-entropy,
   - and how samples with both branches filtered out are handled.  
   Since the claimed robustness depends heavily on pseudo-label filtering, this missing specification matters for both reproducibility and scientific interpretation.

4. **The theorem is only loosely connected to the actual method and overstates what it explains about modern SSL.**  
   **Theorem 1.1 on Pages 1-2** gives a high-probability bound for nearest-prototype pseudo-label error under a Gaussian mixture model with prototype bias. This is a simple stylized argument, but the paper phrases it as establishing a “fundamental limitation of existing SSL methods.” That claim is much broader than what the theorem actually shows. The theorem does not analyze consistency regularization, thresholding, teacher-student dynamics, or the specific co-training mechanism proposed in CaPT. It only shows that a nearest-prototype classifier becomes less reliable with larger prototype bias and fewer labels, which is intuitive.  
   There is also a notational inconsistency between **Equation (1) on Page 1** and **Theorem A.1 on Page 15**. On Page 1,
   \[
   \varepsilon_n := \frac{2\sigma}{\sqrt{n_{\min}}}\sqrt{\log\left(\frac{K\,2^{d/2}}{n}\right)},
   \]
   where the denominator is written as \(n\). In the appendix, the denominator is \(\eta\), which is the correct quantity for a probability bound. This is not minor, because it changes the statement of the theorem in the main paper.

5. **The empirical comparison somewhat mixes two sources of advantage, namely the proposed SSL mechanism and the use of a large pretrained vision-language prior.**  
   The paper’s framing is that CaPT breaks SSL’s label dependency, but the practical mechanism is to inject CLIP’s pretrained knowledge. That is a meaningful strategy, but then the comparison against standard SSL baselines in **Tables 1-3** is not purely an algorithmic SSL comparison. It is partly a comparison between “SSL without a large external vision-language prior” and “SSL with a large external vision-language prior.” I am not saying this is unfair per se, but the paper should be more careful in how it interprets the gains. Some of the advantage may come from the pretrained multimodal knowledge itself rather than the specific co-pseudo-label design. The ablations help, but they do not fully disentangle this.

6. **The experimental positioning against other ways of using VLMs as teachers is too narrow in the main paper.**  
   The paper compares mainly against standard SSL methods, with DebiasPL and CLS discussed but not given front-and-center main-text benchmarking except through ablations and appendix material. Given the claim that CaPT is a better way to integrate CLIP into SSL, stronger direct comparisons against CLIP-based teacher/distillation alternatives would have made the paper much more convincing. Right now, the main evidence mostly says “CaPT beats classic SSL baselines,” not “CaPT is the best way to exploit a pretrained VLM in SSL.”

7. **Some results complicate the narrative and are under-discussed.**  
   In **Table 1**, on STL10 the standalone **adapter-tuned CLIP** is actually better than CaPT, \(96.86\) and \(97.15\) versus \(96.07\) and \(96.34\). Also the zero-shot CLIP baseline is \(97.18\), higher than CaPT in the reported STL10 setup. This is quite important because it means the proposed co-training can underperform simply using CLIP itself on at least one benchmark. Yet the discussion on **Pages 7-8** presents Table 1 almost entirely as a universal win story. A more honest analysis is needed here: when does co-training with a unimodal SSL model help, and when does it dilute a strong VLM prior?

8. **The “asymmetric-modalities mitigate pattern homogeneity” claim is suggestive but not fully established in the main paper.**  
   **Figure 3** is visually interesting and does support the intuition that CLIP and a plain ViT may attend to different regions. But attention maps on a handful of examples are weak evidence for the rather strong claim that asymmetric modalities are what materially drive the co-training advantage. The stronger quantitative evidence, namely conditional mutual information in **Figure 6** and **Table 7**, is relegated to the appendix. In the main paper, the argument is mostly intuition plus pictures. For a central conceptual claim, I would want either stronger main-text quantitative evidence or a more modest claim.

9. **The portability/general-framework claim is stronger than what the main paper actually demonstrates.**  
   The conclusion says CaPT is a “general and future-proof framework,” but in the main paper the system is instantiated almost entirely with CLIP. Evidence with other VLMs appears only later in the appendix. If portability is claimed as a main contribution, it should be substantiated in the main paper, not mostly deferred.

10. **Presentation quality is mixed despite the paper being readable overall.**  
   There are several places where the exposition slips from polished to sloppy: the indexing bug in **Equation (8)**, the pseudo-label type ambiguity in **Equations (3), (10), (13), (15)**, the \(\eta\) vs \(n\) inconsistency in the theorem statement, and a few awkward phrases. None of these individually kills the paper, but together they matter because they touch the core method rather than peripheral details.

## Questions
1. In **Equations (3), (10), and (13)**, are \(\hat q^a\) and \(\hat q^b\) intended to be class indices, one-hot vectors, or full soft distributions? Please rewrite these equations precisely. This is the single most important clarification for me.

2. In **Equation (15)**, when one branch is filtered and replaced by the all-zero vector, do you compute cross-entropy with a target whose entries sum to less than 1, or do you re-normalize the target? Also, what happens when both branches are below threshold for the same sample?

3. Please confirm whether **Equation (8)** is a typo and should use \(W_j^*\) in the denominator. If yes, please correct it everywhere and state whether the implementation matches the corrected formula.

4. The theorem on **Pages 1-2** is about nearest-prototype classification under a Gaussian mixture model. Can you explain more carefully what part of modern SSL this is meant to formalize, and which part is only motivational intuition? Right now the bridge from the theorem to CaPT feels too loose.

5. In **Table 1**, why is adapter-tuned CLIP stronger than CaPT on STL10, and why is zero-shot CLIP also stronger there? A concise failure-mode analysis here would increase my confidence that the method is not simply overclaiming universality.

6. Can you provide a clearer disentanglement of gains from “having CLIP at all” versus gains from the proposed co-training/fusion design? For example, additional comparisons to simpler CLIP-guided teacher or distillation variants would help.

7. The main paper emphasizes portability. Can you move at least one non-CLIP instantiation into the main text, or otherwise soften the portability claim?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the submission. The work uses standard image benchmarks and studies semi-supervised classification. The main caution is scientific framing: some gains may reflect access to powerful pretrained external priors, so claims about “breaking label dependency” should be stated carefully to avoid overstating what is solved.

## Soundness Rating
2: fair. The empirical results are substantial, but there are important specification issues in the core equations and some of the claimed interpretation exceeds what is directly supported.

## Presentation Rating
2: fair. The paper is readable and the figures are helpful, especially Figures 1 and 4, but key equations and training details are not stated with sufficient precision.

## Contribution Rating
2: fair. The paper tackles an important low-label SSL problem and reports impressive numbers, but the scientific contribution is weakened by underspecified methodology, overstrong framing, and limited direct comparison to alternative VLM-based teacher approaches.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper is promising and the low-label empirical results are stronger than what I usually see in this area, but the current version has too many core ambiguities in the formulation and too much overclaiming relative to what is actually established. With a cleaner mathematical specification, sharper positioning, and more candid analysis of when the method helps or hurts, this could become a solid paper.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some implementation details because several parts of the method are underspecified in the paper.