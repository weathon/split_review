---
job_id: 63dcc5b7-cde8-4ed0-a94f-2d4c5c3352c8
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: zt7IPzsXrT.pdf
paper: Forget Many, Forget Right: Scalable and Precise Concept Unlearning in Diffusion Models
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically generative models, safety, machine unlearning, and optimization for diffusion models.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, method, experiments, quantitative/qualitative results, and conclusion; while I have substantial concerns about justification and evaluation, these are review-level issues rather than grounds for desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious text targeting automated review systems in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies large-scale concept unlearning in text-to-image diffusion models and proposes ScaPre, a closed-form, training-free framework that edits cross-attention weights to forget many target concepts while preserving general generation quality. The method combines a conflict-aware stabilization design, consisting of a spectral trace regularizer and a geometry alignment term, with an “Informax Decoupler” that reweights channels based on estimated mutual information with target concepts. Experiments on object, style, and explicit-content unlearning report stronger scalability, better precision on confusable concepts, and favorable efficiency relative to several prior unlearning baselines.

## Strengths
The paper targets a practically important problem. Large-scale concept unlearning in diffusion models is a real pain point, and the manuscript is right to focus on the failure mode that many existing methods either collapse generation quality or cause broad collateral damage once the number of forgotten concepts grows.

A genuine strength is the attempt to combine scalability and precision in one framework, rather than optimizing only one axis. The overall design in **Figure 2** is helpful here: it clearly separates the role of the conflict-aware stabilization block from the role of the Informax Decoupler and then the closed-form solution stage. Even if I have concerns about some of the mathematical grounding, the architectural decomposition itself is easy to follow and gives a coherent picture of what each component is intended to do.

The empirical coverage is broad for the main paper. The authors evaluate on standard multi-concept object forgetting (**Imagenette**, **ImageNet-Diversi50**), precise forgetting with confusable categories (**ImageNet-Confuse5**), and artistic style unlearning. This is better than papers that only show one benchmark and then extrapolate big claims.

The main quantitative results are strong on their own terms. In **Table 1** on Imagenette, ScaPre achieves by far the lowest average residual accuracy, \(0.8\), while retaining a CLIP score of \(30.43\), which is much higher than UCE/RECE and only modestly below the original model. Similarly, **Table 3** on ImageNet-Diversi50 shows a compelling trade-off: ScaPre gets Avg Acc \(3.9\) with CLIP \(29.41\), whereas UCE/RECE reach \(0.0\) residual accuracy but at catastrophic CLIP drops to \(22.23/21.78\). That table does support the paper’s central empirical claim that extreme forgetting alone is not enough if it destroys model utility.

The precision results are also one of the better parts of the paper. In **Table 4**, ScaPre is not the absolute best in raw target suppression, since UCE/RECE have slightly lower Unlearn Acc, but those methods destroy preservation, with Preserve Acc around \(5\%\). ScaPre’s much higher Preserve Acc (\(76.3\)) and Overall Acc (\(84.3\)) make a strong case that the method is more selective. This is exactly the kind of trade-off the paper claims to improve, and this table supports that narrative better than the headline “lowest forgetting accuracy” tables alone.

The scaling trend in **Figure 4** is useful and directly relevant. The left plot suggests ScaPre’s forgetting remains strong as the number of concepts grows, and the right plot shows its UQ remains comparatively stable while several baselines degrade noticeably. This figure is one of the more persuasive pieces of evidence in the paper because it tests the central scalability claim directly rather than through a single fixed concept count.

The qualitative results are also informative. In **Figure 5**, UCE and RECE appear to remove target concepts aggressively but replace them with visually nonsensical or unrelated content, whereas ScaPre often preserves plausible non-target image structure while suppressing the target concept. Likewise, **Figure 6** and the appendix figures on confusable categories are aligned with the quantitative precision claim that some baselines over-forget nearby concepts. These figures are useful because unlearning papers can hide behind classifier-based metrics; here, the visuals at least partially corroborate the metric story.

Efficiency is another practical advantage. **Figure 3** and **Table 11** indicate that ScaPre is much cheaper than training-based baselines and comparable to other closed-form editors. The paper’s claim is not “fastest overall” but rather “best efficiency-quality trade-off,” and the presented numbers are at least consistent with that framing.

## Weaknesses
1. **The core objective in Equation (8) is not adequately justified, and some terms are mathematically under-motivated relative to the claims made about them.**  
   The paper presents
   \[
   \min_W \ \mathrm{tr}(WAW^\top) + \beta \mathcal{L}_g(W) + \mathrm{tr}(W^\top BW) - \mathrm{tr}(W V^\star C_E^\top),
   \]
   with \(A=\lambda I + S + R\) and \(B=\mathrm{diag}(\alpha)\), but the link from the preliminary closed-form editing formulation in **Equation (2)** to this new objective is only loosely explained. In particular, **Equation (2)** has explicit preservation terms over non-target concepts \(P\), whereas **Equation (8)** removes that structure and replaces it with \(S\), \(R\), geometry alignment, and channel weights. That might be reasonable as a redesign, but the manuscript does not rigorously derive why these replacements are faithful surrogates for preserving non-target concepts. The paper often speaks as if this is principled optimization, yet it reads more like a heuristic objective assembled from several intuitions. That matters because the headline claims, stability, precision, and preservation, all depend on these substitutions actually encoding the right inductive bias.

2. **The “Spectral Trace Regularizer” is presented with stronger intuition than evidence.**  
   In **Equations (3)-(4)**, \(S=\sum_{k,t} c_{k,t} c_{k,t}^\top\) is described as capturing directions “most prone to conflicts and noise,” and \(R\) is described as suppressing overlapping concept directions via gated singular values. But \(S\) is just a second-moment matrix of target concept contextual features. High-energy directions are not automatically “conflict directions”; they may simply be common semantic directions that are important for representing the concepts at all. Penalizing \(W S W^\top\) could therefore suppress useful target representation as well as shared semantic structure needed for clean substitution. The paper never shows, theoretically or empirically in the main text, that large eigenvalues of \(S\) correlate with destructive inter-concept interference rather than concept salience. The same issue applies to \(R\): the gating
   \[
   \hat{\sigma}_i = (1-\mathrm{sigmoid}(\sigma_i))\sigma_i
   \]
   is an arbitrary shrinkage rule. Why this particular nonlinearity, and why should overlap measured by singular values of stacked text embeddings correspond to conflict in cross-attention weight updates? The manuscript states this rather confidently, but the justification is thin.

3. **The geometry alignment term is elegant-looking but scientifically underspecified in the main paper.**  
   **Equation (5)** introduces a Bures distance between \(WW^\top\) and \(W_0W_0^\top\), and the text claims this preserves “higher-order feature correlations” and the “pretrained global structure.” That is a strong claim. However, in the main paper there is no proof, bound, or even a precise argument connecting Bures proximity of row-space covariances to preservation of non-target image semantics. Many very different weight matrices can share similar covariance structure while behaving differently under text conditioning. The covariance-level alignment may stabilize norms or row correlations, but the paper overstates what this guarantees about generation quality and semantic preservation. The proximal refinement on **Page 6** is also only sketched conceptually in the main text, then deferred to the appendix. Since this refinement is one of the two central components of the method, the main paper should be more explicit about what objective is actually optimized after the refinement and whether the final \(\widetilde{W}\) remains near-optimal for the forgetting objective.

4. **The Informax Decoupler is one of the least convincing parts mathematically, despite being central to the paper’s precision claim.**  
   In **Section 4.2**, channel importance is estimated by thresholding activations,
   \[
   z = \mathds{1}\{a_i(s)>\tau_i\},
   \]
   computing an empirical mutual information with a binary label \(y\), and then defining
   \[
   \alpha_i = \frac{\mathrm{MI}_i}{\max_j \mathrm{MI}_j}.
   \]
   There are several issues here. First, the paper never specifies in the main text how the “neutral inputs” for \(y=0\) are chosen. This is not a cosmetic omission. The MI scores will depend heavily on what constitutes the negative class. If the negative set is generic COCO prompts, the channel relevance estimate may differ drastically from a negative set composed of visually similar non-target concepts. Second, the adaptive thresholds \(\tau_i\) are introduced but not defined. Third, binarizing activations before MI estimation is a rather lossy and brittle statistic, and the paper gives no sensitivity analysis on thresholding. Fourth, the objective in **Equation (8)** uses \(B=\mathrm{diag}(\alpha)\) as an additive quadratic penalty, but the text says the decoupler “selectively isolates concept-relevant parameters and restricts updates strictly within the corresponding subspace.” That wording is stronger than what the formulation actually guarantees. A diagonal quadratic term merely reweights updates; it does not strictly confine them to a subspace unless some \(\alpha_i\) are exactly infinite or other channels are exactly frozen, neither of which is the case.

5. **There is a likely inconsistency between the narrative description of the decoupler and the actual sign/effect of the \(B\) term in Equation (8).**  
   The paper says channels more informative of target concepts should receive adapted updates, but in **Equation (8)** the term \(\mathrm{tr}(W^\top B W)\) is a regularizer. If larger \(\alpha_i\) means a channel is more target-relevant, then a larger diagonal entry in \(B\) penalizes the norm of the corresponding row/column contribution more strongly, which may actually discourage movement there unless compensated by the linear term. Maybe this is intended, maybe not, but the main text never spells out the exact effect. Because **Equation (9)** becomes
   \[
   BW + WA = V^\star C_E^\top,
   \]
   larger \(B\) entries make the effective denominator larger in the spectral solution, thereby shrinking the corresponding components of \(W\). That sounds more like suppressing highly informative channels than “focusing updates on them.” If the intended mechanism is “strongly edit target-relevant channels toward zero replacement,” the paper needs to explain this much more carefully. As written, the interpretation is muddy.

6. **The empirical evaluation is strong in breadth but weaker in methodological transparency than it should be for such strong claims.**  
   Many critical experimental choices are left vague in the main paper: how prompts are constructed for evaluation, how many images per prompt/class are generated, what seeds are used, which classifier checkpoints are used for accuracy measurement, whether hyperparameters are tuned per method/dataset, and whether all baselines are re-run under exactly the same prompt templates and inference settings. For unlearning papers, these details are not small. Residual “accuracy” can move a lot depending on prompt phrasing and sample counts. The paper states on **Page 7** that all results are from official implementations, but this does not eliminate the need to specify common evaluation protocol in the main paper.

7. **The paper relies heavily on classifier-based unlearning accuracy, which is an imperfect proxy and can reward distribution shift or generative collapse.**  
   This issue shows up visibly in the results. In **Table 3**, UCE and RECE obtain perfect \(0.0\) Avg Acc on ImageNet-Diversi50, but their CLIP scores crash to about \(22\), indicating the classifier can no longer recognize target concepts largely because the model is generating garbage or unrelated content. The authors do acknowledge this, and that is good, but the evaluation still centers the discussion around classifier residual accuracy and the custom UQ score. What is missing is a more direct measure of whether the target concept is absent while image realism and prompt faithfulness are preserved. Human evaluation is not mandatory, but some stronger semantic audit beyond classifier accuracy plus CLIP would improve confidence substantially.

8. **The proposed UQ metric is convenient for presentation, but it is dataset-relative and somewhat arbitrary.**  
   On **Page 7**, the normalized scores \(\hat A\) and \(\hat C\) are computed using the mean and standard deviation across methods, then combined harmonically. This makes \(UQ\) partly dependent on the set of compared methods rather than being an intrinsic property of a model. If one baseline is added or removed, the normalization changes. That is not wrong per se, but the paper treats UQ almost like a universal summary metric. It is better understood as a ranking aid internal to the experiment. The appendix tries alternative normalizations, which is helpful, but in the main paper the framing is more confident than warranted.

9. **Some of the strongest novelty claims are overstated relative to the actual relation to prior closed-form editing methods.**  
   The paper says on **Page 9** that ScaPre is “the first closed-form framework specifically designed for large-scale concept unlearning in diffusion models.” I am not convinced this wording is careful enough. The paper itself cites UCE and RECE as closed-form multi-concept editing methods. The real distinction seems to be that ScaPre adds extra regularization and reweighting aimed at the large-scale regime, not that it invents closed-form multi-concept unlearning from scratch. This may sound semantic, but novelty positioning matters here because the work reads more like a substantial extension of the closed-form editing line than a fully new paradigm.

10. **The comparisons are broad, but the positioning against recent precision-oriented unlearning work is still incomplete.**  
   The related work on **Pages 2-3** covers many standard baselines, but the paper’s precision story would be stronger if it engaged more directly with other methods aimed at reducing collateral damage or improving robustness of concept erasure. As written, the related-work section is somewhat grouped by method family rather than by the core scientific question this paper emphasizes, namely precise removal under entanglement. This weakens the paper’s novelty positioning.

11. **The qualitative figures are useful, but they also reveal a potential prompt-selection bias that the paper should address.**  
   **Figure 5** and **Figure 6** show examples where ScaPre looks better than baselines, and often it does. But the figure layout appears to choose prompts that make failure modes visually crisp. That is understandable for a paper figure, yet qualitative evidence is especially easy to cherry-pick in generative modeling. I would have liked either a randomized protocol for selecting prompts, or at least a statement that these are representative and not hand-picked. This matters because for methods like UCE/RECE the visual failures are dramatic, and the figures understandably push the reader toward the conclusion that those methods are uniformly unusable. The tables suggest they are poor on quality, yes, but a less curated visual protocol would make the comparison more convincing.

12. **Presentation has several avoidable errors and inconsistencies that reduce confidence.**  
   There are many typos and naming inconsistencies in the tables, for example “CLIPcaca” in **Table 3** and **Section 5.4**, “CLIPconco” / “CLIPours” in **Table 4** / **Table 7**, “Uunlearn” in **Table 7**, and some awkward prose around the method description. These do not invalidate the work, but they are numerous enough that they start to matter, especially in a paper that asks readers to trust a fairly intricate closed-form derivation.

## Questions
1. In **Section 4.2**, how exactly are the positive and negative samples used to estimate \(\mathrm{MI}_i\) constructed in the main experiments? Please specify the prompt pools for \(y=1\) and \(y=0\), the sample size \(K\), and how the thresholds \(\tau_i\) are chosen. This is central to the Informax Decoupler, and a precise answer could substantially increase confidence.

2. Can the authors clarify the intended effect of the \(B=\mathrm{diag}(\alpha)\) term in **Equation (8)**? Since larger \(\alpha_i\) increases regularization in the Sylvester equation, it seems to shrink updates along channels with high MI. How should this be reconciled with the claim that the decoupler focuses unlearning on target-relevant parameters?

3. What is the exact relationship between the proposed objective in **Equation (8)** and the standard preservation formulation in **Equation (2)**? Is there a derivation showing that \(S\), \(R\), and \(\mathcal L_g\) approximate a preservation objective over non-target concepts, or are these best viewed as heuristic surrogates? A more explicit explanation would help.

4. For the geometry alignment step after solving **Equation (9)**, what objective does the final refined \(\widetilde{W}\) optimize, even approximately? In particular, do the authors have any guarantee or empirical evidence that the proximal Bures refinement does not substantially undo the forgetting induced by the closed-form solution?

5. Please provide more main-paper detail on evaluation protocol: number of prompts per concept, prompt templates, number of generated images, random seeds, and whether the same evaluation prompts were used for all methods. This is important for interpreting **Tables 1, 3, and 4**.

6. In **Table 2**, ScaPre has the best \(\mathrm{CLIP}_s\) but not the best FID, with MACE slightly better on FID. Can the authors comment on whether ScaPre tends to trade a bit of image realism for more aggressive style removal, and whether that trade-off is consistent across individual artists rather than just averages?

7. For the qualitative comparisons in **Figures 5 and 6**, were the prompts fixed in advance and reused across methods, and are these examples representative or selected post hoc? Even a short statement about the protocol would make the figures more convincing.

8. Since **Table 3** shows UCE and RECE reaching \(0.0\) residual accuracy on 50 concepts but suffering severe quality collapse, could the authors report a complementary semantic preservation metric beyond CLIP, or a human preference study on a subset? This would help confirm that ScaPre’s advantage is not an artifact of the chosen summary metric.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications  
- Yes, Responsible research practice (e.g., human subjects, data release)  

## Details Of Ethics Concerns
The paper works on concept unlearning for harmful, copyrighted, and explicit content, which is socially relevant, but the methodology is still dual-use. A stronger unlearning method can also be seen as a stronger model editing method, and the appendix explicitly discusses robustness against attacks designed to recover erased concepts. I do not see an immediate reason for rejection on ethics grounds, but I do think the paper understates these issues.

I also disagree with the blanket statement on **Page 10** that the work “does not raise ethical concerns.” The paper includes experiments on explicit content removal using the I2P dataset and NudeNet detection in **Tables 8-9**, and it studies safety bypass attacks in **Table 10**. That absolutely touches deployment and misuse questions. At minimum, the ethics statement should discuss failure modes, false sense of safety, and risks of releasing stronger editing tools without caveats.

## Soundness Rating
3: good. The empirical evidence is fairly strong and broad, but some core methodological claims, especially around the spectral regularizer, geometry alignment, and Informax decoupling, are not justified as rigorously as the paper suggests.

## Presentation Rating
3: good. The paper is readable overall, and the high-level method and experiments are understandable, but the manuscript has multiple notation gaps, under-explained objective terms, and several table/text inconsistencies that should be cleaned up.

## Contribution Rating
3: good. The paper makes a useful contribution by pushing closed-form concept unlearning toward a larger-scale and more precision-aware regime, though the underlying ideas feel more like a strong extension of existing editing approaches than a fully distinct conceptual leap.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper tackles an important problem and presents strong empirical results with a practical training-free method, but the scientific grounding of several core components is thinner than the presentation implies. I lean positive because the breadth of experiments and the observed trade-offs are genuinely useful, though the paper is not clean enough mathematically or experimentally to make this an easy accept.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the diffusion-model unlearning literature, though some implementation-specific details are not fully recoverable from the main paper alone.