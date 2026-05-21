---
job_id: 5ebaa16b-4361-404a-85b8-39d2bd52e9cd
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 55GsILa8c9.pdf
paper: CausalNovo: Advancing De Novo Peptide Sequencing Via a Causality-Informed Framework
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it proposes a representation-learning framework with causal motivation for a biology application, namely de novo peptide sequencing from mass spectra.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion/discussion. While I have substantial concerns about formulation, validation, and positioning, these are review-stage weaknesses rather than desk-reject-level omissions or fatal integrity problems.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the paper text.

# Expected Review Outcome:
## Summary
This paper proposes CausalNovo, a model-agnostic framework for de novo peptide sequencing that augments an existing sequencing model with a causality extraction module operating in latent space. The method separates latent representations into estimated causal and non-causal parts using a learned mask, applies a replacement-based intervention on peaks identified as non-causal via a theoretical-spectrum matching heuristic, and trains with an invariance-style contrastive objective plus supervised decoding losses. Experiments on three public proteomics benchmarks and three backbone models report improved amino-acid, peptide-level, and PTM-level metrics, as well as improved robustness under synthetic perturbations and varying noise-signal ratios.

## Strengths
The paper addresses a meaningful practical problem. Robustness to spurious or unstable peaks is a genuine issue in de novo peptide sequencing, and the motivation is not artificial. The preliminary vulnerability analysis in **Figure 1** is useful in establishing that strong recent baselines degrade when the authors replace peaks categorized as noise, which at least gives empirical motivation for trying to reduce reliance on those peaks.

The framework is reasonably general in spirit. It is integrated into three different backbones, and the main empirical pattern in **Table 1** and **Table 2** is consistent: adding CausalNovo improves the authors’ retrained versions of CasaNovo, AdaNovo, and $\pi$-HelixNovo across multiple datasets and metrics. In particular, the gains on the harder Seven-species and HC-PT settings are nontrivial in absolute terms, which suggests the method is doing something beyond a tiny regularization effect.

The paper also includes several forms of analysis beyond the main benchmark table. **Table 4** and **Table 5** provide ablations on the independence/purification/symmetric components and the intervention design; **Table 3** provides leave-one-out cross-species evaluation; **Figure 3** and **Figure 4** examine robustness under perturbation and across varying NSR. I appreciate that the authors did not stop at one headline SOTA table.

The architecture figure is helpful. **Figure 2B** gives a reasonably intuitive overview of where the CEM sits relative to the encoder and decoder, and the split into $\mathbf z_c$ and $\mathbf z_s$ makes the intended mechanism easier to follow than the text alone.

The paper is generally readable at a high level. Even though I have issues with technical precision, the central idea, learn a mask over spectral latent tokens, intervene on likely non-causal peaks, and train for invariance plus prediction, is understandable.

## Weaknesses
1. **The causal framing is much stronger than what the method actually justifies.**  
   The paper repeatedly claims to learn “causal representations” and formalizes the setup with an SCM in **Section 3.2** and **Figure 2A**, but the actual method relies on a supervised heuristic derived from the ground-truth peptide sequence and theoretical ion matching. In practice, the paper does not identify latent causal variables $C$ from observational data; it defines a proxy notion of “causal peaks” using domain heuristics and then regularizes a model toward invariance under synthetic perturbations of the remaining peaks. That is a robustness-oriented representation learning method, not convincing causal discovery. This matters because the paper’s central conceptual contribution is its causal claim. If the causal interpretation is overstated, the novelty and scientific message become much less clear.

2. **The core SCM assumptions in Equation (2) are asserted, not defended, and appear too simplistic for the application.**  
   In **Eq. (2)** the paper assumes
   \[
   X = f(C,S), \quad C \perp S, \quad Y = g(C).
   \]
   The independence assumption $C \perp S$ is doing a huge amount of work, but it is not justified for tandem MS data. In real proteomics pipelines, interfering peaks, co-elution patterns, precursor selection, sample prep effects, and instrument settings can all depend on peptide properties, meaning the “non-causal” component may be statistically and mechanistically related to the peptide. Likewise, $Y=g(C)$ suggests the label is fully determined by causal fragment information alone, but the actual decoder also conditions on precursor information $\mathbf t$, and mass constraints are central to sequencing. The SCM is therefore not merely simplified, it is misaligned with the actual modeling pipeline. Because the subsequent objectives are derived from this SCM, the validity of the causal interpretation is weakened at the foundation.

3. **The intervention design uses label information in a way that limits the claimed applicability and muddies the learning signal.**  
   In **Section 3.4.1**, non-causal ions are localized using the ground-truth peptide to generate a theoretical spectrum, and then perturbations are applied to those peaks. This means the intervention is only available during supervised training with trusted labels. That is not inherently invalid, but it substantially narrows the claim that the framework learns a general causal representation of spectra. More importantly, after the replacement perturbation, the method explicitly unions the modified spectrum with the theoretical spectrum, i.e.
   \[
   \mathbf x_{\text{intervene}} = \mathbf x_{\text{replace}} \cup \mathbf x_{\text{theory}}.
   \]
   This is a very strong teacher signal. It effectively injects idealized fragment peaks into the training input. At that point, improvements may come from training on partially denoised or label-enhanced spectra, rather than from disentangling causal from spurious features in the learned representation. The paper does not disentangle these explanations well enough.

4. **The mathematical objective is underspecified and somewhat inconsistent.**  
   Several parts of **Sections 3.3 and 3.4.2** need much tighter definition.
   - The paper first proposes maximizing \(I(\mathbf z_c;\mathbf z_c' \mid C)\), then says \(Y\) can serve as a proxy for \(C\), and finally optimizes a contrastive expression in **Eq. (5)**. But the conditional mutual information notation is not faithfully reflected in the actual loss. The implemented objective appears closer to an InfoNCE-style positive-pair loss across spectra, not a clear estimator of \(I(\mathbf z_c;\mathbf z_c' \mid Y)\).
   - **Eq. (5)** is not written cleanly. The notation for negative samples is malformed, the function is referred to as “sin” in the equation while the text says cosine similarity, and the aggregation by mean pooling is only described in prose after the equation rather than being defined mathematically. Since $\mathbf z_c \in \mathbb R^{n \times d}$, similarity between sequence-level objects requires an explicit aggregation operator, e.g. \(\bar{\mathbf z}_c = \frac{1}{n}\sum_i (\mathbf z_c)_i\), before cosine similarity is well-defined. As written, the equation is sloppy.
   - In **Eq. (6)**, the paper claims maximizing mutual information is equivalent to minimizing cross-entropy, and then writes
     \[
     I(\mathbf z_c;Y) \propto -\mathcal L_{\mathrm{CE}}(\mathbf z_c,\mathbf t,\mathbf y), \quad
     I(\mathbf z_s;Y) \propto -\mathcal L_{\mathrm{CE}}(\mathbf z_s,\mathbf t,\mathbf y).
     \]
     This is not an equivalence in the general form stated. Cross-entropy upper bounds conditional entropy under a chosen decoder family; it is not a direct plug-in estimator of mutual information without additional assumptions. The paper is too casual here.
   These issues matter because the method is sold as principled and information-theoretic, but the actual training objective is only loosely connected to those claims.

5. **The “purification” objective is conceptually questionable and internally confusing.**  
   In **Section 3.3**, the authors argue that maximizing \(I(\mathbf z_s;Y)\) helps purify \(\mathbf z_c\). Intuitively, this is odd. If $\mathbf z_s$ is supposed to capture non-causal factors, why should encouraging it to be predictive of the label purify the causal branch rather than simply leak more label information into the non-causal branch? The paper says this can “indirectly” purify $\mathbf z_c$, but no convincing argument is given. The ablation in **Table 4** shows some empirical gain from this term, so there may be a useful multi-view or auxiliary supervision effect, but the causal interpretation is shaky. At minimum, the paper should explain whether the loss on $\mathbf z_s$ shares the same decoder parameters, how gradients interact through the mask $\mathbf M$, and why this does not simply encourage both branches to become predictive.

6. **The empirical comparisons are not entirely clean because the paper mixes benchmark-reported numbers with retrained baselines, and the retraining discrepancies are large.**  
   In **Table 1** and **Table 2**, many published baseline numbers differ substantially from the authors’ retrained results, sometimes by a lot. For example, retrained CasaNovo on Nine-species improves amino-acid precision from 0.697 to 0.741 relative to the cited number, while retrained AdaNovo on Nine-species is actually slightly worse than the cited value. Once such discrepancies appear, the fairest comparison is the controlled one against the authors’ own retrained baselines, not the mix with external benchmark numbers. The paper does provide the retrained comparisons, which is good, but the headline language still leans on outperforming recent methods. Given the sensitivity of these benchmarks to preprocessing and implementation choices, this should be handled more carefully.

7. **The robustness evaluation is largely based on synthetic perturbations whose realism is not fully established.**  
   The main evidence for reduced spurious reliance comes from **Figure 1**, **Figure 3**, and **Figure 4**, where peaks designated as non-causal are replaced or noise ratios are varied. This is directionally interesting, but the perturbation mechanism is defined by the same heuristic used in training, namely matching to a theoretical spectrum under threshold $\gamma$. That raises the possibility that the evaluation is partially aligned with the training bias. If the method is trained to be robust to this exact intervention family, then showing robustness to the same family is not as strong as showing robustness to genuinely shifted acquisition conditions, other instruments, or independently curated interference scenarios. The paper acknowledges in the conclusion that evaluation under more realistic protocols remains future work, and I think that limitation is important rather than minor.

8. **The improvement claims would be stronger with statistical variability or repeated runs, but none are reported in the main paper.**  
   Across **Tables 1 to 5**, the paper reports single-point estimates only. For a training procedure that adds several stochastic components, random replacement, contrastive negatives, mask learning, and extra forward passes, variance can matter. This is especially relevant for the smaller gains in some settings, such as the symmetric strategy in **Table 4** or the difference between intervention variants in **Table 5**. Without confidence intervals, standard deviations, or multiple seeds, it is difficult to judge which improvements are robust and which may be run-to-run noise.

9. **The baseline choice and positioning relative to recent work are incomplete.**  
   The paper compares mainly against DeepNovo, PointNovo, InstaNovo, SearchNovo, and three backbones into which CausalNovo is integrated. This is a reasonable set, but the literature positioning still feels selective. For a paper whose main argument is improved robustness and principled modeling under noise, I expected a stronger discussion of how this differs from recent methods that already incorporate bias mitigation, contrastive objectives, or richer decoding constraints. The related work section is short and does not really sharpen what is methodologically distinct here beyond attaching causal terminology to invariance training.

10. **Some figure and table interpretations are oversold relative to what they actually establish.**  
   - **Figure 2A** presents an SCM with clean separation between $C$ and $S$, but this diagram functions more as an aspirational cartoon than a supported model of the data-generating process. The paper treats it almost as a derivational basis, which is too much.
   - **Figure 4** shows consistent gains across NSR bins on HC-PT, which is a useful robustness result, but it is still within a benchmark-specific synthetic categorization of noise. The text extrapolates this to “stronger reliance on causal signal peaks,” which is stronger language than the evidence warrants.
   - **Table 6** is also awkwardly presented: the “RI” values do not seem to be simple relative improvements in the usual sense, and the naming “Prp.Prec” is unclear. Because this table underpins the claim that the method is robust to alternative peak-distinguishing strategies, the metric definition should be much cleaner.

11. **There are presentation and notation issues that materially affect technical confidence.**  
   The paper is readable overall, but there are many small problems that add up: inconsistent notation between scalar/sequence-level variables, a typo-ridden **Eq. (5)**, use of “sin” where “sim” is intended, awkward statements such as “replace-based perturbation strategy improves the CasaNovo baseline by +0.6% in amino acid-level precision and +1.0% in recall” without uncertainty, and some reference formatting issues. These are not just cosmetic. In a paper whose main contribution is a supposedly principled causal and information-theoretic framework, imprecision in the equations and loss definition weakens trust.

12. **The practical cost is substantial relative to the conceptual gain.**  
   The paper notes in **Section 5** and **Appendix Table 15** that training time increases by about 2.3x because of multiple forward passes. Since the method is model-agnostic and intended as a general wrapper, training efficiency matters. I would have liked either a stronger argument for why the gains justify this cost, or a more careful analysis of whether all components are necessary on all datasets and backbones.

## Questions
1. The most important clarification for me is the role of the “enhance” step in **Section 3.4.1**. Can the authors quantify how much of the final gain remains if the intervention excludes the union with \(\mathbf x_{\text{theory}}\), and the model is trained only with replacement on identified non-causal peaks? **Table 5** partly addresses this, but the main concern is not just performance, it is whether the causal claim survives once idealized theory peaks are no longer injected.

2. Please write the actual optimization objective in one complete formula, including all terms, weights, the symmetric variant, the precise aggregation used before the similarity in **Eq. (5)**, and whether the same decoder \(\rho\) is used for both \(\mathbf z_c\) and \(\mathbf z_s\). Right now the method is distributed across prose and partial equations, which makes it hard to verify.

3. Can the authors justify more carefully why maximizing \(I(\mathbf z_s;Y)\) should “purify” \(\mathbf z_c\)? A gradient-level explanation, or an ablation that compares maximizing, minimizing, and removing the \(\mathbf z_s\)-prediction term, would materially increase my confidence.

4. How sensitive are the main results in **Table 1** and **Table 2** to random seed? Please report mean and standard deviation over multiple runs for at least one backbone on each dataset. This is especially important because some gains are modest and the method adds stochastic perturbations.

5. The paper uses \(Y\) as a proxy for \(C\) in the conditional MI term. Under what assumptions is this valid in this application? Please be precise. Is the intended claim that \(Y\) is a deterministic child of \(C\), that \(Y\) is sufficient for grouping positives in supervised contrastive learning, or something stronger?

6. Can the authors provide a more rigorous discussion of why the SCM assumption \(C \perp S\) is reasonable for tandem MS data? If not, I would encourage toning down the causal language and repositioning the method as robustness-oriented invariance learning informed by domain heuristics.

7. For the robustness results in **Figure 3** and **Figure 4**, can the authors include evaluation under a perturbation family that is different from the one used in training, or at least a held-out perturbation protocol? That would help distinguish true robustness from adaptation to a specific synthetic intervention.

8. The retrained baseline discrepancies in **Table 1** are large. Please explain the exact preprocessing, training details, and any deviations from the original implementations. A transparent explanation would help readers interpret whether gains are due to the proposed method versus the retraining pipeline.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper. The work uses public datasets in proteomics and does not involve human subjects in the study itself. My concerns are scientific rather than ethical.

## Soundness Rating
2: fair. The empirical evidence is substantial enough to suggest the method may be useful, but the causal interpretation, mathematical formulation, and robustness claims are not supported as cleanly as the paper suggests.

## Presentation Rating
2: fair. The paper is understandable at a high level, and the figures/tables are useful, but the technical exposition around the objectives and notation is imprecise in several places.

## Contribution Rating
2: fair. There is a practically relevant idea here, and the empirical improvements are interesting, but the conceptual novelty is weakened by overclaimed causality and by the fact that much of the method looks like a heuristic robustness regularizer built on label-derived interventions.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper tackles an important problem and shows encouraging empirical gains, but the central causal story is overstated, the theoretical/objective formulation is not tight enough, and the validation is too tied to synthetic perturbations aligned with the training heuristic. With a more modest framing and sharper methodology, this could become a stronger submission.

## Reviewer Confidence
4: confident. I am confident in the assessment, though not absolutely certain. The application area is specialized, but I carefully checked the main methodological claims, equations, tables, and figures.