---
job_id: 0653773d-e0cc-4462-aecd-1dcdb1e1f641
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: mytIKuRsSE.pdf
paper: Learning with Dual-level Noisy Correspondence for Multi-modal Entity Alignment
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies representation learning for multi-modal knowledge graphs, uncertainty-aware learning, and robust learning under noisy correspondences.

## Minimum Quality
Pass ✅. The submission contains the necessary scientific components, including abstract, introduction, method, related work in the appendix, experiments, quantitative results, and conclusion; despite several technical and presentation issues, it presents a complete and non-trivial research contribution with substantial empirical evidence.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious content targeting automated reviewers in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies multi-modal entity alignment under what the authors call Dual-level Noisy Correspondence (DNC), covering both intra-entity noise in entity-attribute associations and inter-graph noise in entity-entity and attribute-attribute correspondences. The proposed method, RULE, estimates correspondence reliability using uncertainty and consensus, uses these estimates for robust fusion and robust discrepancy elimination during training, and further adds a test-time correspondence reasoning module based on an MLLM to refine alignment decisions. Experiments on five MMEA benchmarks under inherent and synthetically injected noise show consistent improvements over several recent baselines.

## Strengths
The paper addresses a realistic problem setting that is easy to dismiss in benchmark papers but hard to ignore in practice. The distinction between intra-entity noise and inter-graph noise is useful, and the examples in **Figure 1(a)** make the failure modes concrete rather than merely hypothetical. I also appreciated that **Figure 1(b)** goes beyond a conceptual cartoon and directly frames the two claimed consequences of DNC, namely degraded fusion and degraded cross-graph alignment.

Empirically, the paper is strong. Across both evaluation protocols, the method consistently improves over competitive MMEA baselines under inherent noise and injected noise. The gains in **Table 1** are especially notable in the more difficult Non-name setting, where robustness actually matters, for example on ICEWS-WIKI and ICEWS-YAGO under 50% DNC. The margin over the strongest baselines is not a rounding-error win, it is often substantial. **Table 2** also shows that the method remains strong in the All-attributes setting, although that table is closer to saturation on some datasets.

The paper includes reasonably targeted ablations. **Table 3** does a decent job isolating the contribution of DRL, DRF, and TTR, and it is useful that the authors compare “Only Unc.” and “Only Cons.” rather than only reporting a full-model ablation. That strengthens the case that the uncertainty and consensus signals are complementary rather than decorative.

The overall architecture is clearly communicated. **Figure 2** is one of the stronger parts of the paper, it makes the flow from representation extraction to reliability estimation, pair division, robust training, and test-time reasoning easy to follow. Given that the method has several modules, this figure materially improves readability.

The qualitative analyses are also helpful. **Figure 3(b)** and **Figure 5** give some evidence that the reliability scores are not arbitrary, since clean pairs and noisy pairs are visibly separated, and noisy entity-attribute pairs receive lower reliability during fusion. This does not fully validate the estimator, but it is better than relying only on downstream accuracy.

## Weaknesses
1. **The central reliability formulation is intuitive, but mathematically under-justified and partly underspecified.**  
   The core quantity is the reliability score in **Equation 1**, \(w_i = (1-u_i)\gamma + c_i(1-\gamma)\). This linear combination is the backbone of the method, since it influences both pair division and fusion, yet the paper gives little principled justification for why this specific form is appropriate beyond empirical convenience. The choice \(\gamma = 0.5\) is fixed “for simplicity” on **Page 3**, but there is no argument in the main paper for why uncertainty and consensus should be linearly combined, why equal weighting is sensible across datasets, or whether other monotone combinations would behave similarly. This matters because most of the method’s claimed robustness hinges on the quality of \(w_i\). If \(w_i\) is ad hoc, then the paper is closer to a successful heuristic bundle than a well-motivated learning principle.

   There is also a scaling issue. In **Equation 5**, consensus is defined as \(c_i = \max(0, \mathbf{s}_i \cdot \mathbf{y}_i)\). Since \(\mathbf{y}_i\) is one-hot, this is just the positive part of the annotated-pair similarity. But the paper never clearly states whether similarities are normalized to lie in \([0,1]\) or \([-1,1]\) before entering **Equation 1**. By contrast, \(u_i\) from **Equation 3** is bounded in \([0,1]\). If \(c_i\) is not comparably scaled, then the reliability score can be dominated by consensus in a way that is not theoretically or numerically controlled. This is particularly consequential because \(w_i^m\) is directly used as a multiplicative weight in **Equation 14**.

2. **Several equations and notational choices in the main paper are unclear or inconsistent, and some are important enough to affect technical understanding.**  
   The first serious issue is around **Section 2.3** on **Page 6**. The text introduces an “overall objective” and refers to \(\mathcal{L}_{DR}\) and \(\mathcal{L}_{Reg}\), but the actual equation that should define the full loss, presumably **Equation 9**, is missing from the visible main-paper text. That is not a cosmetic omission, it makes the training objective incomplete at the point where the method is being specified.

   There are further inconsistencies. In **Section 2.1** on **Page 3**, the problem setup introduces two graphs with \(M\) and \(\tilde M\) attributes, but the attribute-attribute correspondence is later written as \((x_i^m, \tilde x_j^m, y_{ij}^m)\), which implicitly assumes a shared modality index \(m\) across graphs. That contradicts the earlier notation with possibly different modality counts. If the method assumes aligned modality types, that should be stated explicitly; if not, the notation is misleading.

   The subset notation is also sloppy. In **Section 2.2.3**, \(\mathcal{S}_U,\mathcal{S}_I,\mathcal{S}_C\) are defined as sets of pairs, but in **Equation 11** the indicator is written as \(\mathbb{I}(i \notin \mathcal{S}_U)\), which treats them as index sets. This is fixable, but it makes the formalism feel under-checked.

   The test-time reasoning notation is similarly inconsistent on **Page 6**. The text first defines refined entity-entity scores \(\hat{\mathbf{s}}_i\) in **Equation 15**, then **Equation 16** introduces \(\tilde{\mathbf{s}}_i^m\), while the final sentence uses \(s_i^{joint} = s_i + \tilde s_i\). It is not fully clear how \(\hat{\mathbf{s}}_i^m\), \(\tilde{\mathbf{s}}_i^m\), and \(s_i^{joint}\) relate. For a multi-module method, notation hygiene is not optional.

3. **The theoretical claims are modest in substance, and the main theorem does not pull much weight.**  
   The paper gives special prominence to **Theorem 1** on **Page 4**, which claims that low uncertainty does not necessarily imply the annotated correspondence receives the highest belief. That statement is true, but it is also fairly unsurprising. More importantly, the theorem is not used to derive a stronger guarantee or a concrete property of the proposed estimator; it mainly motivates adding the consensus term. As a result, the theoretical layer feels closer to post hoc justification than to genuine analysis of the learning problem.

   I was also unconvinced by the theorem’s presentation. **Equation 4** is written as  
   \[
   z_i \text{ with low } u_i \neq \arg\max \mathbf{b}_i = \arg\max \mathbf{y}_i,
   \]
   which is not a well-formed mathematical statement. The theorem should compare implications between events or assignments, not juxtapose an embedding \(z_i\), an uncertainty condition, and two argmax expressions in this way. Since this theorem is used to motivate a central design choice, the lack of precision matters.

4. **The greedy correspondence estimation used for consensus at inference time rests on a strong assumption that is insufficiently validated.**  
   In **Definition 3**, **Assumption 1**, and **Equation 7** on **Page 5**, the paper assumes that correctly associated attributes should have non-negative marginal contribution and irrelevant ones should have negative contribution. That is a strong structural assumption. In realistic multi-modal KGs, an attribute can be correct yet unhelpful, redundant, ambiguous, or even temporarily harmful due to encoder noise; conversely, a noisy attribute may accidentally increase retrieval similarity for the wrong reason. So the sign of \(\Delta\) is not a reliable oracle for correctness.

   This matters because the estimated subset \(\pi^*\) is then used to infer a pseudo-correct correspondence when annotation is unavailable. If the assumption fails, the consensus mechanism can become self-reinforcing: attributes that agree with current similarity scores are kept, and dissenting but informative attributes are discarded. The paper provides empirical evidence that this works on the chosen benchmarks, but the conceptual leap from marginal contribution to correctness is too large for such a central module.

5. **The pair division thresholds may be brittle under noisy supervision, and the procedure is somewhat circular.**  
   In **Equation 8** on **Page 5**, the thresholds \(\beta_u\) and \(\beta_c\) are estimated using a set of “true positive pairs”  
   \[
   \mathcal{S}^{TP} = \{ i \mid \arg\max(\mathbf{s}_i) = \arg\max(\mathbf{y}_i)\}.
   \]
   But \(\mathbf{y}_i\) is precisely the annotated correspondence, which may itself be noisy under the DNC setting that the paper targets. So the threshold selection relies on agreement with labels that are not guaranteed to be correct. This makes the procedure partially circular: noisy annotations are used to identify trusted pairs, which are then used to calibrate the filter for noisy annotations.

   Why this matters is visible in the high-noise regime. The whole point of the method is to remain reliable when correspondences are corrupted. A thresholding scheme that depends on the subset of label-agreeing pairs may be fragile exactly where robustness is needed most. The paper should either justify why this proxy remains stable under label noise, or provide sensitivity analysis in the main paper.

6. **The empirical section is strong overall, but some comparisons are not as convincing as they first appear.**  
   The most compelling results are in **Table 1**, especially in the Non-name setting. However, **Table 2** is so close to saturation on several datasets that it becomes harder to judge whether the proposed mechanism is broadly improving entity alignment or whether the task is already largely solved by strong name-centric features. For example, under 50% DNC the method still obtains \(97.7\) H@1 on ICEWS-WIKI and \(99.7\) on DBP15K FR-EN. Those numbers are impressive, but they also suggest that the benchmark under the All-attributes protocol may not strongly stress the dual-noise problem once names are present. A more diagnostic analysis would separate which modalities are actually carrying the robustness improvements.

   Along the same line, the injected noise model on **Page 8** is only a partial proxy for the claimed real-world DNC. Entity-entity replacement is plausible, but perturbing visual attributes with Gaussian noise and textual attributes with random character replacement mostly creates low-level corruption, not semantic mis-association. That is easier to detect than a realistic but wrong attribute attached to the wrong entity. Since the paper’s motivation is semantic mismatch and annotation error, the synthetic noise generation is somewhat mismatched to the problem statement.

7. **The MLLM-based test-time reasoning module raises fairness and scalability questions that are not fully addressed in the main paper.**  
   The method uses Qwen2.5-VL-72B-Instruct in **Section 3.1** on **Page 7** as the default TTR component. This is a substantial extra model at inference time. The ablation in **Table 3** shows TTR does improve results, but it also means part of the reported performance comes from adding a very large external reasoner that baselines are not equipped with. I do not object to using stronger components, but then the paper should be especially careful to disentangle gains from the core noise-robust training design versus gains from test-time MLLM assistance.

   This matters both scientifically and practically. Scientifically, it blurs the contribution: is the improvement due to better robustness modeling, or due to a powerful auxiliary model rescuing ambiguous cases? Practically, the paper does not report main-paper inference cost, latency, or candidate-set size dependence for TTR, even though those are central for entity alignment at scale.

8. **The literature positioning is not fully convincing, especially on robustness-focused and recent MMEA work.**  
   The paper cites several mainstream MMEA baselines, but the positioning around recent robustness-oriented MMEA is thinner than it should be. In particular, I did not see discussion of several closely related recent directions on robust or calibrated MMEA, including work on pseudo-label calibration, robustness to noisy or missing visual modalities, information bottleneck style filtering, or LLM-guided semantic denoising for MMEA. This matters because the paper’s framing could otherwise overstate how unexplored robustness in MMEA really is. The dual-level formulation may still be useful, but the manuscript should do a better job of separating what is genuinely new in the problem setup from what is a task-specific instantiation of already active robustness themes.

## Questions
1. **Please clarify the exact full training objective in the main paper.**  
   On **Page 6**, the text refers to the overall objective and to \(\mathcal{L}_{DR}\) and \(\mathcal{L}_{Reg}\), but the defining equation appears to be missing. In the rebuttal, please write the full objective explicitly and explain how it is optimized in practice.

2. **How is the similarity in Equation 5 scaled before combining it with uncertainty in Equation 1?**  
   I would like a precise answer here. Are embeddings \(z_i,\tilde z_j\) normalized? Is \(s_{ij}\in[-1,1]\)? If not, how do you prevent \(c_i\) from dominating \(1-u_i\) in the reliability score? A concise derivation or implementation detail would increase my confidence.

3. **Can you provide a stronger justification, or at least targeted empirical validation, for Assumption 1 and the greedy subset selection in Equation 7?**  
   For example, what fraction of attributes with negative marginal contribution are actually noisy on a manually checked subset? This would materially strengthen the central logic of the consensus estimator.

4. **How sensitive is the pair division in Equation 8 to label noise in \(\mathcal{S}^{TP}\)?**  
   Since the “true positive” set is defined using potentially noisy annotations, I would like to see either a theoretical argument or a direct robustness analysis showing that the thresholds remain stable as annotation noise rises.

5. **How much of the final gain is attributable to the core RULE training objective versus the TTR module?**  
   **Table 3** helps, but I would like the authors to state this more directly. In particular, would the paper’s main claims still hold if one evaluated only the training-time method and treated TTR as an optional enhancement?

6. **Can you discuss the realism of the synthetic A-A corruption process?**  
   The current injected noise on **Page 8** seems closer to perceptual or string corruption than to semantic misalignment. If possible, a comparison against semantically mismatched attribute reassignment would strengthen the robustness claim.

7. **Please sharpen the relation to recent robust-MMEA papers.**  
   A more explicit paragraph explaining how your setting differs from robustness to missing modality, pseudo-label noise, or LLM-guided denoising would improve the paper’s positioning considerably.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
3: good. The main empirical claims are largely supported by extensive experiments and ablations, but several parts of the mathematical formulation and reliability estimation are under-justified or not fully specified in the main paper.

## Presentation Rating
3: good. The paper is generally readable and the figures are helpful, especially **Figure 2**, but there are notable notation inconsistencies, at least one missing equation in the main text, and some theoretical statements that are imprecisely written.

## Contribution Rating
4: excellent. The paper makes a meaningful contribution by formulating a practically relevant dual-level noise setting for MMEA and showing substantial empirical gains with a reasonably comprehensive evaluation.

## Overall Rating
8: Accept, good paper (poster). The empirical case is strong and the problem setting is important, and while I have real concerns about the precision of the formulation, the justification of the reliability estimator, and the role of the MLLM-based test-time module, the paper still makes a valuable contribution that I expect the community would benefit from seeing.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the method and experiments carefully, though some missing details and notation issues in the main paper prevent absolute certainty.