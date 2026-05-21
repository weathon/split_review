---
job_id: 8d8a546e-d9ca-4b42-a0ac-361c64d5bbcd
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: TjAhTNzRub.pdf
paper: MORE: Mixture of Remapping Experts for Irreversible Feature-Level Unlearning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining representation learning, privacy/safety-oriented machine unlearning, and efficient feature-space editing, with experiments on vision models and diffusion models.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related/background, methodology, experiments, quantitative and qualitative results, and conclusion. While I have substantial concerns about correctness, novelty positioning, and presentation, these rise to the level of a weak review rather than a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes MoRE, a training-free feature-level unlearning method that first maps class prototypes into a prototype-orthogonal space via a pseudoinverse transform, then erases or remaps forget prototypes into remain prototypes, and finally extends this idea with multiple remapping experts and stochastic or conditional routing. The authors position the method as addressing three goals simultaneously, namely preserving utility on remain data, making feature-level forgetting harder to reverse, and improving efficiency relative to activation-storage/SVD-based methods such as ESC. Experiments are reported on class-wise and instance-wise unlearning for image classification, together with a small extension to concept erasure in diffusion models.

## Strengths
The paper tackles an important and timely problem. The focus on feature-level reversibility is well motivated in the introduction, and the attempt to go beyond output-level forgetting metrics is valuable for the unlearning community.

The core idea is intuitively understandable. In particular, the contrast in **Figure 1** is helpful: it clearly communicates the paper’s intended distinction between simple subspace erasure, single-prototype remapping, and multi-expert scattering. Even if the visualization is only illustrative, it does a good job of explaining the claimed mechanism of reducing cohesive residual forget clusters.

The paper also tries to unify three desirable properties that are often treated separately, utility preservation, reversibility resistance, and efficiency. The use of class-wise activation means rather than storing all forget activations is a practically appealing design choice, and the efficiency framing is one of the more compelling parts of the submission.

There are some strong empirical numbers in the main classification experiments. In **Table 1**, MoRE and the single-expert Remap variant often achieve near-zero forget accuracy while maintaining strong remain performance, especially on CIFAR-10 and under the KR-style evaluations. The gap over ESC is large in several rows, especially where ESC retains substantial forget performance. That empirical trend, if fully trustworthy, suggests the proposed remapping step is doing something meaningfully different from pure erasure.

The ablations are directionally useful. **Table 3** and **Figure 6** support the claim that prototype-orthogonalization matters. In particular, **Figure 6** is relevant because it directly visualizes the post-edit prototype similarities that the method is designed to manipulate, rather than only showing downstream accuracy. This is the right kind of diagnostic for a feature-editing paper.

The paper spans several settings rather than relying on a single benchmark. The inclusion of CIFAR-10, CIFAR-100, Tiny-ImageNet, and some ImageNet results gives a broader picture than many unlearning papers. The attempt to test the method on diffusion-style concept erasure, shown qualitatively in **Figure 4** and quantitatively in **Table 2**, also indicates some ambition beyond the narrowest benchmark setting.

## Weaknesses
I have a fairly long list of concerns, and several of them are not cosmetic. The main issue is that the paper’s strongest claims, especially “exact,” “irreversible,” and parts of the mathematical interpretation, are not supported at the level of rigor the paper implies.

1. **The paper repeatedly overclaims “exact” and “irreversible” unlearning without theoretical support.**  
   The abstract says “exact feature-level unlearning,” and multiple parts of the paper describe the method as establishing irreversibility. However, the evidence provided is empirical and limited to specific evaluations, mainly KR via linear probing and some light fine-tuning discussion. This is not enough to justify “exact” in the usual sense, nor “irreversible” in any strong sense. At most, the experiments suggest that the resulting features are harder to linearly recover under the chosen protocol.  
   This matters because the central contribution is framed around stronger guarantees than prior work. If those guarantees are actually heuristic or empirical, the contribution should be stated that way. Right now the title, abstract, and conclusion collectively oversell what is demonstrated.

2. **The mathematical claims around orthogonality and projection are imprecise, and in places misleading.**  
   In **Section 3.1** on Pages 4 to 5, the paper defines a matrix \( \mathbf{D} \) such that \( \mathbf{D}\mathbf{P} = \mathbf{I}_k \), with \( \mathbf{D} = \mathbf{P}^+ \) in **Equation (2)**. This ensures biorthogonality of the coordinate system with respect to the prototype columns, not that the ambient feature space is transformed into one where “prototype vectors are orthogonal by construction” in the stronger geometric sense suggested by the text. The statement is too loose.  
   More importantly, after **Equation (5)** the paper claims that subtracting \( \mathbf{P}_f \mathbf{D}\mathbf{z} \) ensures \( \hat{\mathbf{z}} \) lies entirely in the subspace orthogonal to the forget prototypes. That conclusion does not follow in general. Unless the forget prototypes are part of an orthonormal basis and the operator is the corresponding orthogonal projector, \( \mathbf{I} - \mathbf{P}_f\mathbf{D} \) is not generally the orthogonal projection onto the complement of the forget span. With \( \mathbf{D} = \mathbf{P}^+ \) computed from all prototypes, this is especially not obvious.  
   This is not a pedantic point. The entire method hinges on a geometric interpretation of what the linear operator is removing and what it is preserving.

3. **There is a concrete inconsistency between Equation (6) and the accompanying explanation, and Algorithm 1 adds more confusion.**  
   In **Equation (6)** on Page 6, the remapping transform is  
   \[
   \hat{\mathbf{z}}=\big(\mathbf{I}-\mathbf{P}_{f}\mathbf{D}+\mathbf{P}_{t}\operatorname{diag}(\mathbf{s})\mathbf{D}\big)\mathbf{z}.
   \]
   But the paragraph immediately after says, “The additional term \( \mathbf{P}\operatorname{diag}(\mathbf{1}-\mathbf{s})\mathbf{D} \) serves as a detector,” which is simply not the term in the equation. That is a substantive mismatch at the exact point where the remapping mechanism is supposed to become clear.  
   Then in **Algorithm 1**, line 23 defines
   \[
   \mathbf{E}^{(e)} \gets \mathbf{I} - \mathbf{P}_f \mathrm{diag}(\mathbf{s}) \mathbf{P}^+ + \mathbf{P}_t^{(e)} \mathrm{diag}(\mathbf{s}) \mathbf{P}^+.
   \]
   Since \( \mathbf{P}_f = \mathbf{P}\mathrm{diag}(\mathbf{s}) \) was already defined at line 16, the extra \( \mathrm{diag}(\mathbf{s}) \) multiplying \( \mathbf{P}^+ \) changes the operator relative to the main-text formulas. This is not a harmless notation slip. It leaves the actual implemented transform ambiguous.  
   For a method paper centered on a closed-form linear operator, this is a serious clarity and soundness issue.

4. **The assumptions for the pseudoinverse construction are underexplained and potentially fragile.**  
   On Page 5 the paper says “given that \( \mathbf{P} \) is full-rank,” but does not discuss what happens when prototypes are nearly collinear, poorly estimated, or rank-deficient. That is not a remote edge case, especially since the same section motivates the method by showing substantial prototype correlation in **Figure 3**.  
   If \( \mathbf{P} \in \mathbb{R}^{d \times k} \) has highly correlated columns, then \( \mathbf{P}^+ \) can become numerically unstable, and the transform can amplify noise. The text gestures at condition number concerns when comparing SVD to normal equations, but there is no discussion of regularized pseudoinverses, truncation, or robustness to poorly conditioned prototype sets. Given that the method is supposed to scale to larger settings and other modalities, this omission matters.

5. **The evaluation of “irreversibility” is too narrow for the strength of the claims.**  
   The paper leans heavily on KR, which is defined via linear probing in Appendix B.3, and on the intuition that scattering forget features across multiple experts makes them harder to recover. But linear probing is a very specific adversary. There is no systematic study of stronger recovery attacks in the main paper, such as multi-layer probes, nonlinear probes, targeted fine-tuning under controlled budgets, or attacker access to routing randomness.  
   **Figure 1** is conceptually useful, but as evidence for irreversibility it is weak. A t-SNE picture is not reliable support for separability claims, and certainly not for irreversibility. If the core claim is that MoRE leaves “little residual structure for linear probes to exploit,” then a much stronger recovery study is needed in the main paper.

6. **The paper’s literature positioning around feature-level unlearning is too narrow.**  
   The related work in Section 2 largely funnels the story through ESC, which makes the paper read as “ESC plus remapping.” But feature-level or representation-level unlearning has broader context than what is discussed here, including work explicitly centered on feature unlearning and recent work studying reversibility at the representation level. The current positioning makes the contribution look stronger than it is by not seriously situating it among adjacent approaches.  
   This matters because the claimed novelty is not just an engineering tweak, it is framed as a new pathway to irreversible feature-level unlearning. That framing demands a more complete comparison.

7. **Several experimental tables contain inconsistencies or presentation problems that materially reduce trust.**  
   The notation in **Table 1** is confusing to the point of being error-prone. For example, the column headers repeat \(D_r\) twice, clearly intending train/test variants, but this is never made cleanly consistent in the table itself. The text below the table also refers to \(D_{rt}\), while the table header does not. This makes interpretation unnecessarily difficult.  
   There are more serious issues later. On Page 10, the “Random Data Forgetting” paragraph says “As shown in Table 4, MoRE achieves comparable or superior performance,” but **Table 4** does not contain a MoRE row, only a Remap row. That is not a typo I can brush aside, because it directly affects a claimed result.  
   Likewise, **Table 7** contains method names such as “Xerose” and “MoUE,” which do not match the rest of the paper. These look like copy-editing artifacts from another draft or another method name. Again, this may sound small, but repeated inconsistencies of this sort make it difficult to trust the experimental section as carefully prepared.

8. **The reported efficiency claim is plausible but not fully substantiated in a way that isolates the right comparison.**  
   The efficiency section says MoRE uses \(O(Nd)\) time for prototype collection and \(O(dk)\) memory, which is reasonable for class-mean prototypes. However, the practical comparison in **Figure 5** is underexplained in the main paper. It is not clear whether all methods are measured under matched hardware, matched batch sizes, identical implementation quality, and the same forget/remain configuration. More importantly, the comparison bundles training-based baselines with a training-free method, which is fair in one sense, but the key competitor claimed in the paper is ESC, another training-free feature-level method. That pairwise efficiency comparison should have been cleaner and more detailed.  
   Also, the paper’s abstract contrasts MoRE with ESC on memory grounds, but the main text does not directly report ESC’s activation-storage bottleneck under the same scale in a careful apples-to-apples way.

9. **The stochastic routing design introduces nondeterminism at inference, and the implications are not discussed.**  
   In **Algorithm 2**, each input chooses a random expert at inference time. That means the same input can map to different features and possibly different predictions across runs. This is a nontrivial property, especially if the method is to be used in safety- or compliance-oriented unlearning settings. The paper frames this as beneficial for scattering, but does not discuss stability, calibration, reproducibility, or whether evaluation averages over multiple routing samples.  
   Since some metrics are standard accuracy metrics, it matters whether the reported numbers are from a single routing draw, expectation over draws, or deterministic seeds. The paper does not make this sufficiently clear.

10. **The diffusion-model extension is interesting but underdeveloped relative to the confidence of the claims.**  
    On Pages 8 to 9, the paper claims strong out-of-the-box transfer to Stable Diffusion, and **Table 2** reports the best \( \mathrm{LPIPS}_d \) values. However, this section is too compressed for the strength of the statement. The prototype definition for cross-attention, the exact editing location, the number of edited layers, and the precise baseline setup are not explained in enough detail in the main paper.  
    The qualitative evidence in **Figure 4** is also weakly scoped, because it shows a single prompt for one style-erasure example. The images do suggest that the proposed result preserves prompt adherence better than some baselines, but a single showcase cannot carry the broad claim that the method “outperforms SOTA diffusion model unlearning methods both quantitatively and qualitatively.” This should be toned down or supported much more carefully.

11. **Some comparisons in the results section raise interpretability questions that are not addressed.**  
    In **Table 1**, the single-expert Remap variant is often as good as or better than MoRE on standard KD metrics, while MoRE is motivated as the stronger irreversible variant. The authors later explain that the gap shows up more under KR and with more experts, but the main paper does not clearly separate “utility improvement from PO projection,” “forgetting from remapping,” and “irreversibility from multi-expert routing.” **Table 3** helps, but the narrative still blurs these effects.  
    In other words, the paper often attributes gains to the full framework when the tables suggest that a large portion may come from simpler components.

12. **Presentation quality is below the bar expected for a paper with strong methodological claims.**  
    There are numerous notation inconsistencies and copy-editing problems: \( \mathcal{D}_{fr} \) vs \( \mathcal{D}_{ft} \), repeated \(D_r\) headers, inconsistent use of KR/KD/KB/KH labels across tables, and method-name mismatches in **Table 7** and Appendix tables. These are not just surface-level polish problems. They repeatedly interrupt the reader’s ability to determine exactly what was evaluated and how.  
    A paper can survive some typos, but not this many when the core method is a sequence of linear operators where exact formulas matter.

## Questions
1. In **Equation (5)**, under what assumptions can you justify the statement that \( \hat{\mathbf{z}} = (\mathbf{I} - \mathbf{P}_f \mathbf{D})\mathbf{z} \) lies in the subspace orthogonal to the forget prototypes? If this is only an intuitive statement, please rewrite it more carefully and provide the exact geometric property the operator satisfies.

2. Please resolve the inconsistency between **Equation (6)** and the paragraph immediately after it. Is the remapping term \( \mathbf{P}_t \operatorname{diag}(\mathbf{s})\mathbf{D} \), \( \mathbf{P}\operatorname{diag}(\mathbf{1}-\mathbf{s})\mathbf{D} \), or something else? Also, please clarify the discrepancy with **Algorithm 1**, line 23, where an extra \( \operatorname{diag}(\mathbf{s}) \) appears after \( \mathbf{P}_f \).

3. The method is repeatedly described as “exact” and “irreversible.” What precise definition of exactness are you using here? What evidence in the main paper, beyond linear probing and limited fine-tuning intuition, should convince readers that the method is irreversible rather than just harder to recover under the chosen attack?

4. How are results computed under stochastic routing? For a fixed test input, do you sample one expert once, average predictions over multiple expert samples, or fix a random seed? Please report the variance induced by routing randomness and clarify whether the same protocol is used for all metrics.

5. Please explain the issue in **Table 4**. The text claims “MoRE” results for random data forgetting, but the table only includes “Remap.” Which is correct?

6. Please explain the naming inconsistencies in **Table 7** (“Xerose”, “MoUE”) and confirm whether these results are indeed for the proposed method variants.

7. The motivation for multi-expert scattering is irreversibility. Could you provide stronger rebuttal evidence, ideally in the main paper or response, using at least one stronger attacker than a linear probe, for example a nonlinear probe or constrained fine-tuning protocol with standardized budgets?

8. The pseudoinverse construction may be unstable when prototypes are highly correlated, which your own **Figure 3** suggests can happen. Did you observe numerical instability in practice? Have you tried a regularized pseudoinverse or truncated SVD, and if so, how sensitive is performance to that choice?

9. For the diffusion experiment, please clarify the exact editing target, number of layers edited, and prompt protocol in the main paper. Also, can you provide more than one qualitative prompt beyond **Figure 4** to support the claim of consistent prompt-faithful style removal?

10. The related-work framing is very ESC-centric. Please more clearly position the paper relative to broader feature-level and representation-level unlearning literature, especially work that studies reversibility in representations.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper concerns privacy/safety-oriented unlearning and uses public benchmark datasets. I do not see an ethics issue requiring separate review based on the main paper alone.

## Soundness Rating
2: fair. The empirical results are promising, but the strongest claims are overstated, key equations and algorithms are inconsistent, and the evidence for irreversibility is not strong enough for the paper’s framing.

## Presentation Rating
2: fair. The paper is readable at a high level and some figures are helpful, but notation inconsistencies, equation-text mismatches, and table errors substantially hurt clarity.

## Contribution Rating
2: fair. The remapping idea is interesting and potentially useful, especially as a practical alternative to pure erasure, but the paper currently overstates its guarantees and does not convincingly establish the full claimed contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has an interesting central idea and some strong-looking empirical results, but there are too many unresolved issues in the math, claim calibration, and experimental presentation for me to support acceptance in its current form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The main concerns arise from the paper’s own equations, tables, and claim phrasing rather than niche background assumptions.